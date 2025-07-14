---
title: "מנהלים משבר כלכלי: סימולטור המדיניות הלאומית"
english_slug: managing-national-economic-crisis-interactive-simulator
category: "כלכלה"
tags: [כלכלה, משבר כלכלי, סימולציה, אינפלציה, אבטלה, מדיניות מקרו כלכלית, משחק כלכלי]
---
# מנהלים משבר כלכלי: סימולטור המדיניות הלאומית

אתם ראש הממשלה ונגידת בנק ישראל! האם תצליחו לנווט את ספינת הכלכלה הלאומית במים סוערים של משבר? לרוב, מדיניות שמורידה אבטלה מעלה אינפלציה, ולהיפך. איך מאזנים בין שני אתגרים קריטיים אלה, ומה קורה לצמיחה הכלכלית? צללו פנימה, קבלו החלטות - וראו את ההשלכות!

<div class="simulator-container">
    <div class="graphs-area">
        <h2>מדדים כלכליים מרכזיים</h2>
        <div class="graph-wrapper">
            <canvas id="inflationChart"></canvas>
        </div>
        <div class="graph-wrapper">
            <canvas id="unemploymentChart"></canvas>
        </div>
         <div class="graph-wrapper">
            <canvas id="gdpChart"></canvas>
        </div>
    </div>
    <div class="controls-area">
        <h2>מנופי מדיניות (לשנה הבאה)</h2>
        <p class="controls-intro">קבעו את השינויים במדיניות הכלכלית עבור **השנה הבאה**, ולחצו "קדם שנה" לראות את ההשפעה.</p>
        <div class="current-status">
            <h3><i class="icon-status"></i> מצב נוכחי: <span id="currentYear">--</span></h3>
            <p>אינפלציה: <span id="currentInflation" class="status-value">--</span>% <span class="status-indicator"></span></p>
            <p>אבטלה: <span id="currentUnemployment" class="status-value">--</span>% <span class="status-indicator"></span></p>
            <p>צמיחת תוצר: <span id="currentGdpGrowth" class="status-value">--</span>% <span class="status-indicator"></span></p>
        </div>

        <div class="policy-lever">
            <label for="interestRate">שינוי ריבית בנק מרכזי:</label>
            <input type="range" id="interestRate" min="-3" max="3" value="0" step="0.1">
            <span id="interestRateValue" class="lever-value">0.0%</span>
        </div>
        <div class="policy-lever">
            <label for="govSpending">שינוי בהוצאה ממשלתית (% מהתוצר):</label>
            <input type="range" id="govSpending" min="-5" max="5" value="0" step="0.5">
            <span id="govSpendingValue" class="lever-value">0.0%</span>
        </div>
        <div class="policy-lever">
            <label for="taxRate">שינוי בשיעור המיסוי (נקודות אחוז):</label>
            <input type="range" id="taxRate" min="-5" max="5" value="0" step="0.5">
            <span id="taxRateValue" class="lever-value">0.0 נק'</span>
        </div>
         <div class="policy-lever feedback-area" id="feedbackArea">
             <p class="feedback-message"></p>
         </div>


        <button id="simulateBtn" class="btn btn-primary">קדם שנה <i class="icon-play"></i></button>
        <button id="resetBtn" class="btn btn-secondary">אפס סימולציה <i class="icon-reset"></i></button>
    </div>
</div>

<button id="toggleExplanation" class="toggle-button">הסבר: מאחורי הקלעים של הכלכלה <i class="icon-info"></i></button>

<div id="explanation" class="explanation-area" style="display: none;">
    <h2>הסבר: ניהול משבר כלכלי לאומי</h2>
    <p>ניהול כלכלה לאומית, במיוחד בזמן משבר, הוא משימה מורכבת הדורשת הבנה עמוקה של הכוחות הכלכליים הפועלים והאיזונים העדינים בין יעדים שונים. הסימולטור מציג מודל פשטני של הכלכלה, המדגיש את הקשרים המרכזיים בין מדיניות מוניטרית ופיסקלית לבין מדדי אינפלציה, אבטלה וצמיחה.</p>

    <h3>מהו משבר כלכלי לאומי ומהם מאפייניו העיקריים?</h3>
    <p>משבר כלכלי לאומי מתאפיין בדרך כלל בירידה חדה ומתמשכת בפעילות הכלכלית (מיתון), עלייה באבטלה, ירידה בהכנסות המדינה ממיסים, ולעיתים קרובות גם במשבר פיננסי נלווה (קריסת בנקים, בורסות). משברים יכולים להיגרם מגוון סיבות פנימיות (כמו בועות נדל"ן, חוב ציבורי גבוה) או חיצוניות (כמו משבר נפט, מגיפה עולמית, משבר פיננסי גלובלי).</p>

    <h3>אינפלציה: מהי, מהם גורמיה, ומה השפעתה על הכלכלה?</h3>
    <p>אינפלציה היא עלייה מתמשכת ברמת המחירים הכללית של סחורות ושירותים. היא נגרמת בדרך כלל מעודף ביקוש לעומת היצע (אינפלציית ביקוש) או מעלייה בעלויות הייצור (אינפלציית היצע). אינפלציה גבוהה שוחקת את כוח הקנייה של הכסף, פוגעת בחוסכים, מעלה אי-ודאות עסקית, ומקשה על תכנון כלכלי ארוך טווח.</p>

    <h3>אבטלה: מהי, מהם סוגיה, ומה השפעתה על הכלכלה והחברה?</h3>
    <p>אבטלה מתרחשת כאשר אנשים המחפשים עבודה באופן פעיל אינם מוצאים אותה. ישנם סוגים שונים של אבטלה: אבטלה חיכוך (מעבר בין עבודות), אבטלה מבנית (חוסר התאמה בין כישורים לצרכי השוק), ואבטלה מחזורית (קשורה למחזורי העסקים, עולה במיתון). אבטלה גבוהה גורמת לסבל אנושי, אובדן תוצר פוטנציאלי למשק, ירידה בהכנסות המדינה, ועלייה בהוצאות על קצבאות.</p>

    <h3>הקשר בין אינפלציה לאבטלה: עקומת פיליפס והפשרות</h3>
    <p>עקומת פיליפס המקורית הראתה יחס הפוך בין אינפלציה לאבטלה בטווח הקצר: כשהכלכלה מתחממת (אבטלה נמוכה), לחצי המחירים עולים (אינפלציה עולה), ולהיפך. קשר זה מציג דילמה מרכזית למקבלי ההחלטות: מדיניות שמטרתה הורדת אבטלה (למשל, הגדלת הוצאה ממשלתית) עלולה להוביל לעליית אינפלציה, ומדיניות שמטרתה הורדת אינפלציה (למשל, העלאת ריבית) עלולה להעלות אבטלה. בטווח הארוך, מקובל לחשוב שאין פשרה קבועה בין אינפלציה לאבטלה, ושיש שיעור אבטלה טבעי התואם אינפלציה יציבה.</p>

    <h3>כלי מדיניות מוניטרית והשפעתם</h3>
    <p>כלי מדיניות מוניטרית מופעלים על ידי הבנק המרכזי ומשפיעים בעיקר על כמות הכסף ועל הריבית במשק. הכלי המרכזי הוא הריבית המרכזית:
    <ul>
        <li><b>העלאת ריבית:</b> מייקרת הלוואות ומעודדת חיסכון, מקטינה ביקוש, מורידה אינפלציה ומאטה צמיחה. עלולה להעלות אבטלה.</li>
        <li><b>הורדת ריבית:</b> מוזילה הלוואות ומקטינה חיסכון, מגדילה ביקוש, מעודדת צמיחה וורידה אבטלה. עלולה להעלות אינפלציה.</li>
    </ul>
    כלים נוספים כוללים רכישה/מכירה של אגרות חוב בשוק הפתוח (Quantitative Easing/Tightening) המשפיעים על נזילות וריביות ארוכות טווח.</p>

    <h3>כלי מדיניות פיסקלית והשפעתם</h3>
    <p>כלי מדיניות פיסקלית מופעלים על ידי הממשלה וקשורים לתקציב המדינה (הוצאות והכנסות). כלים מרכזיים:
    <ul>
        <li><b>הגדלת הוצאה ממשלתית:</b> הממשלה מזרימה כסף למשק דרך פרויקטים, שכר וקצבאות. מגדילה ישירות את הביקוש, מורידה אבטלה ומעודדת צמיחה. עלולה להעלות אינפלציה ולהגדיל את הגירעון והחוב הציבורי.</li>
        <li><b>הורדת מיסים:</b> מגדילה את ההכנסה הפנויה של הציבור והרווחים של עסקים. מעודדת צריכה והשקעה, מורידה אבטלה ומעלה צמיחה. עלולה להעלות אינפלציה ולהגדיל את הגירעון והחוב.</li>
        <li><b>קיצוץ הוצאה ממשלתית / העלאת מיסים:</b> בעלות השפעה הפוכה – מורידות ביקוש, מאטות צמיחה, עלולות להעלות אבטלה, אך מסייעות בהורדת אינפלציה וצמצום גירעון וחוב.</li>
    </ul></p>

    <h3>האתגרים בניהול משבר כלכלי (במודל זה ומחוצה לו)</h3>
    <p>ניהול משבר מציב קשיים רבים:
    <ul>
        <li><b>השהיות (Lags):</b> להחלטות כלכליות לוקח זמן להשפיע על הכלכלה. הסימולטור מציג זאת באמצעות השפעה שנפרשת על פני מספר שנים.</li>
        <li><b>ציפיות:</b> החלטות השחקנים הכלכליים מושפעות מציפיותיהם לעתיד, דבר שמודלים פשוטים לרוב אינם מביאים בחשבון במלואו.</li>
        <li><b>זעזועים חיצוניים:</b> אירועים בלתי צפויים בעולם יכולים לשבש את התחזיות ולהשפיע על הכלכלה (בסימולטור זה יש אלמנט אקראי קטן המייצג זאת).</li>
        <li><b>סיכון הסטגפלציה:</b> מצב נדיר בו קיימים בו-זמנית אינפלציה גבוהה ואבטלה גבוהה, אתגר קשה במיוחד למדיניות.</li>
    </ul></p>

    <h3>דוגמאות היסטוריות</h3>
    <p>היסטוריית הכלכלה מלאה בדוגמאות למשברים וניסיונות לנהל אותם, כמו השפל הגדול בשנות ה-30, משבר הנפט בשנות ה-70 (שגרם לסטגפלציה), המשבר הפיננסי העולמי ב-2008, ומשבר הקורונה ב-2020. מכל משבר נלמדים לקחים על יעילותם של כלי מדיניות שונים ועל חשיבות תגובה מהירה אך מחושבת.</p>
</div>

<style>
    /* General Enhancements */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6;
        margin: 0;
        padding: 20px;
    }

    h1, h2, h3 {
        color: #0a3d62; /* Deep blue */
    }

    h1 {
        text-align: center;
        margin-bottom: 30px;
        font-size: 2em;
    }

    .simulator-container {
        display: flex;
        flex-wrap: wrap;
        gap: 30px; /* Increased gap */
        margin-bottom: 30px;
        padding: 30px; /* Increased padding */
        border: 1px solid #dcdcdc; /* Lighter border */
        border-radius: 12px; /* More rounded corners */
        background-color: #ffffff; /* White background for main container */
        box-shadow: 0 4px 12px rgba(0,0,0,0.08); /* Softer shadow */
    }

    .graphs-area {
        flex: 3; /* Give more space to graphs */
        min-width: 320px; /* Ensure minimum width */
    }

    .graph-wrapper {
        margin-bottom: 20px; /* Increased margin */
        background-color: #ffffff;
        padding: 15px; /* Increased padding */
        border-radius: 8px; /* Rounded corners for graph containers */
        box-shadow: 0 2px 6px rgba(0,0,0,0.05); /* Subtle shadow */
        border: 1px solid #eee;
    }

    .controls-area {
        flex: 1;
        min-width: 280px; /* Ensure minimum width */
        display: flex;
        flex-direction: column;
        gap: 20px; /* Increased gap */
        padding: 25px; /* Increased padding */
        background-color: #e8f5e9; /* Light green background */
        border-radius: 12px;
        box-shadow: inset 0 0 8px rgba(0,0,0,0.1); /* Subtle inner shadow */
    }

    .controls-intro {
        font-size: 0.9em;
        color: #555;
        margin-top: -10px;
        margin-bottom: 15px;
    }

    .current-status {
        border: 2px dashed #4caf50; /* Green dashed border */
        padding: 15px;
        border-radius: 8px;
        background-color: #ffffff;
        box-shadow: 0 1px 4px rgba(0,0,0,0.05);
        font-size: 1.1em;
    }

    .current-status h3 {
         margin-top: 0;
         margin-bottom: 10px;
         color: #333;
         display: flex;
         align-items: center;
    }

    .icon-status {
         /* Example icon, replace with actual font icon or SVG */
         display: inline-block;
         width: 1em;
         height: 1em;
         background-color: #4caf50;
         border-radius: 50%;
         margin-left: 8px;
         /* Add actual icon graphic if needed */
    }

    .current-status p {
        margin: 8px 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .status-value {
        font-weight: bold;
        color: #0a3d62; /* Deep blue */
        flex-grow: 1; /* Allow value span to take space */
        text-align: left; /* Align value to the left */
        margin-right: 10px; /* Space before indicator */
    }

    .status-indicator {
        display: inline-block;
        width: 15px;
        height: 15px;
        border-radius: 50%;
        background-color: #ccc; /* Default neutral */
        transition: background-color 0.5s ease-in-out; /* Animation for color change */
    }

    /* Status Indicator Colors (JS will add classes like 'status-good', 'status-warning', 'status-bad') */
    .status-indicator.status-good { background-color: #4caf50; } /* Green */
    .status-indicator.status-warning { background-color: #ff9800; } /* Orange */
    .status-indicator.status-bad { background-color: #f44336; } /* Red */


    .policy-lever {
        display: flex;
        flex-direction: column;
        padding: 10px;
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.05);
    }

    .policy-lever label {
        margin-bottom: 8px; /* Increased margin */
        font-weight: bold;
        color: #555;
        font-size: 0.95em;
    }

    .policy-lever input[type="range"] {
        width: 100%;
        -webkit-appearance: none;
        appearance: none;
        height: 8px;
        background: #d3d3d3;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 5px;
    }

    .policy-lever input[type="range"]:hover {
        opacity: 1;
    }

    .policy-lever input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #0a3d62;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0 1px 4px rgba(0,0,0,0.2);
    }

    .policy-lever input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #0a3d62;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0 1px 4px rgba(0,0,0,0.2);
    }


    .lever-value {
        display: block; /* Make span a block to center text */
        text-align: center;
        font-weight: bold;
        color: #007bff; /* Blue color */
        margin-top: 5px;
        font-size: 1.1em;
    }

    .feedback-area {
        min-height: 40px; /* Reserve space */
        background-color: #fff9c4; /* Light yellow */
        border: 1px solid #fbc02d;
        color: #333;
        font-size: 0.9em;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 8px;
    }
    .feedback-message {
        margin: 0;
    }


    .btn {
        padding: 12px 20px; /* Larger buttons */
        border: none;
        border-radius: 6px; /* More rounded */
        cursor: pointer;
        font-size: 1.1em; /* Larger font */
        margin-top: 10px;
        transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transitions */
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .btn i { /* Icon styling */
        margin-left: 8px;
    }

    .btn-primary {
        background-color: #007bff; /* Primary blue */
        color: white;
    }

    .btn-primary:hover {
        background-color: #0056b3;
        transform: translateY(-1px); /* Slight hover effect */
    }

    .btn-secondary {
        background-color: #6c757d; /* Secondary grey */
        color: white;
    }
    .btn-secondary:hover {
         background-color: #5a6268;
         transform: translateY(-1px);
    }


     #resetBtn {
        background-color: #dc3545; /* Red for reset */
    }
     #resetBtn:hover {
        background-color: #c82333;
    }

    .toggle-button {
        display: block;
        width: fit-content;
        margin: 30px auto; /* More space */
        padding: 12px 25px;
        background-color: #17a2b8; /* Teal color */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease;
         display: flex;
        align-items: center;
        justify-content: center;
    }
     .toggle-button:hover {
        background-color: #138496;
    }
     .toggle-button i {
         margin-left: 8px;
     }


    .explanation-area {
        border: 1px solid #dcdcdc;
        padding: 30px;
        border-radius: 12px;
        background-color: #ffffff;
        line-height: 1.7;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    .explanation-area h2, .explanation-area h3 {
        color: #0a3d62;
        margin-top: 25px;
        margin-bottom: 12px;
    }
    .explanation-area h2 {
        border-bottom: 2px solid #eee;
        padding-bottom: 10px;
    }
    .explanation-area ul {
        margin-left: 25px; /* Increased indent */
        margin-bottom: 15px;
    }
    .explanation-area li {
        margin-bottom: 8px;
    }

    /* Responsive Adjustments */
    @media (max-width: 768px) {
        .simulator-container {
            flex-direction: column;
            padding: 20px;
        }
        .graphs-area, .controls-area {
            min-width: 100%;
        }
        .controls-area {
             padding: 20px;
        }
         .btn {
             font-size: 1em;
             padding: 10px 15px;
         }
          .toggle-button {
              font-size: 1em;
               padding: 10px 20px;
          }
          body {
              padding: 10px;
          }
    }

    /* Add simple icons - could use Font Awesome or similar library if available */
    /* For now, using placeholder styles */
    .icon-play:before { content: '\25BA'; } /* ▶ */
    .icon-reset:before { content: '\21BA'; } /* ↺ */
    .icon-info:before { content: '\2139'; } /* ℹ */


</style>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    // --- Simulation Model Parameters ---
    const initialYear = 2023;
    const totalYears = 15; // Simulate 15 years
    const crisisStartYear = 0; // Crisis starts at the beginning (relative to simulation start, not initialYear)

    // Initial Crisis State (Year 0 of simulation)
    let inflation = 6.0; // High inflation (slightly increased)
    let unemployment = 7.5; // High unemployment (slightly increased)
    let gdpGrowth = -2.0; // Deeper Recession
    let interestRateBase = 3.0; // Base level (not changed directly by slider)
    let govSpendingBase = 100; // Base level
    let taxRateBase = 20; // Base level

    // Targets (Illustrative - actual targets can vary)
    const targetInflation = 2.0;
    const targetUnemployment = 4.0;
    const targetGdpGrowth = 3.0;

    // Model Dynamics (Simplified coefficients - tuned for more noticeable trade-offs and lags)
    // Policy changes apply with a lag and effect might decay over time.
    const lagPolicyToInflation = 2; // Years until effect starts significantly impacting inflation
    const lagPolicyToUnemployment = 1; // Years until effect starts significantly impacting unemployment
    const lagPolicyToGdp = 1; // Years until effect starts significantly impacting GDP

    // How policy changes affect indicators (simplified linear impact)
    // Effects are felt *after* the lag, potentially spread over multiple years.
    // Let's make the effect decay over time after the lag.
    // A positive change in IR: lowers Inf and Gdp, raises Unemp
    const irEffectInf = -0.6; // Stronger impact on inflation
    const irEffectUnemp = 0.4; // Stronger impact on unemployment
    const irEffectGdp = -0.5; // Stronger impact on GDP

    // A positive change in GS: raises Inf, lowers Unemp, raises Gdp
    const gsEffectInf = 0.3; // Stronger impact on inflation
    const gsEffectUnemp = -0.4; // Stronger impact on unemployment
    const gsEffectGdp = 0.6; // Stronger impact on GDP

    // A positive change in Tax: lowers Inf, raises Unemp, lowers Gdp
    const taxEffectInf = -0.2; // Slightly stronger impact
    const taxEffectUnemp = 0.3; // Slightly stronger impact
    const taxEffectGdp = -0.4; // Slightly stronger impact

    // Natural relationships (Simplified Phillips curve type and Okun's Law type)
    // Deviation from target unemployment/GDP influences inflation/unemployment in the next period.
    const unempDevEffectInf = -0.4; // Lower unemployment (below target) increases inflation more
    const gdpDevEffectUnemp = -0.5; // Higher GDP growth (above target) lowers unemployment more

    // Persistence of shocks/past values - determines how much the previous state influences the current one
    const persistence = 0.6; // Lower persistence means policies/shocks have a quicker impact, but also fade faster.

    // Random shock parameters
    const shockMagnitude = 0.5; // Max percentage points deviation due to random shock

    // --- Simulation State ---
    let currentYear = 0; // Year index within the simulation (0 to totalYears)
    let history = [{ year: initialYear, inflation: inflation, unemployment: unemployment, gdpGrowth: gdpGrowth }];
    // Store past policy decisions. Policy decided in year Y affects outcomes from Y+lag onwards.
    // policyHistory stores deltas decided AT THE END OF year Y, to apply FROM year Y+1
    let policyHistory = []; // [{ simYear: Y, delta_ir: X, delta_gs: Y, delta_tax: Z }]

    // --- Chart Setup ---
    let inflationChart, unemploymentChart, gdpChart;
    const feedbackArea = document.getElementById('feedbackArea');
    const feedbackMessage = feedbackArea.querySelector('.feedback-message');


    const setupCharts = () => {
        const commonOptions = {
             animation: {
                duration: 800, // Animation duration in milliseconds
                easing: 'easeInOutQuad' // Animation easing
            },
            scales: {
                x: {
                    type: 'linear',
                    title: {
                        display: true,
                        text: 'שנה'
                    },
                     ticks: {
                        callback: function(value, index, values) {
                            // Display initialYear + value (year index)
                             return initialYear + value;
                        }
                    },
                     min: 0, // Start x-axis at 0 (representing initialYear)
                     max: totalYears, // End x-axis at totalYears
                },
                y: {
                    title: {
                        display: true,
                        text: '%'
                    },
                     suggestedMin: -5, // Suggest a reasonable minimum
                     suggestedMax: 15, // Suggest a reasonable maximum
                }
            },
             plugins: {
                 tooltip: {
                    rtl: true, // Enable RTL for tooltip
                    callbacks: {
                         title: function(context) {
                            // Display initialYear + value (year index) in tooltip title
                             return `שנה: ${initialYear + context[0].parsed.x}`;
                        },
                         label: function(context) {
                             return `${context.dataset.label}: ${context.parsed.y.toFixed(1)}%`;
                         }
                    }
                },
                legend: {
                     rtl: true, // Enable RTL for legend
                     labels: {
                         usePointStyle: true, // Use point style in legend
                         padding: 15,
                     }
                },
            },
            responsive: true,
            maintainAspectRatio: false,
             hover: {
                 mode: 'nearest',
                 intersect: true
             },
             interaction: {
                mode: 'nearest',
                intersect: false,
                axis: 'x'
            }
        };

        const inflationCtx = document.getElementById('inflationChart').getContext('2d');
        inflationChart = new Chart(inflationCtx, {
            type: 'line',
            data: {
                labels: history.map(h => h.year - initialYear), // Use year index for x-axis
                datasets: [
                    {
                        label: 'אינפלציה (%)',
                        data: history.map(h => h.inflation),
                        borderColor: 'rgb(255, 99, 132)', // Reddish
                        backgroundColor: 'rgba(255, 99, 132, 0.3)', // Light Reddish fill
                        fill: true,
                        tension: 0.2, // Smoother line
                        pointRadius: 4,
                        pointBackgroundColor: 'rgb(255, 99, 132)',
                         pointBorderColor: '#fff',
                         pointHoverRadius: 6,
                    },
                     {
                        label: 'יעד אינפלציה (%)',
                        data: Array(totalYears + 1).fill(targetInflation), // +1 for initial state, fixed length for target line
                        borderColor: 'rgb(75, 192, 192)', // Teal
                        borderDash: [5, 5],
                        pointRadius: 0,
                        fill: false,
                        tension: 0,
                        borderWidth: 2,
                    }
                ]
            },
            options: {...commonOptions, scales: {...commonOptions.scales, y: {...commonOptions.scales.y, suggestedMax: 10, suggestedMin: 0} }} // Specific y-axis range for inflation
        });

        const unemploymentCtx = document.getElementById('unemploymentChart').getContext('2d');
        unemploymentChart = new Chart(unemploymentCtx, {
            type: 'line',
            data: {
                 labels: history.map(h => h.year - initialYear),
                datasets: [
                    {
                        label: 'אבטלה (%)',
                        data: history.map(h => h.unemployment),
                        borderColor: 'rgb(54, 162, 235)', // Blueish
                        backgroundColor: 'rgba(54, 162, 235, 0.3)', // Light Blueish fill
                         fill: true,
                        tension: 0.2,
                         pointRadius: 4,
                        pointBackgroundColor: 'rgb(54, 162, 235)',
                         pointBorderColor: '#fff',
                         pointHoverRadius: 6,
                    },
                     {
                        label: 'יעד אבטלה (%)',
                         data: Array(totalYears + 1).fill(targetUnemployment),
                        borderColor: 'rgb(75, 192, 192)',
                        borderDash: [5, 5],
                        pointRadius: 0,
                        fill: false,
                        tension: 0,
                        borderWidth: 2,
                    }
                ]
            },
             options: {...commonOptions, scales: {...commonOptions.scales, y: {...commonOptions.scales.y, suggestedMax: 15, suggestedMin: 2} }} // Specific y-axis range for unemployment
        });

        const gdpCtx = document.getElementById('gdpChart').getContext('2d');
        gdpChart = new Chart(gdpCtx, {
            type: 'line',
            data: {
                 labels: history.map(h => h.year - initialYear),
                datasets: [
                    {
                        label: 'צמיחת תוצר (%)',
                        data: history.map(h => h.gdpGrowth),
                        borderColor: 'rgb(153, 102, 255)', // Purplish
                        backgroundColor: 'rgba(153, 102, 255, 0.3)', // Light Purplish fill
                         fill: true,
                        tension: 0.2,
                         pointRadius: 4,
                        pointBackgroundColor: 'rgb(153, 102, 255)',
                         pointBorderColor: '#fff',
                         pointHoverRadius: 6,
                    },
                     {
                        label: 'יעד צמיחה (%)',
                         data: Array(totalYears + 1).fill(targetGdpGrowth),
                        borderColor: 'rgb(75, 192, 192)',
                        borderDash: [5, 5],
                        pointRadius: 0,
                        fill: false,
                        tension: 0,
                        borderWidth: 2,
                    }
                ]
            },
             options: {...commonOptions, scales: {...commonOptions.scales, y: {...commonOptions.scales.y, suggestedMax: 10, suggestedMin: -10} }} // Specific y-axis range for GDP
        });

         updateCurrentStatus();
    };

     const updateCharts = () => {
         const years = history.map(h => h.year - initialYear);
         const historyLength = history.length;

         // Update data and labels for all charts
         inflationChart.data.labels = years;
         inflationChart.data.datasets[0].data = history.map(h => h.inflation);
         // Keep target line length consistent with max simulation years for better visualization
         inflationChart.data.datasets[1].data = Array(totalYears + 1).fill(targetInflation);
         // Ensure the x-axis scale updates correctly if using linear scale
         inflationChart.options.scales.x.max = totalYears;

         unemploymentChart.data.labels = years;
         unemploymentChart.data.datasets[0].data = history.map(h => h.unemployment);
         unemploymentChart.data.datasets[1].data = Array(totalYears + 1).fill(targetUnemployment);
         unemploymentChart.options.scales.x.max = totalYears;


         gdpChart.data.labels = years;
         gdpChart.data.datasets[0].data = history.map(h => h.gdpGrowth);
         gdpChart.data.datasets[1].data = Array(totalYears + 1).fill(targetGdpGrowth);
         gdpChart.options.scales.x.max = totalYears;


         // Use update with 'show' animation
         inflationChart.update('show');
         unemploymentChart.update('show');
         gdpChart.update('show');


         updateCurrentStatus();
     };

     const updateCurrentStatus = () => {
         const latest = history[history.length - 1];
         document.getElementById('currentYear').innerText = latest.year;

         const inflationSpan = document.getElementById('currentInflation');
         const unemploymentSpan = document.getElementById('currentUnemployment');
         const gdpGrowthSpan = document.getElementById('currentGdpGrowth');

         inflationSpan.innerText = latest.inflation.toFixed(1);
         unemploymentSpan.innerText = latest.unemployment.toFixed(1);
         gdpGrowthSpan.innerText = latest.gdpGrowth.toFixed(1);

         // Update status indicators based on how close they are to targets
         updateStatusIndicator(inflationSpan.nextElementSibling, latest.inflation, targetInflation, false); // false = lower is better/target
         updateStatusIndicator(unemploymentSpan.nextElementSibling, latest.unemployment, targetUnemployment, false); // false = lower is better/target
         updateStatusIndicator(gdpGrowthSpan.nextElementSibling, latest.gdpGrowth, targetGdpGrowth, true); // true = higher is better/target

          // Add dynamic feedback message
          displayFeedback(latest);
     };

     const updateStatusIndicator = (indicatorElement, currentValue, targetValue, higherIsBetter) => {
         indicatorElement.classList.remove('status-good', 'status-warning', 'status-bad');
         const diff = currentValue - targetValue;
         const absDiff = Math.abs(diff);

         let statusClass;
         if (higherIsBetter) {
             if (diff >= -0.5) { // Close to or above target
                 statusClass = 'status-good';
             } else if (diff >= -2) { // Moderately below target
                 statusClass = 'status-warning';
             } else { // Significantly below target
                 statusClass = 'status-bad';
             }
         } else { // Lower is better
             if (diff <= 0.5) { // Close to or below target
                 statusClass = 'status-good';
             } else if (diff <= 2) { // Moderately above target
                 statusClass = 'status-warning';
             } else { // Significantly above target
                 statusClass = 'status-bad';
             }
         }
         indicatorElement.classList.add(statusClass);
     };

     const displayFeedback = (latestState) => {
         let message = "";
         const infDiff = latestState.inflation - targetInflation;
         const unempDiff = latestState.unemployment - targetUnemployment;
         const gdpDiff = latestState.gdpGrowth - targetGdpGrowth;

         // Combine indicators for feedback
         const infStatus = infDiff <= 0.5 ? 'good' : (infDiff <= 2 ? 'warning' : 'bad');
         const unempStatus = unempDiff <= 0.5 ? 'good' : (unempDiff <= 2 ? 'warning' : 'bad');
         const gdpStatus = gdpDiff >= -0.5 ? 'good' : (gdpDiff >= -2 ? 'warning' : 'bad');

         if (infStatus === 'good' && unempStatus === 'good' && gdpStatus === 'good') {
             message = "מצב כלכלי יציב ובריא - המדיניות שלכם אפקטיבית!";
             feedbackArea.style.backgroundColor = '#e8f5e9'; // Greenish
             feedbackArea.style.borderColor = '#4caf50';
         } else if (infStatus === 'bad' && unempStatus === 'bad') {
              message = "סטגפלציה! אינפלציה ואבטלה גבוהות בו זמנית - אתגר קשה למדיניות!";
              feedbackArea.style.backgroundColor = '#ffcdd2'; // Reddish
              feedbackArea.style.borderColor = '#f44336';
         } else if (gdpStatus === 'bad' && (infStatus === 'warning' || unempStatus === 'warning' || infStatus === 'bad' || unempStatus === 'bad')) {
             message = "הכלכלה במיתון או האטה, עם אתגרים נוספים באינפלציה/אבטלה. צריך תמריצים?";
             feedbackArea.style.backgroundColor = '#ffe0b2'; // Orangish
             feedbackArea.style.borderColor = '#ff9800';
         } else if (infStatus === 'bad') {
             message = "האינפלציה ממשיכה לעלות - הגיע הזמן לקרר את הכלכלה?";
             feedbackArea.style.backgroundColor = '#ffcdd2';
             feedbackArea.style.borderColor = '#f44336';
         } else if (unempStatus === 'bad') {
              message = "האבטלה גבוהה - יש צורך במדיניות לעידוד תעסוקה?";
              feedbackArea.style.backgroundColor = '#bbdefb'; // Blueish
              feedbackArea.style.borderColor = '#2196f3';
         } else if (gdpStatus === 'good' && (infStatus === 'warning' || infStatus === 'bad')) {
             message = "הכלכלה צומחת יפה, אך לחצים אינפלציוניים גוברים.";
             feedbackArea.style.backgroundColor = '#fff9c4'; // Yellowish
             feedbackArea.style.borderColor = '#fbc02d';
         }
          else if (gdpStatus === 'good' && unempStatus === 'good') {
              message = "צמיחה טובה וירידה באבטלה - אך שימו לב לאינפלציה בהמשך!";
              feedbackArea.style.backgroundColor = '#e8f5e9';
              feedbackArea.style.borderColor = '#4caf50';
          }
         else {
              message = "המשיכו לקבל החלטות כדי להוציא את הכלכלה מהמשבר.";
               feedbackArea.style.backgroundColor = '#e0e0e0'; // Greyish
               feedbackArea.style.borderColor = '#9e9e9e';
         }


         feedbackMessage.innerText = message;
     };


    // --- Simulation Logic ---
    const simulateYear = () => {
        if (currentYear >= totalYears) {
            alert("הסימולציה הסתיימה לאחר " + totalYears + " שנים.");
            return;
        }

        // Get policy decisions made at the END of currentYear, intended for impact FROM currentYear + 1
        const currentPolicyDelta = {
            simYearDecided: currentYear, // Policy decided now (end of year currentYear)
            delta_ir: parseFloat(document.getElementById('interestRate').value),
            delta_gs: parseFloat(document.getElementById('govSpending').value),
            delta_tax: parseFloat(document.getElementById('taxRate').value)
        };
        policyHistory.push(currentPolicyDelta);

        currentYear++; // Advance to the next year

        const lastState = history[history.length - 1];
        let currentInflation = lastState.inflation;
        let currentUnemployment = lastState.unemployment;
        let currentGdpGrowth = lastState.gdpGrowth;


        // Calculate accumulated effects from past policies (with lags and decay)
        let totalPolicyEffectInf = 0;
        let totalPolicyEffectUnemp = 0;
        let totalPolicyEffectGdp = 0;

        policyHistory.forEach(policy => {
            // Policy decided at simYearDecided starts having effect from simYearDecided + 1
            const yearsSincePolicyDecisionStart = currentYear - (policy.simYearDecided + 1);

             // Apply effects based on specific lags and decay over time
             const decayFactor = (years) => Math.max(0, 1 - years * 0.15); // Example: linear decay after effect starts

             if (yearsSincePolicyDecisionStart >= lagPolicyToInflation) {
                 const effectiveYears = yearsSincePolicyDecisionStart - lagPolicyToInflation;
                 totalPolicyEffectInf += policy.delta_ir * irEffectInf * decayFactor(effectiveYears);
                 totalPolicyEffectInf += policy.delta_gs * gsEffectInf * decayFactor(effectiveYears);
                 totalPolicyEffectInf += policy.delta_tax * taxEffectInf * decayFactor(effectiveYears);
             }

             if (yearsSincePolicyDecisionStart >= lagPolicyToUnemployment) {
                 const effectiveYears = yearsSincePolicyDecisionStart - lagPolicyToUnemployment;
                 totalPolicyEffectUnemp += policy.delta_ir * irEffectUnemp * decayFactor(effectiveYears);
                 totalPolicyEffectUnemp += policy.delta_gs * gsEffectUnemp * decayFactor(effectiveYears);
                 totalPolicyEffectUnemp += policy.delta_tax * taxEffectUnemp * decayFactor(effectiveYears);
             }

              if (yearsSincePolicyDecisionStart >= lagPolicyToGdp) {
                 const effectiveYears = yearsSincePolicyDecisionStart - lagPolicyToGdp;
                 totalPolicyEffectGdp += policy.delta_ir * irEffectGdp * decayFactor(effectiveYears);
                 totalPolicyEffectGdp += policy.delta_gs * gsEffectGdp * decayFactor(effectiveYears);
                 totalPolicyEffectGdp += policy.delta_tax * taxEffectGdp * decayFactor(effectiveYears);
             }
        });

        // Add a small random shock for realism
        const randomShockInf = (Math.random() - 0.5) * shockMagnitude;
        const randomShockUnemp = (Math.random() - 0.5) * shockMagnitude;
        const randomShockGdp = (Math.random() - 0.5) * shockMagnitude;


        // Calculate next state based on persistence, targets, relationships, policies, and shocks
        // Use deviation from target for natural relationships
        let nextInflation = currentInflation * persistence
                            + (1 - persistence) * (targetInflation + (currentUnemployment - targetUnemployment) * unempDevEffectInf)
                            + totalPolicyEffectInf
                            + randomShockInf;

        let nextGdpGrowth = currentGdpGrowth * persistence
                           + (1 - persistence) * targetGdpGrowth
                           + totalPolicyEffectGdp
                           + randomShockGdp;

         // Unemployment responds to its own persistence, target, and deviation from target GDP growth
         let nextUnemployment = currentUnemployment * persistence
                                + (1 - persistence) * (targetUnemployment + (targetGdpGrowth - nextGdpGrowth) * gdpDevEffectUnemp) // Note: Using nextGdpGrowth here for potential feedback loop
                                + totalPolicyEffectUnemp
                                + randomShockUnemp;


        // Ensure indicators stay within reasonable bounds
        nextInflation = Math.max(-3.0, Math.min(25.0, nextInflation)); // Inflation min/max
        nextUnemployment = Math.max(2.0, Math.min(30.0, nextUnemployment)); // Unemployment min/max (natural friction > 0)
        nextGdpGrowth = Math.max(-15.0, Math.min(15.0, nextGdpGrowth)); // GDP growth min/max


        // Update state variables
        inflation = nextInflation;
        unemployment = nextUnemployment;
        gdpGrowth = nextGdpGrowth;

        // Store history
        history.push({ year: initialYear + currentYear, inflation: inflation, unemployment: unemployment, gdpGrowth: gdpGrowth });

        // Update charts and status display
        updateCharts();

         // Reset policy sliders for the next year's decision
         document.getElementById('interestRate').value = 0;
         document.getElementById('govSpending').value = 0;
         document.getElementById('taxRate').value = 0;
         document.getElementById('interestRateValue').innerText = '0.0%';
         document.getElementById('govSpendingValue').innerText = '0.0%';
         document.getElementById('taxRateValue').innerText = '0.0 נק\'';

         // Disable button if simulation ended
         if (currentYear >= totalYears) {
              document.getElementById('simulateBtn').disabled = true;
              document.getElementById('simulateBtn').innerText = "סימולציה הסתיימה";
         }
    };

     const resetSimulation = () => {
         currentYear = 0;
         // Reset to initial crisis state
         inflation = 6.0;
         unemployment = 7.5;
         gdpGrowth = -2.0;

         history = [{ year: initialYear, inflation: inflation, unemployment: unemployment, gdpGrowth: gdpGrowth }];
         policyHistory = []; // Clear past policy decisions

         // Reset sliders and values
         document.getElementById('interestRate').value = 0;
         document.getElementById('govSpending').value = 0;
         document.getElementById('taxRate').value = 0;
         document.getElementById('interestRateValue').innerText = '0.0%';
         document.getElementById('govSpendingValue').innerText = '0.0%';
         document.getElementById('taxRateValue').innerText = '0.0 נק\'';

         // Reset feedback area
          feedbackMessage.innerText = "המשיכו לקבל החלטות כדי להוציא את הכלכלה מהמשבר.";
          feedbackArea.style.backgroundColor = '#e0e0e0';
          feedbackArea.style.borderColor = '#9e9e9e';


          // Re-enable button and text
         document.getElementById('simulateBtn').disabled = false;
         document.getElementById('simulateBtn').innerHTML = 'קדם שנה <i class="icon-play"></i>';


         updateCharts(); // Reset charts
     };

    // --- Event Listeners ---
    document.getElementById('simulateBtn').addEventListener('click', simulateYear);
    document.getElementById('resetBtn').addEventListener('click', resetSimulation);

    document.getElementById('interestRate').addEventListener('input', (e) => {
        document.getElementById('interestRateValue').innerText = parseFloat(e.target.value).toFixed(1) + '%';
    });
     document.getElementById('govSpending').addEventListener('input', (e) => {
        document.getElementById('govSpendingValue').innerText = parseFloat(e.target.value).toFixed(1) + '%';
    });
     document.getElementById('taxRate').addEventListener('input', (e) => {
        document.getElementById('taxRateValue').innerText = parseFloat(e.target.value).toFixed(1) + ' נק\'';
    });

    document.getElementById('toggleExplanation').addEventListener('click', () => {
        const explanationDiv = document.getElementById('explanation');
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
         // Optional: scroll to explanation if showing it
         if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });


    // --- Initial Setup ---
    setupCharts();

</script>
---
```