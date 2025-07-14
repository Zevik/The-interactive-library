---
title: "ריגוש הכבידה: מסע אל המרחב-זמן המעוקם של איינשטיין"
english_slug: spacetime-curvature-understanding-einsteins-gravity
category: "פיזיקה"
tags:
  - מרחב-זמן
  - יחסות כללית
  - כוח המשיכה
  - איינשטיין
  - עקמומיות
  - סימולציה
---
<div class="page-container">
    <h1 class="title">ריגוש הכבידה: מסע אל המרחב-זמן המעוקם של איינשטיין</h1>
    <p class="intro-text">שכחו את "כוח המשיכה" המסתורי של ניוטון. אלברט איינשטיין גילה שהסיפור הרבה, הרבה יותר מוזר - ומדהים! הצטרפו אלינו למסע ויזואלי כדי לגלות כיצד עצמים עם מסה אינם מושכים זה את זה, אלא פשוט רוקדים בתוך המארג המעוקם של היקום עצמו.</p>

    <div id="app" class="simulation-container">
        <canvas id="spacetimeCanvas" width="600" height="600"></canvas>
        <div id="controls" class="controls-panel">
            <div class="control-group">
                <label for="massSizeSlider">עוצמת העקמומיות (מסת כוכב/חור שחור):</label>
                <input type="range" id="massSizeSlider" min="10" max="300" value="150">
                <span id="massSizeValue">150</span>
            </div>
            <div class="control-group">
                <label for="launchVelocitySlider">מהירות שיגור:</label>
                <input type="range" id="launchVelocitySlider" min="1" max="150" value="80">
                 <span id="launchVelocityValue">80</span>
            </div>
             <div class="control-group">
                <label for="launchAngleSlider">זווית שיגור (יחסית לימין):</label>
                <input type="range" id="launchAngleSlider" min="-90" max="90" value="0">
                 <span id="launchAngleValue">0°</span>
            </div>
            <button id="launchObjectBtn" class="action-button primary-button">שגר עצם!</button>
            <button id="resetBtn" class="action-button secondary-button">אפס</button>
        </div>
    </div>

    <button id="toggleExplanationBtn" class="toggle-button">הצג את הסיפור המלא מאחורי העקמומיות</button>

    <div id="explanationSection" class="explanation-panel" style="display: none;">
        <h2 class="explanation-title">הסיפור המדהים של מרחב-זמן מעוקם</h2>

        <p>שנים רבות האמנו שכוח המשיכה הוא "כוח" מסתורי שפועל מרחוק, מושך תפוחים לארץ וכוכבי לכת לשמש. אייזק ניוטון נתן לנו את הנוסחאות המדויקות לכך, והן עבדו נהדר!</p>

        <h3>אבל אז הגיע איינשטיין...</h3>
        <p>אלברט איינשטיין הסתכל על התמונה הגדולה וראה משהו עמוק ויפה הרבה יותר. הוא הבין שמרחב (3 ממדים) וזמן (ממד 1) אינם ישויות נפרדות, אלא ארוגים יחד במארג גמיש אחד ויחיד: **מרחב-זמן**.</p>

        <h3>מסה ואנרגיה מעקמות את המארג!</h3>
        <p>התובנה הגאונית היא שמסה ואנרגיה אינן סתם "יושבות" במארג הזה - הן מפסלות אותו! דמיינו יריעת גומי גדולה ומתוחה (זה המרחב-זמן). כשאתם מניחים עליה כדור באולינג כבד (זה כוכב או חור שחור), היריעה מתעקמת סביבו, נכון? כך בדיוק מסה ואנרגיה מעקמות את המרחב-זמן!</p>

        <h3>תנועה אינה משיכה, היא פשוט "הליכה ישרה" במארג מעוקם</h3>
        <p>עכשיו, דמיינו שאתם מגלגלים גולה קטנה (עצם אחר) על היריעה המעוקמת. הגולה לא "נמשכת" לכדור הבאולינג, היא פשוט ממשיכה לנוע בקו ישר על פני השטח *המעוקם* של היריעה. לנו, הצופים מלמעלה, נראה שהגולה נמשכת לכדור הבאולינג ונעשית במסלול מעוקל - מסלול שהוא למעשה הדרך ה"ישרה ביותר" על פני השטח הלא-שטוח. זהו בדיוק מה שקורה ביקום! כוכבי לכת נעים במסלולים עגולים סביב השמש לא בגלל "כוח משיכה" שמושך אותם, אלא כי הם פשוט עוקבים אחר הדרך הישרה ביותר במרחב-זמן המעוקם שהשמש יצרה סביבה!</p>

        <h3>האפליקציה ממחישה את האנלוגיה:</h3>
        <ul>
            <li>הקנבס עם הרשת מייצג את המרחב-זמן.</li>
            <li>המסה במרכז יוצרת את העקמומיות (שימו לב איך הרשת מתעקמת כשהמסה גדלה!).</li>
            <li>העצמים שאתם משגרים נעים לאורך ה"דרכים הישרות" (גיאודזיות) במארג המעוקם - אנחנו רואים את המסלולים הללו כ"כוח משיכה".</li>
        </ul>

        <h3>הוכחות מדהימות מהיקום</h3>
        <p>הרעיון המהפכני של איינשטיין נשמע אולי מוזר, אבל הוא הוכח שוב ושוב:</p>
        <ul>
            <li>**סטיית אור:** אור מכוכבים רחוקים מתכופף כשהוא חולף ליד עצמים מסיביים כמו גלקסיות. למה? כי האור עוקב אחר העקמומיות שהגלקסיה יצרה במרחב-זמן! תופעה זו, "עידוש כבידתי", מאפשרת לנו לראות עצמים רחוקים ואף לגלות חומר אפל.</li>
            <li>**הזזת מסלול כוכב חמה:** המסלול של מרקורי סביב השמש זז קצת בכל הקפה - תופעה קטנה שנוסחאות ניוטון לא הצליחו להסביר, אבל איינשטיין כן!</li>
            <li>**גלי כבידה:** כשחורים שחורים מתנגשים, הם יוצרים "אדוות" ענקיות במארג המרחב-זמן שמתפשטות ביקום במהירות האור. את הגלים האלה הצלחנו לגלות ישירות רק לאחרונה!</li>
        </ul>
        <p>אז בפעם הבאה שאתם רואים משהו נופל, זכרו שזו אינה משיכה מסתורית, אלא פשוט ריקוד אלגנטי על פני האריג הגמיש והמעוקם של היקום עצמו!</p>
    </div>
</div>

<style>
    /* כללי גופן וצבעים */
    :root {
        --primary-color: #4A90E2; /* כחול מרחב */
        --secondary-color: #50E3C2; /* ירוק טרי */
        --accent-color: #F5A623; /* כתום אנרגטי */
        --background-color: #1A202C; /* רקע כהה - אווירת חלל */
        --card-background: #2D3748; /* רקע כרטיס כהה יותר */
        --text-color: #E2E8F0; /* טקסט בהיר */
        --control-text-color: #A0AEC0; /* טקסט פקד */
        --border-color: #4A5568; /* צבע גבולות */
        --mass-color: #E53E3A; /* אדום מסה */
        --object-color: #63B3ED; /* כחול עצם */
        --grid-color: rgba(113, 128, 150, 0.5); /* אפור רשת שקוף */
        --trail-color: rgba(99, 179, 237, 0.3); /* כחול שקוף לשביל */
    }

    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.8;
        color: var(--text-color);
        background-color: var(--background-color);
        margin: 0;
        padding: 20px;
        direction: rtl; /* עברית */
    }

    .page-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 0 15px;
    }

    .title {
        text-align: center;
        color: var(--secondary-color);
        margin-bottom: 20px;
        font-size: 2.2em;
        text-shadow: 0 0 10px rgba(80, 227, 194, 0.3);
    }

    .intro-text {
        text-align: center;
        margin-bottom: 40px;
        font-size: 1.1em;
        color: var(--control-text-color);
    }

    /* מיכל הסימולציה */
    .simulation-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 20px auto;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--card-background);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
    }

    #spacetimeCanvas {
        border: 1px solid var(--border-color);
        background: radial-gradient(circle at center, #2D3748 0%, #1A202C 100%); /* רקע גרדיאנט עמוק */
        cursor: crosshair;
        box-shadow: 0 5px 15px rgba(0,0,0,0.5);
        border-radius: 8px;
    }

    /* פאנל בקרה */
    .controls-panel {
        margin-top: 20px;
        display: flex;
        flex-direction: column;
        gap: 15px;
        width: 100%;
        max-width: 600px; /* רוחב תואם קנבס */
        color: var(--control-text-color);
    }

    .control-group {
        display: flex;
        align-items: center;
        gap: 10px;
        flex-wrap: wrap;
        background-color: #4A5568; /* רקע כהה יותר לפקד */
        padding: 8px 12px;
        border-radius: 6px;
    }

    .control-group label {
        flex-basis: 180px;
        text-align: right;
        font-weight: bold;
        color: var(--text-color);
        font-size: 0.95em;
    }

    .control-group span {
         min-width: 40px;
         text-align: left;
         font-weight: bold;
         color: var(--secondary-color);
    }

    .controls-panel input[type="range"] {
        flex-grow: 1;
        min-width: 100px;
        -webkit-appearance: none; /* הסרת עיצוב ברירת מחדל */
        appearance: none;
        height: 8px;
        background: var(--background-color);
        outline: none;
        opacity: 0.8;
        transition: opacity .2s ease;
        border-radius: 5px;
    }

    .controls-panel input[type="range"]:hover {
        opacity: 1;
    }

    /* סגנון ידית הסליידר */
    .controls-panel input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 18px;
        height: 18px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 0 5px rgba(74, 144, 226, 0.5);
    }

    .controls-panel input[type="range"]::-moz-range-thumb {
        width: 18px;
        height: 18px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 0 5px rgba(74, 144, 226, 0.5);
    }


    /* כפתורים */
    .action-button {
        padding: 12px 20px;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        width: calc(100% - 20px); /* Make buttons wider */
        margin: 5px auto;
        font-weight: bold;
        text-align: center;
    }

    .primary-button {
        background-color: var(--secondary-color);
        color: var(--background-color);
    }

    .primary-button:hover {
        background-color: #40C0A8;
        transform: translateY(-2px);
    }

     .secondary-button {
         background-color: var(--border-color);
         color: var(--text-color);
     }

     .secondary-button:hover {
         background-color: #5A677E;
         transform: translateY(-2px);
     }


    /* כפתור הצגת הסבר */
    .toggle-button {
        display: block;
        margin: 30px auto 20px auto;
        padding: 10px 25px;
        cursor: pointer;
        border: 1px solid var(--border-color);
        border-radius: 6px;
        background-color: var(--card-background);
        color: var(--text-color);
        font-size: 1em;
        transition: background-color 0.3s ease, border-color 0.3s ease;
        font-weight: bold;
    }

     .toggle-button:hover {
        background-color: #3A455A;
        border-color: var(--primary-color);
     }


    /* פאנל הסבר */
    .explanation-panel {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--card-background);
        line-height: 1.8;
        color: var(--control-text-color);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }

    .explanation-title {
        margin-top: 0;
        margin-bottom: 20px;
        color: var(--primary-color);
        text-align: center;
        border-bottom: 2px solid var(--secondary-color);
        padding-bottom: 10px;
        font-size: 1.8em;
    }

     .explanation-panel h3 {
         margin-top: 30px;
         margin-bottom: 15px;
         color: var(--secondary-color);
         font-size: 1.4em;
     }

    .explanation-panel p {
        margin-bottom: 18px;
    }

    .explanation-panel ul {
         margin-top: 15px;
         margin-bottom: 18px;
         padding-right: 30px; /* כיוון עברית */
         list-style: disc;
         list-style-position: inside; /* נקודות בפנים */
    }

     .explanation-panel li {
        margin-bottom: 10px;
        line-height: 1.6;
     }

     /* שינויים למסכים קטנים */
    @media (max-width: 768px) {
        .page-container {
            padding: 0 10px;
        }

        .title {
            font-size: 1.8em;
        }

        .intro-text {
            font-size: 1em;
        }

        .simulation-container, .explanation-panel {
            padding: 15px;
        }

         #spacetimeCanvas {
             width: 100%;
             height: auto; /* גובה יתאים עצמו */
         }

        .controls-panel label {
            flex-basis: 100%; /* תוויות שורה משלהן */
            text-align: left;
            margin-bottom: 5px;
        }
         .control-group {
             flex-direction: column;
             align-items: flex-start;
             gap: 5px;
         }
          .controls-panel input[type="range"], .control-group span {
              width: 100%;
              min-width: auto;
          }
         .control-group span {
             text-align: right; /* הערך בסוף השורה */
         }

        .action-button {
            width: 100%;
            margin: 5px 0;
        }

         .toggle-button {
             font-size: 0.95em;
         }

         .explanation-title {
             font-size: 1.5em;
         }

         .explanation-panel h3 {
             font-size: 1.2em;
         }
         .explanation-panel ul {
             padding-right: 20px;
         }
    }

    /* הוספת אנימציות עדינות */
    @keyframes pulse {
      0% { transform: scale(1); }
      50% { transform: scale(1.03); }
      100% { transform: scale(1); }
    }

    #mass-circle {
        animation: pulse 2s infinite ease-in-out;
    }

</style>

<script>
    const canvas = document.getElementById('spacetimeCanvas');
    const ctx = canvas.getContext('2d');
    const massSizeSlider = document.getElementById('massSizeSlider');
    const massSizeValueSpan = document.getElementById('massSizeValue');
    const launchVelocitySlider = document.getElementById('launchVelocitySlider');
    const launchVelocityValueSpan = document.getElementById('launchVelocityValue');
    const launchAngleSlider = document.getElementById('launchAngleSlider');
    const launchAngleValueSpan = document.getElementById('launchAngleValue');
    const launchObjectBtn = document.getElementById('launchObjectBtn');
    const resetBtn = document.getElementById('resetBtn');
    const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
    const explanationSection = document.getElementById('explanationSection');

    const canvasSize = 600;
    canvas.width = canvasSize;
    canvas.height = canvasSize;

    const gridSpacing = 25; // Smaller spacing for smoother curvature visualization
    const center = { x: canvasSize / 2, y: canvasSize / 2 };

    // Initial mass parameters - visualRadius is just for drawing, influence controls deformation and 'gravity'
    let centralMass = { x: center.x, y: center.y, visualRadius: 10, influence: 150 }; // Start with higher influence
    let movingObjects = [];
    const objectRadius = 4;
    const objectColor = '#63B3ED'; // Blue
    const trailColor = 'rgba(99, 179, 237, 0.15)'; // Faded blue for trails
    const trailLength = 50; // Number of past points to store for trail

    // Grid points storage - calculated once per mass change, then drawn
    let deformedGridPoints = [];

    // Initial setup
    massSizeSlider.value = centralMass.influence;
    massSizeValueSpan.textContent = centralMass.influence;
    launchVelocitySlider.value = 80; // Default launch velocity
    launchVelocityValueSpan.textContent = launchVelocitySlider.value;
    launchAngleSlider.value = 0; // Default launch angle (right)
    launchAngleValueSpan.textContent = launchAngleSlider.value + '°';

    // --- Simulation Logic (Simulated Gravity / Geodesics) ---

     // Function to get the acceleration vector at a point due to the central mass
     // This simulates the effect of following the curved path (geodesic)
     function getAcceleration(x, y) {
         const dx = centralMass.x - x; // Vector from object to center
         const dy = centralMass.y - y;
         const distSq = dx * dx + dy * dy;

         // Prevent division by zero or huge forces very close to the center.
         // Define a "event horizon" like minimum distance square based on mass influence.
         const minDistanceFactor = 0.8; // How close to the visual edge objects can get
         const minAllowedDistSq = (centralMass.visualRadius * (centralMass.influence / 100) + 5) * (centralMass.visualRadius * (centralMass.influence / 100) + 5) * minDistanceFactor;


         if (distSq < minAllowedDistSq) {
             return { ax: 0, ay: 0, remove: true }; // Object "fell into" the mass/singularity
         }

         const dist = Math.sqrt(distSq);

         // Simulated gravitational constant (tuned for visual effect)
         // Scales with mass influence, inversely with distance squared
         const G_simulated = centralMass.influence * 15000; // Adjusted multiplier for stronger effect

         // Acceleration magnitude (simulating GM/r^2 scaled)
         const accMagnitude = G_simulated / distSq; // Use actual distSq for force calculation

         // Acceleration components pointing towards the center
         const ax = accMagnitude * (dx / dist);
         const ay = accMagnitude * (dy / dist);

         return { ax: ax, ay: ay, remove: false };
     }

    // --- Drawing Functions ---

     // Function to calculate the deformation for a point on the grid
     function getDeformedPosition(x, y) {
         const dx = centralMass.x - x;
         const dy = centralMass.y - y;
         const dist = Math.sqrt(dx * dx + dy * dy);

         // Deformation strength based on mass influence and distance
         // Using 1/dist for visual deformation intensity often looks better than 1/dist^2
         const deformationMagnitude = centralMass.influence * 0.8 / Math.max(1, dist); // Max(1, dist) to avoid division by zero/infinity

         // Displacement vector towards the mass
         const dispX = (dx / dist) * deformationMagnitude;
         const dispY = (dy / dist) * deformationMagnitude;

         return { x: x + dispX, y: y + dispY };
     }


    // Function to pre-calculate deformed grid points
    function calculateDeformedGrid() {
         deformedGridPoints = [];
         // Calculate grid points for horizontal lines
         for (let y = 0; y <= canvasSize; y += gridSpacing) {
             let rowPoints = [];
             for (let x = 0; x <= canvasSize; x += gridSpacing) {
                 rowPoints.push(getDeformedPosition(x, y));
             }
             deformedGridPoints.push(rowPoints);
         }

         // Add grid points for vertical lines (stored separately or interweaved?)
         // Let's store them conceptually as columns for drawing vertical lines later
         let colPoints = [];
         for (let x = 0; x <= canvasSize; x += gridSpacing) {
             let currentColumn = [];
              for (let y = 0; y <= canvasSize; y += gridSpacing) {
                 currentColumn.push(getDeformedPosition(x, y));
             }
             colPoints.push(currentColumn);
         }
         // Store both horizontal and vertical sets
         deformedGridPoints.vertical = colPoints;
         deformedGridPoints.horizontal = deformedGridPoints.slice(); // Copy the horizontal points
    }


    // Function to draw the deformed grid
    function drawGrid() {
        ctx.clearRect(0, 0, canvasSize, canvasSize); // Clear the whole canvas first

        ctx.strokeStyle = 'var(--grid-color)'; // Greyish, semi-transparent
        ctx.lineWidth = 0.8; // Slightly thicker lines

        // Draw horizontal lines
        if (deformedGridPoints.horizontal) {
            deformedGridPoints.horizontal.forEach(rowPoints => {
                ctx.beginPath();
                if (rowPoints.length > 0) {
                    ctx.moveTo(rowPoints[0].x, rowPoints[0].y);
                    for (let i = 1; i < rowPoints.length; i++) {
                        // Draw curve or straight line segment between deformed points
                        // A simple line segment is sufficient given enough points
                        ctx.lineTo(rowPoints[i].x, rowPoints[i].y);
                    }
                    ctx.stroke();
                }
            });
        }


        // Draw vertical lines
         if (deformedGridPoints.vertical) {
             deformedGridPoints.vertical.forEach(colPoints => {
                 ctx.beginPath();
                 if (colPoints.length > 0) {
                     ctx.moveTo(colPoints[0].x, colPoints[0].y);
                      for (let i = 1; i < colPoints.length; i++) {
                          ctx.lineTo(colPoints[i].x, colPoints[i].y);
                      }
                     ctx.stroke();
                 }
             });
         }


        // Draw central mass AFTER the grid so it's on top
        const currentMassRadius = centralMass.visualRadius * (centralMass.influence / 100) + 5; // Radius scales a bit
        ctx.fillStyle = 'var(--mass-color)'; // Red
        //ctx.shadowBlur = 20; // Add a glow effect
        //ctx.shadowColor = 'var(--mass-color)'; // Glow color
        ctx.beginPath();
        ctx.arc(centralMass.x, centralMass.y, currentMassRadius, 0, Math.PI * 2);
        ctx.fill();
        //ctx.shadowBlur = 0; // Reset shadow

        ctx.fillStyle = '#fff'; // White text
        ctx.font = 'bold 16px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText('מסה', centralMass.x, centralMass.y); // Label
    }

    // Function to draw moving objects with trails
    function drawObjects() {
        movingObjects.forEach(obj => {
             // Draw trail
            ctx.strokeStyle = trailColor;
            ctx.lineWidth = obj.radius * 1.5; // Trail width
            ctx.beginPath();
            if (obj.trail.length > 1) {
                 ctx.moveTo(obj.trail[0].x, obj.trail[0].y);
                 for (let i = 1; i < obj.trail.length; i++) {
                     ctx.lineTo(obj.trail[i].x, obj.trail[i].y);
                 }
                 ctx.stroke();
            }


            // Draw object
            ctx.fillStyle = obj.color; // Blue
            ctx.beginPath();
            ctx.arc(obj.x, obj.y, obj.radius, 0, Math.PI * 2);
            ctx.fill();
        });
    }

    // Update object positions based on simulated gravity
    function updateObjects() {
         const dt = 0.5; // Time step (adjust for stability)

         movingObjects = movingObjects.filter(obj => {
             // Check for removal (out of bounds or hit mass)
             if (obj.x < -objectRadius*5 || obj.x > canvasSize + objectRadius*5 || obj.y < -objectRadius*5 || obj.y > canvasSize + objectRadius*5) {
                 return false; // Remove if leaves bounds
             }

             // Add current position to trail
             obj.trail.push({ x: obj.x, y: obj.y });
             // Keep trail length limited
             if (obj.trail.length > trailLength) {
                 obj.trail.shift(); // Remove the oldest point
             }


             // Calculate acceleration based on simulated 'gravity'
             const acc = getAcceleration(obj.x, obj.y);

             // Remove object if it hit the mass
             if(acc.remove) return false;

             // Update velocity (Euler integration)
             obj.vx += acc.ax * dt;
             obj.vy += acc.ay * dt;

             // Update position
             obj.x += obj.vx * dt;
             obj.y += obj.vy * dt;


             return true; // Keep object if not removed
         });
     }


    // Animation loop
    function animate() {
        // Draw grid and mass (deformation calculated on mass change)
        drawGrid();
        // Update object positions
        updateObjects();
        // Draw objects
        drawObjects();

        requestAnimationFrame(animate); // Request next frame
    }

    // --- Event Listeners ---

    massSizeSlider.addEventListener('input', (e) => {
        centralMass.influence = parseInt(e.target.value);
        massSizeValueSpan.textContent = centralMass.influence;
        // Recalculate the grid deformation immediately when mass changes
        calculateDeformedGrid();
        // Redraw canvas immediately to show deformed grid
        drawGrid(); // This will be called again by animate, but good for responsiveness
    });

     launchVelocitySlider.addEventListener('input', (e) => {
        launchVelocityValueSpan.textContent = e.target.value;
     });

     launchAngleSlider.addEventListener('input', (e) => {
        launchAngleValueSpan.textContent = e.target.value + '°';
     });


    launchObjectBtn.addEventListener('click', () => {
        // Scale velocity slider value (tuned for visual effect)
        const velocityScale = 400; // Needs tuning based on gravity strength
        const initialSpeed = parseInt(launchVelocitySlider.value) / velocityScale;

        const angleDeg = parseInt(launchAngleSlider.value);
        // Convert angle from degrees to radians, 0deg is right, positive is down in canvas coords
        const angleRad = angleDeg * Math.PI / 180;

        // Launch from a fixed point on the right edge, vertically centered initially
        // Position slightly inwards to avoid immediate out-of-bounds
        const launchFromX = canvasSize - 10;
        const launchFromY = canvasSize / 2; // Launch from center of right edge initially

         // Launch velocity vector (pointing left and potentially up/down)
         const vx = -initialSpeed * Math.cos(angleRad); // cos(0)=1 -> left, cos(90)=0
         const vy = initialSpeed * Math.sin(angleRad); // sin(0)=0 -> horizontal, sin(90)=1 -> down (canvas y+ is down)

        movingObjects.push({
            x: launchFromX,
            y: launchFromY,
            vx: vx,
            vy: vy,
            radius: objectRadius,
            color: objectColor, // Blue
            trail: [] // Array to store past positions for trail
        });
    });

    resetBtn.addEventListener('click', () => {
        movingObjects = []; // Clear the array of moving objects
        // Recalculate and redraw grid just in case
        calculateDeformedGrid();
        drawGrid();
        // The animation loop will continue and redraw objects (which are now none)
    });

    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationSection.style.display === 'none';
        explanationSection.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר את הסיפור המלא' : 'הצג את הסיפור המלא מאחורי העקמומיות';
         // Optional: scroll to explanation if shown
         if (isHidden) {
             explanationSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });


    // Initial setup: calculate grid once, draw, and start animation
    calculateDeformedGrid(); // Calculate the initial grid deformation
    drawGrid(); // Draw the initial grid and mass
    animate(); // Start the animation loop

    // Optional: Add initial object launch for immediate visual
    // simulate initial object launch
    // launchObjectBtn.click();

</script>
```