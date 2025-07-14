---
title: "קרח פנקייק: הפלא העגול של הים הקפוא"
english_slug: pancake-ice-why-does-the-sea-freeze-in-round-pancake-shapes
category: "מדעי הסביבה / כדור הארץ"
tags: [קרח ימי, אוקיינוגרפיה, קריוספרה, פיזיקה, היווצרות קרח, אנטרקטיקה, ארקטיקה]
---
<h1>קרח פנקייק: הפלא העגול של הים הקפוא</h1>
<p>דמיינו ים קפוא. האם אתם רואים משטח לבן וחלק? לרוב זה מה שקורה בסוף, אבל לעיתים קרובות, בדרך אל הקפיאה המלאה, הטבע מפתיע עם תצורות קרח עגולות וקסומות שצפות על המים ונראות כאילו ענק הכין ארוחת בוקר קפואה. אלו הם "פנקייק קרח". מה בדיוק גורם לים לקפוא דווקא בצורה הזו?</p>

<div id="simulation-container">
    <h2>חקרו את התופעה: איך נוצר פנקייק קרח?</h2>
    <p>שנו את התנאים למטה וצפו בסימולציה כדי לראות כיצד הים קופא!</p>
    <div class="controls">
        <div class="control-group">
            <label for="iceRate">קצב התקררות המים (היווצרות קרח ראשוני):</label>
            <input type="range" id="iceRate" min="0" max="100" value="30">
            <span id="iceRateValue">30%</span>
        </div>
        <div class="control-group">
            <label for="windStrength">עוצמת רוח וגלים:</label>
            <input type="range" id="windStrength" min="0" max="100" value="30">
            <span id="windStrengthValue">30%</span>
        </div>
        <button id="resetSimulation">התחילו מחדש</button>
    </div>
    <canvas id="iceCanvas" width="700" height="450"></canvas>
    <p id="currentCondition" class="condition-display">תנאים נוכחיים: המים מתחילים להתקרר...</p>
</div>

<button id="toggleExplanation" class="toggle-button">הבנתם איך זה עובד? לחצו כאן להסבר המלא</button>

<div id="explanation" class="explanation-section">
    <h2>הסבר מדעי: המסע המופלא ממים נוזליים לפנקייק קרח</h2>

    <p><strong>אז מה זה בעצם קרח פנקייק וממה הוא מורכב?</strong><br>
    קרח פנקייק הוא לא סתם גוש קרח עגול. הוא שלב מרתק וחיוני בהיווצרות קרח ימי באזורים בהם הים אינו שקט לחלוטין. הוא מורכב מדיסקיות קרח ייחודיות: עגולות, שטוחות יחסית במרכז, אך עם שוליים מוגבהים ועבים יותר. הקוטר שלהן נע לרוב בין 30 ס"מ לשלושה מטרים, והעובי בין 10 ל-20 ס"מ. אותם שוליים מוגבהים הם 'חתימת האצבע' של תהליך ההיווצרות הייחודי שלהם.</p>

    <p><strong>המסע של הקרח: שלב אחר שלב</strong><br>
    היווצרות קרח ימי היא דרמה איטית ורבת שלבים. קרח פנקייק הוא שחקן מרכזי באחד הפרקים:
    <ol>
        <li><strong>Frazil Ice (גבישי קרח ראשוניים):</strong> הכל מתחיל כאן. כשטמפרטורת מי הים יורדת מעט מתחת לנקודת הקיפאון (בגלל המלח, זה קצת פחות מ-0°C, לרוב סביב -1.8°C), מתחילים להיווצר גבישי קרח זעירים, דמויי מחטים או דיסקיות זעירות, בתוך עמוד המים העליון.</li>
        <li><strong>Grease Ice (עיסת קרח):</strong> הגבישים הזעירים צפים אל פני השטח ומתקבצים יחד. הם יוצרים שכבה דקה וצמיגה, שעלולה לגרום למים להיראות כהים ומעט אטומים, כמו 'עיסה' או שמן על פני המים. בשלב זה, השכבה עדיין גמישה מאוד.</li>
        <li><strong>Nilas (נילאס):</strong> אם הים שקט (רוח חלשה מאוד), עיסת הקרח יכולה לקפוא במהירות לשכבה אחידה, דקה ואלסטית. נילאס נראה בדרך כלל חלק וכהה יותר מקרח עבה. זהו מסלול היווצרות קרח ימי שונה מזה המוביל לפנקייק.</li>
        <li><strong>Pancake Ice (קרח פנקייק):</strong> כאן נכנסים לתמונה הגלים והרוחות. כאשר עיסת הקרח נוכחת בים שיש בו תנועת גלים בינונית, הגלים מונעים מהשכבה לקפוא למשטח חלק. במקום זאת, הגלים מרסקים את עיסת הקרח לגושים וגורמים לגושים הללו להתנגש זה בזה שוב ושוב.</li>
        <li><strong>Young Ice / First-Year Ice (קרח צעיר / קרח בן שנה):</strong> אם קצב יצירת הקרח נמשך והגלים נרגעים, דיסקיות הפנקייק ימשיכו להתנגש, להידחס, ובסופו של דבר יקפאו יחד ויתחברו ליצירת משטחי קרח גדולים וחזקים יותר, שיהפכו לקרח צעיר ולאחר מכן לקרח בן שנה אם ישרוד את הקיץ.</li>
    </ol>
    </p>

    <p><strong>הקסם של הפנקייק: איך נוצרת הצורה העגולה?</strong><br>
    הצורה העגולה והשוליים המוגבהים הם התוצאה הישירה של ההתנגשויות החוזרות ונשנות. דמיינו את עיסת הקרח מתגבשת לגושים רכים. הגלים מטלטלים את הגושים הללו ודוחפים אותם זה אל זה. בכל התנגשות, הקצוות הרכים של הגושים נמעכים, נדחסים, ומצטברים כלפי מעלה בשוליים. תהליך זה מתרחש מכל הצדדים, "מפסל" בהדרגה את הגושים לצורות עגולות יותר ויותר ובונה את השוליים האופייניים לפנקייק. ככל שהרוח חזקה יותר (ועוצמת הגלים גדולה יותר), כך ההתנגשויות תכופות ואנרגטיות יותר, והשוליים יהיו מודגשים יותר.</p>

    <p><strong>חשיבות הפנקייק:</strong><br>
    קרח פנקייק הוא לא רק יפה, אלא גם חיוני במחזור חיי הקרח הימי באזורים גליים. הוא מאפשר לקרח להיווצר ולהתפתח גם כשהים אינו שקט לחלוטין, ומשמש אבן בניין בדרך ליצירת משטחי קרח גדולים ויציבים יותר המכסים שטחים עצומים באוקיינוסים הקפואים.</p>
</div>

<style>
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        color: #333;
        background-color: #f4f7f6;
        margin: 0;
        padding: 20px;
    }

    h1, h2 {
        color: #0056b3; /* Deep blue */
        text-align: center;
        margin-bottom: 15px;
    }

    h1 {
        border-bottom: 2px solid #007bff; /* Brighter blue */
        padding-bottom: 10px;
        margin-top: 0;
    }

    #simulation-container {
        margin: 30px auto;
        padding: 25px;
        border: 1px solid #cce0f4; /* Light blue border */
        border-radius: 12px;
        background-color: #e9f5ff; /* Very light blue background */
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        text-align: center;
        max-width: 750px;
    }

    #simulation-container h2 {
        color: #004085; /* Darker blue */
        margin-top: 0;
        margin-bottom: 20px;
    }

    .controls {
        margin-bottom: 25px;
        display: flex;
        flex-direction: column; /* Stack controls on small screens */
        align-items: center;
        gap: 15px; /* Space between control groups */
    }

    .control-group {
        display: flex;
        flex-direction: column; /* Stack label and slider */
        align-items: flex-start; /* Align label left */
        gap: 5px;
        width: 100%;
        max-width: 300px; /* Limit slider width */
    }

    .controls label {
        font-weight: bold;
        color: #004085;
        font-size: 0.95em;
    }

    .controls input[type="range"] {
        width: 100%;
        -webkit-appearance: none;
        appearance: none;
        height: 8px;
        background: #b0d7ff; /* Light blue track */
        outline: none;
        opacity: 0.9;
        transition: opacity .2s;
        border-radius: 4px;
    }

    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #007bff; /* Bright blue thumb */
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0 0 4px rgba(0, 0, 0, 0.3);
    }

    .controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0 0 4px rgba(0, 0, 0, 0.3);
    }

    .controls span {
        font-weight: normal;
        color: #004085;
        min-width: 40px; /* Give value span some space */
        text-align: right;
    }

    .control-group {
        display: flex;
        flex-direction: row; /* Arrange in a row */
        align-items: center; /* Center vertically */
        gap: 10px; /* Space between elements */
        width: 100%;
        max-width: 450px; /* Wider limit for horizontal layout */
        justify-content: center; /* Center the group */
    }


    #resetSimulation {
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 5px;
        background-color: #ff4d4d; /* Red for reset */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    #resetSimulation:hover {
        background-color: #ff1a1a; /* Darker red on hover */
    }

    #resetSimulation:active {
        transform: scale(0.98); /* Press effect */
    }


    #iceCanvas {
        display: block;
        margin: 0 auto 20px auto;
        border: 2px solid #b0d7ff; /* Matching border */
        border-radius: 8px; /* Rounded corners */
        background: linear-gradient(to bottom, #e0f7fa 0%, #b2ebf2 100%); /* Subtle water gradient */
        box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.1); /* Inner shadow for depth */
    }

    .condition-display {
        text-align: center;
        font-weight: bold;
        color: #004085;
        min-height: 1.5em; /* Prevent layout shift */
    }

    .toggle-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #007bff;
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .toggle-button:hover {
        background-color: #0056b3;
    }

    .toggle-button:active {
        transform: scale(0.98);
    }

    .explanation-section {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid #cce0f4;
        border-radius: 12px;
        background-color: #e9f5ff;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }

    .explanation-section h2 {
         color: #004085;
        border-bottom: 2px solid #007bff;
        padding-bottom: 8px;
        margin-bottom: 20px;
    }

    .explanation-section p {
        margin-bottom: 18px;
        line-height: 1.7;
        color: #333;
    }

    .explanation-section strong {
        color: #004085;
    }

    .explanation-section ol {
        margin-left: 25px;
        padding-left: 0;
        list-style-type: decimal;
    }

    .explanation-section li {
        margin-bottom: 10px;
    }

    /* Responsive Adjustments */
    @media (max-width: 600px) {
        body {
            padding: 10px;
        }
        .controls {
            flex-direction: column;
            gap: 10px;
        }
         .control-group {
            flex-direction: column; /* Stack label, slider, and value */
            align-items: center;
            gap: 5px;
         }
         .control-group label {
             width: 100%;
             text-align: center;
         }
          .control-group span {
             width: 100%;
             text-align: center;
             margin-top: -5px; /* Pull value closer to slider */
          }
        #simulation-container, .explanation-section {
            padding: 15px;
        }
         .toggle-button {
             padding: 10px 20px;
             font-size: 1em;
         }
    }

</style>

<script>
    const canvas = document.getElementById('iceCanvas');
    const ctx = canvas.getContext('2d');
    const iceRateSlider = document.getElementById('iceRate');
    const windStrengthSlider = document.getElementById('windStrength');
    const iceRateValueSpan = document.getElementById('iceRateValue');
    const windStrengthValueSpan = document.getElementById('windStrengthValue');
    const resetBtn = document.getElementById('resetSimulation');
    const currentConditionSpan = document.getElementById('currentCondition');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationBtn = document.getElementById('toggleExplanation');

    let iceRate = parseInt(iceRateSlider.value);
    let windStrength = parseInt(windStrengthSlider.value);
    let particles = []; // Represents frazil ice / grease ice blobs
    let pancakes = []; // Represents pancake ice discs
    let nilasCoverage = 0; // Represents coverage for smooth ice (Nilas)
    let animationFrameId = null; // To control the animation loop

    const particleMinSize = 1; // Frazil ice min size
    const particleMaxSize = 5; // Frazil ice max size before potentially clumping
    const pancakeMinRadius = 10; // Min size for a new pancake
    const pancakeMaxRadius = 40; // Max initial size for a pancake
    const maxParticles = 500; // Limit total frazil/grease particles
    const maxPancakes = 150; // Limit total pancakes
    const collisionForceFactor = 0.1; // How much collision affects speed
    const edgeGrowthFactor = 0.1; // How much edge grows per collision

    // Update displayed values and condition on slider input
    iceRateSlider.oninput = function() {
        iceRate = parseInt(this.value);
        iceRateValueSpan.textContent = this.value + '%';
        updateConditionDisplay();
    }

    windStrengthSlider.oninput = function() {
        windStrength = parseInt(this.value);
        windStrengthValueSpan.textContent = this.value + '%';
        updateConditionDisplay();
    }

    // Reset simulation state
    resetBtn.onclick = function() {
        cancelAnimationFrame(animationFrameId); // Stop current animation
        particles = [];
        pancakes = [];
        nilasCoverage = 0;
        // Redraw initial state (water)
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        drawBackground(0); // Draw water with no wave effect
        updateConditionDisplay();
        // Restart animation loop
        animationFrameId = requestAnimationFrame(updateSimulation);
    }

    // Toggle explanation visibility
    toggleExplanationBtn.onclick = function() {
        if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
            explanationDiv.style.display = 'block';
            toggleExplanationBtn.textContent = 'הסתר הסבר מדעי';
            explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' }); // Scroll to explanation
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationBtn.textContent = 'הבנתם איך זה עובד? לחצו כאן להסבר המלא';
        }
    }

    // Update condition text based on sliders
    function updateConditionDisplay() {
        const currentIceRateNorm = iceRate / 100;
        const currentWindNorm = windStrength / 100;
        let conditionText = "";

        if (currentIceRateNorm < 0.15) {
            conditionText = "תנאים נוכחיים: המים מתקררים, מעט גבישי קרח ראשוני...";
        } else if (currentIceRateNorm >= 0.15 && currentWindNorm < 0.25) {
             conditionText = "תנאים נוכחיים: מים קפואים מהר, ים שקט... היווצרות נילאס (שכבת קרח חלקה)...";
        } else if (currentIceRateNorm >= 0.15 && currentWindNorm >= 0.25 && currentWindNorm < 0.6) {
             conditionText = "תנאים נוכחיים: מים קפואים, ים גלי... היווצרות עיסת קרח וגושים ראשונים...";
        } else if (currentIceRateNorm >= 0.4 && currentWindNorm >= 0.4) {
             conditionText = "תנאים נוכחיים: מים קפואים מהר, ים גלי! היווצרות קרח פנקייק!";
        } else if (currentIceRateNorm >= 0.15 && currentWindNorm >= 0.6) {
             conditionText = "תנאים נוכחיים: מים קפואים, ים סוער... גלים שוברים את הקרח הראשוני...";
        }
         else {
             conditionText = "תנאים נוכחיים: המים מתחילים להתקרר...";
        }
        currentConditionSpan.textContent = conditionText;
    }

    // Draw the background water with subtle effect
    function drawBackground(windNorm) {
         const gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
         gradient.addColorStop(0, '#e0f7fa'); // Top light blue
         gradient.addColorStop(1, '#b2ebf2'); // Bottom slightly darker blue
         ctx.fillStyle = gradient;
         ctx.fillRect(0, 0, canvas.width, canvas.height);

         // Add subtle wavy overlay based on wind
         if (windNorm > 0.3) {
             const waveOpacity = Math.min(windNorm * 0.3, 0.4); // Max opacity 0.4
             ctx.fillStyle = `rgba(173, 216, 230, ${waveOpacity})`; // Light blue overlay
             ctx.fillRect(0, 0, canvas.width, canvas.height);
         }
    }


    // Create a new particle (frazil/grease ice)
    function createParticle() {
        if (particles.length < maxParticles) {
            particles.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                size: particleMinSize, // Start small
                vx: (Math.random() - 0.5) * 0.5, // Base velocity
                vy: (Math.random() - 0.5) * 0.5,
                color: 'rgba(255, 255, 255, 0.8)', // White/translucent
                isGrease: false // Is it a clumped grease ice blob?
            });
        }
    }

     // Create a new pancake
     function createPancake(x, y, radius) {
         if (pancakes.length < maxPancakes) {
             pancakes.push({
                 x: x,
                 y: y,
                 radius: Math.max(radius, pancakeMinRadius), // Ensure min size
                 edgeThickness: 2, // Starting edge thickness
                 vx: (Math.random() - 0.5) * (windStrength / 50), // Movement based on wind
                 vy: (Math.random() - 0.5) * (windStrength / 50),
                 color: 'rgba(240, 248, 255, 0.9)', // Slightly less translucent white
                 edgeColor: 'rgba(173, 216, 230, 0.9)', // Light blue edge
                 id: Date.now() + Math.random() // Unique ID for potential future features
             });
         }
     }

    // Update and draw particles (Grease Ice)
    function updateParticles(windNorm) {
         // Generate new particles based on ice rate
         const particleCreationRate = iceRate / 200; // Adjusted rate
         if (Math.random() < particleCreationRate && particles.length < maxParticles) {
             createParticle();
         }

        for (let i = particles.length - 1; i >= 0; i--) {
            const p = particles[i];

            // Apply wind influence to movement
            p.vx += (Math.random() - 0.5) * windNorm * 0.2;
            p.vy += (Math.random() - 0.5) * windNorm * 0.2;
            // Add some drag
            p.vx *= 0.98;
            p.vy *= 0.98;

            p.x += p.vx;
            p.y += p.vy;

            // Boundary check (wrap around or remove) - remove is simpler
             if (p.x < -particleMaxSize*2 || p.x > canvas.width + particleMaxSize*2 || p.y < -particleMaxSize*2 || p.y > canvas.height + particleMaxSize*2) {
                 particles.splice(i, 1); // Remove if out of bounds
                 continue;
             }

            // Particle coalescence (form grease ice blobs)
            for (let j = i + 1; j < particles.length; j++) {
                const p2 = particles[j];
                const dx = p.x - p2.x;
                const dy = p.y - p2.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                const collideDist = p.size + p2.size;

                if (distance < collideDist * 0.8) { // If particles are close
                    // Merge them into a larger blob (p)
                    const totalSize = p.size + p2.size;
                    p.x = (p.x * p.size + p2.x * p2.size) / totalSize; // Weighted average position
                    p.y = (p.y * p.size + p2.y * p2.size) / totalSize; // Weighted average position
                    p.vx = (p.vx * p.size + p2.vx * p2.size) / totalSize; // Weighted average velocity
                    p.vy = (p.vy * p.size + p2.vy * p2.size) / totalSize;
                    p.size = Math.min(totalSize * 0.8, particleMaxSize * 3); // New size, limit growth slightly
                    p.isGrease = true; // It's now a grease blob

                    particles.splice(j, 1); // Remove merged particle
                    i--; // Adjust index

                     // If blob is large enough and wind is medium/high, potentially turn into a pancake
                     if (p.size > particleMaxSize * 1.5 && windNorm > 0.3 && pancakes.length < maxPancakes) {
                         createPancake(p.x, p.y, p.size * 2); // Convert blob size to initial pancake radius
                         particles.splice(i, 1); // Remove the blob
                         i--; // Adjust index
                         break; // Stop checking collisions for this blob in this frame
                     }
                     if (i < 0) break; // Handle edge case where i becomes -1
                }
            }

             // Draw particle (as a small blob)
             ctx.fillStyle = p.color;
             ctx.beginPath();
             ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
             ctx.fill();
        }
    }

    // Update and draw pancakes
    function updatePancakes(windNorm) {
         for (let i = pancakes.length - 1; i >= 0; i--) {
             const p = pancakes[i];

             // Apply wind influence to movement
             p.vx += (Math.random() - 0.5) * windNorm * 0.5;
             p.vy += (Math.random() - 0.5) * windNorm * 0.5;
              // Add drag (more drag than particles)
             p.vx *= 0.95;
             p.vy *= 0.95;


             p.x += p.vx;
             p.y += p.vy;

             // Bounce off boundaries (simple)
             if (p.x - p.radius < 0) { p.x = p.radius; p.vx = Math.abs(p.vx) * 0.7; p.edgeThickness = Math.min(p.edgeThickness + edgeGrowthFactor * windNorm * 5, 15); }
             if (p.x + p.radius > canvas.width) { p.x = canvas.width - p.radius; p.vx = -Math.abs(p.vx) * 0.7; p.edgeThickness = Math.min(p.edgeThickness + edgeGrowthFactor * windNorm * 5, 15); }
             if (p.y - p.radius < 0) { p.y = p.radius; p.vy = Math.abs(p.vy) * 0.7; p.edgeThickness = Math.min(p.edgeThickness + edgeGrowthFactor * windNorm * 5, 15); }
             if (p.y + p.radius > canvas.height) { p.y = canvas.height - p.radius; p.vy = -Math.abs(p.vy) * 0.7; p.edgeThickness = Math.min(p.edgeThickness + edgeGrowthFactor * windNorm * 5, 15); }


             // Draw pancake disc
             ctx.fillStyle = p.color;
             ctx.beginPath();
             ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
             ctx.fill();

              // Draw raised edge
             if (p.edgeThickness > 1) { // Only draw if edge exists
                 ctx.strokeStyle = p.edgeColor;
                 ctx.lineWidth = p.edgeThickness;
                 ctx.beginPath();
                 ctx.arc(p.x, p.y, p.radius - p.edgeThickness / 2, 0, Math.PI * 2);
                 ctx.stroke();
             }


             // Check for collisions with other pancakes
             for (let j = i + 1; j < pancakes.length; j++) {
                 const p2 = pancakes[j];
                 const dx = p.x - p2.x;
                 const dy = p.y - p2.y;
                 const distance = Math.sqrt(dx * dx + dy * dy);
                 const minDistance = p.radius + p2.radius;

                 if (distance < minDistance) {
                     // Collision detected!
                     // Simple inelastic collision response + separation
                     const nx = dx / distance; // Normal vector
                     const ny = dy / distance;

                     // Relative velocity
                     const rvx = p.vx - p2.vx;
                     const rvy = p.vy - p2.vy;

                     // Velocity along the normal
                     const velAlongNormal = rvx * nx + rvy * ny;

                     // Only resolve if velocities are separating
                     if (velAlongNormal < 0) {
                          // Impulse scalar (using simplified mass=radius)
                          const impulse = (-(1.5) * velAlongNormal) / (1/p.radius + 1/p2.radius); // 1.5 is a coefficient of restitution > 1 for slight bounce

                          // Apply impulse
                          const impulseX = impulse * nx;
                          const impulseY = impulse * ny;

                          p.vx += impulseX / p.radius * collisionForceFactor; // Scale impulse by mass approx
                          p.vy += impulseY / p.radius * collisionForceFactor;
                          p2.vx -= impulseX / p2.radius * collisionForceFactor;
                          p2.vy -= impulseY / p2.radius * collisionForceFactor;
                     }

                     // Separate overlapping pancakes (push them apart)
                     const overlap = minDistance - distance;
                     const adjustX = nx * (overlap / 2 + 0.5); // Add small buffer
                     const adjustY = ny * (overlap / 2 + 0.5);
                     p.x += adjustX;
                     p.y += adjustY;
                     p2.x -= adjustX;
                     p2.y -= adjustY;


                     // Increase edge thickness slightly on collision (simulating ice buildup)
                     if (windNorm > 0.3) { // Only build edges with wind
                         p.edgeThickness = Math.min(p.edgeThickness + edgeGrowthFactor * windNorm * 2, 15); // Max edge thickness 15
                         p2.edgeThickness = Math.min(p2.edgeThickness + edgeGrowthFactor * windNorm * 2, 15);
                     }
                     // Optional: chance to merge if wind is low AND pancakes are large/slow
                     if (windNorm < 0.2 && distance < minDistance * 0.5 && (p.radius > pancakeMaxRadius*0.8 || p2.radius > pancakeMaxRadius*0.8) && pancakes.length > 2) {
                          // Basic merge: p absorbs p2
                          p.x = (p.x + p2.x) / 2;
                          p.y = (p.y + p2.y) / 2;
                          p.radius = Math.min(Math.sqrt(p.radius*p.radius + p2.radius*p2.radius), pancakeMaxRadius*1.5); // Merge areas, limit size
                          p.edgeThickness = Math.max(p.edgeThickness, p2.edgeThickness) + edgeGrowthFactor * 5; // Keep larger edge and add more
                          p.vx = (p.vx + p2.vx) / 2;
                          p.vy = (p.vy + p2.vy) / 2;
                          pancakes.splice(j, 1);
                          i--; // Adjust index
                           if (i < 0) break;
                      }
                 }
             }
         }
     }

     // Simulate Nilas formation
     function updateNilas(iceRateNorm, windNorm) {
         if (iceRateNorm > 0.15 && windNorm < 0.25) {
             nilasCoverage = Math.min(nilasCoverage + iceRateNorm * 0.005, 1); // Gradually increase coverage
             const coverageAlpha = nilasCoverage * 0.9; // Max opacity
             ctx.fillStyle = `rgba(240, 248, 255, ${coverageAlpha})`; // Off-white/light blue for Nilas
             ctx.fillRect(0, 0, canvas.width, canvas.height);

             // Optional: Draw a subtle border or texture for the sheet
             if (nilasCoverage > 0.2) {
                 ctx.strokeStyle = `rgba(173, 216, 230, ${coverageAlpha * 0.5})`;
                 ctx.lineWidth = 2 + nilasCoverage * 5; // Thickness increases with coverage
                 ctx.strokeRect(0, 0, canvas.width, canvas.height);
             }

         } else {
             nilasCoverage = Math.max(nilasCoverage - 0.01, 0); // Gradually decrease coverage
             if (nilasCoverage > 0) { // Still draw while receding
                 const coverageAlpha = nilasCoverage * 0.9;
                 ctx.fillStyle = `rgba(240, 248, 255, ${coverageAlpha})`;
                 ctx.fillRect(0, 0, canvas.width, canvas.height);
                  if (nilasCoverage > 0.05) {
                     ctx.strokeStyle = `rgba(173, 216, 230, ${coverageAlpha * 0.5})`;
                     ctx.lineWidth = 2 + nilasCoverage * 5;
                     ctx.strokeRect(0, 0, canvas.width, canvas.height);
                 }
             }
         }
     }


    // Main simulation loop
    function updateSimulation() {
        // Normalize slider values
        const currentIceRateNorm = iceRate / 100;
        const currentWindNorm = windStrength / 100;

        // Clear canvas and draw background
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        drawBackground(currentWindNorm);

        // --- Simulation Logic ---

        // Nilas formation takes priority in calm conditions
        if (currentWindNorm < 0.25 && currentIceRateNorm > 0.15) {
             updateNilas(currentIceRateNorm, currentWindNorm);
             // If Nilas is forming, clear particles/pancakes gradually? Or just don't update them?
             // Let's let them coexist for now, maybe fade them out as Nilas grows?
             // For simplicity, maybe just don't spawn new pancakes/particles when Nilas takes over.
             // And particles/pancakes that exist move less in low wind.
             if (nilasCoverage > 0.8) {
                 particles = []; // Clear particles once Nilas is dominant
                 pancakes = pancakes.filter(pancake => pancake.radius > 25); // Keep larger pancakes briefly
             } else {
                  updateParticles(currentWindNorm); // Particles exist alongside forming Nilas
                  updatePancakes(currentWindNorm); // Pancakes exist alongside forming Nilas
             }

        } else { // Windy conditions: Frazil -> Grease -> Pancake
             nilasCoverage = Math.max(nilasCoverage - 0.02, 0); // Recede Nilas if wind picks up
              if (nilasCoverage > 0) { // Draw receding Nilas
                 updateNilas(currentIceRateNorm, currentWindNorm);
             }
             updateParticles(currentWindNorm);
             updatePancakes(currentWindNorm);
        }


        // Loop the simulation
        animationFrameId = requestAnimationFrame(updateSimulation);
    }

    // Initial setup
    explanationDiv.style.display = 'none'; // Hide explanation initially
    updateConditionDisplay(); // Set initial condition text
    animationFrameId = requestAnimationFrame(updateSimulation); // Start the simulation loop

</script>