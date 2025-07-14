---
title: "חשיפת הקסם: סימולציות דיגיטליות של מים ולהבות"
english_slug: animation-magic-water-or-fire-simulation
category: "מדעי המחשב"
tags: [אנימציה, גרפיקה ממוחשבת, סימולציה, פיזיקה חישובית, אפקטים ויזואליים, פיתוח משחקים]
---
# חשיפת הקסם: סימולציות דיגיטליות של מים ולהבות

האם אי פעם עצרתם לרגע להתפעל מהמראה הריאליסטי של מים זורמים במפל בסרט פנטזיה, או מהתנועה הכאוטית והמהפנטת של אש במשחק וידאו? אלו לא קסמים שקורים מעצמם. מאחורי האפקטים הוויזואליים המדהימים הללו מסתתר עולם מרתק של מדע, מתמטיקה וקוד - עולם של **סימולציות פיזיות**.

האפליקציה האינטראקטיבית שלפניכם היא שער ראשון להבנת העקרונות הללו. היא מאפשרת לכם להתנסות בכוחות שמניעים חלקיקים דיגיטליים, ולראות כיצד שינוי פרמטרים בודדים יכול להפוך טפטוף עדין למפל שוצף, או גיצים בודדים ללהבה אדירה. בואו לשחק, לשנות, ולגלות איך נוצר הקסם!

<div class="simulation-container">
    <div class="controls">
        <div class="mode-selector">
             <label class="mode-label">
                <input type="radio" name="simulationMode" value="water" checked> מים
            </label>
            <label class="mode-label">
                <input type="radio" name="simulationMode" value="fire"> אש
            </label>
        </div>


        <div id="waterControls" class="param-group">
            <h3>שליטה על המים</h3>
            <div class="param-row">
                <label for="waterEmissionRate">קצב זרימה:</label>
                <input type="range" id="waterEmissionRate" min="1" max="50" value="15">
                <span class="param-value"></span>
            </div>
            <div class="param-row">
                <label for="waterGravity">כוח משיכה:</label>
                <input type="range" id="waterGravity" min="0" max="20" value="8" step="0.1">
                 <span class="param-value"></span>
            </div>
             <div class="param-row">
                <label for="waterViscosity">צמיגות:</label>
                <input type="range" id="waterViscosity" min="0" max="10" value="3" step="0.1">
                 <span class="param-value"></span>
            </div>
             <div class="param-row">
                <label for="waterCollision">"קפיציות" התנגשות:</label>
                <input type="range" id="waterCollision" min="0" max="1" value="0.7" step="0.01">
                 <span class="param-value"></span>
            </div>
        </div>

        <div id="fireControls" class="param-group" style="display: none;">
            <h3>שליטה על האש</h3>
             <div class="param-row">
                <label for="fireEmissionRate">קצב פליטה:</label>
                <input type="range" id="fireEmissionRate" min="1" max="50" value="20">
                 <span class="param-value"></span>
            </div>
            <div class="param-row">
                <label for="fireInitialTemp">טמפרטורה מקורית:</label>
                <input type="range" id="fireInitialTemp" min="1" max="20" value="12" step="0.1">
                 <span class="param-value"></span>
            </div>
             <div class="param-row">
                <label for="fireAirDensity">צפיפות אוויר (לציפה):</label>
                <input type="range" id="fireAirDensity" min="0.1" max="5" value="1.5" step="0.1">
                 <span class="param-value"></span>
            </div>
            <div class="param-row">
                <label for="fireWindForce">כוח רוח:</label>
                <input type="range" id="fireWindForce" min="-10" max="10" value="0" step="0.1">
                 <span class="param-value"></span>
            </div>
            <div class="param-row">
                <label for="fireDecay">קצב דעיכה (חיים):</label>
                <input type="range" id="fireDecay" min="0.95" max="0.999" value="0.985" step="0.001">
                 <span class="param-value"></span>
            </div>
        </div>
    </div>

    <canvas id="simulationCanvas"></canvas>
</div>

<button id="toggleExplanation">הצג את הסודות מאחורי הקסם</button>

<div id="explanation" style="display: none;">
    <h2>מבוא: קסם הסימולציה הפיזית - לא רק בשביל הכיף!</h2>
    <p>סימולציה פיזית באנימציה היא בעצם בניית מודל דיגיטלי שמחקֶה התנהגות של חומרים או כוחות מהעולם האמיתי, אבל בתוך המחשב. במקום לצייר או לפסל כל רגע בתנועה המורכבת של עשן מתפשט, מים ניתזים, או בד מתנפנף ברוח – אנחנו אומרים למחשב: "הנה החוקים, הנה הכוחות, תחשב לבד איך זה ייראה". זה חוסך אינסוף שעות עבודה ידנית ומאפשר ליצור אפקטים שנראים ומרגישים *אמיתיים*, כי הם באמת מבוססים על עקרונות פיזיקליים. זה כלי קריטי לא רק בסרטים ומשחקים, אלא גם בהדמיות הנדסיות ומדעיות.</p>

    <h2>צלילה לתוך המים: עקרונות סימולציית נוזלים</h2>
    <p>כשמדמים מים או נוזלים אחרים, המטרה היא לגרום להם להתנהג כמו... מים! הם צריכים לזרום, להתפשט, להתיז, ולהיות מושפעים מכבידה וממכשולים. אחת הדרכים הפופולריות לעשות את זה (שעליה מתבסס במידה רבה המודל הבסיסי כאן) היא באמצעות **מערכות חלקיקים (Particle Systems)**. כל "טיפה" היא חלקיק קטן שיש לו תכונות כמו מיקום, מהירות, ולפעמים גם לחץ או טמפרטורה. החלקיקים האלה מושפעים מכוחות חיצוניים וגם מאינטראקציות עם חלקיקים שכנים ועם גבולות המרחב (כמו הקרקע או קירות).
    <ul>
        <li>**כוח משיכה (Gravity):** הכוח הבסיסי ביותר שמושך את חלקיקי המים כלפי מטה. ככל שהמספר גדול יותר בסימולטור, המים יזרמו מהר יותר ו"ייפלו" בעוצמה רבה יותר.</li>
        <li>**צמיגות (Viscosity):** תחשבו על ההבדל בין מים לדבש. צמיגות היא מדד להתנגדות של נוזל לזרימה. בסימולציה שלנו, צמיגות גבוהה יותר מאטה את תנועת החלקיקים ומקטינה את הנטייה שלהם להתפזר, מה שיוצר מראה של נוזל "סמיך" יותר.</li>
        <li>**"קפיציות" התנגשות (Collision Factor):** כשחלקיק מים פוגע בקרקעית או בקירות, מה קורה? האם הוא פשוט עוצר, או ש"קופץ" מעט? פרמטר זה קובע כמה אנרגיה (מהירות) החלקיק ישמור אחרי התנגשות, ובעצם מדמה כמה ה"קפיצה" או הניתז יהיו חזקים. ערך 1 פירושו התנגשות "קפיצית" לחלוטין (לא מציאותי), וערך 0 פירושו עצירה מיידית.</li>
        <li>**קצב זרימה (Emission Rate):** פשוט - כמה חלקיקי מים חדשים נוצרים במקור הסימולציה (במקרה שלנו, בחלק העליון) בכל רגע נתון. זה משפיע על עובי וחוזק זרם המים.</li>
    </ul>
    שיטות מתקדמות יותר לסימולציית נוזלים כוללות פתרון משוואות מורכבות יותר (כמו נאוויה-סטוקס) על רשת (Grid-based) או שילוב של רשת וחלקיקים, אך מערכות חלקיקים מספקות הדגמה ויזואלית מצוינת לעקרונות הבסיסיים.</p>

    <h2>עולים באש: עקרונות סימולציית אש ועשן</h2>
    <p>סימולציית אש מורכבת יותר מסימולציית מים כי היא כוללת לא רק תנועה (של גז חם ועשן) אלא גם שינויי טמפרטורה, התפשטות חום, ולרוב גם שינויים כימיים (בעירה). גם כאן, מערכות חלקיקים הן כלי נפוץ ויעיל. כל חלקיק יכול לייצג גוש זעיר של גז לוהט או עשן. התנהגות החלקיק (צבע, שקיפות, גודל, מהירות) משתנה עם הזמן כדי לדמות את תהליך הבעירה והתקררות/דעיכה.
    <ul>
        <li>**טמפרטורה מקורית (Initial Temperature):** טמפרטורה גבוהה יותר בגוש האש הראשוני פירושה שהגז החם יותר קל ביחס לאוויר הקר סביבו, ולכן חווה כוח ציפה חזק יותר ועולה מהר יותר. בסימולטור, זה בא לידי ביטוי במהירות התחלתית גבוהה יותר כלפי מעלה ובהשפעה על צבע ראשוני.</li>
        <li>**צפיפות אוויר (לציפה) (Air Density):** פרמטר זה משפיע על חוזק כוח הציפה. אוויר "פחות צפוף" (במובן ההדמיה כאן) מגביר את אפקט הציפה של הגז החם, וגורם ללהבה לעלות מהר יותר ולמעלה. אוויר "צפוף" יותר מדכא את הציפה והאש תהיה נמוכה יותר ופחות אנרגטית.</li>
         <li>**כוח רוח (Wind Force):** כוח חיצוני פשוט שדוחף את כל חלקיקי האש והעשן לכיוון מסוים (שמאלה או ימינה). זה מדמה זרם אוויר אמיתי.</li>
        <li>**קצב דעיכה (חיים) (Decay Rate):** חלקיקי אש לא חיים לנצח. הם מתקררים, הופכים לעשן, ולבסוף נעלמים. פרמטר הדעיכה קובע כמה מהר חלקיק מאבד את ה"חיים" שלו (שקשורים לשקיפות, צבע וגודל). ערך קרוב ל-1 (כמו 0.99) פירושו דעיכה איטית ו"חיים" ארוכים יותר לחלקיק, מה שיוצר להבה ועשן גדולים ומתפשטים יותר. ערך נמוך יותר פירושו שהחלקיקים נעלמים מהר, והאש קטנה וקצרה יותר.</li>
         <li>**קצב פליטה (Emission Rate):** בדומה למים, זהו מספר חלקיקי האש החדשים שנוצרים במקור (בתחתית) בכל רגע. משפיע על גודל הלהבה וצפיפות העשן.</li>
    </ul>
    השילוב של תנועת החלקיקים, שינויי הגודל, השקיפות, והצבע שלהם לאורך זמן הוא שיוצר את המראה הדינמי והיפה של האש והעשן בסימולציה.</p>

    <h2>הקשר בין הפרמטרים למראה הסופי</h2>
    <p>כפי שראיתם, כל סליידר משפיע ישירות על כוח או תכונה פיזית, ושינוי קטן בהם יכול לשנות דרמטית את התוצאה הוויזואלית. זה היופי והאתגר בסימולציה פיזית - למצוא את האיזון הנכון בין הפרמטרים כדי ליצור את האפקט הריאליסטי או האמנותי הרצוי. אמני VFX ובמאי אנימציה מבלים שעות רבות בכוונון עדין של הפרמטרים הללו בתוכנות מורכבות כדי להשיג את המראה המושלם לסצנה שלהם.</p>

    <h2>עוד אתגרים ויישומים</h2>
    <p>בניית סימולטורים ריאליסטיים באמת היא משימה שדורשת כוח חישוב אדיר (פתרון המשוואות למיליוני חלקיקים או תאי רשת בזמן אמת זה לא עניין פשוט!) והתמודדות עם אתגרים כמו יציבות הסימולציה (למנוע מהמודל "להתפרק" או להתנהג בצורה לא פיזית), לכידת פרטים עדינים (כמו רסס זעיר או מערבולות עשן), ואינטראקציה מורכבת של הסימולציה עם עצמים אחרים בסצנה. למרות האתגרים, התוצאה שווה את זה, והטכניקות הללו נמצאות בליבת היצירה של רבים מהאפקטים הוויזואליים המרהיבים שאנו רואים סביבנו.</p>

</div>

<script>
    const canvas = document.getElementById('simulationCanvas');
    const ctx = canvas.getContext('2d');
    const waterControls = document.getElementById('waterControls');
    const fireControls = document.getElementById('fireControls');
    const modeSelectors = document.querySelectorAll('input[name="simulationMode"]');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');
    const paramValueSpans = document.querySelectorAll('.param-value');


    let simulationMode = 'water'; // 'water' or 'fire'
    let particles = [];
    const baseParticleSize = 4; // Slightly larger default size
    const maxParticles = 2500; // Increased particle limit for better density

    // Parameters (default values matching sliders)
    let params = {
        water: {
            emissionRate: 15,
            gravity: 0.4, // Adjusted scale for visual feel
            viscosity: 0.03, // Adjusted scale
            collisionFactor: 0.7 // Adjusted scale for visual feel
        },
        fire: {
            emissionRate: 20,
            initialTemp: 1.2, // Adjusted scale
            airDensity: 1.5, // Adjusted scale
            windForce: 0, // Adjusted scale
            decayRate: 0.985 // Adjusted scale
        }
    };

    // Get slider references and add event listeners
    const waterSliders = {
        emissionRate: document.getElementById('waterEmissionRate'),
        gravity: document.getElementById('waterGravity'),
        viscosity: document.getElementById('waterViscosity'),
        collisionFactor: document.getElementById('waterCollision')
    };
    const fireSliders = {
        emissionRate: document.getElementById('fireEmissionRate'),
        initialTemp: document.getElementById('fireInitialTemp'),
        airDensity: document.getElementById('fireAirDensity'),
        windForce: document.getElementById('fireWindForce'),
        decayRate: document.getElementById('fireDecay')
    };

     // Map sliders to their parameter names for easy access
    const slidersMap = {
        water: waterSliders,
        fire: fireSliders
    };

    // Update params from sliders and display current values
    function updateParams() {
        const currentParams = params[simulationMode];
        const currentSliders = slidersMap[simulationMode];

        for (const key in currentSliders) {
            const slider = currentSliders[key];
             // Apply scaling specific to each parameter/mode for better control feel
            let value = parseFloat(slider.value);
            if (simulationMode === 'water') {
                 if (key === 'gravity') value *= 0.05; // Fine tune gravity scale
                 if (key === 'viscosity') value *= 0.005; // Fine tune viscosity scale
                 // Collision factor is used directly
            } else { // fire
                 if (key === 'initialTemp') value *= 0.1; // Fine tune initial velocity from temp
                 if (key === 'airDensity') value *= 0.5; // Fine tune buoyancy force from density
                 if (key === 'windForce') value *= 0.1; // Fine tune wind strength
                 // Decay rate is used directly
            }
             currentParams[key] = key === 'emissionRate' ? parseInt(slider.value) : value;


             // Update the visible value next to the slider
             const valueSpan = slider.parentElement.querySelector('.param-value');
             if (valueSpan) {
                 // Format decay rate differently (more decimal places)
                 valueSpan.textContent = key === 'decayRate' ? currentParams[key].toFixed(3) : currentParams[key].toFixed(1);
             }
        }
    }

    // Particle class - Enhanced
    class Particle {
        constructor(x, y, mode) {
            this.x = x;
            this.y = y;
            this.mode = mode;
            this.alpha = 1; // Opacity
            this.initialSize = baseParticleSize + Math.random() * 2; // Vary size slightly
            this.size = this.initialSize;

            if (mode === 'water') {
                this.vx = (Math.random() - 0.5) * 0.5; // Very slight initial horizontal
                this.vy = Math.random() * -1 - 1; // Initial upward/neutral velocity
                this.color = 'rgba(50, 150, 255, 1)'; // Base water color
                this.lifespan = Infinity; // Water particles don't naturally die
                this.isSplashing = false; // Flag for splash effect
                this.splashCounter = 0;
            } else { // fire
                // Initial velocity based on temp and slight randomness
                this.vx = (Math.random() - 0.5) * 0.5 + params.fire.windForce; // Base wind + random horizontal
                this.vy = -Math.random() * params.fire.initialTemp; // Upward velocity based on temp
                this.initialLifespan = 150 + Math.random() * 100; // Increased base lifespan
                this.lifespan = this.initialLifespan;
                this.color = `hsl(${20 + Math.random() * 20}, 100%, 60%)`; // Bright orange/yellow start
                this.isSmoke = false;
            }
        }

        update() {
            if (this.mode === 'water') {
                this.vy += params.water.gravity; // Apply gravity
                this.vx *= (1 - params.water.viscosity); // Apply viscosity/drag
                this.vy *= (1 - params.water.viscosity);

                this.x += this.vx;
                this.y += this.vy;

                // Basic Collision with bottom
                const groundY = canvas.height - 10; // Position of the ground
                if (this.y > groundY - this.size / 2) {
                    this.y = groundY - this.size / 2;
                    this.vy = -this.vy * params.water.collisionFactor * (0.8 + Math.random() * 0.4); // Bounce with damping & randomness
                    this.vx *= 0.7; // Slow down horizontal on bounce
                    // Add horizontal spread on impact - more pronounced with higher collision factor
                     this.vx += (Math.random() - 0.5) * this.vy * 0.1 * (params.water.collisionFactor + 0.5); // Spread scales with impact velocity and collision factor

                     // Trigger splash effect visually on impact
                     if (!this.isSplashing && this.vy < -1) { // Only splash if hitting downwards with some velocity
                         this.isSplashing = true;
                         this.splashCounter = 10; // Splash animation duration
                         // Optional: Change color temporarily or create small splash particles (more complex)
                     }
                }

                 // Basic Collision with sides (left and right "walls")
                 const wallWidth = 2; // Based on CSS border/line width
                 if (this.x < wallWidth + this.size / 2) {
                    this.x = wallWidth + this.size / 2;
                    this.vx = -this.vx * params.water.collisionFactor * 0.5; // Less bounce off sides
                 } else if (this.x > canvas.width - wallWidth - this.size / 2) {
                     this.x = canvas.width - wallWidth - this.size / 2;
                     this.vx = -this.vx * params.water.collisionFactor * 0.5; // Less bounce off sides
                 }

                 // Update splash effect
                 if (this.isSplashing) {
                     this.splashCounter--;
                     if (this.splashCounter <= 0) {
                         this.isSplashing = false;
                     }
                     // Maybe briefly increase size or change alpha during splash
                      this.alpha = this.splashCounter > 0 ? 0.7 + this.splashCounter * 0.03 : 1; // Flicker/brighten slightly
                 }


            } else { // fire
                 // Buoyancy force (pushes up)
                const buoyancy = -params.fire.airDensity * 0.8; // Adjust multiplier
                this.vy += buoyancy; // Apply buoyancy

                this.vx += params.fire.windForce * 0.05; // Apply continuous wind effect
                // Add some random "turbulence" - small per-frame variation
                 this.vx += (Math.random() - 0.5) * 0.2;
                 this.vy += (Math.random() - 0.5) * 0.2;


                this.x += this.vx;
                this.y += this.vy;

                this.lifespan *= params.fire.decayRate; // Decay lifespan

                // Update appearance based on lifespan/age
                const lifeRatio = this.lifespan / this.initialLifespan;

                if (lifeRatio > 0.5) { // Fire phase
                    this.alpha = Math.min(1, lifeRatio * 2); // Start fully opaque, fade slightly
                     const hue = 20 + lifeRatio * 20; // Orange (20) towards yellow (40)
                    const lightness = 40 + (1 - lifeRatio) * 30; // Brighter when young, slightly darker when older fire
                    this.color = `hsl(${hue}, 100%, ${lightness}%)`;
                    this.size = this.initialSize * (0.5 + lifeRatio * 0.5); // Shrink slightly with age
                    this.isSmoke = false;
                } else { // Smoke phase
                    this.isSmoke = true;
                    this.alpha = lifeRatio * 1.5; // Fade out as smoke
                    const grey = 20 + (1-lifeRatio) * 30; // Darker grey as it fades (20-50)
                     this.color = `hsl(0, 0%, ${grey}%)`; // Grey color
                    this.size = this.initialSize * (0.8 - lifeRatio * 0.4); // Smoke expands then shrinks
                }
                 this.size = Math.max(1, this.size); // Don't let size go below 1
            }
        }

        draw() {
             // Optional: Draw a subtle glow for fire particles
            if (this.mode === 'fire' && !this.isSmoke) {
                const glowAlpha = this.alpha * 0.5; // Glow is semi-transparent
                const glowSize = this.size * 1.5; // Glow is larger than particle
                ctx.globalAlpha = glowAlpha;
                ctx.fillStyle = `rgba(255, 150, 0, ${glowAlpha})`; // Orange glow
                 ctx.filter = `blur(${this.size/2}px)`; // Apply blur for glow effect
                ctx.beginPath();
                ctx.arc(this.x, this.y, glowSize, 0, Math.PI * 2);
                ctx.fill();
                ctx.filter = 'none'; // Reset blur
            }


            ctx.globalAlpha = this.alpha;
            ctx.fillStyle = this.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
            ctx.globalAlpha = 1; // Reset alpha
        }
    }

    function emitParticles() {
         let startX, startY;
         const variance = simulationMode === 'water' ? 15 : 25; // More variance for fire base
         const emissionPointX = canvas.width / 2 + (Math.random() - 0.5) * variance; // Add randomness around center
         const emissionPointY = simulationMode === 'water' ? 0 : canvas.height;


        for (let i = 0; i < params[simulationMode].emissionRate; i++) {
            if (particles.length < maxParticles) {
                particles.push(new Particle(emissionPointX, emissionPointY, simulationMode));
            }
        }
    }

    function update() {
        // Remove dead particles (only for fire, or water leaving screen)
        if (simulationMode === 'fire') {
             particles = particles.filter(p => p.lifespan > 1); // Keep particles until alpha fades
        } else { // Water
             // Remove water particles that are far off screen (e.g., bounced up high)
             particles = particles.filter(p => p.y < canvas.height * 1.5 && p.x > -50 && p.x < canvas.width + 50);
        }


        // Update particle positions and properties
        particles.forEach(p => p.update());

        // Emit new particles
        emitParticles();
    }

    function render() {
        // Clear canvas or draw semi-transparent background for trails
        if (simulationMode === 'fire') {
             ctx.fillStyle = 'rgba(0, 0, 0, 0.15)'; // Darker background, more pronounced trails
             ctx.fillRect(0, 0, canvas.width, canvas.height);
        } else {
             ctx.clearRect(0, 0, canvas.width, canvas.height);
        }

        // Draw ground/container for water
        if (simulationMode === 'water') {
            const groundHeight = 10;
            const wallWidth = 2;
            ctx.fillStyle = '#555'; // Darker ground
            ctx.fillRect(0, canvas.height - groundHeight, canvas.width, groundHeight);
             ctx.fillStyle = '#555'; // Darker walls
             ctx.fillRect(0, canvas.height * 0.8, wallWidth, canvas.height * 0.2 + groundHeight); // Left wall
             ctx.fillRect(canvas.width - wallWidth, canvas.height * 0.8, wallWidth, canvas.height * 0.2 + groundHeight); // Right wall
        }


        // Draw particles - Draw smoke first, then fire for layering
        if (simulationMode === 'fire') {
            const fireParticles = particles.filter(p => !p.isSmoke);
            const smokeParticles = particles.filter(p => p.isSmoke);
            smokeParticles.forEach(p => p.draw());
            fireParticles.forEach(p => p.draw());
        } else {
             particles.forEach(p => p.draw());
        }
    }

    function loop() {
        updateParams(); // Always update parameters from sliders
        update();
        render();
        requestAnimationFrame(loop);
    }

    // --- Event Listeners ---
    modeSelectors.forEach(selector => {
        selector.addEventListener('change', (event) => {
            simulationMode = event.target.value;
            if (simulationMode === 'water') {
                waterControls.style.display = 'block';
                fireControls.style.display = 'none';
                 canvas.style.backgroundColor = '#cceeff'; // Lighter background for water
                 particles = []; // Clear particles on mode switch
                 ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear any fire trails
            } else {
                waterControls.style.display = 'none';
                fireControls.style.display = 'block';
                 canvas.style.backgroundColor = '#000000'; // Black background for fire
                 particles = []; // Clear particles on mode switch
            }
             // Reset initial slider values visually when switching? Optional, keep for now.
             // Reset explanation button text
             toggleExplanationButton.textContent = 'הצג את הסודות מאחורי הקסם';
             explanationDiv.style.display = 'none';
        });
    });

    // Add listeners for slider changes
    Object.values(waterSliders).forEach(slider => slider.addEventListener('input', updateParams));
    Object.values(fireSliders).forEach(slider => slider.addEventListener('input', updateParams));


    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר את הסודות' : 'הצג את הסודות מאחורי הקסם';
    });

    // Initial setup
    canvas.width = 600; // Adjust size as needed
    canvas.height = 400;
    canvas.style.backgroundColor = '#cceeff'; // Default water background
    updateParams(); // Read initial slider values and display them
    loop(); // Start the animation loop

</script>

<style>
     /* Global Styles */
    body {
        font-family: 'Arial', sans-serif; /* Use a common, clean font */
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        background-color: #f4f7f6; /* Light grey background */
        color: #333;
        direction: rtl;
        text-align: right;
    }

    h1, h2, h3 {
        color: #1a2e45; /* Dark blue headings */
    }

     h1 {
         text-align: center;
         margin-bottom: 30px;
         color: #0056b3; /* Blue heading for main title */
     }

    p {
        margin-bottom: 15px;
    }

    ul {
        margin-bottom: 15px;
        padding-right: 20px; /* RTL list padding */
    }

    li {
        margin-bottom: 8px;
    }


    /* Simulation Container */
    .simulation-container {
        display: flex;
        flex-direction: row-reverse; /* Controls on the right in RTL */
        gap: 25px; /* Increased gap */
        margin-bottom: 30px; /* More space below */
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        background-color: #fff; /* White background for the container */
        padding: 20px;
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); /* Softer, larger shadow */
        align-items: flex-start; /* Align items to the top */
    }

     /* Controls Panel */
     .controls {
        flex: 0 0 280px; /* Wider controls panel */
        background-color: #eef2f7; /* Light blue background */
        padding: 20px;
        border-radius: 10px; /* Rounded corners */
        box-shadow: inset 0 1px 5px rgba(0,0,0,0.05); /* Subtle inner shadow */
        direction: rtl; /* Ensure controls are RTL */
        text-align: right;
    }

    .controls h3 {
        margin-top: 0;
        margin-bottom: 15px;
        color: #004085; /* Darker blue for section titles */
        border-bottom: 1px solid #b8daff; /* Light blue border */
        padding-bottom: 8px;
    }

     .mode-selector {
         margin-bottom: 20px;
         text-align: center;
     }

     .mode-label {
         margin: 0 15px;
         font-size: 1.1em;
         cursor: pointer;
         color: #0056b3;
     }

    .param-group {
        border-top: 1px solid #b8daff;
        padding-top: 15px;
    }

    .param-row { /* For individual parameter rows */
        margin-bottom: 18px; /* More space between rows */
    }

     .param-row label {
         display: block; /* Label above slider */
         margin-bottom: 6px; /* More space below label */
         font-weight: bold;
         font-size: 0.95em;
         color: #333;
     }

      .param-value {
          display: inline-block;
          margin-right: 10px; /* Space after label */
          font-size: 0.9em;
          color: #555;
          min-width: 30px; /* Reserve space to prevent layout shifts */
          text-align: left;
      }


     /* Slider Styling */
     .controls input[type="range"] {
         width: calc(100% - 40px); /* Adjust width to make space for value span */
         -webkit-appearance: none; /* Override default look */
         appearance: none;
         height: 10px; /* Thicker slider track */
         background: #dce4ec; /* Lighter track color */
         outline: none;
         opacity: 0.9; /* Slightly less opaque default */
         transition: opacity .2s ease-in-out;
         border-radius: 5px; /* Rounded track */
         margin: 0; /* Remove default margin */
         vertical-align: middle; /* Align with value span */
     }

     .controls input[type="range"]:hover {
         opacity: 1;
     }

     .controls input[type="range"]::-webkit-slider-thumb {
         -webkit-appearance: none;
         appearance: none;
         width: 20px; /* Larger thumb */
         height: 20px; /* Larger thumb */
         background: #007bff; /* Blue thumb */
         cursor: pointer;
         border-radius: 50%;
         border: 2px solid #0056b3; /* Darker blue border */
         transition: background .15s ease-in-out, border-color .15s ease-in-out;
         margin-top: -5px; /* Adjust to vertically center thumb on track */
     }

      .controls input[type="range"]::-moz-range-thumb {
         width: 20px;
         height: 20px;
         background: #007bff;
         cursor: pointer;
         border-radius: 50%;
          border: 2px solid #0056b3;
           transition: background .15s ease-in-out, border-color .15s ease-in-out;
      }

    .controls input[type="range"]::-webkit-slider-thumb:hover,
    .controls input[type="range"]::-moz-range-thumb:hover {
        background: #0056b3; /* Darker blue on hover */
        border-color: #004085;
    }

    /* Canvas */
    #simulationCanvas {
        border: 1px solid #aaa; /* Softer border */
        background-color: #cceeff; /* Default light blue for water */
        flex: 1; /* Canvas takes remaining space */
        min-width: 300px; /* Minimum size before wrapping */
        border-radius: 8px; /* Rounded corners for canvas */
        box-shadow: inset 0 1px 5px rgba(0,0,0,0.05); /* Subtle inner shadow */
    }

     /* Explanation Toggle Button */
    #toggleExplanation {
        display: block;
        margin: 20px auto;
        padding: 12px 25px; /* More padding */
        font-size: 1.05em;
        cursor: pointer;
        background-color: #007bff; /* Blue button */
        color: white;
        border: none;
        border-radius: 6px; /* Rounded button */
        transition: background-color 0.2s ease-in-out;
        box-shadow: 0 2px 5px rgba(0,123,255,0.3);
    }

    #toggleExplanation:hover {
        background-color: #0056b3; /* Darker blue on hover */
    }

    /* Explanation Section */
    #explanation {
        margin-top: 20px;
        padding: 20px; /* More padding */
        border: 1px solid #b8daff; /* Light blue border */
        border-radius: 8px; /* Rounded corners */
        background-color: #eef2f7; /* Light blue background */
        direction: rtl; /* Ensure explanation is RTL */
        text-align: right;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }

    #explanation h2 {
        color: #004085; /* Darker blue */
        margin-top: 0;
        margin-bottom: 15px;
        border-bottom: 1px dashed #b8daff; /* Dashed border */
        padding-bottom: 8px;
    }

    #explanation p {
        line-height: 1.7; /* Increased line height */
        margin-bottom: 18px;
    }

    #explanation ul {
        margin-bottom: 18px;
        padding-right: 25px; /* More RTL list padding */
    }

    #explanation li {
        margin-bottom: 10px;
    }

    #explanation strong {
        color: #0056b3; /* Highlight key terms */
    }

    /* Responsive Adjustments */
     @media (max-width: 768px) {
         .simulation-container {
             flex-direction: column; /* Stack controls above canvas */
         }
         .controls {
             flex: auto; /* Controls take full width */
             width: auto; /* Reset fixed width */
         }
         #simulationCanvas {
             flex: auto; /* Canvas takes full width */
         }
     }

</style>