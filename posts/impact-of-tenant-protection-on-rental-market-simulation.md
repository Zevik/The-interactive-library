---
title: "השפעת הגנת הדייר: סימולציית שוק שכירות דינמית"
english_slug: impact-of-tenant-protection-on-rental-market-simulation
category: "כלכלה"
tags:
  - שוק השכירות
  - הגנת הדייר
  - רגולציה
  - היצע וביקוש
  - מדיניות דיור
---
<h1>השפעת הגנת הדייר: סימולציית שוק שכירות דינמית</h1>
<p>מדינות רבות מנסות להגן על דיירים מפני עליות מחירים ופינויים באמצעות חוקי הגנת הדייר. אך האם חוקים אלו תמיד משיגים את מטרתם? הזז את המחוון כדי לראות כיצד רמות שונות של הגנה יכולות להשפיע על שוק השכירות - לעיתים בדרכים מפתיעות.</p>

<div class="simulation-container">
    <h2>חקר הסימולציה</h2>
    <div class="controls">
        <label for="protectionLevel">עוצמת הגנת הדייר:</label>
        <div class="slider-wrapper">
             <input type="range" id="protectionLevel" min="0" max="100" value="0">
             <span id="protectionValue" class="slider-value">0%</span>
        </div>
         <p class="control-hint">הגנה גבוהה פירושה מחיר מוגבל יותר וקשה יותר לפנות דיירים.</p>
    </div>

    <div class="results">
        <div class="result-item" id="availableUnitsItem">
            <span class="label">היצע דירות זמין בשוק:</span>
            <span id="availableUnits" class="value"></span>
        </div>
        <div class="result-item" id="regulatedPriceItem">
            <span class="label">מחיר שכירות רשמי ממוצע:</span>
            <span id="regulatedPrice" class="value"></span>
        </div>
         <div class="result-item" id="demandItem">
            <span class="label">ביקוש לדירות במחיר הרשמי:</span>
            <span id="demandAtPrice" class="value"></span>
        </div>
        <div class="result-item" id="actualUnitsItem">
            <span class="label">עסקאות שכירות בפועל (מוגבל ע"י היצע):</span>
            <span id="actualUnits" class="value"></span>
        </div>
        <div class="result-item warning" id="shortageItem">
            <span class="label">פער בין ביקוש להיצע (מחסור):</span>
            <span id="shortage" class="value"></span>
        </div>
         <div class="result-item warning" id="pressureItem">
            <span class="label">תופעות לוואי אפשריות:</span>
            <span id="pressure" class="value"></span>
        </div>
    </div>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --primary-color-dark: #0056b3;
        --secondary-color: #6c757d;
        --warning-color: #ffc107;
        --danger-color: #dc3545;
        --success-color: #28a745;
        --light-bg: #f8f9fa;
        --dark-bg: #343a40;
        --card-bg: #ffffff;
        --border-color: #dee2e6;
        --text-color: #212529;
        --text-color-light: #f8f9fa;
    }

    body {
        font-family: 'Arial Hebrew', 'Arial', sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        direction: rtl;
        text-align: right;
        background-color: var(--light-bg);
        color: var(--text-color);
    }

    h1, h2, h3 {
        color: var(--primary-color);
        margin-bottom: 15px;
    }

    p {
        margin-bottom: 15px;
    }

    .simulation-container {
        border: 1px solid var(--border-color);
        padding: 25px;
        margin-bottom: 30px;
        border-radius: 12px;
        background-color: var(--card-bg);
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    .controls {
        margin-bottom: 30px;
        padding-bottom: 20px;
        border-bottom: 1px solid var(--border-color);
    }

    .controls label {
        display: block;
        margin-bottom: 15px;
        font-weight: bold;
        font-size: 1.1em;
        color: var(--secondary-color);
    }

    .slider-wrapper {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .controls input[type="range"] {
        flex-grow: 1;
        -webkit-appearance: none;
        appearance: none;
        height: 8px;
        background: var(--primary-color);
        outline: none;
        opacity: 0.9;
        transition: opacity .2s;
        border-radius: 5px;
    }

    .controls input[type="range"]:hover {
        opacity: 1;
    }

    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 22px;
        height: 22px;
        background: var(--primary-color-dark);
        cursor: pointer;
        border-radius: 50%;
        border: 3px solid var(--card-bg);
        box-shadow: 0 2px 5px rgba(0,0,0,0.3);
        transition: transform 0.1s ease;
    }
     .controls input[type="range"]::-webkit-slider-thumb:active {
         transform: scale(1.1);
     }


    .controls input[type="range"]::-moz-range-thumb {
        width: 22px;
        height: 22px;
        background: var(--primary-color-dark);
        cursor: pointer;
        border-radius: 50%;
        border: 3px solid var(--card-bg);
        box-shadow: 0 2px 5px rgba(0,0,0,0.3);
         transition: transform 0.1s ease;
    }
    .controls input[type="range"]::-moz-range-thumb:active {
         transform: scale(1.1);
    }


     .slider-value {
        font-size: 1.3em;
        font-weight: bold;
        min-width: 60px; /* Ensure space for 3 digits and % */
        text-align: center;
        color: var(--primary-color-dark);
     }

     .control-hint {
         font-size: 0.9em;
         color: var(--secondary-color);
         margin-top: 10px;
         font-style: italic;
     }


    .results {
        margin-top: 20px;
    }

    .result-item {
        margin-bottom: 15px;
        padding: 15px;
        background-color: var(--light-bg);
        border-radius: 8px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: background-color 0.3s ease, border-color 0.3s ease; /* Added transition */
    }

    .result-item .label {
        font-weight: bold;
        color: var(--text-color);
        flex-grow: 1; /* Allows label to take up available space */
    }

    .result-item .value {
        font-weight: bold;
        font-size: 1.1em;
        color: var(--primary-color-dark); /* Default value color */
         min-width: 150px; /* Ensure space for numbers */
        text-align: left; /* Align values to the left in RTL */
         transition: color 0.3s ease; /* Transition for value color */
    }

     /* Specific styling for warning/danger results */
     .result-item.warning {
        background-color: #fffbe6; /* Light yellow background */
        border: 1px solid var(--warning-color);
     }

    .result-item.danger {
        background-color: #f8d7da; /* Light red background */
        border: 1px solid var(--danger-color);
    }

    .result-item.warning .value {
         color: var(--warning-color);
     }

     .result-item.danger .value {
        color: var(--danger-color);
     }

    /* Animation for value updates */
     .result-item .value.updating {
         /* You could add a pulse or highlight animation here if desired */
         /* Example: text-shadow: 0 0 8px rgba(0,0,0,0.2); */
     }


    #toggleExplanation {
        display: block;
        margin: 30px auto;
        padding: 12px 20px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        background-color: var(--primary-color);
        color: var(--text-color-light);
        border-radius: 5px;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    #toggleExplanation:hover {
        background-color: var(--primary-color-dark);
        transform: translateY(-2px);
    }
     #toggleExplanation:active {
        transform: translateY(0);
    }


    #explanation {
        margin-top: 30px;
        border-top: 1px solid var(--border-color);
        padding-top: 30px;
    }

    #explanation h2 {
        color: var(--secondary-color);
        margin-bottom: 20px;
    }

    #explanation h3 {
        color: var(--primary-color);
        margin-top: 20px;
        margin-bottom: 10px;
    }

    #explanation p {
        margin-bottom: 15px;
        color: var(--text-color);
    }

     #explanation ul {
         margin-bottom: 15px;
         padding-right: 20px; /* Adjust for RTL list */
     }

     #explanation ul li {
         margin-bottom: 8px;
         color: var(--text-color);
     }

</style>

<button id="toggleExplanation">הצג הסבר מפורט ומסקנות</button>

<div id="explanation" style="display: none;">
    <h2>הצד התיאורטי מאחורי הסימולציה</h2>

    <h3>שוק שכירות "חופשי" מול רגולציה</h3>
    <p>בשוק ללא רגולציה משמעותית, מחיר השכירות וכמות העסקאות נקבעים על פי האינטרס ההדדי של שוכרים (ביקוש) ומשכירים (היצע). כשהמחיר עולה, שוכרים רבים יותר יחפשו אלטרנטיבות (הביקוש יורד), ומשכירים רבים יותר יראו בכך הזדמנות להשכיר (ההיצע יעלה). שיווי המשקל הוא הנקודה בה רצונות השוכרים והמשכירים נפגשים, וקובעים מחיר ו"כמות שיווי משקל".</p>

    <h3>מטרות הגנת הדייר - וההשפעות בפועל</h3>
    <p>חוקי הגנת הדייר נועדו לשרת מטרה חברתית חשובה: להבטיח יציבות דיור ולמנוע ניצול של שוכרים. הם עושים זאת בדרך כלל על ידי הגבלת גובה שכר הדירה ומניעת פינויים קלים. המטרה היא להפוך את הדיור לנגיש יותר עבור אלו שזקוקים לו.</p>
     <p>עם זאת, לרגולציה כזו יכולות להיות השפעות לא מכוונות על השוק כולו:</p>
    <ul>
        <li><strong>התכווצות ההיצע:</strong> כששכר הדירה המותר מוגבל, או כשהמשכיר מתקשה לפנות דייר בעייתי, הכדאיות הכלכלית והגמישות של השכרת דירה יורדות. משכירים עשויים להעדיף למכור את הנכס, להשתמש בו לצרכים אחרים, או פשוט להשאיר אותו ריק - וכך מקטינים את ההיצע הזמין בשוק.</li>
        <li><strong>ירידה באיכות הדיור:</strong> אם שכר הדירה קבוע או עולה באופן מינימלי בלבד, למשכירים יש פחות תמריץ להשקיע כסף בתחזוקה ושיפורים של הדירה. עם הזמן, איכות יחידות הדיור המוגנות נוטה לרדת.</li>
        <li><strong>התפתחות שוק שחור:</strong> אם המחיר הרשמי נמוך משמעותית ממחיר השוק הפוטנציאלי, נוצר תמריץ חזק לעסקאות "מתחת לשולחן" - שוק שחור שבו המחיר גבוה יותר (לעיתים אף יותר מבשוק חופשי), ולשוכרים אין את ההגנות שהחוק הרשמי אמור לספק.</li>
        <li><strong>קשיים במציאת דירה חדשה:</strong> בעוד שהדיירים ה"וותיקים" בדירות המוגנות נהנים ממחיר נמוך ויציבות, שוכרים חדשים מתקשים למצוא דירות פנויות בשוק הרשמי בשל הירידה בהיצע.</li>
    </ul>

    <h3>מדוע זה קורה? מבט על תמריצים</h3>
    <p>השפעות אלו אינן תוצאה של כוונות רעות, אלא של תמריצים כלכליים בסיסיים. בשוק חופשי, רווח פוטנציאלי מהשכרה מעודד משכירים להציע יותר דירות ולהשקיע בהן. הגנת דייר מוגזמת פוגעת בתמריצים אלו, מה שמוביל לצמצום ההיצע ולתוצאות בלתי רצויות.</p>

    <h3>מסקנה: מורכבות ופשרות הכרחיות</h3>
    <p>הסימולציה מציגה תמונה פשטנית אך ממחישה נקודה חשובה: למדיניות ציבורית יש לעיתים השפעות מורכבות שחורגות מהמטרה המיידית. הגנת הדייר משרתת קבוצה מסוימת (דיירים קיימים), אך עלולה לפגוע בקבוצות אחרות (שוכרים חדשים) וליצור עיוותים בשוק כולו. קובעי מדיניות צריכים לשקול היטב את ה"פשרות" (Trade-offs) השונות ולחפש פתרונות משלימים או חלופיים, כמו סיוע ישיר לשוכרים או הגדלה משמעותית של היצע הדיור הכולל, שפותר את שורש הבעיה.</p>
</div>

<script>
    const protectionSlider = document.getElementById('protectionLevel');
    const protectionValueSpan = document.getElementById('protectionValue');
    const availableUnitsSpan = document.getElementById('availableUnits');
    const regulatedPriceSpan = document.getElementById('regulatedPrice');
    const demandAtPriceSpan = document.getElementById('demandAtPrice');
    const actualUnitsSpan = document.getElementById('actualUnits');
    const shortageSpan = document.getElementById('shortage');
    const pressureSpan = document.getElementById('pressure');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');

    // Elements to add dynamic classes for visual feedback
    const shortageItem = document.getElementById('shortageItem');
    const pressureItem = document.getElementById('pressureItem');


    // Simulation Parameters (tuned for educational effect)
    const totalPotentialUnits = 1500; // Total units if conditions were ideal for landlords
    const baseAvailableUnitsFactor = 0.8; // % of total potential units available at 0 protection
    const unitsDecreaseSlope = 0.006; // How much fraction of total potential units decrease per % protection
    const unitsQuadraticFactor = 0.00005; // Adds non-linearity to supply decrease
    const minAvailableUnitsFactor = 0.15; // Minimum % of total potential units available

    const theoreticalMarketPrice = 3000; // A theoretical price point for scaling
    const baseRegulatedPriceFactor = 0.7; // % of a theoretical market price at 0 protection
    const priceDecreaseSlope = 0.005; // How much fraction of theoretical price decreases per % protection
    const priceQuadraticFactor = 0.00003; // Adds non-linearity to price decrease
    const minRegulatedPriceFactor = 0.2; // Minimum % of theoretical price

    // Demand Model: Demand increases as the *regulated* price decreases (which happens as protection increases)
    const baseDemandFactor = 0.6; // Demand factor at high price (low protection)
    const demandIncreaseSlope = 0.008; // Demand factor increases per % protection


    function updateSimulation() {
        const protectionLevel = parseInt(protectionSlider.value);
        protectionValueSpan.textContent = protectionLevel + '%';

        // Calculate Available Units (Supply decreases with protection, with some acceleration)
        let unitsDecrease = protectionLevel * unitsDecreaseSlope + Math.pow(protectionLevel, 2) * unitsQuadraticFactor;
        unitsDecrease = Math.min(unitsDecrease, baseAvailableUnitsFactor - minAvailableUnitsFactor); // Cap decrease

        const availableUnits = Math.round(totalPotentialUnits * (baseAvailableUnitsFactor - unitsDecrease));
        availableUnitsSpan.textContent = availableUnits.toLocaleString();

        // Calculate Regulated Price (Decreases with protection, with some acceleration)
         let priceDecrease = protectionLevel * priceDecreaseSlope + Math.pow(protectionLevel, 2) * priceQuadraticFactor;
         priceDecrease = Math.min(priceDecrease, baseRegulatedPriceFactor - minRegulatedPriceFactor); // Cap decrease

        const regulatedPrice = Math.round(theoreticalMarketPrice * (baseRegulatedPriceFactor - priceDecrease));
        regulatedPriceSpan.textContent = regulatedPrice.toLocaleString() + ' ש"ח';

        // Calculate Demand at the Regulated Price (Demand is linked to protection level in this simplified model)
        const demandFactor = baseDemandFactor + protectionLevel * demandIncreaseSlope;
        const totalDemandAtPrice = Math.round(totalPotentialUnits * demandFactor); // Demand relative to potential units

        demandAtPriceSpan.textContent = totalDemandAtPrice.toLocaleString();

        // Actual Units Traded is limited by the Available Units (Supply)
        // In a regulated market with shortage, only the available units are actually rented under regulation.
        const actualUnitsTraded = availableUnits;
        actualUnitsSpan.textContent = actualUnitsTraded.toLocaleString();

        // Calculate Shortage
        const shortage = Math.max(0, totalDemandAtPrice - availableUnits);
        shortageSpan.textContent = shortage > 0 ? shortage.toLocaleString() : 'אין פער';

        // Update Shortage Item Styling based on severity
        shortageItem.classList.remove('warning', 'danger');
        if (shortage > 50) shortageItem.classList.add('warning'); // Mild shortage threshold
        if (shortage > 300) shortageItem.classList.add('danger'); // Severe shortage threshold


        // Pressure/Other Effects based on Shortage and Protection
        let pressureText = 'שוק חופשי יחסית, מחיר נקבע ע"י היצע וביקוש'; // Default for 0% protection
        pressureItem.classList.remove('warning', 'danger');


        if (protectionLevel > 5) { // Start showing effects above minimal protection
             if (shortage < 50) {
                 pressureText = 'יציבות יחסית, השפעה מוגבלת';
             } else if (shortage < 300) {
                 pressureText = 'עולה קושי למצוא דירה חדשה, סיכון קטן לשוק לא רשמי';
                 pressureItem.classList.add('warning');
             } else if (shortage < 600) {
                 pressureText = 'מחסור גובר, התפתחות שוק לא רשמי, ירידה אפשרית בתחזוקה';
                  pressureItem.classList.add('warning');
             } else { // shortage >= 600
                 pressureText = 'מחסור חמור ביותר, שוק לא רשמי נרחב, הזנחה קיצונית של נכסים, קפאון בשוק המפוקח';
                 pressureItem.classList.add('danger');
             }

             // Add quality decay effect specifically for higher protection, even if shortage isn't huge yet
             if (protectionLevel > 40 && shortage < 600) { // If high protection but not yet severe shortage
                  if (!pressureText.includes('ירידה אפשרית בתחזוקה')) {
                      pressureText += ', ירידה אפשרית בתחזוקה';
                  }
             }
               if (protectionLevel > 70 && shortage < 600) { // Very high protection
                  if (!pressureText.includes('הזנחה קיצונית')) {
                      pressureText += ', הזנחה קיצונית של נכסים';
                  }
             }

             // Adjust for 0% protection specific text
             if (protectionLevel === 0) {
                  pressureText = 'שוק חופשי יחסית, מחיר נקבע ע"י היצע וביקוש';
                  pressureItem.classList.remove('warning', 'danger');
             }
        } else { // Protection level is 0-5%
             pressureText = 'שוק חופשי יחסית, מחיר נקבע ע"י היצע וביקוש';
             pressureItem.classList.remove('warning', 'danger');
        }


        pressureSpan.textContent = pressureText;

         // Optional: Add a subtle animation class to values on change
        document.querySelectorAll('.results .value').forEach(valueSpan => {
            // Simple animation: add class, let CSS handle transition, remove class
            valueSpan.classList.add('updating');
            // In a real app, check if value actually changed before animating
            setTimeout(() => {
                valueSpan.classList.remove('updating');
            }, 300); // Match CSS transition duration for color/shadow
        });


    }

    // Initial simulation update
    updateSimulation();

    // Add event listener to the slider
    protectionSlider.addEventListener('input', updateSimulation);

    // Add event listener to the toggle button
    toggleExplanationButton.addEventListener('click', function() {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מפורט ומסקנות' : 'הצג הסבר מפורט ומסקנות';

        // Optional: Scroll to explanation if showing it
        if (isHidden) {
            explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

</script>
```