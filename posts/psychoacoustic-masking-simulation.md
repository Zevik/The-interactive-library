---
title: "חשיפה לאוזן: הדמיית מיסוך פסיכואקוסטי"
english_slug: psychoacoustic-masking-simulation
category: "אמנות ועיצוב / מוזיקה"
tags:
  - מיסוך
  - שמיעה
  - פסיכואקוסטיקה
  - אודיו
  - צליל
---
# חשיפה לאוזן: הדמיית מיסוך פסיכואקוסטי

האם אי פעם ניסיתם לשמוע לחישה עדינה בתוך רעש המולה של מסיבה? זוהי דוגמה יומיומית לתופעה מרתקת וקריטית באופן שבו אנו תופסים צלילים: אפקט המיסוך הפסיכואקוסטי. צליל אחד, חזק מספיק, יכול פשוט "למחוק" צליל אחר, חלש יותר, מתודעת השמיעה שלנו. בואו נחקור יחד את התופעה הזו באופן אינטראקטיבי.

<div id="app-container" class="simulation-container">
    <h2>החוויה האינטראקטיבית: שחקו עם צלילים ומסכות</h2>
    <p>כאן תוכלו לבחון את אפקט המיסוך בעצמכם. הגדירו את התדר (גובה הצליל) ואת העוצמה (חזקות הצליל) עבור שני צלילים נפרדים: צליל "מסכה" חזק וצליל "מטרה" חלש יותר. שימו לב כיצד שינויים בהגדרות משפיעים על היכולת שלכם לשמוע את צליל המטרה בנוכחות המסכה.</p>

    <div class="controls-container">
        <div class="control-group masker-controls">
            <h3>צליל המסכה (Masker)</h3>
            <label for="maskerFreq">תדר (הרץ): <span id="maskerFreqValue" class="value-display">400</span></label>
            <input type="range" id="maskerFreq" min="100" max="10000" value="400"> <!-- Increased range -->
            <label for="maskerVol">עוצמה יחסית: <span id="maskerVolValue" class="value-display">70</span></label>
            <input type="range" id="maskerVol" min="0" max="100" value="70">
        </div>

        <div class="control-group target-controls">
            <h3>צליל המטרה (Target)</h3>
            <label for="targetFreq">תדר (הרץ): <span id="targetFreqValue" class="value-display">500</span></label>
            <input type="range" id="targetFreq" min="100" max="10000" value="500"> <!-- Increased range -->
            <label for="targetVol">עוצמה יחסית: <span id="targetVolValue" class="value-display">40</span></label>
            <input type="range" id="targetVol" min="0" max="100" value="40">
        </div>
    </div>

    <button id="playButton" class="action-button">התחילו את ההדמיה</button>
    <div id="statusMessage" class="status-indicator">
        <span id="statusDot" class="status-dot"></span>
        <span id="statusText">לחצו 'התחילו את ההדמיה' כדי לשמוע.</span>
    </div>


     <!-- Visual Cue Area (Conceptual) -->
     <div id="visual-cue-area">
        <h4>סף השמיעה המושפע:</h4>
        <p>דמיינו את סף השמיעה שלכם עולה בנוכחות המסכה, במיוחד בתדרים קרובים. צלילי מטרה חלשים מדי בתוך "סף מורם" זה פשוט נעלמים.</p>
        <!-- Could add dynamic elements here later with more complex JS/CSS -->
     </div>

</div>

<button id="showExplanationButton" class="toggle-button">הסבר מעמיק על מיסוך פסיכואקוסטי</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2>מיסוך פסיכואקוסטי: איך ולמה זה קורה?</h2>

    <p>מיסוך פסיכואקוסטי אינו סתם חסימת צליל פיזית. זו תופעה מורכבת שמקורה באופן שבו מוחנו ומערכת השמיעה שלנו מעבדים מידע קולי. כאשר צליל חזק דומיננטי, הוא גורם לפעילות עצבית ענפה באזורים ספציפיים באוזן הפנימית ובמוח. פעילות זו יכולה "להאפיל" או "להטביע" את הסיגנלים העצביים החלשים יותר המגיעים מצלילים עדינים יותר, במיוחד אם הם דומים בתדר או מתרחשים בסמיכות זמנים.</p>

    <h3>היבטים מרכזיים של מיסוך:</h3>

    <h4>מיסוך בתדר (Frequency Masking):</h4>
    <p>זהו הסוג שפגשתם בהדמיה. צליל חזק בתדר מסוים מקשה על שמיעת צלילים אחרים, בעיקר אלה שתדריהם קרובים. האפקט משמעותי יותר כאשר צליל המטרה נמצא בתדר גבוה יותר מצליל המסכה ("upward spread of masking"). הסיבה? המבנה המכני של השבלול באוזן הפנימית מגיב באופן א-סימטרי: תדרים חזקים "מתפשטים" יותר בקלות לאזורי תדר גבוהים יותר על גבי הממברנה הבזילרית.</p>
    <p>כפי שראיתם בהדמיה, ככל שתדר המטרה קרוב יותר לתדר המסכה וככל שהמסכה חזקה יותר - כך המיסוך חזק יותר. כדי "לחשוף" את צליל המטרה הממוסך, תצטרכו להגביר את עוצמתו משמעותית.</p>

    <h4>מיסוך בזמן (Temporal Masking):</h4>
    <p>השמיעה שלנו מושפעת לא רק מתדרים, אלא גם מרצף הצלילים בזמן. צליל חזק ופתאומי יכול למסך צלילים חלשים שקרו ממש לפניו (pre-masking) או מיד אחריו (post-masking).
    <ul>
        <li>**Pre-masking (מיסוך מקדים):** צליל חלש שהתרחש כמה מילישניות *לפני* צליל חזק יכול להיות ממוסך. המוח מעבד את הצליל החזק מהר יותר, וזה כאילו "מקדים" את תפיסת הצליל החלש.</li>
        <li>**Post-masking (מיסוך עוקב):** צליל חלש שקורה עד כ-50-200 מילישניות *אחרי* צליל חזק יכול להיות ממוסך. מערכת השמיעה כאילו "מתאוששת" מהצליל החזק, וקליטת הצלילים החלשים שאחריו נפגעת זמנית.</li>
    </ul>
    </p>

    <h3>מדוע זה חשוב? שימושים מפתיעים</h3>
    <p>הבנת מיסוך פסיכואקוסטי אינה רק עניין אקדמי. היא חיונית לעיצוב חוויות שמע, למשל בתעשיית האודיו. פורמטים של דחיסת אודיו כמו MP3, AAC ואחרים מנצלים את תופעת המיסוך. הם מסירים מהקובץ מידע על צלילים שהאדם ממילא לא ישמע (כי הם ממוסכים על ידי צלילים אחרים) וכך מקטינים את גודל הקובץ באופן דרמטי מבלי לפגוע משמעותית באיכות הנתפסת. זוהי דוגמה מבריקה לאופן שבו ידע על פסיכואקוסטיקה מאפשר לנו לבנות טכנולוגיות יעילות יותר.</p>
</div>

<script>
    let audioCtx;
    let maskerOscillator = null;
    let maskerGain = null;
    let targetOscillator = null;
    let targetGain = null;
    let isPlaying = false;
    const minDb = -40; // Assuming base audibility is somewhere around -40dB re max slider value
    const maxDb = 40; // Assuming max slider value maps to 40dB above min

    const maskerFreqSlider = document.getElementById('maskerFreq');
    const maskerVolSlider = document.getElementById('maskerVol');
    const targetFreqSlider = document.getElementById('targetFreq');
    const targetVolSlider = document.getElementById('targetVol');

    const maskerFreqValueSpan = document.getElementById('maskerFreqValue');
    const maskerVolValueSpan = document.getElementById('maskerVolValue');
    const targetFreqValueSpan = document.getElementById('targetFreqValue');
    const targetVolValueSpan = document.getElementById('targetVolValue');

    const playButton = document.getElementById('playButton');
    const statusTextSpan = document.getElementById('statusText');
    const statusDotSpan = document.getElementById('statusDot');

    const explanationDiv = document.getElementById('explanation');
    const showExplanationButton = document.getElementById('showExplanationButton');

    // --- Utility Functions ---
    function sliderValueToDb(sliderValue) {
        // Maps slider value (0-100) to a dB range (e.g., -40 to 40)
        // Adjust range as needed for perceived loudness
        return minDb + (sliderValue / 100) * (maxDb - minDb);
    }

    function dbToLinear(db) {
        return Math.pow(10, db / 20);
    }

    function updateStatus() {
        if (!isPlaying) {
             statusTextSpan.textContent = 'הדמיה מושהית.';
             statusDotSpan.style.backgroundColor = '#cccccc'; // Grey
             return;
        }

        const maskerVolDb = sliderValueToDb(parseFloat(maskerVolSlider.value));
        const targetVolDb = sliderValueToDb(parseFloat(targetVolSlider.value));
        const maskerFreq = parseFloat(maskerFreqSlider.value);
        const targetFreq = parseFloat(targetFreqSlider.value);

        // Simple heuristic for masking likelihood
        // Calculate frequency difference in a perceptual scale (e.g., octaves or cents)
        // Octave difference: log2(f2/f1)
        const freqRatio = targetFreq / maskerFreq;
        const octaveDiff = Math.abs(Math.log2(freqRatio)); // Use absolute difference for simplicity across direction

        // Masking effect depends on frequency difference and masker volume
        // A very simple model: Auditory threshold is lifted by masker volume, decaying with frequency distance.
        // Threshold increase is roughly proportional to masker volume.
        // It decays significantly as frequency distance increases.
        // Let's assume a base threshold (implicit in minDb), and the masker adds to it.
        // Threshold increase from masker roughly = maskerVolDb - baseThreshold - decay_per_octave * octaveDiff
        // Let's simplify: Target is likely masked if targetVolDb is significantly below maskerVolDb,
        // adjusted by frequency distance.
        const maskingThresholdLift = (maskerVolDb - minDb); // Simplified: masker lifts threshold above base minDb
        const decayPerOctave = 10; // dB decay per octave difference (simplified model)
        const effectiveTargetAudibilityDb = targetVolDb - (maskingThresholdLift - (decayPerOctave * octaveDiff)); // How much louder target is than the *local* masked threshold

        // Categorize based on effective audibility
        if (effectiveTargetAudibilityDb < -5) { // Target is significantly below the likely masked threshold
            statusTextSpan.textContent = 'צליל המטרה כנראה ממוסך ולא נשמע.';
            statusDotSpan.style.backgroundColor = '#d9534f'; // Red
        } else if (effectiveTargetAudibilityDb < 5) { // Target is close to the likely masked threshold
             statusTextSpan.textContent = 'שמיעת צליל המטרה קשה, ייתכן שהוא ממוסך חלקית או מלא.';
             statusDotSpan.style.backgroundColor = '#f0ad4e'; // Orange/Yellow
        } else { // Target is likely above the masked threshold
            statusTextSpan.textContent = 'צליל המטרה נשמע בבירור בנוכחות המסכה.';
            statusDotSpan.style.backgroundColor = '#5cb85c'; // Green
        }

         statusMessage.classList.add('active'); // Add class for potential animation/styling
    }


    // --- Event Listeners ---
    maskerFreqSlider.addEventListener('input', () => {
        const value = maskerFreqSlider.value;
        maskerFreqValueSpan.textContent = value;
        if (isPlaying && maskerOscillator) {
            maskerOscillator.frequency.value = parseFloat(value);
        }
         updateStatus();
    });

    maskerVolSlider.addEventListener('input', () => {
        const value = maskerVolSlider.value;
        maskerVolValueSpan.textContent = value;
        if (isPlaying && maskerGain) {
            const db = sliderValueToDb(parseFloat(value));
            maskerGain.gain.value = dbToLinear(db);
        }
         updateStatus();
    });

    targetFreqSlider.addEventListener('input', () => {
        const value = targetFreqSlider.value;
        targetFreqValueSpan.textContent = value;
        if (isPlaying && targetOscillator) {
            targetOscillator.frequency.value = parseFloat(value);
        }
         updateStatus();
    });

    targetVolSlider.addEventListener('input', () => {
        const value = targetVolSlider.value;
        targetVolValueSpan.textContent = value;
        if (isPlaying && targetGain) {
            const db = sliderValueToDb(parseFloat(value));
            targetGain.gain.value = dbToLinear(db);
        }
         updateStatus();
    });

    playButton.addEventListener('click', () => {
        if (!audioCtx) {
            audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }

        if (!isPlaying) {
             // Attempt to resume context if suspended (necessary for some browsers, like Safari)
            if (audioCtx.state === 'suspended') {
                audioCtx.resume().then(() => {
                   createAndStartAudio();
                }).catch(e => console.error("AudioContext resume failed:", e));
            } else {
                 createAndStartAudio();
            }

        } else {
            stopAudio();
        }
    });

    showExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        // Optional: Change button text
        // showExplanationButton.textContent = isHidden ? 'הסתירו הסבר מעמיק' : 'הסבר מעמיק על מיסוך פסיכואקוסטי';
        showExplanationButton.classList.toggle('active', isHidden); // Add 'active' class when expanded
    });

    // --- Audio Control Functions ---
    function createAndStartAudio() {
         // Create oscillators and gain nodes
            maskerOscillator = audioCtx.createOscillator();
            maskerGain = audioCtx.createGain();
            targetOscillator = audioCtx.createOscillator();
            targetGain = audioCtx.createGain();

            // Set oscillator types (simple sine waves)
            maskerOscillator.type = 'sine';
            targetOscillator.type = 'sine';

            // Set initial frequencies and volumes
            maskerOscillator.frequency.value = parseFloat(maskerFreqSlider.value);
            const maskerDb = sliderValueToDb(parseFloat(maskerVolSlider.value));
            maskerGain.gain.value = dbToLinear(maskerDb);

            targetOscillator.frequency.value = parseFloat(targetFreqSlider.value);
            const targetDb = sliderValueToDb(parseFloat(targetVolSlider.value));
            targetGain.gain.value = dbToLinear(targetDb);


            // Connect the graph
            maskerOscillator.connect(maskerGain);
            maskerGain.connect(audioCtx.destination);

            targetOscillator.connect(targetGain);
            targetGain.connect(audioCtx.destination);

            // Start the oscillators
            maskerOscillator.start();
            targetOscillator.start();

            playButton.textContent = 'הפסיקו את ההדמיה';
            playButton.classList.add('active');
            isPlaying = true;
            updateStatus(); // Update status when starting
    }

     function stopAudio() {
         if (!isPlaying) return;

         // Use a small ramp to avoid clicking sounds
         const rampDuration = 0.1; // seconds
         const stopTime = audioCtx.currentTime + rampDuration;

         if (maskerGain) maskerGain.gain.exponentialRampToValueAtTime(0.00001, stopTime);
         if (targetGain) targetGain.gain.exponentialRampToValueAtTime(0.00001, stopTime);

         // Stop after the ramp
          if (maskerOscillator) maskerOscillator.stop(stopTime);
          if (targetOscillator) targetOscillator.stop(stopTime);

         // Disconnect after stopping
          setTimeout(() => {
             if (maskerOscillator) maskerOscillator.disconnect();
             if (maskerGain) maskerGain.disconnect();
             if (targetOscillator) targetOscillator.disconnect();
             if (targetGain) targetGain.disconnect();
             maskerOscillator = null;
             maskerGain = null;
             targetOscillator = null;
             targetGain = null;
          }, rampDuration * 1000 + 50); // A little longer than the ramp time

         playButton.textContent = 'התחילו את ההדמיה';
         playButton.classList.remove('active');
         isPlaying = false;
         updateStatus(); // Update status when stopping
     }


    // --- Initialization ---
    // Initialize the value spans on load
    maskerFreqValueSpan.textContent = maskerFreqSlider.value;
    maskerVolValueSpan.textContent = maskerVolSlider.value;
    targetFreqValueSpan.textContent = targetFreqSlider.value;
    targetVolValueSpan.textContent = targetVolSlider.value;

    // Initial status message
    updateStatus();


    // Handle potential AudioContext issues on page load (less critical with interaction start)
    // but good practice if context might be created early.
    // The resume() call inside the click handler is more reliable.
    // if (audioCtx && audioCtx.state === 'suspended') {
    //     audioCtx.resume();
    // }


</script>

<style>
    /* General Styles */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        margin: 0;
        padding: 20px;
        background-color: #f8f8f8;
        direction: rtl; /* Ensure overall RTL direction */
        text-align: right; /* Default text alignment */
    }

    h1, h2, h3, h4 {
        color: #1a237e; /* Deep Indigo */
        margin-bottom: 15px;
        text-align: center; /* Center main titles */
    }
     h2, h3, h4 {
         text-align: right; /* Align section titles to the right */
     }

    p {
        margin-bottom: 15px;
        text-align: justify; /* Justify paragraphs for better flow */
    }

    ul {
        padding-right: 20px; /* Add padding for list markers */
        margin-bottom: 15px;
        text-align: right;
    }

    li {
        margin-bottom: 8px;
    }


    /* Simulation Container */
    .simulation-container {
        max-width: 800px;
        margin: 30px auto;
        padding: 30px;
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        border: 1px solid #e0e0e0;
        overflow: hidden; /* Clear floats if any */
    }

    .simulation-container h2 {
         margin-top: 0;
         margin-bottom: 20px;
    }


    /* Controls Layout */
    .controls-container {
        display: flex;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        gap: 25px; /* Space between control groups */
        margin-bottom: 25px;
        padding: 20px;
        background-color: #e8eaf6; /* Light Indigo */
        border-radius: 8px;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
    }

    .control-group {
        flex: 1; /* Allow groups to grow */
        min-width: 280px; /* Minimum width before wrapping */
        padding: 20px;
        border: 1px solid #c5cae9; /* Lighter Indigo */
        border-radius: 8px;
        background-color: #ffffff;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    .control-group h3 {
        color: #3f51b5; /* Indigo */
        margin-top: 0;
        margin-bottom: 15px;
        text-align: center;
    }

    .control-group label {
        display: block; /* Labels on their own line */
        margin-bottom: 8px;
        font-weight: bold;
        color: #555;
        display: flex; /* Use flex to align label and value */
        justify-content: space-between; /* Push value to the other side */
        align-items: center;
    }

    .value-display {
        font-weight: normal;
        color: #1a237e; /* Deep Indigo */
        font-size: 1.1em;
         min-width: 40px; /* Reserve space to prevent jumping */
         text-align: left; /* Align value to the left within its span */
    }

    .control-group input[type="range"] {
        display: block;
        width: 100%; /* Make sliders fill their container */
        margin-top: 5px;
        margin-bottom: 15px;
        -webkit-appearance: none; /* Override default appearance */
        appearance: none;
        height: 8px;
        background: #c5cae9; /* Lighter Indigo track */
        outline: none;
        opacity: 0.7;
        transition: opacity 0.2s ease;
        border-radius: 4px;
    }

    .control-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #3f51b5; /* Indigo thumb */
        cursor: pointer;
        border-radius: 50%;
        transition: background-color 0.2s ease, transform 0.1s ease;
    }

    .control-group input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #3f51b5; /* Indigo thumb */
        cursor: pointer;
        border-radius: 50%;
        transition: background-color 0.2s ease, transform 0.1s ease;
    }

     .control-group input[type="range"]:hover {
         opacity: 1;
     }

     .control-group input[type="range"]::-webkit-slider-thumb:hover {
         background-color: #1a237e; /* Darker Indigo on hover */
         transform: scale(1.1);
     }

     .control-group input[type="range"]::-moz-range-thumb:hover {
         background-color: #1a237e; /* Darker Indigo on hover */
          transform: scale(1.1);
     }


    /* Buttons */
    .action-button, .toggle-button {
        display: block;
        width: 100%;
        padding: 12px 20px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.2s ease;
        text-align: center;
        margin-bottom: 15px;
    }

    .action-button {
        background-color: #4caf50; /* Green */
        color: white;
        box-shadow: 0 4px 8px rgba(76, 175, 80, 0.2);
    }

    .action-button:hover {
        background-color: #388e3c; /* Darker Green */
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(76, 175, 80, 0.3);
    }

     .action-button.active { /* Style when playing */
        background-color: #f44336; /* Red */
        box-shadow: 0 4px 8px rgba(244, 67, 54, 0.2);
     }

    .action-button.active:hover {
        background-color: #d32f2f; /* Darker Red */
        transform: translateY(-2px);
         box-shadow: 0 6px 12px rgba(244, 67, 54, 0.3);
    }


    .toggle-button {
        background-color: #9e9e9e; /* Grey */
        color: white;
        margin-top: 25px;
        margin-bottom: 25px; /* Space below button */
         max-width: 800px;
         margin-left: auto;
         margin-right: auto;
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .toggle-button:hover {
        background-color: #757575; /* Darker Grey */
        transform: translateY(-1px);
         box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
     .toggle-button.active {
         background-color: #616161; /* Even Darker Grey */
     }


    /* Status Indicator */
    .status-indicator {
        text-align: center;
        min-height: 1.5em; /* Reserve space */
        font-style: italic;
        color: #555;
        margin-bottom: 20px;
        display: flex; /* Arrange dot and text inline */
        align-items: center;
        justify-content: center;
        gap: 8px; /* Space between dot and text */
    }

    .status-dot {
        display: inline-block;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background-color: #cccccc; /* Default grey */
        transition: background-color 0.3s ease;
    }

    /* Visual Cue Area (Placeholder Styling) */
    #visual-cue-area {
        margin-top: 25px;
        padding: 20px;
        border: 1px dashed #c5cae9; /* Lighter Indigo dashed border */
        background-color: #f3f4f6; /* Light light grey/blue */
        border-radius: 8px;
        text-align: center; /* Center text in this area */
        color: #5a64c3; /* Indigo text */
    }
     #visual-cue-area h4 {
         margin-top: 0;
         color: #1a237e; /* Deep Indigo */
     }
     #visual-cue-area p {
         margin-bottom: 0;
         text-align: center; /* Ensure paragraph is centered too */
         font-size: 0.95em;
     }


    /* Explanation Section */
    .explanation-section {
        margin-top: 20px;
        padding: 30px;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        background-color: #ffffff;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
        text-align: right;
    }

    .explanation-section h2 {
        color: #1a237e; /* Deep Indigo */
        margin-top: 0;
        margin-bottom: 20px;
         text-align: center;
    }

    .explanation-section h3, .explanation-section h4 {
        margin-top: 20px;
        margin-bottom: 10px;
        color: #3f51b5; /* Indigo */
        border-bottom: 1px solid #e8eaf6; /* Light Indigo border */
        padding-bottom: 5px;
    }
     .explanation-section h4 {
         font-size: 1.1em;
         color: #5a64c3;
         border: none;
         padding-bottom: 0;
     }


    /* Responsive Adjustments */
    @media (max-width: 600px) {
        .simulation-container, .explanation-section {
            padding: 20px;
        }
        .controls-container {
            flex-direction: column; /* Stack controls vertically on small screens */
            gap: 15px;
        }
        .control-group {
            min-width: 100%;
        }
        .action-button, .toggle-button {
            padding: 10px 15px;
            font-size: 0.9em;
        }
    }

</style>
```