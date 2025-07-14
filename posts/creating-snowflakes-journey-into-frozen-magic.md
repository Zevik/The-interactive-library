---
title: "בריאת פתית השלג: מסע אל תוך הקסם הקפוא"
english_slug: creating-snowflakes-journey-into-frozen-magic
category: "פיזיקה"
tags:
  - שלג
  - גבישים
  - פיזיקה
  - מטאורולוגיה
  - הדמיה
  - אינטראקטיבי
---
<h1>בריאת פתית השלג: מסע אל תוך הקסם הקפוא</h1>

<p>האם אי פעם תהית מדוע אין שני פתיתי שלג זהים? הצטרף למסע קפוא אל לב הענן, ושלוט בתנאי הסביבה כדי לחזות במו עיניך כיצד טמפרטורה ולחות רוקדות יחד כדי לברוא צורות גבישיות מדהימות וחד פעמיות. צור את פתית השלג הייחודי שלך עכשיו!</p>

<div id="simulation-container">
    <div id="controls">
        <h2>פסל את פתית השלג שלך:</h2>
        <p>שנה את התנאים בזמן שהגביש גדל!</p>
        <label for="temperature">טמפרטורה (°C): <span id="temp-value">-15</span></label>
        <input type="range" id="temperature" min="-25" max="0" value="-15" step="1">

        <label for="humidity">לחות (זמינות אדי מים): <span id="humidity-value">50</span>% <span id="humidity-qualitative"></span></label>
        <input type="range" id="humidity" min="0" max="100" value="50" step="1">

        <button id="reset-button">צור פתית שלג חדש!</button>
    </div>
    <div id="snowflake-display">
        <canvas id="snowflake-canvas"></canvas>
    </div>
</div>

<style>
    /* גופנים ועיצוב כללי */
    body {
        font-family: 'Arial', sans-serif; /* פונט נקי וקריא */
        direction: rtl; /* כיוון קריאה מימין לשמאל */
        text-align: right; /* יישור לימין */
        line-height: 1.6;
        color: #333;
        background-color: #eef5f9; /* רקע תכלכל עדין */
        padding: 20px;
    }

    h1, h2, h3 {
        color: #004080; /* כחול כהה יותר לכותרות */
        text-align: center;
        margin-bottom: 15px;
    }

    h1 {
        font-size: 2em;
        margin-top: 0;
        margin-bottom: 20px;
    }

    p {
         margin-bottom: 15px;
         text-align: center; /* יישור פסקה מרכז */
         max-width: 700px; /* רוחב מקסימלי לפסקאות */
         margin-left: auto;
         margin-right: auto;
    }


    /* קונטיינר הסימולציה */
    #simulation-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px; /* מרווח גדול יותר בין האלמנטים */
        padding: 30px;
        background: linear-gradient(to bottom, #f0f8ff, #e0f0ff); /* רקע כחול עדין עם גרדיאנט */
        border-radius: 12px; /* פינות מעוגלות יותר */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* צל עדין יותר */
        margin-bottom: 40px;
        max-width: 800px; /* רוחב מקסימלי לקונטיינר */
        margin-left: auto;
        margin-right: auto;
    }

    /* פקדים */
    #controls {
        background-color: #ffffff;
        padding: 25px; /* ריפוד גדול יותר */
        border-radius: 10px; /* פינות מעוגלות */
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08); /* צל עדין */
        width: 100%;
        max-width: 450px; /* רוחב מקסימלי */
        text-align: right;
        border: 1px solid #d0e0f0; /* גבול עדין */
    }

    #controls h2 {
        text-align: center;
        margin-top: 0;
        color: #0056b3; /* כחול מודגש יותר */
        font-size: 1.5em;
    }
     #controls p {
         text-align: center;
         font-size: 0.9em;
         color: #555;
         margin-top: -10px;
         margin-bottom: 20px;
     }

    #controls label {
        display: block;
        margin-bottom: 10px; /* מרווח גדול יותר בין כפתורים */
        font-weight: bold;
        color: #004080;
        font-size: 1.1em;
    }

    #controls input[type="range"] {
        width: 100%;
        margin-bottom: 20px; /* מרווח גדול יותר אחרי הסליידר */
        -webkit-appearance: none;
        appearance: none;
        height: 8px; /* עובי סליידר */
        background: #b0d0f0; /* רקע סליידר */
        outline: none;
        opacity: 0.7;
        transition: opacity 0.2s ease-in-out;
        border-radius: 4px;
    }

    #controls input[type="range"]:hover {
        opacity: 1;
    }

    #controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px; /* גודל ידית סליידר */
        height: 20px; /* גודל ידית סליידר */
        background: #007bff; /* צבע ידית */
        cursor: pointer;
        border-radius: 50%; /* ידית עגולה */
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
    }

    #controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
    }

    #humidity-qualitative {
        font-weight: normal;
        font-size: 0.9em;
        color: #555;
        margin-right: 5px;
    }

    /* תצוגת פתית השלג */
    #snowflake-display {
        width: 100%;
        max-width: 550px; /* רוחב מקסימלי גדול יותר */
        aspect-ratio: 1 / 1;
        background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="45" fill="none" stroke="%23c0d0e0" stroke-width="1" stroke-dasharray="2,2"/></svg>') center center / cover no-repeat, linear-gradient(to top, #e0f0ff, #f5faff); /* רקע כחלחל עדין עם עיגול עדין במרכז */
        border: 1px solid #c0d0e0;
        border-radius: 12px;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.05); /* צל פנימי עדין */
    }

     #snowflake-canvas {
        width: 100%;
        height: 100%;
        display: block;
    }

    /* כפתור איפוס */
    #reset-button {
        display: block;
        width: fit-content;
        margin: 20px auto 0 auto; /* מרווח גדול יותר אחרי הכפתור */
        padding: 12px 25px; /* ריפוד גדול יותר */
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 6px; /* פינות מעוגלות יותר */
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    #reset-button:hover {
        background-color: #0056b3;
        transform: translateY(-1px); /* אפקט ריחוף קל */
    }
    #reset-button:active {
         transform: translateY(0); /* אפקט לחיצה */
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }


    /* כפתור הסבר */
    #toggle-explanation {
        display: block;
        width: fit-content;
        margin: 30px auto 20px auto; /* מרווח מסביב לכפתור */
        padding: 12px 25px;
        background-color: #28a745; /* ירוק */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    #toggle-explanation:hover {
        background-color: #218838;
        transform: translateY(-1px);
    }
     #toggle-explanation:active {
         transform: translateY(0);
          box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
     }


    /* סעיף ההסבר */
    #explanation-section {
        border-top: 1px solid #d0e0f0; /* קו הפרדה עדין */
        padding-top: 25px; /* מרווח גדול יותר מעל הקו */
        margin-top: 30px;
        display: none;
        opacity: 0; /* התחלה באטימות 0 */
        transition: opacity 0.5s ease-in-out; /* אנימציית התגלות */
        text-align: right;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }

    #explanation-section.visible {
        opacity: 1; /* אטימות 1 כשהוא גלוי */
    }

    #explanation-section h2, #explanation-section h3 {
        color: #004080;
        margin-top: 20px; /* מרווח גדול יותר בין כותרות בסעיף ההסבר */
        margin-bottom: 10px;
    }

    #explanation-section p {
        line-height: 1.7; /* מרווח שורות גדול יותר */
        margin-bottom: 18px;
        text-align: right; /* יישור לימין */
    }
     #explanation-section ul {
        margin-bottom: 18px;
        padding-right: 25px; /* ריווח גדול יותר לרשימה */
        text-align: right;
     }
      #explanation-section li {
       margin-bottom: 8px; /* מרווח בין פריטי רשימה */
     }
</style>

<button id="toggle-explanation">הצג/הסתר הסבר מפורט</button>

<div id="explanation-section">
    <h2>פענוח הקסם: איך נוצרים פתיתי השלג?</h2>

    <h3>התחלה צנועה: מגרעין התעבות לגביש ראשוני</h3>
    <p>כל פתית שלג מתחיל את דרכו כגביש קרח בודד וזעיר בתוך ענן קר מאוד. הוא מתחיל להיווצר סביב חלקיק קטן באוויר (כמו אבק או פיח) שמשמש כ"גרעין התעבות". בטמפרטורות נמוכות מ-0°C, אדי מים באוויר יכולים לדלג על השלב הנוזלי ולהפוך ישירות לקרח על פני הגרעין הזעיר הזה – תהליך מופלא הנקרא <strong>דפוזיציה</strong>. התהליך הזה שונה מיצירת גשם קופא או ברד, שמתחילים כטיפות מים.</p>

    <h3>הריקוד המולקולרי: למה דווקא משושה?</h3>
    <p>מולקולות המים (H₂O) מתחברות זו לזו במבנה קבוע דמוי סריג כשהן קופאות, ויוצרות את מבנה הקרח. המבנה הבסיסי של גביש הקרח הוא <strong>הקסגונלי</strong> (בעל שש צלעות), וזהו המקור לצורת שש הזרועות האופיינית של פתיתי השלג. כשהגביש הזעיר גדל, מולקולות מים נוספות מהאוויר מתקשרות לפאות השונות של המבנה ההקסגונלי הראשוני.</p>

    <h3>שני הקוסמים הראשיים: טמפרטורה ולחות</h3>
    <p>הצורה המורכבת והמגוונת של פתית השלג נקבעת בעיקר על ידי שני גורמים סביבתיים קריטיים <strong>בזמן הגידול</strong>:</p>

    <h4>השפעת הטמפרטורה:</h4>
    <p>הטמפרטורה משפיעה באופן דרמטי על האופן שבו מולקולות המים נקשרות לפאות השונות של הגביש. בפאות מסוימות, ההתקשרות מהירה יותר בטמפרטורות מסוימות, וזה מוביל לצמיחה מועדפת בכיוונים מסוימים. זהו לב ליבה של "תרשים צורות השלג" שמדענים מיפו:</p>
    <ul>
        <li><strong>0°C עד -4°C:</strong> נוטות להיווצר לוחיות דקות ושטוחות (Plates).</li>
        <li><strong>-4°C עד -8°C:</strong> נוטות להיווצר עמודים דקים וארוכים או מחטים (Columns, Needles).</li>
        <li><strong>-8°C עד -12°C:</strong> שוב חוזרות הלוחיות, לפעמים עבות יותר או עם התחלת התפצלות (Thick Plates, Simple Dendrites).</li>
        <li><strong>-12°C עד -16°C:</strong> זהו "תחום הקסם" ליצירת הדנדריטים המורכבים והיפים ביותר – גבישים בעלי שש זרועות מסועפות (Stellar Dendrites). הצמיחה מהירה ומורכבת בקצוות.</li>
        <li><strong>מתחת ל-16°C-:</strong> לרוב נוצרים שוב עמודים ולוחיות פשוטים יותר, לעיתים חלולים.</li>
    </ul>

    <h4>השפעת הלחות (זמינות אדי מים):</h4>
    <p>כמות אדי המים הזמינים בסביבה (המכונה "רוויית יתר" ביחס לקרח) משפיעה בעיקר על <strong>מהירות הגידול ומידת הסיעוף והמורכבות</strong>:</p>
    <ul>
        <li><strong>לחות נמוכה:</strong> הגידול איטי יותר, והצורות נוטות להיות פשוטות ועדינות יותר (משושים, עמודים, מחטים דקות).</li>
        <li><strong>לחות גבוהה:</strong> הגידול מהיר מאוד. בתחומי הטמפרטורה המעודדים צמיחה מהירה של קצוות (כמו בטווח הדנדריטים), לחות גבוהה מספקת שפע "חומר גלם" להתקשרות מהירה, ומאפשרת לזרועות להתפצל ולהתעטר בסיעופים משניים ושלישוניים, ויוצרת פתיתים מרהיבים וסבוכים.</li>
    </ul>

    <h3>מסע אישי: למה כל פתית ייחודי?</h3>
    <p>הסיבה לכך שכמעט כל פתית שלג בטבע הוא יחיד ומיוחד נובעת מכך שכל גביש קפוא חווה <strong>מסע ייחודי</strong> משלו מראש הענן ועד הקרקע. בדרכו הוא עובר דרך אזורים שונים בענן ובאטמוספירה, בהם הטמפרטורה והלחות משתנות כל הזמן. אפילו שינויים קלים ביותר בתנאים לאורך מסלול הנפילה משפיעים על קצב הגידול ועל צורת ההתקשרות של מולקולות המים באותו רגע. מכיוון שרצף התנאים שחווה כל גביש הוא שונה, כל אחד מהם "רושם" את ההיסטוריה האקלימית שלו בצורתו הסופית, והופך ליצירת אמנות קפואה חד-פעמית!</p>
    <p>בסימולציה זו, תוכל לשנות את הטמפרטורה והלחות <strong>בזמן אמת</strong> ולראות כיצד השינויים הללו משפיעים מיידית על אופן הגידול ויוצרים צורות שונות מנקודת השינוי ואילך – בדיוק כפי שקורה לפתיתי שלג אמיתיים במסעם באטמוספירה.</p>
</div>

<script>
    const canvas = document.getElementById('snowflake-canvas');
    const ctx = canvas.getContext('2d');
    const tempSlider = document.getElementById('temperature');
    const humiditySlider = document.getElementById('humidity');
    const tempValueSpan = document.getElementById('temp-value');
    const humidityValueSpan = document.getElementById('humidity-value');
    const humidityQualitativeSpan = document.getElementById('humidity-qualitative');
    const resetButton = document.getElementById('reset-button');
    const explanationSection = document.getElementById('explanation-section');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    let temperature = parseInt(tempSlider.value);
    let humidity = parseInt(humiditySlider.value); // 0-100 percentage

    // Snowflake state: Represents the geometric structure of the snowflake
    // Instead of one growth level, track branches
    let snowflakeArms = []; // Array of 6 arms
    const numArms = 6;
    const maxArmLength = Math.min(canvas.width, canvas.height) * 0.45; // Max visual size of an arm
    const minCoreRadius = 5; // Starting size of the core
    let animationFrameId = null; // For requestAnimationFrame

    // --- Simulation Setup ---

    function initializeSnowflake() {
        snowflakeArms = [];
        for(let i = 0; i < numArms; i++) {
            snowflakeArms.push({
                length: minCoreRadius, // Start with base length
                branches: [] // Store side branches { position: ratio along arm (0-1), length: pixels }
            });
        }
        // Clear any pending animation frames
        if(animationFrameId) {
             cancelAnimationFrame(animationFrameId);
        }
        startSimulation(); // Start growing
    }

    function setupCanvas() {
        const display = document.getElementById('snowflake-display');
        const size = Math.min(display.clientWidth, display.clientHeight);
        canvas.width = size;
        canvas.height = size;
        ctx.setTransform(1, 0, 0, 1, 0, 0); // Reset transform
        ctx.translate(canvas.width / 2, canvas.height / 2);
        ctx.lineCap = 'round';
        ctx.strokeStyle = '#ffffff'; // White snowflake
        ctx.fillStyle = '#ffffff';
    }

    // --- Drawing ---

    function drawSnowflake() {
        ctx.clearRect(-canvas.width / 2, -canvas.height / 2, canvas.width, canvas.height); // Clear previous frame

        const scaleFactor = Math.min(canvas.width, canvas.height) / 550; // Scale drawing based on canvas size relative to max-width in CSS
        const coreRadius = minCoreRadius * scaleFactor;
        ctx.lineWidth = coreRadius / 2; // Base line thickness

        // Draw central core
        ctx.beginPath();
        ctx.arc(0, 0, coreRadius * 0.8, 0, Math.PI * 2);
        ctx.fill();


        for (let i = 0; i < numArms; i++) {
            ctx.save(); // Save state for each arm
            ctx.rotate(i * Math.PI / 3); // Rotate for each arm (60 degrees)

            const arm = snowflakeArms[i];
            const currentArmLength = arm.length * scaleFactor; // Scale arm length

            // Draw main arm segment
            if (currentArmLength > coreRadius) {
                 ctx.beginPath();
                 ctx.moveTo(coreRadius, 0); // Start drawing from the edge of the core
                 ctx.lineTo(currentArmLength, 0);
                 ctx.stroke();
            }

            // Draw side branches/features
            arm.branches.forEach(branch => {
                 ctx.save();
                 // Translate to the position along the main arm (ratio * total length)
                 const branchPos = coreRadius + (currentArmLength - coreRadius) * branch.position;
                 ctx.translate(branchPos, 0);

                 const branchLength = branch.length * scaleFactor; // Scale branch length

                 // Draw two side branches (up and down relative to main arm)
                 const branchAngle = Math.PI / 4; // 45 degrees
                 ctx.lineWidth = ctx.lineWidth * 0.6; // Thinner branch lines

                 ctx.rotate(branchAngle);
                 ctx.beginPath();
                 ctx.moveTo(0,0);
                 ctx.lineTo(branchLength, 0);
                 ctx.stroke();

                 ctx.rotate(-2 * branchAngle); // Rotate back and then down
                 ctx.beginPath();
                 ctx.moveTo(0,0);
                 ctx.lineTo(branchLength, 0);
                 ctx.stroke();

                 ctx.restore(); // Restore to main arm position context
            });

            ctx.restore(); // Restore initial context state
        }
    }

    // --- Simulation Logic ---

    function getGrowthType(temp, humid) {
        // Simplified mapping based on temperature zones from explanation
        // Humidity influences complexity/speed *within* the type
        if (temp >= -4 && temp <= 0) return 'plate'; // Thin plates
        if (temp > -8 && temp < -4) return 'needle'; // Needles/Columns
        if (temp >= -12 && temp <= -8) return 'plate_thick'; // Thicker plates, some simple branching
        if (temp > -16 && temp < -12) return 'dendrite'; // Complex dendrites
        if (temp < -16) return 'column'; // Simple columns/plates
        return 'simple'; // Default/core growth
    }

    function updateSnowflakeState() {
        const currentTemp = temperature;
        const currentHumidity = humidity / 100; // Scale 0-1

        let allArmsFinished = true;

        snowflakeArms.forEach(arm => {
             // If the arm hasn't reached max length, it's still growing
             if (arm.length < maxArmLength) {
                  allArmsFinished = false;

                  const growthType = getGrowthType(currentTemp, currentHumidity);
                  const baseGrowthRate = 0.5; // Base pixels per update
                  const humiditySpeedMultiplier = 1 + currentHumidity * 2; // Humidity makes it faster
                  const growthIncrement = baseGrowthRate * humiditySpeedMultiplier;

                  // Grow the main arm
                  arm.length += growthIncrement;
                  if (arm.length > maxArmLength) {
                      arm.length = maxArmLength; // Cap growth
                  }

                  // Add or grow side branches based on type and humidity
                  const minBranchSeparation = minCoreRadius * 3; // Don't put branches too close
                  const branchLengthFactor = 0.5 + currentHumidity * 0.8; // Branches longer/thicker with humidity

                  if (growthType === 'dendrite' || growthType === 'plate_thick') {
                       const maxBranches = growthType === 'dendrite' ? 10 : 3; // Dendrites have more branches
                       const branchProb = (growthType === 'dendrite' ? 0.2 : 0.05) * currentHumidity; // Probability of adding a new branch point per tick (influenced by humidity)

                       // Add new branch points along the growing tip area
                       const growthTipArea = arm.length - growthIncrement * 2; // Look back slightly from the new tip
                       if (growthTipArea > minCoreRadius * 2) { // Only add branches away from center
                           // Check if we should add a new branch point
                           if (Math.random() < branchProb && arm.branches.length < maxBranches) {
                                // Find a position near the tip, but not too close to previous branches
                                const potentialPos = Math.random() * (arm.length - coreRadius - minBranchSeparation) / (arm.length - coreRadius) + coreRadius / arm.length; // Random ratio from near center to near tip
                                // Ensure position is far enough from last branch
                                if (arm.branches.length === 0 || (potentialPos - arm.branches[arm.branches.length-1].position) * arm.length > minBranchSeparation) {
                                     arm.branches.push({ position: potentialPos, length: 0 }); // Add new branch point with zero length
                                }
                           }
                       }

                       // Grow existing branches
                       arm.branches.forEach(branch => {
                            const maxBranchLength = (arm.length - (coreRadius + (arm.length - coreRadius) * branch.position)) * 0.8 * branchLengthFactor; // Max branch length depends on distance to arm tip
                            const branchGrowthRate = growthIncrement * 0.8; // Branches grow slightly slower than main arm
                            branch.length += branchGrowthRate;
                            if (branch.length > maxBranchLength) {
                                branch.length = maxBranchLength;
                            }
                       });

                  } else if (growthType === 'plate' || growthType === 'plate_thick') {
                       // Simulate thickening or simple side bumps/plates instead of complex branches
                       // For simplicity in this drawing model, we can represent plates as short, wide branches or thickening of the main line.
                       // A simple approach is to grow a fixed number of "plate segments" outwards at intervals.
                       const numPlateSegments = growthType === 'plate' ? 4 : 6;
                       const segmentWidth = coreRadius * (growthType === 'plate' ? 1.5 : 2.5) * branchLengthFactor; // Width depends on type/humidity
                       const segmentSpacing = (arm.length - coreRadius) / numPlateSegments;

                       // Add/grow "branches" that represent the plate extensions
                       while(arm.branches.length < numPlateSegments) {
                            const pos = coreRadius + arm.branches.length * segmentSpacing;
                             if (pos < arm.length - minCoreRadius) { // Add segment if position is within current arm length
                                arm.branches.push({ position: (pos - coreRadius) / (arm.length - coreRadius), length: 0 }); // Add new segment point
                             } else {
                                 break; // Stop adding if out of space
                             }
                       }
                       arm.branches.forEach(branch => {
                           const maxSegmentLength = segmentWidth; // Max length is the desired width
                           const segmentGrowthRate = growthIncrement;
                           branch.length += segmentGrowthRate;
                            if (branch.length > maxSegmentLength) {
                                branch.length = maxSegmentLength;
                            }
                       });

                  }
                  // Note: 'needle' and 'column' types primarily grow the main arm, less emphasis on side features in this model.
             }
        });

        // If all arms reached max length, stop the simulation
        if (allArmsFinished) {
            if (animationFrameId) {
                 cancelAnimationFrame(animationFrameId);
                 animationFrameId = null;
            }
            console.log("Snowflake growth finished.");
        }
    }


     let lastUpdateTime = 0;
     const updatesPerSecond = 30; // Target updates per second
     const msPerUpdate = 1000 / updatesPerSecond;

    function simulationLoop(currentTime) {
        if (!lastUpdateTime) {
            lastUpdateTime = currentTime;
        }

        const deltaTime = currentTime - lastUpdateTime;

        // Update simulation state multiple times if frame rate is low, to keep simulation speed relatively constant
        let updatesToPerform = Math.floor(deltaTime / msPerUpdate);
        if (updatesToPerform > 5) updatesToPerform = 5; // Prevent spiral of death on very slow frames

        for(let i = 0; i < updatesToPerform; i++) {
             updateSnowflakeState();
        }

        lastUpdateTime = currentTime - (deltaTime % msPerUpdate); // Adjust lastUpdateTime for remaining time

        drawSnowflake(); // Redraw after updating state

        // Request the next frame if simulation is not finished
        let allArmsFinished = snowflakeArms.every(arm => arm.length >= maxArmLength);
         if (!allArmsFinished) {
             animationFrameId = requestAnimationFrame(simulationLoop);
         } else {
             // Final draw to ensure max size is rendered clearly
             drawSnowflake();
         }
    }

     function startSimulation() {
        // Reset time tracking
        lastUpdateTime = 0;
        // Cancel any previous frame request
        if(animationFrameId) {
             cancelAnimationFrame(animationFrameId);
        }
        // Start the loop
        animationFrameId = requestAnimationFrame(simulationLoop);
    }

    function resetSimulation() {
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
        }
        initializeSnowflake(); // Reset state and start over
    }


    // --- Event Listeners ---

    tempSlider.addEventListener('input', (event) => {
        temperature = parseInt(event.target.value);
        tempValueSpan.textContent = temperature;
        // Simulation loop uses the new temperature value automatically in the next tick
    });

    humiditySlider.addEventListener('input', (event) => {
        humidity = parseInt(event.target.value);
        humidityValueSpan.textContent = humidity;
        // Update qualitative description
        if (humidity < 30) {
            humidityQualitativeSpan.textContent = '(נמוכה)';
        } else if (humidity < 70) {
            humidityQualitativeSpan.textContent = '(בינונית)';
        } else {
            humidityQualitativeSpan.textContent = '(גבוהה)';
        }
        // Simulation loop uses the new humidity value automatically in the next tick
    });

    resetButton.addEventListener('click', resetSimulation);

     toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationSection.style.display === 'none' || explanationSection.style.display === '';
        if (isHidden) {
            explanationSection.style.display = 'block';
             // Force reflow to enable transition
            explanationSection.offsetHeight;
            explanationSection.classList.add('visible');
            toggleExplanationButton.textContent = 'הסתר הסבר מפורט';

        } else {
             explanationSection.classList.remove('visible');
             // Hide it completely after the transition
             explanationSection.addEventListener('transitionend', function handler() {
                 explanationSection.style.display = 'none';
                 explanationSection.removeEventListener('transitionend', handler);
             });
            toggleExplanationButton.textContent = 'הצג/הסתר הסבר מפורט';
        }
    });


    // --- Initialization ---

    // Initial setup
    setupCanvas();
    initializeSnowflake(); // Reset state and start growing

    // Handle window resize
    window.addEventListener('resize', () => {
        // Stop current simulation temporarily during resize
        if (animationFrameId) {
             cancelAnimationFrame(animationFrameId);
             animationFrameId = null; // Clear the ID
        }
        setupCanvas(); // Re-setup canvas size and context translation
        // Re-calculate max arm length based on new size
        maxArmLength = Math.min(canvas.width, canvas.height) * 0.45;
        // Restart simulation from current state (it will adapt growth rates to new size)
        // Or, maybe better, reset completely on resize? Reset feels safer for consistency.
        resetSimulation(); // Reset and start fresh on resize
    });

     // Initial update of humidity qualitative value and temperature value display
     humiditySlider.dispatchEvent(new Event('input'));
     tempSlider.dispatchEvent(new Event('input'));


</script>
```