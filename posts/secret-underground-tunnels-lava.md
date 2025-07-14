---
title: "מסע אל בטן האדמה: סוד היווצרות מנהרות הלבה"
english_slug: secret-underground-tunnels-lava
category: "מדעי הסביבה / כדור הארץ"
tags:
  - לבה
  - הרי געש
  - מערות לבה
  - גיאולוגיה
  - תופעות טבע
  - סימולציה
---
# מסע אל בטן האדמה: סוד היווצרות מנהרות הלבה

דמיינו נהר לוהט של אש זורמת – לבה! ראיתם פעם סרטונים של זרמים אדומים בוהקים המתפתלים במורד הר געש? מראה עוצר נשימה, אך מה קורה כשהזרם הזה כאילו 'נבלע' באדמה? שם, עמוק בפנים, מתרחש קסם גיאולוגי אמיתי: היווצרותן של מנהרות וחללים תת-קרקעיים נסתרים.

איך נוצרות המנהרות המסתוריות הללו? בואו נחקור יחד בסימולציה אינטראקטיבית! נשחק עם תנאי הזרימה ונראה במו עינינו את התהליך שיוצר את מערות הלבה המדהימות בעולם.

<div class="app-container">
    <div class="controls-panel">
        <h3>שחקו עם תנאי הזרימה:</h3>
        <div class="control-group">
            <label for="temp" title="כמה חמה הלבה? חמה יותר = זורמת יותר בקלות ומתקררת לאט יותר.">טמפרטורת לבה:</label>
            <input type="range" id="temp" min="1" max="10" value="7"><span id="temp-value">7</span> יח'
        </div>

        <div class="control-group">
            <label for="speed" title="קצב פריצת הלבה מהמקור. מהיר יותר = זרם ארוך יותר פוטנציאלית.">עוצמת זרימה התחלתית:</label>
            <input type="range" id="speed" min="1" max="10" value="6"><span id="speed-value">6</span> יח'
        </div>

        <div class="control-group">
            <label for="slope" title="מידת התלילות של המדרון. תלול יותר = זרימה מהירה יותר.">שיפוע קרקע:</label>
            <input type="range" id="slope" min="5" max="30" value="15"><span id="slope-value">15</span>&deg;
        </div>

        <div class="button-group">
            <button id="start-flow" class="btn-action">התחל זרימה</button>
            <button id="stop-flow" class="btn-secondary" disabled>עצור אספקה מהמקור</button>
            <button id="reset" class="btn-tertiary">אתחל</button>
        </div>
         <div class="message-area" id="message-area">לחצו "התחל זרימה" כדי לראות את הקסם מתרחש!</div>
    </div>

    <div class="simulation-area" id="simulation-area">
        <div class="lava-source" id="lava-source" title="המקור ממנו פורצת הלבה"></div>
        <div class="lava-flow" id="lava-flow"></div>
        <div class="crust" id="crust"></div>
        <div class="hollow-space" id="hollow-space"></div>

        <div class="cross-section-container">
            <h4>חתך רוחב</h4>
            <div class="cross-section">
                 <div class="cs-ground"></div>
                <div class="cs-crust"></div>
                <div class="cs-liquid"></div>
                <div class="cs-hollow"></div>
            </div>
            <p class="cross-section-label">הזרם מבפנים</p>
        </div>
         <div class="ground-texture"></div> <!-- Background texture -->
    </div>
</div>

<style>
/* General Styles */
.app-container {
    display: flex;
    flex-direction: column;
    gap: 30px;
    font-family: 'Arial', sans-serif;
    max-width: 900px;
    margin: 20px auto;
    direction: rtl;
    text-align: right;
    background-color: #f0f0f0;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

h3, h4 {
    color: #333;
    margin-top: 0;
    border-bottom: 1px solid #eee;
    padding-bottom: 8px;
    margin-bottom: 15px;
}

/* Controls Panel */
.controls-panel {
    border: 1px solid #ddd;
    padding: 20px;
    border-radius: 8px;
    background-color: #fff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
}

.control-group {
    display: flex;
    align-items: center;
    margin-bottom: 15px;
    flex-wrap: wrap;
}

.control-group label {
    display: inline-block;
    margin-bottom: 5px;
    width: 180px;
    font-weight: bold;
    color: #555;
    cursor: help; /* Indicates tooltip */
}

.control-group input[type="range"] {
    flex-grow: 1;
    margin-right: 10px;
    -webkit-appearance: none;
    appearance: none;
    height: 8px;
    background: linear-gradient(to right, #ff9900, #cc0000);
    outline: none;
    border-radius: 5px;
    transition: opacity .2s;
}
.control-group input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    background: #fff;
    border: 2px solid #cc0000;
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 2px 4px rgba(0,0,0,0.15);
}
.control-group input[type="range"]::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #fff;
    border: 2px solid #cc0000;
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 2px 4px rgba(0,0,0,0.15);
}


.control-group span {
    display: inline-block;
    width: 30px;
    text-align: center;
    font-weight: bold;
    color: #333;
}

.button-group {
    margin-top: 20px;
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}

.controls-panel button {
    padding: 12px 20px;
    cursor: pointer;
    border: none;
    border-radius: 6px;
    font-size: 1em;
    transition: background-color 0.3s ease, opacity 0.3s ease;
    min-width: 120px; /* Ensure consistent button size */
    text-align: center;
}

.btn-action {
    background-color: #e74c3c; /* Red */
    color: white;
}
.btn-action:hover:not(:disabled) {
    background-color: #c0392b;
}

.btn-secondary {
    background-color: #f39c12; /* Orange */
    color: white;
}
.btn-secondary:hover:not(:disabled) {
    background-color: #e67e22;
}

.btn-tertiary {
     background-color: #bdc3c7; /* Grey */
    color: #333;
}
.btn-tertiary:hover:not(:disabled) {
    background-color: #95a5a6;
}


.controls-panel button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
    opacity: 0.7;
}

.message-area {
    margin-top: 15px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #fff9c4; /* Light yellow */
    color: #333;
    min-height: 20px;
    text-align: center;
    font-style: italic;
    font-size: 0.9em;
}


/* Simulation Area */
.simulation-area {
    position: relative;
    width: 100%;
    height: 400px; /* Increased height for longer flow */
    border: 1px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    background-color: #c2b280; /* Earth tone */
    box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.1);
}

.ground-texture {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGcgZmlsbD0iIzBhMGEwYSIgZmlsbC1vcGFjaXR5PSIwLjMiPjxwYXRoIGQ9Ik0wIDEwTDlhMSA5IDAgMCAwIDAtMTBsLTEgMWE4IDggMCAwIDEtOCAwWm0xMCAwYTkgOSAwIDAgMCAwIDEwbDEtMWE4IDggMCAwIDAgMC04Wm05LTlhOSA5IDAgMSAxIDAtMWExIDEgMCAxIDEgMCAxWm0wIDJhOSA5IDAgMSAxIDAgMWExIDEgMCAxIDEgMCAxWm0wIDJhOSA5IDAgMSAxIDAgMWExIDEgMCAxIDEgMCAxWm0wIDJhOSA5IDAgMSAxIDAgMWExIDEgMCAxIDEgMCAxWm0wIDJhOSA5IDAgMSAxIDAgMWExIDEgMCAxIDEgMCAxWm0wIDJhOSA5IDAgMSAxIDAgMWExIDEgMCAxIDEgMCAxWm0wIDJhOSA5IDAgMSAxIDAgMWExIDEgMCAxIDEgMCAxWm0wIDJhOSA5IDAgMSAxIDAgMWExIDEgMCAxIDEgMCAxWm0wIDJhOSA5IDAgMSAxIDAgMWExIDEgMCAxIDEgMCAxWiIgZmlsbD0iI2EwYTBhMCIgZmlsbC1vcGFjaXR5PSIwLjEiLz48L2c+PC9zdmc+'); /* Subtle dots */
    opacity: 0.4;
    pointer-events: none; /* Don't interfere with clicks */
}


.lava-source {
    position: absolute;
    top: 10px;
    left: 50%;
    transform: translateX(-50%);
    width: 50px;
    height: 25px;
    background: radial-gradient(circle, #ff9900, #e74c3c); /* Glowing effect */
    border-radius: 8px;
    box-shadow: 0 0 15px rgba(231, 76, 60, 0.8); /* Glow */
    z-index: 5;
    text-align: center;
    color: white;
    font-size: 11px;
    line-height: 25px;
    font-weight: bold;
     opacity: 0; /* Hidden initially */
     transition: opacity 0.5s ease-in-out;
}

.lava-flow {
    position: absolute;
    top: 35px; /* Start below source */
    left: 50%;
    transform: translateX(-50%);
    width: 25px; /* Initial width */
    height: 0; /* Starts empty */
    background: linear-gradient(to bottom, #ff9900, #e74c3c); /* Hot to less hot */
    border-bottom-left-radius: 12px;
    border-bottom-right-radius: 12px;
    z-index: 3;
    opacity: 1;
    transition: height linear, top linear, left linear, background 0.5s ease; /* Smooth animation */
}

.crust {
    position: absolute;
    top: 35px; /* Aligned with lava */
    left: 50%;
    transform: translateX(-50%);
    width: 25px; /* Matches lava width */
    height: 0; /* Starts empty */
    background-color: #5a4d41; /* Dark grey/brown */
    border-bottom-left-radius: 12px;
    border-bottom-right-radius: 12px;
    z-index: 4; /* Above lava to show crust */
    opacity: 0; /* Initially hidden, shows as it forms */
     transition: height linear, top linear, left linear, width linear, opacity ease-in-out, background-color 0.5s ease;
}

.hollow-space {
    position: absolute;
    top: 35px; /* Aligned with lava */
    left: 50%;
    transform: translateX(-50%);
    width: 18px; /* Slightly smaller than crust/lava */
    height: 0; /* Starts empty */
    background-color: rgba(0,0,0,0.3); /* Dark shade for empty space */
    border: 2px dashed #8b4513; /* Outline of the empty tube */
    box-sizing: border-box;
    border-radius: 10px;
    z-index: 2; /* Below crust, above background */
    opacity: 0; /* Hidden initially */
    transition: height linear, top linear, left linear, width linear, opacity ease-in-out;
}


/* Cross-Section Visualization */
.cross-section-container {
    position: absolute;
    top: 20px;
    right: 20px;
    width: 150px;
    border: 1px solid #ddd;
    padding: 15px 10px 10px 10px;
    background-color: #fff;
    border-radius: 8px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    z-index: 10;
}

.cross-section-container h4 {
    margin-top: 0;
    font-size: 1em;
    margin-bottom: 5px;
    border: none;
    padding: 0;
}
.cross-section-label {
    font-size: 0.8em;
    color: #555;
    margin-top: 5px;
}

.cross-section {
    position: relative;
    width: 100px;
    height: 100px;
    margin: 0 auto;
    border-radius: 50%;
    background-color: transparent; /* Ground handled by cs-ground */
    overflow: hidden; /* Keep contents inside circle */
    box-shadow: inset 0 0 8px rgba(0,0,0,0.2); /* Inner shadow for depth */
}

.cs-ground {
     position: absolute;
     top: 0; left: 0; right: 0; bottom: 0;
     background-color: #c2b280; /* Matches simulation area ground */
     border-radius: 50%;
     z-index: 0;
}

.cs-crust, .cs-liquid, .cs-hollow {
    position: absolute;
    border-radius: 50%;
    box-sizing: border-box;
    transition: all 0.5s ease-out; /* Smooth transitions for CS elements */
}

.cs-liquid {
    background: radial-gradient(circle, #ffcc00, #e74c3c); /* Glowing liquid */
    width: 80%;
    height: 80%;
    top: 10%;
    left: 10%;
    z-index: 2;
}

.cs-crust {
    border: 5px solid #5a4d41; /* Initial border thickness */
    background: transparent;
    z-index: 3;
}

.cs-hollow {
    background-color: rgba(0,0,0,0.4); /* Dark fill for empty space */
    border: 2px dashed #8b4513;
    width: 70%;
    height: 70%;
    top: 15%;
    left: 15%;
    z-index: 1; /* Behind liquid and crust */
    opacity: 0; /* Hidden initially */
}


/* Explanation Section */
#explanation {
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #fff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    display: none; /* Hidden by default */
    line-height: 1.6;
    color: #333;
}

#explanation h2 {
    margin-top: 0;
    color: #e74c3c; /* Red header */
    border-bottom: 2px solid #eee;
    padding-bottom: 10px;
}

#explanation p {
    margin-bottom: 15px;
}

#explanation ul {
    list-style-type: disc;
    margin-right: 25px;
    padding: 0;
}

#explanation li {
    margin-bottom: 15px;
    padding-right: 5px;
}

#explanation li strong {
    color: #5a4d41; /* Crust color */
}


/* Toggle Button */
#toggle-explanation {
    display: block;
    width: auto;
    margin: 30px auto 10px auto;
    padding: 12px 25px;
    cursor: pointer;
    border: none;
    border-radius: 6px;
    background-color: #3498db; /* Blue */
    color: white;
    font-size: 1em;
    transition: background-color 0.3s ease;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
#toggle-explanation:hover {
     background-color: #2980b9;
}

</style>

<button id="toggle-explanation">סקרנים? לחצו לחשיפת סודות מנהרות הלבה!</button>

<div id="explanation">
    <h2>מסע אל בטן האדמה: כיצד נוצרות מערות לבה?</h2>
    <p>מערות לבה אינן סתם חללים באדמה, אלא תוצאה של תהליך טבעי מדהים המתרחש במהלך התפרצויות געשיות של לבה בזלתית. דמיינו נהר לוהט שמקפיא את שוליו תוך כדי זרימה! הנה השלבים המרתקים:</p>
    <ul>
        <li>
            <strong>לבה בזלתית - הנוזל המושלם:</strong> לא כל לבה יוצרת מנהרות. לבה בזלתית, העשירה בברזל ומגנזיום, היא לרוב דלילה מאוד (צמיגות נמוכה) וחמה במיוחד (מעל 1000°C). תכונות אלו מאפשרות לה לזרום במהירות ולמרחקים גדולים יחסית, לפני שהיא מתמצקת לחלוטין. זוהי המועמדת האידיאלית ליצירת מנהרות ארוכות.
        </li>
        <li>
            <strong>התנאים בשטח:</strong> זרם הלבה מתחיל את מסעו במורד מדרון געשי. מהירות הזרימה הראשונית ועוצמת הזרם מהמקור, יחד עם שיפוע הקרקע, קובעים כמה רחוק ובאיזו מהירות הלבה תוכל להתקדם. התנאים שסימלתם משפיעים ישירות על ההתפתחות הראשונית של הזרם.
        </li>
        <li>
            <strong>שלב הקרום החיצוני:</strong> ברגע שהלבה הלוהטת באה במגע עם האוויר (שהוא כמובן קר בהרבה!), השכבה העליונה והחיצונית שלה מתחילה להתקרר ולהתמצק במהירות יחסית. תהליך זה יוצר קרום דק, מעין "צינור" חיצוני קשיח, בעוד שהלבה בפנים עדיין לוהטת ונוזלית לגמרי. ככל שהלבה פחות חמה, או האוויר קר יותר (קצב קירור גבוה בסימולציה), כך הקרום נוצר מהר יותר ונעשה עבה יותר.
        </li>
        <li>
            <strong>הזרימה הפנימית ב"צינור":</strong> הקרום שהתמצק אינו סתם מעטפת; הוא משמש כשכבת בידוד מדהימה! הוא מונע מהחום של הלבה הפנימית לברוח מהר מדי ומגן עליה מפני הקירור החיצוני. בתוך ה"צינור" המבודד הזה, הלבה הנוזלית יכולה להמשיך לזרום בחופשיות יחסית, ממש כמו מים בתוך צינור אינסטלציה תת-קרקעי.
        </li>
        <li>
            <strong>שלב הריקון והיווצרות החלל:</strong> זהו השלב המכריע ביצירת המערה! כאשר אספקת הלבה מהמקור בהר הגעש נפסקת או פוחתת משמעותית (כפי שראיתם כש"עצרתם את האספקה"), הלבה שעדיין נמצאת בתוך ה"צינור" המוצק ממשיכה לזרום במורד המדרון בזכות כוח הכבידה. היא מתנקזת מטה, ומותירה מאחוריה את הצינור הקפוא - אך כעת ריק מחומר נוזלי. החלל הריק הזה בתוך הקרום הממוצק הוא מערת הלבה!
        </li>
         <li>
            <strong>מערות לבה בעולם:</strong> מערות לבה הן תופעה מרהיבה שניתן למצוא במקומות געשיים פעילים או כאלה שהיו פעילים בעבר. המערות הארוכות והמפורסמות ביותר נמצאות בהוואי (איפה שהלבה הבזלתית שופעת), איסלנד, ספרד (האיים הקנריים), ואפילו באוסטרליה. הן משמשות חלון ייחודי לתהליכים הגיאולוגיים המעצבים את כדור הארץ.
        </li>
    </ul>
     <p>כעת, כשהבנתם את התהליך, נסו שוב את הסימולציה עם פרמטרים שונים וראו כיצד הם משפיעים על קצב היווצרות הקרום, מהירות הזרימה, והגודל הפוטנציאלי של המנהרה שתיווצר!</p>
</div>


<script>
document.addEventListener('DOMContentLoaded', () => {
    const simulationArea = document.getElementById('simulation-area');
    const lavaSource = document.getElementById('lava-source');
    const lavaFlow = document.getElementById('lava-flow');
    const crust = document.getElementById('crust');
    const hollowSpace = document.getElementById('hollow-space');
    const crossSectionLiquid = document.querySelector('.cs-liquid');
    const crossSectionCrust = document.querySelector('.cs-crust');
    const crossSectionHollow = document.querySelector('.cs-hollow');
    const tempInput = document.getElementById('temp');
    const speedInput = document.getElementById('speed');
    const slopeInput = document.getElementById('slope');
    const tempValueSpan = document.getElementById('temp-value');
    const speedValueSpan = document.getElementById('speed-value');
    const slopeValueSpan = document.getElementById('slope-value');
    const startButton = document.getElementById('start-flow');
    const stopButton = document.getElementById('stop-flow');
    const resetButton = document.getElementById('reset');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const messageArea = document.getElementById('message-area');


    let isFlowing = false; // Is flow coming from source?
    let animationFrameId = null;
    let startTime = null;
    let currentLength = 0; // Current length of the crust/tube
    let flowSpeedPerSecond = 0;
    let coolingRateFactor = 0; // Higher means faster cooling/crust formation
    const maxFlowLength = 350; // Max height of the simulation area minus padding

    // Update span values when sliders change
    tempInput.addEventListener('input', () => {
        tempValueSpan.textContent = tempInput.value;
        updateLavaColor(parseInt(tempInput.value));
    });
    speedInput.addEventListener('input', () => speedValueSpan.textContent = speedInput.value);
    slopeInput.addEventListener('input', () => slopeValueSpan.textContent = slopeInput.value);


    function updateParameters() {
        const temp = parseInt(tempInput.value); // 1-10
        const speed = parseInt(speedInput.value); // 1-10
        const slope = parseInt(slopeInput.value); // 5-30

        // Model:
        // Flow speed: Influenced by initial speed and slope. Higher values = faster.
        // Base speed around 30-60 px/sec
        flowSpeedPerSecond = (speed / 10) * 30 + (slope / 30) * 30; // Scales between ~3 to 60 px/sec based on inputs

        // Cooling rate: Influenced by temperature. Higher temp = slower cooling (lower rate).
        // Rate determines how fast the crust forms (opacity/thickness increases)
        // Scales from ~0.1 (very slow) to ~1 (fast)
        coolingRateFactor = 1.5 - (temp / 10) * 1.2; // Higher temp -> lower coolingRateFactor
        coolingRateFactor = Math.max(0.1, coolingRateFactor); // Ensure minimum cooling
        console.log(`Flow Speed: ${flowSpeedPerSecond.toFixed(2)} px/s, Cooling Rate Factor: ${coolingRateFactor.toFixed(2)}`);
    }

     function updateLavaColor(temp) {
        // Simple gradient based on temperature
        const r = 231; // Base red (e7)
        const g = 76 + (temp - 1) * (153 - 76) / 9; // Green increases with temp towards #ff9900 orange
        const b = 60 + (temp - 1) * (0 - 60) / 9;   // Blue decreases with temp towards #ff9900 orange
        const startColor = `rgb(${Math.round(r)}, ${Math.round(g)}, ${Math.round(b)})`;

        const endR = 231; // Base red (e7)
        const endG = 76; // Base green (4c)
        const endB = 60; // Base blue (3c)
         const endColor = `rgb(${Math.round(endR)}, ${Math.round(endG)}, ${Math.round(endB)})`;


        lavaFlow.style.background = `linear-gradient(to bottom, ${startColor}, ${endColor})`;
         lavaSource.style.background = `radial-gradient(circle, ${startColor}, #e74c3c)`; // Keep some constant red base
         lavaSource.style.boxShadow = `0 0 15px ${startColor}`; // Glow color matches start color
    }


    function startFlow() {
        if (isFlowing) return;
        isFlowing = true; // Flow is coming from source
        startButton.disabled = true;
        stopButton.disabled = false;
        resetButton.disabled = true; // Disable reset while active simulation is running
        messageArea.textContent = 'זרם לבה לוהטת מתחיל לזרום!';


        updateParameters();
        updateLavaColor(parseInt(tempInput.value)); // Set initial lava color

        startTime = performance.now();
        currentLength = 0;

        // Reset initial visual states
        lavaSource.style.opacity = 1;
        lavaFlow.style.height = '0px';
        crust.style.height = '0px';
        hollowSpace.style.height = '0px';
        crust.style.opacity = 0;
        hollowSpace.style.opacity = 0;
        hollowSpace.style.zIndex = 2; // Ensure hollow is below crust while crust forms

         // Reset cross-section
        crossSectionLiquid.style.transition = 'none'; // Remove transitions for instant reset
        crossSectionCrust.style.transition = 'none';
        crossSectionHollow.style.transition = 'none';

        crossSectionLiquid.style.width = '80%';
        crossSectionLiquid.style.height = '80%';
        crossSectionLiquid.style.top = '10%';
        crossSectionLiquid.style.left = '10%';
        crossSectionLiquid.style.backgroundColor = 'red'; // Initial color, updated by updateLavaColor visually
        crossSectionHollow.style.opacity = 0;
        crossSectionCrust.style.borderWidth = '5px'; // Initial crust border
         crossSectionLiquid.style.opacity = 1; // Ensure liquid is visible


         // Re-add transitions after reset
         requestAnimationFrame(() => {
              // Main elements: height should be linear, opacity can ease
             lavaFlow.style.transition = `height linear ${maxFlowLength / flowSpeedPerSecond}s, top linear, left linear, width linear, background 0.5s ease`;
             crust.style.transition = `height linear ${maxFlowLength / flowSpeedPerSecond}s, top linear, left linear, width linear, opacity 1s ease-in-out, background-color 0.5s ease`; // Crust opacity forms
              hollowSpace.style.transition = 'none'; // Hollow transition starts on stop

              // Cross-section elements
              crossSectionLiquid.style.transition = 'all 0.5s ease-out';
              crossSectionCrust.style.transition = 'border-width 0.5s ease-out';
              crossSectionHollow.style.transition = 'all 0.5s ease-out, opacity 0.5s ease-in-out';
         });


        animateFlow();
    }

    function animateFlow(currentTime) {
        if (!isFlowing && stopButton.disabled) { // Stop animating if both flow and drain stopped
             return;
        }

        if (!startTime) startTime = currentTime; // Initialize startTime on first frame

        const elapsed = (currentTime - startTime) / 1000; // seconds

        if (isFlowing) { // If flow is still coming from the source
            let newLength = elapsed * flowSpeedPerSecond;
            currentLength = Math.min(newLength, maxFlowLength);

            lavaFlow.style.height = currentLength + 'px';
            crust.style.height = currentLength + 'px';

             // Simulate crust formation opacity increase
             // Opacity reaches max (0.8) based on time and cooling rate
             const crustOpacity = Math.min(elapsed * coolingRateFactor * 0.2, 0.8); // Slower opacity increase
             crust.style.opacity = crustOpacity;

             // Update cross-section crust thickness
             const csCrustThickness = Math.min(5 + elapsed * coolingRateFactor * 5, 45); // Max border thickness 45px
             crossSectionCrust.style.borderWidth = csCrustThickness + 'px';

             // Liquid core shrinks as crust grows (simplified visual)
             const liquidSizeFactor = Math.max(0.1, 1 - (csCrustThickness / 45) * 0.9); // Shrinks to 10% min
             crossSectionLiquid.style.width = (80 * liquidSizeFactor) + '%';
             crossSectionLiquid.style.height = (80 * liquidSizeFactor) + '%';
             const liquidOffset = (1 - liquidSizeFactor) * 40; // Center the shrinking liquid
             crossSectionLiquid.style.top = (10 + liquidOffset) + '%';
             crossSectionLiquid.style.left = (10 + liquidOffset) + '%';

             // Check if flow reached max length
             if (currentLength >= maxFlowLength) {
                 messageArea.textContent = 'הזרם הגיע לתחתית המסך! לחצו "עצור אספקה" ליצירת המנהרה.';
                 stopButton.disabled = false; // Allow stopping even if max length reached
             } else {
                  messageArea.textContent = 'הלבה זורמת והקרום מתחיל להתמצק...';
             }


        } else { // If flow from source stopped (draining phase)

             // Only continue animating CS liquid drain if it's not empty
             if (parseFloat(crossSectionLiquid.style.width) > 0) {
                 // Draining animation is primarily handled by CSS transitions on stopFlow,
                 // but we can update the cross-section liquid shrinking here over time
                 // based on elapsed time since stop was pressed. Let's rely on CSS transitions triggered by stopFlow for simplicity.
                 messageArea.textContent = 'האספקה נעצרה, הלבה הפנימית מתנקזת...';
             } else {
                 messageArea.textContent = 'מנהרת לבה נוצרה! כעת החלל הפנימי חשוף.';
                  // Flow and drain finished
                 resetButton.disabled = false; // Allow reset
                 // Stop the animation loop as nothing is changing visually
                 if (animationFrameId) {
                    cancelAnimationFrame(animationFrameId);
                    animationFrameId = null;
                 }
                 return; // Stop the animation loop
             }
        }

         // Only request next frame if animation is ongoing
         if (isFlowing || parseFloat(crossSectionLiquid.style.width) > 0) {
             animationFrameId = requestAnimationFrame(animateFlow);
         }
    }

    function stopFlow() {
        if (!isFlowing || stopButton.disabled) return;
        isFlowing = false; // Stop flow from source
        stopButton.disabled = true;
        messageArea.textContent = 'עצירת אספקה... הלבה הפנימית מתחילה להתנקז!';


        // Stop the main flow length growth animation
         if (animationFrameId) {
             cancelAnimationFrame(animationFrameId);
         }

         // Animate the *visual representation* of the liquid draining *within* the crust
         // We want lavaFlow element to shrink upwards from the bottom of the crust
         const drainDuration = 3000; // ms
         const currentFlowHeight = parseFloat(lavaFlow.style.height);
         const crustTop = parseFloat(crust.style.top);


         // Set transition for draining animation
         lavaFlow.style.transition = `height ${drainDuration / 1000}s linear, top ${drainDuration / 1000}s linear`;
         lavaFlow.style.height = '0px'; // Shrink height
         // top should increase by current height to simulate shrinking from bottom
         // This requires changing transform-origin or calculating final top.
         // Simpler: animate height down and opacity out? Let's animate height down from top.
         // It visually represents the *level* of lava dropping.
         // The hollow space then appears *behind* it.


         // Make hollow space visible and match crust size and position
         hollowSpace.style.opacity = 1;
         hollowSpace.style.height = crust.style.height; // Hollow matches current crust length
         hollowSpace.style.top = crust.style.top;
         hollowSpace.style.left = crust.style.left;
         hollowSpace.style.width = '18px'; // Ensure width is set
         hollowSpace.style.zIndex = 2; // Put hollow space behind crust (z-index 4)

         // Add transition for hollow space appearance and growth
         hollowSpace.style.transition = `height ${drainDuration / 1000}s linear, top ${drainDuration / 1000}s linear, opacity 1s ease-in-out`;


         // Animate cross-section draining and hollow appearance
         crossSectionLiquid.style.transition = 'all 2s ease-in-out';
         crossSectionLiquid.style.width = '0%';
         crossSectionLiquid.style.height = '0%';
         crossSectionLiquid.style.top = '50%';
         crossSectionLiquid.style.left = '50%';
         crossSectionLiquid.style.opacity = 0; // Hide liquid color

         crossSectionHollow.style.transition = 'all 2s ease-in-out';
         crossSectionHollow.style.opacity = 1; // Show hollow outline

         // Start the drain animation loop for messages/final state check
         // Use setTimeout to allow CSS transitions to start
         setTimeout(() => {
              // Continue the animation loop briefly to allow CSS transitions to finish
              // and update messages. The loop will terminate when liquid size is 0.
             animateFlow(performance.now()); // Pass current time to continue timing
         }, 50); // Small delay to ensure transitions are applied
    }

    function resetSimulation() {
        isFlowing = false;
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
            animationFrameId = null;
        }
        startTime = null;
        currentLength = 0;

        // Remove transitions for instant reset
        lavaFlow.style.transition = 'none';
        crust.style.transition = 'none';
        hollowSpace.style.transition = 'none';
         crossSectionLiquid.style.transition = 'none';
         crossSectionCrust.style.transition = 'none';
         crossSectionHollow.style.transition = 'none';
         lavaSource.style.transition = 'none';

        // Reset visual states
        lavaSource.style.opacity = 0;
        lavaFlow.style.height = '0px';
        crust.style.height = '0px';
        hollowSpace.style.height = '0px';

        // Reset initial widths and tops (they are fixed in this sim)
        lavaFlow.style.width = '25px';
        crust.style.width = '25px';
        hollowSpace.style.width = '18px';
        lavaFlow.style.top = '35px';
        crust.style.top = '35px';
        hollowSpace.style.top = '35px';


        crust.style.opacity = 0;
        hollowSpace.style.opacity = 0;
         hollowSpace.style.zIndex = 2; // Default behind crust

         // Reset cross-section
        crossSectionLiquid.style.width = '80%';
        crossSectionLiquid.style.height = '80%';
        crossSectionLiquid.style.top = '10%';
        crossSectionLiquid.style.left = '10%';
        crossSectionLiquid.style.backgroundColor = 'red'; // Default color
         crossSectionLiquid.style.opacity = 1;
        crossSectionHollow.style.opacity = 0;
        crossSectionCrust.style.borderWidth = '5px'; // Initial crust border

        // Reset lava color to initial based on default temp value
        updateLavaColor(parseInt(tempInput.value));

        // Reset buttons and message
        startButton.disabled = false;
        stopButton.disabled = true;
        resetButton.disabled = false; // Reset button is always enabled after reset
        messageArea.textContent = 'לחצו "התחל זרימה" כדי לראות את הקסם מתרחש!';

         // Re-add transitions after reset so animations work next time
         requestAnimationFrame(() => {
             lavaFlow.style.transition = 'height linear, top linear, left linear, width linear, background 0.5s ease';
             crust.style.transition = 'height linear, top linear, left linear, width linear, opacity ease-in-out, background-color 0.5s ease';
              hollowSpace.style.transition = 'height linear, top linear, left linear, width linear, opacity ease-in-out';
              crossSectionLiquid.style.transition = 'all 0.5s ease-out';
              crossSectionCrust.style.transition = 'border-width 0.5s ease-out';
              crossSectionHollow.style.transition = 'all 0.5s ease-out, opacity 0.5s ease-in-out';
               lavaSource.style.transition = 'opacity 0.5s ease-in-out';
         });
    }

    startButton.addEventListener('click', startFlow);
    stopButton.addEventListener('click', stopFlow);
    resetButton.addEventListener('click', resetSimulation);

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מפורט' : 'סקרנים? לחצו לחשיפת סודות מנהרות הלבה!';
    });

    // Initial setup
     resetSimulation();
     updateLavaColor(parseInt(tempInput.value)); // Set color on page load
});

</script>
```