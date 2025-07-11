---
---
---
title: "דמו: איך המוח מגיב לרמזים נסתרים (הטרמה)"
english_slug: lexical-decision-priming
category: "פסיכולוגיה קוגניטיבית"
tags: [הטרמה, פסיכולוגיה, קוגניציה, ניסויים, תפיסה, שפה, ניסוי קוגניטיבי]
---
# הצצה אל התת-מודע: הדגמת הטרמה קוגניטיבית

האם ידעת שחשיפה קצרה ומודעת-חלקית למידע יכולה להשפיע על מהירות התגובה שלך למידע הבא? בוא נחקור יחד את תופעת ה"הטרמה" המרתקת, שמראה איך רמזים סמויים משפיעים על האופן שבו המוח מעבד מילים. תתכונן לראות את הקוגניציה שלך בפעולה!

<div id="app-container" class="container">
  <div id="stimulus-area" class="stimulus-area">
    <div id="fixation-cross" class="stimulus-item">+</div>
    <div id="prime-display" class="stimulus-item prime-item"></div>
    <div id="target-display" class="stimulus-item target-item"></div>
    <div id="response-signal" class="stimulus-item response-signal">החלטה!</div>
  </div>

  <div id="controls">
    <button id="run-trial-button" class="app-button primary-button">בצע הדגמת הטרמה</button>
  </div>

  <div id="results-area" class="results-area">
    <h3 class="results-title">זמני תגובה צפויים (הדמיה):</h3>
    <div class="results-graph">
      <div class="bar-container">
        <div id="related-rt-bar" class="rt-bar related" style="height: 0;"></div>
        <div class="bar-label">מטרה קשורה למטרימ</div>
      </div>
      <div class="bar-container">
        <div id="unrelated-rt-bar" class="rt-bar unrelated" style="height: 0;"></div>
        <div class="bar-label">מטרה לא קשורה</div>
      </div>
       <div class="bar-container">
        <div id="nonword-rt-bar" class="rt-bar nonword" style="height: 0;"></div>
        <div class="bar-label">לא מילה (Non-word)</div>
      </div>
    </div>
     <div class="rt-values">
        <span id="related-rt-value"></span>
        <span id="unrelated-rt-value"></span>
        <span id="nonword-rt-value"></span>
     </div>
    <p class="explanation-note">זמני התגובה בדמו נועדו להמחיש את האפקט הנצפה במחקרים, אינם מבוססים על תגובת המשתמש.</p>
  </div>
</div>

<div id="explanation-button-container" class="app-button-container">
  <button id="toggle-explanation" class="app-button secondary-button">מה בדיוק קרה כאן? (הסבר)</button>
</div>

<div id="explanation" style="display: none;" class="explanation-box">
  <h2>הסבר: הטרמה קוגניטיבית ומבחן החלטה לקסיקלית</h2>
  <p>הדמו שראית ממחיש את תופעת ה<strong>הטרמה (Priming)</strong> - מנגנון קוגניטיבי שבו חשיפה קצרה לגירוי אחד ("המטרימ" או Prime) משפיעה באופן לא מודע על התגובה שלנו לגירוי הבא אחריו ("המטרה" או Target). זו אחת הדרכים המרתקות שבהן המוח שלנו מעבד מידע אוטומטית.</p>
  <p>אחד הכלים המרכזיים לחקר הטרמה שפה הוא <strong>מבחן החלטה לקסיקלית (Lexical Decision Task)</strong>. במבחן זה, משתתפים רואים במהירות מחרוזות אותיות וצריכים להחליט האם זו מילה אמיתית או צירוף חסר משמעות (כמו "לוגב"). נמדדת המהירות והדיוק של התגובה.</p>
  <p><strong>הטרמה סמנטית:</strong> בדמו התמקדנו בהטרמה סמנטית (קשורה למשמעות). אם המטרימ והמטרה קשורים במשמעות (למשל, רואים לרגע קצר "בית חולים" ואז את המילה "אחות"), המוח כבר "מוכן" בצורה כלשהי למילים קשורות. זה גורם לזמן תגובה מהיר יותר בהחלטה אם "אחות" היא מילה אמיתית, בהשוואה למצב שבו המטרימ היה לא קשור (למשל, "שולחן" -> "אחות").</p>
  <p><strong>איך זה עובד?</strong> תיאוריה פופולרית מסבירה זאת באמצעות מודל הרשת הסמנטית. המילים והמושגים במוח מקושרים ברשתות אסוציאטיביות. כש"בית חולים" מופעל, ההפעלה הזו מתפשטת אוטומטית למושגים קרובים כמו "רופא", "אחות", "חולה". כשהמטרה "אחות" מופיעה, הצומת שלה ברשת כבר קיבל "הפעלה מוקדמת", ולכן דרוש פחות זמן או מאמץ להפעיל אותה באופן מלא ולהגיע להחלטה "זו מילה!".</p>
  <p><strong>בסימולציה:</strong></p>
  <ul>
    <li><strong>מטרה קשורה למטרימ:</strong> מדמה מצב של הטרמה סמנטית חיובית (כמו "רופא" -> "אחות"). המוח מעבד את המטרה מהר יותר בזכות ההפעלה המוקדמת מהמטרימ הקשור.</li>
    <li><strong>מטרה לא קשורה:</strong> מדמה מצב שבו המטרימ לא קשור למטרה (כמו "שולחן" -> "אחות"). אין תועלת מההטרמה הקודמת, וזמן התגובה ארוך יותר.</li>
     <li><strong>לא מילה:</strong> מדמה מצב שבו המטרה אינה מילה אמיתית (כמו "חולן"). במקרה כזה, המוח צריך לבדוק את מחרוזת האותיות אל מול אוצר המילים הפנימי שלו. תהליך זה לוקח לרוב יותר זמן מאשר זיהוי מילה אמיתית מוכרת, ללא קשר להטרמה קודמת.</li>
  </ul>
  <p>הדמו ממחיש כיצד ההקשר שבו אנו נחשפים למידע (גם אם לרגע קצר) משפיע באופן אוטומטי ולא מודע על מהירות וקלות עיבוד המידע הבא. זהו כלי חשוב להבנת תהליכי קריאה, זיכרון ותפיסה.</p>
</div>

<style>
/* גלובליים ורקעים */
body {
  font-family: 'Heebo', sans-serif; /* גופן מודרני וידידותי */
  direction: rtl;
  text-align: right;
  line-height: 1.7;
  background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2); /* רקע עדין */
  color: #263238; /* צבע טקסט כהה ונעים */
  padding: 20px;
  margin: 0;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* מיכל ראשי של האפליקציה */
.container {
  background-color: #ffffff;
  padding: 30px;
  border-radius: 15px; /* פינות מעוגלות יותר */
  box-shadow: 0 8px 20px rgba(38, 50, 56, 0.15); /* צל עמוק יותר */
  max-width: 700px; /* רוחב מקסימלי נוח יותר לקריאה */
  margin: 20px auto;
  text-align: center;
  border: 1px solid #e0f7fa; /* גבול עדין */
}

/* כותרות */
h1 {
    color: #00796b; /* צבע כותרת ירוק-כחלחל */
    text-align: center;
    margin-bottom: 20px;
    font-size: 2em;
    font-weight: 700; /* הדגשת כותרת */
}

h2 {
    color: #00796b;
    margin-top: 0;
    font-size: 1.6em;
}

h3 {
    color: #37474f; /* צבע כותרת אזור תוצאות */
    margin-bottom: 20px;
    font-size: 1.3em;
}

/* פסקאות */
p {
    text-align: right;
    margin-bottom: 18px;
    font-size: 1.05em;
    color: #37474f;
}

/* אזור הגירוי (הטרמה ומטרה) */
.stimulus-area {
  min-height: 200px; /* הגדלת גובה האזור */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 40px;
  position: relative;
  background-color: #eceff1; /* רקע בהיר לאזור הגירוי */
  border-radius: 10px;
  overflow: hidden; /* לוודא שהכל בתוך הגבולות */
}

.stimulus-item {
  font-size: 3em; /* הגדלת גודל הפונט */
  font-weight: bold;
  opacity: 0;
  transition: opacity 0.1s ease-in-out, transform 0.1s ease-in-out; /* מעבר מהיר יותר */
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) scale(1); /* התחלה בסקייל רגיל */
  will-change: opacity, transform; /* אופטימיזציה לאנימציה */
}

#fixation-cross {
  font-size: 4em; /* צלב גדול יותר */
  color: #546e7a; /* צבע אפור כהה */
}

.prime-item {
  color: #ff5722; /* צבע כתום אנרגטי למטרימ */
  font-size: 2.5em; /* מעט קטן מהמטרה אולי */
}

.target-item {
  color: #1e88e5; /* צבע כחול בולט למטרה */
  font-size: 3em;
}

.response-signal {
  color: #388e3c; /* צבע ירוק לסיגנל תגובה */
  font-size: 2em;
  opacity: 0; /* התחלה מוסתר */
  transform: translate(-50%, -50%) scale(0.8); /* התחלה מעט קטן */
}

/* אנימציות */
.visible {
  opacity: 1;
  transform: translate(-50%, -50%) scale(1);
}

.flash {
    animation: flash-animation 0.1s ease-in-out forwards; /* אנימציית פלאש */
}

@keyframes flash-animation {
    0% { opacity: 0.8; transform: translate(-50%, -50%) scale(1); }
    50% { opacity: 1; transform: translate(-50%, -50%) scale(1.05); }
    100% { opacity: 0; transform: translate(-50%, -50%) scale(1); }
}

.scale-up-fade-in {
    animation: scale-up-fade-in-animation 0.3s ease-out forwards;
}

@keyframes scale-up-fade-in-animation {
    0% { opacity: 0; transform: translate(-50%, -50%) scale(0.9); }
    100% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
}

/* כפתורים */
#controls {
    text-align: center;
    margin-bottom: 30px;
}

.app-button {
  border: none;
  padding: 14px 30px; /* הגדלת כפתורים */
  font-size: 1.2em;
  border-radius: 8px; /* פינות מעוגלות */
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.1s ease; /* אנימציית לחיצה */
  min-width: 200px; /* רוחב מינימלי לכפתורים */
}

.primary-button {
  background-color: #00bcd4; /* צבע טורקיז ראשי */
  color: white;
}

.primary-button:hover {
  background-color: #00acc1;
}

.primary-button:active {
    transform: scale(0.98); /* אנימציית לחיצה */
}

.secondary-button {
    background-color: #cfd8dc; /* צבע אפור בהיר משני */
    color: #263238;
    border: 1px solid #b0bec5;
}

.secondary-button:hover {
    background-color: #b0bec5;
}

.secondary-button:active {
    transform: scale(0.98);
}

.app-button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
    color: #666666;
    transform: none;
}

.app-button-container {
    text-align: center;
    margin-top: 20px;
}


/* אזור התוצאות */
.results-area {
  margin-top: 40px;
  padding-top: 25px;
  border-top: 1px solid #e0e0e0; /* קו הפרדה עדין */
  text-align: center;
}

.results-graph {
  display: flex;
  justify-content: space-around;
  align-items: flex-end;
  height: 180px; /* הגדלת גובה הגרף */
  border-bottom: 1px solid #b0bec5; /* קו בסיס לגרף */
  padding-bottom: 10px;
  margin-bottom: 15px;
  position: relative; /* למיקום קו בסיס וקווים אופקיים אם נרצה בעתיד */
}

/* קו בסיס לגרף */
.results-graph::before {
    content: '';
    position: absolute;
    bottom: 10px; /* מיושר עם קו הבסיס שמעל */
    left: 0;
    right: 0;
    height: 1px;
    background-color: #b0bec5;
    z-index: 0; /* ודא שהוא מתחת לעמודות */
}


.bar-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 90px; /* רוחב עמודה מותאם */
}

.rt-bar {
  width: 60px; /* רוחב העמודה */
  background-color: #28a745; /* צבע ברירת מחדל (ירוק) */
  transition: height 1.5s ease-out; /* אנימציה איטית וחלקה יותר */
  margin-bottom: 8px;
  border-radius: 5px 5px 0 0; /* פינות עליונות מעוגלות */
  position: relative; /* עבור אנימציית כניסה */
  bottom: 0; /* ודא שהעמודה מתחילה מהקו */
  transform: scaleY(0); /* מתחיל מכווץ לגובה 0 */
  transform-origin: bottom; /* אנימציה צומחת מהתחתית */
  opacity: 0; /* מתחיל מוסתר */
}

/* אנימציית צמיחת עמודות */
.rt-bar.animate {
    transform: scaleY(1);
    opacity: 1;
    transition: height 1.5s ease-out, transform 1.5s ease-out, opacity 0.5s ease-out 1s; /* אנימציה משולבת */
}


.rt-bar.related { background-color: #4caf50; } /* ירוק למטרה קשורה */
.rt-bar.unrelated { background-color: #ff9800; } /* כתום למטרה לא קשורה */
.rt-bar.nonword { background-color: #f44336; } /* אדום ללא מילה */


.bar-label {
    font-size: 0.95em;
    color: #546e7a; /* צבע תווית אפור כהה */
    text-align: center;
    margin-top: 5px;
}

.rt-values {
    display: flex;
    justify-content: space-around;
    width: 100%;
    font-size: 1em;
    color: #37474f;
    font-weight: bold;
    margin-top: 10px;
}

.rt-values span {
    display: block;
    width: 90px; /* רוחב תואם לעמודה */
    text-align: center;
    opacity: 0; /* מתחיל מוסתר */
    transition: opacity 0.5s ease-in-out 1.2s; /* מושהה מעט אחרי אנימציית העמודות */
}
.rt-values span.visible {
    opacity: 1;
}


.explanation-note {
    font-size: 0.85em;
    color: #78909c; /* צבע אפור עדין להערות */
    margin-top: 20px;
    text-align: center;
    padding-top: 15px;
    border-top: 1px dashed #cfd8dc; /* קו מקווקו עדין */
}

/* אזור ההסבר */
.explanation-box {
  background-color: #e1f5fe; /* רקע כחול בהיר */
  padding: 25px;
  border-radius: 12px;
  margin-top: 20px;
  text-align: right;
  border: 1px solid #b3e5fc;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
}

.explanation-box h2 {
  color: #0277bd; /* כחול כהה לכותרת הסבר */
  margin-bottom: 15px;
  padding-bottom: 10px;
  border-bottom: 1px solid #b3e5fc;
}

.explanation-box p {
    color: #37474f;
    margin-bottom: 15px;
}

.explanation-box strong {
    color: #0277bd;
}

.explanation-box ul {
    padding-right: 25px;
    margin-bottom: 15px;
}

.explanation-box li {
    margin-bottom: 10px;
    color: #37474f;
}


/* הוספת גופן Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;700&display=swap');

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const fixationCross = document.getElementById('fixation-cross');
    const primeDisplay = document.getElementById('prime-display');
    const targetDisplay = document.getElementById('target-display');
    const responseSignal = document.getElementById('response-signal');
    const runTrialButton = document.getElementById('run-trial-button');
    const relatedRtBar = document.getElementById('related-rt-bar');
    const unrelatedRtBar = document.getElementById('unrelated-rt-bar');
    const nonwordRtBar = document.getElementById('nonword-rt-bar');
    const relatedRtValue = document.getElementById('related-rt-value');
    const unrelatedRtValue = document.getElementById('unrelated-rt-value');
    const nonwordRtValue = document.getElementById('nonword-rt-value');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const rtValueSpans = document.querySelectorAll('.rt-values span');


    // Simulated RT values (in ms) - demonstrating the effect
    // Values adjusted slightly for visual distinction on graph
    const simulatedRTs = {
        related: 500, // Fastest for related prime
        unrelated: 650, // Slower for unrelated prime
        nonword: 800 // Slowest for non-words
    };

    // Determine max RT for scaling the bars (relative to each other)
    // Adding padding to ensure bars don't touch the top
    const maxRT = Math.max(simulatedRTs.related, simulatedRTs.unrelated, simulatedRTs.nonword) * 1.2;

    function runTrial() {
        // Disable button during trial
        runTrialButton.disabled = true;

        // Hide all stimulus items and previous results
        fixationCross.classList.remove('visible');
        primeDisplay.classList.remove('visible', 'flash');
        targetDisplay.classList.remove('visible', 'scale-up-fade-in');
        responseSignal.classList.remove('visible', 'flash');

        // Reset bar heights and remove animation class
        relatedRtBar.style.height = '0';
        unrelatedRtBar.style.height = '0';
        nonwordRtBar.style.height = '0';
        relatedRtBar.classList.remove('animate');
        unrelatedRtBar.classList.remove('animate');
        nonwordRtBar.classList.remove('animate');


        // Hide text RT values
        rtValueSpans.forEach(span => span.classList.remove('visible'));
        relatedRtValue.textContent = '';
        unrelatedRtValue.textContent = '';
        nonwordRtValue.textContent = '';


        // --- Stimulus Presentation Sequence ---

        // 1. Show Fixation Cross
        fixationCross.classList.add('visible');
        const fixationDuration = 1000; // 1 sec

        setTimeout(() => {
            fixationCross.classList.remove('visible');

            // 2. Flash Prime Area (Abstract representation of prime presentation)
            // Instead of text, just flash the area or a dot conceptually
            // Keeping the primeDisplay element, but maybe no text or just a shape?
            // Let's flash the element itself briefly as a visual cue.
            // primeDisplay.textContent = ''; // No text, just flash
            primeDisplay.classList.add('flash'); // Use the flash animation

            const primeDuration = 50; // Very brief prime exposure (typical in experiments)


            setTimeout(() => {
                primeDisplay.classList.remove('flash');


                // 3. Show Target Area (Abstract representation of target presentation)
                // primeDisplay.textContent = ''; // Clear previous placeholder
                targetDisplay.textContent = ''; // No text for target either, just the area getting focus
                targetDisplay.classList.add('visible', 'scale-up-fade-in'); // Scale up and fade in


                // --- Simulate Decision Time and Response ---
                // We need to simulate the *process* occurring over time
                // This is complex without a real interaction, so we'll simulate the *outcome* timing.

                 // The fastest result (related) shows up conceptually first, then others.
                 // This isn't a real RT, but a sequence to represent the relative times.

                 // Wait a bit after target appears to simulate processing start
                 const processingStartTime = 300; // ms after target appears

                 setTimeout(() => {
                    // Simulate the "Response" moment visually for the fastest case first
                    responseSignal.classList.add('flash'); // Flash 'Decision!'


                    // After the simulated "response", we can transition to showing the *summary* results graph
                    // The graph doesn't show one trial's result, but the *expected outcome* based on the conditions

                    // Wait a moment for the response signal flash
                    setTimeout(() => {
                         responseSignal.classList.remove('flash');
                         targetDisplay.classList.remove('visible', 'scale-up-fade-in'); // Hide target after simulated response


                         // Now display the full simulated results graph showing all conditions
                         displaySimulatedResults(); // Show the bar graph
                         runTrialButton.disabled = false; // Re-enable button

                    }, 500); // Duration of the response signal flash/display

                 }, processingStartTime); // Delay before simulated processing/response starts

            }, primeDuration); // Duration Prime is flashed

        }, fixationDuration); // Duration of Fixation Cross
    }

    function displaySimulatedResults() {
        // Calculate bar heights based on simulated RTs and maxRT
        // Scaling heights relative to a max height for the graph area (e.g., 150px)
        const graphMaxHeight = 160; // Maximum height the bars can reach in the graph area
        const relatedHeight = (simulatedRTs.related / maxRT) * graphMaxHeight;
        const unrelatedHeight = (simulatedRTs.unrelated / maxRT) * graphMaxHeight;
        const nonwordHeight = (simulatedRTs.nonword / maxRT) * graphMaxHeight;

        // Set bar heights (triggers CSS transition via adding 'animate' class)
        // Use a small delay between adding classes to create a staggered animation effect
        setTimeout(() => {
            relatedRtBar.style.height = `${relatedHeight}px`;
            relatedRtBar.classList.add('animate');
        }, 100); // Small delay

        setTimeout(() => {
            unrelatedRtBar.style.height = `${unrelatedHeight}px`;
            unrelatedRtBar.classList.add('animate');
        }, 300); // More delay

        setTimeout(() => {
            nonwordRtBar.style.height = `${nonwordHeight}px`;
            nonwordRtBar.classList.add('animate');
        }, 500); // Even more delay

        // Display RT values after the bar animations have started
        setTimeout(() => {
             relatedRtValue.textContent = `${simulatedRTs.related}ms`;
             unrelatedRtValue.textContent = `${simulatedRTs.unrelated}ms`;
             nonwordRtValue.textContent = `${simulatedRTs.nonword}ms`;
             rtValueSpans.forEach(span => span.classList.add('visible')); // Make values visible
        }, 1500); // Delay adjusted to appear roughly after bars have grown

    }

    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מורחב' : 'מה בדיוק קרה כאן? (הסבר)';
        // Scroll to the explanation if showing it
        if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }

    // Event Listeners
    runTrialButton.addEventListener('click', runTrial);
    toggleExplanationButton.addEventListener('click', toggleExplanation);

    // Initial state: Hide stimulus items and results
    fixationCross.classList.remove('visible');
    primeDisplay.classList.remove('visible');
    targetDisplay.classList.remove('visible');
    responseSignal.classList.remove('visible');

    // Initial state: Reset bars and values
    relatedRtBar.style.height = '0';
    unrelatedRtBar.style.height = '0';
    nonwordRtBar.style.height = '0';
     rtValueSpans.forEach(span => span.classList.remove('visible'));
    relatedRtValue.textContent = '';
    unrelatedRtValue.textContent = '';
    nonwordRtValue.textContent = '';

});
</script>
---