---
title: "אנימציית קשת בענן: מסע האור הקסום בטיפת מים"
english_slug: rainbow-animation-light-path-water-drop
category: "מדעים מדויקים / פיזיקה"
tags: [אור, שבירה, החזרה, נפיצה, אופטיקה, אנימציה, קשת בענן]
---
# קשת בענן: הצצה למסע הקסום של קרן אור בטיפת גשם

האם עצרתם פעם להתפעל באמת מהיופי עוצר הנשימה של קשת בענן? הפלא הצבעוני הזה, המופיע כקסם בשמיים לאחר גשם, הוא תוצאה של ריקוד מופלא בין אור השמש הבוהק לטיפות הגשם הזעירות המרחפות באוויר. בואו נצלול יחד אל תוך טיפת מים אחת ונראה מה באמת קורה שם...

<div id="app">
    <div class="simulation-container">
        <svg id="rainbowSvg" viewBox="0 0 400 300" preserveAspectRatio="xMidYMid meet">
            <!-- Water drop shape (simplified circle) -->
            <circle cx="200" cy="150" r="80" fill="rgba(173, 216, 230, 0.9)" stroke="#66aaff" stroke-width="2"></circle>
            <!-- Sun hint -->
            <circle cx="50" cy="150" r="10" fill="gold" stroke="#ffcc00" stroke-width="2"></circle>
            <!-- Initial sun ray (animated endpoint) -->
            <line id="sunRay" x1="50" y1="150" x2="50" y2="150" stroke="white" stroke-width="3" stroke-linecap="round"></line>

            <!-- Paths for animation (will be drawn/animated by JS) -->
            <path id="entryPath" fill="none" stroke="white" stroke-width="3" stroke-linecap="round"></path>
            <path id="internalPath" fill="none" stroke="white" stroke-width="3" stroke-linecap="round"></path>
            <path id="reflectionPath" fill="none" stroke="white" stroke-width="3" stroke-linecap="round"></path>
            <!-- Spectrum exit paths -->
            <path id="exitRed" fill="none" stroke="red" stroke-width="3" stroke-linecap="round"></path>
            <path id="exitOrange" fill="none" stroke="orange" stroke-width="3" stroke-linecap="round"></path>
            <path id="exitYellow" fill="none" stroke="yellow" stroke-width="3" stroke-linecap="round"></path>
            <path id="exitGreen" fill="none" stroke="green" stroke-width="3" stroke-linecap="round"></path>
            <path id="exitBlue" fill="none" stroke="blue" stroke-width="3" stroke-linecap="round"></path>
            <path id="exitIndigo" fill="none" stroke="indigo" stroke-width="3" stroke-linecap="round"></path>
            <path id="exitViolet" fill="none" stroke="violet" stroke-width="3" stroke-linecap="round"></path>
        </svg>
    </div>
    <div class="controls">
        <button id="animateBtn">התחילו את מסע האור!</button>
    </div>
</div>

<button id="showExplanationBtn" class="toggle-button">הצגת הסבר קצר</button>

<div id="explanation" class="explanation-box">
    <h3>מסע האור בדרך לקשת</h3>
    <p>כאשר אור השמש, המורכב מכל צבעי הספקטרום, פוגש טיפת גשם, מתרחשים שלושה תהליכים אופטיים מרתקים:</p>
    <ol>
        <li>
            <strong>שבירה (Refraction):</strong> קרן האור נכנסת לטיפה ומשנה כיוון כשהיא עוברת מהאוויר למים הצפופים יותר אופטית. בנקודת הכניסה, האור הלבן מתחיל להתפצל לצבעיו המרכיבים (נפיצה), כי כל צבע נשבר בזווית מעט שונה. דמיינו את זה כפריסה של הצבעים.
        </li>
        <li>
            <strong>החזרה פנימית (Internal Reflection):</strong> האור השבור ממשיך לנוע בתוך הטיפה עד שהוא פוגע בדופן האחורית שלה. שם, במקום לצאת, רוב האור מוחזר חזרה פנימה אל תוך הטיפה. שלב זה חיוני כדי שהאור יחזור לכיווננו.
        </li>
        <li>
            <strong>שבירה ונפיצה חוזרת (Refraction & Dispersion):</strong> האור המוחזר חוזר לדופן הקדמית של הטיפה ויוצא ממנה אל האוויר. ביציאה השנייה הזו, האור נשבר ומתפצל עוד יותר לצבעים הבוהקים של הספקטרום - מסגול (הנשבר ביותר) בתחתית הקשת ועד אדום (הנשבר פחות) בחלקה העליון. כל טיפה מתפקדת כמנסרה זעירה, שולחת את הצבעים בכיוונים מדויקים. הקשת שאנו רואים היא האור המפוצל שמגיע לעינינו ממיליוני טיפות גשם שונות, כל אחת תורמת את הצבע הנכון בזווית הנכונה.
        </li>
    </ol>
    <p>האנימציה למעלה ממחישה את המסלול היחיד שעוברת קרן אור אחת בתוך טיפה אחת, ומציגה את הריקוד המורכב של שבירה, החזרה והיפרדות לצבעים המאפשר לנו לחוות את פלא הטבע המדהים הזה.</p>
</div>

<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* More modern font */
        line-height: 1.7; /* Better readability */
        color: #333;
        padding: 20px;
        background: linear-gradient(to bottom right, #e0f7fa, #c8e6c9); /* Subtle gradient background */
        direction: rtl; /* For Hebrew text */
        text-align: right; /* Align text to the right */
    }

    h1 {
        color: #4a148c; /* Darker purple */
        text-align: center;
        margin-bottom: 30px;
        font-size: 2em;
    }

     h3 {
        color: #0277bd; /* Darker blue for explanation title */
        margin-top: 0;
     }


    #app {
        background-color: #ffffff; /* White background */
        border-radius: 12px; /* More rounded corners */
        padding: 25px; /* More padding */
        margin-bottom: 30px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.1); /* Stronger shadow */
        text-align: center; /* Center the simulation */
        max-width: 500px; /* Slightly wider container */
        margin-left: auto;
        margin-right: auto;
        position: relative; /* Needed for potential absolute positioning inside */
    }

    .simulation-container {
        width: 100%;
        max-width: 450px; /* Slightly wider SVG */
        margin: 0 auto 20px auto; /* Center the SVG */
        position: relative;
        overflow: hidden; /* Hide parts of rays outside */
         border-radius: 8px; /* Match app borders */
         box-shadow: inset 0 0 10px rgba(0,0,0,0.05); /* Inner shadow for depth */
    }

    #rainbowSvg {
        background: radial-gradient(circle at 10% 90%, #bbdefb, #e3f2fd); /* Subtle radial background */
        border: 1px solid #b0bec5; /* Light border */
        border-radius: 8px; /* Match container */
        overflow: visible; /* Ensure path animation is visible */
        width: 100%; /* Make SVG responsive within container */
        height: auto;
    }

    circle[fill^="rgba"] { /* Style for the water drop */
         filter: drop-shadow(0px 4px 8px rgba(0,0,0,0.1)); /* Add shadow to drop */
         transition: fill 0.5s ease; /* Smooth transition if fill changes */
    }


    .controls {
        margin-top: 25px;
    }

    button {
        background-color: #673ab7; /* Deep purple */
        color: white;
        border: none;
        border-radius: 25px; /* Pill shape button */
        padding: 12px 25px; /* More padding */
        font-size: 1.1em; /* Slightly larger font */
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease; /* Add transform for press effect */
        font-weight: bold;
    }

    button:hover {
        background-color: #7e57c2; /* Lighter purple */
    }

    button:active {
        transform: scale(0.98); /* Slightly shrink when pressed */
    }

    .toggle-button {
        display: block; /* Make button take full width */
        width: fit-content; /* Adjust width to content */
        margin: 30px auto 15px auto; /* Center and add more margin */
        background-color: #039be5; /* Cyan-like blue */
        border-radius: 25px; /* Pill shape */
        padding: 10px 20px;
    }

    .toggle-button:hover {
         background-color: #0288d1; /* Darker blue */
    }


    .explanation-box {
        background-color: #e1f5fe; /* Very light blue */
        border-right: 5px solid #039be5; /* Blue right border for RTL */
        border-left: none; /* Remove left border */
        padding: 20px; /* More padding */
        margin-top: 25px;
        border-radius: 8px;
        display: none; /* Initially hidden */
        text-align: right;
        line-height: 1.8; /* More space between lines */
        box-shadow: 0 4px 10px rgba(0,0,0,0.08); /* Subtle shadow */
    }

    .explanation-box h3 {
        margin-bottom: 15px;
        color: #01579b; /* Even darker blue */
    }

    .explanation-box ol {
        padding-right: 25px; /* Indent list items more */
        margin-bottom: 15px;
    }

    .explanation-box li {
        margin-bottom: 10px; /* Space between list items */
    }

    .explanation-box li strong {
        color: #333; /* Keep strong text color consistent */
    }


    /* SVG Animation Styles (controlled by JS stroke-dashoffset/array) */
    path, line {
      stroke-dasharray: 0; /* Initially hidden */
      stroke-dashoffset: 0;
      /* JS will set dasharray and animate offset */
    }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const animateBtn = document.getElementById('animateBtn');
        const showExplanationBtn = document.getElementById('showExplanationBtn');
        const explanationDiv = document.getElementById('explanation');
        const svg = document.getElementById('rainbowSvg');
        const sunRay = document.getElementById('sunRay');
        const entryPath = document.getElementById('entryPath');
        const internalPath = document.getElementById('internalPath');
        const reflectionPath = document.getElementById('reflectionPath');
        const exitPaths = [
            document.getElementById('exitRed'),
            document.getElementById('exitOrange'),
            document.getElementById('exitYellow'),
            document.getElementById('exitGreen'),
            document.getElementById('exitBlue'),
            document.getElementById('exitIndigo'),
            document.getElementById('exitViolet')
        ];

        const centerX = 200;
        const centerY = 150;
        const radius = 80;
        const sunSourceX = 50;
        const sunSourceY = 150;

        // Define key points (simplified physics approximation for smooth paths)
        // Entry point slightly offset from center line for a more typical ray
        const entryAngle = Math.PI * 0.15; // Angle relative to horizontal from center
        const entryX = centerX - radius * Math.cos(entryAngle);
        const entryY = centerY - radius * Math.sin(entryAngle);

        // A control point inside the drop for a curved entry path (simplification)
        const internalControl1 = { x: centerX - radius * 0.2, y: centerY - radius * 0.1 };

        // Reflection point on the back side (simplified)
        const reflectionAngle = Math.PI * 0.6; // Angle relative to horizontal from center
        const reflectionX = centerX + radius * Math.cos(reflectionAngle);
        const reflectionY = centerY + radius * Math.sin(reflectionAngle);

         // A control point inside the drop for a curved path before reflection (simplification)
        const internalControl2 = { x: centerX + radius * 0.3, y: centerY + radius * 0.2 };


        // Exit point on the front side (simplified) - close to entry path side but lower
         const exitAngle = Math.PI * 0.2; // Angle relative to horizontal from center, lower part
         const exitX = centerX - radius * Math.cos(exitAngle);
         const exitY = centerY + radius * Math.sin(exitAngle);


        // Pre-calculate path D attributes
        const path1D = `M ${sunSourceX} ${sunSourceY} L ${entryX} ${entryY}`; // Straight line for sun ray approaching
        // Entry path with subtle curve
        const path2D = `M ${entryX} ${entryY} C ${internalControl1.x} ${internalControl1.y}, ${internalControl2.x} ${internalControl2.y}, ${reflectionX} ${reflectionY}`;
        // Reflection path
        const path3D = `M ${reflectionX} ${reflectionY} L ${exitX} ${exitY}`; // Straight line for reflection to exit point (can add curve if needed)

        // Exit path length for spectrum spreading
        const exitLength = 150; // How far the spectrum extends
        const baseExitAngle = Math.atan2(exitY - reflectionY, exitX - reflectionX); // Angle from reflection to exit
        const dispersionTotalAngle = Math.PI * 0.3; // Total angle spread of the spectrum (e.g., 54 degrees)

        // Calculate and set final D attributes for exit paths (including spread)
        const finalExitDs = exitPaths.map((path, index) => {
            // Index 0 is Red, Index 6 is Violet. Violet is refracted most, Red least.
            // Angle offset calculation: Map index 0-6 to -dispersionTotalAngle/2 to +dispersionTotalAngle/2
            const angleOffset = (index / (exitPaths.length - 1) - 0.5) * dispersionTotalAngle; // Negative for Red, Positive for Violet
            const finalAngle = baseExitAngle + angleOffset; // Exit direction

            const endX = exitX + exitLength * Math.cos(finalAngle);
            const endY = exitY + exitLength * Math.sin(finalAngle);

            // Path from exit point outwards
            return `M ${exitX} ${exitY} L ${endX} ${endY}`;
        });

        // Set fixed path data once
        sunRay.setAttribute('d', path1D); // SunRay is now a path for better animation control
        entryPath.setAttribute('d', path2D);
        reflectionPath.setAttribute('d', path3D);
        exitPaths.forEach((path, i) => {
             path.setAttribute('d', finalExitDs[i]);
        });


        function resetAnimation() {
             // Hide all paths
             const allPaths = [sunRay, entryPath, internalPath, reflectionPath, ...exitPaths];
             allPaths.forEach(path => {
                 path.style.strokeDasharray = path.getTotalLength() + ' ' + path.getTotalLength(); // Make dash and gap equal to length
                 path.style.strokeDashoffset = path.getTotalLength(); // Hide path
                 path.style.opacity = 1; // Reset opacity
             });

             // Clear internalPath D initially as it's dynamically set in animation
              internalPath.setAttribute('d', ''); // Clear path data initially
        }


        // Animation sequence using requestAnimationFrame
        function animateSequence() {
             resetAnimation();
             // Disable button during animation
             animateBtn.disabled = true;
             animateBtn.textContent = '...מסע האור בעיצומו';

             const raySegmentLength = 40; // Length of the visible light segment
             const pathAnimationDuration = 1500; // Duration for each main path segment (ms)
             const dispersionDuration = 2000; // Duration for color spreading
             const segmentAnimationSpeed = 0.05; // Speed factor for dashoffset animation

             // Step 1: Animate sun ray approaching the drop
             const sunRayTotalLength = sunRay.getTotalLength();
             sunRay.style.strokeDasharray = `${raySegmentLength} ${sunRayTotalLength}`; // Visible segment + Gap
             // Start segment just off the start point, will animate offset to reveal it moving
             sunRay.style.strokeDashoffset = sunRayTotalLength - raySegmentLength;


             animatePathSegment(sunRay, sunRayTotalLength, sunRayTotalLength - raySegmentLength, 0, pathAnimationDuration, 'easeOutCubic')
                .then(() => {
                     // Step 2: Animate light entering and moving through the drop (entryPath + internalPath)
                     const path2TotalLength = entryPath.getTotalLength();
                      entryPath.style.strokeDasharray = `${raySegmentLength} ${path2TotalLength}`;
                      entryPath.style.strokeDashoffset = path2TotalLength - raySegmentLength;

                    // Instead of drawing path2D directly, let's make internalPath *follow* the light segment for a more dynamic feel
                    // This requires drawing the internalPath dynamically based on the segment's position on entryPath.
                    // This dynamic drawing might be too complex for the strict structure constraint.
                    // Let's revert to animating segment along pre-defined paths but making the internal path appear simultaneously.

                    // Animate segment along entryPath
                    animatePathSegment(entryPath, path2TotalLength, path2TotalLength - raySegmentLength, 0, pathAnimationDuration, 'easeOutCubic')
                        .then(() => {
                            // Step 3: Animate segment along reflectionPath
                            const path3TotalLength = reflectionPath.getTotalLength();
                            reflectionPath.style.strokeDasharray = `${raySegmentLength} ${path3TotalLength}`;
                            reflectionPath.style.strokeDashoffset = path3TotalLength - raySegmentLength;

                            animatePathSegment(reflectionPath, path3TotalLength, path3TotalLength - raySegmentLength, 0, pathAnimationDuration * 0.8, 'easeOutCubic') // Slightly faster reflection
                                .then(() => {
                                     // Step 4: Animate spectrum spreading from exit point
                                     // Transition the white reflection segment to multiple colored segments
                                     reflectionPath.style.strokeDasharray = '0 10000'; // Hide the white segment trail

                                     exitPaths.forEach((path, i) => {
                                         const pathLength = path.getTotalLength();
                                         path.style.strokeDasharray = `${raySegmentLength} ${pathLength}`; // Segment for each color
                                         path.style.strokeDashoffset = pathLength; // Start hidden at the end

                                         // Animate offset from end to start to make segment move away from exit point
                                         // Add a slight delay for each color to enhance the spread effect
                                         const delay = i * (dispersionDuration / exitPaths.length / 1.5); // Staggered delay

                                          animatePathSegment(path, pathLength, pathLength, 0, dispersionDuration, 'easeOutCubic', delay);
                                     });

                                      // Re-enable button after approximate total animation time
                                      setTimeout(() => {
                                           animateBtn.disabled = false;
                                           animateBtn.textContent = 'אנימציה מחדש';
                                      }, pathAnimationDuration * 3 + dispersionDuration + 500); // Wait for all parts + buffer
                                });
                        });
                });
        }

        // Helper function to animate stroke-dashoffset
        function animatePathSegment(pathElement, totalLength, startOffset, endOffset, duration, easing = 'linear', delay = 0) {
            return new Promise(resolve => {
                let startTime = null;

                function step(timestamp) {
                    if (!startTime) startTime = timestamp + delay; // Apply delay
                    let progress = (timestamp - startTime) / duration;

                     if (progress < 0) { // Wait for delay
                        requestAnimationFrame(step);
                        return;
                     }
                    if (progress > 1) progress = 1;

                    // Apply easing function
                    let easedProgress = progress; // Default is linear
                    if (easing === 'easeOutCubic') {
                         easedProgress = 1 - Math.pow(1 - progress, 3);
                    } // Add other easing functions if needed

                    const currentOffset = startOffset + (endOffset - startOffset) * easedProgress;
                    pathElement.style.strokeDashoffset = currentOffset;

                    if (progress < 1) {
                        requestAnimationFrame(step);
                    } else {
                        resolve(); // Resolve the promise when animation is done
                    }
                }
                 requestAnimationFrame(step);
            });
        }


        animateBtn.addEventListener('click', animateSequence);

        // Toggle explanation visibility
        showExplanationBtn.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            showExplanationBtn.textContent = isHidden ? 'הסתרת הסבר' : 'הצגת הסבר קצר'; // Update button text
        });

        // Initial state setup
        resetAnimation();
        animateBtn.textContent = 'התחילו את מסע האור!'; // Set initial button text
    });
</script>