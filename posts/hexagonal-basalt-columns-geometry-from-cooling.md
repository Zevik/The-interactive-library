---
title: "עמודי בזלת משושים: גיאומטריה שנוצרה מהתקררות"
english_slug: hexagonal-basalt-columns-geometry-from-cooling
category: "גיאולוגיה"
tags: גיאולוגיה, בזלת, סלעים ומינרלים, התקררות לבה, משושים, תופעות טבע, מדע
---
# עמודי בזלת משושים: הריקוד הקפוא של הטבע

דמיינו לבה רותחת, שזרמה באין מפריע, מתחילה להתקרר ולהתקשות לאט לאט. כשהחום מתפוגג, החומר מתכווץ, יוצר מתח פנימי עצום... ולפתע – סדקים! לא סדקים אקראיים, אלא תבנית מדויקת, כמעט בלתי נתפסת, של משושים מושלמים. איך הטבע מצליח ליצור הנדסה גיאומטרית כזו בפעולה פסיבית של קירור? בואו נצלול אל תוך התופעה המרתקת הזו ונראה אותה קורית לנגד עינינו.

<div class="simulation-container">
    <canvas id="basaltCanvas"></canvas>
    <div class="controls">
        <button id="startButton" class="control-button">התחל התקררות</button>
        <button id="toggleExplanationButton" class="control-button secondary">הסבר התופעה</button>
    </div>
</div>


<div id="explanation" class="explanation-box" style="display: none;">
    <h2>קסם גיאולוגי: מהם עמודי בזלת משושים?</h2>
    <p>עמודי בזלת משושים הם פלא טבע אמיתי. במקום בו זרמה לבה (או מגמה שהתקררה קרוב לפני השטח), כשהיא מתקשה לסלע בזלת, נוצרים עמודים זקופים, לרוב בעלי חתך משושה מושלם. למרות שלפעמים מופיעות גם צורות אחרות (מרובעות, מחומשות, משובעות), המשושה הוא האלוף הבלתי מעורער – הצורה היציבה והנפוצה ביותר. התופעה המדהימה הזו מפארת נופים וולקניים בכל העולם, מגשר הענק באירלנד ועד נחל משושים האהוב שלנו ברמת הגולן.</p>

    <h2>הסוד מאחורי הצורה: התקררות, התכווצות ומתח</h2>
    <p>הכל מתחיל מהחום העצום. כשלבה לוהטת מתחילה להתקרר מהשפה החיצונית שלה (זו שפוגשת את האוויר או המים), היא מתכווצת, בדיוק כמו חומרים רבים כשהם מאבדים חום. ההתכווצות הזו יוצרת לחץ פנימי אדיר – לחץ מתיחה – בתוך מסת הסלע המתקשה.</p>

    <h2>הרשת הגיאומטרית נחשפת: היווצרות הסדקים</h2>
    <p>כשהמתח הפנימי עולה על יכולת המתיחה של הסלע, משהו חייב "להישבר". נוצרים סדקים! הסדקים מתחילים להופיע בדרך כלל מהמשטח המתקרר והמתכווץ במהירות, ומתפשטים פנימה, לרוב בכיוון הניצב למשטח הקירור (וכך יוצרים את "העמודים"). הם בעצם רודפים אחרי אזורי המתח הגבוה בתוך הסלע.</p>

    <h2>למה דווקא משושים? עניין של יעילות!</h2>
    <p>הבחירה של הטבע בצורה המשושה אינה מקרית – היא גאונות גיאומטרית של יעילות! הסלע "רוצה" לשחרר את המתח הפנימי שלו על ידי סדיקה, אבל הוא רוצה לעשות זאת עם מינימום "מאמץ" – כלומר, על ידי יצירת שטח סדקים כולל מינימלי שעדיין יחלק את המשטח ויפיג את המתח. המתמטיקה אומרת חד משמעית: הפתרון היעיל ביותר לחלק שטח תחת מתח אחיד הוא רשת של מצולעים שבה שלושה סדקים נפגשים בכל פינה בזווית של 120 מעלות בדיוק. והצורה היחידה שמאפשרת רשת כזו? נכון, המשושה! זו הדרך הכי חסכונית מבחינה אנרגטית לפרוק את המתח בצורה אחידה על פני שטח נרחב.</p>

    <h2>לא הכל מושלם: מה משפיע על עמודי הבזלת?</h2>
    <p>למרות שהמשושה הוא הדומיננטי, לא כל עמודי הבזלת זהים. גורמים שונים משפיעים על מראה "התוצר הסופי":</p>
    <ul>
        <li>**קצב הקירור:** קירור איטי מאפשר לסדקים לגדול ולהתפשט למרחקים גדולים יותר לפני שהם נפגשים, וכך יוצרים עמודים גדולים יותר. קירור מהיר יותר "עוצר" את הסדקים מוקדם יותר ויוצר עמודים קטנים יותר.</li>
        <li>**הרכב ואיכות הסלע:** ההרכב הכימי של הלבה והאם היא אחידה או בעלת זיהומים משפיעים על החוזק ועל אופן ההיסדקות.</li>
        <li>**צורת גוף הסלע:** גוף לבה עבה או דק, אופן זרימתו והמשטח עליו הוא מתקרר (יבשה, מים) – כל אלה מכתיבים את כיווני הקירור העיקריים ואת האופן בו הסדקים מתפתחים (לרוב בניצב למשטח הקירור).</li>
    </ul>
    <p>הסימולציה שלפניכם מציגה את התהליך הפשטני והיפהפה של ההתקררות והתארגנות הסדקים לתבנית המשושה האייקונית. צפו בהסלע "נשבר" בצורה חכמה ויעילה!</p>
</div>


<style>
/* גופנים - אפשר לייבא גופן מ-Google Fonts אם רוצים מראה יוקרתי יותר */
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

body {
    font-family: 'Heebo', sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f4f4f4;
    padding: 20px;
}

h1, h2 {
    color: #5a4b41; /* צבע אדמתי כהה */
    text-align: center;
    margin-bottom: 20px;
}

h1 {
    font-size: 2.5em;
    font-weight: 700;
    border-bottom: 2px solid #d4c3b8; /* קו תחתון עדין */
    padding-bottom: 10px;
}

h2 {
    font-size: 1.8em;
    font-weight: 700;
    margin-top: 25px;
    color: #6f5e53; /* גוון אדמתי מעט בהיר יותר */
}

p {
    margin-bottom: 15px;
}

ul {
    margin-bottom: 15px;
    padding-left: 20px;
}

li {
    margin-bottom: 8px;
}


/* עיצוב הקנבס והבקרות */
.simulation-container {
    text-align: center;
    margin: 30px auto;
    max-width: 640px; /* מגביל רוחב הקונטיינר */
    background-color: #fff;
    border-radius: 12px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    overflow: hidden; /* כדי שהצל לא ייחתך */
}

#basaltCanvas {
    display: block; /* מונע רווחים מיותרים מתחת לקנבס */
    margin: 0 auto; /* ממורכז בקונטיינר */
    border-bottom: 1px solid #eee;
    background-color: #f0f0f0; /* צבע התחלתי בסיסי */
    width: 100%; /* רוחב גמיש */
    height: 400px; /* גובה קבוע או מוגדר דינמית ב JS */
    /* הסרת הborder המקורי */
}

.controls {
    padding: 15px;
    background-color: #f8f8f8;
    display: flex; /* מניח את הכפתורים בשורה */
    justify-content: center; /* ממורכז את הכפתורים */
    gap: 15px; /* רווח בין הכפתורים */
}

.control-button {
    padding: 12px 25px;
    font-size: 1.1em;
    cursor: pointer;
    border: none;
    border-radius: 25px; /* כפתורים עגולים יותר */
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-weight: 700;
    text-transform: uppercase; /* טקסט באותיות גדולות */
    letter-spacing: 0.5px;
}

.control-button#startButton {
    background-color: #7a6b60; /* צבע אדמתי חזק */
    color: white;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.control-button#startButton:hover {
    background-color: #6b5c51;
    transform: translateY(-2px); /* אפקט ריחוף עדין */
}
.control-button#startButton:active {
     transform: translateY(0); /* לחיצה */
     box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}


.control-button.secondary {
    background-color: #d4c3b8; /* צבע אדמתי בהיר יותר */
    color: #444;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
}

.control-button.secondary:hover {
    background-color: #c3b2a7;
    transform: translateY(-2px);
}
.control-button.secondary:active {
    transform: translateY(0);
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08);
}

/* עיצוב תיבת ההסבר */
.explanation-box {
    margin: 20px auto;
    max-width: 800px; /* רוחב גדול יותר להסבר */
    padding: 25px;
    border: 1px solid #d4c3b8;
    background-color: #fff; /* רקע לבן */
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    line-height: 1.7;
    color: #444;
}

.explanation-box h2 {
    color: #5a4b41;
    margin-top: 0;
    border-bottom: 2px solid #eee; /* קו הפרדה דק יותר */
    padding-bottom: 10px;
    margin-bottom: 15px;
}

.explanation-box ul {
    margin-top: 15px;
    padding-left: 30px;
}

.explanation-box li {
    margin-bottom: 10px;
    line-height: 1.5;
}


/* אנימציות CSS נוספות אם נדרש (למשל, אנימציות רקע עדינות אם לא מציירים בקנבס) */
/* כרגע רוב האנימציה היא בקנבס */

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('basaltCanvas');
    const ctx = canvas.getContext('2d');
    const startButton = document.getElementById('startButton');
    const toggleExplanationButton = document.getElementById('toggleExplanationButton');
    const explanationDiv = document.getElementById('explanation');

    // Responsive canvas size (adjust on load and resize)
    function resizeCanvas() {
        const container = canvas.parentElement;
        // Set canvas drawing surface size
        canvas.width = container.clientWidth; // Use container width
        canvas.height = 400; // Or calculate based on aspect ratio if preferred

        // Redraw current state after resize
        if (!isRunning) {
             drawCurrentState(); // Function to draw whatever is currently on screen
        } else {
             // If running, the update loop will handle redrawing
        }
    }

    window.addEventListener('resize', resizeCanvas);
    resizeCanvas(); // Initial size setting

    let animationFrameId = null;
    let isRunning = false;
    let coolingProgress = 0; // 0 to 1
    let allSegments = []; // All potential segments
    let drawnSegments = []; // Segments currently being drawn/drawn
    const coolingSpeed = 0.001; // Slower cooling for dramatic effect
    const maxSimulatedSegments = 3000; // Limit complexity for performance

    // --- Simulation & Generation Functions ---

    // Function to generate points for a somewhat irregular hexagonal grid
    // Adjusted density and jitter for potentially more points and randomness
    function generateHexGridPoints(width, height, density, jitter) {
         const points = [];
         const r = density; // Approx radius of hexagon cell
         const h = r * Math.sqrt(3); // Approx height of hexagon
         const w = 2 * r; // Approx width across points (vertex to vertex)

         // Generate points covering slightly more than the canvas
         const bufferX = w * 1.5;
         const bufferY = h * 1.5;

         for (let i = -Math.ceil(bufferY / h); i * h < height + bufferY; i++) {
             for (let j = -Math.ceil(bufferX / w); j * w + (i % 2) * r < width + bufferX; j++) {
                 const x = j * w + (i % 2) * r + (Math.random() - 0.5) * jitter;
                 const y = i * h + (Math.random() - 0.5) * jitter;
                 points.push({ x, y, i, j, distFromEdge: null }); // Store grid indices and prepare for distance calculation
             }
         }

         // Calculate distance from nearest edge for each point
         points.forEach(p => {
              const dx = Math.min(p.x, width - p.x);
              const dy = Math.min(p.y, height - p.y);
              p.distFromEdge = Math.min(dx, dy, // Distance to left/right/top/bottom
                                        Math.sqrt(p.x*p.x + p.y*p.y), // Distance to top-left corner
                                        Math.sqrt((width-p.x)*(width-p.x) + p.y*p.y), // top-right
                                        Math.sqrt(p.x*p.x + (height-p.y)*(height-p.y)), // bottom-left
                                        Math.sqrt((width-p.x)*(width-p.x) + (height-p.y)*(height-p.y)) // bottom-right
                                       );
         });


         return points;
    }

    // Function to generate segments connecting points based on grid indices
    function generateSegmentsFromPoints(points) {
        const segments = [];
        const indexMap = {}; // Map grid index string "i,j" to point object
        points.forEach(p => { indexMap[`${p.i},${p.j}`] = p; });

        const addedSegments = new Set(); // To avoid duplicates

        function addSegment(p1, p2) {
             if (!p1 || !p2) return;
             // Create a unique key for the segment regardless of point order
             const key = `${Math.min(p1.x, p2.x).toFixed(2)},${Math.min(p1.y, p2.y).toFixed(2)},${Math.max(p1.x, p2.x).toFixed(2)},${Math.max(p1.y, p2.y).toFixed(2)}`;
             if (!addedSegments.has(key)) {
                 segments.push({ p1, p2, drawProgress: 0, isComplete: false, distanceFromEdge: Math.min(p1.distFromEdge, p2.distFromEdge) });
                 addedSegments.add(key);
             }
        }

        // Connect neighbors based on indices in a hex grid
        for (const p of points) {
             const { i, j } = p;
             const parity = i % 2;

             const neighborIndices = [
                 [i, j-1], [i, j+1],
                 [i-1, j + parity - 1], [i-1, j + parity],
                 [i+1, j + parity - 1], [i+1, j + parity]
             ];

             for (const neighborIdx of neighborIndices) {
                 const n_i = neighborIdx[0];
                 const n_j = neighborIdx[1];
                 const p2 = indexMap[`${n_i},${n_j}`];
                 if (p2) {
                     addSegment(p, p2);
                 }
             }
        }

        // Sort segments by distance from the edge so cracks appear to propagate inwards
        segments.sort((a, b) => a.distanceFromEdge - b.distanceFromEdge);

        // Limit the number of segments to keep simulation manageable
        return segments.slice(0, maxSimulatedSegments);
    }


    function initializeSimulation() {
        coolingProgress = 0;
        drawnSegments = []; // Clear previous segments
        isRunning = true;
        startButton.textContent = 'במהלך התקררות...';
        startButton.disabled = true; // Disable button while running

        // Generate grid points and segments dynamically based on current canvas size
        const density = 25; // Smaller density = more points/segments
        const jitter = density * 0.3;
        const points = generateHexGridPoints(canvas.width, canvas.height, density, jitter);
        allSegments = generateSegmentsFromPoints(points);

        // Start the animation loop
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
        }
        update();
    }

    function update() {
        if (!isRunning) return;

        // Advance cooling progress
        coolingProgress += coolingSpeed;
        if (coolingProgress > 1) {
            coolingProgress = 1;
        }

        // Add new segments based on cooling progress and distance from edge
        // This part is more complex to make truly propagation-based.
        // Let's simplify: determine how many segments *should* be visible by now,
        // and animate the drawing of new ones.

        // Determine the maximum distance from edge that should have cracked by now
        // Use a non-linear function of coolingProgress (e.g., square or cubic)
        const maxDistanceToCrack = Math.max(canvas.width, canvas.height) * coolingProgress * coolingProgress;

        let segmentsToAddThisFrame = 0;
        const newSegments = [];

        // Iterate through all potential segments (sorted by distance)
        for (const segment of allSegments) {
             if (!segment.isComplete && segment.distanceFromEdge <= maxDistanceToCrack) {
                 // This segment *should* be cracking now or already cracked
                 // If it's not already being drawn or complete, add it to the drawing list
                 if (!drawnSegments.includes(segment)) {
                      newSegments.push(segment);
                      segmentsToAddThisFrame++;
                 }
             } else if (segment.distanceFromEdge > maxDistanceToCrack && drawnSegments.includes(segment)) {
                 // This segment was previously considered "crackable" but maybe the progress
                 // calculation changed? Or cooling reversed? (Not relevant for linear progress)
                 // More likely: we added it, but the animation is not done. Let its animation finish.
             }
             // Stop checking if we've found enough segments for this frame to start drawing
             // or if we reached segments too far from the edge.
             // Break early for performance if allSegments is huge
             if (segment.distanceFromEdge > maxDistanceToCrack && segmentsToAddThisFrame > 0) break; // Optimization
        }


        // Add newly selected segments to the list being drawn
        drawnSegments.push(...newSegments);

        // Animate drawing of the segments currently in drawnSegments
        // Also remove completed segment animations from drawnSegments
        const drawingSpeed = 0.08; // How fast each individual segment draws
        const segmentsStillDrawing = [];
        for (const segment of drawnSegments) {
            if (!segment.isComplete) {
                segment.drawProgress += drawingSpeed;
                if (segment.drawProgress >= 1) {
                    segment.drawProgress = 1;
                    segment.isComplete = true;
                    // Optional: Trigger a particle effect at segment ends here? Complex.
                }
                segmentsStillDrawing.push(segment); // Keep drawing
            } else {
                 segmentsStillDrawing.push(segment); // Keep complete segments visible
            }
        }
        drawnSegments = segmentsStillDrawing; // Update list to only include segments needed for drawing/display

        draw();

        // Continue simulation if cooling is not finished or cracks are still animating
        if (coolingProgress < 1 || drawnSegments.some(s => !s.isComplete)) {
           animationFrameId = requestAnimationFrame(update);
        } else {
           isRunning = false;
           startButton.textContent = 'התחל סימולציה מחדש';
           startButton.disabled = false; // Re-enable button
        }
    }

    // Helper to draw a segment partially
    function drawPartialSegment(p1, p2, progress) {
        const dx = p2.x - p1.x;
        const dy = p2.y - p1.y;
        const currentX = p1.x + dx * progress;
        const currentY = p1.y + dy * progress;
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(currentX, currentY);
    }


    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear previous frame

        // Draw background with gradient based on cooling
        const hotColor = [255, 100, 0]; // Orange/Red
        const coolColor = [100, 100, 120]; // Darker, grey-blue basalt tone
        const coldColor = [60, 60, 70]; // Even darker, solid basalt

        // Create a gradient that changes based on cooling progress
        // More complex: gradient could simulate cooling from edges inwards.
        // Let's keep it simple: a solid color based on coolingProgress, but transitioning smoothly.
        const r = hotColor[0] + (coolColor[0] - hotColor[0]) * coolingProgress;
        const g = hotColor[1] + (coolColor[1] - hotColor[1]) * coolingProgress;
        const b = hotColor[2] + (coolColor[2] - hotColor[2]) * coolingProgress;

        // If cooling is near complete, transition to the final cold color
         const finalColorProgress = Math.max(0, coolingProgress - 0.8) / 0.2; // Only start transitioning in the last 20%
         const final_r = r + (coldColor[0] - r) * finalColorProgress;
         const final_g = g + (coldColor[1] - g) * finalColorProgress;
         const final_b = b + (coldColor[2] - b) * finalColorProgress;


        ctx.fillStyle = `rgb(${Math.floor(final_r)}, ${Math.floor(final_g)}, ${Math.floor(final_b)})`;
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Draw cracks
        ctx.strokeStyle = 'rgba(0, 0, 0, 0.8)'; // Slightly transparent black cracks
        ctx.lineWidth = 2; // Thicker cracks
        ctx.lineCap = 'round'; // Rounded line ends

        ctx.beginPath();
        for (const segment of drawnSegments) {
            if (segment.drawProgress > 0) {
                 drawPartialSegment(segment.p1, segment.p2, segment.drawProgress);
            }
        }
        ctx.stroke();

        // Optional: Add a subtle glow or stress effect ahead of propagating cracks?
        // This is tricky with the current segment-based drawing but would add visual flair.
        // Skipping for now to maintain simplicity and performance.
    }

    // Draw initial state (hot surface)
    function initialDraw() {
         ctx.fillStyle = `rgb(255, 100, 0)`; // Hot color
         ctx.fillRect(0, 0, canvas.width, canvas.height);
         ctx.strokeStyle = 'black';
         ctx.lineWidth = 1.5;
         startButton.textContent = 'התחל התקררות';
         startButton.disabled = false;
    }

    // Draw the current state (used after resize)
    function drawCurrentState() {
         // Re-draw background based on coolingProgress
         const hotColor = [255, 100, 0];
         const coolColor = [100, 100, 120];
         const coldColor = [60, 60, 70];

         const r = hotColor[0] + (coolColor[0] - hotColor[0]) * coolingProgress;
         const g = hotColor[1] + (coolColor[1] - hotColor[1]) * coolingProgress;
         const b = hotColor[2] + (coolColor[2] - hotColor[2]) * coolingProgress;

         const finalColorProgress = Math.max(0, coolingProgress - 0.8) / 0.2;
         const final_r = r + (coldColor[0] - r) * finalColorProgress;
         const final_g = g + (coldColor[1] - g) * finalColorProgress;
         const final_b = b + (coldColor[2] - b) * finalColorProgress;

         ctx.fillStyle = `rgb(${Math.floor(final_r)}, ${Math.floor(final_g)}, ${Math.floor(final_b)})`;
         ctx.fillRect(0, 0, canvas.width, canvas.height);

         // Re-draw all drawn segments at their current completion level
         ctx.strokeStyle = 'rgba(0, 0, 0, 0.8)';
         ctx.lineWidth = 2;
         ctx.lineCap = 'round';

         ctx.beginPath();
         for (const segment of drawnSegments) {
              drawPartialSegment(segment.p1, segment.p2, segment.drawProgress);
         }
         ctx.stroke();
    }


    // --- Event Listeners ---
    startButton.addEventListener('click', () => {
        if (!isRunning) {
            initializeSimulation();
        }
    });

    toggleExplanationButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר הסבר';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'הסבר התופעה';
        }
    });

    // Initial state drawing
    initialDraw();
});
</script>
```