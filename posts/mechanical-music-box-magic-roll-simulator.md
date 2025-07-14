---
title: "תיבת הקסם המכנית: סימולטור גלילי מוזיקה"
english_slug: mechanical-music-box-magic-roll-simulator
category: "מוזיקה"
tags:
  - תיבת נגינה
  - מוזיקה אוטומטית
  - גלילי מוזיקה
  - קומפוזיציה מכנית
  - היסטוריה של הטכנולוגיה
  - פיזיקה של סאונד
---
# תיבת הקסם המכנית: סימולטור גלילי מוזיקה

האם דמיינתם פעם שאתם מהנדסי מוזיקה בזמן? כיצד תורגמו מנגינות קסומות לחורים ופינים על חומר פיזי, הרבה לפני עידן החשמל והקוד הדיגיטלי? הצטרפו אלינו למסע אל ליבה של תיבת נגינה מכנית קלאסית, וצרו בעצמכם מנגינות על "גליל" וירטואלי!

<div class="music-box-simulator-container">
    <div class="controls">
        <label for="noteDuration">אורך תו (ב יחידות זמן):</label>
        <select id="noteDuration" title="בחר את משך התו שתיצור בלחיצה">
            <option value="1">מהיר (1)</option>
            <option value="2">קצר (2)</option>
            <option value="4" selected>רגיל (4)</option>
            <option value="8">ארוך (8)</option>
        </select>

        <label for="tempoBpm">קצב (BPM):</label>
        <input type="number" id="tempoBpm" value="120" min="60" max="240" step="10" title="קבע את מהירות הניגון (פעימות לדקה)">

        <button id="playButton" title="נגן את המנגינה שעל הגליל">נגן</button>
        <button id="clearButton" title="נקה את כל התווים מהגליל">נקה הכל</button>
    </div>

    <div class="grid-stage">
        <div class="pitch-labels"></div>
        <div class="grid-container">
            <div id="playbackIndicator" class="playback-indicator"></div>
            <div id="musicRollGrid" class="music-roll-grid"></div>
        </div>
    </div>


    <div class="grid-info">
        <p>
            <span class="info-icon">ⓘ</span>
            לחץ על תא ריק בגליל כדי ליצור תו באורך הנבחר.
            לחץ על תא התחלה של תו קיים כדי למחוק אותו.
            <span class="info-dir">ציר אופקי: זמן (זורם לימין) | ציר אנכי: גובה צליל (עולה כלפי מעלה)</span>
        </p>
    </div>
</div>

<button id="toggleExplanation" class="toggle-button" title="קרא עוד על איך פועלת תיבת נגינה מכנית">הצג הסבר מלא</button>

<div id="explanation" class="explanation" style="display: none;">
    <h2>מסע אל תוך תיבת הנגינה המכנית</h2>
    <p>תיבות נגינה אוטומטיות הן פלא של הנדסה מכנית מוקדמת. הן איפשרו למוזיקה להתנגן "מעצמה", ללא צורך בנגן אנושי בזמן הביצוע. הליבה של מכשירים אלה היא אחסון המידע המוזיקלי בצורה פיזית על גבי גליל, דיסק, או אפילו רצועת נייר מחוררת.</p>

    <h3>הגליל המכני: קידוד של צליל וזמן</h3>
    <p>גלילי המוזיקה היו לרוב עשויים עץ או מתכת, ו"תוכנתו" על ידי הצבת פינים (בליטות קטנות) או יצירת חורים במקומות מדויקים על פני השטח שלהם. כל מיקום ייצג משהו ספציפי:</p>
    <ul>
        <li>**גובה הצליל (Pitch):** המיקום האנכי של הפין/חור על פני הגליל התאים לשן ספציפית ב"מסרק" מתכת (בתיבות נגינה), או למנגנון הפעלה אחר (כמו פטיש בפסנתר מכני). לכל שן יש אורך ומשקל שונים, מה שגורם לה להפיק צליל בגובה שונה כאשר היא רועדת.</li>
        <li>**זמן (Timing):** המיקום האופקי של הפין/חור לאורך היקף הגליל קבע *מתי* התו ינוגן. כשהגליל הסתובב, הפינים/חורים חלפו על פני מנגנון הקריאה בזמן הנכון.</li>
        <li>**משך התו (Duration):** אורך הפין או החור בכיוון סיבוב הגליל קבע לכמה זמן ישוחרר מנגנון הקריאה, ובכך לכמה זמן התו יישמע. פין ארוך יותר או חור ארוך יותר יצרו תו ארוך יותר.</li>
    </ul>
    <p>הסימולטור שלפניכם ממחיש את העיקרון הזה באמצעות רשת (Grid) דו-ממדית, בה ציר ה-X מייצג זמן (הגליל מסתובב) וציר ה-Y מייצג גובה צליל.</p>

    <h3>המנגנון בפעולה</h3>
    <p>כשהגליל מסתובב, הפינים או החורים מפעילים את מנגנון הנגינה. בתיבות נגינה קלאסיות, פין על הגליל דוחף את שן המסרק המתאימה, מותח אותה ומשחרר אותה במהירות. הרעידות של השן המשתחררת הן שמפיקות את הצליל האופייני של תיבת הנגינה. בכלים מורכבים יותר כמו פסנתרים מכניים, חורים ברצועת נייר יכלו להפעיל מנגנון פנאומטי (הפועל על לחץ אוויר) שמניע פטישים לנגינה על מיתרי הפסנתר.</p>

    <h3>האתגר ההנדסי והחשיבות ההיסטורית</h3>
    <p>יצירת גליל מוזיקה הצריכה דיוק רב ותכנון קפדני כדי שהצלילים הנכונים יופיעו בזמן הנכון ובמשך הנכון. מספר התווים היה מוגבל על ידי רוחב הגליל ומספר שיני המסרק, ואורך היצירה היה מוגבל על ידי היקף הגליל. למרות מגבלות אלו, גלילי מוזיקה היו מהאמצעים הראשונים שאפשרו "הקלטה" וניגון של מוזיקה מורכבת באופן אוטומטי, והיוו צעד משמעותי בהתפתחות טכנולוגיות השמע עד לעידן הדיגיטלי.</p>
    <p>עכשיו, כשאתם מבינים את העקרונות, נסו להנדס בעצמכם יצירה קטנה על הגליל הווירטואלי!</p>
</div>

<style>
    :root {
        --primary-color: #6f4e37; /* Coffee/wood brown */
        --secondary-color: #c8a2c8; /* Soft lavender/music box feel */
        --accent-color: #e8d7a1; /* Aged brass/gold */
        --background-light: #f8f8f8;
        --background-dark: #eeeeee;
        --text-color: #333;
        --border-color: #ccc;
        --note-color: var(--secondary-color);
        --note-hover-color: #b08cbe;
        --indicator-color: #e74c3c; /* Red */
    }

    .music-box-simulator-container {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 10px;
        margin: 20px auto;
        max-width: 900px;
        background-color: var(--background-light);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        overflow: hidden; /* Prevent shadow bleed */
    }

    .music-box-simulator-container h1 {
        text-align: center;
        color: var(--primary-color);
        margin-top: 0;
        margin-bottom: 25px;
    }

    .controls {
        margin-bottom: 25px;
        display: flex;
        gap: 20px;
        align-items: center;
        flex-wrap: wrap;
        background-color: var(--background-dark);
        padding: 15px 20px;
        border-radius: 8px;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
    }

    .controls label {
        margin-left: 5px;
        font-size: 0.95rem;
        color: var(--text-color);
    }

    .controls select,
    .controls input[type="number"],
    .controls button {
        padding: 10px 18px;
        border: 1px solid var(--border-color);
        border-radius: 5px;
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.2s ease;
        font-family: 'Arial', sans-serif;
    }

    .controls select:focus,
    .controls input[type="number"]:focus,
    .controls button:focus {
        outline: none;
        border-color: var(--primary-color);
        box-shadow: 0 0 5px rgba(var(--primary-color), 0.3);
    }

    .controls button {
        color: white;
        font-weight: bold;
    }

    .controls button#playButton {
        background-color: #4CAF50; /* Green */
        border-color: #4CAF50;
    }

    .controls button#playButton:hover {
        background-color: #45a049;
        border-color: #45a049;
    }

     .controls button#playButton:active {
         transform: scale(0.98);
     }

    .controls button#clearButton {
        background-color: #f44336; /* Red */
        border-color: #f44336;
    }

    .controls button#clearButton:hover {
        background-color: #da190b;
        border-color: #da190b;
    }
     .controls button#clearButton:active {
         transform: scale(0.98);
     }


    .grid-stage {
        display: flex;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        overflow: hidden; /* Hide scrollbars on this container */
        background-color: #fff;
        box-shadow: inset 0 0 5px rgba(0,0,0,0.05);
    }

    .pitch-labels {
        display: flex;
        flex-direction: column;
        justify-content: flex-end; /* Align labels to bottom */
        padding: 10px 0;
        padding-right: 15px; /* Space for labels */
        background-color: var(--background-dark);
        border-left: 1px solid var(--border-color); /* Separator */
        flex-shrink: 0;
        width: 60px; /* Fixed width for labels */
        text-align: center;
    }

    .pitch-label {
        height: 20px; /* Should match grid row height */
        line-height: 20px;
        font-size: 0.85em;
        color: var(--text-color);
        writing-mode: horizontal-tb;
        direction: ltr; /* Labels are numbers/notes, read LTR */
        overflow: hidden;
        white-space: nowrap;
        opacity: 0.8;
    }


    .grid-container {
        position: relative;
        display: flex; /* Use flex to contain the grid */
        overflow-x: auto; /* Allow horizontal scrolling */
        flex-grow: 1;
         scrollbar-width: thin; /* For Firefox */
         scrollbar-color: var(--primary-color) var(--background-dark); /* For Firefox */
         padding-bottom: 15px; /* Add space for scrollbar */
    }

    /* Custom scrollbar for Chrome/Safari */
    .grid-container::-webkit-scrollbar {
      height: 8px;
    }

    .grid-container::-webkit-scrollbar-track {
      background: var(--background-dark);
      border-radius: 10px;
    }

    .grid-container::-webkit-scrollbar-thumb {
      background: var(--primary-color);
      border-radius: 10px;
    }

    .grid-container::-webkit-scrollbar-thumb:hover {
      background: var(--primary-color);
    }


    .music-roll-grid {
        display: grid;
        grid-auto-flow: column;
        grid-template-rows: repeat(13, 20px); /* 13 pitches, 20px height each */
        grid-auto-columns: 20px; /* Each column is 20px wide (time unit) */
        flex-shrink: 0; /* Prevent shrinking */
        height: calc(13 * 20px); /* Fixed height based on rows */
        position: relative; /* For cell positioning */
    }

    .grid-cell {
        width: 20px;
        height: 20px;
        border: 1px dotted rgba(var(--primary-color), 0.1); /* Light grid lines */
        box-sizing: border-box;
        cursor: pointer;
        background-color: transparent;
        transition: background-color 0.1s ease;
    }

    .grid-cell:hover {
         background-color: rgba(var(--note-color), 0.1);
    }

    .grid-cell.note-start {
        background-color: var(--note-color);
        border-color: var(--note-hover-color);
        position: relative;
        z-index: 2; /* Bring start cell to front */
        box-shadow: 0 0 5px rgba(var(--secondary-color), 0.5);
    }
     .grid-cell.note-start::after {
         content: '';
         position: absolute;
         top: 2px;
         left: 2px;
         right: 2px;
         bottom: 2px;
         border: 1px solid rgba(255,255,255,0.5);
         border-radius: 2px;
     }


    .grid-cell.note-continuation {
         background-color: rgba(var(--note-color), 0.7);
         border-color: var(--note-color);
         z-index: 1; /* Keep continuation cells behind start cells */
     }

     .grid-cell.playing {
         box-shadow: 0 0 8px 2px rgba(var(--accent-color), 0.7);
     }


    .playback-indicator {
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0; /* Will be moved by JS */
        width: 2px;
        background-color: var(--indicator-color);
        z-index: 10;
        display: none;
        pointer-events: none;
        transition: left linear; /* Smooth transition, speed set by JS tempo */
    }

    .grid-info {
        margin-top: 25px;
        font-size: 0.9em;
        color: var(--text-color);
        text-align: right;
        line-height: 1.6;
        border-top: 1px solid var(--background-dark);
        padding-top: 15px;
    }

    .grid-info .info-icon {
        color: var(--primary-color);
        margin-left: 5px;
        font-weight: bold;
    }

    .grid-info .info-dir {
        display: block;
        margin-top: 5px;
        font-size: 0.85em;
        color: #555;
    }


    .toggle-button {
        display: block;
        margin: 30px auto 20px;
        padding: 12px 25px;
        font-size: 1rem;
        cursor: pointer;
        border: 1px solid var(--border-color);
        border-radius: 5px;
        background-color: var(--background-dark);
        color: var(--text-color);
        transition: background-color 0.2s ease, border-color 0.2s ease;
    }

    .toggle-button:hover {
        background-color: #e0e0e0;
        border-color: #bbb;
    }
    .toggle-button:active {
         transform: scale(0.98);
     }


    .explanation {
        border: 1px solid var(--border-color);
        padding: 25px;
        margin-top: 20px;
        border-radius: 8px;
        background-color: var(--background-light);
        text-align: right;
        direction: rtl;
        line-height: 1.7;
        color: var(--text-color);
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    }

    .explanation h2 {
        margin-top: 0;
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 20px;
    }

    .explanation h3 {
        margin-top: 20px;
        margin-bottom: 10px;
        color: #555;
        border-bottom: 1px dotted var(--border-color);
        padding-bottom: 5px;
    }

    .explanation p {
        margin-bottom: 15px;
    }

    .explanation ul {
        margin-bottom: 15px;
        padding-right: 20px;
    }

    .explanation li {
        margin-bottom: 8px;
    }
</style>

<script src="https://unpkg.com/tone"></script>
<script>
    const gridElement = document.getElementById('musicRollGrid');
    const pitchLabelsElement = document.querySelector('.pitch-labels');
    const playButton = document.getElementById('playButton');
    const clearButton = document.getElementById('clearButton');
    const noteDurationSelect = document.getElementById('noteDuration');
    const tempoBpmInput = document.getElementById('tempoBpm');
    const playbackIndicator = document.getElementById('playbackIndicator');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');

    const numRows = 13; // Number of pitches
    const numCols = 128; // Number of time units (columns)
    // Map row index (0-based, top to bottom in grid) to Note Name
    // Reversed so row 0 is highest pitch, row 12 is lowest (like sheet music)
    const noteMap = [
        'A5', 'G5', 'F5', 'E5', 'D5', 'C5', 'B4',
        'A4', 'G4', 'F4', 'E4', 'D4', 'C4'
    ];
    // Hebrew labels matching the noteMap order
    const pitchesHebrew = [
        'לה5', 'סול5', 'פה5', 'מי5', 'רה5', 'דו5', 'סי4',
        'לה4', 'סול4', 'פה4', 'מי4', 'רה4', 'דו4'
    ];

    // Store note data: Array of [row, startCol, duration]
    const gridData = [];

    // Setup Tone.js synth, aiming for a music box sound
    // Use a SimpleSynth with tweaked envelope and add reverb
    let synth = new Tone.Synth({
        oscillator: { type: 'amsine', modulationType: 'sine', harmonicity: 1.001 }, // Subtle detune/texture
        envelope: {
            attack: 0.005,
            decay: 0.1,
            sustain: 0.05,
            release: 0.2,
        },
        volume: -10 // Slightly reduce volume
    });

    // Add Reverb effect
    const reverb = new Tone.Reverb({
        decay: 1.5, // Amount of reverberation
        preDelay: 0.01,
        wet: 0.4 // Mix level (0 to 1)
    }).toDestination();

    // Connect synth to reverb, then reverb to master output
    synth.connect(reverb);


    // Tone.js Transport setup
    let timeUnit = '16n'; // Define the musical length of one grid column (e.g., 16th note)
    Tone.Transport.bpm.value = parseInt(tempoBpmInput.value);
    Tone.Transport.loop = false; // Don't loop by default

    // Initialize Grid and Pitch Labels
    function initializeGrid() {
        gridElement.innerHTML = ''; // Clear previous grid
        pitchLabelsElement.innerHTML = ''; // Clear previous labels
        gridData.length = 0; // Clear grid data array

        // Create Pitch Labels (matches noteMap order)
        for (let i = 0; i < numRows; i++) {
             const label = document.createElement('div');
             label.classList.add('pitch-label');
             // Display labels according to the reversed noteMap (top=high pitch, bottom=low pitch)
             label.textContent = pitchesHebrew[i];
             pitchLabelsElement.appendChild(label);
         }

        // Create Grid Cells
        for (let i = 0; i < numRows; i++) { // Rows (Pitches)
            for (let j = 0; j < numCols; j++) { // Columns (Time)
                const cell = document.createElement('div');
                cell.classList.add('grid-cell');
                cell.dataset.row = i;
                cell.dataset.col = j;
                cell.addEventListener('click', handleCellClick);
                gridElement.appendChild(cell);
            }
        }

        // Adjust grid columns style based on numCols
        gridElement.style.gridTemplateColumns = `repeat(${numCols}, 20px)`;
         // Ensure indicator starts at 0
        playbackIndicator.style.left = '0px';
        playbackIndicator.style.display = 'none';
    }

     // Redraw all notes stored in gridData onto the visual grid
     function redrawGrid() {
         // Clear all existing note classes
         gridElement.querySelectorAll('.grid-cell').forEach(cell => {
             cell.classList.remove('note-start', 'note-continuation', 'playing');
         });

         // Draw notes from gridData
         gridData.forEach(note => {
             const [row, startCol, duration] = note;
             drawNoteOnGrid(row, startCol, duration);
         });
     }

    // Draw a note on the grid (fill cells)
    function drawNoteOnGrid(row, startCol, duration) {
        for (let i = 0; i < duration; i++) {
            const currentCellCol = startCol + i;
            if (currentCellCol < numCols) {
                const cell = gridElement.querySelector(`.grid-cell[data-row="${row}"][data-col="${currentCellCol}"]`);
                if (cell) {
                    if (i === 0) {
                        cell.classList.add('note-start');
                    } else {
                        cell.classList.add('note-continuation');
                    }
                     // Remove playing class if present (it's added during playback)
                     cell.classList.remove('playing');
                }
            }
        }
    }

    // Clear a note from the grid (unfill cells)
    function clearNoteFromGrid(row, startCol, duration) {
         for (let i = 0; i < duration; i++) {
            const currentCellCol = startCol + i;
            if (currentCellCol < numCols) {
                const cell = gridElement.querySelector(`.grid-cell[data-row="${row}"][data-col="${currentCellCol}"]`);
                 if (cell) {
                    cell.classList.remove('note-start', 'note-continuation', 'playing');
                }
            }
        }
    }

    // Handle Cell Click
    function handleCellClick(event) {
        const cell = event.target;
        const row = parseInt(cell.dataset.row);
        const col = parseInt(cell.dataset.col);
        const duration = parseInt(noteDurationSelect.value);

        // Find if a note STARTING at this cell exists
        const existingNoteIndex = gridData.findIndex(note =>
            note[0] === row && note[1] === col
        );

        if (existingNoteIndex !== -1) {
            // If a note starts here, remove it
            const [existingRow, existingCol, existingDuration] = gridData[existingNoteIndex];
            gridData.splice(existingNoteIndex, 1);
            clearNoteFromGrid(existingRow, existingCol, existingDuration);
        } else {
             // If no note starts here, try to add a new one
             // Check if any cell in the *proposed* note's span is already occupied by *any* note
             let isOccupied = false;
             for(let i = 0; i < duration; i++) {
                 const checkCol = col + i;
                 if (checkCol >= numCols) {
                     // Proposed note goes beyond the grid
                     isOccupied = true;
                     break;
                 }
                 const occupiedCell = gridElement.querySelector(`.grid-cell[data-row="${row}"][data-col="${checkCol}"]`);
                 if (occupiedCell && occupiedCell.classList.contains('note-start') || occupiedCell.classList.contains('note-continuation')) {
                     isOccupied = true;
                     break;
                 }
             }

             if (!isOccupied) {
                 // If the space is clear, add the new note
                 gridData.push([row, col, duration]);
                 drawNoteOnGrid(row, col, duration);
             } else {
                 // Optional: Add visual feedback for failed placement (e.g., shake cell)
                 cell.style.animation = 'shake 0.3s';
                 cell.addEventListener('animationend', () => {
                     cell.style.animation = '';
                 }, { once: true });
             }
        }
    }

    // Schedule notes for playback
    function scheduleNotes() {
        // Clear any existing scheduled events
        Tone.Transport.cancel();

        // Time Unit based on grid column width (e.g., 1 column = 16th note)
        const columnTimeUnit = timeUnit; // '16n'

        gridData.forEach(note => {
            const [row, startCol, duration] = note;
            // Map row to pitch using the corrected noteMap
            const pitch = noteMap[row];
            const startTime = `+${startCol * Tone.Time(columnTimeUnit).toSeconds()}`; // Start time relative to Transport.start()
            const noteDuration = `${duration * Tone.Time(columnTimeUnit).toSeconds()}s`; // Duration in seconds

            // Schedule the note to be played
            Tone.Transport.schedule(time => {
                synth.triggerAttackRelease(pitch, noteDuration, time);

                 // Schedule visual feedback (highlight cells) using Tone.Draw for synchronization
                 Tone.Draw.schedule(() => {
                      // Find all cells for this note
                     for(let i = 0; i < duration; i++) {
                         const cell = gridElement.querySelector(`.grid-cell[data-row="${row}"][data-col="${startCol + i}"]`);
                         if (cell) {
                             cell.classList.add('playing');
                             // Remove playing class after a short delay (slightly longer than note decay)
                             setTimeout(() => {
                                cell.classList.remove('playing');
                             }, Tone.Time(noteDuration).toMilliseconds() + 100); // Add small buffer
                         }
                     }
                 }, time);

            }, startTime);
        });

         // Schedule updates for the indicator for every column
         const totalTime = numCols * Tone.Time(columnTimeUnit).toSeconds();
         for (let col = 0; col <= numCols; col++) { // Include numCols for end position
             const time = col * Tone.Time(columnTimeUnit).toSeconds();
              Tone.Transport.schedule(time => {
                  Tone.Draw.schedule(() => {
                      updatePlaybackIndicator(col);
                  }, time);
              }, `+${time}`); // Use relative time + for scheduling after start
         }

         // Schedule stopping the indicator and reset at the end
          Tone.Transport.schedule(time => {
              Tone.Draw.schedule(() => {
                   playbackIndicator.style.display = 'none';
                   playbackIndicator.style.left = '0px'; // Reset position
                   playButton.textContent = 'נגן'; // Reset button text
                   // Scroll grid back to start if it was scrolled
                   gridElement.scrollTo({ left: 0, behavior: 'smooth' });
                   redrawGrid(); // Ensure all 'playing' classes are removed
              }, time);

              // Stop the Transport slightly after the visual reset
               Tone.Transport.stop();
               Tone.Transport.start(); // Re-arm the transport in stopped state
               Tone.Transport.pause(); // Ensure it's paused after re-arming

          }, `+${totalTime + Tone.Time(columnTimeUnit).toSeconds()}`); // Schedule slightly after the last column time


         // Ensure transport starts paused initially for first play
         if (Tone.Transport.state !== 'started') {
            Tone.Transport.start();
            Tone.Transport.pause(); // Start paused
         }
    }

    // Update playback indicator position and scroll the grid
    function updatePlaybackIndicator(col) {
        const cellWidth = 20; // px (matches CSS grid-auto-columns)
        const indicatorPosition = col * cellWidth;
        playbackIndicator.style.left = `${indicatorPosition}px`;
        playbackIndicator.style.display = 'block'; // Show indicator

        // Set transition duration based on tempo for smooth movement
        // Time to move one column = Tone.Time(columnTimeUnit).toSeconds()
        const transitionDuration = Tone.Time(timeUnit).toSeconds() * 1000; // in milliseconds
        playbackIndicator.style.transitionDuration = `${transitionDuration}ms`;


        // Scroll grid to keep indicator visible
        const containerWidth = gridElement.offsetWidth;
        const scrollLeft = gridElement.scrollLeft;
        const scrollThreshold = containerWidth * 0.3; // Scroll when indicator is within 30% from edge

        if (indicatorPosition > scrollLeft + containerWidth - scrollThreshold) {
             gridElement.scrollTo({
                 left: indicatorPosition - containerWidth + scrollThreshold,
                 behavior: 'smooth'
             });
         } else if (indicatorPosition < scrollLeft + scrollThreshold && scrollLeft > 0) {
             gridElement.scrollTo({
                 left: indicatorPosition - scrollThreshold,
                 behavior: 'smooth'
             });
         } else if (col === 0 && scrollLeft > 0) { // Scroll back to start forcefully at the beginning
              gridElement.scrollTo({
                  left: 0,
                  behavior: 'smooth'
              });
         }
    }


    // Play Button Handler
    playButton.addEventListener('click', async () => {
        // Tone.js requires starting its context on a user gesture
        if (Tone.context.state !== 'running') {
            await Tone.start();
             console.log('Audio context started');
        }

        if (Tone.Transport.state === 'paused' || Tone.Transport.state === 'stopped') {
             scheduleNotes(); // Reschedule in case notes were added/removed/tempo changed
             // Start playback from current Transport position (usually 0 if stopped/paused at start)
             Tone.Transport.start(Tone.now()); // Start immediately
             playButton.textContent = 'השהה';
              // Ensure indicator starts at the correct position if paused mid-playback (optional, requires tracking transport.position)
              // For simplicity, we'll just reset to 0 on stop/clear. On pause, indicator stays.
             playbackIndicator.style.display = 'block';
         } else if (Tone.Transport.state === 'started') {
             Tone.Transport.pause();
             playButton.textContent = 'נגן';
             playbackIndicator.style.display = 'none'; // Hide indicator on pause
         }
    });

     // Clear Button Handler
     clearButton.addEventListener('click', () => {
         Tone.Transport.stop();
         Tone.Transport.cancel();
         gridData.length = 0; // Clear all notes
         redrawGrid(); // Clear visual notes
         playButton.textContent = 'נגן';
         playbackIndicator.style.display = 'none';
         playbackIndicator.style.left = '0px';
         gridElement.scrollTo({ left: 0, behavior: 'smooth' }); // Scroll back to start
     });

    // Tempo Input Handler
    tempoBpmInput.addEventListener('input', () => {
        const newBpm = parseInt(tempoBpmInput.value);
        if (!isNaN(newBpm) && newBpm >= 60 && newBpm <= 240) {
             Tone.Transport.bpm.value = newBpm;
             // Reschedule if playing, or just update tempo for next play
             if (Tone.Transport.state === 'started') {
                 // Stopping and restarting might be jarring, better to let the tempo change take effect mid-playback if possible
                 // Tone.js handles BPM changes dynamically, so no need to reschedule immediately unless the grid logic depends on fixed time values
                 // Our grid logic uses column index -> time, which adapts to BPM changes naturally.
             }
        } else {
             // Optional: provide feedback for invalid input
             console.warn("Invalid BPM value");
        }
    });


    // Toggle Explanation Button Handler
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מלא' : 'הצג הסבר מלא';
         // Scroll to the explanation if showing it
         if (!isHidden) {
              explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });


    // Initial setup
    initializeGrid();

    // Basic CSS animation for cell shake feedback
    const styleSheet = document.styleSheets[0];
    const shakeAnimation = `
        @keyframes shake {
            0% { transform: translateX(0); }
            25% { transform: translateX(-2px); }
            50% { transform: translateX(2px); }
            75% { transform: translateX(-2px); }
            100% { transform: translateX(0); }
        }
    `;
    styleSheet.insertRule(shakeAnimation, styleSheet.cssRules.length);


</script>
```