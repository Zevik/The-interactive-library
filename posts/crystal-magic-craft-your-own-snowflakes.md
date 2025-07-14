---
title: "קסם הגבישים: צרו פתיתי שלג משלכם"
english_slug: crystal-magic-craft-your-own-snowflakes
category: "מדעים מדויקים / פיזיקה"
tags: ["שלג", "גבישים", "טמפרטורה", "לחות", "קריסטלוגרפיה", "מטאורולוגיה", "סימולציה"]
---
# קסם הגבישים: צרו פתיתי שלג משלכם

כל פתית שלג הוא פלא זעיר וחד פעמי של הטבע. למרות שכולם נבנים על פי סימטריה משושה בסיסית, הצורות המגוונות והמורכבות שלהם נראות אינסופיות. מהו הסוד מאחורי המגוון המרהיב הזה? האם ניתן לשלוט על צורת הגביש?

<div class="app-container">
    <h2>בחנו בעצמכם: אילו תנאים יוצרים אילו גבישים?</h2>
    <div class="controls">
        <div class="control-group">
            <label for="temp-slider">טמפרטורה (°C):</label>
            <input type="range" id="temp-slider" min="-30" max="0" value="-15" step="1">
            <span id="temp-value">-15°C</span>
        </div>
        <div class="control-group">
            <label for="humidity-slider">לחות יחסית גבוהה (%):</label>
            <input type="range" id="humidity-slider" min="50" max="100" value="80" step="1">
            <span id="humidity-value">80%</span>
        </div>
        <button id="create-crystal-button">צרו גביש שלג קפוא!</button>
    </div>
    <div class="simulation-area" id="simulation-area">
        <!-- Snowflake SVG will be rendered here -->
        <svg id="snowflake-svg" viewBox="-150 -150 300 300" width="100%" height="100%"></svg>
        <div id="loading-overlay" class="loading-overlay">
            <div class="spinner"></div>
            <p>יוצרים קסם קפוא...</p>
        </div>
    </div>
</div>

<button id="toggle-explanation" aria-expanded="false">הסקרנות מקפיאה? הצג/הסתר את הסודות</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: כיצד נוצרים גבישי שלג? המדע מאחורי הקסם</h2>

    <p>בואו נעשה סדר: "גביש שלג" הוא גביש קרח בודד שצומח ישירות מאדי מים באטמוספרה הקרה. "פתית שלג" הוא בדרך כלל צביר של גבישי שלג מרובים שהתחברו יחד בדרכם מטה אל הקרקע.</p>

    <p>לידתו של גביש שלג מתרחשת בגובה רב בעננים, באזורים שבהם הטמפרטורה צונחת מתחת ל-0°C. הכל מתחיל בגרעין מיקרוסקופי – אולי חלקיק אבק זעיר או אבקת צמחים – שמשמש כבסיס. כשאדי מים קרים במיוחד פוגשים את הגרעין הזה, הם מדלגים על מצב נוזל (מים) וקופאים מיד למצב מוצק (קרח) בתהליך מופלא שנקרא "דפוזיציה". מולקולות המים מתחילות להיערם באופן מסודר סביב הגרעין, ובונות בהדרגה מבנה גבישי בעל שש פינות – הצורה המשושה המוכרת.</p>

    <h3>הטמפרטורה: מפקדת התזמורת של הצורה</h3>
    <p>אם לגביש שלג יש "אדריכל" ראשי, זוהי הטמפרטורה! אופן ומהירות הצטרפותן של מולקולות המים אל פני הגביש משתנים בצורה דרמטית בכל מעלה צלזיוס בודדת, ויוצרים גיוון עצום בצורות הסופיות:</p>
    <ul>
        <li>**0°C עד -4°C:** לרוב גבישים שטוחים דמויי פלטות או כוכבים פשוטים ועדינים.</li>
        <li>**-4°C עד -6°C:** כאן מופיעות המחטים! גבישים דקים וארוכים, כמו עפרונות קרח.</li>
        <li>**-6°C עד -10°C:** צורות פריזמטיות – עמודים חלולים או מלאים, לעיתים קצרים ועבים.</li>
        <li>**-10°C עד -12°C:** חוזרים לצורות שטוחות, פלטות או כוכבים, אך לרוב מוגדרים ומפורטים יותר.</li>
        <li>**-12°C עד -16°C:** הבימה לדנדריטים! אלו הם הכוכבים המורכבים, המסועפים והמרשימים ביותר, המזוהים לרוב עם "הפתית המושלם". זהו "אזור הזהב" לצורות ראוותניות.</li>
        <li>**-16°C ומטה (עד כ-22°C):** שילובים של פלטות ועמודים, לעיתים מורכבים אך בדרך כלל פחות מסועפים מדנדריטים טיפוסיים.</li>
         <li>**מתחת ל-22°C:** לרוב צורות פשוטות יותר, כגון פלטות משושות או עמודים.</li>
    </ul>
    <p>המעברים החדים בין הצורות הללו הם תוצאה של כימיה פיזיקלית מורכבת על פני שטח הקרח, המשפיעה על "היכן" ו"באיזו מהירות" מולקולות המים החדשות נקשרות לגביש.</p>

    <h3>לחות: דלק הגידול והמורכבות</h3>
    <p>הלחות היחסית (כמות אדי המים הזמינה ביחס לרוויה) היא הגורם המאיץ. דמיינו אותה כדלק עבור הגביש: ככל שהלחות גבוהה יותר (קרובה ל-100% או מעט מעליה), כך יש יותר "חומר גלם" זמין להתגבשות. התוצאה:</p>
    <ul>
        <li>**קצב גידול מהיר יותר:** הגביש גדל בקצב מוגבר.</li>
        <li>**מורכבות גבוהה יותר:** בתנאי טמפרטורה מתאימים (כמו בטווח הדנדריטים), לחות גבוהה תוביל לגבישים גדולים יותר, עם יותר ענפים, סעיפים ופרטים עדינים.</li>
    </ul>
    <p>בלחות נמוכה, הגידול איטי יותר והגבישים שומרים על צורות פשוטות יותר, גם אם הטמפרטורה מאפשרת מורכבות פוטנציאלית.</p>

    <h3>מסע הגביש: סיפור חייו המפוסל</h3>
    <p>נדיר שגביש שלג גדל בתנאי טמפרטורה ולחות אחידים לכל אורך חייו. בזמן שהוא צונח מטה דרך שכבות הענן והאטמוספרה, הוא נתקל בתנאים משתנים. כל "תחנה" במסע משפיעה על אופן הגידול באותו רגע, מוסיפה עוד שכבה או מבנה לצורתו הסופית. גביש יכול להתחיל כעמוד, להיכנס לאזור חם יותר ולפתח קצוות בצורת פלטות, ואז אולי לעבור דרך אזור לח במיוחד ולהצמיח ענפים עדינים נוספים. המסלול הייחודי של כל גביש הוא זה שחותם את צורתו הסופית.</p>

    <h3>למה כמעט אין שני פתיתי שלג זהים?</h3>
    <p>השילוב הבלתי-אפשרי כמעט לשחזור של כל הגורמים: התלות הרגישה בטמפרטורה המשתנה בכל רגע, השפעת הלחות התנודתית, ומסלול הנפילה הייחודי שחווה כל גביש בדרכו מטה – יוצרים מגוון עצום שגורם לכל גביש להיות יצירה סטטיסטית כמעט חד פעמית. כל גביש הוא למעשה "יומן מסע" קפוא של התנאים המדויקים בהם הוא נוצר וגדל.</p>
</div>


<style>
/* Import a nice font */
@import url('https://fonts.googleapis.com/css2?family=Varela+Round&display=swap');

body {
    font-family: 'Varela Round', sans-serif;
    line-height: 1.7;
    direction: rtl;
    text-align: right;
    margin: 0;
    background: linear-gradient(to bottom, #e0f2f7, #b3e5fc); /* Gentle blue gradient */
    color: #2c3e50; /* Dark blue-gray */
    padding: 20px;
}

h1, h2, h3 {
    color: #01579b; /* Darker blue */
    text-align: center;
    margin-bottom: 20px;
    font-weight: bold;
}

h1 {
    font-size: 2.5em;
    margin-top: 0;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
}

h2 {
     font-size: 1.8em;
}

.app-container, #explanation {
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    padding: 30px;
    margin: 20px auto;
    max-width: 800px;
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 1px solid #b3e5fc; /* Match gradient border */
}

.controls {
    width: 100%;
    max-width: 500px;
    margin-bottom: 30px;
    padding: 20px;
    background-color: #e1f5fe; /* Very light blue */
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
}

.control-group {
    display: flex;
    flex-direction: column; /* Stack label and slider */
    align-items: flex-start; /* Align labels to the right (RTL) */
    gap: 8px;
}

.control-group label {
    font-weight: bold;
    color: #0277bd; /* Medium blue */
    font-size: 1.1em;
}

.control-group span {
    font-family: monospace; /* Fixed width font for value */
    font-size: 1.1em;
    color: #01579b;
}


.control-group input[type="range"] {
    flex-grow: 1;
    width: 100%; /* Make slider fill container */
    -webkit-appearance: none;
    appearance: none;
    height: 10px;
    background: #b0bec5; /* Light gray */
    outline: none;
    opacity: 0.9;
    transition: opacity .2s, transform 0.2s ease-in-out;
    border-radius: 5px;
    cursor: grab;
}
.control-group input[type="range"]:active {
     cursor: grabbing;
     transform: scale(1.01);
}

.control-group input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 24px;
    height: 24px;
    background: #039be5; /* Bright blue */
    cursor: pointer;
    border-radius: 50%;
    border: 3px solid #ffffff; /* White border */
    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    transition: background-color 0.2s ease, transform 0.2s ease;
}

.control-group input[type="range"]::-webkit-slider-thumb:hover {
    background-color: #0288d1; /* Slightly darker blue */
    transform: scale(1.1);
}

.control-group input[type="range"]::-moz-range-thumb {
    width: 24px;
    height: 24px;
    background: #039be5;
    cursor: pointer;
    border-radius: 50%;
    border: 3px solid #ffffff;
    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    transition: background-color 0.2s ease, transform 0.2s ease;
}
.control-group input[type="range"]::-moz-range-thumb:hover {
     background-color: #0288d1;
     transform: scale(1.1);
}

#create-crystal-button {
    padding: 12px 25px;
    background-color: #007bff; /* Blue */
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.2em;
    font-weight: bold;
    transition: background-color 0.3s ease, transform 0.1s ease;
    align-self: center;
    margin-top: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

#create-crystal-button:hover:not(:disabled) {
    background-color: #0056b3; /* Darker blue */
    transform: translateY(-2px);
}
#create-crystal-button:active:not(:disabled) {
     transform: translateY(0);
     box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
#create-crystal-button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
}


.simulation-area {
    position: relative; /* For overlay */
    width: 100%;
    max-width: 400px;
    aspect-ratio: 1 / 1;
    border: 2px dashed #b3e5fc; /* Icy border */
    background-color: #e0f7fa; /* Very light cyan */
    border-radius: 12px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    box-shadow: inset 0 0 10px rgba(0, 188, 212, 0.1);
    transition: background-color 0.5s ease; /* Smooth background change */
}

#snowflake-svg {
    width: 100%;
    height: 100%;
    display: block;
    stroke: #00bcd4; /* Cyan/Teal */
    stroke-width: 3;
    stroke-linecap: round;
    stroke-linejoin: round;
    fill: none; /* Default - shapes will set fill if needed */
}

.loading-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(255, 255, 255, 0.8);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    z-index: 10;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s ease, visibility 0.3s ease;
}
.loading-overlay.visible {
    opacity: 1;
    visibility: visible;
}

.spinner {
  border: 4px solid rgba(0, 0, 0, 0.1);
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border-left-color: #039be5;
  animation: spin 1s ease infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-overlay p {
    margin-top: 10px;
    font-size: 1.1em;
    color: #01579b;
    font-weight: bold;
}


#toggle-explanation {
    display: block;
    margin: 30px auto;
    padding: 12px 25px;
    background-color: #78909c; /* Blue-gray */
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.1em;
    font-weight: bold;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

#toggle-explanation:hover {
    background-color: #546e7a; /* Darker blue-gray */
    transform: translateY(-2px);
}
#toggle-explanation:active {
     transform: translateY(0);
     box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}


#explanation {
    /* Styles defined above */
    border-top: 3px solid #039be5; /* Accent line */
}

#explanation h3 {
    color: #0277bd; /* Medium blue */
    margin-top: 25px;
    margin-bottom: 12px;
    border-bottom: 1px dashed #b0bec5; /* Subtle separator */
    padding-bottom: 5px;
}

#explanation ul {
    margin-bottom: 20px;
    padding-right: 20px; /* RTL list padding */
}

#explanation li {
    margin-bottom: 8px;
    padding-right: 0; /* Ensure no default padding left */
}

/* Optional: Style for specific shapes */
.snowflake-arm line { stroke: #00bcd4; stroke-width: 3; }
.snowflake-arm.needle line { stroke: #00acc1; stroke-width: 2; }
.snowflake-arm.column line { stroke: #00838f; stroke-width: 6; } /* Thicker */
.snowflake-arm.plate line { stroke: #4dd0e1; stroke-width: 3; }
.snowflake-arm.dendrite line { stroke: #00e5ff; stroke-width: 2; } /* Brighter */
.snowflake-arm polygon { fill: #e0f7fa; stroke: #00bcd4; stroke-width: 2; } /* Fill for simple shapes */

/* Animation styles - basic line growth */
/* Needs JS to apply animations to individual segments or control drawing */

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const tempSlider = document.getElementById('temp-slider');
    const humiditySlider = document.getElementById('humidity-slider');
    const tempValueSpan = document.getElementById('temp-value');
    const humidityValueSpan = document.getElementById('humidity-value');
    const createCrystalButton = document.getElementById('create-crystal-button');
    const snowflakeSVG = document.getElementById('snowflake-svg');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const loadingOverlay = document.getElementById('loading-overlay');

    // Update value displays when sliders move
    tempSlider.addEventListener('input', () => {
        tempValueSpan.textContent = `${tempSlider.value}°C`;
    });

    humiditySlider.addEventListener('input', () => {
        humidityValueSpan.textContent = `${humiditySlider.value}%`;
        // Adjust label text slightly based on value? Or just keep it simple.
        // humidityValueSpan.textContent = `${humiditySlider.value}% לחות גבוהה`; // Example change
    });

    // Function to determine shape type based on temperature
    function determineShapeType(temp) {
        if (temp >= -4 && temp <= 0) return 'plate';
        if (temp > -6 && temp <= -4) return 'needle';
        if (temp > -10 && temp <= -6) return 'column';
        if (temp > -12 && temp <= -10) return 'plate'; // Can be sector plates too
        if (temp > -16 && temp <= -12) return 'dendrite';
        if (temp > -22 && temp <= -16) return 'plate-column-combo'; // Often combinations
        return 'simple'; // Below -22, often simple plates or columns
    }

    // Function to generate snowflake structure (logic for animation)
    function generateSnowflakeSteps(temp, humidity) {
        const size = 120; // Base size for the main arms
        const complexity = (humidity - 50) / 50; // Scale humidity from 0 to 1 (50% to 100%)
        const shapeType = determineShapeType(temp);
        const steps = []; // Array to hold drawing steps (SVG elements to add)

        // Add central node/seed
         steps.push({ type: 'circle', cx: 0, cy: 0, r: 5, fill: '#ffffff', stroke: '#00bcd4', 'stroke-width': 1 });


        // Define arm structure based on shape type and complexity
        for (let i = 0; i < 6; i++) {
            const armGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
            armGroup.setAttribute('transform', `rotate(${i * 60})`);
            armGroup.classList.add('snowflake-arm', shapeType); // Add class for styling

            // Main arm
            const mainArmLength = size;
            steps.push({ group: armGroup, type: 'line', x1: 0, y1: 0, x2: 0, y2: -mainArmLength, length: mainArmLength });

            if (shapeType === 'plate' || shapeType === 'dendrite' || shapeType === 'simple' || shapeType === 'plate-column-combo') {
                 const numSegments = shapeType === 'simple' ? 2 : (shapeType === 'plate' ? 3 : (shapeType === 'dendrite' ? 6 : 4));
                 const segmentLength = mainArmLength / numSegments;
                 const branchAngle = 60;
                 const minBranchLength = size * 0.05;
                 const maxBranchLength = size * 0.3 * complexity; // Max branch size depends on humidity

                for (let j = 1; j <= numSegments; j++) {
                    const y = -j * segmentLength;
                     // Branches get slightly shorter towards the tip, or grow with humidity
                    const currentBranchLength = minBranchLength + maxBranchLength * (1 - (j / numSegments * 0.8));

                     if (currentBranchLength > 2) { // Only add visible branches
                         // Branch left
                         const branchLeftX = -currentBranchLength * Math.sin(branchAngle * Math.PI / 180);
                         const branchLeftY = y - currentBranchLength * Math.cos(branchAngle * Math.PI / 180);
                         steps.push({ group: armGroup, type: 'line', x1: 0, y1: y, x2: branchLeftX, y2: branchLeftY, length: currentBranchLength });

                         // Branch right
                         const branchRightX = currentBranchLength * Math.sin(branchAngle * Math.PI / 180);
                         const branchRightY = y - currentBranchLength * Math.cos(branchAngle * Math.PI / 180);
                         steps.push({ group: armGroup, type: 'line', x1: 0, y1: y, x2: branchRightX, y2: branchRightY, length: currentBranchLength });

                         // Add sub-branches for dendrites
                         if (shapeType === 'dendrite' && complexity > 0.3) {
                             const subBranchLength = currentBranchLength * (complexity - 0.3) * 0.8;
                             if (subBranchLength > 3) {
                                const subBranchAngle = 40; // Angle relative to the main branch
                                 // Sub-branch left (from left branch tip)
                                 steps.push({ group: armGroup, type: 'line', x1: branchLeftX, y1: branchLeftY, x2: branchLeftX - subBranchLength * Math.sin((branchAngle - subBranchAngle) * Math.PI / 180), y2: branchLeftY - subBranchLength * Math.cos((branchAngle - subBranchAngle) * Math.PI / 180), length: subBranchLength });
                                 steps.push({ group: armGroup, type: 'line', x1: branchLeftX, y1: branchLeftY, x2: branchLeftX - subBranchLength * Math.sin((branchAngle + subBranchAngle) * Math.PI / 180), y2: branchLeftY - subBranchLength * Math.cos((branchAngle + subBranchAngle) * Math.PI / 180), length: subBranchLength });

                                 // Sub-branch right (from right branch tip)
                                steps.push({ group: armGroup, type: 'line', x1: branchRightX, y1: branchRightY, x2: branchRightX + subBranchLength * Math.sin((branchAngle + subBranchAngle) * Math.PI / 180), y2: branchRightY - subBranchLength * Math.cos((branchAngle + subBranchAngle) * Math.PI / 180), length: subBranchLength });
                                steps.push({ group: armGroup, type: 'line', x1: branchRightX, y1: branchRightY, x2: branchRightX + subBranchLength * Math.sin((branchAngle - subBranchAngle) * Math.PI / 180), y2: branchRightY - subBranchLength * Math.cos((branchAngle - subBranchAngle) * Math.PI / 180), length: subBranchLength });
                             }
                         }
                     }
                }
            } else if (shapeType === 'needle') {
                 // Needles: just make main arm thinner and potentially longer based on humidity
                 mainArmLength = size * (1 + complexity * 0.7); // Can grow quite long
                 steps.pop(); // Remove previous main arm step
                 steps.push({ group: armGroup, type: 'line', x1: 0, y1: 0, x2: 0, y2: -mainArmLength, length: mainArmLength, 'stroke-width': 2 }); // Thinner
            } else if (shapeType === 'column' || shapeType === 'plate-column-combo') {
                // Columns: Shorter, thicker prisms. Simplify as thick lines or rectangles.
                const columnHeight = size * (0.4 + complexity * 0.2); // Shorter
                const columnWidth = 3 + complexity * 6; // Thicker
                 steps.pop(); // Remove previous main arm step (basic line)
                 steps.push({ group: armGroup, type: 'rect', x: -columnWidth/2, y: -columnHeight, width: columnWidth, height: columnHeight, fill: '#00838f', stroke: 'none' }); // Draw a filled rectangle
                 // Add end caps for column view
                  if (complexity > 0.2) {
                      const capSize = columnWidth * 0.8;
                       steps.push({ group: armGroup, type: 'line', x1: -capSize/2, y1: -columnHeight, x2: capSize/2, y2: -columnHeight, length: capSize, stroke: '#00838f', 'stroke-width': 2 });
                  }
                 if (shapeType === 'plate-column-combo' && complexity > 0.5) {
                      // Add small plates at the ends of columns
                      const plateSize = size * 0.1 * (complexity - 0.5) * 2;
                       if (plateSize > 5) {
                            const plateGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
                            plateGroup.setAttribute('transform', `translate(0, ${-columnHeight - plateSize})`);
                            steps.push({ group: armGroup, subgroup: plateGroup, type: 'polygon', points: `0 ${plateSize}, ${plateSize * Math.sin(Math.PI/3)} ${plateSize * Math.cos(Math.PI/3)}, ${plateSize * Math.sin(Math.PI/3)} ${-plateSize * Math.cos(Math.PI/3)}, 0 ${-plateSize}, ${-plateSize * Math.sin(Math.PI/3)} ${-plateSize * Math.cos(Math.PI/3)}, ${-plateSize * Math.sin(Math.PI/3)} ${plateSize * Math.cos(Math.PI/3)}`, fill: '#4dd0e1', stroke: '#00bcd4', 'stroke-width': 1 });
                       }
                 }

            } else if (shapeType === 'simple') {
                 // Simple plates/hexagons
                 steps.pop(); // Remove basic main arm
                 const simpleHexSize = size * (0.4 + complexity * 0.4);
                 if (simpleHexSize > 15) {
                    let points = "";
                    for(let k=0; k<6; k++) {
                        const angle = Math.PI/2 + k * Math.PI/3; // Start from top, clockwise
                        points += `${simpleHexSize * Math.cos(angle)}, ${-simpleHexSize * Math.sin(angle)} `;
                    }
                     steps.push({ group: armGroup, type: 'polygon', points: points.trim(), fill: '#e0f7fa', stroke: '#00bcd4', 'stroke-width': 2 });
                 } else {
                     // Very simple dot or small line
                      steps.push({ group: armGroup, type: 'circle', cx: 0, cy: -simpleHexSize, r: 3, fill: '#00bcd4' });
                 }
            }
             // Append the arm group itself to SVG in a step if it contains elements
             if (armGroup.hasChildNodes() || steps.some(step => step.group === armGroup)) {
                 steps.push({ type: 'append-group', group: armGroup });
             }
        }

         // Sort steps roughly by length to draw shorter segments first (visual preference)
        steps.sort((a, b) => (a.length || 0) - (b.length || 0));


        return steps;
    }

    // Function to animate snowflake growth
    function animateSnowflake(steps) {
        snowflakeSVG.innerHTML = ''; // Clear previous snowflake
        snowflakeSVG.style.opacity = 0; // Start invisible
        snowflakeSVG.style.transition = 'opacity 0.5s ease-in'; // Add fade-in transition

        const totalSteps = steps.length;
        let currentStepIndex = 0;
        const animationDuration = 1500; // Total animation time in ms
        const stepInterval = animationDuration / totalSteps; // Time between drawing each step

        loadingOverlay.classList.remove('visible'); // Hide loading on animation start
        createCrystalButton.disabled = true; // Disable button during animation

        function performStep() {
            if (currentStepIndex >= totalSteps) {
                // Animation finished
                snowflakeSVG.style.opacity = 1; // Ensure full visibility
                 createCrystalButton.disabled = false; // Re-enable button
                return;
            }

            const step = steps[currentStepIndex];
            let element;

            if (step.type === 'append-group') {
                snowflakeSVG.appendChild(step.group);
            } else if (step.type === 'circle') {
                 element = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
                 element.setAttribute('cx', step.cx);
                 element.setAttribute('cy', step.cy);
                 element.setAttribute('r', step.r);
                 element.setAttribute('fill', step.fill || 'none');
                 if (step.stroke) element.setAttribute('stroke', step.stroke);
                 if (step['stroke-width']) element.setAttribute('stroke-width', step['stroke-width']);
                 snowflakeSVG.appendChild(element); // Append directly for central circle
            }
            else {
                // Create SVG element
                element = document.createElementNS('http://www.w3.org/2000/svg', step.type);
                if (step.type === 'line') {
                    element.setAttribute('x1', step.x1);
                    element.setAttribute('y1', step.y1);
                    element.setAttribute('x2', step.x2);
                    element.setAttribute('y2', step.y2);
                } else if (step.type === 'rect') {
                     element.setAttribute('x', step.x);
                     element.setAttribute('y', step.y);
                     element.setAttribute('width', step.width);
                     element.setAttribute('height', step.height);
                     element.setAttribute('fill', step.fill || 'none');
                } else if (step.type === 'polygon') {
                     element.setAttribute('points', step.points);
                     element.setAttribute('fill', step.fill || 'none');
                }

                // Apply styles from step or default from CSS
                 if (step.stroke) element.setAttribute('stroke', step.stroke);
                 if (step['stroke-width']) element.setAttribute('stroke-width', step['stroke-width']);
                 if (step.fill) element.setAttribute('fill', step.fill);


                // Append to correct group or SVG root
                if (step.subgroup) {
                    if (!step.group.contains(step.subgroup)) {
                         step.group.appendChild(step.subgroup);
                    }
                     step.subgroup.appendChild(element);
                }
                else if (step.group) {
                     step.group.appendChild(element);
                } else {
                    snowflakeSVG.appendChild(element);
                }
            }


            currentStepIndex++;
            requestAnimationFrame(() => setTimeout(performStep, stepInterval)); // Use requestAnimationFrame for smoothness
        }

        // Initial opacity for fade-in
         snowflakeSVG.style.opacity = 0;

        // Start the animation sequence
         requestAnimationFrame(() => {
              setTimeout(performStep, stepInterval); // Wait initial interval before first draw
         });
    }


    // Event listener for the button click
    createCrystalButton.addEventListener('click', () => {
        loadingOverlay.classList.add('visible'); // Show loading overlay
         createCrystalButton.disabled = true; // Disable button immediately
        const currentTemp = parseInt(tempSlider.value);
        const currentHumidity = parseInt(humiditySlider.value);

         // Add a small delay before starting generation/animation to show loading
         setTimeout(() => {
              const steps = generateSnowflakeSteps(currentTemp, currentHumidity);
             animateSnowflake(steps);
         }, 500); // 500ms delay

    });

    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.setAttribute('aria-expanded', !isHidden);
        // Update button text (optional)
        // toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'הצג הסבר';
    });

    // Generate initial snowflake on page load with a short animation
    // Use default values or maybe a random interesting combination? Let's use default.
     const initialTemp = parseInt(tempSlider.value);
     const initialHumidity = parseInt(humiditySlider.value);

     // Add a small delay before the first animation too
     setTimeout(() => {
          const initialSteps = generateSnowflakeSteps(initialTemp, initialHumidity);
          animateSnowflake(initialSteps);
     }, 300); // Short delay for page load animation
});
</script>