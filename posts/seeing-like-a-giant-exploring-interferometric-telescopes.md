---
title: "לראות כמו ענק: לחשוף את היקום עם אינטרפרומטריה טלסקופית"
english_slug: seeing-like-a-giant-exploring-interferometric-telescopes
category: "מדעים מדויקים / אסטרונומיה"
tags: ["אינטרפרומטריה", "טלסקופים", "רזולוציה", "אסטרונומיה", "גלים", "מערך טלסקופים", "UV plane"]
---
# לראות כמו ענק: לחשוף את היקום עם אינטרפרומטריה טלסקופית

תארו לעצמכם שאתם מנסים לראות מטבע על פני הירח! משימה בלתי אפשרית עבור טלסקופ יחיד על פני כדור הארץ, נכון? כושר ההפרדה, או היכולת לראות פרטים קטנים, של טלסקופ יחיד מוגבל על ידי גודל המראה שלו. גדול יותר = טוב יותר. אבל מה קורה כשאנחנו רוצים "לראות" בחדות של טלסקופ בגודל יבשת? ברוכים הבאים לעולם המופלא של האינטרפרומטריה!

במקום לבנות מראה יחידה בגודל דמיוני, טלסקופי אינטרפרומטריה משתמשים בכוחם של רבים: הם משלבים מידע ממספר טלסקופים הפזורים על שטח נרחב, ויוצרים ביחד "טלסקופ וירטואלי" בקוטר עצום - לפעמים אלפי קילומטרים! בואו נחקור איך זה עובד בסימולציה אינטראקטיבית זו.

<div id="interferometry-app" dir="rtl">
    <h2>סימולציה: כוחם של בסיסי-קווים</h2>
    <p>שחקו עם מספר הטלסקופים והמרחק המקסימלי ביניהם כדי לראות איך זה משפיע על ה"אפרטורה הסינתטית" שלכם, שהיא למעשה סך כל ה"בסיסי-קווים" - המרחקים בין כל זוג טלסקופים במערך.</p>

    <div class="controls">
        <div class="control-group">
            <label for="num-telescopes">מספר "טלסקופים" במערך:</label>
            <input type="range" id="num-telescopes" min="2" max="30" value="5">
            <span id="num-telescopes-value">5</span>
        </div>

        <div class="control-group">
            <label for="max-distance">גודל המערך (מרחק מקסימלי - יחידות שרירותיות):</label>
            <input type="range" id="max-distance" min="50" max="1000" value="500">
            <span id="max-distance-value">500</span>
        </div>
        <!-- Wavelength control removed for simulation focus on baselines geometry -->
    </div>

    <div class="canvas-container">
        <div class="canvas-item">
            <h3>פריסת הטלסקופים</h3>
            <p class="canvas-description">מקמו טלסקופים בשטח. השטח המקסימלי שווה לגודל המערך.</p>
            <canvas id="telescope-layout-canvas" width="400" height="400"></canvas>
            <div id="max-baseline-display">בסיס-קו מקסימלי: <span id="max-baseline-value">0</span> יח'.</div>
        </div>
        <div class="canvas-item">
            <h3>האפרטורה הסינתטית (מישור u-v)</h3>
             <p class="canvas-description">כל נקודה כאן מייצגת בסיס-קו בין זוג טלסקופים. צפיפות ופיזור הנקודות מגדירים את כושר ההפרדה.</p>
            <canvas id="aperture-synthesis-canvas" width="400" height="400"></canvas>
             <div id="uv-extent-display">היקף u-v מקסימלי: <span id="uv-extent-value">0</span> יח'.</div>
        </div>
    </div>
</div>

<style>
/* כללי */
#interferometry-app {
    font-family: 'Arial', sans-serif; /* Use a common, clean font */
    padding: 25px;
    background: linear-gradient(to bottom right, #1a2a3a, #2a3a4a); /* Subtle dark gradient */
    border-radius: 12px;
    margin-bottom: 30px;
    text-align: right;
    color: #e0e0e0; /* Light grey text */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); /* Deeper shadow */
}

#interferometry-app h2 {
    text-align: center;
    color: #7fc9ff; /* Bright blue for headings */
    margin-bottom: 20px;
    font-size: 2em; /* Larger heading */
    text-shadow: 0 0 5px rgba(127, 201, 255, 0.5); /* Subtle glow */
}

#interferometry-app h3 {
    text-align: center;
    color: #b3e0ff; /* Lighter blue */
    margin-bottom: 10px;
    font-size: 1.5em;
}

#interferometry-app p {
    text-align: center;
    margin-bottom: 20px;
    line-height: 1.6;
}

.canvas-description {
    font-size: 0.9em;
    color: #c0c0c0; /* Slightly darker grey */
    margin-top: -10px; /* Pull closer to heading */
    min-height: 30px; /* Reserve space */
}


/* Controls Styling */
.controls {
    display: flex;
    flex-direction: column;
    gap: 20px; /* Increased gap */
    margin-bottom: 30px;
    align-items: center; /* Center controls group */
    background-color: #253545; /* Darker background for controls */
    padding: 20px;
    border-radius: 8px;
    width: 80%; /* Limit width */
    max-width: 600px; /* Max width */
    margin-left: auto; /* Center the block */
    margin-right: auto;
    box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.2); /* Inner shadow */
}

.control-group {
     display: flex;
     flex-direction: row; /* Arrange label and input horizontally */
     align-items: center;
     justify-content: space-between; /* Space out label and input */
     width: 100%; /* Take full width of controls container */
}

.controls label {
    font-weight: bold;
    color: #e0e0e0;
    flex-grow: 1; /* Allow label to take space */
    text-align: right; /* Align label right */
    margin-left: 15px; /* Space after label */
    min-width: 150px; /* Ensure labels have enough space */
}

.controls input[type="range"] {
    width: 50%; /* Control slider width */
    direction: ltr;
    -webkit-appearance: none; /* Hide default slider */
    appearance: none;
    height: 8px;
    background: #556778; /* Slider track color */
    outline: none;
    opacity: 0.9;
    transition: opacity .2s;
    border-radius: 4px;
}

.controls input[type="range"]:hover {
    opacity: 1;
}

.controls input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    background: #7fc9ff; /* Slider thumb color */
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.controls input[type="range"]::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #7fc9ff;
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}


.controls span {
    min-width: 40px; /* Ensure value has enough space */
    display: inline-block;
    text-align: left;
    color: #b3e0ff;
    font-weight: bold;
}


/* Canvas Container & Items */
.canvas-container {
    display: flex;
    flex-wrap: wrap; /* Allow wrapping on smaller screens */
    justify-content: center;
    gap: 30px; /* Increased gap between canvases */
}

.canvas-item {
    text-align: center;
    background-color: #253545; /* Darker background for canvas items */
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Subtle shadow */
    min-width: 300px;
    flex-grow: 1; /* Allow items to grow */
    max-width: 450px; /* Max width for larger screens */
    display: flex; /* Use flex to arrange contents */
    flex-direction: column;
    align-items: center;
}


canvas {
    border: 1px solid #556778; /* Border color matching slider track */
    background-color: #1a2a3a; /* Very dark background for canvas */
    margin-bottom: 15px;
    border-radius: 6px;
}

#max-baseline-display, #uv-extent-display {
    font-size: 0.9em;
    color: #c0c0c0;
    margin-top: 5px;
}

#max-baseline-value, #uv-extent-value {
    font-weight: bold;
    color: #b3e0ff;
}


/* Explanation Toggle Button */
button#toggle-explanation {
    display: block;
    margin: 30px auto; /* Center button */
    padding: 12px 25px; /* Larger padding */
    font-size: 1.1em;
    cursor: pointer;
    background: linear-gradient(to right, #007bff, #0056b3); /* Blue gradient */
    color: white;
    border: none;
    border-radius: 6px;
    transition: all 0.3s ease; /* Smooth transition for hover */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

button#toggle-explanation:hover {
    background: linear-gradient(to right, #0056b3, #003d82);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
    transform: translateY(-2px); /* Slight lift effect */
}

button#toggle-explanation:active {
    transform: translateY(0); /* Press effect */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

/* Explanation Block */
#explanation {
    display: none; /* Initially hidden */
    margin-top: 20px;
    padding: 25px;
    background-color: #253545; /* Matching controls background */
    border-right: 5px solid #7fc9ff; /* Blue border on the right for RTL */
    border-radius: 8px;
    color: #e0e0e0;
    line-height: 1.7; /* Increased line height */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    text-align: right; /* Ensure text is right aligned */
}

#explanation h2 {
    color: #7fc9ff; /* Matching heading color */
    margin-top: 0;
    margin-bottom: 15px;
    font-size: 1.8em;
    text-align: right; /* Align explanation heading right */
    text-shadow: none; /* Remove glow from explanation heading */
}

#explanation p {
    margin-bottom: 18px; /* Increased spacing */
    text-align: right; /* Ensure text is right aligned */
}

#explanation ul {
    margin-bottom: 18px;
    padding-right: 20px; /* Add padding for bullets */
    list-style: disc outside; /* Use discs, outside the padding */
    text-align: right; /* Ensure list is right aligned */
}

#explanation li {
    margin-bottom: 10px;
    text-align: right; /* Ensure list items are right aligned */
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .controls {
        width: 95%;
        padding: 15px;
        gap: 15px;
    }
    .control-group {
        flex-direction: column; /* Stack label and input vertically */
        align-items: flex-end; /* Align items to the right */
    }
     .controls label {
         width: 100%; /* Label takes full width */
         text-align: right; /* Ensure label is right-aligned */
         margin-left: 0; /* Remove left margin */
         margin-bottom: 5px; /* Space below label */
    }
    .controls input[type="range"] {
        width: 95%; /* Slider takes more width */
    }
    .controls span {
         width: 100%;
         text-align: right; /* Align value right */
    }
    .canvas-container {
        flex-direction: column; /* Stack canvases vertically */
        gap: 20px;
    }
    .canvas-item {
        padding: 15px;
    }
    canvas {
        width: 100%; /* Canvases take full width */
        height: auto; /* Height adjusts */
    }
}

</style>

<button id="toggle-explanation">הצג/הסתר הסבר: הכוח של אינטרפרומטריה</button>

<div id="explanation">
    <h2>הסבר: הכוח האדיר של אינטרפרומטריה טלסקופית</h2>

    <p>מדוע טלסקופים גדולים יותר רואים טוב יותר? התשובה טמונה בתופעת העקיפה (דיפרקציה). אור שמגיע ממקור רחוק יוצר תבנית עקיפה כשהוא עובר דרך צמצם (הפתח או המראה של הטלסקופ). ככל שהצמצם גדול יותר, תבנית העקיפה קטנה יותר, וזה אומר ששני אובייקטים קרובים בשמיים ייראו בנפרד ולא כמקור מטושטש אחד. כושר ההפרדה הטוב ביותר האפשרי לטלסקופ יחיד נתון על ידי יחס פשוט: אורך הגל הנצפה חלקי קוטר הטלסקופ.</p>

    <p>ככל שאנו צופים באורכי גל ארוכים יותר (כמו גלי רדיו) או רוצים לראות פרטים קטנים יותר (דורש רזולוציה גבוהה מאוד), היינו זקוקים לטלסקופים בקטרים בלתי נתפסים. בניית טלסקופים אופטיים יחידים מעבר לקוטר מסוים (כמו 8-10 מטרים) הופכת להיות מורכבת, יקרה וכמעט בלתי אפשרית הנדסית בגלל המשקל העצום והצורך לשמור על צורה מושלמת.</p>

    <p>כאן נכנסת לתמונה האינטרפרומטריה הטלסקופית - פתרון גאוני שמנצל את טבע הגלים של האור. במקום לאסוף אור במראה יחידה ענקית, מערך אינטרפרומטרי אוסף אור באמצעות מספר טלסקופים קטנים יותר המפוזרים על שטח גדול. האותות הנקלטים בכל טלסקופ נשלחים למעבד מרכזי.</p>

    <p>הקסם קורה כשהאותות משולבים. אור שמגיע ממקור רחוק מגיע לכל טלסקופ בזמנים שונים ועם הפרשי פאזה קטנים, בהתאם למיקום המדויק של כל טלסקופ במערך. כאשר משלבים את האותות הללו, הם יוצרים תבנית התאבכות - אזורים בהם הגלים מחזקים זה את זה (התאבכות בונה) ואזורים בהם הם מבטלים זה את זה (התאבכות הורסת). ניתוח מדוקדק של תבנית ההתאבכות הזו, המכונה "היכרות" (visibility), מאפשר לשחזר תמונה מפורטת של המקור האסטרונומי.</p>

    <p>התובנה המרכזית היא שכושר ההפרדה של מערך אינטרפרומטרי אינו נקבע על ידי גודל הטלסקופים הבודדים, אלא על ידי **המרחק המקסימלי בין שני טלסקופים כלשהם במערך**. מרחק זה נקרא "בסיס-קו" (baseline). ככל שהבסיס-קו המקסימלי גדול יותר, כך כושר ההפרדה של המערך גבוה יותר. למעשה, מערך אינטרפרומטרי עם בסיס-קו מקסימלי של 100 קילומטרים משיג רזולוציה השקולה לזו של טלסקופ יחיד עם מראה בקוטר 100 קילומטרים - זוהי ה"אפרטורה הסינתטית" (Synthetic Aperture) שראיתם בסימולציה.</p>

    <p>מישור ה-u-v בסימולציה מייצג למעשה את תבנית הדגימה של "האפרטורה הסינתטית" במרחב מסוים שקשור לתמונה אותה רוצים לשחזר. כל זוג טלסקופים במערך תורם נקודה (ובעצם שתי נקודות סימטריות) למישור זה, במיקום שנקבע על ידי וקטור הבסיס-קו ביניהם. ככל שיש יותר טלסקופים (יותר בסיסי-קווים, כלומר יותר נקודות במישור ה-u-v) וככל שהבסיסי-קווים ארוכים יותר (הנקודות מפוזרות רחוק יותר ממרכז מישור ה-u-v), כך תמונת האובייקט שתשוחזר תהיה מפורטת וחדה יותר. המערך "מכסה" את מישור ה-u-v ודוגם אותו בנקודות שונות.</p>

    <p>אינטרפרומטריה פתחה בפנינו צוהר ליקום ברזולוציות חסרות תקדים, במיוחד בתחומי הרדיו והאינפרה-אדום, שם אורכי הגל ארוכים יותר ומגבלת הדיפרקציה משמעותית יותר עבור טלסקופים יחידים. מערכים מפורסמים כמו ה-VLA, ה-VLTI, ו-ALMA מאפשרים לנו לחקור תופעות אסטרופיזיות בפירוט עוצר נשימה - מלידות כוכבים וכוכבי לכת, דרך גלקסיות רחוקות, ועד לאופק האירועים של חורים שחורים סופרמאסיביים (כמו במקרה של פרויקט ה-Event Horizon Telescope ששילב מערכי רדיו גלובליים ליצירת "טלסקופ" בגודל כדור הארץ).</p>
</div>


<script>
document.addEventListener('DOMContentLoaded', () => {
    const numTelescopesSlider = document.getElementById('num-telescopes');
    const numTelescopesValue = document.getElementById('num-telescopes-value');
    const maxDistanceSlider = document.getElementById('max-distance');
    const maxDistanceValue = document.getElementById('max-distance-value');
    const maxBaselineDisplay = document.getElementById('max-baseline-value');
    const uvExtentDisplay = document.getElementById('uv-extent-value');
    const layoutCanvas = document.getElementById('telescope-layout-canvas');
    const apertureCanvas = document.getElementById('aperture-synthesis-canvas');
    const toggleButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    const layoutCtx = layoutCanvas.getContext('2d');
    const apertureCtx = apertureCanvas.getContext('2d');

    let telescopes = [];
    const animationDuration = 300; // ms for simple animations

    function updateDisplayValues() {
        numTelescopesValue.textContent = numTelescopesSlider.value;
        maxDistanceValue.textContent = maxDistanceSlider.value;
    }

    function generateTelescopeLayout() {
        const num = parseInt(numTelescopesSlider.value);
        const maxDist = parseInt(maxDistanceSlider.value);
        telescopes = [];
        for (let i = 0; i < num; i++) {
            // Place telescopes randomly within a square area defined by maxDist
            // This gives a rectangular/square array capability, common in radio astronomy
            const x = (Math.random() * 2 - 1) * maxDist / 2; // Random x between -maxDist/2 and +maxDist/2
            const y = (Math.random() * 2 - 1) * maxDist / 2; // Random y between -maxDist/2 and +maxDist/2
            telescopes.push({ x: x, y: y });
        }
    }

     function findMaxBaseline() {
        let maxSqDist = 0;
        let tel1 = null;
        let tel2 = null;

        if (telescopes.length < 2) {
            return { distance: 0, tel1: null, tel2: null };
        }

        for (let i = 0; i < telescopes.length; i++) {
            for (let j = i + 1; j < telescopes.length; j++) {
                const dx = telescopes[i].x - telescopes[j].x;
                const dy = telescopes[i].y - telescopes[j].y;
                const sqDist = dx * dx + dy * dy;
                if (sqDist > maxSqDist) {
                    maxSqDist = sqDist;
                    tel1 = telescopes[i];
                    tel2 = telescopes[j];
                }
            }
        }
        return { distance: Math.sqrt(maxSqDist), tel1: tel1, tel2: tel2 };
    }


    function drawLayout(animationProgress = 1) {
        const canvasSize = layoutCanvas.width;
        const center = canvasSize / 2;
        const maxDist = parseInt(maxDistanceSlider.value);
        // Scale maxDist/2 (half the square side) to canvas edge
        const scale = (canvasSize / 2) / (maxDist / 2);

        layoutCtx.clearRect(0, 0, canvasSize, canvasSize);

        // Draw boundary square (optional, but good visualization of maxDist area)
        // layoutCtx.strokeStyle = '#444';
        // layoutCtx.strokeRect(center - maxDist/2 * scale, center - maxDist/2 * scale, maxDist * scale, maxDist * scale);


        // Draw center origin
        layoutCtx.fillStyle = '#888';
        layoutCtx.beginPath();
        layoutCtx.arc(center, center, 4, 0, Math.PI * 2);
        layoutCtx.fill();

         // Draw max baseline line
        const maxBaseline = findMaxBaseline();
        if (maxBaseline.tel1 && maxBaseline.tel2) {
            const x1 = center + maxBaseline.tel1.x * scale;
            const y1 = center + maxBaseline.tel1.y * scale;
            const x2 = center + maxBaseline.tel2.x * scale;
            const y2 = center + maxBaseline.tel2.y * scale;

            layoutCtx.strokeStyle = '#ff6666'; // Reddish for emphasis
            layoutCtx.lineWidth = 2;
            layoutCtx.beginPath();
            layoutCtx.moveTo(x1, y1);
            layoutCtx.lineTo(x2, y2);
            layoutCtx.stroke();

            // Update display value
            maxBaselineDisplay.textContent = maxBaseline.distance.toFixed(0); // Display integer value
        } else {
             maxBaselineDisplay.textContent = '0';
        }

        // Draw telescopes
        layoutCtx.fillStyle = '#7fc9ff'; // Blue color
        telescopes.forEach((tel, index) => {
             // Simple fade-in animation based on index and progress if needed,
             // For now, just draw based on current positions.
            layoutCtx.beginPath();
            // Scale and translate coordinates
            const drawX = center + tel.x * scale;
            const drawY = center + tel.y * scale;
            layoutCtx.arc(drawX, drawY, 6, 0, Math.PI * 2); // Slightly larger dots
            layoutCtx.fill();
        });
    }

    function drawApertureSynthesis(animationProgress = 1) {
        const canvasSize = apertureCanvas.width;
        const center = canvasSize / 2;
        const maxDist = parseInt(maxDistanceSlider.value);
        // The max baseline defines the max extent in the u-v plane
        const maxBaseline = findMaxBaseline().distance;
        // Scale the max baseline (max extent of u-v) to the canvas edge
        const uvScale = (canvasSize / 2) / maxBaseline;


        apertureCtx.clearRect(0, 0, canvasSize, canvasSize);

        // Draw center origin (represents baseline of telescope with itself - (0,0))
        apertureCtx.fillStyle = '#888';
        apertureCtx.beginPath();
        apertureCtx.arc(center, center, 4, 0, Math.PI * 2); // Larger dot for origin
        apertureCtx.fill();

        // Draw circle representing the full u-v extent
        if (maxBaseline > 0) {
             apertureCtx.strokeStyle = '#ff6666'; // Reddish for emphasis
             apertureCtx.lineWidth = 2;
             apertureCtx.beginPath();
             apertureCtx.arc(center, center, maxBaseline * uvScale, 0, Math.PI * 2);
             apertureCtx.stroke();

             // Update display value for uv extent
             uvExtentDisplay.textContent = (maxBaseline * 2).toFixed(0); // Diameter is max baseline * 2
        } else {
             uvExtentDisplay.textContent = '0';
        }


        // Draw uv points (baselines)
        apertureCtx.fillStyle = '#b3e0ff'; // Light blue points
        const pointSize = 2.5; // Slightly larger points

        // Add the (0,0) point explicitly again for clarity if needed, but origin arc covers it.
        // apertureCtx.beginPath();
        // apertureCtx.arc(center, center, pointSize, 0, Math.PI * 2);
        // apertureCtx.fill();

        let drawnPoints = 0;
        const totalPoints = telescopes.length * (telescopes.length - 1) / 2 * 2; // Number of unique baseline pairs * 2 (for symmetry)

        for (let i = 0; i < telescopes.length; i++) {
            for (let j = i + 1; j < telescopes.length; j++) {
                const tel_i = telescopes[i];
                const tel_j = telescopes[j];

                // Calculate baseline vector (u, v) relative to array center
                const u = (tel_i.x - tel_j.x) * uvScale;
                const v = (tel_i.y - tel_j.y) * uvScale;

                // Plot the (u, v) point
                 if (drawnPoints / totalPoints <= animationProgress) {
                    apertureCtx.beginPath();
                    apertureCtx.arc(center + u, center + v, pointSize, 0, Math.PI * 2);
                    apertureCtx.fill();
                    drawnPoints++;
                 }


                // Plot the (-u, -v) point (since baselines are symmetric)
                 if (drawnPoints / totalPoints <= animationProgress) {
                    apertureCtx.beginPath();
                    apertureCtx.arc(center - u, center - v, pointSize, 0, Math.PI * 2);
                    apertureCtx.fill();
                    drawnPoints++;
                 }
            }
        }
         // Simple animation: draw points gradually
         if (animationProgress < 1) {
             requestAnimationFrame(() => drawApertureSynthesis(animationProgress + 0.05)); // Adjust 0.05 for speed
         }
    }

    function updateSimulation() {
        generateTelescopeLayout(); // Regenerate random layout based on current sliders
        drawLayout(); // Draw layout immediately
        drawApertureSynthesis(); // Start aperture drawing animation
    }

    // Initial setup
    updateDisplayValues();
    updateSimulation();

    // Event listeners for controls - use 'change' for better performance or 'input' for continuous update
    numTelescopesSlider.addEventListener('change', () => {
        updateDisplayValues();
        updateSimulation(); // Update simulation on change
    });
     numTelescopesSlider.addEventListener('input', () => {
         updateDisplayValues(); // Only update value display continuously
     });


    maxDistanceSlider.addEventListener('change', () => {
        updateDisplayValues();
        updateSimulation(); // Update simulation on change
    });
    maxDistanceSlider.addEventListener('input', () => {
         updateDisplayValues(); // Only update value display continuously
    });


    // Explanation toggle
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר: הכוח של אינטרפרומטריה' : 'הצג/הסתר הסבר: הכוח של אינטרפרומטריה';
    });

    // Add a resize observer to redraw if canvas size changes (optional, more complex)
    // const resizeObserver = new ResizeObserver(entries => {
    //     for (let entry of entries) {
    //         if (entry.target.id === 'telescope-layout-canvas' || entry.target.id === 'aperture-synthesis-canvas') {
    //              // Need to potentially update canvas dimensions based on parent size
    //              // entry.target.width = entry.contentRect.width;
    //              // entry.target.height = entry.contentRect.height;
    //             updateSimulation(); // Redraw on resize
    //         }
    //     }
    // });
    // resizeObserver.observe(layoutCanvas.parentElement); // Observe the parent div
    // resizeObserver.observe(apertureCanvas.parentElement);

});
</script>