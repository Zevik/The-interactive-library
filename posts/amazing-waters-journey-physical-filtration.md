---
title: "המסע המופלא של המים: הצצה לעולם הסינון הפיזי"
english_slug: amazing-waters-journey-physical-filtration
category: "כללי"
tags: טיהור שפכים, סינון מים, מתקן טיהור, מים ממוחזרים, הנדסת סביבה, מים נקיים, מחזור מים
---
# המסע המופלא של המים: הצצה לעולם הסינון הפיזי

לאן נעלמים המים שאתם מורידים באסלה או המים מהכיור והמקלחת? הם יוצאים למסע מורכב ומדהים כדי לחזור נקיים ככל האפשר לטבע או לשימוש חוזר. השלב הראשון והקריטי במסע הזה הוא הסינון הפיזי – הפרדת כל המוצקים הגסים והעדינים. צאו איתנו למסע אינטראקטיבי וגלו איך מתקן טיהור פשוט, אך גאוני, משתמש בשכבות של חצץ, חול ופחם פעיל כדי להפוך מים עכורים למים צלולים יותר, צעד אחר צעד!

<div id="simulation-container">
    <div id="input-section">
        <h2>מקור המים העכורים</h2>
        <div id="input-tank">
            <p>מי שפכים</p>
            <div id="dirty-water-overlay"></div> <!-- Visual overlay for dirt -->
        </div>
    </div>
    <div id="filter-section">
        <h2>מערכת הסינון הרב-שכבתית</h2>
        <div id="filter-system">
            <!-- Added counter elements -->
            <div class="filter-layer" id="layer-gravel">
                <span>חצץ גס</span>
                 <div class="caught-counter">נלכדו: <span id="gravel-count">0</span></div>
            </div>
            <div class="filter-layer" id="layer-sand">
                <span>חול דק</span>
                <div class="caught-counter">נלכדו: <span id="sand-count">0</span></div>
            </div>
            <div class="filter-layer" id="layer-charcoal">
                <span>פחם פעיל</span>
                 <div class="caught-counter">נלכדו: <span id="charcoal-count">0</span></div>
            </div>
             <!-- Particles will be appended here -->
        </div>
        <div id="output-tank">
            <p>מים מסוננים (לפני טיפול נוסף)</p>
             <div class="caught-counter">עברו סינון: <span id="filtered-count">0</span></div>
        </div>
        <div id="controls">
            <label for="flow-rate">קצב זרימת המים (שחרור חלקיקים):</label>
            <input type="range" id="flow-rate" min="1" max="10" value="5">
            <span id="flow-rate-label">בינוני</span>
            <button id="start-simulation">התחל סינון מופלא</button>
            <button id="reset-simulation" style="display: none;">אפס מערכת</button>
        </div>
    </div>
</div>

<button id="toggle-explanation">הצגת ההסבר המלא / הסתרת ההסבר</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: מסע המים הנקי</h2>

    <h3>מבוא מרתק: למה טיהור שפכים הוא סופר חשוב?</h3>
    <p>שפכים – המים המשומשים שלנו מהבתים, התעשייה והחקלאות – הם עשירים במזהמים: פסולת מוצקה, חומרים אורגניים מומסים, מיקרואורגניזמים ואפילו כימיקלים. אם נזרים אותם ישירות לנהרות או לאדמה, נגרום נזק עצום: זיהום מקורות המים שלנו, פגיעה אנושה בחי ובצומח, סיכון לבריאות הציבור, ובזבוז משאב מים יקר במדינה צחיחה כמו שלנו. טיהור שפכים הוא פשוט הכרחי כדי לשמור על הסביבה, על בריאות כולנו, ולאפשר שימוש חוזר במים – פתרון חכם לעתיד.</p>

    <h3>שלבים קסומים בתהליך טיהור שפכים</h3>
    <p>במתקן טיהור מודרני, המים עוברים סדרת "הרפתקאות" שמנקות אותם, שלב אחר שלב:</p>
    <ul>
        <li>**טיפול ראשוני (פיזי):** השלב שאתם רואים כאן! מסלקים את כל "הדברים הגדולים" – מוצקים גסים ומרחפים – באמצעות מסננים, שיקוע (כשהכבד שוקע) וציפה (כשהקל צף).</li>
        <li>**טיפול שניוני (ביולוגי):** כאן נכנסים לפעולה חיידקים ידידותיים ש"אוכלים" את החומרים האורגניים המומסים שנשארו במים.</li>
        <li>**טיפול שלישוני (מתקדם):** שלב ה"פיניש". מסירים מזהמים ספציפיים כמו חנקן וזרחן, מתכות כבדות, ולבסוף מחטאים את המים (למשל באמצעות כלור או קרינת UV) כדי להרוג חיידקים מזיקים.</li>
    </ul>

    <h3>הכירו את גיבור הסיפור: שלב הסינון הפיזי</h3>
    <p>הסינון הפיזי הוא השוער של מתקן הטיהור, החלק המכני הראשון שפוגש את המים. תפקידו העיקרי הוא ללכוד ולהסיר את כל החלקיקים המוצקים שצפים או מרחפים במים, מגדולים מאוד ועד קטנים יחסית. הסרת הפסולת המוצקה הזו חיונית – היא מגינה על המשאבות והציוד העדין בשלבים הבאים מפני סתימות ושחיקה, והופכת את עבודתם של החיידקים בשלב הביולוגי לקלה ויעילה יותר.</p>

    <h3>איך עובד קסם הסינון? העיקרון הפשוט</h3>
    <p>זה פשוט כמו מסננת, רק גדולה ומתוחכמת יותר! המים מוזרמים דרך מצע שמלא בנקבוביות. חלקיקים מוצקים שגדולים יותר מהנקבוביות נתקעים ונשארים מאחור, בעוד שהמים הנקיים יחסית עוברים דרך. גודל הנקבוביות, ובהתאם גודל החלקיקים הנלכדים, נקבעים על ידי גודל וסוג הגרגרים שמהם מורכב מצע הסינון.</p>

    <h3>השחקנים הראשיים: סוגי מצעי סינון נפוצים</h3>
    <p>ברוב מתקני הטיהור הגדולים משתמשים בכמה סוגי מצעים, מסודרים זה על גבי זה:</p>
    <ul>
        <li>**חצץ (Gravel):** הגרגרים הגדולים ביותר. נמצא לרוב בשכבה העליונה (כמו בסימולציה כאן) ולוכד את המוצקים הגסים ביותר, או משמש כשכבה תומכת בתחתית.</li>
        <li>**חול (Sand):** גרגרים קטנים יותר מהחצץ. מהווה את רוב נפח המצע ולוכד חלקיקים בינוניים ודקים יותר.</li>
        <li>**פחם פעיל (Activated Charcoal):** חומר מדהים עם שטח פנים פנימי עצום (בגלל מבנה נקבובי מאוד עדין). מסוגל ללכוד אפילו חלקיקים מיקרוסקופיים ואף לספוח אליו (בתהליך שנקרא אדסורפציה) חומרים מומסים מסוימים שגורמים לריח או צבע.</li>
    </ul>

    <h3>למה סדר השכבות חשוב? הסידור החכם</h3>
    <p>במתקני סינון שבהם המים זורמים מלמעלה למטה (כמו בסימולציה), הסידור ההגיוני והיעיל ביותר הוא להתחיל במצע הגס (חצץ) ולעבור למצעים הולכים ודקים (חול, פחם פעיל). למה? כי השכבה העליונה תופסת את החלקיקים הגדולים ביותר. זה מונע מהחלקיקים הגדולים להגיע במהירות לשכבות הדקות שמתחת ולסתום אותן. כך, כל שכבה עושה את עבודתה ומגנה על השכבות העדינות יותר, והמסנן כולו יכול לעבוד ביעילות לאורך זמן רב יותר לפני שהוא נסתם לחלוטין ודורש ניקוי.</p>

    <h3>מה משפיע על הצלחת הסינון? הגורמים החשובים</h3>
    <ul>
        <li>**קצב הזרימה:** אם המים זורמים מהר מדי, לחץ הזרימה עלול לדחוף חלק מהחלקיקים הקטנים דרך הנקבוביות או אפילו לפגוע בשלמות שכבות המצע. זרימה אופטימלית מאפשרת למים "לבלות" מספיק זמן במגע עם המצע ולכוד כמה שיותר חלקיקים.</li>
        <li>**גודל וריכוז המזהמים:** ככל שיש יותר חלקיקים וככל שהם קטנים יותר, כך הסינון הופך קשה יותר והמסנן נסתם מהר יותר.</li>
        <li>**סוג ועובי המצע:** מצע דק יותר (כמו פחם פעיל) לוכד חלקיקים קטנים יותר. שכבה עבה יותר יכולה ללכוד יותר לכלוך לפני סתימה.</li>
        <li>**שטיפה חוזרת (Backwashing):** כמו כל מסנן, גם המסנן הזה נסתם בסוף מהלכלוך שנלכד. כדי לנקות אותו ולהחזיר לו את יעילותו, מזרימים מים נקיים (לרוב בכיוון ההפוך, מלמטה למעלה) בלחץ כדי לשטוף החוצה את החלקיקים שנלכדו.</li>
    </ul>

    <h3>ומה הלאה? לאן ממשיכים המים המסוננים?</h3>
    <p>חשוב לזכור: המים שיצאו משלב הסינון הפיזי אומנם נראים נקיים בהרבה, והמוצקים הוסרו מהם, אך הם עדיין מכילים חומרים מומסים ומיקרואורגניזמים. לכן, הם ממשיכים מיד לשלבים הבאים במתקן הטיהור: לטיפול הביולוגי המטהר לעומק, ולעיתים קרובות גם לטיפול שלישוני מתקדם. רק לאחר שעברו את כל השלבים, המים נחשבים ראויים לשחרור לסביבה או לשימוש חוזר בטוח (למשל, להשקיית גינות ושדות). המסע המופלא שלהם הסתיים בהצלחה!</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const inputTank = document.getElementById('input-tank');
    const dirtyWaterOverlay = document.getElementById('dirty-water-overlay');
    const filterSystem = document.getElementById('filter-system');
    const outputTank = document.getElementById('output-tank');
    const flowRateSlider = document.getElementById('flow-rate');
    const flowRateLabel = document.getElementById('flow-rate-label');
    const startSimulationButton = document.getElementById('start-simulation');
    const resetSimulationButton = document.getElementById('reset-simulation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // Counters
    const gravelCountSpan = document.getElementById('gravel-count');
    const sandCountSpan = document.getElementById('sand-count');
    const charcoalCountSpan = document.getElementById('charcoal-count');
    const filteredCountSpan = document.getElementById('filtered-count');

    let particles = [];
    let simulationInterval = null;
    let particleReleaseInterval = null;
    const particleSpeed = 0.8; // Base speed, slightly faster
    const particleReleaseRateBase = 100; // milliseconds between releasing batches (fast base)
    let particlesToReleasePerBatch = 5; // Based on flow rate slider value
    const maxParticles = 400; // Limit total particles for performance

    // Define layer Y boundaries and filtering properties
    const layers = [
        { id: 'layer-gravel', type: 'large', element: document.getElementById('layer-gravel'), count: 0, countElement: gravelCountSpan },
        { id: 'layer-sand', type: 'medium', element: document.getElementById('layer-sand'), count: 0, countElement: sandCountSpan },
        { id: 'layer-charcoal', type: 'small', element: document.getElementById('layer-charcoal'), count: 0, countElement: charcoalCountSpan },
    ];

    let layerBoundaries = []; // { topY, bottomY, filterSize, layerIndex }
    let filterSystemHeight = 0;
    let outputTankRelativeTop = 0; // Y position where particles enter output tank area (relative to filterSystem top)
    let totalSystemHeight = 0; // filterSystem height + outputTank height

    function calculateLayoutMetrics() {
        const filterRect = filterSystem.getBoundingClientRect();
        const outputTankRect = outputTank.getBoundingClientRect();
        const containerRect = document.getElementById('simulation-container').getBoundingClientRect(); // Use container for relative calculation

        // Calculate layer boundaries relative to the filter-system's top edge
        layerBoundaries = []; // Clear previous
        layers.forEach((layer, index) => {
             const layerRect = layer.element.getBoundingClientRect();
             layerBoundaries.push({
                 topY: layerRect.top - filterRect.top,
                 bottomY: layerRect.bottom - filterRect.top,
                 filterSize: layer.type,
                 layerIndex: index // Store index to update layer's count
             });
        });

        filterSystemHeight = filterRect.height;
        // Calculate output tank top relative to filter system top
        // The gap between filterSystem and outputTank is also relevant
        outputTankRelativeTop = outputTank.offsetTop - filterSystem.offsetTop + filterSystemHeight; // This is distance from filterSystem top to outputTank top margin-top

        // Total visual space for particles to fall through (filter + output tank)
        totalSystemHeight = filterSystemHeight + outputTank.offsetHeight + parseInt(window.getComputedStyle(outputTank).marginTop);
    }


    function createParticle() {
        const filterRect = filterSystem.getBoundingClientRect();
        const startX = Math.random() * (filterRect.width - 10) + 5; // Random X within filter width

        const particle = document.createElement('div');
        particle.classList.add('particle');

        const sizeType = ['small', 'medium', 'large'][Math.floor(Math.random() * 3)]; // Random size
        particle.classList.add('size-' + sizeType);

        // Assign color based on size/type (earthy/dirty tones)
        let color;
        if (sizeType === 'small') color = '#333'; // Dark grey/black
        else if (sizeType === 'medium') color = '#8B4513'; // SaddleBrown
        else color = '#5A2D00'; // Darker brown
        particle.style.backgroundColor = color;


        // Slight randomness in starting X within a narrow central band perhaps? Or just random across width.
        // Let's stick to random across width for simplicity.
        particle.style.left = `${startX}px`;
        particle.style.top = '0px'; // Start at the very top of the filter system

        filterSystem.appendChild(particle); // Append to filter system

        particles.push({
            element: particle,
            x: startX,
            y: 0, // Start Y relative to filterSystem top
            size: sizeType,
            state: 'falling' // 'falling', 'stuck', 'filtered'
        });
    }

    function updateSimulation() {
        // Filter out particles that have fallen completely out of view
        particles = particles.filter(p => p.state !== 'filtered' || p.y < totalSystemHeight + 20); // Keep particles briefly after 'filtered' state

        particles.forEach(p => {
            if (p.state === 'falling') {
                p.y += particleSpeed;

                // Check for layer collision from top layer downwards
                let caught = false;
                for (const layer of layerBoundaries) {
                    // Check if particle's current position is within the layer's vertical span
                    if (p.y >= layer.topY && p.y < layer.bottomY) {
                        // Determine if this layer catches this particle size
                        let catches = false;
                        if (layer.filterSize === 'large' && p.size === 'large') catches = true;
                        else if (layer.filterSize === 'medium' && (p.size === 'medium' || p.size === 'large')) catches = true; // Sand catches Medium and Large
                        else if (layer.filterSize === 'small' && (p.size === 'small' || p.size === 'medium' || p.size === 'large')) catches = true; // Charcoal catches Small, Medium, Large

                        if (catches) {
                            // Particle gets stuck
                            p.state = 'stuck';
                            caught = true;

                            // Increment counter for the layer it got stuck in
                            layers[layer.layerIndex].count++;
                            layers[layer.layerIndex].countElement.textContent = layers[layer.layerIndex].count;

                            // Position it visually *within* the layer it got stuck in
                            // Ensure particle is inside the layer's visual boundaries
                            const particleHeight = p.element.offsetHeight;
                            // Randomize the Y position slightly within the layer's bounds
                            p.y = Math.max(layer.topY, Math.min(p.y, layer.bottomY - particleHeight / 2)); // Keep it within layer bounds
                             // Add slight horizontal randomness when stuck
                             const layerElementRect = layer.element.getBoundingClientRect();
                             const filterElementRect = filterSystem.getBoundingClientRect();
                             const currentX = p.x; // Current X relative to filter system
                             const randomOffsetX = (Math.random() - 0.5) * 10; // +/- 5px offset
                             const newX = Math.max(5, Math.min(filterElementRect.width - particleHeight - 5, currentX + randomOffsetX));
                             p.x = newX; // Update particle's internal x state


                             p.element.style.left = `${p.x}px`;
                            p.element.style.top = `${p.y}px`;
                            p.element.style.opacity = '0.7'; // Make stuck particles slightly faded

                            // No further movement for this particle this frame
                            break; // Particle was caught, stop checking lower layers
                        }
                    }
                }

                // If particle wasn't caught by any layer, check if it reached the output tank area
                if (!caught && p.y >= outputTankRelativeTop) {
                    p.state = 'filtered';
                    // Increment filtered counter
                    let currentFilteredCount = parseInt(filteredCountSpan.textContent);
                    filteredCountSpan.textContent = currentFilteredCount + 1;

                    // Position it within the output tank area (relative to filterSystem top)
                     p.y = outputTankRelativeTop + (p.y - outputTankRelativeTop); // Continue falling into tank space
                    // Reposition particle relative to filterSystem
                    p.element.style.top = `${p.y}px`;
                     // Ensure particle is visually contained within the output tank
                     const outputTankVisualBottomRelative = totalSystemHeight; // Bottom of output tank relative to filterSystem top
                     if (p.y > outputTankVisualBottomRelative - p.element.offsetHeight) {
                         p.y = outputTankVisualBottomRelative - p.element.offsetHeight;
                         p.element.style.top = `${p.y}px`;
                     }

                     // Optional: Add a class or style for filtered particles
                     p.element.classList.add('filtered-particle');
                } else if (!caught) {
                     // Particle is still falling through filter system
                     p.element.style.top = `${p.y}px`;
                }
            } else if (p.state === 'filtered') {
                 // Particles in filtered state might continue settling down in the output tank area
                 const totalSystemHeight = filterSystemHeight + outputTank.offsetHeight + parseInt(window.getComputedStyle(outputTank).marginTop);
                 const particleHeight = p.element.offsetHeight;
                  if (p.y < totalSystemHeight - particleHeight / 2) {
                      p.y += particleSpeed * 0.3; // Slower settling speed
                       p.y = Math.min(p.y, totalSystemHeight - particleHeight / 2); // Don't fall out the bottom
                       p.element.style.top = `${p.y}px`;
                  }
            }
            // Stuck particles don't move (their position was set when state became 'stuck')
        });
    }

     function updateFlowRateLabel(value) {
        let label = "";
        if (value >= 1 && value <= 3) label = "איטי";
        else if (value >= 4 && value <= 7) label = "בינוני";
        else label = "מהיר";
        flowRateLabel.textContent = label;
    }


    function startSimulation() {
        resetSimulation(); // Clear previous run
        // Calculate boundaries only after elements are rendered
        calculateLayoutMetrics();

        // Determine particle release rate based on slider
        particlesToReleasePerBatch = parseInt(flowRateSlider.value);

        // Start releasing particles periodically
        particleReleaseInterval = setInterval(() => {
             if (particles.length < maxParticles) { // Limit total number of particles
                 for(let i = 0; i < particlesToReleasePerBatch; i++) {
                     createParticle();
                 }
             }
        }, particleReleaseRateBase); // Release a batch every X ms

        // Start the main simulation update loop
        simulationInterval = setInterval(updateSimulation, 30); // Update more frequently for smoother animation

        startSimulationButton.style.display = 'none';
        resetSimulationButton.style.display = 'inline-block';
        flowRateSlider.disabled = false; // Allow changing flow rate during simulation
    }

    function resetSimulation() {
        clearInterval(simulationInterval);
        clearInterval(particleReleaseInterval);
        particles.forEach(p => p.element.remove());
        particles = [];

        // Reset counters
        layers.forEach(layer => {
            layer.count = 0;
            layer.countElement.textContent = '0';
        });
        filteredCountSpan.textContent = '0';

        // Reset UI states
        startSimulationButton.style.display = 'inline-block';
        resetSimulationButton.style.display = 'none';
         flowRateSlider.value = 5; // Reset slider
        updateFlowRateLabel(5); // Reset label
        flowRateSlider.disabled = false; // Ensure slider is enabled before next start
        inputTank.innerHTML = '<p>מי שפכים</p><div id="dirty-water-overlay"></div>'; // Restore overlay
        outputTank.innerHTML = '<p>מים מסוננים (לפני טיפול נוסף)</p><div class="caught-counter">עברו סינון: <span id="filtered-count">0</span></div>'; // Restore filtered counter span
        // Need to re-get filteredCountSpan element as innerHTML replaced it
         document.getElementById('filtered-count').textContent = '0';


         // Recalculate metrics just in case
        calculateLayoutMetrics();
    }

    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none';
        // Add a slight transition effect
        if (isHidden) {
             explanationDiv.style.transition = 'opacity 0.5s ease-in-out';
             explanationDiv.style.opacity = '0';
             explanationDiv.style.display = 'block';
             // Force reflow to make transition work
             explanationDiv.offsetHeight;
             explanationDiv.style.opacity = '1';
        } else {
             explanationDiv.style.transition = 'opacity 0.5s ease-in-out';
             explanationDiv.style.opacity = '0';
             explanationDiv.addEventListener('transitionend', function handler() {
                 explanationDiv.style.display = 'none';
                 explanationDiv.style.removeProperty('transition');
                 explanationDiv.style.removeProperty('opacity'); // Clean up inline styles
                 explanationDiv.removeEventListener('transitionend', handler);
             });
        }
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מלא' : 'הצגת ההסבר המלא / הסתרת ההסבר';
    }

    // Event Listeners
    startSimulationButton.addEventListener('click', startSimulation);
    resetSimulationButton.addEventListener('click', resetSimulation);
    toggleExplanationButton.addEventListener('click', toggleExplanation);
    flowRateSlider.addEventListener('input', (event) => {
         particlesToReleasePerBatch = parseInt(event.target.value);
         updateFlowRateLabel(event.target.value);
    });


    // Initial setup
    updateFlowRateLabel(flowRateSlider.value); // Set initial label
    // Need to calculate layout metrics once initially too
    calculateLayoutMetrics();
    // Listen for window resize to recalculate boundaries
    window.addEventListener('resize', calculateLayoutMetrics);

});
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Varela+Round&display=swap'); /* Using Varela Round for a friendly feel */

body {
    font-family: 'Varela Round', sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f4f7f6; /* Soft background */
    padding: 20px;
    direction: rtl; /* Ensure RTL for Hebrew */
    text-align: right;
}

h1, h2, h3 {
    color: #004080; /* Darker blue for headings */
    margin-bottom: 10px;
}

h1 { font-size: 2em; text-align: center; margin-bottom: 20px;}
h2 { font-size: 1.5em; }
h3 { font-size: 1.2em; margin-top: 20px;}

p, ul {
    margin-bottom: 15px;
}

ul {
     padding-right: 20px; /* Indent list items */
}

li {
    margin-bottom: 8px;
}

#simulation-container {
    display: flex;
    gap: 30px; /* Increased gap */
    justify-content: center;
    margin: 30px auto; /* Center the container and add space */
    max-width: 900px; /* Limit max width */
    flex-wrap: wrap;
    background-color: #fff; /* White background for simulation area */
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); /* Subtle shadow */
}

#input-section, #filter-section {
    flex: 1;
    min-width: 300px; /* Adjusted minimum width */
    display: flex;
    flex-direction: column;
    background-color: #e9ecef; /* Light grey background for sections */
    border-radius: 8px;
    padding: 15px;
}

#input-tank {
    width: 100%;
    flex-grow: 1; /* Occupy available space */
    min-height: 200px; /* Increased minimum height */
    border: 2px solid #5a6268; /* Darker border */
    position: relative;
    overflow: hidden;
    background-color: #7B3F00; /* Deep muddy brown */
    display: flex;
    justify-content: center;
    align-items: center;
    color: rgba(255, 255, 255, 0.9);
    font-weight: bold;
    font-size: 1.1em;
    border-radius: 8px;
     box-shadow: inset 0 0 10px rgba(0,0,0,0.3); /* Inner shadow for depth */
}

#dirty-water-overlay {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(circle at 50% 50%, rgba(139,69,19, 0.8) 0%, rgba(165,42,42, 0.6) 50%, rgba(128,0,0, 0.4) 100%); /* Muddy gradient */
     opacity: 1; /* Initially fully opaque */
     /* Add subtle animation potential later */
}

#filter-section {
    display: flex;
    flex-direction: column;
}

#filter-system {
    width: 100%;
    flex-grow: 1; /* Occupy space above output */
    border: 2px solid #5a6268; /* Darker border */
    position: relative;
    overflow: hidden; /* Hide particles outside */
    display: flex;
    flex-direction: column;
    min-height: 250px; /* Increased minimum height */
    border-radius: 8px;
     box-shadow: inset 0 0 10px rgba(0,0,0,0.3); /* Inner shadow for depth */
}

.filter-layer {
    width: 100%;
    flex-grow: 1; /* Divide height among layers */
    display: flex;
    flex-direction: column; /* Stack text and counter vertically */
    justify-content: center;
    align-items: center;
    border-bottom: 1px solid #5a6268;
    box-sizing: border-box;
    position: relative;
    color: #333;
    font-size: 0.95em;
    text-align: center;
    padding: 5px; /* Add some padding */
}

.filter-layer:last-child {
    border-bottom: none; /* No border on the last layer */
}

/* Add background patterns to layers for texture */
#layer-gravel { background-color: #a9a9a9; background-image: radial-gradient(circle, #bdbdbd 15%, transparent 15%), radial-gradient(circle, #bdbdbd 15%, transparent 15%); background-size: 20px 20px; background-position: 0 0, 10px 10px;} /* Gravel texture */
#layer-sand { background-color: #f0e68c; background-image: radial-gradient(circle, #f5f5dc 10%, transparent 10%), radial-gradient(circle, #f5f5dc 10%, transparent 10%); background-size: 15px 15px; background-position: 0 0, 7.5px 7.5px;}   /* Sand texture */
#layer-charcoal { background-color: #36454f; color: #eee; background-image: radial-gradient(circle, #4f5f6f 8%, transparent 8%), radial-gradient(circle, #4f5f6f 8%, transparent 8%); background-size: 10px 10px; background-position: 0 0, 5px 5px;} /* Charcoal texture */

.caught-counter {
    font-size: 0.8em;
    color: #004080; /* Dark blue */
    margin-top: 5px;
    background-color: rgba(255, 255, 255, 0.7);
    padding: 2px 5px;
    border-radius: 3px;
}
#layer-charcoal .caught-counter { color: #e9ecef; background-color: rgba(0, 0, 0, 0.5);}

#output-tank {
    width: 100%;
    min-height: 80px; /* Increased minimum height */
    background-color: #87CEEB; /* Sky blue for filtered water */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 15px; /* Space between filter and output */
    border: 2px solid #5a6268; /* Darker border */
    color: #333;
    font-weight: bold;
    font-size: 1.1em;
    border-radius: 8px;
     box-shadow: inset 0 0 10px rgba(0,0,0,0.3); /* Inner shadow */
     position: relative; /* Needed for filtered particles positioning */
     overflow: hidden;
}

#output-tank p {
    margin-bottom: 5px;
}


.particle {
    position: absolute;
    border-radius: 50%;
    z-index: 2; /* Above layers and counters */
    pointer-events: none; /* Don't interfere with clicks */
    transition: top 0.03s linear, left 0.03s linear; /* Smooth movement */
}

/* Particle colors defined in JS */

.particle.size-large { width: 10px; height: 10px; }
.particle.size-medium { width: 7px; height: 7px; }
.particle.size-small { width: 4px; height: 4px; }

.particle.filtered-particle {
    /* Optional: style change for filtered particles */
     /* background-color: rgba(135, 206, 235, 0.8); /* Slightly transparent blue */
}


#controls {
    margin-top: 20px; /* More space */
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 15px; /* Increased gap */
    padding: 10px;
    background-color: #dee2e6; /* Light background for controls */
    border-radius: 8px;
}

#controls label {
    white-space: nowrap;
    font-weight: bold;
    color: #004080;
}

#controls input[type="range"] {
    flex-grow: 1; /* Allow slider to take space */
    max-width: 150px;
}

#controls span {
     min-width: 40px; /* Give space for label */
     text-align: center;
     font-weight: bold;
     color: #5a6268;
}


button {
    padding: 10px 20px; /* Larger buttons */
    background-color: #007bff; /* Primary blue */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1.1em;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    font-family: 'Varela Round', sans-serif; /* Use consistent font */
}

button:hover {
    background-color: #0056b3; /* Darker blue on hover */
    box-shadow: 0 3px 7px rgba(0, 0, 0, 0.3);
}

button:active {
    transform: scale(0.98); /* Press effect */
}

button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
    box-shadow: none;
}

#toggle-explanation {
    display: block;
    margin: 30px auto; /* Center and space */
    width: fit-content;
    background-color: #6c757d; /* Secondary color */
}
#toggle-explanation:hover {
    background-color: #5a6268;
}


#explanation {
    border: 1px solid #ced4da; /* Light border */
    padding: 20px; /* More padding */
    border-radius: 8px;
    margin-top: 20px;
    background-color: #e9ecef; /* Light grey background */
    color: #333;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    opacity: 1; /* Default state for js transition */
    transition: opacity 0.5s ease-in-out;
}

#explanation h2, #explanation h3 {
    color: #004080;
    margin-top: 20px;
    margin-bottom: 10px;
    border-bottom: 1px solid #adb5bd; /* Subtle separator */
    padding-bottom: 5px;
}

#explanation ul {
    margin-top: 10px;
    padding-right: 25px; /* Indent list items */
}

#explanation li {
    margin-bottom: 10px;
    position: relative; /* For potential bullet styling */
}

/* Add a custom bullet style */
#explanation li::before {
    content: '•'; /* Use a simple dot */
    color: #007bff; /* Blue bullet */
    font-weight: bold;
    display: inline-block;
    width: 1em;
    margin-right: 0.5em;
    margin-left: -1em; /* Pull bullet back */
    text-align: center;
}


/* Responsive adjustments */
@media (max-width: 768px) {
    #simulation-container {
        flex-direction: column;
        gap: 20px;
    }

    #input-section, #filter-section {
        min-width: unset; /* Remove min-width on small screens */
        width: 100%;
    }

    #controls {
        flex-direction: column;
        gap: 10px;
    }

    #controls input[type="range"] {
         width: 100%;
         max-width: unset;
    }
}
</style>