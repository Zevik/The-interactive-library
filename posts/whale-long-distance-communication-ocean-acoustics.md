---
title: "השיר הגדול: הסימפוניה התת-ימית של לווייתנים למרחקים עצומים"
english_slug: whale-long-distance-communication-ocean-acoustics
category: "מדעי החיים / ביולוגיה ימית"
tags:
  - לווייתנים
  - תקשורת בעלי חיים
  - אוקיינוס
  - סאונד
  - אקוסטיקה ימית
---
# השיר הגדול: הסימפוניה התת-ימית של לווייתנים למרחקים עצומים

דמיינו עולם שבו החושך שולט, והמרחק מודד באלפי קילומטרים. זהו ביתם של הלווייתנים באוקיינוס העמוק. איך יצורי ענק אלה מצליחים לנגן את שיריהם ולשמוע זה את זה על פני מרחבים כה עצומים, כשהראייה מוגבלת כל כך? הצטרפו אלינו למסע אקוסטי לגלות את סודות התקשורת התת-ימית המופלאה שלהם.

<div class="simulation-container">
    <div class="controls">
        <div class="control-group">
            <label for="transmitter-depth">עומק הלווייתן (מטרים):</label>
            <input type="range" id="transmitter-depth" min="0" max="2000" value="100">
            <span id="depth-value">100 מ'</span>
        </div>
        <div class="control-group">
            <label for="sound-frequency">תדר הצליל:</label>
            <select id="sound-frequency">
                <option value="low">נמוך (כחול/סנפיר)</option>
                <option value="medium">בינוני (אורקה/גבן)</option>
                <option value="high">גבוה (דולפין/ראשתן)</option>
            </select>
        </div>
         <div class="signal-strength">
            <span id="strength-label">עוצמה בקולט:</span>
            <div class="strength-bar-indicator"></div>
            <span id="strength-text">אין קליטה</span>
        </div>
    </div>
    <div class="canvas-area">
        <canvas id="ocean-canvas" width="800" height="400"></canvas>
        <div class="sofar-label">ערוץ SOFAR (ערוץ הקול העמוק)</div>
    </div>
    <div class="legend">
        <span>הסבר צבע קול:</span>
        <div class="strength-gradient"></div>
        <span>חזק</span>
        <span>חלש מאוד</span>
    </div>
</div>

<button id="toggle-explanation">גלו את הסודות: הסבר מעמיק על אקוסטיקה ימית</button>

<div id="explanation" class="hidden">
    <h2>גלו את הסודות: אקוסטיקה ימית ותקשורת לווייתנים למרחקים</h2>

    <p>עבור התושבים הימיים, הים הוא זירה של אתגרים ותחבולות תקשורתיות. אור השמש נגוז במהירות בעומק, מותיר את הראייה ככלי תקשורת קצר טווח בלבד. אך קול, הו קול! הוא דוהר במים במהירות העולה פי ארבעה על מהירותו באוויר, ופורץ את גבולות החשכה למרחקים אדירים. לא פלא שהקול הפך לשפה העיקרית בעומקים, בפרט כשמדובר בשיחות חוצות אוקיינוסים.</p>

    <p>התנהגות הקול במים אינה פשוטה. מהירותו משתנה בהתאם לטמפרטורה, מליחות ולחץ (עומק). ככל שהים חם יותר, מלוח יותר או עמוק יותר, הקול ממהר יותר. אך גם הקול נחלש במסעו - חלק מהאנרגיה שלו נבלעת על ידי המים עצמם ועל ידי כל מה שצף ומומס בהם. תופעה זו, המכונה בליעה אקוסטית, אכזרית במיוחד כלפי צלילים בתדר גבוה.</p>

    <p>כאן טמון סוד מרחק התקשורת: צלילים גבוהי תדר נבלעים במהירות הבזק, ולכן בעלי חיים קטנים כמו דולפינים, המשתמשים ב"קליקים" ו"שריקות" גבוהים לצורך איכון הד וקשר מקומי, מוגבלים ל"שיחות" קצרות טווח. לעומתם, ענקי הים - לווייתנים כחולים, לווייתני סנפיר, ואחרים - פיתחו יכולת קולית מדהימה: הם מפיקים צלילים בתדר נמוך במיוחד (לעיתים בלתי נשמעים לאוזן אדם - אינפרא-סאונד), הנבלעים בקושי רב ויכולים לחצות אוקיינוסים שלמים.</p>

    <p>אך לא רק התדר קובע. מבנה האוקיינוס עצמו הוא שותף בסוד. בעומקים מסוימים (לרוב סביב 800-1200 מטר, משתנה לפי מיקום ותנאים), קיים אזור ייחודי שבו מהירות הקול מגיעה למינימום. הסיבה? שילוב של ירידת הטמפרטורה הנעצרת ולחץ שעדיין אינו גבוה מספיק כדי להעלות משמעותית את מהירות הקול. אזור זה הוא "ערוץ הקול העמוק" או "ערוץ SOFAR" (Sound Fixing and Ranging channel). זהו כמו "כביש מהיר" אקוסטי: כאשר צליל נוצר בתוך הערוץ הזה, הוא "נכלא" בו. קרני קול המנסות לברוח למעלה נתקלות בשכבות מהירות יותר ומתכופפות חזרה כלפי מטה, ואילו קרני קול היורדות מטה פוגשות שכבות מהירות יותר ומתכופפות חזרה למעלה. אפקט "שבירה" מתמשך זה גורם לקול לדהור בתוך הערוץ כמעט ללא פיזור והתנגשות עם הקרקעית או פני הים, ולאפשר לו להגיע למרחקים עצומים, לעיתים אלפי קילומטרים!</p>

    <p>הלווייתנים הגדולים לא רק משתמשים בתדרים נמוכים, אלא גם נמצאו כמי ששׂרִים ומשדרים את קולם בעומקים המאפשרים להם להיכנס לערוץ ה-SOFAR הקסום הזה ולנצל אותו. יכולת תקשורת מדהימה זו אינה מותרות - היא קריטית להישרדותם: למצוא בני זוג במרחבי הים האינסופיים, אולי לתאם פעילות קבוצתית, ובעיקר לשמור על קשר חברתי בסביבה עוינת ומרוחקת.</p>

    <p>הסימולציה שלפניכם מציגה מודל פשטני אך ממחיש את העקרונות הגדולים: צלילים נמוכים מחזיקים מעמד זמן רב יותר, ויש עומק "אידיאלי" שבו הקול יכול לנסוע הכי רחוק בזכות כליאתו בערוץ SOFAR. הבנת סימפוניית הקול הזו אינה רק מרתקת ביולוגית, אלא חיונית גם למחקר ימי, ניטור סביבתי ואפילו ניווט ותקשורת תת-ימיים.</p>
</div>

<style>
    /* גופנים ועיצוב כללי */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6;
        margin: 0;
        padding: 20px;
    }

    h1, h2 {
        color: #004080; /* Deep blue */
        text-align: center;
        margin-bottom: 20px;
    }

    p {
        margin-bottom: 15px;
    }

    /* קונטיינר הסימולציה */
    .simulation-container {
        border: 1px solid #a0d0f0; /* Lighter blue border */
        padding: 25px;
        margin-bottom: 30px;
        background: linear-gradient(to bottom, #e0f2f7, #cce7f0); /* Subtle gradient */
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        overflow: hidden; /* Clear floats */
    }

    /* פקדים */
    .controls {
        margin-bottom: 25px;
        display: flex;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        justify-content: center; /* Center controls */
        align-items: center;
        padding: 15px;
        background-color: #b3e5fc; /* Slightly lighter blue */
        border-radius: 8px;
        gap: 20px; /* Space between control groups */
    }

    .control-group {
        display: flex;
        align-items: center;
    }

    .controls label {
        margin-right: 10px;
        font-weight: bold;
        color: #004080; /* Deep blue text */
    }

    .controls input[type="range"] {
        flex-grow: 1; /* Allow slider to take available space */
        min-width: 150px; /* Minimum width */
        -webkit-appearance: none; /* Remove default style */
        appearance: none;
        height: 8px;
        background: #0288d1; /* Medium blue */
        outline: none;
        opacity: 0.8;
        transition: opacity 0.2s ease-in-out;
        border-radius: 5px;
    }

    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #004080; /* Dark blue thumb */
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    .controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #004080;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }


    .controls select {
        padding: 8px;
        border-radius: 5px;
        border: 1px solid #0288d1;
        background-color: #e1f5fe; /* Very light blue */
        color: #004080;
        font-size: 1em;
        cursor: pointer;
    }

    #depth-value {
        margin-left: 10px;
        min-width: 50px; /* Prevent jumping layout */
        text-align: left;
        color: #004080;
    }

    .signal-strength {
        display: flex;
        align-items: center;
        gap: 5px;
        color: #004080;
    }

    .strength-bar-indicator {
         width: 20px;
         height: 20px;
         border-radius: 50%;
         background-color: #ccc; /* Default grey */
         border: 2px solid #004080;
         transition: background-color 0.3s ease; /* Smooth transition */
    }

    #strength-text {
        font-weight: bold;
         min-width: 80px; /* Prevent jumping */
    }


    /* קנבס ושטח הסימולציה */
    .canvas-area {
        position: relative;
        margin: 0 auto;
        border: 2px solid #004080; /* Darker border */
        border-radius: 8px;
        overflow: hidden; /* Hide anything outside */
    }

    #ocean-canvas {
        display: block;
        background: linear-gradient(to bottom, #00aaff 0%, #004080 100%); /* Deeper blue gradient */
    }

    .sofar-label {
         position: absolute;
         top: calc(400px * (1000 / 2000) - 10px); /* Approximately 1000m depth */
         right: 10px;
         background-color: rgba(255, 255, 255, 0.8);
         padding: 3px 8px;
         border-radius: 4px;
         font-size: 0.8em;
         color: #004080;
         pointer-events: none; /* Don't interfere with canvas interactions */
         z-index: 10;
    }


    /* מקרא */
    .legend {
        text-align: center;
        margin-top: 15px;
        font-size: 0.9em;
        color: #555;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
    }

    .strength-gradient {
        display: inline-block;
        width: 150px;
        height: 15px;
        background: linear-gradient(to right, #00ff00, #ffff00, #ffa500, #ff0000); /* Green (strong) to Red (weak) */
        vertical-align: middle;
        border-radius: 5px;
    }


    /* כפתור הסבר */
    #toggle-explanation {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        background-color: #0288d1; /* Medium blue */
        color: white;
        border-radius: 8px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        font-weight: bold;
    }

    #toggle-explanation:hover {
        background-color: #01579b; /* Darker blue on hover */
        transform: translateY(-1px); /* Subtle lift effect */
    }

    #toggle-explanation:active {
        transform: translateY(0); /* Press effect */
    }

    /* אזור הסבר */
    #explanation {
        margin-top: 20px;
        padding: 25px;
        border: 1px solid #a0d0f0;
        background-color: #e1f5fe; /* Very light blue */
        border-radius: 10px;
        line-height: 1.7;
        color: #333;
    }

    #explanation h2 {
        color: #0056b3; /* Slightly darker blue for title */
        margin-top: 0;
        margin-bottom: 15px;
        border-bottom: 1px solid #b3e5fc;
        padding-bottom: 10px;
        text-align: right;
    }

    #explanation p {
        margin-bottom: 18px;
        text-align: justify;
    }

    .hidden {
        display: none;
    }

    /* אנימציות ורכיבים דינמיים */

    @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.1); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
    }

     .whale-icon {
        position: absolute;
        width: 20px; /* Size of the circle */
        height: 20px;
        background-color: #333; /* Dark grey */
        border-radius: 50%;
        cursor: grab;
        z-index: 5; /* Above canvas */
         left: 40px; /* Position relative to canvas container */
         top: 0; /* Will be set by JS based on depth */
         display: flex;
         align-items: center;
         justify-content: center;
         color: white;
         font-size: 12px;
         font-weight: bold;
    }

    .whale-icon:active {
        cursor: grabbing;
    }

     .receiver-icon {
         position: absolute;
         width: 20px; /* Size of the circle */
         height: 20px;
         background-color: #d32f2f; /* Red */
         border-radius: 50%;
         z-index: 5; /* Above canvas */
         left: calc(700px - 10px); /* Position relative to canvas container (700 is receiverDistance) */
         top: 0; /* Will be set by JS based on depth */
         display: flex;
         align-items: center;
         justify-content: center;
         color: white;
         font-size: 12px;
         font-weight: bold;
     }

    .receiver-icon::after {
        content: '';
        position: absolute;
        width: 30px;
        height: 30px;
        border: 2px solid rgba(211, 47, 47, 0.5);
        border-radius: 50%;
        animation: pulse 2s infinite ease-in-out;
    }


</style>

<script>
    const canvas = document.getElementById('ocean-canvas');
    const ctx = canvas.getContext('2d');
    const depthSlider = document.getElementById('transmitter-depth');
    const depthValueSpan = document.getElementById('depth-value');
    const frequencySelect = document.getElementById('sound-frequency');
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');
    const strengthBarIndicator = document.querySelector('.strength-bar-indicator');
    const strengthTextSpan = document.getElementById('strength-text');
    const canvasArea = document.querySelector('.canvas-area'); // Container for positioning icons


    const canvasWidth = canvas.width;
    const canvasHeight = canvas.height;
    const maxDepth = 2000; // Max depth represented in canvas (meters)
    const surfaceY = 0; // Top of canvas is surface
    const bottomY = canvasHeight; // Bottom of canvas is 2000m

    const transmitterStartX = 50; // X position for the whale (pixels from left)
    const receiverX = canvasWidth - 100; // X position for the receiver (pixels from left) - Adjusted for better view
    const receiverDepth = 1000; // Fixed receiver depth (meters)
    const receiverY = scaleDepth(receiverDepth); // Y position for the receiver (pixels)

    // Create whale and receiver elements
    const whaleIcon = document.createElement('div');
    whaleIcon.classList.add('whale-icon');
     whaleIcon.textContent = '🐳'; // Use emoji or icon letter
    canvasArea.appendChild(whaleIcon);

    const receiverIcon = document.createElement('div');
    receiverIcon.classList.add('receiver-icon');
    receiverIcon.textContent = '🎧'; // Use emoji or icon letter
    canvasArea.appendChild(receiverIcon);

    let isDraggingWhale = false;


    // Scale depth from meters to canvas pixels (Y coordinate)
    function scaleDepth(depth) {
        return (depth / maxDepth) * canvasHeight;
    }

    // Scale Y coordinate from canvas pixels to meters
     function unscaleDepth(y) {
         return (y / canvasHeight) * maxDepth;
     }


    // Simplified model for sound speed profile (approximating SOFAR)
    // This function returns sound speed relative to a base speed,
    // or can be used to calculate bending. Bending is towards lower speed.
    // Minimum speed is around 1000m.
    function getSoundSpeedRelative(depth) {
        // Basic quadratic approximation of speed profile relative to minimum
        const sofarDepth = 1000;
        const depthDiff = depth - sofarDepth;
        // Example profile: minimum at 1000, increases as you move away
        // speed = base + k * (depth - sofarDepth)^2
        // We only care about the *change* in speed with depth for bending
        // d(speed)/d(depth) is what matters for ray tracing (Snell's Law)
        // A simpler approach for bending: BEND TOWARDS the minimum speed layer (1000m)
        return Math.abs(depthDiff); // Representing 'slowness' or 'resistance' - lower value means faster sound/less bending resistance
                                    // Rays bend AWAY from high speed / TOWARDS low speed
    }

     function getSpeedGradient(depth) {
         // This determines the bending direction and strength
         // Positive gradient means speed increases with depth (bends up)
         // Negative gradient means speed decreases with depth (bends down)
         // Simplified: negative slope above SOFAR, positive slope below
         const sofarDepth = 1000;
         const slopeFactor = 0.0001; // Controls how strong the bending is
         if (depth < sofarDepth) {
             return (depth - sofarDepth) * slopeFactor; // Negative below sofar, positive above
         } else {
             return (depth - sofarDepth) * slopeFactor;
         }
     }


    // State for animated rays
    let soundRays = [];
    const raySpeed = 3; // Pixels per animation frame
    const numRays = 15; // More rays for a fuller look
    const initialAngleSpread = Math.PI / 4; // Spread of initial angles (+/-)
    const raysPerPulse = 3; // How many rays in a single pulse wave

    // Function to generate a pulse of rays
    function createSoundPulse() {
         const transmitterDepth = parseInt(depthSlider.value);
         const txY = scaleDepth(transmitterDepth);
         const pulseRays = [];
         for(let i = 0; i < raysPerPulse; i++) {
             // Slightly vary angles within the pulse
             const angle = -initialAngleSpread/2 + (i / (raysPerPulse - 1)) * initialAngleSpread + (Math.random() - 0.5) * (initialAngleSpread / 5); // Add slight randomness
             pulseRays.push({
                 x: transmitterStartX,
                 y: txY,
                 angle: angle,
                 strength: 1, // Start at full strength
                 history: [{x: transmitterStartX, y: txY}], // To draw the path
                 speed: raySpeed + (Math.random() - 0.5) * 0.5 // Slight speed variation
             });
         }
         soundRays = soundRays.concat(pulseRays); // Add to the main array
    }

    let pulseInterval; // To control the timing of pulses

    function startSoundTransmission() {
         // Clear existing rays and intervals
         soundRays = [];
         clearInterval(pulseInterval);

         // Start new pulses
         // Send an initial burst
         for(let i=0; i<5; i++) {
             setTimeout(createSoundPulse, i * 150); // Stagger initial pulses slightly
         }
         // Then send regular pulses
        pulseInterval = setInterval(createSoundPulse, 1000); // Send a new pulse every second
    }


    // Animation loop
    function animate() {
        // Clear canvas or draw background
        ctx.clearRect(0, 0, canvasWidth, canvasHeight);
        // Background gradient is handled by CSS

         // Draw SOFAR channel indicator
         const sofarY = scaleDepth(1000);
         ctx.save();
         ctx.globalAlpha = 0.3;
         ctx.fillStyle = '#a0d0f0'; // Light blue highlight
         ctx.fillRect(0, sofarY - scaleDepth(100), canvasWidth, scaleDepth(200)); // Highlight a 200m band around SOFAR
         ctx.strokeStyle = '#004080';
         ctx.setLineDash([5, 5]);
         ctx.strokeRect(0, sofarY - scaleDepth(100), canvasWidth, scaleDepth(200));
         ctx.restore();
         ctx.setLineDash([]); // Reset line dash


        // Update and draw rays
        soundRays = soundRays.filter(ray => ray.strength > 0.01 && ray.x < canvasWidth && ray.y > 0 && ray.y < canvasHeight); // Remove dead/out-of-bounds rays

        soundRays.forEach(ray => {
            // Calculate bending
            const currentDepth = unscaleDepth(ray.y);
            const speedGradient = getSpeedGradient(currentDepth); // How much speed changes with depth
            const bendingAngleChange = -speedGradient * Math.cos(ray.angle); // Simplified bending based on gradient and current angle

            ray.angle += bendingAngleChange;

            // Update position
            const stepX = ray.speed * Math.cos(ray.angle);
            const stepY = ray.speed * Math.sin(ray.angle);

            const nextX = ray.x + stepX;
            const nextY = ray.y + stepY;

            // Calculate attenuation (weakening)
            const distanceStep = Math.sqrt(stepX*stepX + stepY*stepY);
            let attenuationRate = 0.00001; // Base attenuation per pixel distance

             // Adjust attenuation based on frequency (higher frequency attenuates much faster)
            const frequency = frequencySelect.value;
            switch (frequency) {
                case 'low': attenuationRate *= 1; break;
                case 'medium': attenuationRate *= 10; break; // 10x faster attenuation
                case 'high': attenuationRate *= 100; break; // 100x faster attenuation
            }

            ray.strength -= attenuationRate * distanceStep;
            ray.strength = Math.max(0, ray.strength); // Strength doesn't go below zero

            // Add current position to history (for drawing the trail)
             ray.history.push({x: ray.x, y: ray.y});
             // Limit history length for performance and trailing effect
             const maxHistory = 100; // Pixels of trail
             if (ray.history.length > maxHistory) {
                 ray.history.shift(); // Remove the oldest point
             }


            ray.x = nextX;
            ray.y = nextY;

            // Draw ray trail
            ctx.beginPath();
            ctx.moveTo(ray.history[0].x, ray.history[0].y);
            for(let i = 1; i < ray.history.length; i++) {
                ctx.lineTo(ray.history[i].x, ray.history[i].y);
            }
             // Draw current segment
            ctx.lineTo(ray.x, ray.y);

            // Set color and width based on strength
            const hue = ray.strength * 120; // Green (120) to Red (0)
            ctx.strokeStyle = `hsla(${hue}, 100%, 50%, ${ray.strength * 0.8})`; // Use alpha for fading trail
            ctx.lineWidth = Math.max(0.5, ray.strength * 4); // Thicker for stronger signal
            ctx.stroke();

             // Draw current ray head
             ctx.fillStyle = `hsl(${hue}, 100%, 50%)`;
             ctx.beginPath();
             ctx.arc(ray.x, ray.y, Math.max(1, ray.strength * 3), 0, Math.PI * 2); // Pulsing head
             ctx.fill();
        });

         // Update receiver signal strength
         updateReceiverStrength();


        // Request next frame
        requestAnimationFrame(animate);
    }

     function updateReceiverStrength() {
         let totalStrength = 0;
         let count = 0;
         const receiverDetectionRadius = 15; // Pixels radius around receiver icon

         soundRays.forEach(ray => {
             const distanceToReceiver = Math.sqrt((ray.x - receiverX)**2 + (ray.y - receiverY)**2);
             if (distanceToReceiver < receiverDetectionRadius) {
                 // Simple model: strength contributes based on its current strength and proximity
                 // Max strength if exactly on receiver, less if within radius
                 const proximityFactor = 1 - (distanceToReceiver / receiverDetectionRadius);
                 totalStrength += ray.strength * proximityFactor;
                 count++;
             }
         });

         // Average strength (or just sum, depending on desired effect)
         const averageStrength = count > 0 ? totalStrength / count : 0;

         // Map average strength (0 to 1) to a display value/color
         const displayStrength = Math.min(1, averageStrength * 2); // Amplify small signals for display
         const strengthHue = displayStrength * 120; // Green (120) to Red (0)
         const strengthColor = `hsl(${strengthHue}, 100%, 50%)`;

         if (averageStrength > 0.05) { // Only show text/color if there's a meaningful signal
              strengthBarIndicator.style.backgroundColor = strengthColor;
              strengthTextSpan.textContent = `${(displayStrength * 100).toFixed(0)}% עוצמה`;
              strengthTextSpan.style.color = strengthColor;
               strengthBarIndicator.style.borderColor = strengthColor; // Border matches color
               // Optional: pulse the indicator if strength is high
                if (displayStrength > 0.5) {
                     strengthBarIndicator.style.animation = 'pulse 1s infinite';
                } else {
                     strengthBarIndicator.style.animation = 'none';
                }

         } else {
             strengthBarIndicator.style.backgroundColor = '#ccc';
             strengthTextSpan.textContent = 'אין קליטה';
             strengthTextSpan.style.color = '#555';
              strengthBarIndicator.style.borderColor = '#004080';
              strengthBarIndicator.style.animation = 'none';
         }

     }


    // Update icon positions based on current values
     function updateIconPositions() {
         const txY = scaleDepth(parseInt(depthSlider.value));
         whaleIcon.style.top = `${txY - whaleIcon.offsetHeight / 2}px`; // Center vertically

         receiverIcon.style.top = `${receiverY - receiverIcon.offsetHeight / 2}px`; // Center vertically
         receiverIcon.style.left = `${receiverX - receiverIcon.offsetWidth / 2}px`; // Center horizontally
     }


     // Handle whale icon drag
     whaleIcon.addEventListener('mousedown', (e) => {
         isDraggingWhale = true;
         whaleIcon.style.cursor = 'grabbing';
         // Prevent default to avoid text selection etc.
         e.preventDefault();
     });

     document.addEventListener('mousemove', (e) => {
         if (!isDraggingWhale) return;

         // Get mouse position relative to the canvas area
         const rect = canvasArea.getBoundingClientRect();
         let mouseY = e.clientY - rect.top;

         // Clamp Y position to canvas bounds
         mouseY = Math.max(0, Math.min(canvasHeight, mouseY));

         // Update slider value based on mouse Y
         const newDepth = Math.round(unscaleDepth(mouseY));
         depthSlider.value = newDepth;
         depthValueSpan.textContent = `${newDepth} מ'`;

         // Update whale icon position and restart transmission
         updateIconPositions();
         startSoundTransmission();
     });

     document.addEventListener('mouseup', () => {
         if (isDraggingWhale) {
             isDraggingWhale = false;
             whaleIcon.style.cursor = 'grab';
             // Restart transmission when drag ends
             startSoundTransmission();
         }
     });


    // Event listeners for controls
    depthSlider.addEventListener('input', () => {
        depthValueSpan.textContent = `${depthSlider.value} מ'`;
         updateIconPositions(); // Move icon when slider changes
         // Delay restart slightly if rapidly changing? Or maybe restart immediately
         // Restarting immediately provides more direct feedback
         startSoundTransmission();
    });

    frequencySelect.addEventListener('change', () => {
        startSoundTransmission(); // Restart transmission with new frequency
    });

    // Toggle explanation visibility
    toggleButton.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
        if (!explanationDiv.classList.contains('hidden')) {
            // Optional: Scroll to explanation if it becomes visible
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

    // Initial setup and drawing
     updateIconPositions(); // Position icons initially
     startSoundTransmission(); // Start the sound transmission animation
    animate(); // Start the animation loop

</script>
</html>