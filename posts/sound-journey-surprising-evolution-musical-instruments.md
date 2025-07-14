---
title: "מסע הצליל: האבולוציה המפתיעה של כלי הנגינה"
english_slug: sound-journey-surprising-evolution-musical-instruments
category: "מוזיקה"
tags:
  - כלי נגינה
  - היסטוריה של המוזיקה
  - תזמורת
  - אבולוציה
  - צליל
---
# מסע הצליל: האבולוציה המפתיעה של כלי הנגינה

הצטרפו למסע מרתק בזמן וגלו איך צלילים בסיסיים מהטבע הפכו לכלי הנגינה המופלאים והמורכבים שאנו מכירים היום. זו לא רק היסטוריה - זו אבולוציה של צליל, טכנולוגיה ויצירתיות אנושית. האם תצליחו לחשוף את כל סודות המסע?

<div id="app-container">
  <div id="game-area">
    <div id="instrument-display">
      <img id="current-instrument-image" src="" alt="כלי נגינה">
      <div class="image-overlay"></div> <!-- For potential hover/interaction effects -->
      <audio id="instrument-sound" src="" preload="auto"></audio>
    </div>
    <div id="description-area">
      <p id="stage-description"></p>
    </div>
    <div id="upgrade-options">
      <!-- Upgrade buttons will be placed here by JavaScript -->
    </div>
    <div id="completion-status">
      <span id="percussion-status" class="path-status" data-path="percussion3">כלי הקשה</span>
      <span id="wind-status" class="path-status" data-path="wind3">כלי נשיפה</span>
      <span id="string-status" class="path-status" data-path="string3">כלי מיתר</span>
    </div>
     <button id="restart-button" class="game-button primary">התחל מסע חדש</button>
  </div>
</div>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;700&display=swap'); /* Using a modern, readable font */

  :root {
    --primary-color: #007bff;
    --secondary-color: #28a745;
    --dark-text: #333;
    --medium-text: #555;
    --light-bg: #f4f7f6; /* Lighter background */
    --card-bg: #ffffff; /* Card background */
    --border-color: #ddd;
    --percussion-color: #e74c3c; /* Reddish */
    --wind-color: #3498db; /* Bluish */
    --string-color: #f39c12; /* Yellowish */
    --completed-color: #2ecc71; /* Green */
    --hover-shadow: rgba(0, 0, 0, 0.1);
    --button-shadow: rgba(0, 0, 0, 0.1);
  }

  body {
    font-family: 'Heebo', sans-serif;
    line-height: 1.6;
    color: var(--dark-text);
    background-color: var(--light-bg);
    margin: 0;
    padding: 20px;
    direction: rtl; /* Ensure RTL layout */
    text-align: right; /* Default text alignment */
  }

  h1 {
    text-align: center;
    color: var(--dark-text);
    margin-bottom: 30px;
  }

  #app-container {
    text-align: center; /* Center the game area */
    max-width: 800px;
    margin: 20px auto;
    padding: 0; /* Padding handled by game-area */
    background: linear-gradient(to bottom right, #e0eafc, #cfdef3); /* Subtle gradient background */
    border-radius: 12px;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
    overflow: hidden; /* Ensures border-radius is applied */
  }

  #game-area {
     padding: 20px;
     background-color: var(--card-bg); /* White background for game content */
     border-radius: 12px;
     box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
     margin: 0; /* Use full container space */
  }


  #instrument-display {
    margin-bottom: 25px;
    position: relative; /* Needed for absolute positioning of overlay */
    border-radius: 8px; /* Match container corners */
    overflow: hidden; /* Ensure image doesn't break border-radius */
    box-shadow: 0 2px 5px var(--button-shadow);
    background-color: #eee; /* Placeholder background */
    min-height: 180px; /* Increased min-height for better appearance */
    display: flex;
    align-items: center;
    justify-content: center;
  }

  #current-instrument-image {
    max-width: 100%;
    height: auto;
    max-height: 300px; /* Limit max height */
    display: block;
    margin: 0 auto;
    transition: opacity 0.8s ease-in-out, transform 0.8s ease-in-out; /* Animation for image change */
    opacity: 1; /* Start state */
    transform: scale(1); /* Start state */
  }

  #current-instrument-image.animate-in {
     opacity: 0;
     transform: scale(0.95);
  }
  #current-instrument-image.animate-out {
     opacity: 1;
     transform: scale(1);
  }


  .image-overlay { /* Subtle overlay for interaction ideas */
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0); /* Transparent default */
      pointer-events: none; /* Don't block clicks */
      transition: background 0.3s ease;
  }
   /* Example: #instrument-display:hover .image-overlay { background: rgba(0, 0, 0, 0.05); } */


  #description-area {
    margin-bottom: 25px;
    min-height: 80px; /* Increased min-height */
    display: flex;
    align-items: center; /* Vertically center text */
    justify-content: center; /* Horizontally center text */
    background-color: var(--light-bg);
    padding: 15px;
    border-radius: 8px;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.08);
    text-align: center; /* Description text centered */
  }

  #description-area p {
    font-size: 1.15em; /* Slightly larger text */
    color: var(--medium-text);
    margin: 0; /* Remove default paragraph margin */
    opacity: 1;
    transition: opacity 0.6s ease-in-out; /* Animation for text change */
  }
   #description-area p.animate-out {
      opacity: 0;
   }


  #upgrade-options {
    margin-bottom: 25px;
    display: flex; /* Use flexbox for buttons */
    flex-wrap: wrap; /* Allow wrapping */
    justify-content: center; /* Center buttons */
    gap: 10px; /* Space between buttons */
  }

  .game-button {
    padding: 12px 25px; /* Increased padding */
    font-size: 1.1em;
    cursor: pointer;
    border: none;
    border-radius: 25px; /* Pill shape */
    transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
    box-shadow: 0 4px 6px var(--button-shadow);
    text-align: center;
  }

  .game-button:hover {
    transform: translateY(-2px); /* Lift effect on hover */
    box-shadow: 0 6px 12px var(--hover-shadow);
  }

  .game-button:active {
    transform: translateY(0); /* Press effect */
    box-shadow: 0 2px 4px var(--button-shadow);
  }

  .path-button {
      background-color: #6c757d; /* Default grey */
      color: white;
  }
  .path-button.percussion { background-color: var(--percussion-color); }
  .path-button.wind { background-color: var(--wind-color); }
  .path-button.string { background-color: var(--string-color); }
  .path-button:hover { background-color: #5a6268; }

  .step-button {
    background-color: var(--primary-color);
    color: white;
  }
  .step-button:hover { background-color: #0056b3; }

  .primary { /* For Restart button */
    background-color: var(--secondary-color);
    color: white;
    display: inline-block; /* Make sure it's visible when needed */
  }
   .primary:hover { background-color: #218838; }


  #completion-status {
    margin-top: 20px;
    margin-bottom: 20px;
    font-size: 0.9em;
    color: var(--medium-text);
    display: flex;
    justify-content: center;
    gap: 15px; /* Space between path statuses */
  }

  .path-status {
      display: inline-block;
      padding: 5px 10px;
      border-radius: 15px;
      border: 1px solid var(--border-color);
      background-color: var(--light-bg);
  }

  .path-status.completed {
      border-color: var(--completed-color);
      background-color: rgba(46, 204, 113, 0.2); /* Light green background */
      color: var(--completed-color);
      font-weight: bold;
  }
   .path-status.completed::before {
      content: '✓ '; /* Checkmark */
   }


  #restart-button {
    display: none; /* Initially hidden, managed by JS */
  }

  #explanation-button {
    display: block;
    margin: 30px auto 20px auto; /* More space above/below */
    padding: 12px 25px;
    font-size: 1.1em;
    cursor: pointer;
    background-color: #6c757d; /* Grey button */
    color: white;
    border: none;
    border-radius: 25px;
    box-shadow: 0 4px 6px var(--button-shadow);
    transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
    text-align: center;
  }
  #explanation-button:hover {
    background-color: #5a6268;
    transform: translateY(-2px);
    box-shadow: 0 6px 12px var(--hover-shadow);
  }
   #explanation-button:active {
    transform: translateY(0);
    box-shadow: 0 2px 4px var(--button-shadow);
  }


  #explanation-content {
    margin-top: 20px;
    padding: 20px; /* Increased padding */
    border: 1px solid var(--border-color);
    border-radius: 12px;
    background-color: var(--card-bg);
    display: none; /* Initially hidden */
    line-height: 1.7; /* Improved readability */
    color: var(--dark-text);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    text-align: right; /* Align text inside explanation */
  }

  #explanation-content h2 {
    color: #0056b3;
    margin-top: 15px;
    margin-bottom: 10px; /* Increased margin */
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 8px; /* Increased padding */
    font-size: 1.5em; /* Larger headings */
  }

  #explanation-content h2:first-child {
      margin-top: 0;
  }

  #explanation-content p {
    margin-bottom: 15px; /* Increased margin */
  }

  #explanation-content ul {
    list-style: disc inside;
    padding-left: 0; /* Adjust for RTL */
    margin-bottom: 15px;
  }

  #explanation-content li {
    margin-bottom: 8px; /* Increased margin */
  }

   /* Responsive adjustments */
   @media (max-width: 600px) {
       .game-button, #explanation-button {
           width: 100%; /* Full width buttons on small screens */
           margin: 5px 0;
       }
       #upgrade-options {
           flex-direction: column;
           align-items: center;
       }
       #app-container, #explanation-content {
           padding: 10px;
           margin: 10px auto;
       }
       #instrument-display {
           min-height: 120px;
       }
       #description-area {
            min-height: 100px;
       }
   }
</style>

<button id="explanation-button">הצג / הסתר הסבר מורחב על אבולוציית כלי הנגינה</button>

<div id="explanation-content">
  <h2>הסבר מורחב: מסע הצליל - האבולוציה של כלי הנגינה</h2>

  <p>כלי הנגינה אינם המצאה מודרנית, אלא תוצר של מסע אבולוציוני מדהים שהחל עם הסקרנות הצלילית של האדם הקדמון והגיע עד לפסגות התזמורת הסימפונית. זהו סיפור על התגליות, הטכנולוגיה והצורך העמוק שלנו לבטא את עצמנו באמצעות צליל.</p>

  <h2>מקורות פרימיטיביים</h2>
  <p>האדם הקדמון, עוד לפני שידע לכתוב, גילה את הקסם שבצליל. הקשה על סלעים, תיפוף על עצמות חלולות, או נשיפה לתוך קרניים - אלה היו ניצני המוזיקה הראשונים. כלים טבעיים אלו לא רק שימשו ליצירת קצב, אלא גם לתקשורת, ריפוי וטקסים שבטיים. הם לימדו את האדם על הקשר בין פעולה (הקשה, נשיפה) לבין תוצאה צלילית.</p>

  <h2>הפיזיקה שבבסיס הצליל</h2>
  <p>גם ללא נוסחאות מדעיות, האדם למד להכיר אינטואיטיבית את עקרונות הצליל. ההבנה שרטט יוצר צליל (בין אם של מיתר רוטט או של עמוד אוויר בצינור) והגילוי שחלל מהדהד מגביר ומעשיר אותו (תיבת תהודה) אפשרו להתפתח מעבר לחפצים פשוטים לכלי נגינה אמיתיים. אורך ומתח קובעים גובה, חוזק הפעולה קובע עוצמה, ומבנה הכלי קובע את "צבע" הצליל הייחודי.</p>

  <h2>ענפי האבולוציה המרכזיים</h2>
  <ul>
    <li>
      <strong>כלי נשיפה:</strong> התפתחו מ"נשיפה" מקרית ל"צלילים מכוונים". מחלילי עצם או חימר עם חור נשיפה אחד, גילו האנשים שחורים נוספים יכולים לשנות את גובה הצליל. כך נולדו החלילים הפרימיטיביים. מאוחר יותר, מנגנונים מתוחכמים יותר של קלפות ושסתומים בכלי מתכת ועץ אפשרו מנעד עצום, גמישות טכנית וצליל עשיר ומלא - מהפיקולו הצפצפני ועד הטובה העמוקה.
    </li>
    <li>
      <strong>כלי מיתר:</strong> סיפורם מתחיל כנראה עם קשת הציד המתוחה. הוספת מיתרים מרובים יצרה את הלירה והנבל הקדומים, ששימשו לליווי שירה או סיפור. כשיצרו תיבות תהודה וגילו את הקשת, יכלו להפיק צליל מתמשך, עשיר ורב הבעה - כך נולדה משפחת כלי הקשת (כינור, ויולה, צ'לו, קונטרבס). שילוב מיתרים עם מקלדת הביא לעולם את הצ'מבלו ולבסוף את הפסנתר - "מלך הכלים" המאפשר הרמוניה, מלודיה וקצב בו זמנית.
    </li>
    <li>
      <strong>כלי הקשה:</strong> הצורך במקצב הוא אולי הקדום ביותר. אבנים, ענפים ועצמות שימשו לכך. עורות שהותקנו על חללים יצרו את התופים הראשונים, ששימשו גם להעברת מסרים וטקסים. האבולוציה הביאה למגוון עצום - תופים בעלי גובה צליל מכוון (טימפני), כלי הקשה מלודיים (קסילופון), וכלים בעלי צליל ייחודי (מצילות, גונג, תוף סנר). הם מהווים את עמוד השדרה הקצבי והגוון הצלילי של כל הרכב.
    </li>
  </ul>

  <h2>השפעת הטכנולוגיה והחומרים</h2>
  <p>כל התקדמות טכנולוגית - מעיבוד עץ מתקדם, דרך גילוי ושימוש במתכות, ועד המצאת מנגנונים מכאניים מורכבים - השפיעה ישירות על התפתחות הכלים. חומרים טובים יותר אפשרו צלילים איכותיים יותר. מנגנונים מדויקים אפשרו נגינה מהירה ומורכבת יותר, והרחיבו את המנעד והאפשרויות הטכניות.</p>

  <h2>המסע לתזמורת</h2>
  <p>מנגינה בודדת או הרכב קטן, המסע הגיע לשיאו עם התפתחות ההרכבים הגדולים והשילובים בין משפחות הכלים. התזמורת הסימפונית המודרנית, המאגדת בתוכה את מיטב ההישגים האבולוציוניים של כל משפחות הכלים, היא פלטת צלילים אנושית וטכנולוגית חסרת תקדים, המאפשרת יצירת יצירות מוזיקליות בעלות עושר, עומק וגודל שאין כדוגמתם.</p>
</div>

<script>
  const stages = {
    start: {
      description: "מסענו מתחיל עם הצלילים הראשונים שהאדם גילה בטבע. איך יתפתח עולם המוזיקה?",
      image: "https://cdn.pixabay.com/photo/2017/07/17/16/44/cave-2512716_960_720.jpg", // Cave painting / early human art vibe
      sound: null,
      upgrades: [
        { text: "חקור צלילי הקשה (מקצב)", next_stage_id: "percussion1", type: "percussion" },
        { text: "חקור צלילי נשיפה (מנגינה ראשונית)", next_stage_id: "wind1", type: "wind" },
        { text: "חקור צלילי מיתר (רטט וצליל)", next_stage_id: "string1", type: "string" }
      ]
    },
    percussion1: {
      description: "הקשה בסיסית: שימוש באבנים או עצמות ליצירת מקצב פשוט. שמעו את ההד הקדום!",
      image: "https://cdn.pixabay.com/photo/2013/07/12/15/58/flint-stone-150822_960_720.png", // Flint stones
      sound: "https://www.soundjay.com/percussion/rock-clack-2-1.mp3",
      upgrades: [
        { text: "השתמשו בעור מתוח ליצירת תוף", next_stage_id: "percussion2", type: "percussion" }
      ]
    },
    percussion2: {
      description: "תופים פרימיטיביים: עור מתוח על חלל או מסגרת. הקצב מתחיל לחיות!",
      image: "https://cdn.pixabay.com/photo/2017/02/01/18/30/shaman-2031089_960_720.jpg", // Tribal drum
      sound: "https://www.soundjay.com/drums/tribal-drum-01.mp3",
      upgrades: [
        { text: "פתח מגוון כלי הקשה וכוונן אותם", next_stage_id: "percussion3", type: "percussion" }
      ]
    },
    percussion3: {
      description: "פסגת הקשה: טימפני, סנר, קסילופון ועוד! העולם נשמע אחרת עם צלילים מוגדרים ולא מוגדרים.",
      image: "https://cdn.pixabay.com/photo/2016/11/23/15/30/timpani-1854203_960_720.jpg", // Timpani and drums
      sound: "https://www.soundjay.com/orchestra/timpani-hit-1.mp3",
      upgrades: [],
      end_message: "המסע של כלי ההקשה הושלם! הוספתם את הקצב והצבע לתזמורת האבולוציונית."
    },
    wind1: {
      description: "צלילי הנשיפה הראשונים: נשיפה לתוך עצם חלולה או קונכייה. צליל בודד אך מהדהד...",
      image: "https://cdn.pixabay.com/photo/2017/07/01/18/05/bone-2462685_960_720.jpg", // Bone fragment
      sound: "https://www.soundjay.com/nature/conch-horn-1.mp3", // Conch sound
      upgrades: [
        { text: "חורר את העצם ליצירת גובהי צליל שונים", next_stage_id: "wind2", type: "wind" }
      ]
    },
    wind2: {
      description: "חליל פשוט: עצם או עץ עם מספר חורים. אפשר לנגן מנגינות ראשוניות!",
      image: "https://cdn.pixabay.com/photo/2016/03/05/22/00/flute-1239023_960_720.jpg", // Simple wooden flute
      sound: "https://www.soundjay.com/flute/flute-01.mp3",
      upgrades: [
        { text: "שכלל את המבנה והוסף קלפות ושסתומים", next_stage_id: "wind3", type: "wind" }
      ]
    },
    wind3: {
      description: "פסגת הנשיפה: חליל, קלרינט, חצוצרה ועוד! מנגינות מורכבות וצלילים עשירים.",
      image: "https://cdn.pixabay.com/photo/2017/08/06/21/39/brass-2597585_960_720.jpg", // Brass section
      sound: "https://www.soundjay.com/brass/trumpet-fanfare-1.mp3",
      upgrades: [],
      end_message: "המסע של כלי הנשיפה הושלם! הוספתם את המנגינה וההרמוניה לתזמורת האבולוציונית."
    },
    string1: {
      description: "המיתר הראשון: בהשראת קשת הציד? מיתר בודד מתוח. צליל פשוט אך טעון פוטנציאל.",
      image: "https://cdn.pixabay.com/photo/2013/07/12/17/55/bow-153159_960_720.png", // Simple bow
      sound: "https://www.soundjay.com/strings/single-string-pluck-1.mp3",
      upgrades: [
        { text: "הוסף מיתרים מרובים ותיבת תהודה", next_stage_id: "string2", type: "string" }
      ]
    },
    string2: {
      description: "לירה או כינור פרימיטיבי: מספר מיתרים ותהודה. מוזיקה יותר עשירה אפשרית!",
      image: "https://cdn.pixabay.com/photo/2016/03/05/21/58/lyre-1238687_960_720.jpg", // Lyre
      sound: "https://www.soundjay.com/strings/harp-glide-1.mp3",
      upgrades: [
        { text: "שכלל את המבנה והשתמש בקשת", next_stage_id: "string3", type: "string" }
      ]
    },
    string3: {
      description: "פסגת המיתר: כינורות, ויולות, צ'לו וקונטרבס! טווח רגשות ודינמיקה אינסופיים.",
      image: "https://cdn.pixabay.com/photo/2017/01/05/13/03/violin-1955644_960_720.jpg", // Violin and cello
      sound: "https://www.soundjay.com/orchestra/orchestra-hit-1.mp3", // Short orchestral string phrase
      upgrades: [],
      end_message: "המסע של כלי המיתר הושלם! הוספתם את הנשמה והדרמה לתזמורת האבולוציונית."
    }
  };

  let completedPaths = new Set();
  const allPaths = ['percussion3', 'wind3', 'string3']; // IDs of the final stages in each path
  const pathColors = { percussion: 'percussion', wind: 'wind', string: 'string' }; // Mapping types to colors

  const instrumentImage = document.getElementById('current-instrument-image');
  const stageDescription = document.getElementById('stage-description');
  const upgradeOptionsDiv = document.getElementById('upgrade-options');
  const instrumentSound = document.getElementById('instrument-sound');
  const restartButton = document.getElementById('restart-button');
  const explanationButton = document.getElementById('explanation-button');
  const explanationContent = document.getElementById('explanation-content');
  const completionStatusDiv = document.getElementById('completion-status');

  function updateCompletionStatus() {
    allPaths.forEach(pathId => {
      const statusSpan = document.querySelector(`.path-status[data-path="${pathId}"]`);
      if (statusSpan) {
        if (completedPaths.has(pathId)) {
          statusSpan.classList.add('completed');
        } else {
          statusSpan.classList.remove('completed');
        }
      }
    });
     if (completedPaths.size === 0) {
         completionStatusDiv.style.display = 'flex'; // Show at start
     }
  }

  function renderStage(stageId) {
    const stage = stages[stageId];

    // Animate out current content
    instrumentImage.classList.add('animate-in');
    stageDescription.classList.add('animate-out');
    upgradeOptionsDiv.style.opacity = '0'; // Fade out buttons

    // Use a timeout to change content after animation starts
    setTimeout(() => {
      instrumentImage.src = stage.image;
      stageDescription.textContent = stage.description;

      // Animate in new content
      instrumentImage.classList.remove('animate-in');
      instrumentImage.classList.add('animate-out'); // Trigger animate-in after content load/change
      stageDescription.classList.remove('animate-out');
      upgradeOptionsDiv.style.opacity = '1'; // Fade in buttons

      // Play sound
      if (stage.sound) {
        instrumentSound.src = stage.sound;
        instrumentSound.load(); // Ensure sound is ready
        instrumentSound.play().catch(e => console.warn("Error playing sound:", e)); // Use warn for autoplay policy issues
      } else {
        // Stop any currently playing sound
        if (!instrumentSound.paused) {
           instrumentSound.pause();
           instrumentSound.currentTime = 0;
        }
        instrumentSound.removeAttribute('src');
      }

      // Clear old buttons
      upgradeOptionsDiv.innerHTML = '';

      // Add new buttons
      if (stage.upgrades && stage.upgrades.length > 0) {
        stage.upgrades.forEach(upgrade => {
          // Only show upgrades if the target path is not yet completed,
          // OR if we are at the 'start' stage showing path choices.
          const targetPathEnd = allPaths.find(id => id.startsWith(upgrade.next_stage_id.replace(/\d+$/, '')));
          const pathCompleted = targetPathEnd ? completedPaths.has(targetPathEnd) : false;

          if (stageId === 'start' || !pathCompleted) {
            const button = document.createElement('button');
            button.textContent = upgrade.text;
            button.classList.add('game-button', 'step-button'); // Default step button style
            if (upgrade.type) {
                button.classList.add('path-button', upgrade.type); // Add path specific class
                button.classList.remove('step-button'); // Remove step button if it's a path button
            }
            button.onclick = () => renderStage(upgrade.next_stage_id);
            upgradeOptionsDiv.appendChild(button);
          }
        });
        restartButton.style.display = 'none'; // Hide restart while in a path
        completionStatusDiv.style.display = 'flex'; // Show status during path exploration
      } else {
        // End of a path
        if (stage.end_message) {
            stageDescription.textContent += "\n" + stage.end_message;
        }
        completedPaths.add(stageId);
        updateCompletionStatus(); // Update UI status

        const allPathsCompleted = allPaths.every(pathId => completedPaths.has(pathId));

        if (allPathsCompleted) {
            // All paths finished, show a final message and restart
            stageDescription.textContent += "\nכל מסלולי האבולוציה נחקרו! עכשיו אתם מבינים את התזמורת כולה.";
            restartButton.style.display = 'block';
            upgradeOptionsDiv.style.display = 'none'; // Hide path buttons
             completionStatusDiv.style.display = 'flex'; // Keep status visible at the end
        } else {
            // Path finished, but others remain. Offer to return to start.
             const startOverButton = document.createElement('button');
             startOverButton.textContent = "חזרה להתחלה לחקור מסלולים נוספים";
             startOverButton.classList.add('game-button', 'primary'); // Style as primary button
             startOverButton.onclick = () => {
               renderStage('start');
               upgradeOptionsDiv.style.display = 'flex'; // Show path buttons container
                updateCompletionStatus(); // Ensure status is correct on return
             };
             upgradeOptionsDiv.appendChild(startOverButton);
             restartButton.style.display = 'none'; // Hide main restart button here
              completionStatusDiv.style.display = 'flex'; // Keep status visible
        }
      }
    }, 600); // Match this timeout to animation duration
  }

  // Initial render
  renderStage('start');
  updateCompletionStatus(); // Initial status display

  // Explanation button toggle
  explanationButton.onclick = () => {
    const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
    explanationContent.style.display = isHidden ? 'block' : 'none';
    explanationButton.textContent = isHidden ? 'הסתר הסבר מורחב' : 'הצג / הסתר הסבר מורחב על אבולוציית כלי הנגינה';
  };

  // Restart button logic
  restartButton.onclick = () => {
    completedPaths.clear(); // Reset completed paths
    renderStage('start');
    upgradeOptionsDiv.style.display = 'flex'; // Show path buttons container
    updateCompletionStatus(); // Reset status display
  };

</script>
```