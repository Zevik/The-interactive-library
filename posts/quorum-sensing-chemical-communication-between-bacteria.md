---
title: "קוורום סנסינג: סוד התקשורת הכימית של חיידקים"
english_slug: quorum-sensing-chemical-communication-between-bacteria
category: "מדעי החיים / ביולוגיה"
tags:
  - קוורום סנסינג
  - חיידקים
  - תקשורת כימית
  - התנהגות קולקטיבית
  - ביולוגיה מולקולרית
---
<h1>קוורום סנסינג: סוד התקשורת הכימית של חיידקים</h1>
<p>דמיינו עולם זעיר בו יצורים מיקרוסקופיים מתאמים פעולות מורכבות כלהקה - ציד משותף, בניית 'מבצרים' הגנתיים, או אפילו הארה קבוצתית בחושך. זה נשמע כמו מדע בדיוני, נכון? ובכן, זהו עולמם המרתק של החיידקים, והסוד מאחורי "ההתנהגות החברתית" שלהם טמון בכימיה. הכירו את מנגנון ה'קוורום סנסינג', שמאפשר להם לדעת בדיוק מתי יש מספיק חברים בסביבה כדי לפעול יחד.</p>

<div id="app-container">
    <div id="petri-dish">
        <div id="bacteria-container">
            <!-- Bacteria will be added here by JS -->
        </div>
         <div id="signal-visualization">
            <!-- Signal pulses will be added here by JS -->
        </div>
    </div>
    <div id="signal-indicator">
        <span>ריכוז מולקולות איתות: </span><span id="signal-concentration">0</span>
        <span class="separator">|</span>
        <span>סף קוורום: </span><span id="quorum-threshold-display">500</span>
    </div>
    <div id="controls">
        <button id="add-bacteria" class="control-button">הוסף חיידק</button>
        <button id="remove-bacteria" class="control-button">הסר חיידק</button>
        <button id="reset-sim" class="control-button">התחל מחדש</button>
    </div>
    <div id="status-message"></div>
</div>

<button id="toggle-explanation" class="toggle-button">הצג הסבר מפורט</button>

<div id="explanation" style="display: none;">
    <h2>צוללים לעומק: איך עובד קוורום סנסינג?</h2>
    <p><strong>קוורום סנסינג (Quorum Sensing, QS)</strong> הוא לא פחות ממערכת תקשורת מתוחכמת להפליא. הוא מאפשר לאוכלוסיית חיידקים כולה לתפקד כיחידה אחת, ולקבל "החלטה" משותפת מתי להפעיל גנים מסוימים - אך ורק כאשר מספרם בסביבה מספיק גדול. דמיינו קבוצת מרגלים שמחליטה לתקוף רק כשהגיע המספר המוסכם מראש (ה"קוורום").</p>

    <p><strong>השפה הכימית: מולקולות האיתות (אוטואינדוסרים)</strong></p>
    <p>החיידקים "מדברים" באמצעות מולקולות כימיות קטנות שהם מפרישים לסביבה, הנקראות <strong>אוטואינדוסרים (Autoinducers)</strong>. כל חיידק בקבוצה מייצר ומפריש ללא הרף כמות בסיסית של מולקולות כאלה, כמו שכל אדם פולט קול באופן תמידי (אפילו בנשימה). המולקולות האלה מתפזרות בסביבה החיידקית (כמו קול שמתפשט באוויר).</p>

    <p><strong>החיידק כ'סנסור' כימי</strong></p>
    <p>במקביל להפרשה, כל חיידק מצויד ב"אנטנות" - רצפטורים ספציפיים - שיודעים לזהות ולקשור בחזרה את אותן מולקולות איתות מהסביבה. הרצפטורים האלה יכולים להיות על פני קרום התא או בתוכו.</p>

    <p><strong>"ספירת ראשים" כימית: ריכוז האות</strong></p>
    <p>כשהחיידקים בודדים או מעטים, מולקולות האיתות מתפזרות במהירות בסביבה הרחבה, והריכוז שלהן בסמוך לכל חיידק נשאר נמוך. אבל ככל שאוכלוסיית החיידקים גדלה וצפופה יותר, קצב הפרשת המולקולות עולה בהתאמה, והסביבה הולכת ומתמלאת בהן. הריכוז המקומי של מולקולות האיתות עולה בצורה דרמטית. החיידק "מרגיש" את צפיפות האוכלוסייה פשוט על ידי "מדידת" ריכוז מולקולות האיתות החוזרות ונקשרות לרצפטורים שלו.</p>

    <p><strong>נקודת המפנה: סף הקוורום</strong></p>
    <p>ישנו ריכוז קריטי של מולקולות איתות - <strong>סף הקוורום</strong>. ברגע שריכוז זה נחצה, כמות מספקת של מולקולות נקשרת לרצפטורים בתוך כל תא. הקישור הזה גורם לשינוי במבנה הרצפטור ולהפעלתו.</p>

    <p><strong>הפעלת המנגנון הקבוצתי</strong></p>
    <p>הרצפטור המופעל אינו נשאר אדיש. הוא פועל כמעין "מתג מולקולרי" - לרוב, הוא נקשר ל-DNA ומפעיל שעתוק (ביטוי) של גנים ספציפיים. אלו אינם גנים לתפקוד יומיומי, אלא גנים המקודדים לחלבונים הדרושים אך ורק לביצוע פעולות הדורשות את שיתוף הפעולה של אוכלוסייה גדולה.</p>

    <p><strong>מקהלת החיידקים: דוגמאות לפעולות מתואמות</strong></p>
    <p>קוורום סנסינג שולט על מגוון רחב של התנהגויות חיידקיות קולקטיביות, שהיו לא יעילות (או אף מסוכנות) לחיידק בודד:</p>
    <ul>
        <li><strong>ביולומינסנציה (הארה):</strong> חיידקי <em>Vibrio fischeri</em> החיים בסימביוזה עם דיונונים מאירים רק כאשר ריכוזם מספיק גבוה ליצירת אור הנראה לעין.</li>
        <li><strong>ייצור רעלנים וגורמי אלימות:</strong> חיידקים פתוגניים כמו <em>Pseudomonas aeruginosa</em> מתחילים לייצר רעלנים בכמויות גדולות רק כאשר יש מספיק מהם כדי להכריע את מערכת החיסון של המאכסן.</li>
        <li><strong>בניית ביופילם:</strong> מבנים דביקים ומורכבים המכילים קהילות חיידקים עטופות במטריקס מגן (למשל, אבנית על שיניים). דורש תיאום ובנייה משותפת.</li>
        <li><strong>הפרשת אנזימים משותפת:</strong> פירוק יעיל של חומרים מורכבים בסביבה דורש כמות גדולה של אנזימים המופרשים יחד.</li>
    </ul></p>

    <p><strong>מדוע זה חשוב לחיידקים?</strong></p>
    <p>מנגנון ה-QS מעניק לחיידקים יתרון עצום באבולוציה. הוא מאפשר להם "לחסוך באנרגיה" ולא לבזבז משאבים על ייצור חלבונים יקרים (כמו רעלנים או אנזימים) כאשר הם בודדים והפעולה לא תהיה אפקטיבית. רק כשהם מגיעים למסה קריטית, הפעולה הופכת לכדאית, והם פועלים במתואם כדי לשרוד, להתחרות ולשגשג.</p>

    <p><strong>השלכות מרחיקות לכת</strong></p>
    <p>הבנת קוורום סנסינג פתחה דלתות חדשות למחקר ולפיתוח. במקום להילחם בחיידקים על ידי הריגתם (מה שמעודד עמידות לאנטיביוטיקה), ניתן לנסות לשבש את מערכת התקשורת שלהם באמצעות <strong>מעכבי קוורום סנסינג (QS Inhibitors)</strong>. כך, החיידקים עדיין חיים, אך מאבדים את היכולת לפעול כקבוצה להפרשת רעלנים או יצירת ביופילם, והופכים פחות אלימים וקלים יותר לטיפול ע"י מערכת החיסון. זוהי גישה מבטיחה במאבק בעמידות לאנטיביוטיקה.</p>
</div>

<style>
    :root {
        --petri-bg: #e0ffe0; /* Light green agar */
        --petri-border: #ccc;
        --bacteria-color-default: #3498db; /* Blue */
        --bacteria-color-quorum: #e74c3c; /* Red */
        --signal-color: rgba(52, 152, 219, 0.6); /* Semi-transparent blue */
        --signal-color-quorum: rgba(231, 76, 60, 0.8); /* Semi-transparent red */
        --control-button-bg: #2ecc71; /* Emerald green */
        --control-button-hover: #27ae60;
        --control-button-active: #229954;
        --toggle-button-bg: #bdc3c7; /* Silver */
        --toggle-button-hover: #95a5a6;
        --status-color-default: #2c3e50; /* Dark blue/gray */
        --status-color-quorum: #e74c3c; /* Red */
        --text-color: #333;
        --app-bg: #ecf0f1; /* Light gray */
    }

    #app-container {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: center;
        margin: 20px auto;
        border: 1px solid var(--petri-border);
        padding: 25px;
        border-radius: 12px;
        background-color: var(--app-bg);
        max-width: 600px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        position: relative; /* Needed for potential absolute children */
    }

    #petri-dish {
        width: 95%;
        max-width: 450px;
        aspect-ratio: 1 / 1; /* Keep it circular */
        border: 3px solid var(--petri-border);
        border-radius: 50%;
        margin: 20px auto;
        position: relative;
        overflow: hidden;
        background: radial-gradient(circle at center, var(--petri-bg) 0%, darken(var(--petri-bg), 10%) 100%);
        box-shadow: inset 0 0 15px rgba(0,0,0,0.1), 0 2px 8px rgba(0,0,0,0.15);
    }

    #bacteria-container, #signal-visualization {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none; /* Allow clicking controls behind */
    }

    .bacteria {
        position: absolute;
        width: 10px;
        height: 10px;
        background: radial-gradient(circle, var(--bacteria-color-default) 40%, darken(var(--bacteria-color-default), 15%) 100%);
        border-radius: 50%;
        transform: translate(-50%, -50%) scale(1); /* Center and initial scale */
        transition: background-color 0.5s ease, transform 0.5s ease; /* Smooth transitions */
        box-shadow: 0 0 4px rgba(0,0,0,0.3);
        animation: wiggleslightly 3s ease-in-out infinite alternate; /* Subtle movement */
    }

    @keyframes wiggleslightly {
        0% { transform: translate(-50%, -50%) rotate(0deg); }
        50% { transform: translate(-48%, -52%) rotate(2deg); }
        100% { transform: translate(-52%, -48%) rotate(-2deg); }
    }

    .bacteria.quorum {
        background: radial-gradient(circle, var(--bacteria-color-quorum) 40%, darken(var(--bacteria-color-quorum), 15%) 100%);
        transform: translate(-50%, -50%) scale(1.3); /* Bigger when quorum */
        animation: pulse-quorum 1.5s ease-in-out infinite alternate; /* More prominent pulse */
        box-shadow: 0 0 8px var(--bacteria-color-quorum); /* Add a glow */
    }

     @keyframes pulse-quorum {
        0% { transform: translate(-50%, -50%) scale(1.3); opacity: 1; }
        100% { transform: translate(-50%, -50%) scale(1.4); opacity: 0.9; }
    }

    .signal-pulse {
        position: absolute;
        width: 10px;
        height: 10px;
        background-color: var(--signal-color);
        border-radius: 50%;
        transform: translate(-50%, -50%);
        animation: signal-fade-out 1.5s ease-out forwards; /* Signal animation */
        pointer-events: none;
         z-index: 0; /* Below bacteria */
    }

     .signal-pulse.quorum {
         background-color: var(--signal-color-quorum);
         animation: signal-fade-out-quorum 1.5s ease-out forwards;
     }


    @keyframes signal-fade-out {
        0% { transform: translate(-50%, -50%) scale(1); opacity: 0.8; width: 10px; height: 10px; }
        100% { transform: translate(-50%, -50%) scale(3); opacity: 0; width: 30px; height: 30px; }
    }
     @keyframes signal-fade-out-quorum {
        0% { transform: translate(-50%, -50%) scale(1); opacity: 1; width: 12px; height: 12px; }
        100% { transform: translate(-50%, -50%) scale(4); opacity: 0; width: 48px; height: 48px; }
    }


    #signal-indicator {
        margin-top: 15px;
        padding: 10px 15px;
        background-color: #fff;
        border: 1px solid #ddd;
        border-radius: 8px;
        font-size: 0.95em;
        color: var(--text-color);
        display: inline-block;
        min-width: 280px;
    }

    #signal-indicator .separator {
        margin: 0 10px;
        color: #bbb;
    }

    #signal-concentration, #quorum-threshold-display {
        font-weight: bold;
        color: var(--bacteria-color-default);
    }
     #signal-indicator.quorum #signal-concentration, #signal-indicator.quorum #quorum-threshold-display {
        color: var(--bacteria-color-quorum);
     }


    #controls {
        margin-top: 20px;
        display: flex;
        justify-content: center;
        flex-wrap: wrap; /* Allow wrapping on small screens */
        gap: 10px; /* Spacing between buttons */
    }

    .control-button {
        padding: 12px 20px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: var(--control-button-bg);
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.15);
    }

    .control-button:hover {
        background-color: var(--control-button-hover);
    }

    .control-button:active {
        background-color: var(--control-button-active);
        transform: scale(0.98);
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    #status-message {
        margin-top: 20px;
        font-weight: bold;
        min-height: 1.5em; /* Reserve space */
        color: var(--status-color-default);
        transition: color 0.5s ease;
    }
     #status-message.quorum {
         color: var(--status-color-quorum);
     }


    .toggle-button {
        display: block;
        margin: 30px auto 20px auto;
        padding: 12px 25px;
        font-size: 1em;
        cursor: pointer;
        border: 1px solid #ccc;
        border-radius: 6px;
        background-color: var(--toggle-button-bg);
        color: var(--text-color);
        transition: background-color 0.3s ease, border-color 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .toggle-button:hover {
        background-color: var(--toggle-button-hover);
        border-color: #a0a0a0;
    }

     .toggle-button:active {
        transform: scale(0.98);
     }


    #explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: 10px;
        background-color: #fff;
        text-align: right;
        direction: rtl;
        line-height: 1.7;
        color: var(--text-color);
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }

    #explanation h2 {
        text-align: center;
        margin-bottom: 20px;
        color: #333;
        font-size: 1.8em;
    }

    #explanation p {
        margin-bottom: 15px;
    }

     #explanation strong {
         color: #555;
     }

     #explanation ul {
        margin-bottom: 15px;
        padding-right: 25px;
     }

     #explanation li {
        margin-bottom: 8px;
     }

     /* Responsive adjustments */
    @media (max-width: 500px) {
        #app-container {
            padding: 15px;
        }
         #petri-dish {
             margin: 15px auto;
         }
        #controls {
            flex-direction: column;
            align-items: center;
        }
        .control-button {
             width: 80%;
        }
        #signal-indicator {
            font-size: 0.85em;
             min-width: unset;
        }
    }


</style>

<script>
    const petriDish = document.getElementById('petri-dish');
    const bacteriaContainer = document.getElementById('bacteria-container');
     const signalVisualization = document.getElementById('signal-visualization');
    const signalIndicator = document.getElementById('signal-indicator');
    const signalConcentrationSpan = document.getElementById('signal-concentration');
    const quorumThresholdDisplay = document.getElementById('quorum-threshold-display');
    const addBacteriaButton = document.getElementById('add-bacteria');
    const removeBacteriaButton = document.getElementById('remove-bacteria');
    const resetSimButton = document.getElementById('reset-sim');
    const statusMessageDiv = document.getElementById('status-message');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    let bacteriaCount = 0;
    let signalConcentration = 0;
    const QUORUM_THRESHOLD = 800; // Increased threshold slightly for visual buildup
    const SIGNAL_PRODUCTION_RATE_PER_BACTERIA = 1.5; // Signal added per bacteria per step
    const SIGNAL_DECAY_RATE = 0.97; // Percentage remaining each step (slightly slower decay)
    const SIMULATION_INTERVAL = 80; // ms between simulation steps (faster updates)
    const SIGNAL_PULSE_INTERVAL = 300; // ms between visual signal pulses from each bacteria
    let simulationIntervalId;
    let signalPulseIntervalId;
    const MAX_BACTERIA = 150; // Allow more bacteria
    const MAX_SIGNAL_PULSES = 200; // Limit number of visual pulses for performance

     // Object to store bacteria elements and their positions for signal visualization
    const bacteriaElements = [];


    quorumThresholdDisplay.textContent = QUORUM_THRESHOLD;

    function addBacteria() {
        if (bacteriaCount < MAX_BACTERIA) {
            bacteriaCount++;
            const bacteriaElement = document.createElement('div');
            bacteriaElement.classList.add('bacteria');

            // Random position within the petri dish circle
            const petriDishSize = petriDish.offsetWidth;
            const center = petriDishSize / 2;
            const maxRadius = center - 15; // Padding from edge
            let angle = Math.random() * 2 * Math.PI;
            let radius = Math.random() * maxRadius;
            let x = center + radius * Math.cos(angle);
            let y = center + radius * Math.sin(angle);

            bacteriaElement.style.left = `${x}px`;
            bacteriaElement.style.top = `${y}px`;

            bacteriaContainer.appendChild(bacteriaElement);
            bacteriaElements.push({ element: bacteriaElement, x: x, y: y }); // Store for signal pulses

            updateStatus();
            startSimulation(); // Ensure simulation is running
            startSignalPulseVisuals(); // Ensure signal visuals are running
        } else {
            statusMessageDiv.textContent = `הגענו למספר החיידקים המקסימלי (${MAX_BACTERIA}).`;
        }
    }

    function removeBacteria() {
        if (bacteriaCount > 0) {
            bacteriaCount--;
            const lastBacteria = bacteriaContainer.lastChild;
            if (lastBacteria) {
                bacteriaContainer.removeChild(lastBacteria);
                 bacteriaElements.pop(); // Remove from the array
            }
            updateStatus();
            if (bacteriaCount === 0) {
                stopSimulation();
                stopSignalPulseVisuals();
                signalConcentration = 0;
                updateSignalDisplay();
            }
        } else {
             statusMessageDiv.textContent = 'אין חיידקים להסרה.';
        }
    }

    function updateStatus() {
        const quorumMet = signalConcentration >= QUORUM_THRESHOLD && bacteriaCount > 0;

        if (quorumMet) {
            statusMessageDiv.textContent = 'הקוורום הושג! החיידקים מתאמים פעולה...';
            statusMessageDiv.classList.add('quorum');
             signalIndicator.classList.add('quorum');
            bacteriaContainer.querySelectorAll('.bacteria').forEach(b => b.classList.add('quorum'));

        } else if (bacteriaCount > 0) {
             statusMessageDiv.textContent = `ישנם ${bacteriaCount} חיידקים. ריכוז האות עולה... מחכים לקוורום (${Math.round(signalConcentration)}/${QUORUM_THRESHOLD}).`;
             statusMessageDiv.classList.remove('quorum');
             signalIndicator.classList.remove('quorum');
             bacteriaContainer.querySelectorAll('.bacteria').forEach(b => b.classList.remove('quorum'));
        } else {
            statusMessageDiv.textContent = 'הוסף חיידקים כדי להתחיל את הסימולציה.';
             statusMessageDiv.classList.remove('quorum');
             signalIndicator.classList.remove('quorum');
             bacteriaContainer.querySelectorAll('.bacteria').forEach(b => b.classList.remove('quorum'));
        }
    }

    function updateSignalDisplay() {
        signalConcentrationSpan.textContent = Math.round(signalConcentration);
         // Update status message if only concentration changes (e.g., decay below threshold)
         if (bacteriaCount > 0) {
            updateStatus();
         }
    }

    function simulateStep() {
        // Signal production: each bacteria adds signal
        signalConcentration += bacteriaCount * SIGNAL_PRODUCTION_RATE_PER_BACTERIA;

        // Signal decay: simulates diffusion/breakdown
        signalConcentration *= SIGNAL_DECAY_RATE;

        // Prevent concentration from becoming negative
        signalConcentration = Math.max(0, signalConcentration);

        updateSignalDisplay();
    }

     function emitSignalPulseVisuals() {
         const quorumMet = signalConcentration >= QUORUM_THRESHOLD && bacteriaCount > 0;
         const pulseClass = quorumMet ? 'signal-pulse quorum' : 'signal-pulse';

         // Limit the number of visible pulses for performance
         const currentPulses = signalVisualization.childElementCount;
         const pulsesToRemove = currentPulses + bacteriaElements.length - MAX_SIGNAL_PULSES;
         if (pulsesToRemove > 0) {
             for(let i = 0; i < pulsesToRemove; i++) {
                 if (signalVisualization.firstChild) {
                     signalVisualization.removeChild(signalVisualization.firstChild);
                 }
             }
         }


         // Create a signal pulse element for each bacteria
         bacteriaElements.forEach(b => {
             const pulse = document.createElement('div');
             pulse.className = pulseClass;
             pulse.style.left = `${b.x}px`;
             pulse.style.top = `${b.y}px`;
             signalVisualization.appendChild(pulse);

             // Remove the pulse element after its animation finishes
             pulse.addEventListener('animationend', () => {
                 pulse.remove();
             });
         });
     }


    function startSimulation() {
        if (!simulationIntervalId) {
            simulationIntervalId = setInterval(simulateStep, SIMULATION_INTERVAL);
        }
    }

    function stopSimulation() {
        clearInterval(simulationIntervalId);
        simulationIntervalId = null;
    }

     function startSignalPulseVisuals() {
        if (!signalPulseIntervalId) {
             signalPulseIntervalId = setInterval(emitSignalPulseVisuals, SIGNAL_PULSE_INTERVAL);
        }
     }

     function stopSignalPulseVisuals() {
        clearInterval(signalPulseIntervalId);
        signalPulseIntervalId = null;
     }


    function resetSimulation() {
        stopSimulation();
        stopSignalPulseVisuals();
        bacteriaCount = 0;
        signalConcentration = 0;
        bacteriaContainer.innerHTML = ''; // Remove all bacteria elements
        signalVisualization.innerHTML = ''; // Remove all signal pulses
        bacteriaElements.length = 0; // Clear the array
        updateSignalDisplay();
        updateStatus();
        statusMessageDiv.textContent = 'הסימולציה אופסה. הוסף חיידקים כדי להתחיל.';
    }


    addBacteriaButton.addEventListener('click', addBacteria);
    removeBacteriaButton.addEventListener('click', removeBacteria);
    resetSimButton.addEventListener('click', resetSimulation);

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מפורט' : 'הצג הסבר מפורט';
    });

    // Initial state
    updateStatus(); // Sets initial status message

</script>