---
title: "מסע קוונטי: איך טלפורטציה קוונטית עובדת?"
english_slug: quantum-magic-teleportation-revealed
category: "פיזיקה"
tags:
  - פיזיקה קוונטית
  - טלפורטציה
  - סבוך קוונטי
  - מידע קוונטי
  - שזירה
---
# מסע קוונטי: איך טלפורטציה קוונטית עובדת?

דמיינו שאתם יכולים 'לשלוח' את המצב המדויק של חלקיק אטום אחד לחלקיק אחר, מרוחק, מבלי שהחלקיק הראשון זז ממקומו ומבלי שידעתם בכלל מה היה המצב המדויק שלו! נשמע כמו מדע בדיוני? זו המציאות המדהימה של טלפורטציה קוונטית.

**התנסו בעצמכם:**

<div id="quantum-teleportation-app">
    <div class="locations-container">
        <div class="location" id="location1">
            <h2>עמדת אליס <span class="role">(שולחת)</span></h2>
            <div class="particle-container">
                <span>חלקיק A (ה"נשלח"):</span> <div class="particle" id="particleA">?</div>
            </div>
             <div class="particle-container">
                <span>חלקיק B (זוג סבוך):</span> <div class="particle" id="particleB">B</div>
            </div>
            <div class="action-area measurement-area">
                <button id="bell-measurement-button" class="action-button">1. בצעו מדידת בל על A ו-B</button>
                <div id="measurement-result" class="status-message">תוצאת מדידה: ממתין...</div>
            </div>
        </div>

        <div class="classical-channel">
            <div class="classical-channel-label">ערוץ קלאסי</div>
            <div id="classical-signal-path">
                <div id="classical-signal"></div>
            </div>
            <div id="classical-signal-status" class="status-message">אות קלאסי: ממתין...</div>
        </div>

        <div class="location" id="location2">
            <h2>עמדת בוב <span class="role">(מקבל)</span></h2>
             <div class="particle-container">
                <span>חלקיק C (המטרה):</span> <div class="particle" id="particleC">C</div>
            </div>
            <div class="action-area transformation-area">
                <button id="apply-transformation-button" class="action-button" disabled>2. הפעילו טרנספורמציה על C</button>
                <div id="final-state-comparison" class="status-message">מצב C הסופי: ממתין...</div>
            </div>
        </div>
    </div>
    <div class="entanglement-link">
        <div class="entanglement-label">סבוך קוונטי</div>
    </div>

     <button id="reset-simulation-button" class="secondary-button">התחל סימולציה מחדש</button>
</div>

<button id="toggle-explanation" class="secondary-button">הצג הסבר מלא על טלפורטציה קוונטית</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: טלפורטציה קוונטית, שלב אחר שלב</h2>
    <p>טלפורטציה קוונטית אינה מעבירה חומר פיזי, אלא את המצב הקוונטי (כלומר, את כל המידע המדויק) של חלקיק אחד (חלקיק A) לחלקיק אחר מרוחק (חלקיק C). המצב הקוונטי יכול להיות ספין "למעלה" או "למטה", או כל סופרפוזיציה מורכבת שלהם.</p>

    <h3>רכיבים חיוניים:</h3>
    <ul>
        <li><b>חלקיק A:</b> החלקיק שמצבו הקוונטי יעבור טלפורטציה. המצב ההתחלתי שלו יכול להיות כל מצב קוונטי אפשרי, והוא *אינו ידוע* למי שמבצע את הטלפורטציה (אליס).</li>
        <li><b>זוג חלקיקים סבוכים (B ו-C):</b> חלקיקים אלו חולקים מצב "שזירה" או "סבוך" (Entanglement). זהו קשר קוונטי חזק במיוחד: מדידה על אחד משפיעה באופן מיידי על מצב האחר, לא משנה מה המרחק. חלקיק B נמצא עם A אצל אליס, וחלקיק C נמצא אצל בוב. הסבוך משמש כ"ערוץ קוונטי" סמוי.</li>
    </ul>

    <h3>התהליך (כמו בסימולציה):</h3>
    <ol>
        <li><b>מדידת בל על A ו-B:</b> אליס מבצעת מדידה מיוחדת על חלקיק A (המצב הלא ידוע) ועל חלקיק B (חלק מהזוג הסבוך). המדידה "אורגת" את המידע ממצב A עם הקשר הסבוך שבין B ל-C. תוצאת המדידה היא קלאסית לחלוטין (אחד מ-4 מצבים אפשריים של הזוג A+B הנקראים "מצבי בל"). שימו לב: המדידה *הורסת* את מצבו הקוונטי המקורי של A.</li>
        <li><b>שליחת מידע קלאסי:</b> אליס משדרת את תוצאת מדידת בל (המידע הקלאסי, 2 ביטים) לבוב, דרך ערוץ תקשורת רגיל (לא קוונטי). זהו השלב שמוגבל למהירות האור. בלי המידע הזה, בוב לא יידע מה לעשות.</li>
        <li><b>ביצוע טרנספורמציה על C:</b> בוב מקבל את תוצאת המדידה הקלאסית. בהתאם לתוצאה (אחד מ-4 סוגי מצבי בל), הוא מפעיל פעולה קוונטית (טרנספורמציה יוניטרית) ספציפית על חלקיק C. הטרנספורמציה המתאימה "משלימה" את ההשפעה של מדידת בל וגורמת למצב הקוונטי של C להיות זהה לחלוטין למצב הקוונטי ההתחלתי של A!</li>
    </ol>

    <h3>נקודות חשובות להבנה:</h3>
    <ul>
        <li><b>מצב A נעלם:</b> טלפורטציה אינה שיבוט! מצבו המקורי של חלקיק A נהרס במדידת בל. אי אפשר ליצור עותק מדויק של מצב קוונטי לא ידוע ("משפט אי-השיבוט"). המצב פשוט *עבר* מ-A ל-C.</li>
        <li><b>אין תקשורת מהירה מאור:</b> למרות שהסבוך יוצר קשר מיידי, העברת המידע הקלאסי הכרחית להשלמת התהליך. מכיוון שהמידע הקלאסי כפוף למהירות האור, לא ניתן להשתמש בטלפורטציה להעברת מידע מהר יותר ממהירות האור.</li>
        <li><b>הסבוך הוא המשאב:</b> מצב הסבוך של B ו-C הוא "הדלק" של הטלפורטציה. ללא זוג סבוך, התהליך לא אפשרי.</li>
    </ul>

    <h3>יישומים עתידיים:</h3>
    <p>טלפורטציה קוונטית היא טכנולוגיה בסיסית שתשמש לבניית "אינטרנט קוונטי", שיחבר מעבדים קוונטיים מרוחקים ויאפשר תקשורת קוונטית מאובטחת ביותר.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const particleA = document.getElementById('particleA');
    const particleB = document.getElementById('particleB');
    const particleC = document.getElementById('particleC');
    const bellMeasurementButton = document.getElementById('bell-measurement-button');
    const measurementResultDiv = document.getElementById('measurement-result');
    const classicalSignalDiv = document.getElementById('classical-signal');
    const classicalSignalPathDiv = document.getElementById('classical-signal-path');
    const classicalSignalStatusDiv = document.getElementById('classical-signal-status');
    const applyTransformationButton = document.getElementById('apply-transformation-button');
    const finalStateComparisonDiv = document.getElementById('final-state-comparison');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const resetButton = document.getElementById('reset-simulation-button');
    const entanglementLink = document.querySelector('.entanglement-link');


    // Mapping of state indices to visual representations (colors)
    // Using more distinct and vibrant colors
    const stateColors = ['#E74C3C', '#3498DB', '#2ECC71', '#F1C40F']; // Red, Blue, Green, Yellowish-Orange
    const stateNames = ['מצב 1 (אדום)', 'מצב 2 (כחול)', 'מצב 3 (ירוק)', 'מצב 4 (צהוב)'];
    const measurementOutcomes = ['תוצאה 00', 'תוצאה 01', 'תוצאה 10', 'תוצאה 11']; // Simplified Bell states

    let initialStateIndexA = -1;
    let measurementOutcomeIndex = -1;
    let simulationStep = 0; // 0: Initial, 1: Bell Measurement Done, 2: Signal Sent, 3: Transformation Done

    function initializeSimulation() {
        simulationStep = 0;

        // Randomly select an initial state for particle A
        initialStateIndexA = Math.floor(Math.random() * stateColors.length);

        // Set initial state of A with animation
        particleA.style.backgroundColor = stateColors[initialStateIndexA];
        particleA.textContent = ''; // Remove initial '?'
        particleA.classList.remove('measured', 'final-state');
        particleA.classList.add('initial-state-pulse'); // Add pulse animation

        // Reset other particles and results
        particleB.style.backgroundColor = '#ccc'; // Represent B neutrally
        particleB.textContent = 'B';
         particleB.classList.remove('measured');

        particleC.style.backgroundColor = '#ccc'; // C starts neutral/unknown relative to A's state
        particleC.textContent = 'C';
        particleC.classList.remove('initial-state-pulse', 'measured', 'final-state'); // Clean classes

        measurementResultDiv.textContent = 'תוצאת מדידה: ממתין...';
        classicalSignalStatusDiv.textContent = 'אות קלאסי: ממתין...';
        finalStateComparisonDiv.textContent = 'מצב C הסופי: ממתין...';
        finalStateComparisonDiv.style.color = '#333'; // Reset color

        // Reset buttons and signal animation
        bellMeasurementButton.disabled = false;
        applyTransformationButton.disabled = true;

        // Reset classical signal animation state
        classicalSignalDiv.style.transition = 'none';
        classicalSignalDiv.style.width = '0';
        classicalSignalDiv.style.opacity = '0';
        // Force reflow to apply width: 0 immediately
        void classicalSignalDiv.offsetWidth;

        // Reset entanglement link animation
        entanglementLink.classList.remove('active');

        // Add subtle animation to particles B and C showing entanglement
        particleB.classList.add('entangled');
        particleC.classList.add('entangled');
        entanglementLink.classList.add('active');
    }

    function performBellMeasurement() {
        if (simulationStep !== 0) return; // Only allow if in initial step
        simulationStep = 1;

        bellMeasurementButton.disabled = true;
        particleA.classList.remove('initial-state-pulse'); // Stop pulse on A
        particleB.classList.remove('entangled'); // Stop entanglement pulse on B

        // Simulate measurement outcome (randomly choose one of the 4 Bell states)
        measurementOutcomeIndex = Math.floor(Math.random() * measurementOutcomes.length);
        measurementResultDiv.textContent = `תוצאת מדידה: ${measurementOutcomes[measurementOutcomeIndex]}`;

        // Visual indication that A's state is measured/destroyed and B is part of measurement
        particleA.style.backgroundColor = '#999'; // Grey out A
        particleA.textContent = 'מצב נהרס';
        particleA.classList.add('measured');

        particleB.style.backgroundColor = '#999'; // Grey out B
        particleB.textContent = 'B'; // Keep B label
        particleB.classList.add('measured');


        // Start classical signal animation after a short delay
        setTimeout(() => {
            simulationStep = 2;
            classicalSignalStatusDiv.textContent = 'אות קלאסי: נשלח...';
            classicalSignalDiv.style.backgroundColor = '#007bff'; // Signal color
            classicalSignalDiv.style.opacity = '1';

            // Set up transition for animation
            const signalDuration = 3000; // 3 seconds
            classicalSignalDiv.style.transition = `width ${signalDuration}ms linear`;
            classicalSignalDiv.style.width = '100%';

            // Wait for the signal animation to complete before enabling next step
            classicalSignalDiv.addEventListener('transitionend', onClassicalSignalComplete, { once: true });
        }, 800); // Delay starting the signal animation
    }

    function onClassicalSignalComplete() {
        classicalSignalStatusDiv.textContent = 'אות קלאסי: התקבל';
        applyTransformationButton.disabled = false;
        simulationStep = 3;
    }

    function applyTransformationOnC() {
         if (simulationStep !== 3) return; // Only allow if signal received
        simulationStep = 4; // Transformation started

        applyTransformationButton.disabled = true;
        particleC.classList.remove('entangled'); // Stop entanglement pulse on C


        // Simulate the transformation effect on C
        // In a real scenario, the transformation applied depends on measurementOutcomeIndex.
        // The magic is that the *correct* transformation always results in C having A's original state.
        // So, for this simulation, we just transition C's state to A's initial state color.

        // Add a temporary class for the transformation animation
        particleC.classList.add('transforming');
        particleC.textContent = 'מעבד...';

        setTimeout(() => {
             particleC.classList.remove('transforming');
             particleC.style.backgroundColor = stateColors[initialStateIndexA];
             particleC.textContent = ''; // Remove 'מעבד...'
             particleC.classList.add('final-state'); // Add final state pulse

             finalStateComparisonDiv.textContent = `🎉 הצלחה! מצב C הסופי זהה למצב A המקורי! (${stateNames[initialStateIndexA]}) 🎉`;
             finalStateComparisonDiv.style.color = '#28a745'; // Highlight success message

             simulationStep = 5; // Simulation finished

             // Add a visual cue or button to restart
             // Auto-restart is off now, user needs to click Reset
        }, 1500); // Simulate transformation time
    }

    function toggleExplanation() {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר הסבר מלא';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'הצג הסבר מלא על טלפורטציה קוונטית';
        }
    }

    // Event Listeners
    bellMeasurementButton.addEventListener('click', performBellMeasurement);
    applyTransformationButton.addEventListener('click', applyTransformationOnC);
    toggleExplanationButton.addEventListener('click', toggleExplanation);
    resetButton.addEventListener('click', initializeSimulation);

    // Initialize the simulation when the page loads
    initializeSimulation();
});
</script>

<style>
/* Basic Reset/Setup */
#quantum-teleportation-app {
    font-family: 'Heebo', sans-serif; /* Use Heebo for Hebrew, fallback to sans-serif */
    direction: rtl;
    text-align: right;
    margin-top: 30px;
    padding: 25px;
    border-radius: 12px;
    background: linear-gradient(145deg, #e0e0e0, #ffffff); /* Soft gradient background */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    position: relative;
    overflow: hidden; /* Clean up potential overflow from animations */
}

/* Layout */
.locations-container {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 30px; /* Increased gap */
}

.location {
    flex: 1;
    border: 2px dashed #a0a0a0; /* More prominent dashed border */
    padding: 20px;
    border-radius: 10px;
    background-color: #ffffff;
    min-height: 300px; /* Ensure consistent height */
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center; /* Center text within location */
    box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.05);
}

.location h2 {
    margin-top: 0;
    color: #333;
    font-size: 1.4em;
    margin-bottom: 25px;
    font-weight: 700; /* Bold font */
}

.location .role {
    font-size: 0.8em;
    color: #555;
    font-weight: 400;
}

.particle-container {
    display: flex;
    align-items: center;
    margin-bottom: 20px; /* Increased margin */
    font-weight: bold;
    font-size: 1.1em;
    color: #444;
}

/* Particles */
.particle {
    width: 60px; /* Larger particles */
    height: 60px;
    border-radius: 50%;
    background-color: #ccc; /* Default neutral color */
    margin-right: 15px; /* Space after label */
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff; /* White text on color */
    font-size: 1em;
    border: 3px solid #666; /* Thicker border */
    box-sizing: border-box;
    transition: background-color 0.5s ease, border-color 0.5s ease, transform 0.3s ease; /* Smooth transitions */
    font-weight: bold;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
}

#particleA {
    border-color: #3498DB; /* Highlight A initially */
}

#particleC {
     border-color: #2ECC71; /* Highlight C as the target */
}

/* Particle Animations */
@keyframes pulse {
    0% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.05); opacity: 0.9; }
    100% { transform: scale(1); opacity: 1; }
}

.initial-state-pulse {
    animation: pulse 1.5s infinite ease-in-out;
}

.measured {
    opacity: 0.7; /* Dim measured particles */
}

.transforming {
     animation: pulse 0.8s infinite ease-in-out; /* Pulse while transforming */
     background-color: #f39c12 !important; /* Indicate processing */
     color: white;
}

.final-state {
    animation: pulse 1.5s infinite ease-in-out; /* Pulse when final state is set */
     border-color: #28a745; /* Success color border */
}


/* Action Areas (Buttons & Status) */
.action-area {
    margin-top: auto;
    text-align: center;
    width: 100%;
    padding-top: 20px;
    border-top: 1px solid #eee;
    min-height: 80px; /* Reserve space */
    display: flex;
    flex-direction: column;
    justify-content: flex-end; /* Push content to bottom */
    align-items: center;
}

.action-button {
    padding: 12px 20px; /* Larger padding */
    font-size: 1.1em;
    cursor: pointer;
    border: none;
    border-radius: 6px;
    background-color: #007bff;
    color: white;
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-weight: bold;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

.action-button:hover:not(:disabled) {
    background-color: #0056b3;
    transform: translateY(-2px); /* Subtle lift effect */
}

.action-button:active:not(:disabled) {
    transform: translateY(0); /* Press effect */
}

.action-button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
    box-shadow: none;
    transform: none;
    opacity: 0.8;
}

.status-message {
    margin-top: 15px; /* Space above status */
    font-weight: bold;
    min-height: 1.4em; /* Reserve space */
    color: #555;
    font-size: 1em;
}

#final-state-comparison {
     color: #28a745; /* Default color for comparison */
     font-size: 1.1em;
}


/* Classical Channel */
.classical-channel {
    flex-grow: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 150px; /* Wider channel area */
    text-align: center;
    margin-top: 100px; /* Adjust based on particle vertical position */
    position: relative; /* Needed for absolute positioning inside */
}

.classical-channel-label {
    font-size: 0.9em;
    color: #555;
    margin-bottom: 10px;
    font-weight: bold;
}

#classical-signal-path {
    width: 100%;
    height: 6px; /* Thicker path */
    background-color: #ddd; /* Light path background */
    border-radius: 3px;
    overflow: hidden; /* Hide signal overflow */
}

#classical-signal {
    width: 0;
    height: 100%; /* Fill path height */
    background-color: #007bff; /* Blue signal color */
    opacity: 0;
    transition: width 0s linear, opacity 0.5s ease; /* Initial state, opacity transition */
}

#classical-signal-status {
    margin-top: 10px;
    font-size: 0.9em;
    color: #555;
    min-height: 1.2em;
}

/* Entanglement Link */
.entanglement-link {
    position: absolute;
    top: calc(50% + 10px); /* Adjust to be slightly below particle center */
    left: calc(25% - 15px); /* Start near particle B */
    width: 50%; /* Span across the gap */
    height: 0; /* No height, just border */
    border-top: 3px dotted #8a2be2; /* Thicker, colored dotted line */
    z-index: -1; /* Behind particles */
    pointer-events: none; /* Don't block clicks */
    opacity: 0; /* Start hidden */
    transition: opacity 0.8s ease;
}

.entanglement-link.active {
    opacity: 1; /* Fade in when active */
}

.entanglement-label {
    position: absolute;
    top: -25px; /* Position above the link */
    left: 50%;
    transform: translateX(-50%);
    font-size: 0.8em;
    color: #8a2be2; /* Match link color */
    font-weight: bold;
    white-space: nowrap; /* Prevent line break */
}

/* Explanation Toggle Button */
#toggle-explanation, #reset-simulation-button {
    display: block;
    margin: 30px auto 20px auto; /* Center button, space above/below */
    padding: 10px 18px;
    font-size: 1em;
    cursor: pointer;
    border: none;
    border-radius: 5px;
    background-color: #6c757d;
    color: white;
    transition: background-color 0.3s ease;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

#toggle-explanation:hover:not(:disabled), #reset-simulation-button:hover:not(:disabled) {
    background-color: #5a6268;
}

/* Explanation Section */
#explanation {
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #f9f9f9;
    line-height: 1.6; /* Improved readability */
    color: #333;
}

#explanation h2, #explanation h3 {
    color: #333;
    margin-top: 20px;
    margin-bottom: 10px;
    font-weight: 700;
}

#explanation h2 {
    font-size: 1.3em;
    border-bottom: 1px solid #eee;
    padding-bottom: 5px;
}

#explanation h3 {
    font-size: 1.1em;
    color: #555;
}

#explanation ul, #explanation ol {
    margin-bottom: 15px;
    padding-right: 20px; /* Add padding for list markers */
}

#explanation li {
    margin-bottom: 8px;
    font-size: 0.95em;
}

/* Font import (Heebo from Google Fonts) */
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;700&display=swap');
</style>
```