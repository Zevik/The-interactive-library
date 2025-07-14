---
title: "בלשי טבע: זיהוי עקבות בשלג ובבוץ"
english_slug: nature-detectives-identifying-tracks-in-snow-and-mud
category: "מדעי החיים / ביולוגיה"
tags:
  - עקבות בעלי חיים
  - זיהוי עקבות
  - טבע
  - זואולוגיה
  - סימני שדה
---
# בלשי טבע: מי השאיר עקבות?

יצאתם לטייל וגיליתם סימנים מסתוריים על האדמה הבוצית או בשלג הרך? כל עקבה היא כמו רמז קטן בסיפור בלשי מרתק על יצור שחלף כאן רגע לפניכם. האם אתם מוכנים לקבל את האתגר ולפענח את החידה? בואו נצא למסע גילוי!

<div class="app-container">
    <div id="track-image-container" class="image-container">
        <img id="current-track-image" src="" alt="עקבת בעל חיים" class="track-image">
    </div>
    <div id="options-container" class="options-grid">
        <!-- Options buttons will be populated here by JS -->
    </div>
    <div id="feedback-container" class="feedback-box">
        <div id="feedback-text" class="feedback-message"></div>
        <img id="animal-illustration" src="" alt="איור בעל חיים" class="illustration hidden">
    </div>
    <button id="next-track-button" class="next-button hidden">העקבה הבאה מחכה לכם!</button>
</div>

<style>
  /* General Styles */
  body {
    font-family: 'Alef', sans-serif; /* Using a Hebrew-friendly web font if available, else fallback */
    line-height: 1.6;
    direction: rtl;
    text-align: right;
    margin: 0;
    padding: 20px;
    background-color: #e8f5e9; /* Light green, earthy tone */
    color: #333;
  }

  h1 {
      color: #1b5e20; /* Dark green */
      text-align: center;
      margin-bottom: 25px;
  }

  p {
      margin-bottom: 15px;
  }

  /* App Container */
  .app-container {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    margin-bottom: 30px;
    max-width: 650px; /* Slightly wider */
    margin-left: auto;
    margin-right: auto;
    border: 1px solid #dcedc8; /* Light green border */
  }

  /* Image Display */
  .image-container {
      text-align: center;
      margin-bottom: 30px;
      background-color: #f1f8e9; /* Very light green background */
      border-radius: 8px;
      padding: 15px;
      box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
  }

  .track-image {
    max-width: 100%;
    height: auto;
    border-radius: 8px; /* Rounded corners */
    border: 2px solid #a5d6a7; /* Medium green border */
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    transition: transform 0.5s ease-in-out; /* Animation for loading new track */
  }

  .track-image.loading {
      transform: scale(0.95);
      opacity: 0.7;
  }

  /* Options */
  .options-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); /* Slightly wider buttons */
    gap: 15px; /* More space */
    margin-bottom: 25px;
  }

  .option-button {
    background-color: #4caf50; /* Green */
    color: white;
    border: none;
    padding: 12px 20px; /* More padding */
    border-radius: 25px; /* Pill shape */
    cursor: pointer;
    font-size: 1.1em;
    transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transition */
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }

  .option-button:hover:not(:disabled) {
    background-color: #388e3c; /* Darker green */
    transform: translateY(-2px); /* Slight lift effect */
  }

   .option-button:active:not(:disabled) {
    transform: translateY(0);
    box-shadow: 0 1px 2px rgba(0,0,0,0.1);
   }

  .option-button:disabled {
    background-color: #bdbdbd; /* Grey */
    cursor: not-allowed;
    box-shadow: none;
  }

  /* Feedback */
  .feedback-box {
    margin-top: 20px;
    padding: 20px;
    border-radius: 8px;
    min-height: 80px; /* Ensure enough space */
    display: flex; /* Use flexbox for alignment */
    flex-direction: column; /* Stack items vertically */
    align-items: center; /* Center items horizontally */
    justify-content: center; /* Center items vertically */
    text-align: center;
    transition: all 0.5s ease; /* Smooth transition for feedback change */
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }

  .feedback-message {
      font-size: 1.1em;
      font-weight: bold;
      margin-bottom: 10px; /* Space between text and illustration */
  }

  .feedback-box.correct {
    background-color: #d4edda; /* Light green */
    color: #155724; /* Dark green text */
    border: 1px solid #c3e6cb; /* Green border */
  }

  .feedback-box.incorrect {
    background-color: #f8d7da; /* Light red */
    color: #721c24; /* Dark red text */
    border: 1px solid #f5c6cb; /* Red border */
  }

  .illustration {
      max-width: 180px; /* Slightly larger illustration */
      height: auto;
      border-radius: 8px;
      margin-top: 15px; /* More space */
      box-shadow: 0 2px 5px rgba(0,0,0,0.2);
      opacity: 0; /* Start hidden for animation */
      transform: translateY(10px); /* Start slightly below */
      transition: opacity 0.6s ease-out, transform 0.6s ease-out; /* Animation */
  }

  .illustration.visible {
      opacity: 1;
      transform: translateY(0);
  }


  /* Next Button */
  .next-button {
    display: block;
    width: 100%;
    padding: 14px; /* More padding */
    background-color: #1976d2; /* Blue */
    color: white;
    border: none;
    border-radius: 25px; /* Pill shape */
    font-size: 1.2em;
    cursor: pointer;
    margin-top: 25px; /* More space */
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  }

  .next-button:hover:not(:disabled) {
    background-color: #1565c0; /* Darker blue */
    transform: translateY(-2px);
  }

   .next-button:active:not(:disabled) {
    transform: translateY(0);
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
   }

  .hidden {
    display: none;
  }

  /* Explanation Section */
  #toggle-explanation {
      display: block;
      width: 100%;
      padding: 12px;
      background-color: #757575; /* Grey */
      color: white;
      border: none;
      border-radius: 25px;
      font-size: 1.1em;
      cursor: pointer;
      margin-top: 20px;
      transition: background-color 0.3s ease, transform 0.1s ease;
      max-width: 650px;
      margin-left: auto;
      margin-right: auto;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }

  #toggle-explanation:hover {
      background-color: #616161; /* Darker grey */
       transform: translateY(-2px);
  }
   #toggle-explanation:active {
    transform: translateY(0);
    box-shadow: 0 1px 2px rgba(0,0,0,0.1);
   }


  #explanation {
    background-color: #fff9c4; /* Light yellow */
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    margin-top: 20px;
    max-width: 650px;
    margin-left: auto;
    margin-right: auto;
    border: 1px solid #fbc02d; /* Yellow border */
    opacity: 0; /* Start hidden for animation */
    transform: translateY(10px); /* Start slightly below */
    transition: opacity 0.6s ease-out, transform 0.6s ease-out; /* Animation */
  }

  #explanation.visible {
      opacity: 1;
      transform: translateY(0);
  }

  #explanation h2 {
      color: #f57f17; /* Orange-yellow */
      margin-top: 15px;
      margin-bottom: 10px;
      border-bottom: 2px solid #fbc02d; /* Yellow border */
      padding-bottom: 8px;
  }

  #explanation ul {
      list-style: disc;
      padding-right: 25px; /* More padding */
      margin-bottom: 15px;
  }

  #explanation li {
      margin-bottom: 10px; /* More space */
      line-height: 1.8;
  }

  #explanation p {
      margin-bottom: 15px; /* More space */
  }

  /* Responsive Adjustments */
  @media (max-width: 480px) {
      .app-container, #explanation {
          padding: 15px;
      }
      .options-grid {
          grid-template-columns: 1fr; /* Stack buttons on small screens */
      }
      .option-button, .next-button, #toggle-explanation {
          font-size: 1em;
          padding: 10px;
      }
      .feedback-message {
          font-size: 1em;
      }
  }

</style>

<button id="toggle-explanation">רוצים לדעת עוד על פענוח עקבות?</button>

<div id="explanation" class="hidden">
    <h2>מה מספרת לנו עקבה?</h2>
    <p>עקבות הן הרבה יותר מסתם סימנים על הקרקע. הן שפה נסתרת של הטבע, שמגלה לנו סיפורים על היצורים שחיים סביבנו. כל צעד, כל טביעת כף או פרסה, משאירים אחריהם עדות לפעילות שקרתה ממש כאן.</p>

    <h2>אילו סודות מסתתרים בעקבה?</h2>
    <p>פענוח עקבה מאפשר לנו לגלות מגוון דברים מרתקים:</p>
    <ul>
        <li>**מיהו בעל החיים?** זו השאלה הראשונה והכי מרגשת! בעזרת צורת העקבה ומאפייניה הייחודיים, נזהה את היצור שחלף.</li>
        <li>**לאן מיהר? ומה עשה?** דפוס הצעידה (האם הלך לאט, רץ, קפץ?) וכיוון העקבות מספרים לנו על מסלול התנועה והתנהגות בעל החיים. עקבות ריצה נראות שונה מעקבות הליכה!</li>
        <li>**באיזה גודל היה?** עומק וגודל העקבה רומזים על גודלו ומשקלו של היצור.</li>
        <li>**מתי עבר כאן?** מצב העקבה (האם היא טרייה או ישנה, יבשה או מלאה במים) נותן לנו מושג על הזמן שחלף מאז הושארה.</li>
    </ul>

    <h2>מה משפיע על מראה העקבה?</h2>
    <p>עקבה אחת של אותו בעל חיים יכולה להיראות שונה לחלוטין בהתאם לתנאים:</p>
    <ul>
        <li>**המצע:** עקבה בשלג טרי תיראה שונה מעקבה בבוץ עמוק או בחול יבש. מצע רך ולח כמו בוץ נוטה לשמר פרטים רבים.</li>
        <li>**מזג האוויר:** גשם מטשטש, שמש מייבשת, ושלג נמס משנה את צורת העקבה המקורית.</li>
        <li>**מהירות התנועה:** כפי שציינו, הליכה, ריצה או קפיצה יוצרות דפוסי עקבות שונים ואף משפיעות על כמה פרטים נראים (למשל, האם טפרים נראים).</li>
    </ul>

    <h2>איך נזהה? שימו לב לפרטים!</h2>
    <p>כמו בלשים, עלינו להתמקד ברמזים המרכזיים:</p>
    <ul>
        <li>**גודל וצורה כוללת:** האם היא עגולה, ארוכה, מחודדת? מה גודלה ביחס לאצבע או לכף יד?</li>
        <li>**מספר אצבעות/כריות:** כמה אצבעות בולטות? האם יש סימני כריות רגל?</li>
        <li>**טפרים או ציפורניים:** האם רואים את סימני הטפרים? אצל רוב הכלביים כן, אצל חתוליים לרוב לא (הם מחזירים אותם).</li>
        <li>**דפוס הליכה:** איך מונחות הרגליים? בזוגות (קפיצה)? בקו ישר? האם יש סימן של זנב נגרר?</li>
    </ul>

    <h2>הבדלים בין קבוצות נפוצות:</h2>
    <p>הנה כמה כללי אצבע לזיהוי קבוצות בעלי חיים שונות:</p>
    <ul>
        <li>**כלביים (שועלים, כלבים, זאבים):** בדרך כלל 4 אצבעות נראות ועקבות טפרים ברורות. כרית מרכזית גדולה בצורת לב או טיפה הפוכה.</li>
        <li>**חתוליים (חתולי בר, חתולים):** גם 4 אצבעות לרוב, אבל הטפרים אינם נראים (נשלפים רק לצורך טיפוס או תפיסה). כרית מרכזית קטנה ועגולה יותר.</li>
        <li>**מכפילי פרסה (צבאים, יעלים, חזירי בר, כבשים):** העקבה מורכבת משתי "ציפורניים" מחודדות שיוצרות צורת V או U. אצל חזיר בר לעיתים רואים גם את הטלפיים האחוריות הקטנות יותר מאחור.</li>
        <li>**מכרסמים וארנבות:** רגליים קדמיות קטנות, רגליים אחוריות גדולות. דפוס תנועה קופצני אופייני, שבו עקבות הרגליים האחוריות נוחתות לפני הקדמיות ויוצרות מעין "משולש" או קו ישר של שתי עקבות גדולות ושתיים קטנות מאחור.</li>
        <li>**עופות:** מגוון רחב, אך לרוב רואים 3 אצבעות פונות קדימה ואחת אחורה (או שתיים ושתיים אצל חלק כמו ינשופים). אין כריות רגל כמו ליונקים, ולעיתים קו ישר או מתפתל המעיד על דשדוש.</li>
    </ul>
     <p>עכשיו, כשאתם מצוידים בידע הזה, נסו שוב לזהות את העקבות!</p>
</div>

<script>
  const tracks = [
      {
          image: 'https://via.placeholder.com/400x300?text=Fox+Tracks+in+Snow', // Larger image
          options: ['שועל', 'ארנבת', 'סנאי', 'עורב'],
          correct: 'שועל',
          feedbackCorrect: 'כל הכבוד, זיהוי מדויק! זוהי אכן עקבת שועל אופיינית. שימו לב לארבע האצבעות ולסימני הטפרים העדינים, והכרית המרכזית דמוית לב.',
          feedbackIncorrect: 'כמעט! נסו להסתכל שוב על פרטי העקבה: האם אתם רואים טפרים? מה צורת הכרית המרכזית? רמז: זוהי עקבה של בעל חיים ממשפחת הכלביים.',
          illustration: 'https://via.placeholder.com/200x150?text=Fox+Illustration' // Larger illustration
      },
      {
          image: 'https://via.placeholder.com/400x300?text=Boar+Tracks+in+Mud',
          options: ['חזיר בר', 'צבי', 'כלב בית', 'חתול בר'],
          correct: 'חזיר בר',
          feedbackCorrect: 'מעולה! פענוח נכון. זוהי עקבת פרסה שסועה גדולה וכבדה של חזיר בר. לעיתים קרובות נראות נקודות קטנות יותר מאחור - אלו סימני הטלפיים האחוריות.',
          feedbackIncorrect: 'לא מדויק. זוהי עקבה של בעל חיים בעל פרסה שסועה, אך היא גדולה וכבדה יותר מזו של צבי. חשבו איזו חיית בר גדולה מסתובבת עם פרסות כאלה.',
          illustration: 'https://via.placeholder.com/200x150?text=Boar+Illustration'
      },
      {
          image: 'https://via.placeholder.com/400x300?text=Rabbit+Tracks+in+Snow',
          options: ['שועל', 'ארנבת', 'סנאי', 'עורב'],
          correct: 'ארנבת',
          feedbackCorrect: 'נכון מאוד, בלשים צעירים! עקבות אלו, עם הרגליים האחוריות הגדולות שנחתו לפני הקדמיות הקטנות יותר ויוצרות דפוס "קופצני" מיוחד, אופייניות מאוד לארנבות ומכרסמים אחרים בתנועת קפיצה.',
          feedbackIncorrect: 'לא זו התשובה. הסתכלו היטב על דפוס הנחת הכפות: יש כאן שתי עקבות גדולות מלפנים ושתיים קטנות מאחור, בדפוס שמזכיר קפיצה. איזו חיה קטנה מקפצת כך בשלג?',
          illustration: 'https://via.placeholder.com/200x150?text=Rabbit+Illustration'
      },
      {
          image: 'https://via.placeholder.com/400x300?text=Bird+Tracks+in+Snow',
          options: ['שועל', 'חתול בר', 'עורב', 'חזיר בר'],
          correct: 'עורב', // Using 'עורב' as a placeholder for a generic bird track
          feedbackCorrect: 'מעולה! זוהי עקבת עוף. שימו לב למבנה האצבעות הדק וללא סימני כריות רגל אופייניים ליונקים. זה יכול להיות עורב או עוף אחר בגודל דומה.',
          feedbackIncorrect: 'נסו שוב. התבוננו במבנה העקבה: היא מורכבת מאצבעות דקות בלבד, ללא כריות או טפרים בולטים כמו אצל יונקים. איזו קבוצת בעלי חיים משאירה עקבות כאלה?',
          illustration: 'https://via.placeholder.com/200x150?text=Bird+Illustration'
      }
      // Add more tracks here following the same structure
      // {
      //     image: 'URL_TO_IMAGE',
      //     options: ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
      //     correct: 'Correct Option',
      //     feedbackCorrect: 'Great job! [Specific detail about this track]',
      //     feedbackIncorrect: 'Not quite. [Hint about this track]',
      //     illustration: 'URL_TO_ILLUSTRATION'
      // }
  ];

  let currentTrackIndex = 0;
  const trackImage = document.getElementById('current-track-image');
  const optionsContainer = document.getElementById('options-container');
  const feedbackContainer = document.getElementById('feedback-box'); // Changed ID in HTML, update JS
  const feedbackText = document.getElementById('feedback-text');
  const animalIllustration = document.getElementById('animal-illustration');
  const nextTrackButton = document.getElementById('next-track-button');
  const explanationDiv = document.getElementById('explanation');
  const toggleExplanationButton = document.getElementById('toggle-explanation');

  function loadTrack(index) {
      // Check if all tracks are completed
      if (index >= tracks.length) {
          trackImage.src = 'https://via.placeholder.com/400x300?text=מסע+הבלשות+הסתיים!'; // End image
          trackImage.classList.remove('loading'); // Remove loading class
          optionsContainer.innerHTML = ''; // Clear options
          feedbackText.textContent = 'סיימתם את כל העקבות! אתם בלשי טבע מצוינים!';
          feedbackContainer.className = 'feedback-box correct'; // Green box for completion
          animalIllustration.style.display = 'none';
          animalIllustration.classList.remove('visible'); // Hide illustration
          nextTrackButton.classList.add('hidden'); // Hide next button
          return;
      }

      const track = tracks[index];

      // Add loading class for animation
      trackImage.classList.add('loading');
      // Set timeout to allow loading class animation to start before changing src
      setTimeout(() => {
          trackImage.src = track.image;
          // Remove loading class when image is loaded (basic check)
          trackImage.onload = () => {
              trackImage.classList.remove('loading');
          };
      }, 300); // Delay matches CSS transition duration

      optionsContainer.innerHTML = ''; // Clear previous options
      feedbackText.textContent = ''; // Clear previous feedback
      feedbackContainer.className = 'feedback-box'; // Reset class
      animalIllustration.style.display = 'none';
      animalIllustration.classList.remove('visible'); // Hide illustration
      nextTrackButton.classList.add('hidden'); // Hide next button

      // Populate options with shuffled order for replayability (optional but nice touch)
      const shuffledOptions = shuffleArray([...track.options]);
      shuffledOptions.forEach(option => {
          const button = document.createElement('button');
          button.textContent = option;
          button.classList.add('option-button');
          button.addEventListener('click', () => handleAnswer(option, track, button));
          optionsContainer.appendChild(button);
      });
  }

  function shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [array[i], array[j]] = [array[j], array[i]]; // Swap elements
      }
      return array;
  }

  function handleAnswer(selectedOption, track, clickedButton) {
      // Disable all option buttons after selection and apply colors
      optionsContainer.querySelectorAll('.option-button').forEach(button => {
          button.disabled = true;
          if (button.textContent === track.correct) {
              button.style.backgroundColor = '#28a745'; // Green for correct
              button.style.color = 'white'; // Ensure text color is readable
          } else if (button.textContent === selectedOption) {
               button.style.backgroundColor = '#dc3545'; // Red for incorrect chosen option
               button.style.color = 'white'; // Ensure text color is readable
          } else {
              button.style.backgroundColor = '#bdbdbd'; // Grey for other options
          }
      });

      // Show feedback and illustration with delay/animation
      setTimeout(() => {
          animalIllustration.src = track.illustration;
          animalIllustration.style.display = 'block';
          animalIllustration.classList.add('visible'); // Trigger illustration animation

          if (selectedOption === track.correct) {
              feedbackText.textContent = track.feedbackCorrect;
              feedbackContainer.className = 'feedback-box correct';
          } else {
              feedbackText.textContent = track.feedbackIncorrect;
              feedbackContainer.className = 'feedback-box incorrect';
          }

          // Show next track button with delay/animation
          setTimeout(() => {
              nextTrackButton.classList.remove('hidden');
              nextTrackButton.style.opacity = 0; // Start hidden for fade-in
              setTimeout(() => {
                  nextTrackButton.style.opacity = 1; // Fade in
                  nextTrackButton.style.transition = 'opacity 0.5s ease';
              }, 50); // Small delay after display block
          }, 1000); // Show button after 1 second
      }, 500); // Show feedback/illustration after 0.5 seconds
  }

  function moveToNextTrack() {
      // Reset opacity/transition for next button before hiding
      nextTrackButton.style.opacity = 0;
      nextTrackButton.style.transition = 'none';
      nextTrackButton.classList.add('hidden'); // Hide instantly

      currentTrackIndex++;
      loadTrack(currentTrackIndex);
  }

  function toggleExplanation() {
      const isHidden = explanationDiv.classList.contains('hidden');
      if (isHidden) {
          explanationDiv.classList.remove('hidden');
           // Trigger animation
          setTimeout(() => {
             explanationDiv.classList.add('visible');
          }, 50); // Small delay to allow display block
          toggleExplanationButton.textContent = 'הסתר הסבר על עקבות';
      } else {
           explanationDiv.classList.remove('visible');
           // Hide after animation
           setTimeout(() => {
             explanationDiv.classList.add('hidden');
           }, 600); // Matches CSS transition duration
          toggleExplanationButton.textContent = 'רוצים לדעת עוד על פענוח עקבות?';
      }
  }

  // Event listeners
  nextTrackButton.addEventListener('click', moveToNextTrack);
  toggleExplanationButton.addEventListener('click', toggleExplanation);

  // Initialize the first track on page load
  document.addEventListener('DOMContentLoaded', () => {
      loadTrack(currentTrackIndex);
      // Ensure explanation is hidden and button text is correct initially
      explanationDiv.classList.add('hidden');
      explanationDiv.classList.remove('visible'); // Ensure visible class is not present
      toggleExplanationButton.textContent = 'רוצים לדעת עוד על פענוח עקבות?';
  });

</script>
```