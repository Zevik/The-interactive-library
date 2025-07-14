---
title: "גלו את סוד העילוי: הדמיית כנף וזרימת אוויר"
english_slug: aerodynamic-profile-lift-simulation
category: "מדעים מדויקים / פיזיקה"
tags: [הדמיה, אינטראקטיבי, אווירודינמיקה, כנף, עילוי, זווית תקיפה, סימולציה]
---
# גלו את סוד העילוי: הדמיית כנף וזרימת אוויר

פעם תהיתם איך גוף מתכת ענק כמו מטוס יכול להישאר באוויר? זה קסם מדעי, והסוד טמון בצורת כנפיו ובאופן שבו הן מנהלות "שיחה" עם האוויר. הצטרפו אלינו למשחק אינטראקטיבי שבו תוכלו לשנות את זווית הכנף ולראות במו עיניכם כיצד נוצר הכוח המופלא שנקרא עילוי! שחקו, התנסו, וגלו את העקרונות הבסיסיים מאחורי הטיסה.

<div id="simulation-container">
    <canvas id="airfoilCanvas" width="700" height="450"></canvas>
    <div class="controls">
        <label for="angleSlider">זווית התקיפה: <span id="angleValue">0</span>°</label>
        <input type="range" id="angleSlider" min="-10" max="20" value="0" step="0.5">
        <div id="liftDisplay">כוח עילוי (משוער): 0</div>
    </div>
</div>

<button id="toggleExplanation">פשע את סוד העילוי (הסבר מדעי)</button>

<div id="explanation" class="hidden">
    <h2>איך עילוי גורם לנו לטוס?</h2>
    <p>עילוי הוא הכוח המרכזי שפועל כלפי מעלה על כנף מטוס (או כל פרופיל אווירודינמי) כשהיא נעה דרך האוויר. הוא נוצר משילוב של שני גורמים עיקריים:</p>

    <ul>
        <li><strong>הפרש לחצים (עקרון ברנולי):</strong> שימו לב בצורה האינטראקטיבית: בדרך כלל, הצד העליון של כנף מעוצב בצורה קמורה יותר מהצד התחתון. כשהאוויר זורם מעל הכנף, הוא נאלץ לעבור דרך ארוכה יותר באותו פרק זמן מאשר האוויר שזורם מתחת לכנף. כדי שהאוויר משני הצדדים יגיע בערך בו זמנית לקצה האחורי של הכנף (תופעה המכונה "שוויון זמני מעבר" או "השערת זמני המעבר השווים", למרות שמדובר בהפשטה - ההבדל במהירות הוא העיקר), האוויר מעל הכנף חייב לזרום *מהר יותר*. עקרון ברנולי קובע שככל שמהירות זרימת נוזל או גז (כמו אוויר) גבוהה יותר, הלחץ שלו נמוך יותר. לכן, זרימת האוויר המהירה יותר מעל הכנף יוצרת לחץ נמוך שם, בעוד שהזרימה האיטית יותר מתחת לכנף יוצרת לחץ גבוה יותר. הפרש הלחצים הזה – לחץ גבוה מלמטה "דוחף" כלפי מעלה לעבר הלחץ הנמוך מלמעלה – הוא שמייצר את כוח העילוי נטו כלפי מעלה.</li>
        <li><strong>סטיית האוויר (חוקי ניוטון):</strong> גורם חשוב נוסף הוא זווית הכנף. זווית התקיפה (Angle of Attack - AoA) היא הזווית בין הכנף עצמה לבין כיוון זרימת האוויר הנכנס (בסימולציה, זו הזווית שאתם משנים). גם אם הכנף שטוחה, זווית תקיפה חיובית (כשהקצה הקדמי מעט מורם) גורמת לכנף "לדחוף" את זרימת האוויר מטה. לפי החוק השלישי של ניוטון, לכל פעולה יש תגובה שווה והפוכה. אם הכנף דוחפת את האוויר מטה, האוויר דוחף את הכנף מעלה – וזהו גם כן כוח עילוי. ככל שזווית התקיפה גדולה יותר (עד גבול מסוים), כך סטיית האוויר מטה גדלה והעילוי עולה.</li>
    </ul>
    <p>שני הגורמים פועלים יחד ליצירת כוח העילוי. בסימולציה זו, תוכלו לראות כיצד שינוי זווית התקיפה משפיע על דפוס זרימת האוויר (המיוצגת על ידי חלקיקי האוויר הנעים) ועל עוצמת כוח העילוי המשוער (המיוצג על ידי אורך וצבע החץ). שימו לב לתופעת ה<a href="#stall-explanation">הזדקרות</a> בזוויות תקיפה גבוהות מדי!</p>

    <h3 id="stall-explanation">מה קורה בהזדקרות (Stall)?</h3>
    <p>אם זווית התקיפה גדלה יתר על המידה (בדרך כלל מעל 15-20 מעלות, תלוי בצורת הכנף), זרימת האוויר המהירה והחלקה מעל הכנף "נשברת" ונפרדת משטח הכנף. במצב זה, הפרש הלחצים המייצר את רוב העילוי נעלם או אפילו מתהפך חלקית, וכוח העילוי יורד בצורה דרסטית מאוד. זוהי תופעת ההזדקרות, מצב מסוכן באווירודינמיקה שמטוסים מנסים להימנע ממנו. בסימולציה, נסו להגיע לזווית כזו וראו כיצד זרימת האוויר הופכת כאוטית והעילוי צונח!</p>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    body {
        font-family: 'Roboto', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;
        background: linear-gradient(to bottom, #eef4f8, #d0e4f4); /* Soft blue gradient */
        color: #333d47; /* Dark charcoal */
        line-height: 1.7;
        min-height: 100vh;
    }

    h1, h2, h3 {
        color: #004a7f; /* Deep blue */
        margin-bottom: 15px;
        text-align: center;
    }

    h1 {
         font-size: 2.2em;
         margin-bottom: 20px;
         text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
     h2 {
         font-size: 1.8em;
         border-bottom: 2px solid #007bff;
         padding-bottom: 8px;
         margin-bottom: 15px;
     }
      h3 {
         font-size: 1.4em;
         margin-top: 20px;
         margin-bottom: 10px;
          color: #0056b3;
      }


    #simulation-container {
        background-color: #ffffff;
        border-radius: 16px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        padding: 30px;
        margin-bottom: 30px;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        max-width: 800px;
        border: 1px solid #e0e0e0;
    }

    #airfoilCanvas {
        border: 1px solid #cccccc;
        background: linear-gradient(to right, #f8fcff, #eaf2f8); /* Very light blue gradient for sky */
        border-radius: 10px;
        margin-bottom: 25px;
        width: 100%; /* Make canvas responsive */
        height: auto; /* Maintain aspect ratio */
        max-height: 450px; /* Limit height */
        aspect-ratio: 700 / 450; /* Preferred aspect ratio */
        box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.05);
    }

    .controls {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .controls label {
        margin-bottom: 12px;
        font-size: 1.15em;
        color: #004a7f; /* Deep blue */
        font-weight: 700;
    }

    .controls input[type="range"] {
        width: 90%;
        -webkit-appearance: none;
        height: 10px;
        background: linear-gradient(to right, #007bff, #00c0ff); /* Blue gradient track */
        border-radius: 5px;
        outline: none;
        opacity: 0.9;
        transition: opacity .2s, box-shadow 0.3s ease;
        margin-bottom: 20px;
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .controls input[type="range"]:hover {
        opacity: 1;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }

    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 22px;
        height: 22px;
        background: #0056b3; /* Darker blue */
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.3);
         transition: background-color 0.3s ease, transform 0.1s ease;
    }
     .controls input[type="range"]::-webkit-slider-thumb:hover {
         background-color: #003f8c;
     }
      .controls input[type="range"]::-webkit-slider-thumb:active {
         transform: scale(0.95);
      }

    .controls input[type="range"]::-moz-range-thumb {
        width: 22px;
        height: 22px;
        background: #0056b3;
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.3);
         transition: background-color 0.3s ease, transform 0.1s ease;
    }
     .controls input[type="range"]::-moz-range-thumb:hover {
         background-color: #003f8c;
     }
      .controls input[type="range"]::-moz-range-thumb:active {
         transform: scale(0.95);
      }


    #liftDisplay {
        margin-top: 10px;
        font-size: 1.2em;
        font-weight: bold;
        color: #28a745; /* Green */
        min-height: 1.6em; /* Reserve space */
        text-align: center;
        transition: color 0.3s ease; /* Smooth color change */
    }

     #liftDisplay.low-lift {
         color: #dc3545; /* Red for low/negative lift */
     }
     #liftDisplay.stalled-lift {
          color: #ff9800; /* Orange for stalled lift */
     }


    #toggleExplanation {
        background: linear-gradient(to right, #17a2b8, #138496); /* Teal gradient */
        color: white;
        padding: 14px 30px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
        font-weight: 700;
    }

    #toggleExplanation:hover {
        background: linear-gradient(to right, #138496, #0f6674); /* Darker teal gradient */
         box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
    #toggleExplanation:active {
        transform: scale(0.98);
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    #explanation {
        background-color: #e9ecef; /* Light gray */
        border-radius: 12px;
        padding: 0 25px; /* Initial padding for smooth transition */
        margin: 0 0 20px 0; /* Initial margin */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 800px;
        width: 100%;
        opacity: 0;
        max-height: 0; /* Start hidden with max-height */
        overflow: hidden;
        transition: opacity 0.5s ease-in-out, max-height 0.6s ease-in-out, padding 0.6s ease-in-out, margin 0.6s ease-in-out;
        box-sizing: border-box; /* Include padding in element's total width and height */
    }

    #explanation.visible {
        opacity: 1;
        max-height: 2000px; /* Large value to accommodate content */
        padding: 25px;
        margin-bottom: 20px;
         transition: opacity 0.5s ease-in-out, max-height 0.6s ease-in-out, padding 0.6s ease-in-out, margin 0.6s ease-in-out;
    }

    #explanation h2 {
        color: #0056b3;
        margin-top: 0;
        border-bottom: 2px solid #007bff;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }

    #explanation ul {
        margin-bottom: 15px;
        padding-left: 25px;
    }

    #explanation li {
        margin-bottom: 10px;
    }

     #explanation a {
         color: #0056b3;
         text-decoration: none;
         font-weight: bold;
     }
     #explanation a:hover {
         text-decoration: underline;
     }


    /* Responsive adjustments */
    @media (max-width: 768px) {
        body {
            padding: 15px;
        }
        h1 {
            font-size: 1.8em;
        }
        #simulation-container, #explanation {
            padding: 20px;
        }
        .controls input[type="range"] {
            width: 95%;
        }
        #toggleExplanation {
            padding: 12px 25px;
            font-size: 1em;
        }
         #explanation.visible {
              padding: 20px;
         }
    }

     @media (max-width: 480px) {
         h1 { font-size: 1.5em; }
         h2 { font-size: 1.4em; }
         h3 { font-size: 1.2em; }
         #simulation-container, #explanation.visible { padding: 15px; }
         .controls label { font-size: 1em; }
         #toggleExplanation { font-size: 0.9em; padding: 10px 20px; }
         #liftDisplay { font-size: 1.1em; }
         #explanation ul { padding-left: 20px; }
     }
</style>

<script>
    const canvas = document.getElementById('airfoilCanvas');
    const ctx = canvas.getContext('2d');
    const angleSlider = document.getElementById('angleSlider');
    const angleValueSpan = document.getElementById('angleValue');
    const liftDisplay = document.getElementById('liftDisplay');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggleExplanation');

    let angleOfAttack = parseFloat(angleSlider.value);
    const animationSpeed = 0.008; // Base speed of air particles (adjusted for smoothness)
    const numberOfParticles = 100; // Number of air particles per streamline
    const particleSize = 2;
    const particleColorNormal = '#3498db'; // Blue for normal flow
    const particleColorFast = '#87cefa'; // Lighter blue for faster flow
    const particleColorStall = '#e74c3c'; // Reddish for stalled/turbulent flow
    const particleTrailLength = 15; // Number of previous positions to draw

    // Airfoil dimensions and position relative to canvas center
    const airfoilWidth = 450; // Chord length approx
    const airfoilThickness = 50; // Max thickness approx
    const airfoilCenterX = canvas.width / 2;
    const airfoilCenterY = canvas.height / 2;

    // Airflow streamlines - simplified paths relative to airfoil, affected by AoA
    // Define starting Y positions relative to airfoil base Y
    const numStreamlines = 12;
    const streamSpacing = 30;
    const startX = -airfoilCenterX - 100; // Start far left
    const endX = canvas.width + 100; // End far right

    const initialStreamlineStartYs = [];
    for (let i = 0; i < numStreamlines; i++) {
        initialStreamlineStartYs.push(airfoilCenterY + (i - (numStreamlines - 1) / 2) * streamSpacing);
    }

    let airParticles = [];

    function initParticles() {
        airParticles = [];
        initialStreamlineStartYs.forEach(startY => {
             let streamlineParticles = [];
             for(let i = 0; i < numberOfParticles; i++) {
                 streamlineParticles.push({
                     t: i / numberOfParticles, // Position along curve (0 to 1)
                     color: particleColorNormal,
                     history: [] // To store previous positions for trails
                 });
             }
             airParticles.push(streamlineParticles);
        });
    }

    // Function to generate bezier curve points that simulate flow around an airfoil
    // This is a conceptual model, not physically accurate fluid dynamics
    function calculateStreamlineBezierPoints(startY, angleDeg) {
        const angleRad = angleDeg * Math.PI / 180;

        // Points relative to the airfoil's intended (unrotated) center at (0,0)
        const p0_rel = { x: startX - airfoilCenterX, y: startY - airfoilCenterY };
        const p3_rel = { x: endX - airfoilCenterX, y: startY - airfoilCenterY }; // End point

        // Control points need to curve around the airfoil.
        // The vertical position of the streamline relative to the airfoil's y=0 affects curvature.
        const relativeY = startY - airfoilCenterY; // Y distance from airfoil center line (canvas Y=airfoilCenterY)

        // Influence of AoA and vertical position on curvature
        // Higher AoA -> more upward bend above, more downward bend below
        // Closer to airfoil -> more affected
        // Sine function creates smoother influence curve based on vertical distance
        const influenceFactor = -Math.sin(relativeY / (numStreamlines/2 * streamSpacing) * Math.PI/2); // -1 to 1 based on position
        const aoaEffectY = influenceFactor * angleRad * 80; // Scale factor for AoA effect on Y

        // Base curvature to make lines go around the airfoil even at 0 AoA
        const baseCurvatureY = influenceFactor * 30;

        // Control points (relative to airfoil center)
        // p1: near leading edge area
        // p2: near trailing edge area

        const cp1_x_base = -airfoilWidth / 2 + airfoilWidth * 0.3; // Near leading edge
        const cp2_x_base = airfoilWidth / 2 - airfoilWidth * 0.3; // Near trailing edge

        const cp1_y = relativeY + baseCurvatureY - aoaEffectY;
        const cp2_y = relativeY + baseCurvatureY * 0.8 - aoaEffectY * 0.9; // Slightly less effect at trailing edge

        const p1_rel = { x: cp1_x_base + Math.abs(aoaEffectY) * 0.2, y: cp1_y }; // Slight forward shift for curvature
        const p2_rel = { x: cp2_x_base - Math.abs(aoaEffectY) * 0.2, y: cp2_y }; // Slight backward shift

         // Apply stall effect at high AoA to upper streamlines
         const stallAngleThreshold = 14; // Start showing stall effects
         const fullStallAngle = 18; // Full stall chaos
         let stallFactor = 0;
         if (angleDeg > stallAngleThreshold) {
             stallFactor = Math.min(1, (angleDeg - stallAngleThreshold) / (fullStallAngle - stallAngleThreshold));
         }

         // Only apply stall to streamlines *above* the airfoil
         if (relativeY < -5 && stallFactor > 0) {
             const turbulenceStart = airfoilWidth * 0.1; // Point relative to airfoil center where turbulence starts
             // Find points on the bezier curve after the turbulence start
             // This requires finding 't' values corresponding to x positions, which is hard.
             // A simpler approach: apply random jiggle to CP2 and P3 if they are downstream enough
             if (p2_rel.x > turbulenceStart) {
                  p2_rel.y += (Math.random() - 0.5) * stallFactor * 60; // Random vertical jiggle
             }
              if (p3_rel.x > turbulenceStart) {
                 p3_rel.y += (Math.random() - 0.5) * stallFactor * 40;
             }
         }


        // Rotate points by -AoA (because the *airfoil* is rotated +AoA, the *airflow relative to the airfoil* is -AoA)
        // No, this is wrong. The airfoil is rotated, but the airflow is coming horizontally.
        // The paths calculated *relative to the unrotated airfoil frame* are then rotated by +AoA to get their canvas coordinates.
        // Let's recalculate points in the canvas frame directly by rotating the control points.
        // Initial straight path: P0(startX, startY), P1(midX, startY), P2(midX, startY), P3(endX, startY)
        // We need to transform P1 and P2 based on AoA and relative position.

         const p0 = { x: startX, y: startY };
         const p3 = { x: endX, y: startY };

         const wingChordStart = airfoilCenterX - airfoilWidth / 2;
         const wingChordEnd = airfoilCenterX + airfoilWidth / 2;

         // Control points are influenced by the wing's presence and angle
         // Let's place CP1 and CP2 roughly aligned vertically with the wing's extent
         const cp1_x = wingChordStart + airfoilWidth * 0.2;
         const cp2_x = wingChordEnd - airfoilWidth * 0.2;

         // The Y position of control points is where the "magic" happens.
         // It's a function of initial startY, angleOfAttack, and horizontal position (x).
         // Simplified model:
         // Streamlines above the wing (startY < airfoilCenterY): pulled up then down.
         // Streamlines below the wing (startY > airfoilCenterY): pulled down then up.
         // The amount of pull depends on AoA and how close the streamline is to the wing.

         const streamlineHeightRelativeToWing = startY - airfoilCenterY;
         const verticalInfluence = -Math.sin((streamlineHeightRelativeToWing / (numStreamlines/2 * streamSpacing)) * Math.PI/2); // -1 (top) to 1 (bottom)

         // Adjust Y based on vertical position and angle
         const aoaVerticalDisplacement = angleRad * 80; // How much vertical shift AoA causes

         const cp1_y_canvas = startY + verticalInfluence * 30 - aoaVerticalDisplacement; // Base curve + AoA push
         const cp2_y_canvas = startY + verticalInfluence * 20 - aoaVerticalDisplacement * 0.8; // Slightly less effect towards rear

          // Apply stall turbulence to upper streamlines past mid-chord
          if (streamlineHeightRelativeToWing < -5 && stallFactor > 0) {
               const turbulenceOnsetCanvasX = airfoilCenterX + airfoilWidth * 0.1; // Canvas X where turbulence starts
               // If CP2 is after this point, jiggle it
               if (cp2_x > turbulenceOnsetCanvasX) {
                     cp2_y_canvas += (Math.random() - 0.5) * stallFactor * 70; // Stronger jiggle
                     p3.y += (Math.random() - 0.5) * stallFactor * 50; // Affect endpoint too
               }
          }


        return [
            p0,
            { x: cp1_x, y: cp1_y_canvas },
            { x: cp2_x, y: cp2_y_canvas },
            p3
        ];
    }


     function getBezierPoint(t, p0, p1, p2, p3) {
        const mt = 1 - t;
        const mt2 = mt * mt;
        const mt3 = mt2 * mt;
        const t2 = t * t;
        const t3 = t2 * t;

        const x = mt3 * p0.x + 3 * mt2 * t * p1.x + 3 * mt * t2 * p2.x + t3 * p3.x;
        const y = mt3 * p0.y + 3 * mt2 * t * p1.y + 3 * mt * t2 * p2.y + t3 * p3.y;

        return { x, y };
    }

     function getBezierTangent(t, p0, p1, p2, p3) {
        const mt = 1 - t;
        const mt2 = mt * mt;
        const t2 = t * t;

        const dx = 3 * mt2 * (p1.x - p0.x) + 6 * mt * t * (p2.x - p1.x) + 3 * t2 * (p3.x - p2.x);
        const dy = 3 * mt2 * (p1.y - p0.y) + 6 * mt * t * (p2.y - p1.y) + 3 * t2 * (p3.y - p2.y);

         // Calculate speed magnitude
         const speed = Math.sqrt(dx * dx + dy * dy);

         // Return both tangent (direction) and speed
        return { dx, dy, speed };
     }


    function drawStreamlines(ctx, angleDeg) {
        ctx.lineWidth = 1;
        ctx.globalAlpha = 0.9; // Slight transparency

        initialStreamlineStartYs.forEach((startY, pathIndex) => {
            const pathPoints = calculateStreamlineBezierPoints(startY, angleDeg);
             if (pathPoints.length < 4) return; // Need 4 points for cubic bezier

            // Draw path outline (optional, maybe just particles is enough)
            // ctx.strokeStyle = '#b0e0ff'; // Lighter blue for path
            // ctx.beginPath();
            // ctx.moveTo(pathPoints[0].x, pathPoints[0].y);
            // ctx.bezierCurveTo(
            //     pathPoints[1].x, pathPoints[1].y,
            //     pathPoints[2].x, pathPoints[2].y,
            //     pathPoints[3].x, pathPoints[3].y
            // );
            // ctx.stroke();


            // Draw animated particles
            if (airParticles[pathIndex]) {
                airParticles[pathIndex].forEach(particle => {
                    // Get current position and tangent (for speed)
                    const pos = getBezierPoint(particle.t, ...pathPoints);
                    const tangent = getBezierTangent(particle.t, ...pathPoints);

                    // Store position for trail
                    particle.history.push({ x: pos.x, y: pos.y });
                    if (particle.history.length > particleTrailLength) {
                        particle.history.shift();
                    }

                    // Determine particle color based on speed and position relative to wing
                     const relativeY = startY - airfoilCenterY;
                     const stallAngleThreshold = 14;
                     const isAboveWing = relativeY < -5;

                    if (isAboveWing && angleDeg > stallAngleThreshold) {
                         // Stalled flow above stall angle
                         particle.color = particleColorStall;
                    } else {
                         // Normal or fast flow
                        // Simple speed coloring: faster -> lighter blue
                        // Speed is relative to curve length and t change. Tangent speed is a proxy.
                         const speedFactor = tangent.speed / 5; // Normalize speed for coloring effect
                         if (speedFactor > 5) { // Threshold for "fast" coloring (adjust as needed)
                             particle.color = particleColorFast;
                         } else {
                             particle.color = particleColorNormal;
                         }
                    }


                    // Draw trail
                    ctx.strokeStyle = particle.color;
                    ctx.lineWidth = particleSize / 2;
                    ctx.beginPath();
                    ctx.moveTo(particle.history[0].x, particle.history[0].y);
                    for (let i = 1; i < particle.history.length; i++) {
                        // Draw segments and fade opacity along the trail
                        ctx.lineTo(particle.history[i].x, particle.history[i].y);
                    }
                    ctx.stroke();


                    // Draw particle (optional, trails might be enough)
                    ctx.fillStyle = particle.color;
                    ctx.beginPath();
                    ctx.arc(pos.x, pos.y, particleSize, 0, Math.PI * 2);
                    ctx.fill();


                    // Move particle along the curve
                    // Speed variation: particles over the top move faster at positive AoA
                     let speedMultiplier = 1;
                     if (isAboveWing && angleDeg > 0) {
                         // Increase speed based on angle and vertical position (closer to wing = more speed up)
                         speedMultiplier += Math.abs(relativeY / (numStreamlines/2 * streamSpacing)) * (angleDeg / 20); // Simple model
                     } else if (!isAboveWing && angleDeg > 0) {
                         // Slightly slower below at positive AoA
                          speedMultiplier -= Math.abs(relativeY / (numStreamlines/2 * streamSpacing)) * (angleDeg / 30);
                          speedMultiplier = Math.max(0.5, speedMultiplier); // Don't go too slow
                     } else if (angleDeg < 0) {
                         // Reverse effects for negative AoA
                          if (isAboveWing) { speedMultiplier -= Math.abs(relativeY / (numStreamlines/2 * streamSpacing)) * (-angleDeg / 30); speedMultiplier = Math.max(0.5, speedMultiplier); }
                          else { speedMultiplier += Math.abs(relativeY / (numStreamlines/2 * streamSpacing)) * (-angleDeg / 20); }
                     }


                    // Apply stall effect on speed/movement
                     const stallAngleThreshold = 14;
                     const fullStallAngle = 18;
                     if (isAboveWing && angleDeg > stallAngleThreshold) {
                         const stallFactor = Math.min(1, (angleDeg - stallAngleThreshold) / (fullStallAngle - stallAngleThreshold));
                         // Reduce forward speed and add randomness
                         speedMultiplier *= (1 - stallFactor * 0.8); // Slow down significantly
                         particle.t += (Math.random() - 0.5) * 0.01 * stallFactor; // Add jiggle to position parameter
                         // Ensure t stays within a reasonable range (might jump a bit due to jiggle)
                         particle.t = Math.max(-0.2, Math.min(1.2, particle.t));
                     } else {
                         // Normal speed update
                         particle.t += animationSpeed * speedMultiplier;
                     }


                    // Reset particle if it goes beyond the end
                    if (particle.t > 1.1 || particle.t < -0.1) { // Reset slightly beyond bounds
                         particle.t = (startX - pathPoints[0].x) / (pathPoints[3].x - pathPoints[0].x) - (Math.random() * 0.1); // Reset near start, slight random offset
                         particle.history = []; // Clear trail on reset
                    }
                });
            }
        });

        ctx.globalAlpha = 1; // Reset alpha
    }

    function drawAirfoil(ctx, angleDeg) {
        ctx.save();
        const centerX = airfoilCenterX;
        const centerY = airfoilCenterY;
        const angleRad = angleDeg * Math.PI / 180;

        ctx.translate(centerX, centerY);
        ctx.rotate(angleRad);

        ctx.fillStyle = '#4a5568'; // Dark gray for airfoil
        ctx.strokeStyle = '#2d3748'; // Even darker outline
        ctx.lineWidth = 2;

        // Draw a simplified airfoil shape using bezier curves
        const LE = { x: airfoilWidth / 2, y: 0 }; // Leading Edge (relative to rotated center)
        const TE = { x: -airfoilWidth / 2, y: 0 }; // Trailing Edge

        // Upper surface control points
        const upperCP1 = { x: LE.x - airfoilWidth * 0.2, y: airfoilThickness * 0.8 };
        const upperCP2 = { x: TE.x + airfoilWidth * 0.3, y: airfoilThickness * 0.5 };

        // Lower surface control points
        const lowerCP1 = { x: LE.x - airfoilWidth * 0.1, y: -airfoilThickness * 0.2 };
        const lowerCP2 = { x: TE.x + airfoilWidth * 0.2, y: -airfoilThickness * 0.1 };


        ctx.beginPath();
        ctx.moveTo(LE.x, LE.y);
        ctx.bezierCurveTo(upperCP1.x, upperCP1.y, upperCP2.x, upperCP2.y, TE.x, TE.y);
        ctx.bezierCurveTo(lowerCP2.x, lowerCP2.y, lowerCP1.x, lowerCP1.y, LE.x, LE.y);

        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        ctx.restore();
    }


    function drawLiftVector(ctx, liftMagnitude, angleDeg) {
        const centerX = airfoilCenterX;
        const centerY = airfoilCenterY;

        ctx.save();
        ctx.translate(centerX, centerY); // Position at airfoil center

        // Lift acts vertically upwards relative to the direction of motion (horizontal flow)
        // The vector originates from the airfoil center and points up (negative Y in canvas)
        const liftScale = 0.6; // Scale lift magnitude to pixel length
        const maxLiftPixelLength = 180; // Maximum pixel length for the arrow
        const baseLiftOffset = 20; // Start arrow slightly above wing surface

        const arrowLength = Math.min(maxLiftPixelLength, Math.max(0, liftMagnitude * liftScale)); // Don't show negative lift

        if (arrowLength > 0) {
             // Pulsing effect for lift vector
             const pulse = Math.sin(Date.now() / 300) * 0.05 + 1; // Subtle size variation
             const currentArrowLength = arrowLength * pulse;

             ctx.strokeStyle = '#28a745'; // Green color for lift
             ctx.fillStyle = '#28a745';
             ctx.lineWidth = 4;
             ctx.lineCap = 'round';

             // Draw vertical line (lift) from origin upwards
             ctx.beginPath();
             ctx.moveTo(0, -baseLiftOffset); // Start slightly above center
             ctx.lineTo(0, -(baseLiftOffset + currentArrowLength));
             ctx.stroke();

             // Draw arrow head (triangle)
             const headSize = 10;
             ctx.beginPath();
             ctx.moveTo(0, -(baseLiftOffset + currentArrowLength));
             ctx.lineTo(-headSize * 0.7, -(baseLiftOffset + currentArrowLength - headSize));
             ctx.lineTo(headSize * 0.7, -(baseLiftOffset + currentArrowLength - headSize));
             ctx.closePath();
             ctx.fill();
        } else {
             // Optionally draw a small downward vector for negative lift
              const negLiftThreshold = -5; // Threshold for showing negative lift vector
              if (liftMagnitude < negLiftThreshold) {
                  const negArrowLength = Math.min(50, -liftMagnitude * liftScale * 0.5); // Smaller scale for negative lift

                   ctx.strokeStyle = '#dc3545'; // Red color for down force
                   ctx.fillStyle = '#dc3545';
                   ctx.lineWidth = 3;

                   ctx.beginPath();
                   ctx.moveTo(0, baseLiftOffset); // Start slightly below center
                   ctx.lineTo(0, baseLiftOffset + negArrowLength);
                   ctx.stroke();

                    // Draw arrow head (triangle)
                    const headSize = 8;
                    ctx.beginPath();
                    ctx.moveTo(0, baseLiftOffset + negArrowLength);
                    ctx.lineTo(-headSize * 0.7, baseLiftOffset + negArrowLength + headSize);
                    ctx.lineTo(headSize * 0.7, baseLiftOffset + negArrowLength + headSize);
                    ctx.closePath();
                    ctx.fill();
              }
        }

        ctx.restore();
    }

    // Simplified Lift Calculation (Conceptual)
    // Approximates a typical Cl vs AoA curve
    function calculateLift(angleDeg) {
        const stallAngle = 15; // Angle (degrees) where lift peaks
        const negativeStallAngle = -7; // Angle where negative lift "stalls"
        const maxAngle = 20; // Max angle in slider
        const minAngle = -10; // Min angle in slider

        let lift = 0;

        if (angleDeg > negativeStallAngle && angleDeg <= stallAngle) {
            // Linear increase in normal operating range
            const slope = 1.5; // Sensitivity
            lift = angleDeg * slope;
        } else if (angleDeg > stallAngle) {
            // Model stall: Rapid drop after peak
            const peakLift = stallAngle * 1.5;
            // Cubic drop for smoother transition into stall
            const angleDelta = angleDeg - stallAngle;
            const stallRange = maxAngle - stallAngle;
            const normalizedDelta = angleDelta / stallRange; // 0 to 1
            // Lift drops from peak to a small value (e.g., 5) at max angle
            const minStallLift = 5;
            lift = peakLift - (peakLift - minStallLift) * Math.pow(normalizedDelta, 2); // Squared drop
            lift = Math.max(0, lift); // Lift doesn't go below 0 in simple model post-stall
        } else if (angleDeg <= negativeStallAngle) {
             // Model negative stall / saturated negative lift
             const peakNegLift = negativeStallAngle * 1.5;
             const angleDelta = angleDeg - negativeStallAngle;
             const negStallRange = minAngle - negativeStallAngle;
             const normalizedDelta = angleDelta / negStallRange; // 0 to -1
             // Lift drops from peak negative to a larger negative value (e.g., -10) at min angle
             const maxNegLift = -10;
             lift = peakNegLift - (peakNegLift - maxNegLift) * Math.pow(normalizedDelta, 2); // Squared change
             lift = Math.min(peakNegLift, lift); // Ensure it doesn't exceed peak neg lift
        }

        return lift;
    }


    function updateLiftDisplay(lift) {
         liftDisplay.textContent = `כוח עילוי (משוער): ${lift.toFixed(1)}`;
         liftDisplay.classList.remove('low-lift', 'stalled-lift');
         const stallAngleThreshold = 14; // Use same threshold as particle effect
         if (lift < 10 && angleOfAttack > stallAngleThreshold - 2) { // Below 10 lift and near stall angle
             liftDisplay.classList.add('stalled-lift');
         } else if (lift < 5) { // General low/negative lift
              liftDisplay.classList.add('low-lift');
         }
    }


    function draw() {
        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Redraw elements
        drawAirfoil(ctx, angleOfAttack);
        drawStreamlines(ctx, angleOfAttack); // Streamlines need angle to calculate paths
        const currentLift = calculateLift(angleOfAttack);
        drawLiftVector(ctx, currentLift, angleOfAttack); // Lift vector might use angle for orientation if needed (not here)

        // Update lift display (only update text/color when value changes significantly?)
        updateLiftDisplay(currentLift);

        // Request next frame for animation
        requestAnimationFrame(draw);
    }

    // Event listener for slider
    angleSlider.addEventListener('input', (event) => {
        const newAngle = parseFloat(event.target.value);
        if (newAngle !== angleOfAttack) {
             angleOfAttack = newAngle;
             angleValueSpan.textContent = angleOfAttack;
             // Particles will update position based on new angle in the next draw frame
        }
    });

    // Event listener for explanation button
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.classList.contains('hidden');
        if (isHidden) {
            explanationDiv.classList.remove('hidden');
            // To enable smooth max-height transition, we need to set max-height
            // after removing hidden, but before adding visible. A small delay helps.
            // Or, better, set max-height to scrollHeight immediately.
            explanationDiv.style.maxHeight = explanationDiv.scrollHeight + 'px'; // Set to content height
            explanationDiv.classList.add('visible');
        } else {
             // Before hiding, set max-height explicitly to its current computed height
             // so the transition knows the starting point.
             explanationDiv.style.maxHeight = explanationDiv.scrollHeight + 'px'; // Or getComputedStyle(explanationDiv).height

             // Use a slight delay before removing max-height: auto and setting to 0
             requestAnimationFrame(() => {
                 explanationDiv.classList.remove('visible');
                 explanationDiv.style.maxHeight = '0'; // Start collapse transition
                 // Add hidden class after transition ends (optional, css handles overflow:hidden)
                 // setTimeout(() => explanationDiv.classList.add('hidden'), 600); // Match CSS transition time
             });
        }
    });

    // Handle window resize to make canvas somewhat responsive
    function resizeCanvas() {
        const container = document.getElementById('simulation-container');
        const containerWidth = container.clientWidth - 60; // Subtract padding
        // Maintain aspect ratio (700/450)
        const aspectRatio = 700 / 450;
        let canvasWidth = containerWidth;
        let canvasHeight = containerWidth / aspectRatio;

        // Cap height on larger screens
        if (canvasHeight > 450) {
            canvasHeight = 450;
            canvasWidth = canvasHeight * aspectRatio;
        }

        canvas.width = canvasWidth;
        canvas.height = canvasHeight;

        // Need to re-calculate positions based on new canvas size if elements were fixed positions
        // In this simple model, elements are relative to center, so it scales ok conceptually.
        // If we had fixed ground/sky lines, they'd need adjustment. AirfoilCenter is fixed at width/2, height/2.
         airfoilCenterX = canvas.width / 2;
         airfoilCenterY = canvas.height / 2;
         // Re-initialize particles and paths if needed, or ensure calculateStreamlineBezierPoints is robust to size changes.
         // Re-initializing is simpler for this example.
         initParticles(); // Recreate particles for new size
         // Recalculate initial streamline start Ys based on new canvas height
          initialStreamlineStartYs.length = 0; // Clear array
          for (let i = 0; i < numStreamlines; i++) {
             initialStreamlineStartYs.push(airfoilCenterY + (i - (numStreamlines - 1) / 2) * streamSpacing);
         }
    }

     // Add resize listener
    window.addEventListener('resize', resizeCanvas);

    // Initial setup
    resizeCanvas(); // Set initial canvas size
    initParticles(); // Initialize particles
    draw(); // Start the animation loop

     // Ensure initial state of explanation is hidden by setting max-height to 0
     explanationDiv.style.maxHeight = '0';
     explanationDiv.classList.add('hidden');
     explanationDiv.classList.remove('visible');


</script>
---