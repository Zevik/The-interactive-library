---
title: "הדמיה של תנועת לוחות טקטוניים"
english_slug: tectonic-plate-movement-simulation
category: "גאולוגיה"
tags: ["הדמיה", "טקטוניקה", "לוחות", "גאולוגיה", "כדור הארץ", "מדע"]
---
# הדמיה: הלוחות הטקטוניים בפעולה!

דמיינו את פני כדור הארץ כפסיפס ענק של לוחות סלע אדירים, הלוחות הטקטוניים, המרחפים באיטיות על גבי השכבה החמה והצמיגה שמתחת. התנועה הכמעט בלתי מורגשת שלהם היא הכוח המניע מאחורי הרי הגעש המתפרצים, רעידות האדמה המחרידות, ורכסי ההרים המתנשאים. בואו נצלול עמוק ונחזה כיצד הלוחות הללו מתנהגים בגבולות המפגש שלהם.

<div class="simulation-container">
    <div class="controls">
        <label for="movement-type">בחר סוג מפגש לוחות:</label>
        <select id="movement-type">
            <option value="convergent">מתכנסים (התנגשות)</option>
            <option value="divergent">מתרחקים (היפרדות)</option>
            <option value="transform">החלקה (חיכוך)</option>
        </select>
        <button id="start-simulation">התחל פעולה!</button>
    </div>
    <div class="simulation-area">
        <div class="plate plate-left">
            <span class="plate-label">לוח א'</span>
            <div class="plate-feature continent"></div>
            <div class="plate-feature ocean"></div>
        </div>
        <div class="boundary-area">
             <div class="boundary-effect subduction"></div>
             <div class="boundary-effect collision"></div>
             <div class="boundary-effect rift"></div>
             <div class="boundary-effect transform-crack"></div>
        </div>
        <div class="plate plate-right">
             <span class="plate-label">לוח ב'</span>
             <div class="plate-feature continent"></div>
             <div class="plate-feature ocean"></div>
        </div>
         <!-- Effects container for shared effects like shaking -->
         <div class="global-effects"></div>
    </div>
    <div class="reset-button-container">
         <button id="reset-simulation">איפוס</button>
    </div>
</div>

<button id="show-explanation" class="show-explanation-button">הסבר לי מה קורה כאן!</button>

<div id="explanation" class="explanation-section">
    <h2>מסע אל גבולות הלוחות</h2>
    <p>הקרום הקשיח של כדור הארץ, הליתוספירה, אינו יחידה אחת. הוא מפוצל ללוחות ענק שנמצאים בתנועה מתמדת על גבי האסתנוספירה החצי-נוזלית. רוב הפעילות הגיאולוגית הדרמטית (רעידות אדמה, הרי געש, בניית הרים) מתרחשת בגבולות שבהם לוחות אלו נפגשים. קיימים שלושה סוגי גבולות עיקריים:</p>

    <h3>1. גבולות מתכנסים (Convergent Boundaries)</h3>
    <p>כאשר שני לוחות נעים זה לקראת זה ומתנגשים בעוצמה. התוצאות משתנות בהתאם לסוגי הלוחות המעורבים:</p>
    <ul>
        <li><strong>קרום ימי וקרום יבשתי:</strong> הקרום הימי, הצפוף יותר, צולל מתחת לקרום היבשתי בתהליך הנקרא סובדוקציה. נוצרות שוחות אוקייניות עמוקות ורכסי הרי געש ביבשה (לדוגמה: הרי האנדים בדרום אמריקה).</li>
        <li><strong>קרום ימי וקרום ימי:</strong> לוח ימי אחד עובר סובדוקציה מתחת לשני. התוצאה היא שוחה אוקיינית וקשת איים געשיים (לדוגמה: יפן והפיליפינים).</li>
        <li><strong>קרום יבשתי וקרום יבשתי:</strong> הלוחות היבשתיים פחות צפופים ולא שוקעים בקלות. ההתנגשות האדירה מקמטת ומרימה את הקרום ויוצרת רכסי הרים עצומים ולא געשיים (לדוגמה: הרי ההימלאיה).</li>
    </ul>

    <h3>2. גבולות מתרחקים (Divergent Boundaries)</h3>
    <p>כאשר שני לוחות נעים ומתרחקים זה מזה. במרחב שנוצר עולה מאגמה מהמעטפת ומתמצקת ליצירת קרום חדש. תהליך זה מתרחש בעיקר ברכסים מרכז-אוקייניים היוצרים קרקעית אוקיינוס חדשה, וביבשה הוא יוצר עמקי בקע רחבים (לדוגמה: הבקע הסורי-אפריקאי).</p>

    <h3>3. גבולות טרנספורם (Transform Boundaries)</h3>
    <p>כאשר שני לוחות מחליקים זה לצד זה בכיוונים מנוגדים או באותו כיוון אך במהירויות שונות. בגבולות אלו אין יצירה או הרס משמעותי של קרום, אך החיכוך האדיר גורם להצטברות מתח המשתחרר ברעידות אדמה תכופות וחזקות (לדוגמה: העתק סן אנדראס בקליפורניה). הסימולציה מציגה תנועה פשטנית לעיקרון ההחלקה.</p>

    <p>ההדמיה כאן מציגה מודל פשטני המדגים את התנועה היחסית הבסיסית בגבולות אלו. במציאות, התהליכים מורכבים ואיטיים הרבה יותר!</p>
</div>

<style>
    :root {
        --earth-brown: #8B4513; /* SaddleBrown */
        --ocean-blue: #1E90FF; /* DodgerBlue */
        --mantle-red: #DC143C; /* Crimson for magma/heat */
        --mountain-grey: #A9A9A9; /* DarkGrey */
        --crack-color: #333;
        --bg-color: #f0f8ff; /* AliceBlue */
        --card-bg: #ffffff;
        --primary-blue: #007bff;
        --primary-green: #28a745;
        --primary-orange: #ffc107;
        --text-dark: #343a40;
        --text-secondary: #6c757d;
        --border-color: #ced4da;
    }

    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        direction: rtl;
        text-align: right;
        background-color: var(--bg-color);
        padding: 20px;
        line-height: 1.7;
        color: var(--text-dark);
    }

    h1, h2, h3 {
        color: var(--primary-blue);
        text-align: center;
        margin-bottom: 20px;
        font-weight: 600;
    }
     h2, h3 {
         text-align: right; /* Align explanation headers right */
     }


    p, ul {
        color: var(--text-secondary);
        margin-bottom: 15px;
    }

    ul {
        padding-right: 20px;
    }

    .simulation-container {
        background-color: var(--card-bg);
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        padding: 25px;
        margin: 30px auto;
        max-width: 750px;
        overflow: hidden; /* Ensure animations stay within bounds */
    }

    .controls {
        margin-bottom: 25px;
        text-align: center;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        gap: 15px;
    }

    .controls label {
        margin: 0;
        font-weight: bold;
        color: var(--text-dark);
    }

    .controls select, .controls button {
        padding: 10px 15px;
        border: 1px solid var(--border-color);
        border-radius: 6px;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.1s ease;
        font-family: inherit;
    }

     .controls select:focus, .controls button:focus {
         outline: none;
         border-color: var(--primary-blue);
         box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
     }

    .controls button {
        background-color: var(--primary-green);
        color: white;
        border-color: var(--primary-green);
    }

    .controls button:hover {
        background-color: #218838;
        border-color: #1e7e34;
        transform: translateY(-1px);
    }
     .controls button:active {
         transform: translateY(0);
     }


    .simulation-area {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: 250px; /* Increased height for more visual space */
        overflow: hidden;
        position: relative;
        background: linear-gradient(to bottom, #87ceeb 0%, #e0f6ff 50%, var(--ocean-blue) 100%); /* Sky to Ocean gradient */
        border: 2px solid var(--border-color);
        border-radius: 8px;
        box-sizing: border-box;
        perspective: 1000px; /* For 3D effects if needed */
    }

     .global-effects {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         pointer-events: none; /* Allow clicking through */
         z-index: 10; /* Above plates and boundary */
     }

     .simulation-area.shaking .global-effects {
         animation: shake 0.5s infinite cubic-bezier(.36,.07,.19,.97) both;
          transform: translate3d(0, 0, 0); /* Optimize for transform */
          backface-visibility: hidden;
     }

     @keyframes shake {
        10%, 90% { transform: translate3d(-1px, 0, 0); }
        20%, 80% { transform: translate3d(2px, 0, 0); }
        30%, 50%, 70% { transform: translate3d(-4px, 0, 0); }
        40%, 60% { transform: translate3d(4px, 0, 0); }
     }


    .plate {
        width: 50%; /* Start edge-to-edge */
        height: 100%;
        position: relative;
        box-sizing: border-box;
        transition: transform 3s ease-in-out; /* Longer, smoother transition */
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: bold;
        font-size: 1.3rem;
        z-index: 2; /* Above boundary effects */
        background-size: cover; /* Ensure patterns cover the area */
        background-position: center;
         overflow: hidden; /* Hide internal features outside plate */
    }

     .plate-label {
         position: absolute;
         bottom: 10px;
         left: 10px;
         color: white;
         text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
         font-size: 1.1rem;
         z-index: 5; /* Above plate features */
     }
      .plate-right .plate-label {
          left: auto;
          right: 10px;
      }


    .plate-left {
         /* Default state: no transform */
         transform-origin: right center;
         border-right: none;
         background-image: url('https://via.placeholder.com/300x250/a0522d/ffffff?text='); /* Earth texture placeholder */
         border-radius: 8px 0 0 8px;
    }

    .plate-right {
         /* Default state: no transform */
         transform-origin: left center;
         border-left: none;
         background-image: url('https://via.placeholder.com/300x250/a0522d/ffffff?text='); /* Earth texture placeholder */
         border-radius: 0 8px 8px 0;
    }

     /* Add internal features for plate types (optional, but adds depth) */
     /* These would need JS logic to swap based on imagined plate types */
     /* For simplicity, let's style the plates based on movement outcome */

    .boundary-area {
        width: 5px; /* Minimal width initially */
        height: 100%;
        position: relative;
        z-index: 1; /* Below plates */
        overflow: visible; /* Allow effects to spill over slightly */
    }

    /* Animation States */
    .simulation-area.convergent .plate-left {
        transform: translateX(25%);
    }
    .simulation-area.convergent .plate-right {
        transform: translateX(-25%);
    }

    .simulation-area.divergent .plate-left {
        transform: translateX(-25%);
    }
    .simulation-area.divergent .plate-right {
        transform: translateX(25%);
    }

    .simulation-area.transform .plate-left {
        transform: translateY(-30px); /* Example vertical slide */
    }
    .simulation-area.transform .plate-right {
        transform: translateY(30px); /* Example vertical slide */
    }

    /* --- Boundary Effects --- */

    .boundary-effect {
        position: absolute;
        display: none; /* Hidden by default */
        pointer-events: none;
    }

    /* Convergent - Collision (Mountains) */
    .simulation-area.convergent .boundary-effect.collision {
        display: block;
        bottom: 0;
        left: 45%; /* Centered between the now-collided plates */
        width: 10%; /* Area where mountains rise */
        height: 50%; /* Height of mountains */
        background: linear-gradient(to top, var(--mountain-grey), #ccc);
        border-radius: 5px 5px 0 0;
        transform-origin: bottom center;
        animation: growMountains 3s ease-in-out forwards;
        z-index: 3; /* Above plates */
        filter: drop-shadow(2px 2px 3px rgba(0,0,0,0.3));
    }
     @keyframes growMountains {
        0% { transform: scaleY(0); }
        50% { transform: scaleY(1.1); } /* Overshoot slightly */
        100% { transform: scaleY(1); }
     }


    /* Convergent - Subduction (Trench/Volcano - Simplified) */
     .simulation-area.convergent .boundary-effect.subduction {
         display: block;
         bottom: 0;
         left: 48%; /* Position near the boundary */
         width: 4px; /* Trench line */
         height: 100%; /* Goes full depth */
         background: linear-gradient(to bottom, rgba(0,0,0,0.5), rgba(0,0,0,0.1)); /* Darker trench */
         animation: formTrench 3s ease-in-out forwards;
          z-index: 3;
     }
      @keyframes formTrench {
          0% { transform: scaleY(0); }
          100% { transform: scaleY(1); }
      }
     /* Add a simple volcano effect on the overriding plate */
     .simulation-area.convergent .plate-left::after { /* Or plate-right, depends on which one subducts */
          content: '';
          display: block;
          position: absolute;
          bottom: 50px; /* Position above sea level */
          right: 20px; /* On the overriding plate */
          width: 30px;
          height: 40px;
          background: linear-gradient(to top, #b22222, #dc143c); /* FireBrick to Crimson */
          clip-path: polygon(50% 0%, 0% 100%, 100% 100%); /* Triangle shape */
          transform-origin: bottom center;
          transform: scale(0); /* Start hidden */
          animation: eruptVolcano 3s ease-in-out forwards;
          z-index: 4;
          filter: drop-shadow(1px 1px 2px rgba(0,0,0,0.5));
     }
      @keyframes eruptVolcano {
          0% { transform: scale(0); opacity: 0; }
          70% { transform: scale(1); opacity: 1; }
          100% { opacity: 0.8; } /* Stay visible but slightly transparent */
      }


    /* Divergent (Rift Valley / Mid-Ocean Ridge) */
    .simulation-area.divergent .boundary-effect.rift {
        display: block;
        top: 0;
        left: 45%; /* Position between separating plates */
        width: 10%; /* Width of the rift area */
        height: 100%;
        background: linear-gradient(to top, var(--mantle-red) 0%, orange 50%, yellow 80%, transparent 100%); /* Magma glow effect */
        animation: openRift 3s ease-in-out forwards;
         z-index: 0; /* Below plates */
    }
     @keyframes openRift {
        0% { width: 0%; left: 50%; }
        100% { width: 10%; left: 45%; }
     }


    /* Transform (Cracks) */
    .simulation-area.transform .boundary-effect.transform-crack {
        display: block;
        top: 0;
        left: 50%; /* Centered initially */
        width: 2px; /* Crack line */
        height: 100%;
        background-color: var(--crack-color);
        transform: translateY(0);
        animation: slideCrack 3s ease-in-out forwards;
        z-index: 3;
    }
     @keyframes slideCrack {
        0% { transform: translateY(0); }
        100% { transform: translateY(-30px); /* Matches plate movement */ }
     }
     /* Add another crack for visual effect */
      .simulation-area.transform .boundary-effect.transform-crack::after {
          content: '';
          display: block;
          position: absolute;
          top: 0;
          left: -10px; /* Offset slightly */
          width: 2px;
          height: 100%;
          background-color: var(--crack-color);
          transform: translateY(0);
          animation: slideCrackAlt 3s ease-in-out forwards;
      }
       @keyframes slideCrackAlt {
        0% { transform: translateY(0); }
        100% { transform: translateY(30px); /* Opposite direction */ }
     }
     /* Add shaking effect */
      .simulation-area.transform.shaking {
         animation: shake 0.5s infinite cubic-bezier(.36,.07,.19,.97) both;
          transform: translate3d(0, 0, 0);
          backface-visibility: hidden;
      }


    .reset-button-container {
        text-align: center;
        margin-top: 20px;
    }

    #reset-simulation {
        background-color: var(--primary-orange);
        color: var(--text-dark);
        border-color: var(--primary-orange);
    }
    #reset-simulation:hover {
         background-color: #ffb300;
         border-color: #ffb300;
         transform: translateY(-1px);
    }
     #reset-simulation:active {
         transform: translateY(0);
     }


    .show-explanation-button {
        display: block;
        margin: 30px auto 10px auto; /* Add space below */
        padding: 12px 20px;
        background-color: var(--primary-blue);
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 1.1rem;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-family: inherit;
    }

    .show-explanation-button:hover {
        background-color: #0056b3;
        transform: translateY(-1px);
    }
     .show-explanation-button:active {
         transform: translateY(0);
     }


    .explanation-section {
        background-color: #e9ecef; /* Light grey-blue */
        border-left: 5px solid var(--primary-blue);
        padding: 20px;
        margin-top: 20px;
        border-radius: 8px;
        display: none; /* Hidden by default */
        animation: fadeIn 0.6s ease-in-out;
    }

    .explanation-section h3 {
        color: #5a6268; /* Darker grey */
        margin-top: 20px;
        margin-bottom: 8px;
        font-weight: 600;
    }

     .explanation-section ul {
         list-style-type: disc;
         padding-right: 25px;
     }

     .explanation-section li {
         margin-bottom: 8px;
     }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

     /* Hide plate features by default - JS/CSS could show specific ones */
     .plate-feature {
         display: none;
     }


</style>

<script>
    const startButton = document.getElementById('start-simulation');
    const resetButton = document.getElementById('reset-simulation');
    const movementTypeSelect = document.getElementById('movement-type');
    const simulationArea = document.querySelector('.simulation-area');
    const plates = document.querySelectorAll('.plate');
    const boundaryEffects = document.querySelectorAll('.boundary-effect'); // Get all effects
    const explanationButton = document.getElementById('show-explanation');
    const explanationDiv = document.getElementById('explanation');

    // Define effect classes corresponding to movement types
    const effectClasses = {
        convergent: ['collision', 'subduction'], // Can have multiple effects active
        divergent: ['rift'],
        transform: ['transform-crack']
    };

    function resetSimulation() {
        // Remove all movement and effect classes from simulationArea
        simulationArea.classList.remove('convergent', 'divergent', 'transform', 'shaking');

        // Remove all specific boundary effect classes from boundary-effect elements
        boundaryEffects.forEach(effect => {
            effect.classList.forEach(className => {
                if (className !== 'boundary-effect') { // Keep the base class
                    effect.classList.remove(className);
                }
            });
             effect.style.display = 'none'; // Explicitly hide effects
             effect.style.animation = 'none'; // Stop animations
        });

        // Reset plate positions visually by removing transforms
        plates.forEach(plate => {
            plate.style.transform = 'none';
             // Remove any added pseudo-element animations if needed
             plate.classList.remove('erupting'); // Example class if used for pseudo-element control
        });

        // Force reflow to restart animations on next 'start' click
        void simulationArea.offsetWidth;

        // Re-hide volcano pseudo-element if it was added/animated
        const volcano = document.querySelector('.plate-left::after, .plate-right::after'); // Select potential pseudo-elements
         if(volcano) {
            // Cannot directly manipulate pseudo-elements with JS.
            // Need to control via parent class on the plate.
            // Let's add a class to the plate that controls the pseudo-element visibility/animation.
             plates.forEach(plate => plate.classList.remove('show-volcano'));
         }


        startButton.disabled = false; // Enable start button
    }

    function startSimulation() {
        startButton.disabled = true; // Disable start button while animating
        resetSimulation(); // Always reset before starting a new simulation

        const selectedType = movementTypeSelect.value;

        // Add the main movement class to simulationArea
        simulationArea.classList.add(selectedType);

        // Add specific effect classes to the corresponding boundary-effect elements
        if (effectClasses[selectedType]) {
            effectClasses[selectedType].forEach(effectName => {
                 const effectElement = simulationArea.querySelector(`.boundary-effect.${effectName}`);
                 if(effectElement) {
                      effectElement.style.display = 'block'; // Show the effect element
                     // Re-apply animation by setting/resetting it
                     effectElement.style.animation = 'none';
                     void effectElement.offsetWidth; // Trigger reflow
                     if (effectName === 'collision') effectElement.style.animation = 'growMountains 3s ease-in-out forwards';
                     if (effectName === 'subduction') {
                         effectElement.style.animation = 'formTrench 3s ease-in-out forwards';
                         // Trigger volcano animation on the specific plate (e.g., plate-left)
                         // This requires adding a class to the plate itself
                         simulationArea.querySelector('.plate-left').classList.add('show-volcano'); // Assume left plate is overriding for this example
                     }
                     if (effectName === 'rift') effectElement.style.animation = 'openRift 3s ease-in-out forwards';
                     if (effectName === 'transform-crack') effectElement.style.animation = 'slideCrack 3s ease-in-out forwards'; // Need to handle the 'after' pseudo-element animation separately via CSS/class

                     // Add shaking for transform boundary
                      if (selectedType === 'transform') {
                           simulationArea.classList.add('shaking');
                      }
                 }
            });
        }


        // Re-enable button after animation finishes (based on the longest transition duration)
        const longestDuration = 3000; // Matches the CSS transition duration
        setTimeout(() => {
            startButton.disabled = false;
             // Stop shaking effect after a bit, even if plates are still slightly offset
             if (selectedType === 'transform') {
                 simulationArea.classList.remove('shaking');
             }
        }, longestDuration);
    }

    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        if (isHidden) {
            explanationDiv.style.display = 'block';
            explanationButton.textContent = 'הסתר הסבר';
             explanationDiv.style.animation = 'fadeIn 0.6s ease-in-out forwards'; // Re-apply animation
        } else {
            explanationDiv.style.display = 'none';
            explanationButton.textContent = 'הסבר לי מה קורה כאן!';
        }
    }

    startButton.addEventListener('click', startSimulation);
    resetButton.addEventListener('click', resetSimulation);
    explanationButton.addEventListener('click', toggleExplanation);

    // Initial state setup
    resetSimulation();

    // CSS needed for the volcano pseudo-element triggered by JS class
    // Put this inside the <style> block
    /*
     .plate-left.show-volcano::after {
          content: '';
          display: block;
          position: absolute;
          bottom: 50px; // Adjust position
          right: 20px; // Adjust position
          width: 30px;
          height: 40px;
          background: linear-gradient(to top, #b22222, #dc143c);
          clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
          transform-origin: bottom center;
          animation: eruptVolcano 3s ease-in-out forwards;
          z-index: 4;
          filter: drop-shadow(1px 1px 2px rgba(0,0,0,0.5));
     }
    */


</script>