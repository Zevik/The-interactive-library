---
title: "מסע בתוך ענן סערה: כך נוצר ברד"
english_slug: journey-inside-storm-cloud-hail-formation
category: "מדעי האטמוספרה"
tags: [ברד, סופת רעמים, ענן סערה, מזג אוויר קיצוני, היווצרות משקעים]
---
# מסע בתוך ענן סערה: כך נוצר ברד

האם יצא לכם פעם לראות כדורי קרח נופלים מהשמיים בזמן סערה? זהו ברד! איך נוצרות חתיכות קרח כאלה, שלעיתים מגיעות לגודל של אבן או אפילו כדור טניס, דווקא בענן סערה גשום וחם יחסית בחלקו התחתון? ואיך הן מצליחות לשרוד את המסע הארוך מהפסגות הקפואות של הענן ועד לקרקע החמה בלי להפשיר?

הצטרפו למסע וירטואלי בתוך ענן סערה אימתני וגלו את סוד היווצרות הברד בסימולציה אינטראקטיבית:

<div class="hail-simulation-container">
    <div class="cloud-representation">
        <div class="cloud cloud-bottom"></div>
        <div class="cloud cloud-middle"></div>
        <div class="cloud cloud-top"></div>
        <div class="updraft-indicator">↑ זרם אוויר עולה</div>
        <div class="downdraft-indicator">↓ נפילה</div>
        <div class="freezing-level">רום הקיפאון (0°C)</div>
        <div class="hailstone">
            <div class="hail-core"></div>
            <div class="hail-layer layer-1"></div>
            <div class="hail-layer layer-2"></div>
            <div class="hail-layer layer-3"></div>
            <div class="hail-layer layer-4"></div>
            <div class="hail-layer layer-5"></div>
        </div>
        <div class="region-label base">בסיס הענן</div>
        <div class="region-label top">פסגת הענן</div>
    </div>
    <div class="controls">
        <button id="start-simulation">התחל מסע בענן</button>
        <div class="status">
            <span class="status-item">גודל: <span id="hail-size-display">טיפה ראשונית</span></span>
            <span class="status-item">שכבות קרח: <span id="hail-layers-display">0</span></span>
            <span class="status-item">גובה (משוער): <span id="hail-altitude-display">0</span> מ'</span>
             <span class="status-item velocity">מהירות אנכית: <span id="hail-speed-display">0</span> מ'/שניה</span>
        </div>
    </div>
</div>

<button id="show-explanation">מה באמת קורה שם למעלה? הצג הסבר מפורט</button>

<div id="explanation" style="display: none;">
    <h2>מהו ברד ומה מבדיל אותו ממשקעים אחרים?</h2>
    <p>ברד הוא צורת משקע ייחודית, המורכבת מגושי קרח או כדורי קרח מוצקים הנקראים "אבני ברד". בניגוד לגשם (טיפות מים), שלג (גבישי קרח קלים) או גשם קופא (גשם שקופא במגע עם משטח קפוא), הברד נוצר וגדל רק בתוך ליבת ענני סערה עצומים ועוצמתיים במיוחד מסוג קומולונימבוס.</p>

    <h2>הזירה: ענן סערה (קומולונימבוס)</h2>
    <p>אבני הברד נולדות וגדלות בענני קומולונימבוס, שיכולים להתנשא לגבהים אדירים – עשרות קילומטרים! בתוך הענן העצום הזה שוררים תנאים קיצוניים: בחלקו התחתון טמפרטורות מעל האפס, בחלקו האמצעי (מעל רום הקיפאון) טמפרטורות עמוק מתחת לאפס אך עדיין עם הרבה טיפות מים "סופר קפואות" (נוזליות בטמפרטורות שליליות), ובפסגות הקפואות ביותר גבישי קרח וטמפרטורות קיצוניות.</p>

    <h2>השחקנים המרכזיים בתהליך:</h2>
    <ul>
        <li>**זרמי אוויר עולים (Updrafts):** אלו הם "מעליות" טבעיות חזקות במיוחד בתוך הענן, הנושאות אוויר חם ולח מהקרקע כלפי מעלה. זרמים אלה הם הכוח המניע ששומר את אבני הברד המתפתחות בתוך הענן, מאפשר להן לעלות שוב ושוב לאזורים הקפואים ולצבור עוד קרח. ככל שהזרמים חזקים יותר, כך הברד יכול לגדול לגדלים מרשימים יותר.</li>
        <li>**רום הקיפאון (0°C Level):** הגובה שבו הטמפרטורה יורדת מתחת לאפס מעלות צלזיוס. כל מה שמעליו הוא אזור פוטנציאלי לצמיחת קרח.</li>
        <li>**טיפות מים סופר קפואות (Supercooled Water Droplets):** אלו טיפות מים שנשארו במצב נוזלי גם בטמפרטורות עמוק מתחת לאפס. הן המפתח לצמיחת הברד: כשאבן ברד מתנגשת בהן, הן קופאות באופן מיידי במגע ו"נדבקות" אליה, וכך מוסיפות עוד שכבת קרח.</li>
        <li>**גבישי קרח:** קיימים בחלקים הקפואים של הענן וגם הם יכולים להיאסף על הברד הגדל.</li>
    </ul>

    <h2>כוריאוגרפיית הריקוד הקטלני של הברד - שלב אחר שלב:</h2>
    <ol>
        <li>**התחלה קטנה:** הכל מתחיל עם גרגר קרח קטן או אפילו טיפת מים קפואה בתחתית או אמצע הענן.</li>
        <li>**עלייה ראשונה:** זרם אוויר עולה חזק לוכד את הגרגר הקטן ונושא אותו כלפי מעלה אל מעבר לרום הקיפאון.</li>
        <li>**מפגשים קפואים וצמיחה:** באזור הקר (במיוחד היכן שיש טיפות מים סופר קפואות רבות), הגרגר מתנגש בטיפות הללו ובגבישי קרח אחרים. המים הסופר קפואים קופאים עליו מיד, וגורמים לו לגדול ולצבור שכבה חדשה של קרח. תהליך זה נקרא צבירה (Accretion).</li>
        <li>**נפילה זמנית:** כשהברד צובר מספיק קרח והופך כבד יותר, כוח הכבידה גובר על זרם האוויר העולה והוא מתחיל ליפול בחזרה לכיוון תחתית הענן.</li>
        <li>**לכידה מחדש ומסע חוזר:** אם הברד לא נופל אל מחוץ לענן לחלוטין, הוא עלול להילכד מחדש על ידי זרם אוויר עולה אחר, או על ידי חלק חזק יותר באותו זרם, ולהישלח שוב כלפי מעלה.</li>
        <li>**הריקוד נמשך (מחזורים):** הברד חוזר על מחזורי עלייה, צבירת קרח באזורים הקפואים, ונפילה, שוב ושוב. כל "ריצה" כזו כלפי מעלה מוסיפה לו עוד שכבת קרח. אבן ברד גדולה שתחתכו לשניים תראה לרוב מבנה שכבתי, כמו "בצל", עדות למסעות הרבים שלה בתוך הענן.</li>
        <li>**הנפילה הגורלית:** אבן הברד ממשיכה לגדול ולהתכבד עד שהיא הופכת כבדה מדי אפילו עבור זרמי האוויר העולים החזקים ביותר בענן. בשלב זה, היא נופלת מחוץ לענן אל הקרקע. אם הטמפרטורות בדרכה למטה חמות מספיק, חלק ממנה עלול להפשיר, אך אבני ברד גדולות מספיק ישמרו על צורתן המוצקה עד לפגיעה בקרקע.</li>
    </ol>

    <h2>ככל שהסערה חזקה יותר, כך הברד גדול יותר!</h2>
    <p>גודלה הסופי של אבן הברד תלוי בעיקר בעוצמתם ומשכם של זרמי האוויר העולים. סופות רעמים עם זרמים עולים חזקים במיוחד, כמו בסופות "סופר-סל", יכולות להחזיק אבני ברד גדולות בתוך הענן לזמן ארוך יותר, לאפשר להן לצבור יותר קרח ולייצר ברד ענק שיכול לגרום לנזק רב.</p>
</div>

<style>
    /* Overall Container and Layout */
    .hail-simulation-container {
        width: 100%;
        max-width: 650px; /* Slightly wider */
        margin: 20px auto;
        border: 2px solid #333; /* Darker border */
        border-radius: 12px; /* More rounded corners */
        overflow: hidden;
        position: relative;
        background: linear-gradient(to bottom, #6E9ECF, #A2D2FF); /* Deeper sky blue */
        font-family: 'Arial', sans-serif; /* Clearer font */
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2); /* Add shadow */
    }

    /* Cloud Representation Area */
    .cloud-representation {
        width: 100%;
        height: 500px; /* Taller cloud */
        position: relative;
        background: linear-gradient(to top, rgba(255, 255, 255, 0.9) 0%, rgba(255, 255, 255, 0.6) 50%, rgba(255, 255, 255, 0.2) 100%); /* More distinct cloud fade */
        overflow: hidden; /* Keep elements inside */
    }

     /* Cloud Background Elements (for visual depth) */
    .cloud {
        position: absolute;
        left: 0;
        width: 100%;
        background: rgba(255, 255, 255, 0.8);
        border-radius: 50% / 10%; /* Elipse shape */
        filter: blur(15px); /* Soft blur */
        opacity: 0.7;
        z-index: 1;
    }

    .cloud-bottom {
        bottom: -50px; /* Position below base line */
        height: 150px;
        width: 120%; /* Wider than container */
        left: -10%;
        animation: cloudDrift 30s infinite linear; /* Subtle movement */
    }

    .cloud-middle {
        bottom: 150px; /* Higher up */
        height: 180px;
        width: 110%;
         left: -5%;
        animation: cloudDrift 35s infinite linear reverse; /* Opposite direction */
    }

     .cloud-top {
        top: -80px; /* Above top line */
        height: 200px;
        width: 100%;
        animation: cloudDrift 40s infinite linear;
    }

    @keyframes cloudDrift {
        0% { transform: translateX(0); }
        50% { transform: translateX(20px); }
        100% { transform: translateX(0); }
    }


    /* Region Labels */
    .region-label {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        width: 100%;
        text-align: center;
        font-size: 0.9em;
        color: #333;
        text-shadow: 0 0 3px rgba(255,255,255,0.5); /* Add text shadow */
        z-index: 5; /* Above clouds */
    }

    .region-label.base {
        bottom: 15px; /* Above cloud-base visual line */
    }

     .region-label.top {
        top: 15px; /* Below cloud-top visual line */
     }


    .freezing-level {
        position: absolute;
        left: 0;
        width: 100%;
        text-align: center;
        font-size: 0.9em;
        padding: 4px 0;
        box-sizing: border-box;
        bottom: 50%; /* Example: Freezing level in the middle */
        border-bottom: 2px dashed #00aaff; /* Brighter blue dashed line */
        color: #00aaff; /* Brighter blue text */
        background-color: rgba(173, 216, 230, 0.2); /* Lighter, more transparent blue */
        z-index: 5; /* Above clouds */
        text-shadow: 0 0 3px rgba(255,255,255,0.5);
    }

    /* Hailstone Styling */
    .hailstone {
        position: absolute;
        width: 10px;
        height: 10px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 10; /* Above everything else */
        box-sizing: border-box;
        border-radius: 50%;
        background-color: rgba(255, 255, 255, 0.9); /* White with some transparency */
        border: 1px solid rgba(0, 0, 0, 0.3); /* Subtle dark border */
        transition: width 0.2s ease-out, height 0.2s ease-out; /* Smooth size transition */
        display: flex; /* Use flex to center layers */
        justify-content: center;
        align-items: center;
        filter: drop-shadow(0 0 2px rgba(0,0,0,0.2)); /* Small shadow */
    }

    /* Inner layers visual */
    .hail-core {
         width: 50%; height: 50%; border-radius: 50%; background-color: rgba(200, 200, 200, 0.8);
         position: absolute; opacity: 0; transition: opacity 0.3s ease;
    }
     .hail-layer {
        position: absolute;
        border-radius: 50%;
        border: 1px solid rgba(255, 255, 255, 0.5);
        box-sizing: border-box;
        opacity: 0;
        transition: opacity 0.3s ease, width 0.2s ease, height 0.2s ease;
     }

     .hailstone.has-core .hail-core { opacity: 1; }
     .hailstone.layer-1 .hail-layer.layer-1 { opacity: 1; width: 60%; height: 60%; border-color: rgba(220, 220, 220, 0.6); }
     .hailstone.layer-2 .hail-layer.layer-2 { opacity: 1; width: 70%; height: 70%; border-color: rgba(200, 200, 200, 0.7); }
     .hailstone.layer-3 .hail-layer.layer-3 { opacity: 1; width: 80%; height: 80%; border-color: rgba(180, 180, 180, 0.8); }
     .hailstone.layer-4 .hail-layer.layer-4 { opacity: 1; width: 90%; height: 90%; border-color: rgba(160, 160, 160, 0.9); }
     .hailstone.layer-5 .hail-layer.layer-5 { opacity: 1; width: 100%; height: 100%; border-color: rgba(140, 140, 140, 1); }
     /* Add more layers if JS allows > 5 */


    /* Force Indicators */
    .updraft-indicator, .downdraft-indicator {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        font-size: 0.8em;
        font-weight: bold;
        padding: 2px 5px;
        border-radius: 4px;
        opacity: 0;
        transition: opacity 0.3s ease-out;
        z-index: 8; /* Below hailstone */
    }

    .updraft-indicator {
        bottom: 20%; /* Example position */
        color: #1a7a00; /* Green */
        background-color: rgba(144, 238, 144, 0.5); /* Light green */
    }

     .downdraft-indicator {
        top: 20%; /* Example position */
        color: #cc0000; /* Red */
        background-color: rgba(250, 128, 114, 0.5); /* Light coral */
     }


    /* Controls and Status */
    .controls {
        padding: 15px;
        text-align: center;
        background-color: #e0f0ff; /* Very light blue */
        border-top: 1px solid #b0c4de; /* Lighter border */
        display: flex; /* Use flexbox */
        flex-direction: column; /* Stack items */
        align-items: center;
    }

    .controls button {
        padding: 12px 25px; /* Larger button */
        font-size: 1.1em;
        cursor: pointer;
        margin-bottom: 15px;
        background-color: #007bff; /* Primary blue */
        color: white;
        border: none;
        border-radius: 6px; /* More rounded */
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3); /* Button shadow */
    }

    .controls button:hover:not(:disabled) {
        background-color: #0056b3; /* Darker blue on hover */
    }

     .controls button:active:not(:disabled) {
        transform: scale(0.98); /* Press effect */
     }

     .controls button:disabled {
        background-color: #cccccc; /* Grey out when disabled */
        cursor: not-allowed;
        box-shadow: none;
     }

    .status {
        font-size: 0.95em;
        color: #333; /* Darker text */
        display: flex; /* Arrange status items in a row */
        justify-content: center; /* Center items */
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
    }

    .status-item {
        margin: 0 10px; /* Spacing between items */
         white-space: nowrap; /* Prevent breaking lines within an item */
    }

    .status-item span {
        font-weight: bold; /* Make values stand out */
        color: #004085; /* Dark blue for values */
    }

     .status-item.velocity span {
        color: #28a745; /* Green for velocity */
     }

    /* Explanation Button */
    #show-explanation {
        display: block;
        margin: 20px auto;
        padding: 12px 20px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #28a745; /* Green button */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(40, 167, 69, 0.3);
    }

    #show-explanation:hover {
         background-color: #218838;
    }
     #show-explanation:active {
        transform: scale(0.98);
     }


    /* Explanation Section */
    #explanation {
        margin: 20px auto;
        max-width: 650px; /* Match container width */
        padding: 25px; /* More padding */
        border: 1px solid #d6eaff; /* Light blue border */
        border-radius: 12px;
        background-color: #eef7ff; /* Very light blue background */
        line-height: 1.7; /* Improved readability */
        color: #333;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }

    #explanation h2 {
        color: #0056b3; /* Darker blue */
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 2px solid #b0c4de; /* Matching border color */
        padding-bottom: 6px;
        font-size: 1.4em;
    }

     #explanation h2:first-child {
         margin-top: 0;
     }

    #explanation p, #explanation ul, #explanation ol {
        margin-bottom: 18px;
        font-size: 1em;
    }

    #explanation ul, #explanation ol {
        padding-left: 20px; /* Indent lists */
    }

    #explanation li {
        margin-bottom: 8px;
    }

     #explanation strong {
         color: #004085; /* Highlight key terms */
     }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const hailstone = document.querySelector('.hailstone');
        const cloudRepresentation = document.querySelector('.cloud-representation');
        const freezingLevelElement = document.querySelector('.freezing-level');
        const regionBaseElement = document.querySelector('.region-label.base');
        const regionTopElement = document.querySelector('.region-label.top');
        const startButton = document.getElementById('start-simulation');
        const showExplanationButton = document.getElementById('show-explanation');
        const explanationDiv = document.getElementById('explanation');
        const hailSizeDisplay = document.getElementById('hail-size-display');
        const hailLayersDisplay = document.getElementById('hail-layers-display');
        const hailAltitudeDisplay = document.getElementById('hail-altitude-display');
        const hailSpeedDisplay = document.getElementById('hail-speed-display');
        const updraftIndicator = document.querySelector('.updraft-indicator');
        const downdraftIndicator = document.querySelector('.downdraft-indicator');
        const hailCore = document.querySelector('.hail-core');
        const hailLayers = document.querySelectorAll('.hail-layer');


        let animationFrameId = null;
        let isSimulating = false;
        let startTime = null;

        // Simulation parameters
        const cloudHeightPx = 500; // Matches CSS height of .cloud-representation
        const cloudAltitudeScale = 15000; // Max meters for altitude display (~ Top of Cumulonimbus)
        const groundAltitude = 0; // Meters
        const freezingLevelAltitude = cloudAltitudeScale * 0.5; // Example: Freezing level is halfway up the scaled altitude
        const cloudBaseAltitude = cloudAltitudeScale * 0.1; // Example: Cloud base is 10% up scaled altitude

        // Positions relative to the bottom of .cloud-representation (yPx = 0 at bottom)
        // These will be calculated based on the displayed elements' positions
        let cloudBaseYPx = 0;
        let cloudTopYPx = cloudHeightPx;
        let freezingLevelYPx = 0;

        // Conversion factor for visual pixels to simulated meters
        let pxToMeter = 1; // Will be calculated

        let hailstoneData = {
            yPx: 0, // Distance from the bottom of cloudRepresentation (pixels)
            yMeter: 0, // Simulated altitude (meters)
            verticalSpeedPx: 0, // pixels per frame
            verticalSpeedMeterPerSec: 0, // simulated m/s
            horizontalOffsetPx: 0, // px from center
            sizePx: 10, // px, current visual size
            simulatedMass: 0.1, // kg (arbitrary starting mass)
            layers: 0,
            isGrowing: false,
            timeInColdZone: 0 // time steps
        };

        // Physics Constants (tuned for visual simulation)
        const GRAVITY_PX_PER_FRAME = 0.05; // Base gravity acceleration (pixels per frame^2)
        const DRAG_COEFFICIENT = 0.0005; // Affects drag force
        const BASE_UPDRAFT_PX_PER_FRAME = 0.5; // Base updraft strength at cloud base
        const UPDRAFT_DECAY_RATE = 1.5; // How fast updraft weakens with height (higher number means faster decay)
        const STORM_INTENSITY = 1.2; // Multiplier for overall storm strength (updraft, growth chance)
        const GROWTH_PROBABILITY_PER_FRAME = 0.02; // Base chance to grow per frame in cold zone
        const MAX_HAIL_LAYERS = 5; // Cap visual layers

        // Function to calculate positions based on rendered elements
        const calculatePositions = () => {
             const containerRect = cloudRepresentation.getBoundingClientRect();
             const baseRect = regionBaseElement.getBoundingClientRect();
             const topRect = regionTopElement.getBoundingClientRect();
             const freezingRect = freezingLevelElement.getBoundingClientRect();

             // Calculate Y position (distance from the bottom of the cloudRepresentation div)
             // Note: getBoundingClientRect().bottom is distance from *viewport* top to element's bottom.
             // containerRect.bottom - baseRect.top gives distance from container bottom to base top line.
             cloudBaseYPx = containerRect.bottom - baseRect.top;
             cloudTopYPx = containerRect.bottom - topRect.bottom; // Distance from container bottom to top region bottom line
             freezingLevelYPx = containerRect.bottom - freezingRect.bottom; // Distance from container bottom to freezing line

             // Calculate px to meter scaling based on the total active simulation height
             const simulatableHeightPx = cloudTopYPx - cloudBaseYPx;
             const simulatableHeightMeter = cloudAltitudeScale - cloudBaseAltitude;
             pxToMeter = simulatableHeightMeter / simulatableHeightPx;

             // Adjust initial hailstone Y position based on calculated cloudBaseYPx
             if (!isSimulating) { // Only adjust initial position if not already running
                 hailstoneData.yPx = cloudBaseYPx + hailstoneData.sizePx / 2; // Start just above base
             }
        };


        // --- Simulation Logic ---
        function updateSimulation(currentTime) {
            if (!isSimulating) return;

            if (!startTime) startTime = currentTime;
            const elapsed = currentTime - startTime; // Total time elapsed since start (ms)
            const deltaTime = (currentTime - (hailstoneData._lastTime || currentTime)) / 1000; // Time elapsed since last frame (seconds)
             hailstoneData._lastTime = currentTime; // Store current time

             // Prevent physics glitches with very large delta times (e.g., tab switching)
             if (deltaTime > 0.1) {
                 animationFrameId = requestAnimationFrame(updateSimulation);
                 return;
             }


            // Convert pixel speed to meters per second for display
            hailstoneData.verticalSpeedMeterPerSec = (hailstoneData.verticalSpeedPx / (cloudHeightPx)) * cloudAltitudeScale / deltaTime ; // Simplified scaling

            // --- Simulate Forces (simplified physics) ---
            let netForcePx = 0; // Net force in pixels/frame^2 (acceleration)

            // Gravity: Constant downwards force
            const gravityForcePx = GRAVITY_PX_PER_FRAME * hailstoneData.simulatedMass;
            netForcePx -= gravityForcePx; // Gravity acts downwards (decreasing yPx)

            // Updraft Force: Strongest at base, weakens with height
            const heightAboveBasePx = hailstoneData.yPx - cloudBaseYPx;
            const simulatableHeightPx = cloudTopYPx - cloudBaseYPx;
            const heightRatio = Math.max(0, Math.min(1, heightAboveBasePx / simulatableHeightPx)); // Ratio from cloud base (0) to cloud top (1)

            // Updraft calculation: Base strength * decay with height * storm intensity
            const updraftStrengthPx = BASE_UPDRAFT_PX_PER_FRAME * Math.pow((1 - heightRatio), UPDRAFT_DECAY_RATE) * STORM_INTENSITY;

            // Apply updraft, reduced slightly by hailstone mass
            const massInfluence = Math.min(0.5, hailstoneData.simulatedMass / 5); // More massive stones less affected
            const effectiveUpdraft = updraftStrengthPx * (1 - massInfluence);
            netForcePx += effectiveUpdraft; // Updraft acts upwards (increasing yPx)

            // Drag Force: Opposes velocity, proportional to speed^2 and size/mass
            const dragForcePx = DRAG_COEFFICIENT * hailstoneData.sizePx * hailstoneData.verticalSpeedPx * Math.abs(hailstoneData.verticalSpeedPx); // Simple drag
            netForcePx -= dragForcePx; // Drag opposes current motion


            // --- Update Velocity and Position ---
            hailstoneData.verticalSpeedPx += netForcePx; // Apply acceleration
            hailstoneData.yPx += hailstoneData.verticalSpeedPx; // Update position

            // Simulate horizontal drift (random walk)
            const randomHorizontalForce = (Math.random() - 0.5) * 0.5; // Smaller random steps
            hailstoneData.horizontalOffsetPx += randomHorizontalForce;
            const maxHorizontalOffset = (cloudRepresentation.offsetWidth - hailstoneData.sizePx) / 2 - 5; // Prevent stone from touching edges
            hailstoneData.horizontalOffsetPx = Math.max(-maxHorizontalOffset, Math.min(maxHorizontalOffset, hailstoneData.horizontalOffsetPx));


            // --- Boundaries and Interactions ---

            // Check if above freezing level
            const isAboveFreezing = hailstoneData.yPx > freezingLevelYPx;

            // Growth Logic: Accretion in the cold zone
            if (isAboveFreezing) {
                hailstoneData.isGrowing = true;
                hailstoneData.timeInColdZone++; // Track time in cold zone

                // Increased chance to grow based on vertical speed and time in cold zone
                const speedFactor = Math.max(0, Math.min(2, Math.abs(hailstoneData.verticalSpeedPx) * 0.5)); // Faster means more collisions
                const timeFactor = Math.min(1, hailstoneData.timeInColdZone / 500); // Longer time increases chance slightly
                const growthChance = GROWTH_PROBABILITY_PER_FRAME * STORM_INTENSITY * (1 + speedFactor + timeFactor);

                if (Math.random() < growthChance) {
                     if (hailstoneData.layers < MAX_HAIL_LAYERS) { // Cap visual layers
                        hailstoneData.layers++;
                        const sizeIncrease = 4 + hailstoneData.layers * 0.5; // Size increases slightly more with layers
                        hailstoneData.sizePx += sizeIncrease;
                        hailstoneData.simulatedMass += 0.5 + hailstoneData.layers * 0.1; // Mass increases
                        // Add visual layer class (handled below)
                    } else {
                         // Stone still grows, but visually capped
                         hailstoneData.sizePx += 2;
                         hailstoneData.simulatedMass += 0.3;
                    }
                }

            } else {
                 hailstoneData.isGrowing = false;
                 hailstoneData.timeInColdZone = 0; // Reset time tracker
            }


            // Check if falling out of cloud base (below cloud base line and moving down)
            if (hailstoneData.yPx < cloudBaseYPx && hailstoneData.verticalSpeedPx < 0) {
                 endSimulation();
            } else if (hailstoneData.yPx < cloudBaseYPx) {
                 // Prevent falling below base if moving upwards (simulating updraft keeping it just above)
                 hailstoneData.yPx = cloudBaseYPx;
                 if (hailstoneData.verticalSpeedPx < 0) hailstoneData.verticalSpeedPx = 0; // Stop downwards movement at base
             }


             // Prevent going above cloud top
             if (hailstoneData.yPx > cloudTopYPx) {
                 hailstoneData.yPx = cloudTopYPx;
                 hailstoneData.verticalSpeedPx *= -0.6; // Bounce off top, lose some speed
             }


            // --- Update Visuals ---
            // yPx is distance from bottom of container to the center of the hailstone
            hailstone.style.bottom = (hailstoneData.yPx - hailstone.offsetHeight / 2) + 'px';
            hailstone.style.left = `calc(50% + ${hailstoneData.horizontalOffsetPx}px)`;
            hailstone.style.width = hailstone.style.height = hailstoneData.sizePx + 'px';


            // Update visual layers
             if (hailstoneData.layers > 0) {
                hailstone.classList.add('has-core');
             } else {
                hailstone.classList.remove('has-core');
             }
             hailLayers.forEach((layer, index) => {
                if (index < hailstoneData.layers) {
                    layer.style.opacity = 1;
                     // Adjust size slightly to fit within the outer circle as it grows
                     const layerSizeRatio = 1 - (hailstoneData.layers - index - 1) * 0.15; // Smaller layers inside
                     layer.style.width = layer.style.height = `${layerSizeRatio * 100}%`;
                } else {
                    layer.style.opacity = 0;
                }
             });


            // Update Force Indicators (show briefly when relevant)
            updraftIndicator.style.opacity = (hailstoneData.verticalSpeedPx > 0.1 && netForcePx > 0) ? 1 : 0;
            downdraftIndicator.style.opacity = (hailstoneData.verticalSpeedPx < -0.1 && netForcePx < 0) ? 1 : 0;
             // Position indicators near the hailstone (relative to cloud representation)
             const hailstoneBottomPx = parseFloat(hailstone.style.bottom);
             updraftIndicator.style.bottom = `${hailstoneBottomPx + hailstoneData.sizePx / 2 + 20}px`; // Above hailstone
             downdraftIndicator.style.bottom = `${hailstoneBottomPx - hailstoneData.sizePx / 2 - 20}px`; // Below hailstone


            // Update status display
             // Estimate altitude based on yPx relative to cloud base/top
             const currentHeightInCloudPx = hailstoneData.yPx - cloudBaseYPx;
             const simulatableHeightPx = cloudTopYPx - cloudBaseYPx;
             const heightRatio = Math.max(0, currentHeightInCloudPx / simulatableHeightPx);
             hailstoneData.yMeter = cloudBaseAltitude + (heightRatio * (cloudAltitudeScale - cloudBaseAltitude));


            hailSizeDisplay.textContent = `${Math.round(hailstoneData.sizePx)}px (${(hailstoneData.simulatedMass * 1000).toFixed(0)}g)`; // Show size in px and estimated grams
            hailLayersDisplay.textContent = hailstoneData.layers;
             hailAltitudeDisplay.textContent = Math.round(hailstoneData.yMeter);
             hailSpeedDisplay.textContent = (hailstoneData.verticalSpeedMeterPerSec).toFixed(1); // Display speed in m/s


            // Continue animation loop
            animationFrameId = requestAnimationFrame(updateSimulation);
        }

        function startSimulation() {
            if (isSimulating) return;

            // Recalculate positions in case container size changed (unlikely but safe)
            calculatePositions();

            // Reset state
            hailstoneData = {
                yPx: cloudBaseYPx + 5, // Start just above base line
                yMeter: cloudBaseAltitude,
                verticalSpeedPx: 0,
                verticalSpeedMeterPerSec: 0,
                horizontalOffsetPx: 0,
                sizePx: 10, // Start size
                simulatedMass: 0.1, // Start mass
                layers: 0,
                isGrowing: false,
                timeInColdZone: 0,
                _lastTime: performance.now() // Initialize time for delta time calculation
            };
             startTime = null; // Reset start time for accurate elapsed calculation

             // Reset visual
             hailstone.style.width = hailstone.style.height = hailstoneData.sizePx + 'px';
             hailstone.style.bottom = (hailstoneData.yPx - hailstone.offsetHeight / 2) + 'px'; // Position based on yPx from bottom
             hailstone.style.left = '50%';
             hailstone.className = 'hailstone'; // Reset classes
             hailLayers.forEach(layer => layer.style.opacity = 0);
             hailCore.style.opacity = 0;
             updraftIndicator.style.opacity = 0;
             downdraftIndicator.style.opacity = 0;


             // Reset status
             hailSizeDisplay.textContent = 'טיפה ראשונית';
             hailLayersDisplay.textContent = '0';
             hailAltitudeDisplay.textContent = Math.round(hailstoneData.yMeter);
             hailSpeedDisplay.textContent = '0.0';


            isSimulating = true;
            startButton.textContent = 'המסע בעיצומו...';
            startButton.disabled = true;

            animationFrameId = requestAnimationFrame(updateSimulation);
        }

        function endSimulation() {
             if (!isSimulating) return;
            isSimulating = false;
            cancelAnimationFrame(animationFrameId);
            startButton.textContent = 'התחל מסע חדש';
            startButton.disabled = false;

             // Final status update
             hailSizeDisplay.textContent = `${Math.round(hailstoneData.sizePx)}px (${(hailstoneData.simulatedMass * 1000).toFixed(0)}g) - הגיע לקרקע!`;
             hailAltitudeDisplay.textContent = 'קרקע';
             hailSpeedDisplay.textContent = hailstoneData.verticalSpeedMeterPerSec.toFixed(1); // Show final speed

             updraftIndicator.style.opacity = 0; // Hide indicators
             downdraftIndicator.style.opacity = 0;

        }

        // --- Event Listeners ---
        startButton.addEventListener('click', startSimulation);

        showExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            showExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'מה באמת קורה שם למעלה? הצג הסבר מפורט';
        });

         // Initial setup - calculate positions once DOM is ready and positioned
         // Use requestAnimationFrame to ensure elements are rendered before calculating positions
         requestAnimationFrame(() => {
            calculatePositions();
             // Set initial visual position based on calculated yPx for the starting point
             hailstoneData.yPx = cloudBaseYPx + hailstoneData.sizePx / 2; // Position at start height (just above base)
             hailstone.style.bottom = (hailstoneData.yPx - hailstone.offsetHeight / 2) + 'px'; // Set visual bottom property

             // Set initial status display correctly
             hailAltitudeDisplay.textContent = Math.round(cloudBaseAltitude); // Display base altitude initially

         });


         // Optional: Recalculate positions if window resizes (less critical in embedded content, but good practice)
         // window.addEventListener('resize', calculatePositions); // Disabled for simplicity as container is fixed size

    });
</script>
---