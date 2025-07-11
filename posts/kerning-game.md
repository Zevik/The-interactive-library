---
title: "אמן הקרנינג: משחק ההתאמה החזותית"
english_slug: kerning-game
category: "טיפוגרפיה"
tags: [עיצוב, פונטים, ריווח, טיפוגרפיה]
---
# אמן הקרנינג: משחק ההתאמה החזותית

האם שמת לב פעם כמה קריטי הריווח בין אותיות למראה של מילה? בוא נצלול פנימה ונשחק קצת עם הריווח כדי לראות איך הוא משפיע על התחושה הכללית של הטקסט. המטרה? למצוא את הריווח הנכון שגורם למילה פשוט... להיראות טוב.

<div class="kerning-container">
  <div id="kerning-word" class="kerning-word">
    <span>ה</span><span>י</span><span>ו</span><span class="kerning-pair-start">ם</span><span class="kerning-pair-end">!</span>
  </div>
  <div class="kerning-controls">
    <button id="decrease-kerning" aria-label="Decrease Kerning">-</button>
    <span id="kerning-value" class="kerning-value">0.0px</span>
    <button id="increase-kerning" aria-label="Increase Kerning">+</button>
  </div>
  <div id="feedback" class="feedback"></div>
</div>

<button id="toggle-explanation" class="toggle-button">מה זה בכלל קרנינג? הצג הסבר 🧐</button>

<div id="explanation" class="explanation" style="display: none;">
  <h2>קרנינג (Kerning): האמנות הנסתרת של הטיפוגרפיה</h2>
  <p>דמיינו שהאותיות שלכם רוקדות. קרנינג הוא כמו המרחק הנכון בין כל זוג רקדנים כדי שההופעה תיראה הרמונית. בניגוד לריווח אחיד (Tracking) שמזיז את כל הרקדנים במקביל, קרנינג מתמקד בהתאמה מדויקת בין זוגות ספציפיים של אותיות – אלה שצורתן עלולה ליצור רווחים ויזואליים מוזרים או גדולים מדי אם נשאירים אותן בריווח ברירת המחדל.</p>
  <p>לדוגמה, אם תשימו לב לאות "ע" ליד "ו", החלק העליון של ה"ע" והזנב של ה"ו" יכולים להיפגש וליצור רווח גדול ולא אחיד. קרנינג מאפשר לצמצם רווח כזה (או להרחיב במקרים אחרים, כמו בין מירכאות לאות הראשונה), כך שהמרחקים הלבנים בין כל האותיות ייראו שווים ונעימים לעין. זהו פרט קטן אבל עוצמתי שיכול לשדרג טקסט מנחמד למדהים, במיוחד בכותרות גדולות, לוגואים או טקסטים שמיועדים להדפסה איכותית.</p>
  <p>פונטים מקצועיים מגיעים עם טבלאות קרנינג מובנות שמטפלות באלפי זוגות אותיות נפוצים, אבל העין האנושית היא השופטת האולטימטיבית. לפעמים, נגיעת קרנינג ידנית קלה היא כל מה שנדרש כדי שהמילה תיראה מושלמת.</p>
</div>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;700&display=swap');

  body {
    font-family: 'Heebo', sans-serif;
    direction: rtl;
    text-align: center;
    padding: 20px;
    background-color: #f0f2f5; /* Soft background */
    color: #333;
    line-height: 1.6;
    margin: 0;
  }

  h1, h2 {
    color: #2c3e50; /* Dark blue/grey for headings */
    font-weight: 700;
  }

  .kerning-container {
    margin: 40px auto;
    padding: 30px;
    background-color: #ffffff; /* White container */
    border-radius: 12px; /* More rounded corners */
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1); /* Deeper shadow */
    max-width: 650px; /* Slightly wider container */
    border: 1px solid #e0e0e0;
    perspective: 1000px; /* Add perspective for potential 3D effects */
  }

  .kerning-word {
    font-size: 4em; /* Larger text */
    font-weight: 700;
    margin-bottom: 40px;
    white-space: nowrap; /* Prevent wrapping */
    display: flex; /* Use flexbox */
    justify-content: center; /* Center the word */
    align-items: baseline; /* Align letters nicely */
    min-height: 1.2em; /* Ensure consistent height */
  }

  .kerning-word span {
    display: inline-block;
    transition: margin-left 0.3s ease-out, color 0.3s ease; /* Smooth transition for kerning and color */
    position: relative; /* Needed for absolute positioning of effects */
  }

   /* Optional: Add a visual guide/highlight on the affected pair */
  .kerning-word .kerning-pair-end.adjusting {
     /* Example: Briefly change color or add a subtle effect */
     /* color: #007bff; */
     /* text-shadow: 0 0 5px rgba(0, 123, 255, 0.5); */
  }

   .kerning-pair-end {
      position: relative; /* To position the effect below */
   }

   /* Add a subtle visual gap indicator */
   .kerning-pair-end::before {
       content: '';
       position: absolute;
       top: 100%; /* Position below the text */
       left: -1000px; /* Start far left */
       right: 0;
       width: calc(1000px + var(--kerning-margin, 0px)); /* Cover the variable gap + padding */
       height: 3px; /* Thickness of the indicator */
       background-color: #ffda63; /* Yellow/Gold indicator */
       opacity: 0; /* Start invisible */
       transition: opacity 0.3s ease, width 0.3s ease; /* Animate opacity and width */
       transform-origin: right; /* Animate from the right (RTL) */
       z-index: 1; /* Ensure it's above other things if needed */
   }

    .kerning-pair-end.adjusting::before {
        opacity: 1; /* Become visible when adjusting */
        width: var(--kerning-margin, 0px); /* Show the width of the current margin */
        left: -5px; /* A little nudge to the left for better visibility */
        right: auto; /* Undo right:0 */
        /* Add a pulse animation to the indicator */
        animation: pulseIndicator 1s infinite alternate ease-in-out;
    }

    @keyframes pulseIndicator {
        0% { background-color: #ffda63; }
        100% { background-color: #ffc107; } /* Brighter yellow */
    }


  .kerning-controls {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px; /* Increased gap */
    margin-bottom: 25px;
  }

  .kerning-controls button {
    padding: 12px 25px; /* More padding */
    font-size: 1.3em; /* Larger font */
    cursor: pointer;
    border: none;
    border-radius: 8px; /* More rounded */
    background-color: #007bff; /* Primary blue */
    color: white;
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-weight: 700;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    min-width: 60px; /* Ensure consistent button size */
  }

  .kerning-controls button:hover {
    background-color: #0056b3; /* Darker blue on hover */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }

  .kerning-controls button:active {
    background-color: #004085; /* Even darker on active */
    transform: scale(0.98); /* Slightly press effect */
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
  }

  .kerning-value {
    font-size: 1.4em; /* Larger font */
    font-weight: 700;
    color: #2c3e50;
    min-width: 80px; /* Ensure space for value */
    text-align: center;
  }

  .feedback {
    min-height: 1.5em; /* More space for feedback */
    color: #28a745; /* Green for positive feedback (if any added later) */
    font-weight: 700;
    margin-top: 15px;
  }

  .toggle-button {
    padding: 12px 25px;
    font-size: 1.1em;
    cursor: pointer;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #ecf0f1; /* Light grey background */
    color: #333;
    transition: background-color 0.3s ease, border-color 0.3s ease;
    margin-top: 25px;
    font-weight: 400;
  }

  .toggle-button:hover {
    background-color: #dcdfe4;
    border-color: #bbb;
  }

  .explanation {
    margin-top: 30px;
    padding: 25px; /* More padding */
    background-color: #e9ecef; /* Lighter grey/blue */
    border-radius: 10px;
    text-align: right;
    line-height: 1.8; /* Improved line spacing */
    border-left: 5px solid #007bff; /* Accent border */
    color: #555;
  }

  .explanation h2 {
    margin-top: 0;
    color: #0056b3;
    margin-bottom: 15px;
  }

  .explanation p {
      margin-bottom: 15px;
  }
</style>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const kerningPairEnd = document.querySelector('.kerning-pair-end');
    const decreaseButton = document.getElementById('decrease-kerning');
    const increaseButton = document.getElementById('increase-kerning');
    const kerningValueSpan = document.getElementById('kerning-value');
    const feedbackDiv = document.getElementById('feedback');
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');
    const kerningWordDiv = document.getElementById('kerning-word'); // Added reference to the word container

    let currentKerning = 0; // in pixels
    const step = 0.5; // Adjustment step

    // Function to update the kerning style
    function updateKerning() {
      kerningPairEnd.style.marginLeft = currentKerning + 'px';
      // Update CSS variable for the visual indicator
      kerningPairEnd.style.setProperty('--kerning-margin', currentKerning + 'px');
      kerningValueSpan.textContent = currentKerning.toFixed(1) + 'px';

      // Add a temporary class for animation/highlight
      kerningPairEnd.classList.add('adjusting');
      // Remove the class after the transition/animation duration
      setTimeout(() => {
         kerningPairEnd.classList.remove('adjusting');
      }, 400); // Match or slightly exceed CSS transition/animation duration

      // Clear feedback for now, focusing on the visual change
      feedbackDiv.textContent = '';
    }

    // Function to handle button clicks
    function handleKerningChange(delta) {
        currentKerning += delta;
        // Optional: Clamp values if needed, e.g., currentKerning = Math.max(-10, Math.min(10, currentKerning));
        updateKerning();

        // Add a subtle pulse effect to the word container
        kerningWordDiv.classList.add('pulse');
        setTimeout(() => {
            kerningWordDiv.classList.remove('pulse');
        }, 300); // Match pulse animation duration
    }

    // Event listeners for buttons
    decreaseButton.addEventListener('click', () => {
      handleKerningChange(-step);
    });

    increaseButton.addEventListener('click', () => {
      handleKerningChange(step);
    });

     // Optional: Add keyboard support for more interactive feel
     document.addEventListener('keydown', (event) => {
         if (event.target.tagName === 'INPUT' || event.target.tagName === 'BUTTON') {
             // Don't interfere with input fields or buttons
             return;
         }
         if (event.key === 'ArrowLeft') { // Left arrow to decrease kerning (RTL context)
             event.preventDefault(); // Prevent page scroll
             handleKerningChange(-step);
         } else if (event.key === 'ArrowRight') { // Right arrow to increase kerning (RTL context)
             event.preventDefault(); // Prevent page scroll
             handleKerningChange(step);
         }
     });


    // Event listener for explanation toggle button
    toggleButton.addEventListener('click', () => {
      const isHidden = explanationDiv.style.display === 'none';
      explanationDiv.style.display = isHidden ? 'block' : 'none';
      toggleButton.textContent = isHidden ? 'הסתר הסבר' : 'מה זה בכלל קרנינג? הצג הסבר 🧐'; // More engaging text
       // Optional: Scroll to explanation when shown
       if (isHidden) {
           explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
       }
    });

    // Initial update
    updateKerning();
  });
</script>
---