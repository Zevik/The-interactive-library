---
title: "המסע המופלא של הר הגעש אל תוך הים: הולדת האטול הקסום"
english_slug: the-amazing-journey-of-the-volcano-into-the-sea-the-birth-of-the-magical-atoll
category: "מדעי הסביבה / כדור הארץ"
tags:
  - אטול
  - שונית אלמוגים
  - הר געש
  - גיאולוגיה
  - אוקיינוגרפיה
---
# המסע המופלא של הר הגעש אל תוך הים: הולדת האטול הקסום

דמיינו אי טרופי יפהפה, פסגתו מחודדת ונישאת מעל פני הים התכולים. כעת דמיינו מסע בזמן, שבו האי שוקע אט אט, והחיים התוססים שסביבו בונים מבנה מדהים במקומו. זהו סיפורה של הולדת האטול - טבעת אלמוגים קסומה הצפה בלב האוקיינוס. איך קורה הקסם הגיאולוגי-ביולוגי הזה? בואו נצלול פנימה!

<div class="atoll-simulation-container">
    <h2>חקרו את הולדת האטול</h2>
    <div class="atoll-canvas-wrapper">
        <canvas id="atollCanvas" width="700" height="450"></canvas>
        <div id="waterOverlay"></div> <!-- For water effects -->
    </div>
    <div class="controls">
        <input type="range" id="stageSlider" min="0" max="100" value="0">
        <span id="stageLabel" class="control-label">שלב ההתפתחות: הר געש צעיר ושונית חופית</span>
    </div>
     <div id="dynamicTextOverlay" class="dynamic-overlay"></div> <!-- For dynamic text -->
</div>

<style>
/* General Styles */
body {
    font-family: 'Arial', sans-serif; /* Use a standard, clean font */
    line-height: 1.6;
    color: #333;
    background-color: #f4f4f4;
}

h1, h2, h3 {
    color: #0056b3; /* Deep blue for headings */
    text-align: center;
    margin-bottom: 20px;
}

/* Simulation Container */
.atoll-simulation-container {
    text-align: center;
    margin: 30px auto;
    max-width: 750px; /* Slightly wider for better visual */
    background: #ffffff;
    border-radius: 15px; /* More rounded corners */
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15); /* Softer, larger shadow */
    padding: 25px;
    position: relative; /* For overlay positioning */
    overflow: hidden; /* Keep everything inside */
}

.atoll-simulation-container h2 {
    margin-top: 0;
    color: #007bff; /* Lighter blue for simulation title */
    font-size: 1.8em;
}

/* Canvas Wrapper for effects */
.atoll-canvas-wrapper {
    position: relative;
    width: 100%;
    max-width: 700px; /* Match canvas width */
    margin: 0 auto 20px auto;
    border: 1px solid #007bff; /* Match simulation title color */
    border-radius: 10px; /* Rounded canvas border */
    overflow: hidden; /* Hide anything drawn outside */
    box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.1); /* Inner shadow for depth */
    background-color: #a0e0ff; /* Base water color */
}

#atollCanvas {
    display: block;
    width: 100%; /* Make canvas responsive within wrapper */
    height: auto; /* Maintain aspect ratio */
}

/* Water Overlay (Subtle animation/effect) */
#waterOverlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none; /* Allow clicks to pass through */
    background: linear-gradient(to bottom, rgba(160, 224, 255, 0.1) 0%, rgba(160, 224, 255, 0.3) 50%, rgba(160, 224, 255, 0.5) 100%); /* Subtle gradient */
    opacity: 0.8; /* Slightly transparent */
    /* Add subtle animation later with JS if needed, or keep static gradient */
}


/* Controls */
.controls {
    margin-top: 15px;
    display: flex; /* Use flexbox for layout */
    align-items: center; /* Vertically align */
    justify-content: center; /* Center content */
    flex-wrap: wrap; /* Allow wrapping on small screens */
    padding: 0 10px; /* Add some padding */
}

#stageSlider {
    flex-grow: 1; /* Allow slider to take available space */
    margin: 0 15px; /* Space around slider */
    height: 8px; /* Thicker slider track */
    -webkit-appearance: none; /* Remove default styles */
    appearance: none;
    background: #ddd;
    outline: none;
    opacity: 0.9;
    transition: opacity .2s;
    border-radius: 5px;
}

#stageSlider:hover {
    opacity: 1;
}

/* Custom slider thumb */
#stageSlider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px; /* Thumb size */
    height: 20px;
    background: #007bff; /* Thumb color */
    cursor: pointer;
    border-radius: 50%; /* Round thumb */
    border: 2px solid #fff; /* White border */
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    transition: background .3s ease-in-out;
}

#stageSlider::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #007bff;
    cursor: pointer;
    border-radius: 50%;
    border: 2px solid #fff;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    transition: background .3s ease-in-out;
}


.control-label {
    font-weight: normal; /* Not necessarily bold */
    color: #555;
    font-size: 1.1em;
    min-width: 250px; /* Ensure space for longer labels */
    text-align: right; /* Align right for RTL */
    white-space: nowrap; /* Prevent label wrapping if possible */
}

/* Dynamic text overlay */
.dynamic-overlay {
     position: absolute;
     top: 50%; /* Center vertically */
     left: 50%; /* Center horizontally */
     transform: translate(-50%, -50%); /* Perfect centering */
     font-size: 2em; /* Large text */
     font-weight: bold;
     color: rgba(255, 255, 255, 0.8); /* White with transparency */
     text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5); /* Text shadow for readability */
     pointer-events: none; /* Do not block interactions */
     z-index: 10; /* Above canvas */
}


/* Explanation Section */
#toggleExplanation {
    display: block;
    margin: 30px auto;
    padding: 12px 25px; /* Larger padding */
    font-size: 1.2em; /* Larger text */
    cursor: pointer;
    border: none;
    border-radius: 8px; /* Rounded button */
    background-color: #007bff; /* Blue button */
    color: white;
    transition: background-color 0.3s ease; /* Smooth transition */
    box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3); /* Button shadow */
}

#toggleExplanation:hover {
    background-color: #0056b3; /* Darker blue on hover */
}

.explanation {
    margin-top: 40px; /* More space */
    border-top: 2px solid #eee; /* Thicker separator */
    padding-top: 30px;
    display: none; /* Initially hidden */
    text-align: right; /* RTL */
    background: #f9f9f9; /* Light background for explanation */
    padding: 20px;
    border-radius: 10px;
}

.explanation h2 {
    text-align: center;
    margin-bottom: 25px;
    color: #0056b3;
}

.explanation p, .explanation ul {
    line-height: 1.7; /* Improved readability */
    margin-bottom: 20px;
    color: #555;
}

.explanation ul {
    padding-right: 25px; /* RTL padding */
    list-style: disc; /* Standard bullet points */
}

.explanation li {
    margin-bottom: 10px;
}

.explanation strong {
    color: #007bff; /* Highlight key terms */
}

.hidden {
    display: none;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .atoll-simulation-container {
        padding: 15px;
        margin: 20px auto;
    }
    .controls {
        flex-direction: column; /* Stack controls vertically */
        align-items: stretch;
    }
    #stageSlider {
        width: 100%; /* Slider full width */
        margin: 10px 0;
    }
    .control-label {
        text-align: center; /* Center label when stacked */
        min-width: auto;
    }
    #toggleExplanation {
        padding: 10px 20px;
        font-size: 1.1em;
    }
    .explanation {
        padding: 15px;
    }
    .dynamic-overlay {
        font-size: 1.5em;
    }
}

</style>

<button id="toggleExplanation">הצג/הסתר את הסבר המסע המלא</button>

<div id="explanationContent" class="explanation hidden">
    <h2>המסע המופלא של היווצרות האטול</h2>
    <p><strong>אטול</strong> הוא פלא גיאולוגי וביולוגי כאחד: טבעת קסומה של שונית אלמוגים, המקיפה לגונה שלווה במקום שבו פעם נישא הר געש. מבנים איקוניים אלה, המנקדים את האוקיינוסים הטרופיים, מספרים סיפור ארוך ומרתק על תהליכים קוסמיים וביולוגיים.</p>
    <p>ההסבר המדעי המקובל ביותר להולדת האטול, שפותח לראשונה על ידי החוקר הדגול צ'ארלס דרווין במסעו האגדי על ספינת ביגל, קושר את גורל האי הגעשי לזה של שונית האלמוגים הצומחת סביבו.</p>

    <h3>שלבי המסע: מאי געשי לאטול טבעתי</h3>
    <p>המסע מתחיל עמוק בלב האוקיינוס, כאשר <strong>נקודה חמה</strong> מתחת לקרום כדור הארץ יוצרת זרימת מאגמה שמבקיעה את דרכה כלפי מעלה. לאורך אלפי או מיליוני שנים, התפרצויות חוזרות ונשנות בונות הר געש תת-ימי, שצומח בסופו של דבר מעל פני המים ויוצר אי געשי חדש ופורה.</p>
    <ul>
        <li><strong>השלב הראשון: לידת האי והשונית החופית</strong><br>
        כשהאי הגעשי צעיר ובולט מעל פני הים, המים החמים והצלולים סביבו הם סביבה מושלמת לצמיחת אלמוגים. מושבות האלמוגים מתחילות לבנות את שלדיהן הסידניים ממש בסמוך לחופי האי, ויוצרות <strong>שונית חופית (Fringing Reef)</strong> הצמודה ליבשה או מופרדת ממנה על ידי לגונה רדודה וצרה.</li>
        <li><strong>השלב השני: שקיעת האי והולדת שונית המחסום</strong><br>
        הסיפור מקבל תפנית כשהאי הגעשי מתחיל לשקוע בהדרגה. שקיעה זו מתרחשת בעיקר משום שהלוח הטקטוני עליו יושב ההר זז בהדרגה אל מחוץ לאזור ה"נקודה החמה" שסיפק לו מאגמה, מה שגורם להפסקת צמיחתו ולקירורו, ומכיוון שהקרום עצמו מתקרר ומתכווץ מעט. האלמוגים, התלויים באור השמש לצורך קיומם (הודות לאצות שחיות בסימביוזה בתוכם), חייבים לצמוח כלפי מעלה כדי להישאר באזור המואר הרדוד. הם צומחים בקצב כזה שהם מפצים על שקיעת קרקעית הים. עיקר הצמיחה מתרחשת בשוליים החיצוניים של השונית. ככל שהאי שוקע, המרחק בין שרידי האי הטובע לבין השונית הצומחת גדל, ונוצרת <strong>שונית מחסום (Barrier Reef)</strong>, המופרדת מהאי על ידי לגונה רחבה ועמוקה יותר.</li>
        <li><strong>השלב השלישי: האי נעלם, האטול נולד</strong><br>
        המסע מגיע לשיאו כאשר האי הגעשי שוקע לחלוטין אל מתחת לפני הים (למעט אולי שריד זעיר). שונית האלמוגים ממשיכה לצמוח כלפי מעלה במעגל שהיה פעם קו החוף של האי, ועתה היא יוצרת טבעת מושלמת של אלמוגים המקיפה <strong>לגונה מרכזית</strong>. זוהי הולדת ה<strong>אטול</strong>. הלגונה שוכנת מעל פסגת ההר הגעשי השקוע ומכילה לרוב מים שקטים ורדודים יחסית לים הפתוח שמסביב.</li>
    </ul>

    <p><strong>מדוע האלמוגים מצליחים להישאר למעלה בעוד שהאי שוקע?</strong> זהו מרוץ בין שקיעת קרקעית הים לבין קצב צמיחת האלמוגים. בתנאים הנכונים (מים חמים, צלולים ומוארים), האלמוגים יכולים לצמוח במהירות שמפצה על שקיעת הקרקעית, וכך לשמור על עצמם בטווח העומק המתאים לאור השמש החיוני לקיומם.</p>
    <p>אטולים הם עדויות מרשימות לתהליכים גיאולוגיים ארוכי טווח ולכוחה המדהים של הביולוגיה לבנות מבנים בקנה מידה פלנטרי. הם לא סתם איים יפים, אלא אנדרטאות טבעיות למסע בן מיליוני שנים.</p>
</div>

<script>
const canvas = document.getElementById('atollCanvas');
const ctx = canvas.getContext('2d');
const slider = document.getElementById('stageSlider');
const stageLabel = document.getElementById('stageLabel');
const explanationContent = document.getElementById('explanationContent');
const toggleButton = document.getElementById('toggleExplanation');
const dynamicTextOverlay = document.getElementById('dynamicTextOverlay');

// --- Drawing Parameters and Interpolation ---
// Define key parameters at different stages (0, 0.5, 1 representing progress)
const params = {
    volcanoHeight: [canvas.height * 0.6, canvas.height * 0.3, 0], // Peak Y relative to top
    volcanoBaseWidth: [160, 200, 220], // Base width
    volcanoPeakWidth: [10, 20, 30], // Width near the peak (for smoother shape)
    reefOuterRadius: [120, 180, 220], // Distance of outer reef edge from center X
    reefInnerRadius: [90, 110, 130], // Distance of inner reef edge (for lagoon)
    lagoonDepth: [0, 50, 100], // Visual indication of lagoon depth/size relative to base Y
    waterLevel: [canvas.height * 0.8, canvas.height * 0.85, canvas.height * 0.9] // Base Y position
};

// Simple linear interpolation
function lerp(start, end, t) {
    return start + (end - start) * t;
}

// Smoother interpolation between specific stages (optional, linear is often fine for sliders)
// function smoothStep(t) { return t * t * (3 - 2 * t); } // E.g., smooth progression

// Map slider value (0-100) to progress (0-1)
function getProgress(sliderValue) {
    return sliderValue / 100;
}

// Get interpolated value for a parameter based on progress (t from 0 to 1)
function getInterpolatedParam(paramName, t) {
    const values = params[paramName];
    if (t <= 0.5) {
        // Interpolate between stage 0 (t=0) and stage 1 (t=0.5)
        const local_t = t * 2; // Scale t from 0-0.5 to 0-1 for this interval
        return lerp(values[0], values[1], local_t);
    } else {
        // Interpolate between stage 1 (t=0.5) and stage 2 (t=1)
        const local_t = (t - 0.5) * 2; // Scale t from 0.5-1 to 0-1 for this interval
         return lerp(values[1], values[2], local_t);
    }
}

// --- Drawing Functions ---
function draw(progress) {
    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Get interpolated parameters
    const currentVolcanoHeight = getInterpolatedParam('volcanoHeight', progress);
    const currentVolcanoBaseWidth = getInterpolatedParam('volcanoBaseWidth', progress);
    const currentVolcanoPeakWidth = getInterpolatedParam('volcanoPeakWidth', progress);
    const currentReefOuterRadius = getInterpolatedParam('reefOuterRadius', progress);
    const currentReefInnerRadius = getInterpolatedParam('reefInnerRadius', progress);
    const currentWaterLevel = getInterpolatedParam('waterLevel', progress);
    const currentLagoonDepth = getInterpolatedParam('lagoonDepth', progress); // Use for visual lagoon differentiation

    const centerX = canvas.width / 2;

    // Draw Sky (Gradient)
    const skyGradient = ctx.createLinearGradient(0, 0, 0, currentWaterLevel * 0.6);
    skyGradient.addColorStop(0, '#87CEEB'); // Light Sky Blue
    skyGradient.addColorStop(1, '#E0F6FF'); // Very Light Blue
    ctx.fillStyle = skyGradient;
    ctx.fillRect(0, 0, canvas.width, currentWaterLevel);

    // Draw Ocean (Gradient)
    const oceanGradient = ctx.createLinearGradient(0, currentWaterLevel, 0, canvas.height);
     // Adjust gradient stops based on progress for subtle color change
    oceanGradient.addColorStop(0, '#00BFFF'); // Deep Sky Blue at surface
    oceanGradient.addColorStop(progress * 0.5, '#1E90FF'); // Deeper blue as it sinks
    oceanGradient.addColorStop(1, '#00008B'); // Dark Blue at bottom
    ctx.fillStyle = oceanGradient;
    ctx.fillRect(0, currentWaterLevel, canvas.width, canvas.height - currentWaterLevel);


    // Draw Volcano (Visible part)
    if (currentVolcanoHeight > 0) {
        const volcanoColor = '#A0522D'; // Siennadark
        ctx.fillStyle = volcanoColor;
        ctx.beginPath();
        // Smoother volcano shape using quadratic curves
        ctx.moveTo(centerX, currentWaterLevel - currentVolcanoHeight); // Peak
        ctx.quadraticCurveTo(centerX + currentVolcanoPeakWidth, currentWaterLevel - currentVolcanoHeight * 0.5, centerX + currentVolcanoBaseWidth / 2, currentWaterLevel); // Right side curve
        ctx.lineTo(centerX - currentVolcanoBaseWidth / 2, currentWaterLevel); // Left base point
        ctx.quadraticCurveTo(centerX - currentVolcanoPeakWidth, currentWaterLevel - currentVolcanoHeight * 0.5, centerX, currentWaterLevel - currentVolcanoHeight); // Left side curve
        ctx.closePath();
        ctx.fill();
    }

    // Draw Submerged Volcano (Hint of what's below)
     if (progress > 0.3) { // Start showing submerged part after stage 1
        const submergedProgress = (progress - 0.3) / 0.7; // Scale 0.3-1 progress to 0-1
        const submergedAlpha = submergedProgress * 0.4; // Fades in
        const submergedColor = 'rgba(85, 107, 47, ' + submergedAlpha + ')'; // Dark Olive Green with alpha

        const submergedPeakY = currentWaterLevel + (canvas.height - currentWaterLevel) * (0.5 + submergedProgress * 0.3); // Sink deeper
        const submergedBaseWidth = lerp(currentVolcanoBaseWidth, currentVolcanoBaseWidth * 1.2, progress); // Base might spread slightly

        ctx.fillStyle = submergedColor;
        ctx.beginPath();
         // Simple bump for now
        ctx.arc(centerX, submergedPeakY, lerp(currentVolcanoBaseWidth/4, 30, progress), 0, Math.PI * 2, false);
        // Could draw a submerged mountain shape similar to the top one
        // ctx.moveTo(centerX, submergedPeakY - lerp(0, 50, submergedProgress)); // Higher point underwater
        // ctx.quadraticCurveTo(centerX + submergedBaseWidth / 3, submergedPeakY - lerp(0, 20, submergedProgress), centerX + submergedBaseWidth / 2, submergedPeakY);
        // ctx.lineTo(centerX - submergedBaseWidth / 2, submergedPeakY);
        // ctx.quadraticCurveTo(centerX - submergedBaseWidth / 3, submergedPeakY - lerp(0, 20, submergedProgress), centerX, submergedPeakY - lerp(0, 50, submergedProgress));
        // ctx.closePath();
        ctx.fill();
     }


    // Draw Reef
    const reefColor = '#FF7F50'; // Coral color (adjust opacity based on depth?)
    ctx.fillStyle = reefColor;

    ctx.beginPath();
    // Outer arc (always visible boundary)
    ctx.arc(centerX, currentWaterLevel, currentReefOuterRadius, Math.PI, 0, false);

    // Inner boundary (changes based on reef type/lagoon)
    if (progress < 0.3) { // Fringing reef - inner boundary is the island base
        // Draw reef as a solid shape attached to the island base
         ctx.lineTo(centerX + currentVolcanoBaseWidth / 2, currentWaterLevel); // Go down to base
         ctx.arc(centerX, currentWaterLevel, currentVolcanoBaseWidth / 2 + 5, Math.PI, 0, true); // Follow island base contour slightly wider
         ctx.lineTo(centerX - currentVolcanoBaseWidth / 2, currentWaterLevel); // Go down to base
         ctx.closePath(); // Close back to the start (outer arc left)

    } else { // Barrier or Atoll reef - inner boundary is the lagoon edge
        ctx.lineTo(centerX + currentReefOuterRadius, currentWaterLevel); // Move to right outer edge
        ctx.arc(centerX, currentWaterLevel, currentReefInnerRadius, 0, Math.PI, true); // Inner arc for lagoon (clockwise)
        ctx.lineTo(centerX - currentReefOuterRadius, currentWaterLevel); // Move to left outer edge
         ctx.closePath(); // Close back to the start (outer arc left)
    }

    ctx.fill();

     // Draw Lagoon (as a lighter area *inside* the reef)
    if (progress > 0.1) { // Start showing lagoon effect early
        const lagoonColor = 'rgba(160, 224, 255, ' + Math.min(1, (progress - 0.1) * 2) + ')'; // Lighter blue, fades in
        const lagoonRadius = currentReefInnerRadius * 0.95; // Slightly smaller than inner reef radius
        ctx.fillStyle = lagoonColor;
        ctx.beginPath();
        // Draw a circle for the lagoon inside the reef
        ctx.arc(centerX, currentWaterLevel, lagoonRadius, 0, Math.PI * 2, false);
        ctx.fill();
    }


    // Add simple wave effect (optional, visual flourish)
    // Draw a slightly wavy line for the water surface
    ctx.strokeStyle = '#007bff';
    ctx.lineWidth = 2;
    ctx.beginPath();
    const waveAmplitude = 5; // Height of waves
    const waveFrequency = 0.02; // How many waves across the screen
    const time = Date.now() * 0.001; // Use time for animation (or progress for static effect)

    ctx.moveTo(0, currentWaterLevel + Math.sin(0 * waveFrequency + time * 2) * waveAmplitude);
    for (let x = 0; x <= canvas.width; x += 10) {
        // Use quadratic curve to draw segments
        const y = currentWaterLevel + Math.sin(x * waveFrequency + time * 2) * waveAmplitude;
        ctx.lineTo(x, y); // Simple line segments
        // For smoother waves: ctx.quadraticCurveTo(x - 5, currentWaterLevel + Math.sin((x-5) * waveFrequency + time*2) * waveAmplitude, x, y);
    }
     ctx.lineTo(canvas.width, currentWaterLevel); // Ensure line reaches edge
    ctx.stroke();


    // Update dynamic text overlay (optional, more descriptive text changes)
     let overlayText = '';
     if (progress < 0.1) overlayText = 'הר געש צעיר';
     else if (progress < 0.4) overlayText = 'האי גדל, שונית חופית';
     else if (progress < 0.7) overlayText = 'האי שוקע, שונית מחסום מתרחקת';
     else if (progress < 0.9) overlayText = 'כמעט אטול מלא';
     else overlayText = 'אטול נוצר!';

     // Animate opacity based on when text changes
     const fadeDuration = 0.1; // Progress range over which to fade
     let opacity = 1;
     if (progress % 0.3 < fadeDuration || (1 - progress) % 0.3 < fadeDuration ) { // Fade near transition points (rough check)
         // Simple fade out/in logic near transition points
          // Need a more robust way to manage text changes and fades, maybe state machine or timestamps.
          // For simplicity, let's just update text instantly based on range for now.
     }
     // dynamicTextOverlay.style.opacity = opacity; // Disabled for now

     dynamicTextOverlay.textContent = ''; // Clear the text overlay to avoid conflict with label

}

// --- Event Handlers and Initialization ---

const stageLabels = [
    { threshold: 0, text: 'שלב 1: הר געש צעיר ושונית חופית' },
    { threshold: 35, text: 'שלב 2: האי שוקע, שונית מחסום נוצרת ולגונה מתרחבת' },
    { threshold: 70, text: 'שלב 3: האי נעלם לחלוטין, האטול נוצר!' }
];

function updateSimulation(sliderValue) {
    const progress = getProgress(sliderValue);

    // Update drawing
    draw(progress);

    // Update label
    let currentLabel = stageLabels[0].text;
    for (let i = 0; i < stageLabels.length; i++) {
        if (sliderValue >= stageLabels[i].threshold) {
            currentLabel = stageLabels[i].text;
        }
    }
     // Add visual cue for progress within the current stage
     if (sliderValue < stageLabels[1].threshold) {
         currentLabel += ` (${Math.round(sliderValue / stageLabels[1].threshold * 100)}% לקראת שונית מחסום)`;
     } else if (sliderValue < stageLabels[2].threshold) {
          const localProgress = (sliderValue - stageLabels[1].threshold) / (stageLabels[2].threshold - stageLabels[1].threshold);
           currentLabel += ` (${Math.round(localProgress * 100)}% לקראת אטול מלא)`;
     } else {
          currentLabel += ` (הושלם!)`;
     }


    stageLabel.textContent = currentLabel;
}

slider.addEventListener('input', (event) => {
    updateSimulation(parseInt(event.target.value));
});

toggleButton.addEventListener('click', () => {
    const isHidden = explanationContent.classList.contains('hidden');
    if (isHidden) {
        explanationContent.classList.remove('hidden');
        toggleButton.textContent = 'הסתר את הסבר המסע המלא';
    } else {
        explanationContent.classList.add('hidden');
        toggleButton.textContent = 'הצג/הסתר את הסבר המסע המלא';
    }
});

// Initial draw based on slider default value
updateSimulation(parseInt(slider.value));

// Optional: Add a subtle animation loop for water/sky if needed, independent of slider
// function animateWater() {
//     updateSimulation(parseInt(slider.value)); // Redraw based on current slider position to include time component
//     requestAnimationFrame(animateWater);
// }
// animateWater(); // Start animation loop

</script>