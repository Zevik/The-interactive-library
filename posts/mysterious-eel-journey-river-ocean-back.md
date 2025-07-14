---
title: "מסע הצלופח המסתורי: מהנהר לאוקיינוס ובחזרה"
english_slug: "mysterious-eel-journey-river-ocean-back"
category: "ביולוגיה"
tags:
- צלופח
- נדידה
- מחזור חיים
- מים מתוקים
- אוקיינוס
---
# מסע החיים הפלאי של הצלופח: מהנהר העצום לאוקיינוס המסתורי

הצלופח, יצור אניגמטי ומרתק, מבלה שנים רבות משנות חייו השלוות במים המתוקים של נהרות אירופה. אך כשהקריאה להתרבות מגיעה, הוא יוצא למסע אפי ובלתי נתפס – אלפי קילומטרים אל מעמקי האוקיינוס האטלנטי ויעד התרבות החידתי שלו. כיצד הוא מוצא את הדרך, ואיך הדור הבא חוזר אל נקודת המוצא של הוריהם? הצטרפו אלינו למסע מופלא שיחשוף את מחזור החיים המסתורי הזה.

<div id="eel-journey-app">
    <div class="controls">
        <button id="play-pause-btn" class="control-btn">התחל מסע</button>
        <button id="reset-btn" class="control-btn">התחל מחדש</button>
    </div>
    <div class="map-container">
        <svg id="eel-map" viewBox="0 0 800 400" preserveAspectRatio="xMidYMid meet">
            <!-- Map Background & Features -->
            <rect x="0" y="0" width="800" height="400" fill="url(#oceanGradient)"></rect> <!-- Ocean with Gradient -->
            <rect x="0" y="200" width="250" height="200" fill="url(#landGradient)"></rect> <!-- Land with Gradient -->
            <path d="M 0 300 C 50 280, 180 330, 250 310 V 400 H 0 Z" fill="url(#riverGradient)"></path> <!-- River representation -->
            <circle cx="700" cy="100" r="40" fill="rgba(255, 100, 180, 0.3)" class="sargasso-area"></circle> <!-- Sargasso Sea area -->
            <text x="700" y="100" text-anchor="middle" alignment-baseline="middle" font-size="16" fill="#003366" font-weight="bold" class="map-label">ים סרגסו</text>
            <text x="120" y="350" text-anchor="middle" alignment-baseline="middle" font-size="16" fill="#003366" font-weight="bold" class="map-label">נהרות אירופה</text>

             <!-- SVG Definitions (Gradients) -->
            <defs>
                <linearGradient id="oceanGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" style="stop-color:#a0e0ff;stop-opacity:1" />
                    <stop offset="100%" style="stop-color:#50a0e0;stop-opacity:1" />
                </linearGradient>
                 <linearGradient id="landGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" style="stop-color:#8b4513;stop-opacity:1" /> <!-- SaddleBrown -->
                    <stop offset="100%" style="stop-color:#a0522d;stop-opacity:1" /> <!-- Sienna -->
                </linearGradient>
                 <linearGradient id="riverGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" style="stop-color:#4682b4;stop-opacity:1" /> <!-- SteelBlue -->
                    <stop offset="100%" style="stop-color:#6a5acd;stop-opacity:1" /> <!-- SlateBlue -->
                </linearGradient>
            </defs>


            <!-- Journey Paths -->
            <!-- Forward path: River to Sargasso -->
            <path id="forward-path" d="M 100 300 L 250 310 C 300 300, 350 250, 400 250 L 650 250 C 700 250, 700 150, 700 100"
                  fill="none" stroke="#004080" stroke-width="3" stroke-linecap="round" class="journey-path forward"></path>

            <!-- Return path: Sargasso to River (Larva/Elver) -->
             <path id="return-path" d="M 700 100 C 680 50, 600 60, 550 100 C 500 150, 500 220, 450 280 C 400 340, 300 370, 200 360 L 100 350 C 50 340, 50 310, 100 300"
                  fill="none" stroke="#66ccff" stroke-width="3" stroke-linecap="round" class="journey-path return"></path>

            <!-- Eel/Larva representation - starts in river -->
            <circle id="eel" cx="100" cy="300" r="8" fill="yellow" class="eel-sprite"></circle>

             <!-- Stage Markers -->
            <circle class="stage-marker" cx="100" cy="300" r="6" fill="#e74c3c" data-info="**שלב 1:** חיים בנהר כצלופח צהוב. שנים של גדילה והתפתחות במים מתוקים או מליחים."></circle>
            <circle class="stage-marker" cx="220" cy="305" r="6" fill="#e67e22" data-info="**שלב 2:** שינוי דרמטי! הופך לצלופח כסוף מוכן לנדידה. שינויים פיזיולוגיים עצומים לקראת המסע לאוקיינוס."></circle>
            <circle class="stage-marker" cx="700" cy="100" r="6" fill="#9b59b6" data-info="**שלב 3:** הגעה ליעד המסתורי - ים סרגסו. כאן מתרחשת ההתרבות, ולאחריה הצלופחים הבוגרים מסיימים את מחזור חייהם."></circle>
            <circle class="stage-marker" cx="550" cy="100" r="6" fill="#3498db" data-info="**שלב 4:** מהביצים בוקעים זחלי לפטוצפל שקופים ושטוחים. הם מתחילים את מסעם בחזרה, נסחפים בזרם הגולף."></circle>
             <circle class="stage-marker" cx="200" cy="360" r="6" fill="#2ecc71" data-info="**שלב 5:** הזחלים הופכים לאילים - צלופחונים קטנים ושקופים, הדומים יותר לבוגרים. הם הגיעו לחופי אירופה."></circle>
            <circle class="stage-marker" cx="100" cy="350" r="6" fill="#f1c40f" data-info="**שלב 6:** האילים נכנסים למים מתוקים ומתחילים את העלייה האתגרית במעלה הנהרות, בניגוד לזרם."></circle>


        </svg>
    </div>
     <div id="info-box" class="info-box">לחצו על 'התחל מסע' כדי לראות את מסע הצלופח המופלא. ניתן גם ללחוץ על הסימנים הצבעוניים במסלול למידע נוסף.</div>
</div>

<button id="toggle-explanation" class="control-btn secondary">הצג הסבר מפורט</button>

<div id="explanation" class="explanation-box" style="display: none;">
    <h2>פלא טבע: מסע החיים המלא של הצלופח האירופי</h2>
    <p>מסע החיים של הצלופח האירופי (Anguilla anguilla) הוא אחד האודיסיאות המרתקות והמסתוריות ביותר בעולם הטבע. הוא מדגים יכולת הישרדות, ניווט ושינוי צורה מדהימות לאורך מסע חוצה אוקיינוסים.</p>
    <h3>שלבי המסע וההתפתחות:</h3>
    <ul>
        <li>**שלב 1: הצלופח הצהוב בנהר**<br>שנים ארוכות, לרוב 5-20 שנה ואף יותר, הצלופחים מבלים במים מתוקים או מליחים (שפכי נהרות). הם מכונים "צלופחים צהובים" בשל גוונם הירוק-צהבהב. זהו שלב הגדילה והאכילה העיקרי, במהלכו הם צוברים אנרגיה לקראת המסע הגדול.</li>
        <li>**שלב 2: ההתגלגלות לצלופח כסוף והיציאה לים**<br>כאשר הצלופח מגיע לבגרות מינית והתנאים מתאימים, הוא עובר טרנספורמציה פיזית מדהימה: צבעו הופך כסוף-מטאלי (מכאן השם "צלופח כסוף"), עיניו גדלות פי 2-3 כדי להתאים לראייה במעמקי הים, מערכת העיכול שלו מצטמצמת (הוא מפסיק לאכול), ומאגרי השומן גדלים באופן משמעותי. הוא נודד במורד הנהר אל עבר הים הפתוח.</li>
        <li>**שלב 3: המסע חוצה האוקיינוס וההגעה לים סרגסו**<br>כצלופחים כסופים, הם יוצאים למסע בן אלפי קילומטרים במורד הנהרות ולאורך חופי אירופה, ומשם חוצים את האוקיינוס האטלנטי. יעד המסע הוא אזור מסתורי במרכז צפון האוקיינוס האטלנטי המכונה ים סרגסו, אזור שקט יחסית עשיר באצות ים. המסע הימי נמשך חודשים רבים.</li>
        <li>**שלב 4: התרבות וסיום המסע של הבוגרים בים סרגסו**<br>בים סרגסו, במים עמוקים ובתנאים מסתוריים שטרם הובנו לחלוטין, הצלופחים מתרבים (הטלה והפריה). לאחר מכן, הצלופחים הבוגרים, שהשקיעו את כל מרצם במסע ובהתרבות, מתים ובכך משלימים את מחזור חייהם.</li>
        <li>**שלב 5: זחלי לפטוצפל נסחפים בחזרה לאירופה**<br>מהביצים בוקעים זחלים שקופים, שטוחים ודמויי עלה, הנקראים לפטוצפלים (Leptocephali). הם אינם שוחים באופן פעיל לכיוון אירופה, אלא נסחפים במשך כשנה עד שלוש שנים בזרם הגולף העצום ממערב למזרח, חוצים שוב את האוקיינוס האטלנטי עד לחופי אירופה וצפון אפריקה.</li>
        <li>**שלב 6: התגלגלות לאיל (צלופחון שקוף) בחופים**<br>כשהלפטוצפלים מגיעים סמוך לחופי אירופה, הם עוברים גלגול נוסף והופכים ל"איל" (Elver) - צלופחון קטן, שקוף וגלילי, שכבר מזכיר בצורתו צלופח בוגר. שקיפותם מסייעת להם להתגונן מטורפים במים הרדודים.</li>
        <li>**שלב 7: העלייה האתגרית במעלה הנהרות וחזרה למים מתוקים**<br>האילים נכנסים מהים למים מתוקים ומתחילים את מסעם המדהים במעלה הנהרות והנחלים. הם מסוגלים להתגבר על מכשולים רבים, כולל מפלים ותעלות, בדרכם למעלה הזרם, אל בתי הגידול של הצלופחים הצהובים.</li>
        <li>**שלב 8: חזרה לשלב הצלופח הצהוב והשלמת המעגל**<br>האילים מגיעים ליעדם בנהרות, אגמים או בריכות, מאבדים את שקיפותם, מקבלים את צבעם הצהבהב-ירקרק והופכים שוב לצלופחים צהובים. הם מתחילים את שלב הגדילה הארוך במים המתוקים, עד שיגיע תורם לצאת למסע ההתרבות הבלתי נתפס ולסגור את מעגל החיים הפלאי.</li>
    </ul>
</div>

<style>
    /* General Styles for premium look */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6;
        margin: 0;
        padding: 20px;
    }

    h1, h2, h3 {
        color: #004080; /* Deep Blue */
        text-align: center;
        margin-bottom: 15px;
    }

    h1 {
        font-size: 2em;
        margin-top: 0;
    }

    h2 {
        font-size: 1.5em;
    }

    h3 {
        font-size: 1.2em;
        margin-top: 20px;
        margin-bottom: 10px;
        color: #0056b3; /* Slightly lighter blue */
    }

    p, ul {
        margin-bottom: 15px;
    }

    ul {
        padding-left: 20px;
    }

    li {
        margin-bottom: 8px;
    }

    strong {
        color: #004080;
    }


    /* App Container */
    #eel-journey-app {
        border: 1px solid #d1d9e6; /* Soft border */
        padding: 25px;
        border-radius: 12px;
        background-color: #ffffff; /* Clean white background */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        max-width: 850px; /* Slightly wider */
        margin: 30px auto;
        text-align: center;
        direction: rtl; /* Ensure RTL layout */
    }

    /* Controls */
    .controls {
        margin-bottom: 20px;
        display: flex;
        justify-content: center;
        gap: 15px; /* Space between buttons */
    }

    .control-btn {
        padding: 10px 20px;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        font-size: 1rem;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.2s ease;
        min-width: 100px; /* Ensure consistent button width */
    }

    .control-btn:hover {
         transform: translateY(-2px);
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }

     .control-btn:active {
        transform: translateY(0);
        box-shadow: none;
    }


    /* Primary Button */
    #play-pause-btn, #reset-btn {
        background: linear-gradient(to bottom, #007bff, #0056b3); /* Gradient */
        color: white;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
    }

    #play-pause-btn:hover, #reset-btn:hover {
        background: linear-gradient(to bottom, #0067cc, #004080);
    }


    /* Secondary Button */
    .control-btn.secondary {
        background: linear-gradient(to bottom, #28a745, #218838); /* Green Gradient */
        color: white;
         box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
    }

    .control-btn.secondary:hover {
         background: linear-gradient(to bottom, #218838, #1a6f2d);
    }


    /* Map Container */
    .map-container {
        width: 100%;
        height: auto; /* Maintain aspect ratio */
        border: 1px solid #ccc; /* Subtle border for map area */
        border-radius: 8px;
        overflow: hidden; /* Ensure map elements stay within bounds */
        box-shadow: inset 0 0 10px rgba(0,0,0,0.05); /* Inner shadow */
    }

    #eel-map {
        display: block; /* Remove extra space below svg */
        width: 100%;
        height: auto;
        background-color: #e0f0ff; /* Fallback background, gradient takes over */
    }

     /* Map labels */
     .map-label {
         text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
     }

     /* Sargasso Area Pulse */
     .sargasso-area {
         animation: pulse 2s infinite ease-in-out;
     }

     @keyframes pulse {
         0% { transform: scale(1); opacity: 0.3; }
         50% { transform: scale(1.05); opacity: 0.5; }
         100% { transform: scale(1); opacity: 0.3; }
     }


    /* Eel Sprite Animation */
    .eel-sprite {
        transform-origin: center; /* Ensure rotation is around its center */
        transition: cx linear, cy linear, fill 0.5s ease-in-out, r 0.5s ease-in-out; /* Smooth transition for position, color, size */
        cursor: pointer;
         /* Add a subtle pulse or glow? */
         /* animation: subtle-pulse 3s infinite ease-in-out; */
    }

     @keyframes subtle-pulse {
         0%, 100% { transform: scale(1); opacity: 1; }
         50% { transform: scale(1.02); opacity: 0.95; }
     }


    /* Journey Path Styles (drawing animation handled by JS) */
    .journey-path {
        fill: none;
        stroke-width: 3;
        stroke-linecap: round;
         /* Initial state for drawing effect */
        stroke-dasharray: 1000; /* Needs to be larger than max path length */
        stroke-dashoffset: 1000; /* Start hidden */
        transition: stroke-dashoffset linear; /* Animate offset */
        opacity: 0.7; /* Make path slightly transparent */
    }

    #forward-path {
         stroke: #004080; /* Deep blue for forward journey */
    }

     #return-path {
         stroke: #66ccff; /* Light blue for return journey */
     }


    /* Stage Markers */
    .stage-marker {
        cursor: pointer;
        opacity: 0.9;
        transition: r 0.3s ease-in-out, opacity 0.3s ease-in-out;
        stroke: rgba(255,255,255,0.5); /* Add a white stroke */
        stroke-width: 1;
    }

    .stage-marker:hover {
         r: 9; /* Increase size on hover */
         opacity: 1;
         stroke-width: 2;
         stroke: rgba(255,255,255,0.8);
    }

    /* Info Box */
    .info-box {
        margin-top: 20px;
        padding: 15px;
        border: 1px solid #b8daff; /* Light blue border */
        background-color: #e9f5ff; /* Very light blue background */
        border-radius: 8px;
        min-height: 50px; /* Ensure space even when empty */
        text-align: center;
        font-size: 1rem;
        color: #004080; /* Match heading color */
        display: flex; /* Use flexbox for centering text */
        align-items: center;
        justify-content: center;
        font-weight: bold;
         direction: rtl;
         text-align: right; /* Align text right within the box */
    }

    /* Explanation Section */
    .explanation-box {
        border: 1px solid #d6d8db;
        padding: 25px;
        border-radius: 12px;
        background-color: #f8f9fa; /* Light gray background */
        max-width: 850px;
        margin: 20px auto;
        line-height: 1.7;
        direction: rtl; /* Ensure RTL layout */
        text-align: right; /* Align text right */
    }

    .explanation-box h2, .explanation-box h3 {
        text-align: right; /* Align headings right within the box */
        margin-top: 15px;
        margin-bottom: 10px;
    }

    .explanation-box ul {
        list-style: disc outside; /* Disc outside list style */
        margin-right: 20px; /* Adjust margin for RTL */
        padding: 0; /* Reset padding */
    }

    .explanation-box li {
        margin-bottom: 12px;
        padding-right: 5px; /* Add slight padding */
    }

     .explanation-box li strong {
         display: block; /* Make the bold stage title a block */
         margin-bottom: 5px;
         color: #0056b3;
     }


    /* Responsive adjustments */
    @media (max-width: 600px) {
        #eel-journey-app, .explanation-box {
            padding: 15px;
        }
        .controls {
            flex-direction: column;
            gap: 10px;
        }
        .control-btn {
            width: 100%;
            min-width: auto;
        }
        h1 {
            font-size: 1.5em;
        }
        h2 {
            font-size: 1.3em;
        }
         .map-label {
             font-size: 14px;
         }
         .info-box {
             font-size: 0.9rem;
         }
    }
</style>

<script>
    const eel = document.getElementById('eel');
    const forwardPath = document.getElementById('forward-path');
    const returnPath = document.getElementById('return-path');
    const playPauseBtn = document.getElementById('play-pause-btn');
    const resetBtn = document.getElementById('reset-btn');
    const infoBox = document.getElementById('info-box');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const stageMarkers = document.querySelectorAll('.stage-marker');

    let animation;
    let startTime;
    let pathLengthForward;
    let pathLengthReturn;
    let currentPath = 'forward'; // 'forward' or 'return'
    let pathElement;
    let animationPaused = false;
    let pauseTime = 0;
    let animationProgress = 0; // 0 to 1, total journey progress

    // Get path lengths - recalculate if SVG size changes?
    function getPathLengths() {
        pathLengthForward = forwardPath.getTotalLength();
        returnPath.style.strokeDasharray = returnPath.getTotalLength(); // Set dasharray for return path initially
        returnPath.style.strokeDashoffset = returnPath.getTotalLength(); // Hide return path initially
        forwardPath.style.strokeDasharray = pathLengthForward; // Set dasharray for forward path
        // forwardPath.style.strokeDashoffset = pathLengthForward; // Set by reset initially
        pathLengthReturn = returnPath.getTotalLength();

        console.log("Forward path length:", pathLengthForward);
        console.log("Return path length:", pathLengthReturn);
    }
    getPathLengths(); // Calculate initially and when window resizes? Add resize listener? Keep simple for now.

    // Function to get point and tangent on path at a given distance
    function getPointAndTangentAtDistance(distance) {
        const point = pathElement.getPointAtLength(distance);
        // To get direction/tangent, get a point slightly ahead
        const nextPoint = pathElement.getPointAtLength(distance + 0.1 > pathElement.getTotalLength() ? pathElement.getTotalLength() : distance + 0.1);
        const angle = Math.atan2(nextPoint.y - point.y, nextPoint.x - point.x) * 180 / Math.PI;
        return { point, angle };
    }

    // Update eel position, rotation, color, size, and path drawing
    function updateAnimation(timestamp) {
        if (!startTime) startTime = timestamp;
        if (animationPaused) {
            startTime = timestamp - pauseTime; // Adjust start time to resume from pause
        }
        const elapsed = timestamp - startTime;
        let duration; // milliseconds
        let currentLength;
        let info = "";
        let eelColor = "yellow";
        let eelRadius = 8;

        const totalJourneyDuration = 20000; // Total duration for the whole journey (e.g., 20 seconds)
        const forwardDuration = totalJourneyDuration * (pathLengthForward / (pathLengthForward + pathLengthReturn));
        const returnDuration = totalJourneyDuration * (pathLengthReturn / (pathLengthForward + pathLengthReturn));


        if (currentPath === 'forward') {
            duration = forwardDuration;
            pathElement = forwardPath;
            currentLength = (elapsed / duration) * pathLengthForward;

            if (currentLength >= pathLengthForward) {
                // Reached Sargasso - Transition to return path
                currentLength = pathLengthForward;
                const { point, angle } = getPointAndTangentAtDistance(currentLength);
                eel.setAttribute('cx', point.x);
                eel.setAttribute('cy', point.y);
                // No rotation needed at Sargasso? Or reset? Keep angle from previous point.
                eel.style.transform = `rotate(${angle + 90}deg)`; // Rotate circle sprite to align with path

                 // Final state for forward path drawing
                forwardPath.style.strokeDashoffset = 0;

                currentPath = 'return';
                startTime = timestamp; // Reset timer for the new path
                pauseTime = 0; // Reset pause time
                animationProgress = 0.5; // Halfway point roughly

                 // Set return path for drawing
                 returnPath.style.strokeDasharray = pathLengthReturn; // Ensure it's set
                 returnPath.style.strokeDashoffset = pathLengthReturn; // Start hidden

                // Info update at Sargasso
                updateInfoBox(stageMarkers[2].getAttribute('data-info')); // Stage 3 info
                eelColor = "#9b59b6"; // Match marker color temporarily? Or keep silver? Let's make it fade out visually.
                eel.setAttribute('fill', eelColor);
                eel.setAttribute('r', eelRadius);

                 // Animation continues immediately to the return journey
                 animation = requestAnimationFrame(updateAnimation);
                 return; // Exit current frame to start new path logic

            }

            const { point, angle } = getPointAndTangentAtDistance(currentLength);
            eel.setAttribute('cx', point.x);
            eel.setAttribute('cy', point.y);
            eel.style.transform = `rotate(${angle + 90}deg)`; // Rotate circle sprite to align with path

            // Animate forward path drawing
            forwardPath.style.strokeDashoffset = pathLengthForward - currentLength;

            // Update color and info based on progress along forward path
            const progress = currentLength / pathLengthForward;
            animationProgress = progress * 0.5; // Represents first half of total journey

            if (progress < 0.1) { // River (Yellow eel)
                 eelColor = "yellow";
                 info = stageMarkers[0].getAttribute('data-info'); // Stage 1 info
            } else if (progress < 0.9) { // Ocean travel (Silver eel)
                 eelColor = "silver";
                 info = stageMarkers[1].getAttribute('data-info'); // Stage 2 info
            } else { // Approaching Sargasso
                 eelColor = "silver"; // Still silver
                 info = stageMarkers[2].getAttribute('data-info'); // Stage 3 info (Approaching)
            }
            eelRadius = 8; // Keep size consistent for adult stages


        } else { // currentPath === 'return'
            duration = returnDuration;
            pathElement = returnPath;
            currentLength = (elapsed / duration) * pathLengthReturn;

            if (currentLength >= pathLengthReturn) {
                // Animation finished
                currentLength = pathLengthReturn;
                const { point, angle } = getPointAndTangentAtDistance(currentLength);
                eel.setAttribute('cx', point.x);
                eel.setAttribute('cy', point.y);
                 eel.style.transform = `rotate(${angle + 90}deg)`; // Rotate to align with final point

                 // Final state for return path drawing
                returnPath.style.strokeDashoffset = 0;

                cancelAnimationFrame(animation);
                animation = null;
                animationPaused = false; // Ensure state is reset
                playPauseBtn.textContent = 'התחל מסע מחדש'; // Change button text
                animationProgress = 1; // Completed

                // Final info message
                updateInfoBox("מעגל החיים הושלם! הצלופח חזר לנהר כצלופח צהוב ומתחיל שלב חדש.");
                eelColor = "yellow"; // Back to yellow
                eelRadius = 8; // Reset size
                eel.setAttribute('fill', eelColor);
                eel.setAttribute('r', eelRadius);

                 // Reset path drawing visually for next play
                 forwardPath.style.strokeDashoffset = pathLengthForward;
                 returnPath.style.strokeDashoffset = pathLengthReturn;

                return; // End animation
            }

            const { point, angle } = getPointAndTangentAtDistance(currentLength);
            eel.setAttribute('cx', point.x);
            eel.setAttribute('cy', point.y);
             eel.style.transform = `rotate(${angle + 90}deg)`; // Rotate circle sprite to align with path

             // Animate return path drawing
             returnPath.style.strokeDashoffset = pathLengthReturn - currentLength;

            // Update color/size and info based on progress along return path
            const progress = currentLength / pathLengthReturn;
            animationProgress = 0.5 + progress * 0.5; // Represents second half of total journey


             if (progress < 0.05) { // Just left Sargasso (symbolizing parents died/transition)
                 eelColor = "rgba(155, 89, 182, 0.5)"; // Faded color from Sargasso marker
                 info = stageMarkers[2].getAttribute('data-info') + "<br>...הורים מסיימים מסע. מתחיל שלב הזחלים."; // Info remains from Sargasso entry briefly
                 eelRadius = 8; // Still adult size temporarily
             } else if (progress < 0.5) { // Larval drift (Leptocephalus)
                 eelColor = "rgba(173, 216, 230, 0.7)"; // Light blue with opacity for transparent look
                 eelRadius = 5; // Smaller size for larva
                 info = stageMarkers[3].getAttribute('data-info'); // Stage 4 info
             } else if (progress < 0.9) { // Glass eel / Elver
                 eelColor = "#66ccff"; // Light blue, more solid
                 eelRadius = 7; // Slightly larger, approaching juvenile size
                 info = stageMarkers[4].getAttribute('data-info'); // Stage 5 info
             } else { // Moving up river (turning Yellow)
                 // Transition color from light blue to yellow
                 const transitionProgress = (progress - 0.9) / 0.1; // Progress in the last 10%
                 const startColor = [102, 204, 255]; // RGB for #66ccff (light blue)
                 const endColor = [255, 255, 0]; // RGB for yellow
                 const interpColor = startColor.map((start, i) =>
                     Math.round(start + (endColor[i] - start) * transitionProgress)
                 );
                 eelColor = `rgb(${interpColor.join(',')})`;
                 eelRadius = 8; // Back to adult size
                 info = stageMarkers[5].getAttribute('data-info') + "<br>...הופך לצלופח צהוב."; // Stage 6 info + turning yellow
             }
        }

        // Apply visual updates
        eel.setAttribute('fill', eelColor);
        eel.setAttribute('r', eelRadius);
        updateInfoBox(info);


        if (!animationPaused) {
             animation = requestAnimationFrame(updateAnimation);
        }
    }

    // Control buttons
    playPauseBtn.addEventListener('click', () => {
        if (!animation && !animationPaused) {
            // Start animation from beginning
            currentPath = 'forward';
            startTime = null; // Reset start time
            pauseTime = 0;
            animationPaused = false;
            playPauseBtn.textContent = 'השהה מסע';
            updateInfoBox("המסע החל! צלופח צהוב יוצא מהנהר...");

             // Reset eel position, color, size, rotation
            eel.setAttribute('cx', '100');
            eel.setAttribute('cy', '300');
            eel.setAttribute('fill', 'yellow');
            eel.setAttribute('r', 8);
            eel.style.transform = 'rotate(90deg)'; // Initial rotation along river path

             // Reset path drawing visual state
            forwardPath.style.strokeDashoffset = pathLengthForward;
            returnPath.style.strokeDashoffset = pathLengthReturn;


            animation = requestAnimationFrame(updateAnimation);
        } else if (animationPaused) {
            // Resume animation
            animationPaused = false;
            playPauseBtn.textContent = 'השהה מסע';
            // startTime will be adjusted in updateAnimation to account for pauseTime
             animation = requestAnimationFrame(updateAnimation);
        } else {
            // Pause animation
            animationPaused = true;
            playPauseBtn.textContent = 'המשך מסע';
            pauseTime = performance.now() - startTime; // Record elapsed time
            cancelAnimationFrame(animation);
            animation = null; // Clear animation frame ID
        }
    });

    resetBtn.addEventListener('click', () => {
        cancelAnimationFrame(animation);
        animation = null;
        animationPaused = false;
        startTime = null;
        pauseTime = 0;
        animationProgress = 0;
        currentPath = 'forward';

        // Reset eel state
        eel.setAttribute('cx', '100');
        eel.setAttribute('cy', '300');
        eel.setAttribute('fill', 'yellow');
        eel.setAttribute('r', 8);
        eel.style.transform = 'rotate(90deg)'; // Reset initial rotation

        // Reset path drawing visual state
        forwardPath.style.strokeDashoffset = pathLengthForward;
        returnPath.style.strokeDashoffset = returnPath.getTotalLength();


        playPauseBtn.textContent = 'התחל מסע'; // Reset button text
        updateInfoBox("לחצו על 'התחל מסע' כדי לראות את מסע הצלופח המופלא. ניתן גם ללחוץ על הסימנים הצבעוניים במסלול למידע נוסף.");
    });

    // Toggle explanation visibility
    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מפורט' : 'הצג הסבר מפורט';
         // Scroll to the explanation if showing it
         if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });

    // Update info box
    function updateInfoBox(text) {
        infoBox.innerHTML = text; // Use innerHTML to support simple formatting like <br>
    }

    // Add click listeners to stage markers
    stageMarkers.forEach(marker => {
        marker.addEventListener('click', () => {
            const info = marker.getAttribute('data-info');
            updateInfoBox("<h4>מידע על שלב זה:</h4>" + info); // Use heading for marker info
             // Optionally pause animation when clicking a marker
            if (animation && !animationPaused) {
                playPauseBtn.click(); // Simulate click to pause
            }
        });
    });

    // Add click listener to the eel itself
    eel.addEventListener('click', () => {
         // Display current stage info or a prompt
        if (animation || animationPaused) {
            // If animation is running or paused, the info box likely shows current stage info.
            // Let's ensure it's visible and maybe re-iterate.
             if (infoBox.textContent) {
                 // Just make sure it's prominent or briefly highlight the info box?
                 // For now, clicking eel when active does nothing extra as info is updated dynamically.
             } else {
                 updateInfoBox("המסע מתקדם... עקבו אחר הצלופח והמידע המופיע.");
             }
        } else {
             // If not started, show initial prompt
             updateInfoBox("לחצו על 'התחל מסע' כדי להתחיל! לחצו על הסימנים הצבעוניים למסלול.");
        }
    });

    // Handle initial state
    resetBtn.click(); // Initialize button text and info box

</script>
```