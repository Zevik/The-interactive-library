---
title: "המגנים הפנימיים: הדמיית מערכת החיסון בפעולה"
english_slug: "immune-system-simulation"
category: "ביולוגיה"
tags:
  - מערכת החיסון
  - ביולוגיה
  - הדמיה
  - תאים
  - אינטראקטיבי
  - פאגוציטוזה
---
# המגנים הפנימיים: הדמיית מערכת החיסון בפעולה

האם תהיתם פעם מה קורה ברגע שחיידק או נגיף חודר לגופכם? מתחיל מיד קרב! כוח ההגנה הפנימי שלנו, מערכת החיסון, נכנסת לפעולה במהירות הבזק. החיילים האמיצים בחזית הראשונה הם תאי הדם הלבנים - סיירים בלתי נלאים שמגלים, רודפים ובולעים את הפולשים הזרים לפני שהם מספיקים לגרום נזק. בואו נצלול פנימה ונדמה את המאבק המרתק הזה בקנה מידה מיקרוסקופי ונצפה בגיבורי מערכת החיסון בפעולה חיה ונושמת!

<div id="simulation-area">
  <div id="controls">
    <button id="start-sim" class="control-button">התחל קרב</button>
    <button id="add-pathogen" class="control-button">+ פולש (פתוגן)</button>
    <button id="add-wbc" class="control-button">+ מגֵן (תא לבן)</button>
    <div id="status">
      פולשים: <span id="pathogen-count">0</span> |
      מגנים: <span id="wbc-count">0</span>
    </div>
  </div>
  <div id="simulation-container">
    <!-- Simulation elements will be added here by JS -->
  </div>
</div>

<button id="toggle-explanation" class="info-button">הצג סיפור רקע מדעי</button>

<div id="explanation" class="hidden">
  <h2>סיפור רקע מדעי: הגיבורים הנסתרים שבתוכנו</h2>
  <p>הדמיה זו מציגה מודל אנימטיבי ופשטני לתהליך ביולוגי מדהים המתרחש בגופנו בכל רגע נתון – פעולת השורה הראשונה של מערכת החיסון – המערכת המולדת (Innate Immune System). גיבורי ההדמיה, תאי הדם הלבנים מסוגים כמו מקרופאג'ים ונויטרופילים, הם חלק ממערכת זו ונלחמים בפולשים זרים הנקראים פתוגנים (כמו חיידקים, נגיפים ופולשים אחרים).</p>

  <h3>מה ראינו בזירת הקרב הדיגיטלית?</h3>
  <ul>
    <li><strong>פולשים (עיגולים אדומים):</strong> מייצגים את הפתוגנים – האורחים הבלתי רצויים והמאיימים על בריאות הגוף. דמיינו אותם כחיידקים, נגיפים או פטריות שמנסים להשתלט.</li>
    <li><strong>מגנים (עיגולים כחולים תוססים):</strong> אלו הם תאי הדם הלבנים הגיבורים שלנו. הם מסיירים ללא הרף ברחבי "המפה" (שמדמה רקמה בגוף), מחפשים אחר כל סימן לפולש זר. הם זזים באופן דינמי ומגיבים במהירות.</li>
    <li><strong>המפגש הקריטי (בליעה - פאגוציטוזה):</strong> שיא הפעולה! כשתא דם לבן מזהה פתוגן קרוב, הוא מתמקד בו וזוחל לעברו. עם המפגש, התא הלבן עוטף את הפתוגן בתהליך מדהים שנקרא **פאגוציטוזה (Phagocytosis)** – ממש "בליעה" של הפולש לתוך התא. בתוך התא הלבן, הפתוגן מפורק ומנוטרל ביעילות. צפו באנימציה כשהתא הלבן "בולע" את הפתוגן והוא נעלם!</li>
  </ul>

  <h3>למה הקרב הזה כל כך חשוב?</h3>
  <ul>
    <li>**תגובה סופר-מהירה:** היתרון העצום של מערכת החיסון המולדת הוא המהירות. היא מגיבה תוך דקות עד שעות לחדירת פתוגנים, הרבה לפני שמערכת החיסון הנרכשת (המורכבת יותר, הכוללת נוגדנים) מספיקה להתארגן.</li>
    <li>**זיהוי כללי:** התאים הלבנים הללו לא צריכים לזהות ספציפית את סוג החיידק או הנגיף. הם מזהים "סימני היכר" כלליים המשותפים לקבוצות רחבות של פתוגנים.</li>
    <li>**קו הגנה ראשון:** מנגנונים אלו הם החומה הראשונה שמגינה עלינו מפני זיהומים יומיומיים. בלעדיהם, היינו חשופים למחלות רבות.</li>
    <li>**הפעלת אזעקה:** פעולת התאים הלבנים משחררת אותות (מולקולות) שגורמים לתהליך דלקתי מקומי – זה לא תמיד נעים (אדמומיות, נפיחות), אבל זה סימן שהגוף מגייס כוחות חיסון נוספים לאזור הפלישה!</li>
  </ul>

  <p>הדמיה זו היא רק הצצה זעירה לעולם המורכב והמרתק של מערכת החיסון. זהו מנגנון הגנה מופלא, רשת של תאים, מולקולות ואיברים הפועלים יחד בהרמוניה מדהימה כדי לשמור עלינו בריאים. פעם הבאה שאתם שומעים על "תאים לבנים" או "מערכת החיסון", זכרו את הגיבורים הבלתי נראים שנלחמים בשבילכם!</p>
</div>

<style>
  /* הוספת פונטים מודרניים (אופציונלי, תלוי זמינות) */
  @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;700&display=swap');

  body {
    font-family: 'Heebo', sans-serif;
    line-height: 1.6;
    color: #333;
    margin: 0;
    padding: 20px;
    background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2); /* Light blue gradient */
    direction: rtl; /* Ensure RTL layout */
    text-align: right;
  }

  h1, h2, h3 {
    color: #004d40; /* Dark Teal */
    margin-bottom: 10px;
  }

  h1 {
      text-align: center;
      margin-bottom: 20px;
      color: #004d40;
      font-size: 2em;
  }

  p {
      margin-bottom: 15px;
  }

  #simulation-area {
    background-color: #ffffff; /* White background for the container */
    border-radius: 12px;
    padding: 25px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    margin-bottom: 30px;
    border: 1px solid #b2ebf2; /* Light border */
  }

  #controls {
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 15px; /* Increased spacing */
    justify-content: center; /* Center controls */
  }

  .control-button, .info-button {
    padding: 12px 25px; /* More padding */
    color: white;
    border: none;
    border-radius: 25px; /* Pill shape */
    cursor: pointer;
    font-size: 1em;
    font-weight: bold;
    transition: background-color 0.3s ease, transform 0.1s ease;
    text-align: center;
    min-width: 120px; /* Minimum width */
  }

  .control-button {
      background-color: #00796b; /* Teal */
      box-shadow: 0 4px 8px rgba(0, 121, 107, 0.3);
  }

  .control-button:hover {
    background-color: #004d40; /* Darker Teal */
    transform: translateY(-2px); /* Lift effect */
  }

  .control-button:active {
      transform: translateY(0);
  }

  .info-button {
      display: block; /* Make it a block button */
      margin: 20px auto; /* Center the button */
      background-color: #558b2f; /* Dark Green */
      box-shadow: 0 4px 8px rgba(85, 139, 47, 0.3);
  }

  .info-button:hover {
      background-color: #33691e; /* Darker Green */
      transform: translateY(-2px); /* Lift effect */
  }

  .info-button:active {
      transform: translateY(0);
  }


  #status {
    margin-right: auto; /* Push status to the left (RTL) */
    font-weight: bold;
    color: #004d40; /* Match heading color */
    background-color: #e0f2f7; /* Light background */
    padding: 8px 15px;
    border-radius: 20px;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
    font-size: 0.9em;
  }

  #status span {
      color: #d32f2f; /* Red for pathogens */
  }

  #status #wbc-count {
       color: #0277bd; /* Blue for WBCs */
  }


  #simulation-container {
    position: relative;
    width: 100%;
    height: 500px; /* Increased height */
    border: 1px solid #b2ebf2; /* Match simulation area border */
    background-color: #e1f5fe; /* Very light blue */
    overflow: hidden; /* Ensure elements stay inside */
    border-radius: 8px;
    box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.05); /* Subtle inner shadow */
  }

  .pathogen, .wbc {
    position: absolute;
    border-radius: 50%;
    /* Removed transform transition from here, will handle movement via JS updates and potential CSS animations */
    box-sizing: border-box; /* Include border in size */
  }

  .pathogen {
    width: 18px; /* Slightly larger */
    height: 18px;
    background-color: #ef5350; /* Bright Red */
    border: 2px solid #c62828; /* Darker Red Border */
    box-shadow: 0 0 8px rgba(239, 83, 80, 0.6);
    transition: opacity 0.4s ease, transform 0.4s ease; /* Transition for consumption */
  }

  .wbc {
    width: 28px; /* Larger */
    height: 28px;
    background-color: #42a5f5; /* Bright Blue */
    border: 3px solid #1565c0; /* Darker Blue Border */
    box-shadow: 0 0 10px rgba(66, 165, 245, 0.8);
    animation: wbc-alive 2s infinite ease-in-out; /* More prominent animation */
    transition: opacity 0.4s ease, transform 0.4s ease; /* Transition for movement/consumption */
  }

  @keyframes wbc-alive {
    0% { transform: scale(1) rotate(0deg); }
    50% { transform: scale(1.08) rotate(2deg); }
    100% { transform: scale(1) rotate(0deg); }
  }

  /* Animation for when a pathogen is consumed */
  .consumed {
    opacity: 0;
    transform: scale(0.2); /* Shrink */
    /* transition: opacity 0.5s ease, transform 0.5s ease; <-- Defined on element class now */
  }

  #explanation {
    background-color: #e0f2f7; /* Light blue background */
    border-right: 5px solid #0277bd; /* Blue border on the right (RTL) */
    padding: 20px;
    margin-top: 30px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    line-height: 1.8; /* More space between lines */
  }

  #explanation h2 {
      margin-top: 0;
      color: #0277bd; /* Blue */
      border-bottom: 2px solid #b2ebf2; /* Light blue underline */
      padding-bottom: 5px;
      margin-bottom: 15px;
  }
   #explanation h3 {
       color: #004d40; /* Dark Teal */
       margin-top: 20px;
       margin-bottom: 10px;
   }

  #explanation ul {
      margin-bottom: 20px;
      padding-right: 20px; /* Indent list items */
  }

  #explanation li {
      margin-bottom: 10px;
      position: relative; /* For custom bullet */
  }

  /* Custom bullet point */
  #explanation li::before {
      content: '•'; /* Or use an image/icon */
      color: #00796b; /* Teal */
      font-weight: bold;
      display: inline-block;
      width: 1em;
      margin-right: -1em; /* Adjust positioning */
      position: absolute;
      right: 0; /* Position on the right for RTL */
      text-align: left; /* Ensure the bullet aligns left within its space */
  }

  #explanation li {
      padding-right: 1.5em; /* Make space for the custom bullet */
  }


  .hidden {
      display: none;
  }

  /* Responsive adjustments */
  @media (max-width: 768px) {
    #controls {
      flex-direction: column;
      align-items: stretch;
    }
    .control-button, .info-button {
      width: 100%;
      min-width: auto;
    }
    #status {
      margin-right: 0;
      margin-top: 10px;
      text-align: center;
      justify-content: center;
    }
  }

</style>

<script>
  const simContainer = document.getElementById('simulation-container');
  const startButton = document.getElementById('start-sim');
  const addPathogenButton = document.getElementById('add-pathogen');
  const addWBCButton = document.getElementById('add-wbc');
  const pathogenCountSpan = document.getElementById('pathogen-count');
  const wbcCountSpan = document.getElementById('wbc-count');
  const explanationDiv = document.getElementById('explanation');
  const toggleExplanationButton = document.getElementById('toggle-explanation');

  let simWidth = simContainer.offsetWidth;
  let simHeight = simContainer.offsetHeight;

  // Update dimensions on window resize
  const updateSimDimensions = () => {
      simWidth = simContainer.offsetWidth;
      simHeight = simContainer.offsetHeight;
      // Re-position elements might be needed on significant resize,
      // but for simplicity, we'll just ensure they stay within bounds
      // during movement in the update loop.
  };
  window.addEventListener('resize', updateSimDimensions);


  const pathogenSize = 18; // Corresponds to CSS
  const wbcSize = 34; // Corresponds to CSS (includes border)
  const consumptionDistance = wbcSize / 2 + pathogenSize / 2; // Distance at which consumption occurs

  let pathogens = [];
  let wbcs = [];
  let isRunning = false;
  let animationFrameId = null;

  // Helper function to create elements
  function createElement(className, x, y) {
    const element = document.createElement('div');
    element.classList.add(className);
    element.style.position = 'absolute';
    element.style.left = `${x}px`;
    element.style.top = `${y}px`;
    // Sizes are primarily controlled by CSS now, but we can set them initially
    if (className === 'pathogen') {
       element.style.width = `${pathogenSize}px`;
       element.style.height = `${pathogenSize}px`;
    } else { // wbc
       element.style.width = `${wbcSize}px`;
       element.style.height = `${wbcSize}px`;
    }
    simContainer.appendChild(element);
    return element;
  }

  // Add a single pathogen
  function addPathogen() {
    const x = Math.random() * (simWidth - pathogenSize);
    const y = Math.random() * (simHeight - pathogenSize);
    const element = createElement('pathogen', x, y);
    // Pathogens have random movement velocity when not targeted
    const angle = Math.random() * Math.PI * 2;
    const speed = 0.3 + Math.random() * 0.5; // Slower random movement
    pathogens.push({ element, x, y, dx: Math.cos(angle) * speed, dy: Math.sin(angle) * speed, target: null, consumed: false });
    updateCounts();
  }

  // Add a single white blood cell
  function addWBC() {
    const x = Math.random() * (simWidth - wbcSize);
    const y = Math.random() * (simHeight - wbcSize);
    const element = createElement('wbc', x, y);
    // WBCs have a speed range
    const speed = 1.5 + Math.random() * 1; // Faster movement than pathogens
    wbcs.push({ element, x, y, speed: speed, target: null });
    updateCounts();
  }

  // Update counts displayed
  function updateCounts() {
    pathogenCountSpan.textContent = pathogens.filter(p => !p.consumed).length; // Only count unconsumed
    wbcCountSpan.textContent = wbcs.length;
  }

  // Find nearest *unconsumed* pathogen for a WBC
  function findNearestPathogen(wbc) {
      let nearest = null;
      let minDistSq = Infinity;

      const availablePathogens = pathogens.filter(p => !p.consumed);

      availablePathogens.forEach(p => {
          // Use the center of the elements for distance calculation
          const pCenterX = p.x + pathogenSize / 2;
          const pCenterY = p.y + pathogenSize / 2;
          const wbcCenterX = wbc.x + wbcSize / 2;
          const wbcCenterY = wbc.y + wbcSize / 2;

          const dx = pCenterX - wbcCenterX;
          const dy = pCenterY - wbcCenterY;
          const distSq = dx * dx + dy * dy;
          if (distSq < minDistSq) {
              minDistSq = distSq;
              nearest = p;
          }
      });
      return nearest;
  }

  // Simulation loop
  function updateSimulation() {
    if (!isRunning) return;

    // Update Pathogen positions (random walk if not targeted)
    pathogens.forEach(p => {
        if (!p.consumed) {
             // Simple random walk: change direction occasionally
            if (Math.random() < 0.02) { // 2% chance to change direction
                const angle = Math.random() * Math.PI * 2;
                const speed = 0.3 + Math.random() * 0.5;
                p.dx = Math.cos(angle) * speed;
                p.dy = Math.sin(angle) * speed;
            }

            p.x += p.dx;
            p.y += p.dy;

            // Bounce off walls
            if (p.x < 0) { p.x = 0; p.dx = -p.dx; }
            if (p.x > simWidth - pathogenSize) { p.x = simWidth - pathogenSize; p.dx = -p.dx; }
            if (p.y < 0) { p.y = 0; p.dy = -p.dy; }
            if (p.y > simHeight - pathogenSize) { p.y = simHeight - pathogenSize; p.dy = -p.dy; }

            p.element.style.left = `${p.x}px`;
            p.element.style.top = `${p.y}px`;
        }
    });


    // WBC movement and targeting
    wbcs.forEach(wbc => {
      // If current target is consumed or null, find a new one
      if (!wbc.target || wbc.target.consumed) {
        wbc.target = findNearestPathogen(wbc);
      }

      if (wbc.target && !wbc.target.consumed) { // Ensure target is valid and not already consumed
        // Target the center of the pathogen
        const targetX = wbc.target.x + pathogenSize / 2;
        const targetY = wbc.target.y + pathogenSize / 2;

        // Current center of the WBC
        const wbcCenterX = wbc.x + wbcSize / 2;
        const wbcCenterY = wbc.y + wbcSize / 2;

        const dx = targetX - wbcCenterX;
        const dy = targetY - wbcCenterY;
        const distance = Math.sqrt(dx * dx + dy * dy);

        // Collision detection using center distance vs sum of radii
        if (distance < consumptionDistance) {
            // Consume the pathogen
            wbc.target.element.classList.add('consumed');
            wbc.target.consumed = true; // Mark for removal
            wbc.target = null; // Clear target for this WBC
            // Play a consumption sound? (More advanced)
            // Add a visual effect? (More advanced)
            updateCounts(); // Update counts immediately on consumption
        } else if (distance > 1) { // Move towards target (add tolerance for 'arrival')
          const moveX = (dx / distance) * wbc.speed;
          const moveY = (dy / distance) * wbc.speed;

          wbc.x += moveX;
          wbc.y += moveY;

          // Keep WBCs within bounds (optional, but good practice)
          wbc.x = Math.max(0, Math.min(wbc.x, simWidth - wbcSize));
          wbc.y = Math.max(0, Math.min(wbc.y, simHeight - wbcSize));

          wbc.element.style.left = `${wbc.x}px`;
          wbc.element.style.top = `${wbc.y}px`;
        }
        // If distance is between 0.1 and 1, they are very close, stop moving but haven't officially collided yet by the check above.
      }
       // If no target, WBC could potentially perform a random walk like pathogens,
       // but keeping them stationary when idle is simpler and shows their "patrolling" state.
    });

    // Remove elements from DOM AFTER their consumption animation completes
    // We can select elements by the 'consumed' class and set a timeout to remove them
    simContainer.querySelectorAll('.pathogen.consumed').forEach(el => {
        // Add a check to prevent setting multiple timeouts for the same element
        if (!el.dataset.removalTimeout) {
            const timeoutId = setTimeout(() => {
                 if (el.parentElement === simContainer) { // Double-check existence
                    simContainer.removeChild(el);
                    // Remove the element from the `pathogens` array as well
                    // (This is already handled by the filter next, but for clarity...)
                 }
            }, 400); // Match this duration with the CSS transition duration for '.consumed'
            el.dataset.removalTimeout = timeoutId; // Store timeout ID to prevent duplicates
        }
    });

    // Filter out consumed pathogens from the array periodically (or could be done in consumption logic)
    // pathogens = pathogens.filter(p => !p.consumed); // Moved updateCounts to consumption for faster feedback

    // Check for win condition (all pathogens consumed)
    if (pathogens.length > 0 && pathogens.filter(p => !p.consumed).length === 0) {
        // All pathogens consumed - WIN!
        if (isRunning) {
            isRunning = false;
            cancelAnimationFrame(animationFrameId);
            animationFrameId = null;
            startButton.textContent = 'קרב הסתיים בהצלחה!';
            startButton.disabled = true; // Disable button after win
             // Add a victory message or effect? (More advanced)
             // Reset button could appear.
        }
    }


    animationFrameId = requestAnimationFrame(updateSimulation);
  }

  // Start/Stop simulation
  startButton.addEventListener('click', () => {
    if (!isRunning) {
      // If button says 'קרב הסתיים בהצלחה!', reset instead of starting
      if (startButton.textContent === 'קרב הסתיים בהצלחה!') {
           initializeSimulation();
           startButton.disabled = false;
      } else {
          isRunning = true;
          startButton.textContent = 'השהה קרב';
          updateSimulation();
      }

    } else {
      isRunning = false;
      startButton.textContent = 'המשך קרב';
      cancelAnimationFrame(animationFrameId);
      animationFrameId = null; // Clear ID
    }
  });

  // Add buttons functionality
  addPathogenButton.addEventListener('click', addPathogen);
  addWBCButton.addEventListener('click', addWBC);

  // Toggle explanation visibility
  toggleExplanationButton.addEventListener('click', () => {
    explanationDiv.classList.toggle('hidden'); // Toggle the CSS class
    const isHidden = explanationDiv.classList.contains('hidden');
    toggleExplanationButton.textContent = isHidden ? 'הצג סיפור רקע מדעי' : 'הסתר סיפור רקע מדעי';
     // Optional: Scroll to explanation if showing
     if (!isHidden) {
         explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
     }
  });

  // Initial setup: Add a few elements
  function initializeSimulation() {
      // Clear previous elements safely after potential consumption animations
      simContainer.querySelectorAll('.pathogen, .wbc').forEach(el => {
           if (el.parentElement === simContainer) {
              simContainer.removeChild(el);
           }
      });

      pathogens = [];
      wbcs = [];
      isRunning = false;
      if (animationFrameId) {
          cancelAnimationFrame(animationFrameId);
          animationFrameId = null;
      }
      startButton.textContent = 'התחל קרב';
      startButton.disabled = false; // Ensure button is enabled on reset


      // Ensure explanation is hidden initially by adding the class
      explanationDiv.classList.add('hidden');
      toggleExplanationButton.textContent = 'הצג סיפור רקע מדעי';

      // Ensure dimensions are updated on load
      updateSimDimensions();

      // Add initial elements (more dynamic start?)
      for (let i = 0; i < 15; i++) { // Start with slightly more pathogens
          addPathogen();
      }
      for (let i = 0; i < 7; i++) { // Start with slightly more WBCs
          addWBC();
      }
      updateCounts();
  }

  // Run initialization when page loads
  initializeSimulation();

</script>