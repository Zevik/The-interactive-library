---
title: "הסוד השחור: מפחם ל-Carbon Black"
english_slug: the-black-secret-from-coal-to-carbon-black
category: "הנדסה כימית"
tags: [Carbon black, פחם, כימיה תעשייתית, סימולציה, ייצור]
---
<h1>הסוד השחור: מהפך פחם ל-Carbon Black</h1>
<p>דמיינו לרגע: הצבע העמוק בצמיגים שלכם, הדיו שמדפיס עיתונים, הפיגמנט בפלסטיק שסביבנו – רבים מהם חייבים את קיומם לאבקה שחורה וקסומה המופקת מפחם או מחומרי גלם פחמימניים אחרים. איך הופכים חומר גלם מוכר כמו פחם לאבקת Carbon Black הטהורה והחיונית הזו, דרך תהליך כימי מבוקר בטמפרטורות קיצוניות? בואו נגלה ונשפיע על התוצאה בעצמנו!</p>

<div id="carbonBlackApp">
    <div class="app-container">
        <div class="controls">
            <h2>כוונו את הכור</h2>
            <div class="control-group">
                <label for="temperature">טמפרטורה בכור (°C):</label>
                <input type="range" id="temperature" min="1000" max="1800" value="1400">
                <span id="tempValue">1400</span>
            </div>
            <div class="control-group">
                <label for="residenceTime">זמן שהייה (שניות):</label>
                <input type="range" id="residenceTime" min="0.05" max="0.8" step="0.01" value="0.30"> <!-- Adjusted range/step -->
                <span id="timeValue">0.30</span>
            </div>
            <button id="runSimulation">התחילו את הייצור!</button>
        </div>
        <div class="simulation-results">
            <div class="simulation-area">
                <div class="reactor-visualization">
                    <div class="inlet">חומר גלם</div>
                    <div class="furnace">
                        <span class="furnace-label">כור לוהט</span>
                        <div class="flame" id="flame"></div>
                    </div>
                    <div class="outlet">תוצר + גזים</div>
                    <div class="product-collection">
                         <div class="carbon-black-pile" id="carbonBlackPile"></div>
                         <div class="collection-label">Carbon Black</div>
                    </div>
                    <div class="process-indicator" id="processIndicator">מוכן לפעולה</div>
                </div>
            </div>
            <div class="results">
                <h2>תוצאות הייצור</h2>
                <p><i class="icon-yield"></i> תפוקה (Yield): <span id="yieldResult" class="result-value">- %</span></p>
                <p><i class="icon-purity"></i> טוהר המוצר: <span id="purityResult" class="result-value">- %</span></p>
                <p><i class="icon-particle"></i> גודל חלקיק ממוצע: <span id="particleSizeResult" class="result-value">- nm</span></p>
            </div>
        </div>
    </div>
</div>

<style>
/* General Styles */
#carbonBlackApp {
    font-family: 'Arial', sans-serif;
    direction: rtl;
    text-align: right;
    margin: 20px auto;
    max-width: 900px;
    border: 1px solid #dcdcdc;
    padding: 25px;
    border-radius: 10px;
    background-color: #f8f8f8;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    color: #333;
}

.app-container {
    display: flex;
    flex-direction: column;
    gap: 30px;
}

/* Controls & Results Panels */
.controls, .results {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.controls h2, .results h2 {
    margin-top: 0;
    text-align: center;
    color: #2c3e50; /* Dark blue-grey */
    margin-bottom: 20px;
    font-size: 1.5em;
}

.control-group {
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 15px;
}

.control-group label {
    flex-shrink: 0;
    width: 140px; /* Increased width for labels */
    font-weight: bold;
    color: #555;
}

.control-group input[type="range"] {
    flex-grow: 1;
    cursor: pointer;
    accent-color: #e74c3c; /* Red accent */
}

.control-group span {
    flex-shrink: 0;
    width: 50px; /* Increased width for value */
    text-align: center;
    font-weight: bold;
    color: #333;
}

/* Button */
#runSimulation {
    display: block;
    width: 100%;
    padding: 12px;
    background-color: #3498db; /* Blue */
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 1.1em;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-weight: bold;
}

#runSimulation:hover:not(:disabled) {
    background-color: #2980b9; /* Darker blue */
}

#runSimulation:active:not(:disabled) {
    transform: scale(0.98);
}

#runSimulation:disabled {
    background-color: #bdc3c7; /* Grey */
    cursor: not-allowed;
}

/* Simulation Area */
.simulation-results {
    display: flex;
    flex-direction: column;
    gap: 30px;
}

.simulation-area {
    flex-grow: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #ecf0f1; /* Light grey */
    border: 1px solid #dcdcdc;
    border-radius: 8px;
    padding: 30px 20px;
    min-height: 250px; /* Ensure more height */
    position: relative; /* Needed for absolute positioning of elements */
}

.reactor-visualization {
    display: flex;
    align-items: center;
    position: relative;
    width: 100%;
    max-width: 600px; /* Limit reactor width */
    height: 120px; /* Reactor height */
}

.inlet, .outlet {
    width: 90px; /* Wider labels */
    text-align: center;
    font-size: 1em;
    color: #555;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    font-weight: bold;
}

.inlet {
    right: 0;
}

.outlet {
    left: 0;
}

.furnace {
    flex-grow: 1;
    height: 100%;
    background-color: #c0392b; /* Reddish for heat */
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    border: 3px solid #a03020; /* Darker border */
    position: relative;
    overflow: hidden;
    margin: 0 100px; /* Space for inlet/outlet labels */
    border-radius: 8px;
    box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.5); /* Inner shadow for depth */
}

.furnace-label {
    position: relative; /* Z-index over flame */
    z-index: 1;
    font-size: 1.2em;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}


/* Flame Animation */
.flame {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to right, rgba(255, 215, 0, 0.6), rgba(255, 87, 51, 0.8)); /* Gold to reddish-orange */
    opacity: 0.7; /* Base opacity */
    transition: opacity 0.5s ease, background 0.5s ease; /* Smooth transition for temp effect */
    animation: flicker 1.5s infinite alternate; /* Subtle flicker effect */
}

@keyframes flicker {
    0%, 100% { opacity: 0.7; }
    50% { opacity: 0.85; }
}

/* Temperature-based flame intensity (handled by JS changing opacity/gradient) */
/* Example CSS class, JS will modify style directly */
.flame.high-temp {
    background: linear-gradient(to right, rgba(255, 165, 0, 0.8), rgba(255, 0, 0, 0.9)); /* More intense colors */
    opacity: 0.9;
    animation-duration: 1s; /* Faster flicker at higher temp */
}

.flame.low-temp {
     background: linear-gradient(to right, rgba(255, 230, 150, 0.4), rgba(255, 120, 80, 0.6)); /* Less intense colors */
     opacity: 0.5;
     animation-duration: 2s; /* Slower flicker at lower temp */
}


.product-collection {
    position: absolute;
    left: 20px; /* Position near outlet, slightly offset */
    bottom: -40px; /* Below the reactor */
    width: 70px; /* Collection area width */
    height: 40px; /* Collection area height */
    background-color: #ddd; /* Base for pile area */
    border: 1px solid #ccc;
    border-radius: 0 0 8px 8px;
    display: flex;
    justify-content: center;
    align-items: flex-end;
    overflow: hidden; /* Ensure pile stays within bounds */
}

.collection-label {
     position: absolute;
     top: -20px; /* Above the collection area */
     left: 50%;
     transform: translateX(-50%);
     font-size: 0.9em;
     color: #555;
     white-space: nowrap;
}

.carbon-black-pile {
    width: 0; /* Starts empty */
    height: 0; /* Starts empty */
    background-color: #1a1a1a; /* Very dark black */
    border-radius: 50% 50% 0 0 / 100% 100% 0 0; /* Pile shape */
    transition: all 1s cubic-bezier(0.4, 0, 0.2, 1); /* Smoother animation */
    position: absolute; /* Position correctly within collection area */
    bottom: 0;
    left: 50%;
    transform: translateX(-50%); /* Center the pile */
}

.process-indicator {
    position: absolute;
    top: -30px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 1em;
    color: #333;
    font-weight: bold;
    transition: color 0.5s ease; /* Animate color change */
}

.process-indicator.processing {
    color: #e74c3c; /* Red/orange when processing */
}

.process-indicator.done {
    color: #2ecc71; /* Green when done */
}


/* Results Section */
.results {
    text-align: right;
}

.results p {
    margin: 10px 0;
    font-size: 1.1em;
    color: #555;
}

.results p i {
    margin-left: 10px; /* Space for icons */
    color: #3498db; /* Icon color */
    /* Basic placeholder icons */
    display: inline-block;
    width: 1em;
    text-align: center;
}

.icon-yield::before { content: '📦'; } /* Example unicode icon */
.icon-purity::before { content: '✨'; }
.icon-particle::before { content: '🔬'; }

.result-value {
    font-weight: bold;
    color: #2c3e50; /* Dark blue-grey */
    transition: color 0.5s ease; /* Animate color change */
}


/* Responsive Adjustments */
@media (min-width: 768px) {
    .app-container {
        flex-direction: row;
    }
    .controls {
        flex-basis: 350px; /* Wider control panel */
        flex-shrink: 0;
    }
    .simulation-results {
        flex-grow: 1;
        flex-direction: row; /* Arrange simulation area and results side-by-side */
        gap: 20px;
    }
     .simulation-area {
         flex-grow: 2; /* Simulation area takes more space */
         min-height: 300px; /* More height for visualization */
         padding: 40px 20px; /* More padding */
     }
     .results {
         flex-basis: 200px; /* Results panel width */
         flex-shrink: 0;
         align-self: flex-start; /* Align results to the top */
     }
    .reactor-visualization {
         width: 100%;
         max-width: none;
         margin: 0 auto;
         height: 150px; /* Taller reactor */
    }
     .inlet { right: auto; left: 0; transform: translateY(-50%); } /* Adjust for LTR visual flow */
     .outlet { left: auto; right: 0; transform: translateY(-50%); } /* Adjust for LTR visual flow */
     .furnace { margin: 0 100px; } /* Maintain space */
     .product-collection { left: auto; right: 20px; bottom: -50px; width: 80px; height: 50px; } /* Position near outlet (right side visually) */
     .collection-label { right: 0; left: auto; transform: translateX(50%); top: -25px; } /* Adjust label position */
}


/* Explanation Section Styles */
#toggleExplanation {
    display: block;
    margin: 30px auto;
    padding: 12px 25px;
    background-color: #95a5a6; /* Grey */
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 1em;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-weight: bold;
}

#toggleExplanation:hover {
    background-color: #7f8c8d; /* Darker grey */
}
#toggleExplanation:active {
    transform: scale(0.98);
}


#explanation {
    margin-top: 20px;
    padding: 25px;
    border: 1px solid #dcdcdc;
    border-radius: 8px;
    background-color: #f8f8f8;
    direction: rtl;
    text-align: right;
    line-height: 1.7;
    color: #444;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

#explanation h2, #explanation h3 {
    color: #2c3e50;
    margin-top: 20px;
    margin-bottom: 10px;
    font-weight: bold;
}

#explanation h2 {
    font-size: 1.6em;
    border-bottom: 2px solid #3498db;
    padding-bottom: 5px;
    margin-bottom: 15px;
}

#explanation h3 {
    font-size: 1.3em;
    color: #3498db;
}

#explanation p {
    margin-bottom: 15px;
}

#explanation ul {
    margin-bottom: 15px;
    padding-right: 25px; /* Adjust for RTL list indent */
    list-style: disc outside; /* Ensure list style is visible */
}

#explanation li {
    margin-bottom: 8px;
    padding-right: 5px; /* Small padding for spacing */
}
</style>

<button id="toggleExplanation">הצגת הסבר מפורט</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מעמיק: מסעו של הפחמן - מהפחם ל-Carbon Black</h2>
    <p>Carbon Black הוא חומר פחמני טהור בצורת אבקה עדינה, המיוצר בתהליך הנדסי מדויק. בניגוד לפיח ביתי (soot), שהוא תוצר לוואי לא מבוקר של שריפה, Carbon Black מיוצר בתנאים קפדניים כדי להקנות לו תכונות ספציפיות ההופכות אותו לחיוני בתעשיות רבות.</p>

    <h3>למה Carbon Black? שימושים שהופכים אותו למרכיב סודי</h3>
    <p>תכונותיו הייחודיות של Carbon Black – גודל חלקיק זעיר, שטח פנים גדול, צבע שחור עמוק, ומוליכות חשמלית – הופכות אותו לחיוני עבור:</p>
    <ul>
        <li><strong>תעשיית הגומי:</strong> מרכיב קריטי (עד 30%) בצמיגי רכב ומוצרי גומי אחרים. הוא לא רק מעניק את הצבע השחור האופייני, אלא בעיקר משפר באופן דרמטי את עמידות הגומי בפני שחיקה, קרעים וחום, ומאריך את חיי המוצר.</li>
        <li><strong>פיגמנט שחור:</strong> הצבע השחור העמוק והיציב ביותר המשמש בדיו (דפוס, הזרקת דיו), צבעים תעשייתיים, ציפויים, ופלסטיק. הוא מאפשר כיסוי מעולה ועמידות בפני דהייה.</li>
        <li><strong>תוסף מוליך:</strong> במוצרי פלסטיק, ציפויים וסוללות כדי להגביר את המוליכות החשמלית.</li>
        <li><strong>שימושים מיוחדים:</strong> במסננים, בטקסטיל, במוצרי קוסמטיקה ועוד.</li>
    </ul>

    <h3>מסע המולקולות: חומרי גלם ותהליך הפירוק</h3>
    <p>הייצור מתבסס על חימום קיצוני של חומרי גלם עשירים בפחמן, לרוב בתהליך הנקרא Furnace Black Process, הנפוץ בעולם. חומרי הגלם האופייניים כוללים:</p>
    <ul>
        <li><strong>שמנים כבדים:</strong> תוצרי לוואי של זיקוק נפט (כמו Carbon Black Oil, Decant Oil) - המקור העיקרי כיום.</li>
        <li><strong>גז טבעי:</strong> (מתאן) - שימש בעבר ועדיין בשימוש עבור סוגי Carbon Black מסוימים.</li>
    </ul>
    <p>בלב התהליך עומד הכור התעשייתי, שם מוזרם חומר הגלם לתוך זרם גזים חמים בטמפרטורות הנעות בין 1000 ל-1800 מעלות צלזיוס! בטמפרטורות אלו, מולקולות הפחמימנים הגדולות עוברות פירוק תרמי מהיר (פירוליזה) בסביבה עם כמות מוגבלת מאוד של חמצן (שריפה חלקית בלבד). שיירי הפחמן שנוצרים מתגבשים במהירות ליצירת החלקיקים הכדוריים המיקרוסקופיים של Carbon Black. התערובת החמה מקוררת בפתאומיות ("Quenching") על ידי הזרקת מים, והחלקיקים נאספים מהגזים.</p>

    <h3>שליטה בתהליך = שליטה במוצר: הפרמטרים המשפיעים</h3>
    <p>הסימולציה שבה התנסיתם ממחישה כיצד שינוי תנאי הכור משפיע על התוצאה הסופית. התכונות המרכזיות של Carbon Black – גודל החלקיק, שטח הפנים שלו, המבנה האגרגטיבי (צורת ההתחברות של החלקיקים) והטוהר – נקבעות באופן מהותי על ידי פרמטרי התהליך:</p>
    <ul>
        <li><strong>טמפרטורה בכור:</strong> טמפרטורה גבוהה מאיצה את הפירוק אך עשויה להשפיע על גודל החלקיקים והמבנה. שליטה מדויקת חיונית לקבלת התכונות הרצויות.</li>
        <li><strong>זמן שהייה בכור:</strong> משך הזמן שבו חומר הגלם שוהה בטמפרטורה הגבוהה. זמן קצר מדי יגרום לפירוק לא מלא ולתפוקה נמוכה; זמן ארוך מדי עלול לגרום לגדילה ואיחוי יתר של החלקיקים.</li>
        <li><strong>יחס חומר גלם לגזים החמים:</strong> משפיע על הטמפרטורה בפועל ועל ריכוז חומרי המוצא.</li>
        <li><strong>סוג חומר הגלם:</strong> משפיע באופן יסודי על הרכב וגודל החלקיקים שיווצרו.</li>
    </ul>
    <p>באופן כללי, טמפרטורות גבוהות יותר וזמני שהייה קצרים יותר נוטים לייצר חלקיקים קטנים יותר עם שטח פנים גדול יותר (דרוש, למשל, עבור צבעי דפוס איכותיים), בעוד שטמפרטורות נמוכות יותר וזמני שהייה ארוכים יותר נוטים לייצר חלקיקים גדולים יותר (מתאים, למשל, לשימושים מסוימים בגומי). המורכבות טמונה בקבלת השילוב המדויק של כל התכונות יחד.</p>

    <h3>אתגרים וקיימות</h3>
    <p>ייצור Carbon Black דורש אנרגיה רבה ומתמודד עם אתגרים תפעוליים וסביבתיים. תהליכי הייצור המודרניים כוללים מערכות מתוחכמות לבקרת פליטות ולניצול אנרגיית החום המשתחררת (לרוב לייצור קיטור או חשמל), תוך שאיפה מתמדת לשיפור יעילות וצמצום ההשפעה הסביבתית.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const tempSlider = document.getElementById('temperature');
    const tempValueSpan = document.getElementById('tempValue');
    const timeSlider = document.getElementById('residenceTime');
    const timeValueSpan = document.getElementById('timeValue');
    const runButton = document.getElementById('runSimulation');
    const yieldResultSpan = document.getElementById('yieldResult');
    const purityResultSpan = document.getElementById('purityResult');
    const particleSizeResultSpan = document.getElementById('particleSizeResult');
    const carbonBlackPileDiv = document.getElementById('carbonBlackPile');
    const processIndicator = document.getElementById('processIndicator');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const flameDiv = document.getElementById('flame'); // Get the flame element

    // Update slider value displays
    tempSlider.addEventListener('input', () => {
        const temp = parseInt(tempSlider.value);
        tempValueSpan.textContent = temp;
        updateFlameVisual(temp); // Update flame visualization
    });

    timeSlider.addEventListener('input', () => {
        timeValueSpan.textContent = parseFloat(timeSlider.value).toFixed(2);
    });

    // Function to update flame appearance based on temperature
    function updateFlameVisual(temperature) {
        const tempNorm = (temperature - 1000) / (1800 - 1000); // Normalize 1000-1800 to 0-1
        // Interpolate colors/opacity based on tempNorm
        const r1 = Math.round(255); g1 = Math.round(215 - 50 * tempNorm); b1 = Math.round(0); a1 = 0.6 + 0.2 * tempNorm; // Start color (Gold to Orange)
        const r2 = Math.round(255); g2 = Math.round(87 - 87 * tempNorm); b2 = Math.round(51 - 51 * tempNorm); a2 = 0.8 + 0.1 * tempNorm; // End color (Reddish-Orange to Red)

        flameDiv.style.background = `linear-gradient(to right, rgba(${r1}, ${g1}, ${b1}, ${a1.toFixed(2)}), rgba(${r2}, ${g2}, ${b2}, ${a2.toFixed(2)}))`;
        flameDiv.style.opacity = (0.7 + 0.2 * tempNorm).toFixed(2); // Overall opacity increases slightly
        flameDiv.style.animationDuration = `${2 - 1 * tempNorm}s`; // Faster flicker at higher temp
    }


    // Simulation logic (Adjusted ranges and formula slightly for illustration)
    function simulateProcess(temperature, residenceTime) {
        // Normalize inputs to 0-1 range based on slider min/max
        const tempNorm = (temperature - 1000) / (1800 - 1000); // 1000-1800
        const timeNorm = (residenceTime - 0.05) / (0.8 - 0.05); // 0.05-0.8

        // Simplified, non-linear mapping for results
        // These relationships are illustrative and not based on precise chemical kinetics.
        // They aim to show general trends:
        // - Yield: Peaks at intermediate T/t, drops at extremes.
        // - Purity: Decreases slightly with higher T, maybe also with longer t.
        // - Particle Size: Increases with higher T and longer t.

        // Example formulas showing slightly more complex interaction
        let yieldVal = 60 + 35 * Math.sin(Math.PI * tempNorm) * Math.sin(Math.PI * timeNorm); // Peaks around 0.5,0.5 normalized
        yieldVal = Math.max(55, Math.min(95, yieldVal)); // Clamp

        let purityVal = 98 - 8 * tempNorm - 3 * timeNorm - 5 * tempNorm * timeNorm; // Decreases with both, some synergy
        purityVal = Math.max(85, Math.min(98, purityVal)); // Clamp

        let particleSizeVal = 15 + 135 * (tempNorm * 0.5 + timeNorm * 0.5 + tempNorm * timeNorm * 0.5); // Strong increase with both
        particleSizeVal = Math.max(15, Math.min(150, particleSizeVal)); // Clamp

        return {
            yield: yieldVal.toFixed(1),
            purity: purityVal.toFixed(1),
            particleSize: particleSizeVal.toFixed(1)
        };
    }

    // Run simulation and update display
    runButton.addEventListener('click', () => {
        const temp = parseInt(tempSlider.value);
        const time = parseFloat(timeSlider.value);

        // Visual feedback: Indicate processing
        processIndicator.textContent = 'מעבד...';
        processIndicator.classList.add('processing');
        processIndicator.classList.remove('done');
        runButton.disabled = true;

        // Reset results and pile visually
        yieldResultSpan.textContent = '- %';
        purityResultSpan.textContent = '- %';
        particleSizeResultSpan.textContent = '- nm';
        carbonBlackPileDiv.style.width = '0';
        carbonBlackPileDiv.style.height = '0';
        carbonBlackPileDiv.style.backgroundColor = '#1a1a1a'; // Reset pile color if it was changed

        // Determine simulation duration based on residence time slider (faster feedback for shorter times)
        const simulationDuration = 500 + (1 - (time - 0.05) / (0.8 - 0.05)) * 1000; // 500ms to 1500ms

        // Simulate with a delay for visual effect
        setTimeout(() => {
            const results = simulateProcess(temp, time);

            // Animate results appearing (simple delay/fade effect implied by CSS transition on result-value)
            yieldResultSpan.textContent = results.yield + ' %';
            purityResultSpan.textContent = results.purity + ' %';
            particleSizeResultSpan.textContent = results.particleSize + ' nm';

             // Update visual pile based on yield (example mapping yield 55-95 to pile size)
            const pileSizeFactor = (results.yield - 55) / (95 - 55); // Normalize yield 55-95 to 0-1
            const pileWidth = 30 + pileSizeFactor * 60; // Pile width 30-90px
            const pileHeight = 20 + pileSizeFactor * 50; // Pile height 20-70px
            carbonBlackPileDiv.style.width = `${pileWidth}px`;
            carbonBlackPileDiv.style.height = `${pileHeight}px`;

             // Optional: Subtle pile color/texture change based on particle size (CSS gradient/filter could do this)
             // For simplicity, we'll just slightly vary color towards lighter/greyer for larger particles
             const particleNorm = (results.particleSize - 15) / (150 - 15); // Normalize 15-150nm to 0-1
             const greyValue = Math.round(26 + particleNorm * 50); // From 1a1a1a (26) towards 5a5a5a (90)
             carbonBlackPileDiv.style.backgroundColor = `rgb(${greyValue}, ${greyValue}, ${greyValue})`;


            processIndicator.textContent = 'ייצור הסתיים!';
            processIndicator.classList.remove('processing');
            processIndicator.classList.add('done');
            runButton.disabled = false;

        }, simulationDuration); // Use calculated duration
    });

    // Toggle explanation
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מפורט' : 'הצגת הסבר מפורט';
    });

    // Initial update of slider values and flame visualization
    tempValueSpan.textContent = tempSlider.value;
    timeValueSpan.textContent = parseFloat(timeSlider.value).toFixed(2);
    updateFlameVisual(parseInt(tempSlider.value)); // Set initial flame state
});
</script>