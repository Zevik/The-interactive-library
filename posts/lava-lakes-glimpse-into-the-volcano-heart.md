---
title: "אגמי לבה: הצצה אל לב ההר הגעשי הלוהט"
english_slug: lava-lakes-glimpse-into-the-volcano-heart
category: "מדעי הסביבה / כדור הארץ"
tags:
  - הרי געש
  - לבה
  - אגמי לבה
  - גיאולוגיה
  - מאגמה
  - סימולציה
---
# אגמי לבה: הצצה אל לב ההר הגעשי הלוהט

דמיינו את לוע הר געש. בדרך כלל, הוא נראה קפוא, פה שחור של סלע מוקשה. אבל בהרי געש נדירים במיוחד ברחבי העולם, תוכלו להציץ פנימה ולגלות מראה מהפנט ומסוכן כאחד: אגם ענק של לבה מבעבעת ולוהטת, שנשאר במצבו הנוזלי הקיצוני לאורך חודשים ואפילו שנים רבות. כיצד נשמר גוף לוהט כזה, חשוף יחסית לסביבה הקרה, מבלי להתקרר ולהתקשות? הצטרפו למסע אל המעמקים וגלו את הסוד.

## אתגר הסימולציה: צור ושמר על אגם לבה יציב!

האם תוכלו לשלוט בכוחות הפועלים בבטן ההר הגעשי ולמצוא את האיזון הנכון שיאפשר לאגם הלבה להתקיים לאורך זמן? התנסו בשליטה על הגורמים המכריעים – זרימת המאגמה מהמעמקים והבידוד של פני השטח – וראו בזמן אמת כיצד ההחלטות שלכם משפיעות על מפלס הלבה וטמפרטורה שלה. המטרה: להגיע למצב של אגם לבה יציב ופעיל ולשמור עליו ככל הניתן!

<div class="simulation-container">
    <div class="controls">
        <div class="control-group">
            <h3>קצב אספקת מאגמה מהמעמקים:</h3>
            <label><input type="radio" name="magmaFlow" value="low"> זרזיף (נמוך)</label><br>
            <label><input type="radio" name="magmaFlow" value="medium" checked> זרימה (בינוני)</label><br>
            <label><input type="radio" name="magmaFlow" value="high"> שיטפון (גבוה)</label>
        </div>
        <div class="control-group">
            <h3>בידוד פני שטח הלבה:</h3>
            <label><input type="radio" name="surfaceInsulation" value="low"> קרום דק (בידוד נמוך)</label><br>
            <label><input type="radio" name="surfaceInsulation" value="high" checked> קרום עבה ויציב (בידוד גבוה)</label>
        </div>
    </div>
    <div class="volcano-throat">
        <div class="lava-lake"></div>
        <div class="lava-surface-effect"></div> <!-- Added for animations -->
    </div>
    <div class="status">
        <p>מפלס הלבה: <span id="lavaLevelText">0%</span></p>
        <p>טמפרטורה: <span id="lavaTempText">0°C</span></p>
        <p>מצב האגם: <span id="simulationStatus">ממתין...</span></p>
        <p>זמן יציבות רצוף: <span id="stableTimerText">0</span> שניות</p> <!-- Added timer -->
    </div>
</div>

<button id="toggleExplanation">הצג את הסוד מאחורי אגמי הלבה</button>

<div id="explanation" style="display: none;">
    <h2>מה הופך אגם לבה למיוחד כל כך?</h2>
    <p>אגם לבה הוא תופעה גיאולוגית נדירה: גוף גדול של לבה מותכת (בדרך כלל סוג בזלתי דליל יחסית), שמתמקם בתוך לוע הר געש או שקע דומה. בניגוד לרוב זרמי הלבה שמתקררים ומתקשים במהירות, אגמים אלו מצליחים להישאר במצב נוזלי ולוהט לאורך תקופות ארוכות, לפעמים שנים! דמיינו בריכה ענקית מלאה בסלע נוזלי בטמפרטורות של מעל 1000°C.</p>

    <h2>היכן ניתן למצוא פלאים כאלה?</h2>
    <p>רק קומץ קטן של הרי געש בעולם מסוגלים לקיים אגמי לבה יציבים. הדבר דורש שילוב מדויק של תנאים. בין המקומות המפורסמים שבהם נצפו או נצפים אגמי לבה: הר ארטה אלה האגדי באתיופיה, הרי הגעש הפעילים בהוואי (כמו קילוואה בעבר), הר נייראגונגו ברפובליקה הדמוקרטית של קונגו, והר ארבוס האנטארקטי.</p>

    <h2>האתגר הגדול: לנצח את הקור!</h2>
    <p>למרות הטמפרטורה העצומה שלה, לבה מאבדת חום לסביבה בקצב משמעותי, במיוחד כאשר היא נחשפת לאוויר הקר יחסית (ולעתים גם למים או סלעים קרים). האתגר העיקרי בשמירה על אגם לבה הוא לפצות ללא הרף על איבוד החום הזה ולמנוע מהלבה להתקרר ולהתקשות לקרום סלע חסר חיים.</p>

    <h2>הסוד: אספקת חום קבועה ומנגנוני בידוד טבעיים</h2>
    <p>כדי שאגם לבה יישאר פעיל, נדרשים שני תנאים עיקריים:</p>
    <ul>
        <li><strong>מקור חום אמין ורציף:</strong> העורק הראשי של האגם הוא צינור המזין אותו במאגמה חמה וטרייה מבטן כדור הארץ. זרם יציב וקבוע של מאגמה הוא חיוני כדי להזרים אנרגיה תרמית לאגם ולפצות על כל איבוד החום לסביבה. ככל שאספקת המאגמה מהירה יותר, כך קל יותר לשמור על האגם חם.</li>
        <li><strong>הפחתת איבוד חום:</strong> הלבה מאבדת חום בעיקר דרך פני השטח הפתוחים שלה (קרינה והסעה של חום לאוויר) ודרך מגע עם קירות הלוע (הולכה). אגמי לבה "חכמים" מפתחים מנגנונים להפחתת האיבוד הזה:
            <ul>
                <li><strong>קרום עילי מבודד:</strong> לעיתים קרובות נוצרת שכבה דקה או עבה של לבה שהתקררה והתקשתה חלקית על פני האגם. קרום זה אינו אטום לחלוטין (לעתים רואים בו סדקים או אזורים מבעבעים), אך הוא משמש כשכבת בידוד משמעותית שמקטינה דרמטית את קצב איבוד החום לסביבה. ככל שהקרום עבה ויציב יותר, כך הבידוד יעיל יותר.</li>
                <li><strong>גאומטריית הלוע:</strong> לוע עמוק יחסית יכול לעזור ללכוד אוויר חם מעל האגם ולהפחית את איבוד החום על ידי הסעה.</li>
            </ul>
        </li>
    </ul>

    <h2>נקודת האיזון הקריטית: החיים על הקצה</h2>
    <p>אגם לבה יציב מתקיים כאשר קיים איזון עדין ומדויק: קצב הגעת החום מהמעמקים (אספקת מאגמה) שווה לקצב איבוד החום לסביבה (דרך הקרינה, ההסעה וההולכה, מופחת על ידי הבידוד). אם אספקת המאגמה מספיק מהירה והבידוד מספיק יעיל, האגם יכול להישאר במצב נוזלי ודינמי. כל שינוי באיזון הזה יכול להוביל לסופו של האגם.</p>

    <h2>מדוע אגם לבה יכול "למות"?</h2>
    <p>אגם לבה אינו נצחי. הוא יכול לסיים את דרכו מכמה סיבות:</p>
    <ul>
        <li><strong>חולשה או הפסקה באספקת המאגמה:</strong> אם הזרם המזין את האגם נחלש או נפסק לגמרי, אין יותר מקור חום שמפצה על האיבוד הטבעי, והלבה מתקררת ומתקשה במהירות.</li>
        <li><strong>עלייה חדה באיבוד החום:</strong> התמוטטות של קירות הלוע, יצירת סדקים חדשים, או שינויים אחרים המגדילים את שטח המגע של הלבה עם הסביבה יכולים להגביר את קצב איבוד החום לרמה שאספקת המאגמה אינה יכולה לעמוד בה.</li>
        <li><strong>התמוטטות או התרוקנות:</strong> לעיתים, הלבה באגם יכולה לזרום החוצה דרך פתחים תת-קרקעיים שנפתחו, או שהאגם כולו קורס פנימה לתוך מערכת הצינורות שמתחתיו.</li>
    </ul>
    <p>עכשיו שאתם מבינים את הכוחות הפועלים, חזרו לסימולציה ונסו שוב! האם תצליחו לשמור על האגם חי ופעיל?</p>
</div>

<style>
    /* Global Styles for a better feel */
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6; /* Soft background */
    }

    h1, h2, h3 {
        color: #2c3e50;
        margin-bottom: 15px;
    }

    p {
        margin-bottom: 10px;
    }

    /* Simulation Container Styling */
    .simulation-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 30px auto;
        padding: 30px;
        background: linear-gradient(to bottom, #e0e5ec, #f9fbfc); /* Subtle gradient */
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        max-width: 600px; /* Limit width for better presentation */
    }

    /* Controls Styling */
    .controls {
        display: flex;
        gap: 40px;
        margin-bottom: 30px;
        flex-wrap: wrap;
        justify-content: center;
        width: 100%;
    }

    .control-group {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        flex: 1; /* Allow groups to grow */
        min-width: 200px; /* Minimum width */
    }

    .control-group h3 {
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.1em;
        color: #34495e;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
    }

    .control-group label {
        display: block; /* Stack radio buttons */
        margin-bottom: 8px;
        cursor: pointer;
        font-size: 0.95em;
        transition: color 0.2s ease;
    }

    .control-group label:hover {
        color: #e74c3c; /* Highlight on hover */
    }

    .control-group input[type="radio"] {
         margin-right: 8px;
         accent-color: #e74c3c; /* Style radio button color */
    }


    /* Volcano Throat Styling */
    .volcano-throat {
        width: 120px; /* Slightly wider */
        height: 250px; /* Taller */
        border: 3px solid #5a524a; /* Darker, earthy border */
        border-top: none;
        position: relative;
        overflow: hidden;
        background: linear-gradient(to bottom, #8b7e72, #5a524a); /* Rocky gradient */
        border-bottom-left-radius: 15px;
        border-bottom-right-radius: 15px;
        box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.3); /* Inner shadow for depth */
        display: flex;
        flex-direction: column-reverse; /* Fill from bottom */
    }

     /* Lava Lake Styling */
    .lava-lake {
        width: 100%;
        height: 0%;
        background-color: #ff8c00; /* Initial orange */
        transition: height 0.8s ease-out, background-color 0.8s ease; /* Slower, smoother transition */
        position: relative; /* Needed for pseudo-elements/surface effects */
        z-index: 1; /* Ensure it's below surface effects if any */
        box-shadow: inset 0 0 20px rgba(255, 140, 0, 0.5), 0 0 30px rgba(255, 140, 0, 0.7); /* Inner and outer glow */
    }

     /* Lava Surface Effects (Bubbling) */
     .lava-surface-effect {
        position: absolute;
        bottom: 0; /* Position at the top of the lava (which fills from bottom) */
        left: 0;
        width: 100%;
        height: 50px; /* Effect zone height */
        z-index: 2; /* Above the base lava color */
        overflow: hidden; /* Hide effects outside the throat */
        opacity: 0; /* Start hidden */
        transition: opacity 0.5s ease; /* Smooth fade in */
     }

     /* Bubbling Animation */
     @keyframes bubbling {
         0%, 100% { transform: translateY(0); opacity: 0.6; }
         50% { transform: translateY(-10px); opacity: 1; } /* Bubbles rise */
     }

     .lava-surface-effect::before,
     .lava-surface-effect::after {
         content: '';
         position: absolute;
         width: 15px; /* Size of bubbles */
         height: 15px;
         background-color: rgba(255, 255, 200, 0.8); /* Bright yellowish bubbles */
         border-radius: 50%;
         filter: blur(3px); /* Soft edges */
     }

     .lava-surface-effect::before {
         left: 20%;
         bottom: 5px;
         animation: bubbling 2s ease-in-out infinite alternate;
     }

     .lava-surface-effect::after {
         left: 70%;
         bottom: 15px;
         animation: bubbling 2.5s ease-in-out infinite alternate 0.5s; /* Different timing */
     }


    /* Status Display Styling */
    .status {
        margin-top: 30px;
        text-align: center;
        font-size: 1em;
        color: #34495e;
        background-color: #ecf0f1;
        padding: 15px;
        border-radius: 8px;
        width: 100%;
        box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .status p {
        margin: 5px 0;
    }

    .status span {
        font-weight: bold;
        color: #e74c3c; /* Default status color */
        transition: color 0.5s ease; /* Smooth color change */
    }

    /* Specific status colors (JS will add classes) */
    .status .status-stable { color: #2ecc71; } /* Green */
    .status .status-cooling { color: #f39c12; } /* Orange */
    .status .status-solidified { color: #95a5a6; } /* Grey */
    .status .status-heating { color: #e74c3c; } /* Red */
    .status .status-unstable { color: #c0392b; } /* Dark Red */


    /* Explanation Toggle Button */
    #toggleExplanation {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        background-color: #3498db; /* Blue */
        color: white;
        border-radius: 25px; /* Pill shape */
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        font-weight: bold;
    }

    #toggleExplanation:hover {
        background-color: #2980b9; /* Darker blue */
        transform: translateY(-1px); /* Subtle lift */
    }

    #toggleExplanation:active {
        transform: translateY(1px); /* Subtle press */
    }

    /* Explanation Section Styling */
    #explanation {
        border-top: 2px solid #bdc3c7; /* Light grey line */
        padding-top: 25px;
        margin-top: 25px;
        line-height: 1.7;
        color: #555;
    }

    #explanation h2 {
        margin-top: 20px;
        margin-bottom: 12px;
        font-size: 1.3em;
        color: #2c3e50;
        border-bottom: 1px dashed #bdc3c7; /* Subtle separator */
        padding-bottom: 8px;
    }

    #explanation ul {
        margin-top: 12px;
        padding-left: 20px; /* Indent lists */
    }

    #explanation li {
        margin-bottom: 8px;
    }

    #explanation ul ul { /* Nested lists */
         margin-top: 5px;
         padding-left: 15px;
         font-size: 0.95em;
         color: #666;
    }

    /* Make simulation area responsive */
    @media (max-width: 600px) {
        .simulation-container {
            padding: 20px;
        }
        .controls {
            flex-direction: column;
            gap: 20px;
        }
        .control-group {
            width: 100%; /* Full width on small screens */
            min-width: auto;
        }
        .volcano-throat {
             width: 100px; /* Smaller volcano on mobile */
             height: 200px;
        }
        .status {
             font-size: 0.9em;
        }
    }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const lavaLake = document.querySelector('.lava-lake');
        const lavaSurfaceEffect = document.querySelector('.lava-surface-effect'); // Get the effect element
        const lavaLevelText = document.getElementById('lavaLevelText');
        const lavaTempText = document.getElementById('lavaTempText');
        const simulationStatusSpan = document.getElementById('simulationStatus'); // Changed var name
        const stableTimerText = document.getElementById('stableTimerText'); // Get timer element
        const magmaFlowInputs = document.querySelectorAll('input[name="magmaFlow"]');
        const surfaceInsulationInputs = document.querySelectorAll('input[name="surfaceInsulation"]');
        const explanationDiv = document.getElementById('explanation');
        const toggleButton = document.getElementById('toggleExplanation');

        let lavaLevel = 0; // Percentage of volcano throat height (0-100)
        let lavaTemperature = 800; // Real-world temp scale for display, e.g., starting cool (800-1200°C range)
        let internalTemp = 0; // Internal calculation scale (0-100)

        let simulationInterval = null;
        let stableTimer = 0; // Timer for stability

        const MAX_LAVA_LEVEL = 100; // Max height percentage
        const MIN_REAL_TEMP = 800; // Min realistic basalt temp
        const MAX_REAL_TEMP = 1200; // Max realistic basalt temp
        const MAX_INTERNAL_TEMP = 100; // Internal max temp scale

        // Mapping functions between real and internal temp
        const realToInternalTemp = (realTemp) => (realTemp - MIN_REAL_TEMP) / (MAX_REAL_TEMP - MIN_REAL_TEMP) * MAX_INTERNAL_TEMP;
        const internalToRealTemp = (internalTemp) => MIN_REAL_TEMP + (internalTemp / MAX_INTERNAL_TEMP) * (MAX_REAL_TEMP - MIN_REAL_TEMP);

        // Initialize internal temp based on initial real temp
        internalTemp = realToInternalTemp(lavaTemperature);


        // Define simulation parameters based on controls (tuned for gamification/stability)
        const flowRates = {
            low: { levelIncrease: 0.3, tempIncrease: 0.5 }, // Slow inflow, less heat
            medium: { levelIncrease: 1.0, tempIncrease: 1.2 }, // Moderate inflow, more heat
            high: { levelIncrease: 2.0, tempIncrease: 2.0 } // Fast inflow, high heat
        };

        const heatLossRates = {
            low: { baseLoss: 1.0, levelMultiplier: 0.05 }, // High heat loss from surface/sides
            high: { baseLoss: 0.3, levelMultiplier: 0.02 } // Lower heat loss due to insulation
        };

        // Simulation Update Frequency (in ms)
        const simulationStepTime = 100; // Update every 100ms

        function getSelectedMagmaFlow() {
            return document.querySelector('input[name="magmaFlow"]:checked').value;
        }

        function getSelectedSurfaceInsulation() {
            return document.querySelector('input[name="surfaceInsulation"]:checked').value;
        }

        function updateSimulation() {
            const currentFlow = getSelectedMagmaFlow();
            const currentInsulation = getSelectedSurfaceInsulation();
            const flowParams = flowRates[currentFlow];
            const lossParams = heatLossRates[currentInsulation];

            // --- Update Internal Temperature ---
            // Heat Gain from inflow
            let tempChange = flowParams.tempIncrease;

            // Heat Loss: Depends on insulation and current level (more surface exposed = more loss)
            let heatLoss = lossParams.baseLoss + (lossParams.levelMultiplier * lavaLevel); // Loss increases with level
            tempChange -= heatLoss;

            internalTemp += tempChange;

            // Clamp internal temp between 0 and MAX_INTERNAL_TEMP
            internalTemp = Math.max(0, Math.min(MAX_INTERNAL_TEMP, internalTemp));

            // Update real temperature for display
            lavaTemperature = internalToRealTemp(internalTemp);

            // --- Update Lava Level ---
            // Inflow: Lava level increases based on magma flow rate
            let levelChange = flowParams.levelIncrease;

            // Outflow/Cooling Contraction/Solidification: Simulate some level decrease
            // This should be higher if temp is low (solidifying) or level is high (overflow/spreading)
            let coolingContraction = 0;
            if (internalTemp < 50) { // Significant contraction if cooling below threshold (internal 50 maps to ~1000°C)
                 coolingContraction = (50 - internalTemp) * 0.2; // More contraction as temp drops
            }
             if (lavaLevel > 80) { // Simulate overflow/spreading at high levels
                 coolingContraction += (lavaLevel - 80) * 0.1;
             } else if (lavaLevel > 60) { // Small loss factor even at moderate high levels
                 coolingContraction += (lavaLevel - 60) * 0.05;
             }

            levelChange -= coolingContraction;


            lavaLevel += levelChange;

            // Clamp level between 0 and MAX_LAVA_LEVEL
            lavaLevel = Math.max(0, Math.min(MAX_LAVA_LEVEL + 5, lavaLevel)); // Allow slight overflow visually


            // --- Update Visuals ---
            // Limit visual level to 100% but simulate overflow logic above 100%
            const visualLavaLevel = Math.min(MAX_LAVA_LEVEL, lavaLevel);
            lavaLake.style.height = `${visualLavaLevel}%`;

            // Change color based on internal temperature (0-100 scale)
            const colorScale = (intTemp) => {
                 // Map internal temp (0-100) to HSL color (Hue, Saturation, Lightness)
                 // Hue: Start red-orange (0-30) at low temp, move towards yellow (60) at high temp
                 const hue = 30 - (intTemp / MAX_INTERNAL_TEMP) * 30; // Start at 30 (orange), end at 0 (red)
                 const saturation = 90; // Keep high saturation
                 // Lightness: Increase lightness significantly with temperature
                 const lightness = 30 + (intTemp / MAX_INTERNAL_TEMP) * 30; // Start darker, end brighter
                 // Reverse hue direction for more typical lava color progression (red->orange->yellowish)
                 const hue_reversed = (intTemp / MAX_INTERNAL_TEMP) * 60; // Start at 0 (red), move towards 60 (yellow)
                 const finalHue = Math.max(0, Math.min(60, hue_reversed)); // Clamp hue

                 // Use HSL for smooth transition: h from ~0 (red) to ~50 (yellow), s 100%, l from ~20% to ~50%
                 const h = finalHue;
                 const s = 100;
                 const l = 20 + (intTemp / MAX_INTERNAL_TEMP) * 30; // L from 20 to 50
                 return `hsl(${h}, ${s}%, ${l}%)`;
            };
            lavaLake.style.backgroundColor = colorScale(internalTemp);
             // Adjust glow based on temp
            const glowOpacity = Math.max(0.3, internalTemp / MAX_INTERNAL_TEMP * 0.7);
            const glowSize = Math.max(10, internalTemp / MAX_INTERNAL_TEMP * 30);
            lavaLake.style.boxShadow = `inset 0 0 ${glowSize}px rgba(255, 140, 0, ${glowOpacity * 0.7}), 0 0 ${glowSize * 1.5}px rgba(255, 140, 0, ${glowOpacity})`;


            // Control bubbling animation visibility/intensity
            if (internalTemp > 70 && visualLavaLevel > 30) { // Start bubbling when hot and level is sufficient
                lavaSurfaceEffect.style.opacity = Math.min(1, (internalTemp - 70) / 30); // Fade in bubbling effect
                lavaSurfaceEffect.style.animationPlayState = 'running';
             } else {
                 lavaSurfaceEffect.style.opacity = 0;
                 lavaSurfaceEffect.style.animationPlayState = 'paused';
             }
            // Position bubbling effect at the top of the visual lava level
             lavaSurfaceEffect.style.bottom = `${100 - visualLavaLevel}px`;


            // --- Update Status Text and Timer ---
            lavaLevelText.textContent = `${Math.round(visualLavaLevel)}%`; // Show visual level
            lavaTempText.textContent = `${Math.round(lavaTemperature)}°C`; // Show real temp

            let status = "פעיל...";
            let isStable = false;
            const currentStatusSpan = simulationStatusSpan; // Use the renamed variable

            // Remove previous status classes
            currentStatusSpan.classList.remove('status-stable', 'status-cooling', 'status-solidified', 'status-heating', 'status-unstable');


            if (internalTemp < 10 && lavaLevel < 10) { // Very cold and low level
                 status = "התקרר והתקשה! 🥶";
                 currentStatusSpan.classList.add('status-solidified');
                 isStable = false; // Not stable when solidified
            } else if (internalTemp < 30) { // Cooling significantly (internal temp < 30 maps to < ~920°C)
                 status = "מתקרר במהירות... 🧊";
                 currentStatusSpan.classList.add('status-cooling');
                 isStable = false;
            } else if (lavaLevel > 100) { // Overflow state
                 status = "עומד לגלוש! 🔥🌋";
                 currentStatusSpan.classList.add('status-unstable');
                 isStable = false;
            } else if (lavaLevel < 20 && internalTemp > 40) { // High temp but low level
                 status = "אספקת מאגמה נמוכה מדי... 🤔";
                  currentStatusSpan.classList.add('status-cooling'); // Tends to cool down
                 isStable = false;
            } else if (lavaLevel > 85 && internalTemp > 90 && Math.abs(levelChange) < 0.5 && Math.abs(tempChange) < 0.5) { // High level, high temp, stable rates
                status = "אגם לבה יציב ופעיל! ✨";
                currentStatusSpan.classList.add('status-stable');
                isStable = true; // Stable condition met
            } else if (lavaLevel > 70 && internalTemp > 70) { // High enough level and temp, but not perfectly stable rates
                 status = "פעיל ויציב יחסית...";
                 currentStatusSpan.classList.add('status-heating'); // Or status-cooling, depends on tempChange
                 isStable = false; // Only perfectly stable for the timer
            } else {
                 status = "משתנה... נסה לשפר את התנאים";
                 currentStatusSpan.classList.add('status-unstable');
                 isStable = false;
            }

            simulationStatusSpan.textContent = status;

            // Update timer based on stability
            if (isStable) {
                 stableTimer += simulationStepTime / 1000; // Add interval time in seconds
            } else {
                 stableTimer = 0; // Reset timer if not stable
            }
            stableTimerText.textContent = Math.floor(stableTimer); // Display whole seconds

        }

        // Start/Reset simulation
        function startSimulation() {
             if (simulationInterval) {
                 clearInterval(simulationInterval);
             }
             // Reset state
             lavaLevel = 0;
             lavaTemperature = MIN_REAL_TEMP; // Start cool
             internalTemp = realToInternalTemp(lavaTemperature); // Reset internal temp
             stableTimer = 0; // Reset timer
             stableTimerText.textContent = Math.floor(stableTimer);

             // Update initial display
             lavaLake.style.height = '0%';
             lavaLake.style.backgroundColor = colorScale(internalTemp);
             lavaLake.style.boxShadow = `inset 0 0 10px rgba(255, 140, 0, 0.3), 0 0 15px rgba(255, 140, 0, 0.4)`; // Reset glow
             lavaLevelText.textContent = `${Math.round(lavaLevel)}%`;
             lavaTempText.textContent = `${Math.round(lavaTemperature)}°C`;
             simulationStatusSpan.textContent = "מתחיל...";
             simulationStatusSpan.className = ''; // Clear status classes


             // Start the simulation loop
             simulationInterval = setInterval(updateSimulation, simulationStepTime);
        }

        // Restart simulation when controls change
        magmaFlowInputs.forEach(input => input.addEventListener('change', startSimulation));
        surfaceInsulationInputs.forEach(input => input.addEventListener('change', startSimulation));

        // Toggle Explanation Visibility
        toggleButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleButton.textContent = isHidden ? 'הסתר את הסוד' : 'הצג את הסוד מאחורי אגמי הלבה'; // More engaging text
        });

        // Initial start of the simulation when the page loads
        startSimulation();

         // Initial color scale helper (needed before updateSimulation runs first)
         const colorScale = (intTemp) => {
             const h = (intTemp / MAX_INTERNAL_TEMP) * 60;
             const s = 100;
             const l = 20 + (intTemp / MAX_INTERNAL_TEMP) * 30;
             return `hsl(${h}, ${s}%, ${l}%)`;
         };
    });
</script>
```