---
title: "הצפנה בעקומים אליפטיים: מסע ויזואלי אל סודות האבטחה הדיגיטלית"
english_slug: elliptic-curve-cryptography-visualizing-the-math
category: "טכנולוגיה / מדעי המחשב"
tags: ["הצפנה", "קריפטוגרפיה", "אבטחת מידע", "עקומים אליפטיים", "מתמטיקה ויזואלית"]
---
# הצפנה בעקומים אליפטיים: מסע ויזואלי אל סודות האבטחה הדיגיטלית

איך הודעות סודיות עוברות בבטחה ברשת ומגנות על הכסף הדיגיטלי שלכם? הסודות הטמונים בלב ההצפנה המתקדמת של ימינו אינם מבוססים על מספרים ראשוניים ענקיים בלבד, אלא גם על מבנים גיאומטריים מופלאים שאינם דומים למה שלמדתם בבית הספר. הצטרפו אלינו למסע ויזואלי כדי לראות איך מתמטיקה חיה נושמת ופועלת כשהיא מצוירת על הגרף, וכיצד פעולת "חיבור" פשוטה הופכת לבסיס לביטחון הדיגיטלי שלנו.

<div class="interactive-container">
    <canvas id="eccCanvas" width="700" height="500"></canvas>
    <div class="controls">
        <button id="nextStepBtn">הוסף את P לנקודה הנוכחית (חשב את הצעד הבא)</button>
        <button id="resetBtn">התחל מחדש</button>
        <div id="currentPointDisplay"></div>
    </div>
</div>

<button id="toggleExplanationBtn">הצג/הסתר הסבר תיאורטי ומעמיק</button>

<div id="explanation" class="hidden">
    <h2>מהם עקומים אליפטיים?</h2>
    <p>עקום אליפטי, בהקשר קריפטוגרפי (ובמקרים רבים מעל שדות סופיים, אך לצורך הדגמה ויזואלית אנו מציגים עקום מעל המספרים הממשיים), הוא אוסף הנקודות (x,y) המקיימות משוואה מהצורה y² = x³ + ax + b, בתוספת נקודה מיוחדת הנקראת "הנקודה באינסוף" (מסומנת לרוב כ-O). הדרישה הטכנית ש-4a³ + 27b² ≠ 0 מבטיחה שהעקום אינו מכיל נקודות "חדות" או "קפלים" (סינגולריות) ושהוא חלק. הגרף שלו נראה בדרך כלל כפי שמוצג באינטראקציה. על עקומים אלו, ניתן להגדיר פעולת "חיבור" בין נקודות המקיימת תכונות דומות לחיבור רגיל, כמו קומוטטיביות ואסוציאטיביות, ונקודת האינסוף משמשת כאיבר האדיש (נקודת האפס) לחיבור.</p>

    <h2>האלגברה הגיאומטרית: איך 'מחברים' נקודות (P+Q)?</h2>
    <p>הגדרת פעולת החיבור על עקום אליפטי אלגנטית ומבוססת על גיאומטריה:
        <ul>
            <li>**חיבור שתי נקודות שונות, P ו-Q:** מציירים קו ישר דרך P ו-Q. קו זה, אם הוא לא אנכי לחלוטין, יחתוך את העקום בנקודה שלישית יחידה R (אם הקו משיק לאחת הנקודות, R תהיה הנקודה האחרת או אותה נקודה אם הוא משיק וחולף דרכה). "החיבור" P+Q מוגדר להיות השיקוף של R ביחס לציר ה-X (כלומר, אם R=(x,y) אז P+Q=(x,-y)).</li>
            <li>**כפל נקודה בעצמה (P+P או 2P):** אי אפשר לצייר קו דרך שתי נקודות זהות. במקרה זה, מציירים קו משיק לעקום בנקודה P. קו זה יחתוך את העקום בנקודה יחידה נוספת R (אלא אם המשיק משיק וחולף רק ב-P, או משיק ב-P והנקודה הנוספת היא P עצמה - מקרים מיוחדים). 2P מוגדר להיות השיקוף של R ביחס לציר ה-X.</li>
             <li>**חיבור P ונקודת האינסוף O:** P + O = P. (O הוא איבר האפס).</li>
             <li>**חיבור P והנקודה הנגדית לה (-P):** P + (-P) = O (הנקודה באינסוף). הנקודה הנגדית ל-(x,y) היא (x,-y).</li>
        </ul>
        האינטראקציה למעלה מדגימה באופן ויזואלי את המקרים הראשונים: חיבור שתי נקודות שונות (בצעד הראשון, חיבור P לנקודת ההתחלה O, שתוצאתו P; ובצעדים הבאים, חיבור הנקודה הנוכחית nP עם P) וכפל נקודה בעצמה (הצעד הראשון, P+P=2P, הוא מקרה פרטי של חיבור nP+P כאשר n=1). שימו לב שברגע שנמצאת נקודה R על הקו, החישוב האלגברי של x ו-y של R ואז של נקודת התוצאה הוא דטרמיניסטי וניתן לביצוע גם ללא הגיאומטריה.
    </p>

    <h2>מכפלה סקלרית (nP): הלב הקריפטוגרפי</h2>
    <p>הפעולה המרכזית בקריפטוגרפיית עקומים אליפטיים היא "מכפלה סקלרית": חישוב nP, כאשר n הוא מספר שלם (סקלר, לרוב חיובי) ו-P היא נקודת בסיס מוסכמת וקבועה על העקום. חישוב זה הוא פשוט חיבור P לעצמה n פעמים: nP = P + P + ... + P (n פעמים). בפועל, חישוב nP אינו מתבצע על ידי n חיבורים בודדים, אלא בצורה יעילה הרבה יותר באמצעות אלגוריתמים המשלבים כפלים (P -> 2P -> 4P וכו') וחיבורים, בדומה לאלגוריתם "ריבוע וכפל" לחישוב חזקות (אקספוננציאציה מהירה). למשל, 10P = 2*(5P) = 2*(4P + P) = 2*(2*(2P) + P).</p>

    <h2>הקשר למפתחות ציבוריים ופרטיים בהצפנה</h2>
    <p>קריפטוגרפיית עקומים אליפטיים (ECC) משמשת ליצירת מערכות מפתח ציבורי. במערכות אלו, לכל משתמש יש זוג מפתחות: מפתח פרטי סודי (מספר שלם אקראי n) ומפתח ציבורי גלוי (נקודה Q על העקום). המפתח הציבורי Q מחושב מהמפתח הפרטי n על ידי ביצוע מכפלה סקלרית של n בנקודת בסיס מוסכמת וציבורית G (נקודה גנרטורית) על עקום מוסכם: Q = nG. נקודת הבסיס G והעקום נבחרים כפרמטרים של המערכת וגלויים לכולם.</p>

    <h2>בעיית הלוגריתם הדיסקרטי על עקומים אליפטיים (ECDLP)</h2>
    <p>הביטחון של ECC נובע מהקושי החישובי ב"היפוך" הפעולה. בהינתן נקודת הבסיס G והנקודה Q שהיא מכפלה סקלרית שלה (Q = nG), קשה ביותר מבחינה חישובית למצוא את הסקלר n. זוהי "בעיית הלוגריתם הדיסקרטי על עקומים אליפטיים" (ECDLP). קל לחשב Q מ-n ומ-G (זהו חישוב המפתח הציבורי מהפרטי), אך קשה מאוד למצוא את n בהינתן G ו-Q. הקושי הזה הוא האבן היסוד שעליה נבנה הביטחון של פרוטוקולי ECC.</p>

    <h2>מדוע ECC כל כך פופולרי?</h2>
    <p>היתרון המרכזי של ECC לעומת אלגוריתמי מפתח ציבורי ותיקים כמו RSA הוא היכולת לספק רמת אבטחה מקבילה עם מפתחות קצרים משמעותית. לדוגמה, מפתח ECC באורך 256 סיביות נחשב מאובטח כמו מפתח RSA באורך 3072 סיביות. מפתחות קצרים יותר פירושם חישובים מהירים יותר (חישוב nP עבור n גדול יעיל יותר מחישוב חזקות גדולות במודולו גדול), הודעות קצרות יותר, ופחות דרישות למשאבי עיבוד ואחסון. זו הסיבה ש-ECC אידיאלי עבור מכשירים עם הגבלות משאבים כמו טלפונים ניידים, כרטיסים חכמים, ורשתות IoT.</p>

    <h2>יישומים בעולם האמיתי</h2>
    <p>ECC נמצא בשימוש נרחב כיום באבטחת התקשורת הדיגיטלית שלנו. הוא מהווה חלק מרכזי בתקן TLS/SSL המאבטח גלישה באינטרנט (HTTPS), הוא הבסיס לחתימות דיגיטליות בארנקי מטבעות קריפטוגרפיים (כמו ביטקוין ואת'ריום), משמש לאבטחת דוא"ל, תקשורת מאובטחת במכשירים ניידים, ועוד.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const canvas = document.getElementById('eccCanvas');
        const ctx = canvas.getContext('2d');
        const nextStepBtn = document.getElementById('nextStepBtn');
        const resetBtn = document.getElementById('resetBtn');
        const currentPointDisplay = document.getElementById('currentPointDisplay');
        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');

        // Curve parameters: y^2 = x^3 + ax + b
        const a = -7;
        const b = 10;

        // Starting point P (chosen to have nice small integer coordinates initially)
        const P = { x: 1, y: 2 };
        const O = { x: Infinity, y: Infinity }; // Point at Infinity

        let currentPoint = { ...O }; // Start at Point at Infinity (0P)
        let multiple = 0;
        let history = []; // Store sequence of calculated points (nP) including O

        // Animation related variables
        let animationFrameId = null;
        let animationStep = 0; // 0: idle, 1: draw line, 2: draw R, 3: draw reflection, 4: draw result
        let animationStartTime = null;
        const animationDuration = 1000; // milliseconds for each animation segment

        // Canvas settings and transformations
        const canvasWidth = canvas.width;
        const canvasHeight = canvas.height;
        const xScale = 40; // Pixels per unit on x-axis (increased for better detail)
        const yScale = -40; // Pixels per unit on y-axis (negative for screen coordinates)
        const xOffset = canvasWidth / 2; // Center the origin horizontally
        const yOffset = canvasHeight / 2; // Center the origin vertically
        const pointRadius = 5; // Increased radius

        // Coordinate transformation functions
        function toCanvasX(x) { return x * xScale + xOffset; }
        function toCanvasY(y) { return y * yScale + yOffset; }
        function fromCanvasX(cx) { return (cx - xOffset) / xScale; }
        function fromCanvasY(cy) { return (cy - yOffset) / yScale; }

        // --- Drawing Functions ---

        function drawAxes() {
            ctx.strokeStyle = '#666'; // Darker gray for axes
            ctx.lineWidth = 1;

            // X-axis
            ctx.beginPath();
            ctx.moveTo(0, yOffset);
            ctx.lineTo(canvasWidth, yOffset);
            ctx.stroke();

            // Y-axis
            ctx.beginPath();
            ctx.moveTo(xOffset, 0);
            ctx.lineTo(xOffset, canvasHeight);
            ctx.stroke();

            // Draw axis labels (optional but helpful)
            ctx.fillStyle = '#333';
            ctx.font = '12px Arial';
            ctx.textAlign = 'right';
            ctx.fillText('X', canvasWidth - 10, yOffset - 5);
            ctx.textAlign = 'left';
            ctx.fillText('Y', xOffset + 5, 15);
            ctx.textAlign = 'center';
             ctx.fillText('O (0,0)', xOffset, yOffset + 15); // Label origin
        }

        function drawCurve() {
            ctx.strokeStyle = '#007bff'; // Primary blue for curve
            ctx.lineWidth = 2;

            ctx.beginPath();
            let firstPoint = true;

            // Iterate over x values and calculate y
            const xMin = -5; // Extended range
            const xMax = 8; // Extended range
            const step = 0.05;

            // Draw positive y branch
            for (let x = xMin; x <= xMax; x += step) {
                const ySquared = Math.pow(x, 3) + a * x + b;
                if (ySquared >= 0) {
                    const y = Math.sqrt(ySquared);
                     if (firstPoint) {
                         ctx.moveTo(toCanvasX(x), toCanvasY(y));
                         firstPoint = false;
                     } else {
                         ctx.lineTo(toCanvasX(x), toCanvasY(y));
                     }
                }
            }
             ctx.stroke(); // Draw the positive branch

             // Now draw the negative y branch
             ctx.beginPath();
             firstPoint = true;
             for (let x = xMax; x >= xMin; x -= step) { // Iterate backwards for continuous path if possible
                 const ySquared = Math.pow(x, 3) + a * x + b;
                 if (ySquared >= 0) {
                     const y = -Math.sqrt(ySquared);
                      if (firstPoint) {
                         ctx.moveTo(toCanvasX(x), toCanvasY(y));
                         firstPoint = false;
                     } else {
                         ctx.lineTo(toCanvasX(x), toCanvasY(y));
                     }
                 }
             }
            ctx.stroke(); // Draw the negative branch
        }

        function drawPoint(point, color, radius = pointRadius, label = null) {
            if (point.x === Infinity) return; // Don't draw point at infinity
            ctx.fillStyle = color;
            ctx.beginPath();
            ctx.arc(toCanvasX(point.x), toCanvasY(point.y), radius, 0, Math.PI * 2);
            ctx.fill();

            if (label) {
                 ctx.fillStyle = '#333';
                 ctx.font = '12px Arial';
                 ctx.textAlign = 'left';
                 ctx.textBaseline = 'bottom';
                 const labelX = toCanvasX(point.x) + radius + 2;
                 const labelY = toCanvasY(point.y) - radius - 2;
                 ctx.fillText(label, labelX, labelY);
            }
        }

        function drawLineSegment(p1, p2, color, lineWidth = 1, dashed = false) {
             if (p1.x === Infinity || p2.x === Infinity) return;
             ctx.strokeStyle = color;
             ctx.lineWidth = lineWidth;
             if (dashed) {
                 ctx.setLineDash([5, 5]);
             } else {
                 ctx.setLineDash([]);
             }
             ctx.beginPath();
             ctx.moveTo(toCanvasX(p1.x), toCanvasY(p1.y));
             ctx.lineTo(toCanvasX(p2.x), toCanvasY(p2.y));
             ctx.stroke();
             ctx.setLineDash([]); // Reset dash
         }

         // Draw a line that potentially extends beyond the two points
         function drawExtendedLine(p1, p2, color, lineWidth = 1, dashed = false) {
             if (p1.x === Infinity || p2.x === Infinity) return;

             let m, c;
             let isVertical = false;

             if (p1.x === p2.x) {
                 isVertical = true;
             } else {
                 m = (p2.y - p1.y) / (p2.x - p1.x);
                 c = p1.y - m * p1.x;
             }

             ctx.strokeStyle = color;
             ctx.lineWidth = lineWidth;
             if (dashed) {
                 ctx.setLineDash([5, 5]);
             } else {
                 ctx.setLineDash([]);
             }

             ctx.beginPath();
             if (isVertical) {
                 // Draw a vertical line that spans the canvas height
                 const canvasX = toCanvasX(p1.x);
                 ctx.moveTo(canvasX, 0);
                 ctx.lineTo(canvasX, canvasHeight);
             } else {
                 // Draw a line that spans the canvas width
                 const startX = fromCanvasX(0);
                 const endX = fromCanvasX(canvasWidth);
                 ctx.moveTo(toCanvasX(startX), toCanvasY(m * startX + c));
                 ctx.lineTo(toCanvasX(endX), toCanvasY(m * endX + c));
             }
             ctx.stroke();
             ctx.setLineDash([]); // Reset dash
         }

        // Find the third intersection point of a line with the curve
        // Line through P1 and P2. Need to solve cubic equation.
        // For y^2 = x^3 + ax + b, line y = m*x + c
        // (m*x+c)^2 = x^3 + ax + b
        // m^2 x^2 + 2mc x + c^2 = x^3 + ax + b
        // x^3 - m^2 x^2 + (a - 2mc) x + (b - c^2) = 0
        // We know two roots are x1 (from P1) and x2 (from P2) (possibly x1=x2 in doubling case).
        // Sum of roots: x1 + x2 + x3 = - (coeff of x^2) = -(-m^2) = m^2
        // So, x3 = m^2 - x1 - x2
        // y3 = m * x3 + c
        function findThirdIntersection(p1, p2, m) {
            const x1 = p1.x;
            const x2 = p2.x;

            const xR = m * m - x1 - x2;

            // Find c using the line equation y = m * x + c
            // Use p1: c = p1.y - m * p1.x
            const c = p1.y - m * p1.x;
            const yR = m * xR + c;

            // Return the intersection point R
            return { x: xR, y: yR };
        }

        // Elliptic Curve Point Addition
        // Adds point Q to point P on the curve y^2 = x^3 + ax + b
        // Returns P+Q or point at infinity (represented here as { x: Infinity, y: Infinity })
        function addPoints(p1, p2) {
             // Handle point at infinity (O)
            if (p1.x === Infinity) return p2;
            if (p2.x === Infinity) return p1;

            // Handle P + (-P) = O
            if (p1.x === p2.x && p1.y === -p2.y) {
                return { x: Infinity, y: Infinity };
            }

            let m; // Slope
            // Handle Point Doubling P + P
            if (p1.x === p2.x && p1.y === p2.y) {
                if (p1.y === 0) { // Tangent is vertical at y=0
                    return { x: Infinity, y: Infinity };
                }
                // Slope of tangent: dy/dx of y^2 = x^3 + ax + b is 2y dy/dx = 3x^2 + a
                // dy/dx = (3x^2 + a) / (2y)
                m = (3 * p1.x * p1.x + a) / (2 * p1.y);
            } else { // Point Addition P + Q (P != Q, and not P = -Q)
                m = (p2.y - p1.y) / (p2.x - p1.x);
            }

            // Calculate x-coordinate of the third intersection point R
            const xR = m * m - p1.x - p2.x;
            // Calculate y-coordinate of the third intersection point R using P1 and slope
            const yR = m * (p1.x - xR) - p1.y;

            // Result is the reflection of (xR, yR) across the x-axis
            return { x: xR, y: -yR };
        }


        // --- Animation Logic ---

        let p1Anim, p2Anim, nextPointAnim, intermediateR; // Points for animation step
        let mAnim; // Slope for animation

        function animateStep(timestamp) {
             if (!animationStartTime) animationStartTime = timestamp;
             const elapsed = timestamp - animationStartTime;
             const progress = Math.min(elapsed / animationDuration, 1); // 0 to 1

             redraw(false); // Redraw static elements (curve, axes, path, P, nP)

             if (animationStep === 1) { // Draw line between p1Anim and p2Anim
                 // Interpolate line drawing
                 const start = p1Anim;
                 const end = p2Anim;
                 // Need to draw line segment from start up to the point corresponding to 'progress'
                 // If vertical line: interpolate Y range
                 // If sloped line: interpolate X range
                 let currentP2;
                 if (p1Anim.x === p2Anim.x) { // Vertical line
                     // Assuming p1Anim.y <= p2Anim.y for simplicity, adjust if needed
                     const yStart = Math.min(p1Anim.y, p2Anim.y);
                     const yEnd = Math.max(p1Anim.y, p2Anim.y);
                     const currentY = yStart + (yEnd - yStart) * progress;
                     // Need to draw line from p1Anim.y up to currentY, and p2Anim.y down to currentY?
                     // Or simpler: just draw a segment that grows from p1Anim towards p2Anim?
                     // Let's draw the full line extent and just change its opacity or use a drawing animation effect later
                     // For now, just draw the full line but maybe visually emphasize the connection
                     drawExtendedLine(p1Anim, p2Anim, '#ffc107', 2, true); // Yellow, thicker, dashed
                     drawPoint(p1Anim, '#28a745', pointRadius + 1); // Green current point
                     drawPoint(p2Anim, '#dc3545', pointRadius); // Red P
                 } else { // Sloped line
                      drawExtendedLine(p1Anim, p2Anim, '#ffc107', 2, true); // Yellow, thicker, dashed
                      drawPoint(p1Anim, '#28a745', pointRadius + 1); // Green current point
                      drawPoint(p2Anim, '#dc3545', pointRadius); // Red P
                 }


                 if (progress === 1) {
                     animationStep = 2; // Move to next step: show intersection R
                     animationStartTime = null; // Reset timer for next step
                     // Calculate R now that the line is "fully drawn"
                     let tempM;
                     if (p1Anim.x === p2Anim.x && p1Anim.y === p2Anim.y) { // Doubling
                         tempM = (3 * p1Anim.x * p1Anim.x + a) / (2 * p1Anim.y);
                     } else { // Addition
                         tempM = (p2Anim.y - p1Anim.y) / (p2Anim.x - p1Anim.x);
                     }
                     intermediateR = findThirdIntersection(p1Anim, p2Anim, tempM);
                 }

             } else if (animationStep === 2) { // Draw R
                 // Draw the line from previous step
                  if (p1Anim.x === p2Anim.x) {
                     drawExtendedLine(p1Anim, p2Anim, '#ffc107', 2, true);
                  } else {
                     drawExtendedLine(p1Anim, p2Anim, '#ffc107', 2, true);
                  }
                 drawPoint(p1Anim, '#28a745', pointRadius + 1); // Green current point
                 drawPoint(p2Anim, '#dc3545', pointRadius); // Red P

                 // Draw R with a pulse animation? Or just appear?
                 // Simple appear for now
                 drawPoint(intermediateR, '#17a2b8', pointRadius); // Cyan for R
                 // Maybe draw a small line from R to the curve point used to calculate it? No, R IS the curve point.

                 if (progress === 1) {
                     animationStep = 3; // Move to next step: draw reflection line
                     animationStartTime = null; // Reset timer
                 }

             } else if (animationStep === 3) { // Draw reflection line from R to result
                 // Draw elements from previous steps
                 if (p1Anim.x === p2Anim.x) {
                     drawExtendedLine(p1Anim, p2Anim, '#ffc107', 2, true);
                 } else {
                     drawExtendedLine(p1Anim, p2Anim, '#ffc107', 2, true);
                 }
                 drawPoint(p1Anim, '#28a745', pointRadius + 1);
                 drawPoint(p2Anim, '#dc3545', pointRadius);
                 drawPoint(intermediateR, '#17a2b8', pointRadius);

                 // Draw vertical reflection line from R to nextPointAnim
                 drawLineSegment(intermediateR, nextPointAnim, '#6f42c1', 2, true); // Purple, thicker, dashed

                 if (progress === 1) {
                     animationStep = 4; // Move to next step: draw the final result point
                     animationStartTime = null; // Reset timer
                 }

             } else if (animationStep === 4) { // Draw the final result point (nextPointAnim)
                 // Draw elements from previous steps
                 if (p1Anim.x === p2Anim.x) {
                    drawExtendedLine(p1Anim, p2Anim, '#ffc107', 2, true);
                 } else {
                    drawExtendedLine(p1Anim, p2Anim, '#ffc107', 2, true);
                 }
                 drawPoint(p1Anim, '#28a745', pointRadius + 1);
                 drawPoint(p2Anim, '#dc3545', pointRadius);
                 drawPoint(intermediateR, '#17a2b8', pointRadius);
                 drawLineSegment(intermediateR, nextPointAnim, '#6f42c1', 2, true);

                 // Draw the final point with a little emphasis (e.g. larger radius briefly)
                 const finalRadius = pointRadius + (progress < 0.5 ? progress * 2 : (1 - progress) * 2);
                 drawPoint(nextPointAnim, '#28a745', finalRadius); // Green, final result

                 if (progress === 1) {
                     // Animation sequence finished for this step
                     animationStep = 0; // Reset animation state
                     animationStartTime = null;
                     // Update the actual current point and history *after* animation finishes
                     currentPoint = { ...nextPointAnim };
                     history.push(currentPoint);
                     updateDisplay();
                     redraw(true); // Final redraw to set the state
                     nextStepBtn.disabled = false; // Enable button
                 }
             }

             if (animationStep !== 0) {
                 animationFrameId = requestAnimationFrame(animateStep);
             }
        }


        // Redraw the entire canvas (static elements)
        function redraw(drawHistoryPath = true) {
            ctx.clearRect(0, 0, canvasWidth, canvasHeight);
            drawAxes();
            drawCurve();

            // Draw initial point P (base point)
            drawPoint(P, '#dc3545', pointRadius, 'P'); // Red for initial P

            // Draw path history (only if not currently animating a step visualization)
            if (drawHistoryPath && history.length > 1) {
                 ctx.strokeStyle = '#6610f2'; // Purple for path
                 ctx.lineWidth = 1;
                 ctx.beginPath();
                 let movedToFirst = false;
                 for(let i = 0; i < history.length; i++) {
                      if (history[i].x !== Infinity) { // Only draw segment if point is finite
                         if (!movedToFirst) {
                             ctx.moveTo(toCanvasX(history[i].x), toCanvasY(history[i].y));
                             movedToFirst = true;
                         } else {
                             ctx.lineTo(toCanvasX(history[i].x), toCanvasY(history[i].y));
                         }
                      } else {
                          movedToFirst = false; // Break line on infinity point
                      }
                 }
                 ctx.stroke();
            }

             // Draw the current point (nP) if it's not the start (0P) and not currently animating the NEXT point's result
             if (multiple > 0 && animationStep === 0) {
                drawPoint(currentPoint, '#28a745', pointRadius + 1, `${multiple}P`); // Green for current nP
             } else if (multiple > 0 && animationStep > 0) {
                 // If animating, draw the point *before* the animation started
                 const pointBeforeAnim = history[history.length - 1];
                 if (pointBeforeAnim && pointBeforeAnim.x !== Infinity) {
                     drawPoint(pointBeforeAnim, '#28a745', pointRadius + 1, `${multiple}P`);
                 }
             }
        }

        // Update the text display below the canvas
        function updateDisplay() {
             if (currentPoint.x === Infinity) {
                 currentPointDisplay.textContent = `צעד ${multiple}: הנקודה כעת היא ${multiple}P והיא באינסוף (O).`;
                 nextStepBtn.disabled = true; // Disable button if we reached infinity
                 //currentPointDisplay.textContent += ' סיום הדגמה עבור נקודה זו. התחילו מחדש כדי לראות עוד צעדים.'; // Or just disable button
            } else {
                 const pointLabel = multiple === 0 ? 'O' : `${multiple}P`;
                 currentPointDisplay.textContent = `צעד ${multiple}: הנקודה הנוכחית (${pointLabel}) היא בערך (${currentPoint.x.toFixed(2)}, ${currentPoint.y.toFixed(2)})`;
            }
        }


        // Handle the button click for the next step
        nextStepBtn.addEventListener('click', () => {
            if (animationStep !== 0) return; // Prevent multiple clicks during animation

            nextStepBtn.disabled = true; // Disable button during animation

            // Points for the addition: The current point (nP) and the base point (P)
            p1Anim = { ...currentPoint };
            p2Anim = { ...P };

            // Calculate the next point: (nP) + P = (n+1)P
            nextPointAnim = addPoints(p1Anim, p2Anim);
            multiple++; // Increment multiple assuming we will successfully calculate the next point

            // Start the animation sequence
            animationStep = 1; // Start by drawing the line
            animationStartTime = null; // Will be set in the first frame of animateStep
            animationFrameId = requestAnimationFrame(animateStep);

             // If the result is infinity, the animation might not make sense geometrically.
             // Need to decide how to handle this visually. For now, the addPoints returns infinity,
             // and the animation step 4 will draw it if finite, or do nothing if infinity.
             // The display text will be updated after animation finishes.
        });

        // Handle reset button
        resetBtn.addEventListener('click', () => {
             if (animationFrameId) {
                 cancelAnimationFrame(animationFrameId);
                 animationFrameId = null;
             }
             animationStep = 0; // Reset animation state
             animationStartTime = null;

             currentPoint = { ...O }; // Reset to Point at Infinity
             multiple = 0;
             history = [{...O}]; // History starts with O (0P)

             redraw(true);
             updateDisplay();
             nextStepBtn.disabled = false; // Enable button
        });


        // Handle explanation toggle
        toggleExplanationBtn.addEventListener('click', () => {
            explanationDiv.classList.toggle('hidden');
            if (!explanationDiv.classList.contains('hidden')) {
                 toggleExplanationBtn.textContent = 'הסתר הסבר תיאורטי ומעמיק';
            } else {
                 toggleExplanationBtn.textContent = 'הצג הסבר תיאורטי ומעמיק';
            }
        });

        // Initial setup
        resetBtn.click(); // Use reset logic for initial state
    });
</script>

<style>
    /* General Page Styling */
    body {
        font-family: 'Arial', sans-serif; /* Use a common system font */
        line-height: 1.7; /* Slightly increased line height */
        margin: 0; /* Remove default margin */
        padding: 20px; /* Add padding around content */
        background-color: #eef2f7; /* Light background color */
        color: #333; /* Default text color */
        direction: rtl; /* Ensure right-to-left */
        text-align: right; /* Align text to the right */
    }

    h1 {
        text-align: center;
        color: #003366; /* Darker blue for headings */
        margin-bottom: 25px;
        font-size: 2em; /* Larger main heading */
        line-height: 1.3;
    }

     h2 {
         color: #0056b3; /* Slightly lighter blue for subheadings */
         margin-top: 20px;
         margin-bottom: 10px;
         font-size: 1.6em;
         border-bottom: 1px solid #cce5ff; /* Light border */
         padding-bottom: 5px;
     }

    p {
        margin-bottom: 1em;
    }

    ul {
        margin-bottom: 1em;
        padding-right: 20px; /* Add padding for list markers */
    }

    li {
        margin-bottom: 0.5em;
    }


    /* Interactive Section Styling */
    .interactive-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 30px;
        background-color: #ffffff; /* White background for interactive part */
        border-radius: 8px; /* Rounded corners */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        padding: 20px;
    }

    #eccCanvas {
        border: 1px solid #ddd; /* Lighter border */
        background-color: #f8f9fa; /* Light gray background */
        margin-bottom: 15px;
        border-radius: 5px; /* Rounded corners for canvas */
    }

    .controls {
        text-align: center;
        display: flex; /* Arrange buttons and display in a row/column */
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        justify-content: center; /* Center items horizontally */
        align-items: center;
        width: 100%; /* Take full width of container */
    }

    button {
        padding: 12px 20px; /* More padding */
        font-size: 1em;
        cursor: pointer;
        margin: 8px; /* Increased margin */
        border: none; /* Remove default border */
        border-radius: 5px; /* Rounded button corners */
        transition: background-color 0.2s ease, opacity 0.2s ease; /* Smooth transitions */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Subtle button shadow */
    }

    button#nextStepBtn {
        background-color: #28a745; /* Green button */
        color: white;
    }

    button#nextStepBtn:hover:not(:disabled) {
        background-color: #218838; /* Darker green on hover */
    }

     button#resetBtn {
         background-color: #dc3545; /* Red button */
         color: white;
     }

     button#resetBtn:hover:not(:disabled) {
         background-color: #c82333; /* Darker red on hover */
     }

    button#toggleExplanationBtn {
        background-color: #6c757d; /* Gray button */
        color: white;
        display: block; /* Make it a block element */
        margin: 20px auto; /* Center the toggle button */
        width: fit-content; /* Fit button width to content */
    }

     button#toggleExplanationBtn:hover:not(:disabled) {
         background-color: #5a6268; /* Darker gray on hover */
     }


    button:disabled {
        opacity: 0.6; /* Dim disabled buttons */
        cursor: not-allowed;
        box-shadow: none;
    }


    #currentPointDisplay {
        margin-top: 10px;
        padding: 8px 15px; /* Add padding */
        font-size: 1.1em;
        font-weight: bold;
        min-height: 1.5em; /* Reserve space to prevent layout shift */
        background-color: #e9ecef; /* Light gray background for display */
        border-radius: 5px;
        text-align: center; /* Center text in display */
        width: calc(100% - 30px); /* Adjust width considering padding/margin */
        max-width: 400px; /* Max width for display */
    }

    /* Explanation Section Styling */
    #explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #cce5ff; /* Light blue border */
        background-color: #e9f5ff; /* Very light blue background */
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }

    .hidden {
        display: none;
    }

    /* Optional: Add some responsiveness */
    @media (max-width: 768px) {
        .interactive-container {
            padding: 15px;
        }
        #eccCanvas {
            width: 100%; /* Make canvas take full width on small screens */
            height: auto; /* Adjust height automatically */
        }
        .controls {
            flex-direction: column; /* Stack controls vertically */
        }
        button {
            width: calc(100% - 16px); /* Full width buttons minus margin */
        }
        #currentPointDisplay {
             width: calc(100% - 30px);
        }
         body {
             padding: 10px;
         }
         h1 {
             font-size: 1.6em;
         }
          h2 {
              font-size: 1.4em;
          }
    }

    /* Canvas specific styles for points and lines */
    /* Handled by JS fillStyle/strokeStyle, but conceptually belongs here */
    /* Example colors:
       - Curve: #007bff (Blue)
       - Axes: #666 (Dark Gray)
       - Initial P: #dc3545 (Red)
       - Current nP: #28a745 (Green)
       - Intermediate R: #17a2b8 (Cyan)
       - Addition/Tangent Line: #ffc107 (Yellow)
       - Reflection Line: #6f42c1 (Purple)
       - Path History: #6610f2 (Dark Purple)
    */

</style>
---