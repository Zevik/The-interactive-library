---
title: "נהרות אטמוספיריים: ענקי הלחות שמעצבים מחדש את מזג האוויר"
english_slug: atmospheric-rivers-hidden-giants-changing-weather
category: "מדעי הסביבה / מדעי האטמוספרה"
tags:
  - נהרות אטמוספיים
  - גשם קיצוני
  - שיטפונות
  - שינויי אקלים
  - מזג אוויר
---
# נהרות אטמוספיריים: ענקי הלחות שמעצבים מחדש את מזג האוויר

דמיינו נהרות ענק בשמיים, בלתי נראים לעין בלתי מזוינת, המובילים כמויות אדירות של לחות על פני אלפי קילומטרים. אלו הם ה'נהרות האטמוספיריים' - תופעה מטאורולוגית מדהימה אך הרסנית, האחראית לחלק הארי מאירועי הגשם הקיצוניים ביותר על פני כדור הארץ. הבנה של נהרות אלו חיונית כדי לחזות ולהתמודד עם אירועי מזג אוויר דרמטיים ושינויי אקלים עתידיים.

<div class="app-container">
    <div id="simulation-area">
        <canvas id="weatherCanvas"></canvas>
        <div id="controls">
            <h3>הגדרת העולם והנהר</h3>
            <div class="control-group">
                <label for="waterTemp">טמפרטורת מי האוקיינוס (°C):</label>
                <input type="range" id="waterTemp" min="15" max="35" value="25" step="1">
                <span id="waterTempValue">25</span>
            </div>

            <div class="control-group">
                <label for="jetStreamStrength">עוצמת זרם הסילון (מהירות יחסית):</label>
                <input type="range" id="jetStreamStrength" min="50" max="250" value="150" step="10">
                <span id="jetStreamStrengthValue">150</span>
            </div>

            <div class="control-group">
                <label for="mountainPosition">מיקום רכס ההרים (% מהיבשה):</label>
                <input type="range" id="mountainPosition" min="15" max="85" value="50" step="5">
                <span id="mountainPositionValue">50</span>
            </div>

            <div class="button-group">
                <button id="startSimulation" class="control-button">התחל זרימת נהר</button>
                <button id="resetSimulation" class="control-button reset">איפוס</button>
            </div>
        </div>
    </div>
    <div id="stats-area">
        <h3>נתוני הסימולציה</h3>
        <div class="stat-item">
            <span class="stat-label">סה"כ משקעים מעל ההרים:</span>
            <span id="totalPrecipitation" class="stat-value">0.0 מ"מ</span>
        </div>
         <div class="stat-item">
             <span class="stat-label">זמן סימולציה:</span>
             <span id="simulationTime" class="stat-value">0.0 שניות</span>
        </div>
        <div class="stat-item">
             <span class="stat-label">חלקיקי לחות באוויר:</span>
             <span id="particleCount" class="stat-value">0</span>
        </div>
    </div>
</div>

<style>
/* Global Styles */
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.7;
    margin: 0;
    padding: 20px;
    background-color: #eef2f7; /* Light blue-grey background */
    color: #333;
    direction: rtl; /* Right-to-left for Hebrew */
    text-align: right;
    overflow-x: hidden; /* Prevent horizontal scroll */
}

h1, h3 {
    color: #1a2e4d; /* Dark blue headings */
    text-align: center;
    margin-bottom: 15px;
}

h1 {
    margin-top: 0;
    font-size: 2em;
}

/* App Container - Layout */
.app-container {
    display: flex;
    flex-direction: column;
    gap: 30px; /* Increased gap */
    margin: 20px auto; /* Center container */
    max-width: 1000px; /* Max width for larger screens */
    background-color: #fff; /* White background for the app */
    padding: 30px; /* Increased padding */
    border-radius: 12px; /* More rounded corners */
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1); /* Softer, larger shadow */
}

#simulation-area {
    display: flex;
    flex-direction: column;
    gap: 25px; /* Gap between canvas and controls */
}

/* Canvas Styling - The core visual */
#weatherCanvas {
    width: 100%;
    height: 450px; /* Slightly increased height */
    border: 1px solid #d0d0d0; /* Subtle border */
    background: linear-gradient(to bottom, #a0c8ff, #e0f7ff); /* Sky gradient - initial */
    border-radius: 8px; /* Match container radius */
    box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.05); /* Subtle inner shadow */
}

/* Controls Styling - User interaction */
#controls {
    background-color: #f8f9fa; /* Light grey background for controls */
    padding: 20px; /* Increased padding */
    border-radius: 8px; /* Match container radius */
    border: 1px solid #e9ecef; /* Subtle border */
    display: grid; /* Use grid for better control layout */
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); /* Responsive columns */
    gap: 20px; /* Gap between control items */
    align-items: center; /* Vertically center controls */
}

#controls h3 {
    grid-column: 1 / -1; /* Span across all columns */
    text-align: center;
    margin-top: 0;
    margin-bottom: 15px;
    color: #1a2e4d;
}

.control-group {
    display: flex; /* Flex for label and input/span */
    align-items: center;
    gap: 10px; /* Space between label and control */
}

.control-group label {
    flex-shrink: 0; /* Prevent label from shrinking */
    font-weight: bold;
    color: #555;
    width: 180px; /* Fixed width for consistency */
    text-align: left; /* Align labels to the left */
}

.control-group input[type="range"] {
    flex-grow: 1; /* Allow range slider to take available space */
    -webkit-appearance: none; /* Remove default styling */
    appearance: none;
    height: 8px; /* Thicker track */
    background: #d0d0d0; /* Grey track */
    outline: none;
    opacity: 0.8;
    transition: opacity .15s ease-in-out;
    border-radius: 4px;
}

.control-group input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px; /* Thumb size */
    height: 20px;
    background: #007bff; /* Blue thumb */
    cursor: pointer;
    border-radius: 50%; /* Round thumb */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.control-group input[type="range"]::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #007bff;
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.control-group input[type="range"]:hover {
    opacity: 1;
}

.control-group span {
    flex-shrink: 0; /* Prevent span from shrinking */
    width: 40px; /* Fixed width for value display */
    text-align: center;
    font-weight: bold;
    color: #007bff; /* Blue color for values */
}

.button-group {
    grid-column: 1 / -1; /* Span across all columns */
    text-align: center; /* Center buttons */
    margin-top: 10px;
}

.control-button {
    padding: 12px 25px; /* Larger padding */
    margin: 0 10px; /* Space between buttons */
    background-color: #28a745; /* Green for start */
    color: white;
    border: none;
    border-radius: 6px; /* Slightly rounded */
    cursor: pointer;
    font-size: 1em; /* Standard font size */
    transition: background-color 0.2s ease-in-out, opacity 0.2s ease-in-out;
}

.control-button:hover:not(:disabled) {
    background-color: #218838; /* Darker green on hover */
}

.control-button.reset {
    background-color: #dc3545; /* Red for reset */
}

.control-button.reset:hover:not(:disabled) {
    background-color: #c82333; /* Darker red on hover */
}

.control-button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}


/* Stats Area - Displaying data */
#stats-area {
     background-color: #f8f9fa; /* Light grey background */
     padding: 20px; /* Increased padding */
     border-radius: 8px; /* Match container radius */
     border: 1px solid #e9ecef; /* Subtle border */
     display: grid;
     grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* Responsive columns */
     gap: 15px; /* Gap between stat items */
}

#stats-area h3 {
    grid-column: 1 / -1; /* Span across all columns */
    text-align: center;
    margin-top: 0;
    margin-bottom: 15px;
    color: #1a2e4d;
}

.stat-item {
    display: flex;
    justify-content: space-between; /* Space between label and value */
    border-bottom: 1px dashed #eee; /* Subtle separator */
    padding-bottom: 5px;
}

.stat-label {
    font-weight: bold;
    color: #555;
}

.stat-value {
    color: #007bff; /* Blue color for values */
    font-weight: normal; /* Normal weight for value */
}


/* Explanation Section */
#explanation-button {
    display: block;
    width: 220px; /* Wider button */
    margin: 30px auto; /* More margin, center button */
    padding: 15px 25px; /* Increased padding */
    text-align: center;
    background-color: #007bff; /* Blue button */
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.1em; /* Slightly larger font */
    transition: background-color 0.2s ease-in-out;
}

#explanation-button:hover {
    background-color: #0056b3; /* Darker blue on hover */
}

.explanation-content {
    display: none; /* Initially hidden */
    margin-top: 25px; /* More margin */
    padding: 30px; /* Increased padding */
    background-color: #fff;
    border-radius: 12px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
}

.explanation-content h3 {
    border-bottom: 2px solid #e9ecef; /* Softer border */
    padding-bottom: 10px; /* More padding below heading */
    margin-top: 25px;
    color: #1a2e4d;
    text-align: right; /* Align explanation headings right */
}

.explanation-content h3:first-child {
    margin-top: 0;
}

.explanation-content p {
    margin-bottom: 20px; /* More space between paragraphs */
    color: #555; /* Softer text color */
}

/* Canvas Drawing Styles - These are hints, actual drawing is in JS */
/* Drawing colors will be updated in JS */

/* Responsive adjustments */
@media (max-width: 768px) {
    .app-container {
        padding: 20px;
    }
    #controls {
        grid-template-columns: 1fr; /* Stack controls on smaller screens */
        gap: 15px;
    }
     .control-group label {
         width: 150px; /* Adjust label width */
     }
     .control-group input[type="range"] {
         width: calc(100% - 200px); /* Adjust input width */
     }
    #stats-area {
        grid-template-columns: 1fr; /* Stack stats on smaller screens */
        gap: 10px;
    }
    #explanation-button {
        width: 100%; /* Full width button */
        max-width: 250px; /* But keep a max width */
    }
    .explanation-content {
        padding: 20px;
    }
}

</style>

<button id="explanation-button">הצג הסבר מורחב על נהרות אטמוספיריים</button>

<div class="explanation-content" id="explanationContent">
    <h3>מהו נהר אטמוספירי? הגדרה ותיאור ויזואלי</h3>
    <p>דמיינו צינור ענק ובלתי נראה בשמיים, רחב פי כמה מנהר המיסיסיפי, הנושא אדי מים בכמות אסטרונומית ממעמקי האוקיינוס אל היבשה. זהו נהר אטמוספירי - זרם אוויר ארוך, צר ומרוכז מאוד בלחות, הנע באטמוספרה התחתונה (בגובה של עד כ-3 קילומטרים). הוא יכול להתפרס על פני אלפי קילומטרים לאורך, אך רק מאות קילומטרים לרוחב. למרות שהשם כולל "נהר", אין מדובר במים נוזליים, אלא באדי מים (גז) בריכוז גבוה בתוך זרם אוויר מהיר. נהרות אלו הם מעין "כבישים מהירים" של לחות, המסיעים אותה מהאזורים הטרופיים והסובטרופיים החמים לעבר הקטבים.</p>

    <h3>כיצד נוצרים נהרות אטמוספיריים? שילוב קטלני של לחות ודינמיקה</h3>
    <p>הסיפור מתחיל מעל אוקיינוסים חמים, שם אידוי נרחב מעלה כמויות עצומות של אדי מים לאטמוספרה. לחות זו אינה נשארת מפוזרת - היא נאספת ומנותבת על ידי מערכות לחץ נמוך וזרמי סילון חזקים. זרם הסילון (Jet Stream) הוא זרם אוויר מהיר בגובה רב המשמש כמנוע ומנחה; הוא יוצר אזורי הפרשי לחץ משמעותיים המסייעים לריכוז האוויר הלחוץ לכדי "נהר" ממוקד. תנאים אטמוספריים ספציפיים, כמו מיקום מדויק של רכסי לחץ גבוה ושקעים ברומטריים, מכוונים את הזרם הזה ומעצימים אותו, הופכים אותו מכבשן לחות רגיל למכונה ליצירת גשם קיצוני.</p>

    <h3>המסע וההשפעה: ממעמקי האוקיינוס ועד לפסגות ההרים</h3>
    <p>נהרות אטמוספיריים נעים לרוב לאורך שולי מערכות סערה, עוקבים אחר תוואי זרם הסילון, ולעיתים קרובות מגיעים ליבשות. כאשר נהר אטמוספירי נתקל במכשול פיזי משמעותי כמו רכס הרים (אפקט ה'התרוממות האורוגרפית'), האוויר הלחוץ נאלץ לעלות במעלה המדרון. כשהאוויר מטפס לגובה רב יותר, הוא מתקרר. אוויר קר מסוגל להחזיק פחות אדי מים מאוויר חם. הלחות העודפת "נדחסת" החוצה, מתעבה במהירות ויוצרת ענני גשם עבים ועמוסים בצד ההר הפונה לרוח (Windward side). תהליך זה, יחד עם הכמות העצומה של הלחות שהנהר נושא, מוביל לגשמים עזים ומתמשכים שיכולים להימשך שעות ואף ימים, ולהצטבר במהירות לכמויות משקעים עצומות.</p>

    <h3>לא רק גשם: הסכנות והיתרונות הנסתרים</h3>
    <p>כמויות הגשם האדירות שנוחתות בזמן קצר עלולות לגרום לאסונות טבע קשים: שיטפונות בזק, הצפות ענק, מפולות בוץ, וגרימת נזק נרחב לתשתיות ולרכוש. הם גורם מרכזי לאירועי שיטפון קטלניים במקומות כמו קליפורניה, מערב אירופה וניו זילנד. עם זאת, במקומות מסוימים ובתקופות של בצורת, נהרות אטמוספיריים יכולים להיות חיוניים למילוי מאגרי מים, הצטברות שלג על רכסי הרים (המשמש כמקור מים בקיץ) וחידוש מאגרי מי תהום, ובכך להוות ברכה חיונית אך מסוכנת.</p>

    <h3>נהרות אטמוספיריים בעידן שינויי האקלים</h3>
    <p>כאשר כדור הארץ מתחמם, האוקיינוסים מתחממים גם הם, והאידוי גובר. אוויר חם יותר יכול להכיל כמות גדולה יותר של אדי מים (כ-7% יותר לחות לכל עלייה של מעלה צלזיוס אחת). מודלים אקלימיים מראים ששינויי האקלים צפויים להגביר את תדירות ועוצמת נהרות אטמוספיריים. נהרות "שמנים" יותר אלו, הטעונים ביותר לחות, צפויים להביא לאירועי גשם קיצוניים יותר וגורמים לשיטפונות הרסניים יותר בעתיד באזורים שונים בעולם.</p>

    <h3>השפעה מקומית: נהרות אטמוספיריים והקשר לישראל</h3>
    <p>בישראל, אנו חווים לרוב מערכות גשם המושפעות מהים התיכון. למרות שאיננו נמצאים במסלולים הקלאסיים של הנהרות האטמוספיריים העוצמתיים ביותר בעולם (כמו ה"Pineapple Express" שמשפיע על קליפורניה), גם הים התיכון יכול להוות מקור ללחות רבה. לעיתים, זרימת אוויר ממוקדת ולחה במיוחד ממרכז הים התיכון מגיעה לישראל, ופוגשת ברכסי ההרים שלנו (הרי יהודה, הרי הגליל והגולן). התרוממות האוויר מעל מכשולים אלו עלולה לגרום לאירועי גשם עזים ומקומיים, הדומים במנגנון שלהם לאפקט הנגרם על ידי נהרות אטמוספיריים גדולים יותר, ולהוביל לשיטפונות משמעותיים בנחלים ובאזורים המועדים לכך, במיוחד באזורים מדרוניים.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('weatherCanvas');
    const ctx = canvas.getContext('2d');
    const startButton = document.getElementById('startSimulation');
    const resetButton = document.getElementById('resetSimulation');
    const waterTempInput = document.getElementById('waterTemp');
    const waterTempValue = document.getElementById('waterTempValue');
    const jetStreamStrengthInput = document.getElementById('jetStreamStrength');
    const jetStreamStrengthValue = document.getElementById('jetStreamStrengthValue');
    const mountainPositionInput = document.getElementById('mountainPosition');
    const mountainPositionValue = document.getElementById('mountainPositionValue');
    const totalPrecipitationDiv = document.getElementById('totalPrecipitation');
    const simulationTimeDiv = document.getElementById('simulationTime');
    const particleCountDiv = document.getElementById('particleCount'); // New element for particle count
    const explanationButton = document.getElementById('explanation-button');
    const explanationContent = document.getElementById('explanationContent');

    let animationFrameId = null;
    let particles = [];
    let totalPrecipitation = 0;
    let simulationRunning = false;
    let simulationTime = 0;
    const timeStep = 1/60; // Assuming 60 frames per second

    let canvasWidth, canvasHeight;
    let oceanWidth, landWidth;
    let mountainStart = 0; // Calculated dynamically
    const mountainHeight = 150; // Increased height
    const mountainWidth = 200; // Increased width

    // --- Canvas and Drawing Setup ---
    const resizeCanvas = () => {
        canvasWidth = canvas.offsetWidth;
        canvasHeight = canvas.offsetHeight;
        canvas.width = canvasWidth;
        canvas.height = canvasHeight;
        oceanWidth = canvasWidth * 0.4; // 40% ocean (River forms near the left edge)
        landWidth = canvasWidth * 0.6;  // 60% land
        updateMountainPosition();
        drawBackground();
        drawMountains();
        // Re-position particles relative to new scale? Too complex for this constraint.
        // Let's just accept they might jump visually on resize mid-sim.
    };

    window.addEventListener('resize', resizeCanvas);
    resizeCanvas(); // Initial resize

    function updateMountainPosition() {
         const landStart = oceanWidth;
         const landEnd = canvasWidth;
         // Position percentage is relative to the *entire* width, but mountain is on land
         // Let's re-interpret: mountain position is % across the *land* area starting after the ocean.
         const usableLandWidth = landEnd - landStart - mountainWidth;
         // Ensure mountain position is within the usable land width
         const mountainPercentage = parseInt(mountainPositionInput.value) / 100;
         const mountainOffset = usableLandWidth * mountainPercentage;
         mountainStart = landStart + mountainOffset;
    }

    function drawBackground() {
        // Sky Gradient
        const skyGradient = ctx.createLinearGradient(0, 0, 0, canvasHeight);
        skyGradient.addColorStop(0, '#87CEEB'); // Light blue sky
        skyGradient.addColorStop(0.6, '#B0E0E6'); // Powder blue lower sky
        skyGradient.addColorStop(1, '#E0F7FA'); // Very light blue near horizon
        ctx.fillStyle = skyGradient;
        ctx.fillRect(0, 0, canvasWidth, canvasHeight);

        // Ocean
        const oceanGradient = ctx.createLinearGradient(0, canvasHeight * 0.7, 0, canvasHeight);
        oceanGradient.addColorStop(0, '#0077BE'); // Deep ocean blue
        oceanGradient.addColorStop(1, '#00BBD4'); // Lighter ocean blue
        ctx.fillStyle = oceanGradient;
        ctx.fillRect(0, canvasHeight * 0.7, oceanWidth, canvasHeight * 0.3); // Lower part of ocean area

        // Land
        const landGradient = ctx.createLinearGradient(0, canvasHeight * 0.8, 0, canvasHeight);
        landGradient.addColorStop(0, '#8B4513'); // Saddle Brown
        landGradient.addColorStop(1, '#A0522D'); // Sienna
        ctx.fillStyle = landGradient;
        ctx.fillRect(oceanWidth, canvasHeight * 0.8, landWidth, canvasHeight * 0.2); // Lower part of land area

         // Draw the atmospheric river layer visually
         if (simulationRunning) {
             ctx.fillStyle = 'rgba(100, 100, 255, 0.1)'; // Translucent blue layer
             const riverLayerMin = canvasHeight * 0.3;
             const riverLayerMax = canvasHeight * 0.6;
             ctx.fillRect(0, riverLayerMin, canvasWidth, riverLayerMax - riverLayerMin);
         }
    }

    function drawMountains() {
        const mountainColor = '#5F4F4C'; // Dark grey/brown for mountains
        const snowColor = '#FFFFFF'; // White for snow peaks

        ctx.fillStyle = mountainColor;
        ctx.beginPath();
        ctx.moveTo(mountainStart - 20, canvasHeight); // Start slightly before base
        ctx.lineTo(mountainStart + mountainWidth * 0.5, canvasHeight - mountainHeight);
        ctx.lineTo(mountainStart + mountainWidth + 20, canvasHeight); // End slightly after base
        ctx.closePath();
        ctx.fill();

        // Add snow cap
        ctx.fillStyle = snowColor;
        ctx.beginPath();
        const peakX = mountainStart + mountainWidth * 0.5;
        const peakY = canvasHeight - mountainHeight;
        ctx.moveTo(peakX, peakY);
        ctx.lineTo(peakX - mountainWidth * 0.15, peakY + mountainHeight * 0.2);
        ctx.lineTo(peakX + mountainWidth * 0.15, peakY + mountainHeight * 0.2);
        ctx.closePath();
        ctx.fill();
    }

    // --- Particle System ---
    function createParticle() {
        // Particle represents a packet of moisture/water vapor
        const temp = parseInt(waterTempInput.value);
        const jetStrength = parseInt(jetStreamStrengthInput.value);

        // Probability of creating a particle based on temp (evaporation) and jet stream (pull)
        // Scale temp [15, 35] -> creation factor [0.5, 2]
        const tempFactor = (temp - 15) / 20 * 1.5 + 0.5;
        // Scale jet strength [50, 250] -> creation factor [0.5, 2]
        const jetFactor = (jetStrength - 50) / 200 * 1.5 + 0.5;

        // Combined probability per frame
        const creationProb = 0.008 * tempFactor * jetFactor; // Base prob * factors

        if (Math.random() < creationProb) {
             const riverLayerMin = canvasHeight * 0.3;
             const riverLayerMax = canvasHeight * 0.6;
             particles.push({
                x: 0, // Start at the very left edge (ocean source)
                y: riverLayerMin + Math.random() * (riverLayerMax - riverLayerMin), // Start within the river layer height
                z: Math.random() * 10, // Depth for size/opacity variation (unused in this 2D render)
                color: 'rgba(150, 150, 255, 0.9)', // Light blue for moisture
                size: 3,
                state: 'river', // Particles start directly in the river state
                condensation: 0 // How much condensation has occurred (0 to 1)
            });
        }
    }

    function updateParticles() {
        const jetStrength = parseInt(jetStreamStrengthInput.value) / 100; // Scale jet strength (e.g., 150 -> 1.5)

        for (let i = particles.length - 1; i >= 0; i--) {
            const p = particles[i];

            if (p.state === 'river') {
                // Move horizontally with jet stream
                p.x += jetStrength * 3 * timeStep * 60; // Scale movement by strength and time step (~pixels/sec)

                // Random vertical movement within the atmospheric layer
                const riverLayerMin = canvasHeight * 0.3;
                const riverLayerMax = canvasHeight * 0.6;
                p.y += (Math.random() - 0.5) * 5 * timeStep * 60;
                 // Constrain particle height
                 p.y = Math.max(riverLayerMin, Math.min(riverLayerMax, p.y));


                // Check if over mountain influence area
                 if (p.x >= mountainStart - 50 && p.x <= mountainStart + mountainWidth + 50) { // Influence area starts before mountain
                     // Calculate the mountain base y position at the particle's x coordinate
                     let mountainBaseY = canvasHeight;
                      if (p.x >= mountainStart - 20 && p.x <= mountainStart + mountainWidth + 20) {
                          // Simple linear interpolation for mountain shape
                           if (p.x <= mountainStart + mountainWidth / 2) {
                              // Left slope
                              mountainBaseY = canvasHeight - (p.x - mountainStart) * (mountainHeight / (mountainWidth / 2));
                           } else {
                              // Right slope
                              mountainBaseY = canvasHeight - (mountainStart + mountainWidth - p.x) * (mountainHeight / (mountainWidth / 2));
                           }
                          mountainBaseY = Math.max(canvasHeight - mountainHeight, mountainBaseY); // Clamp at peak height
                      } else {
                          // If slightly before/after mountain bounds, but still in influence zone, mountainBaseY is canvasHeight
                           mountainBaseY = canvasHeight;
                      }


                     // If particle is above the potential mountain base height, it's forced up
                     if (p.y > mountainBaseY + 10) { // Add a buffer
                         // Force particle upwards towards mountain contour
                         const forceUpSpeed = (p.y - mountainBaseY) * 0.1; // Force increases as it gets closer/below mountain
                         p.y -= forceUpSpeed * timeStep * 60;

                          // Increase condensation as it is forced up
                         p.condensation += 0.02;
                         p.condensation = Math.min(1, p.condensation); // Clamp condensation at 1

                         // Change color towards white/grey as it condenses
                          const c = 150 + Math.round(p.condensation * 100); // Ranges from 150 to 250
                          p.color = `rgba(${c}, ${c}, ${c}, 0.9)`;
                          p.size = 3 + p.condensation * 2; // Grow slightly

                         // If significant condensation, transition to raining
                         if (p.condensation >= 0.8) { // Threshold for rain
                             p.state = 'raining';
                             p.color = 'rgba(100, 100, 255, 1)'; // Darker blue for rain
                             p.size = 2; // Raindrops are smaller
                         }

                     } else {
                          // Over influence area but not forced up yet, maybe slight condensation happens anyway?
                          p.condensation += 0.005;
                          p.condensation = Math.min(0.5, p.condensation); // Limited condensation without lift
                           const c = 150 + Math.round(p.condensation * 100);
                           p.color = `rgba(${c}, ${c}, ${c}, 0.9)`;
                           p.size = 3 + p.condensation * 1;
                     }
                 } else if (p.condensation > 0) {
                     // Particle is outside mountain influence and has condensation, it will lose it
                     p.condensation -= 0.01;
                     p.condensation = Math.max(0, p.condensation);
                     const c = 150 + Math.round(p.condensation * 100);
                     p.color = `rgba(${c}, ${c}, ${c}, 0.9)`;
                      p.size = 3 + p.condensation * 1;
                      if (p.condensation === 0) {
                           p.color = 'rgba(150, 150, 255, 0.9)'; // Revert to initial color
                           p.size = 3;
                      }
                 }


            } else if (p.state === 'raining') {
                 // Move downwards towards ground faster
                 p.y += 15 * timeStep * 60; // Faster descent for rain

                 // Calculate the landscape y position at the particle's x position
                 let landscapeY = canvasHeight; // Default ground level

                 // Check if particle x is within mountain bounds (including base)
                 if (p.x >= mountainStart - 20 && p.x <= mountainStart + mountainWidth + 20) {
                      // Simple linear interpolation for mountain shape
                       if (p.x <= mountainStart + mountainWidth / 2) {
                          // Left slope
                          landscapeY = canvasHeight - (p.x - mountainStart) * (mountainHeight / (mountainWidth / 2));
                       } else {
                          // Right slope
                          landscapeY = canvasHeight - (mountainStart + mountainWidth - p.x) * (mountainHeight / (mountainWidth / 2));
                       }
                      landscapeY = Math.max(canvasHeight - mountainHeight, landscapeY); // Clamp at peak height
                 } else if (p.x > oceanWidth) {
                     // Over flat land area
                     landscapeY = canvasHeight;
                 } else {
                      // Over ocean - should not rain here based on current logic, but handle edge case
                      landscapeY = canvasHeight + 100; // Essentially below ground
                 }

                 // Check if particle's y position is below (or equal to) the landscape y position
                 if (p.y >= landscapeY) {
                      // Hit the ground or the mountain slope
                      // Check if it's on the windward side (left side, where the river comes from) of the mountain
                      // From the start of the mountain base to just past the peak (approx)
                      if (p.x >= mountainStart - 20 && p.x <= mountainStart + mountainWidth / 2 + 40) {
                           totalPrecipitation += 0.1; // Add a small amount of rain per particle (increased amount)
                           totalPrecipitationDiv.textContent = `סה"כ משקעים מעל ההרים: ${totalPrecipitation.toFixed(1)} מ"מ`;
                      }
                      p.state = 'done'; // Particle finished its cycle
                 }
            }

            // Remove particles that are done or have gone significantly off screen
            if (p.state === 'done' || p.x < -50 || p.y < -50 || p.y > canvasHeight + 50 || p.x > canvasWidth + 50) {
                particles.splice(i, 1);
            }
        }
         // Update particle count display
         particleCountDiv.textContent = particles.length;
    }

    function drawParticles() {
        particles.forEach(p => {
            if (p.state !== 'done') {
                 ctx.fillStyle = p.color;
                 if (p.state === 'raining') {
                     // Draw as a small vertical line (raindrop)
                     ctx.fillRect(p.x - p.size/2, p.y - p.size*2, p.size, p.size*3); // Draw a short vertical line
                 } else {
                     // Draw as a circle (moisture particle)
                     ctx.beginPath();
                     ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                     ctx.fill();
                 }
            }
        });
    }

    // --- Game Loop and Simulation Control ---
    function gameLoop() {
        // Redraw everything for the current frame regardless of simulation state
        drawBackground();
        drawMountains();

        if (simulationRunning) {
            // Update simulation state
            createParticle();
            updateParticles();

            // Update simulation time (simplified, actual time varies with frame rate)
            simulationTime += timeStep;
            simulationTimeDiv.textContent = `זמן סימולציה: ${simulationTime.toFixed(1)} שניות`;

            // Draw particles only if simulation is running
            drawParticles();
        }


        // Request next frame
        animationFrameId = requestAnimationFrame(gameLoop);
    }

    function startSimulation() {
        if (simulationRunning) return; // Prevent multiple starts
        simulationRunning = true;
        particles = []; // Clear existing particles
        totalPrecipitation = 0;
        simulationTime = 0;
        totalPrecipitationDiv.textContent = `סה"כ משקעים מעל ההרים: ${totalPrecipitation.toFixed(1)} מ"מ`;
        simulationTimeDiv.textContent = `זמן סימולציה: ${simulationTime.toFixed(1)} שניות`;
        particleCountDiv.textContent = particles.length;

        startButton.disabled = true;
        resetButton.disabled = false;
        // Disable inputs during simulation
        waterTempInput.disabled = true;
        jetStreamStrengthInput.disabled = true;
        mountainPositionInput.disabled = true;

         // Start the animation loop if it's not already running
         if (!animationFrameId) {
             gameLoop();
         }
    }

    function resetSimulation() {
         simulationRunning = false;
         // No need to cancelAnimationFrame if the loop checks simulationRunning
         particles = [];
         totalPrecipitation = 0;
         simulationTime = 0;
         totalPrecipitationDiv.textContent = `סה"כ משקעים מעל ההרים: ${totalPrecipitation.toFixed(1)} מ"מ`;
         simulationTimeDiv.textContent = `זמן סימולציה: ${simulationTime.toFixed(1)} שניות`;
         particleCountDiv.textContent = particles.length;

         startButton.disabled = false;
         resetButton.disabled = true;
         // Enable inputs after reset
         waterTempInput.disabled = false;
         jetStreamStrengthInput.disabled = false;
         mountainPositionInput.disabled = false;

         // Redraw initial state immediately
         drawBackground();
         drawMountains();
    }

    // --- Event Listeners and Initial State ---
    startButton.addEventListener('click', startSimulation);
    resetButton.addEventListener('click', resetSimulation);
    resetButton.disabled = true; // Initially disabled

    // Update display for initial values
    waterTempValue.textContent = waterTempInput.value;
    jetStreamStrengthValue.textContent = jetStreamStrengthInput.value;
    mountainPositionValue.textContent = mountainPositionInput.value;

    // Add listeners to update values display
    waterTempInput.addEventListener('input', () => { waterTempValue.textContent = waterTempInput.value; });
    jetStreamStrengthInput.addEventListener('input', () => { jetStreamStrengthValue.textContent = jetStreamStrengthInput.value; });
    mountainPositionInput.addEventListener('input', () => {
        mountainPositionValue.textContent = mountainPositionInput.value;
        updateMountainPosition();
        drawBackground(); // Redraw background and mountains when mountain position changes
        drawMountains();
    });


    // Explanation button toggle
    explanationButton.addEventListener('click', () => {
        const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
        explanationContent.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר הסבר מורחב' : 'הצג הסבר מורחב על נהרות אטמוספיריים';
    });

    // Start the animation loop once to draw the initial state and keep it running for updates
    gameLoop();

});
</script>