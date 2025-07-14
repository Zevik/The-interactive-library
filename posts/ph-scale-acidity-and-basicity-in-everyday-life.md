---
title: "סולם pH: חומציות ובסיסיות בחיי היומיום"
english_slug: ph-scale-acidity-and-basicity-in-everyday-life
category: "כימיה"
tags: [כימיה, pH, חומצות, בסיסים, מדע, חיי היומיום]
---
# סולם pH: חומציות ובסיסיות בחיי היומיום

מה משותף למיץ לימון ולחומר להסרת אבנית, וממה שונה סבון נוזלי משתיית מים? התשובה טמונה ברמת החומציות או הבסיסיות שלהם, שנמדדת בסולם מיוחד. בואו נגלה זאת באמצעות סימולציה אינטראקטיבית!

<div class="simulation-container">
    <div class="simulation-area">
        <div class="test-tube-container">
            <div class="test-tube">
                <!-- The liquid element will represent the substance added -->
                <div class="liquid" id="testTubeLiquid"></div>
            </div>
            <div class="test-tube-stand"></div>
            <div class="pour-animation"></div> <!-- Element for pour animation -->
        </div>
        <div class="meter-area">
            <div class="ph-display-container">
                <div class="digital-ph-label">pH:</div>
                <div class="digital-ph" id="digitalPH">7.0</div>
            </div>
            <div class="indicator-strip-container">
                <div class="indicator-strip" id="colorIndicator"></div>
                <div class="strip-label">אינדיקטור pH</div>
            </div>
        </div>
    </div>
    <div class="ph-scale-container">
        <div class="ph-scale">
            <div class="scale-pointer" id="scalePointer"></div>
            <div class="scale-numbers">
                <span>0</span><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span><span>8</span><span>9</span><span>10</span><span>11</span><span>12</span><span>13</span><span>14</span>
            </div>
            <div class="scale-labels">
                <span class="acidic-label">חומצי מאוד</span>
                <span class="neutral-label">ניטרלי</span>
                <span class="basic-label">בסיסי מאוד</span>
            </div>
        </div>
    </div>
    <div class="substance-list-container">
        <h3>גררו חומר למבחנה כדי לבדוק את ה-pH שלו:</h3>
        <ul class="substance-list">
            <li class="substance" draggable="true" data-ph="2.0" data-name="מיץ לימון">מיץ לימון</li>
            <li class="substance" draggable="true" data-ph="2.5" data-name="חומץ">חומץ</li>
            <li class="substance" draggable="true" data-ph="5.0" data-name="קפה">קפה</li>
            <li class="substance" draggable="true" data-ph="7.0" data-name="מים מזוקקים">מים מזוקקים</li>
            <li class="substance" draggable="true" data-ph="8.5" data-name="מי סודה לשתייה">מי סודה לשתייה</li>
            <li class="substance" draggable="true" data-ph="9.5" data-name="סבון נוזלי">סבון נוזלי</li>
            <li class="substance" draggable="true" data-ph="12.5" data-name="אקונומיקה">אקונומיקה</li>
        </ul>
    </div>
</div>

<style>
/* --- General Styling --- */
.simulation-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    font-family: 'Heebo', sans-serif; /* Hebrew friendly font, fallback to sans-serif */
    margin: 20px auto;
    padding: 30px 20px;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    background: linear-gradient(to bottom, #f8f8f8, #e8e8e8);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
    max-width: 600px; /* Constrain max width for better look */
}

h1 {
    text-align: center;
    color: #333;
    margin-bottom: 20px;
    font-size: 1.8em;
}

h3 {
    color: #555;
    text-align: center;
    margin-bottom: 15px;
    font-size: 1.2em;
}

/* --- Simulation Area Layout --- */
.simulation-area {
    display: flex;
    align-items: flex-end; /* Align bottoms */
    gap: 40px;
    margin-bottom: 30px;
    position: relative; /* For absolute positioning of pour animation */
}

/* --- Test Tube --- */
.test-tube-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative; /* For pour animation */
}

.test-tube {
    width: 70px; /* Slightly wider */
    height: 220px; /* Slightly taller */
    border: 3px solid #555; /* Stronger border */
    border-bottom: none;
    border-top-left-radius: 35px;
    border-top-right-radius: 35px;
    position: relative;
    overflow: hidden;
    background-color: rgba(224, 247, 250, 0.5); /* Semi-transparent light blue for empty tube */
    box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.1); /* Inner shadow for depth */
    /* Adding glass effect */
    background: linear-gradient(to right, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.5) 30%, rgba(255,255,255,0.1) 100%),
                linear-gradient(to bottom, rgba(224, 247, 250, 0.5), rgba(179, 230, 236, 0.5)); /* Blend empty color with highlight */
    background-blend-mode: overlay;
}

.liquid {
    width: 100%;
    height: 100%; /* Represents full liquid level */
    position: absolute;
    bottom: 0;
    background-color: #4fc3f7; /* Initial water color */
    transition: background-color 0.8s ease-in-out; /* Smooth color transition */
    /* Add subtle liquid surface effect */
    border-top-left-radius: 50% 5px;
    border-top-right-radius: 50% 5px;
}

.test-tube-stand {
    width: 110px; /* Wider stand */
    height: 25px; /* Taller stand */
    background-color: #444;
    border-radius: 8px;
    margin-top: -5px; /* Overlap slightly */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* Drag over effect */
.test-tube.drag-over {
    border-color: #007bff;
    box-shadow: 0 0 15px rgba(0, 123, 255, 0.6), inset 0 0 10px rgba(0, 123, 255, 0.3);
}

/* Pour Animation Element */
.pour-animation {
    position: absolute;
    top: 0;
    left: 50%;
    width: 30px; /* Size of the pouring visual */
    height: 40px;
    background-color: rgba(100, 149, 237, 0.8); /* Default pour color (cornflowerblue) */
    border-bottom-left-radius: 15px 20px;
    border-bottom-right-radius: 15px 20px;
    opacity: 0;
    transform: translateX(-50%);
    pointer-events: none; /* Don't interfere with drag/drop */
    transition: opacity 0.1s ease-out, transform 0.6s ease-in; /* Pour effect */
}

.test-tube-container.pouring .pour-animation {
    opacity: 1;
    transform: translate(-50%, 200px); /* Animate down into the tube */
}


/* --- Meter Area --- */
.meter-area {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
}

.ph-display-container {
    display: flex;
    align-items: center;
    background-color: #222; /* Darker background */
    color: #0f0; /* Bright green LED style */
    padding: 8px 15px; /* More padding */
    border-radius: 8px; /* More rounded corners */
    font-size: 1.8em; /* Larger font */
    font-weight: bold;
    border: 3px inset #444; /* Stronger inset border */
    font-family: 'Share Tech Mono', monospace; /* Digital font */
    box-shadow: inset 0 0 8px rgba(0, 255, 0, 0.3);
}

.digital-ph-label {
    margin-right: 8px; /* More space */
    color: #0c0; /* Slightly darker green */
}

.indicator-strip-container {
    text-align: center;
}

.indicator-strip {
    width: 50px; /* Wider strip */
    height: 180px; /* Taller strip */
    border: 2px solid #333;
    margin-bottom: 8px;
    /* Background color will be set by JS based on pH */
    background-color: #aaa; /* Default neutral color */
    box-shadow: inset 0 0 5px rgba(0,0,0,0.2); /* Inner shadow */
    border-radius: 4px;
    transition: background-color 0.8s ease-in-out; /* Smooth color transition */
}

.strip-label {
    font-size: 1em; /* Slightly larger font */
    color: #555;
    font-weight: bold;
}

/* --- pH Scale --- */
.ph-scale-container {
    width: 100%;
    max-width: 550px; /* Slightly wider max width */
    margin-bottom: 30px;
    padding: 0 15px; /* Add horizontal padding */
    box-sizing: border-box;
}

.ph-scale {
    width: 100%;
    height: 25px; /* Shorter bar */
    background: linear-gradient(to right,
        #e74c3c, #e67e22, #f1c40f, #2ecc40, #3498db, #9b59b6, #8e44ad); /* More distinct colors */
    position: relative;
    border-radius: 12px; /* More rounded caps */
    overflow: visible;
    box-shadow: inset 0 2px 5px rgba(0,0,0,0.2);
}

.scale-pointer {
    width: 16px; /* Wider pointer */
    height: 35px; /* Taller pointer */
    background-color: #333;
    position: absolute;
    top: -5px; /* Position above */
    left: calc(50% - 8px); /* Start at pH 7 (middle), centered */
    transform: translateX(0); /* JS updates left */
    border-radius: 4px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.3);
    transition: left 0.8s ease-in-out; /* Smooth slide transition */
    z-index: 10; /* Ensure pointer is above scale */

    /* Add a small triangle pointing down */
    &::after {
        content: '';
        position: absolute;
        bottom: -8px; /* Position below the pointer */
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 0;
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        border-top: 8px solid #333;
    }
}

.scale-numbers {
    display: flex;
    justify-content: space-between;
    position: absolute;
    width: 100%;
    top: 30px; /* Position below the scale */
    font-size: 0.9em;
    color: #555;
    padding: 0 5px; /* Align numbers better with scale */
    box-sizing: border-box;
}

.scale-numbers span {
    flex-basis: calc(100% / 14); /* Distribute space evenly */
    text-align: center;
    transform: translateX(0); /* Remove previous transform */
    position: relative;
}
/* Fine tuning positions for 0 and 14 to align with ends */
.scale-numbers span:first-child { text-align: left; margin-left: -0.5em; } /* Shift 0 slightly left */
.scale-numbers span:last-child { text-align: right; margin-right: -0.5em; } /* Shift 14 slightly right */


.scale-labels {
    display: flex;
    justify-content: space-between;
    position: absolute;
    width: 100%;
    bottom: 35px; /* Position above the scale */
    font-size: 1em;
    font-weight: bold;
    color: #333;
    padding: 0 10px; /* Padding to align labels */
    box-sizing: border-box;
}

.acidic-label { color: #c0392b; } /* Stronger red */
.neutral-label { color: #27ae60; flex-grow: 0; margin: 0 auto;} /* Darker green, center */
.basic-label { color: #8e44ad; } /* Purple */


/* --- Substance List --- */
.substance-list-container {
    width: 100%;
    max-width: 550px;
    text-align: center;
    padding: 0 15px;
    box-sizing: border-box;
}

.substance-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-wrap: wrap;
    gap: 12px; /* More space between items */
    justify-content: center;
}

.substance {
    background-color: #fff;
    border: 1px solid #ccc;
    padding: 10px 18px; /* More padding */
    border-radius: 20px; /* Pill shape */
    cursor: grab;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.15);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    font-size: 1em;
    color: #333;
    white-space: nowrap; /* Prevent wrapping */
}

.substance:hover {
    border-color: #888;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
}

.substance:active {
    cursor: grabbing;
    transform: scale(0.95);
    box-shadow: 1px 1px 4px rgba(0,0,0,0.1);
}

/* Drag feedback */
.substance.dragging {
    opacity: 0.7; /* Less transparent */
    transform: scale(1.05); /* Slightly larger */
    cursor: grabbing;
}


/* --- Explanation Toggle and Section --- */
#toggleExplanation {
    display: block;
    margin: 30px auto 20px auto; /* More space */
    padding: 12px 25px; /* More padding */
    font-size: 1.1em; /* Larger font */
    cursor: pointer;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 6px;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

#toggleExplanation:hover {
    background-color: #0056b3;
    box-shadow: 0 3px 6px rgba(0,0,0,0.25);
}
#toggleExplanation:active {
    transform: scale(0.98);
}


#explanation {
    border-top: 1px solid #ddd; /* Lighter border */
    margin-top: 20px;
    padding-top: 20px;
    display: none; /* Initially hidden */
    line-height: 1.7; /* More comfortable reading */
    color: #444; /* Darker text color */
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

#explanation h2 {
    color: #333;
    margin-top: 20px; /* More space above headers */
    margin-bottom: 10px;
    font-size: 1.5em;
}

#explanation p {
    margin-bottom: 15px; /* More space between paragraphs */
}

#explanation ul {
    margin-bottom: 15px;
    padding-left: 20px; /* Indent list */
}

#explanation li {
    margin-bottom: 8px;
    color: #555;
}

</style>

<button id="toggleExplanation">הצג/הסתר הסבר על סולם pH</button>

<div id="explanation">
    <h2>מהו pH ומה הוא מייצג?</h2>
    <p>pH (קיצור של potential of Hydrogen) הוא סולם המודד את מידת החומציות או הבסיסיות של תמיסה מימית. הוא מתבסס על ריכוז יוני המימן (H⁺) או יוני ההידרוקסיד (OH⁻) בתמיסה. ריכוז גבוה של יוני H⁺ מעיד על חומציות, וריכוז גבוה של יוני OH⁻ (או ריכוז נמוך של H⁺) מעיד על בסיסיות (אלקליניות). חשוב לזכור שהסולם הוא לוגריתמי, כלומר שינוי של יחידה אחת ב-pH מייצג שינוי פי 10 בריכוז היונים!</p>

    <h2>סולם ה-pH - טווח הערכים (0-14)</h2>
    <p>הסולם המקובל נע בין 0 ל-14. תמיסות עם pH נמוך מ-7 הן חומציות, ותמיסות עם pH גבוה מ-7 הן בסיסיות. ערכים קיצוניים (קרוב ל-0 או קרוב ל-14) מייצגים חומצות או בסיסים חזקים במיוחד, שיכולים להיות מסוכנים ומאכלים.</p>

    <h2>נקודת הניטרליות: pH=7 (מים טהורים)</h2>
    <p>pH=7 הוא נקודת האמצע בסולם ומייצג תמיסה ניטרלית. במים טהורים (בטמפרטורה של 25°C), ריכוז יוני המימן שווה בדיוק לריכוז יוני ההידרוקסיד, ולכן הם ניטרליים.</p>

    <h2>חומצות (pH < 7) - מאפיינים ודוגמאות יומיומיות</h2>
    <p>חומצות הן חומרים שנוטים לשחרר יוני מימן (H⁺) בתמיסה. ככל שה-pH נמוך יותר, כך החומצה "חזקה" יותר ויש בה יותר יוני H⁺. לחומצות רבות יש טעם חמוץ (כמו לימון או חומץ). דוגמאות יומיומיות: מיץ תפוזים (pH ~3.5), קפה (pH ~5), קיבה (pH ~1.5-3.5).</p>

    <h2>בסיסים (pH > 7) - מאפיינים ודוגמאות יומיומיות</h2>
    <p>בסיסים (אלקליים) הם חומרים שנוטים לקבל יוני מימן או לשחרר יוני הידרוקסיד (OH⁻). ככל שה-pH גבוה יותר, כך הבסיס "חזק" יותר. בסיסים רבים מרגישים חלקלקים למגע (כמו סבון). דוגמאות יומיומיות: סבון נוזלי (pH ~9-10), סודה לשתייה מומסת (pH ~8.5), אקונומיקה (pH ~12-13).</p>

    <h2>כיצד מודדים pH (אינדיקטורים ומדי pH)</h2>
    <p>ישנן מספר דרכים למדידת pH:
    <ul>
        <li>**אינדיקטורים כימיים:** חומרים המשנים את צבעם בהתאם ל-pH. דוגמה קלאסית היא נייר ליטמוס. בסימולציה שלנו, "אינדיקטור ה-pH" מחקה את האופן שבו אינדיקטור כימי משנה צבע בהתאם לחומציות/בסיסיות.</li>
        <li>**מדי pH אלקטרוניים:** מכשירים דיגיטליים מדויקים המודדים את ריכוז יוני המימן ומציגים את ה-pH באופן מספרי, בדומה למד הדיגיטלי בסימולציה.</li>
    </ul></p>

    <h2>חשיבות ה-pH בתחומים שונים</h2>
    <p>ל-pH תפקיד מכריע במערכות רבות:
    <ul>
        <li>**גוף האדם:** לכל איבר ונוזל בגוף יש טווח pH אופטימלי לפעילותו. pH הדם נשמר בטווח צר מאוד (7.35-7.45).</li>
        <li>**סביבה:** pH של קרקעות ומים משפיע על חיים צמחיים ובעלי חיים. גשם חומצי (pH נמוך) יכול לפגוע קשות באגמים ויערות.</li>
        <li>**חקלאות:** pH האדמה משפיע על ספיגת חומרי הזנה על ידי צמחים, ולכן חקלאים מתאימים אותו לגידולים שונים.</li>
    </ul></p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const testTubeLiquid = document.getElementById('testTubeLiquid');
    const testTubeElement = testTubeLiquid.closest('.test-tube');
    const testTubeContainer = testTubeLiquid.closest('.test-tube-container');
    const digitalPH = document.getElementById('digitalPH');
    const colorIndicator = document.getElementById('colorIndicator');
    const scalePointer = document.getElementById('scalePointer');
    const substances = document.querySelectorAll('.substance');
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggleExplanation');
    const phScaleElement = document.querySelector('.ph-scale');
    const pourAnimationElement = document.querySelector('.pour-animation');


    // --- Drag and Drop Logic ---
    substances.forEach(substance => {
        substance.addEventListener('dragstart', (event) => {
            event.dataTransfer.setData('text/plain', event.target.dataset.ph);
            event.dataTransfer.setData('text/pourColor', getIndicatorColor(parseFloat(event.target.dataset.ph))); // Pass color for pour animation
            event.target.classList.add('dragging');
        });

        substance.addEventListener('dragend', (event) => {
            event.target.classList.remove('dragging');
        });
    });

    testTubeElement.addEventListener('dragover', (event) => {
        event.preventDefault(); // Allow drop
        event.currentTarget.classList.add('drag-over');
        // Position the pour animation element near the top of the tube
        const rect = testTubeElement.getBoundingClientRect();
        const containerRect = simulationArea.getBoundingClientRect(); // Get parent container's position
        pourAnimationElement.style.left = `${rect.left + rect.width / 2 - containerRect.left}px`;
        pourAnimationElement.style.top = `${rect.top - containerRect.top - 30}px`; // Position above the tube
    });

     testTubeElement.addEventListener('dragenter', (event) => {
         // Get the pour color data transferred
         const pourColor = event.dataTransfer.getData('text/pourColor');
         if (pourColor) {
             pourAnimationElement.style.backgroundColor = pourColor;
             pourAnimationElement.style.opacity = 1; // Show pour element on drag enter
             pourAnimationElement.style.transition = 'none'; // Disable transition on entry
         }
     });

    testTubeElement.addEventListener('dragleave', (event) => {
        // Check if leaving the tube area completely, not just moving inside
        if (!event.currentTarget.contains(event.relatedTarget)) {
             event.currentTarget.classList.remove('drag-over');
             // Hide pour element
             pourAnimationElement.style.opacity = 0;
             pourAnimationElement.style.transition = 'opacity 0.3s ease'; // Add fade out transition
        }
    });

    testTubeElement.addEventListener('drop', (event) => {
        event.preventDefault();
        event.currentTarget.classList.remove('drag-over');

        // Hide pour element immediately or with a quick fade
        pourAnimationElement.style.opacity = 0;
        pourAnimationElement.style.transition = 'opacity 0.1s ease'; // Quick fade out

        const phValue = parseFloat(event.dataTransfer.getData('text/plain'));
        if (!isNaN(phValue)) {
            // Trigger the pour animation CSS class
            testTubeContainer.classList.add('pouring');
             // Reset pour element position/style after animation
             setTimeout(() => {
                 testTubeContainer.classList.remove('pouring');
                 pourAnimationElement.style.transform = 'translate(-50%, 0)'; // Reset position
             }, 600); // Match CSS animation duration

            // Update displays with a slight delay to sync with pour animation
            setTimeout(() => {
                updateDisplay(phValue);
            }, 200); // Small delay
        }
    });

     // Reset pour element if drag ends outside dropzone
     document.body.addEventListener('dragend', () => {
         testTubeElement.classList.remove('drag-over');
         pourAnimationElement.style.opacity = 0;
         pourAnimationElement.style.transition = 'opacity 0.3s ease';
     });


    // --- Update Display Function ---
    function updateDisplay(ph) {
        const clampedPH = Math.max(0, Math.min(14, ph));
        const currentPH = parseFloat(digitalPH.textContent);

        // Animate Digital Display
        animateNumber(currentPH, clampedPH, digitalPH, 800); // Animate over 800ms

        // Get Target Color
        const targetColor = getIndicatorColor(clampedPH);

        // Animate Liquid Color and Indicator Strip Color
        // CSS transitions handle the smooth change due to the transition property in CSS
        testTubeLiquid.style.backgroundColor = targetColor;
        colorIndicator.style.backgroundColor = targetColor;

        // Animate Scale Pointer Position
        const scaleWidth = phScaleElement.offsetWidth;
        const pointerWidth = scalePointer.offsetWidth; // Get actual pointer width
        // Calculate pixel position: pH 0 is at 0px, pH 14 is at scaleWidth px
        const pointerPositionPx = (clampedPH / 14) * scaleWidth;
        // Adjust position so the center of the pointer aligns with the correct pH point
        const centeredPositionPx = pointerPositionPx - (pointerWidth / 2);
        scalePointer.style.left = `${centeredPositionPx}px`;
    }

    // Helper function to map pH to a distinct color (simulated universal indicator ranges)
    function getIndicatorColor(ph) {
        if (ph < 1) return '#E74C3C'; // Red (Strong Acid)
        if (ph < 3) return '#E67E22'; // Orange (Acid)
        if (ph < 6) return '#F1C40F'; // Yellow (Weak Acid)
        if (ph < 8) return '#2ECC40'; // Green (Neutral)
        if (ph < 10) return '#3498DB'; // Blue (Weak Base)
        if (ph < 12) return '#9B59B6'; // Indigo (Base)
        return '#8E44AD'; // Violet/Purple (Strong Base)
    }


    // Helper function for smooth number animation
    function animateNumber(start, end, element, duration) {
        let startTime = null;
        const range = end - start;
        const startValue = start;

        function step(timestamp) {
            if (!startTime) startTime = timestamp;
            const elapsed = timestamp - startTime;
            const progress = Math.min(elapsed / duration, 1);

            const currentValue = startValue + range * progress;
            element.textContent = currentValue.toFixed(1);

            if (progress < 1) {
                requestAnimationFrame(step);
            }
        }

        requestAnimationFrame(step);
    }


    // --- Explanation Toggle Logic ---
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        if (isHidden) {
            explanationDiv.style.display = 'block';
            toggleButton.textContent = 'הסתר הסבר על סולם pH';
        } else {
            explanationDiv.style.display = 'none';
            toggleButton.textContent = 'הצג/הסתר הסבר על סולם pH';
        }
    });

    // Initial state: Set to pH 7 (water)
    // Use a slight delay for initial setup to ensure CSS is loaded
    setTimeout(() => {
        updateDisplay(7.0);
         // Set initial liquid color to neutral green without transition
        const neutralColor = getIndicatorColor(7.0);
        testTubeLiquid.style.transition = 'none';
        colorIndicator.style.transition = 'none';
        testTubeLiquid.style.backgroundColor = neutralColor;
        colorIndicator.style.backgroundColor = neutralColor;
        scalePointer.style.transition = 'none';
        updateDisplay(7.0); // Call again to position pointer correctly after transition removed
         // Re-enable transitions
        setTimeout(() => {
             testTubeLiquid.style.transition = 'background-color 0.8s ease-in-out';
             colorIndicator.style.transition = 'background-color 0.8s ease-in-out';
             scalePointer.style.transition = 'left 0.8s ease-in-out';
        }, 50);
    }, 100);


    // Ensure explanation is hidden initially (CSS handles this, but JS double-checks and sets button text)
    explanationDiv.style.display = 'none';
    toggleButton.textContent = 'הצג/הסתר הסבר על סולם pH';

});

</script>
---