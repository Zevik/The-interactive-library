---
title: "מים מתאזנים: החידה הוויזואלית של כלים שלובים"
english_slug: water-leveling-connected-vessels-simulation
category: "פיזיקה והידרוסטטיקה"
tags:
  - סימולציה
  - אינטראקטיבי
  - נוזלים
  - הידרוסטטיקה
  - כלים שלובים
  - חוקי פיזיקה
---
# מים מתאזנים: החידה הוויזואלית של כלים שלובים

דמיינו שיש לכם מערכת של כלים מחוברים בתחתיתם, אבל כל כלי נראה אחרת לגמרי - אחד רחב, שני צר, שלישי עבה יותר... מה יקרה כשתתחילו למלא מים במערכת? האם המים יגיעו לגבהים שונים בכל כלי בגלל הצורה שלו, או שיקרה משהו אחר? בואו נחקור את זה דרך אנימציה אינטראקטיבית ומרהיבה!

<div class="simulation-wrapper">
  <div class="simulation-container">
    <div class="vessel-container">
      <!-- Adding visual connector -->
      <div class="connector"></div>
      <div class="vessel wide">
        <div class="water"></div>
        <span class="vessel-label">כלי רחב</span>
      </div>
      <div class="vessel narrow">
        <div class="water"></div>
        <span class="vessel-label">כלי צר</span>
      </div>
      <div class="vessel medium">
        <div class="water"></div>
         <span class="vessel-label">כלי בינוני</span>
      </div>
      <div class="vessel widest">
        <div class="water"></div>
         <span class="vessel-label">כלי רחב מאוד</span>
      </div>
       <!-- Horizontal line to visualize water level -->
      <div class="water-level-line"></div>
       <div class="equilibrium-indicator">שווי משקל הושג!</div>
    </div>
    <div class="controls">
      <div class="control-group">
        <label for="fill-speed">מהירות מילוי:</label>
        <input type="range" id="fill-speed" min="0.2" max="4" value="1.5" step="0.1">
      </div>
       <div class="button-group">
        <button id="start-fill"><i class="fas fa-play"></i> התחל</button>
        <button id="stop-fill" disabled><i class="fas fa-pause"></i> עצור</button>
        <button id="reset-fill"><i class="fas fa-redo"></i> איפוס</button>
       </div>
    </div>
  </div>
</div>

<button class="explanation-button" id="toggle-explanation"><i class="fas fa-question-circle"></i> הצג/הסתר סודות פיזיקליים</button>

<div class="explanation" id="explanation-content">
  <h2>הסבר פיזיקלי: קסם הכלים השלובים</h2>
  <p>מה שראיתם באנימציה הוא לא קסם, אלא עיקרון פיזיקלי יסודי שנקרא "כלים שלובים". העיקרון הזה קובע שנוזל במנוחה (שאינו זורם), שנמצא במערכת של כלים שמחוברים בתחתיתם ומעליהם יש את אותו לחץ (בדרך כלל הלחץ האטמוספרי הפתוח), תמיד ישאף להגיע לגובה אחיד בכל הכלים המחוברים – בלי קשר לצורה, לגודל או לנפח שלהם! המפלס האופקי שראיתם שווה בכל הכלים מדגים בדיוק את זה.</p>
  <p>למה זה קורה? הסוד טמון בלחץ. באותה רמה אופקית בתוך נוזל במנוחה, הלחץ ההידרוסטטי חייב להיות זהה. לחץ זה תלוי רק בעומק (גובה עמוד הנוזל מעל הנקודה) ובצפיפות הנוזל. אם גובה המים היה שונה בשני כלים מחוברים, הלחץ בתחתית הכלי עם המפלס הגבוה יותר היה גדול יותר. הפרש הלחצים הזה היה מייצר כוח שהיה דוחף את המים מהכלי הגבוה לנמוך, עד שהגבהים היו משתווים והלחצים היו מאזנים זה את זה מחדש.</p>
  <p>העיקרון הזה הוא הבסיס להמון דברים שאנחנו רואים בחיי היום יום: הוא עוזר למגדלי מים לספק לחץ אחיד לבתים, מאפשר לסירות לעבור במנעולים בתעלות שייט, ואפילו משמש במערכות אינסטלציה פשוטות. בפעם הבאה שתראו מים מתנהגים בצורה "מוזרה" אבל סימטרית, תזכרו את קסם הכלים השלובים!</p>
</div>


<style>
  /* Import Google Fonts for a nicer look */
  @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

  body {
      font-family: 'Heebo', sans-serif;
      line-height: 1.6;
      color: #333;
      background-color: #f8f9fa; /* Light background */
      padding: 20px;
  }

  h1, h2 {
      color: #0056b3; /* Darker blue for headings */
      text-align: center;
      margin-bottom: 20px;
  }

  p {
      margin-bottom: 15px;
  }

  .simulation-wrapper {
      display: flex;
      justify-content: center;
      margin-top: 30px;
      margin-bottom: 30px;
  }

  .simulation-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    background: linear-gradient(to bottom, #e9ecef, #dee2e6); /* Subtle gradient background */
    padding: 30px;
    border-radius: 15px; /* More rounded corners */
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Softer shadow */
    width: 100%;
    max-width: 750px; /* Wider container */
    border: 1px solid #ced4da;
  }

  .vessel-container {
    display: flex;
    align-items: flex-end;
    height: 300px; /* Increased max height for vessels */
    width: 100%;
    max-width: 650px;
    /* Removed bottom border, adding a connector element instead */
    position: relative;
    justify-content: center;
    padding-bottom: 20px; /* Space for connector */
  }

   .connector {
       position: absolute;
       bottom: 0;
       left: 0;
       right: 0;
       height: 15px; /* Thickness of the connection */
       background-color: #6c757d; /* Grey color for connector */
       border-radius: 0 0 10px 10px; /* Slightly rounded bottom */
       box-shadow: inset 0 5px 10px rgba(0,0,0,0.2);
       z-index: 0; /* Behind vessels */
   }

  .vessel {
    position: relative;
    bottom: 0;
    border: 2px solid #495057; /* Darker border */
    border-bottom: none; /* Connector acts as bottom */
    height: 250px; /* Actual vessel height above connector base */
    margin: 0 15px; /* Increased margin */
    display: flex;
    flex-direction: column-reverse; /* Water fills from bottom */
    overflow: hidden; /* Hide water above vessel height */
    box-sizing: border-box;
    background-color: rgba(255, 255, 255, 0.7); /* Semi-transparent vessel body */
    border-radius: 5px 5px 0 0; /* Rounded top corners */
     z-index: 1; /* Above connector */
      width: 80px; /* Base width */
  }

  .vessel.wide {
    width: 120px; /* Wider */
  }

  .vessel.narrow {
    width: 60px; /* Narrower */
  }

  .vessel.medium {
    width: 90px; /* Medium */
  }
   .vessel.widest {
    width: 150px; /* Widest */
  }

   .vessel-label {
       position: absolute;
       bottom: -25px; /* Position below the vessel */
       left: 50%;
       transform: translateX(-50%);
       font-size: 0.9em;
       color: #555;
       white-space: nowrap; /* Prevent wrapping */
   }


  .water {
    width: 100%;
    height: 0; /* Start empty */
    background: linear-gradient(to top, #0077cc, #00aaff); /* Blue gradient */
    transition: height 0.3s ease-out; /* Slower, smoother transition */
    position: absolute;
    bottom: 0;
    left: 0;
     box-shadow: inset 0 5px 10px rgba(0,0,0,0.1); /* Inner shadow for depth */
  }

   .water-level-line {
       position: absolute;
       bottom: 0px; /* Starts at the connector base */
       left: 0;
       right: 0;
       height: 2px; /* Thin line */
       background-color: #ff0000; /* Red line for visibility */
       z-index: 2; /* Above water */
       transition: bottom 0.3s ease-out; /* Animate the line position */
       display: none; /* Hide until simulation starts */
   }

    .equilibrium-indicator {
        position: absolute;
        top: 10px; /* Position at the top of the container */
        left: 50%;
        transform: translateX(-50%);
        background-color: #28a745; /* Green */
        color: white;
        padding: 8px 15px;
        border-radius: 5px;
        font-weight: bold;
        display: none; /* Hidden by default */
        opacity: 0;
        transition: opacity 0.5s ease-in-out;
        z-index: 3; /* Above everything */
    }

   .equilibrium-indicator.visible {
       display: block;
       opacity: 1;
   }


  .controls {
    margin-top: 30px;
    display: flex;
    flex-direction: column; /* Stack controls vertically on small screens */
    align-items: center;
    gap: 20px; /* Space between control groups */
    width: 100%;
  }

    .control-group {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .button-group {
        display: flex;
        gap: 10px; /* Space between buttons */
        flex-wrap: wrap;
        justify-content: center;
    }


  .controls label {
      font-weight: bold;
      color: #555;
  }

  .controls input[type="range"] {
      -webkit-appearance: none; /* Override default appearance */
      appearance: none;
      width: 150px; /* Width of slider */
      height: 8px;
      background: #ddd;
      outline: none;
      opacity: 0.7;
      transition: opacity .2s;
      border-radius: 5px;
  }

  .controls input[type="range"]:hover {
      opacity: 1;
  }

  .controls input[type="range"]::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 20px;
      height: 20px;
      background: #007bff; /* Blue thumb */
      cursor: pointer;
      border-radius: 50%; /* Round thumb */
      border: 2px solid #fff;
      box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  }

  .controls input[type="range"]::-moz-range-thumb {
      width: 20px;
      height: 20px;
      background: #007bff;
      cursor: pointer;
      border-radius: 50%;
      border: 2px solid #fff;
      box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  }


  .controls button {
    padding: 10px 20px; /* Larger padding */
    border: none;
    border-radius: 25px; /* Pill-shaped buttons */
    cursor: pointer;
    font-size: 1rem;
    font-weight: bold;
    transition: background-color 0.3s ease, transform 0.1s ease, opacity 0.3s ease;
    display: flex; /* Use flexbox for icon and text */
    align-items: center;
    gap: 5px; /* Space between icon and text */
  }

  .controls button i {
      /* Icon styling if using Font Awesome */
  }

  #start-fill {
    background-color: #28a745; /* Green */
    color: white;
  }

  #start-fill:hover:not(:disabled) {
    background-color: #218838; /* Darker green */
     transform: translateY(-2px); /* Slight lift on hover */
  }

  #start-fill:active:not(:disabled) {
     transform: translateY(0); /* Press effect */
  }


  #start-fill:disabled {
    background-color: #94d3a2;
    cursor: not-allowed;
    opacity: 0.7;
  }

  #stop-fill {
    background-color: #dc3545; /* Red */
    color: white;
  }
   #stop-fill:hover:not(:disabled) {
    background-color: #c82333; /* Darker red */
     transform: translateY(-2px);
  }
   #stop-fill:active:not(:disabled) {
     transform: translateY(0);
  }
   #stop-fill:disabled {
    background-color: #e9949c;
    cursor: not-allowed;
    opacity: 0.7;
  }

  #reset-fill {
    background-color: #007bff; /* Blue */
    color: white;
  }
   #reset-fill:hover:not(:disabled) {
    background-color: #0069d9; /* Darker blue */
     transform: translateY(-2px);
  }
   #reset-fill:active:not(:disabled) {
     transform: translateY(0);
  }

   #reset-fill:disabled {
     background-color: #8ac2ff;
     cursor: not-allowed;
     opacity: 0.7;
  }

  .explanation-button {
    display: block; /* Make it a block element */
    margin: 30px auto; /* Center the button */
    padding: 12px 25px; /* More padding */
    background-color: #ffc107; /* Yellow */
    border: none;
    border-radius: 25px; /* Pill shape */
    cursor: pointer;
    font-size: 1.1rem; /* Larger font */
    font-weight: bold;
    color: #333; /* Dark text */
    transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Shadow */
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .explanation-button:hover {
    background-color: #e0a800; /* Darker yellow */
     transform: translateY(-3px);
     box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
  }
   .explanation-button:active {
       transform: translateY(-1px);
       box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
   }


  .explanation {
    margin: 20px auto; /* Center the explanation box */
    padding: 25px; /* More padding */
    background-color: #e9ecef;
    border-radius: 10px;
    display: none; /* Hidden by default */
    max-width: 700px;
    line-height: 1.7;
    border-left: 5px solid #007bff; /* Accent border */
  }

  .explanation h2 {
    margin-top: 0;
    color: #0056b3;
    border-bottom: 1px solid #ced4da; /* Separator line */
    padding-bottom: 10px;
    margin-bottom: 15px;
  }

  .explanation p:last-child {
      margin-bottom: 0;
  }

  /* Responsive adjustments */
  @media (max-width: 600px) {
      .vessel-container {
          flex-wrap: wrap; /* Allow vessels to wrap */
          justify-content: center;
          height: auto; /* Auto height when wrapping */
          padding-bottom: 40px; /* More space for labels/connector */
      }
      .vessel {
          margin: 10px; /* Adjust margin for wrapping */
          height: 150px; /* Smaller height on small screens */
      }
      .water {
           transition: height 0.2s ease-out; /* Faster transition on smaller devices */
      }
      .water-level-line {
          /* Might need more complex positioning if vessels wrap significantly */
          /* For simplicity, keep it absolute bottom and assume some vertical space */
      }
       .controls {
           flex-direction: column;
           gap: 15px;
       }
       .button-group {
           flex-direction: column;
           align-items: center;
       }
       .controls button {
           width: 80%; /* Make buttons wider */
           justify-content: center;
       }
       .explanation {
           padding: 20px;
       }
  }

</style>

<script>
  // Load Font Awesome for icons if not already loaded
  if (!document.querySelector('link[href*="font-awesome"]')) {
      const link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css';
      document.head.appendChild(link);
  }


  const waterElements = document.querySelectorAll('.vessel .water');
  const vessels = document.querySelectorAll('.vessel');
  const vesselContainer = document.querySelector('.vessel-container'); // Get container for line positioning
  const fillSpeedControl = document.getElementById('fill-speed');
  const startButton = document.getElementById('start-fill');
  const stopButton = document.getElementById('stop-fill');
  const resetButton = document.getElementById('reset-fill');
  const toggleExplanationButton = document.getElementById('toggle-explanation');
  const explanationContent = document.getElementById('explanation-content');
  const waterLevelLine = document.querySelector('.water-level-line');
  const equilibriumIndicator = document.querySelector('.equilibrium-indicator');

  let waterLevel = 0; // Global water level in pixels, measured from the bottom of the *vessel container*
  // Max height of the vessels is 250px above the connector. The connector is 15px high.
  // The vessel container has 20px padding-bottom.
  // The water level 0 should be at the top of the connector (bottom of the vessel visual part).
  // The connector is at bottom: 0 relative to vessel-container. Its height is 15px.
  // Water starts filling *above* the connector.
  // Max water level should correspond to the top of the vessels.
  // The vessels are 250px high.
  // The bottom of the vessels is 15px from the very bottom of the vessel-container (height of connector).
  // The water level `height` CSS property is relative to the bottom of the *vessel div*.
  // The vessel div's bottom is position: relative; bottom: 0; inside the vessel-container.
  // Ah, the CSS has `position: absolute; bottom: 0; left: 0;` for `.water`. This means the `height` of the water is relative to the bottom of its parent `.vessel`.
  // The `.vessel` itself has `position: relative; bottom: 0;`. This places the bottom of the vessel visually at the top of the connector.
  // So, the `waterLevel` variable should represent the height of water *within* the vessel, measured from the bottom of the vessel's interior (top of the connector).
  // The max height is the height of the vessel div: 250px.
  const maxLevel = 250; // Max height water can reach inside a vessel (matches vessel height CSS)

  let animationFrameId = null;
  let isFilling = false;

  function updateWaterLevel() {
    if (!isFilling) {
      cancelAnimationFrame(animationFrameId);
      return;
    }

    const fillSpeed = parseFloat(fillSpeedControl.value);
    // Increase speed is proportional to fillSpeed value
    let levelIncrease = fillSpeed * (maxLevel / 600); // Scale increase based on max height and target duration (e.g., 10s for speed 1)

    // Increase the global water level (which is the height *within* the vessel)
    waterLevel += levelIncrease;

    // Ensure water level does not exceed maxLevel
    waterLevel = Math.min(waterLevel, maxLevel);

    // Update water height in each vessel
    waterElements.forEach(waterEl => {
        // The height property of .water directly corresponds to waterLevel
        waterEl.style.height = `${waterLevel}px`;
    });

    // Update the position of the horizontal water level line
    // The line's 'bottom' property should be relative to the vessel-container.
    // The bottom of the vessel is 0 relative to the vessel-container (position: relative; bottom: 0;).
    // The height of the waterLevel is measured from the bottom of the vessel.
    // So, the line's bottom position is the waterLevel height + the height of the connector (15px) + the padding-bottom of the vessel-container (20px).
    // Wait, the CSS for .water-level-line has `bottom: 0px;`. This needs to be relative to the *top* of the connector.
    // Let's change the CSS `bottom: 0px;` to `bottom: 15px;` (height of connector). Then its `bottom` property can just be `waterLevel + 15px`.
    // Let's re-check the HTML structure. The line is inside vessel-container.
    // vessel-container has `align-items: flex-end` and `padding-bottom: 20px`. The connector is `position: absolute; bottom: 0; height: 15px;`.
    // The vessels are `position: relative; bottom: 0;` and sit on top of the connector area.
    // The water in the vessel has `position: absolute; bottom: 0;` within the vessel.
    // So, the bottom of the water (`height: 0`) is aligned with the bottom of the vessel.
    // The water level line needs to be at the *top* of the water column.
    // Its position from the bottom of the vessel-container should be `waterLevel` (height in vessel) + `15px` (connector) + `20px` (padding-bottom). This seems complex.

    // Let's rethink the coordinate system.
    // Assume the bottom of the visual vessels (top of connector) is the reference point (y=0).
    // Water level is `waterLevel` pixels above this reference. Max height is `maxLevel`.
    // The water element's `height` property directly reflects `waterLevel`.
    // The `.vessel-container` has `height: 300px` and `padding-bottom: 20px`.
    // The `connector` is at `bottom: 0` and `height: 15px`.
    // The vessels sit on top of the connector area. The visual bottom of the vessels is `15px` from the container bottom.
    // The water level line is `position: absolute` inside the container.
    // Its `bottom` property should be `waterLevel` (measured from vessel bottom) + `15px` (connector height).
    // Let's adjust the CSS `bottom` for `.water-level-line` to be relative to the container's bottom edge.
    // The height of the water inside the vessel is `waterLevel`. This height is measured from the bottom of the vessel (which is 15px from container bottom).
    // So, the absolute position of the water surface from the container bottom is `waterLevel + 15px`.
     waterLevelLine.style.bottom = `${waterLevel + 15}px`;


    // Check if the global water level has reached the maximum vessel height
    if (waterLevel >= maxLevel) {
        isFilling = false;
        stopButton.disabled = true;
        startButton.disabled = true; // Cannot start if already full
        resetButton.disabled = false;
        showEquilibriumIndicator();
        cancelAnimationFrame(animationFrameId);
        return;
    }

    // Continue animation if global water level is below maxLevel
    animationFrameId = requestAnimationFrame(updateWaterLevel);
  }

  function startFilling() {
    if (!isFilling && waterLevel < maxLevel) {
      isFilling = true;
      startButton.disabled = true;
      stopButton.disabled = false;
      resetButton.disabled = false;
      hideEquilibriumIndicator();
      waterLevelLine.style.display = 'block'; // Show the line
      animationFrameId = requestAnimationFrame(updateWaterLevel);
    }
  }

  function stopFilling() {
    isFilling = false;
    startButton.disabled = false;
    stopButton.disabled = true;
    // Keep reset enabled if not at 0
    if (waterLevel > 0) {
      resetButton.disabled = false;
    } else {
      resetButton.disabled = true;
    }
    cancelAnimationFrame(animationFrameId);
  }

  function resetFilling() {
    stopFilling(); // Ensure animation stops and buttons are in stop state
    waterLevel = 0;
    waterElements.forEach(waterEl => {
      waterEl.style.height = '0px';
    });
    // Reset line position to the bottom (top of connector)
    waterLevelLine.style.bottom = '15px'; // Height of connector
    waterLevelLine.style.display = 'none'; // Hide the line when empty
    hideEquilibriumIndicator();
    startButton.disabled = false;
    stopButton.disabled = true; // Stop is disabled when starting from 0
    resetButton.disabled = true; // Reset is disabled when at 0
  }

  function showEquilibriumIndicator() {
      equilibriumIndicator.classList.add('visible');
  }

  function hideEquilibriumIndicator() {
       equilibriumIndicator.classList.remove('visible');
  }


  // Event listeners
  startButton.addEventListener('click', startFilling);
  stopButton.addEventListener('click', stopFilling);
  resetButton.addEventListener('click', resetFilling);

  // Initial state
  resetButton.disabled = true; // Disable reset until started or stopped mid-fill
  stopButton.disabled = true; // Stop is disabled until filling starts
   waterLevelLine.style.display = 'none'; // Hide line initially
   hideEquilibriumIndicator(); // Hide indicator initially

  // Explanation toggle
  toggleExplanationButton.addEventListener('click', () => {
    const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
    explanationContent.style.display = isHidden ? 'block' : 'none';
    // Optional: Change button text based on state
    // toggleExplanationButton.innerHTML = isHidden ? '<i class="fas fa-minus-circle"></i> הסתר סודות פיזיקליים' : '<i class="fas fa-question-circle"></i> הצג/הסתר סודות פיזיקליים';
  });

  // Initialize explanation state
  explanationContent.style.display = 'none';

  // Initialize water level line position (at the base)
  waterLevelLine.style.bottom = '15px'; // Corresponds to the top of the 15px high connector

</script>