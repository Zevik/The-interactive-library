---
title: "עומק קיצוני: כך שורדים יצורי הים את הלחץ האדיר"
english_slug: extreme-depth-how-sea-creatures-survive-immense-pressure
category: "ביולוגיה ימית"
tags: ["ביולוגיה ימית", "ים עמוק", "לחץ הידרוסטטי", "התאמה פיזיולוגית", "ביוכימיה"]
---
# עומק קיצוני: כך שורדים יצורי הים את הלחץ האדיר

דמיינו לחץ עצום שמסוגל למעוך צוללת. זו המציאות היומיומית של יצורי הים העמוק. כיצד הם מתמודדים עם כוח בלתי נתפס זה ושומרים על תפקוד החיים? צללו איתנו למעמקי הים וגלו את המנגנונים הביוכימיים והפיזיולוגיים המדהימים המאפשרים חיים בסביבה הקיצונית ביותר על פני כדור הארץ.

<div id="deep-sea-pressure-app">
    <div id="ocean-column">
        <div id="depth-marker"></div>
         <div id="depth-indicator">0 מטר</div>
    </div>
    <div id="interactive-area">
        <div id="pressure-gauge">
            <h3>לחץ הידרוסטטי:</h3>
            <div id="pressure-display">1.0 אטמוספירות</div>
            <div class="slider-container">
                <input type="range" id="depth-slider" min="0" max="11000" value="0">
                <div id="slider-min-label">0 מ' (1 אטמ')</div>
                <div id="slider-max-label">11,000 מ' (~1101 אטמ')</div>
            </div>
        </div>

        <div id="molecule-area">
            <div class="molecule-model" id="normal-molecule">
                <h3>מולקולה רגילה (לא מותאמת):</h3>
                <div class="molecule-representation">
                    <div class="folding-unit unit-1"></div>
                    <div class="folding-unit unit-2"></div>
                    <div class="folding-unit unit-3"></div>
                    <div class="folding-unit unit-4"></div>
                </div>
                <div class="molecule-status" id="normal-status">יציבה ותקינה</div>
            </div>
            <div class="molecule-model" id="deep-sea-molecule">
                <h3>מולקולת ים עמוק (מותאמת):</h3>
                <div class="molecule-representation">
                    <div class="folding-unit adaptable unit-a" data-mechanism="protein-structure" data-tooltip="מבנה חלבון עמיד ללחץ"></div>
                    <div class="folding-unit adaptable unit-b" data-mechanism="osmolytes" data-tooltip="אוסמוליטים מייצבים (כמו TMAO)"></div>
                    <div class="membrane-unit adaptable unit-c" data-mechanism="membrane-lipids" data-tooltip="ממברנה עם ליפידים מותאמים"></div>
                    <div class="folding-unit adaptable unit-d" data-mechanism="protein-structure" data-tooltip="מבנה חלבון עמיד ללחץ"></div>
                </div>
                <div class="molecule-status" id="deep-sea-status">יציבה ועמידה</div>
            </div>
        </div>
        <div id="adaptation-explanation">
            <h4>לחצו על חלק במולקולה המותאמת:</h4>
            <p id="explanation-text">גלו את סודות ההישרדות ברמה המולקולרית.</p>
        </div>
    </div>
</div>

<style>
:root {
    --ocean-start-color: #0077be;
    --ocean-end-color: #0a0a5c;
    --ui-background: rgba(255, 255, 255, 0.95);
    --molecule-normal-color: #3498db;
    --molecule-membrane-color: #2ecc71;
    --status-normal: green;
    --status-warning: orange;
    --status-danger: red;
    --denature-color: #e74c3c;
    --denature-transform-scale: 1.1;
    --denature-transform-rotate: 15deg; /* Reduced rotation for gradual effect */
     --membrane-transform-scaleY: 1.3; /* Reduced scaleY for gradual effect */
}

#deep-sea-pressure-app {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    padding: 30px;
    background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2); /* Softer background */
    border-radius: 12px;
    max-width: 1100px;
    margin: 30px auto;
    box-shadow: 0 10px 20px rgba(0,0,0,0.15);
    overflow: hidden; /* Clean edges */
}

#ocean-column {
    flex: 1;
    min-width: 250px;
    background: linear-gradient(to bottom, var(--ocean-start-color), var(--ocean-end-color));
    position: relative;
    height: 500px; /* Increased height */
    border-radius: 8px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-end;
    padding-bottom: 20px;
    box-shadow: inset 0 0 15px rgba(0,0,0,0.2); /* Inner shadow for depth */
}

#depth-marker {
    width: 40px; /* Larger marker */
    height: 40px;
    background-color: #ffeb3b; /* Yellow */
    border-radius: 50%;
    position: absolute;
    left: 50%;
    transform: translate(-50%, -50%); /* Center marker */
    transition: top 0.5s ease-out; /* Smooth movement */
    box-shadow: 0 0 15px rgba(255,235,59,0.5); /* Glow effect */
    z-index: 10; /* Ensure it's above ocean effects */
}

#depth-indicator {
    position: absolute;
    top: 0;
    left: calc(50% + 30px); /* Position next to marker */
    transform: translateY(-50%);
    background-color: rgba(0, 0, 0, 0.6);
    color: white;
    padding: 5px 10px;
    border-radius: 5px;
    font-size: 0.9em;
    white-space: nowrap;
     transition: top 0.5s ease-out;
    z-index: 9;
}


#interactive-area {
    flex: 2;
    min-width: 350px; /* Adjusted min-width */
    display: flex;
    flex-direction: column;
    gap: 25px; /* Increased gap */
}

#pressure-gauge {
    background-color: var(--ui-background);
    padding: 20px; /* More padding */
    border-radius: 8px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

#pressure-gauge h3 {
     margin-top: 0;
     color: #2c3e50;
}

#pressure-display {
    font-size: 1.5em; /* Larger font */
    font-weight: bold;
    margin-bottom: 15px; /* More space */
    color: #e74c3c; /* Default to cautionary color, changes with pressure */
    transition: color 0.5s ease;
}

.slider-container {
    width: 100%;
    position: relative;
    padding-top: 15px; /* Space for labels */
}

#depth-slider {
    width: 100%;
    -webkit-appearance: none; /* Remove default styling */
    appearance: none;
    height: 8px;
    background: #bdc3c7;
    outline: none;
    opacity: 0.9;
    transition: opacity .2s;
    border-radius: 4px;
    cursor: pointer;
}

#depth-slider:hover {
    opacity: 1;
}

#depth-slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    background: #3498db;
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 0 5px rgba(0,0,0,0.2);
    transition: background-color 0.2s ease;
}

#depth-slider::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #3498db;
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 0 5px rgba(0,0,0,0.2);
     transition: background-color 0.2s ease;
}

#slider-min-label, #slider-max-label {
    position: absolute;
    font-size: 0.8em;
    color: #555;
    bottom: -18px;
}

#slider-min-label {
    left: 0;
}

#slider-max-label {
    right: 0;
}


.molecule-model {
    background-color: var(--ui-background);
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    transition: transform 0.3s ease; /* Add slight hover effect */
}

.molecule-model:hover {
     transform: translateY(-5px);
}


.molecule-representation {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100px; /* More vertical space */
    gap: 15px; /* Increased gap */
    margin-top: 15px;
    perspective: 800px; /* Add perspective for 3D transforms */
}

.folding-unit, .membrane-unit {
    width: 40px; /* Larger units */
    height: 40px;
    background-color: var(--molecule-normal-color);
    border: 2px solid #2980b9;
    border-radius: 6px; /* Slightly rounded corners */
    transition: transform 0.6s ease-out, background-color 0.6s ease, border-color 0.6s ease; /* Smoother transitions */
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.9em;
    color: white;
    font-weight: bold;
    position: relative; /* For tooltips */
}

.membrane-unit {
    width: 60px; /* Wider membrane */
    background-color: var(--molecule-membrane-color);
    border-color: #27ae60;
}

/* Tooltip styling (optional but nice) */
.adaptable::before {
    content: attr(data-tooltip);
    position: absolute;
    bottom: 100%;
    left: 50%;
    transform: translateX(-50%);
    background-color: rgba(0, 0, 0, 0.7);
    color: white;
    padding: 5px 10px;
    border-radius: 4px;
    font-size: 0.8em;
    white-space: nowrap;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s ease, visibility 0.3s ease;
    pointer-events: none; /* Do not interfere with click */
    z-index: 1; /* Ensure tooltip is above */
}

.adaptable:hover::before {
    opacity: 1;
    visibility: visible;
}

.molecule-status {
    text-align: center;
    margin-top: 15px;
    font-weight: bold;
    font-size: 1.1em;
    color: var(--status-normal);
    transition: color 0.6s ease;
}

/* States for normal molecule under pressure - GRADUAL EFFECT */
/* Apply transformations based on pressure ratio */

/* Default state */
#normal-molecule .folding-unit {
    transform: translateZ(0) rotateX(0deg) rotateY(0deg) scale(1);
    background-color: var(--molecule-normal-color);
     border-color: #2980b9;
}
#normal-molecule .membrane-unit {
    transform: translateZ(0) scaleY(1);
    background-color: var(--molecule-membrane-color);
     border-color: #27ae60;
}


/* Adaptation explanation area */
#adaptation-explanation {
    flex-basis: 100%;
    background-color: #e0f2f7; /* Lighter blue background */
    padding: 20px;
    border-radius: 8px;
    margin-top: 10px;
    min-height: 80px; /* Ensure minimum height */
    display: flex;
    flex-direction: column;
    justify-content: center; /* Center text vertically */
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);
}

#adaptation-explanation h4 {
    margin-top: 0;
    color: #01579b; /* Darker blue */
    text-align: center;
    margin-bottom: 10px;
}

#explanation-text {
    margin: 0;
    text-align: center;
    font-size: 1.1em;
    color: #333;
}

#explanation-text strong {
    color: #004d40; /* Dark green for emphasis */
}


/* Full explanation section */
button {
    display: block;
    margin: 25px auto;
    padding: 12px 25px;
    font-size: 1.1em;
    cursor: pointer;
    background-color: #0077be; /* Ocean blue */
    color: white;
    border: none;
    border-radius: 6px;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

button:hover {
    background-color: #005f99;
    transform: translateY(-2px);
}
button:active {
     transform: translateY(0);
}


#explanation-content {
    margin-top: 20px;
    padding: 20px;
    border-top: 2px dashed #b0bec5; /* Dotted line separator */
    display: none; /* Initially hidden */
    background-color: #ffffff; /* White background */
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.08);
}

#explanation-content h2, #explanation-content h3 {
    color: #01579b; /* Match h4 in interactive area */
    margin-bottom: 15px;
    padding-bottom: 5px;
    border-bottom: 1px solid #e0f2f7;
}

#explanation-content p, #explanation-content li {
    line-height: 1.7; /* Improved readability */
    color: #333;
    margin-bottom: 15px;
}

#explanation-content ul {
    list-style: disc inside;
    padding-left: 20px;
}

#explanation-content li strong {
    color: #004d40; /* Dark green for key terms */
}

/* Add some subtle animations or effects */
@keyframes pulsate {
    0% { transform: scale(1); opacity: 0.8; }
    50% { transform: scale(1.05); opacity: 1; }
    100% { transform: scale(1); opacity: 0.8; }
}

.pulsate {
    animation: pulsate 1.5s infinite ease-in-out;
}

/* Click feedback for adaptable parts */
.adaptable:active {
    transform: scale(0.95);
}
.adaptable:focus { /* Add focus style for accessibility */
    outline: 2px solid #ffeb3b;
    outline-offset: 2px;
}

</style>

<button id="toggle-explanation">צלול עמוק יותר: גלה את ההסבר המלא</button>

<div id="explanation-content">
    <h2>התמודדות מול לחץ אדיר במעמקי הים: סיפור של התאמה קיצונית</h2>

    <p>הים העמוק, מעבר לגבול האור (מתחת ל-200 מטר), הוא ממלכה של חושך, קור מקפיא – ולחץ הידרוסטטי שאין לו אח ורע על פני האדמה. הלחץ עולה בקצב מדהים: כ-1 אטמוספירה (Atm) על כל 10 מטרים של צלילה. דמיינו את זה: בעומק 1,000 מטר, הלחץ הוא כבר כ-101 Atm; בשקע מריאנה, הנקודה העמוקה ביותר הידועה (כ-11 ק"מ), הלחץ מגיע לכ-1,100 Atm! לחץ כזה מפעיל כוחות אדירים על כל עצם, כולל המולקולות הזעירות המרכיבות את החיים.</p>

    <h3>כוח הלחץ על מנועי החיים: מולקולות ביולוגיות תחת איום</h3>
    <p>לחץ גבוה אינו סתם כוח מכאני; הוא משפיע ישירות על הדינמיקה הכימית של המים ועל המבנה העדין של מולקולות החיים. הוא "דוחף" תהליכים כימיים ופיזיקליים שמקטינים את הנפח הכולל של המערכת. השפעה זו קטלנית במיוחד עבור מבנים ביולוגיים המבוססים על אינטראקציות חלשות, כמו קשרי מימן או כוחות הידרופוביים, שהם בדיוק הכוחות שמקפלים חלבונים ומרכיבים ממברנות:</p>
    <ul>
        <li><strong>חלבונים:</strong> אבני הבניין והמנועים של התא. הקיפול התלת-ממדי המדויק שלהם חיוני לתפקודם כאנזימים, חלבוני מבנה, או נשאים. לחץ גבוה משבש קיפול זה (גורם ל<strong>דנטורציה</strong>), פוגע באתרים הפעילים ומונע אינטראקציות תקינות. חלבון "מקולקל" משמעותו תא שאינו יכול לנשום, לנוע, או לייצר אנרגיה – מוות ודאי.</li>
        <li><strong>ממברנות התא:</strong> הגבול החיצוני של התא והמחיצות הפנימיות שלו, המורכבות בעיקר משכבה כפולה של שומנים. לחץ גבוה "מהדק" את אריזת מולקולות השומן, הופך את הממברנה לנוקשה ופחות נוזלית. נוזליות הממברנה חיונית לתפקודם של חלבונים המשובצים בה – תעלות שמעבירות חומרים, משאבות ששומרות על איזון יונים, וקולטנים שמקבלים אותות. ממברנה נוקשה פוגעת בכל אלה.</li>
        <li><strong>DNA ו-RNA:</strong> פחות רגישים באופן דרמטי מחלבונים וממברנות, אך גם מבנים אלו, המבוססים על סלילים כפולים וקיפולים מורכבים, יכולים להיות מושפעים מלחץ קיצוני מאוד, אם כי השפעה זו פחות קריטית בהשוואה לשני הראשונים בטווח הלחצים שרוב יצורי הים העמוק פוגשים.</li>
    </ul>

    <h3>ארסנל מולקולרי: סודות ההתאמה של אלופי העומק</h3>
    <p>יצורי הים העמוק אינם נכנעים לגורלם; הם פיתחו לאורך מיליוני שנים ארסנל ביוכימי ופיזיולוגי מדהים כדי לשרוד ולשגשג בתנאי לחץ אדירים:</p>
    <ul>
        <li><strong>צבירת אוסמוליטים מגנים (Protective Osmolytes):</strong> זהו אולי המנגנון המפורסם ביותר. יצורים רבים צוברים בתאיהם מולקולות קטנות ומסיסות המכונות אוסמוליטים. לאוסמוליטים מסוימים, ובראשם <strong>Trimethylamine N-oxide (TMAO)</strong>, יש יכולת יוצאת דופן לייצב חלבונים – בדיוק ההפך ממה שהלחץ עושה! ככל שהיצור חי עמוק יותר, כך הוא אוגר יותר TMAO. ה-TMAO למעשה "קשור" מולקולות מים סביב החלבון באופן שמקשה על הלחץ לשבש את מבנהו. עם זאת, ריכוזים גבוהים של TMAO יכולים לפגוע בתהליכים תאיים אחרים. לכן, יצורים אלו לעיתים קרובות מייצרים אוסמוליטים "נגדיים" (<strong>Counter-osmolytes</strong>) כמו קריאטין, המאזנים חלק מההשפעות השליליות של TMAO תוך שמירה על יכולת ההגנה העיקרית שלו מלחץ.</li>
        <li><strong>מבנה חלבונים עמיד ללחץ (Pressure-Resistant Proteins):</strong> אבולוציה פעלה על גנים של חלבונים חיוניים. לחלבונים של יצורי ים עמוק יש לעיתים קרובות שינויים ספורים בהרכב חומצות האמינו או בארגון המבני הפנימי שלהם. שינויים עדינים אלה הופכים את הקיפול שלהם ליציב יותר בפני לחץ, ומבטיחים שהם ימשיכו לתפקד ביעילות גם בתנאי תהום. אנזימים מרכזיים, למשל, עשויים להיות "מכוילים" לעבודה אופטימלית בלחץ גבוה במקום בלחץ אטמוספרי רגיל.</li>
        <li><strong>התאמות מברנליות (Membrane Adaptations):</strong> כדי להתמודד עם התקשחות הממברנה, יצורי ים עמוק משנים את הרכב השומנים שלה. הם מגדילים משמעותית את כמות חומצות השומן ה<strong>בלתי רוויות</strong> (המכילות קשרים כפולים) ומשנים את היחסים בין סוגים שונים של פוספוליפידים. מולקולות אלו יוצרות אריזה פחות צפופה ו"נוזלית" יותר בממברנה, וכך מאזנות את השפעת הלחץ ומאפשרות לחלבונים המשובצים בממברנה להמשיך לתפקד.</li>
    </ul>

    <h3>אלופי השרידה: דוגמאות מהמעמקים</h3>
    <p>דגים ממשפחות כמו Macrouridae (דגי גרזן) הידועים בצלילתם לעומקים של אלפי מטרים, מציגים ריכוזי TMAO מהגבוהים ביותר בטבע. חיידקים וארכאונים החיים סביב מעיינות הידרותרמיים רותחים בעומק הים מתמודדים עם לחץ וטמפרטורה קיצוניים בעזרת אנזימים וממברנות שעמידים לשני האיומים בו זמנית. בנוסף למנגנונים המולקולריים, יצורי ים עמוק רבים נמנעים מבניית שלד גרמי כבד או איברים המכילים גז (כמו שלפוחית ציפה), המועדים למעיכה בלחץ, ובמקום זאת בעלי גוף ג'לטיני וצפוף יותר.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const depthSlider = document.getElementById('depth-slider');
    const pressureDisplay = document.getElementById('pressure-display');
    const depthMarker = document.getElementById('depth-marker');
    const depthIndicator = document.getElementById('depth-indicator');
    const oceanColumn = document.getElementById('ocean-column');
    const normalMolecule = document.getElementById('normal-molecule');
    const normalStatus = document.getElementById('normal-status');
    const deepSeaMolecule = document.getElementById('deep-sea-molecule');
    const adaptationExplanation = document.getElementById('adaptation-explanation');
    const explanationText = document.getElementById('explanation-text');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const fullExplanation = document.getElementById('explanation-content');
    const normalMoleculeUnits = normalMolecule.querySelectorAll('.folding-unit, .membrane-unit');

    // Pressure calculation: 1 Atm increase per 10 meters depth, plus 1 Atm at surface
    // Pressure = 1 + depth / 10
    const calculatePressure = (depth) => {
        return (1 + depth / 10);
    };

    // Thresholds (example values)
    const warningPressure = 50; // Start showing warning signs
    const criticalPressure = 200; // Significant damage
    const maxPressureEffect = 500; // Maximum effect reached beyond this pressure

    const updateSimulation = (depth) => {
        const pressure = calculatePressure(depth);
        pressureDisplay.textContent = `${pressure.toFixed(1)} אטמוספירות`;
        depthIndicator.textContent = `${depth} מטר`;

        // Update marker position (smoothly)
        const maxDepth = parseFloat(depthSlider.max);
        const columnHeight = oceanColumn.clientHeight;
        // Position marker from top (0 depth at top, max depth at bottom)
        const markerTop = (depth / maxDepth) * columnHeight;
        depthMarker.style.top = `${markerTop}px`;
        depthIndicator.style.top = `${markerTop}px`;

        // Update pressure gauge color based on pressure
        let gaugeColor = '#3498db'; // Blue below warning
        if (pressure >= warningPressure && pressure < criticalPressure) {
            gaugeColor = 'var(--status-warning)'; // Orange
        } else if (pressure >= criticalPressure) {
            gaugeColor = 'var(--status-danger)'; // Red
        }
        pressureDisplay.style.color = gaugeColor;


        // --- Simulate normal molecule behavior GRADUALLY based on pressure ---
        let normalStatusText = 'יציבה ותקינה';
        let normalStatusColor = 'var(--status-normal)'; // Green

        // Calculate pressure effect ratio (0 to 1)
        // Effect starts at warningPressure, maxes out at maxPressureEffect
        let pressureEffectRatio = 0;
        if (pressure >= warningPressure) {
            pressureEffectRatio = Math.min(1, (pressure - warningPressure) / (maxPressureEffect - warningPressure));
        }

        normalMoleculeUnits.forEach(unit => {
            // Apply gradual transformations
            let scale = 1 + pressureEffectRatio * (parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--denature-transform-scale')) - 1);
            let rotate = pressureEffectRatio * parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--denature-transform-rotate'));
             let color = `lerpColor('${var(--molecule-normal-color)}', '${var(--denature-color)}', ${pressureEffectRatio})`; // Need a helper for this or do it differently

             if(unit.classList.contains('membrane-unit')) {
                 let scaleY = 1 + pressureEffectRatio * (parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--membrane-transform-scaleY')) - 1);
                 unit.style.transform = `translateZ(0) scaleY(${scaleY})`;
                  unit.style.backgroundColor = `hsl(120, ${100 - pressureEffectRatio*100}%, ${45 + pressureEffectRatio*10}%)`; // Lerp green to redish using HSL
             } else {
                 // Example: units slightly rotate and scale
                 // Use different axis/amount for each unit for varied distortion
                 if(unit.classList.contains('unit-1')) unit.style.transform = `translateZ(0) rotateZ(${rotate}deg) scale(${scale})`;
                 if(unit.classList.contains('unit-2')) unit.style.transform = `translateZ(0) rotateY(${rotate}deg) scale(${scale})`;
                 if(unit.classList.contains('unit-3')) unit.style.transform = `translateZ(0) rotateX(${rotate}deg) scale(${scale})`;
                 if(unit.classList.contains('unit-4')) unit.style.transform = `translateZ(0) rotateZ(${-rotate}deg) scale(${scale})`;

                 // Interpolate color
                 unit.style.backgroundColor = `hsl(200, ${100 - pressureEffectRatio*100}%, ${45 + pressureEffectRatio*10}%)`; // Lerp blue to redish using HSL
             }


        });

         // Update normal molecule status text based on ratio
         if (pressureEffectRatio === 0) {
             normalStatusText = 'יציבה ותקינה';
             normalStatusColor = 'var(--status-normal)';
         } else if (pressureEffectRatio < 0.5) {
              normalStatusText = 'מתחילה לאבד יציבות...';
              normalStatusColor = 'var(--status-warning)';
         } else if (pressureEffectRatio < 1) {
             normalStatusText = 'נאבקת לשמור על צורה!';
             normalStatusColor = 'var(--status-warning)';
         }
          else { // pressureEffectRatio === 1
             normalStatusText = 'פגומה ואינה מתפקדת!';
             normalStatusColor = 'var(--status-danger)';
             normalMolecule.classList.add('pulsate'); // Add pulsate on severe damage
         }
         normalStatus.textContent = normalStatusText;
         normalStatus.style.color = normalStatusColor;

         if (pressureEffectRatio < 1) {
             normalMolecule.classList.remove('pulsate'); // Remove pulsate if recovering
         }


        // Deep-sea molecule (remains stable - no changes based on pressure here)
        // The deep-sea molecule visual is static, its 'adaptation' is why it IS static.
        // Its status text is always stable in this simulation.
        // deepSeaStatus.textContent = 'יציבה ועמידה'; // Static text
        // deepSeaStatus.style.color = 'var(--status-normal)'; // Static color

    };

    // Helper function for linear interpolation of colors (using HSL for simplicity)
     function lerpColor(color1, color2, factor) {
        // Basic HSL interpolation - requires colors in HSL format or conversion
        // For simplicity with predefined CSS vars, using direct HSL calculation in updateSimulation
         return `rgba(${
            Math.round(parseInt(color1.substring(1, 3), 16) * (1 - factor) + parseInt(color2.substring(1, 3), 16) * factor)
        }, ${
            Math.round(parseInt(color1.substring(3, 5), 16) * (1 - factor) + parseInt(color2.substring(3, 5), 16) * factor)
        }, ${
            Math.round(parseInt(color1.substring(5, 7), 16) * (1 - factor) + parseInt(color2.substring(5, 7), 16) * factor)
        }, 1)`; // Simplified RGB interpolation - HSL approach in CSS is better for visual smoothness
    }


    // Initial update
    updateSimulation(parseFloat(depthSlider.value));

    // Event listener for slider
    depthSlider.addEventListener('input', (event) => {
        const depth = parseFloat(event.target.value);
        updateSimulation(depth);
    });

    // Event listener for clicking on adaptable parts
    deepSeaMolecule.querySelectorAll('.adaptable').forEach(part => {
        part.addEventListener('click', () => {
             // Remove glow from previous clicks
             deepSeaMolecule.querySelectorAll('.adaptable').forEach(p => p.style.boxShadow = '');

            const mechanism = part.dataset.mechanism;
            let text = 'לחץ על חלק במולקולת הים העמוק כדי לגלות את סוד ההישרדות שלה.';
            let partColor = getComputedStyle(part).backgroundColor; // Get current background color for glow

            switch (mechanism) {
                case 'osmolytes':
                    text = '<strong>אוסמוליטים (כמו TMAO):</strong> מולקולות קטנות שמצטברות בתאים. הן "מייצבות" חלבונים ומונעות מהלחץ לשבש את הקיפול והתפקוד שלהם.';
                     partColor = '#ff9800'; // Orange glow
                    break;
                case 'protein-structure':
                    text = '<strong>מבנה חלבון מותאם:</strong> שינויים עדינים במבנה החלבון עצמו הופכים אותו עמיד יותר בפני הלחץ, ומאפשרים לו לתפקד כרגיל בעומק.';
                     partColor = '#4caf50'; // Green glow
                    break;
                case 'membrane-lipids':
                    text = '<strong>הרכב ליפידים מותאם בממברנה:</strong> הוספת חומצות שומן בלתי רוויות לממברנה "מאזנת" את ההשפעה המקשיחה של הלחץ ושומרת על נוזליות חיונית לתפקוד.';
                    partColor = '#2196f3'; // Blue glow
                    break;
                default:
                     text = 'מידע על מנגנון ההתאמה הספציפי.'; // Fallback
            }
            adaptationExplanation.innerHTML = `<h4>מנגנון התאמה:</h4><p id="explanation-text">${text}</p>`;

            // Add glow effect to the clicked part
            part.style.boxShadow = `0 0 15px 5px ${partColor}`;
        });
    });

     // Toggle full explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = fullExplanation.style.display === 'none' || fullExplanation.style.display === '';
        fullExplanation.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'סגור הסבר מפורט' : 'צלול עמוק יותר: גלה את ההסבר המלא';

         // Scroll to the explanation section if showing it
         if (!isHidden) {
             fullExplanation.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });

     // Initially hide the full explanation
     fullExplanation.style.display = 'none';
});
</script>
```