---
title: "מעבדת ההרמוניה המופלאה"
english_slug: musical-harmony-tool
category: "מוזיקה"
tags: [interactive, music, harmony, intervals, chords, piano, experiment, play]
---
# מעבדת ההרמוניה המופלאה

ברוכים הבאים למעבדת ההרמוניה! האם אתם מוכנים לצאת למסע מרתק אל לב המוזיקה? הכלי האינטראקטיבי הזה הוא המגרש משחקים שלכם לחקר הקשרים הקסומים בין הצלילים. בחרו תו התחלה, ותראו איך נוצרים ממנו מרווחים ואקורדים, קופצים לחיים ממש מול עיניכם על קלידי הפסנתר הווירטואלי. שחקו עם הצלילים, גלו את התבניות, והתחילו להרגיש את השפה הסודית של ההרמוניה!

<div class="harmony-tool-app">
    <div class="controls">
        <label for="base-note-select">צאו לדרך עם תו:</label>
        <select id="base-note-select">
            <option value="C">דו (C)</option>
            <option value="C#">דו דיאז (C#)</option>
            <option value="D">רה (D)</option>
            <option value="D#">רה דיאז (D#)</option>
            <option value="E">מי (E)</option>
            <option value="F">פה (F)</option>
            <option value="F#">פה דיאז (F#)</option>
            <option value="G">סול (G)</option>
            <option value="G#">סול דיאז (G#)</option>
            <option value="A">לה (A)</option>
            <option value="A#">לה דיאז (A#)</option>
            <option value="B">סי (B)</option>
        </select>
    </div>

    <div class="results">
        <div class="intervals-section">
            <h2>המרווחים שפורחים מהתו שבחרת:</h2>
            <ul id="interval-list">
                <!-- Intervals will be populated here by JS -->
            </ul>
        </div>
        <div class="chords-section">
             <h2>האקורדים שנוצרים (משולשים קסומים):</h2>
             <div id="chord-list">
                <!-- Chords will be populated here by JS -->
             </div>
        </div>
    </div>

    <div class="piano-container">
        <div class="piano">
            <!-- 2.5 octaves of keys C3 to C5 -->
            <div class="key white" data-note="C3"></div>
            <div class="key black" data-note="C#3"></div>
            <div class="key white" data-note="D3"></div>
            <div class="key black" data-note="D#3"></div>
            <div class="key white" data-note="E3"></div>
            <div class="key white" data-note="F3"></div>
            <div class="key black" data-note="F#3"></div>
            <div class="key white" data-note="G3"></div>
            <div class="key black" data-note="G#3"></div>
            <div class="key white" data-note="A3"></div>
            <div class="key black" data-note="A#3"></div>
            <div class="key white" data-note="B3"></div>

            <div class="key white" data-note="C4"></div>
            <div class="key black" data-note="C#4"></div>
            <div class="key white" data-note="D4"></div>
            <div class="key black" data-note="D#4"></div>
            <div class="key white" data-note="E4"></div>
            <div class="key white" data-note="F4"></div>
            <div class="key black" data-note="F#4"></div>
            <div class="key white" data-note="G4"></div>
            <div class="key black" data-note="G#4"></div>
            <div class="key white" data-note="A4"></div>
            <div class="key black" data-note="A#4"></div>
            <div class="key white" data-note="B4"></div>

             <div class="key white" data-note="C5"></div>
        </div>
    </div>
</div>

<button id="toggle-explanation">הצצה אל מאחורי הקלעים: מה קורה כאן?</button>

<div id="explanation" style="display: none;">
    <h2>הסבר עמוק יותר: מסע אל תוך ההרמוניה</h2>
    <p>ברוכים השבים מהמעבדה! אחרי ששיחקתם וגיליתם בעצמכם, בואו נבין קצת יותר לעומק את הקסם.</p>

    <h3>מהו מרווח?</h3>
    <p>מרווח הוא פשוט המרחק בין שני תווים. חשבו על זה כעל "קפיצה" בין תו אחד למשנהו. המרחק הזה נמדד ביחידות קטנות שנקראות "חצאי טונים". סוג המרווח (גדול, קטן, זך) נקבע על פי מספר חצאי הטונים והשם שלו בסולם הדיאטוני. הכלי שלנו הדגיש לכם את התו שמרוחק מהשורש שבחרתם במרווחים הנפוצים. לחיצה על מרווח ברשימה הדגישה את התו המתאים בפסנתר – ראיתם את המיקום, ועכשיו אתם יודעים את השם!</p>
    <ul>
        <li><strong>שורש (R):</strong> התו שבחרתם – נקודת ההתחלה של כל המרווחים והאקורדים כאן.</li>
        <li><strong>סקונדה (m2/M2):</strong> המרווח הקטן ביותר (חצי טון) או קצת יותר (טון שלם). נשמע צפוף!</li>
        <li><strong>טרצה (m3/M3):</strong> המרווח המכונן של אקורדים (3 או 4 חצאי טונים). הטרצה היא זו שנותנת לאקורד את ה"צבע" שלו – שמח (גדולה) או עצוב (קטנה).</li>
        <li><strong>קוורטה זכה (P4):</strong> מרווח יציב ויפהפה של 5 חצאי טונים.</li>
        <li><strong>קווינטה זכה (P5):</strong> מרווח יציב וחזק במיוחד של 7 חצאי טונים – עמוד השדרה של רוב האקורדים.</li>
        <li><strong>סקסטה (m6/M6):</strong> מרווח "צבעוני" יותר (8 או 9 חצאי טונים).</li>
        <li><strong>ספטימה (m7/M7):</strong> מרווח שמוסיף "מתח" או אופי מיוחד לאקורדים (10 או 11 חצאי טונים).</li>
        <li><strong>אוקטבה (Oct):</strong> אותו תו בדיוק, רק גבוה או נמוך יותר (12 חצאי טונים). נשמע זהה אך מרגיש "שלם".</li>
    </ul>

    <h3>מהו אקורד?</h3>
    <p>אקורד הוא קבוצה של תווים שנשמעים יחד – כמו "צליל מורכב". האקורדים המשולשים הם אבני הבניין הבסיסיות של רוב המוזיקה שאנחנו שומעים. הם מורכבים מהשורש, הטרצה מעליו והקווינטה מעליו. ראיתם איך לחיצה על שם אקורד הדגישה לכם בפסנתר את כל שלושת התווים המרכיבים אותו. אלה הצלילים שיוצרים את התחושה המיוחדת של האקורד!</p>
    <ul>
        <li><strong>אקורד מז'ור:</strong> שורש + טרצה גדולה + קווינטה זכה. נשמע פתוח, בהיר, ולרוב "שמח".</li>
        <li><strong>אקורד מינור:</strong> שורש + טרצה קטנה + קווינטה זכה. נשמע עמוק, מעט מלנכולי, ולרוב "עצוב".</li>
    </ul>
    <p>הכלי הזה עזר לכם לראות ולהבין את הקשר בין המבנה התיאורטי (מרווחים, אקורדים) לבין המיקום הפיזי על הכלי (הפסנתר). המשיכו לשחק ולחקור – ככל שתתנסו יותר, כך תפתחו אינטואיציה טובה יותר להרמוניה!</p>
</div>

<style>
    /* General Styling */
    body {
        font-family: 'Heebo', sans-serif; /* A more modern Hebrew-friendly font */
        line-height: 1.7;
        margin: 0; /* Remove default body margin */
        padding: 20px;
        background: linear-gradient(to bottom right, #ece9e6, #ffffff); /* Soft gradient background */
        color: #333;
        direction: rtl; /* Right-to-left */
        text-align: right;
    }

    h1, h2, h3 {
        color: #0056b3;
        margin-bottom: 15px;
        font-weight: bold;
    }

    h1 { font-size: 2em; text-align: center; margin-bottom: 30px; }
    h2 { font-size: 1.5em; }
    h3 { font-size: 1.2em; color: #007bff; margin-top: 20px;}


    /* App Container */
    .harmony-tool-app {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        margin-bottom: 30px;
        display: flex;
        flex-direction: column;
        align-items: center;
        border: 1px solid #e0e0e0; /* Subtle border */
    }

    /* Controls Section */
    .controls {
        margin-bottom: 30px;
        text-align: center;
        width: 100%;
        max-width: 300px; /* Limit width */
    }

    .controls label {
        font-weight: bold;
        margin-left: 10px; /* Adjusted for RTL */
        font-size: 1.1em;
        color: #555;
    }

    .controls select {
        padding: 10px 15px;
        font-size: 1.1em;
        border-radius: 6px;
        border: 1px solid #ccc;
        background-color: #f9f9f9;
        cursor: pointer;
        outline: none; /* Remove default focus outline */
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
        -webkit-appearance: none; /* Remove default dropdown arrow */
        -moz-appearance: none;
        appearance: none;
        background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23333%22%20d%3D%22M287%2C197.9L159.9%2C68.6c-3.1-3.1-8.2-3.1-11.3%2C0L5.4%2C197.9c-3.1%2C3.1-3.1%2C8.2%2C0%2C11.3l19.6%2C19.6c3.1%2C3.1%2C8.2%2C3.1%2C11.3%2C0L149%2C128.2l108.7%2C108.9c3.1%2C3.1%2C8.2%2C3.1%2C11.3%2C0l19.6-19.6C290.1%2C206.1%2C290.1%2C201%2C287%2C197.9z%22%2F%3E%3C%2Fsvg%3E');
        background-repeat: no-repeat;
        background-position: left 15px center; /* Position arrow on the left for RTL */
        background-size: 12px;
        padding-left: 30px; /* Make space for the custom arrow */
        text-align-last: right; /* Align selected text to the right */
    }

    .controls select:hover {
        border-color: #007bff;
    }
     .controls select:focus {
        border-color: #007bff;
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.3);
     }


    /* Results Section */
    .results {
        display: flex;
        flex-wrap: wrap;
        gap: 25px; /* Increased gap */
        margin-bottom: 30px;
        width: 100%;
        justify-content: center;
    }

    .intervals-section, .chords-section {
        flex: 1;
        min-width: 300px; /* Slightly increased min width */
        background-color: #f8f9fa; /* Lighter background */
        padding: 20px; /* Increased padding */
        border-radius: 10px;
        border: 1px solid #e9ecef;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
     .intervals-section h2, .chords-section h2 {
        margin-top: 0;
        font-size: 1.4em; /* Slightly larger heading */
        border-bottom: 2px solid #dee2e6; /* Thicker border */
        padding-bottom: 10px; /* Increased padding */
        margin-bottom: 15px; /* Increased margin */
        color: #007bff; /* Match select color */
     }


    #interval-list {
        list-style: none;
        padding: 0;
        margin: 0;
        display: flex;
        flex-wrap: wrap;
        gap: 10px; /* Increased gap */
    }

    #interval-list li {
        background-color: #007bff; /* Primary blue */
        color: white;
        padding: 8px 15px; /* Increased padding */
        border-radius: 20px; /* Pill shape */
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.2s ease;
        font-size: 1em;
        font-weight: 500;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    #interval-list li:hover {
        background-color: #0056b3; /* Darker blue */
        transform: translateY(-2px); /* Lift effect */
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }

    #interval-list li.active-interval {
        background-color: #28a745; /* Success green */
        font-weight: bold;
        box-shadow: 0 3px 6px rgba(40, 167, 69, 0.3);
        transform: scale(1.03); /* Subtle scale */
    }


    #chord-list {
        display: flex;
        flex-wrap: wrap;
        gap: 12px; /* Increased gap */
    }

     #chord-list .chord-item {
        background-color: #ffc107; /* Warning yellow */
        color: #333;
        padding: 10px 18px; /* Increased padding */
        border-radius: 20px; /* Pill shape */
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.2s ease;
        font-size: 1em;
        font-weight: 500;
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
     }

     #chord-list .chord-item:hover {
        background-color: #e0a800; /* Darker yellow */
        transform: translateY(-2px); /* Lift effect */
         box-shadow: 0 4px 8px rgba(0,0,0,0.15);
     }

     #chord-list .chord-item.active-chord {
         background-color: #dc3545; /* Danger red */
         color: white;
         font-weight: bold;
         box-shadow: 0 3px 6px rgba(220, 53, 69, 0.3);
         transform: scale(1.03); /* Subtle scale */
     }


    /* Piano Styling */
    .piano-container {
        width: 100%;
        max-width: 800px; /* Limit piano width */
        overflow-x: auto; /* Add scroll if needed */
        padding-bottom: 15px; /* Space for scrollbar */
        direction: ltr; /* Force LTR for piano layout */
    }
     .piano-container::-webkit-scrollbar {
        height: 8px;
     }

     .piano-container::-webkit-scrollbar-track {
         background: #f1f1f1;
         border-radius: 10px;
     }

     .piano-container::-webkit-scrollbar-thumb {
         background: #888;
         border-radius: 10px;
     }

     .piano-container::-webkit-scrollbar-thumb:hover {
         background: #555;
     }


    .piano {
        display: flex;
        position: relative;
        height: 250px; /* Increased Height of the piano */
        margin: 20px auto;
         /* Total width needs to accommodate all keys */
         /* C3-B3 (7 white, 5 black) + C4-B4 (7 white, 5 black) + C5 (1 white) */
         /* White key width = 50px (adjusted) */
         /* Black key width = 30px (adjusted) */
         /* Octave width: 7*50 = 350px */
         /* 2 octaves + C5: 350*2 + 50 = 750px. Need some padding/spacing */
         width: 850px; /* Adjust based on key size and spacing */
    }

    .key {
        position: absolute;
        box-sizing: border-box;
        border: 1px solid #666; /* Softer border */
        border-top: none;
        border-radius: 0 0 6px 6px; /* Slightly larger radius */
        cursor: pointer; /* Make keys clickable visually */
        transition: background-color 0.2s ease, box-shadow 0.2s ease, transform 0.1s ease;
        display: flex; /* For centering label */
        justify-content: center; /* For centering label */
        align-items: flex-end; /* Position label at the bottom */
        padding-bottom: 10px; /* Space for label */
        color: #333; /* Default text color for white keys */
        font-size: 0.9em;
        font-weight: bold;
    }

    .key .note-label {
        position: absolute;
        bottom: 5px;
        left: 0;
        right: 0;
        text-align: center;
        font-size: 0.8em;
        font-weight: bold;
        pointer-events: none; /* Don't interfere with click */
        opacity: 0; /* Initially hidden */
        transition: opacity 0.3s ease;
    }

    .key.white {
        width: 50px; /* Adjusted width */
        height: 250px; /* Adjusted height */
        background: linear-gradient(to bottom, #ffffff 95%, #f0f0f0); /* Gradient */
        z-index: 1;
         box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }

    .key.black {
        width: 30px; /* Adjusted width */
        height: 150px; /* Adjusted height */
        background: linear-gradient(to bottom, #222 95%, #000); /* Gradient */
        color: #eee; /* Text color for black keys */
        z-index: 2;
         box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
         border-color: #000;
    }

    /* Positioning the keys - Adjusted for new sizes */
    /* White key width = 50px */
    /* Black key width = 30px */
    /* Offset for black keys = white key width - black key width / 2 approx = 50 - 15 = 35 */
    /* Spacing between white keys with black keys = (50 * 2 - 30) / 2 approx = 35 */

    .piano [data-note="C3"] { left: 0px; }
    .piano [data-note="C#3"] { left: 35px; }
    .piano [data-note="D3"] { left: 50px; }
    .piano [data-note="D#3"] { left: 85px; }
    .piano [data-note="E3"] { left: 100px; } /* E-F has no black key, so E position + white key width */
    .piano [data-note="F3"] { left: 150px; }
    .piano [data-note="F#3"] { left: 185px; }
    .piano [data-note="G3"] { left: 200px; }
    .piano [data-note="G#3"] { left: 235px; }
    .piano [data-note="A3"] { left: 250px; }
    .piano [data-note="A#3"] { left: 285px; }
    .piano [data-note="B3"] { left: 300px; } /* B-C has no black key */

    /* C4 starts after B3 + white key width */
    .piano [data-note="C4"] { left: 350px; }
    .piano [data-note="C#4"] { left: 385px; }
    .piano [data-note="D4"] { left: 400px; }
    .piano [data-note="D#4"] { left: 435px; }
    .piano [data-note="E4"] { left: 450px; }
    .piano [data-note="F4"] { left: 500px; }
    .piano [data-note="F#4"] { left: 535px; }
    .piano [data-note="G4"] { left: 550px; }
    .piano [data-note="G#4"] { left: 585px; }
    .piano [data-note="A4"] { left: 600px; }
    .piano [data-note="A#4"] { left: 635px; }
    .piano [data-note="B4"] { left: 650px; }

    /* C5 starts after B4 + white key width */
    .piano [data-note="C5"] { left: 700px; }


    /* Highlighting Classes */
    .key.highlight-root {
        background: linear-gradient(to bottom, #007bff 95%, #0056b3); /* Blue gradient */
        box-shadow: 0 0 15px rgba(0, 123, 255, 0.7), 0 0 5px rgba(0,0,0,0.3);
        color: white; /* White text on dark background */
        z-index: 3; /* Bring to front */
        transform: scaleY(1.03); /* Subtle press effect */
    }
    .key.highlight-root .note-label { opacity: 1; color: white; } /* Show label */


    .key.highlight-interval {
        background: linear-gradient(to bottom, #28a745 95%, #218838); /* Green gradient */
        box-shadow: 0 0 15px rgba(40, 167, 69, 0.7), 0 0 5px rgba(0,0,0,0.3);
         color: white;
         z-index: 3;
          transform: scaleY(1.03);
    }
     .key.highlight-interval .note-label { opacity: 1; color: white; }

     .key.highlight-chord {
        background: linear-gradient(to bottom, #ffc107 95%, #e0a800); /* Yellow gradient */
        box-shadow: 0 0 15px rgba(255, 193, 7, 0.7), 0 0 5px rgba(0,0,0,0.3);
         color: #333; /* Dark text on light background */
         z-index: 3;
          transform: scaleY(1.03);
     }
      .key.highlight-chord .note-label { opacity: 1; color: #333; }

      .key.black.highlight-root,
      .key.black.highlight-interval,
      .key.black.highlight-chord {
          color: white; /* Ensure black keys text remains white */
      }
       .key.black.highlight-chord .note-label { color: white; } /* Ensure label is white on black highlight */


    /* Pulse animation for interaction */
    @keyframes key-pulse {
        0% { transform: scaleY(1.03); }
        50% { transform: scaleY(1.05); }
        100% { transform: scaleY(1.03); }
    }
     .key.pulsing {
         animation: key-pulse 0.6s ease-in-out infinite; /* Apply pulse */
     }

    /* Explanation Section */
    #toggle-explanation {
        display: block;
        margin: 30px auto; /* Increased margin */
        padding: 12px 25px; /* Increased padding */
        font-size: 1.1em; /* Larger font */
        cursor: pointer;
        border: none;
        border-radius: 25px; /* Rounded button */
        background-color: #6c757d; /* Secondary gray */
        color: white;
        transition: background-color 0.3s ease, transform 0.2s ease;
        font-weight: bold;
    }

    #toggle-explanation:hover {
        background-color: #5a6268; /* Darker gray */
        transform: translateY(-2px);
    }

    #explanation {
        background-color: #e9ecef; /* Light background */
        padding: 30px; /* Increased padding */
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border: 1px solid #dee2e6;
         direction: rtl; /* Ensure RTL for explanation */
         text-align: right;
    }

    #explanation ul {
        padding-right: 25px; /* Adjusted for RTL */
        padding-left: 0;
        list-style: disc outside; /* Default disc style */
    }

    #explanation li {
        margin-bottom: 12px; /* Increased margin */
        line-height: 1.8;
    }
     #explanation li strong {
         color: #0056b3; /* Highlight terms */
     }


    /* Responsive adjustments */
    @media (max-width: 768px) {
        .harmony-tool-app {
            padding: 20px;
        }
         .results {
             flex-direction: column;
             gap: 15px;
         }
         .intervals-section, .chords-section {
             min-width: auto; /* Allow sections to shrink */
             width: 100%;
             padding: 15px;
         }
         #interval-list, #chord-list {
             gap: 8px;
         }
         #interval-list li, #chord-list .chord-item {
             padding: 6px 12px;
             font-size: 0.9em;
         }


        .piano-container {
            padding-bottom: 10px;
        }

        .piano {
            height: 200px; /* Adjusted height */
             /* Recalculate width for smaller keys */
             width: 680px; /* Example width */
        }
         .key.white { width: 40px; height: 200px; } /* Adjusted size */
         .key.black { width: 25px; height: 120px; } /* Adjusted size */

         /* Re-calculate positions roughly for smaller keys */
         /* White key width = 40px */
         /* Black key width = 25px */
         /* Offset = 40 - 25/2 = 27.5 -> use 28px */

         .piano [data-note="C3"] { left: 0px; }
         .piano [data-note="C#3"] { left: 28px; }
         .piano [data-note="D3"] { left: 40px; }
         .piano [data-note="D#3"] { left: 68px; }
         .piano [data-note="E3"] { left: 80px; }
         .piano [data-note="F3"] { left: 120px; } /* 80 + 40 */
         .piano [data-note="F#3"] { left: 148px; }
         .piano [data-note="G3"] { left: 160px; }
         .piano [data-note="G#3"] { left: 188px; }
         .piano [data-note="A3"] { left: 200px; }
         .piano [data-note="A#3"] { left: 228px; }
         .piano [data-note="B3"] { left: 240px; }

         .piano [data-note="C4"] { left: 280px; } /* 240 + 40 */
         .piano [data-note="C#4"] { left: 308px; }
         .piano [data-note="D4"] { left: 320px; }
         .piano [data-note="D#4"] { left: 348px; }
         .piano [data-note="E4"] { left: 360px; }
         .piano [data-note="F4"] { left: 400px; }
         .piano [data-note="F#4"] { left: 428px; }
         .piano [data-note="G4"] { left: 440px; }
         .piano [data-note="G#4"] { left: 468px; }
         .piano [data-note="A4"] { left: 480px; }
         .piano [data-note="A#4"] { left: 508px; }
         .piano [data-note="B4"] { left: 520px; }

          .piano [data-note="C5"] { left: 560px; } /* 520 + 40 */

        .key .note-label {
            font-size: 0.7em; /* Smaller label font */
            bottom: 3px;
        }
    }

</style>

<script>
    const notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];
    const noteMap = {
        "C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5,
        "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11
    };
    const intervals = {
        0: { name: "שורש", short: "R" },
        1: { name: "סקונדה קטנה", short: "m2" },
        2: { name: "סקונדה גדולה", short: "M2" },
        3: { name: "טרצה קטנה", short: "m3" },
        4: { name: "טרצה גדולה", short: "M3" },
        5: { name: "קוורטה זכה", short: "P4" },
        6: { name: "טריטון", short: "TT" },
        7: { name: "קווינטה זכה", short: "P5" },
        8: { name: "סקסטה קטנה", short: "m6" },
        9: { name: "סקסטה גדולה", short: "M6" },
        10: { name: "ספטימה קטנה", short: "m7" },
        11: { name: "ספטימה גדולה", short: "M7" },
        12: { name: "אוקטבה", short: "Oct" }
    };

    const chords = {
        "מז'ור": { pattern: [0, 4, 7], labels: ["R", "M3", "P5"] }, // Root, Major 3rd, Perfect 5th
        "מינור": { pattern: [0, 3, 7], labels: ["R", "m3", "P5"] }  // Root, Minor 3rd, Perfect 5th
    };

    const selectElement = document.getElementById('base-note-select');
    const intervalListElement = document.getElementById('interval-list');
    const chordListElement = document.getElementById('chord-list');
    const pianoKeys = document.querySelectorAll('.piano .key');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    // --- Helper Functions ---

    // Gets the note name (C, C#, etc.) based on a root index and semitones
    function getNoteNameBySemitone(rootNoteIndex, semitones) {
        const totalSemitones = rootNoteIndex + semitones;
        const noteIndex = totalSemitones % 12;
        return notes[noteIndex];
    }

     // Gets the note name *with octave* based on a root name, root octave, and semitones
     function getNoteWithOctave(rootNoteName, rootOctave, semitones) {
        const rootNoteIndex = noteMap[rootNoteName];
        // Calculate total semitones from C0
        const totalSemitonesFromC0 = rootNoteIndex + (rootOctave * 12);
        // Target total semitones from C0
        const targetTotalSemitones = totalSemitonesFromC0 + semitones;
        // Handle negative semitones to ensure correct octave calculation
        const normalizedTargetSemitones = targetTotalSemitones >= 0 ? targetTotalSemitones : targetTotalSemitones + (Math.ceil(-targetTotalSemitones / 12) * 12);

        const targetNoteIndex = normalizedTargetSemitones % 12;
        const targetOctave = Math.floor(normalizedTargetSemitones / 12);

        return notes[targetNoteIndex] + targetOctave;
     }

     // Clear all previous highlights and labels from piano keys
     function clearPianoHighlights() {
          pianoKeys.forEach(key => {
              key.classList.remove('highlight-root', 'highlight-interval', 'highlight-chord', 'pulsing');
              // Remove any existing labels
              const label = key.querySelector('.note-label');
              if(label) {
                  label.remove();
              }
          });
          // Clear active state from lists
          document.querySelectorAll('#interval-list li').forEach(li => li.classList.remove('active-interval'));
          document.querySelectorAll('#chord-list .chord-item').forEach(item => item.classList.remove('active-chord'));
     }

    // Add a label to a piano key
    function addLabelToKey(keyElement, labelText) {
        const label = document.createElement('span');
        label.classList.add('note-label');
        label.textContent = labelText;
        keyElement.appendChild(label);
        // Trigger fade-in animation after adding
        requestAnimationFrame(() => {
             label.style.opacity = 1;
        });
    }

    // --- Main Display Function ---

    function updateHarmonyDisplay(baseNote) {
        clearPianoHighlights(); // Start fresh

        const baseNoteIndex = noteMap[baseNote];
        const selectedOctave = 4; // Reference octave for the root (C4)

        // --- Highlight Root Note ---
        pianoKeys.forEach(key => {
             const keyNote = key.dataset.note.slice(0, -1); // Get note letter part (C, C#, etc.)
             if (keyNote === baseNote) {
                 // Highlight all occurrences of the root note
                 key.classList.add('highlight-root');
                 addLabelToKey(key, 'R'); // Add 'R' label to root keys
             }
        });


        // --- Display Intervals ---
        intervalListElement.innerHTML = '';
        // Only show intervals within a reasonable range (e.g., up to an octave)
        const semitonesToShow = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

        semitonesToShow.forEach(semitone => {
            const intervalInfo = intervals[semitone];
            if (intervalInfo) {
                const targetNoteName = getNoteNameBySemitone(baseNoteIndex, semitone);
                 // Get the target note with octave. Try to keep it close to the root octave (C4)
                 // For intervals 0-11, target is usually in the same or next octave.
                 // For octave (12), it's one octave higher.
                 const targetSemitonesFromC0 = noteMap[baseNote] + (selectedOctave * 12) + semitone;
                 const targetNoteWithOctave = getNoteWithOctave(baseNote, selectedOctave, semitone);


                const listItem = document.createElement('li');
                listItem.textContent = `${intervalInfo.name} (${intervalInfo.short}): ${targetNoteName}`;
                listItem.dataset.note = targetNoteWithOctave; // Store the note+octave for highlighting
                listItem.title = `לחץ כדי לראות את ${targetNoteName} (${intervalInfo.name}) בפסנתר`;

                listItem.addEventListener('click', () => {
                    clearPianoHighlights(); // Clear previous selections (including default root)

                     // Highlight the selected interval note AND the root note
                     const targetKey = document.querySelector(`.piano .key[data-note="${targetNoteWithOctave}"]`);
                     const rootKey = document.querySelector(`.piano .key[data-note="${baseNote}${selectedOctave}"]`); // Find the root in the reference octave

                     // Highlight the specific root used for this calculation
                     if(rootKey) {
                         rootKey.classList.add('highlight-root');
                         addLabelToKey(rootKey, 'R');
                     } else { // If root C4 isn't shown, maybe show C3 or C5?
                         document.querySelector(`.piano .key[data-note="${baseNote}3"]`)?.classList.add('highlight-root');
                         document.querySelector(`.piano .key[data-note="${baseNote}3"] span`)?.remove(); // Remove old label if exists
                          document.querySelector(`.piano .key[data-note="${baseNote}3"]`) && addLabelToKey(document.querySelector(`.piano .key[data-note="${baseNote}3"]`), 'R');


                         document.querySelector(`.piano .key[data-note="${baseNote}5"]`)?.classList.add('highlight-root');
                          document.querySelector(`.piano .key[data-note="${baseNote}5"] span`)?.remove(); // Remove old label if exists
                         document.querySelector(`.piano .key[data-note="${baseNote}5"]`) && addLabelToKey(document.querySelector(`.piano .key[data-note="${baseNote}5"]`), 'R');
                     }


                    if (targetKey) {
                         targetKey.classList.add('highlight-interval');
                         targetKey.classList.add('pulsing'); // Add pulse animation
                         addLabelToKey(targetKey, intervalInfo.short); // Add interval label
                    }

                    // Set active state on list item
                     document.querySelectorAll('#interval-list li').forEach(li => li.classList.remove('active-interval'));
                     listItem.classList.add('active-interval');

                });

                intervalListElement.appendChild(listItem);
            }
        });

        // --- Display Chords ---
        chordListElement.innerHTML = '';
        for (const [chordName, chordInfo] of Object.entries(chords)) {
            const semitonePattern = chordInfo.pattern;
            const labels = chordInfo.labels;

            const chordNotesNames = semitonePattern.map(semitone => getNoteNameBySemitone(baseNoteIndex, semitone));

             // Get notes with specific octaves for highlighting.
             // Place the root around C4, and subsequent notes in the closest octave above or equal to the previous note.
             let currentOctave = selectedOctave;
             let lastTotalSemitones = noteMap[baseNote] + (currentOctave * 12); // Start with root semitones

             const chordNotesWithOctaves = semitonePattern.map((semitone, index) => {
                 const targetTotalSemitones = noteMap[baseNote] + (selectedOctave * 12) + semitone; // Calculate relative to root C4
                 const targetNoteOctave = Math.floor(targetTotalSemitones / 12);
                  const targetNoteIndexInOctave = targetTotalSemitones % 12;

                  // Adjust octave to keep notes close together, forming a basic chord voicing
                  // If the target note is more than half an octave *below* the previous note, jump up an octave.
                  // This simple logic helps form basic root position chords within 1-2 octaves.
                  let finalOctave = targetNoteOctave;

                  // Simple check: If the note index is lower than the previous one (e.g., B after C), increase octave.
                  // This isn't perfect for all inversions/voicings but works for basic root position.
                  // A more robust method would track last *absolute* semitones and add 12 if the new note's absolute semitones are less.
                   const absoluteSemitones = noteMap[baseNote] + (selectedOctave * 12) + semitone;
                   if (index > 0 && absoluteSemitones < lastTotalSemitones) {
                        // If the next note in the pattern falls below the previous one's absolute position relative to C0+root octave,
                        // it likely means we crossed the octave boundary downwards relative to the pattern starting point.
                        // We need to find the key that exists on the piano.
                        // Let's stick to the getNoteWithOctave logic relative to C4 root for simplicity and existing key mapping.
                        // The getNoteWithOctave handles wrapping correctly.

                         // The issue is getNoteWithOctave calculates relative to *C4* base note.
                         // We want notes relative to the *actual* selected base note in C4.
                         // Let's calculate absolute semitones from C0 for the desired chord notes,
                         // assuming the root is in C4.
                         const rootAbsoluteSemitonesC4 = noteMap[baseNote] + (4 * 12);
                         const noteAbsoluteSemitones = rootAbsoluteSemitonesC4 + semitone;
                         const noteName = notes[noteAbsoluteSemitones % 12];
                         const noteOctave = Math.floor(noteAbsoluteSemitones / 12);
                         return noteName + noteOctave;

                   } else {
                       // Use the original calculation if sticking to that pattern.
                        const targetNoteWithOctaveSimple = getNoteWithOctave(baseNote, selectedOctave, semitone);
                        // A simple correction: if the *semitone* is greater than the octave (12), assume it's in the next octave.
                        // This is a hack but works for 9ths, 11ths, etc if added later. For triad (0, 3/4, 7), this isn't strictly needed.
                        // Let's just use the absolute semitone calculation relative to the root in C4.
                         const rootAbsoluteSemitonesC4 = noteMap[baseNote] + (4 * 12);
                         const noteAbsoluteSemitones = rootAbsoluteSemitonesC4 + semitone;
                         const noteName = notes[noteAbsoluteSemitones % 12];
                         const noteOctave = Math.floor(noteAbsoluteSemitones / 12);
                         lastTotalSemitones = noteAbsoluteSemitones; // Update last semitones for voicing logic if needed later
                         return noteName + noteOctave;

                   }
             });


            const chordItem = document.createElement('div');
            chordItem.classList.add('chord-item');
            chordItem.textContent = `${baseNote}${chordName.startsWith("מ") ? '' : ' '}${chordName}: ${chordNotesNames.join(', ')}`; // Use Hebrew chord name directly
            chordItem.dataset.notes = chordNotesWithOctaves.join(','); // Store notes+octaves for highlighting
            chordItem.dataset.labels = labels.join(','); // Store labels
            chordItem.title = `לחץ כדי לראות את אקורד ${baseNote} ${chordName} בפסנתר`;

            chordItem.addEventListener('click', () => {
                 clearPianoHighlights(); // Clear previous selections

                 const notesToHighlight = chordItem.dataset.notes.split(',');
                 const chordLabels = chordItem.dataset.labels.split(',');

                 notesToHighlight.forEach((noteOctave, index) => {
                     const key = document.querySelector(`.piano .key[data-note="${noteOctave}"]`);
                     if (key) {
                         key.classList.add('highlight-chord');
                          key.classList.add('pulsing'); // Add pulse animation
                         addLabelToKey(key, chordLabels[index]); // Add chord role label
                     }
                 });

                 // Set active state on list item
                 document.querySelectorAll('#chord-list .chord-item').forEach(item => item.classList.remove('active-chord'));
                 chordItem.classList.add('active-chord');
            });

            chordListElement.appendChild(chordItem);
        }

         // Default state: Highlight the root note(s) across visible octaves initially
        pianoKeys.forEach(key => {
            const keyNote = key.dataset.note.slice(0, -1); // Get note letter part
            if (keyNote === baseNote) {
                key.classList.add('highlight-root');
                 addLabelToKey(key, 'R'); // Add 'R' label by default
            }
        });
    }

    // --- Event Listeners ---

    // Event listener for base note selection
    selectElement.addEventListener('change', (event) => {
        updateHarmonyDisplay(event.target.value);
    });

    // Event listener for clicking piano keys (Optional: could add sound or note name display)
    // pianoKeys.forEach(key => {
    //     key.addEventListener('click', () => {
    //         console.log("Clicked key:", key.dataset.note);
    //         // Add sound playing logic here if applicable
    //     });
    // });


    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? "הסתר הסבר" : "הצצה אל מאחורי הקלעים: מה קורה כאן?";
    });


    // --- Initial Setup ---

    // Initial display based on default selected note
    updateHarmonyDisplay(selectElement.value);

</script>