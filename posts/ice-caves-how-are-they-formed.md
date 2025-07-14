---
title: "מערות קרח: איך הן נוצרות?"
english_slug: ice-caves-how-are-they-formed
category: "מדעי כדור הארץ"
tags:
  - מערות קרח
  - קרחונים
  - גיאולוגיה
  - הידרולוגיה
  - תהליכים גיאומורפיים
---
# מערות קרח: איך הן נוצרות?

דמיינתם פעם שאתם צועדים לתוך לב קרחון, מוקפים בגוונים כחולים מהפנטים? מערות קרח הן פלאים אמיתיים של הטבע, שנראים כאילו פוסלו ביד אמן. אבל מהו הכוח הנסתר שיוצר את החללים הכחולים האלה בתוך מסת קרח ענקית? הצטרפו למסע אינטראקטיבי שיגלה לכם את הסוד המפתיע!

<div class="simulation-container">
    <div class="glacier-section">
        <div class="ice-texture"></div> <!-- Layer for ice texture/gradient -->
        <div class="initial-crack">
             <div class="water-drip"></div> <!-- Animated water drip -->
        </div>
        <div class="melt-area melt-path-1">
             <div class="water-flow"></div> <!-- Animated water flow -->
        </div>
        <div class="melt-area melt-path-2">
             <div class="water-flow"></div> <!-- Animated water flow -->
        </div>
        <div class="melt-area melt-cave">
             <div class="melt-effect"></div> <!-- Visual melt/blue effect -->
        </div>
        <div class="ice-label">חתך רוחב של קרחון</div>
    </div>
    <div class="controls">
        <h3>שחררו את הכוח המסתורי:</h3>
        <label for="flow">עוצמת זרימת מים:</label>
        <input type="range" id="flow" min="1" max="10" value="3">
        <span id="flowValue">3</span><br>

        <label for="temp">טמפרטורת מים (°C מעל 0):</label>
        <input type="range" id="temp" min="0.1" max="5" step="0.1" value="1">
        <span id="tempValue">1.0</span><br>

        <button id="startSim">התחילו את המסע!</button>
        <button id="resetSim" disabled>לאפס קרחון</button>
    </div>
    <div class="timeline">
        זמן גיאולוגי מואץ: <span id="currentTime">0</span> שנים
    </div>
</div>

<style>
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

body {
    font-family: 'Heebo', sans-serif;
    line-height: 1.6;
    color: #333;
}

h1, h2, h3 {
    color: #004d40; /* Deep teal */
}

.simulation-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 30px auto;
    padding: 30px;
    border: 1px solid #b2ebf2; /* Light blue border */
    border-radius: 12px;
    background: linear-gradient(to bottom right, #e0f7fa, #ffffff); /* Soft blue gradient */
    max-width: 650px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    overflow: hidden; /* Ensure inner shadows/elements are clipped */
}

.glacier-section {
    position: relative;
    width: 100%; /* Use full container width */
    max-width: 600px;
    height: 300px; /* Increased height */
    background: linear-gradient(to bottom, #e1f5fe 0%, #b3e5fc 50%, #81d4fa 100%); /* Icy blue gradient */
    border: 3px solid #0277bd; /* Deeper blue border */
    overflow: hidden;
    margin-bottom: 30px;
    border-radius: 8px;
    box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.3); /* Inner shadow for depth */
    isolation: isolate; /* Create a stacking context */
}

.ice-texture {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAiIGhlaWdodD0iMTAwIj4KICA8ZmlsdGVyIGlkPSJub2lzZSI+CiAgICA8ZmVUcmFjdGFsTm9pc2UgdHlwZT0idHVyYnVsZW5jZSIgYmFzZUZyZXF1ZW5jeT0iMC42IiBudW1PY3RhdmVzPSIyIiBzdGl0Y2hUaWxlcz0ic3RpdGNoIi8+CiAgICA8ZmVTY2FsZUluZlcgbW9zdExpZ2h0PSIxIiBrZXlzPSIwIDAuNTsgMSAxIiByZXN1bHQ9InNjYWxlZCIvPgogICAgPHhlbWFnaW5lIGluPSJzY2FsZWQiIGltYWdlMiI9IlNvdXJjZUdyYXBoaWMiIG9wZXJhdG9yPSJhdG9wIiByZXN1bHQ9Im1hc2siLz4KICA8ZmVDb2xvck1hdHJpeCB0eXBlPSJtYXRyaXgiIHZhbHVlcz0iMSAwIDAgMCAwICAgMCAxIDAgMCAwICAgMCAwIDEgMCAwICAgMCAwIDAgLTAuNyAwIiAvPgogIDwvZmlsdGVyPgogIDxyZWN0IHdpZHRoPSIxMDAiIGhlaWdodD0iMTAwIiBmaWxsPSIjZmZmZmZmIiBmaWx0ZXI9InVybCgjbm9pc2UpIiBvcGFjaXR5PSIwLjMiLz4KPC9zdmc+'); /* Subtle noise texture */
    background-size: cover;
    opacity: 0.3; /* Make texture subtle */
    z-index: 1;
}


.ice-label {
    position: absolute;
    top: 10px;
    left: 10px;
    font-size: 1em;
    color: #01579b; /* Darker blue */
    font-weight: bold;
    z-index: 3; /* Above texture and melt areas initially */
    padding: 5px 10px;
    background-color: rgba(255, 255, 255, 0.7);
    border-radius: 4px;
}


.initial-crack {
    position: absolute;
    top: 0;
    left: 50%; /* Center the crack */
    width: 8px; /* Thinner crack */
    height: 40px; /* Deeper initial crack */
    background: linear-gradient(to bottom, rgba(0, 188, 212, 0.8), rgba(0, 140, 255, 0.5)); /* Water gradient */
    transform: translateX(-50%); /* Center horizontally */
    z-index: 2;
    border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
}

.water-drip {
    position: absolute;
    bottom: -5px; /* Position below the crack */
    left: 50%;
    width: 5px;
    height: 5px;
    background-color: rgba(0, 140, 255, 0.8);
    border-radius: 50%;
    transform: translateX(-50%);
    animation: drip 1.5s infinite linear;
    opacity: 0; /* Starts hidden */
}

@keyframes drip {
    0% { transform: translate(-50%, 0); opacity: 1; }
    50% { transform: translate(-50%, 20px); opacity: 0; }
    100% { transform: translate(-50%, 0); opacity: 0; }
}


.melt-area {
    position: absolute;
    z-index: 2;
    opacity: 0; /* Starts invisible */
    transition: height 0.5s ease-out, width 0.5s ease-out, opacity 0.5s ease-out, background-color 0.5s ease-out, top 0.5s ease-out, left 0.5s ease-out, transform 0.5s ease-out; /* Smooth transitions */
    overflow: hidden; /* Keep flow animation inside bounds */
}

.water-flow {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, rgba(0, 188, 212, 0.5), rgba(0, 140, 255, 0.7), rgba(0, 188, 212, 0.5));
    background-size: 100% 300%; /* Make gradient longer than element */
    animation: flow-vertical 1.5s linear infinite;
    opacity: 0; /* Hidden until melting starts */
}

.melt-path-1 {
    top: 40px; /* Start below initial crack */
    left: 50%;
    width: 8px; /* Matches crack width */
    height: 0px; /* Starts as a line */
    transform: translateX(-50%); /* Center below crack */
    transform-origin: top center;
}

.melt-path-2 {
    top: 60px; /* Start slightly lower */
    left: 45%; /* Branching off */
    width: 6px; /* Thinner path */
    height: 0px;
    transform-origin: top right;
    transform: rotate(-15deg); /* Angle */
}

.melt-cave {
    top: 200px; /* Deeper inside the glacier */
    left: 40%; /* Position */
    width: 0px;
    height: 0px;
    border-radius: 50%; /* Circular initial shape */
    background-color: rgba(0, 100, 255, 0); /* Start transparent blue */
    transform: translate(-50%, -50%); /* Center based on top/left */
    box-shadow: 0 0 15px rgba(0, 100, 255, 0); /* Blue glow shadow, starts transparent */
    display: flex; /* Use flex to center inner effect */
    justify-content: center;
    align-items: center;
}

.melt-effect {
    width: 80%;
    height: 80%;
    background: radial-gradient(circle, rgba(0, 140, 255, 0.6) 0%, rgba(0, 100, 255, 0.4) 50%, rgba(0, 50, 200, 0) 100%); /* Inner blue glow/depth effect */
    border-radius: 50%;
    opacity: 0; /* Starts hidden */
    transition: opacity 0.5s ease-out;
}


@keyframes flow-vertical {
    0% { background-position: 0 0; }
    100% { background-position: 0 100%; }
}

.controls {
    width: 100%;
    max-width: 600px;
    background-color: #e3f2fd; /* Lighter blue */
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 20px;
    box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.1);
}

.controls h3 {
    text-align: center;
    margin-top: 0;
    color: #0277bd; /* Deep blue */
}

.controls label {
    display: inline-block;
    width: 180px; /* Increased width for labels */
    margin-bottom: 10px;
    font-weight: bold;
    color: #01579b; /* Darker blue */
}

.controls input[type="range"] {
    width: calc(100% - 190px); /* Adjust width */
    vertical-align: middle;
    margin-bottom: 10px;
    -webkit-appearance: none; /* Override default */
    appearance: none;
    height: 8px;
    background: #b3e5fc; /* Light blue track */
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
    background: #0277bd; /* Deep blue thumb */
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.controls input[type="range"]::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #0277bd;
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.controls span {
    display: inline-block;
    width: 40px;
    text-align: right;
    font-weight: bold;
    color: #01579b;
}


.controls button {
    display: block; /* Make buttons block level for better spacing */
    width: calc(50% - 10px); /* Half width minus margin */
    margin-top: 20px;
    padding: 12px 20px; /* Increased padding */
    cursor: pointer;
    background-color: #00bcd4; /* Primary blue */
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 1em;
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-weight: bold;
}

.controls button:hover {
    background-color: #0097a7; /* Darker blue on hover */
}

.controls button:active {
    transform: scale(0.98); /* Subtle press effect */
}

#startSim {
    float: right; /* Align start right */
    background-color: #4CAF50; /* Green for start */
}
#startSim:hover {
    background-color: #388E3C; /* Darker green */
}


#resetSim {
     float: left; /* Align reset left */
     background-color: #f44336; /* Red for reset */
}
#resetSim:hover {
    background-color: #d32f2f; /* Darker red */
}

.controls button:disabled {
    background-color: #b2ebf2; /* Lighter blue when disabled */
    cursor: not-allowed;
    opacity: 0.7;
    transform: none;
    box-shadow: none;
}

.timeline {
    width: 100%;
    max-width: 600px;
    text-align: center;
    font-weight: bold;
    color: #004d40;
    font-size: 1.1em;
    margin-top: 10px; /* Add some space */
}

#explanationButton {
    display: block;
    margin: 30px auto 10px auto; /* Space below button */
    padding: 12px 25px; /* Increased padding */
    cursor: pointer;
    background-color: #0277bd; /* Deep blue */
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 1.1em;
    font-weight: bold;
    transition: background-color 0.3s ease, transform 0.1s ease;
}

#explanationButton:hover {
    background-color: #01579b; /* Darker blue */
}
#explanationButton:active {
     transform: scale(0.98);
}


#explanation {
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #b2ebf2;
    border-radius: 8px;
    background-color: #e1f5fe; /* Lightest blue background */
    display: none; /* Hidden by default */
    box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.05);
}

#explanation h2 {
    color: #0277bd; /* Deep blue */
    margin-top: 0;
    margin-bottom: 15px;
    border-bottom: 2px solid #b3e5fc; /* Light blue underline */
    padding-bottom: 5px;
}

#explanation h3 {
    color: #03a9f4; /* Brighter blue */
    margin-top: 15px;
    margin-bottom: 10px;
}

#explanation p, #explanation ul {
    line-height: 1.7; /* More readable line height */
    margin-bottom: 15px;
}

#explanation ul {
    padding-left: 30px; /* Increased padding */
    list-style-type: disc; /* Ensure discs are visible */
}

#explanation li {
    margin-bottom: 8px;
}

.simulation-running .water-drip {
    animation-play-state: running;
}
.melt-area .water-flow {
    animation-play-state: paused; /* Start paused */
    opacity: 0; /* Hidden by default */
    transition: opacity 0.5s ease;
}
.melt-area.active .water-flow {
    animation-play-state: running;
    opacity: 1; /* Visible when active */
}


</style>

<button id="explanationButton">גלו את הסוד המדעי</button>

<div id="explanation">
    <h2>הסבר מעמיק: מסע אל תוך מערת הקרח</h2>

    <p>מערות קרח קרחוניות (Glacier Caves) הן תופעה מרהיבה שמתרחשת בתוך או מתחת לגושי קרח עצומים כמו קרחונים. חשוב להבדיל בינן לבין מערות בהן מצטבר קרח באופן זמני בחורף (Ice Caves שאינן קשורות לקרחונים). הקסם של המערות הקרחוניות טמון באופן היווצרותן - לא קיפאון, אלא דווקא...</p>

    <h3>הכוח המניע: המסה על ידי מים!</h3>
    <p>כן, שמעתם נכון. הגורם העיקרי ליצירת מערות קרח בקרחונים הוא <strong>המסתו</strong> של הקרח על ידי מים זורמים. מים אלו מגיעים בדרך כלל מפני שטח הקרחון (מי נמס בקיץ או ממי גשמים) או כתוצאה מחיכוך ובסיס הקרחון. גם מים בטמפרטורה מעט מעל 0°C מסוגלים להעביר חום לקרח ולהמיס אותו בהדרגה. זרימת המים חיונית כי היא מסלקת את מי ההמסה הקרים ומביאה כל הזמן מים 'חדשים' עם יכולת המסה נוספת.</p>

    <h3>מאיפה מגיעים המים?</h3>
    <ul>
        <li><strong>מי נמס עיליים:</strong> בקיץ, השמש ממיסה שלג וקרח על פני הקרחון, ויוצרת זרמי מים על פני השטח.</li>
        <li><strong>מוּלנים (Moulins):</strong> כאשר זרמי המים העיליים הללו נתקלים בסדק בקרחון, הם יכולים לצנוח לתוך הקרחון ולהקים פירים אנכיים דמויי בארות בעומק רב. המים הזורמים מטה בכוח רב מגבירים את קצב ההמסה.</li>
        <li><strong>זרימה תת-קרחונית:</strong> מים יכולים לזרום גם בבסיס הקרחון, המסה שנוצרת מלחץ עצום או מחום כדור הארץ (חום גיאותרמי).</li>
    </ul>

    <h3>המסלול הפנימי: תעלות ומערות</h3>
    <p>כשהמים חודרים לתוך הקרחון דרך סדקים או מולנים, הם מתחילים לזרום ברשת מסועפת של נתיבים. המים זורמים לאורך המורדות, בתוך סדקים קיימים, או חופרים לעצמם נתיבים חדשים תוך כדי המסה. לאורך זמן, הזרימה הממושכת באותם נתיבים מרחיבה אותם בהדרגה, ויוצרת תעלות קרח ואף חללים גדולים ומפוארים - מערות הקרח שאנו כה מתפעלים מהן.</p>

    <h3>השפעת התנאים: טמפרטורה וזרימה</h3>
    <ul>
        <li><strong>טמפרטורת המים:</strong> מים 'חמים' יותר (גם אם רק מעלה אחת או שתיים מעל הקיפאון) נושאים יותר אנרגיית חום שיכולה להמס קרח. טמפרטורה גבוהה יותר מובילה לקצב המסה מהיר יותר.</li>
        <li><strong>קצב זרימת המים:</strong> זרימה מהירה יותר מביאה נפח גדול יותר של מים (ולכן יותר חום) ליחידת זמן למגע עם הקרח. היא גם מסייעת בסילוק יעיל של מי ההמסה הרוויים והקרים, ומאפשרת למים 'רעננים' להמשיך בתהליך ההמסה. זרימה חזקה יותר מאיצה משמעותית את התהליך.</li>
    </ul>

    <h3>מדוע הן כחולות כל כך?</h3>
    <p>הצבע הכחול העמוק האופייני למערות קרח קרחוניות נובע מתכונות בליעת האור של קרח דחוס ונקי מבועות אוויר רבות. קרח בולע את אורכי הגל האדומים והירוקים של האור הנראה בצורה יעילה יותר מאשר את אורכי הגל הכחולים. כשאור השמש חודר לתוך מסה גדולה של קרח דחוס (כמו בדפנות המערה), הרכיבים האדומים והירוקים נבלעים בהדרגה לאורך המסלול הארוך שעובר האור בתוך הקרח, והרכיב הכחול הוא זה שמתפזר וחוזר לעין הצופה. ככל שמסת הקרח עבה ודחוסה יותר, כך הבליעה חזקה יותר והצבע הכחול נראה עמוק ועז יותר.</p>

    <h3>טבען החמקמק והמשתנה</h3>
    <p>חשוב לזכור שמערות קרח הן מבנים דינמיים וזמניים. הן משתנות ללא הרף כתוצאה מתנועת הקרחון, שינויים עונתיים בטמפרטורה ובזרימת המים, ואף קריסות. מה שנראה היום כמערה קסומה עשוי להשתנות, לקטון, או להיעלם בעונה הבאה, ולהפנות מקום ליצירות קרח חדשות.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const flowSlider = document.getElementById('flow');
    const tempSlider = document.getElementById('temp');
    const startButton = document.getElementById('startSim');
    const resetButton = document.getElementById('resetSim');
    const flowValueSpan = document.getElementById('flowValue');
    const tempValueSpan = document.getElementById('tempValue');
    const currentTimeSpan = document.getElementById('currentTime');
    const explanationButton = document.getElementById('explanationButton');
    const explanationDiv = document.getElementById('explanation');
    const simulationContainer = document.querySelector('.simulation-container');

    const initialCrack = document.querySelector('.initial-crack');
    const waterDrip = initialCrack.querySelector('.water-drip');
    const meltPath1 = document.querySelector('.melt-path-1');
    const meltPath2 = document.querySelector('.melt-path-2');
    const meltCave = document.querySelector('.melt-cave');
    const meltEffect = meltCave.querySelector('.melt-effect');
     const waterFlows = document.querySelectorAll('.water-flow');


    let simulationInterval = null;
    let time = 0; // Accelerated years
    let currentSize = { // Current dimensions in pixels
        'melt-path-1': 0,
        'melt-path-2': 0,
        'melt-cave': 0
    };

    const maxSize = { // Max dimensions in pixels for visual representation
        'melt-path-1': 250, // Max height of path 1
        'melt-path-2': 200, // Max height of path 2
        'melt-cave': 250    // Max diameter of the cave
    };

    // Update slider value displays
    flowSlider.oninput = () => {
        flowValueSpan.textContent = flowSlider.value;
    };
    tempSlider.oninput = () => {
        tempValueSpan.textContent = parseFloat(tempSlider.value).toFixed(1);
    };

    // Simulation update logic
    function updateSimulation() {
        time += 0.05; // 0.05 accelerated years per interval (100ms)
        currentTimeSpan.textContent = time.toFixed(1);

        const flowRate = parseInt(flowSlider.value); // 1-10
        const waterTemp = parseFloat(tempSlider.value); // 0.1-5

        // Calculate melt rate based on sliders
        // Scale flow (1-10) and temp (0.1-5) to influence rate.
        // Let's create a multiplier that ranges from low (flow=1, temp=0.1) to high (flow=10, temp=5).
        // Simple linear mapping of the product (flow * temp) which ranges from 0.1 to 50.
        const minProduct = 0.1;
        const maxProduct = 50;
        const currentProduct = flowRate * waterTemp;

        // Map product range [0.1, 50] to a desired pixel growth rate range per interval, e.g., [0.03, 1.5]
        const minRate = 0.03; // Pixels per interval at min settings
        const maxRate = 1.5;  // Pixels per interval at max settings

        const meltRatePerInterval = minRate + (maxRate - minRate) * (currentProduct - minProduct) / (maxProduct - minProduct);

        // Update sizes based on melt rate, capped by maxSize
        // Path 1 melts continuously
        currentSize['melt-path-1'] = Math.min(maxSize['melt-path-1'], currentSize['melt-path-1'] + meltRatePerInterval);

        // Path 2 starts melting significantly only when path 1 is somewhat established
        if (currentSize['melt-path-1'] > maxSize['melt-path-1'] * 0.2) { // Start path 2 melt after path 1 is 20%
             currentSize['melt-path-2'] = Math.min(maxSize['melt-path-2'], currentSize['melt-path-2'] + meltRatePerInterval * 0.8); // Path 2 slightly slower
        }


        // Cave starts melting significantly only when a path reaches it
        // Simple condition: start melting cave when path 1 or path 2 reaches a certain depth
        const pathReachThreshold = 150; // pixels depth
        const caveMeltFactor = 1.8; // Cave melts faster once flow reaches it

        if (currentSize['melt-path-1'] >= pathReachThreshold || currentSize['melt-path-2'] >= pathReachThreshold) {
             currentSize['melt-cave'] = Math.min(maxSize['melt-cave'], currentSize['melt-cave'] + meltRatePerInterval * caveMeltFactor);
        }


        // --- Update Visuals ---

        // Initial crack drip starts when sim runs
         waterDrip.style.animationPlayState = 'running';

        // Path 1 height and opacity
        meltPath1.style.height = `${currentSize['melt-path-1']}px`;
        meltPath1.style.opacity = `${Math.min(1, currentSize['melt-path-1'] / 40)}`; // Fade in as it grows

         // Activate water flow animation in path 1 when it starts growing
        if (currentSize['melt-path-1'] > 5) {
            meltPath1.classList.add('active');
        } else {
             meltPath1.classList.remove('active');
        }


        // Path 2 height and opacity
        meltPath2.style.height = `${currentSize['melt-path-2']}px`;
         meltPath2.style.opacity = `${Math.min(1, currentSize['melt-path-2'] / 30)}`; // Fade in as it grows

         // Activate water flow animation in path 2
         if (currentSize['melt-path-2'] > 5) {
             meltPath2.classList.add('active');
         } else {
             meltPath2.classList.remove('active');
         }


        // Cave size, opacity, color, and effect
        if (currentSize['melt-cave'] > 0) {
             const caveSize = currentSize['melt-cave'];
             const caveProgress = caveSize / maxSize['melt-cave']; // 0 to 1

             meltCave.style.width = `${caveSize}px`;
             meltCave.style.height = `${caveSize}px`;
             meltCave.style.opacity = `${Math.min(1, caveSize / 50)}`; // Fade in

             // Transition background color towards deeper blue as it grows
             // Map progress [0, 1] to blue color component [100, 255] and alpha [0.4, 1]
             const blueComponent = Math.floor(100 + (255 - 100) * caveProgress);
             const alpha = Math.min(1, 0.4 + caveProgress * 0.6);
             meltCave.style.backgroundColor = `rgba(0, 0, ${blueComponent}, ${alpha})`;

             // Animate inner glow effect opacity
             meltEffect.style.opacity = `${Math.min(1, caveProgress * 2)}`; // Glow appears faster than size

             // Add subtle blue box shadow as it grows
             const shadowSpread = Math.min(15, caveSize / 10);
             const shadowOpacity = Math.min(0.5, caveProgress * 0.8);
             meltCave.style.boxShadow = `0 0 ${shadowSpread}px rgba(0, 100, 255, ${shadowOpacity})`;
        }


        // Stop condition: Stop when cave is nearly full size
        if (currentSize['melt-cave'] >= maxSize['melt-cave'] * 0.98) {
             clearInterval(simulationInterval);
             simulationInterval = null;
             startButton.disabled = false;
             resetButton.disabled = false;
             waterDrip.style.animationPlayState = 'paused';
             waterFlows.forEach(wf => wf.parentElement.classList.remove('active'));
        }
    }

    // Button handlers
    startButton.addEventListener('click', () => {
        if (!simulationInterval) {
            // Reset if it was stopped near the end
            if (currentSize['melt-cave'] >= maxSize['melt-cave'] * 0.98) {
                 resetSimulation(); // Reset entirely before starting again
            }
            simulationInterval = setInterval(updateSimulation, 100); // Run update every 100ms
            startButton.disabled = true;
            resetButton.disabled = false;
            simulationContainer.classList.add('simulation-running');
        }
    });

    resetButton.addEventListener('click', resetSimulation); // Use the reset function

    function resetSimulation() {
        clearInterval(simulationInterval);
        simulationInterval = null;
        time = 0;
        currentTimeSpan.textContent = time.toFixed(1);

        // Reset sizes
        currentSize = {
            'melt-path-1': 0,
            'melt-path-2': 0,
            'melt-cave': 0
        };

        // Reset visual states
        meltPath1.style.height = '0px';
        meltPath1.style.opacity = '0';
        meltPath1.classList.remove('active');


        meltPath2.style.height = '0px';
        meltPath2.style.opacity = '0';
        meltPath2.classList.remove('active');


        meltCave.style.width = '0px';
        meltCave.style.height = '0px';
        meltCave.style.opacity = '0';
        meltCave.style.backgroundColor = 'rgba(0, 100, 255, 0)';
        meltCave.style.boxShadow = 'none';
        meltEffect.style.opacity = '0';

        waterDrip.style.animationPlayState = 'paused';
        simulationContainer.classList.remove('simulation-running');


        startButton.disabled = false;
        resetButton.disabled = true;

        // Reset sliders to initial values (optional, but good for a full reset)
        // flowSlider.value = 3;
        // tempSlider.value = 1.0;
        // flowValueSpan.textContent = 3;
        // tempValueSpan.textContent = 1.0.toFixed(1);

    }


    // Explanation button handler
    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר הסבר מלא' : 'גלו את הסוד המדעי'; // Toggle button text
        // Scroll to explanation?
         if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth' });
         }
    });

    // Initial display update for sliders
    flowValueSpan.textContent = flowSlider.value;
    tempValueSpan.textContent = parseFloat(tempSlider.value).toFixed(1);

    // Set initial state for water drip (paused)
    waterDrip.style.animationPlayState = 'paused';
});
</script>
```