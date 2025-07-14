---
title: "בונים היררכיה טיפוגרפית: משחק סידור"
english_slug: typographical-hierarchy-game
category: "עיצוב גרפי"
tags: ["טיפוגרפיה", "היררכיה ויזואלית", "עיצוב כרזה", "אינטראקטיבי", "משחק"]
---
# בונים היררכיה טיפוגרפית: משחק סידור

ברוכים הבאים, מעצבים לעתיד! לפניכם אלמנטים טקסטואליים שנועדו ליצור כרזת אירוע. המשימה שלכם היא לגרור ולסדר אותם באזור הכרזה כך שתיווצר היררכיה ויזואלית ברורה והגיונית. חשבו מהו המידע החשוב ביותר שצריך לקפוץ לעין מיד, ומהם הפרטים התומכים שבאים אחריו.

**גררו את האלמנטים באזור המקווקו כדי לשנות את סדרם.**

<div class="hierarchy-game-container">
  <div id="poster-area" class="poster-area">
    <div class="text-element" data-type="date-time">
      <p>יום חמישי, 23 במאי, 20:00</p>
    </div>
     <div class="text-element" data-type="body">
      <p>הצטרפו אלינו לערב שירה ומוזיקה חגיגי, בהשתתפות אמנים מקומיים. האירוע יתקיים באולם המרכזי ויכלול כיבוד קל.</p>
    </div>
    <div class="text-element" data-type="cta">
      <p>להרשמה ופרטים נוספים בקרו באתר: <a>www.example.com</a></p>
    </div>
    <div class="text-element" data-type="headline">
      <h1>אירוע מיוחד!</h1>
    </div>
    <div class="text-element" data-type="subtitle">
      <h2>ערב שירה ומוזיקה</h2>
    </div>
  </div>
   <div id="feedback-message" class="feedback-message" aria-live="polite"></div>
</div>

<div class="game-controls">
    <button id="check-hierarchy" class="game-button primary-button">בדיקת סידור</button>
    <button id="reset-game" class="game-button secondary-button">אתחול</button>
</div>


<button id="toggle-explanation" class="explanation-button">מהי היררכיה טיפוגרפית? (הסבר)</button>

<div id="explanation" class="explanation hidden">
  <h3>היררכיה טיפוגרפית על קצה המזלג</h3>
  <p>היררכיה טיפוגרפית היא האופן שבו מעצבים מארגנים טקסט כדי להנחות את עין הקורא ולתקשר סדר חשיבות. היא עושה סדר במידע ומאפשרת לסרוק טקסט במהירות ולזהות את הנקודות המרכזיות.</p>
  <p>חושב על זה כמו מפה ויזואלית: הכותרת הראשית היא היעד הגדול, כותרות המשנה הן הערים המרכזיות, וגוף הטקסט הוא הכבישים המקשרים. פרטים נוספים כמו תאריך או קריאה לפעולה הם נקודות עניין ספציפיות.</p>
  <p>באמצעות שינויים כמו גודל גופן, עובי (משקל), רווח בין שורות (לידינג), רווח בין אותיות (קרנינג), ומיקום בעמוד, אנחנו יוצרים שוני ויזואלי שמצביע על חשיבות שונה. ככל שאלמנט בולט יותר, כך מוחנו מזהה אותו כחשוב יותר.</p>
  <p>בכרזה שיצרת, היררכיה יעילה תמשוך את העין תחילה לכותרת הראשית, תמשיך לנושא האירוע, תספק את הפרטים העיקריים, ולבסוף תכלול מידע לוגיסטי וקריאה לפעולה. סידור כזה לא רק נראה טוב, אלא הופך את הכרזה לכלי תקשורת אפקטיבי שמוודא שהמסר עובר בצורה ברורה ובסדר הנכון.</p>
</div>

<style>
  /* General Styles & Colors */
  :root {
    --primary-color: #5a67d8; /* Indigo */
    --primary-dark: #4c5aae;
    --secondary-color: #e2e8f0; /* Light gray */
    --secondary-dark: #cbd5e0;
    --success-color: #48bb78; /* Green */
    --error-color: #f56565; /* Red */
    --text-color-dark: #2d3748; /* Dark gray */
    --text-color-medium: #4a5568; /* Medium gray */
    --text-color-light: #718096; /* Light gray */
    --background-color-light: #f7fafc; /* Very light gray */
    --background-color-card: #ffffff;
    --border-color: #e2e8f0;
    --poster-border-color: #a0aec0; /* Grey border */
  }

  body {
      font-family: 'Arial Hebrew', 'David Libre', sans-serif; /* Modern system fonts + Hebrew */
      line-height: 1.6;
      color: var(--text-color-dark);
      background-color: var(--background-color-light);
      margin: 0;
      padding: 20px;
  }

  h1, h2, h3 {
      color: var(--text-color-dark);
      margin-top: 0;
  }

  a {
      color: var(--primary-color);
      text-decoration: none;
  }
   a:hover {
      text-decoration: underline;
  }

  /* Game Container */
  .hierarchy-game-container {
    display: flex;
    flex-direction: column; /* Stack poster and feedback */
    align-items: center;
    padding: 30px 20px;
    background-color: var(--background-color-light);
    border-radius: 12px;
    box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
    min-height: 500px; /* Ensure enough space */
    position: relative; /* Needed for feedback message positioning */
  }

  /* Poster Area */
  .poster-area {
    width: 100%;
    max-width: 450px; /* Slightly wider */
    min-height: 400px; /* Taller */
    background-color: var(--background-color-card);
    border: 3px dashed var(--poster-border-color); /* Clearer dashed border */
    border-radius: 8px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 12px; /* More space between elements */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
    transition: border-color 0.4s ease-in-out, box-shadow 0.4s ease-in-out; /* Smooth transitions for feedback */
    user-select: none;
  	-webkit-user-select: none;
  	-khtml-user-select: none;
  	-moz-user-select: none;
  	-ms-user-select: none;
  }

  /* Poster Feedback States */
  .poster-area.correct-order {
      border-color: var(--success-color);
      box-shadow: 0 0 20px rgba(72, 187, 120, 0.4); /* Green glow */
  }

   .poster-area.incorrect-order {
      border-color: var(--error-color);
      box-shadow: 0 0 15px rgba(245, 101, 101, 0.4); /* Red glow */
  }


  /* Text Elements (Draggable Items) */
  .text-element {
    background-color: var(--secondary-color);
    border: 1px solid var(--border-color);
    padding: 12px 18px;
    border-radius: 6px;
    cursor: grab;
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out, background-color 0.2s ease-in-out;
    font-family: inherit; /* Inherit from body */
    text-align: center;
    color: var(--text-color-medium);
  }

  /* Typography within elements based on data-type - simulating final look */
  .text-element[data-type="headline"] {
      background-color: #fefcbf; /* Light yellow accent */
      border-color: #faf089;
  }
  .text-element[data-type="headline"] h1 {
      font-size: 2.5em; /* Larger headline */
      margin: 0;
      color: var(--text-color-dark);
      font-weight: 700; /* Bold */
  }

   .text-element[data-type="subtitle"] {
       background-color: #bee3f8; /* Light blue accent */
       border-color: #90cdf4;
   }
   .text-element[data-type="subtitle"] h2 {
      font-size: 1.6em; /* Subtitle size */
       margin: 0;
       color: var(--text-color-medium);
       font-weight: 600;
  }
   .text-element[data-type="body"] {
        background-color: var(--background-color-card); /* White background */
        border-color: var(--border-color);
   }
   .text-element[data-type="body"] p {
      font-size: 1em; /* Body text size */
       margin: 0;
       color: var(--text-color-dark);
       line-height: 1.5;
  }
   .text-element[data-type="date-time"] {
       background-color: #c3dafe; /* Another light blue */
       border-color: #a3bffa;
   }
   .text-element[data-type="date-time"] p {
      font-size: 0.9em; /* Smaller detail text */
       margin: 0;
       color: var(--text-color-medium);
       font-style: italic;
       font-weight: 500;
  }
   .text-element[data-type="cta"] {
       background-color: #b2f5ea; /* Light teal */
       border-color: #81e6d9;
   }
   .text-element[data-type="cta"] p {
      font-size: 1.1em; /* CTA slightly larger */
       margin: 0;
       color: var(--primary-color); /* CTA color */
       font-weight: 700;
  }
  .text-element a {
      color: var(--primary-color);
      text-decoration: none;
  }
   .text-element a:hover {
      text-decoration: underline;
  }


  .text-element:hover {
    background-color: var(--secondary-dark);
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  }

  .text-element:active {
    cursor: grabbing;
    transform: scale(1.03); /* Slight scale up on drag */
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    z-index: 100; /* Bring dragged element to front */
  }

  /* SortableJS ghost class */
  .sortable-ghost {
    opacity: 0.3;
    background-color: var(--poster-border-color);
    border: 2px dashed var(--text-color-light);
    box-shadow: none;
    transform: scale(1); /* Prevent ghost from scaling */
  }

   /* Feedback Message */
   .feedback-message {
        margin-top: 20px;
        padding: 10px 20px;
        border-radius: 6px;
        font-size: 1.1em;
        font-weight: bold;
        text-align: center;
        min-height: 1.5em; /* Reserve space */
        opacity: 0; /* Start hidden */
        transition: opacity 0.3s ease-in-out, background-color 0.3s ease-in-out, color 0.3s ease-in-out;
   }

    .feedback-message.visible {
        opacity: 1;
    }

   .feedback-message.success {
       background-color: var(--success-color);
       color: white;
   }

    .feedback-message.error {
       background-color: var(--error-color);
       color: white;
   }


  /* Game Controls */
  .game-controls {
      display: flex;
      justify-content: center;
      gap: 15px;
      margin-top: 20px;
      margin-bottom: 30px;
  }

  .game-button {
    display: inline-block;
    padding: 12px 25px;
    font-size: 1em;
    font-weight: bold;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease;
    text-align: center;
  }

  .primary-button {
    background-color: var(--primary-color);
    color: white;
  }
   .primary-button:hover {
    background-color: var(--primary-dark);
  }
   .primary-button:active {
       transform: scale(0.98);
   }

  .secondary-button {
    background-color: var(--secondary-color);
    color: var(--text-color-dark);
    border: 1px solid var(--border-color);
  }
   .secondary-button:hover {
    background-color: var(--secondary-dark);
  }
   .secondary-button:active {
       transform: scale(0.98);
   }


  /* Explanation Section */
  .explanation-button {
    display: block;
    margin: 20px auto;
    padding: 10px 20px;
    font-size: 1em;
    color: var(--text-color-medium);
    background-color: transparent;
    border: none;
    text-decoration: underline;
    cursor: pointer;
    transition: color 0.3s ease;
  }

  .explanation-button:hover {
    color: var(--text-color-dark);
  }

  .explanation {
    background-color: #ebf8ff; /* Very light blue */
    border: 1px solid #b8f3ff;
    border-radius: 8px;
    padding: 25px;
    margin-top: 20px;
    line-height: 1.7;
    color: var(--text-color-medium);
    transition: opacity 0.5s ease, max-height 0.5s ease, padding 0.5s ease;
    overflow: hidden;
    max-height: 1000px; /* Sufficiently large for visible state */
    opacity: 1;
  }

  .explanation.hidden {
    max-height: 0;
    opacity: 0;
    padding-top: 0;
    padding-bottom: 0;
    border-top-color: transparent;
    border-bottom-color: transparent;
  }

  .explanation h3 {
    margin-top: 0;
    color: var(--text-color-dark);
    font-size: 1.3em;
  }

  /* Responsive adjustments */
  @media (max-width: 600px) {
      body {
          padding: 15px;
      }
      .poster-area {
          padding: 15px;
          max-width: 100%;
      }
      .text-element {
          padding: 10px 15px;
      }
      .text-element[data-type="headline"] h1 {
          font-size: 2em;
      }
      .text-element[data-type="subtitle"] h2 {
          font-size: 1.4em;
      }
      .game-controls {
          flex-direction: column;
          gap: 10px;
      }
  }
</style>

<script>
  // Assume SortableJS is available globally.
  // A production environment would load it like:
  // <script src="https://cdnjs.cloudflare.com/ajax/libs/Sortable/1.14.0/Sortable.min.js"></script>

  document.addEventListener('DOMContentLoaded', (event) => {
    const posterArea = document.getElementById('poster-area');
    const explanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const checkButton = document.getElementById('check-hierarchy');
    const resetButton = document.getElementById('reset-game');
    const feedbackMessage = document.getElementById('feedback-message');

    // Store the initial HTML of the poster area for resetting
    const initialPosterHTML = posterArea.innerHTML;

    // Define the correct order of element types
    const correctOrder = ['headline', 'subtitle', 'body', 'date-time', 'cta'];

    // Initialize SortableJS on the poster area
    let sortableInstance = null; // Variable to hold the Sortable instance

    function initializeSortable() {
        if (typeof Sortable !== 'undefined') {
            sortableInstance = Sortable.create(posterArea, {
                animation: 250, // Smoother animation
                ghostClass: 'sortable-ghost',
                easing: 'cubic-bezier(0.4, 0, 0.2, 1)', // Material Design easing
                handle: '.text-element' // Only drag by the element itself
            });
        } else {
            console.error("SortableJS library not found. Drag-and-drop functionality will not work.");
            posterArea.innerHTML = "<p style='text-align:center; color: red; font-weight: bold;'>שגיאה: ספריית גרירה ושחרור לא נטענה. המשחק לא יעבוד.</p>";
            posterArea.style.border = 'none';
        }
    }

    // Function to check the current hierarchy
    function checkHierarchy() {
        const currentElements = Array.from(posterArea.children);
        const currentOrder = currentElements.map(el => el.dataset.type);

        // Remove previous feedback classes
        posterArea.classList.remove('correct-order', 'incorrect-order');
        feedbackMessage.classList.remove('visible', 'success', 'error');


        if (currentOrder.length !== correctOrder.length) {
             // Should not happen with the current setup, but good for robustness
             feedbackMessage.textContent = 'ודא שכל האלמנטים נמצאים בכרזה.';
             feedbackMessage.classList.add('visible', 'error');
             posterArea.classList.add('incorrect-order');
             return;
        }

        let isCorrect = true;
        for (let i = 0; i < correctOrder.length; i++) {
            if (currentOrder[i] !== correctOrder[i]) {
                isCorrect = false;
                break;
            }
        }

        if (isCorrect) {
            feedbackMessage.textContent = 'מצוין! זו היררכיה ויזואלית ברורה ואפקטיבית.';
            feedbackMessage.classList.add('visible', 'success');
            posterArea.classList.add('correct-order');
             // Optional: Disable dragging after success
             // if (sortableInstance) {
             //     sortableInstance.option("disabled", true);
             // }
        } else {
            feedbackMessage.textContent = 'עוד לא מדויק. נסה/י שוב לחשוב על סדר החשיבות.';
            feedbackMessage.classList.add('visible', 'error');
            posterArea.classList.add('incorrect-order');
             // Optional: Re-enable dragging if it was disabled
             // if (sortableInstance) {
             //     sortableInstance.option("disabled", false);
             // }
        }
    }

    // Function to reset the game
    function resetGame() {
        // Destroy the current Sortable instance before changing DOM
        if (sortableInstance) {
            sortableInstance.destroy();
            sortableInstance = null;
        }

        // Restore initial HTML
        posterArea.innerHTML = initialPosterHTML;

        // Re-initialize SortableJS
        initializeSortable();

        // Clear feedback
        feedbackMessage.textContent = '';
        feedbackMessage.classList.remove('visible', 'success', 'error');
        posterArea.classList.remove('correct-order', 'incorrect-order');

         // Optional: Ensure dragging is enabled after reset
         // if (sortableInstance) {
         //     sortableInstance.option("disabled", false);
         // }

         // Simple animation for reset - fade in elements
         Array.from(posterArea.children).forEach((el, index) => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(10px)';
            setTimeout(() => {
                el.style.transition = 'opacity 0.4s ease-out, transform 0.4s ease-out';
                el.style.opacity = '1';
                el.style.transform = 'translateY(0)';
            }, index * 50); // Stagger the animation
         });
    }

    // Add event listeners
    if (checkButton) {
        checkButton.addEventListener('click', checkHierarchy);
    }
    if (resetButton) {
        resetButton.addEventListener('click', resetGame);
    }


    // Toggle explanation visibility
    if (explanationButton && explanationDiv) {
      explanationButton.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
        if (explanationDiv.classList.contains('hidden')) {
          explanationButton.textContent = 'מהי היררכיה טיפוגרפית? (הסבר)';
        } else {
          explanationButton.textContent = 'הסתר הסבר';
        }
      });

      // Initially hide the explanation
      explanationDiv.classList.add('hidden');
       explanationButton.textContent = 'מהי היררכיה טיפוגרפית? (הסבר)';
    } else {
        console.error("Explanation button or div not found.");
    }

    // Initialize the game on load
    initializeSortable();
     // Perform an initial reset to apply any potential styling/animation side effects
     // and ensure the initial state is consistent.
     // setTimeout(resetGame, 100); // Small delay to ensure DOM is ready and initialHTML is captured

  });
</script>
---