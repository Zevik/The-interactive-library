---
title: "הצליל שמשנה גובה בתנועה: אפקט דופלר - סימולציה אינטראקטיבית"
english_slug: the-sound-that-changes-pitch-in-motion-doppler-effect-interactive
category: "פיזיקה"
tags: ["אפקט דופלר", "גלים", "תדר", "תנועה יחסית", "אקוסטיקה", "סימולציה"]
---
<h1>הצליל שמשנה גובה בתנועה: אפקט דופלר</h1>
<p class="lead">האם אי פעם עמד/ה ליד כביש ושמת/ה לב איך הצליל של מכונית חולפת משתנה מרגע ההתקרבות לרגע ההתרחקות? זו לא סתם אשליה שמיעתית! זוהי תופעה פיזיקלית מדהימה שמשפיעה על כל סוגי הגלים - מאור ועד גלי קול - ומכונה 'אפקט דופלר'. היא מסבירה בדיוק מדוע התדר (ולכן גם גובה הצליל) שאת/ה שומע/ת תלוי בתנועה היחסית בינך לבין מקור הצליל.</p>
<p class="lead">בואו נצלול לתוך הסימולציה הזו כדי לראות את אפקט דופלר בפעולה ולהבין איך הוא עובד, לפני שנקרא את ההסבר הפיזיקלי המלא.</p>

<div class="simulation-container">
    <canvas id="dopplerCanvas" width="700" height="350"></canvas>
    <div class="controls-info-flex">
        <div class="controls panel">
            <h3>שליטה בסימולציה</h3>
            <div class="control-group">
                 <label for="sourceSpeed">מהירות המקור:</label>
                <input type="range" id="sourceSpeed" min="-150" max="150" value="0" step="1">
                <span id="currentSpeedValue" class="value-display">0 יח'/שנייה</span>
                <p class="control-hint">גרור את המחוון לשינוי מהירות המקור (<span class="speed-neg">שמאלה</span> או <span class="speed-pos">ימינה</span>).</p>
            </div>
             <!-- Future Idea: Add observer speed control here -->
        </div>
        <div class="info panel">
            <h3>נתונים בזמן אמת</h3>
            <p><strong>תדר מקור:</strong> <span id="sourceFreqValue" class="value-display"></span> הרץ</p>
            <p><strong>מהירות גל:</strong> <span id="waveSpeedValue" class="value-display"></span> יח'/שנייה</p>
            <p><strong>תדר נצפה:</strong> <span id="perceivedFreqValue" class="value-display perceived-freq"></span> הרץ</p>
             <div class="freq-indicator" id="freqIndicator"></div>
        </div>
    </div>
     <p class="canvas-hint">ציר X בסימולציה מייצג מרחב. המקור פולט גלים קוליים (המעגלים הכחולים) והצופה מקשיב להם.</p>

</div>

<button id="toggleExplanation" class="explanation-button">רוצה להבין לעומק? הצג/הסתר הסבר פיזיקלי</button>

<div id="explanation" class="hidden explanation-box">
    <h2>הסבר: מהו אפקט דופלר?</h2>
    <p>אפקט דופלר הוא שינוי בתדר הנצפה (התדר שנקלט על ידי הצופה) של גל, כאשר המקור הפולט את הגל או הצופה שקולט אותו נמצאים בתנועה יחסית זה לזה. התופעה קרויה על שם הפיזיקאי האוסטרי כריסטיאן דופלר, שתיאר אותה ב-1842.</p>

    <h3>למה זה קורה? הדמיה ויזואלית</h3>
    <p>דמיינו מקור קול נייח הפולט גלים. הגלים מתפשטים ממנו לכל הכיוונים במהירות קבועה, יוצרים מעגלים שמתרחבים באופן אחיד. המרחק בין פסגות גלים סמוכות (זהו אורך הגל) זהה בכל הכיוונים, ולכן צופה בכל מקום ישמע את אותו התדר (מספר הגלים שמגיעים אליו בשנייה).</p>

    <p>עכשיו דמיינו שהמקור מתחיל לנוע, למשל, ימינה. הוא עדיין פולט גלים בתדר קבוע, אבל כל גל חדש נפלט מנקודה מעט שונה במרחב. הגלים שנפלטים בכיוון התנועה 'נדחסים' - המקור "רודף" אחרי הגלים הקודמים שהוא פלט באותו כיוון, ולכן המרחק ביניהם קטן יותר. לעומת זאת, הגלים שנפלטים בכיוון ההפוך לתנועת המקור 'נמתחים' - המקור מתרחק מהם, ולכן המרחק ביניהם גדל.</p>

     <div class="image-placeholder">
        <!-- Ideally, an image showing compressed waves ahead of moving source and stretched waves behind -->
        <p>[דמיינו כאן איור של גלים דחוסים מלפנים ומתוחים מאחורי מקור נע]</p>
     </div>

    <p>כאשר אורך הגל הנקלט משתנה, ומהירות הגל בתווך (למשל, מהירות הקול באוויר) נשארת קבועה, התדר הנקלט חייב להשתנות בהתאם לנוסחה הבסיסית של גלים: **מהירות גל = תדר × אורך גל**.</p>
    <ul>
        <li>כיוון ההתקרבות: אורך גל קצר יותר ← **תדר נצפה גבוה יותר** (צליל גבוה).</li>
        <li>כיוון ההתרחקות: אורך גל ארוך יותר ← **תדר נצפה נמוך יותר** (צליל נמוך).</li>
    </ul>

    <p>האפקט מתרחש גם כשהצופה נע ביחס למקור נייח. במקרה זה, הצופה "פוגש" יותר או פחות גלים בשנייה, בהתאם לכיוון תנועתו ביחס לגלים, מה שמשנה את התדר הנקלט.</p>

    <h3>נוסחאות (למתקדמים):</h3>
    <p>כשהמקור נע והצופה נייח:</p>
    <p>\[ f' = f_0 \left(\frac{v_w}{v_w \mp v_s}\right) \]</p>
    <p>כאשר:</p>
    <ul>
        <li>\(f'\) הוא התדר הנצפה</li>
        <li>\(f_0\) הוא תדר המקור</li>
        <li>\(v_w\) היא מהירות הגל בתווך</li>
        <li>\(v_s\) היא מהירות המקור יחסית לתווך</li>
    </ul>
    <p>משתמשים במינוס במכנה כאשר המקור **מתקרב** לצופה, ובפלוס כאשר המקור **מתרחק** מהצופה.</p>
     <p><em>שימו לב: הסימולציה הנוכחית מדגימה מקרה פרטי שבו הצופה נייח והמקור נע אופקית.</em></p>

    <h3>דוגמאות ויישומים בחיי היומיום ובמדע:</h3>
    <ul>
        <li><strong>אמבולנס או ניידת משטרה:</strong> הדוגמה הקלאסית והמפורסמת ביותר.</li>
        <li><strong>מכ"ם (רדאר) משטרתי:</strong> מודד את מהירות הרכב על ידי שליחת גלי רדיו והשוואת התדר שלהם לתדר הגלים המוחזרים (ששינו את תדרם עקב תנועת הרכב).</li>
        <li><strong>אסטרונומיה (הסחת דופלר של אור):</strong> כוכבים וגלקסיות שמתרחקים מאיתנו מראים "הסחה לאדום" (תדר אור נמוך יותר), וכאלה שמתקרבים מראים "הסחה לכחול" (תדר אור גבוה יותר). זהו כלי מרכזי להבנת תנועתם של גרמי שמיים והתפשטות היקום.</li>
        <li><strong>אולטרסאונד רפואי:</strong> בודק זרימת דם בעורקים על ידי מדידת אפקט דופלר של גלי קול המוחזרים מתאי הדם הנעים.</li>
    </ul>
    <p>אפקט דופלר הוא לא רק תופעה פיזיקלית מעניינת, אלא כלי רב עוצמה שמאפשר לנו לחקור ולמדוד תנועה במגוון עצום של תחומים!</p>
</div>

<style>
    /* הגדרות כלליות */
    body {
        font-family: 'Heebo', sans-serif; /* נשתמש בפונט מודרני ונפוץ, או ב-sans-serif ברירת מחדל */
        line-height: 1.7;
        padding: 30px;
        direction: rtl; /* כיוון מימין לשמאל */
        text-align: right;
        background-color: #f0f4f8; /* רקע נעים */
        color: #333;
    }

    h1, h2, h3 {
        text-align: center;
        color: #1a2e42; /* כחול כהה לכותרות */
        margin-bottom: 20px;
    }

    h1 {
        font-size: 2.5em;
        margin-bottom: 10px;
        font-weight: 700;
    }

    h2 {
         font-size: 1.8em;
         margin-top: 30px;
         border-bottom: 2px solid #aed6f1; /* קו תחתון עדין */
         padding-bottom: 5px;
         display: inline-block; /* כדי שהקו התחתון יהיה רק ברוחב הטקסט */
         margin-right: auto; /* ממקם לימין אם הטקסט קצר */
         margin-left: auto; /* ממקם למרכז אם הטקסט ארוך יותר מהבלוק */
         text-align: right; /* יישור לימין */
    }

     h3 {
         font-size: 1.4em;
         margin-top: 20px;
         color: #1a2e42;
     }


    p.lead {
        text-align: center;
        font-size: 1.2em;
        color: #555;
        max-width: 800px;
        margin: 10px auto 30px auto;
    }

    /* סטיילינג למיכל הסימולציה */
    .simulation-container {
        border: 1px solid #cce0f2;
        padding: 25px;
        margin: 30px auto;
        background-color: #eef7ff; /* רקע בהיר לסימולציה */
        max-width: 740px; /* רחב יותר להתאמה לקנבס */
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        text-align: center; /* מרכז אלמנטים פנימיים */
    }

     .controls-info-flex {
        display: flex;
        flex-direction: column; /* עמודה במובייל */
        gap: 20px;
        margin-top: 15px;
        justify-content: center;
        align-items: stretch; /* מותח פאנלים לרוחב שווה */
    }

    @media (min-width: 768px) { /* פריסה צד-לצד בדסקטופ */
        .controls-info-flex {
            flex-direction: row;
             align-items: flex-start; /* יישור למעלה */
        }
         .controls-info-flex > div {
             flex: 1; /* כל פאנל תופס שטח שווה */
         }
    }

    .panel {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        text-align: right; /* יישור תוכן הפאנל לימין */
    }

     .panel h3 {
        margin-top: 0;
        text-align: center;
        margin-bottom: 15px;
        color: #1a2e42;
        font-size: 1.2em;
     }

    canvas {
        display: block;
        margin: 0 auto 15px auto;
        border: 1px solid #aed6f1;
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.1);
    }

    .control-group {
        margin-bottom: 15px;
        text-align: center; /* מרכז את תוכן קבוצת הבקרה */
    }

    .control-group label {
        margin-right: 10px;
        font-weight: bold;
        color: #555;
        display: block; /* כל לייבל בשורה משלו */
        margin-bottom: 8px;
    }

    #sourceSpeed {
        width: 95%; /* מחוון רחב */
        max-width: 400px;
        direction: ltr; /* המחוון עצמו LTR */
        -webkit-appearance: none; /* סגנון קלאסי */
        appearance: none;
        height: 8px;
        background: #ddd;
        outline: none;
        opacity: 0.7;
        transition: opacity 0.2s;
        border-radius: 4px;
         cursor: pointer;
    }

    #sourceSpeed:hover {
        opacity: 1;
    }

    #sourceSpeed::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    #sourceSpeed::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }


     .value-display {
        font-weight: bold;
        color: #007bff; /* כחול */
         font-size: 1.1em;
         display: inline-block; /* כדי לאפשר מרג'ין */
         margin-left: 5px; /* רווח קטן מהלייבל */
     }

     .perceived-freq {
         color: #28a745; /* ירוק לתדר הנצפה */
         font-size: 1.3em;
         transition: color 0.3s ease; /* אנימציה לשינוי צבע */
     }

     .perceived-freq.high { color: #ff4d4d; } /* אדום לתדר גבוה */
     .perceived-freq.low { color: #4da6ff; } /* כחול לתדר נמוך */


     .control-hint, .canvas-hint {
        font-size: 0.9em;
        color: #777;
        margin-top: 10px;
     }
      .speed-neg { color: #e74c3c; font-weight: bold; } /* אדום */
      .speed-pos { color: #2ecc71; font-weight: bold; } /* ירוק */


     /* כפתור הסבר */
    .explanation-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background: linear-gradient(to bottom, #5cb874, #4cae66); /* גרדיאנט ירוק */
        color: white;
        border: none;
        border-radius: 6px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        font-weight: bold;
    }

    .explanation-button:hover {
        background: linear-gradient(to bottom, #4cae66, #3c9d55);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px); /* אפקט לחיצה קטן */
    }

     .explanation-button:active {
         transform: translateY(0);
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
     }

    /* תיבת הסבר */
    .explanation-box {
        margin-top: 20px;
        padding: 25px;
        border: 1px solid #cce0f2;
        background-color: #eef7ff;
        border-radius: 12px;
        text-align: right;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }

    .explanation-box p {
        margin-bottom: 15px;
    }

    .explanation-box ul {
        list-style-type: disc;
        padding-right: 25px; /* רווח לרשימה */
        margin-bottom: 15px;
    }

     .explanation-box ul li {
        margin-bottom: 8px;
     }

    .image-placeholder {
        text-align: center;
        margin: 20px 0;
        font-style: italic;
        color: #777;
        padding: 20px;
        border: 1px dashed #aed6f1;
        border-radius: 8px;
        background-color: #f9f9f9;
    }

     math { /* סגנון לנוסחאות מתמטיות */
        display: block;
        text-align: center;
        margin: 20px 0;
        font-size: 1.1em;
        direction: ltr; /* נוסחאות RTL */
     }

    .hidden {
        display: none;
    }

    /* אינדיקטור תדר נצפה - ויזואליזציה פשוטה */
    .freq-indicator {
        width: 100%;
        height: 15px;
        margin-top: 10px;
        border-radius: 4px;
        background: linear-gradient(to right, #4da6ff, #aed6f1, #ff4d4d); /* כחול (נמוך) -> נייח -> אדום (גבוה) */
        position: relative;
        overflow: hidden;
    }

    .freq-indicator::after {
        content: '';
        position: absolute;
        top: 0;
        bottom: 0;
        width: 4px; /* עובי הקו */
        background-color: #333; /* צבע הקו המצביע */
        left: 50%; /* התחל באמצע (תדר מקור) */
        transform: translateX(-50%);
        transition: left 0.3s ease; /* אנימציה לתנועת הקו */
        box-shadow: 0 0 5px rgba(0,0,0,0.3);
    }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const canvas = document.getElementById('dopplerCanvas');
        const ctx = canvas.getContext('2d');
        const sourceSpeedSlider = document.getElementById('sourceSpeed');
        const currentSpeedValueSpan = document.getElementById('currentSpeedValue');
        const perceivedFreqValueSpan = document.getElementById('perceivedFreqValue');
        const sourceFreqValueSpan = document.getElementById('sourceFreqValue');
        const waveSpeedValueSpan = document.getElementById('waveSpeedValue');
        const toggleExplanationButton = document.getElementById('toggleExplanation');
        const explanationDiv = document.getElementById('explanation');
        const freqIndicator = document.getElementById('freqIndicator');

        // --- Simulation Parameters ---
        const waveSpeed = 200; // units per second - Increased for more dynamic visualization
        const sourceFrequency = 2; // waves emitted per second (Hz) - Increased for more waves
        const timePerWave = 1 / sourceFrequency; // seconds per wave
        const waveColor = '#007bff'; // Bright blue for waves
        const sourceColor = '#e74c3c'; // Red for source
        const observerColor = '#2ecc71'; // Green for observer
        const sourcePulseColor = '#f1c40f'; // Yellowish for pulse

        // Source and Observer positions
        const source = { x: canvas.width * 0.25, y: canvas.height / 2, vx: 0, vy: 0, pulse: 0 }; // Start source left of center
        const observer = { x: canvas.width * 0.75, y: canvas.height / 2 }; // Observer right of center

        let waves = [];
        let lastWaveTime = 0; // Time of last wave emission (in simulation seconds)
        let simulationTime = 0; // Total simulation time elapsed

        // Display initial constant values
        sourceFreqValueSpan.textContent = sourceFrequency;
        waveSpeedValueSpan.textContent = waveSpeed;

        // --- Drawing Functions ---
        function drawSource(x, y, pulseIntensity) {
            const baseRadius = 8;
            const pulseRadius = baseRadius + pulseIntensity * 5; // Animate size based on pulse

            // Draw base circle
            ctx.fillStyle = sourceColor;
            ctx.beginPath();
            ctx.arc(x, y, baseRadius, 0, Math.PI * 2);
            ctx.fill();

            // Draw pulse effect
            if (pulseIntensity > 0) {
                ctx.strokeStyle = sourcePulseColor;
                 ctx.lineWidth = 3;
                 ctx.globalAlpha = pulseIntensity; // Fade out pulse
                ctx.beginPath();
                ctx.arc(x, y, pulseRadius, 0, Math.PI * 2);
                ctx.stroke();
                 ctx.globalAlpha = 1; // Reset alpha
                 ctx.lineWidth = 1; // Reset line width
            }


            ctx.font = '14px Arial';
            ctx.fillStyle = '#000';
            ctx.textAlign = 'center';
            ctx.fillText('מקור', x, y - 20);
        }

        function drawObserver(x, y) {
            ctx.fillStyle = observerColor;
            ctx.beginPath();
            ctx.arc(x, y, 8, 0, Math.PI * 2);
            ctx.fill();
             ctx.font = '14px Arial';
            ctx.fillStyle = '#000';
            ctx.textAlign = 'center';
            ctx.fillText('צופה', x, y + 25);
        }

        function drawWave(emissionX, emissionY, radius, opacity) {
            ctx.strokeStyle = waveColor;
            ctx.globalAlpha = opacity; // Fade out older waves
            ctx.lineWidth = 2; // Thicker waves
            ctx.beginPath();
            ctx.arc(emissionX, emissionY, radius, 0, Math.PI * 2);
            ctx.stroke();
            ctx.globalAlpha = 1; // Reset alpha
             ctx.lineWidth = 1; // Reset line width
        }

         // Draw a line connecting source and observer
         function drawConnectingLine(sx, sy, ox, oy) {
             ctx.strokeStyle = '#777';
             ctx.lineWidth = 1;
             ctx.setLineDash([5, 5]); /* קו מקווקו */
             ctx.beginPath();
             ctx.moveTo(sx, sy);
             ctx.lineTo(ox, oy);
             ctx.stroke();
             ctx.setLineDash([]); /* איפוס קו מקווקו */
         }

        // --- Simulation Logic ---
        let lastTimestamp = 0;

        function updateSimulation(timestamp) {
            if (!lastTimestamp) lastTimestamp = timestamp;
            const deltaTime = (timestamp - lastTimestamp) / 1000; // Time in seconds since last frame
            lastTimestamp = timestamp;

            simulationTime += deltaTime; // Accumulate simulation time

            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Update source position
            source.x += source.vx * deltaTime;

            // Apply boundary wrap-around for source for continuous simulation
             if (source.x < -canvas.width * 0.3) source.x = canvas.width + canvas.width * 0.3;
             if (source.x > canvas.width + canvas.width * 0.3) source.x = -canvas.width * 0.3;

            // Update source pulse animation
            if (source.pulse > 0) {
                source.pulse -= deltaTime * 3; // Decay faster
                if (source.pulse < 0) source.pulse = 0;
            }

            // Emit new waves based on simulation time
            // Emit when simulationTime >= lastWaveTime + timePerWave (with tolerance)
            if (simulationTime >= lastWaveTime + timePerWave - 0.01) {
                waves.push({ emissionX: source.x, emissionY: source.y, emissionTime: simulationTime });
                lastWaveTime += timePerWave;
                source.pulse = 1; // Start pulse animation
                // Handle potential catching up if frame rate is low
                 while(simulationTime >= lastWaveTime + timePerWave - 0.01) {
                     lastWaveTime += timePerWave;
                 }
            }


            // Update and draw waves
            // Filter waves that are too large or far off-screen
            waves = waves.filter(wave => {
                const radius = waveSpeed * (simulationTime - wave.emissionTime);
                const waveIsVisible = wave.emissionX + radius > 0 && wave.emissionX - radius < canvas.width &&
                                      wave.emissionY + radius > 0 && wave.emissionY - radius < canvas.height;
                const waveIsNotTooBig = radius < Math.max(canvas.width, canvas.height) * 1.5; // Limit max size

                return waveIsVisible && waveIsNotTooBig;
            });


            waves.forEach(wave => {
                const radius = waveSpeed * (simulationTime - wave.emissionTime);
                 const maxRadius = Math.max(canvas.width, canvas.height) * 1.5;
                 const opacity = 1 - Math.pow(radius / maxRadius, 0.5); // Fade out older waves non-linearly
                 if (opacity > 0.1) { // Only draw if reasonably visible
                    drawWave(wave.emissionX, wave.emissionY, radius, opacity);
                 }
            });

             // Draw connecting line
            drawConnectingLine(source.x, source.y, observer.x, observer.y);


             // Draw source and observer AFTER waves for visibility
            drawSource(source.x, source.y, source.pulse);
            drawObserver(observer.x, observer.y);


            // Calculate and display perceived frequency
            // Formula: f' = f0 * vw / (vw + vs_radial)
            // vs_radial is the component of source velocity *away* from the observer.
            // Vector from source (sx, sy) to observer (ox, oy) is (ox-sx, oy-sy) = (dx, dy).
            // Source velocity vector is (vx, vy).
            // vs_radial = dot product of source velocity (vx, vy) and normalized vector from source to observer (dx/dist, dy/dist)
            // vs_radial = (vx * dx + vy * dy) / dist
            const dx = observer.x - source.x;
            const dy = observer.y - source.y; // dy is 0 in this horizontal movement case
            const dist = Math.sqrt(dx * dx + dy * dy);
            let vs_radial = 0;
            if (dist > 1) { // Avoid division by very small numbers
                 vs_radial = (source.vx * dx + source.vy * dy) / dist; // This is velocity component AWAY from observer
            }

            // f' = f0 * vw / (vw - vs_towards_observer)
            // vs_towards_observer = -vs_radial
            const perceivedFrequency = sourceFrequency * waveSpeed / (waveSpeed - (-vs_radial));


            // Update perceived frequency display and indicator
            const clampedPerceivedFrequency = Math.max(0, perceivedFrequency); // Prevent negative freq if source speed > wave speed towards observer
            perceivedFreqValueSpan.textContent = clampedPerceivedFrequency.toFixed(2);

            // Update visual indicator position and color
            const freqRatio = clampedPerceivedFrequency / sourceFrequency; // Ratio to original frequency
            // Map ratio to a position between 0 (low) and 1 (high)
            // Need to handle cases where freqRatio is very large or very small
            let indicatorPosition = 0.5; // Default to center (original freq)
            if (freqRatio > 1) { // Higher frequency
                // Map 1 -> 0.5, larger numbers towards 1 (right side)
                indicatorPosition = 0.5 + (Math.min(freqRatio - 1, 2)) * 0.25; // Cap at freqRatio=3 mapping to 1 (right end)
                 perceivedFreqValueSpan.className = 'value-display perceived-freq high';
            } else if (freqRatio < 1) { // Lower frequency
                // Map 1 -> 0.5, smaller numbers towards 0 (left side)
                 indicatorPosition = 0.5 - (Math.min(1 - freqRatio, 1)) * 0.5; // Cap at freqRatio=0 mapping to 0 (left end)
                 perceivedFreqValueSpan.className = 'value-display perceived-freq low';
            } else { // freqRatio == 1
                 indicatorPosition = 0.5;
                 perceivedFreqValueSpan.className = 'value-display perceived-freq'; // Reset class
            }


             freqIndicator.style.setProperty('--indicator-pos', `${indicatorPosition * 100}%`);
             // Use CSS transition for smooth movement

            requestAnimationFrame(updateSimulation);
        }

        // --- Event Listeners ---
        sourceSpeedSlider.addEventListener('input', (event) => {
             // Slider value directly sets the source's horizontal velocity
            source.vx = parseFloat(event.target.value);
             // Update the displayed speed value
            currentSpeedValueSpan.textContent = `${source.vx.toFixed(0)} יח'/שנייה`;
        });


        toggleExplanationButton.addEventListener('click', () => {
            explanationDiv.classList.toggle('hidden');
            // Optional: change button text based on state
            if (explanationDiv.classList.contains('hidden')) {
                toggleExplanationButton.textContent = 'רוצה להבין לעומק? הצג/הסתר הסבר פיזיקלי';
                 toggleExplanationButton.style.backgroundColor = '#5cb874'; // Reset button color
            } else {
                 toggleExplanationButton.textContent = 'הסתר הסבר פיזיקלי';
                 toggleExplanationButton.style.backgroundColor = '#d9534f'; /* אדום */
            }
        });

         // Initialize the indicator position
         freqIndicator.style.setProperty('--indicator-pos', '50%');
         // Add pseudo-element CSS rule via JS as it's hardcoded above
         const styleSheet = document.styleSheets[document.styleSheets.length - 1];
         const freqIndicatorRule = Array.from(styleSheet.cssRules).find(rule => rule.selectorText === '.freq-indicator::after');
         if(freqIndicatorRule) {
             freqIndicatorRule.style.setProperty('left', 'var(--indicator-pos)');
         }


        // Start the simulation loop
        requestAnimationFrame(updateSimulation);

         // Initial perceived frequency calculation (before loop starts)
         const initialDx = observer.x - source.x;
         const initialDy = observer.y - source.y;
         const initialDist = Math.sqrt(initialDx * initialDx + initialDy * initialDy);
         let initialVsRadial = 0;
         if (initialDist > 1) {
              initialVsRadial = (source.vx * initialDx + source.vy * initialDy) / initialDist;
         }
         const initialPerceivedFrequency = sourceFrequency * waveSpeed / (waveSpeed - (-initialVsRadial));
         perceivedFreqValueSpan.textContent = initialPerceivedFrequency.toFixed(2);

    });
</script>
```