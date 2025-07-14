---
title: "מעבדת הגידול ההידרופוני: לשלוט במים, להחיות צמחים"
english_slug: hydroponics-simulator-nutrient-ph-control-enhanced
category: "מדעי החיים / ביולוגיה"
tags: ["הידרופוניקה", "גידול צמחים", "pH", "EC", "תזונת צמחים", "סימולציה", "חינוך מדעי", "חקלאות ללא אדמה"]
---
<h1>מעבדת הגידול ההידרופוני: לשלוט במים, להחיות צמחים</h1>
<p>צמחים לא זקוקים לאדמה כדי לשגשג. כל מה שהם צריכים נמצא במים... אבל רק אם התנאים שם מושלמים! בסימולטור הזה, אתם האגרונומים הראשיים. המשימה שלכם: למצוא את האיזון המדויק של דשן (EC) וחומציות (pH) כדי להפוך שתיל צעיר לצמח שופע ובריא. שחקו עם המחוונים וראו כיצד כל שינוי קטן משפיע ישירות על בריאותו וחיוניותו של הצמח שלכם!</p>

<div class="hydro-lab-container">
    <div class="plant-display-area">
        <div class="water-tank"></div>
        <div class="plant-container">
             <!-- Plant visualization elements go here -->
            <div class="plant-stem"></div>
            <div class="plant-leaf plant-leaf-left"></div>
            <div class="plant-leaf plant-leaf-right"></div>
            <div class="plant-roots"></div>
        </div>
         <div class="plant-feedback"></div>
    </div>

    <div class="controls-panel">
        <h2>פאנל בקרה</h2>
        <div class="control-group">
            <label for="ec-slider">רמת דשן (EC - מוליכות חשמלית): <span class="control-value" id="ec-value">0.18 S/m</span></label>
            <input type="range" id="ec-slider" min="0.05" max="0.35" step="0.01" value="0.18">
            <div class="optimal-range" style="left: calc((0.16 - 0.05) / (0.35 - 0.05) * 100%); width: calc((0.20 - 0.16) / (0.35 - 0.05) * 100%);"></div>
        </div>
        <div class="control-group">
            <label for="ph-slider">רמת חומציות (pH): <span class="control-value" id="ph-value">6.0</span></label>
            <input type="range" id="ph-slider" min="4.0" max="8.0" step="0.1" value="6.0">
             <div class="optimal-range" style="left: calc((5.5 - 4.0) / (8.0 - 4.0) * 100%); width: calc((6.5 - 5.5) / (8.0 - 4.0) * 100%);"></div>
        </div>
         <div class="control-tips">
            <p><b>טיפ:</b> חפשו את "הטווח הירוק" על המחוונים לאזור האיזון!</p>
        </div>
    </div>
</div>

<button id="toggle-explanation" class="explanation-button">הצג/הסתר מדע ההידרופוניקה</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2>מדע ההידרופוניקה: צלילה לעומק</h2>

    <h3>הידרופוניקה 101: לגדל בלי אדמה</h3>
    <p>דמיינו עולם שבו אוכל טרי גדל לאורך כל השנה, בכל מקום, עם 90% פחות מים. זהו עולם ההידרופוניקה. במקום אדמה, השורשים מקבלים את כל מה שהם צריכים מתמיסת מים מועשרת בנוטריינטים. זה מאפשר שליטה חסרת תקדים על תנאי הגידול, קצב גדילה מהיר יותר, וצמצום מזיקים ומחלות שבאות מהקרקע.</p>
    <p><b>יתרונות מרכזיים:</b> חיסכון עצום במים, גידול בצפיפות גבוהה, פחות מזיקים/מחלות, גדילה מהירה יותר, אפשרות גידול במדבריות/ערים, שליטה אופטימלית. <b>אתגרים:</b> עלות הקמה, דורש ידע וניטור קפדניים, תלות באנרגיה.</p>

    <h3>תפריט הצמח ההידרופוני: נוטריינטים חיוניים</h3>
    <p>בדיוק כמונו, צמחים זקוקים לתזונה מאוזנת. הם קולטים מינרלים מומסים במים, המחולקים למקרו ומיקרו נוטריינטים:</p>
    <ul>
        <li><b>מקרו:</b> חנקן (N), זרחן (P), אשלגן (K), סידן (Ca), מגנזיום (Mg), גופרית (S) - ה"פחמימות והחלבונים" של הצמח, נדרשים בכמויות גדולות.</li>
        <li><b>מיקרו:</b> ברזל (Fe), מנגן (Mn), אבץ (Zn), נחושת (Cu), בורון (B), מוליבדן (Mo), כלור (Cl) - ה"ויטמינים והמינרלים", נדרשים בכמויות קטנות אך קריטיים לבריאות ותפקוד.</li>
    </ul>
    <p>במערכת הידרופונית, אנחנו אחראים לספק את כל אלו בתמיסת ההזנה.</p>

    <h3>EC: כמה "מזון" יש במים?</h3>
    <p>EC (מוליכות חשמלית) הוא בעצם "מד הדשן" שלנו. הוא מודד כמה מלחים (נוטריינטים מומסים) יש במים. ככל שיש יותר מלחים, המוליכות עולה.</p>
    <ul>
        <li><b>EC נמוך מדי:</b> הצמח "רעב". אין מספיק נוטריינטים זמינים לקליטה. נראה גדילה איטית, עלווה חיוורת, סימני מחסור ספציפיים (תלוי בנוטריינט החסר).</li>
        <li><b>EC גבוה מדי:</b> "מנת יתר" של דשן. ריכוז המלחים הגבוה יוצר לחץ אוסמוטי הפוך - במקום שהשורשים יקלטו מים ונוטריינטים, הם עלולים לאבד מים! התוצאה: "צריבת דשן" בקצות העלים, נבילה, ואפילו מוות.</li>
        <li><b>טווח אופטימלי:</b> משתנה לפי סוג הצמח ושלב הגידול, אך תמיד יש טווח מדויק בו הצמח יקלוט את הנוטריינטים בצורה הטובה ביותר. הסימולטור משתמש בטווח גנרי לדוגמה.</li>
    </ul>

    <h3>pH: המפתח ל"נעילת" הנוטריינטים</h3>
    <p>pH מודד את חומציות המים. זה אולי הפרמטר הכי קריטי! למה? כי pH משפיע ישירות על <b>זמינות</b> הנוטריינטים לשורשים. גם אם ה-EC מושלם (יש מספיק נוטריינטים), אם ה-pH לא בטווח הנכון, השורשים פשוט לא יוכלו לקלוט אותם. תופעה זו נקראת "נעילת נוטריינטים" (Nutrient Lockout).</p>
    <ul>
        <li><b>pH גבוה מדי (בסיסי):</b> במים בסיסיים (מעל 6.5), מיקרו-נוטריינטים כמו ברזל, מנגן, אבץ ונחושת "ננעלים" והופכים לבלתי זמינים. נראה סימני מחסור, במיוחד הצהבה בין עורקי העלים (Chlorosis), למרות שהם קיימים במים.</li>
        <li><b>pH נמוך מדי (חומצי):</b> במים חומציים (מתחת ל-5.5), זמינות של זרחן, סידן ומגנזיום יורדת. בנוסף, יסודות מסוימים (ברזל, מנגן, אלומיניום) הופכים זמינים *מדי* ועלולים לגרום לרעילות בצמח.</li>
        <li><b>טווח אופטימלי:</b> רוב הצמחים ההידרופוניים מעדיפים טווח מעט חומצי: 5.5 עד 6.5. בטווח זה, רוב הנוטריינטים זמינים לקליטה בקלות.</li>
    </ul>

    <h3>סינרגיה קריטית: EC ו-pH עובדים יחד</h3>
    <p>הסימולטור מראה בצורה חיה את הקשר ההדוק: גם EC וגם pH חייבים להיות בטווח האופטימלי כדי שהצמח ישגשג. EC תקין עם pH לא נכון = רעב. pH תקין עם EC נמוך = רעב. pH תקין עם EC גבוה = רעילות. רק שניהם יחד, בטווח הנכון, יאפשרו קליטת נוטריינטים אופטימלית וגדילה בריאה.</p>
    <p>ההצלחה בהידרופוניקה טמונה ביכולת לנטר ולהתאים את שני הפרמטרים הללו בקביעות. הצמח הוא המדריך הטוב ביותר - שימו לב לסימנים שהוא שולח!</p>
</div>

<style>
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f4f7f6;
    margin: 0;
    padding: 20px;
    direction: rtl;
    text-align: right;
}

h1, h2, h3 {
    color: #2c3e50;
    text-align: center;
    margin-bottom: 15px;
}

h1 {
    font-size: 2em;
    border-bottom: 2px solid #3498db;
    padding-bottom: 10px;
    margin-bottom: 20px;
}

h2 {
    font-size: 1.5em;
    color: #3498db;
}

h3 {
     font-size: 1.2em;
     color: #555;
     margin-top: 20px;
     border-bottom: 1px dotted #ccc;
     padding-bottom: 5px;
}

p {
    margin-bottom: 15px;
}

ul {
    margin-bottom: 15px;
    padding-right: 20px;
}

li {
    margin-bottom: 8px;
}

.hydro-lab-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px auto;
    padding: 25px;
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    max-width: 600px;
}

.plant-display-area {
    position: relative;
    width: 100%;
    max-width: 300px; /* Keep plant area focused */
    height: 350px; /* Increased height for visual */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-end; /* Align plant/water at the bottom */
    margin-bottom: 30px;
    overflow: hidden; /* Ensure elements stay within bounds */
}

.water-tank {
    position: absolute;
    bottom: 0;
    left: 10%;
    right: 10%;
    height: 80px; /* Water level */
    background: linear-gradient(to bottom, #3498db, #2980b9); /* Blue gradient for water */
    border-radius: 10px 10px 0 0;
    opacity: 0.9;
}


.plant-container {
    position: relative;
    width: 80px; /* Width of the base */
    height: 250px; /* Total height */
    display: flex;
    flex-direction: column;
    align-items: center;
    z-index: 1; /* Ensure plant is above water */
    bottom: 70px; /* Position above water */
}

/* Plant Elements - using CSS shapes */
.plant-stem {
    width: 15px;
    height: 150px; /* Stem height */
    background-color: #27ae60; /* Green stem color */
    border-radius: 5px;
    position: absolute;
    bottom: 100px; /* Position above roots/water */
    transition: background-color 0.5s ease, height 0.5s ease;
}

.plant-leaf {
    width: 60px;
    height: 100px;
    background-color: #2ecc71; /* Leaf color */
    border-radius: 0 50% 0 50%; /* Leaf shape */
    position: absolute;
    bottom: 190px; /* Position higher */
    transform-origin: bottom center;
    transition: background-color 0.5s ease, transform 0.5s ease;
}

.plant-leaf-left {
    left: -20px;
    transform: rotate(-35deg);
}

.plant-leaf-right {
    right: -20px;
    transform: rotate(35deg);
}

.plant-roots {
    width: 60px;
    height: 120px; /* Roots extending into water */
    background-color: rgba(200, 180, 160, 0.7); /* Root color (semi-transparent) */
    position: absolute;
    bottom: 0; /* Extend from the base */
    border-radius: 0 0 10px 10px;
    transition: background-color 0.5s ease, height 0.5s ease;
}


/* Plant States - colors and transforms for different conditions */
.plant-container.healthy .plant-stem,
.plant-container.healthy .plant-leaf { background-color: #2ecc71; }
.plant-container.healthy .plant-roots { background-color: rgba(200, 180, 160, 0.7); height: 120px;}
.plant-container.healthy .plant-stem { height: 150px; }
.plant-container.healthy .plant-leaf-left { transform: rotate(-35deg); }
.plant-container.healthy .plant-leaf-right { transform: rotate(35deg); }


.plant-container.low-ec .plant-stem,
.plant-container.low-ec .plant-leaf { background-color: #f1c40f; } /* Yellowish */
.plant-container.low-ec .plant-roots { background-color: rgba(200, 180, 160, 0.5); }
.plant-container.low-ec .plant-stem { height: 130px; } /* Slightly shorter */
.plant-container.low-ec .plant-leaf { transform: scale(0.9); } /* Smaller leaves */


.plant-container.high-ec .plant-stem { background-color: #e74c3c; } /* Reddish stem */
.plant-container.high-ec .plant-leaf {
    background-color: #e67e22; /* Orange/Brownish leaves */
    box-shadow: 0 0 5px 2px rgba(140, 70, 20, 0.5); /* "Burn" effect */
}
.plant-container.high-ec .plant-roots { background-color: rgba(160, 100, 80, 0.8); height: 80px;} /* Shrunken roots */
.plant-container.high-ec .plant-stem { height: 140px; } /* Stunted stem */
.plant-container.high-ec .plant-leaf-left { transform: rotate(-45deg); }
.plant-container.high-ec .plant-leaf-right { transform: rotate(45deg); }


.plant-container.high-ph .plant-stem,
.plant-container.high-ph .plant-leaf { background-color: #f39c12; } /* Amber/Orange - iron deficiency */
.plant-container.high-ph .plant-roots { background-color: rgba(200, 180, 160, 0.6); }
.plant-container.high-ph .plant-leaf { transform: scale(0.95); } /* Slightly smaller */


.plant-container.low-ph .plant-stem,
.plant-container.low-ph .plant-leaf { background-color: #bdc3c7; } /* Greyish/Pale - general stress/toxicity */
.plant-container.low-ph .plant-roots { background-color: rgba(120, 80, 60, 0.8); height: 100px; } /* Darker, shorter roots */
.plant-container.low-ph .plant-leaf { transform: rotate(0deg); top: 200px;} /* Drooping leaves */
.plant-container.low-ph .plant-stem { height: 130px; }


.plant-container.severe-stress .plant-stem { background-color: #c0392b; } /* Dark Red */
.plant-container.severe-stress .plant-leaf {
    background-color: #7f8c8d; /* Grey/Dead color */
    transform: scale(0.8) rotate(0deg); /* Shrunken, droopy */
    top: 210px;
}
.plant-container.severe-stress .plant-roots { background-color: rgba(50, 30, 20, 0.9); height: 60px; } /* Very shrunken, dark */
.plant-container.severe-stress .plant-stem { height: 100px; } /* Severely stunted */


.plant-feedback {
    text-align: center;
    min-height: 40px; /* Reserve space */
    font-weight: bold;
    color: #e74c3c; /* Default alert color */
    margin-top: 10px;
    font-size: 1.1em;
}

.plant-container.healthy + .plant-feedback {
     color: #27ae60; /* Green for healthy feedback */
}


.controls-panel {
    width: 100%;
    max-width: 450px;
}

.controls-panel h2 {
    text-align: center;
    color: #2c3e50;
    margin-bottom: 20px;
}

.control-group {
    margin-bottom: 25px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    background-color: #ecf0f1;
    padding: 15px;
    border-radius: 8px;
    border: 1px solid #bdc3c7;
}

.control-group label {
    margin-bottom: 8px;
    font-weight: bold;
    color: #34495e;
    display: flex;
    justify-content: space-between;
    width: 100%;
}

.control-value {
    font-weight: normal;
    color: #555;
}

.control-group input[type="range"] {
    width: 100%;
    margin-bottom: 5px;
    -webkit-appearance: none; /* Override default CSS styles */
    appearance: none;
    height: 8px;
    background: #dcdcdc;
    outline: none;
    opacity: 0.7;
    transition: opacity .2s;
    border-radius: 5px;
    position: relative;
    z-index: 0; /* Ensure optimal range sits above */
}

.control-group input[type="range"]:hover {
  opacity: 1;
}

.control-group input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    background: #3498db;
    cursor: pointer;
    border-radius: 50%;
    border: 2px solid #ffffff;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}

.control-group input[type="range"]::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #3498db;
    cursor: pointer;
    border-radius: 50%;
    border: 2px solid #ffffff;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}

.control-group .optimal-range {
    position: absolute;
    height: 8px;
    background-color: #2ecc71; /* Green for optimal */
    border-radius: 5px;
    z-index: 1; /* Sit below thumb, above track */
    pointer-events: none; /* Don't interfere with slider */
    transform: translateY(-8px); /* Position directly on the track */
}

.control-tips {
    text-align: center;
    margin-top: 10px;
    font-size: 0.9em;
    color: #555;
}

.explanation-button {
    display: block;
    margin: 30px auto;
    padding: 12px 20px;
    font-size: 1.1em;
    cursor: pointer;
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 6px;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.explanation-button:hover {
    background-color: #2980b9;
    transform: translateY(-1px);
}

.explanation-button:active {
    background-color: #1f628d;
    transform: translateY(0);
}

.explanation-section {
    margin-top: 20px;
    padding: 25px;
    border: 1px solid #bdc3c7;
    border-radius: 12px;
    background-color: #ecf0f1;
    direction: rtl;
    text-align: right;
    line-height: 1.7;
}

.explanation-section h2, .explanation-section h3 {
    color: #2c3e50;
}

.explanation-section ul {
    list-style: disc;
    padding-right: 20px;
}

.explanation-section li {
    margin-bottom: 10px;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const ecSlider = document.getElementById('ec-slider');
    const phSlider = document.getElementById('ph-slider');
    const ecValueSpan = document.getElementById('ec-value');
    const phValueSpan = document.getElementById('ph-value');
    const plantContainer = document.querySelector('.plant-container'); // Target the container for state classes
    const plantFeedback = document.querySelector('.plant-feedback');
    const toggleButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // Optimal ranges based on the explanation text
    const optimalEC_low = 0.16; // S/m (Mapping example 0.8-1.2 mS/cm to 0.16-0.20 S/m is rough for demo)
    const optimalEC_high = 0.20; // S/m
    const optimalPH_low = 5.5;
    const optimalPH_high = 6.5;

    function updatePlantState() {
        const ec = parseFloat(ecSlider.value);
        const ph = parseFloat(phSlider.value);

        ecValueSpan.textContent = `${ec.toFixed(2)} S/m`;
        phValueSpan.textContent = ph.toFixed(1);

        let state = 'healthy';
        let feedback = 'הצמח משגשג - תנאים מושלמים!';

        // Remove all previous state classes
        plantContainer.className = 'plant-container';

        // Determine current state based on ranges
        const isEC_low = ec < optimalEC_low;
        const isEC_high = ec > optimalEC_high;
        const isPH_low = ph < optimalPH_low;
        const isPH_high = ph > optimalPH_high;
        const isPH_optimal = ph >= optimalPH_low && ph <= optimalPH_high;
        const isEC_optimal = ec >= optimalEC_low && ec <= optimalEC_high;

        // Check for severe stress (extreme values)
         if (ph < 4.5 || ph > 7.0 || ec < 0.08 || ec > 0.28) {
             state = 'severe-stress';
             feedback = 'מצב קריטי! התנאים קיצוניים מדי, הצמח עלול למות.';
        }
        // Check for specific issues, prioritizing pH issues if EC is also off but not extreme
        else if (isPH_high && !isEC_optimal) { // High pH is a strong blocker
            state = 'high-ph';
            feedback = 'pH גבוה מדי! נוטריינטים ננעלים, הצמח לא יכול לאכול.';
        } else if (isPH_low && !isEC_optimal) { // Low pH causes toxicity/lockout
            state = 'low-ph';
            feedback = 'pH נמוך מדי! בעיות קליטה וחשש לרעילות נוטריינטים.';
        }
        // If pH is optimal or just slightly off, check EC
        else if (isEC_low && isPH_optimal) {
             state = 'low-ec';
             feedback = 'מחסור בנוטריינטים! הצמח רעב, העלווה מצהיבה.';
        } else if (isEC_high && isPH_optimal) {
            state = 'high-ec';
            feedback = 'עודף נוטריינטים! חשש לצריבה ורעילות.';
        }
        // Handle cases where BOTH are slightly off but not extreme enough for 'severe'
        else if (isEC_low) { // pH might be slightly high/low, but EC is main issue
             state = 'low-ec'; // Could potentially refine this state combining issues
             feedback = 'EC נמוך (מחסור) וגם ה-pH לא מושלם... כדאי להתמקד באיזון.';
        } else if (isEC_high) { // pH might be slightly high/low
            state = 'high-ec'; // Could potentially refine this state
            feedback = 'EC גבוה (עודף) וגם ה-pH לא מושלם... סכנה לצמח!';
        } else if (isPH_high) { // EC is okay, but pH is the issue
             state = 'high-ph';
             feedback = 'pH גבוה מדי! הנוטריינטים קיימים אך לא זמינים.';
        } else if (isPH_low) { // EC is okay, but pH is the issue
            state = 'low-ph';
            feedback = 'pH נמוך מדי! כדאי להעלות אותו לאזור הבטוח.';
        }
        // If none of the specific stress conditions match the thresholds, assume optimal within a small margin
        // The initial 'healthy' state handles the perfect range.


        // Apply the determined state class
        plantContainer.classList.add(state);
        plantFeedback.textContent = feedback;
    }

    // Initial state update
    updatePlantState();

    // Add event listeners to sliders
    ecSlider.addEventListener('input', updatePlantState);
    phSlider.addEventListener('input', updatePlantState);

    // Add event listener to toggle button
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר מדע ההידרופוניקה' : 'הצג/הסתר מדע ההידרופוניקה';
    });
});
</script>