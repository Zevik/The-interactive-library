---
title: "סימולציה אינטראקטיבית: אפקט העומד מן הצד (פיזור אחריות)"
english_slug: bystander-effect-simulation
category: "פסיכולוגיה"
tags:
  - אפקט העומד מן הצד
  - פיזור אחריות
  - ניסויים קלאסיים
  - פסיכולוגיה
  - אינטראקטיבי
  - סימולציה
---

# האם היית עוזר? גלו בסימולציה אינטראקטיבית!

דמיינו את זה: מישהו במצוקה זקוק לעזרה דחופה. האם תרוצו לסייע? התשובה אולי תלויה בדבר מפתיע... כמה אנשים נוספים נמצאים לידכם. בואו נצלול לתוך תופעה מרתקת בפסיכולוגיה חברתית ונגלה מדוע קבוצה גדולה עלולה לעיתים להוביל לפחות עזרה, דווקא כשהיא נחוצה ביותר.

<div class="simulation-container">
    <h2>מצב חירום מדומה</h2>
    <p class="subtitle">קבעו כמה אנשים נמצאים בסביבה (ה"עומדים מן הצד") וראו איך הסיכוי לקבלת עזרה משתנה.</p>

    <div class="controls">
        <label for="bystander-count">מספר ה"עומדים מן הצד":</label>
        <input type="number" id="bystander-count" value="5" min="1" max="25">
        <button id="run-simulation">הפעל סימולציה</button>
    </div>

    <div class="scenario">
        <div class="person-in-need" id="person-in-need">
            <span class="icon">⚠️</span><span class="text">זקוק לעזרה!</span>
        </div>
        <div class="bystanders" id="bystanders-area">
            <!-- Bystander circles will be added here by JS -->
        </div>
         <div class="ground"></div> <!-- Visual ground -->
    </div>

    <div class="results" id="simulation-results">
        <!-- Simulation results will be displayed here -->
    </div>
</div>

<button id="toggle-explanation" class="explanation-button">מה קרה כאן? לחצו להסבר</button>

<div id="explanation" class="hidden">
    <h2>אפקט העומד מן הצד (Bystander Effect) ופיזור אחריות (Diffusion of Responsibility)</h2>
    <p>הסימולציה שחוויתם ממחישה באופן פשטני את אחד הממצאים החזקים והמדאיגים בפסיכולוגיה חברתית: אפקט העומד מן הצד. תופעה זו מתארת מצב בו הסיכוי שאדם יסייע לקורבן במצוקה קטן ככל שמספר האנשים הנוכחים באירוע גדל. Paradoxal, אך אמיתי.</p>
    <p>הסיבה המרכזית לכך היא **פיזור אחריות (Diffusion of Responsibility)**. כאשר ישנם עומדים מן הצד רבים, האחריות האישית להגיב למצב החירום "מתפזרת" בין כל הנוכחים. במקום שאדם יחיד ירגיש 100% מהאחריות, בקבוצה של עשרה אנשים, כל אחד עשוי להרגיש רק 10% מהאחריות, מה שמוריד משמעותית את הלחץ הפסיכולוגי לפעולה מיידית.</p>
    <p>סיבות נוספות התורמות לאפקט:</p>
    <ul>
        <li>**עמימות ואי-ודאות:** לעיתים מצבי חירום אינם ברורים לחלוטין. אנשים נוטים להסתכל על תגובותיהם של אחרים כדי להבין את המצב. אם כולם נראים רגועים או לא בטוחים כיצד להגיב, זה עלול להוביל למסקנה שגויה שהמצב אינו חמור כפי שהוא נראה (זוהי תופעה בפני עצמה הנקראת **בורות פלורליסטית - Pluralistic Ignorance**).</li>
        <li>**פחד משיפוט:** אנשים חוששים להיראות מגוחכים, לטעות או להגיב בצורה לא הולמת לעיני אחרים. פחד זה יכול לשתק ולמנוע נקיטת פעולה.</li>
        <li>**עלות לעומת תועלת:** אנשים עשויים לשקול (גם אם באופן לא מודע) את העלות הכרוכה בעזרה (סכנה אישית, מבוכה, מאמץ) לעומת התועלת. כשיש אחרים, יש ציפייה ש"מישהו אחר" יישא בעלות זו.</li>
    </ul>
    <p>בסימולציה, כל "עומד מן הצד" (העיגולים הצבעוניים) מקבל "הזדמנות" להגיב, אך הסבירות שהוא ירגיש אחריות מספקת לעשות זאת פוחתת ככל שמספר העומדים גדל. האנימציה מראה כיצד אחד מהם (אם בכלל) עשוי "להחליט" לגשת ולסייע לאדם במצוקה (האייקון המהבהב).</p>
    <h3>כיצד ניתן להתגבר על אפקט העומד מן הצד?</h3>
    <p>המודעות לאפקט היא הצעד הראשון. במצבי חירום, נסו:</p>
    <ul>
        <li>**להיות ישירים:** פנו לאדם ספציפי בקבוצה ובקשו עזרה ("אתה בחולצה האדומה, התקשר למד"א!"). זה מנטרל את פיזור האחריות.</li>
        <li>**להיות ברורים:** הגדירו את המצב כחירום ("אני זקוק לעזרה! הוא לא נושם!"). זה מנטרל את העמימות והבורות הפלורליסטית.</li>
        <li>**לפעול בעצמכם:** אם בטוח לעשות זאת, פעולה ראשונית מצדכם יכולה לעורר אחרים להצטרף.</li>
    </ul>
    <p>זכרו, כל אחד מאיתנו יכול להיות "העומד מן הצד" או "האדם במצוקה". הבנת האפקט היא מפתח ליצירת חברה אכפתית יותר.</p>
</div>

<style>
    body {
        font-family: 'Heebo', sans-serif; /* Changed font */
        line-height: 1.7;
        margin: 0; /* Remove default margin */
        padding: 20px;
        background: linear-gradient(to bottom, #e0f7fa, #ffffff); /* Subtle gradient background */
        color: #333;
        direction: rtl;
        text-align: right;
        overflow-x: hidden; /* Prevent horizontal scroll */
    }

    h1, h2 {
        color: #0056b3;
        text-align: center;
        margin-bottom: 10px;
    }

    h1 {
        color: #003f82; /* Darker blue for main title */
        margin-top: 0;
        padding-top: 10px;
        font-size: 2em;
    }

    .simulation-container {
        background-color: #fff;
        padding: 30px;
        margin: 20px auto;
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 6px 20px rgba(0,0,0,0.1); /* Deeper shadow */
        max-width: 750px; /* Slightly wider */
        text-align: right;
        border-top: 6px solid #007bff; /* Accent border */
        position: relative; /* Needed for absolute positioning inside */
        overflow: hidden; /* Hide overflow from animations */
    }

    .subtitle {
        text-align: center;
        color: #555;
        margin-top: -5px;
        margin-bottom: 20px;
        font-size: 1.1em;
    }

    .controls {
        margin-bottom: 30px; /* More space below controls */
        text-align: center;
        display: flex; /* Use flexbox for controls */
        justify-content: center; /* Center align items */
        align-items: center;
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .controls label {
        margin-left: 15px; /* Adjusted margin for RTL */
        font-weight: bold;
        font-size: 1.1em;
        color: #0056b3;
    }

    .controls input[type="number"] {
        padding: 10px; /* Increased padding */
        border: 1px solid #ccc;
        border-radius: 5px; /* Slightly more rounded */
        width: 70px; /* Wider input */
        text-align: center;
        font-size: 1em;
        -moz-appearance: textfield; /* Hide default arrows in Firefox */
    }

    .controls input[type="number"]::-webkit-outer-spin-button,
    .controls input[type="number"]::-webkit-inner-spin-button {
        -webkit-appearance: none; /* Hide default arrows in Chrome/Safari */
        margin: 0;
    }

    #run-simulation {
        padding: 12px 25px; /* Larger button */
        background-color: #28a745;
        color: white;
        border: none;
        border-radius: 6px; /* More rounded */
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease; /* Add transform transition */
        margin-right: 15px; /* Adjusted margin for RTL */
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    #run-simulation:hover {
        background-color: #218838;
        box-shadow: 0 3px 7px rgba(0,0,0,0.3);
    }
     #run-simulation:active {
        transform: scale(0.98); /* Add active state press effect */
    }


    .scenario {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end; /* Align to bottom */
        margin-bottom: 20px;
        position: relative;
        min-height: 300px; /* Taller scenario area */
        border: 2px dashed #a0d8f0; /* More prominent border */
        background-color: #eefaff; /* Lighter background */
        border-radius: 8px;
        overflow: hidden; /* Crucial for containing absolute children */
    }

    .ground {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 50px; /* Represents ground */
        background-color: #d4edda; /* Greenish ground color */
        z-index: 0; /* Below other elements */
    }


    .person-in-need {
        width: 100px; /* Larger */
        height: 100px; /* Larger */
        background-color: #dc3545; /* Red */
        color: white;
        border-radius: 50%;
        display: flex;
        flex-direction: column; /* Stack icon and text */
        justify-content: center;
        align-items: center;
        font-weight: bold;
        text-align: center;
        position: absolute;
        bottom: 40px; /* Position above the ground */
        left: 50%;
        transform: translateX(-50%); /* Center horizontally */
        z-index: 2; /* Above bystanders initially */
        box-shadow: 0 0 15px rgba(220, 53, 69, 0.7); /* Stronger glow */
        animation: pulse-danger 1.5s infinite alternate ease-in-out; /* Pulsing animation */
        font-size: 0.9em; /* Smaller text */
        padding: 5px;
    }

    .person-in-need .icon {
        font-size: 2em; /* Larger icon */
        margin-bottom: 5px; /* Space between icon and text */
    }
     .person-in-need .text {
        font-size: 0.8em;
     }


    @keyframes pulse-danger {
        from { transform: translateX(-50%) scale(1); opacity: 1; }
        to { transform: translateX(-50%) scale(1.05); opacity: 0.9; }
    }

    .bystanders {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: 1; /* Below person-in-need */
    }

    .bystander {
        width: 40px; /* Larger bystanders */
        height: 40px;
        background-color: #007bff; /* Blue */
        color: white;
        border-radius: 50%;
        position: absolute;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 0.8em;
        opacity: 0;
        transition: opacity 0.5s ease-out; /* Fade in */
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        cursor: pointer; /* Hint of interactivity */
    }

    .bystander.visible {
        opacity: 1; /* Make visible */
    }

    .bystander.thinking {
         background-color: #ffc107; /* Yellowish - considering */
         animation: pulse-thinking 1s infinite alternate ease-in-out; /* Subtle pulse */
    }

    @keyframes pulse-thinking {
         from { transform: scale(1); }
         to { transform: scale(1.05); }
    }

    .bystander.not-helping {
        background-color: #6c757d; /* Gray - decided not to */
        opacity: 0.7; /* Slightly fade out */
        transition: background-color 0.3s ease, opacity 0.5s ease;
        animation: none; /* Stop thinking pulse */
    }

    .bystander.helping {
        background-color: #28a745; /* Green - decided to help */
        z-index: 3; /* Bring to front */
        transition: transform 1.5s ease-in-out, background-color 0.5s ease, opacity 0.5s ease; /* Smooth move animation */
        animation: none; /* Stop thinking pulse */
    }


    .results {
        margin-top: 25px; /* More space above results */
        padding: 18px; /* More padding */
        border-radius: 8px; /* More rounded */
        text-align: center;
        min-height: 40px; /* Ensure space */
        font-weight: bold;
        font-size: 1.2em;
        transition: all 0.5s ease; /* Smooth transition for color/background */
    }

    .results.help {
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
        box-shadow: 0 2px 5px rgba(212, 237, 218, 0.5);
    }

    .results.no-help {
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
        box-shadow: 0 2px 5px rgba(248, 215, 218, 0.5);
    }

     .results.initial {
         background-color: #e9ecef;
         color: #495057;
         border: 1px solid #dee2e6;
         box-shadow: none;
     }


    .explanation-button {
        display: block;
        width: fit-content;
        margin: 30px auto; /* More margin */
        padding: 12px 25px; /* Larger button */
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 6px; /* More rounded */
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    .explanation-button:hover {
        background-color: #0056b3;
         box-shadow: 0 3px 7px rgba(0,0,0,0.3);
    }
     .explanation-button:active {
        transform: scale(0.98);
     }


    #explanation {
        background-color: #e9f7fe;
        padding: 30px; /* More padding */
        margin: 20px auto;
        border-radius: 12px; /* More rounded */
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        max-width: 750px; /* Match simulation width */
        text-align: right;
        border-right: 6px solid #007bff; /* Accent border */
        transition: all 0.5s ease-in-out; /* Smooth toggle */
        opacity: 1;
        visibility: visible;
        height: auto; /* Allow height based on content */
    }

    #explanation.hidden {
        opacity: 0;
        visibility: hidden;
        height: 0;
        padding-top: 0;
        padding-bottom: 0;
        margin-top: 0;
        margin-bottom: 0;
        border: none; /* Hide border when hidden */
    }

    #explanation h2 {
        color: #0056b3;
        margin-top: 0;
        margin-bottom: 15px;
    }

    #explanation p {
        margin-bottom: 15px;
        color: #555;
    }

     #explanation h3 {
         margin-top: 20px;
         margin-bottom: 10px;
         color: #0056b3;
         font-size: 1.3em;
     }


    #explanation ul {
        padding-right: 25px; /* More padding */
        margin-bottom: 15px;
    }

    #explanation li {
        margin-bottom: 10px;
        list-style-type: disc; /* Explicit bullet points */
        color: #555;
    }

     /* Add a subtle animation for bystanders appearing */
    @keyframes fadeAndScaleIn {
        from { opacity: 0; transform: scale(0.8); }
        to { opacity: 1; transform: scale(1); }
    }


</style>

<script>
    const bystanderCountInput = document.getElementById('bystander-count');
    const runSimulationButton = document.getElementById('run-simulation');
    const bystandersArea = document.getElementById('bystanders-area');
    const simulationResults = document.getElementById('simulation-results');
    const personInNeed = document.getElementById('person-in-need');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const scenarioArea = document.querySelector('.scenario');


     // Function to scatter bystanders within the scenario area, avoiding the center person
    function positionBystanders(count) {
        // Clear previous bystanders and remove old event listeners
        const oldBystanders = bystandersArea.querySelectorAll('.bystander');
        oldBystanders.forEach(b => {
            // Remove transitionend listener if it exists
            const oldListener = b.dataset.transitionListener;
            if (oldListener) {
                b.removeEventListener('transitionend', oldListener);
            }
             b.remove(); // Remove element
        });


        const areaRect = scenarioArea.getBoundingClientRect(); // Use scenario area for positioning
        const personRect = personInNeed.getBoundingClientRect();

        // Calculate center of the scenario area (approx)
        const areaCenterX = areaRect.width / 2;
        const areaCenterY = areaRect.height / 2;

         // Define a "safe zone" around the person in need
         const safeZoneRadius = Math.max(personRect.width, personRect.height) * 1.2; // Make zone larger than person

        for (let i = 0; i < count; i++) {
            const bystander = document.createElement('div');
            bystander.classList.add('bystander');
            bystander.textContent = i + 1; // Add number for identification

            let randomX, randomY;
            let attempts = 0;
            const maxAttempts = 100;

            // Generate random positions, ensuring they are outside the "safe zone" around the person
            do {
                randomX = Math.random() * (areaRect.width - 40); // 40 is bystander size
                randomY = Math.random() * (areaRect.height - 40 - 50); // 40 size, 50 ground height
                 // Adjust Y to be above the ground
                 randomY = Math.max(randomY, 10); // Don't place too high
                 randomY = Math.min(randomY, areaRect.height - 40 - 60); // Don't place too low, give space above ground

                // Calculate distance from the center of the person
                const distFromPersonCenterX = randomX + 20 - areaCenterX; // 20 is half bystander size
                const distFromPersonCenterY = randomY + 20 - (areaCenterY + (personRect.height/2) - (areaRect.height/2) ); // 20 half size, adjust person center relative to area center

                const distance = Math.sqrt(distFromPersonCenterX * distFromPersonCenterX + distFromPersonCenterY * distFromPersonCenterY);

                attempts++;
                if (attempts > maxAttempts) {
                    console.warn("Could not find clear spot for bystander, placing near edge.");
                    // Fallback: place near the edge if too many attempts
                    randomX = Math.random() * (areaRect.width - 40);
                    randomY = 10; // Place near top
                    break;
                }

            } while (distance < safeZoneRadius); // Ensure distance is outside the safe zone


            bystander.style.left = `${randomX}px`;
            bystander.style.top = `${randomY}px`;

            bystandersArea.appendChild(bystander);

            // Trigger appear animation with slight delay
            setTimeout(() => {
                bystander.classList.add('visible');
                 bystander.style.animation = 'fadeAndScaleIn 0.5s ease-out forwards'; // Apply the animation
            }, i * 50); // Stagger appearance
        }
         simulationResults.classList.add('initial');
         simulationResults.textContent = 'לחצו "הפעל סימולציה" כדי לראות מה קורה...';
    }

    // Main simulation logic
    function runSimulation(bystanderCount) {
        simulationResults.classList.remove('help', 'no-help', 'initial');
        simulationResults.textContent = 'עומדים מן הצד חושבים...';

        const bystanders = document.querySelectorAll('.bystander');
        let someoneHelped = false;
        const baseProbabilityPerIndividualIfAlone = 0.7; // High chance if 1 person
        const diffusionFactor = 0.6; // How much responsibility is diluted by each additional person (simplified)
        // A rough model: perceived individual chance = base / (N * diffusionFactor + 1) - Need N in denominator
        // Let's use the simpler 1/N concept but add visual steps.
        // Base chance *for the *group* to fail* increases with N.
        // Or, base chance *for an individual* to step up decreases with N.
        // Probability a *specific* person steps up = BaseChanceAlone / (N + SomeConstant)
        const someConstant = 2; // Additive constant helps avoid division by zero/very large chance for N=1
        const chanceToActPerPerson = baseProbabilityPerIndividualIfAlone / (bystanderCount + someConstant);


        // Add 'thinking' state and stagger the 'decision'
        bystanders.forEach((bystander, index) => {
             bystander.classList.remove('not-helping', 'helping', 'thinking'); // Reset states
             bystander.style.transition = 'none'; // Remove transitions before adding state
             bystander.style.transform = 'none'; // Reset transform

            setTimeout(() => {
                bystander.classList.add('thinking'); // Start thinking animation
            }, index * 150 + 300); // Stagger the thinking state

            // Simulate decision after thinking
            setTimeout(() => {
                 bystander.classList.remove('thinking'); // Stop thinking animation

                if (!someoneHelped) { // Only proceed if no one else has helped yet
                    const randomValue = Math.random(); // Random number between 0 and 1

                    if (randomValue < chanceToActPerPerson) {
                        someoneHelped = true; // Mark that someone is helping
                        bystander.classList.add('helping');
                        simulationResults.textContent = 'מישהו החליט לעזור!';
                        simulationResults.classList.add('help');

                        // Animate the helping bystander moving towards the person in need
                        const personRect = personInNeed.getBoundingClientRect();
                        const bystanderRect = bystander.getBoundingClientRect();
                        const areaRect = bystandersArea.getBoundingClientRect();

                        // Calculate target position relative to the bystander's initial position
                         // Target is the center of the person in need, relative to the bystander's parent (.bystanders area)
                        const targetX = (personRect.left + personRect.width / 2) - (bystanderRect.left + bystanderRect.width / 2) + bystander.offsetLeft;
                        const targetY = (personRect.top + personRect.height / 2) - (bystanderRect.top + bystanderRect.height / 2) + bystander.offsetTop;

                        bystander.style.transition = 'transform 1.5s ease-in-out, background-color 0.5s ease, opacity 0.5s ease';
                        bystander.style.transform = `translate(${targetX}px, ${targetY}px)`;

                        // Add a listener to re-position after animation IF this was the helping bystander
                         const listener = () => {
                             // Wait a bit then reset positions for next run
                             setTimeout(() => {
                                 resetSimulationState(bystanderCount);
                             }, 1500); // Show final state briefly
                         };
                         bystander.addEventListener('transitionend', listener, { once: true });
                         // Store listener so we can remove it later if needed (though 'once' makes it less critical)
                         bystander.dataset.transitionListener = listener;


                    } else {
                         // This bystander decided not to help in this specific run
                         bystander.classList.add('not-helping');
                    }
                } else {
                     // Someone else already decided to help, this person also doesn't act
                     bystander.classList.add('not-helping');
                }

            }, index * 150 + 1000); // Stagger the decision moment, after thinking starts
        });

        // Check if no one helped *after* all individual decision timeouts have potentially finished
        // The total delay needs to be longer than the last decision timeout and the animation
        const finalCheckDelay = bystanderCount * 150 + 1000 + 1600; // Last decision + a bit more than animation duration

        setTimeout(() => {
            // Only update results if someoneHelped is still false (meaning no one was triggered to help)
            if (!someoneHelped) {
                simulationResults.textContent = 'אף אחד לא עזר.';
                simulationResults.classList.add('no-help');
                 // Reset state here as no specific bystander animation triggers the reset
                 setTimeout(() => {
                    resetSimulationState(bystanderCount);
                }, 1500); // Show final state briefly
            }
             // If someoneHelped is true, the helping bystander's transitionend listener will handle the reset
        }, finalCheckDelay);
    }

    function resetSimulationState(bystanderCount) {
        const bystanders = document.querySelectorAll('.bystander');
        bystanders.forEach(bystander => {
             bystander.classList.remove('helping', 'not-helping', 'thinking', 'visible');
             bystander.style.transition = 'none'; // Disable transition for reset
             bystander.style.transform = 'none'; // Reset transform
             // Remove listener if it wasn't removed by 'once'
             const oldListener = bystander.dataset.transitionListener;
            if (oldListener) {
                bystander.removeEventListener('transitionend', oldListener);
                delete bystander.dataset.transitionListener;
            }
        });
        positionBystanders(bystanderCount); // Re-position bystanders for the next run
    }


    // Initial setup
    document.addEventListener('DOMContentLoaded', () => {
        const initialCount = parseInt(bystanderCountInput.value);
         if (!isNaN(initialCount) && initialCount >= 1 && initialCount <= 25) {
            positionBystanders(initialCount);
         } else {
             positionBystanders(5); // Default if value is invalid
         }
    });

    // Event listener for running the simulation
    runSimulationButton.addEventListener('click', () => {
        const count = parseInt(bystanderCountInput.value);
        if (isNaN(count) || count < 1 || count > 25) {
            alert('אנא הכנס מספר עומדים מן הצד בין 1 ל-25.');
            return;
        }
         runSimulationButton.disabled = true; // Disable button during simulation
         simulationResults.textContent = 'מריץ סימולציה...';
         simulationResults.classList.remove('help', 'no-help', 'initial');
         simulationResults.classList.add('initial'); // Indicate process started

        // Clear existing bystanders with fade out animation
        const bystanders = bystandersArea.querySelectorAll('.bystander');
         let removedCount = 0;
         if(bystanders.length > 0) {
             bystanders.forEach((b, index) => {
                 b.style.transition = 'opacity 0.5s ease-out';
                 b.style.opacity = 0;
                 // Wait for fade out to finish before removing
                 setTimeout(() => {
                     b.remove();
                     removedCount++;
                     if(removedCount === bystanders.length) {
                         // Once all removed, position new ones and run sim
                         positionBystanders(count);
                         setTimeout(() => {
                             runSimulation(count);
                             runSimulationButton.disabled = false; // Re-enable button after sim ends (handled within runSimulation logic)
                         }, count * 50 + 600); // Delay for new bystanders to appear + buffer
                     }
                 }, index * 30 + 500); // Stagger fade out slightly
             });
         } else {
              // If no bystanders initially (e.g., first run), just position and run
              positionBystanders(count);
                setTimeout(() => {
                    runSimulation(count);
                    runSimulationButton.disabled = false; // Re-enable button
                }, count * 50 + 600); // Delay for new bystanders to appear + buffer
         }
    });


    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.classList.contains('hidden');
        if (isHidden) {
            explanationDiv.classList.remove('hidden');
            toggleExplanationButton.textContent = 'הסתר הסבר';
            // Optional: scroll to explanation
            explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        } else {
            explanationDiv.classList.add('hidden');
            toggleExplanationButton.textContent = 'מה קרה כאן? לחצו להסבר';
        }
    });

    // Re-enable button logic is now mostly handled within runSimulation/resetSimulationState
     // Fallback to re-enable button if simulation gets stuck (unlikely with current structure but good practice)
     const simulationTimeout = (count) => count * 150 + 1000 + 1600 + 2000; // Max possible sim time + buffer
     runSimulationButton.addEventListener('click', () => {
         runSimulationButton.disabled = true;
         const count = parseInt(bystanderCountInput.value);
         setTimeout(() => {
             runSimulationButton.disabled = false;
         }, simulationTimeout(count)); // Set a maximum timeout to re-enable button
     });


</script>