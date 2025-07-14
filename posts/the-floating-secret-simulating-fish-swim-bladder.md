---
title: "סודות הציפה: שליטה בעומק בעזרת שלפוחית השחייה"
english_slug: the-floating-secret-simulating-fish-swim-bladder
category: "ביולוגיה"
tags:
  - ביולוגיה ימית
  - אנטומיה
  - פיזיולוגיה
  - ציפה
  - שלפוחית השחייה
---
# סודות הציפה: שליטה בעומק בעזרת שלפוחית השחייה

איך דגים מצליחים לרחף במים, לצלול למעמקים או לעלות בחזרה אל פני השטח בקלות כזו? גלו את האיבר הפלאי שמאפשר להם לשלוט במשקלם היחסי ולשמור על שיווי משקל מושלם בכל עומק! צללו איתנו להדמיה אינטראקטיבית ותראו במו עיניכם איך זה עובד.

<div class="simulation-container">
    <div class="water">
        <!-- Static bubbles for decoration -->
        <div class="bubble b1"></div>
        <div class="bubble b2"></div>
        <div class="bubble b3"></div>
        <div class="bubble b4"></div>

        <div class="fish-container">
            <div class="fish">
                <div class="body">
                    <div class="eye"></div>
                </div>
                <div class="tail"></div>
                <div class="fin top"></div>
                <div class="fin bottom"></div>
                <div class="swim-bladder"></div>
            </div>
        </div>
        <div class="depth-meter">
            <div class="meter-line"></div>
             <!-- Current depth display -->
            <div class="current-depth-display">0.0 מ'</div>
            <div class="meter-indicator"></div>
            <div class="depth-label top">0 מ'</div>
            <div class="depth-label bottom">10 מ'</div> <!-- Label max depth -->
        </div>
    </div>
    <div class="controls">
        <h3>שלפוחית השחייה</h3>
        <button id="add-gas" class="control-button add-button">מלא גז (+)</button>
        <button id="remove-gas" class="control-button remove-button">רוקן גז (-)</button>
        <div class="bladder-size-display">נפח: <span id="gas-volume">50%</span></div>
    </div>
</div>

<style>
    /* General body styling */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        margin: 0;
        padding: 20px;
        background-color: #f8f8f8;
    }

    h1, h2, h3 {
        color: #34495e;
    }

    p {
        margin-bottom: 1em;
    }

    /* Simulation container styling */
    .simulation-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 20px auto; /* Center the container */
        max-width: 400px; /* Limit max width */
        background-color: #ffffff; /* White background */
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); /* Soft shadow */
        overflow: hidden; /* Ensure nothing spills out */
    }

    /* Water area styling */
    .water {
        position: relative;
        width: 300px; /* Fixed width */
        height: 400px; /* Fixed height */
        background: linear-gradient(to bottom, #aed6f1 0%, #3498db 100%); /* Blue gradient for depth */
        border: 2px solid #2980b9;
        border-radius: 8px;
        overflow: hidden; /* Hide fish outside water */
        margin-bottom: 20px;
        box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.1); /* Inner shadow for water effect */
    }

    /* Fish container for positioning */
    .fish-container {
        position: absolute;
        width: 100%;
        height: 100%;
        /* Use 'top' for main vertical positioning - JS updates this */
        top: 5%; /* Initial position near top */
        display: flex;
        justify-content: center;
        align-items: flex-start; /* Align fish to the logical top of the container */
        transition: top 1.5s cubic-bezier(0.4, 0, 0.2, 1); /* Smoother, more natural movement transition */
    }

    /* Fish base style */
    .fish {
        position: relative;
        width: 80px;
        height: 40px;
        transform: translateX(-50%); /* Center horizontally */
        left: 50%;
        /* Add subtle idle animation */
        animation: subtleFloat 4s ease-in-out infinite alternate;
    }

    /* Fish body */
    .fish .body {
        position: absolute;
        width: 60px;
        height: 40px;
        background-color: #e74c3c; /* Reddish fish body */
        border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
        left: 0;
        top: 0;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    /* Fish eye - pseudo element */
    .fish .body::after {
        content: '';
        position: absolute;
        width: 8px;
        height: 8px;
        background-color: #333;
        border-radius: 50%;
        top: 12px;
        left: 20px;
        border: 2px solid white;
    }


    /* Fish tail */
    .fish .tail {
        position: absolute;
        width: 35px; /* Slightly larger tail */
        height: 40px;
        background-color: #e74c3c;
        clip-path: polygon(0% 0%, 100% 20%, 100% 80%, 0% 100%);
        right: -30px; /* Position further out */
        top: 0;
        transform-origin: 0% 50%; /* Pivot for animation */
        animation: tailWag 1s ease-in-out infinite alternate; /* Tail animation */
    }

    /* Fish fins */
    .fish .fin {
        position: absolute;
        width: 25px; /* Slightly larger fins */
        height: 18px;
        background-color: #f1c40f; /* Yellowish fins */
        clip-path: polygon(0% 0%, 100% 50%, 0% 100%);
        left: 25px; /* Position slightly back */
        transform-origin: 0% 50%; /* Pivot */
        animation: finFlutter 1s ease-in-out infinite alternate; /* Fin animation */
    }

    .fish .fin.top {
         top: -8px; /* Position slightly higher */
         transform: rotate(-20deg); /* Less steep angle */
    }
     .fish .fin.bottom {
         bottom: -8px; /* Position slightly lower */
         transform: rotate(20deg); /* Less steep angle */
    }

    /* Swim bladder styling */
    .swim-bladder {
        position: absolute;
        width: 30px;
        height: 20px;
        background-color: rgba(255, 255, 255, 0.8); /* More opaque white */
        border: 1px solid #bdc3c7;
        border-radius: 12px; /* More rounded */
        left: 15px;
        top: 10px;
        transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1); /* Smooth scale transition */
        transform-origin: center;
        transform: scale(1); /* Default scale (50% volume) */
        box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.1); /* Inner shadow */
    }

     /* Bladder pulse animation */
    .swim-bladder.pulsing {
        animation: pulseBladder 0.5s ease-out;
    }

    /* Depth meter styling */
    .depth-meter {
        position: absolute;
        top: 10px; /* Adjust position */
        right: 15px; /* Adjust position */
        height: calc(100% - 20px); /* Adjust height */
        width: 25px; /* Wider meter */
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .meter-line {
        width: 4px; /* Wider line */
        height: calc(100% - 60px); /* Adjust for labels and display */
        background: linear-gradient(to bottom, #2c3e50 0%, #7f8c8d 100%); /* Gradient line */
        margin-top: 30px; /* Space for top label and display */
        margin-bottom: 30px; /* Space for bottom label */
        position: relative;
        border-radius: 2px;
    }

     /* Current depth display */
     .current-depth-display {
         position: absolute;
         top: -5px; /* Position above meter top label */
         right: 0;
         transform: translateX(110%); /* Position to the right */
         font-size: 1em;
         font-weight: bold;
         color: #34495e;
         min-width: 70px; /* Prevent layout shifts */
         text-align: left;
     }


    .meter-indicator {
        position: absolute;
        width: 20px; /* Wider indicator */
        height: 6px; /* Thicker indicator */
        background-color: #e74c3c; /* Red indicator */
        right: -10px; /* Position aligned with meter line */
        transform: translateY(-50%);
        transition: top 1.5s cubic-bezier(0.4, 0, 0.2, 1); /* Smooth movement, match fish */
        border-radius: 3px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    }

    .depth-label {
        position: absolute;
        right: 25px; /* Position to the right of the meter */
        font-size: 0.9em;
        color: #555;
        white-space: nowrap; /* Prevent text wrapping */
    }

    .depth-label.top {
        top: 25px; /* Align with meter top */
    }

    .depth-label.bottom {
        bottom: 25px; /* Align with meter bottom */
    }

    /* Static bubbles */
    .bubble {
        position: absolute;
        bottom: 10px; /* Start from bottom */
        width: 5px;
        height: 5px;
        background-color: rgba(255, 255, 255, 0.5);
        border-radius: 50%;
        opacity: 0.6;
        animation: bubbleFlow 6s infinite linear; /* Bubble animation */
    }

    .bubble.b1 { left: 10%; animation-delay: 0s; width: 4px; height: 4px; }
    .bubble.b2 { left: 30%; animation-delay: 2s; width: 6px; height: 6px; opacity: 0.8;}
    .bubble.b3 { left: 50%; animation-delay: 1s; }
    .bubble.b4 { left: 70%; animation-delay: 3s; width: 5px; height: 5px; opacity: 0.7; }


    /* Controls styling */
    .controls {
        display: flex;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        justify-content: center; /* Center controls */
        align-items: center;
        gap: 15px; /* Space between items */
        width: 100%; /* Take full width */
        padding: 10px 0;
    }

    .controls h3 {
        margin: 0;
        font-size: 1.1em;
        color: #34495e;
    }

    .controls .control-button {
        padding: 10px 15px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        font-weight: bold;
    }

    .controls .add-button {
        background-color: #2ecc71; /* Green */
        color: white;
    }

    .controls .add-button:hover {
        background-color: #27ae60;
    }

    .controls .remove-button {
        background-color: #e74c3c; /* Red */
        color: white;
    }

     .controls .remove-button:hover {
        background-color: #c0392b;
    }

    .controls .control-button:active {
        transform: scale(0.95); /* Press effect */
    }


    .bladder-size-display {
        font-weight: bold;
        color: #34495e;
        min-width: 90px; /* Ensure consistent width */
        text-align: center;
        font-size: 1.1em;
    }

    /* Explanation toggle button */
    #toggle-explanation {
        display: block;
        margin: 25px auto; /* Center button */
        padding: 12px 20px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #3498db; /* Blue button */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        font-weight: bold;
    }

    #toggle-explanation:hover {
        background-color: #2980b9;
    }

    #toggle-explanation:active {
         transform: scale(0.98); /* Press effect */
    }

    /* Explanation section styling */
    #explanation {
        border-top: 1px solid #ddd; /* Lighter border */
        padding-top: 25px;
        margin-top: 25px;
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    }

    #explanation h2 {
        color: #2c3e50; /* Darker blue-grey */
        margin-bottom: 20px;
        text-align: center;
    }

     #explanation h3 {
        color: #34495e;
        margin-top: 20px;
        margin-bottom: 10px;
        font-size: 1.2em;
        border-bottom: 1px solid #eee; /* Subtle underline */
        padding-bottom: 5px;
    }

     #explanation p {
        line-height: 1.7; /* Increased line height */
        color: #555;
        margin-bottom: 15px;
     }

     #explanation ul {
         margin-bottom: 15px;
         padding-left: 20px; /* Indent list */
     }

     #explanation li {
        margin-bottom: 8px; /* Space list items */
        line-height: 1.6;
     }

     /* Animation Keyframes */
     @keyframes subtleFloat {
         0%, 100% { transform: translateX(-50%) translateY(0); }
         50% { transform: translateX(-50%) translateY(-3px); } /* Subtle vertical movement */
     }

     @keyframes tailWag {
         0%, 100% { transform: rotateY(0deg) rotate(0deg); }
         50% { transform: rotateY(0deg) rotate(10deg); } /* Wag angle */
     }

     @keyframes finFlutter {
        0%, 100% { transform: rotate(20deg); } /* Keep base angle */
        50% { transform: rotate(30deg); } /* Flutter slightly up */
     }
     .fish .fin.top {
         animation: finFlutterTop 0.8s ease-in-out infinite alternate;
     }
     .fish .fin.bottom {
         animation: finFlutterBottom 0.8s ease-in-out infinite alternate;
     }
      @keyframes finFlutterTop {
        0%, 100% { transform: rotate(-20deg); }
        50% { transform: rotate(-30deg); }
     }
      @keyframes finFlutterBottom {
        0%, 100% { transform: rotate(20deg); }
        50% { transform: rotate(30deg); }
     }

    @keyframes pulseBladder {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); } /* Pulse effect */
        100% { transform: scale(1); }
    }

    @keyframes bubbleFlow {
        0% { transform: translateY(0) translateX(0); opacity: 0.6; }
        100% { transform: translateY(-400px) translateX(10px); opacity: 0; } /* Move up and slightly sideways */
    }


    /* Hide explanation by default */
    .hidden {
        display: none;
    }

</style>

<button id="toggle-explanation">הצג הסבר מורחב</button>

<div id="explanation" class="hidden">
    <h2>הסבר מורחב: הצלילה לעומק מנגנון הציפה</h2>

    <h3>למה דגים צריכים לשלוט בעומק?</h3>
    <p>עבור דגים, היכולת לשלוט במדויק בעומק השהייה במים היא סופר קריטית להישרדות יומיומית! תחשבו על זה:
    <ul>
        <li>**מסיבת ארוחת צהריים:** כל עומק מציע תפריט שונה של מזון וגם מארח טורפים אחרים.</li>
        <li>**בריחה דרמטית:** עלייה או ירידה מהירה יכולה להיות ההבדל בין חיים ל... טוב, אתם מבינים.</li>
        <li>**חיסכון באנרגיה:** לדמיין לשחות כל הזמן רק כדי לא לשקוע? שלפוחית השחייה חוסכת לדג המון אנרגיה!</li>
        <li>**איזור נוחות אישי:** טמפרטורה, מליחות, חמצן ואור - כל אלה משתנים עם העומק. הדג יכול למצוא את התנאים הכי מתאימים לו.</li>
    </ul>
    </p>

    <h3>אז מה זו השלפוחית הזאת?</h3>
    <p>שלפוחית השחייה (Swim Bladder), או כמו שחלק קוראים לה, שלפוחית הגז, היא בעצם שקית דקיקה ומלאת גז שנמצאת בחלל הבטן של רוב הדגים הגרמיים. זהו כמו בלון פנימי שהדג יכול לנפח או לרוקן, ובכך לשחק עם כוח הציפה שפועל עליו.</p>

    <h3>הקסם הפיזיקלי: ארכימדס ושיווי משקל</h3>
    <p>זוכרים את ארכימדס שקפץ מהאמבטיה וצעק "אאוריקה!"? הוא גילה שגוף השקוע בנוזל חווה כוח ציפה ששווה למשקל הנוזל שהגוף דוחק. דג שוקע אם כוח הציפה עליו קטן ממשקלו, צף אם הוא גדול, ונשאר באותו עומק אם שניהם שווים – זהו שיווי משקל ציפה. הדג עצמו (בשר, עצמות) צפוף יותר ממים, ולכן נוטה לשקוע. אבל הגז שבשלפוחית? הוא קליל! כשהדג מגדיל את נפח השלפוחית, הוא מגדיל את הנפח הכולל של גופו, דוחק יותר מים, וכוח הציפה גדל. כך הדג יכול לשנות את הצפיפות הממוצעת של עצמו ולהתאים אותה לצפיפות המים בעומק הרצוי. כשהצפיפות הממוצעת שלו שווה לצפיפות המים, הוא מרחף במקום כמו אסטרונאוט בחלל (בערך).</p>

    <h3>איך הדג מנפח ומרוקן את הבלון הפנימי?</h3>
    <p>הדגים משתמשים במנגנונים ביולוגיים מדהימים כדי לשלוט בגז בשלפוחית:
    <ul>
        <li>**מנגנון מילוי קסום (Rete Mirabile & Gas Gland):** זה כמו מערכת סופר מורכבת של כלי דם בלוטת מיוחדת שיכולה "למשוך" גז מהדם ולדחוס אותו לתוך השלפוחית, אפילו בלחצים אדירים בעומק רב. זה תהליך יחסית איטי, שמתאים לדגים שמשנים עומק בהדרגה.</li>
        <li>**חלון יציאה מהיר (Oval Window):** איזור עם דופן דקה במיוחד ואספקת דם עשירה בשלפוחית, אותו הדג יכול לפתוח. פתיחת החלון מאפשרת לגז לחזור מהשלפוחית אל הדם במהירות יחסית, מה שמאפשר ירידה מהירה יותר בעמודת המים.</li>
    </ul>
    </p>

    <h3>לא כולם צריכים בלון: חלופות אבולוציוניות</h3>
    <p>לא כל דג קיבל שלפוחית במתנה. לדגי סחוס כמו כרישים ובטאים, למשל, אין אותה. הם פיתחו אסטרטגיות אחרות:
    <ul>
        <li>**כבד שומני ענק:** לכרישים רבים יש כבד גדול מאוד ועשיר בשומן (שהוא פחות צפוף ממים), המספק ציפה חלקית.</li>
        <li>**צורה הידרודינמית וסנפירים:** צורת גופם ובעיקר סנפירי החזה שלהם פועלים כמו כנפי מטוס קטנות, ויוצרים כוח עילוי כשהם שוחים קדימה. לכן הם צריכים לשחות כל הזמן כדי לא לשקוע!</li>
    </ul>
    </p>

    <h3>ועוד חברים שצפים...</h3>
    <p>גם יצורים ימיים אחרים משתמשים בטכניקות מגניבות כדי לשלוט בציפה:
    <ul>
        <li>**יונקים ימיים (לווייתנים, דולפינים):** משנים את נפח האוויר בריאותיהם ונהנים מכמות שומן גדולה בגופם.</li>
        <li>**צבי ים:** שולטים באוויר בריאות ומסתמכים על שומן גוף.</li>
        <li>**דיונונים ותמנונים מסוימים:** משתמשים בשינוי הרכב הנוזלים בגופם או בוויסות גז בחללים פנימיים.</li>
    </ul>
    </p>
</div>

<script>
    const fishContainer = document.querySelector('.fish-container');
    const fishElement = document.querySelector('.fish'); // Get the fish element itself
    const swimBladder = document.querySelector('.swim-bladder');
    const addGasButton = document.getElementById('add-gas');
    const removeGasButton = document.getElementById('remove-gas');
    const gasVolumeDisplay = document.getElementById('gas-volume');
    const meterIndicator = document.querySelector('.meter-indicator');
    const waterElement = document.querySelector('.water');
    const currentDepthDisplay = document.querySelector('.current-depth-display'); // New element
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    let gasVolume = 50; // Initial volume in percent (0 to 100)
    const volumeStep = 10; // Percentage change per click

    // Define the depth range corresponding to the visual fish position range
    const minFishTop = 5; // % from top of water container
    const maxFishTop = 80; // % from top of water container
    const minDepth = 0; // meters
    const maxDepth = 10; // meters

    function updateSimulation() {
        // Update bladder size visual (scale)
        // Map volume 0-100 to scale 0.8-1.5 (example range for visual effect)
        const bladderScale = 0.8 + (gasVolume / 100) * 0.7; // Scale ranges from 0.8 to 1.5
        swimBladder.style.transform = `scale(${bladderScale})`;

        // Update fish position (depth) based on gas volume
        // Higher gasVolume = lower depth = lower 'top' percentage
        // Use linear mapping between gasVolume and fishTop position
        const fishTopPercentage = maxFishTop - (gasVolume / 100) * (maxFishTop - minFishTop);
        fishContainer.style.top = `${fishTopPercentage}%`; // Update fish container top position

        // Update depth meter indicator position to match fish
        // The indicator position should be the same as the fish's top percentage
        meterIndicator.style.top = `${fishTopPercentage}%`; // Update indicator top position

        // Update current depth display
        // Map fishTopPercentage (which reflects depth) back to depth value
        const currentDepth = minDepth + (fishTopPercentage - minFishTop) / (maxFishTop - minFishTop) * (maxDepth - minDepth);
        currentDepthDisplay.textContent = `${currentDepth.toFixed(1)} מ'`; // Display with one decimal place

        // Update gas volume text display
        gasVolumeDisplay.textContent = `${gasVolume}%`;
    }

    // Function to trigger bladder pulse animation
    function pulseBladder() {
        swimBladder.classList.add('pulsing');
        // Remove the class after the animation duration
        setTimeout(() => {
            swimBladder.classList.remove('pulsing');
        }, 500); // Match animation duration
    }


    // Event listeners for buttons
    addGasButton.addEventListener('click', () => {
        if (gasVolume < 100) {
            gasVolume = Math.min(100, gasVolume + volumeStep); // Ensure it doesn't go over 100
            updateSimulation();
            pulseBladder(); // Trigger pulse animation
        }
    });

    removeGasButton.addEventListener('click', () => {
        if (gasVolume > 0) {
            gasVolume = Math.max(0, gasVolume - volumeStep); // Ensure it doesn't go below 0
            updateSimulation();
             pulseBladder(); // Trigger pulse animation
        }
    });

     // Event listener for explanation toggle button
    toggleExplanationButton.addEventListener('click', () => {
        // Toggle the 'hidden' class on the explanation div
        explanationDiv.classList.toggle('hidden');
        // Update button text based on the new state
        const isNowHidden = explanationDiv.classList.contains('hidden');
        toggleExplanationButton.textContent = isNowHidden ? 'הצג הסבר מורחב' : 'הסתר הסבר מורחב';
    });


    // Initial simulation state
    updateSimulation();

</script>