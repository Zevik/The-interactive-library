---
title: "לראות מסביב לפינה: קסם האור בסיבים אופטיים והחזרת אור מלאה"
english_slug: seeing-around-the-corner-optical-fiber-and-total-internal-reflection
category: "מדעים מדויקים / פיזיקה"
tags: [אופטיקה, החזרת אור, סיב אופטי, זווית קריטית, שבירת אור]
---
# לראות מסביב לפינה: קסם האור בסיבים אופטיים

איך גלי אור, ששואפים לנוע ישר כמו חץ, מצליחים לשייט בנפתולי כבל דקיק וגמיש ולהגיע ליעדם במהירות מסחררת, גם כשהכבל מתפתל ומסתלסל? הצטרפו אלינו לגלות את סוד הסיבים האופטיים ואת התופעה הפיזיקלית המדהימה שמאפשרת להם לשגר אינפורמציה סביב הגלובוס!

<div id="fiber-optic-sim">
    <canvas id="fiberCanvas" width="800" height="200"></canvas>
    <div class="controls-container">
        <div class="control-group">
            <label for="angleSlider">זווית כניסה (מעלות ביחס לציר הסיב):</label>
            <input type="range" id="angleSlider" min="-40" max="40" value="15" step="1">
            <span id="angleValue" class="value-display">15°</span>
        </div>
        <div class="control-group">
            <label for="positionSlider">מיקום כניסה (יחסית למרכז הליבה):</label>
            <input type="range" id="positionSlider" min="-0.9" max="0.9" value="0" step="0.01">
            <span id="positionValue" class="value-display">0.00</span>
        </div>
         <button id="resetButton">התחל מחדש</button>
    </div>
     <div id="status-message" class="status"></div>
</div>

<style>
#fiber-optic-sim {
    direction: rtl;
    text-align: center;
    margin: 20px auto;
    border: 1px solid #cce; /* Softer border */
    border-radius: 8px; /* Rounded corners */
    padding: 15px;
    max-width: 850px;
    background: linear-gradient(to bottom, #f0f4f8, #d9e2ec); /* Gentle gradient background */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    font-family: 'Arial', sans-serif; /* Clean font */
}
#fiberCanvas {
    border: 1px solid #aaa; /* Softer canvas border */
    background-color: #eef; /* Light background for cladding area */
    box-shadow: inset 0 0 5px rgba(0,0,0,0.1); /* Inner shadow for depth */
    display: block; /* Remove extra space below canvas */
    margin: 0 auto 15px;
}
.controls-container {
    margin-top: 10px;
    padding: 10px;
    background-color: #e0e9f3; /* Background for controls */
    border-radius: 5px;
    display: flex; /* Arrange controls horizontally */
    flex-wrap: wrap; /* Allow wrapping on smaller screens */
    justify-content: center; /* Center controls */
    gap: 15px; /* Space between control groups */
}
.control-group {
    display: flex;
    align-items: center;
}
label {
    margin-left: 8px;
    font-weight: bold;
    color: #333;
    font-size: 0.95em;
}
input[type="range"] {
    direction: ltr; /* Sliders are more intuitive left-to-right */
    flex-grow: 1; /* Allow slider to take available space */
    min-width: 100px; /* Prevent slider from becoming too small */
}
.value-display {
    display: inline-block;
    width: 45px; /* Fixed width for value */
    text-align: left; /* Align value to the left */
    margin-right: 5px;
    font-family: 'Courier New', monospace; /* Monospace for numbers */
    color: #0056b3; /* Blue color for values */
}
#resetButton {
    padding: 8px 15px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease;
}
#resetButton:hover {
    background-color: #0056b3;
}
.status {
    margin-top: 15px;
    font-size: 1em;
    color: #333;
    min-height: 1.2em; /* Reserve space to prevent layout shifts */
}
#explanation {
    margin-top: 30px;
    padding: 20px;
    border: 1px solid #d0d9e6; /* Softer border */
    border-radius: 8px; /* Rounded corners */
    background-color: #eef2f7; /* Light blue background */
    text-align: right;
    display: none; /* Start hidden */
    direction: rtl;
    line-height: 1.7; /* Improved readability */
    color: #333;
    box-shadow: 0 2px 5px rgba(0,0,0,0.08);
}
#explanation h2 {
    text-align: center;
    margin-bottom: 20px;
    color: #0056b3;
}
#explanation h3 {
    margin-top: 20px;
    margin-bottom: 10px;
    color: #004085;
}
#explanation p {
    margin-bottom: 15px;
}
#explanation ul, #explanation ol {
    margin-bottom: 15px;
    padding-right: 25px; /* Increased padding */
}
#explanation li {
    margin-bottom: 8px;
}
#explanation a {
    color: #007bff;
    text-decoration: none;
}
#explanation a:hover {
    text-decoration: underline;
}
#toggleExplanation {
    display: block;
    margin: 20px auto;
    padding: 10px 20px;
    background-color: #6c757d; /* Grey button */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease;
}
#toggleExplanation:hover {
    background-color: #5a6268;
}

/* Canvas Drawing Styles (JS will set these) */
.core-color { color: #ffffff; }
.cladding-color { color: #eef; } /* Matches background */
.ray-color-core { color: #e74c3c; } /* Vibrant Red */
.ray-color-cladding { color: #3498db; } /* Vibrant Blue */
.normal-color { color: #7f8c8d; } /* Grey */
.angle-color { color: #f39c12; } /* Orange */
.critical-angle-color { color: #2ecc71; } /* Green */

</style>

<button id="toggleExplanation" style="display: block; margin: 20px auto; padding: 10px 20px;">הצג את הסיפור המלא</button>

<div id="explanation">
    <h2>הקסם שבפנים: החזרת אור פנימית מלאה וסיבים אופטיים</h2>
    <p>דמיינו צינור זכוכית דקיק, שקוף לחלוטין, המוליך אור מקצה אחד לשני, גם כשהוא מתפתל כנחש. זהו סיב אופטי, וזו לא קסם, זוהי פיזיקה מרהיבה! סיבים אופטיים הם הגיבורים השקופים מאחורי מהפכת האינטרנט המהיר, שיחות הטלפון הבינלאומיות ותמונות רפואיות מצילות חיים.</p>

    <h3>עקרון הניווט הפנימי: החזרת אור פנימית מלאה (TIR)</h3>
    <p>הסוד מאחורי יכולתו של סיב אופטי להדריך אור טמון בתופעה מרתקת בשם החזרת אור פנימית מלאה (Total Internal Reflection - TIR). תארו לעצמכם קרן אור הנעה בתוך חומר צפוף יותר (אופטית), כמו זכוכית, ופוגעת בגבול עם חומר דליל יותר, כמו אוויר או סוג אחר של זכוכית עם מקדם שבירה נמוך יותר. במקום לצאת החוצה ולהישבר, האור "מוחזר במלואו" בחזרה פנימה, כאילו פגע במראה סמויה!</p>

    <h3>מתי הקסם קורה? תנאי ה-TIR</h3>
    <p>החזרת אור פנימית מלאה אינה קורית תמיד. היא דורשת שני תנאים הכרחיים:</p>
    <ol>
        <li><b>מעבר מצפוף לדליל:</b> האור חייב לעבור מתווך בעל מקדם שבירה גבוה (הצפוף יותר אופטית) לתווך בעל מקדם שבירה נמוך (הדליל יותר אופטית). בסיב אופטי, זה המעבר מהליבה הזכוכיתית למעטפת המקיפה אותה.</li>
        <li><b>זווית פגיעה נכונה:</b> זווית הפגיעה של קרן האור בגבול בין התווכים (הזווית בין הקרן לבין הנורמל - קו אנכי לגבול) חייבת להיות גדולה או שווה ל"זווית הקריטית".</li>
    </ol>
    <p>הזווית הקריטית היא זווית קסומה! זוהי זווית הפגיעה הסף, שמעליה כל האור מוחזר פנימה, ומתחתיה חלק מהאור נשבר ובורח החוצה. הזווית הקריטית תלויה במקדמי השבירה של שני התווכים ומחושבת בעזרת <a href="https://he.wikipedia.org/wiki/%D7%97%D7%95%D7%A7_%D7%A1%D7%A0%D7%9C" target="_blank">חוק סנל</a>.</p>

    <h3>מבנה הסיב האופטי: הליבה והמעטפת</h3>
    <p>סיב אופטי מתוכנן בדיוק לפי עקרונות ה-TIR. הוא מורכב משני חלקים עיקריים:</p>
    <ul>
        <li><b>הליבה (Core):</b> החלק הפנימי, עשוי זכוכית מיוחדת או פלסטיק שקוף, בעל מקדם שבירה *גבוה*. זוהי המסילה שבה האור מטייל.</li>
        <li><b>המעטפת (Cladding):</b> שכבה דקה המקיפה את הליבה, עשויה גם היא מחומר שקוף, אך כזה בעל מקדם שבירה *נמוך יותר* מהליבה. המעטפת היא "הקיר" שמחזיר את האור פנימה באמצעות TIR.</li>
    </ul>

    <h3>מסע האור בתוך הסיב</h3>
    <p>כשקרן אור נכנסת לקצה הליבה בזווית מתאימה (זווית כניסה המאפשרת זווית פגיעה גדולה מהקריטית בכל פגיעה בדופן), היא מתחילה במסע פנימי. בכל פעם שהיא פוגעת בדופן הליבה (בגבול עם המעטפת), מתקיים תנאי המעבר מצפוף לדליל. אם זווית הפגיעה גדולה מספיק (מעל הזווית הקריטית), מתרחשת החזרת אור פנימית מלאה, והקרן קופצת חזרה פנימה בזווית שווה. כך, קרן האור "מקפצת" לאורך הליבה, מוחזרת שוב ושוב מדפנותיה, ומתקדמת קדימה גם כשהסיב מתעקל. הסימולטור למעלה מציג את המסע המרתק הזה!</p>
    <p><b>התנסו בעצמכם בסימולטור:</b> שנו את "זווית הכניסה" ואת "מיקום הכניסה". שימו לב מה קורה כאשר זווית הכניסה גדולה מדי – האור פוגע בדופן הליבה בזווית *קטנה* מהקריטית, הוא נשבר אל תוך המעטפת ו"בורח"! רק קרניים הנכנסות בזווית הנכונה נכלאות בליבה וממשיכות לנוע לאורכה באמצעות TIR.</p>

    <h3>למה זה חשוב? שימושים מדהימים!</h3>
    <p>סיבים אופטיים הם הרבה יותר מסתם טריק פיזיקלי יפה. הם עמוד התווך של העולם המודרני:</p>
    <ul>
        <li><b>האינטרנט שאתם מכירים:</b> רוב תעבורת המידע העולמית (אינטרנט, שיחות טלפון, טלוויזיה) עוברת כיום בסיבים אופטיים תת-ימיים ויבשתיים.</li>
        <li><b>רפואה מתקדמת:</b> אנדוסקופים (המצלמות הזעירות ש"מציצות" לתוך הגוף) משתמשים בסיבים אופטיים להעברת אור ותמונה. גם טיפולי לייזר רבים נעשים באמצעות סיבים.</li>
        <li><b>תעשייה וחיישנים:</b> משמשים למדידות מדויקות בסביבות קיצוניות ולמגוון רחב של חיישנים.</li>
        <li><b>תאורה ועיצוב:</b> מאפשרים להעביר אור למקומות קשים לגישה וליצור אפקטים ויזואליים מרהיבים.</li>
    </ul>
    <p>הסיב האופטי הוא דוגמה אלגנטית לאופן שבו עקרון פיזיקלי יחיד יכול להוביל למהפכה טכנולוגית עצומה שמשפיעה על חיי כולנו.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('fiberCanvas');
    const ctx = canvas.getContext('2d');
    const angleSlider = document.getElementById('angleSlider');
    const angleValueSpan = document.getElementById('angleValue');
    const positionSlider = document.getElementById('positionSlider');
    const positionValueSpan = document.getElementById('positionValue');
    const toggleButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');
    const resetButton = document.getElementById('resetButton');
    const statusMessage = document.getElementById('status-message');

    // Constants for physics and drawing
    const n1 = 1.5; // Refractive index of core (e.g., glass)
    const n2 = 1.3; // Refractive index of cladding (e.g., different glass or plastic)
    const criticalAngleRad = Math.asin(n2 / n1); // Critical angle in radians
    const criticalAngleDeg = radToDeg(criticalAngleRad);

    const fiberWidth = canvas.width;
    const fiberHeight = canvas.height;
    const coreHeight = fiberHeight * 0.6; // Core takes 60% of height
    const claddingHeight = (fiberHeight - coreHeight) / 2; // Cladding on top/bottom

    const pixelsPerFrame = 8; // Speed of ray animation (pixels per frame)
    let animationId = null; // To hold the requestAnimationFrame ID

    // Ray state
    let rayX, rayY, rayAngleRad;
    let isAnimating = false;
    let rayColor = '#e74c3c'; // Default ray color (core)

    // Function to convert degrees to radians
    function degToRad(degrees) {
        return degrees * (Math.PI / 180);
    }

    // Function to convert radians to degrees
    function radToDeg(radians) {
        return radians * (180 / Math.PI);
    }

    // Function to draw the fiber structure
    function drawFiber() {
        // Draw cladding area (canvas background color is cladding)
        ctx.fillStyle = '#eef'; // Light blue
        ctx.fillRect(0, 0, fiberWidth, fiberHeight);

        // Draw core
        ctx.fillStyle = '#ffffff'; // White for core
        ctx.fillRect(0, claddingHeight, fiberWidth, coreHeight);

        // Draw core boundaries
        ctx.strokeStyle = '#aaa'; // Softer boundary color
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(0, claddingHeight);
        ctx.lineTo(fiberWidth, claddingHeight);
        ctx.moveTo(0, claddingHeight + coreHeight);
        ctx.lineTo(fiberWidth, claddingHeight + coreHeight);
        ctx.stroke();
    }

    // Function to draw a single segment of the ray
    function drawRaySegment(x1, y1, x2, y2, color) {
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);
        ctx.stroke();
    }

    // Function to draw normal and angle indicators at a point
    function drawAngleIndicators(x, y, angleRad, hitBoundary) {
        // Draw dot at incidence point
        ctx.fillStyle = '#333';
        ctx.beginPath();
        ctx.arc(x, y, 3, 0, Math.PI * 2);
        ctx.fill();

        // Draw normal line (vertical)
        ctx.strokeStyle = '#7f8c8d'; // Grey
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(x, y - 20);
        ctx.lineTo(x, y + 20);
        ctx.stroke();

        // Calculate angle of incidence (relative to normal)
        // The ray angle 'angleRad' is relative to the horizontal (x-axis).
        // The normal is vertical (y-axis).
        // Angle of incidence = |90 degrees - ray angle relative to horizontal|
        const angleOfIncidenceRad = Math.PI / 2 - Math.abs(angleRad);

        // Draw angle of incidence arc
        const arcRadius = 15;
        ctx.strokeStyle = '#f39c12'; // Orange
        ctx.lineWidth = 1.5;

        // Determine start and end angles for the arc based on which boundary was hit
        let startAngle, endAngle;
        // If hit top boundary (going up), angle is between ray and normal pointing down (-PI/2)
        // If hit bottom boundary (going down), angle is between ray and normal pointing up (PI/2)
        if (hitBoundary === 'top') {
            // Ray going up (sin(angleRad) > 0), normal is effectively down (-PI/2)
             // Angle of incidence is relative to the downward normal
            startAngle = Math.PI / 2; // Start from the normal (pointing up, for drawing convenience)
            endAngle = Math.PI / 2 + angleOfIncidenceRad * Math.sign(angleRad); // End towards the ray
             if (angleRad > 0) { // Ray goes up-right
                 startAngle = Math.PI / 2 - angleOfIncidenceRad;
                 endAngle = Math.PI / 2;
             } else { // Ray goes up-left (this shouldn't happen if entering from left) - but for completeness
                  startAngle = Math.PI/2;
                  endAngle = Math.PI/2 + angleOfIncidenceRad;
             }
             // Correcting for drawing from X=0 only: rayAngleRad will be between -PI/2 and PI/2
             // If hitting top, rayAngleRad > 0. Normal is vertical.
             // Angle of incidence is 90 - angleRad. Arc goes from vertical up towards ray path.
             startAngle = -Math.PI/2 + 0.05; // Small offset from normal
             endAngle = -Math.PI/2 + angleOfIncidenceRad - 0.05; // Small offset
             if (angleRad < 0) { // Should not happen at X=0, but necessary if ray enters from right
                  startAngle = -Math.PI/2 - angleOfIncidenceRad + 0.05;
                  endAngle = -Math.PI/2 - 0.05;
             }


        } else { // hitBottom (going down)
             // Ray going down (sin(angleRad) < 0). Normal is effectively up (PI/2)
             // Angle of incidence is relative to the upward normal
             startAngle = Math.PI / 2 - angleOfIncidenceRad + 0.05; // Start from normal (pointing up)
             endAngle = Math.PI / 2 - 0.05; // End towards ray
             if (angleRad > 0) { // Ray goes down-right
                 startAngle = Math.PI/2 - angleOfIncidenceRad + 0.05;
                 endAngle = Math.PI/2 - 0.05;
             } else { // Ray goes down-left
                 startAngle = Math.PI/2 + 0.05;
                 endAngle = Math.PI/2 + angleOfIncidenceRad - 0.05;
             }

        }

         // Simpler approach: Draw angle from normal (vertical line) towards ray.
         // Angle of incidence is relative to the normal.
         // Ray angle is relative to horizontal.
         // Angle between ray and normal is PI/2 - |rayAngleRad|.
         // If rayAngleRad > 0 (going up/right), ray path is between horizontal and +PI/2. Normal is vertical.
         // If rayAngleRad < 0 (going down/right), ray path is between horizontal and -PI/2. Normal is vertical.

         const normalAngle = hitBoundary === 'top' ? -Math.PI/2 : Math.PI/2; // Normal direction for drawing convenience
         const rayDirection = angleRad; // Ray direction relative to horizontal

         // Draw angle of incidence arc from the normal towards the ray
         ctx.beginPath();
         // Need to handle arc direction (clockwise/counter-clockwise) correctly
         // Draw from normal towards the ray direction relative to normal
         const effectiveNormalAngle = hitBoundary === 'top' ? -Math.PI/2 : Math.PI/2;
         const angleFromNormalToRay = angleOfIncidenceRad; // This is always positive by definition

         // Let's use the actual ray angle relative to the horizontal axis for arc drawing reference
         const angleRelativeToHorizontal = angleRad;

          // Start arc from the normal line. The normal is vertical.
          // Need to figure out the correct start and end angles for the arc relative to the canvas coordinate system (0 is right, PI/2 is down).
          // Normal is at -PI/2 (up) and PI/2 (down).
          // Angle of incidence is always measured from the normal towards the ray path.

          // Let's simplify: Draw arc from vertical line segment starting at y towards the ray direction.
          // Angle of incidence is PI/2 - |angleRad|.
          // The arc should go from the vertical line AT y, towards the ray's direction.

          let normX = x;
          let normY1 = y - 20; // Point on normal up
          let normY2 = y + 20; // Point on normal down

          // Determine arc angles relative to horizontal (0 radians to the right)
          // Arc is centered at (x, y).
          // It should span from the normal direction to the ray direction.
          // Normal direction is vertical (PI/2 or -PI/2). Ray direction is angleRad.

          // Angle of incidence arc:
           if (hitBoundary === 'top') { // Normal points "down" relative to the core boundary
               startAngle = -Math.PI/2; // Towards normal up
               endAngle = startAngle + angleOfIncidenceRad; // Towards ray (assuming angleRad > 0)
               if (angleRad < 0) endAngle = startAngle - angleOfIncidenceRad; // Towards ray (assuming angleRad < 0)
               // Adjust for visual direction relative to actual ray
               if (angleRad > 0) { // ray is up/right
                    startAngle = -Math.PI/2;
                    endAngle = -Math.PI/2 + angleOfIncidenceRad;
               } else { // ray is up/left (should not happen from x=0)
                    startAngle = -Math.PI/2 - angleOfIncidenceRad;
                    endAngle = -Math.PI/2;
               }

           } else { // hitBottom - Normal points "up" relative to the core boundary
              startAngle = Math.PI/2; // Towards normal down
              endAngle = startAngle - angleOfIncidenceRad; // Towards ray (assuming angleRad > 0)
              if (angleRad < 0) endAngle = startAngle + angleOfIncidenceRad; // Towards ray (assuming angleRad < 0)
              // Adjust for visual direction relative to actual ray
               if (angleRad > 0) { // ray is down/right
                   startAngle = Math.PI/2 - angleOfIncidenceRad;
                   endAngle = Math.PI/2;
               } else { // ray is down/left (should not happen from x=0)
                   startAngle = Math.PI/2;
                   endAngle = Math.PI/2 + angleOfIncidenceRad;
               }
           }

        // Let's simplify again. Draw the arc from the *actual vertical line* towards the ray.
        // The angle of incidence is between the ray and the vertical.
        // The vertical line at (x,y) goes from (x, y-10) to (x, y+10).
        // The ray goes from (x,y) towards (x + cos(angleRad), y + sin(angleRad)).
        // We want to draw an arc from (x, y+10) or (x, y-10) depending on hitBoundary, towards the ray.

        // For a bounce at y = claddingHeight (top): Normal is down. Angle of incidence is measured from DOWNWARDS vertical line.
        // For a bounce at y = claddingHeight + coreHeight (bottom): Normal is up. Angle of incidence is measured from UPWARDS vertical line.

        if (hitBoundary === 'top') { // Normal "down" relative to core
             startAngle = Math.PI / 2; // Downwards vertical
             endAngle = Math.PI / 2 + (Math.PI / 2 - Math.abs(angleRad)); // Towards ray
              if (angleRad < 0) { // Ray going up/left - shouldn't happen from start=0
                   endAngle = Math.PI/2 - (Math.PI/2 - Math.abs(angleRad));
              }
        } else { // hitBottom - Normal "up" relative to core
             startAngle = -Math.PI / 2; // Upwards vertical
             endAngle = -Math.PI / 2 - (Math.PI / 2 - Math.abs(angleRad)); // Towards ray
             if (angleRad < 0) { // Ray going down/left
                 endAngle = -Math.PI / 2 + (Math.PI / 2 - Math.abs(angleRad));
             }
        }

         // Correct angles for Canvas arc: 0=right, PI/2=down, PI=left, -PI/2=up.
         // Normal up is -PI/2. Normal down is PI/2.
         // Angle of incidence is measured from the normal.
         // If hit top, normal is down (PI/2). Angle of incidence is between ray and down vertical.
         // If hit bottom, normal is up (-PI/2). Angle of incidence is between ray and up vertical.

         let arcStart, arcEnd, arcClockwise;
         const angleIncidCanvas = Math.PI/2 - Math.abs(angleRad); // Angle of incidence, positive value

         if (hitBoundary === 'top') { // Normal points to PI/2 (down)
             arcStart = Math.PI/2; // Start from downward normal
             if (angleRad > 0) { // Ray is upwards-right
                arcEnd = Math.PI/2 - angleIncidCanvas; // Arc towards ray path
                arcClockwise = false;
             } else { // Ray is upwards-left (should not happen from x=0)
                arcEnd = Math.PI/2 + angleIncidCanvas;
                arcClockwise = true;
             }
         } else { // hitBottom - Normal points to -PI/2 (up)
            arcStart = -Math.PI/2; // Start from upward normal
            if (angleRad > 0) { // Ray is downwards-right
               arcEnd = -Math.PI/2 + angleIncidCanvas; // Arc towards ray path
               arcClockwise = true;
            } else { // Ray is downwards-left
               arcEnd = -Math.PI/2 - angleIncidCanvas;
               arcClockwise = false;
            }
         }


        ctx.beginPath();
        ctx.arc(x, y, arcRadius, arcStart, arcEnd, arcClockwise);
        ctx.stroke();

        // Draw Critical angle arc for comparison
        const criticalArcRadius = arcRadius + 5;
        ctx.strokeStyle = '#2ecc71'; // Green
        ctx.lineWidth = 1.5;

        // Critical angle arc goes from normal up to critical angle
        let criticalArcStart, criticalArcEnd, criticalArcClockwise;

         if (hitBoundary === 'top') { // Normal is effectively PI/2 (down)
             criticalArcStart = Math.PI/2;
             criticalArcEnd = Math.PI/2 - criticalAngleRad;
             criticalArcClockwise = false;
             // Also draw the other side
             ctx.beginPath();
             ctx.arc(x, y, criticalArcRadius, Math.PI/2, Math.PI/2 + criticalAngleRad, true);
             ctx.stroke();

         } else { // hitBottom - Normal is effectively -PI/2 (up)
             criticalArcStart = -Math.PI/2;
             criticalArcEnd = -Math.PI/2 + criticalAngleRad;
             criticalArcClockwise = true;
              // Also draw the other side
             ctx.beginPath();
             ctx.arc(x, y, criticalArcRadius, -Math.PI/2, -Math.PI/2 - criticalAngleRad, false);
             ctx.stroke();
         }

        ctx.beginPath();
        ctx.arc(x, y, criticalArcRadius, criticalArcStart, criticalArcEnd, criticalArcClockwise);
        ctx.stroke();


        // Add text labels (optional, can clutter) - let's skip text for now, visual is better
    }


    // Animation function
    function animateRay(timestamp) {
        if (!isAnimating) return;

        const vx = Math.cos(rayAngleRad);
        const vy = Math.sin(rayAngleRad);

        // Calculate next small step
        const dt = pixelsPerFrame; // Move fixed distance each frame
        const nextX = rayX + vx * dt;
        const nextY = rayY + vy * dt;

        // Check if hitting boundary in this step
        let hitBoundary = null;
        let bounceX = nextX, bounceY = nextY;

        // Check Top boundary
        if (vy < 0 && rayY >= claddingHeight && nextY < claddingHeight) {
             // Ray is going up and crosses top boundary
             // Find exact intersection point
             const t = (claddingHeight - rayY) / vy;
             bounceX = rayX + vx * t;
             bounceY = claddingHeight;
             hitBoundary = 'top';
        }
        // Check Bottom boundary
        else if (vy > 0 && rayY <= (claddingHeight + coreHeight) && nextY > (claddingHeight + coreHeight)) {
             // Ray is going down and crosses bottom boundary
             // Find exact intersection point
             const t = (claddingHeight + coreHeight - rayY) / vy;
             bounceX = rayX + vx * t;
             bounceY = claddingHeight + coreHeight;
             hitBoundary = 'bottom';
        }

        // Draw segment up to bounce point or next step point
        const segmentEndX = hitBoundary ? bounceX : nextX;
        const segmentEndY = hitBoundary ? bounceY : nextY;

        // Clear canvas and redraw fiber structure *before* drawing current segment
        // This ensures previous animation frames are erased, but the fiber is visible.
        // DRAWING THE WHOLE FIBER EACH FRAME IS INEFFICIENT, BUT SIMPLER FOR THIS CASE.
        // A better way would be to clear only the area of the ray movement or draw on an overlay canvas.
        // Sticking to constraints, let's redraw fiber - performance might degrade for many bounces.
        drawFiber();

        // Redraw the ray path drawn so far
        // This requires storing the ray's path... which makes the animation stateful.
        // Let's rethink: draw the entire ray path *up to the current animation point*.
        // Store bounce points and types. Re-calculate path up to current point each frame.
        // This is also complex.

        // Alternative approach: Draw fiber once. In animation loop, clear only the previous ray drawing, then draw the new ray position/segments.
        // This requires storing previous ray segments.

        // Simplest (and likely intended): Draw segment by segment *on top* of the static fiber.
        // This leaves trails. User might prefer trails for understanding. Let's try that.

        drawRaySegment(rayX, rayY, segmentEndX, segmentEndY, rayColor);

        rayX = segmentEndX;
        rayY = segmentEndY;

        // Check for hitting end of fiber
        if (rayX >= fiberWidth) {
            statusMessage.textContent = 'האור הגיע לקצה הסיב!';
            isAnimating = false;
            return;
        }

        // Handle bounce
        if (hitBoundary) {
            const angleOfIncidenceRad = Math.PI / 2 - Math.abs(rayAngleRad); // Angle relative to normal

            // Draw angle indicators at the bounce point BEFORE updating the angle/color
            drawAngleIndicators(rayX, rayY, rayAngleRad, hitBoundary);

            if (angleOfIncidenceRad >= criticalAngleRad - 1e-3) { // Use tolerance for float comparison
                // Total Internal Reflection (TIR)
                rayAngleRad = -rayAngleRad; // Reflect angle across horizontal
                rayColor = '#e74c3c'; // Keep ray red (in core)
                statusMessage.textContent = 'החזרת אור פנימית מלאה!';
            } else {
                // Refraction occurs
                rayColor = '#3498db'; // Change ray color (entering cladding)
                 // Calculate refracted angle (relative to horizontal)
                 // Snell's Law: n1 * sin(theta_i) = n2 * sin(theta_r)
                 // theta_i is angleOfIncidenceRad (relative to normal)
                 const sinThetaR = (n1 / n2) * Math.sin(angleOfIncidenceRad);
                 const angleOfRefractionRad_Normal = Math.asin(Math.max(-1, Math.min(1, sinThetaR))); // Angle relative to normal

                 // Convert angle relative to normal to angle relative to horizontal
                 // If hit top, normal is down (PI/2). Refracted angle relative to horizontal is PI/2 + angleRefracted_Normal.
                 // If hit bottom, normal is up (-PI/2). Refracted angle relative to horizontal is -PI/2 - angleRefracted_Normal.

                 if (hitBoundary === 'top') {
                      // Ray hit top (going up). Normal is "down". Refracted ray goes "down" and away from normal.
                      rayAngleRad = Math.PI / 2 + angleOfRefractionRad_Normal;
                 } else { // hitBottom
                     // Ray hit bottom (going down). Normal is "up". Refracted ray goes "up" and away from normal.
                      rayAngleRad = -Math.PI / 2 - angleOfRefractionRad_Normal;
                 }
                 // The angle sign needs to match the original direction away from core
                 if (vy < 0) { // Was going up (hit top)
                      rayAngleRad = Math.PI/2 + angleOfRefractionRad_Normal; // Refracted ray goes down
                 } else { // Was going down (hit bottom)
                     rayAngleRad = -Math.PI/2 - angleOfRefractionRad_Normal; // Refracted ray goes up
                 }


                statusMessage.textContent = 'האור נשבר וברח אל המעטפת!';
                isAnimating = false; // Stop animation after refraction
            }
        }

        if (isAnimating) {
            animationId = requestAnimationFrame(animateRay);
        }
    }

    // Function to start or restart the animation
    function startRayAnimation() {
        if (animationId) {
            cancelAnimationFrame(animationId); // Cancel any existing animation
        }
        isAnimating = true;
        statusMessage.textContent = 'האור בתנועה...';

        // Get values from sliders
        const initialAngleDeg = parseFloat(angleSlider.value);
        const initialPositionRatio = parseFloat(positionSlider.value);

        // Calculate initial ray position and angle
        rayX = 0;
        // Y position relative to canvas top: claddingHeight + half_core + ratio * half_core
        rayY = claddingHeight + coreHeight / 2 + initialPositionRatio * (coreHeight / 2);

        // Angle relative to horizontal axis (0=right). Slider is angle relative to fiber axis.
        // A positive slider angle means going up from the center.
        // Canvas Y increases downwards. So positive slider angle (up) means negative angleRad.
        rayAngleRad = -degToRad(initialAngleDeg);
        rayColor = '#e74c3c'; // Start red (in core)

        // Clear canvas and draw initial state
        drawFiber();
        // Draw the very first segment entering the fiber
        // Let's just start the animation loop directly from (rayX, rayY)
        // drawRaySegment(rayX, rayY, rayX + pixelsPerFrame * Math.cos(rayAngleRad), rayY + pixelsPerFrame * Math.sin(rayAngleRad), rayColor);

        // Start the animation loop
        animationId = requestAnimationFrame(animateRay);
    }


    // Event listeners for sliders
    angleSlider.addEventListener('input', () => {
        angleValueSpan.textContent = parseFloat(angleSlider.value) + '°';
        startRayAnimation(); // Restart animation on slider change
    });

    positionSlider.addEventListener('input', () => {
        positionValueSpan.textContent = parseFloat(positionSlider.value).toFixed(2);
        startRayAnimation(); // Restart animation on slider change
    });

    // Event listener for the reset button
    resetButton.addEventListener('click', () => {
        startRayAnimation(); // Restart animation
    });


    // Event listener for the toggle button
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר את הסיפור המלא' : 'הצג את הסיפור המלא';
         // Scroll to explanation if showing it (optional but nice UX)
        if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth' });
        }
    });

    // Initial setup: Draw fiber and start first animation
    drawFiber();
    startRayAnimation();
});
</script>
```