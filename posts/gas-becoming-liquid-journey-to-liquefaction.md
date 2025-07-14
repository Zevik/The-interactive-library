---
title: "קסם ההתנזלות: מסע בין גז, נוזל ומעבר לכך"
english_slug: gas-becoming-liquid-journey-to-liquefaction
category: "מדעים מדויקים / פיזיקה"
tags: גזים, נוזלים, שינוי מצב צבירה, לחץ, טמפרטורה, התנזלות, נקודה קריטית, תרמודינמיקה, מצב סופר קריטי
---
# קסם ההתנזלות: מסע בין גז, נוזל ומעבר לכך

האם אי פעם תהיתם איך גז כמו הגפ"מ בבלון הביתי הופך פתאום לנוזל שניתן למזוג? ומה קורה אם מחממים אותו מאוד ולוחצים עליו בו זמנית? הצטרפו אלינו למסע אינטראקטיבי בעולם מצבי הצבירה, גלו את הסודות הכמוסים של התנזלות גזים, והכירו את הנקודה הקריטית שמשנה את כללי המשחק.

<div id="app-container">
    <h2>חקר מצבי צבירה: גז לנוזל</h2>
    <div id="simulation-area">
        <canvas id="gasCanvas" width="500" height="300"></canvas>
    </div>
    <div id="controls">
        <div class="control-group">
            <label for="pressure-slider">לחץ:</label>
            <input type="range" id="pressure-slider" min="1" max="200" value="50">
            <span id="pressure-value">50</span> יח'
        </div>

        <div class="control-group">
            <label for="temperature-slider">טמפרטורה:</label>
            <input type="range" id="temperature-slider" min="1" max="300" value="150">
            <span id="temperature-value">150</span> יח'
        </div>

        <div id="state-display">מצב נוכחי: <span id="current-state">גז</span></div>
        <div id="critical-info">
            <small>טמפרטורה קריטית (בסימולציה): <span id="critical-temp">200</span> יח', לחץ קריטי (בסימולציה): <span id="critical-pressure">100</span> יח'</small>
        </div>
    </div>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --secondary-color: #6c757d;
        --success-color: #28a745;
        --info-color: #17a2b8;
        --warning-color: #ffc107;
        --danger-color: #dc3545;
        --light-color: #f8f9fa;
        --dark-color: #343a40;
        --white-color: #fff;
        --gray-color: #e9ecef;
        --border-radius: 8px;
        --box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        --gas-color: #4db6ac; /* Teal */
        --liquid-color: #0277bd; /* Dark Blue */
        --supercritical-color: #8e24aa; /* Purple */
        --twophase-color: linear-gradient(to bottom, #4db6ac 50%, #0277bd 50%); /* Split */
    }

    #app-container {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        max-width: 700px;
        margin: 30px auto;
        padding: 25px;
        background-color: var(--white-color);
        border: 1px solid var(--gray-color);
        border-radius: var(--border-radius);
        box-shadow: var(--box-shadow);
        text-align: center;
        direction: rtl; /* Ensure RTL */
    }

    h2 {
        color: var(--dark-color);
        margin-top: 0;
        margin-bottom: 20px;
        font-size: 1.8em;
    }

    #simulation-area {
        margin-bottom: 20px;
        border-radius: var(--border-radius);
        overflow: hidden; /* Ensures canvas corners are rounded with container */
        box-shadow: inset 0 0 10px rgba(0,0,0,0.05); /* Subtle inner shadow */
    }

    canvas {
        display: block;
        margin: 0 auto;
        background: var(--light-color); /* Light background for the container */
    }

    #controls {
        margin-top: 20px;
        padding: 20px;
        background-color: var(--light-color);
        border-radius: var(--border-radius);
        text-align: right; /* Align labels right */
    }

    .control-group {
        margin-bottom: 15px;
        display: flex;
        align-items: center;
    }

    .control-group label {
        flex-basis: 120px; /* Fixed width for labels */
        margin-left: 15px; /* Space after label */
        font-weight: bold;
        color: var(--dark-color);
        text-align: right;
    }

    .control-group input[type="range"] {
        flex-grow: 1; /* Slider takes remaining space */
        height: 5px; /* Thinner track */
        -webkit-appearance: none;
        appearance: none;
        background: var(--gray-color);
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 5px;
    }

    .control-group input[type="range"]:hover {
        opacity: 1;
    }

    .control-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 18px;
        height: 18px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    .control-group input[type="range"]::-moz-range-thumb {
        width: 18px;
        height: 18px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    .control-group span {
        display: inline-block;
        width: 40px; /* Give value span enough space */
        text-align: left; /* Align value left */
        font-weight: bold;
        color: var(--primary-color);
    }

    #state-display {
        margin-top: 20px;
        font-size: 1.3em;
        font-weight: bold;
        text-align: center;
        padding: 12px;
        border-top: 1px solid var(--gray-color);
        color: var(--dark-color);
    }

    #state-display span {
         /* Styles updated by JS based on state */
        font-weight: bold;
    }

     #critical-info {
        margin-top: 10px;
        font-size: 0.8em;
        color: var(--secondary-color);
        text-align: center;
    }

    #explanation-button {
        display: block;
        margin: 30px auto 20px auto;
        padding: 12px 25px;
        font-size: 1em;
        cursor: pointer;
        background-color: var(--primary-color);
        color: var(--white-color);
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    #explanation-button:hover {
        background-color: #0056b3; /* Darker shade */
        transform: translateY(-1px); /* Subtle lift */
    }
     #explanation-button:active {
        transform: translateY(0);
    }

    #explanation-content {
        margin-top: 20px;
        padding: 25px;
        background-color: var(--white-color);
        border: 1px solid var(--gray-color);
        border-radius: var(--border-radius);
        text-align: justify;
        direction: rtl;
        opacity: 0; /* Start hidden and transparent */
        max-height: 0;
        overflow: hidden;
        transition: opacity 0.5s ease-in-out, max-height 0.5s ease-in-out;
    }
     #explanation-content.visible {
         opacity: 1;
         max-height: 2000px; /* Sufficiently large height for transition */
         transition: opacity 0.5s ease-in-out, max-height 0.8s ease-in-out;
     }


    #explanation-content h2, #explanation-content h3 {
        color: var(--primary-color);
        margin-top: 20px;
        margin-bottom: 12px;
        text-align: right;
    }
     #explanation-content h2:first-child, #explanation-content h3:first-child {
         margin-top: 0;
     }


    #explanation-content p {
        margin-bottom: 15px;
        line-height: 1.7;
        color: var(--dark-color);
    }

    #explanation-content ul {
        list-style: disc inside;
        padding-right: 20px; /* Adjust for RTL */
        margin-bottom: 15px;
    }

    #explanation-content li {
        margin-bottom: 8px;
        line-height: 1.6;
        color: var(--dark-color);
    }

    #explanation-content li strong {
        color: var(--dark-color);
    }

</style>

<button id="explanation-button">הצג/הסתר הסבר</button>

<div id="explanation-content">
    <h2>הצלילה לעומק: כך מתרחשת התנזלות</h2>

    <h3>מצבי הצבירה הבסיסיים: ריקוד החלקיקים</h3>
    <p>חומר קיים סביבנו במצבים שונים, שהמוכרים בהם הם מוצק, נוזל וגז. ההבדל המהותי ביניהם נעוץ באופן שבו החלקיקים הזעירים (אטומים או מולקולות) המרכיבים אותם מתנהגים ומתקשרים זה עם זה:</p>
    <ul>
        <li>**מוצק:** דמיינו חיילים במסדר נוקשה. החלקיקים צפופים ביותר, מסודרים במבנה קבוע ותלת-ממדי (סריג גבישי), ותנועתם מוגבלת לרעידות קטנות סביב מקומם הקבוע. למוצק צורה ונפח משלו שקשה לשנותם.</li>
        <li>**נוזל:** כמו קהל צפוף שמתנועע בחופשיות יחסית. החלקיקים עדיין קרובים מאוד, אך איבדו את המבנה המסודר. הם יכולים לנוע ולהחליק זה על פני זה, מה שמאפשר לנוזל לזרום ולקבל את צורת הכלי המכיל אותו, אך עדיין יש ביניהם כוחות משיכה המונעים מהם להתפזר לחלוטין. לנוזל נפח מוגדר אך צורה גמישה.</li>
        <li>**גז:** נחילי יתושים המתעופפים בחופשיות אינסופית. החלקיקים מרוחקים מאוד זה מזה, נעים במהירות אדירה ובאופן אקראי לחלוטין, ומלאים את כל הנפח שעומד לרשותם. כוחות המשיכה ביניהם חלשים מאוד, לכן לגז אין לא צורה ולא נפח קבועים.</li>
    </ul>

    <h3>האתגר: מעבר מגז לנוזל</h3>
    <p>התנזלות (או עיבוי) היא הקסם שבו גז הופך לנוזל. כדי לגרום לחלקיקי הגז הדוהרים להתקרב ולהיצמד זה לזה עד כדי יצירת פאזה צפופה יותר, עלינו לגבור על אנרגיית התנועה הגבוהה שלהם ועל המרחק הגדול ביניהם. שני מנופי הקסם העיקריים שעומדים לרשותנו הם:</p>
    <ul>
        <li>**קירור:** הורדת הטמפרטורה גורמת לחלקיקים להאט. כשהם נעים לאט יותר, כוחות המשיכה החלשים יחסית ביניהם הופכים למשמעותיים יותר ויכולים "ללכוד" אותם יחד וליצור את הפאזה הנוזלית.</li>
        <li>**הגברת לחץ:** הגברת הלחץ על גז פירושה הקטנת הנפח הזמין עבורו. זה מכריח את החלקיקים להתקרב זה לזה. כשהם קרובים יותר, כוחות המשיכה מתחזקים משמעותית והופכים להיות אפקטיביים מספיק כדי לגרום להתנזלות.</li>
    </ul>
     <p>שימו לב: קו הגבול בין פאזת הגז לפאזת הנוזל (כלומר, נקודת הרתיחה/עיבוי) אינו קבוע, אלא תלוי בלחץ. בלחץ גבוה יותר, נדרשת טמפרטורה גבוהה יותר כדי לשמור על החומר במצב גז, ולהפך.</p>


    <h3>הנקודה הקריטית: גבול עולם הנוזל והגז</h3>
    <p>לכל חומר יש "מחסום" טמפרטורה עליון מעליו לא ניתן להבחין עוד בהבדל הברור בין נוזל לגז. זוהי ה**טמפרטורה הקריטית** (T<sub>c</sub>). יחד איתה קיימת ה**לחץ הקריטי** (P<sub>c</sub>) - הלחץ הנדרש כדי להנזיל גז בדיוק בטמפרטורה הקריטית שלו. הנקודה המתאימה בגרף לחץ-טמפרטורה נקראת ה**נקודה הקריטית**.</p>
    <ul>
        <li>**מעל הטמפרטורה הקריטית (T > T<sub>c</sub>):** כאן מתרחש הקסם האמיתי! לא משנה כמה נגביר את הלחץ, לעולם לא נראה את הגז הופך באופן ברור לנוזל עם גבול הפרדה ברור. במקום זאת, החומר עובר למצב צבירה מסתורי וייחודי המכונה "נוזל סופר-קריטי".</li>
    </ul>

    <h3>הנוזל הסופר-קריטי: לא זה ולא זה</h3>
     <p>נוזל סופר-קריטי הוא מצב צבירה שמתקיים מעל הטמפרטורה הקריטית ובלחץ שמעל הלחץ הקריטי. הוא מתנהג כמו הכלאה מוזרה בין גז לנוזל:</p>
    <ul>
        <li>**כמו גז:** הוא ממלא את כל נפח הכלי הנתון (אין לו נפח משלו).</li>
        <li>**כמו נוזל:** הוא צפוף מאוד, בדומה לנוזל, ויכול להמיס חומרים אחרים בצורה יעילה ביותר.</li>
    </ul>
     <p>המעבר למצב סופר-קריטי מפאזת הגז הוא רציף - אין "קפיצה" או שינוי דרמטי פתאומי, כמו רתיחה או עיבוי רגיל. פשוט מגבירים את הצפיפות בהדרגה ככל שהלחץ עולה.</p>

    <h3>למה זה חשוב? שימושים בעולם האמיתי</h3>
    <p>הבנת תהליכי התנזלות והנקודה הקריטית אינה רק סקרנות מדעית, אלא בסיס לתעשיות וטכנולוגיות רבות:</p>
    <ul>
        <li>**גפ"מ (גז בישול/חימום):** מאוחסן ומובל כנוזל בלחץ במיכלים, מה שמאפשר לאחסן כמות גדולה של אנרגיה בנפח קטן.</li>
        <li>**קריוגניקה:** אחסון גזים כמו חמצן וחנקן נוזליים בטמפרטורות נמוכות במיוחד לשימושים תעשייתיים, רפואיים וחקר החלל.</li>
        <li>**קירור ומיזוג אוויר:** מבוססים על מחזורי אידוי ועיבוי של גז קירור כדי להעביר חום.</li>
        <li>**מיצוי בעזרת נוזל סופר-קריטי:** שיטה "ירוקה" להפרדת חומרים (למשל, קפאין מקפה) באמצעות נוזל סופר-קריטי (כמו דו-תחמוצת הפחמן) שחודר לחומר הגלם כמו גז אך ממס כמו נוזל.</li>
    </ul>
     <p>עכשיו, חזרו לסימולציה ושחקו עם הלחץ והטמפרטורה. נסו לזהות מתי החלקיקים מתחילים להתקרב ולהתנהג כמו נוזל, מתי הם מתפזרים כגז, ומתי הם נכנסים למצב הסופר-קריטי המיוחד!</p>
</div>

<script>
    const canvas = document.getElementById('gasCanvas');
    const ctx = canvas.getContext('2d');
    const pressureSlider = document.getElementById('pressure-slider');
    const temperatureSlider = document.getElementById('temperature-slider');
    const pressureValueSpan = document.getElementById('pressure-value');
    const temperatureValueSpan = document.getElementById('temperature-value');
    const currentStateSpan = document.getElementById('current-state');
    const explanationButton = document.getElementById('explanation-button');
    const explanationContent = document.getElementById('explanation-content');

    // Simulation Parameters
    const NUM_PARTICLES = 300;
    let particles = [];
    const PARTICLE_RADIUS = 3; // Pixels (slightly larger for better visibility)
    const CRITICAL_TEMP = 200; // Arbitrary simulation units
    const CRITICAL_PRESSURE = 100; // Arbitrary simulation units
    const MAX_SPEED_SCALE = 4; // Max speed based on temperature
    const BASE_PARTICLE_SPEED = 0.1; // Base speed at min temp (slower base)
    const COLLISION_DAMPING = 0.9; // Energy loss on collision
    const INTERACTION_RADIUS = PARTICLE_RADIUS * 8; // Radius for checking neighbors for forces
    const INTERACTION_RADIUS_SQ = INTERACTION_RADIUS * INTERACTION_RADIUS;
    const REPULSION_FORCE_SCALE = 0.1; // Strength of repulsion
    const ATTRACTION_FORCE_SCALE_LIQUID = 0.002; // Strength of attraction in liquid-like state
     const GRAVITY_EFFECT_LIQUID = 0.05; // Slight pull downwards in liquid state

    // Particle Representation
    class Particle {
        constructor(x, y) {
            this.x = x;
            this.y = y;
            // Initial velocity based on a moderate temperature
            this.vx = (Math.random() - 0.5) * (BASE_PARTICLE_SPEED + MAX_SPEED_SCALE * 0.5);
            this.vy = (Math.random() - 0.5) * (BASE_PARTICLE_SPEED + MAX_SPEED_SCALE * 0.5);
            this.color = 'var(--gas-color)';
        }

        update(dt, pressure, temperature, currentState, neighbors) {
            const speedScale = BASE_PARTICLE_SPEED + (temperature / 300) * MAX_SPEED_SCALE;

            // Apply forces (simplified LJ-like + conditional attraction/gravity)
            let forceX = 0;
            let forceY = 0;

            for (const other of neighbors) {
                const dx = other.x - this.x;
                const dy = other.y - this.y;
                const distSq = dx * dx + dy * dy;

                if (distSq < INTERACTION_RADIUS_SQ && distSq > 0.1) { // Avoid self and very small distances
                    const dist = Math.sqrt(distSq);
                    const inverseDist = 1 / dist;
                    const inverseDist6 = Math.pow(inverseDist, 6);
                    const inverseDist12 = inverseDist6 * inverseDist6;

                    // Lennard-Jones like potential force derivative ~ (1/r^13 - 1/r^7)
                    // Force is proportional to -(dV/dr) ~ (1/r^14 - 1/r^8)
                    // Let's simplify: strong repulsion close, weak attraction further out.
                    // Repulsion dominates when dist < ~1.12 * sigma (where sigma is particle size)
                    // Let's use a threshold based on PARTICLE_RADIUS
                    if (dist < PARTICLE_RADIUS * 2.5) { // Strong repulsion if getting too close
                         const repulsion = REPULSION_FORCE_SCALE * (1 / dist) * (1 / dist); // Strong inverse square repulsion
                         forceX -= repulsion * (dx / dist);
                         forceY -= repulsion * (dy / dist);
                    } else if (currentState === 'נוזל' || currentState === 'דו-פאזי (גז+נוזל)') {
                         // Add a weak attraction only when in or near liquid state
                         const attraction = ATTRACTION_FORCE_SCALE_LIQUID / dist; // Inverse distance attraction
                         forceX += attraction * (dx / dist);
                         forceY += attraction * (dy / dist);
                    }
                }
            }

            // Add gravity effect only in liquid/two-phase state
            if (currentState === 'נוזל' || currentState === 'דו-פאזי (גז+נוזל)') {
                forceY += GRAVITY_EFFECT_LIQUID;
            }


            // Update velocity based on forces
            this.vx += forceX * dt * 60; // Scale force effect by dt and a factor
            this.vy += forceY * dt * 60;

            // Limit speed based on temperature and state
            let currentSpeed = Math.sqrt(this.vx * this.vx + this.vy * this.vy);
            let maxAllowedSpeed = speedScale;

            if (currentState === 'נוזל') {
                 maxAllowedSpeed *= 0.3; // Liquid moves much slower
            } else if (currentState === 'סופר-קריטי') {
                 maxAllowedSpeed *= 0.7; // Supercritical moves slower than gas, faster than liquid
            }
            // Gas state uses speedScale directly

            if (currentSpeed > maxAllowedSpeed) {
                 const speedRatio = maxAllowedSpeed / currentSpeed;
                 this.vx *= speedRatio;
                 this.vy *= speedRatio;
             } else if (currentSpeed < BASE_PARTICLE_SPEED * 0.1 && currentState === 'גז') {
                 // Prevent particles from stopping completely in gas state
                 const randomAngle = Math.random() * Math.PI * 2;
                 this.vx = Math.cos(randomAngle) * BASE_PARTICLE_SPEED * 0.5;
                 this.vy = Math.sin(randomAngle) * BASE_PARTICLE_SPEED * 0.5;
             }


            // Update position
            this.x += this.vx * dt * 60; // Scale velocity by dt and a factor for visible movement
            this.y += this.vy * dt * 60;


            // Bounce off walls with damping
            if (this.x < PARTICLE_RADIUS) {
                this.x = PARTICLE_RADIUS;
                this.vx = -this.vx * COLLISION_DAMPING;
            } else if (this.x > canvas.width - PARTICLE_RADIUS) {
                this.x = canvas.width - PARTICLE_RADIUS;
                this.vx = -this.vx * COLLISION_DAMPING;
            }
            if (this.y < PARTICLE_RADIUS) {
                this.y = PARTICLE_RADIUS;
                this.vy = -this.vy * COLLISION_DAMPING;
            } else if (this.y > canvas.height - PARTICLE_RADIUS) {
                this.y = canvas.height - PARTICLE_RADIUS;
                this.vy = -this.vy * COLLISION_DAMPING;
            }

             // Set color based on state
             switch (currentState) {
                 case 'גז':
                     this.color = 'var(--gas-color)';
                     break;
                 case 'נוזל':
                     this.color = 'var(--liquid-color)';
                     break;
                 case 'סופר-קריטי':
                      this.color = 'var(--supercritical-color)';
                      break;
                 case 'דו-פאזי (גז+נוזל)':
                     // Color logic is tricky for individual particles in two-phase
                     // Maybe color depends on local environment? Or just use a base color?
                     // For simplicity, let's color based on rough vertical position or local density?
                     // Simple: color by density threshold or position. Let's use position for visual separation
                     if (this.y > canvas.height * 0.6 || neighbors.length > 8) { // Arbitrary threshold or high local density
                          this.color = 'var(--liquid-color)';
                     } else {
                          this.color = 'var(--gas-color)';
                     }
                     break;
                 default:
                     this.color = 'var(--gas-color)';
             }
        }

        draw(ctx) {
            ctx.fillStyle = this.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, PARTICLE_RADIUS, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    // Initialize particles
    function initializeParticles() {
        particles = [];
        const spawnArea = canvas.width * canvas.height * 0.8; // Start slightly less dense
        const particlesPerRow = Math.sqrt(NUM_PARTICLES * (canvas.width / canvas.height));
         const rowHeight = canvas.height / particlesPerRow * (canvas.height / canvas.width);

        for (let i = 0; i < NUM_PARTICLES; i++) {
            // Distribute particles more evenly initially
             const row = Math.floor(i / particlesPerRow);
             const col = i % particlesPerRow;
            particles.push(new Particle(
                 (col / particlesPerRow) * canvas.width + (Math.random()-0.5)*10,
                 (row / particlesPerRow) * canvas.height + (Math.random()-0.5)*10
            ));
        }
    }

    // Determine the current state based on slider values
    function determineState(pressure, temperature, particles) {
        let state = "גז";

        // Simplified phase boundary below critical temperature (approximating a curve)
        // Using a power law curve P_saturation = Pc * (T/Tc)^k + baseline_pressure
        // k > 1 makes the curve steeper towards Tc
        const k = 3; // Curve shape parameter
        const baselinePressure = 5; // Small pressure needed to be 'gas' even at low temp
        const pressureThresholdBelowTc = CRITICAL_PRESSURE * Math.pow(Math.max(0, temperature / CRITICAL_TEMP), k) + baselinePressure;


        if (temperature < CRITICAL_TEMP) {
            // Below critical temperature
            if (pressure > pressureThresholdBelowTc) {
                // Potentially Liquid or Two-Phase. Check particle density.
                let denseAreaCount = 0;
                 const densityCheckGridSize = 30; // Divide canvas into a grid
                 const gridCellsX = Math.floor(canvas.width / densityCheckGridSize);
                 const gridCellsY = Math.floor(canvas.height / densityCheckGridSize);
                 const cellParticleThreshold = NUM_PARTICLES / (gridCellsX * gridCellsY) * 2; // Threshold: 2x average density

                 const grid = Array(gridCellsX).fill(0).map(() => Array(gridCellsY).fill(0));

                 for(const p of particles) {
                     const cellX = Math.floor(p.x / densityCheckGridSize);
                     const cellY = Math.floor(p.y / densityCheckGridSize);
                     if(cellX >= 0 && cellX < gridCellsX && cellY >= 0 && cellY < gridCellsY) {
                         grid[cellX][cellY]++;
                     }
                 }

                 let totalDenseCells = 0;
                 for(let i = 0; i < gridCellsX; i++) {
                     for(let j = 0; j < gridCellsY; j++) {
                         if(grid[i][j] > cellParticleThreshold) {
                             totalDenseCells++;
                         }
                     }
                 }

                 const totalCells = gridCellsX * gridCellsY;
                 const denseAreaRatio = totalDenseCells / totalCells;

                if (denseAreaRatio > 0.2) { // If a significant area is dense
                    // Refine: check how many particles are in dense areas
                    let particlesInDenseAreas = 0;
                    const particleDenseThreshold = 8; // A particle is "dense" if it has this many neighbors within INTERACTION_RADIUS

                    for(let i=0; i < particles.length; i++) {
                        let neighborCount = 0;
                        for(let j=0; j < particles.length; j++) {
                             if (i !== j) {
                                const dx = particles[i].x - particles[j].x;
                                const dy = particles[i].y - particles[j].y;
                                if (dx*dx + dy*dy < INTERACTION_RADIUS_SQ) {
                                     neighborCount++;
                                 }
                             }
                        }
                        if(neighborCount >= particleDenseThreshold) {
                            particlesInDenseAreas++;
                        }
                    }


                    const denseParticleRatio = particlesInDenseAreas / NUM_PARTICLES;

                    if (denseParticleRatio > 0.6) { // If most particles are in dense clumps
                         state = "נוזל";
                    } else if (denseParticleRatio > 0.1) { // If some particles are in dense clumps
                         state = "דו-פאזי (גז+נוזל)";
                    } else {
                         state = "גז (צפוף)"; // High pressure gas, but not yet condensed
                    }

                } else {
                     state = "גז (צפוף)"; // High pressure but not clumping visually
                }

            } else {
                state = "גז";
            }
        } else {
            // Above critical temperature
            if (pressure > CRITICAL_PRESSURE) {
                state = "סופר-קריטי";
            } else {
                state = "גז";
            }
        }

         // Update state display text and color based on the determined state
         currentStateSpan.textContent = state;
         switch (state) {
             case 'גז':
             case 'גז (צפוף)':
                 currentStateSpan.style.color = 'var(--gas-color)';
                 break;
             case 'נוזל':
                 currentStateSpan.style.color = 'var(--liquid-color)';
                 break;
             case 'סופר-קריטי':
                 currentStateSpan.style.color = 'var(--supercritical-color)';
                 break;
             case 'דו-פאזי (גז+נוזל)':
                 // Use background gradient for two-phase if possible, or a neutral color
                 currentStateSpan.style.color = 'var(--secondary-color)'; // Or another color indicating mixed state
                 break;
             default:
                 currentStateSpan.style.color = 'inherit';
         }


        return state; // Return the state for particles to use
    }


    // Animation loop
    let lastTime = 0;
    let animationFrameId = null;

    function animate(currentTime) {
        const dt = (currentTime - lastTime) / 1000; // Time difference in seconds
        lastTime = currentTime;

        const pressure = parseInt(pressureSlider.value);
        const temperature = parseInt(temperatureSlider.value);

        // Determine current state once per frame (or less often)
        const currentState = determineState(pressure, temperature, particles);


        // Clear canvas
        // Use a background color or gradient
        ctx.fillStyle = 'var(--light-color)'; // Default light background
        if (currentState === 'דו-פאזי (גז+נוזל)') {
             // Draw a gradient to hint at the two phases
             const gradient = ctx.createLinearGradient(0, 0, 0, canvas.height);
             gradient.addColorStop(0, 'rgba(77, 182, 172, 0.3)'); // Gas color (slightly transparent)
             gradient.addColorStop(0.5, 'rgba(77, 182, 172, 0.2)');
             gradient.addColorStop(0.5, 'rgba(2, 119, 189, 0.2)'); // Liquid color (slightly transparent)
             gradient.addColorStop(1, 'rgba(2, 119, 189, 0.3)');
             ctx.fillStyle = gradient;
             ctx.fillRect(0, 0, canvas.width, canvas.height);
        } else {
             ctx.fillRect(0, 0, canvas.width, canvas.height);
        }


         // Simple spatial partitioning for neighbor checks (optimization for forces)
         // Divide canvas into cells and store particles in cells
         const cellSize = INTERACTION_RADIUS;
         const grid = {};
         for(const p of particles) {
             const cellX = Math.floor(p.x / cellSize);
             const cellY = Math.floor(p.y / cellSize);
             const key = `${cellX},${cellY}`;
             if (!grid[key]) grid[key] = [];
             grid[key].push(p);
         }


        // Update and draw particles
        for (const particle of particles) {
            // Get neighbors from current and surrounding cells
            const cellX = Math.floor(particle.x / cellSize);
            const cellY = Math.floor(particle.y / cellSize);
            const neighbors = [];
             for (let i = -1; i <= 1; i++) {
                 for (let j = -1; j <= 1; j++) {
                     const key = `${cellX + i},${cellY + j}`;
                     if (grid[key]) {
                         neighbors.push(...grid[key]);
                     }
                 }
             }
            // Remove self from neighbors list
            const particleNeighbors = neighbors.filter(p => p !== particle);


            particle.update(dt, pressure, temperature, currentState, particleNeighbors);
            particle.draw(ctx);
        }

        animationFrameId = requestAnimationFrame(animate);
    }

    // Event Listeners for sliders
    pressureSlider.addEventListener('input', (event) => {
        pressureValueSpan.textContent = event.target.value;
        // Update state display immediately on input
        determineState(parseInt(event.target.value), parseInt(temperatureSlider.value), particles);
    });

    temperatureSlider.addEventListener('input', (event) => {
        temperatureValueSpan.textContent = event.target.value;
         // Update state display immediately on input
        determineState(parseInt(pressureSlider.value), parseInt(event.target.value), particles);
    });

    // Event Listener for explanation button
    explanationButton.addEventListener('click', () => {
        const isVisible = explanationContent.classList.contains('visible');
        if (isVisible) {
            explanationContent.classList.remove('visible');
             // Use a small timeout to allow transition to start before setting display: none
             setTimeout(() => { explanationContent.style.display = 'none'; }, 500); // Match CSS transition time
        } else {
             explanationContent.style.display = 'block';
             // Force reflow to enable transition
             void explanationContent.offsetHeight;
             explanationContent.classList.add('visible');
        }
    });


    // Initial setup
    initializeParticles();
    pressureValueSpan.textContent = pressureSlider.value;
    temperatureValueSpan.textContent = temperatureSlider.value;
    document.getElementById('critical-temp').textContent = CRITICAL_TEMP;
    document.getElementById('critical-pressure').textContent = CRITICAL_PRESSURE;
    determineState(parseInt(pressureSlider.value), parseInt(temperatureSlider.value), particles); // Initial state display and color
    lastTime = performance.now(); // Initialize lastTime for dt calculation
    animate(lastTime); // Start the animation loop

</script>