---
title: "אפקט דופלר: איך צלילים משתנים בתנועה?"
english_slug: doppler-effect-how-sounds-change-motion
category: "מדעים מדויקים / פיזיקה"
tags:
  - אפקט דופלר
  - גלים
  - תנועה יחסית
  - צליל
  - פיזיקה
---
# אפקט דופלר: איך צלילים משתנים בתנועה?

שמעתם פעם את הצליל המסתורי הזה של אמבולנס חולף, שמשנה את גובהו מרגע לרגע? זו לא אשליה! זו תופעת טבע מדהימה שנקראת אפקט דופלר, והיא מספרת לנו איך תנועה פשוטה יכולה לעוות את התדירות של גלים – מצליל יום-יומי ועד אור מכוכבים רחוקים. בואו נחקור יחד!

<div id="doppler-app">
    <div class="controls">
        <h2>סימולציית אפקט דופלר אינטראקטיבית</h2>
        <p class="instructions">גרור את העיגולים האדום (מקור) והירוק (צופה) על הקנבס כדי להזיז אותם ולשנות את מהירותם! או השתמש בפקדים מטה.</p>
         <div class="param-group">
            <h3>תרחישים מוגדרים מראש</h3>
            <select id="preset-scenario">
                <option value="custom">תרחיש מותאם אישית</option>
                <option value="source-towards-static">מקור מתקרב לצופה נייח</option>
                <option value="source-away-static">מקור מתרחק מצופה נייח</option>
                <option value="observer-towards-static-source">צופה מתקרב למקור נייח</option>
                <option value="observer-away-static-source">צופה מתרחק ממקור נייח</option>
                <option value="source-pass-by-observer">מקור חולף על פני צופה</option>
                <option value="observer-pass-by-source">צופה חולף על פני מקור</option>
                 <option value="supersonic-source">מקור על-קולי (הלם גל)</option>
            </select>
        </div>
        <div class="param-group">
            <h3>מקור הקול (אדום)</h3>
            <div>
                <label for="source-freq">תדירות מקורית (Hz):</label>
                <input type="number" id="source-freq" value="300" min="50" max="1000" step="10">
            </div>
            <div>
                <label for="source-vel-x">מהירות X (יח'/שניה):</label>
                <input type="number" id="source-vel-x" value="0" step="1" min="-150" max="150">
            </div>
             <div>
                <label for="source-vel-y">מהירות Y (יח'/שניה):</label>
                <input type="number" id="source-vel-y" value="0" step="1" min="-150" max="150">
            </div>
        </div>
        <div class="param-group">
            <h3>צופה (ירוק)</h3>
             <div>
                <label for="observer-vel-x">מהירות X (יח'/שניה):</label>
                <input type="number" id="observer-vel-x" value="0" step="1" min="-150" max="150">
            </div>
             <div>
                <label for="observer-vel-y">מהירות Y (יח'/שניה):</label>
                <input type="number" id="observer-vel-y" value="0" step="1" min="-150" max="150">
            </div>
        </div>
         <div class="param-group">
            <h3>סביבה</h3>
             <div>
                <label for="wave-speed">מהירות גל (יח'/שניה):</label>
                <input type="number" id="wave-speed" value="100" min="50" max="300" step="10">
            </div>
        </div>

        <div class="status">
            <p>תדירות מקורית: <span id="original-freq-display">300 Hz</span></p>
            <p>תדירות נצפית: <span id="observed-freq-display">? Hz</span></p>
        </div>
         <button id="reset-button">איפוס מיקום והגדרות</button>
    </div>
    <div class="canvas-container">
        <canvas id="doppler-canvas"></canvas>
    </div>
</div>

<style>
/* General App Styling */
#doppler-app {
    display: flex;
    flex-wrap: wrap;
    gap: 25px; /* Increased gap */
    margin-bottom: 40px; /* More space below */
    font-family: 'Arial', sans-serif; /* Modern font */
    background-color: #eef2f7; /* Light blue background */
    padding: 25px; /* Increased padding */
    border-radius: 12px; /* More rounded corners */
    box-shadow: 0 4px 15px rgba(0,0,0,0.1); /* Stronger shadow */
    align-items: flex-start; /* Align items to the top */
}

/* Controls Panel Styling */
#doppler-app .controls {
    flex: 1;
    min-width: 300px; /* Slightly wider minimum */
    background-color: #ffffff; /* White background */
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    display: flex; /* Use flex for internal layout */
    flex-direction: column;
    gap: 15px; /* Space between control groups */
}

#doppler-app .controls h2 {
    margin-top: 0;
    color: #1a237e; /* Dark blue heading */
    border-bottom: 2px solid #e0e0e0; /* Thicker, lighter border */
    padding-bottom: 12px;
    font-size: 1.6em; /* Larger heading */
    text-align: center;
}

#doppler-app .instructions {
    text-align: center;
    color: #555;
    font-size: 0.9em;
    margin-bottom: 20px;
}

#doppler-app .controls .param-group {
    margin-bottom: 0; /* Remove bottom margin here, gap handles spacing */
    padding-bottom: 15px;
    border-bottom: 1px dashed #cfd8dc; /* Lighter dashed border */
}

#doppler-app .controls .param-group:last-child {
     border-bottom: none; /* No border for the last group */
     padding-bottom: 0;
}


#doppler-app .controls .param-group h3 {
    margin-top: 0;
    margin-bottom: 12px; /* Space below subheading */
    color: #3949ab; /* Medium blue subheading */
    font-size: 1.2em; /* Slightly larger subheading */
    border-left: 4px solid #5c6bc0; /* Accent border */
    padding-left: 8px;
}

#doppler-app .controls .param-group div {
    margin-bottom: 12px; /* Space between input lines */
    display: flex; /* Use flex for label/input alignment */
    align-items: center;
    gap: 10px; /* Space between label and input */
}

#doppler-app .controls label {
    flex-basis: 160px; /* Fixed width for labels */
    font-weight: bold;
    color: #455a64; /* Dark grey label color */
    font-size: 1em;
}

#doppler-app .controls input[type="number"],
#doppler-app .controls select {
    flex-grow: 1; /* Allow input/select to take remaining space */
    padding: 8px; /* More padding */
    border: 1px solid #b0bec5; /* Lighter border */
    border-radius: 5px; /* Slightly more rounded */
    font-size: 1em;
    box-sizing: border-box; /* Include padding and border in element's total width and height */
}

#doppler-app .controls .status {
    margin-top: 20px;
    padding-top: 15px;
    border-top: 2px solid #e0e0e0; /* Match heading border */
    font-size: 1.2em; /* Larger status text */
    color: #1a237e; /* Dark blue status text */
    text-align: center;
}

#doppler-app .controls .status p {
    margin: 8px 0; /* More space between status lines */
}

#doppler-app .controls .status span {
    font-weight: bold;
    color: #007bff; /* Blue color for values */
}

#doppler-app .controls #reset-button {
    display: block;
    width: 100%;
    padding: 12px; /* More padding */
    background-color: #ff9800; /* Orange color */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1.1em; /* Larger font */
    margin-top: 20px; /* More space above button */
    transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transition */
    box-shadow: 0 2px 5px rgba(0,0,0,0.2); /* Add button shadow */
}

#doppler-app .controls #reset-button:hover {
    background-color: #f57c00; /* Darker orange on hover */
}

#doppler-app .controls #reset-button:active {
    transform: scale(0.98); /* Slightly shrink on click */
}

/* Canvas Container Styling */
#doppler-app .canvas-container {
    flex: 2;
    min-width: 350px; /* Wider minimum canvas */
    background-color: #ffffff; /* White background */
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden; /* Prevent waves from drawing outside */
    position: relative; /* Needed for absolute positioning if adding UI elements */
}

#doppler-canvas {
    width: 100%;
    height: 450px; /* Slightly taller canvas */
    background: linear-gradient(to bottom, #e3f2fd, #bbdefb); /* Light blue gradient background */
    border-radius: 10px;
    display: block; /* Remove extra space below canvas */
    cursor: grab; /* Indicate canvas is interactive */
}

#doppler-canvas.dragging {
    cursor: grabbing;
}

/* Explanation Section Styling */
#toggle-explanation {
    display: block;
    margin: 30px auto; /* More space above/below */
    padding: 12px 25px; /* More padding */
    background-color: #4caf50; /* Green color */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1.1em;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

#toggle-explanation:hover {
    background-color: #388e3c; /* Darker green on hover */
}

#toggle-explanation:active {
    transform: scale(0.98);
}

#explanation {
    margin-top: 20px;
    padding: 25px;
    background-color: #ffffff; /* White background */
    border: 1px solid #e0e0e0; /* Light border */
    border-radius: 8px;
    display: none; /* Hidden by default */
    font-family: 'Arial', sans-serif;
    line-height: 1.7; /* Improved readability */
    color: #333;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

#explanation h2, #explanation h3 {
    color: #1a237e; /* Dark blue headings */
    margin-top: 25px; /* More space above headings */
    margin-bottom: 12px;
}

#explanation h2 {
    border-bottom: 1px solid #e0e0e0;
    padding-bottom: 8px;
}


#explanation p {
    margin-bottom: 18px; /* More space between paragraphs */
}

#explanation ul {
    margin-bottom: 18px;
    padding-left: 25px; /* More padding */
}

#explanation li {
    margin-bottom: 10px; /* More space between list items */
}

#explanation strong {
    color: #555; /* Darker color for strong text */
}

/* Responsive adjustments */
@media (max-width: 768px) {
    #doppler-app {
        flex-direction: column;
        gap: 20px;
        padding: 15px;
    }

    #doppler-app .controls,
    #doppler-app .canvas-container {
        min-width: unset;
        width: 100%;
    }

    #doppler-canvas {
        height: 300px; /* Shorter canvas on small screens */
    }

    #doppler-app .controls label {
        flex-basis: 120px; /* Adjust label width */
    }
}

</style>

<button id="toggle-explanation">הצג/הסתר הסבר והנוסחה</button>

<div id="explanation">
    <h2>מהו אפקט דופלר? הצליל שמשנה את פניו בתנועה</h2>
    <p>דמיינו את עצמכם עומדים ברחוב ושומעים סירנה של אמבולנס מתקרב. הצליל נשמע גבוה וחד, אך ברגע שהאמבולנס חולף על פניכם ומתחיל להתרחק, גובה הצליל צונח באופן דרמטי. התופעה הזו, שמרגישה כמעט קסומה, היא דוגמה קלאסית לאפקט דופלר – עיקרון פיזיקלי שמסביר איך תנועה יחסית בין מקור גל לצופה משפיעה על התדירות שאנו קולטים.</p>
    <p>אפקט דופלר גורם לשינוי בתדירות הנצפית: התדירות נראית (או נשמעת) גבוהה יותר כשהמקור והצופה מתקרבים זה לזה, ונמוכה יותר כשהם מתרחקים. זה נכון לא רק לצליל, אלא לכל סוג של גל – כולל גלי אור, גלי רדיו ואפילו גלי מים!</p>

    <h2>הסבר פיזיקלי: למה זה קורה?</h2>
    <p>חשבו על מקור קול נייח: הוא שולח גלי קול לכל הכיוונים באופן שווה, כמו אדוות מעגליות שמתפשטות באגם שקט. המרחק בין כל שיא גל לשיא הבא (אורך הגל) זהה בכל הכיוונים.</p>
    <p>עכשיו, דמיינו שהמקור מתחיל לנוע. הוא עדיין שולח גלים בתדירות קבועה, אבל כל גל חדש נפלט מנקודת מוצא אחרת! הגלים הנפלטים בכיוון שאליו המקור נע "נדחסים" – המרחק ביניהם קטן. חשבו על זה כמו דחיפת קפיץ. לעומת זאת, הגלים הנפלטים בכיוון ההפוך לתנועה "נמתחים" – המרחק ביניהם גדל, כמו מתיחת קפיץ.</p>
    <p>מהירות הגל בסביבה (למשל, מהירות הקול באוויר) נשארת קבועה (בהנחה שהאוויר נייח). מכיוון שמהירות = תדירות × אורך גל, שינוי באורך הגל חייב לגרום לשינוי בתדירות הנצפית. אורך גל קטן פירושו תדירות נצפית גבוהה יותר (צליל גבוה), ואורך גל גדול פירושו תדירות נצפית נמוכה יותר (צליל נמוך).</p>

    <h2>ומה קורה כשהצופה זז?</h2>
    <p>גם לתנועת הצופה יש השפעה! אם הצופה נע לכיוון מקור נייח, הוא פוגש את שיאי הגלים בתדירות גבוהה יותר מאשר לו היה נייח – הוא "אוסף" יותר גלים ביחידת זמן. אם הוא מתרחק מהמקור, הוא פוגש פחות שיאי גלים ביחידת זמן, והתדירות הנצפית נמוכה יותר.</p>
    <p>אפקט דופלר נובע למעשה מהתנועה ה<strong>יחסית</strong> בין המקור לצופה, ומהירות הגל בתווך.</p>

    <h2>הנוסחה המתמטית של אפקט דופלר</h2>
    <p>עבור גלי קול הנעים בתווך נייח (כמו אוויר ללא רוח), כאשר גם המקור וגם הצופה עשויים לנוע, התדירות הנצפית ($f_o$) ניתנת על ידי הנוסחה הכללית:</p>
    <p>$$f_o = f_s \left( \frac{v + v_o}{v - v_s} \right)$$</p>
    <p>כאשר:</p>
    <ul>
        <li>$f_s$ היא התדירות המקורית של הגל כפי שנפלטת מהמקור (תדירות המקור).</li>
        <li>$v$ היא מהירות הגל בתווך (למשל, מהירות הקול באוויר).</li>
        <li>$v_o$ היא מהירות הצופה <strong>ביחס לתווך</strong>. הסימן של $v_o$ הוא חיובי אם הצופה נע <strong>לכיוון</strong> המקור, ושלילי אם הוא נע <strong>הרחק</strong> מהמקור.</li>
        <li>$v_s$ היא מהירות המקור <strong>ביחס לתווך</strong>. הסימן של $v_s$ הוא חיובי אם המקור נע <strong>לכיוון</strong> הצופה, ושלילי אם הוא נע <strong>הרחק</strong> מהצופה.</li>
    </ul>
    <p><strong>הבהרה חשובה:</strong> הנוסחה לעיל תקפה כאשר התנועה של המקור והצופה היא אך ורק <strong>לאורך הקו הישר</strong> המחבר ביניהם. בסימולציה הדו-ממדית שלנו, חישוב התדירות הנצפית בכל רגע נתון מתבסס על <strong>רכיבי המהירות</strong> של המקור והצופה המקבילים לקו המחבר ביניהם באותו רגע.</p>
     <p><strong>מקרה מיוחד: הלם גל (Shockwave)</strong> כאשר מקור הקול נע מהר יותר ממהירות הגל בתווך ($v_s > v$), הגלים "נערמים" זה על זה ויוצרים חזית גל חזקה וקונית המכונה "חרוט מאך". זו התופעה שגורמת ל"בום על-קולי" של מטוסים שטסים מהר יותר מהקול. הסימולציה מסוגלת להציג את היווצרות חרוט המאך בתרחישים על-קוליים.</p>

    <h2>מעבר לצליל: יישומים מרתקים של אפקט דופלר</h2>
    <p>אפקט דופלר הוא כלי רב עוצמה בפיזיקה ובהנדסה:</p>
    <ul>
        <li><strong>אסטרונומיה:</strong> מדידת מהירות כוכבים וגלקסיות! אור שמגיע מכוכב שמתקרב אלינו מראה "הסטה לכחול" (Blue Shift - תדירות גבוהה), ואור מכוכב שמתרחק מראה "הסטה לאדום" (Red Shift - תדירות נמוכה). גילוי ההסטה לאדום בגלקסיות רחוקות הוא אחת ההוכחות המרכזיות לכך שהיקום מתפשט!</li>
        <li><strong>רדאר ומכ"ם:</strong> משטרת התנועה, מטאורולוגים ובקרת טיסה משתמשים באפקט דופלר במכשירי רדאר כדי למדוד את מהירות המטרה (מכונית, ענן גשם, מטוס) על ידי ניתוח שינוי התדירות בגלי הרדיו המוחזרים.</li>
        <li><strong>אולטרסאונד רפואי:</strong> בבדיקות אולטרסאונד דופלר, משתמשים בשינוי תדירות גלי קול המוחזרים מכדוריות דם כדי למדוד את מהירות זרימת הדם בעורקים ובוורידים.</li>
    </ul>
    <p>אז בפעם הבאה שתשמעו צליל שמשנה את גובהו, זכרו שאתם עדים לאפקט דופלר בפעולה – תזכורת מרתקת לכוחה של תנועה יחסית בעולם הגלים!</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('doppler-canvas');
    const ctx = canvas.getContext('2d');
    const sourceFreqInput = document.getElementById('source-freq');
    const sourceVelXInput = document.getElementById('source-vel-x');
    const sourceVelYInput = document.getElementById('source-vel-y');
    const observerVelXInput = document.getElementById('observer-vel-x');
    const observerVelYInput = document.getElementById('observer-vel-y');
    const waveSpeedInput = document.getElementById('wave-speed');
    const originalFreqDisplay = document.getElementById('original-freq-display');
    const observedFreqDisplay = document.getElementById('observed-freq-display');
    const resetButton = document.getElementById('reset-button');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const presetScenarioSelect = document.getElementById('preset-scenario');


    let animationFrameId = null;

    // Simulation parameters
    let source = { x: 0, y: 0, vx: 0, vy: 0 };
    let observer = { x: 0, y: 0, vx: 0, vy: 0 };
    let sourceFreq = 300; // Hz
    let waveSpeed = 100; // units per second
    const timeStep = 1 / 60; // seconds per frame (assuming 60 fps)
    let time = 0; // simulation time

    // Waves: store origin point and time of emission
    const waves = [];
    let lastWaveTime = 0;

    // Dragging state
    let isDraggingSource = false;
    let isDraggingObserver = false;
    let dragStartX = 0;
    let dragStartY = 0;
    let lastSourceX = 0;
    let lastSourceY = 0;
    let lastObserverX = 0;
    let lastObserverY = 0;


    // Presets definition
    const presets = {
        "custom": { sourceVelX: 0, sourceVelY: 0, observerVelX: 0, observerVelY: 0 },
        "source-towards-static": { sourceVelX: 50, sourceVelY: 0, observerVelX: 0, observerVelY: 0, initialPositions: 'source-left' },
        "source-away-static": { sourceVelX: -50, sourceVelY: 0, observerVelX: 0, observerVelY: 0, initialPositions: 'source-right' },
        "observer-towards-static-source": { sourceVelX: 0, sourceVelY: 0, observerVelX: -50, observerVelY: 0, initialPositions: 'observer-right' },
        "observer-away-static-source": { sourceVelX: 0, sourceVelY: 0, observerVelX: 50, observerVelY: 0, initialPositions: 'observer-left' },
        "source-pass-by-observer": { sourceVelX: 50, sourceVelY: 0, observerVelX: 0, observerVelY: 0, initialPositions: 'source-far-left' },
        "observer-pass-by-source": { sourceVelX: 0, sourceVelY: 0, observerVelX: -50, observerVelY: 0, initialPositions: 'observer-far-right' },
         "supersonic-source": { sourceVelX: 150, sourceVelY: 0, observerVelX: 0, observerVelY: 0, initialPositions: 'source-far-left', waveSpeed: 100, sourceFreq: 200}
    };


    // Initial setup
    resizeCanvas();
    loadPreset('custom'); // Load initial values from inputs
    resetPositions(); // Set initial positions after loading values
    updateDisplays();

    // Event Listeners
    sourceFreqInput.addEventListener('input', updateParameters);
    sourceVelXInput.addEventListener('input', updateParameters);
    sourceVelYInput.addEventListener('input', updateParameters);
    observerVelXInput.addEventListener('input', updateParameters);
    observerVelYInput.addEventListener('input', updateParameters);
    waveSpeedInput.addEventListener('input', updateParameters);
    resetButton.addEventListener('click', resetPositions);
    presetScenarioSelect.addEventListener('change', (event) => {
        loadPreset(event.target.value);
        resetPositions(); // Reset positions specific to preset if needed
    });

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
    });

    window.addEventListener('resize', () => {
        resizeCanvas();
        resetPositions(); // Reset positions to be centered on the new canvas size
    });

    // Canvas Dragging Event Listeners
    canvas.addEventListener('mousedown', startDrag);
    canvas.addEventListener('mousemove', drag);
    canvas.addEventListener('mouseup', endDrag);
    canvas.addEventListener('mouseout', endDrag); // End drag if mouse leaves canvas

    canvas.addEventListener('touchstart', startDrag);
    canvas.addEventListener('touchmove', drag);
    canvas.addEventListener('touchend', endDrag);
    canvas.addEventListener('touchcancel', endDrag);


    function resizeCanvas() {
        const container = canvas.parentElement;
        canvas.width = container.clientWidth;
        canvas.height = 450; // Keep height fixed as defined in CSS
        // Positions will be relative to the new size in resetPositions
    }

    function loadPreset(presetName) {
        const preset = presets[presetName];
        if (preset) {
            // Update input values first
            sourceVelXInput.value = preset.sourceVelX;
            sourceVelYInput.value = preset.sourceVelY;
            observerVelXInput.value = preset.observerVelX;
            observerVelYInput.value = preset.observerVelY;
            if (preset.waveSpeed !== undefined) waveSpeedInput.value = preset.waveSpeed;
            if (preset.sourceFreq !== undefined) sourceFreqInput.value = preset.sourceFreq;

            // Then update simulation parameters from inputs
            updateParameters();

            // Store initial position type for reset
            canvas.dataset.initialPositionType = preset.initialPositions || 'default';
        } else {
            // If custom, just update parameters from current input values
             updateParameters();
             canvas.dataset.initialPositionType = 'default';
        }
    }


    function resetPositions() {
        const currentWidth = canvas.width;
        const currentHeight = canvas.height;

        const initialPositionType = canvas.dataset.initialPositionType || 'default';

        switch (initialPositionType) {
            case 'source-left':
                 source.x = currentWidth * 0.1; source.y = currentHeight * 0.5;
                 observer.x = currentWidth * 0.8; observer.y = currentHeight * 0.5;
                 break;
            case 'source-right':
                 source.x = currentWidth * 0.9; source.y = currentHeight * 0.5;
                 observer.x = currentWidth * 0.2; observer.y = currentHeight * 0.5;
                 break;
             case 'observer-right':
                 source.x = currentWidth * 0.2; source.y = currentHeight * 0.5;
                 observer.x = currentWidth * 0.9; observer.y = currentHeight * 0.5;
                 break;
            case 'observer-left':
                 source.x = currentWidth * 0.8; source.y = currentHeight * 0.5;
                 observer.x = currentWidth * 0.1; observer.y = currentHeight * 0.5;
                 break;
            case 'source-far-left': // For pass-by or supersonic
                 source.x = currentWidth * 0.05; source.y = currentHeight * 0.5;
                 observer.x = currentWidth * 0.5; observer.y = currentHeight * 0.5;
                 break;
            case 'observer-far-right': // For pass-by
                 source.x = currentWidth * 0.5; source.y = currentHeight * 0.5;
                 observer.x = currentWidth * 0.95; observer.y = currentHeight * 0.5;
                 break;
            case 'default':
            default:
                // Center source on left, observer on right
                source.x = currentWidth * 0.25;
                source.y = currentHeight * 0.5;
                observer.x = currentWidth * 0.75;
                observer.y = currentHeight * 0.5;
                break;
        }


        // Reset velocities from inputs (which were potentially set by preset)
        source.vx = parseFloat(sourceVelXInput.value);
        source.vy = parseFloat(sourceVelYInput.value);
        observer.vx = parseFloat(observerVelXInput.value);
        observer.vy = parseFloat(observerVelYInput.value);

        waves.length = 0; // Clear existing waves
        time = 0; // Reset simulation time
        lastWaveTime = 0; // Reset wave emission time
        lastSourceX = source.x; // Initialize last positions for dragging velocity calc
        lastSourceY = source.y;
        lastObserverX = observer.x;
        lastObserverY = observer.y;
        updateDisplays(); // Update displays based on new positions/velocities
    }


    function updateParameters() {
        sourceFreq = parseFloat(sourceFreqInput.value);
        source.vx = parseFloat(sourceVelXInput.value);
        source.vy = parseFloat(sourceVelYInput.value);
        observer.vx = parseFloat(observerVelXInput.value);
        observer.vy = parseFloat(observerVelYInput.value);
        waveSpeed = parseFloat(waveSpeedInput.value);

        if (waveSpeed <= 0) waveSpeed = 0.1; // Prevent division by zero or negative speed
        if (sourceFreq <= 0) sourceFreq = 1; // Prevent division by zero

        updateDisplays();

        // If preset is custom, update select dropdown
        if (presetScenarioSelect.value !== 'custom') {
             presetScenarioSelect.value = 'custom';
        }
    }

    function updateDisplays() {
        originalFreqDisplay.textContent = `${sourceFreq.toFixed(1)} Hz`;

        // Calculate observed frequency
        // Need vector from source to observer
        const dx = observer.x - source.x;
        const dy = observer.y - source.y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        let observedFreq = sourceFreq; // Default if no motion or distance is zero

        if (dist > 5) { // Avoid division by near zero distance, use a small threshold
            // Unit vector from source to observer
            const ux = dx / dist;
            const uy = dy / dist;

            // Project source and observer velocities onto the line of sight (source to observer)
            // v_s_radial = component of source velocity ALONG S->O vector
            // v_o_radial = component of observer velocity ALONG S->O vector
            const v_s_radial = source.vx * ux + source.vy * uy; // Positive if source moves towards observer
            const v_o_radial = observer.vx * ux + observer.vy * uy; // Positive if observer moves towards source

            // Doppler formula: f_o = f_s * (v + v_o_radial) / (v - v_s_radial)
            // v_o_radial is observer velocity component TOWARDS source (+ve)
            // v_s_radial is source velocity component TOWARDS observer (+ve)
            // Formula is f_o = f_s * (v_wave + v_observer_towards_source) / (v_wave - v_source_towards_observer)
            // Our v_o_radial is observer towards source
            // Our v_s_radial is source towards observer
            // Formula becomes f_o = f_s * (v_wave + v_o_radial) / (v_wave - v_s_radial)

            const denominator = waveSpeed - v_s_radial;

            if (Math.abs(denominator) > 0.1) { // Avoid division by zero (source moving at wave speed towards observer)
                 observedFreq = sourceFreq * (waveSpeed + v_o_radial) / denominator;
            } else {
                 // Handle approaching/receding at wave speed - frequency goes to infinity/zero
                 observedFreq = v_s_radial > 0 ? Infinity : 0; // Approaching -> Infinity, Receding -> 0
            }

             // Handle extremely large/small frequencies for display
            if (observedFreq > 99999) observedFreq = 99999; // Cap display
            if (observedFreq < 0) observedFreq = 0; // Cannot have negative frequency in this context (though formula might yield it with wrong sign conventions)
        }


        observedFreqDisplay.textContent = `${observedFreq.toFixed(1)} Hz`;
    }

    function update(deltaTime) {
        // Update positions based on current velocities
        // This is done *before* potentially updating velocities from drag in the same frame
        // or after drag ends.
        if (!isDraggingSource) {
             source.x += source.vx * deltaTime;
             source.y += source.vy * deltaTime;
        }
         if (!isDraggingObserver) {
            observer.x += observer.vx * deltaTime;
            observer.y += observer.vy * deltaTime;
        }


        // Emit new wave if enough time has passed
        const wavePeriod = 1.0 / sourceFreq;
        if (time - lastWaveTime >= wavePeriod) {
            waves.push({ x: source.x, y: source.y, startTime: time });
            lastWaveTime = time;
        }

        // Remove old waves that are off-screen or too large
        // More robust check: is any part of the wave circle still within bounds?
        // Circle at (cx, cy) with radius r is within bounds if cx+r > 0 and cx-r < width and cy+r > 0 and cy-r < height
         const minX = 0, maxX = canvas.width, minY = 0, maxY = canvas.height;
         while (waves.length > 0) {
             const wave = waves[0];
             const radius = waveSpeed * (time - wave.startTime);
             // Check if wave is completely outside canvas boundaries
             if (wave.x + radius < minX || wave.x - radius > maxX || wave.y + radius < minY || wave.y - radius > maxY) {
                 waves.shift(); // Remove the oldest wave
             } else {
                 break; // Subsequent waves are emitted later and likely still visible
             }
        }


        // Update time
        time += deltaTime;

        // Update displays (especially observed frequency)
        updateDisplays();

        // Store current positions for next frame's velocity calculation if dragging
        lastSourceX = source.x;
        lastSourceY = source.y;
        lastObserverX = observer.x;
        lastObserverY = observer.y;
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw waves
        // Use a semi-transparent color and maybe a subtle gradient
        ctx.strokeStyle = 'rgba(0, 123, 255, 0.4)'; /* Lighter, more transparent blue */
        ctx.lineWidth = 2; /* Slightly thicker lines */
        waves.forEach(wave => {
            const radius = waveSpeed * (time - wave.startTime);
            if (radius > 0) {
                ctx.beginPath();
                ctx.arc(wave.x, wave.y, radius, 0, Math.PI * 2);
                ctx.stroke();
            }
        });

        // Draw source (Red)
        ctx.fillStyle = '#f44336'; /* Brighter Red */
        ctx.beginPath();
        ctx.arc(source.x, source.y, 12, 0, Math.PI * 2); /* Slightly larger */
        ctx.fill();
        // Optional: Add a subtle outline
        ctx.strokeStyle = '#c62828';
        ctx.lineWidth = 2;
        ctx.stroke();


        // Draw observer (Green)
        ctx.fillStyle = '#4CAF50'; /* Brighter Green */
        ctx.beginPath();
        ctx.arc(observer.x, observer.y, 12, 0, Math.PI * 2); /* Slightly larger */
        ctx.fill();
         // Optional: Add a subtle outline
        ctx.strokeStyle = '#2e7d32';
        ctx.lineWidth = 2;
        ctx.stroke();

        // Draw line between source and observer
        ctx.strokeStyle = '#546E7A'; /* Dark grey */
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(source.x, source.y);
        ctx.lineTo(observer.x, observer.y);
        ctx.stroke();

        // Draw velocity vectors
        const vectorScale = 0.7; // pixels per sim unit/sec
        ctx.strokeStyle = '#c62828'; /* Red for source */
        ctx.lineWidth = 2;
        drawArrow(source.x, source.y, source.x + source.vx * vectorScale, source.y + source.vy * vectorScale, 8);

        ctx.strokeStyle = '#2e7d32'; /* Green for observer */
        drawArrow(observer.x, observer.y, observer.x + observer.vx * vectorScale, observer.y + observer.vy * vectorScale, 8);

        // Draw observed frequency text near observer
        ctx.fillStyle = '#1a237e'; /* Dark blue text */
        ctx.font = 'bold 14px Arial, sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'bottom';
        const freqText = observedFreqDisplay.textContent; // Get formatted text from display
        ctx.fillText(freqText, observer.x, observer.y - 20); // Position above observer
    }

    function drawArrow(x1, y1, x2, y2, headlen) {
        // Draw the line
        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);
        ctx.stroke();

        // Draw arrowhead only if the vector has non-zero length
        const dx = x2 - x1;
        const dy = y2 - y1;
        const lengthSq = dx*dx + dy*dy;
        if (lengthSq > 4) { // Only draw arrow if vector is long enough (length > 2 pixels)
            const angle = Math.atan2(dy, dx);
            ctx.beginPath();
            ctx.moveTo(x2, y2);
            ctx.lineTo(x2 - headlen * Math.cos(angle - Math.PI / 6), y2 - headlen * Math.sin(angle - Math.PI / 6));
            ctx.moveTo(x2, y2);
            ctx.lineTo(x2 - headlen * Math.cos(angle + Math.PI / 6), y2 - headlen * Math.sin(angle + Math.PI / 6));
            ctx.stroke();
        }
    }

    // Helper to get mouse/touch position relative to canvas
    function getCanvasMousePosition(event) {
        const rect = canvas.getBoundingClientRect();
        let clientX, clientY;
        if (event.clientX !== undefined) { // Mouse event
            clientX = event.clientX;
            clientY = event.clientY;
        } else if (event.touches && event.touches.length > 0) { // Touch event
            clientX = event.touches[0].clientX;
            clientY = event.touches[0].clientY;
        } else {
             return null; // Should not happen with correct event types
        }

        return {
            x: clientX - rect.left,
            y: clientY - rect.top
        };
    }

    // Helper to check if a point is near an object
    function isNear(pointX, pointY, objectX, objectY, threshold) {
        const dx = pointX - objectX;
        const dy = pointY - objectY;
        return Math.sqrt(dx * dx + dy * dy) < threshold;
    }

    function startDrag(event) {
        event.preventDefault(); // Prevent default touch behavior (scrolling, etc.)
        const pos = getCanvasMousePosition(event);
        if (!pos) return;

        const dragThreshold = 20; // pixels radius around object center

        if (isNear(pos.x, pos.y, source.x, source.y, dragThreshold)) {
            isDraggingSource = true;
            dragStartX = pos.x;
            dragStartY = pos.y;
             // Set initial velocity to zero when starting drag? Or maintain? Let's maintain.
             // source.vx = 0; source.vy = 0;
            canvas.classList.add('dragging');
        } else if (isNear(pos.x, pos.y, observer.x, observer.y, dragThreshold)) {
            isDraggingObserver = true;
            dragStartX = pos.x;
            dragStartY = pos.y;
            // observer.vx = 0; observer.vy = 0;
            canvas.classList.add('dragging');
        }
    }

    function drag(event) {
        if (!isDraggingSource && !isDraggingObserver) return;
        event.preventDefault(); // Prevent default touch behavior (scrolling, etc.)
        const pos = getCanvasMousePosition(event);
         if (!pos) return;

        const currentX = pos.x;
        const currentY = pos.y;

        // Calculate velocity based on change in position since last frame/update
        // This approach makes velocity proportional to drag speed
        // Need to get the delta time since the last position update.
        // Using a fixed small deltaTime here might be simpler for drag velocity calculation
        // Or, calculate velocity based on current position vs start position and elapsed time?
        // Let's just use the difference from the LAST position and assume a tiny timestep
        // This makes velocity directly proportional to mouse move delta per frame.

        // A better approach: Store the position from the PREVIOUS frame's draw/update call.
        // This is what lastSourceX, lastSourceY, etc., are for.
        // The deltaTime is available from the main game loop.

        if (isDraggingSource) {
            // Calculate velocity based on how much the source *would* move to reach the mouse position
            // from its position at the start of this frame's update.
            // The update function already moved source based on its *old* velocity.
            // Let's update velocity based on the difference between current mouse pos and last recorded source pos.
            // The update loop will then use this *new* velocity in the next frame.
            // This creates a slight lag but avoids complex position overriding within the same frame.

             // Calculate velocity based on movement since the last frame's recorded position
             // Velocity = (Current Mouse Pos - Last Object Pos) / deltaTime
             // Problem: deltaTime is from the *game loop*, not necessarily the drag event frequency.
             // Simpler: Set velocity based on the difference between the *current* mouse pos and the object's *current* pos, scaled.
             // Or: Set velocity based on the difference between the *current* mouse pos and the *previous* mouse pos, scaled.
             // Let's use the difference between the *current* mouse pos and the object's position at the start of the drag,
             // and set the velocity proportional to that vector.
             // This makes the object "spring" towards the mouse if mouse stops, or follow if mouse moves steadily.
             // Let's make it simpler: Calculate velocity based on mouse movement delta between frames.

             const dt = timeStep; // Assume a small, fixed timestep for velocity calculation during drag

             // Calculate velocity based on change from last recorded position
             const deltaX = currentX - lastSourceX;
             const deltaY = currentY - lastSourceY;

             // Set the velocity directly based on the mouse movement
             source.vx = deltaX / dt;
             source.vy = deltaY / dt;

             // Also update the input fields to reflect the current velocity
             sourceVelXInput.value = source.vx.toFixed(0);
             sourceVelYInput.value = source.vy.toFixed(0);

             // Update the object's position immediately while dragging for smooth follow
             source.x = currentX;
             source.y = currentY;


        } else if (isDraggingObserver) {
             const dt = timeStep; // Assume a small, fixed timestep for velocity calculation during drag

             const deltaX = currentX - lastObserverX;
             const deltaY = currentY - lastObserverY;

             observer.vx = deltaX / dt;
             observer.vy = deltaY / dt;

             observerVelXInput.value = observer.vx.toFixed(0);
             observerVelYInput.value = observer.vy.toFixed(0);

             observer.x = currentX;
             observer.y = currentY;
        }
         // Update last positions immediately during drag
         lastSourceX = source.x;
         lastSourceY = source.y;
         lastObserverX = observer.x;
         lastObserverY = observer.y;

         // Update displays while dragging to show frequency change
         updateDisplays();
    }

    function endDrag(event) {
        if (isDraggingSource || isDraggingObserver) {
            event.preventDefault(); // Prevent default touch behavior
            isDraggingSource = false;
            isDraggingObserver = false;
            canvas.classList.remove('dragging');
             // Velocities were updated during drag. They will persist now.
             // updateParameters(); // Ensure inputs are synced and parameters updated
        }
    }


    let lastTime = 0;
    function gameLoop(currentTime) {
        if (!lastTime) lastTime = currentTime;
        const deltaTime = (currentTime - lastTime) / 1000; // Convert ms to seconds
        lastTime = currentTime;

        // Cap delta time to prevent physics weirdness on slow frames
        const cappedDeltaTime = Math.min(deltaTime, 0.1);

        update(cappedDeltaTime);
        draw();

        animationFrameId = requestAnimationFrame(gameLoop);
    }

    // Start the animation loop
    gameLoop();
});
</script>