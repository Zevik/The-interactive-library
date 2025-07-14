---
title: "ריקוד קוסמי: למה עונות השנה משנות לנו את החיים?"
english_slug: earth-journey-why-are-there-seasons
category: "כללי"
tags:
  - עונות השנה
  - כדור הארץ
  - שמש
  - מסלול
  - הטיית ציר כדור הארץ
  - קיץ
  - חורף
  - אביב
  - סתיו
description: "גללו וצפו במסע השנתי של כדור הארץ סביב השמש, וגלו את הסיבה האמיתית, והמפתיעה, לעונות השנה - זו לא המרחק מהשמש!"
---
# ריקוד קוסמי: למה עונות השנה משנות לנו את החיים?

פעם חם ולח, פעם קפוא וגשום, פעם הכל מלבלב. עונות השנה צובעות את חיינו ומשפיעות על הכל – מהבגדים שאנחנו לובשים ועד מחזורי החקלאות והטבע. אבל מה באמת גורם לשינויים הדרמטיים האלה? האם כדור הארץ פשוט מתקרב לשמש בקיץ ומתרחק בחורף? התשובה הנפוצה הזו שגויה לחלוטין! בואו נצא למסע מרתק בחלל ונגלה את האמת המפתיעה מאחורי עונות השנה.

<div id="seasons-sim-container">
    <svg id="seasons-sim" viewBox="-400 -300 800 600" preserveAspectRatio="xMidYMid meet">
        <!-- Background Stars -->
        <rect x="-400" y="-300" width="800" height="600" fill="#0a0a0a"/>
         <circle cx="-250" cy="-100" r="1" fill="#eee"/>
         <circle cx="150" cy="200" r="1.5" fill="#ddd"/>
         <circle cx="300" cy="-250" r="0.8" fill="#ccc"/>
         <circle cx="-350" cy="150" r="1.2" fill="#eee"/>
         <circle cx="50" cy="-280" r="0.9" fill="#ddd"/>
         <!-- Add more stars dynamically or manually if desired -->


        <!-- Orbit -->
        <ellipse cx="0" cy="0" rx="300" ry="200" fill="none" stroke="#555" stroke-dasharray="3,3" stroke-width="1.5"/>

        <!-- Sun -->
        <circle id="sun" cx="0" cy="0" r="40" fill="#ffcc00"/>
        <text x="0" y="65" text-anchor="middle" fill="#fff" font-size="16" font-weight="bold">השמש</text>

        <!-- Earth - Group for rotation/positioning -->
        <g id="earth-group">
            <!-- Earth circle - maybe add a subtle radial gradient -->
             <circle id="earth" cx="0" cy="0" r="20" fill="url(#earth-gradient)" stroke="#333" stroke-width="0.8"/>
            <!-- Earth Axis (relative to its center) -->
            <!-- The axis is tilted relative to the *orbital plane*. We'll draw it tilted 23.5 degrees -->
            <!-- The tilt direction needs to be fixed relative to the background -->
            <line id="earth-axis" x1="0" y1="-25" x2="0" y2="25" stroke="#fff" stroke-width="2" stroke-dasharray="3,3"/>
            <!-- Equator (example visualization) -->
             <ellipse id="earth-equator" cx="0" cy="0" rx="20" ry="5" fill="none" stroke="#fff" stroke-width="1" opacity="0.7"/>

             <!-- Hemisphere markers (simplified) -->
             <circle id="north-pole" cx="0" cy="-20" r="3" fill="#ff4444"/>
             <text x="8" y="-20" fill="#fff" font-size="12" font-weight="bold">צפון</text>
             <circle id="south-pole" cx="0" cy="20" r="3" fill="#4444ff"/>
             <text x="8" y="20" fill="#fff" font-size="12" font-weight="bold">דרום</text>
        </g>

        <!-- Illumination Visualization - Simplified -->
         <defs>
             <!-- Radial gradient for Earth's general shading -->
              <radialGradient id="earth-gradient" cx="50%" cy="50%" r="50%" fx="65%" fy="45%">
                <stop offset="0%" stop-color="#4da6ff"/> <!-- Brighter blue -->
                <stop offset="60%" stop-color="#0055aa"/> <!-- Deeper blue -->
                <stop offset="100%" stop-color="#003366"/> <!-- Darker blue for shadow -->
              </radialGradient>

              <!-- Linear gradient for simulating day/night line direction -->
            <linearGradient id="day-night-sim-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
                <!-- Start bright, transition to dark -->
                <stop offset="0%" style="stop-color:rgba(255,255,180,0.7)" />
                <stop offset="50%" style="stop-color:rgba(0,0,0,0)" />
                 <stop offset="100%" style="stop-color:rgba(0,0,0,0)" />
            </linearGradient>

             <!-- Mask to show only the Earth circle -->
             <mask id="earth-circle-mask">
                <circle cx="0" cy="0" r="20" fill="white"/>
             </mask>
        </defs>

        <!-- Group for illumination overlay, positioned at Earth's center -->
         <g id="earth-illumination-overlay" mask="url(#earth-circle-mask)">
             <!-- This rectangle will be rotated to show the general direction of sunlight -->
             <!-- It covers the Earth circle (40x40 centered at 0,0 relative to group origin) -->
             <rect x="-20" y="-20" width="40" height="40" fill="url(#day-night-sim-gradient)"/>
         </g>


         <!-- Dynamic Label for Current Season/Position -->
         <text id="season-label" x="0" y="-250" text-anchor="middle" fill="#61dafb" font-size="18" font-weight="bold">טוען...</text>


    </svg>
    <div id="controls">
         <div id="position-label" style="color:white; margin-top: 10px; font-size: 14px;">עמדת כדור הארץ: 0%</div>
        <div id="season-indicator" style="color:#61dafb; margin-top: 5px; font-size: 16px; min-height: 1.2em;"></div>
        <button id="play-pause-btn">הפעל/השהה</button>
         <div id="jump-buttons" style="margin-top: 15px;">
             <button data-pos="0">חורף (צפ')</button>
             <button data-pos="0.25">אביב (צפ')</button>
             <button data-pos="0.5">קיץ (צפ')</button>
             <button data-pos="0.75">סתיו (צפ')</button>
         </div>
    </div>
</div>

<button id="toggle-explanation" style="margin-top: 20px;">מה בעצם קורה כאן? (הסבר מלא)</button>

<div id="explanation" style="display: none; margin-top: 20px; background-color: #f0f0f0; padding: 20px; border-radius: 10px; color: #333;">
    <h2>הסוד נחשף: מדוע יש עונות שנה?</h2>
    <p>הסימולציה שראיתם ממחישה את הגורם האמיתי לעונות השנה. בניגוד לאמונה הרווחת, זה לא המרחק המשתנה בין כדור הארץ לשמש שיוצר את הקיץ והחורף.</p>
    <ul>
        <li><strong style="color:#61dafb;">המסלול האליפטי:</strong> כדור הארץ אכן חג סביב השמש במסלול מעט אליפטי, אבל השינוי במרחק זניח והשפעתו על הטמפרטורה קטנה מאוד. למעשה, בחצי הכדור הצפוני חם הכי בקיץ, דווקא כשהכדור הארץ הכי <span style="font-weight: bold; color: #e74c3c;">רחוק</span> מהשמש במסלולו! ובחורף קר הכי, כשהכדור הארץ הכי <span style="font-weight: bold; color: #2ecc71;">קרוב</span>. מוזר, נכון?</li>
        <li><strong style="color:#61dafb;">הטיית הציר - הכוכב האמיתי!:</strong> ציר הסיבוב של כדור הארץ (הקו הדמיוני שעובר בין הקטבים) אינו ישר ביחס למסלול סביב השמש. הוא מוטה בזווית קבועה של כ-23.5 מעלות, וכיוון ההטיה הזו נשאר קבוע בחלל (כלפי כוכב הצפון, פולריס). זוהי הסיבה <span style="font-weight: bold;">העיקרית</span> לעונות השנה.</li>
        <li><strong style="color:#61dafb;">כשהציר מוטה "לכיוון":</strong> כאשר חצי כדור מסוים (למשל, הצפוני) מוטה <span style="font-weight: bold; color: #e74c3c;">לכיוון</span> השמש, הוא חווה את עונת הקיץ:
            <ul>
                <li><span style="font-weight: bold;">קרני השמש פוגעות בזווית ישרה יותר:</span> כמו פנס שמכוון ישירות למקום אחד - האור והחום מרוכזים יותר ליחידת שטח.</li>
                <li><span style="font-weight: bold;">השמש נמצאת יותר זמן בשמיים:</span> אורך היום ארוך משמעותית מאורך הלילה, מה שמאפשר יותר זמן חימום מהשמש.</li>
                <li><span style="font-weight: bold;">תוצאה:</span> הרבה יותר חום ואור - <span style="font-weight: bold; color: #e74c3c;">קיץ!</span> (בו זמנית, חצי הכדור השני, שמוטה הרחק מהשמש, חווה חורף).</li>
            </ul>
        </li>
        <li><strong style="color:#61dafb;">כשהציר מוטה "הרחק":</strong> כאשר חצי כדור מסוים מוטה <span style="font-weight: bold; color: #2ecc71;">הרחק</span> מהשמש, הוא חווה את עונת החורף:
            <ul>
                <li><span style="font-weight: bold;">קרני השמש פוגעות בזווית חדה יותר:</span> כמו פנס שמאיר מהצד - האור והחום מתפזרים על שטח גדול יותר, והעוצמה ליחידת שטח נמוכה יותר.</li>
                <li><span style="font-weight: bold;">השמש נמצאת פחות זמן בשמיים:</span> אורך היום קצר משמעותית מאורך הלילה, ויש פחות זמן חימום.</li>
                <li><span style="font-weight: bold;">תוצאה:</span> פחות חום ואור - <span style="font-weight: bold; color: #2ecc71;">חורף!</span></li>
            </ul>
        </li>
        <li><strong style="color:#61dafb;">עונות המעבר:</strong> האביב והסתיו קורים כאשר ציר כדור הארץ אינו מוטה משמעותית לכיוון השמש או הרחק ממנה. בנקודות אלו במסלול, אורך היום והלילה כמעט שווים בכל העולם, וזווית פגיעת השמש מתונה יותר.</li>
    </ul>
     <p style="margin-top: 15px; font-size: 14px; color: #555;"><strong>לסיכום:</strong> זכרו, עונות השנה נובעות כמעט כולן מהטיית ציר כדור הארץ ביחס למישור ההקפה סביב השמש, ולא מהשינוי הקטן במרחק.</p>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.7;
        direction: rtl; /* Right-to-left for Hebrew */
        text-align: right;
        background: linear-gradient(180deg, #282c34 0%, #1a1d24 100%); /* Subtle gradient background */
        color: #e0e0e0; /* Light grey text */
        padding: 20px;
        overflow-x: hidden; /* Prevent horizontal scroll */
    }

    h1 {
        color: #61dafb; /* Light blue */
        text-align: center;
        margin-bottom: 20px;
        font-weight: 700;
        font-size: 2em;
    }

     p {
        margin-bottom: 15px;
        font-size: 1.1em;
     }

    #seasons-sim-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 30px;
        background-color: #1a1d24; /* Very dark background */
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3); /* Soft shadow */
        border: 1px solid #3a3f47;
    }

    #seasons-sim {
        width: 100%;
        max-width: 700px; /* Limit max width */
        height: auto;
        background-color: #0a0a0a; /* Deep space black */
        border-radius: 8px;
        overflow: visible; /* Allow labels/elements slightly outside */
         box-shadow: inset 0 0 10px rgba(0,0,0,0.5); /* Inner shadow for depth */
    }

    #sun {
        fill: #ffcc00;
        filter: drop-shadow(0 0 20px rgba(255, 204, 0, 0.9)); /* Stronger glow effect */
        animation: pulse 2s infinite alternate; /* Subtle pulse animation */
    }

    @keyframes pulse {
        from { r: 40; }
        to { r: 42; }
    }

    #earth-group {
        cursor: grab;
        transition: transform 0.1s ease-out; /* Smooth dragging feedback */
         transform-origin: center; /* Rotate Earth group around its center */
         transform-box: fill-box;
    }

    #earth {
         stroke: #333;
          /* Fill is now handled by #earth-gradient def */
    }

     #earth-axis, #earth-equator, #north-pole, #south-pole {
         pointer-events: none; /* Don't interfere with dragging */
         /* Added specific colors for poles */
     }

      #north-pole { fill: #e74c3c; /* Red for North */ }
      #south-pole { fill: #3498db; /* Blue for South */ }


     #earth-illumination-overlay rect {
        /* Initial styles, JS will update transform */
         transform-origin: 20px 20px; /* Center of the rect (relative to its own coordinates) */
         opacity: 0.9; /* Make illumination slightly translucent */
     }

    #controls {
        margin-top: 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        max-width: 600px;
    }

    #position-label {
        margin-bottom: 10px;
         font-size: 1em;
          color: #ccc;
    }

    #season-indicator {
         margin-bottom: 15px;
         font-size: 1.2em;
         font-weight: bold;
         min-height: 1.5em; /* Reserve space to prevent layout shift */
         color: #61dafb; /* Matching headline color */
         text-align: center;
    }

    button {
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        background-color: #61dafb;
        color: #1a1d24; /* Dark text on button */
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-family: 'Heebo', sans-serif;
         margin: 0 5px; /* Spacing between jump buttons */
         min-width: 80px; /* Minimum button width */
    }

    button:hover {
        background-color: #21a1f1;
        transform: translateY(-2px); /* Subtle hover effect */
    }

     button:active {
         transform: translateY(0);
     }

    #jump-buttons {
        display: flex;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        justify-content: center;
        gap: 10px; /* Space between wrapped buttons */
    }

    #toggle-explanation {
         background-color: #3a3f47; /* Darker button */
         color: #fff; /* White text */
         margin-top: 25px;
         padding: 12px 25px;
         border-radius: 25px; /* Pill shape */
    }

     #toggle-explanation:hover {
         background-color: #5a626e;
     }


    #explanation {
        background-color: #fff; /* White background for readability */
        color: #333; /* Dark text */
        padding: 25px;
        border-radius: 10px;
        margin-top: 25px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        border: 1px solid #ddd;
    }

    #explanation h2 {
        color: #1a1d24; /* Very dark heading */
        margin-top: 0;
        margin-bottom: 20px;
        font-weight: 700;
         text-align: center;
    }

    #explanation ul {
        list-style: disc;
        margin-right: 20px;
        padding-right: 0; /* Reset default padding */
    }

    #explanation ul li {
        margin-bottom: 10px;
        line-height: 1.8;
    }

    #explanation ul ul {
        list-style: circle;
        margin-right: 20px;
        margin-top: 8px;
        margin-bottom: 8px;
        padding-right: 0;
    }

     #explanation strong {
        color: #61dafb; /* Highlight key terms */
     }

     /* Responsive adjustments */
     @media (max-width: 600px) {
         h1 { font-size: 1.6em; }
         p { font-size: 1em; }
         button { font-size: 0.9em; padding: 8px 15px; }
         #jump-buttons { flex-direction: column; align-items: stretch; }
         #jump-buttons button { margin: 5px 0; }
         #explanation { padding: 15px; }
         #explanation h2 { font-size: 1.4em; }
     }

</style>

<script>
    const svg = document.getElementById('seasons-sim');
    const earthGroup = document.getElementById('earth-group');
    const earthIlluminationOverlay = document.getElementById('earth-illumination-overlay');
    const illuminationRect = earthIlluminationOverlay.querySelector('rect');
    const playPauseBtn = document.getElementById('play-pause-btn');
    const positionLabel = document.getElementById('position-label');
    const seasonIndicator = document.getElementById('season-indicator');
    const jumpButtons = document.getElementById('jump-buttons');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const seasonLabelInSvg = document.getElementById('season-label');

    const SUN_POS = { x: 0, y: 0 };
    const ORBIT_RX = 300; // Horizontal radius
    const ORBIT_RY = 200; // Vertical radius (elliptical orbit)
    const EARTH_RADIUS = 20;
    const AXIAL_TILT_DEGREES = 23.5;
    const AXIAL_TILT_RADIANS = AXIAL_TILT_DEGREES * Math.PI / 180;

    let currentOrbitPosition = 0; // Value from 0 to 1 (representing percentage of orbit)
    let isPlaying = false;
    let animationFrameId = null;
    let lastTime = 0;
    const ORBIT_DURATION_MS = 20000; // Time for one full orbit (20 seconds) - slightly slower for smoother visual

    let isDragging = false;
    let dragStartAngle = 0; // Angle from SVG center to start drag point
    let dragStartOrbitPosition = 0;

    // Define key positions and corresponding seasons (Northern Hemisphere centric)
    // 0% (Right): Winter N / Summer S
    // 25% (Bottom): Spring N / Autumn S (Equinox)
    // 50% (Left): Summer N / Winter S
    // 75% (Top): Autumn N / Spring S (Equinox)
    const keyPositions = [
        { pos: 0, label: "חורף בצפון / קיץ בדרום" },
        { pos: 0.25, label: "אביב בצפון / סתיו בדרום (שוויון יום ולילה)" },
        { pos: 0.5, label: "קיץ בצפון / חורף בדרום" },
        { pos: 0.75, label: "סתיו בצפון / אביב בדרום (שוויון יום ולילה)" },
        { pos: 1, label: "חורף בצפון / קיץ בדרום" } // End is same as start
    ];

    // Function to calculate Earth's position on the ellipse for a given angle
    function getOrbitPosition(angleRadians) {
        const x = ORBIT_RX * Math.cos(angleRadians);
        const y = ORBIT_RY * Math.sin(angleRadians);
        return { x, y };
    }

    // Map percentage (0-1) to angle (0-2PI)
    // 0% -> 0 angle (right), 25% -> PI/2 (down), 50% -> PI (left), 75% -> 3PI/2 (up)
    function percentageToAngle(percentage) {
         return percentage * 2 * Math.PI;
    }

     // Function to update the season indicator text based on position
     function updateSeasonIndicator(percentage) {
         let seasonText = "";
         // Find the closest season marker or show transition
         if (percentage >= 0 && percentage < 0.125) seasonText = keyPositions[0].label; // Near 0
         else if (percentage >= 0.125 && percentage < 0.375) seasonText = keyPositions[1].label; // Near 0.25
         else if (percentage >= 0.375 && percentage < 0.625) seasonText = keyPositions[2].label; // Near 0.5
         else if (percentage >= 0.625 && percentage < 0.875) seasonText = keyPositions[3].label; // Near 0.75
         else seasonText = keyPositions[0].label; // Near 1 (which is same as 0)

         // Add transitions between main seasons
         if (percentage >= 0.1 && percentage < 0.2) seasonText = "מעבר לאביב (צפון)";
         if (percentage >= 0.35 && percentage < 0.45) seasonText = "מעבר לקיץ (צפון)";
         if (percentage >= 0.6 && percentage < 0.7) seasonText = "מעבר לסתיו (צפון)";
         if (percentage >= 0.85 && percentage < 0.95) seasonText = "מעבר לחורף (צפון)";


         seasonIndicator.textContent = seasonText;
         seasonLabelInSvg.textContent = seasonText; // Update SVG label too
     }


    // Calculate the rotation needed for the illumination overlay rect
    // This aims to rotate a horizontal gradient (bright left, dark right)
    // so its bright side faces the sun from Earth's perspective.
    function updateIllumination(earthX, earthY) {
         // Vector from Earth to Sun
         const sunVectorX = SUN_POS.x - earthX;
         const sunVectorY = SUN_POS.y - earthY;

         // Angle from Earth to Sun relative to positive X axis (right)
         let angleEarthToSun = Math.atan2(sunVectorY, sunVectorX); // Radians

         // The illumination rect needs to be rotated so its "bright" side (originally left) faces this direction.
         // A rotation of `angleEarthToSun` should align the gradient's bright-to-dark axis with the sun direction.
         // The linear gradient is horizontal (x1=0, x2=1).
         // Rotation 0: horizontal, bright left, dark right.
         // Rotation 90deg: vertical, bright down, dark up.
         // Rotation 180deg: horizontal, bright right, dark left.
         // Rotation -90deg: vertical, bright up, dark down.

         // We want the "bright" side to face the sun.
         // If angleEarthToSun is 0 (Sun is right of Earth), rotation should be 0.
         // If angleEarthToSun is PI/2 (Sun is below Earth), rotation should be 90.
         // If angleEarthToSun is PI (Sun is left of Earth), rotation should be 180.
         // If angleEarthToSun is -PI/2 (Sun is above Earth), rotation should be -90.
         // So the rotation angle in degrees is `angleEarthToSun * 180 / Math.PI`.

         let illuminationRotationDegrees = angleEarthToSun * 180 / Math.PI;

         // Position the illumination group at Earth's center first
         earthIlluminationOverlay.setAttribute('transform', `translate(${earthX}, ${earthY})`);

         // Rotate the rect within the illumination group around its own center (20,20)
         illuminationRect.setAttribute('transform', `rotate(${illuminationRotationDegrees}, 20, 20)`);

         // Note: This simplified illumination doesn't perfectly simulate the terminator ellipse shape on a tilted sphere.
         // It serves as a visual cue for the general direction of light. The *effect* of tilt is shown by the tilted axis
         // and explained by the season text changing and the explanation.
    }


    // Function to update Earth's position based on orbit percentage
    function updateEarthPosition(percentage) {
        // Ensure percentage is between 0 and 1
        percentage = percentage % 1;
        if (percentage < 0) percentage += 1;

        // Map percentage (0-1) to angle (0-2PI) for ellipse calculation
        // 0% maps to angle 0 (right), 25% to PI/2 (down), etc.
        const ellipseAngle = percentageToAngle(percentage);

        const { x, y } = getOrbitPosition(ellipseAngle);

        // Update Earth group position and apply fixed tilt rotation
        // The transform-origin and transform-box are set in CSS to rotate around the element's center.
        // The correct order is translate then rotate relative to the element's origin.
        // `transform: translate(${x}px, ${y}px) rotate(${-AXIAL_TILT_DEGREES}deg)`
        // is CSS syntax. For SVG transform attribute, it's space-separated functions.
        // The tilt is -23.5 relative to the vertical.
        // So, rotate the earth group by -23.5 degrees around its center, THEN translate it.
        // This applies the fixed tilt relative to the SVG coordinate system.
         earthGroup.setAttribute('transform', `translate(${x}, ${y}) rotate(${-AXIAL_TILT_DEGREES})`);


        // Update the illumination overlay based on the relative position to the sun
        updateIllumination(x, y);

        // Update the position label
        positionLabel.textContent = `מיקום במסלול: ${(percentage * 100).toFixed(0)}%`;

        // Update the season indicator
        updateSeasonIndicator(percentage);
    }


    // Animation loop
    function animateOrbit(currentTime) {
        if (!isPlaying) {
            animationFrameId = null;
            lastTime = 0; // Reset time for consistent start on next play
            return;
        }

        if (lastTime === 0) lastTime = currentTime;
        const elapsed = currentTime - lastTime;
        lastTime = currentTime;

        let progress = (elapsed / ORBIT_DURATION_MS);
        currentOrbitPosition += progress;

        // Loop the orbit
        if (currentOrbitPosition >= 1) {
            currentOrbitPosition -= 1;
        }

        updateEarthPosition(currentOrbitPosition);

        animationFrameId = requestAnimationFrame(animateOrbit);
    }

    // Dragging functionality
    function startDrag(event) {
        // Pause animation if playing
        if (isPlaying) {
             togglePlayPause(); // Use the toggle function to update button text etc.
        }

        isDragging = true;
        svg.style.cursor = 'grabbing';

         // Get mouse/touch position relative to SVG coordinate system
        const svgPoint = svg.createSVGPoint();
        svgPoint.x = event.clientX || (event.touches ? event.touches[0].clientX : 0);
        svgPoint.y = event.clientY || (event.touches ? event.touches[0].clientY : 0);
        const transformedPoint = svgPoint.matrixTransform(svg.getScreenCTM().inverse());

        const dragX = transformedPoint.x;
        const dragY = transformedPoint.y;

        // Calculate the angle from the center (0,0) to the drag start point
        // This angle is used as a proxy for progress along the orbit for dragging
        dragStartAngle = Math.atan2(dragY, dragX);
        dragStartOrbitPosition = currentOrbitPosition; // Store current position when drag starts

        // Prevent default touch actions like scrolling
        if (event.type === 'touchstart') {
            event.preventDefault();
        }
    }

     function drag(event) {
        if (!isDragging) return;

        const svgPoint = svg.createSVGPoint();
        svgPoint.x = event.clientX || (event.touches ? event.touches[0].clientX : 0);
        svgPoint.y = event.clientY || (event.touches ? event.touches[0].clientY : 0);
        const transformedPoint = svgPoint.matrixTransform(svg.getScreenCTM().inverse());

        const currentX = transformedPoint.x;
        const currentY = transformedPoint.y;

         // Calculate the current angle from the center (0,0)
        let currentAngle = Math.atan2(currentY, currentX); // Range -PI to PI

         // Convert current angle to 0-2PI range
         if (currentAngle < 0) currentAngle += 2 * Math.PI;

         // The angle we use for ellipse calculation is 0-2PI starting right (0%)
         // Map the current angle (0 to 2PI) back to the 0-1 percentage.
         // The mapping is simply angle / (2*PI).
         let newOrbitPosition = currentAngle / (2 * Math.PI);

         // Update position
         currentOrbitPosition = newOrbitPosition;

        updateEarthPosition(currentOrbitPosition);
     }

    function endDrag(event) {
        isDragging = false;
        svg.style.cursor = 'grab';
    }

    // Add event listeners for dragging (mouse and touch) on the SVG itself
    svg.addEventListener('mousedown', startDrag);
    svg.addEventListener('mousemove', drag);
    document.addEventListener('mouseup', endDrag); // Use document to capture release even if mouse leaves SVG

    svg.addEventListener('touchstart', startDrag, { passive: false }); // Use passive: false for preventDefault
    svg.addEventListener('touchmove', drag, { passive: false });
    document.addEventListener('touchend', endDrag);


    // Toggle Play/Pause function
    function togglePlayPause() {
         isPlaying = !isPlaying;
         if (isPlaying) {
             playPauseBtn.textContent = 'השהה';
             // Start animation loop. Pass performance.now() as the initial time.
             lastTime = performance.now();
             animationFrameId = requestAnimationFrame(animateOrbit);
         } else {
             playPauseBtn.textContent = 'הפעל';
             if (animationFrameId) {
                  cancelAnimationFrame(animationFrameId);
                  animationFrameId = null;
             }
             lastTime = 0; // Reset time so next play starts from current position's 'time = 0'
         }
    }

    playPauseBtn.addEventListener('click', togglePlayPause);

    // Jump buttons functionality
    jumpButtons.querySelectorAll('button').forEach(button => {
        button.addEventListener('click', (event) => {
            const targetPos = parseFloat(event.target.dataset.pos);
             // Pause animation if playing before jumping
             if (isPlaying) {
                 togglePlayPause();
             }
            currentOrbitPosition = targetPos;
            updateEarthPosition(currentOrbitPosition);
        });
    });


    // Toggle Explanation Button
    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מלא' : 'מה בעצם קורה כאן? (הסבר מלא)';
         // Optional: Scroll to the explanation when shown
         if (!isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });


    // Initial setup
    updateEarthPosition(0); // Start at the beginning of the orbit (Northern Winter)


</script>
```