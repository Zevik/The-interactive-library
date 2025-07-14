---
title: "סרוטונין, סינפסות ו-SSRI: הצצה מרתקת אל המוח"
english_slug: how-antidepressants-work-a-look-inside-the-brain
category: "מדעי החיים / מדעי המוח"
tags:
  - SSRI
  - דיכאון
  - סינפסה
  - סרוטונין
  - פרמקולוגיה
---

# סרוטונין, סינפסות ו-SSRI: הצצה מרתקת אל המוח

האם שאלתם את עצמכם פעם מדוע מצב הרוח שלנו משתנה? ואיך תרופות כמו פרוזאק או ציפרלקס משפיעות עליו? הצטרפו למסע ויזואלי עוצר נשימה אל עומק המוח, למרחב הזעיר שבין תאי העצב, שם מתרחש הריקוד המולקולרי המשפיע על רגשותינו.

<div id="simulation-container">
    <div class="environment"></div>
    <div class="neuron pre-synaptic">
        <div class="neuron-label">נוירון קדם-סינפטי</div>
        <div class="vesicles"></div>
        <div class="sert-pumps"></div>
    </div>
    <div class="synaptic-cleft">
        <div class="serotonin-molecules"></div>
        <div class="ssri-molecules"></div>
    </div>
    <div class="neuron post-synaptic">
        <div class="neuron-label">נוירון פוסט-סינפטי</div>
        <div class="receptors"></div>
        <div class="activity-meter">
            <div class="meter-label">פעילות:</div>
            <div class="meter-bar"><div id="activity-level" class="level-low"></div></div>
        </div>
    </div>

    <button id="toggle-ssri" class="control-button">הוסף SSRI</button>
</div>

<button id="toggle-explanation" class="explanation-button">הצג הסבר מעמיק</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מפורט: הריקוד המולקולרי בסינפסה</h2>
    <p>המוח שלנו הוא רשת מופלאה של מיליארדי תאי עצב (נוירונים) המתקשרים ביניהם. נקודות המפגש הללו נקראות סינפסות, והן מאפשרות העברת מידע מנוירון אחד לשני.</p>

    <h3>הסינפסה: מבנה ופונקציה</h3>
    <p>דמיינו מרווח קטן, כמו תהום מיקרוסקופית, בין שני נוירונים. זהו המרווח הסינפטי. הנוירון השולח את המידע נקרא **נוירון קדם-סינפטי**, והנוירון המקבל את המידע נקרא **נוירון פוסט-סינפטי**.</p>

    <h3>סרוטונין: השליח העצבי המרכזי</h3>
    <p>כדי להעביר מידע דרך המרווח הסינפטי, הנוירון הקדם-סינפטי משחרר מולקולות מיוחדות הנקראות מוליכים עצביים (נוירוטרנסמיטורים). **סרוטונין** הוא אחד המוליכים העצביים החשובים ביותר, המעורב בוויסות מצב הרוח, שינה, תיאבון, ואף תחושת אושר ורוגע. חוסר איזון או רמות נמוכות מדי של סרוטונין במרווח הסינפטי נקשרים לעיתים קרובות למצבי דיכאון וחרדה.</p>

    <h3>מסלול סרוטונין תקין (ללא SSRI)</h3>
    <p>בסינפסה בריאה ותקינה, תהליך העברת הסרוטונין מתרחש במדויק:</p>
    <ol>
        <li>אות חשמלי מגיע לנוירון הקדם-סינפטי.</li>
        <li>בתגובה, שקיקים קטנים (שלפוחיות או וסיקולות) המכילים סרוטונין מתמזגים עם קצה הנוירון ומשחררים את מולקולות הסרוטונין לתוך המרווח הסינפטי.</li>
        <li>מולקולות הסרוטונין שוות במרווח ומחפשות את "נקודות העגינה" שלהן – **רצפטורים** ספציפיים שנמצאים על פני הנוירון הפוסט-סינפטי. קישור סרוטונין לרצפטור "מפעיל" את הנוירון הפוסט-סינפטי ומעביר לו את האות.</li>
        <li>כדי לוודא שהאות לא יימשך לנצח ולווסת את כמות הסרוטונין במרווח, רוב מולקולות הסרוטונין נאספות בחזרה אל תוך הנוירון הקדם-סינפטי על ידי "משאבות שאיבה" מיוחדות הנקראות **SERT** (Serotonin Transporters). זהו תהליך ה"קליטה מחדש" (Reuptake).</li>
        <li>סרוטונין שלא נאסף בחזרה או נקשר לרצפטורים מפורק על ידי אנזימים במרווח הסינפטי.</li>
    </ol>
    <p>בסימולציה, תוכלו לראות את מולקולות הסרוטונין הכתומות משתחררות, חלקן נקשרות לרצפטורים הסגולים בנוירון הפוסט-סינפטי (ומעלות את מד הפעילות), ורובן נשאבות בחזרה דרך משאבות ה-SERT הירוקות בנוירון הקדם-סינפטי ונעלמות מהמרווח.</p>

    <h3>SSRI: המפתח לשינוי</h3>
    <p>תרופות ממשפחת **SSRI** (מעכבי קליטה מחדש בררניים של סרוטונין), כמו אלו המוצגות בסימולציה כמולקולות קורל (אלמוג), פועלות בצורה גאונית אך פשוטה: הן נקשרות למשאבות ה-SERT וחוסמות אותן! דמיינו שה-SSRI "תופסים את המקום" במשאבה כך שהסרוטונין כבר לא יכול להישאב פנימה.</p>
    <p>כאשר משאבות ה-SERT חסומות על ידי SSRI, תהליך הקליטה מחדש של סרוטונין מואט משמעותית. התוצאה? ריכוז הסרוטונין במרווח הסינפטי עולה! כעת, הרבה יותר מולקולות סרוטונין נשארות במרווח וזמינות להיקשר לרצפטורים על הנוירון הפוסט-סינפטי. בסימולציה, כשתלחצו על כפתור "הוסף SSRI", תראו את המולקולות הקורליות חוסמות את המשאבות, יותר מולקולות סרוטונין נשארות במרווח, ויותר מהן נקשרות לרצפטורים, מה שמתבטא בעלייה בפעילות הנוירון הפוסט-סינפטי.</p>

    <h3>מדוע לוקח זמן עד שה-SSRI משפיעים?</h3>
    <p>חשוב להבין שהקלה בסימפטומי דיכאון בעקבות נטילת SSRI אינה מיידית. לרוב לוקח מספר שבועות (4-6) עד שהתרופה משפיעה באופן טיפולי מלא. ההסבר לכך מורכב וכולל שינויים הסתגלותיים ארוכי טווח המתרחשים במוח בתגובה לרמות הסרוטונין הגבוהות יותר. המוח מסתגל, הרצפטורים עשויים להשתנות ברגישותם או בכמותם, והמסלולים העצביים משתנים בהדרגה. תהליך זה הוא שמוביל לאיזון מחודש ולשיפור מתמשך במצב הרוח.</p>
    <p>הסימולציה מציגה מודל פשטני של התהליך המורכב הזה, אך היא מספקת הדגמה ויזואלית עוצמתית של מנגנון הפעולה הבסיסי של SSRI.</p>
</div>

<style>
    :root {
        --neuron-color-light: #b0e0e6; /* Powder Blue */
        --neuron-color-dark: #4682b4; /* Steel Blue */
        --cleft-bg: #e0ffff; /* Light Cyan */
        --serotonin-color: #ff8c00; /* Dark Orange */
        --serotonin-color-bound: #ff4500; /* Orange Red */
        --sert-color: #32cd32; /* Lime Green */
        --sert-color-blocked: #006400; /* Dark Green */
        --ssri-color: #f08080; /* Light Coral */
        --ssri-color-bound: #cd5c5c; /* Indian Red */
        --receptor-color: #9370db; /* Medium Purple */
        --receptor-color-active: #ba55d3; /* Medium Orchid */
        --activity-low: #3cb371; /* Medium Sea Green */
        --activity-high: #dc143c; /* Crimson */
        --button-primary-bg: #4682b4;
        --button-primary-hover: #5a9ad2;
        --button-secondary-bg: #32cd32;
        --button-secondary-hover: #3ad83a;
        --text-color-dark: #000080; /* Navy */
        --shadow-light: 0 2px 5px rgba(0,0,0,0.2);
        --shadow-medium: 0 4px 10px rgba(0,0,0,0.3);
        --border-radius-smooth: 10px;
    }

    #simulation-container {
        width: 95%; /* More width */
        max-width: 900px; /* Limit max size */
        margin: 20px auto;
        border: 2px solid var(--neuron-color-dark);
        border-radius: var(--border-radius-smooth);
        padding: 0; /* Remove padding here, use inner elements */
        position: relative;
        overflow: hidden; /* Hide things outside */
        height: 350px; /* Slightly taller */
        background: linear-gradient(to bottom, #f0f8ff, #e0ffff); /* Soft gradient background */
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: var(--shadow-medium);
        font-family: 'Arial', sans-serif; /* Use a common font */
    }

     .environment {
         position: absolute;
         top: 0; left: 0; right: 0; bottom: 0;
         background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"><circle cx="10" cy="10" r="2" fill="%23cceeff"/></svg>') repeat; /* Subtle background pattern */
         opacity: 0.3;
         pointer-events: none;
     }

    .neuron {
        width: 220px; /* Wider */
        height: 100%; /* Full height */
        background: linear-gradient(to bottom, var(--neuron-color-light), var(--neuron-color-dark));
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-weight: bold;
        color: white; /* White text on dark background */
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        box-sizing: border-box;
        padding: 20px;
        z-index: 1; /* Above environment */
    }

    .neuron-label {
        position: absolute;
        top: 15px;
        width: 100%;
        font-size: 1.1em;
    }


    .pre-synaptic {
        border-top-right-radius: 175px; /* More rounded */
        border-bottom-right-radius: 175px;
        border-right: 2px solid var(--neuron-color-dark);
        left: 0;
        align-items: flex-end; /* Align content to the cleft side */
        padding-right: 40px; /* Add padding inside the curve */
    }

    .post-synaptic {
        border-top-left-radius: 175px; /* More rounded */
        border-bottom-left-radius: 175px;
         border-left: 2px solid var(--neuron-color-dark);
        right: 0;
        align-items: flex-start; /* Align content to the cleft side */
         padding-left: 40px; /* Add padding inside the curve */
    }

    .synaptic-cleft {
        width: 200px; /* Wider cleft */
        height: 100%;
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: visible; /* Allow molecules to briefly exit */
        z-index: 0; /* Below neurons */
    }

    /* Molecule Containers */
    .serotonin-molecules, .ssri-molecules {
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        pointer-events: none; /* Don't interfere with clicks */
    }

    /* Individual Molecules (managed by JS positioning) */
    .serotonin, .ssri {
        position: absolute; /* JS will set top/left */
        border-radius: 50%;
        opacity: 0.9;
        transition: transform 0.1s ease-out, opacity 0.5s ease-in-out, background-color 0.3s ease; /* Smooth transitions */
         will-change: transform, opacity; /* Optimize animations */
    }

    .serotonin {
        width: 12px; height: 12px;
        background-color: var(--serotonin-color);
        z-index: 5;
    }

    .serotonin.bound {
         background-color: var(--serotonin-color-bound);
         width: 15px; height: 15px; /* Slightly larger when bound */
         opacity: 1;
    }

     .serotonin.reuptaking {
         opacity: 0; /* Fade out */
     }

    .ssri {
        width: 10px; height: 10px;
        background-color: var(--ssri-color);
        border-radius: 3px; /* Square with slight radius */
        z-index: 4;
        animation: float 5s infinite ease-in-out; /* Subtle floating */
    }

    @keyframes float {
        0%, 100% { transform: translate(0, 0); }
        50% { transform: translate(5px, 5px); }
    }

     .ssri.binding-to-sert {
        transition: transform 0.3s ease-out, background-color 0.3s ease; /* Smooth movement to pump */
         background-color: var(--ssri-color-bound);
         opacity: 1;
     }


    .sert-pumps, .receptors {
        position: absolute;
        width: 30px; /* Wider target area */
        height: 80%; /* Takes up more vertical space */
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        align-items: center;
        z-index: 2;
    }

    .sert-pumps {
        left: 10px; /* Position inside pre-synaptic, near cleft edge */
    }

    .receptors {
        right: 10px; /* Position inside post-synaptic, near cleft edge */
    }

    .sert, .receptor {
        width: 20px; height: 25px; /* Larger targets */
        border-radius: 5px;
        border: 2px solid rgba(0,0,0,0.2);
        position: relative; /* For positioning bound molecules */
        display: flex;
        justify-content: center;
        align-items: center;
        transition: background-color 0.3s ease, border-color 0.3s ease;
    }

    .sert {
        background-color: var(--sert-color);
    }

    .sert.blocked {
        background-color: var(--sert-color-blocked);
         border-color: rgba(255,255,255,0.5);
         box-shadow: inset 0 0 5px rgba(0,0,0,0.5);
    }

    .receptor {
        width: 25px; height: 25px; /* Receptors are circles */
        border-radius: 50%;
        background-color: var(--receptor-color);
    }

    .receptor.active {
        background-color: var(--receptor-color-active);
         border-color: rgba(255,255,255,0.5);
         box-shadow: 0 0 8px var(--receptor-color-active); /* Glow effect */
    }

    .vesicles {
        position: absolute;
        top: 20%; /* Position near the cleft */
        right: 20px;
        width: 50px;
        height: 50px;
        background-color: rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        border: 2px solid rgba(255, 255, 255, 0.5);
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        opacity: 0.8;
    }
     .vesicle-serotonin {
        width: 6px; height: 6px;
        background-color: var(--serotonin-color-bound);
        border-radius: 50%;
        margin: 2px;
     }


    .activity-meter {
        position: absolute;
        bottom: 20px;
        left: 20px;
        background-color: rgba(255, 255, 255, 0.9);
        padding: 8px;
        border-radius: 8px;
        font-size: 1em;
        color: var(--text-color-dark);
        box-shadow: var(--shadow-light);
        display: flex;
        align-items: center;
    }
     .meter-label {
         margin-right: 8px;
         font-weight: normal;
     }
     .meter-bar {
         width: 80px;
         height: 15px;
         background-color: #eee;
         border-radius: 7px;
         overflow: hidden;
     }
     #activity-level {
         height: 100%;
         width: 0%; /* JS controls width */
         background-color: var(--activity-low);
         transition: width 0.5s ease-out, background-color 0.5s ease;
     }
     #activity-level.level-low { background-color: var(--activity-low); }
     #activity-level.level-medium { background-color: orange; } /* Added medium state */
     #activity-level.level-high { background-color: var(--activity-high); }


    .control-button {
        position: absolute;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        padding: 12px 25px;
        cursor: pointer;
        background-color: var(--button-primary-bg);
        color: white;
        border: none;
        border-radius: 25px; /* Pill shape */
        font-size: 1.1em;
        font-weight: bold;
        box-shadow: var(--shadow-light);
        transition: background-color 0.3s ease, transform 0.1s ease;
        z-index: 10;
    }

     .control-button:hover {
         background-color: var(--button-primary-hover);
         transform: translateX(-50%) scale(1.05);
     }

      .explanation-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        cursor: pointer;
        background-color: var(--button-secondary-bg);
        color: white;
        border: none;
        border-radius: 25px;
        font-size: 1.1em;
        font-weight: bold;
        box-shadow: var(--shadow-light);
        transition: background-color 0.3s ease, transform 0.1s ease;
      }

    .explanation-button:hover {
         background-color: var(--button-secondary-hover);
         transform: scale(1.05);
    }


    #explanation {
        width: 95%;
        max-width: 900px;
        margin: 30px auto;
        border: 1px solid #ccc;
        border-radius: var(--border-radius-smooth);
        padding: 25px;
        background-color: #fff;
        box-shadow: var(--shadow-light);
        line-height: 1.6;
        color: #333;
    }

    #explanation h2, #explanation h3 {
        color: var(--text-color-dark);
        margin-bottom: 10px;
        border-bottom: 1px solid #eee;
        padding-bottom: 5px;
    }

    #explanation h2 { font-size: 1.8em; }
    #explanation h3 { font-size: 1.4em; margin-top: 20px; }

    #explanation p {
        margin-bottom: 15px;
    }

    #explanation ul, #explanation ol {
        margin-bottom: 15px;
        padding-left: 20px;
    }

    #explanation li {
        margin-bottom: 8px;
    }

    /* Add some serotonin molecules to the vesicle visually */
    .vesicles .vesicle-serotonin:nth-child(1) { transform: translate(-5px, -5px); }
    .vesicles .vesicle-serotonin:nth-child(2) { transform: translate(5px, -5px); }
    .vesicles .vesicle-serotonin:nth-child(3) { transform: translate(-5px, 5px); }
    .vesicles .vesicle-serotonin:nth-child(4) { transform: translate(5px, 5px); }


</style>

<script>
    const simulationContainer = document.getElementById('simulation-container');
    const cleftContainer = simulationContainer.querySelector('.synaptic-cleft');
    const serotoninContainer = cleftContainer.querySelector('.serotonin-molecules');
    const ssriContainer = cleftContainer.querySelector('.ssri-molecules');
    const sertPumpsContainer = simulationContainer.querySelector('.sert-pumps');
    const receptorsContainer = simulationContainer.querySelector('.receptors');
    const activityLevelBar = document.getElementById('activity-level');
    const toggleSSRIButton = document.getElementById('toggle-ssri');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const vesiclesContainer = simulationContainer.querySelector('.vesicles');


    const numSertPumps = 5; // Increased for visual density
    const numReceptors = 6; // Increased
    const numSerotoninMax = 30; // Max serotonin molecules in cleft
    const serotoninReleaseRate = 500; // ms between releases (faster for more action)
    const ssriCount = numSertPumps * 2; // More SSRI than SERT
    const moleculeSpeed = 0.5; // Pixels per frame for movement
    const bindingDistance = 10; // Pixels distance to bind

    let ssriActive = false;
    let serotoninMolecules = [];
    let ssriMolecules = [];
    let sertPumps = []; // Store objects with element and state
    let receptors = []; // Store objects with element and state
    let boundReceptorsCount = 0;

    // --- Helper Functions ---

    function getElementCenter(element) {
        const rect = element.getBoundingClientRect();
        const containerRect = simulationContainer.getBoundingClientRect();
        // Get center relative to the simulation container
        const x = (rect.left + rect.width / 2) - containerRect.left;
        const y = (rect.top + rect.height / 2) - containerRect.top;
        return { x, y };
    }

    function distance(p1, p2) {
        return Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2));
    }

    function moveTowards(mover, targetPos, speed) {
         const currentPos = { x: mover.x, y: mover.y };
         const dx = targetPos.x - currentPos.x;
         const dy = targetPos.y - currentPos.y;
         const dist = distance(currentPos, targetPos);

         if (dist < speed) {
             mover.x = targetPos.x;
             mover.y = targetPos.y;
             return true; // Reached target
         } else {
             mover.x += dx / dist * speed;
             mover.y += dy / dist * speed;
             return false; // Not reached
         }
     }

    function applyPosition(molecule) {
         // Position relative to simulation container for absolute positioning
        molecule.element.style.left = molecule.x + 'px';
        molecule.element.style.top = molecule.y + 'px';
    }

    // --- Setup Simulation Elements ---

    // Create SERT pumps
    const sertGap = (sertPumpsContainer.offsetHeight - numSertPumps * 25) / (numSertPumps + 1); // Calculate spacing
    for (let i = 0; i < numSertPumps; i++) {
        const sertEl = document.createElement('div');
        sertEl.classList.add('sert');
        sertPumpsContainer.appendChild(sertEl);
        // Position vertically within its container
        sertEl.style.top = `${sertGap + i * (25 + sertGap)}px`; // 25 is element height
        sertEl.style.left = '15px'; // Position relative to pumps container
        sertPumps.push({ element: sertEl, blocked: false, ssriBound: null });
    }

     // Create Receptors
     const receptorGap = (receptorsContainer.offsetHeight - numReceptors * 25) / (numReceptors + 1);
    for (let i = 0; i < numReceptors; i++) {
        const receptorEl = document.createElement('div');
        receptorEl.classList.add('receptor');
        receptorsContainer.appendChild(receptorEl);
         // Position vertically within its container
        receptorEl.style.top = `${receptorGap + i * (25 + receptorGap)}px`; // 25 is element height
        receptorEl.style.left = '15px'; // Position relative to receptors container
        receptors.push({ element: receptorEl, bound: false, serotoninBound: null });
    }

    // Create Visual Serotonin in Vesicle
    for(let i = 0; i < 4; i++) {
        const vesicleSerotonin = document.createElement('div');
        vesicleSerotonin.classList.add('vesicle-serotonin');
        vesiclesContainer.appendChild(vesicleSerotonin);
    }


    // Create SSRI molecules (initially hidden)
    function createSSRI() {
        const cleftRect = cleftContainer.getBoundingClientRect();
        const simRect = simulationContainer.getBoundingClientRect();

        for (let i = 0; i < ssriCount; i++) {
             const ssriEl = document.createElement('div');
             ssriEl.classList.add('ssri');
             ssriEl.style.display = 'none'; // Initially hidden

              // Random position within the cleft area (relative to simulation container)
             const startX = cleftRect.left - simRect.left + Math.random() * cleftRect.width;
             const startY = cleftRect.top - simRect.top + Math.random() * cleftRect.height;

             ssriContainer.appendChild(ssriEl);
             ssriMolecules.push({
                 element: ssriEl,
                 x: startX,
                 y: startY,
                 state: 'floating', // floating, binding-to-sert, bound-to-sert
                 targetSert: null,
                 dx: (Math.random() - 0.5) * 0.5, // Gentle random drift
                 dy: (Math.random() - 0.5) * 0.5
            });
             applyPosition(ssriMolecules[i]); // Apply initial position
        }
    }
    createSSRI();


    // Function to create and release a serotonin molecule
    function releaseSerotonin() {
        if (serotoninMolecules.length >= numSerotoninMax) {
            // Don't release if already too crowded
            return;
        }

        const serotoninEl = document.createElement('div');
        serotoninEl.classList.add('serotonin');

        const preSynapticRect = simulationContainer.querySelector('.pre-synaptic').getBoundingClientRect();
        const simRect = simulationContainer.getBoundingClientRect();

        // Start position just outside the pre-synaptic side of the cleft opening
         const startX = preSynapticRect.right - simRect.left - 20; // Just inside the edge
         const startY = preSynapticRect.top - simRect.top + preSynapticRect.height * 0.3 + Math.random() * (preSynapticRect.height * 0.4); // Vertical spread

        serotoninContainer.appendChild(serotoninEl);
        serotoninMolecules.push({
            element: serotoninEl,
            x: startX,
            y: startY,
            state: 'released', // released, binding-receptor, bound-receptor, reuptaking
            targetReceptor: null,
             dx: 1 + Math.random() * 0.5, // Move right towards cleft
             dy: (Math.random() - 0.5) * 1 // Some vertical variation
       });
        applyPosition(serotoninMolecules[serotoninMolecules.length - 1]); // Apply initial position
    }

    // --- Simulation Logic (JS Animation & Interaction) ---

    function updateSimulation() {
        const simRect = simulationContainer.getBoundingClientRect();
        const cleftRect = cleftContainer.getBoundingClientRect();

        boundReceptorsCount = 0; // Reset count for current frame

        // Update SSRI states and positions
        ssriMolecules.forEach(ssri => {
            if (!ssriActive) {
                ssri.element.style.display = 'none'; // Hide if inactive
                ssri.state = 'floating'; // Reset state
                ssri.targetSert = null;
                ssri.element.classList.remove('binding-to-sert');
                return; // Skip update if inactive
            } else {
                ssri.element.style.display = 'block'; // Show if active
            }

            if (ssri.state === 'floating') {
                // Simple drift
                ssri.x += ssri.dx;
                ssri.y += ssri.dy;

                // Bounce off cleft edges (simplified)
                 if (ssri.x < cleftRect.left - simRect.left || ssri.x > cleftRect.right - simRect.left - ssri.element.offsetWidth) ssri.dx *= -1;
                 if (ssri.y < cleftRect.top - simRect.top || ssri.y > cleftRect.bottom - simRect.top - ssri.element.offsetHeight) ssri.dy *= -1;


                // Look for available SERT pumps to bind
                const availableSert = sertPumps.find(sert => !sert.blocked);
                if (availableSert) {
                    const sertCenter = getElementCenter(availableSert.element);
                    const ssriCenter = getElementCenter(ssri.element);
                    if (distance(ssriCenter, sertCenter) < bindingDistance * 2 && Math.random() < 0.05) { // Small chance to start binding if near
                        ssri.state = 'binding-to-sert';
                        ssri.targetSert = availableSert;
                         ssri.element.classList.add('binding-to-sert');
                    }
                }
            } else if (ssri.state === 'binding-to-sert') {
                // Move towards the target SERT pump
                const sertCenter = getElementCenter(ssri.targetSert.element);
                 const reached = moveTowards(ssri, sertCenter, moleculeSpeed * 2); // Move faster to bind

                if (reached) {
                     ssri.state = 'bound-to-sert';
                     ssri.targetSert.blocked = true;
                     ssri.targetSert.element.classList.add('blocked');
                     // Lock SSRI visually onto the SERT
                     const sertRect = ssri.targetSert.element.getBoundingClientRect();
                     const ssriRect = ssri.element.getBoundingClientRect();
                     const simRect = simulationContainer.getBoundingClientRect();
                     ssri.x = (sertRect.left + sertRect.width/2) - ssriRect.width/2 - simRect.left;
                     ssri.y = (sertRect.top + sertRect.height/2) - ssriRect.height/2 - simRect.top;
                     ssri.element.classList.remove('binding-to-sert'); // Remove transition class
                     applyPosition(ssri); // Final position lock

                }
            }
             // If state is 'bound-to-sert', its position is fixed, nothing to do here.
        });

        // Update Serotonin states and positions
        serotoninMolecules.forEach(serotonin => {
             const seroCenter = getElementCenter(serotonin.element);

            if (serotonin.state === 'released') {
                // Move across the cleft
                serotonin.x += serotonin.dx;
                serotonin.y += serotonin.dy;

                // Check for binding to Receptors (when near post-synaptic side)
                const postSynapticEdgeX = simRect.width - simulationContainer.querySelector('.post-synaptic').offsetWidth + 20; // Just inside post-synaptic edge
                if (serotonin.x > postSynapticEdgeX) {
                    const availableReceptor = receptors.find(r => !r.bound);
                    if (availableReceptor) {
                        serotonin.state = 'binding-receptor';
                        serotonin.targetReceptor = availableReceptor;
                        serotonin.element.classList.add('bound'); // Add visual cue
                    } else {
                        // No receptors available, serotonin hangs around briefly or diffuses away (simple: redirect or fade)
                         serotonin.dx *= -0.5; // Bounce back slightly and slow down
                         serotonin.state = 'diffusing'; // New state? Or just let it drift back
                    }
                }

                 // Check for Reuptake (when near pre-synaptic side) - happens *if* not binding
                 const preSynapticEdgeX = simulationContainer.querySelector('.pre-synaptic').offsetWidth - 20; // Just inside pre-synaptic edge
                 if (serotonin.x < preSynapticEdgeX && serotonin.state === 'released') { // Only try reuptake if not actively binding
                     const availableSert = sertPumps.find(sert => !sert.blocked); // Find UNBLOCKED SERT
                      if (availableSert) {
                         serotonin.state = 'reuptaking';
                         serotonin.element.classList.add('reuptaking'); // Visual cue (fade out)
                         // Remove the molecule after a short delay (simulating uptake)
                         setTimeout(() => {
                             if (serotonin.element.parentElement) {
                                 serotonin.element.parentElement.removeChild(serotonin.element);
                                 serotoninMolecules = serotoninMolecules.filter(mol => mol !== serotonin);
                             }
                         }, 300); // Fade out quickly
                      } else {
                           // SERT blocked, cannot reuptake. Serotonin stays in cleft, might try binding again or drift.
                            serotonin.dx = Math.abs(serotonin.dx); // Ensure it moves right back into cleft
                            serotonin.dy = (Math.random() - 0.5) * 1; // Add some vertical drift
                      }
                 }

            } else if (serotonin.state === 'binding-receptor') {
                 // Move towards the target Receptor
                const receptorCenter = getElementCenter(serotonin.targetReceptor.element);
                 const reached = moveTowards(serotonin, receptorCenter, moleculeSpeed * 1.5); // Move slightly faster to bind

                if (reached) {
                     serotonin.state = 'bound-receptor';
                     serotonin.targetReceptor.bound = true;
                     serotonin.targetReceptor.serotoninBound = serotonin; // Link receptor to molecule
                     serotonin.targetReceptor.element.classList.add('active'); // Activate receptor visuals
                     // Lock serotonin visually onto the Receptor
                     const receptorRect = serotonin.targetReceptor.element.getBoundingClientRect();
                      const seroRect = serotonin.element.getBoundingClientRect();
                      const simRect = simulationContainer.getBoundingClientRect();
                      serotonin.x = (receptorRect.left + receptorRect.width/2) - seroRect.width/2 - simRect.left;
                      serotonin.y = (receptorRect.top + receptorRect.height/2) - seroRect.height/2 - simRect.top;
                      applyPosition(serotonin); // Final position lock

                     boundReceptorsCount++; // Count this bound receptor

                    // Serotonin stays bound for a short time, then detaches
                    setTimeout(() => {
                        serotonin.targetReceptor.element.classList.remove('active');
                        serotonin.targetReceptor.bound = false;
                         serotonin.targetReceptor.serotoninBound = null; // Unlink
                        serotonin.element.classList.remove('bound');
                        serotonin.state = 'released'; // Becomes available for reuptake or re-binding
                         // Give it a push back into the cleft
                         serotonin.dx = -0.5; // Push towards pre-synaptic for reuptake chance
                         serotonin.dy = (Math.random() - 0.5) * 1;
                    }, 800); // Stay bound for 0.8 seconds
                } else {
                     // Not reached yet, count it as potentially active for this frame if close
                     if (distance(seroCenter, receptorCenter) < bindingDistance * 3) {
                          boundReceptorsCount++; // Count it while approaching
                     }
                }
            } else if (serotonin.state === 'bound-receptor') {
                 boundReceptorsCount++; // Continue counting while bound
                 // Position is already locked by the 'binding-receptor' state logic
            } else if (serotonin.state === 'diffusing') {
                 // Simple drift when not binding/reuptaking
                 serotonin.x += serotonin.dx * 0.5; // Slower diffusion
                 serotonin.y += serotonin.dy * 0.5;

                  // Bounce off cleft edges
                 if (serotonin.x < cleftRect.left - simRect.left || serotonin.x > cleftRect.right - simRect.left - serotonin.element.offsetWidth) serotonin.dx *= -0.5; // Soft bounce
                 if (serotonin.y < cleftRect.top - simRect.top || serotonin.y > cleftRect.bottom - simRect.top - serotonin.element.offsetHeight) serotonin.dy *= -0.5;


                  // After diffusing for a bit, maybe become eligible for binding/reuptake again?
                  // For now, they just drift. Could add a timer to revert to 'released'.
            }
            // Reuptaking state is handled by removal timer, no position update needed.

             // Apply the calculated position
            if (serotonin.state !== 'bound-receptor' && serotonin.state !== 'reuptaking') {
                 applyPosition(serotonin);
            }
        });


        // Update activity meter based on currently bound receptors
         const activityPercentage = (boundReceptorsCount / numReceptors) * 100;
         activityLevelBar.style.width = `${activityPercentage}%`;

         if (activityPercentage > 70) {
             activityLevelBar.className = 'level-high';
         } else if (activityPercentage > 30) {
              activityLevelBar.className = 'level-medium';
         }
         else {
             activityLevelBar.className = 'level-low';
         }


        // Keep SSRI bound count updated (mostly for debugging, but could be visual)
        // const currentlyBoundSert = sertPumps.filter(sert => sert.blocked).length;
        // console.log("SSRI Bound:", currentlyBoundSert);
        // console.log("Serotonin Bound:", boundReceptorsCount);


        requestAnimationFrame(updateSimulation); // Continue the loop
    }

    // --- Event Listeners ---

    toggleSSRIButton.addEventListener('click', () => {
        ssriActive = !ssriActive;
        toggleSSRIButton.textContent = ssriActive ? 'הסר SSRI' : 'הוסף SSRI';

        // Reset simulation state slightly when toggling SSRI
        // Remove all serotonin molecules instantly to show clear state change
        serotoninMolecules.forEach(s => {
            if (s.element.parentElement) s.element.parentElement.removeChild(s.element);
        });
        serotoninMolecules = []; // Clear array


        // Reset SERT and Receptor states
        sertPumps.forEach(sert => {
            sert.blocked = false;
            sert.ssriBound = null;
            sert.element.classList.remove('blocked');
        });
         receptors.forEach(r => {
             r.bound = false;
             r.serotoninBound = null;
             r.element.classList.remove('active');
         });

        // Reset SSRI states and positions if turning off
         if (!ssriActive) {
             ssriMolecules.forEach(ssri => {
                 ssri.state = 'floating';
                 ssri.targetSert = null;
                 ssri.element.classList.remove('binding-to-sert');
                 // Reset position within cleft area (relative to simulation container)
                 const cleftRect = cleftContainer.getBoundingClientRect();
                 const simRect = simulationContainer.getBoundingClientRect();
                 ssri.x = cleftRect.left - simRect.left + Math.random() * cleftRect.width;
                 ssri.y = cleftRect.top - simRect.top + Math.random() * cleftRect.height;
                 applyPosition(ssri);
             });
         } else {
              // If turning SSRI on, they will dynamically find SERT in the update loop
         }


        boundReceptorsCount = 0; // Reset visual counts


        // Start releasing serotonin again
        startSerotoninRelease();

        // The updateSimulation loop will handle the rest
    });

     toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'הצג הסבר מעמיק';
     });


    // --- Initial Setup ---

    // Start the serotonin release loop
    let serotoninInterval;
    function startSerotoninRelease() {
        if (serotoninInterval) clearInterval(serotoninInterval);
        // Release bursts of serotonin for visual effect
        serotoninInterval = setInterval(() => {
            const burstSize = ssriActive ? 2 : 4; // Release more if SSRI are on (to see the effect)
            for(let i = 0; i < burstSize; i++) {
                 releaseSerotonin();
            }
        }, serotoninReleaseRate);
    }


    // Start the simulation update loop
    startSerotoninRelease();
    updateSimulation(); // Start the animation frame loop


</script>
```