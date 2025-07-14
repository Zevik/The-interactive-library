---
title: "אוצרות מהיער: מסע לזיהוי צמחי בר"
english_slug: forest-treasures-journey-to-identifying-wild-plants
category: "מדעי החיים / ביולוגיה"
tags:
  - צמחים אכילים
  - ליקוט
  - צמחי בר
  - זיהוי צמחים
  - הישרדות
---
# אוצרות מהיער: מסע לזיהוי צמחי בר

צא למסע מרתק אל לבו של הטבע הפראי! היער שופע חיים, וצמחים רבים מסתירים בתוכם אוצרות: מזון, מרפא ואף ידע עתיק. אך הטבע טומן בחובו גם סכנות, וצמחים רעילים אורבים בין העלים. האם יש לך את הידע והחושים החדים הנדרשים כדי להבדיל בין אוצר לבין סכנה?

הסימולציה הזו תאתגר אותך לתרגל זיהוי בסיסי. התבונן היטב בצמח המוצג והחלט האם הוא אכיל או רעיל. זכור: זיהוי אמיתי בשדה דורש ליווי מומחה ומגדיר שדה מהימן. טעות כאן היא רק חלק מהלמידה, טעות בשטח עלולה להיות קטלנית. בהצלחה, וחזור בשלום (עם ידע חדש)!

<div class="app-container">
  <div class="progress-score-container">
    <span id="progress">צמח <span id="current-plant-index">1</span> מתוך <span id="total-plants">5</span></span>
    <span id="score">ניקוד: <span id="correct-score">0</span></span>
  </div>
  <div id="plant-image-container">
    <img id="plant-image" src="" alt="תמונת הצמח לזיהוי">
  </div>
  <div class="buttons-container">
    <button id="edible-button" class="game-button edible-button">זה אכיל!</button>
    <button id="poisonous-button" class="game-button poisonous-button">זה רעיל!</button>
  </div>
  <div id="feedback-container" class="feedback-container">
    <div class="feedback-icon"></div>
    <p id="feedback-message" class="feedback-message"></p>
    <p id="plant-details" class="plant-details"></p>
  </div>
  <button id="next-plant-button" class="next-button" style="display: none;">הצמח הבא >></button>
</div>

<style>
  /* Basic Reset & Body Styles (Enhancements) */
  body {
      margin: 0;
      padding: 20px;
      background-color: #e8f5e9; /* Light green/nature inspired */
      color: #333;
      line-height: 1.6;
      font-family: 'Arial', sans-serif; /* Can't use custom fonts without external resources */
  }

  /* CSS Variables for Theme */
  :root {
    --primary-color: #388e3c; /* Deeper green */
    --primary-light: #4caf50; /* Green */
    --primary-dark: #1b5e20; /* Dark green */
    --secondary-color: #fbc02d; /* Yellow/Orange accent */
    --text-color: #333;
    --background-color: #f9f9f9;
    --card-background: #ffffff;
    --border-color: #ccc;
    --success-color: #4caf50;
    --error-color: #f44336;
    --info-color: #03a9f4;
    --next-button-color: #0277bd; /* Darker blue */
  }

  .app-container {
    font-family: inherit;
    max-width: 650px; /* Slightly wider */
    margin: 30px auto; /* More margin */
    padding: 30px; /* More padding */
    border: none; /* Remove border */
    border-radius: 12px; /* More rounded corners */
    background-color: var(--card-background);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* Deeper shadow */
    text-align: center;
    overflow: hidden; /* For image transitions */
    position: relative;
  }

  /* Progress and Score */
  .progress-score-container {
      display: flex;
      justify-content: space-between;
      margin-bottom: 20px;
      font-size: 1em;
      color: var(--primary-dark);
      padding-bottom: 10px;
      border-bottom: 1px dashed var(--border-color);
  }

  #plant-image-container {
      position: relative;
      width: 100%;
      height: 300px; /* Fixed height for better layout */
      margin-bottom: 20px;
      overflow: hidden; /* Hide overflowing parts during transition */
      border-radius: 8px;
      background-color: #eee; /* Placeholder background */
      display: flex; /* Center image */
      align-items: center;
      justify-content: center;
  }

  #plant-image {
    display: block; /* Remove extra space below image */
    max-width: 100%;
    max-height: 100%;
    height: auto;
    border-radius: 8px;
    /* object-fit: contain; */ /* Should be handled by flex centering */
    transition: opacity 0.5s ease-in-out; /* Fade transition */
  }

   #plant-image.fade-out {
       opacity: 0;
   }

    #plant-image.fade-in {
       opacity: 1;
   }


  .buttons-container {
      margin-bottom: 20px;
  }

  .game-button {
    padding: 12px 25px; /* Slightly larger padding */
    margin: 0 10px;
    font-size: 1.1em; /* Slightly larger font */
    cursor: pointer;
    border: none;
    border-radius: 25px; /* Pill shape */
    transition: background-color 0.3s ease, transform 0.1s ease; /* Add transform for press effect */
    font-weight: bold;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }

  .game-button:disabled {
      opacity: 0.6;
      cursor: not-allowed;
      box-shadow: none;
  }


  .edible-button {
    background-color: var(--success-color); /* Green */
    color: white;
  }

  .edible-button:hover:not(:disabled) {
    background-color: var(--primary-dark); /* Darker green */
     transform: translateY(-2px); /* Lift slightly */
  }
   .edible-button:active:not(:disabled) {
     transform: translateY(0); /* Press down */
   }

  .poisonous-button {
    background-color: var(--error-color); /* Red */
    color: white;
  }

  .poisonous-button:hover:not(:disabled) {
    background-color: #c62828; /* Darker red */
     transform: translateY(-2px); /* Lift slightly */
  }
    .poisonous-button:active:not(:disabled) {
     transform: translateY(0); /* Press down */
   }

  .feedback-container {
    margin-top: 20px; /* More margin */
    padding: 15px; /* More padding */
    min-height: 60px; /* Reserve more space */
    border: 2px solid transparent; /* Thicker border */
    border-radius: 8px;
    transition: border-color 0.4s ease, background-color 0.4s ease; /* Smooth transition for color */
    text-align: center;
    position: relative; /* For absolute positioning of icon */
  }

  .feedback-icon {
      position: absolute;
      top: 50%;
      left: 15px;
      transform: translateY(-50%);
      font-size: 2em; /* Larger icon */
      line-height: 1; /* Align vertically */
  }

  .feedback-container.correct {
      border-color: var(--success-color);
      background-color: #e8f5e9; /* Very light green */
  }
  .feedback-container.correct .feedback-icon:before {
      content: '✅'; /* Checkmark emoji */
  }
  .feedback-container.correct .feedback-message {
      color: var(--primary-dark); /* Darker green text */
  }


  .feedback-container.incorrect {
      border-color: var(--error-color);
      background-color: #ffebee; /* Very light red */
       animation: shake 0.5s ease-in-out; /* Shake animation */
  }
   .feedback-container.incorrect .feedback-icon:before {
      content: '❌'; /* X emoji */
  }
   .feedback-container.incorrect .feedback-message {
      color: var(--error-color); /* Red text */
   }

  /* Shake animation for incorrect feedback */
  @keyframes shake {
    0%, 100% { transform: translateX(0); }
    20%, 60% { transform: translateX(-5px); }
    40%, 80% { transform: translateX(5px); }
  }


  .feedback-message {
    font-size: 1.1em; /* Slightly larger */
    font-weight: bold;
    margin: 0 0 10px 30px; /* Adjust margin for icon */
    text-align: center;
  }

  .plant-details {
      margin-top: 10px;
      font-size: 0.95em; /* Slightly larger */
      color: var(--text-color);
      font-style: normal; /* Remove italics */
      min-height: 20px;
      padding-left: 30px; /* Align with message */
  }

  .next-button {
    margin-top: 20px;
    padding: 10px 25px; /* More padding */
    font-size: 1.1em;
    cursor: pointer;
    border: none;
    border-radius: 25px; /* Pill shape */
    background-color: var(--next-button-color); /* Blue */
    color: white;
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-weight: bold;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }

  .next-button:hover {
    background-color: #01579b; /* Darker blue */
     transform: translateY(-2px);
  }
   .next-button:active {
     transform: translateY(0);
   }

  #explanation {
      margin-top: 40px; /* More space */
      border-top: 2px dashed var(--border-color); /* Dashed border */
      padding-top: 30px; /* More padding */
      text-align: initial; /* Align text left */
      background-color: var(--card-background);
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
  }

  #explanation h2 {
      color: var(--primary-dark); /* Deep green for headings */
      margin-top: 25px;
      margin-bottom: 15px;
      border-bottom: 1px solid #eee;
      padding-bottom: 5px;
  }

  #explanation p, #explanation ul, #explanation ol {
      line-height: 1.7; /* More line height */
      margin-bottom: 18px; /* More margin */
      color: var(--text-color);
  }

  #explanation ul, #explanation ol {
      padding-left: 25px;
  }

   #explanation ul li, #explanation ol li {
       margin-bottom: 10px;
   }

   .show-explanation-button {
       display: block;
       width: max-content;
       margin: 30px auto; /* More margin */
       padding: 12px 25px; /* More padding */
       font-size: 1.1em;
       cursor: pointer;
       border: 2px solid var(--next-button-color); /* Blue border */
       border-radius: 25px;
       background-color: transparent; /* Transparent background */
       color: var(--next-button-color); /* Blue text */
       transition: background-color 0.3s ease, color 0.3s ease, transform 0.1s ease;
       font-weight: bold;
   }

   .show-explanation-button:hover {
       background-color: var(--next-button-color);
       color: white;
       transform: translateY(-2px);
       box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
   }
    .show-explanation-button:active {
     transform: translateY(0);
   }

   /* Final state when quiz is complete */
    .app-container.quiz-complete .buttons-container,
    .app-container.quiz-complete #plant-image-container {
        opacity: 0.5; /* Fade out */
        pointer-events: none; /* Disable interaction */
    }


</style>

<button class="show-explanation-button" id="toggle-explanation-button">מידע נוסף על ליקוט צמחי בר</button>

<div id="explanation" style="display: none;">
    <h2>למה כדאי ללמוד על צמחי בר?</h2>
    <p>היכרות עם עולם הצומח הפראי פותחת דלת לעולם של ידע מסורתי, עצמאות והרפתקאות. היא יכולה להיות מצילת חיים במצבי חירום, מקור להעשרת התזונה במזון טרי ומזין, ואף דרך להכיר צמחי מרפא טבעיים. מעבר להיבט המעשי, זוהי גם דרך עמוקה להתחבר מחדש לטבע ולסביבה בה אנו חיים.</p>

    <h2>כללי הזהב לליקוט בטוח ואחראי</h2>
    <p>ליקוט צמחי בר דורש משנה זהירות וכבוד לסביבה. הקפדה על הכללים הבאים היא קריטית:</p>
    <ul>
        <li><strong>זיהוי ברזל:</strong> אסוף רק צמחים שאתה בטוח במאה אחוז בזיהויים. השתמש במספר מקורות: מגדירים מודפסים, אפליקציות אמינות (ככלי עזר בלבד!), ולפחות פעם אחת - ליווי ואישור של מומחה מוסמך.</li>
        <li><strong>ספק = סכנה:</strong> אם יש לך הספק הקל שבקלים, ולו הקטן ביותר, אל תלקט! עדיף לוותר על ארוחה מאשר לסכן את בריאותך.</li>
        <li><strong>סביבה נקייה:</strong> לקט רק ממקומות שאתה יודע שהם נקיים מחומרי הדברה, זיהום תעשייתי, או ביוב. הימנע מליקוט ליד כבישים סואנים, שטחים חקלאיים מרססים או אזורי תעשייה.</li>
        <li><strong>ליקוט בר קיימא:</strong> טבע דומם הוא טבע מת. לקט רק מה שאתה צריך, והשאר מספיק כדי שהצמח יוכל להתאושש ולהתרבות. לעיתים עדיף לקט עלים או פרחים במקום לעקור את כל הצמח. התייחס לטבע בכבוד.</li>
         <li><strong>היכרות עם החוק:</strong> זכור שחלק מהצמחים בישראל מוגנים אסורים בליקוט. הכר את הרשימה!</li>
    </ul>

    <h2>מפתחות לזיהוי מדויק</h2>
    <p>כל צמח הוא עולם ומלואו של פרטים. כדי לזהות נכון, הפוך לבלש בוטני! שים לב לפרטים הבאים:</p>
    <ul>
        <li><strong>העלים מספרים סיפור:</strong> צורה (לב, אזמל, מחט, אליפסה, אצבעות?), שוליים (חלקים לגמרי? משוננים כמו מסור? גליים?), סידור על הגבעול (אחד אחרי השני בספירלה? זוגות זה מול זה? קבוצה מסביב לגבעול?), מרקם (חלק, שעיר, דביק, בשרני?).</li>
        <li><strong>הפרחים - כרטיס הביקור:</strong> מספר עלי הכותרת והגביע, צבע, צורה כללית (פעמון, כוכב, צינור?), איך הם מאורגנים (בודדים, אשכול, סוכך?). מועד הפריחה חשוב גם הוא.</li>
        <li><strong>הפירות - הסוף המתוק (או המר!):</strong> האם זה ענבה? בית גלעין? תרמיל? הלקט? אצטרובל? מה הצבע והגודל כשהוא בשל?</li>
        <li><strong>הגבעול והשורש:</strong> האם הגבעול עגול, מרובע, משולש? חלק או שעיר? עשבוני או מעוצה? מה צורת השורש (אגירה, שורשון, קנה שורש)?</li>
        <li><strong>הריח - רמז חשוב:</strong> מעוך בעדינות עלה או פרח ושייף את הריח. לצמחים רבים ריח אופייני שיכול לעזור בזיהוי, ולעיתים גם להזהיר (ריחות לא נעימים יכולים להעיד על רעילות).</li>
        <li><strong>בית הגידול:</strong> היכן הצמח גדל? באדמה לחה ליד נחל? על סלע יבש במדבר? בצל עמוק ביער? בבית גידול ספציפי? סביבת הגידול היא רמז משמעותי.</li>
    </ul>

    <h2>דוגמאות נפוצות בישראל (לצורך המחשה בלבד - **לעולם אל תסתמך על זה לליקוט בשטח!**)</h2>
    <p>הסימולציה משתמשת בדוגמאות כלליות. במציאות, חשוב להכיר צמחים ספציפיים לאזור מגוריך. הנה כמה דוגמאות לצמחים נפוצים בישראל (אכילים ורעילים), תוך הדגשת הצורך בזיהוי ודאי וקבלת סיוע ממומחה:</p>
    <ul>
        <li>**אכילים לדוגמה:** חוביזה, רגלת הגינה, סרפד (לאחר חליטה), חרצית עטורה (עלי כותרת ועלים צעירים), עירית.</li>
        <li>**רעילים לדוגמה:** הרדוף הנחלים, דטורה סוסית, פעמונית גלדנית, פקטוריס (שעלול להיתחלף עם חרצית), רקפת (פקעת רעילה).</li>
    </ul>
    <p><strong>המפתח להצלה:</strong> לימוד ההבדלים הדקים והמכריעים בין צמחים דומים. לעיתים, הבדל קטן בסידור עלים או בצבע עורקי הגבעול יכול להציל חיים.</p>

    <h2>מקרה חירום: חשד להרעלה מצמח</h2>
    <p>זהו מצב מסכן חיים המחייב טיפול רפואי מיידי. אם אדם אכל צמח כלשהו ומופיעים תסמינים חריגים (בחילות, הקאות, סחרחורת, כאבי בטן, קושי בנשימה וכו'): פנה מיד לעזרה רפואית! חייג 101 (מגן דוד אדום) או גש לחדר מיון. אם הדבר אפשרי ובטוח, נסה לצלם את הצמח או לקחת דגימה ממנו (עם כפפות, אם קיים חשד לרעילות מגע) כדי לסייע לצוות הרפואי בזיהוי.</p>

    <h2>צעדים נוספים להעמקת הידע</h2>
    <p>סימולציה זו היא רק נקודת פתיחה. כדי לרכוש מיומנות אמיתית, מומלץ בחום:</p>
    <ul>
        <li>להשתמש במגדירי שדה בוטניים מודפסים או באפליקציות (בזהירות ותוך הצלבת מידע).</li>
        <li>להצטרף לקורסים וסיורים מודרכים על ידי מלקטים ובוטנאים מוסמכים.</li>
        <li>לקרוא ספרים ומאמרים אמינים בנושא צמחי בר אכילים ורעילים בישראל.</li>
        <li>לתרגל זיהוי בשדה, אך רק עם מומחה ולעולם לא ללקט ולאכול ללא זיהוי ודאי לחלוטין.</li>
    </ul>
    <p>מסע הלימוד מרתק ואינסופי. הידע נמצא שם בחוץ, ביער ובשדה. כל שנותר הוא לצאת ולגלות אותו בזהירות ובכבוד.</p>
</div>


<script>
  const plants = [
    {
      image: "https://via.placeholder.com/500x300?text=Mystery+Plant+1", // Placeholder image
      isEdible: true,
      correctFeedback: "מצוין! זיהית נכון! זהו אכן צמח אכיל.",
      incorrectFeedback: "אופס! זו טעות בזיהוי. צמח זה עלול להיות רעיל או לא-אכיל. יש לנקוט במשנה זהירות!",
      details: "שימו לב למאפיינים הייחודיים שלו: צורת העלים השעירים, סידורם על הגבעול, והאופן בו הוא גדל בקבוצות צפופות.",
      name: "צמח דוגמה א'"
    },
    {
      image: "https://via.placeholder.com/500x300?text=Mystery+Plant+2+-+Poisonous", // Placeholder image
      isEdible: false,
      correctFeedback: "נכון מאוד! צדקת שהצמח אינו אכיל. זיהוי נכון של צמחים רעילים הוא קריטי!",
      incorrectFeedback: "טעות קריטית! צמח זה רעיל מאוד! טעות בזיהוי בשטח עלולה להיות מסוכנת ביותר.",
      details: "למרות דמיונו לצמח אכיל נפוץ, שימו לב להבדלים הדקים: לרוב יש לו כתמים אדומים על הגבעול וריח אדמתי חזק שאינו אופייני לצמח האכיל הדומה.",
      name: "צמח דוגמה ב'"
    },
     {
      image: "https://via.placeholder.com/500x300?text=Mystery+Plant+3", // Placeholder image
      isEdible: true,
      correctFeedback: "מעולה! זיהוי נכון. הצמח הזה הוא אוצר אמיתי מהטבע.",
      incorrectFeedback: "טעות. הצמח הזה אכיל! פיספסת הזדמנות למצוא מזון טרי ובריא, אך חשוב מכך - חייבים לדעת לזהות אותו בבטחה.",
      details: "מאפייניו העיקריים כוללים עלים בשרניים ועסיסיים ופרחים קטנים בצבע מסוים. לרוב גדל בשטחים פתוחים, גינות נטושות ושולי דרכים. הוא בעל ערך תזונתי גבוה.",
      name: "צמח דוגמה ג'"
    },
    {
      image: "https://via.placeholder.com/500x300?text=Mystery+Plant+4+-+Tricky+One", // Placeholder image - Looks similar to Edible 3?
      isEdible: false,
      correctFeedback: "ידעת להיזהר! צדקת, צמח זה רעיל ואין לגעת בו או ללקט אותו.",
      incorrectFeedback: "שגוי, וזו טעות מסוכנת! הצמח הזה רעיל!",
      details: "למרות שהוא דומה חיצונית לצמח אכיל נפוץ (דוגמה ג'), קיימים הבדלים ברורים: עליו דקים יותר וקיימים פסים כהים בבסיסם, והוא חסר את הריר העסיסי של הצמח האכיל.",
      name: "צמח דוגמה ד'"
    },
     {
      image: "https://via.placeholder.com/500x300?text=Mystery+Plant+5", // Placeholder image
      isEdible: true,
      correctFeedback: "פנטסטי! זיהוי מעולה. זהו צמח אכיל ובריא מאוד.",
      incorrectFeedback: "לא נכון. הצמח הזה אכיל ומוכר מזה דורות כירק בר בעל סגולות. חשוב להכיר אותו!",
      details: "צמח זה מאופיין בעלים גדולים יחסית בעלי שפה משוננת וסיביות עדינה. הוא גדל בדרך כלל ליד מקורות מים או בקרקע לחה. שימו לב למבנה הגבעול הייחודי שלו.",
      name: "צמח דוגמה ה'"
    }
  ];

  let currentPlantIndex = 0;
  let correctScore = 0;
  const totalPlants = plants.length;

  const plantImage = document.getElementById('plant-image');
  const edibleButton = document.getElementById('edible-button');
  const poisonousButton = document.getElementById('poisonous-button');
  const feedbackContainer = document.getElementById('feedback-container');
  const feedbackMessage = document.getElementById('feedback-message');
  const plantDetails = document.getElementById('plant-details');
  const nextPlantButton = document.getElementById('next-plant-button');
  const explanationDiv = document.getElementById('explanation');
  const toggleExplanationButton = document.getElementById('toggle-explanation-button');
  const currentPlantIndexSpan = document.getElementById('current-plant-index');
  const totalPlantsSpan = document.getElementById('total-plants');
  const correctScoreSpan = document.getElementById('correct-score');
  const appContainer = document.querySelector('.app-container'); // Get the main container


  // Update score and progress display
  function updateScoreAndProgress() {
    currentPlantIndexSpan.textContent = currentPlantIndex + 1;
    totalPlantsSpan.textContent = totalPlants;
    correctScoreSpan.textContent = correctScore;
  }

  function loadPlant(index) {
    if (index < plants.length) {
      currentPlantIndex = index;
      const currentPlant = plants[currentPlantIndex];

      // Add fade-out class and change image after a short delay
      plantImage.classList.add('fade-out');
      setTimeout(() => {
        plantImage.src = currentPlant.image;
        // Ensure alt text is updated (optional but good practice)
        plantImage.alt = "תמונת " + currentPlant.name;
        // Remove fade-out and add fade-in to start the transition back
        plantImage.classList.remove('fade-out');
        plantImage.classList.add('fade-in');
      }, 300); // Match this duration with CSS transition duration

      // Reset feedback and buttons
      feedbackMessage.textContent = '';
      plantDetails.textContent = '';
      feedbackContainer.classList.remove('correct', 'incorrect');
      feedbackContainer.style.backgroundColor = 'transparent'; // Reset background color
      feedbackContainer.style.borderColor = 'transparent'; // Reset border color
      feedbackContainer.querySelector('.feedback-icon').textContent = ''; // Clear icon


      edibleButton.disabled = false;
      poisonousButton.disabled = false;
      nextPlantButton.style.display = 'none';

      // Ensure buttons are visible (they might be hidden at the end)
      edibleButton.style.display = 'inline-block';
      poisonousButton.style.display = 'inline-block';

      updateScoreAndProgress();

       // Remove fade-in class after transition completes
      plantImage.addEventListener('transitionend', function handler() {
          plantImage.classList.remove('fade-in');
           plantImage.removeEventListener('transitionend', handler);
      });


    } else {
      // Quiz finished
      feedbackMessage.textContent = `סיימת את כל הצמחים! צדקת ב-${correctScore} מתוך ${totalPlants} זיהויים. כל הכבוד!`;
      feedbackMessage.style.color = var(--primary-dark);
      plantDetails.textContent = 'תוצאה מצוינת! המשיכו ללמוד ולתרגל זיהויים עם מקורות מוסמכים.';
      feedbackContainer.classList.remove('correct', 'incorrect');
      feedbackContainer.style.backgroundColor = var(--background-color);
      feedbackContainer.style.borderColor = var(--border-color);
      feedbackContainer.querySelector('.feedback-icon').textContent = '🏆'; // Trophy emoji


      edibleButton.style.display = 'none';
      poisonousButton.style.display = 'none';
      nextPlantButton.style.display = 'none';

      // Optionally, add a class to the container to indicate quiz complete
      appContainer.classList.add('quiz-complete');
    }
  }

  function handleAnswer(isEdibleGuess) {
    const currentPlant = plants[currentPlantIndex];
    const isCorrect = (isEdibleGuess === currentPlant.isEdible);

    // Disable buttons immediately
    edibleButton.disabled = true;
    poisonousButton.disabled = true;

    // Update feedback container class and message
    feedbackContainer.classList.remove('correct', 'incorrect');
    feedbackContainer.classList.add(isCorrect ? 'correct' : 'incorrect');

    if (isCorrect) {
      feedbackMessage.textContent = currentPlant.correctFeedback;
      feedbackContainer.querySelector('.feedback-icon').textContent = '✅'; // Correct icon
      correctScore++; // Increment score
      correctScoreSpan.textContent = correctScore; // Update score display
    } else {
      feedbackMessage.textContent = currentPlant.incorrectFeedback;
       feedbackContainer.querySelector('.feedback-icon').textContent = '❌'; // Incorrect icon
    }

     // Display details after a short delay
     setTimeout(() => {
        plantDetails.textContent = currentPlant.details;
     }, 400); // Delay matches feedback animation


    // Show next button
    nextPlantButton.style.display = 'block';
  }

  // Event Listeners
  edibleButton.addEventListener('click', () => handleAnswer(true));
  poisonousButton.addEventListener('click', () => handleAnswer(false));
  nextPlantButton.addEventListener('click', () => {
      nextPlantButton.style.display = 'none'; // Hide next button immediately on click
      loadPlant(currentPlantIndex + 1);
  });

  toggleExplanationButton.addEventListener('click', () => {
    const isHidden = explanationDiv.style.display === 'none';
    explanationDiv.style.display = isHidden ? 'block' : 'none';
    toggleExplanationButton.textContent = isHidden ? 'הסתר מידע נוסף' : 'מידע נוסף על ליקוט צמחי בר';
  });

  // Initial setup: Load the first plant and set total plants count
  totalPlantsSpan.textContent = totalPlants;
  loadPlant(0);

</script>
```