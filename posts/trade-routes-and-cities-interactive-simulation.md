---
title: "מסחר, דרכים וערים: מסע אינטראקטיבי"
english_slug: trade-routes-and-cities-interactive-simulation
category: "מדעי הסביבה / גאוגרפיה"
tags: [התיישבות, תכנון מרחבי, כלכלה, מודלים, התפתחות עירונית, סימולציה, גאוגרפיה היסטורית]
---

<h1>מסחר, דרכים וערים: מסע אינטראקטיבי אל לב הצמיחה העירונית</h1>

<p>האם אי פעם תהיתם מדוע ערים מסוימות הפכו למרכזים שוקקים ותוססים, בעוד אחרות נותרו כפרים קטנים או נבלו עם הזמן? לעיתים קרובות, התשובה נמצאת ברשת הנסתרת והדינמית של תנועה וחיבורים. הצטרפו למסע אינטראקטיבי וגלו כיצד דרכי מסחר עתיקות ומודרניות מעצבות את מפת ההתיישבות האנושית ויוצרות את הערים של עולמנו.</p>

<div class="simulation-container">
    <canvas id="tradeSimulationCanvas"></canvas>
    <div class="controls">
        <button id="startStopSimulation">התחל סימולציה</button>
        <label for="simulationSpeed">מהירות סימולציה:</label>
        <input type="range" id="simulationSpeed" min="0.1" max="5" value="1" step="0.1">
        <span id="currentSpeed">1x</span>
        <button id="clearRoutes">נקה הכל</button>
        <div class="instructions">
            <strong>איך לשחק:</strong>
            <br> לחצו וגררו על המפה כדי לצייר דרכי מסחר.
            <br> נקודות על הדרכים, צמתים, וקרבה למשאבים (⭐) יצברו "פוטנציאל".
            <br> ככל שנקודה צוברת יותר פוטנציאל, היא צומחת להיות יישוב גדול יותר!
            <br> לחצו על "התחל סימולציה" כדי לראות את הערים גדלות בזמן אמת.
        </div>
    </div>
</div>

<button id="toggleExplanation">הצג רקע תיאורטי ודוגמאות</button>

<div id="explanation" class="hidden">
    <h2>מעבר למפה: הרקע התיאורטי והיסטורי</h2>
    <p>ברוכים הבאים לסימולציה האינטראקטיבית של מסחר, דרכים וערים. כאן אתם הבמאים של ההיסטוריה, ויכולים לראות במו עיניכם כיצד קישוריות ותנועה בונות אימפריות ומרכזים עירוניים. הסימולציה מדגימה באופן פשטני אך עוצמתי את הקשר העמוק בין נתיבי תנועה להתפתחות מרחבית.</p>

    <h3>מהי דרך מסחר ומה תפקידה ההיסטורי?</h3>
    <p>דרך מסחר היא הרבה יותר מסתם שביל. היא עורק חיים שדרכו זורמים סחורות, טכנולוגיות, דתות, רעיונות ואנשים בין אזורים שונים. לאורך אלפי שנים, דרכים אלו היו הבסיס לשגשוג וקשר בין ציוויליזציות. הן אפשרו ייצור מיוחד באזור אחד וצריכתו באזור אחר, עודדו חדשנות, יצרו אינטגרציה תרבותית, והיו זרז לצמיחה כלכלית. דרכים אגדיות כמו דרך המשי, דרך הבשמים, או נתיבי סחר ימיים שינו את פני העולם.</p>

    <h3>הקשר בין דרכי מסחר ומיקום יישובים קדומים ומודרניים</h3>
    <p>אם תביטו במפה היסטורית או מודרנית, תגלו שיישובים רבים נולדו וצמחו בנקודות מפתח לאורך דרכי מסחר. מיקומים אסטרטגיים כללו: צומתי דרכים יבשתיות, נקודות מעבר בנהרות (מעבורות, גשרים), שפכי נהרות לים, נמלי ים טבעיים, מעברי הרים, או בסמוך למקורות חומרי גלם יקרי ערך. מיקום כזה העניק גישה נוחה לשווקים, הפך את היישוב למרכז שירותים (הספקה, לינה, תיקונים), ואף סיפק יתרונות הגנתיים או טופוגרפיים. גם בעידן המודרני, קרבה לצמתי תחבורה ראשיים (רכבות, כבישים מהירים, נמלי תעופה) ממשיכה להיות גורם קריטי לצמיחה כלכלית ודמוגרפית.</p>

    <h3>עקרונות מרכזיים במודלים של התיישבות: משיכה לקישוריות, אפקט צומת</h3>
    <p>מודלים רבים בגאוגרפיה, כלכלה וסוציולוגיה מנתחים את חשיבותה של "קישוריות" (Connectivity) ו"מרכזיות" (Centrality) ברשתות. ככל שמקום מחובר יותר ביעילות לרשת רחבה יותר של מקומות אחרים, כך גדל הפוטנציאל שלו למשוך פעילות, אוכלוסייה והשקעות. נקודות צומת, בהן מספר דרכים נפגשות, נהנות מיתרון מיוחד הנקרא "אפקט הצומת" (Junction Effect). נקודות אלו הופכות טבעית למרכזי מעבר, הפצה וריכוז, ומושכות אליהן יותר תנועה ופעילות מאשר נקודות בודדות על דרך אחת.</p>

    <h3>איך נוצר 'משוב חיובי': התיישבות מושכת עוד מסחר, שמביא עוד התיישבות</h3>
    <p>צמיחת יישובים במוקדי קישוריות יוצרת לרוב דינמיקה של "משוב חיובי" (Positive Feedback Loop). ככל שיישוב גדל, הוא הופך בעצמו ליעד משמעותי למסחר, ייצור וצריכה. זה מגדיל את התנועה על הדרכים המובילות אליו וממנו, מה שמחזק את חשיבותן של הדרכים ואת הפוטנציאל של נקודות אחרות לאורכן. תהליך זה יכול להוביל לצמיחה מהירה של מוקדים מרכזיים ולדיכוי יחסי של אזורים פחות מחוברים.</p>

    <h3>דוגמאות היסטוריות וגיאוגרפיות לקשר זה</h3>
    <ul>
        <li><strong>דרכי המשי:</strong> רשת נתיבי מסחר ענפה שקישרה את אירופה, אסיה ואפריקה. ערים כמו סמרקנד, בוכרה וקסגר שגשגו והפכו למרכזים תרבותיים וכלכליים בזכות מיקומן האסטרטגי על דרכים אלו.</li>
        <li><strong>ערי נמל:</strong> ערים כמו ונציה, לונדון, ניו יורק, סינגפור ותל אביב התפתחו והפכו למטרופולינים בזכות תפקידן כנקודות מעבר קריטיות בין נתיבי ים ליבשה.</li>
        <li><strong>עידן הרכבות:</strong> במאות ה-19 וה-20, פיתוח רשתות מסילות ברזל יצר ערים חדשות ("ערי רכבת") ושינה באופן דרמטי את חשיבותן וגודלן של ערים קיימות (דוגמת שיקגו, שצמחה בזכות מיקומה בצומת רכבות מרכזי).</li>
        <li><strong>רשתות כבישים מהירים:</strong> בעידן המודרני, בניית מערכות כבישים מהירים וטבעות מטרופוליניות ממשיכה לעצב את פריסת האוכלוסייה והפעילות הכלכלית, ויוצרת מרכזי משנה חדשים (Suburban Centers) בקרבת יציאות וצמתים.</li>
    </ul>

    <h3>מגבלות המודל - הסימולציה ככלי למידה</h3>
    <p>חשוב לזכור שסימולציה זו היא מודל פשוט של מציאות מורכבת לאין ערוך. היא מתמקדת בהיבט אחד מרכזי (קישוריות ותנועה) ומתבססת על הנחות פשטניות. גורמים חשובים רבים המשפיעים על מיקום וגידול יישובים אינם נכללים במודל זה, כגון: טופוגפיה, זמינות מים ומזון (מעבר ל"משאבים" הבודדים שבמפה), החלטות פוליטיות, השפעות תרבותיות וחברתיות, טכנולוגיה משתנה (למשל, המעבר מרכבות למכוניות), אסונות טבע, מלחמות ועוד. למרות פישוט זה, המודל מדגים בצורה אינטואיטיבית עקרון יסוד רב עוצמה בתכנון מרחבי והתפתחות עירונית.</p>
</div>

<style>
/* כללי */
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 20px;
    background-color: #f0f4f8; /* רקע עדין */
    color: #333;
    direction: rtl;
    text-align: right;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
}

h1, h2, h3 {
    color: #1a5a93; /* כותרות כחולות עמוקות */
    text-align: center;
    margin-bottom: 15px;
}

h1 {
    margin-top: 0;
    margin-bottom: 25px;
    font-size: 2em;
}

p {
    margin-bottom: 15px;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}

/* קונטיינר הסימולציה */
.simulation-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* צל עדין יותר */
    border: 1px solid #e0e0e0;
    width: 100%;
    max-width: 800px; /* הגבלת רוחב לנוחות */
    box-sizing: border-box;
}

#tradeSimulationCanvas {
    border: 2px solid #ccc;
    background-color: #c8e6c9; /* רקע ירוק בהיר למפה */
    cursor: crosshair; /* סמן שרטוט */
    margin-bottom: 15px;
    border-radius: 8px;
    /* גודל נקבע ב JS */
}

/* בקרה */
.controls {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 15px;
    padding: 15px;
    background-color: #e3f2fd; /* רקע תכלת בהיר לבקרות */
    border-radius: 8px;
    width: 100%;
    box-sizing: border-box;
    font-size: 0.95em;
}

.controls button {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease, transform 0.1s ease;
}

#startStopSimulation {
    background-color: #4CAF50; /* ירוק כפתור התחל */
    color: white;
}

#startStopSimulation:hover {
    background-color: #388E3C;
    transform: translateY(-1px);
}

#clearRoutes {
    background-color: #f44336; /* אדום כפתור נקה */
    color: white;
}

#clearRoutes:hover {
    background-color: #d32f2f;
    transform: translateY(-1px);
}

.controls label {
    font-weight: bold;
    color: #1a5a93;
}

#simulationSpeed {
    width: 120px; /* רוחב רחב יותר לסליידר */
    -webkit-appearance: none;
    appearance: none;
    height: 8px;
    background: #bbdefb;
    outline: none;
    opacity: 0.7;
    transition: opacity .2s;
    border-radius: 4px;
}

#simulationSpeed:hover {
    opacity: 1;
}

#simulationSpeed::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 18px;
    height: 18px;
    background: #2196F3;
    cursor: pointer;
    border-radius: 50%;
    border: 2px solid #fff;
}

#simulationSpeed::-moz-range-thumb {
    width: 18px;
    height: 18px;
    background: #2196F3;
    cursor: pointer;
    border-radius: 50%;
    border: 2px solid #fff;
}


#currentSpeed {
    min-width: 30px; /* כדי למנוע תזוזה בגלל שינוי תוכן */
    text-align: center;
}


.instructions {
    width: 100%;
    text-align: center;
    font-size: 0.9em;
    color: #555;
    margin-top: 10px;
    padding-top: 10px;
    border-top: 1px solid #e0e0e0;
    line-height: 1.5;
}

.instructions strong {
    color: #1a5a93;
}

/* כפתור הצגת הסבר */
#toggleExplanation {
    display: block;
    width: fit-content;
    margin: 20px auto;
    padding: 12px 25px;
    background-color: #2196F3; /* כחול עמוק */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1.1em;
    transition: background-color 0.3s ease, transform 0.1s ease;
}

#toggleExplanation:hover {
    background-color: #1976D2;
    transform: translateY(-1px);
}


/* קונטיינר ההסבר */
#explanation {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    border: 1px solid #e0e0e0;
    max-width: 800px;
    margin: 20px auto;
    box-sizing: border-box;
}

#explanation.hidden {
    display: none;
}

#explanation h2 {
    margin-top: 0;
    border-bottom: 2px solid #1a5a93;
    padding-bottom: 10px;
    margin-bottom: 20px;
}

#explanation h3 {
    color: #303f9f; /* כותרות משנה כחולות כהות */
    margin-top: 20px;
    margin-bottom: 10px;
}

#explanation ul {
    padding-right: 25px; /* Adjust for RTL */
    margin-bottom: 15px;
}

#explanation li {
    margin-bottom: 8px;
}

/* אנימציה עדינה לכפתורים בעת לחיצה */
button:active {
  transform: translateY(0);
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('tradeSimulationCanvas');
    const ctx = canvas.getContext('2d');
    const startStopBtn = document.getElementById('startStopSimulation');
    const speedSlider = document.getElementById('simulationSpeed');
    const currentSpeedSpan = document.getElementById('currentSpeed');
    const clearRoutesBtn = document.getElementById('clearRoutes');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationBtn = document.getElementById('toggleExplanation');

    // Set canvas size based on container or fixed
    const canvasWidth = Math.min(600, document.querySelector('.simulation-container').offsetWidth - 40); // Fit within container padding
    const canvasHeight = 500;
    canvas.width = canvasWidth;
    canvas.height = canvasHeight;

    let routes = []; // Array of arrays of points {x, y}
    let isDrawing = false;
    let currentRoute = [];
    let simulationRunning = false;
    let animationFrameId = null;
    let simulationSpeed = parseFloat(speedSlider.value); // Speed multiplier

    // Simulation state grid
    const potentialGridSize = 8; // Smaller grid for finer detail
    const gridWidth = Math.ceil(canvasWidth / potentialGridSize);
    const gridHeight = Math.ceil(canvasHeight / potentialGridSize);
    let potentialGrid = Array(gridWidth).fill(0).map(() => Array(gridHeight).fill(0));
    let simulationTime = 0; // Simple counter for simulation steps
    let lastTime = 0; // For delta time calculation

    // Initial resource points (static points of interest)
    const resourcePoints = [
        { x: 100, y: 100, radius: 12, color: '#ffc107' }, // Gold source
        { x: 400, y: 150, radius: 12, color: '#795548' }, // Timber source
        { x: 250, y: 400, radius: 12, color: '#03a9f4' }, // Water/River spot
        { x: 500, y: 300, radius: 12, color: '#e57373' }  // Fertile land
    ];

    // Simulation parameters
    const potentialDecay = 0.005; // Slow decay per step
    const routePotentialBoost = 0.1; // Base potential added per grid cell on a route per frame
    const resourceProximityBoost = 0.5; // Extra boost near resources per frame
    const resourceProximityRadius = potentialGridSize * 4; // How far resource influence extends
    const intersectionBoost = 0.2; // Extra boost for grid cells near route intersections
    const minIntersectionDistance = potentialGridSize * 2; // How close points need to be to be considered an intersection
    const cityGrowthFactor = 0.005; // How much accumulated potential contributes to size per frame
    const minCityDisplayPotential = 5; // Minimum potential to start displaying a city
    const maxCitySize = 40; // Maximum visual size of a city


    // Helper function to get grid coordinates from canvas coordinates
    function getGridCoords(x, y) {
        const gridX = Math.floor(x / potentialGridSize);
        const gridY = Math.floor(y / potentialGridSize);
        if (gridX >= 0 && gridX < gridWidth && gridY >= 0 && gridY < gridHeight) {
            return { gridX, gridY };
        }
        return null;
    }

    // Helper function to interpolate points along a line
    function interpolatePoints(p1, p2, density = 1) {
        const points = [];
        const dx = p2.x - p1.x;
        const dy = p2.y - p1.y;
        const distance = Math.sqrt(dx * dx + dy * dy);
        const steps = Math.max(1, Math.ceil(distance / density)); // At least 1 step
        for (let i = 0; i <= steps; i++) {
            const t = i / steps;
            points.push({
                x: p1.x + dx * t,
                y: p1.y + dy * t
            });
        }
        return points;
    }

    // --- Drawing Functions ---
    function drawBackground() {
        ctx.fillStyle = '#c8e6c9'; // Greenish light background
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Optional: Draw potential grid for debugging/visualization
        // drawPotentialOverlay();
    }

    function drawPotentialOverlay() {
         // Draw a subtle heatmap based on potential
         const maxPotential = Math.max(1, ...potentialGrid.flat()); // Avoid division by zero
         for (let i = 0; i < gridWidth; i++) {
             for (let j = 0; j < gridHeight; j++) {
                 const potential = potentialGrid[i][j];
                 if (potential > 0) {
                     const alpha = Math.min(0.5, potential / (maxPotential * 2)); // Cap opacity
                     const color = `rgba(255, 152, 0, ${alpha})`; // Orange heatmap

                     ctx.fillStyle = color;
                     ctx.fillRect(i * potentialGridSize, j * potentialGridSize, potentialGridSize, potentialGridSize);
                 }
             }
         }
    }

    function drawResources() {
         resourcePoints.forEach(p => {
             ctx.save(); // Save current context state
             ctx.translate(p.x, p.y); // Move origin to resource center
             ctx.fillStyle = p.color;
             ctx.strokeStyle = '#333';
             ctx.lineWidth = 1;

             // Draw a simple star/burst shape for resources
             const outerRadius = p.radius;
             const innerRadius = outerRadius * 0.5;
             const points = 5;
             ctx.beginPath();
             for (let i = 0; i < points * 2; i++) {
                 const r = (i % 2 === 0) ? outerRadius : innerRadius;
                 const angle = Math.PI * i / points;
                 ctx.lineTo(r * Math.sin(angle), r * Math.cos(angle));
             }
             ctx.closePath();
             ctx.fill();
             ctx.stroke();

             ctx.restore(); // Restore context state
         });
    }

    function drawRoutes(deltaTime) {
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';

        // Draw existing routes
        routes.forEach(route => {
            if (route.length > 1) {
                ctx.strokeStyle = '#5D4037'; // Brownish grey for routes
                ctx.lineWidth = 4;
                ctx.beginPath();
                ctx.moveTo(route[0].x, route[0].y);
                for (let i = 1; i < route.length; i++) {
                    ctx.lineTo(route[i].x, route[i].y);
                }
                ctx.stroke();

                // Add animated flow effect
                if (simulationRunning) {
                     const flowSpeed = 0.05 * simulationSpeed; // Speed of flow dots
                     const flowGap = 15; // Space between dots
                     const flowSize = 3; // Size of dots
                     const flowColor = '#ffab40'; // Orange/Amber for flow

                     // Calculate total length of the route to normalize time
                     let totalLength = 0;
                     for(let i = 0; i < route.length - 1; i++){
                         totalLength += Math.sqrt(Math.pow(route[i+1].x - route[i].x, 2) + Math.pow(route[i+1].y - route[i].y, 2));
                     }

                     let currentFlowPos = (simulationTime * flowSpeed * totalLength) % totalLength; // Position along the route, wraps around

                     ctx.fillStyle = flowColor;
                     ctx.beginPath();

                     let distanceCovered = 0;
                     for(let i = 0; i < route.length - 1; i++){
                         const p1 = route[i];
                         const p2 = route[i+1];
                         const segmentLength = Math.sqrt(Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2));

                         // Check if the current flow position is within this segment
                         if (currentFlowPos >= distanceCovered && currentFlowPos < distanceCovered + segmentLength) {
                              const segmentProgress = currentFlowPos - distanceCovered;
                              const ratio = segmentProgress / segmentLength;
                              const flowX = p1.x + (p2.x - p1.x) * ratio;
                              const flowY = p1.y + (p2.y - p1.y) * ratio;
                              ctx.arc(flowX, flowY, flowSize, 0, Math.PI * 2);
                              ctx.fill(); // Draw the first dot
                              break; // Found the segment, draw and exit
                         }
                         distanceCovered += segmentLength;
                     }
                }
            }
        });

        // Draw the current route being drawn
        if (isDrawing && currentRoute.length > 1) {
             ctx.strokeStyle = '#007bff'; // Blue for current route
             ctx.lineWidth = 4;
             ctx.beginPath();
             ctx.moveTo(currentRoute[0].x, currentRoute[0].y);
             for (let i = 1; i < currentRoute.length; i++) {
                 ctx.lineTo(currentRoute[i].x, currentRoute[i].y);
             }
             ctx.stroke();
        }
    }

    function drawCities() {
        ctx.fillStyle = 'rgba(255, 87, 34, 0.8)'; // Deep Orange for cities
        ctx.strokeStyle = '#bf360c'; // Darker border
        ctx.lineWidth = 1;

        for (let i = 0; i < gridWidth; i++) {
            for (let j = 0; j < gridHeight; j++) {
                const potential = potentialGrid[i][j];
                if (potential > minCityDisplayPotential) {
                    // Size grows with potential, capped at maxCitySize
                    const size = Math.min(maxCitySize, minCityDisplayPotential + (potential - minCityDisplayPotential) * cityGrowthFactor * 10); // Scale potential to size
                    const centerX = i * potentialGridSize + potentialGridSize / 2;
                    const centerY = j * potentialGridSize + potentialGridSize / 2;

                    // Draw city as a growing circle with a small pulse
                    ctx.beginPath();
                    // Add a subtle pulse effect based on simulationTime
                    const pulse = Math.sin(simulationTime * 0.05) * (size * 0.05); // Pulse size is 5% of current size
                    ctx.arc(centerX, centerY, size + pulse, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.stroke();

                    // Optional: Draw city name/potential value (for advanced versions)
                    // ctx.fillStyle = '#000';
                    // ctx.font = '10px Arial';
                    // ctx.textAlign = 'center';
                    // ctx.fillText(Math.floor(potential), centerX, centerY + size + 12);
                }
            }
        }
    }

    function draw(currentTime) {
        if (!simulationRunning) {
             // If simulation is not running, draw static state
             drawBackground();
             drawResources();
             drawRoutes(0); // Pass delta time 0 as no movement animation needed
             drawCities();
             return;
        }

        const deltaTime = currentTime - lastTime;
        lastTime = currentTime;

        // Update simulation state
        updatePotential(deltaTime);

        // Redraw everything
        drawBackground();
        drawResources();
        drawRoutes(deltaTime); // Pass delta time for flow animation
        drawCities();

        // Request next frame
        animationFrameId = requestAnimationFrame(draw);
    }

    // --- Simulation Logic ---
    function updatePotential(deltaTime) {
        const potentialGain = routePotentialBoost * simulationSpeed * (deltaTime / 16); // Scale gain by speed and delta time (assuming 60fps base)
        const resourceGain = resourceProximityBoost * simulationSpeed * (deltaTime / 16);
        const intersectionGain = intersectionBoost * simulationSpeed * (deltaTime / 16);

        // Decay potential slightly over time
        for (let i = 0; i < gridWidth; i++) {
            for (let j = 0; j < gridHeight; j++) {
                potentialGrid[i][j] = Math.max(0, potentialGrid[i][j] - potentialDecay * simulationSpeed * (deltaTime / 16));
            }
        }

        // Add potential from routes, resources, and intersections
        routes.forEach(route => {
            if (route.length < 2) return;

            // Interpolate points more densely along the route for better grid coverage
            const routePoints = route.reduce((acc, p, i, arr) => {
                if (i < arr.length - 1) {
                    acc.push(...interpolatePoints(p, arr[i+1], potentialGridSize / 2)); // Interpolate every half grid cell
                } else {
                    acc.push(p);
                }
                return acc;
            }, []);


            routePoints.forEach(p => {
                const gridCoords = getGridCoords(p.x, p.y);
                if (gridCoords) {
                    const { gridX, gridY } = gridCoords;
                    potentialGrid[gridX][gridY] += potentialGain; // Base route potential

                    // Add resource proximity boost
                    resourcePoints.forEach(resource => {
                        const dist = Math.sqrt(Math.pow(p.x - resource.x, 2) + Math.pow(p.y - resource.y, 2));
                        if (dist < resourceProximityRadius) {
                            // Boost is stronger closer to the resource
                            potentialGrid[gridX][gridY] += resourceGain * (1 - dist / resourceProximityRadius);
                        }
                    });
                }
            });
        });

        // Add intersection boost - check proximity of points from different routes
        // This is computationally expensive, a simpler approximation is to boost points where route density is high
         const densityGrid = Array(gridWidth).fill(0).map(() => Array(gridHeight).fill(0));
         routes.forEach(route => {
             if (route.length < 2) return;
             const routePoints = route.reduce((acc, p, i, arr) => {
                 if (i < arr.length - 1) {
                     acc.push(...interpolatePoints(p, arr[i+1], potentialGridSize / 2));
                 } else {
                     acc.push(p);
                 }
                 return acc;
             }, []);

             routePoints.forEach(p => {
                 const gridCoords = getGridCoords(p.x, p.y);
                 if (gridCoords) {
                      densityGrid[gridCoords.gridX][gridCoords.gridY]++;
                 }
             });
         });

         for (let i = 0; i < gridWidth; i++) {
             for (let j = 0; j < gridHeight; j++) {
                 if (densityGrid[i][j] > 1) { // If more than one interpolated point in a cell (suggests intersection or dense route)
                      potentialGrid[i][j] += intersectionGain * (densityGrid[i][j] - 1); // Boost scales with density
                 }
             }
         }


        // Optional: Add positive feedback from existing cities (cities attract more activity)
        // This would require iterating through grid, finding cities, and boosting potential in their vicinity
        // Based on their size/potential. Left out for simplicity in this version.
    }

    // --- Event Handlers ---
    function getCanvasMousePosition(e) {
        const rect = canvas.getBoundingClientRect();
        return {
            x: e.clientX - rect.left,
            y: e.clientY - rect.top
        };
    }

    function getCanvasTouchPosition(e) {
         const rect = canvas.getBoundingClientRect();
         const touch = e.touches[0];
         return {
             x: touch.clientX - rect.left,
             y: touch.clientY - rect.top
         };
    }

    canvas.addEventListener('mousedown', (e) => {
        const pos = getCanvasMousePosition(e);
        if (!isDrawing) {
            isDrawing = true;
            currentRoute = [pos];
            // Prevent default behavior only if starting a draw
            e.preventDefault();
        }
         draw(performance.now()); // Redraw immediately
    });

     canvas.addEventListener('mousemove', (e) => {
        if (!isDrawing) return;
        const pos = getCanvasMousePosition(e);
        // Only add point if moved a significant distance
        const lastPoint = currentRoute[currentRoute.length - 1];
        const dist = Math.sqrt(Math.pow(pos.x - lastPoint.x, 2) + Math.pow(pos.y - lastPoint.y, 2));
        if (dist > 5) { // Add point roughly every 5 pixels
             currentRoute.push(pos);
             draw(performance.now()); // Draw live feedback
        }
        e.preventDefault(); // Prevent selection etc.
    });

    canvas.addEventListener('mouseup', () => {
        if (isDrawing) {
            isDrawing = false;
            if (currentRoute.length > 1) { // Only save if route has at least 2 points
                routes.push(currentRoute);
            }
            currentRoute = []; // Reset current route
             // Recalculate potential grid *once* after adding a route before simulation runs
            // This gives an initial potential boost from the new route
             potentialGrid = Array(gridWidth).fill(0).map(() => Array(gridHeight).fill(0)); // Reset grid for recalculation
             // Temporarily set simulation speed high for faster initial calculation if needed, or just run updatePotential multiple times
             // Let's just iterate calculate potential a few times to seed the grid based on routes
             for(let i = 0; i < 100; i++) { // Run a few "setup" steps
                updatePotential(16); // Simulate one frame's worth of potential calculation
             }

            draw(performance.now()); // Final redraw with initial potential
        }
    });

     canvas.addEventListener('mouseleave', () => {
        // Treat mouse leaving canvas as mouse up
         if (isDrawing) {
            isDrawing = false;
            if (currentRoute.length > 1) { // Only save if route has at least 2 points
                routes.push(currentRoute);
            }
            currentRoute = []; // Reset current route
             potentialGrid = Array(gridWidth).fill(0).map(() => Array(gridHeight).fill(0)); // Reset grid for recalculation
             for(let i = 0; i < 100; i++) { // Run a few "setup" steps
                updatePotential(16);
             }
            draw(performance.now()); // Final redraw
        }
     });


    // Handle touch events for drawing on touch devices
    canvas.addEventListener('touchstart', (e) => {
        const pos = getCanvasTouchPosition(e);
        if (!isDrawing) {
            isDrawing = true;
            currentRoute = [pos];
        }
        e.preventDefault(); // Prevent scrolling etc.
         draw(performance.now()); // Redraw immediately
    });

    canvas.addEventListener('touchmove', (e) => {
        if (!isDrawing || e.touches.length !== 1) return; // Only handle single touch drag
        const pos = getCanvasTouchPosition(e);
        const lastPoint = currentRoute[currentRoute.length - 1];
        const dist = Math.sqrt(Math.pow(pos.x - lastPoint.x, 2) + Math.pow(pos.y - lastPoint.y, 2));
        if (dist > 5) { // Add point roughly every 5 pixels
             currentRoute.push(pos);
             draw(performance.now()); // Draw live feedback
        }
        e.preventDefault();
    });

    canvas.addEventListener('touchend', () => {
        if (isDrawing) {
            isDrawing = false;
            if (currentRoute.length > 1) { // Only save if route has at least 2 points
                routes.push(currentRoute);
            }
            currentRoute = []; // Reset current route
             potentialGrid = Array(gridWidth).fill(0).map(() => Array(gridHeight).fill(0)); // Reset grid for recalculation
             for(let i = 0; i < 100; i++) { // Run a few "setup" steps
                updatePotential(16);
             }
            draw(performance.now()); // Final redraw
        }
    });


    startStopBtn.addEventListener('click', () => {
        simulationRunning = !simulationRunning;
        if (simulationRunning) {
            startStopBtn.textContent = 'עצור סימולציה';
            lastTime = performance.now(); // Initialize lastTime for delta time
            draw(performance.now()); // Start the loop
        } else {
            startStopBtn.textContent = 'התחל סימולציה';
            cancelAnimationFrame(animationFrameId); // Stop the loop
            draw(performance.now()); // Draw final static state
        }
    });

    speedSlider.addEventListener('input', () => {
        simulationSpeed = parseFloat(speedSlider.value);
        currentSpeedSpan.textContent = `${speedSlider.value}x`;
    });

    clearRoutesBtn.addEventListener('click', () => {
        routes = [];
        // Reset potential grid and simulation time when clearing routes
        potentialGrid = Array(gridWidth).fill(0).map(() => Array(gridHeight).fill(0));
        simulationTime = 0;

        // Stop simulation if running
        const wasRunning = simulationRunning;
        if(wasRunning) {
           startStopBtn.click(); // This also stops the loop
        } else {
            // If not running, just redraw static cleared state
            draw(performance.now());
        }

        // If simulation was running, the click toggled it off. We don't restart automatically.
        // User needs to click "התחל" again.
    });


    toggleExplanationBtn.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
        if (!explanationDiv.classList.contains('hidden')) {
            // Scroll to explanation div smoothly
            explanationDiv.scrollIntoView({ behavior: 'smooth' });
        }
    });

    // Initial draw
    draw(performance.now());
});
</script>
```