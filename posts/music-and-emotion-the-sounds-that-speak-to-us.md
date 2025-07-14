---
title: "הצלילים שמדברים אליכם: איך מוזיקה מעוררת רגש?"
english_slug: music-and-emotion-the-sounds-that-speak-to-us
category: "אמנות ועיצוב / מוזיקה"
tags: מוזיקה, רגש, סולמות, הרמוניה, פסיכולוגיה של המוזיקה, אינטראקטיבי
---
<div class="interactive-music-experience">
    <h1>הצלילים שמדברים אליכם: איך מוזיקה מעוררת רגש?</h1>
    <p class="intro-text">למה צלילים מסוימים גורמים לנו לרצות לרקוד, ואחרים גורמים לעצב להתגנב ללב? האם זה קסם או מדע? בואו נשחק קצת עם אבני הבניין של המוזיקה ונגלה יחד איך הצלילים משפיעים עלינו.</p>

    <div id="music-playground-container" class="app-container">
        <h2>בנו את המנגינה שלכם וחוו את הקסם!</h2>

        <div class="visualizer-container">
             <div id="music-visualizer" class="visualizer"></div>
        </div>


        <div class="controls-panel">
            <div class="control-group">
                <label class="control-label">סוג הסולם:</label>
                <div class="radio-group">
                    <div>
                        <input type="radio" id="scale-major" name="scale" value="major" checked>
                        <label for="scale-major">מז'ור (שמח/בהיר)</label>
                    </div>
                    <div>
                        <input type="radio" id="scale-minor" name="scale" value="minor">
                        <label for="scale-minor">מינור (עצוב/קודר)</label>
                    </div>
                </div>
            </div>

            <div class="control-group slider-control">
                <label for="tempo-slider" class="control-label">קצב (טמפו - BPM):</label>
                 <input type="range" id="tempo-slider" min="60" max="180" value="100">
                <span id="tempo-value" class="slider-value">100</span> פעימות בדקה
            </div>

            <div class="control-group">
                <input type="checkbox" id="add-dissonance">
                <label for="add-dissonance">הוסיפו נגיעה של מתח (דיסוננס)</label>
            </div>
        </div>

        <button id="play-button" class="app-button play-button">התחילו לנגן</button>

        <div class="emotion-feedback">
            <label for="emotion-slider" class="control-label">איך המנגינה הזו גורמת לכם להרגיש?</label>
            <input type="range" id="emotion-slider" min="0" max="100" value="50">
            <div class="emotion-labels">
                <span>עצוב מאוד 😥</span>
                <span>ניטרלי 😐</span>
                <span>שמח מאוד 😁</span>
            </div>
        </div>
    </div>

    <button id="toggle-explanation" class="app-button explanation-button">רוצים להבין יותר לעומק? לחצו כאן להסבר המלא</button>

    <div id="explanation" class="explanation-section" style="display: none;">
        <h2>הסבר עמוק יותר: צלילים, מבנה, וים של רגש</h2>

        <p>מוזיקה היא שפה אוניברסלית שמשפיעה עלינו ברבדים עמוקים. אבל איך בדיוק היא עושה את זה? בואו נצלול לאבני הבניין שלה:</p>

        <h3>אבני הבניין המרכזיות: לא רק תווים בודדים</h3>
        <ul>
            <li><strong>תווים וסולמות:</strong> תו הוא צליל בגובה מסוים. סולם הוא סדרה מסודרת של תווים (כמו דו-רה-מי-פא-סול-לה-סי-דו). הסולמות הם כמו הפלטה של הצבעים שהמלחין בוחר לעבוד איתה.</li>
            <li><strong>אקורדים והרמוניה:</strong> כשאנחנו משמיעים מספר תווים יחד, אנחנו יוצרים אקורד. רצף של אקורדים יוצר הרמוניה. ההרמוניה היא כמו הרקע התמונה המוזיקלית, והיא משפיעה מאוד על התחושה הכללית.</li>
            <li><strong>קצב (טמפו ומקצב):</strong> הקצב הוא פעימות הלב של המוזיקה - המהירות והאופן שבו הצלילים מסודרים בזמן. הוא משפיע ישירות על האנרגיה והתנועה.</li>
        </ul>

        <h3>הסוד של מז'ור ומינור: במרווחים הקטנים טמונה ההרגשה</h3>
        <p>ההבדל המהותי בין סולם מז'ורי למינורי מסתתר ב"מרווח" בין התו הראשון לשלישי בסולם (הנקרא "טרצה"). טרצה גדולה (רחבה יותר) אופיינית לסולמות מז'וריים ויוצרת תחושה של פתיחות, יציבות ושמחה. טרצה קטנה (צרה יותר) אופיינית לסולמות מינוריים ויוצרת תחושה של התכנסות, רצינות או עצב. זו לא רק מוסכמה תרבותית; יש לכך גם הסבר אקוסטי הקשור לצלילים "הנסתרים" בתוך כל תו (הרמוניות עיליות).</p>

        <h3>הקצב: מנוע הרגש והאנרגיה</h3>
        <p>נסו לדמיין שיר אהבה עצוב בקצב מהיר, או שיר מסיבה שמח בקצב איטי להחריד. זה לא עובד, נכון? הקצב הוא גורם מכריע: טמפו מהיר מעורר וממריץ, ומקושר לרוב לשמחה, התרגשות, או מתח קופצני. טמפו איטי מרגיע או מעמיק תחושות כמו רוגע, עצב, מלנכוליה או חגיגיות רצינית.</p>

        <h3>מתח ושחרור: כוחם של הקונסוננס והדיסוננס</h3>
        <p>שילובים הרמוניים יכולים להיות "קונסוננטיים" (נעימים, יציבים, "נשמעים טוב יחד") או "דיסוננטיים" (מתוחים, צורמים יחסית, דורשים "פתרון" למקום יציב יותר). האוזן האנושית (ולמעשה, הפיזיקה של הצליל) שואפת בדרך כלל ממתח (דיסוננס) לשחרור (קונסוננס). השימוש המיומן בדיסוננס יוצר מתח, ציפייה, ואף חוסר נוחות קלה, שמתחלפים בתחושת סיפוק כשההרמוניה "נפתרת". זהו כלי עוצמתי ביצירת תנועה דרמטית והבעה רגשית עשירה.</p>

        <h3>מעבר למבנה: הסיפור השלם</h3>
        <p>כמובן, מוזיקה היא הרבה יותר מסכום חלקיה. גם המלודיה (המנגינה הראשית), הדינמיקה (עוצמות), גוון הצליל של הכלים (טימבר), הארטיקולציה (איך מנגנים/שרים את התווים), ומבנה היצירה הכולל - כולם תורמים לתמונה הרגשית המלאה. בנוסף, הניסיון האישי וההקשר התרבותי שלנו משפיעים עמוקות על האופן שבו אנו מפרשים ומרגישים מוזיקה.</p>

        <h3>מדע הרגש: מה קורה לנו במוח?</h3>
        <p>מחקרים בפסיכולוגיה ונוירו-מדע מגלים שמוזיקה מפעילה מגוון רחב של אזורים במוח, כולל אלו הקשורים לעיבוד רגשות, זיכרון, ואפילו תנועה. האזנה למוזיקה יכולה להשפיע על קצב הלב, הנשימה, ואף להוביל לשחרור דופמין, מוליך עצבי הקשור להנאה ותגמול. הקשר בין מבנה מוזיקלי לתגובה פיזיולוגית ורגשית אינו מקרי, אלא נובע מאינטראקציה מורכבת בין המאפיינים הפיזיקליים של הצליל, המבנה האנטומי של האוזן והמוח, והלמידה התרבותית שלנו.</p>

        <p>עכשיו, אחרי שהבנתם קצת יותר על מאחורי הקלעים, חזרו לשחק עם המנגינה ושימו לב איך כל שינוי קטן משפיע על ההרגשה שלכם!</p>

    </div>
</div>

<style>
    :root {
        --primary-color: #6A057F; /* Deep Purple */
        --secondary-color: #88399D; /* Lighter Purple */
        --accent-color-major: #4CAF50; /* Green for Major */
        --accent-color-minor: #F44336; /* Red for Minor */
        --accent-color-dissonance: #FF9800; /* Orange for Dissonance */
        --text-color: #333;
        --bg-color-light: #F3E5F5; /* Very Light Purple */
        --bg-color-darker: #E1BEE7; /* Slightly Darker Purple */
        --control-bg: #FFFFFF;
        --border-color: #D1C4E9;
        --button-bg: var(--primary-color);
        --button-text: white;
        --button-hover: var(--secondary-color);
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        direction: rtl;
        text-align: right;
        background-color: var(--bg-color-light);
        color: var(--text-color);
        overflow-x: hidden; /* Prevent horizontal scroll on animations */
    }

    .interactive-music-experience {
         max-width: 800px;
         margin: 20px auto;
         background-color: #fff;
         padding: 30px;
         border-radius: 12px;
         box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
         border: 1px solid var(--border-color);
    }


    h1, h2, h3 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 20px;
        line-height: 1.4;
    }

    h1 {
        font-size: 2.2em;
        margin-bottom: 10px;
    }

    h2 {
        font-size: 1.8em;
        margin-top: 25px;
    }

    h3 {
         font-size: 1.4em;
         margin-top: 20px;
         margin-bottom: 10px;
         color: var(--secondary-color);
    }

    .intro-text {
        text-align: center;
        font-size: 1.1em;
        margin-bottom: 30px;
        color: #555;
    }

    .app-container {
        background-color: var(--bg-color-darker);
        padding: 30px;
        border-radius: 10px;
        margin-bottom: 30px;
        border: 1px solid var(--border-color);
        position: relative; /* Needed for visualizer absolute positioning */
        overflow: hidden; /* Hide visualizer overflow */
    }

     .visualizer-container {
        height: 150px; /* Fixed height for visualizer */
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px;
        position: relative;
    }

    .visualizer {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        background-color: var(--accent-color-major); /* Default */
        opacity: 0.7;
        transition: all 0.4s ease-out;
        transform-origin: center;
        box-shadow: 0 0 20px rgba(0,0,0,0.2);
    }

    .visualizer.minor {
        background-color: var(--accent-color-minor);
    }

    .visualizer.dissonance {
        box-shadow: 0 0 25px 10px var(--accent-color-dissonance), 0 0 40px 15px rgba(255, 152, 0, 0.5);
        /* animation: pulsate-dissonance 1s infinite alternate ease-in-out; */ /* Maybe too distracting? */
    }

    @keyframes pulsate-dissonance {
        from { box-shadow: 0 0 25px 10px var(--accent-color-dissonance), 0 0 40px 15px rgba(255, 152, 0, 0.5); }
        to { box-shadow: 0 0 30px 12px var(--accent-color-dissonance), 0 0 50px 20px rgba(255, 152, 0, 0.7); }
    }

    .controls-panel {
        display: flex;
        flex-direction: column;
        gap: 20px;
        margin-bottom: 30px;
    }

    .control-group {
        background-color: var(--control-bg);
        padding: 20px;
        border-radius: 8px;
        border: 1px solid var(--border-color);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }

    .control-label {
        display: block;
        margin-bottom: 10px;
        font-weight: bold;
        color: var(--primary-color);
        font-size: 1.1em;
    }

    .radio-group div {
        margin-bottom: 8px;
    }

     .radio-group label {
         font-weight: normal;
         color: var(--text-color);
         cursor: pointer;
     }

    input[type="radio"], input[type="checkbox"] {
        margin-left: 5px; /* Space between input and label */
        vertical-align: middle;
    }

    .slider-control input[type="range"] {
        width: calc(100% - 60px); /* Make slider take most space */
        vertical-align: middle;
        margin-left: 10px;
    }

     .slider-control .slider-value {
        display: inline-block;
        width: 40px;
        text-align: center;
        font-weight: bold;
        color: var(--primary-color);
     }


    .app-button {
        display: block;
        width: 100%;
        padding: 12px;
        font-size: 1.2em;
        font-weight: bold;
        background-color: var(--button-bg);
        color: var(--button-text);
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .app-button:hover {
        background-color: var(--button-hover);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

    .app-button:active {
        background-color: var(--primary-color);
        transform: scale(0.98);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .play-button {
         margin-bottom: 20px;
         background-color: var(--accent-color-major);
         color: white;
    }

     .play-button:hover {
         background-color: #449d44; /* Darker Green */
     }

     .play-button:active {
         background-color: #398439; /* Even Darker Green */
     }


    .emotion-feedback {
        margin-top: 30px;
        padding: 20px;
        background-color: var(--bg-color-light);
        border-radius: 8px;
        border: 1px solid var(--border-color);
    }

    .emotion-feedback label {
        display: block;
        margin-bottom: 15px;
        font-weight: bold;
        text-align: center;
        font-size: 1.1em;
        color: var(--primary-color);
    }

    .emotion-feedback input[type="range"] {
        width: 100%;
        -webkit-appearance: none; /* Override default slider appearance */
        appearance: none;
        height: 10px;
        background: linear-gradient to left, var(--accent-color-minor), #ffeb3b, var(--accent-color-major)); /* Color gradient */
        background: -moz-linear-gradient(right, var(--accent-color-major), #ffeb3b, var(--accent-color-minor)); /* Firefox */
        background: -webkit-linear-gradient(right, var(--accent-color-major), #ffeb3b, var(--accent-color-minor)); /* Chrome, Safari */
        border-radius: 5px;
        outline: none;
        opacity: 0.9;
        transition: opacity 0.2s;
    }

    .emotion-feedback input[type="range"]:hover {
        opacity: 1;
    }

    .emotion-feedback input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        border: 2px solid white;
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    .emotion-feedback input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        border: 2px solid white;
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }


    .emotion-labels {
        display: flex;
        justify-content: space-between;
        font-size: 0.9em;
        margin-top: 8px;
        color: #555;
    }

    .explanation-button {
        margin-top: 20px;
        margin-bottom: 20px;
        background-color: var(--secondary-color);
    }

     .explanation-button:hover {
         background-color: #7B248D;
     }


    .explanation-section {
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid var(--border-color);
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
    }

    .explanation-section p {
         margin-bottom: 15px;
         color: #444;
         text-align: right;
    }

     .explanation-section ul {
        margin-bottom: 15px;
        padding-right: 20px; /* Add padding for list markers */
     }

     .explanation-section li {
        margin-bottom: 8px;
     }

     .explanation-section strong {
        color: var(--primary-color);
     }

    /* Responsive Adjustments */
    @media (max-width: 600px) {
        body {
            padding: 10px;
        }

        .interactive-music-experience {
            padding: 20px;
        }

        h1 {
            font-size: 1.8em;
        }

        h2 {
            font-size: 1.5em;
        }

        .app-button {
            font-size: 1em;
            padding: 10px;
        }

         .control-group {
             padding: 15px;
         }
         .control-label {
             font-size: 1em;
         }
         .slider-control input[type="range"] {
             width: calc(100% - 50px);
         }
         .slider-control .slider-value {
             width: 35px;
         }
    }

</style>

<script src="https://cdn.jsdelivr.net/npm/tone@14.7.58/build/Tone.min.js"></script>
<script>
    let polySynth = null; // Will be initialized on first play

    const playButton = document.getElementById('play-button');
    const scaleMajorRadio = document.getElementById('scale-major');
    const scaleMinorRadio = document.getElementById('scale-minor');
    const tempoSlider = document.getElementById('tempo-slider');
    const tempoValueSpan = document.getElementById('tempo-value');
    const addDissonanceCheckbox = document.getElementById('add-dissonance');
    const emotionSlider = document.getElementById('emotion-slider'); // User input, no JS logic needed for playback
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const visualizer = document.getElementById('music-visualizer');
    const appContainer = document.getElementById('music-playground-container'); // Use this for checking state/classes

    let currentSequence = null;
    let isPlaying = false;

    // More musical note sequences (using Tone.js time format)
    // This sequence loosely follows a I - vi - IV - V progression
    const majorSequenceData = [
        // C Major arpeggio/chord feel
        { time: '0:0:0', note: 'C4', duration: '4n' },
        { time: '0:0:7', note: 'E4', duration: '4n' },
        { time: '0:1:4', note: 'G4', duration: '4n' },
        { time: '0:2:0', note: 'E4', duration: '4n' },

        // A Minor arpeggio/chord feel
        { time: '1:0:0', note: 'A4', duration: '4n' },
        { time: '1:0:7', note: 'C5', duration: '4n' },
        { time: '1:1:4', note: 'E5', duration: '4n' },
        { time: '1:2:0', note: 'C5', duration: '4n' },

        // F Major arpeggio/chord feel
        { time: '2:0:0', note: 'F4', duration: '4n' },
        { time: '2:0:7', note: 'A4', duration: '4n' },
        { time: '2:1:4', note: 'C5', duration: '4n' },
        { time: '2:2:0', note: 'A4', duration: '4n' },

        // G Major arpeggio/chord feel (leading to C)
        { time: '3:0:0', note: 'G4', duration: '4n' },
        { time: '3:0:7', note: 'B4', duration: '4n' },
        { time: '3:1:4', note: 'D5', duration: '4n' },
        { time: '3:2:0', note: 'B4', duration: '4n' },

        // Final C Major resolution
        { time: '4:0:0', note: 'C5', duration: '1m' }
    ];

    const minorSequenceData = [
        // C Minor arpeggio/chord feel
        { time: '0:0:0', note: 'C4', duration: '4n' },
        { time: '0:0:7', note: 'Eb4', duration: '4n' },
        { time: '0:1:4', note: 'G4', duration: '4n' },
        { time: '0:2:0', note: 'Eb4', duration: '4n' },

        // Ab Major arpeggio/chord feel (relative major of C minor's parallel major - used often) or F Minor (iv)
         // Let's use Ab Major (VI chord) for a more common minor key feel
        { time: '1:0:0', note: 'Ab4', duration: '4n' },
        { time: '1:0:7', note: 'C5', duration: '4n' },
        { time: '1:1:4', note: 'Eb5', duration: '4n' },
        { time: '1:2:0', note: 'C5', duration: '4n' },

        // F Minor arpeggio/chord feel (iv chord)
        { time: '2:0:0', note: 'F4', duration: '4n' },
        { time: '2:0:7', note: 'Ab4', duration: '4n' },
        { time: '2:1:4', note: 'C5', duration: '4n' },
        { time: '2:2:0', note: 'Ab4', duration: '4n' },


        // G Major (Dominant V chord in Minor, uses B natural)
        { time: '3:0:0', note: 'G4', duration: '4n' },
        { time: '3:0:7', note: 'B4', duration: '4n' }, // Leading tone to C
        { time: '3:1:4', note: 'D5', duration: '4n' },
        { time: '3:2:0', note: 'B4', duration: '4n' },


        // Final C Minor resolution
        { time: '4:0:0', note: 'C5', duration: '1m' } // Could be Cm chord: ['C4', 'Eb4', 'G4']
    ];

    const dissonanceMajorInsert = { time: '3:3:0', note: ['G4', 'C#5', 'F#5'], duration: '4n' }; // Add a dissonant chord/notes before final resolution
     const dissonanceMinorInsert = { time: '3:3:0', note: ['G4', 'D#5', 'A5'], duration: '4n' }; // Another dissonant option in minor

    function createSequence() {
         const isMajor = scaleMajorRadio.checked;
         let sequenceBase = isMajor ? [...majorSequenceData] : [...minorSequenceData]; // Create a copy
         const addDissonance = addDissonanceCheckbox.checked;

         if (addDissonance) {
              // Insert dissonance just before the final chord/note
              const dissonanceInsert = isMajor ? dissonanceMajorInsert : dissonanceMinorInsert;
              sequenceBase.splice(sequenceBase.length - 1, 0, dissonanceInsert); // Insert before the last element
         }

         if (currentSequence) {
             currentSequence.dispose(); // Clean up old sequence
         }

         currentSequence = new Tone.Part((time, value) => {
              // Trigger multiple notes if value.note is an array (for chords/dissonance)
             if (Array.isArray(value.note)) {
                 polySynth.triggerAttackRelease(value.note, value.duration, time);
             } else {
                 polySynth.triggerAttackRelease(value.note, value.duration, time);
             }

             // Trigger visualizer pulse/animation on note
             pulseVisualizer(value.note, addDissonance);

         }, sequenceBase).start(0); // Start the sequence immediately when transport starts

         // Make it loop
         currentSequence.loop = true;
         currentSequence.loopEnd = '5m'; // Loop after the assumed 5 measures (adjust based on sequence length)
    }

     function pulseVisualizer(note, isDissonance) {
         // Simple pulse animation
         visualizer.style.transform = 'scale(1.1)';
         visualizer.style.opacity = 0.9;

         // Update color/state based on settings
         visualizer.classList.toggle('minor', scaleMinorRadio.checked);
         visualizer.classList.toggle('dissonance', isDissonance);


         // Reset after a short delay
         setTimeout(() => {
             visualizer.style.transform = 'scale(1)';
             visualizer.style.opacity = scaleMajorRadio.checked ? 0.7 : 0.6; // Slightly less opaque for minor visual
             visualizer.classList.toggle('dissonance', false); // Remove dissonance class quickly
         }, 150); // Shorter delay for faster notes

          // If dissonance is active, re-add the dissonance class after a shorter pulse for a flickering effect
          if (isDissonance) {
              setTimeout(() => {
                   visualizer.classList.add('dissonance');
              }, 200); // Re-add briefly
          }
     }


    // Initialize Tone.js and sequence only when the user interacts for the first time
    // This is crucial for browser autoplay policies
    let isInitialized = false;

    function initializeAudio() {
        if (!isInitialized) {
            Tone.start();
             polySynth = new Tone.PolySynth(Tone.Synth, {
                oscillator: {
                    type: "triangle" // A simple waveform
                },
                envelope: {
                    attack: 0.01, // Shorter attack for a slightly plucky feel
                    decay: 0.2,
                    sustain: 0.4,
                    release: 1.2 // Longer release
                },
                 volume: -8 // Reduce volume slightly
            }).toDestination();

             Tone.Transport.bpm.value = tempoSlider.value;
             createSequence();
             isInitialized = true;
        }
    }


    // Event listener for the play button
    playButton.addEventListener('click', () => {
        initializeAudio(); // Initialize audio context on first click

        if (!isPlaying) {
            Tone.Transport.start();
            playButton.textContent = 'הפסיקו לנגן';
            playButton.style.backgroundColor = var('--accent-color-minor'); /* Red for Stop */
            playButton.style.boxShadow = '0 4px 8px rgba(244, 67, 54, 0.3)';
            isPlaying = true;
             visualizer.style.display = 'block'; // Show visualizer
        } else {
            Tone.Transport.stop();
            playButton.textContent = 'התחילו לנגן';
            playButton.style.backgroundColor = var('--accent-color-major'); /* Green for Play */
             playButton.style.boxShadow = '0 4px 8px rgba(76, 175, 80, 0.3)';
            isPlaying = false;
            // visualizer.style.display = 'none'; // Hide visualizer when stopped
             visualizer.style.transform = 'scale(1)'; // Reset scale
             visualizer.style.opacity = 0.7;
             visualizer.classList.remove('dissonance'); // Reset dissonance visual
        }
    });

    // Event listeners for controls
    // When controls change, update the sequence and restart playback if it was active
    scaleMajorRadio.addEventListener('change', () => {
        if (isInitialized) { // Only update if audio is initialized
            createSequence();
            visualizer.classList.toggle('minor', false);
            if (isPlaying) {
                Tone.Transport.stop();
                Tone.Transport.start();
            }
        }
    });

    scaleMinorRadio.addEventListener('change', () => {
         if (isInitialized) { // Only update if audio is initialized
            createSequence();
             visualizer.classList.toggle('minor', true);
             if (isPlaying) {
                Tone.Transport.stop();
                Tone.Transport.start();
            }
        }
    });

    tempoSlider.addEventListener('input', (event) => {
        const tempo = event.target.value;
        tempoValueSpan.textContent = tempo;
        if (isInitialized) { // Only update if audio is initialized
             Tone.Transport.bpm.value = tempo;
             // No need to restart sequence for tempo change
        }
    });

    addDissonanceCheckbox.addEventListener('change', () => {
        if (isInitialized) { // Only update if audio is initialized
            createSequence(); // Recreate sequence with/without dissonance
             visualizer.classList.toggle('dissonance', addDissonanceCheckbox.checked);
            if (isPlaying) {
                Tone.Transport.stop();
                Tone.Transport.start();
            }
        }
    });

    // User provides feedback with the emotion slider - no effect on audio
    // emotionSlider.addEventListener('input', (event) => { /* ... */ });


    // Event listener for the explanation button
    toggleExplanationButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתירו את ההסבר';
            toggleExplanationButton.style.backgroundColor = var('--button-hover');
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'רוצים להבין יותר לעומק? לחצו כאן להסבר המלא';
             toggleExplanationButton.style.backgroundColor = var('--secondary-color');
        }
    });

    // Initial state setup
     visualizer.classList.toggle('minor', scaleMinorRadio.checked);
     visualizer.classList.toggle('dissonance', addDissonanceCheckbox.checked);
     // visualizer.style.display = 'none'; // Initially hide visualizer until play
     visualizer.style.opacity = scaleMajorRadio.checked ? 0.7 : 0.6;


</script>
```