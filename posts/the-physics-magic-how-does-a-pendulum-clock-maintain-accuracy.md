---
title: "ריקוד הזמן הגדול: הסוד הפיזיקלי מאחורי דיוק שעוני המטוטלת"
english_slug: the-physics-magic-how-does-a-pendulum-clock-maintain-accuracy
category: "מדעים מדויקים / פיזיקה"
tags: [פיזיקה, שעון מטוטלת, תנועה מחזורית, מכניקה, זמן]
---
# ריקוד הזמן הגדול: הסוד הפיזיקלי מאחורי דיוק שעוני המטוטלת

במשך מאות שנים, שעוני המטוטלת היו השליטים הבלתי מעורערים של מדידת הזמן. איך הצליח מנגנון פשוט לכאורה, של משקולת מתנדנדת, להפוך לסמל של דיוק ויציבות? הצטרפו אלינו למסע מרתק אל ליבת המכניקה והפיזיקה, וגלו את ההמצאה הגאונית שהפכה מטוטלת רגילה לשומר זמן בלתי רגיל. צללו לסימולציה האינטראקטיבית, התנסו בעצמכם, וגלו את הסוד!

<div id="pendulum-app">
    <canvas id="pendulumCanvas" width="700" height="550"></canvas>
    <div class="controls">
        <button id="playPauseBtn" class="control-button">התחל</button>
        <button id="toggleEscapementBtn" class="control-button">הפעל מנגנון בריחה</button>
        <div class="parameter-control">
            <label for="lengthSlider">אורך המטוטלת (מטרים): <span id="lengthValue">1.00</span></label>
            <input type="range" id="lengthSlider" min="0.5" max="2" value="1" step="0.01">
        </div>
        <div class="parameter-control">
            <label for="angleSlider">זווית התחלתית (מעלות): <span id="angleValue">30</span></label>
            <input type="range" id="angleSlider" min="0" max="60" value="30" step="1">
        </div>
        <div class="parameter-control">
            <label for="dampingSlider">חיכוך (0 = אין חיכוך): <span id="dampingValue">0.10</span></label>
            <input type="range" id="dampingSlider" min="0" max="0.5" value="0.1" step="0.01">
        </div>
        <div class="time-display">
            <div>זמן השעון (שניות): <span id="simTime" class="time-value">0.00</span></div>
            <div>זמן אידיאלי (שניות): <span id="idealTime" class="time-value">0.00</span></div>
            <div>הפרש (שניות): <span id="timeDiff" class="time-value">0.00</span></div>
        </div>
         <div class="help-text">
            <p><strong>איך להתנסות?</strong></p>
            <p>לחצו "התחל" כדי לראות את המטוטלת נעה בחופשיות.</p>
            <p><strong>כשהמנגנון כבוי:</strong> המטוטלת תאבד אנרגיה (אלא אם החיכוך אפס) ותיעצר. "זמן השעון" <strong>לא</strong> יתקדם.</p>
            <p><strong>כשהמנגנון מופעל:</strong> המנגנון דוחף את המטוטלת ומקדם את "זמן השעון". בדקו איך שינוי האורך והזווית משפיעים על דיוק השעון בהשוואה ל"זמן האידיאלי".</p>
        </div>
    </div>
</div>

<button id="showExplanationBtn" class="explanation-button">הצג/הסתר את סוד הדיוק</button>

<div id="explanation" style="display: none;">
    <h2>גילוי הסוד: הקסם הפיזיקלי מאחורי שעוני המטוטלת</h2>

    <h3>מבוא היסטורי וטכנולוגי: למה מטוטלת?</h3>
    לפני הופעת שעוני המטוטלת במאה ה-17, מדידת זמן מדויקת הייתה אתגר משמעותי. המצאתו של כריסטיאן הויגנס, שהשתמש במטוטלת כמנגנון העיקרי לוויסות קצב השעון, חוללה מהפכה. פתאום ניתן היה למדוד זמן בדיוק חסר תקדים, דבר שהיה חיוני לא רק בחיי היום-יום, אלא גם למדעים כמו אסטרונומיה ופיזיקה, ולצרכים פרקטיים כמו ניווט בים. שעון המטוטלת הפך ללב הפועם של המדע והטכנולוגיה במשך דורות.

    <h3>הבסיס הפיזיקלי: הריקוד הקבוע של מטוטלת אידיאלית</h3>
    מטוטלת פשוטה, במודל הפיזיקלי האידיאלי, היא למעשה ריקוד של אנרגיה: כוח הכבידה מושך את המשקולת מטה, גורם לה לצבור מהירות (אנרגיה קינטית), שהופכת שוב לאנרגיה פוטנציאלית כשהיא מתרוממת לצד השני. עבור זוויות נדנוד קטנות, הפלא הוא שתקופת המחזור – הזמן שלוקח למטוטלת להשלים נדנוד שלם (קדימה ואחורה) – תלויה כמעט אך ורק באורך המוט ובתאוצת הכבידה המקומית. הנוסחה המפורסמת T = 2π√(L/g) מגלה שבאופן מפתיע, תקופת המחזור אינה תלויה במסת המשקולת או, חשוב מכל, בזווית הסטייה ההתחלתית! זוהי תכונה קסומה שהופכת את המטוטלת למועמדת אידיאלית לשומר זמן קבוע.

    <h3>התמודדות עם המציאות: האתגרים שמטוטלת "אמיתית" מציבה</h3>
    אך העולם האמיתי אינו אידיאלי. מטוטלת אמיתית מתמודדת עם "כוחות מעכבים":
    *   **חיכוך והתנגדות אוויר:** בכל שנייה שעוברת, כוחות אלו "גוזלים" מעט אנרגיה מהמטוטלת.
    *   **דעיכה:** איבוד האנרגיה גורם למשרעת הנדנוד (הזווית המקסימלית) לקטון בהדרגה. הנדנוד נחלש עד שלבסוף המטוטלת נעצרת.
    *   **תלות בזווית:** הנוסחה האידיאלית נכונה רק לזוויות קטנות. בזוויות גדולות יותר, תקופת המחזור כן תלויה בזווית. משמעות הדבר היא שדעיכה במשרעת לא רק מחלישה את הנדנוד, אלא גם משנה את קצב השעון!
    *   **שינויי טמפרטורה:** שינויים זעירים בטמפרטורה משפיעים על אורך המוט (התפשטות והתכווצות), וכידוע מהנוסחה, שינוי באורך משנה את תקופת המחזור.

    <h3>ההמצאה המבריקה: מנגנון הבריחה (Escapement) נכנס לפעולה</h3>
    כאן נכנסת לתמונה הגאונות ההנדסית: מנגנון הבריחה. מנגנון זה הוא הלב הפועם של שעון המטוטלת, והוא פותר שתי בעיות קריטיות בבת אחת:
    1.  **הזנת אנרגיה:** הוא מספק בעדינות דחיפה קטנה למטוטלת בכל נדנוד, בדיוק בכמות הנדרשת כדי לפצות על איבוד האנרגיה ולשמור על משרעת נדנוד קבועה.
    2.  **וויסות קצב השעון:** הוא מתרגם את תנועת המטוטלת (הקבועה, בזכות הזנת האנרגיה) לתנועה מדויקת של גלגלי השיניים המניעים את מחוגי השעון.

    <h3>ריקוד השיניים והעוגן: כך עובד מנגנון הבריחה (בפשטות)</h3>
    תארו לעצמכם גלגל שיניים תחת לחץ קבוע (ממשקולות או קפיץ). מנגנון הבריחה כולל מעין "עוגן" דו-זרועי המחובר למטוטלת. בכל פעם שהמטוטלת עוברת בנקודת מסוימת (בדרך כלל סמוך למרכז התנועה), העוגן "משחרר" לרגע קצר שן אחת של גלגל הבריחה ("בריחה"). גלגל הבריחה מסתובב מעט, והשן הבאה נתקעת בחלק אחר של העוגן ונעצרת שוב. תוך כדי השחרור והבלימה הזו, העוגן מקבל מכה או דחיפה קטנה מגלגל הבריחה – זוהי הדחיפה שמחזירה אנרגיה למטוטלת ושומרת על הנדנוד. כל "בריחה" כזו מקדמת את גלגלי השעון במידה קבועה ומדויקת.

    <h3>סיכום: סימפוניה של פיזיקה והנדסה</h3>
    שעון מטוטלת הוא הרבה יותר ממשקולת מתנדנדת. הוא יצירת מופת המשלבת את העיקרון הפיזיקלי העוצמתי של תנודה מחזורית קבועה עם מנגנון מכני גאוני שמזין אנרגיה ומווסת את הקצב. השילוב ההרמוני הזה מבטיח שהמטוטלת תמשיך לרקוד את הריקוד שלה במשרעת קבועה ובתקופת מחזור כמעט אידיאלית, ובכך יאפשר לשעון למדוד זמן בדיוק עקבי לאורך שנים רבות. הסימולציה שבה התנסיתם מראה בבירור: ללא מנגנון הבריחה, הדיוק אובד כשהמטוטלת דועכת. המנגנון הוא הקסם ההופך אותה לכרונומטר אמין.

</div>

<script>
    const canvas = document.getElementById('pendulumCanvas');
    const ctx = canvas.getContext('2d');
    const playPauseBtn = document.getElementById('playPauseBtn');
    const toggleEscapementBtn = document.getElementById('toggleEscapementBtn');
    const lengthSlider = document.getElementById('lengthSlider');
    const angleSlider = document.getElementById('angleSlider');
    const dampingSlider = document.getElementById('dampingSlider');
    const lengthValueSpan = document.getElementById('lengthValue');
    const angleValueSpan = document.getElementById('angleValue');
    const dampingValueSpan = document.getElementById('dampingValue');
    const simTimeSpan = document.getElementById('simTime');
    const idealTimeSpan = document.getElementById('idealTime');
    const timeDiffSpan = document.getElementById('timeDiff');
    const showExplanationBtn = document.getElementById('showExplanationBtn');
    const explanationDiv = document.getElementById('explanation');

    // Physics constants and state
    const g = 9.81; // acceleration due to gravity
    let L = parseFloat(lengthSlider.value); // Length of pendulum (meters)
    let initialTheta = parseFloat(angleSlider.value) * (Math.PI / 180); // Initial angle (radians)
    let damping = parseFloat(dampingSlider.value); // Damping factor (0 to 1, affects alpha)
    const boostFactor = 0.1; // Factor for escapement impulse (velocity boost)
    const physics_dt = 0.005; // Time step for physics calculation (seconds - smaller for more precision)

    let theta = initialTheta; // current angle
    let dtheta = 0; // current angular velocity

    let running = false;
    let escapementEnabled = false;
    let animationFrameId = null;
    let lastTimestamp = 0;
    let elapsedRealTime = 0; // Total real time the simulation has run

    // Clock state
    let simTime = 0; // Time shown by the simulated clock (increments per swing)
    let idealTime = 0; // Time based on the ideal pendulum period (increments per ideal period)
    let gearAngle = 0; // Angle of the escapement gear visual
    const gearNumTeeth = 12; // Number of teeth on the escapement gear
    const gearStepAngle = (Math.PI * 2) / gearNumTeeth; // Visual gear rotation per tooth
    let halfPeriodsCompleted = 0; // Count zero crossings to track periods

    let lastThetaSign = Math.sign(theta) || 1; // For detecting zero crossings (handle initial 0 angle)
    let isBoosting = false; // State variable for animation feedback
    let boostTimer = 0; // Timer for boost animation duration

    // Drawing constants and scaling
    const canvasWidth = canvas.width;
    const canvasHeight = canvas.height;
    const pivotX = canvasWidth / 2;
    const pivotY = 80;
    const bobRadius = 18;
    const rodColor = '#555';
    const bobColor = '#007bff';
    const pivotColor = '#333';
    const gearColor = '#ffc107'; // Yellow
    const escapementColor = '#dc3545'; // Red
    const boostHighlightColor = '#ffffff'; // White flash

    const pixelsPerMeter = (canvasHeight - pivotY - bobRadius - 20) / 2.0; // Scale L to fit nicely

    // Escapement visual parameters (simplified)
    const escapementPivotY = pivotY + 40;
    const anchorLength = 35;
    const palletAngleOffset = Math.PI / 2.5;

    const gearVisualRadius = 25;
    const gearVisualX = pivotX;
    const gearVisualY = escapementPivotY + anchorLength + gearVisualRadius + 5;


    function getIdealPeriod(length) {
        if (length <= 0) return Infinity; // Prevent division by zero
        return 2 * Math.PI * Math.sqrt(length / g);
    }

    function drawPendulum() {
        ctx.clearRect(0, 0, canvasWidth, canvasHeight);

        const displayLength = L * pixelsPerMeter;

        // Calculate bob position
        const bobX = pivotX + displayLength * Math.sin(theta);
        const bobY = pivotY + displayLength * Math.cos(theta);

        // Draw pivot
        ctx.fillStyle = pivotColor;
        ctx.beginPath();
        ctx.arc(pivotX, pivotY, 8, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#000';
        ctx.lineWidth = 1;
        ctx.stroke();

        // Draw rod
        ctx.strokeStyle = rodColor;
        ctx.lineWidth = 4;
        ctx.lineCap = 'round';
        ctx.beginPath();
        ctx.moveTo(pivotX, pivotY);
        ctx.lineTo(bobX, bobY);
        ctx.stroke();

        // Draw bob
        ctx.fillStyle = bobColor;
        ctx.beginPath();
        ctx.arc(bobX, bobY, bobRadius, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#fff'; // White border for contrast
        ctx.lineWidth = 2;
        ctx.stroke();

        // --- Draw Escapement Mechanism (Simplified Visual) ---

        // Draw Gear
        ctx.save(); // Save current canvas state
        ctx.translate(gearVisualX, gearVisualY); // Move origin to gear center
        ctx.rotate(gearAngle); // Rotate canvas for gear rotation

        ctx.fillStyle = gearColor;
        ctx.beginPath();
        ctx.arc(0, 0, gearVisualRadius, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#333';
        ctx.lineWidth = 1;
        ctx.stroke();

        // Draw gear teeth (simplified)
        for (let i = 0; i < gearNumTeeth; i++) {
             const angle = (i / gearNumTeeth) * Math.PI * 2;
             const x1 = gearVisualRadius * Math.cos(angle);
             const y1 = gearVisualRadius * Math.sin(angle);
             const x2 = (gearVisualRadius + 8) * Math.cos(angle);
             const y2 = (gearVisualRadius + 8) * Math.sin(angle);
             ctx.beginPath();
             ctx.moveTo(x1, y1);
             ctx.lineTo(x2, y2);
             ctx.stroke();
        }
        ctx.restore(); // Restore canvas state

        // Draw Anchor (moves with pendulum)
        // Position the anchor pivot slightly below main pivot
        const anchorPivotX = pivotX;
        const anchorPivotY = pivotY + 40;

        // Calculate anchor pallet positions based on pendulum angle
        const currentPendulumAngle = theta; // Anchor angle directly tied to pendulum angle (simplification)
        const p1x = anchorPivotX + anchorLength * Math.sin(currentPendulumAngle - palletAngleOffset);
        const p1y = anchorPivotY + anchorLength * Math.cos(currentPendulumAngle - palletAngleOffset);
        const p2x = anchorPivotX + anchorLength * Math.sin(currentPendulumAngle + palletAngleOffset);
        const p2y = anchorPivotY + anchorLength * Math.cos(currentPendulumAngle + palletAngleOffset);

        ctx.strokeStyle = escapementColor;
        ctx.lineWidth = 6;
        ctx.lineCap = 'round';

        ctx.beginPath();
        ctx.moveTo(anchorPivotX, anchorPivotY);
        ctx.lineTo(p1x, p1y);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(anchorPivotX, anchorPivotY);
        ctx.lineTo(p2x, p2y);
        ctx.stroke();

        // Add a central hub for the anchor
        ctx.fillStyle = escapementColor;
        ctx.beginPath();
        ctx.arc(anchorPivotX, anchorPivotY, 5, 0, Math.PI * 2);
        ctx.fill();


        // Indicate connection from anchor pivot to pendulum rod visual point
        const connectionPointDist = displayLength * 0.8; // Visual connection point along rod
        const connectionX = pivotX + connectionPointDist * Math.sin(theta);
        const connectionY = pivotY + connectionPointDist * Math.cos(theta);

        ctx.strokeStyle = escapementColor;
        ctx.lineWidth = 2;
        ctx.setLineDash([5, 5]); // Dashed line for visual connection
        ctx.beginPath();
        ctx.moveTo(anchorPivotX, anchorPivotY);
        ctx.lineTo(connectionX, connectionY);
        ctx.stroke();
        ctx.setLineDash([]); // Reset line style


        // Add visual boost feedback
        if (isBoosting) {
            const boostRadius = bobRadius + 5 + (boostTimer * 10); // Expand slightly
            const boostAlpha = 1.0 - (boostTimer / 0.1); // Fade out quickly
            if (boostAlpha > 0) {
                ctx.fillStyle = `rgba(255, 255, 255, ${boostAlpha})`;
                ctx.beginPath();
                ctx.arc(bobX, bobY, boostRadius, 0, Math.PI * 2);
                ctx.fill();
            }
        }
    }

    function updatePhysics(dt) {
        const steps = Math.ceil(dt / physics_dt);
        const micro_dt = dt / steps;

        for (let i = 0; i < steps; i++) {
            // Physics: Angular acceleration (includes damping)
            // alpha = -g/L * sin(theta) - damping * angular_velocity
            const alpha = -(g / L) * Math.sin(theta) - damping * dtheta;

            // Save previous angle sign before updating theta
            const prevThetaSign = Math.sign(theta) || lastThetaSign; // Use last known sign if theta is 0

            // Update angular velocity and angle using Euler method
            dtheta += alpha * micro_dt;
            theta += dtheta * micro_dt;

            // Escapement logic: Detect zero crossing and apply boost/clock step
            const currentThetaSign = Math.sign(theta) || prevThetaSign; // Use prev sign if theta is 0 now

            if (currentThetaSign !== prevThetaSign && prevThetaSign !== 0 && currentThetaSign !== 0) {
                // Zero crossing detected (theta changed sign)
                 halfPeriodsCompleted++;

                 if (escapementEnabled) {
                     // Apply impulse/boost at the crossing
                     dtheta += boostFactor;
                     isBoosting = true; // Start boost animation
                     boostTimer = 0;

                     // Advance simulated clock every two half-periods (i.e., every full period)
                     if (halfPeriodsCompleted % 2 === 0) {
                         simTime += 1;
                         // Advance gear visually for one tooth per full period (or per half? Per half seems better visual tick)
                         // Let's advance gear per crossing (half period)
                          gearAngle += gearStepAngle;
                     }
                 }
            }
            lastThetaSign = currentThetaSign;

            // Update boost timer
            if(isBoosting) {
                 boostTimer += micro_dt;
                 if (boostTimer > 0.1) { // Boost animation duration
                     isBoosting = false;
                 }
            }
        }
    }

    function animationLoop(timestamp) {
        if (!lastTimestamp) {
            lastTimestamp = timestamp;
        }

        const dt = (timestamp - lastTimestamp) / 1000; // time elapsed in seconds
        lastTimestamp = timestamp;

        if (running) {
            elapsedRealTime += dt; // Accumulate real time if running
            updatePhysics(dt);
        } else {
             // When paused, still update boost timer to fade out any ongoing animation
             if(isBoosting) {
                boostTimer += dt; // Use real dt even if not running physics
                 if (boostTimer > 0.1) {
                    isBoosting = false;
                 }
             }
        }


        drawPendulum();
        updateDisplay();

        animationFrameId = requestAnimationFrame(animationLoop);
    }

    function updateDisplay() {
        // Ideal time based on the current length L and elapsed real time
        const idealPeriod = getIdealPeriod(L);
        // Ideal time represents the number of seconds that *should* have passed if the pendulum
        // was ideal and each full period corresponds to 1 "clock second".
        idealTime = elapsedRealTime / idealPeriod; // This counts ideal periods as seconds

        // simTime is already updated in the physics loop, incrementing by 1 per full period.
        // Both simTime and idealTime now represent elapsed "clock seconds", where 1 second = 1 ideal period duration.

        simTimeSpan.textContent = simTime.toFixed(2);
        idealTimeSpan.textContent = idealTime.toFixed(2);

        const diff = simTime - idealTime;
        timeDiffSpan.textContent = diff.toFixed(3); // More precision for diff

        // Update diff span color based on value
        const diffAbs = Math.abs(diff);
        if (diffAbs < 0.05) {
            timeDiffSpan.style.color = '#28a745'; // Green
        } else if (diffAbs < 0.5) {
            timeDiffSpan.style.color = '#ffc107'; // Yellow
        } else {
            timeDiffSpan.style.color = '#dc3545'; // Red
        }


        // Display current angle (for parameter control consistency, although not a slider output)
        // angleValueSpan.textContent = (theta * 180 / Math.PI).toFixed(0); // Display current angle is distracting, show initial angle instead
         lengthValueSpan.textContent = L.toFixed(2);
         angleValueSpan.textContent = (initialTheta * 180 / Math.PI).toFixed(0); // Display initial angle from slider
         dampingValueSpan.textContent = damping.toFixed(2);

    }

    function resetSimulation() {
        // Stop simulation briefly if running, to reset state cleanly
        const wasRunning = running;
        running = false;
        // No need to cancel animation frame, the loop checks `running` flag

        theta = initialTheta;
        dtheta = 0;
        simTime = 0;
        idealTime = 0;
        elapsedRealTime = 0;
        gearAngle = 0;
        halfPeriodsCompleted = 0;
        lastThetaSign = Math.sign(initialTheta) || 1; // Reset sign
        isBoosting = false; // Reset animation state
        boostTimer = 0;


        drawPendulum();
        updateDisplay();

        // Restart if it was running before reset
        if (wasRunning) {
             running = true;
             // animationFrameId = requestAnimationFrame(animationLoop); // animationLoop is already running
        }
         lastTimestamp = 0; // Reset timestamp for smooth resume
    }

    // Event Listeners
    playPauseBtn.addEventListener('click', () => {
        running = !running;
        playPauseBtn.textContent = running ? 'השהה' : 'התחל';
        playPauseBtn.style.backgroundColor = running ? '#ffc107' : '#28a745'; // Yellow when paused, Green when playing
        playPauseBtn.style.color = running ? '#333' : 'white';

        if (running) {
             lastTimestamp = 0; // Reset timestamp for accurate dt on resume
             // If animation loop was stopped (shouldn't be based on logic), restart it here.
             // animationFrameId = requestAnimationFrame(animationLoop); // It runs continuously, just checks 'running'
        }
    });

    toggleEscapementBtn.addEventListener('click', () => {
        escapementEnabled = !escapementEnabled;
        toggleEscapementBtn.textContent = escapementEnabled ? 'כבה מנגנון בריחה' : 'הפעל מנגנון בריחה';
        toggleEscapementBtn.style.backgroundColor = escapementEnabled ? '#dc3545' : '#007bff'; // Red when on, Blue when off
         toggleEscapementBtn.style.color = 'white';
        // Optional: Reset or slightly nudge the pendulum to show immediate effect?
        // Let it continue, the effect will be seen as damping stops reducing amplitude.
    });

    lengthSlider.addEventListener('input', (e) => {
        L = parseFloat(e.target.value);
        // lengthValueSpan.textContent = L.toFixed(2); // Updated in updateDisplay
        resetSimulation(); // Reset when length changes as period changes
    });

    angleSlider.addEventListener('input', (e) => {
        // Update initial angle, but only apply it on reset
        initialTheta = parseFloat(e.target.value) * (Math.PI / 180);
        // angleValueSpan.textContent = e.target.value; // Updated in updateDisplay
        resetSimulation(); // Reset to new initial angle
    });

     dampingSlider.addEventListener('input', (e) => {
        damping = parseFloat(e.target.value);
        // dampingValueSpan.textContent = damping.toFixed(2); // Updated in updateDisplay
        // No reset needed, damping changes dynamically
    });

    showExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        showExplanationBtn.textContent = isHidden ? 'הסתר את סוד הדיוק' : 'הצג/הסתר את סוד הדיוק';
    });


    // Initial setup
    resetSimulation();
    animationLoop(0); // Start the animation loop (it will be paused initially)

</script>

<style>
    #pendulum-app {
        display: flex;
        flex-direction: column;
        align-items: center;
        font-family: 'Arial', sans-serif; /* Use a common system font */
        margin-bottom: 30px;
        border: 1px solid #e0e0e0; /* Softer border */
        padding: 20px;
        border-radius: 12px; /* More rounded corners */
        background-color: #f8f8f8; /* Lighter background */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }

    #pendulumCanvas {
        border: 1px solid #a0a0a0; /* Slightly darker border for canvas */
        background: linear-gradient(to bottom, #eef, #ddf); /* Subtle gradient background */
        display: block;
        margin-bottom: 20px;
        border-radius: 8px;
    }

    .controls {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px; /* Increased gap */
        width: 100%;
        max-width: 700px; /* Match canvas width */
        padding: 10px;
    }

    .controls button {
        padding: 12px 20px; /* More padding */
        font-size: 1.1rem; /* Larger font */
        cursor: pointer;
        border: none;
        border-radius: 6px; /* Rounded buttons */
        transition: background-color 0.2s ease, transform 0.1s ease; /* Smooth transitions */
        font-weight: bold;
    }

     .controls button:hover {
        transform: translateY(-2px); /* Lift button on hover */
     }
      .controls button:active {
        transform: translateY(0); /* Press effect */
      }

    #playPauseBtn {
        background-color: #28a745; /* Green */
        color: white;
    }


    #toggleEscapementBtn {
        background-color: #007bff; /* Blue */
        color: white;
    }


    .parameter-control {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        width: calc(50% - 10px); /* Two columns with gap */
        min-width: 250px; /* Minimum width */
        background-color: #fff;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 15px;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
    }

     @media (max-width: 600px) {
        .parameter-control {
            width: 100%; /* Stack on smaller screens */
        }
     }


    .parameter-control label {
        margin-bottom: 8px; /* More space */
        font-weight: bold;
        font-size: 1rem;
        color: #333;
        width: 100%; /* Full width label */
        display: flex;
        justify-content: space-between; /* Value on the right */
        align-items: center;
    }
    .parameter-control label span {
         font-weight: normal;
         color: #007bff; /* Highlight value */
    }


    .parameter-control input[type="range"] {
        width: 100%;
        margin-bottom: 0;
        cursor: grab;
         -webkit-appearance: none;
         appearance: none;
         height: 8px;
         background: #d3d3d3;
         outline: none;
         opacity: 0.7;
         transition: opacity 0.2s;
         border-radius: 4px;
    }

     .parameter-control input[type="range"]:hover {
        opacity: 1;
     }

    /* Custom slider thumb */
    .parameter-control input[type="range"]::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 20px;
      height: 20px;
      background: #007bff;
      cursor: grab;
      border-radius: 50%;
      border: 2px solid #fff;
      box-shadow: 0 2px 4px rgba(0,0,0,0.2);
      transition: background-color 0.2s ease;
    }

    .parameter-control input[type="range"]::-moz-range-thumb {
      width: 20px;
      height: 20px;
      background: #007bff;
      cursor: grab;
      border-radius: 50%;
      border: 2px solid #fff;
      box-shadow: 0 2px 4px rgba(0,0,0,0.2);
       transition: background-color 0.2s ease;
    }
     .parameter-control input[type="range"]::-webkit-slider-thumb:active,
     .parameter-control input[type="range"]::-moz-range-thumb:active {
         cursor: grabbing;
         background-color: #0056b3;
     }


    .time-display {
        width: calc(50% - 10px); /* Two columns with gap */
         min-width: 250px;
        background-color: #fff;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 15px;
        font-size: 1.1rem;
        color: #333;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
        font-weight: bold;
    }
     @media (max-width: 600px) {
        .time-display {
            width: 100%; /* Stack on smaller screens */
        }
     }

    .time-display div {
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
    }
     .time-display div:last-child {
        margin-bottom: 0;
     }

    .time-value {
        font-weight: normal;
        color: #0056b3; /* Default blue for values */
    }
     /* Colors for timeDiff are set via JS */


    .help-text {
        width: 100%;
        max-width: 700px;
        margin-top: 20px;
        padding: 15px;
        border: 2px dashed #007bff;
        border-radius: 8px;
        background-color: #e9f7ff;
        font-size: 1rem;
        color: #333;
        line-height: 1.5;
    }
     .help-text p {
        margin: 8px 0;
     }
      .help-text strong {
         color: #0056b3;
      }


    .explanation-button {
        display: block;
        margin: 30px auto; /* Centered, more space */
        padding: 12px 25px; /* More padding */
        font-size: 1.1rem; /* Larger font */
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #6c757d; /* Grey */
        color: white;
        transition: background-color 0.2s ease, transform 0.1s ease;
        font-weight: bold;
    }
     .explanation-button:hover {
        background-color: #5a6268;
         transform: translateY(-2px);
     }
      .explanation-button:active {
         transform: translateY(0);
      }


    #explanation {
        border: 1px solid #c3e6cb; /* Greenish border */
        background-color: #d4edda; /* Greenish background */
        color: #155724; /* Dark green text */
        padding: 20px;
        margin-top: 20px;
        border-radius: 8px;
        line-height: 1.7; /* Increased line spacing */
        font-size: 1.1rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }

    #explanation h2,
    #explanation h3 {
        color: #0c5460; /* Dark teal color for headings */
        margin-top: 20px;
        margin-bottom: 12px;
        border-bottom: 1px solid #b2dfdb; /* Subtle separator */
        padding-bottom: 5px;
    }
    #explanation h2 {
        margin-top: 0;
    }

    #explanation p {
        margin-bottom: 15px;
    }

    /* General body improvements */
    body {
        line-height: 1.6;
        color: #333;
        direction: rtl; /* Ensure RTL */
        text-align: right; /* Ensure RTL text alignment */
    }
    h1, h2, h3 {
        text-align: center; /* Center titles */
        color: #004085; /* Dark blue for main headings */
        margin-bottom: 15px;
    }

    /* Improve link styles if any were added in the explanation */
    a {
        color: #0056b3;
        text-decoration: none;
        transition: color 0.2s ease;
    }
    a:hover {
        color: #003580;
        text-decoration: underline;
    }

</style>
```