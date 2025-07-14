---
title: "כוח הכבידה נגד האתלט: פיזיקת הקפיצה לגובה"
english_slug: physics-of-high-jump
category: "פיזיקה"
tags:
    - פיזיקה
    - קפיצה לגובה
    - ביומכניקה
    - תנועה בליסטית
    - אנרגיה
---
<h1>כוח הכבידה נגד האתלט: פיזיקת הקפיצה לגובה</h1>

<p>האם אי פעם עצרתם לחשוב איך קופצי גובה מרחפים מעל רף שגבוה מכם בהרבה? האם זה רק שרירים אדירים, או שיש כאן גם קסם פיזיקלי? בואו נחקור את המדע שמאחורי אחת מתחרויות האתלטיקה המרתקות ביותר!</p>

<div id="app-container">
    <h2>התנסו: בנו את הקפיצה המושלמת</h2>
    <div class="controls">
        <div>
            <label for="angle">זווית הזינוק (&deg;):</label>
            <input type="range" id="angle" min="10" max="85" value="45">
            <span id="angle-value">45</span>
        </div>
        <div>
            <label for="speed">מהירות הזינוק (מ"ש):</label>
            <input type="range" id="speed" min="4" max="11" value="7">
            <span id="speed-value">7</span>
        </div>
        <button id="jump-button">צאו לדרך!</button>
    </div>
    <div class="simulation-area">
        <canvas id="jump-canvas" width="600" height="400"></canvas>
        <div id="results">גובה מקסימלי שהושג: <span id="peak-height">0.00</span> מטר</div>
         <div id="clearance-message"></div>
    </div>
</div>

<button id="toggle-explanation">רוצים להבין את הפיזיקה? לחצו כאן</button>

<div id="explanation" style="display: none;">
    <h2>הפיזיקה שמאחורי הקפיצה: הצלילה לעומק</h2>
    <p>הקפיצה לגובה היא הרבה מעבר ליכולת אתלטית גולמית – היא הדגמה מרתקת של עקרונות פיזיקליים בסיסיים, במיוחד של <strong>תנועה בליסטית</strong>.</p>

    <h3>הקופץ כקליע: ניתוח פיזיקלי</h3>
    <p>מרגע שהקופץ מנתק מגע מהקרקע, הוא הופך למעין "קליע" אנושי. הכוח הדומיננטי היחיד שפועל עליו (בהזנחת התנגדות האוויר) הוא כוח הכבידה, המושך אותו מטה. לכן, מסלול תנועתו באוויר נקבע אך ורק על ידי מהירות הזינוק ההתחלתית וכוח הכבידה.</p>

    <h3>תנועה בליסטית: המסלול הפרבולי</h3>
    <p>גוף הנזרק באוויר ומושפע רק מכוח כבידה קבוע מבצע תנועה בליסטית, שצורתה היא <strong>פרבולה</strong>. כדי להבין את התנועה, נוח לפרק את מהירות הזינוק ההתחלתית לשני רכיבים שפועלים באופן בלתי תלוי:</p>
    <ul>
        <li><strong>רכיב אופקי (\(v_x\)):</strong> אם מהירות הזינוק הכוללת היא \(v_0\) והזווית היא \(\theta\), הרכיב האופקי הוא \(v_x = v_0 \cos(\theta)\). רכיב זה נשאר קבוע לאורך כל התנועה.</li>
        <li><strong>רכיב אנכי (\(v_y\)):</strong> הרכיב האנכי הוא \(v_y(t) = v_0 \sin(\theta) - gt\). רכיב זה משתנה לאורך זמן בשל השפעת כוח הכבידה (\(g\) היא תאוצת הכבידה). הגובה האנכי בכל רגע נתון הוא \(y(t) = v_0 \sin(\theta) t - \frac{1}{2} g t^2\).</li>
    </ul>

    <h3>זווית ומהירות: השפעתן על הגובה</h3>
    <p><strong>זווית הזינוק (\(\theta\)):</strong> קובעת את חלוקת המהירות הכוללת בין הרכיב האנכי לאופקי. ככל שהזווית גדולה יותר (קרובה ל-90 מעלות), כך רכיב המהירות האנכי גדול יותר. רכיב אנכי גדול יותר מעניק לקופץ "דחיפה" ראשונית חזקה יותר כלפי מעלה, ומאפשר לו להגיע לגובה רב יותר לפני שכוח הכבידה מבלם אותו ומחזיר אותו מטה.</p>
    <p><strong>מהירות הזינוק (\(v_0\)):</strong> קובעת את האנרגיה הקינטית ההתחלתית (\(\frac{1}{2}mv_0^2\)). מהירות גבוהה יותר פירושה יותר אנרגיה שיכולה להמיר לאנרגיה פוטנציאלית (גובה). ככל שקופץ מהיר יותר, כך הוא יכול להגיע לגובה רב יותר עבור אותה זווית זינוק.</p>

    <h3>פסגת המסלול: הגובה המקסימלי</h3>
    <p>הגובה המקסימלי אליו מגיע הקופץ (\(y_{max}\)) מושג כאשר הרכיב האנכי של מהירותו מתאפס. בעזרת הנוסחאות של תנועה בליסטית, ניתן להראות שהגובה המקסימלי מעל נקודת הזינוק נתון על ידי:</p>
    <p class="formula">\[ y_{max} = \frac{v_0^2 \sin^2(\theta)}{2g} \]</p>
    <p>נוסחה זו מדגישה שגובה השיא תלוי בריבוע מהירות הזינוק ו<strong>בריבוע סינוס זווית הזינוק</strong>. תיאורטית, הזווית שתיתן את הגובה המקסימלי עבור מהירות נתונה היא 90 מעלות (קפיצה אנכית לגמרי), שכן \(\sin(90^\circ) = 1\). אך בספורט המעשי, יש צורך גם במהירות אופקית וטכניקה מתאימה (כמו סגנון פוסברי) כדי לעבור את הרף. לכן, הקופצים משלבים בין רכיבים אופקיים ואנכיים ומשתמשים בטכניקה כדי להרים את מרכז הכובד שלהם מעל הרף ביעילות, למרות שמרכז הכובד עצמו עשוי לעבור מתחת לרף בחלק מהזמן! הסימולציה כאן ממדלת את תנועת מרכז הכובד.</p>
</div>

<style>
    /* כללי */
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        direction: rtl;
        text-align: center;
        margin: 0;
        padding: 20px;
        background-color: #eef2f7; /* רקע עדין */
        color: #333;
    }

    h1, h2, h3 {
        color: #0056b3; /* כותרות בכחול עמוק */
        text-align: right;
    }

    p {
        text-align: right;
        line-height: 1.7;
    }

    .formula {
        text-align: center;
        margin: 20px 0;
        font-style: italic;
        font-size: 1.1em;
        color: #007bff;
    }

    /* מיכל האפליקציה */
    #app-container {
        background: linear-gradient(to bottom, #ffffff, #f0f0f0); /* רקע הדרגתי עדין */
        border: 1px solid #dcdcdc;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }

    /* בקרי שליטה */
    .controls {
        margin-bottom: 25px;
        display: flex;
        justify-content: center;
        gap: 30px;
        flex-wrap: wrap;
        padding: 10px;
        background-color: #e9ecef; /* רקע בהיר לבקרים */
        border-radius: 8px;
    }

    .controls > div {
        display: flex;
        align-items: center;
        gap: 8px; /* הגדלת המרווח בין הרכיבים */
    }

    label {
        font-weight: bold;
        color: #555;
        min-width: 80px; /* רוחב מינימלי לתוויות */
        text-align: right;
    }

    input[type="range"] {
        width: 180px; /* רוחב סליידר גדול יותר */
        accent-color: #007bff; /* צבע לסליידר */
    }

    /* כפתור קפיצה */
    #jump-button {
        padding: 12px 25px; /* פדינג גדול יותר */
        font-size: 17px;
        cursor: pointer;
        background-color: #28a745; /* ירוק לאינטראקציה ראשית */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    }

    #jump-button:hover {
        background-color: #218838;
        transform: translateY(-1px); /* אפקט ריחוף עדין */
    }
     #jump-button:active {
        background-color: #1e7e34;
        transform: translateY(0);
     }


    /* אזור הסימולציה */
    .simulation-area {
        position: relative;
        width: 600px; /* רוחב קבוע */
        height: 400px; /* גובה קבוע */
        margin: 0 auto;
        border: 2px solid #0056b3; /* מסגרת בצבע הכותרות */
        border-radius: 8px;
        background: linear-gradient(to bottom, #87ceeb, #aed9e0); /* רקע שמיים כחול בהיר */
        overflow: hidden;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1); /* צל פנימי עדין */
    }

    #jump-canvas {
        display: block;
        background-color: transparent; /* שקוף כדי לראות רקע simulation-area */
    }

    /* אזור התוצאות */
    #results {
        margin-top: 15px;
        font-size: 1.2em;
        font-weight: bold;
        color: #0056b3; /* צבע התוצאות כצבע הכותרות */
        min-height: 1.5em; /* Reserve space */
    }

    #clearance-message {
        margin-top: 5px;
        font-size: 1.1em;
        font-weight: bold;
        color: #d9534f; /* אדום כברירת מחדל לכישלון */
        min-height: 1.2em;
    }

    /* כפתור הצגת/הסתרת הסבר */
    #toggle-explanation {
        padding: 12px 20px;
        font-size: 16px;
        cursor: pointer;
        background-color: #007bff; /* כחול לכפתור משני */
        color: white;
        border: none;
        border-radius: 6px;
        margin-bottom: 20px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    }

     #toggle-explanation:hover {
        background-color: #0056b3;
        transform: translateY(-1px);
     }
     #toggle-explanation:active {
        background-color: #004085;
        transform: translateY(0);
     }


    /* אזור ההסבר */
    #explanation {
        border: 1px solid #dcdcdc;
        padding: 20px;
        border-radius: 12px;
        background-color: #f9f9f9; /* רקע בהיר יותר להסבר */
        text-align: right;
        line-height: 1.7;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }

    #explanation h2, #explanation h3 {
        color: #0056b3;
        text-align: right;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    #explanation ul {
        list-style-type: disc;
        margin-right: 25px;
        padding-right: 0; /* ודא שאין פדינג מימין */
    }

     #explanation li {
        margin-bottom: 8px;
     }

    /* רספונסיביות בסיסית */
    @media (max-width: 768px) {
        .simulation-area {
            width: 100%; /* מאפשר התאמה לרוחב מסך קטן */
            height: 300px; /* גובה מופחת במסכים קטנים */
        }
        input[type="range"] {
            width: 120px;
        }
        .controls {
            gap: 15px; /* צמצום מרווחים בבקרים */
        }
         label {
            min-width: auto;
         }
    }
</style>

<script>
    const angleInput = document.getElementById('angle');
    const angleValueSpan = document.getElementById('angle-value');
    const speedInput = document.getElementById('speed');
    const speedValueSpan = document.getElementById('speed-value');
    const jumpButton = document.getElementById('jump-button');
    const canvas = document.getElementById('jump-canvas');
    const ctx = canvas.getContext('2d');
    const peakHeightSpan = document.getElementById('peak-height');
    const clearanceMessageDiv = document.getElementById('clearance-message');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    const G = 9.81; // Gravity (m/s^2)
    const CANVAS_WIDTH = canvas.width;
    const CANVAS_HEIGHT = canvas.height;
    const GROUND_Y = CANVAS_HEIGHT - 20; // Position of the ground line (pixels)
    const SCALE = 25; // Pixels per meter (adjust based on expected max jump distance/height)
    const BAR_HEIGHT_METERS = 2.45; // Target bar height (e.g., World Record)

    let animationFrameId = null; // To store animation frame ID for cancellation

    // Update displayed values when sliders move & draw preview
    angleInput.addEventListener('input', () => {
        angleValueSpan.textContent = angleInput.value;
        drawPreviewPath();
    });

    speedInput.addEventListener('input', () => {
        speedValueSpan.textContent = speedInput.value;
        drawPreviewPath();
    });

    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר הסבר';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'רוצים להבין את הפיזיקה? לחצו כאן';
        }
    });

     // Convert physics coordinates (meters) to canvas coordinates (pixels)
     // Origin (0,0) physics is at (0, GROUND_Y) on canvas
    function toCanvasX(x_meters) {
        return x_meters * SCALE;
    }

    function toCanvasY(y_meters) {
        return GROUND_Y - y_meters * SCALE; // Y increases upwards in physics, downwards in canvas
    }

    // Drawing function
    function draw(jumperX_meters, jumperY_meters, pathPoints, peakY_meters, barY_meters, previewPathPoints) {
        ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);

        // Draw Ground (more detailed)
        ctx.fillStyle = '#4CAF50'; // Green color
        ctx.fillRect(0, GROUND_Y, CANVAS_WIDTH, CANVAS_HEIGHT - GROUND_Y);
        ctx.strokeStyle = '#333';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(0, GROUND_Y);
        ctx.lineTo(CANVAS_WIDTH, GROUND_Y);
        ctx.stroke();

        // Draw Bar
        const barX_start = toCanvasX(5); // Draw bar 5 meters from start point horizontally
        const barHeight_pixels = barY_meters * SCALE;
        const barY_canvas = GROUND_Y - barHeight_pixels; // Top of the bar
        const barWidth = 10; // Width in pixels

        if (barX_start < CANVAS_WIDTH) { // Only draw if bar is on canvas
            ctx.fillStyle = '#f44336'; // Red bar
            ctx.fillRect(barX_start, barY_canvas, barWidth, barHeight_pixels);
        }


        // Draw Preview Path (dashed, light color)
        if (previewPathPoints && previewPathPoints.length > 1) {
            ctx.strokeStyle = '#aed6f1'; // Light blue
            ctx.lineWidth = 2;
            ctx.setLineDash([5, 5]); // Dashed line
            ctx.beginPath();
            ctx.moveTo(toCanvasX(previewPathPoints[0].x), toCanvasY(previewPathPoints[0].y));
            for (let i = 1; i < previewPathPoints.length; i++) {
                 // Only draw points that are above ground + small buffer
                 if (previewPathPoints[i].y * SCALE > -5) { // Allow slightly below ground for preview
                    ctx.lineTo(toCanvasX(previewPathPoints[i].x), toCanvasY(previewPathPoints[i].y));
                 } else {
                     break; // Stop drawing path if it goes significantly below ground
                 }
            }
            ctx.stroke();
            ctx.setLineDash([]); // Reset line dash
        }


        // Draw Path (solid, main color)
        if (pathPoints && pathPoints.length > 1) {
            ctx.strokeStyle = '#007bff'; // Blue
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(toCanvasX(pathPoints[0].x), toCanvasY(pathPoints[0].y));
            for (let i = 1; i < pathPoints.length; i++) {
                 // Only draw points that are above ground + small buffer
                 if (pathPoints[i].y * SCALE > -5) {
                    ctx.lineTo(toCanvasX(pathPoints[i].x), toCanvasY(pathPoints[i].y));
                 } else {
                     break; // Stop drawing path if it goes significantly below ground
                 }
            }
            ctx.stroke();
        }

         // Draw Peak Height Line (dashed, red)
         if (peakY_meters > 0) {
             const peakY_canvas = toCanvasY(peakY_meters);
              if (peakY_canvas > 0) { // Only draw if peak is above canvas top
                 ctx.strokeStyle = '#d9534f'; // Red
                 ctx.lineWidth = 2;
                 ctx.setLineDash([8, 4]); // Dashed line
                 ctx.beginPath();
                 ctx.moveTo(0, peakY_canvas);
                 ctx.lineTo(CANVAS_WIDTH, peakY_canvas);
                 ctx.stroke();
                 ctx.setLineDash([]); // Reset line dash

                 // Add text label for peak height
                 ctx.fillStyle = '#d9534f';
                 ctx.font = '14px Arial';
                 ctx.textAlign = 'left';
                 ctx.fillText(`${peakY_meters.toFixed(2)}m`, 10, peakY_canvas - 5);
              }
         }


        // Draw Jumper (simple rectangle representing body/center of mass)
        const jumperWidth = 8; // pixels
        const jumperHeight = 18; // pixels (represents roughly the body height)
        const drawX = toCanvasX(jumperX_meters);
        const drawY = toCanvasY(jumperY_meters); // This is the Y of the center of mass

        ctx.fillStyle = '#000'; // Black color for the jumper
        // Draw body - rectangle anchored at the bottom center of mass
        // Adjusted to draw from top-left corner
        ctx.fillRect(drawX - jumperWidth / 2, drawY - jumperHeight / 2, jumperWidth, jumperHeight);


        // Draw Takeoff point marker
        ctx.fillStyle = '#555';
        ctx.beginPath();
        ctx.arc(toCanvasX(0), GROUND_Y, 5, 0, Math.PI * 2);
        ctx.fill();
    }

    // Animation function
    function animateJump(angle_deg, speed_m_s) {
        // Cancel any previous animation frame
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
        }

        const angle_rad = angle_deg * Math.PI / 180;
        const v0x = speed_m_s * Math.cos(angle_rad);
        const v0y = speed_m_s * Math.sin(angle_rad);

        // Calculate total time of flight (until y=0)
        const totalTime = 2 * v0y / G;
        const animationDuration = totalTime > 0 ? Math.max(1000, totalTime * 500) : 0; // Scale animation duration, min 1s
        let startTime = null;

        // Calculate peak height
        const t_peak = v0y / G;
        const peakHeight = v0y * t_peak - 0.5 * G * t_peak * t_peak; // meters
        peakHeightSpan.textContent = peakHeight.toFixed(2);

        // Calculate full path points for drawing the trajectory
        const pathPoints = [];
        const stepTime = totalTime / 100; // Calculate 100 points for the path
        for (let t = 0; t <= totalTime * 1.1; t += stepTime) { // Add slightly beyond totalTime to draw landing
            const x = v0x * t;
            const y = v0y * t - 0.5 * G * t * t;
            pathPoints.push({x, y});
        }

        // Reset clearance message
        clearanceMessageDiv.textContent = '';
        clearanceMessageDiv.style.color = '#d9534f'; // Default to fail color


        function frame(timestamp) {
            if (!startTime) startTime = timestamp;
            const elapsedTime = timestamp - startTime;
            let t = (elapsedTime / animationDuration) * totalTime; // Scale time to match totalTime

            const currentX = v0x * t;
            const currentY = v0y * t - 0.5 * G * t * t;

             // Stop animation if jumper goes significantly below ground after start
            if (t > 0.1 && currentY < -0.5) { // Add small threshold for starting point and landing buffer
                 draw(currentX, 0, pathPoints, peakHeight, BAR_HEIGHT_METERS, null); // Draw at landing spot
                 animationFrameId = null; // Clear frame ID
                 // Display clearance message after animation
                 setTimeout(() => { // Delay message slightly
                      if (peakHeight >= BAR_HEIGHT_METERS) {
                        clearanceMessageDiv.textContent = 'עברת את הרף!';
                        clearanceMessageDiv.style.color = '#28a745'; // Green for success
                      } else {
                        clearanceMessageDiv.textContent = 'לא עברת את הרף :(';
                        clearanceMessageDiv.style.color = '#d9534f'; // Red for failure
                      }
                 }, 100); // Small delay

                return; // Stop animation
            }


            draw(currentX, currentY, pathPoints, peakHeight, BAR_HEIGHT_METERS, null); // Draw jumper, path, peak line, bar

            if (t < totalTime) {
               animationFrameId = requestAnimationFrame(frame);
            } else {
                 // Ensure final state is drawn (landing)
                 draw(v0x * totalTime, 0, pathPoints, peakHeight, BAR_HEIGHT_METERS, null);
                 animationFrameId = null; // Clear frame ID
                  // Display clearance message after animation finishes naturally
                 setTimeout(() => { // Delay message slightly
                      if (peakHeight >= BAR_HEIGHT_METERS) {
                        clearanceMessageDiv.textContent = 'עברת את הרף!';
                        clearanceMessageDiv.style.color = '#28a745'; // Green for success
                      } else {
                        clearanceMessageDiv.textContent = 'לא עברת את הרף :(';
                        clearanceMessageDiv.style.color = '#d9534f'; // Red for failure
                      }
                 }, 100); // Small delay
            }
        }

        animationFrameId = requestAnimationFrame(frame);
    }

    // Draw preview path based on current slider values
    function drawPreviewPath() {
         // Cancel ongoing animation if any
         if (animationFrameId) {
             cancelAnimationFrame(animationFrameId);
             animationFrameId = null;
         }

        const angle_deg = parseFloat(angleInput.value);
        const speed_m_s = parseFloat(speedInput.value);
        const angle_rad = angle_deg * Math.PI / 180;
        const v0x = speed_m_s * Math.cos(angle_rad);
        const v0y = speed_m_s * Math.sin(angle_rad);

         // Calculate trajectory points for preview
        const previewPathPoints = [];
        // Estimate time based on Y component to get a reasonable path length
        const estimatedTotalTime = 2 * v0y / G;
        const stepTime = estimatedTotalTime > 0 ? estimatedTotalTime / 100 : 0.1;

        // Draw path for a fixed horizontal distance or estimated time
        const maxPreviewX = 20; // meters - draw path up to 20m horizontally for preview
        let t = 0;
        while (true) {
            const x = v0x * t;
            const y = v0y * t - 0.5 * G * t * t;
            if (x > maxPreviewX && t > 0.5) break; // Stop if too far horizontally (and after a moment)
            if (y < -2 && t > 0.5) break; // Stop if significantly below ground
            previewPathPoints.push({x, y});
            if (t > estimatedTotalTime * 2 && t > 1) break; // Prevent infinite loop for vertical jumps
             t += stepTime;
              if (t > 10) break; // Safety break
        }

        // Calculate peak height for preview
        const t_peak = v0y / G;
        const peakHeight = v0y * t_peak - 0.5 * G * t_peak * t_peak;

        // Draw the scene with the preview path
        draw(0, 0, [], peakHeight, BAR_HEIGHT_METERS, previewPathPoints); // Draw static jumper at origin, preview path

        // Update peak height display immediately for preview
        peakHeightSpan.textContent = peakHeight.toFixed(2);
        clearanceMessageDiv.textContent = ''; // Clear message during preview
    }


    // Event listener for the button
    jumpButton.addEventListener('click', () => {
        const angle = parseFloat(angleInput.value);
        const speed = parseFloat(speedInput.value);
        animateJump(angle, speed);
    });

    // Initial setup: Draw the scene and the initial preview path
     drawPreviewPath(); // Draw initial state and preview
</script>
```