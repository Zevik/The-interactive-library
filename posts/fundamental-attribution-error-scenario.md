---
title: "טעות הייחוס הבסיסית: האם אנחנו באמת מבינים למה אנשים עושים את מה שהם עושים?"
english_slug: fundamental-attribution-error-scenario
category: "פסיכולוגיה"
tags:
  - פסיכולוגיה חברתית
  - הטיות קוגניטיביות
  - טעות ייחוס בסיסית
---
# חקר הייחוס: למה אנשים מתנהגים כמו שהם מתנהגים?

האם אי פעם מצאתם את עצמכם שופטים במהירות מישהו על סמך התנהגות יחידה? המוח האנושי הוא מכונה לייחוס סיבות, אך האם אנחנו תמיד מצליחים להבחין בין מי הוא האדם לבין מה קורה לו? בואו נצלול לעומק...

<div id="fae-app">
  <h2>תרחיש חברתי: איפה דני?</h2>
  <p>דמיינו את הסיטואציה הבאה: אתם יושבים בכיתה, מוכנים לשיעור, ולפתע דני מגיח באיחור ניכר. הוא נראה נסער, נכנס בבהלה, אין לו את הספר או המחברת הרלוונטיים והוא מתיישב בפינה אחורית מבלי ליצור קשר עין או להשתתף.</p>

  <p><strong>לפני שאתם ממשיכים, עצרו רגע וחשבו: מה הסיבה *הסבירה ביותר* לדעתכם להתנהגותו של דני?</strong></p>

  <div class="attribution-controls">
    <label for="disposition-slider">עד כמה אתם מייחסים את ההתנהגות ל...?</label>
    <input type="range" id="disposition-slider" min="0" max="100" value="50">
    <span class="percent-display"><span id="disposition-percent">50</span>%</span>
  </div>
    <div class="slider-labels">
        <span>תכונות פנימיות<br>(הוא כזה...)</span>
        <span>נסיבות חיצוניות<br>(משהו קרה לו...)</span>
    </div>

  <div class="attribution-viz">
    <div class="viz-bar">
      <div id="disposition-segment" class="segment disposition-color"></div>
      <div id="situation-segment" class="segment situation-color"></div>
    </div>
    <div class="viz-labels">
      <span class="viz-label disposition-color">פנימי: <span id="viz-disposition-percent">50</span>%</span>
      <span class="viz-label situation-color">חיצוני: <span id="viz-situation-percent">50</span>%</span>
    </div>
  </div>

  <p>השתמשו במחוון למעלה כדי לבטא את התחושה שלכם: עד כמה אתם מאמינים שהתנהגותו (האיחור, חוסר ההכנה, חוסר הקשב) נובעת מתכונות האופי והאישיות של דני (למשל, הוא לא אכפתי, עצלן, לא רציני) לעומת גורמים ומצבים חיצוניים שקרו לו (למשל, אוטובוס התקלקל, הייתה לו בעיה משפחתית בבוקר, הוא חלה פתאום)? כשתזיזו את המחוון, החלוקה בין הסיבות הפנימיות לחיצוניות תתעדכן אוטומטית.</p>

</div>

<button id="show-explanation">גלו את ההסבר הפסיכולוגי מאחורי זה</button>

<div id="explanation" class="hidden">
  <h2>הכירו את טעות הייחוס הבסיסית (Fundamental Attribution Error - FAE)</h2>
  <p>התרחיש שחוויתם ממחיש עיקרון יסודי בפסיכולוגיה חברתית שנקרא טעות הייחוס הבסיסית. זוהי נטייה אנושית נפוצה לייחס את ההתנהגות של *אחרים* בעיקר לגורמים פנימיים (אישיות, אופי, תכונות) תוך שאנחנו מזלזלים או מתעלמים לחלוטין מהשפעתם האדירה של גורמים חיצוניים ומצביים (הקשר, נסיבות, אירועים שקרו). במילים אחרות, אנחנו נוטים לחשוב שמישהו הוא *כזה* (עצלן, לא אכפתי, אדיב, נדיב) כי זו האישיות שלו, במקום לחשוב שייתכן שהתנהגותו מושפעת במידה רבה ממה שקורה *לו* באותו הרגע או באותו ההקשר.</p>
  <p>במקרה של דני, הנטייה המיידית והאוטומטית עשויה להיות לחשוב "איזה תלמיד לא רציני!" או "הוא בטח סתם עצלן". האפליקציה האינטראקטיבית אפשרה לכם "לשחק" עם הייחוס הזה ולראות איך התמונה משתנה כשמביאים בחשבון גם את הסיבות המצביות. למעשה, לעיתים קרובות אין לנו את כל המידע על הנסיבות החיצוניות, ולכן קל מאוד ליפול למלכודת הזו ולשפוט אחרים בחומרה יתרה.</p>
  <p>המודעות לטעות הייחוס הבסיסית היא צעד חשוב לפיתוח אמפתיה והבנה מעמיקה יותר של העולם החברתי שסביבנו. היא מזכירה לנו שכמעט תמיד יש סיפור שלם מאחורי התנהגות של אדם אחר, ושכדאי לחשוב פעמיים לפני שמסיקים מסקנות נחרצות על האופי שלו.</p>
</div>

<style>
  /* General body and typography */
  body {
    font-family: 'Arial', sans-serif;
    line-height: 1.7; /* Slightly increased line height */
    color: #333;
    margin: 0; /* Reset margin */
    padding: 20px;
    background: linear-gradient(135deg, #f4f7f6, #e0eafc); /* Softer background gradient */
    direction: rtl;
    text-align: right;
    min-height: 100vh; /* Full viewport height */
    box-sizing: border-box; /* Include padding in height */
  }

  h1, h2 {
    color: #5a3e8a; /* Deep Purple */
    text-align: center;
    margin-bottom: 20px;
    font-weight: bold;
  }

  h1 {
      font-size: 2.2em;
      margin-top: 0;
  }

  h2 {
      font-size: 1.8em;
      margin-top: 15px;
  }

  p {
      margin-bottom: 15px;
      font-size: 1.1em;
  }

  strong {
      color: #4a2f72; /* Slightly darker purple */
  }

  /* App Container Styling */
  #fae-app {
    background-color: #fff;
    padding: 30px; /* Increased padding */
    margin: 30px auto; /* Increased margin */
    border-radius: 15px; /* More rounded corners */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* Enhanced shadow */
    max-width: 750px; /* Slightly wider */
    text-align: right;
    border: 1px solid #ddd; /* Subtle border */
    position: relative; /* Needed for potential animations */
  }

  #fae-app h2 {
      margin-top: 0;
      color: #5a3e8a;
  }

  /* Attribution Controls (Slider and Labels) */
  .attribution-controls {
    margin: 25px 0;
    display: flex;
    flex-direction: column; /* Stack elements vertically */
    align-items: flex-start; /* Align items to the right (in RTL) */
    gap: 15px;
  }

  .attribution-controls label {
    font-weight: bold;
    font-size: 1.1em;
    color: #4a2f72;
  }

  .attribution-controls input[type="range"] {
    width: 100%; /* Full width */
    -webkit-appearance: none;
    appearance: none;
    background: #ddd;
    outline: none;
    opacity: 0.9; /* Slightly more opaque */
    transition: opacity .3s ease-in-out;
    height: 10px; /* Thicker slider track */
    border-radius: 5px;
    cursor: pointer;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.1); /* Inner shadow for track */
  }

  .attribution-controls input[type="range"]:hover {
    opacity: 1;
  }

  /* Slider thumb styling */
  .attribution-controls input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 24px; /* Larger thumb */
    height: 24px; /* Larger thumb */
    background: #5a3e8a; /* Deep Purple */
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.25); /* More prominent shadow */
    border: 2px solid #fff; /* White border */
    transition: transform 0.1s ease-in-out; /* Subtle press animation */
  }

  .attribution-controls input[type="range"]::-webkit-slider-thumb:active {
    transform: scale(1.1); /* Scale up when pressed */
  }


  .attribution-controls input[type="range"]::-moz-range-thumb {
    width: 24px; /* Larger thumb */
    height: 24px; /* Larger thumb */
    background: #5a3e8a; /* Deep Purple */
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.25); /* More prominent shadow */
    border: 2px solid #fff; /* White border */
    transition: transform 0.1s ease-in-out; /* Subtle press animation */
  }
   .attribution-controls input[type="range"]::-moz-range-thumb:active {
    transform: scale(1.1); /* Scale up when pressed */
  }


  .percent-display {
    font-weight: bold;
    min-width: 50px; /* Wider space for percent */
    text-align: center; /* Center the percent text */
    color: #5a3e8a; /* Purple color for percent */
    font-size: 1.2em;
  }

  .slider-labels {
      display: flex;
      justify-content: space-between;
      width: 100%;
      font-size: 0.9em;
      color: #555;
      margin-top: -10px; /* Position closer to slider */
      padding: 0 10px; /* Add padding to align with slider track */
      box-sizing: border-box; /* Include padding in width */
      text-align: center;
  }

  .slider-labels span {
      flex: 1; /* Distribute space evenly */
  }

  .slider-labels span:first-child {
      text-align: right; /* Align 'internal' label right in RTL */
  }

   .slider-labels span:last-child {
      text-align: left; /* Align 'external' label left in RTL */
  }


  /* Attribution Visualization */
  .attribution-viz {
    margin-top: 30px;
    padding-top: 20px;
    border-top: 1px dashed #eee; /* Separator line */
    text-align: center;
  }

  .viz-bar {
    width: 100%;
    height: 35px; /* Thicker bar */
    border-radius: 8px; /* More rounded */
    overflow: hidden;
    display: flex;
    margin-bottom: 15px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15); /* Softer bar shadow */
  }

  .segment {
    height: 100%;
    transition: width 0.4s ease-out; /* Smooth transition */
    display: flex; /* Use flex to potentially center text inside if needed later */
    align-items: center;
    justify-content: center; /* Center text if added */
    color: white; /* Text color for segments */
    font-weight: bold;
    font-size: 1em;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.2); /* Text shadow for readability */
  }

  /* Enhanced Color Palette */
  .disposition-color {
    background-color: #c0392b; /* Deep Red (Internal) */
    background: linear-gradient(to left, #e74c3c, #c0392b); /* Gradient for internal */
  }

  .situation-color {
    background-color: #2980b9; /* Steel Blue (External) */
     background: linear-gradient(to right, #3498db, #2980b9); /* Gradient for external */
  }

  .viz-labels {
    display: flex;
    justify-content: space-around;
    font-size: 1em;
    font-weight: bold;
    margin-top: 10px;
  }

  .viz-labels span {
      display: inline-block;
      padding: 8px 15px; /* More padding */
      border-radius: 5px;
      color: white;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Label shadow */
      transition: transform 0.2s ease-in-out; /* Hover effect */
      cursor: help; /* Indicate interaction possible */
  }

  .viz-labels span:hover {
      transform: translateY(-2px); /* Lift effect on hover */
  }

  .viz-labels .disposition-color {
      background-color: #c0392b;
  }

  .viz-labels .situation-color {
      background-color: #2980b9;
  }


  /* Button Styling */
  button {
    display: block;
    margin: 40px auto; /* More vertical margin */
    padding: 12px 25px; /* More padding */
    font-size: 1.1em; /* Larger font */
    color: #fff;
    background-color: #5a3e8a; /* Deep Purple */
    border: none;
    border-radius: 8px; /* More rounded */
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease-in-out; /* Add transform transition */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15); /* Button shadow */
    font-weight: bold;
  }

  button:hover {
    background-color: #4a3172; /* Darker purple */
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2); /* Stronger shadow on hover */
  }

  button:active {
      transform: scale(0.98); /* Subtle press effect */
  }


  /* Explanation Section */
  #explanation {
    background-color: #eef2f7; /* Light blue-gray */
    padding: 25px; /* Increased padding */
    margin: 30px auto;
    border-radius: 15px;
    max-width: 750px; /* Match app width */
    border: 1px solid #d0d8e3; /* Subtle border */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Softer shadow */
    opacity: 0;
    height: 0;
    overflow: hidden;
    transition: opacity 0.6s ease-in-out, height 0.6s ease-in-out, padding 0.6s ease-in-out; /* Smoother transition */
  }

  #explanation.visible {
    opacity: 1;
    height: auto; /* Allow content to define height */
    padding: 25px; /* Ensure padding is applied in visible state */
  }

  #explanation h2 {
      color: #4a3172; /* Darker purple for explanation heading */
      text-align: right; /* Align explanation heading to the right */
      margin-bottom: 15px;
      border-bottom: 2px solid #d0d8e3; /* Separator line */
      padding-bottom: 10px;
  }

  .hidden {
    display: none; /* Keep display none initially */
  }

</style>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const dispositionSlider = document.getElementById('disposition-slider');
    const dispositionPercentSpan = document.getElementById('disposition-percent');
    const dispositionSegment = document.getElementById('disposition-segment');
    const situationSegment = document.getElementById('situation-segment');
    const vizDispositionPercentSpan = document.getElementById('viz-disposition-percent');
    const vizSituationPercentSpan = document.getElementById('viz-situation-percent');
    const showExplanationButton = document.getElementById('show-explanation');
    const explanationDiv = document.getElementById('explanation');

    function updateAttributionViz() {
      const disposition = parseInt(dispositionSlider.value, 10); // Ensure integer
      const situation = 100 - disposition;

      // Update text percentages
      dispositionPercentSpan.textContent = disposition;
      vizDispositionPercentSpan.textContent = disposition;
      vizSituationPercentSpan.textContent = situation;

      // Update bar widths with transition
      dispositionSegment.style.width = disposition + '%';
      situationSegment.style.width = situation + '%';

      // Add subtle class for animation if needed (optional, width transition is key)
      // dispositionSegment.classList.add('segment-animated');
      // situationSegment.classList.add('segment-animated');
      // setTimeout(() => {
      //    dispositionSegment.classList.remove('segment-animated');
      //    situationSegment.classList.remove('segment-animated');
      // }, 500); // Match transition duration
    }

    // Initial visualization update
    updateAttributionViz();

    // Update visualization when slider moves (input event gives smoother live update than change)
    dispositionSlider.addEventListener('input', updateAttributionViz);

    // Show explanation functionality
    showExplanationButton.addEventListener('click', () => {
      if (explanationDiv.classList.contains('hidden')) {
        // Before making visible, ensure it's not hidden by display: none
        explanationDiv.classList.remove('hidden');

        // Force reflow to enable transition from height 0
        void explanationDiv.offsetHeight;

        // Add visible class to trigger opacity/height transition
        explanationDiv.classList.add('visible');

        showExplanationButton.textContent = 'הסתר הסבר';
      } else {
        // Remove visible class to trigger opacity/height transition back to 0
        explanationDiv.classList.remove('visible');

        // After transition completes, add display: none
        // The transition duration is 0.6s, use slightly more for safety
        setTimeout(() => {
            explanationDiv.classList.add('hidden');
        }, 650); // Match CSS transition duration + buffer

        showExplanationButton.textContent = 'גלו את ההסבר הפסיכולוגי מאחורי זה';
      }
    });
  });
</script>