---
title: "פעימות קצב: מסע אל השפעת חומרים על הלב"
english_slug: variable-beats-how-drugs-affect-the-heart
category: "מדעי החיים / פיזיולוגיה"
tags:
  - סמים
  - לב
  - לחץ דם
  - פיזיולוגיה
  - סימולציה
  - אינטראקטיבי
---
# פעימות קצב: מסע אל השפעת חומרים על הלב

דמיינו את הלב שלכם - משאבה מופלאה הפועמת בקצב אחיד. אבל מה קורה כשאנו מכניסים לגופנו חומרים זרים? איך ייתכן שספל קפה מעלה את הדופק, בעוד כדור שינה מרגיע אותו? וכיצד השינויים האלו משפיעים על לחץ הדם, הכוח שמניע את הדם בוורידים ובעורקים? צאו למסע אינטראקטיבי וגלו בעצמכם את הכוחות הנסתרים המשפיעים על המערכת הקרדיווסקולרית שלכם!

<div id="simulation-container">
    <h2>מעבדת הסימולציה הקרדיווסקולרית</h2>
    <p class="subtitle">בחרו חומר ובדקו את השפעתו המיידית על הלב ולחץ הדם.</p>
    <div class="controls">
        <label for="substance-select">בחרו חומר לניסוי:</label>
        <select id="substance-select">
            <option value="none">מצב מנוחה (ללא השפעה)</option>
            <option value="stimulant">ממריץ (לדוגמה: קפאין, ניקוטין)</option>
            <option value="depressant">מדכא (לדוגמה: אלכוהול, תרופת הרגעה)</option>
        </select>
        <button id="apply-button">הפעל השפעה</button>
         <button id="reset-button" style="display: none;">אפס ניסוי</button>
    </div>
    <div class="display-area">
        <div class="heart-display">
            <div class="heart-icon">❤️</div>
            <p>קצב לב נוכחי: <span id="heart-rate">72</span> פעימות לדקה</p>
        </div>
        <div class="bp-display">
            <p>לחץ דם נוכחי: <span id="blood-pressure-systolic">120</span> / <span id="blood-pressure-diastolic">80</span> ממ"כ</p>
        </div>
    </div>
     <div class="value-indicator" id="indicator">
        <div class="indicator-bar"></div>
    </div>
     <p id="status-message" class="status"></p>
</div>

<style>
:root {
    --color-normal: #4CAF50; /* Green */
    --color-high: #f44336; /* Red */
    --color-low: #2196F3; /* Blue */
    --color-background: #eef2f7; /* Light blue-grey */
    --color-card-background: #ffffff;
    --color-text-primary: #333;
    --color-text-secondary: #555;
    --color-border: #dcdcdc;
    --color-button-primary: #007bff;
    --color-button-primary-hover: #0056b3;
    --color-button-danger: #dc3545;
    --color-button-danger-hover: #c82333;
}


#simulation-container {
    font-family: 'Arial', sans-serif; /* Modern font stack */
    border: 1px solid var(--color-border);
    padding: 30px; /* More padding */
    border-radius: 12px; /* More rounded corners */
    max-width: 650px; /* Slightly wider */
    margin: 20px auto;
    text-align: center;
    background-color: var(--color-background);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    color: var(--color-text-primary);
    position: relative; /* For absolute positioning of elements */
}

#simulation-container h2 {
    color: #0056b3; /* Deeper blue */
    margin-bottom: 10px;
    font-size: 1.8em;
}

.subtitle {
    color: var(--color-text-secondary);
    margin-top: 0;
    margin-bottom: 25px;
    font-size: 1em;
}

.controls {
    margin-bottom: 30px;
    display: flex; /* Use flexbox for layout */
    justify-content: center; /* Center controls */
    align-items: center;
    flex-wrap: wrap; /* Allow wrapping on smaller screens */
}

.controls label {
    margin-right: 15px; /* More space */
    font-weight: bold;
    font-size: 1.1em;
    color: var(--color-text-primary);
    margin-bottom: 10px; /* Space when wrapping */
}

.controls select, .controls button {
    padding: 10px 15px; /* More padding */
    margin: 5px; /* Adjust margin */
    border-radius: 6px; /* More rounded */
    border: 1px solid var(--color-border);
    cursor: pointer;
    font-size: 1em;
    transition: all 0.3s ease; /* Smooth transitions for hover/disabled */
}

.controls select {
    background-color: var(--color-card-background);
    color: var(--color-text-primary);
    min-width: 180px; /* Give select a min-width */
}

.controls button#apply-button {
    background-color: var(--color-button-primary);
    color: white;
    border: none;
}

.controls button#apply-button:hover:not(:disabled) {
    background-color: var(--color-button-primary-hover);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.controls button#reset-button {
    background-color: var(--color-button-danger);
    color: white;
    border: none;
}

.controls button#reset-button:hover:not(:disabled) {
    background-color: var(--color-button-danger-hover);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.controls button:disabled {
    opacity: 0.5; /* Dim disabled buttons */
    cursor: not-allowed;
    box-shadow: none;
}


.display-area {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin-bottom: 30px; /* More space */
    background-color: var(--color-card-background);
    padding: 20px; /* More padding */
    border-radius: 10px; /* More rounded */
    border: 1px solid var(--color-border);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.07); /* Subtle shadow */
    flex-wrap: wrap; /* Allow wrapping */
}

.heart-display, .bp-display {
    flex: 1;
    min-width: 200px; /* Minimum width for display areas */
    padding: 15px;
    border-radius: 8px;
    text-align: center;
    margin: 10px; /* Space between wrapped items */
}


.heart-icon {
    font-size: 4em; /* Larger heart */
    margin-bottom: 8px;
    cursor: pointer; /* Hint that it's interactive (though click doesn't do anything yet) */
     /* Removed direct transition here, animations handle scale */
}

.heart-display p, .bp-display p {
    margin: 5px 0;
    font-size: 1.2em; /* Larger text */
    color: var(--color-text-secondary);
}

#heart-rate, #blood-pressure-systolic, #blood-pressure-diastolic {
    font-weight: bold;
    color: var(--color-text-primary); /* Make values stand out */
}

.value-indicator {
    width: 80%; /* Make indicator wider */
    height: 15px; /* Thicker indicator */
    border-radius: 8px; /* More rounded */
    margin: 15px auto 10px auto; /* Center and add margin */
    background-color: #eee; /* Default grey background */
    overflow: hidden; /* Hide overflowing bar during transition */
    position: relative;
}

.indicator-bar {
    width: 50%; /* Default width, will be set by JS */
    height: 100%;
    background-color: var(--color-normal); /* Default color */
    transition: width 0.8s ease-out, background-color 0.8s ease-out; /* Smooth transition for width and color */
    position: absolute;
    left: 50%; /* Start from center */
    transform: translateX(-50%); /* Pull back by half its width to center */
}

.value-indicator.normal .indicator-bar {
    width: 50%; /* Stays centered */
    background-color: var(--color-normal);
}

.value-indicator.high .indicator-bar {
     width: 80%; /* Expands to the right */
     background-color: var(--color-high);
     left: 50%;
     transform: translateX(-50%); /* Center it */
}

.value-indicator.low .indicator-bar {
    width: 80%; /* Expands to the left */
    background-color: var(--color-low);
     left: 50%;
     transform: translateX(-50%); /* Center it */
}

.status {
    min-height: 1.2em; /* Reserve space */
    color: var(--color-text-secondary);
    font-style: italic;
    margin-top: 10px;
    font-size: 0.9em;
}


/* Animation Definitions - More granular control */
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.08); } /* Slightly more pronounced pulse */
    100% { transform: scale(1); }
}

.heart-icon.pulsing {
    animation-name: pulse;
    animation-timing-function: ease-in-out;
    animation-iteration-count: infinite;
}

/* Animation Durations linked to speed */
.heart-icon[data-pulse-speed="slow"] { animation-duration: 1.2s; }
.heart-icon[data-pulse-speed="normal"] { animation-duration: 0.8s; }
.heart-icon[data-pulse-speed="fast"] { animation-duration: 0.5s; }


/* Explanation styles - Improved */
#explanation {
    margin-top: 40px;
    padding: 25px;
    border: 1px solid var(--color-border);
    border-radius: 10px;
    background-color: #f8f9fa; /* Lighter background for explanation */
    text-align: right;
    line-height: 1.7; /* More comfortable reading */
    color: var(--color-text-primary);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
}

#explanation h3 {
    color: #0056b3;
    margin-top: 20px; /* More space above headers */
    margin-bottom: 10px;
    text-align: right;
    font-size: 1.4em;
    border-bottom: 1px solid #eee; /* Separator line */
    padding-bottom: 5px;
}
#explanation h3:first-child {
     margin-top: 0;
}

#explanation p {
    margin-bottom: 15px;
    text-align: right;
}

#explanation ul {
    list-style-type: disc;
    padding-right: 25px; /* More padding */
    margin-bottom: 15px;
}

#explanation li {
    margin-bottom: 8px;
}

.toggle-explanation-button {
    display: block;
    margin: 30px auto 20px auto; /* More space */
    padding: 12px 20px; /* More padding */
    background-color: var(--color-button-primary);
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.1em; /* Slightly larger font */
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
}

.toggle-explanation-button:hover {
    background-color: var(--color-button-primary-hover);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

</style>

<button class="toggle-explanation-button" id="toggle-explanation">הצג הסבר מעמיק</button>

<div id="explanation" style="display: none;">
    <h3>הסבר מעמיק: השפעת חומרים על מערכת הלב וכלי הדם</h3>

    <h3>מבוא למערכת הקרדיווסקולרית</h3>
    <p>מערכת הדם, או המערכת הקרדיווסקולרית, היא רשת מורכבת של הלב, כלי הדם (עורקים, ורידים, נימים) והדם עצמו. הלב מתפקד כמשאבה מרכזית המזרימה דם עשיר בחמצן וחומרי מזון לכל תאי הגוף, ומובילה דם עשיר בפחמן דו-חמצני ופסולת אל הריאות והכליות. קצב הלב ולחץ הדם מבוקרים בדייקנות על ידי מערכת העצבים האוטונומית ומערכות הורמונליות, המגיבות לצרכי הגוף המשתנים (למשל, במאמץ פיזי או במנוחה).</p>

    <h3>ממריצים מול מדכאים: מלחמת המוליכים העצביים</h3>
    <p>חומרים רבים, בין אם הם תרופות, סמים או אפילו רכיבים במזון ושתייה (כמו קפאין), משפיעים על הגוף באמצעות השפעה על מערכת העצבים - במיוחד על מוליכים עצביים כמו אדרנלין, נוראדרנלין ו-GABA. <strong>ממריצים</strong> מגבירים לרוב את הפעילות של מוליכים עצביים "מעוררים", ויוצרים אפקט של "האצה". <strong>מדכאים</strong>, לעומתם, מגבירים פעילות של מוליכים "מעכבים" או מפחיתים פעילות של מעוררים, ויוצרים אפקט של "האטה".</p>

    <h3>מסלול ההשפעה של ממריצים על הלב ולחץ הדם</h3>
    <p>ממריצים נפוצים (קפאין, ניקוטין, אמפטמינים, קוקאין) פועלים לעיתים קרובות על ידי חיקוי או הגברה של פעילות המערכת הסימפתטית ("מצב חירום"). השפעות אלו כוללות:</p>
    <ul>
        <li><strong>האצת קצב הלב:</strong> המוליכים העצביים נקשרים לקולטנים בלב ומורים לו לפעום מהר יותר וחזק יותר.</li>
        <li><strong>כיווץ כלי דם היקפיים:</strong> בעיקר בעורקים קטנים, מה שמגביר את ההתנגדות הכוללת לזרימת הדם ומעלה את לחץ הדם.</li>
        <li><strong>הגברת עוצמת ההתכווצות של שריר הלב:</strong> בכל פעימה נזרקת כמות גדולה יותר של דם, מה שתורם גם הוא לעליית לחץ הדם.</li>
    </ul>
    <p>שילוב גורמים אלו מביא לעלייה משמעותית הן בקצב הלב והן בלחץ הדם.</p>

    <h3>מסלול ההשפעה של מדכאים על הלב ולחץ הדם</h3>
    <p>מדכאים (אלכוהול, בנזודיאזפינים, אופיאטים) מאטים את הפעילות הכללית של מערכת העצבים. השפעתם על מערכת הלב והדם יכולה לכלול:</p>
     <ul>
        <li><strong>האטת קצב הלב:</strong> דיכוי פעילות המערכת הסימפתטית ולעיתים הגברת פעילות המערכת הפארא-סימפתטית ("מצב מנוחה").</li>
        <li><strong>הרחבת כלי דם:</strong> בעיקר מדכאים מסוימים, המובילה לירידה בהתנגדות לזרימת הדם.</li>
        <li><strong>הפחתת עוצמת ההתכווצות של הלב:</strong> יש מדכאים המשפיעים ישירות על שריר הלב ומחלישים את התכווצותו.</li>
    </ul>
    <p>תוצאת השילוב היא לרוב ירידה בקצב הלב ובלחץ הדם. חשוב לזכור שהשפעות אלו תלויות מאוד בסוג המדכא, המינון ומצב האדם.</p>


    <h3>חומרים יום-יומיים וחומרים מסוכנים: מנעד ההשפעה</h3>
    <ul>
        <li><strong>דוגמאות לממריצים (במינונים שונים):</strong> קפה, תה, שוקולד (קפאין, תאוברומין), סיגריות (ניקוטין), משקאות אנרגיה, תרופות לצינון ואלרגיה מסוימות, וכמובן סמים כמו קוקאין ואמפטמינים.</li>
        <li><strong>דוגמאות למדכאים (במינונים שונים):</strong> אלכוהול, תרופות לשינה והרגעה, תרופות לטיפול ביתר לחץ דם (חוסמי בטא), סמים כמו הרואין ואופיאטים.</li>
    </ul>

    <h3>הסכנות הבריאותיות: מעבר לסימולציה</h3>
    <p>בעוד שהסימולציה מציגה השפעות מיידיות, חשוב לדעת ששימוש כרוני או לרעה בחומרים אלו עלול לגרום לנזקים ארוכי טווח ואף קטלניים:</p>
    <ul>
        <li><strong>נזק ללב:</strong> הגדלה, היחלשות או התקשות של שריר הלב.</li>
        <li><strong>הפרעות קצב חמורות:</strong> כולל פרפור חדרים מסכן חיים.</li>
        <li><strong>מחלות כלי דם:</strong> טרשת עורקים מואצת, יתר לחץ דם כרוני.</li>
        <li><strong>אירועים לבביים חריפים:</strong> התקפי לב ושבץ מוחי, גם בקרב אנשים צעירים.</li>
    </ul>
    <p>הבנת מנגנוני ההשפעה היא צעד ראשון במודעות לסיכונים הכרוכים בשימוש לא מבוקר בחומרים המשפיעים על המערכת הקרדיווסקולרית, בין אם הם חוקיים או לא.</p>
</div>


<script>
document.addEventListener('DOMContentLoaded', () => {
    const heartRateSpan = document.getElementById('heart-rate');
    const bpSystolicSpan = document.getElementById('blood-pressure-systolic');
    const bpDiastolicSpan = document.getElementById('blood-pressure-diastolic');
    const substanceSelect = document.getElementById('substance-select');
    const applyButton = document.getElementById('apply-button');
    const resetButton = document.getElementById('reset-button');
    const indicator = document.getElementById('indicator');
    const indicatorBar = document.querySelector('.indicator-bar');
    const heartIcon = document.querySelector('.heart-icon');
    const statusMessage = document.getElementById('status-message');

    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    let currentHR = 72;
    let currentBPSystolic = 120;
    let currentBPDiastolic = 80;

    const normalHR = 72;
    const normalBPSystolic = 120;
    const normalBPDiastolic = 80;

    // Define target ranges for effects (more realistic variation)
    const effects = {
        stimulant: {
            hr: { min: 15, max: 40 },
            bp_s: { min: 10, max: 25 },
            bp_d: { min: 5, max: 13 }
        },
        depressant: {
            hr: { min: -25, max: -10 }, // Negative for decrease
            bp_s: { min: -15, max: -5 },
            bp_d: { min: -8, max: -3 }
        },
        none: { // Transition targets back to normal
             hr: { min: 0, max: 0 },
            bp_s: { min: 0, max: 0 },
            bp_d: { min: 0, max: 0 }
        }
    };

    let simulationFrame;
    let startTime;
    const animationDuration = 4000; // 4 seconds for transition animation
    let startHR, startBPS, startBPD;
    let targetHR, targetBPS, targetBPD;

    function animate(time) {
        if (!startTime) startTime = time;
        const elapsed = time - startTime;
        const progress = Math.min(elapsed / animationDuration, 1); // Ensure progress doesn't exceed 1

        // Linear interpolation for values during animation
        currentHR = startHR + (targetHR - startHR) * progress;
        currentBPSystolic = startBPS + (targetBPS - startBPS) * progress;
        currentBPDiastolic = startBPD + (targetBPD - startBPD) * progress;

        updateDisplay();

        if (progress < 1) {
            simulationFrame = requestAnimationFrame(animate);
        } else {
            // Animation finished
            currentHR = targetHR; // Snap to final target to prevent floating point issues
            currentBPSystolic = targetBPS;
            currentBPDiastolic = targetBPD;
            updateDisplay(); // Final update

            applyButton.disabled = false;
            substanceSelect.disabled = false;
             const selectedSubstance = substanceSelect.value;
            if (selectedSubstance !== 'none') {
                 resetButton.style.display = 'inline-block';
                 statusMessage.textContent = `השפעת ה${selectedSubstance === 'stimulant' ? 'ממריץ' : 'מדכא'} פעילה.`;
            } else {
                 resetButton.style.display = 'none';
                 statusMessage.textContent = 'מצב מנוחה.';
            }

        }
    }


    function updateDisplay() {
        heartRateSpan.textContent = Math.round(currentHR);
        bpSystolicSpan.textContent = Math.round(currentBPSystolic);
        bpDiastolicSpan.textContent = Math.round(currentBPDiastolic);

        // Update indicator color and width based on deviation from normal
        const hrDiff = currentHR - normalHR;
        const bpDiffCombined = (currentBPSystolic - normalBPSystolic) + (currentBPDiastolic - normalBPDiastolic);

        let indicatorClass = 'normal';
        let indicatorWidth = 50; // %
        let indicatorColor = varFromCSS('--color-normal'); // Default to normal color

        const hrDeviationPercent = Math.abs(hrDiff) / (effects.stimulant.hr.max + 10) * 100; // Scale deviation
        const bpDeviationPercent = Math.abs(bpDiffCombined) / (effects.stimulant.bp_s.max + effects.stimulant.bp_d.max + 10) * 100;

        // Combine deviation for indicator width - use max deviation
        let totalDeviationPercent = Math.max(hrDeviationPercent, bpDeviationPercent);
        totalDeviationPercent = Math.min(totalDeviationPercent, 100); // Cap at 100%

        indicatorWidth = 50 + (totalDeviationPercent / 2); // Base 50% + half of deviation (max 100%)
        if (hrDiff > 5 || bpDiffCombined > 10) {
             indicatorClass = 'high';
             indicatorColor = varFromCSS('--color-high');
        } else if (hrDiff < -5 || bpDiffCombined < -10) {
             indicatorClass = 'low';
             indicatorColor = varFromCSS('--color-low');
        } else {
             indicatorClass = 'normal';
             indicatorColor = varFromCSS('--color-normal');
              indicatorWidth = 50;
        }


        indicator.classList.remove('normal', 'high', 'low');
        indicator.classList.add(indicatorClass);
        // indicatorBar.style.width = `${indicatorWidth}%`; // Width is handled by CSS classes now
        // indicatorBar.style.backgroundColor = indicatorColor; // Color is handled by CSS classes

        // Update heart icon animation speed based on HR
        let pulseSpeed = 'normal';
        if (currentHR > normalHR + 10) {
            pulseSpeed = 'fast';
        } else if (currentHR < normalHR - 10) {
            pulseSpeed = 'slow';
        }
        heartIcon.setAttribute('data-pulse-speed', pulseSpeed);
         heartIcon.classList.add('pulsing'); // Ensure pulsing class is always there
    }

     // Helper function to get CSS variable value
    function varFromCSS(varName) {
        return getComputedStyle(document.documentElement).getPropertyValue(varName).trim();
    }


    function applySubstance(substance) {
        cancelAnimationFrame(simulationFrame); // Stop previous animation

        startHR = currentHR;
        startBPS = currentBPSystolic;
        startBPD = currentBPDiastolic;

        if (substance === 'none') {
            targetHR = normalHR;
            targetBPS = normalBPSystolic;
            targetBPD = normalBPDiastolic;
             statusMessage.textContent = 'חוזר למצב מנוחה...';
        } else {
            const effect = effects[substance];
            // Calculate target values based on random variation within ranges
            targetHR = normalHR + (Math.random() * (effect.hr.max - effect.hr.min) + effect.hr.min);
             if (targetHR < 40) targetHR = 40; // Prevent dangerously low HR

            targetBPS = normalBPSystolic + (Math.random() * (effect.bp_s.max - effect.bp_s.min) + effect.bp_s.min);
             if (targetBPS < 80) targetBPS = 80; // Prevent dangerously low BP

            targetBPD = normalBPDiastolic + (Math.random() * (effect.bp_d.max - effect.bp_d.min) + effect.bp_d.min);
             if (targetBPD < 50) targetBPD = 50; // Prevent dangerously low BP

             statusMessage.textContent = `מפעיל השפעת ${substance === 'stimulant' ? 'ממריץ' : 'מדכא'}...`;
        }


        applyButton.disabled = true;
        substanceSelect.disabled = true;
        resetButton.style.display = 'none'; // Hide reset during transition

        startTime = null; // Reset start time for the new animation
        simulationFrame = requestAnimationFrame(animate); // Start the animation loop
    }

    function resetSimulation() {
       cancelAnimationFrame(simulationFrame); // Stop animation
       currentHR = normalHR;
       currentBPSystolic = normalBPSystolic;
       currentBPDiastolic = normalBPDiastolic;
       updateDisplay();
       substanceSelect.value = 'none';
       applyButton.disabled = false;
       substanceSelect.disabled = false;
       resetButton.style.display = 'none';
       heartIcon.setAttribute('data-pulse-speed', 'normal');
       statusMessage.textContent = 'הסימולציה אופסה. מצב מנוחה.';
    }


    applyButton.addEventListener('click', () => {
        const selectedSubstance = substanceSelect.value;
        applySubstance(selectedSubstance);
    });

    resetButton.addEventListener('click', resetSimulation);

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'הצג הסבר מעמיק';
    });

    // Initial setup
    updateDisplay();
    heartIcon.setAttribute('data-pulse-speed', 'normal'); // Start with normal pulse animation speed
    heartIcon.classList.add('pulsing');
    statusMessage.textContent = 'בחרו חומר והתחילו את הניסוי!';
});
</script>