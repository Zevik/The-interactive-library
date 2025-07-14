---
title: "שתי תמונות כמעט זהות... האם תצליחו למצוא את ההבדל היחיד?"
english_slug: two-almost-identical-images-change-blindness-upgraded
category: "כללי"
tags:
  - פסיכולוגיה
  - תפיסה
  - מוח
  - ניסוי
---
# שתי תמונות כמעט זהות... האם תצליחו למצוא את ההבדל היחיד?

מערכת הראייה שלנו פועלת באופן מדהים ויעיל, אך גם היא מוגבלת. לעיתים קרובות אנו 'עיוורים' לשינויים גדולים שמתרחשים לנגד עינינו, במיוחד כשהם מלווים בהפרעה קצרה. בואו נאתגר את המוח ונראה האם תצליחו לזהות את ההבדל בין שתי תמונות המתחלפות במהירות, עם הבזק קצר ביניהן. התנסו בעצמכם וחוו תופעה פסיכולוגית מפתיעה!

**הוראות:** התבוננו היטב בתמונות המתחלפות. כשתחשבו שמצאתם את ההבדל, לחצו עם העכבר (או געו באצבע) על האזור שבו אתם חושבים שהשינוי קורה.

<div class="experiment-area-wrapper">
  <div id="image1" class="image-frame"></div>
  <div id="image2" class="image-frame"></div>
  <div id="difference-marker" class="difference-marker"></div>
  <div id="feedback-message" class="feedback-message">מצאו את ההבדל!</div>
</div>

<div class="controls-area">
  <button id="reveal-button" class="control-button">גלוי את ההבדל עבורי</button>
  <button id="toggle-explanation" class="control-button secondary">הצג הסבר מדעי</button>
</div>


<style>
  :root {
    --primary-color: #008080; /* Teal */
    --secondary-color: #4682B4; /* Steelblue */
    --background-color: #f8f8f8;
    --text-color: #333;
    --border-color: #ddd;
    --success-color: #28a745; /* Green */
    --error-color: #dc3545; /* Red */
  }

  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 20px;
    background-color: var(--background-color);
    color: var(--text-color);
    text-align: center;
    direction: rtl; /* Hebrew direction */
  }

  h1 {
    color: var(--primary-color);
    text-align: center;
    margin-bottom: 15px;
    font-size: 1.8rem;
  }

  p {
    text-align: center;
    max-width: 700px;
    margin: 0 auto 25px auto;
    color: #555;
    font-size: 1rem;
  }

  strong {
      color: var(--primary-color);
  }

  .experiment-area-wrapper {
    position: relative;
    width: 500px; /* Set a fixed size for the experiment area */
    height: 350px; /* Set a fixed size */
    margin: 20px auto;
    border: 3px solid var(--border-color);
    border-radius: 8px;
    overflow: hidden; /* Keep images and marker inside */
    background-color: #fff; /* White background */
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    cursor: crosshair; /* Indicate clickable area */
  }

  .image-frame {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover; /* Cover the area */
    background-position: center; /* Center the image */
    opacity: 0; /* Start hidden, controlled by JS */
    /* Use your actual image URLs below */
    /* Placeholder URLs: */
  }

  #image1 {
      background-image: url('https://cdn.jsdelivr.net/gh/orpatashnik/simple-demos@main/change-blindness/image-a.png');
  }

  #image2 {
      background-image: url('https://cdn.jsdelivr.net/gh/orpatashnik/simple-demos@main/change-blindness/image-b.png');
  }

  .difference-marker {
      position: absolute;
      width: 40px; /* Example size, adjust based on difference */
      height: 40px; /* Example size */
      border: 3px solid var(--success-color); /* Highlight color */
      border-radius: 50%; /* Circular marker */
      pointer-events: none; /* Don't interfere with clicks */
      opacity: 0; /* Start hidden */
      transition: opacity 0.3s ease-in-out;
      box-sizing: border-box; /* Include border in dimensions */
      z-index: 10; /* Ensure it's above images */
      /* Animation for marker */
      animation: pulse 1.5s infinite ease-in-out;
  }

  @keyframes pulse {
      0% { transform: scale(0.9); opacity: 0.7; }
      50% { transform: scale(1.1); opacity: 1; }
      100% { transform: scale(0.9); opacity: 0.7; }
  }

  .feedback-message {
    position: absolute;
    bottom: 15px;
    left: 50%;
    transform: translateX(-50%);
    background-color: rgba(255, 255, 255, 0.85);
    color: var(--text-color);
    padding: 8px 15px;
    border-radius: 5px;
    font-size: 0.9rem;
    min-width: 150px;
    text-align: center;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    z-index: 5; /* Above images, below marker */
  }

  .controls-area {
      margin-top: 20px;
      display: flex;
      justify-content: center;
      gap: 15px; /* Space between buttons */
  }

  .control-button {
    padding: 12px 20px;
    font-size: 1rem;
    cursor: pointer;
    background-color: var(--primary-color);
    color: white;
    border: none;
    border-radius: 5px;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }

  .control-button:hover {
    background-color: var(--secondary-color);
  }

  .control-button:active {
      transform: scale(0.98);
  }

  .control-button.secondary {
      background-color: #e0e0e0;
      color: var(--text-color);
  }

  .control-button.secondary:hover {
      background-color: #d5d5d5;
  }

  #explanation {
    margin-top: 30px;
    padding: 25px;
    background-color: #ffffff; /* White background */
    border-right: 5px solid var(--secondary-color); /* Border on right for RTL */
    text-align: right; /* Align text to the right for Hebrew */
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
    display: none; /* Start hidden */
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
  }

  #explanation h2 {
    margin-top: 0;
    color: var(--primary-color);
    font-size: 1.5rem;
    margin-bottom: 15px;
  }

  #explanation p {
      text-align: right;
      margin-left: 0;
      margin-right: 0;
      margin-bottom: 15px;
  }

  #explanation p:last-child {
      margin-bottom: 0;
  }

</style>

<div id="explanation">
  <h2>הסבר מדעי: עיוורון לשינויים (Change Blindness)</h2>
  <p>
    אם התקשיתם למצוא את ההבדל, אתם לא לבד! התופעה שחוויתם נקראת "עיוורון לשינויים" ומדגימה עיקרון בסיסי אך מפתיע לגבי האופן שבו המוח שלנו תופס את העולם הויזואלי. בניגוד לאינטואיציה, אנחנו לא "מצלמים" את כל הסצנה מול עינינו כל הזמן. הראייה שלנו אינה הקלטה וידאו רציפה ומושלמת.
  </p>
  <p>
    במקום זאת, המערכת הויזואלית מסתמכת במידה רבה על **קשב**. אנו קולטים פרטים באופן מלא רק באזורים שאליהם אנו מפנים את הקשב שלנו באופן אקטיבי. כאשר ישנה הפרעה ויזואלית קצרה (כמו ההבזק הריק בין התמונות בניסוי, או אפילו מצמוץ טבעי), המוח מתקשה מאוד להבחין בשינויים גדולים וברורים שחלו בסצנה, אלא אם כן הקשב היה ממוקד בדיוק באזור שהשתנה בזמן השינוי.
  </p>
  <p>
    ההבזק הקצר מונע ממערכת הראייה להשוות בקלות בין "לפני" ו"אחרי". המוח "ממלא את החסר" ומניח שהעולם נשאר יציב, מבלי להשקיע משאבי עיבוד עצומים בניטור מתמיד של כל פיקסל. תופעה זו ממחישה שהתפיסה שלנו היא בניה פעילה ותלוית קשב, ולא שיקוף פסיבי של המציאות. היא יכולה להסביר מדוע לפעמים אנחנו מפספסים פרטים לכאורה בולטים בסביבה שלנו אם דעתנו מוסחת או קשבנו מופנה למקום אחר.
  </p>
</div>

<script>
  const image1Div = document.getElementById('image1');
  const image2Div = document.getElementById('image2');
  const experimentWrapper = document.querySelector('.experiment-area-wrapper');
  const explainButton = document.getElementById('toggle-explanation');
  const explanationDiv = document.getElementById('explanation');
  const revealButton = document.getElementById('reveal-button');
  const differenceMarker = document.getElementById('difference-marker');
  const feedbackMessage = document.getElementById('feedback-message');

  let cycleTimeoutId = null;
  let experimentActive = true;

  // --- Experiment Timing ---
  const showDuration = 450; // Time each image is displayed (ms)
  const flashDuration = 100; // Time between images (blank flash, ms)
  let currentState = 'showA'; // 'showA', 'flash1', 'showB', 'flash2'

  // --- Difference Area (PLACEHOLDER - ADJUST FOR YOUR IMAGES!) ---
  // This is a rectangle {x, y, width, height} relative to the top-left of the experimentWrapper.
  // You NEED to adjust these coordinates based on the actual location of the difference in your images.
  // Example placeholder: a 40x40px area near the bottom left corner (approx).
  const differenceArea = {
    x: 50, // pixels from left edge
    y: 280, // pixels from top edge
    width: 40,
    height: 40
  };
  // --- END PLACEHOLDER ---


  // --- Core Experiment Cycle ---
  function runExperimentCycle() {
    switch (currentState) {
      case 'showA':
        image1Div.style.opacity = 1;
        image2Div.style.opacity = 0;
        currentState = 'flash1';
        cycleTimeoutId = setTimeout(runExperimentCycle, showDuration);
        break;
      case 'flash1':
        image1Div.style.opacity = 0;
        image2Div.style.opacity = 0;
        currentState = 'showB';
        cycleTimeoutId = setTimeout(runExperimentCycle, flashDuration);
        break;
      case 'showB':
        image1Div.style.opacity = 0;
        image2Div.style.opacity = 1;
        currentState = 'flash2';
        cycleTimeoutId = setTimeout(runExperimentCycle, flashDuration);
        break;
      case 'flash2':
        image1Div.style.opacity = 0;
        image2Div.style.opacity = 0;
        currentState = 'showA'; // Cycle back
        cycleTimeoutId = setTimeout(runExperimentCycle, flashDuration);
        break;
    }
  }

  // --- Experiment Control Functions ---
  function stopExperiment(message = "הניסוי הסתיים.") {
    clearTimeout(cycleTimeoutId);
    experimentActive = false;
    image1Div.style.opacity = 0; // Hide images
    image2Div.style.opacity = 0;
    feedbackMessage.textContent = message;
    experimentWrapper.style.cursor = 'default'; // Change cursor back
  }

  function showDifferenceMarker() {
    // Position and show the marker based on differenceArea
    differenceMarker.style.left = `${differenceArea.x}px`;
    differenceMarker.style.top = `${differenceArea.y}px`;
    differenceMarker.style.width = `${differenceArea.width}px`;
    differenceMarker.style.height = `${differenceArea.height}px`;
    differenceMarker.style.opacity = 1;
  }

  // --- Event Listeners ---

  // Handle clicks on the experiment area
  experimentWrapper.addEventListener('click', (event) => {
    if (!experimentActive) {
      // If experiment is stopped, maybe restart? For now, do nothing.
      // Or perhaps hide marker and message if clicking outside it?
      if (differenceMarker.style.opacity === '1') {
         differenceMarker.style.opacity = 0;
         feedbackMessage.textContent = "נסה שוב!";
         // Optional: Restart experiment
         // experimentActive = true;
         // currentState = 'showA';
         // runExperimentCycle();
         // experimentWrapper.style.cursor = 'crosshair';
      }
      return;
    }

    // Get click coordinates relative to the wrapper
    const clickX = event.offsetX;
    const clickY = event.offsetY;

    // Check if click is within the difference area
    if (clickX >= differenceArea.x && clickX <= differenceArea.x + differenceArea.width &&
        clickY >= differenceArea.y && clickY <= differenceArea.y + differenceArea.height) {

      // Correct click!
      stopExperiment("מצאתם את ההבדל!");
      // Show the image that contains the difference (assuming image2 has it)
      image2Div.style.opacity = 1;
      showDifferenceMarker(); // Highlight the area
      revealButton.textContent = "ההבדל סומן למעלה";
      revealButton.disabled = true; // Disable reveal button
      experimentWrapper.style.cursor = 'default';

    } else {
      // Incorrect click
      feedbackMessage.textContent = "זה לא שם... נסו שוב!";
      // Optional: Add a temporary visual cue for wrong click
      // experimentWrapper.style.border = `3px solid ${getComputedStyle(document.documentElement).getPropertyValue('--error-color')}`;
      // setTimeout(() => { experimentWrapper.style.border = `3px solid var(--border-color)`; }, 500);
    }
  });

  // Toggle Explanation button
  explainButton.addEventListener('click', () => {
    const isHidden = explanationDiv.style.display === 'none';
    explanationDiv.style.display = isHidden ? 'block' : 'none';
    explainButton.textContent = isHidden ? 'הסתר הסבר מדעי' : 'הצג הסבר מדעי';

    // Optional: Stop the experiment when explanation is shown
    // if (!isHidden && experimentActive) {
    //     stopExperiment("הניסוי הופסק. גלוי הסבר.");
    // } else if (isHidden && !experimentActive && feedbackMessage.textContent === "הניסוי הופסק. גלוי הסבר.") {
    //    // Restart experiment if it was stopped specifically for explanation
    //     experimentActive = true;
    //     currentState = 'showA'; // Reset state
    //     runExperimentCycle();
    //     feedbackMessage.textContent = "מצאו את ההבדל!";
    //     differenceMarker.style.opacity = 0; // Hide marker
    //     revealButton.textContent = "גלוי את ההבדל עבורי";
    //     revealButton.disabled = false;
    //     experimentWrapper.style.cursor = 'crosshair';
    // }
  });

  // Reveal Difference button
  revealButton.addEventListener('click', () => {
    if (!experimentActive && feedbackMessage.textContent !== "מצאתם את ההבדל!") {
         // If already revealed or stopped for other reason, don't reveal again
         return;
    }
    stopExperiment("ההבדל גלוי למעלה.");
    // Show the image that contains the difference (assuming image2 has it)
    image2Div.style.opacity = 1;
    showDifferenceMarker(); // Highlight the area
    revealButton.textContent = "ההבדל סומן למעלה";
    revealButton.disabled = true; // Disable reveal button
  });


  // --- Initialization ---
  document.addEventListener('DOMContentLoaded', () => {
      // Start the experiment cycle
      runExperimentCycle();
      // Ensure explanation is hidden and button text is correct initially
      explanationDiv.style.display = 'none';
      explainButton.textContent = 'הצג הסבר מדעי';
      // Ensure marker is hidden
      differenceMarker.style.opacity = 0;
      // Initial feedback message
      feedbackMessage.textContent = "מצאו את ההבדל!";
  });

</script>