---
title: "קסם הדלק: איך תא מימן מייצר חשמל ומים נקיים?"
english_slug: fuel-magic-how-a-hydrogen-cell-produces-electricity-and-pure-water
category: "מדעים מדויקים / כימיה"
tags:
  - תא דלק
  - מימן
  - חשמל
  - מים
  - אנרגיה ירוקה
  - אלקטרוכימיה
---
# קסם הדלק: איך תא מימן מייצר חשמל ומים נקיים?

דמיינו טכנולוגיה שמייצרת את כל החשמל הדרוש לכם, כשה"פסולת" היחידה שהיא פולטת היא... מים טהורים. נשמע כמו חלום מהעתיד? זהו העיקרון המדהים מאחורי תא הדלק המימני – פתרון אנרגיה נקי ומרתק שמשנה את כללי המשחק. בואו נגלה יחד איך הקסם הזה קורה!

<div class="fuel-cell-container">
    <div class="inlet hydrogen-inlet">כניסת H₂</div>
    <div class="inlet oxygen-inlet">כניסת O₂</div>

    <div class="cell-section anode">
        <h2>אנודה (-)</h2>
        <div class="catalyst-area"></div>
        <div class="reaction-label anode-label">תגובת חמצון</div>
         <div class="particles-container anode-particles"></div>
    </div>

    <div class="membrane">
        <p>ממברנה אלקטרוליטית (PEM)</p>
         <div class="proton-flow-indicator"></div>
    </div>

    <div class="cell-section cathode">
        <h2>קתודה (+)</h2>
        <div class="catalyst-area"></div>
        <div class="reaction-label cathode-label">תגובת חיזור</div>
         <div class="particles-container cathode-particles"></div>
    </div>

    <div class="external-circuit">
        <div class="electron-flow-path"></div>
        <div class="light-bulb">💡</div>
    </div>

    <div class="outlet water-outlet">יציאת H₂O</div>

    <button id="startButton">הפעל קסם</button>
    <div id="resetButton" class="reset-button" style="display: none;">התחל מחדש</div>
</div>

<button id="toggleExplanation" class="toggle-explanation">גלו את הסוד: הסבר מפורט</button>

<div id="explanation" style="display: none;">
    <h2>הסוד נחשף: כך פועל תא דלק מימני</h2>
    <p>תא דלק מימני הוא גאונות אלקטרוכימית! הוא לא "אוגר" חשמל כמו סוללה, אלא "מייצר" אותו באופן רציף כל עוד מקבל דלק (מימן) ומחמצן (חמצן, בדרך כלל מהאוויר). התהליך ממיר אנרגיה כימית ישירות לחשמל, חום, והכי מדהים – מים!</p>

    <h3>השחקנים הראשיים במבנה התא:</h3>
    <ul>
        <li><strong>האנודה (-) - צד המימן:</strong> כאן מתחיל הריקוד המולקולרי. אלקטרודה בעלת מטען שלילי שמושכת אליה את מולקולות המימן.</li>
        <li><strong>הקתודה (+) - צד החמצן:</strong> האלקטרודה החיובית, שאליה מגיע החמצן. כאן מתרחשת התגובה הסופית שיוצרת את המים.</li>
        <li><strong>הממברנה האלקטרוליטית (PEM - Proton Exchange Membrane):</strong> הלב של התא. שכבה דקה וחכמה במיוחד שמאפשרת מעבר סלקטיבי של יונים חיוביים בלבד (פרוטונים H⁺), בעוד שהיא חוסמת לחלוטין את מעבר האלקטרונים והגזים האחרים. זהו המנגנון שמאלץ את האלקטרונים לנסוע בדרך עוקפת – המעגל החיצוני!</li>
        <li><strong>קטליזטורים (זרזים):</strong> חומרים (לרוב פלטינה יקרה) שמצפים את האנודה והקתודה, ומאיצים דרמטית את התגובות הכימיות, ומאפשרים להן להתרחש בטמפרטורות נמוכות יחסית.</li>
    </ul>

    <h3>המסע המופלא של המולקולות והאלקטרונים:</h3>
    <p><strong>שלב 1: באנודה - פירוק המימן</strong></p>
    <p>מולקולות המימן (H₂) נכנסות לתא ומגיעות לאנודה. בעזרת הקטליזטור שעל האנודה, כל מולקולת H₂ מתפרקת לשני יוני מימן חיוביים (פרוטונים, H⁺) ושני אלקטרונים (e⁻):</p>
    <p class="equation">2H₂ → 4H⁺ + 4e⁻</p>

    <p><strong>שלב 2: מסע האלקטרונים המחשמל</strong></p>
    <p>הממברנה חוסמת את האלקטרונים. הם לא יכולים לעבור דרכה! לכן, הם נאלצים לנדוד דרך מסלול חיצוני המחבר את האנודה והקתודה – זהו המעגל החשמלי. תנועת האלקטרונים המאורגנת הזו היא למעשה זרם חשמלי, אותו אנו יכולים לנצל כדי להפעיל מכשירים (כמו המנורה שראיתם בהדמיה!).</p>

    <p><strong>שלב 3: מסע הפרוטונים דרך הממברנה</strong></p>
    <p>בניגוד לאלקטרונים, הפרוטונים (H⁺) כן יכולים לעבור דרך הממברנה הסלקטיבית. הם נעים דרכה אל הקתודה.</p>

    <p><strong>שלב 4: בקתודה - חיבור מחדש ויצירת מים</strong></p>
    <p>בקתודה נפגשים שלושה שחקנים: מולקולות החמצן (O₂) שנכנסו מצד הקתודה, הפרוטונים (H⁺) שהגיעו דרך הממברנה, והאלקטרונים (e⁻) שהגיעו דרך המעגל החיצוני. בעזרת הקטליזטור שעל הקתודה, הם מתאחדים ליצירת מולקולות מים (H₂O):</p>
    <p class="equation">O₂ + 4H⁺ + 4e⁻ → 2H₂O</p>

    <h3>התמונה הגדולה: התגובה הכוללת</h3>
    <p>כאשר מחברים את התגובות באנודה ובקתודה, מקבלים את התגובה הכוללת והמרשימה של תא הדלק המימני:</p>
    <p class="equation">2H₂ (גז מימן) + O₂ (גז חמצן) → 2H₂O (מים) + חשמל + חום</p>
    <p>התוצאה: חשמל נקי וחום שימושי, וה"פסולת" היחידה היא מים טהורים (לרוב בצורת אדים). זו הסיבה שתאי דלק מימניים נחשבים לאחת מטכנולוגיות האנרגיה הנקיות והמבטיחות ביותר לעתיד, החל מכלי רכב ועד תחנות כוח קטנות וגדולות.</p>

    <h3>מדוע תאי דלק מרגשים?</h3>
    <ul>
        <li>**סופר-נקיים:** פולטים רק מים בנקודת השימוש. אין זיהום אוויר או גזי חממה!</li>
        <li>**יעילות גבוהה:** ממירים הרבה יותר אנרגיה מהדלק לחשמל בהשוואה למנועי בערה.</li>
        <li>**שקטים:** פועלים כמעט ללא רעש, מה שהופך אותם לאידיאליים ליישומים שונים.</li>
        <li>**סקלביליים:** ניתן להתאים את גודל המערכת לצרכים שונים, מרכבים קטנים ועד מפעלים.</li>
    </ul>
</div>

<style>
:root {
    --primary-color: #4CAF50; /* Green */
    --secondary-color: #2196F3; /* Blue */
    --anode-color: #E0F7FA; /* Light Cyan */
    --cathode-color: #FFECB3; /* Light Yellow */
    --membrane-color: #B2EBF2; /* Light Cyan-Blue */
    --hydrogen-color: #1976D2; /* Darker Blue */
    --oxygen-color: #D32F2F; /* Darker Red */
    --proton-color: #FF9800; /* Orange */
    --electron-color: #FFEB3B; /* Yellow */
    --water-color: #00BCD4; /* Cyan */
    --text-color: #333;
    --border-color: #9E9E9E; /* Grey */
    --external-circuit-color: #555;
}

.fuel-cell-container {
    direction: rtl;
    width: 680px; /* Increased width for better layout */
    height: 400px; /* Increased height */
    margin: 40px auto;
    border: 2px solid var(--border-color);
    position: relative;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f9f9f9;
    border-radius: 12px; /* More rounded corners */
    overflow: hidden;
    box-shadow: 0 10px 20px rgba(0,0,0,0.1); /* Subtle shadow */
}

.cell-section {
    position: absolute;
    top: 50px; /* Space for external circuit */
    width: 280px; /* Wider sections */
    height: 250px;
    border: 1px solid var(--border-color);
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    box-sizing: border-box;
    background-color: #fff;
    border-radius: 8px;
    overflow: hidden; /* For particles */
}

.anode {
    right: 0;
    border-right: none;
    border-top-right-radius: 12px;
    border-bottom-right-radius: 12px;
    background-color: var(--anode-color);
}

.cathode {
    left: 0;
    border-left: none;
    border-top-left-radius: 12px;
    border-bottom-left-radius: 12px;
    background-color: var(--cathode-color);
}

.membrane {
    position: absolute;
    top: 50px; /* Aligned with cell sections */
    left: 280px; /* Positioned between anode/cathode */
    width: 120px; /* Wider membrane */
    height: 250px;
    background-color: var(--membrane-color);
    border: 1px solid var(--secondary-color);
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-size: 0.9em;
    color: var(--text-color);
    border-radius: 0;
    box-shadow: inset 0 0 5px rgba(0,0,0,0.1);
}

.membrane p {
    transform: rotate(90deg);
    white-space: nowrap;
    font-weight: bold;
    color: var(--hydrogen-color);
}

.proton-flow-indicator {
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 40px;
    height: 100%;
    background: linear-gradient(to bottom, rgba(255,152,0,0.5) 0%, rgba(255,152,0,0) 100%);
    opacity: 0; /* Hidden by default */
    transition: opacity 0.5s ease-in;
}
.proton-flow-indicator.active {
    opacity: 1;
    animation: pulse-proton-indicator 1.5s infinite alternate;
}
@keyframes pulse-proton-indicator {
    from { background-position: 0 0; opacity: 1; }
    to { background-position: 0 100%; opacity: 0.5; }
}


.inlet, .outlet {
    position: absolute;
    width: 100px;
    height: 30px;
    background-color: #eee;
    border: 1px solid var(--border-color);
    text-align: center;
    line-height: 30px;
    font-size: 0.85em;
    color: var(--text-color);
    border-radius: 5px;
    z-index: 1; /* Ensure they are above the main cell */
}
.inlet { top: 20px; } /* Position inlets above the cell */
.outlet { bottom: 20px; } /* Position outlet below the cell */


.hydrogen-inlet {
    right: calc(280px / 2 - 50px); /* Center above anode section */
    background-color: var(--anode-color);
    border-color: var(--hydrogen-color);
    color: var(--hydrogen-color);
    border-top: 3px solid var(--hydrogen-color);
}

.oxygen-inlet {
    left: calc(280px / 2 - 50px); /* Center above cathode section */
    background-color: var(--cathode-color);
    border-color: var(--oxygen-color);
    color: var(--oxygen-color);
     border-top: 3px solid var(--oxygen-color);
}

.water-outlet {
    left: calc(680px / 2 - 50px); /* Center below the whole structure */
    bottom: 20px; /* Positioned below */
    background-color: var(--membrane-color);
    border-color: var(--water-color);
    color: var(--water-color);
    border-bottom: 3px solid var(--water-color);
}

.external-circuit {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 50px;
    border-bottom: 3px solid var(--external-circuit-color);
    box-sizing: border-box;
}

.electron-flow-path {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
     /* Can use background gradient/animation for flow indicator */
}

.light-bulb {
    position: absolute;
    top: 5px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 2.5em; /* Larger bulb */
    transition: color 0.5s ease-in-out, text-shadow 0.5s ease-in-out;
    color: #ccc; /* Default off color */
}

.light-bulb.on {
    color: #FFD700; /* Gold */
    text-shadow: 0 0 8px #FFD700, 0 0 12px #FFA500, 0 0 16px #FF4500; /* More glow */
}

#startButton, .reset-button {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    padding: 12px 25px; /* Larger padding */
    font-size: 1.3em; /* Larger font */
    cursor: pointer;
    border: none;
    border-radius: 6px; /* Slightly more rounded */
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    z-index: 10;
}

#startButton {
    background-color: var(--primary-color); /* Green */
    color: white;
}

#startButton:hover {
    background-color: #45a049;
    transform: translateX(-50%) scale(1.03);
}
#startButton:active {
     transform: translateX(-50%) scale(0.98);
}

.reset-button {
    background-color: var(--oxygen-color); /* Red */
    color: white;
    text-align: center;
}
.reset-button:hover {
    background-color: #c62828;
    transform: translateX(-50%) scale(1.03);
}
.reset-button:active {
    transform: translateX(-50%) scale(0.98);
}

.reaction-label {
    position: absolute;
    bottom: 10px;
    font-size: 0.9em;
    font-weight: bold;
    opacity: 0.8;
}
.anode-label { right: 20px; color: var(--hydrogen-color); }
.cathode-label { left: 20px; color: var(--oxygen-color); }


/* Animation Elements */
.particle {
    position: absolute;
    width: 20px; /* Larger particles */
    height: 20px;
    border-radius: 50%;
    text-align: center;
    line-height: 20px;
    font-size: 0.8em;
    color: white;
    font-weight: bold;
    box-sizing: border-box;
    z-index: 2; /* Ensure particles are above sections */
     box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    transition: transform 0.5s ease-out, opacity 0.5s ease-out; /* For initial movement */
}

.h2-particle {
     background-color: var(--hydrogen-color);
     border: 2px solid #0D47A1; /* Dark blue border */
}
.o2-particle {
     background-color: var(--oxygen-color);
     border: 2px solid #B71C1C; /* Dark red border */
}
.proton {
    background-color: var(--proton-color);
    border: 2px solid #E65100; /* Dark orange border */
}
.electron {
     background-color: var(--electron-color);
     border: 2px solid #FBC02D; /* Darker yellow border */
}
.water {
    background-color: var(--water-color);
     border: 2px solid #00838F; /* Dark cyan border */
}

/* Particle animation stages - managed by JS adding/removing classes */
.particle.move-to-anode {
    animation: move-h2-to-anode 2s linear forwards;
}
.particle.move-to-cathode {
     animation: move-o2-to-cathode 2s linear forwards;
}
.particle.flow-proton {
    animation: flow-proton 3s linear forwards;
}
.particle.flow-electron {
     animation: flow-electron-circuit 6s linear infinite; /* Continuous loop */
}
.particle.flow-water {
    animation: flow-water-out 3s linear forwards;
}


/* Animation Keyframes */
@keyframes move-h2-to-anode {
    from { top: 50px; right: calc(280px / 2 - 10px); opacity: 1; }
    to { top: 150px; right: calc(280px - 30px); opacity: 1; } /* Position inside anode near membrane */
}
@keyframes move-o2-to-cathode {
    from { top: 50px; left: calc(280px / 2 - 10px); opacity: 1; }
    to { top: 150px; left: calc(280px - 30px); opacity: 1; } /* Position inside cathode near membrane */
}


@keyframes flow-proton {
    from { top: 150px; right: calc(280px - 30px); opacity: 1; } /* Start inside anode */
    to { top: 150px; left: calc(280px - 30px); opacity: 1; } /* End inside cathode */
}


@keyframes flow-electron-circuit {
    0% { top: 150px; right: calc(280px - 30px); transform: translateX(0) translateY(0); opacity: 1; } /* Start at anode reaction area */
    10% { top: 150px; right: calc(280px - 30px); opacity: 1; } /* Pause slightly at start */
    20% { top: 25px; right: calc(280px - 30px); opacity: 1; } /* Move up to external circuit level */
    30% { top: 25px; right: calc(680px - 30px); opacity: 1; } /* Move across top right */
    40% { top: 25px; right: calc(680px - 30px); opacity: 1; } /* Pause at bulb start */
    50% { top: 25px; left: calc(680px/2 - 10px); transform: scale(1.2); opacity: 1; } /* Pass through bulb area */
    60% { top: 25px; left: calc(680px - 30px); transform: scale(1); opacity: 1; } /* Move across top left */
    70% { top: 25px; left: calc(280px - 30px); opacity: 1; } /* Arrive above cathode section */
    80% { top: 25px; left: calc(280px - 30px); opacity: 1; } /* Pause slightly above cathode */
    90% { top: 150px; left: calc(280px - 30px); opacity: 1; } /* Move down to cathode reaction area */
    100% { top: 150px; left: calc(280px - 30px); opacity: 1; } /* End and loop */
}


@keyframes flow-water-out {
    from { top: 150px; left: calc(280px - 30px); opacity: 1; } /* Start inside cathode */
    50% { top: 320px; left: calc(680px / 2 - 10px); opacity: 1; } /* Move towards outlet */
    100% { top: 370px; left: calc(680px / 2 - 10px); opacity: 0; } /* Exit downwards and fade */
}

.catalyst-area {
    position: absolute;
    top: 140px;
    width: 90%;
    height: 30px;
    background-color: rgba(158,158,158,0.3); /* Greyish translucent */
    border-radius: 5px;
    border: 1px dashed var(--border-color);
}
.anode .catalyst-area { right: 10px; }
.cathode .catalyst-area { left: 10px; }

.particles-container { /* Not strictly needed with absolute positioning, but good for structure */
     position: absolute;
     top: 0;
     left: 0;
     width: 100%;
     height: 100%;
     pointer-events: none; /* Allow clicks on elements below */
}


#explanation {
    margin-top: 30px; /* More space */
    padding: 25px; /* More padding */
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #fff; /* White background */
    direction: rtl;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    box-shadow: 0 5px 15px rgba(0,0,0,0.08);
}

#explanation h2, #explanation h3 {
    color: var(--primary-color); /* Green headings */
    border-bottom: 2px solid var(--membrane-color); /* Light blue border */
    padding-bottom: 8px;
    margin-top: 25px;
    margin-bottom: 15px;
}

#explanation ul {
    list-style-type: disc;
    margin-right: 25px; /* Adjusted margin */
    padding-right: 0;
}

#explanation li {
    margin-bottom: 10px;
    line-height: 1.5;
    color: var(--text-color);
}

.equation {
    font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace; /* Monospace font for equations */
    background-color: #e8f5e9; /* Lighter green */
    padding: 10px;
    border-left: 4px solid var(--primary-color); /* Green border */
    margin: 20px 0;
    text-align: center;
    font-size: 1.1em;
    overflow-x: auto; /* Allow scrolling if equation is too long */
}

.toggle-explanation {
    display: block;
    margin: 30px auto; /* More space */
    padding: 12px 25px;
    font-size: 1.1em;
    cursor: pointer;
    background-color: var(--secondary-color); /* Blue */
    color: white;
    border: none;
    border-radius: 6px;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.toggle-explanation:hover {
    background-color: #1565c0; /* Darker blue */
     transform: scale(1.03);
}
.toggle-explanation:active {
     transform: scale(0.98);
}

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const startButton = document.getElementById('startButton');
    const resetButton = document.getElementById('resetButton');
    const container = document.querySelector('.fuel-cell-container');
    const lightBulb = container.querySelector('.light-bulb');
    const anodeParticlesContainer = container.querySelector('.anode-particles');
    const cathodeParticlesContainer = container.querySelector('.cathode-particles');
    const protonFlowIndicator = container.querySelector('.proton-flow-indicator');


    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggleExplanation');

    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'גלו את הסוד: הסבר מפורט' : 'הסתר הסבר מפורט';
    });

    let animationRunning = false;
    let particleIntervals = []; // Store intervals for continuous particle creation
    let animationTimeouts = []; // Store timeouts for single animations or cleanup

    function createParticle(type, label) {
        const particle = document.createElement('div');
        particle.classList.add('particle', type);
        particle.textContent = label;
        container.appendChild(particle); // Append to main container for absolute positioning
        return particle;
    }

    function removeParticle(particle, delay = 0) {
         animationTimeouts.push(setTimeout(() => {
              if (particle && particle.parentElement) {
                  particle.remove();
              }
         }, delay));
    }


    function startAnimation() {
        if (animationRunning) return;
        animationRunning = true;

        startButton.style.display = 'none';
        resetButton.style.display = 'block';
        lightBulb.classList.remove('on');
        protonFlowIndicator.classList.remove('active');

        resetAnimation(); // Ensure clean slate before starting

        // --- Step 1: H2 & O2 Inflow ---
        particleIntervals.push(setInterval(() => {
            if (!animationRunning) return;
            const h2 = createParticle('h2-particle', 'H₂');
            // Initial position set via CSS, animation triggered by class
            h2.style.top = '50px';
            h2.style.right = 'calc(280px / 2 - 10px)';
            h2.classList.add('move-to-anode');
            removeParticle(h2, 2000); // Remove H2 after it reaches anode area animation finishes

            const o2 = createParticle('o2-particle', 'O₂');
             // Initial position set via CSS, animation triggered by class
            o2.style.top = '50px';
            o2.style.left = 'calc(280px / 2 - 10px)';
            o2.classList.add('move-to-cathode');
             removeParticle(o2, 2000); // Remove O2 after it reaches cathode area animation finishes

        }, 1500)); // Inject new molecules every 1.5 seconds


         // --- Step 2 & 3: H2 Split, Proton Flow, Electron Flow (continuous) ---
         // This is a bit simplified; in reality, it's tied to H2 splitting.
         // Here, we'll simulate a continuous stream of protons and electrons
         // appearing at the reaction site and flowing.
         animationTimeouts.push(setTimeout(() => { // Start after H2/O2 start flowing
             protonFlowIndicator.classList.add('active');
             lightBulb.classList.add('on');

             // Continuous stream of protons and electrons
             particleIntervals.push(setInterval(() => {
                  if (!animationRunning) return;
                   // Simulate 4 protons and 4 electrons per conceptual reaction cycle
                   for(let i=0; i<4; i++) {
                        const p = createParticle('proton', 'H⁺');
                         // Start position inside anode reaction area
                         p.style.top = `${140 + (i*5)}px`; // Stagger start slightly
                         p.style.right = 'calc(280px - 30px)';
                         p.classList.add('flow-proton');
                         removeParticle(p, 3000); // Remove after flowing through membrane

                        const e = createParticle('electron', 'e⁻');
                         // Start position inside anode reaction area
                         e.style.top = `${140 + (i*5)}px`; // Stagger start slightly
                         e.style.right = 'calc(280px - 30px)';
                         e.classList.add('flow-electron');
                         // Electrons flow continuously, no removal here unless resetting
                         // We let resetAnimation handle removal
                   }
             }, 800)); // Create batches of protons/electrons every 800ms

         }, 1500)); // Start splitting/flow simulation shortly after H2/O2 appear


        // --- Step 4: Water Formation (continuous) ---
        // This is tied to protons/electrons/oxygen arriving at the cathode.
        // We'll simulate water appearing periodically at the cathode reaction site.
         animationTimeouts.push(setTimeout(() => { // Start after electron/proton flow begins
             particleIntervals.push(setInterval(() => {
                 if (!animationRunning) return;
                  // Simulate water formation (e.g., 2 H2O per cycle)
                  for(let i=0; i<2; i++) {
                       const w = createParticle('water', 'H₂O');
                        // Start position inside cathode reaction area
                        w.style.top = `${140 + (i*15)}px`; // Stagger start slightly
                        w.style.left = 'calc(280px - 30px)';
                        w.classList.add('flow-water');
                        removeParticle(w, 3000); // Remove after flowing out
                  }
             }, 1000)); // Create new water molecules every 1 second (slightly offset from particle creation)

         }, 3000)); // Start water formation after components have time to arrive


    }

    function resetAnimation() {
        animationRunning = false;

        // Clear all intervals and timeouts
        particleIntervals.forEach(clearInterval);
        particleIntervals = [];

        animationTimeouts.forEach(clearTimeout);
        animationTimeouts = [];

        // Remove all particles
        container.querySelectorAll('.particle').forEach(p => p.remove());

        // Turn off light and indicator
        lightBulb.classList.remove('on');
        protonFlowIndicator.classList.remove('active');

        // Reset button visibility
        startButton.style.display = 'block';
        resetButton.style.display = 'none';
    }
});
</script>
---