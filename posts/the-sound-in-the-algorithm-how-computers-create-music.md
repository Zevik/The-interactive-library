---
title: "הקומפוזיטור הדיגיטלי: גלו את הקסם שבמוזיקה גנרטיבית"
english_slug: the-sound-in-the-algorithm-how-computers-create-music
category: "מוזיקה"
tags:
  - מוזיקה גנרטיבית
  - אלגוריתמים
  - בינה מלאכותית
  - יצירתיות חישובית
  - עיצוב סאונד
---
# הקומפוזיטור הדיגיטלי: גלו את הקסם שבמוזיקה גנרטיבית
דמיינו יצירה מוזיקלית חדשה לגמרי, שנולדה מתוך קוד ולא מתוך נשמה אנושית. האם מחשבים יכולים באמת ליצור מוזיקה מקורית, מפתיעה ומרגשת? צללו פנימה וגלו כיצד מערכת כללים פשוטה יכולה להפוך לקומפוזיטור הדיגיטלי האישי שלכם!

<div id="app-container">
    <div class="controls-panel">
        <h2>הגדירו את חוקי היצירה:</h2>
        <div class="control-group">
            <label for="scale" class="control-label">סולם מוזיקלי:</label>
            <select id="scale" class="control-select">
                <option value="major">מז'ור (עליז)</option>
                <option value="minor">מינור (מלנכולי)</option>
                <option value="pentatonic">פנטטוני (מזרחי/בלוזי)</option>
            </select>
        </div>
        <div class="control-group">
            <label for="tempo" class="control-label">קצב (BPM - פעימות בדקה):</label>
            <input type="number" id="tempo" class="control-input" value="120" min="30" max="300">
        </div>
        <div class="control-group">
            <label class="control-label">צעדים מותרים (מעלות בסולם):</label>
            <div class="checkbox-group">
                <div><input type="checkbox" id="step0" value="0" checked> <label for="step0">+0 (חזרה על הצליל)</label></div>
                <div><input type="checkbox" id="step1" value="1" checked> <label for="step1">±1 (צעד קטן)</label></div>
                <div><input type="checkbox" id="step2" value="2"> <label for="step2">±2 (קפיצה בינונית)</label></div>
                <div><input type="checkbox" id="step3" value="3"> <label for="step3">±3 (קפיצה גדולה)</label></div>
            </div>
        </div>
        <div class="control-group">
            <label for="randomness" class="control-label">אלמנט ההפתעה (אקראיות %):</label>
            <input type="range" id="randomness" class="control-slider" value="20" min="0" max="100">
            <span id="randomness-value" class="slider-value">20%</span>
        </div>
        <div class="control-group">
            <label for="sequence-length" class="control-label">אורך היצירה (מספר צלילים):</label>
            <input type="number" id="sequence-length" class="control-input" value="32" min="8" max="100">
        </div>
        <div class="button-group">
            <button id="generate-btn" class="control-button generate-button">צור מנגינה קסומה!</button>
            <button id="stop-btn" class="control-button stop-button" disabled>עצור את הקסם</button>
        </div>
        <div id="status" class="status-message">מוכן ליצירה</div>
    </div>
    <div class="visualization-panel">
        <h2>הצלילים מתעוררים לחיים:</h2>
        <div id="notes-display">
            <!-- Visual representation of notes will appear here -->
        </div>
         <div class="visualization-info">הגובה מייצג את הצליל בסולם. לחצו "צור מנגינה" כדי להתחיל!</div>
    </div>
</div>

<style>
    /* Hebrew typography and direction */
    body {
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif; /* Or a more modern web font */
        line-height: 1.6;
        color: #333;
        background-color: #eef2f7; /* Light background */
        padding: 20px;
    }

    #app-container {
        display: flex;
        flex-wrap: wrap;
        gap: 30px;
        margin: 20px auto;
        padding: 30px;
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        max-width: 1000px; /* Limit max width for better readability */
    }

    .controls-panel, .visualization-panel {
        flex: 1;
        min-width: 300px;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
        background-color: #f9f9f9; /* Slightly different background for panels */
        display: flex;
        flex-direction: column;
    }

    .controls-panel {
         min-width: 320px;
    }

    .visualization-panel {
         flex: 2;
         min-width: 450px;
         justify-content: space-between; /* Push info to bottom */
    }


    h1, h2 {
        color: #2c3e50; /* Dark blue-grey */
        margin-top: 0;
        margin-bottom: 20px;
    }

    h1 {
        text-align: center;
        margin-bottom: 40px;
    }

    .control-group {
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 1px dashed #ddd; /* Subtle separator */
    }
     .control-group:last-child {
         border-bottom: none;
         padding-bottom: 0;
     }

    .control-label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        color: #555;
        font-size: 1.1em;
    }

    .control-select,
    .control-input[type="number"] {
        width: calc(100% - 22px); /* Adjust for padding/border */
        padding: 10px;
        border: 1px solid #bdc3c7; /* Light grey */
        border-radius: 5px;
        font-size: 1em;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
     .control-select:focus,
     .control-input[type="number"]:focus,
     .control-slider:focus {
         border-color: #3498db; /* Blue accent */
         box-shadow: 0 0 8px rgba(52, 152, 219, 0.3);
         outline: none;
     }

    .control-slider {
        width: calc(100% - 12px);
        margin-top: 5px;
        cursor: pointer;
         accent-color: #3498db; /* Blue accent for slider fill */
    }

    .slider-value {
         display: inline-block;
         margin-right: 10px;
         font-weight: bold;
         color: #3498db; /* Blue accent */
    }

    .checkbox-group {
        display: flex; /* Arrange checkboxes in a row */
        flex-wrap: wrap;
        gap: 15px; /* Spacing between checkbox items */
    }
     .checkbox-group div {
         display: flex; /* Align input and label */
         align-items: center;
     }

    .checkbox-group input[type="checkbox"] {
        margin-left: 5px; /* Space between checkbox and label */
         accent-color: #2ecc71; /* Green accent */
    }
     .checkbox-group label {
         font-weight: normal;
         margin-bottom: 0; /* Reset label margin */
         font-size: 1em;
         color: #333;
         cursor: pointer;
     }


    .button-group {
        margin-top: 20px;
        margin-bottom: 15px;
        display: flex; /* Arrange buttons side by side */
        gap: 10px;
    }

    .control-button {
        padding: 12px 25px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
        flex-grow: 1; /* Allow buttons to grow */
        text-align: center;
    }
     .control-button:hover:not(:disabled) {
         transform: translateY(-2px); /* Slight lift on hover */
     }
      .control-button:active:not(:disabled) {
         transform: translateY(0); /* Press down effect */
     }

    .generate-button {
        background-color: #2ecc71; /* Emerald green */
        color: white;
    }
    .generate-button:hover:not(:disabled) {
        background-color: #27ae60; /* Darker green */
    }

    .stop-button {
        background-color: #e74c3c; /* Alizarin red */
        color: white;
    }
     .stop-button:hover:not(:disabled) {
         background-color: #c0392b; /* Darker red */
     }

     .control-button:disabled {
         opacity: 0.6;
         cursor: not-allowed;
         transform: none; /* Disable transform when disabled */
     }

    .status-message {
        margin-top: 10px;
        font-weight: bold;
        color: #3498db; /* Blue accent */
        text-align: center;
        min-height: 1.2em; /* Reserve space to prevent layout shifts */
    }

    #notes-display {
        display: flex;
        align-items: flex-end; /* Notes sit on the bottom */
        height: 200px; /* Increased height for better visualization */
        border-bottom: 2px solid #34495e; /* Dark border for staff line feel */
        position: relative;
        margin-top: 15px;
        overflow-x: auto; /* Enable horizontal scrolling */
        overflow-y: hidden; /* Hide vertical overflow */
        padding-bottom: 5px; /* Space for scrollbar on some systems */
    }

    .note {
        width: 18px; /* Wider bars */
        min-width: 10px;
        margin: 0 2px; /* Spacing between notes */
        background: linear-gradient(to top, #3498db, #2980b9); /* Blue gradient */
        opacity: 0.9;
        border-radius: 3px 3px 0 0; /* Rounded top corners */
        transition: height 0.15s ease-out, background-color 0.15s ease-out, opacity 0.15s ease-out;
        position: relative;
         bottom: 0; /* Align to bottom of container */
        /* Add subtle pulsing animation for playing notes */
        animation: pulse 1s infinite alternate; /* Default pulse, overridden when playing */
        animation-play-state: paused; /* Pause default animation */
    }

     .note.playing {
         background: linear-gradient(to top, #f1c40f, #f39c12); /* Yellow/Orange gradient */
         opacity: 1;
         box-shadow: 0 0 15px rgba(241, 196, 15, 0.7); /* Glow effect */
         animation-play-state: running; /* Start animation when playing */
     }

    @keyframes pulse {
        from { transform: scaleY(1); }
        to { transform: scaleY(1.05); } /* Subtle scale pulse */
    }


     .visualization-info {
         text-align: center;
         margin-top: 15px;
         color: #555;
         font-size: 0.9em;
     }


    #toggle-explanation {
        display: block;
        margin: 40px auto 20px;
        padding: 15px 30px;
        background-color: #9b59b6; /* Amethyst */
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.2em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    #toggle-explanation:hover {
        background-color: #8e44ad; /* Darker amethyst */
        transform: translateY(-2px);
    }
     #toggle-explanation:active {
         transform: translateY(0);
     }


    #explanation {
        margin: 20px auto;
        padding: 30px;
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        display: none; /* Hidden by default */
        direction: rtl;
        text-align: right;
        max-width: 1000px; /* Limit max width */
    }
    #explanation h2, #explanation h3 {
        color: #2c3e50;
        border-bottom: 1px solid #eee;
        padding-bottom: 8px;
        margin-top: 25px;
        margin-bottom: 15px;
    }
     #explanation h2 {
         border-bottom: 2px solid #ddd;
         padding-bottom: 10px;
     }
    #explanation p {
        line-height: 1.8;
        color: #555;
        margin-bottom: 15px;
    }
     #explanation ul {
         margin-bottom: 15px;
         padding-right: 20px;
     }
     #explanation li {
         margin-bottom: 8px;
         color: #555;
     }
     #explanation strong {
         color: #333;
     }

     /* Responsive adjustments */
     @media (max-width: 768px) {
         #app-container {
             flex-direction: column;
             gap: 20px;
             padding: 20px;
         }
         .controls-panel, .visualization-panel {
             min-width: unset; /* Remove min-width on smaller screens */
             width: 100%; /* Take full width */
             padding: 20px;
         }
          .checkbox-group {
             flex-direction: column; /* Stack checkboxes vertically */
             gap: 10px;
          }
         .control-button {
             padding: 10px 15px;
             font-size: 1em;
         }
         #notes-display {
              height: 150px; /* Reduce height slightly */
         }
         .note {
             width: 15px;
         }
     }

</style>

<button id="toggle-explanation">רוצים להבין איך הקסם קורה? לחצו כאן להסבר!</button>

<div id="explanation">
    <h2>מהי מוזיקה גנרטיבית ולמה היא כל כך מרתקת?</h2>
    <p>מוזיקה גנרטיבית היא יצירת מוזיקה באמצעות מערכות אוטונומיות – לרוב מבוססות על אלגוריתמים, כללים מוגדרים מראש או מודלים של למידת מכונה – ולא על ידי הלחנה ישירה של אדם. היא פותחת דלתות לעולם חדש של צלילים, מאפשרת לחקור את מהות היצירתיות, ליצור יצירות אינסופיות ובלתי צפויות, ואף להבין טוב יותר כיצד עובדים מבנים מוזיקליים.</p>

    <h3>אילו סוגי אלגוריתמים קיימים ליצירת מוזיקה?</h3>
    <p>ישנן גישות רבות ומגוונות ליצירת מוזיקה חישובית:</p>
    <ul>
        <li>**דקדוקים מוזיקליים (Musical Grammars):** מערכות כללים המגדירות אילו צירופי צלילים, מקצבים או אקורדים מותרים, בדומה לחוקי תחביר בשפה.</li>
        <li>**תהליכים אקראיים מבוקרים (Stochastic Processes):** משתמשים באקראיות בצורה מחושבת. דוגמה קלאסית היא שרשרות מרקוב, שבהן הבחירה בצליל הבא תלויה בהסתברות המבוססת על הצליל הנוכחי או צלילים קודמים.</li>
        <li>**למידת מכונה (Machine Learning):** אלגוריתמים מתקדמים כמו רשתות נוירונים "מאומנים" על כמויות גדולות של מוזיקה קיימת, ולומדים את הסגנונות והמבנים שלה כדי ליצור יצירות חדשות "בסגנון" שנלמד.</li>
        <li>**אלגוריתמים גנטיים (Genetic Algorithms):** בהשראת האבולוציה הביולוגית, אלגוריתמים אלו "מפתחים" יצירות מוזיקליות על ידי יצירת וריאציות אקראיות על "דור" קיים של יצירות ובחירת ה"מתאימות" ביותר (לפי קריטריונים מוגדרים או הערכת מאזינים) ליצירת ה"דור" הבא.</li>
    </ul>

    <h3>איך "מחשבים" מוזיקה: ייצוג וכללים</h3>
    <p>כדי שמחשב יוכל לעבוד עם מוזיקה, היא צריכה להיות מיוצגת בצורה דיגיטלית. זה יכול להיות ברמת הצליל הבודד (תווים, MIDI), רמת האודיו עצמו (גלי קול), או ברמות מופשטות יותר (סולמות, אקורדים, מבנים). האלגוריתמים מפעילים את הכללים על הייצוגים הללו. למשל, האלגוריתם שראיתם בפעולה כאן הוא דוגמה פשוטה לתהליך אקראי מבוקר: הוא בוחר את הצליל הבא על בסיס הצליל הנוכחי והצעדים המותרים בסולם הנבחר, בתוספת רמת אקראיות שאתם קובעים.</p>

    <h3>שורשים היסטוריים וגלגולים מודרניים</h3>
    <p>הרעיון של יצירת מוזיקה באמצעות כללים אינו המצאה מודרנית. אפילו מוצרט התנסה ב"משחקי קוביות" ליצירת מינואטים. המלחין ארנולד שנברג במאה ה-20 פיתח את שיטת הדודקפוניה (12 טונים), שהיא מערכת קומפוזיציה מבוססת כללים פורמליים. עם הופעת המחשבים בשנות ה-50, החלו חוקרים ומלחינים להשתמש בהם ליישום רעיונות אלו. הפריצה הגדולה באמת הגיעה עם התקדמות למידת המכונה ועלייתם של מודלים עצביים, שהפכו את המוזיקה הגנרטיבית למורכבת, עשירה וקרובה יותר ליצירה אנושית.</p>

    <h3>איפה פוגשים מוזיקה גנרטיבית היום?</h3>
    <p>מעבר לעולם האמנות, למוזיקה גנרטיבית יישומים פרקטיים רבים: פסקולים דינמיים למשחקי וידאו המשתנים בהתאם לעלילה או לפעולות השחקן, יצירת מוזיקת רקע אינסופית ומתאימה אישית לאפליקציות או סביבות דיגיטליות, סיוע למלחינים בתהליך היצירה (הצעת רעיונות, השלמת קטעים), ואף שימוש בתרפיה מוזיקלית.</p>

    <h3>האם מחשב יכול להיות באמת יצירתי?</h3>
    <p>זו אחת השאלות המרתקות ביותר בתחום. אם נגדיר יצירתיות כ"יכולת ליצור משהו חדש ובעל ערך", הרי שמערכות אלגוריתמיות מסוימות אכן עונות על הגדרה זו. אך האם יצירתיות דורשת מודעות, רגשות, כוונה או חוויה? כאן הדיון הופך לפילוסופי ועמוק. ככל הנראה, היצירתיות במקרה של מוזיקה גנרטיבית טמונה איפשהו בשילוב שבין התכנון, הכללים והנתונים שסיפק האדם למערכת, לבין התוצאות המפתיעות, הבלתי צפויות ולעיתים גאוניות, שהאלגוריתם מסוגל לייצר. זהו גבול מרתק בין אדם למכונה, שנחקר ומתפתח כל הזמן.</p>
</div>

<script>
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    let oscillator = null;
    let gainNode = null;
    let isPlaying = false;
    let sequenceTimeout = null; // Renamed interval to timeout for clarity
    let currentNoteIndex = 0;
    let noteElements = [];
    let generatedSequence = []; // Store the generated sequence


    // Define scales (using relative scale degrees for simplicity, C root)
    // Values are semitone offsets from the root
    const scales = {
        major: [0, 2, 4, 5, 7, 9, 11, 12], // C D E F G A B C
        minor: [0, 2, 3, 5, 7, 8, 10, 12], // C D Eb F G Ab Bb C (Natural Minor)
        pentatonic: [0, 2, 4, 7, 9, 12] // C D E G A C (Major Pentatonic)
    };

     // Simple frequency mapping based on MIDI note number
    const midiToFrequency = (midi) => 440 * Math.pow(2, (midi - 69) / 12); // A4 = 440 Hz, MIDI 69

    // Base MIDI note for the root (C4 = 60)
    const baseMidi = 60; // C4

    // Get elements
    const scaleSelect = document.getElementById('scale');
    const tempoInput = document.getElementById('tempo');
    const stepCheckboxes = document.querySelectorAll('.checkbox-group input[type="checkbox"]');
    const randomnessSlider = document.getElementById('randomness');
    const randomnessValueSpan = document.getElementById('randomness-value');
    const sequenceLengthInput = document.getElementById('sequence-length');
    const generateBtn = document.getElementById('generate-btn');
    const stopBtn = document.getElementById('stop-btn');
    const statusDiv = document.getElementById('status');
    const notesDisplay = document.getElementById('notes-display');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // Event listeners
    randomnessSlider.addEventListener('input', () => {
        randomnessValueSpan.textContent = randomnessSlider.value + '%';
    });

    generateBtn.addEventListener('click', startGeneration);
    stopBtn.addEventListener('click', stopGeneration);
    toggleExplanationBtn.addEventListener('click', toggleExplanation);


    // --- Core Logic ---

    function getSelectedRules() {
        const selectedScaleKey = scaleSelect.value;
        const scale = scales[selectedScaleKey];
        const tempo = parseInt(tempoInput.value, 10); // BPM
        const randomness = parseInt(randomnessSlider.value, 10) / 100; // 0-1
        const sequenceLength = parseInt(sequenceLengthInput.value, 10);

        const allowedSteps = [];
        stepCheckboxes.forEach(checkbox => {
            const stepValue = parseInt(checkbox.value, 10);
            if (checkbox.checked) {
                allowedSteps.push(stepValue);
                if (stepValue > 0) { // Add negative steps for non-zero values
                     allowedSteps.push(-stepValue);
                }
            }
        });

        // Filter out duplicates and sort for consistency (though not strictly needed for logic)
        const uniqueAllowedSteps = [...new Set(allowedSteps)].sort((a, b) => a - b);


        return {
            scale,
            tempo,
            randomness,
            sequenceLength,
            allowedSteps: uniqueAllowedSteps
        };
    }

    function generateSequence(rules) {
        const sequence = [];
        let currentScaleDegreeIndex = 0; // Start on the root of the scale (index 0)
        const scaleLength = rules.scale.length - 1; // Number of usable notes before octave

        for (let i = 0; i < rules.sequenceLength; i++) {
            let nextScaleDegreeIndex = currentScaleDegreeIndex;
            let chosenStep = 0;

            if (rules.allowedSteps.length > 0) {
                // Decide whether to apply randomness or follow rules based on randomness percentage
                if (Math.random() < rules.randomness || rules.allowedSteps.length === 1 && rules.allowedSteps[0] === 0) {
                     // High randomness or only repeat allowed: Pick any index within a reasonable range
                    // Let's pick a random step that results in an index within +/- 5 degrees of the root? Or based on total range?
                    // Simpler: pick a random index relative to current position that stays within a general playing range.
                    // Let's aim for +/- an octave or two relative to the base MIDI
                     const minPlayableMidi = baseMidi - 12 * 2; // C2
                     const maxPlayableMidi = baseMidi + 12 * 3; // C5 or C6 range

                     // Find potential target scale degrees within the range
                     const potentialTargets = [];
                     for(let octaveShift = -2; octaveShift <= 3; octaveShift++) { // Search +/- 2 octaves from root index
                         for(let degree = 0; degree < scaleLength; degree++) {
                              const absoluteDegreeIndex = degree + octaveShift * scaleLength;
                              const semitoneOffset = rules.scale[degree] + octaveShift * 12;
                              const midi = baseMidi + semitoneOffset;
                              if (midi >= minPlayableMidi && midi <= maxPlayableMidi) {
                                   potentialTargets.push(absoluteDegreeIndex); // Store absolute scale degree index
                              }
                         }
                     }

                    if (potentialTargets.length > 0) {
                         // Pick a random target index
                         nextScaleDegreeIndex = potentialTargets[Math.floor(Math.random() * potentialTargets.length)];
                    } else {
                         // Fallback if range is somehow restricted
                         nextScaleDegreeIndex = currentScaleDegreeIndex;
                    }


                } else {
                    // Follow rules: Pick an allowed step
                    const possibleNextDegrees = [];
                    rules.allowedSteps.forEach(step => {
                        const potentialDegree = currentScaleDegreeIndex + step;
                         // Check if the potential degree index is somewhat reasonable (within +/- a few octaves of center)
                         // Let's check if the resulting MIDI is within a wide playable range (e.g., C1 to C7, MIDI 36-96)
                         // This requires calculating the MIDI first... slightly complex here.
                         // Simpler check: keep degree index within +/- a generous range relative to the root (e.g., +/- 4 octaves worth of steps)
                         const maxRelativeDegree = scaleLength * 4;
                         if (potentialDegree >= -maxRelativeDegree && potentialDegree <= maxRelativeDegree) {
                             possibleNextDegrees.push(potentialDegree);
                         }
                    });

                    if (possibleNextDegrees.length > 0) {
                        nextScaleDegreeIndex = possibleNextDegrees[Math.floor(Math.random() * possibleNextDegrees.length)];
                    } else {
                         // If no allowed step keeps it in range, just repeat the note
                        nextScaleDegreeIndex = currentScaleDegreeIndex;
                    }
                }
            } else {
                 // If no steps allowed at all, just repeat the note
                 nextScaleDegreeIndex = currentScaleDegreeIndex;
            }

            // Calculate the actual MIDI note based on the chosen scale degree index
            // Normalize the scale degree index to be within the 0 to scaleLength-1 range for scale lookup
            const normalizedDegree = (nextScaleDegreeIndex % scaleLength + scaleLength) % scaleLength;
            // Calculate the octave offset from the root octave based on the absolute degree index
            // Add 1 to the baseMidi octave (C4=60) for the calculation if index 0 means the root note.
            // Example: index 0 -> rules.scale[0] + 0*12 = baseMidi + 0
            // Example: index scaleLength -> rules.scale[0] + 1*12 = baseMidi + 12 (Octave up)
            // Example: index -scaleLength -> rules.scale[0] + -1*12 = baseMidi - 12 (Octave down)
            const octaveOffset = Math.floor(nextScaleDegreeIndex / scaleLength);

            // Get the semitone offset from the scale definition for the normalized degree
            const semitoneOffsetInOctave = rules.scale[normalizedDegree];
            // Calculate the total semitone offset from the base MIDI note (C4)
            const totalSemitoneOffset = semitoneOffsetInOctave + octaveOffset * 12;

            // Calculate the final MIDI note
            let finalMidiNote = baseMidi + totalSemitoneOffset;

             // Clamp the resulting MIDI note to a reasonable playable range (e.g., C3 to C6, MIDI 48-84)
             // C3 (48), C4 (60), C5 (72), C6 (84)
            const minMidi = 48; // C3
            const maxMidi = 84; // C6
            finalMidiNote = Math.max(minMidi, Math.min(maxMidi, finalMidiNote));

            // To ensure subsequent steps are relative to the *actual* clamped note,
            // we need to find the closest scale degree index for this finalMidiNote.
            // This is tricky because multiple scale degree indices might map to the same MIDI (e.g., due to clamping).
            // For simplicity and to keep the "step" logic predictable relative to the previous *intended* note,
            // let's just update the currentScaleDegreeIndex based on the chosen step *before* clamping.
            // This means the visualization height reflects the clamped note, but the *next* note generation
            // is based on the step from the *unclamped* previous position. This is a simplification.
            // A more accurate simulation would find the closest scale degree index of the finalMidiNote.
            // Let's stick to the simpler method for now as it fits the existing step logic better.
            currentScaleDegreeIndex = nextScaleDegreeIndex; // Update for the next iteration


            sequence.push(finalMidiNote);
        }
        return sequence;
    }

    function visualizeSequence(sequence, rules) {
        notesDisplay.innerHTML = ''; // Clear previous visualization
        noteElements = [];
        generatedSequence = sequence; // Store the sequence for playback

        if (sequence.length === 0) {
             notesDisplay.innerHTML = '<div class="visualization-info">לא נוצרו צלילים עם חוקים אלו. נסו לשנות הגדרות.</div>';
             return;
        }

        // Calculate range dynamically based on the generated sequence
        const maxNote = Math.max(...sequence);
        const minNote = Math.min(...sequence);
        const noteRange = maxNote - minNote;
        const displayHeight = notesDisplay.offsetHeight - 10; // Account for some padding/border space
        const minNoteHeight = 8; // Minimum height for a note bar
        const maxNoteHeight = displayHeight - minNoteHeight; // Max height

        // Determine note width based on sequence length to fit or allow scrolling
        const containerWidth = notesDisplay.offsetWidth;
        const totalNotes = sequence.length;
        const minNoteWidth = 10;
        const maxNoteRenderWidth = 20; // Max reasonable display width per note
        const gap = 3; // Margin between notes

        // Calculate width to fit if possible, otherwise use max render width and allow scroll
        let noteWidth = Math.floor((containerWidth / totalNotes) - gap);
        if (noteWidth > maxNoteRenderWidth) {
             noteWidth = maxNoteRenderWidth;
        }
         // Ensure minimum width
         noteWidth = Math.max(minNoteWidth, noteWidth);


        sequence.forEach((midi, index) => {
            const noteDiv = document.createElement('div');
            noteDiv.classList.add('note');
            noteDiv.dataset.midi = midi; // Store midi value

            // Calculate height based on pitch relative to the sequence range
            let height;
            if (noteRange === 0) { // Handle sequences with only one note
                 height = displayHeight / 2; // Center it roughly
            } else {
                 // Scale height based on pitch, mapping minNote to min height, maxNote to max height
                 height = minNoteHeight + ((midi - minNote) / noteRange) * (maxNoteHeight - minNoteHeight);
            }
            noteDiv.style.height = `${Math.max(minNoteHeight, Math.min(height, displayHeight))}px`; // Clamp height

            noteDiv.style.width = `${noteWidth}px`;
            noteDiv.style.marginRight = `${gap}px`;

            // Add a subtle hue shift based on pitch (optional, adds visual flair)
             const hue = (midi - 36) * 5 % 360; // Map MIDI range (approx C1=36 to C6=84) to hues
            // noteDiv.style.filter = `hue-rotate(${hue}deg)`; // Can use filter, or adjust background color


            noteElements.push(noteDiv);
            notesDisplay.appendChild(noteDiv);
        });

         // Remove margin from the last element
         if (noteElements.length > 0) {
             noteElements[noteElements.length - 1].style.marginRight = '0';
         }

         // Scroll to the beginning
         notesDisplay.scrollLeft = 0;
    }


    function playSequence() {
        if (!audioContext || generatedSequence.length === 0) return;

        // Ensure audio context is running
        if (audioContext.state === 'suspended') {
            audioContext.resume().then(() => {
                console.log('AudioContext resumed!');
                startPlaybackLoop();
            }).catch(e => console.error('Error resuming AudioContext:', e));
        } else {
             startPlaybackLoop();
        }

        function startPlaybackLoop() {
            stopCurrentSound(); // Stop any previous sound/interval
            isPlaying = true;
            currentNoteIndex = 0;
            const rules = getSelectedRules(); // Get current tempo rule
            const noteDuration = 60 / rules.tempo; // Duration in seconds for a quarter note

            // Clear any previous highlights
             noteElements.forEach(el => el.classList.remove('playing'));
             statusDiv.textContent = 'מנגן...';


            function scheduleNextNote(time) {
                if (!isPlaying || currentNoteIndex >= generatedSequence.length) {
                    stopGeneration(); // Sequence finished or stopped manually
                    return;
                }

                const midiNote = generatedSequence[currentNoteIndex];
                const frequency = midiToFrequency(midiNote);
                const currentTime = audioContext.currentTime;

                 // --- Visual Update (synced as best as possible with audio scheduling) ---
                 // Highlight the current note visually
                 if (noteElements[currentNoteIndex]) {
                     // Debounce or use a dedicated visual update loop for better sync?
                     // For simplicity, we'll apply class immediately, but it might be slightly off audio.
                     // A common pattern is a visual "playhead" or a separate RAF loop.
                     // Let's just update classes here for now.
                    requestAnimationFrame(() => { // Use RAF to hopefully sync better with rendering cycle
                        if (isPlaying) { // Only update if still playing
                             noteElements.forEach(el => el.classList.remove('playing')); // Remove previous highlight
                             noteElements[currentNoteIndex].classList.add('playing');

                             // Scroll to keep the playing note visible
                            const noteEl = noteElements[currentNoteIndex];
                             // Calculate scroll position to center the note
                            const scrollPos = noteEl.offsetLeft - (notesDisplay.offsetWidth / 2) + (noteEl.offsetWidth / 2);
                            notesDisplay.scrollTo({
                                 left: scrollPos,
                                 behavior: 'smooth' // Optional: smooth scrolling
                            });
                        }
                    });
                 }
                 // --- End Visual Update ---


                // Create oscillator and gain node for this specific note
                const osc = audioContext.createOscillator();
                const gain = audioContext.createGain();

                osc.type = 'sine'; // sine, square, saw, triangle (simple synth voice)
                osc.frequency.setValueAtTime(frequency, currentTime);

                 // ADSR-like envelope (Attack, Decay, Sustain, Release)
                const attackTime = 0.05; // Quick attack
                const decayTime = noteDuration * 0.3; // Decay phase
                const sustainLevel = 0.2; // Sustain level (lower volume)
                const releaseTime = 0.05; // Release at the very end

                // Envelope
                gain.gain.setValueAtTime(0, currentTime); // Start at silence
                gain.gain.linearRampToValueAtTime(0.5, currentTime + attackTime); // Attack to max volume
                gain.gain.linearRampToValueAtTime(sustainLevel, currentTime + attackTime + decayTime); // Decay to sustain level
                // Sustain is implicit during the note duration until release

                // Connect nodes
                osc.connect(gain).connect(audioContext.destination);

                // Start and stop the oscillator
                osc.start(currentTime);
                 // Schedule stop slightly before the end of the note duration to allow for release
                osc.stop(currentTime + noteDuration);


                // Schedule the release envelope fade-out
                // Need to schedule the gain decrease just before the note ends
                 gain.gain.setValueAtTime(sustainLevel, currentTime + noteDuration - releaseTime); // Ensure sustain level just before release
                 gain.gain.linearRampToValueAtTime(0, currentTime + noteDuration); // Release to silence

                 // Disconnect nodes after they are finished
                 osc.onended = () => {
                     osc.disconnect();
                     gain.disconnect();
                 };


                // Schedule the next note
                currentNoteIndex++;
                if (currentNoteIndex < generatedSequence.length) {
                    // Schedule the next note based on the duration of the current one
                    // We schedule slightly ahead of time for better timing accuracy in Web Audio API
                    const nextNoteTime = currentTime + noteDuration;
                    sequenceTimeout = setTimeout(() => { // Use setTimeout for scheduling the next event loop tick
                        scheduleNextNote(nextNoteTime); // Pass the *scheduled* time for the next note
                    }, (nextNoteTime - audioContext.currentTime) * 1000); // Calculate delay in milliseconds
                } else {
                     // Last note scheduled, clean up after its duration
                     sequenceTimeout = setTimeout(() => {
                         stopGeneration();
                     }, noteDuration * 1000);
                }
            }

             // Start the first note
            scheduleNextNote(audioContext.currentTime);
        }
    }

     function stopCurrentSound() {
         // Stop all currently active oscillators/gain nodes if managing them globally
         // With the per-note oscillator/gain setup, we primarily need to:
         // 1. Clear the timeout for the next note.
         clearTimeout(sequenceTimeout);
         sequenceTimeout = null;
         // 2. Ideally, stop any currently playing sound with a quick fade-out to avoid clicks.
         // This requires keeping track of the *current* oscillator/gain, or applying a fade to the main destination.
         // The per-note setup makes stopping *all* potentially scheduled notes complex.
         // A simpler approach for a basic example: just clear the timeout and let currently playing notes finish or stop global gain.
         // Let's try a quick fade on the main audio context destination gain.
         if (audioContext && audioContext.state === 'running') {
              // Create a temporary gain node to fade out
              const tempGain = audioContext.createGain();
              tempGain.connect(audioContext.destination);
              // Try to disconnect the previous main output (might not exist or might be multiple)
              // This is tricky with the current setup.
              // Let's rely on the per-note osc.onended for cleanup and just clear the timeout.
              // If we *must* stop immediately, we'd need to keep references to all osc/gain nodes or use a single output chain.

             // Let's add a check and stop the *last* created oscillator/gain node if it exists and is connected.
              if (oscillator && gainNode) {
                  try {
                      // Apply a quick fade out
                      gainNode.gain.cancelScheduledValues(audioContext.currentTime);
                      gainNode.gain.setValueAtTime(gainNode.gain.value, audioContext.currentTime); // Start fade from current value
                      gainNode.gain.linearRampToValueAtTime(0, audioContext.currentTime + 0.05); // Fade to zero in 50ms
                      // Disconnect after fade
                      oscillator.stop(audioContext.currentTime + 0.06); // Stop slightly after fade
                      oscillator.onended = () => { // Clean up connections
                          oscillator.disconnect();
                          gainNode.disconnect();
                          oscillator = null;
                          gainNode = null;
                      };
                  } catch (e) {
                      console.warn("Error during stop fade/disconnect:", e);
                       // Fallback: just disconnect
                       if (oscillator) { try { oscillator.disconnect(); } catch(e) {} }
                       if (gainNode) { try { gainNode.disconnect(); } catch(e) {} }
                       oscillator = null;
                       gainNode = null;
                  }
              }
         }

         // Clear all visual highlights
         noteElements.forEach(el => el.classList.remove('playing'));
         currentNoteIndex = 0; // Reset visual index
     }


    function startGeneration() {
        if (isPlaying) {
             stopGeneration(); // Stop current playback before generating new
        }

        statusDiv.textContent = 'יוצר מנגינה...';
        generateBtn.disabled = true;
        stopBtn.disabled = false;
        noteElements.forEach(el => el.classList.remove('playing')); // Clear any lingering highlights

        const rules = getSelectedRules();
        const sequence = generateSequence(rules);
        visualizeSequence(sequence, rules);
        // Playback is initiated *after* visualization
         if (sequence.length > 0) {
             playSequence();
         } else {
              statusDiv.textContent = 'לא נוצרו צלילים.';
              generateBtn.disabled = false;
              stopBtn.disabled = true;
         }
    }

    function stopGeneration() {
        if (!isPlaying && sequenceTimeout === null && !oscillator && !gainNode) return; // Already stopped state

        isPlaying = false;
        stopCurrentSound(); // Handles clearing timeout and audio nodes

        statusDiv.textContent = 'הנגינה נעצרה.'; // More specific status
        generateBtn.disabled = false;
        stopBtn.disabled = true;

        // Visual cleanup already in stopCurrentSound
         // noteElements.forEach(el => el.classList.remove('playing'));
         // currentNoteIndex = 0; // Already reset in stopCurrentSound
    }

    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר את ההסבר' : 'רוצים להבין איך הקסם קורה? לחצו כאן להסבר!';
    }

     // Initial state setup
    function initializeApp() {
        statusDiv.textContent = 'מוכן ליצירה';
        randomnessValueSpan.textContent = randomnessSlider.value + '%'; // Set initial value display
        explanationDiv.style.display = 'none'; // Ensure explanation is hidden on load
        toggleExplanationBtn.textContent = 'רוצים להבין איך הקסם קורה? לחצו כאן להסבר!'; // Set initial button text
         // Optionally generate a default sequence on load
         // startGeneration(); // Could start with a default sequence playing
    }

    initializeApp();

</script>
```