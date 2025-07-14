---
title: "הנדסת מילים: הסימולטור האולטימטיבי למבנים שיריים"
english_slug: word-engineering-poetic-forms-in-action
category: "ספרות"
tags:
  - שירה
  - מבנים שיריים
  - לימריק
  - ססטינה
  - כתיבה יוצרת
---
<div class="app-wrapper">
  <h1>הנדסת מילים: הסימולטור האולטימטיבי</h1>
  <p class="intro-text">הצטרפו למסע קסום בעולם המבנים השיריים. האם אתם מוכנים להפוך למהנדסי מילים ולגלות איך השלד של שיר מעצב את נשמתו? בואו נבנה יחד לימריק שובב או ססטינה מלכותית, צעד אחר צעד.</p>

  <style>
  /* Global Styles & Typography */
  @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700&family=Varela+Round&display=swap');

  :root {
      --primary-color: #673AB7; /* Deep Purple */
      --secondary-color: #FFC107; /* Amber */
      --accent-color: #00BCD4; /* Cyan */
      --background-light: #f3e5f5; /* Lighter Purple */
      --background-medium: #e1bee7; /* Medium Purple */
      --text-color: #212121; /* Dark Grey */
      --subtle-text-color: #616161; /* Grey */
      --border-color: #d1c4e9; /* Light Purple */
      --success-color: #4CAF50; /* Green */
      --error-color: #F44336; /* Red */
      --card-background: #ffffff;
  }

  body {
      font-family: 'Heebo', sans-serif;
      direction: rtl;
      text-align: right;
      line-height: 1.6;
      color: var(--text-color);
      background-color: var(--background-light);
      margin: 0;
      padding: 20px;
  }

  .app-wrapper {
      max-width: 800px;
      margin: 40px auto;
      background-color: var(--card-background);
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
      border: 1px solid var(--border-color);
  }

  h1, h2, h3 {
      font-family: 'Varela Round', sans-serif;
      color: var(--primary-color);
      text-align: center;
      margin-bottom: 20px;
  }

  h1 { font-size: 2.5em; }
  h2 { font-size: 1.8em; margin-bottom: 15px; }
  h3 { font-size: 1.4em; margin-bottom: 10px; color: var(--subtle-text-color); }

  .intro-text {
      text-align: center;
      font-size: 1.1em;
      margin-bottom: 30px;
      color: var(--subtle-text-color);
  }

  p {
      margin-bottom: 1em;
  }

  /* Section & Card Styling */
  #choice-screen,
  .poem-app,
  #explanation {
      margin-top: 30px;
      padding: 20px;
      border-radius: 8px;
      background-color: var(--background-medium);
      box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.08);
      transition: all 0.5s ease-in-out;
  }

  .poem-app {
      display: none; /* Controlled by JS */
      border: 1px solid var(--border-color);
      background-color: var(--card-background); /* Poems displayed on white card */
  }

  #explanation {
      display: none; /* Controlled by JS */
      background-color: var(--background-medium);
  }

  /* Button Styles */
  button {
      padding: 12px 25px;
      font-size: 1em;
      cursor: pointer;
      border: none;
      border-radius: 25px; /* Pill shape */
      transition: all 0.3s ease;
      font-family: 'Heebo', sans-serif;
      font-weight: 500;
      margin: 5px; /* Spacing between buttons */
  }

  button:hover {
      opacity: 0.9;
      transform: translateY(-2px);
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }

  button:active {
      transform: translateY(0);
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }

  #choice-screen button {
      background-color: var(--primary-color);
      color: white;
      padding: 15px 30px; /* Larger initial buttons */
      margin: 15px;
  }

  /* Specific button styles within apps */
  .poem-app button {
      background-color: var(--accent-color);
      color: white;
      margin-right: 10px; /* Space from input */
  }

  .poem-app button:last-child {
      margin-right: 0;
  }

  .poem-app button:disabled {
      background-color: #cccccc;
      cursor: not-allowed;
  }

  #show-explanation-btn {
      display: block; /* Take full width available */
      width: fit-content;
      margin: 30px auto 0 auto; /* Center button below app */
      background-color: var(--secondary-color);
      color: var(--text-color);
      font-weight: 700;
  }

  /* Input Styles */
  label {
      display: block;
      margin-bottom: 8px;
      font-weight: 500;
      color: var(--primary-color);
  }

  input[type="text"] {
      padding: 10px 15px;
      font-size: 1.1em;
      margin-bottom: 15px;
      border: 1px solid var(--border-color);
      border-radius: 5px;
      width: calc(100% - 120px); /* Adjust width to accommodate button */
      max-width: 500px; /* Max width for input */
      transition: border-color 0.3s ease;
      box-sizing: border-box; /* Include padding/border in element's total width */
  }

   input[type="text"]:focus {
       outline: none;
       border-color: var(--accent-color);
       box-shadow: 0 0 5px rgba(0, 188, 212, 0.3);
   }

  /* Specific Section Layouts */
  .current-line-section {
      display: flex;
      align-items: center;
      margin-bottom: 20px;
      flex-wrap: wrap; /* Allow wrapping on smaller screens */
  }

   .current-line-section label {
       margin-bottom: 0; /* Adjust margin for flex layout */
       margin-inline-end: 10px;
   }

   .current-line-section input {
       flex-grow: 1; /* Allow input to take available space */
       margin-bottom: 0; /* Adjust margin for flex layout */
       margin-inline-end: 10px;
   }

   .current-line-section button {
       flex-shrink: 0; /* Prevent button from shrinking */
   }


  .poem-info {
      margin-top: 15px;
      font-style: italic;
      color: var(--subtle-text-color);
      font-size: 0.9em;
      background-color: #f8f1ff; /* Very light purple */
      padding: 10px 15px;
      border-left: 4px solid var(--primary-color);
      border-radius: 4px;
  }

  .poem-stanza,
  .envoi-lines {
      margin-bottom: 20px;
      padding: 15px;
      background-color: #f9f9f9;
      border: 1px dashed var(--border-color);
      border-radius: 8px;
      min-height: 50px; /* Reserve space */
  }

   .poem-stanza p,
   .envoi-lines p {
       margin-bottom: 8px;
       padding: 3px 0;
       border-bottom: 1px dotted #eee;
       opacity: 0; /* Start hidden for animation */
       transform: translateY(10px); /* Start slightly below for animation */
   }

   .poem-stanza p.fade-in,
   .envoi-lines p.fade-in {
       opacity: 1;
       transform: translateY(0);
       transition: opacity 0.5s ease-out, transform 0.5s ease-out;
   }


  /* Results and Envoi Sections */
  .poem-result,
  #sestina-envoi {
      display: none; /* Controlled by JS */
      margin-top: 20px;
      padding-top: 20px;
      border-top: 2px dashed var(--primary-color);
  }

  .poem-result h3,
   #sestina-envoi h3 {
       text-align: right;
       color: var(--primary-color);
       margin-bottom: 15px;
   }

  /* Style for the end words display in Sestina */
  #sestina-end-words-display {
      margin-bottom: 20px;
      padding: 15px;
      background-color: #e0f7fa; /* Light Cyan */
      border: 1px solid var(--accent-color);
      border-radius: 8px;
      display: none; /* Controlled by JS */
      transition: all 0.5s ease-in-out;
  }

  #sestina-end-words-display strong {
      color: var(--primary-color);
      font-weight: 700;
  }

   #sestina-end-words-display p {
       margin: 0;
       font-size: 1em;
   }


  /* Style for the envoi word placeholders */
  .envoi-word1,
  .envoi-word2 {
      color: var(--success-color);
      font-weight: 700;
  }

  /* Style for the sestina error message */
  .error-message {
      color: var(--error-color);
      margin-top: 10px;
      padding: 10px;
      border: 1px solid var(--error-color);
      background-color: #ffebee; /* Light Red */
      border-radius: 5px;
      display: none; /* Controlled by JS */
      animation: shake 0.5s ease-in-out;
  }

   @keyframes shake {
       0% { transform: translateX(0); }
       20% { transform: translateX(-5px); }
       40% { transform: translateX(5px); }
       60% { transform: translateX(-5px); }
       80% { transform: translateX(5px); }
       100% { transform: translateX(0); }
   }


  /* Style for pre tags displaying poems */
  pre {
       background-color: #eeeeee;
       padding: 20px;
       border: 1px solid #dddddd;
       border-radius: 8px;
       white-space: pre-wrap;
       word-wrap: break-word;
       font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace; /* Monospaced font for poem display */
       font-size: 1em;
       line-height: 1.8;
       color: #333;
  }

  /* Style for HR separator between Sestina stanzas */
  .poem-stanza hr {
       margin: 25px 0;
       border: 0;
       border-top: 1px dashed var(--border-color);
  }

  /* Explanation Section Styles */
  #explanation {
      margin-top: 40px;
      padding: 25px;
      border-top: 2px solid var(--secondary-color);
      background-color: var(--background-medium);
  }

   #explanation h2, #explanation h3 {
       color: var(--primary-color);
       text-align: right; /* Align explanation headers right */
       margin-bottom: 10px;
   }

   #explanation h3 {
       margin-top: 20px;
       color: var(--subtle-text-color);
   }

   #explanation p {
       margin-bottom: 1.2em;
   }

   #explanation ul {
       margin-bottom: 1.2em;
       padding-right: 20px;
   }

   #explanation li {
       margin-bottom: 0.5em;
   }

  /* Responsive Adjustments */
   @media (max-width: 600px) {
       .app-wrapper {
           padding: 20px;
           margin: 20px auto;
       }

       h1 { font-size: 2em; }
       h2 { font-size: 1.5em; }
       button { padding: 10px 20px; }
       #choice-screen button { padding: 12px 25px; margin: 10px; }
       input[type="text"] { width: calc(100% - 10px); margin-inline-end: 0; margin-bottom: 15px; } /* Full width inputs on small screens */
       .current-line-section { flex-direction: column; align-items: flex-start; }
       .current-line-section label { margin-inline-end: 0; margin-bottom: 8px; }
       .current-line-section input { margin-inline-end: 0; }
       .current-line-section button { width: 100%; margin-inline-end: 0; }
   }

  </style>

  <div id="app-container">
      <div id="choice-screen">
          <h2>איזו יצירה נבנה היום?</h2>
          <p>בחרו מבנה שירי כדי להתחיל במסע ההנדסי שלכם!</p>
          <button id="limerick-btn">🛠️ לימריק שובב (פשוט)</button>
          <button id="sestina-btn">🏰 ססטינה מלכותית (מאתגר)</button>
      </div>

      <div id="limerick-app" class="poem-app">
          <h2>בונים לימריק</h2>
          <p>לימריק - 5 שורות, חרוז AABBA, קצב מדבק! בואו נראה מה תצרו.</p>
          <div id="limerick-stanza" class="poem-stanza">
              <!-- Limerick lines will be added here -->
          </div>
          <div id="limerick-current-line" class="current-line-section">
              <label for="limerick-line-input">
                  שורה <span id="limerick-line-num">1</span> (<span id="limerick-rhyme">חרוז A</span>):
              </label>
              <input type="text" id="limerick-line-input" size="60" placeholder="כתבו את השורה כאן...">
              <button id="add-limerick-line-btn">הוסף שורה</button>
          </div>
          <div id="limerick-info" class="poem-info"></div>
          <div id="limerick-error" class="error-message"></div>
          <div id="limerick-result" class="poem-result">
              <h3>הלימריק המוכן שלכם:</h3>
              <pre id="display-limerick"></pre>
              <button id="reset-limerick">🛠️ בונים לימריק חדש</button>
          </div>
      </div>

      <div id="sestina-app" class="poem-app">
          <h2>בונים ססטינה</h2>
          <p>ססטינה - יצירה מרתקת בת 6 בתים בני 6 שורות ועוד בית סיום! האתגר הוא לשבץ את אותן מילות סיום שוב ושוב בסדר משתנה.</p>
           <div id="sestina-error" class="error-message"></div>
          <div id="sestina-info" class="poem-info"></div>
          <div id="sestina-end-words-display">
               <p>🥳 <strong>מילות הסיום הנבחרות שלכם:</strong> <strong id="display-sestina-end-words"></strong></p>
               <p class="sestina-info-permutation"></p>
          </div>
          <div id="sestina-stanza" class="poem-stanza">
              <!-- Sestina lines/stanzas will be added here -->
          </div>
           <div id="sestina-current-line" class="current-line-section">
              <label for="sestina-line-input">
                  בית <span id="sestina-stanza-num">1</span>, שורה <span id="sestina-line-num">1</span>:
                  <span id="sestina-line-instruction"></span>
              </label>
              <input type="text" id="sestina-line-input" size="80" placeholder="כתבו את השורה כאן...">
              <button id="add-sestina-line-btn">הוסף שורה</button>
          </div>
           <div id="sestina-envoi" class="poem-result">
               <h3>בית הסיום (אנווי) - הסגירה הגדולה</h3>
               <p>כמעט סיימתם! כעת בונים את 3 שורות האנווי. כל שורה מכילה שתי מילות סיום מהרשימה המקורית - אחת בתוך השורה ואחת בסופה.</p>
               <div id="envoi-lines" class="envoi-lines">
                   <!-- Envoi lines will be added here -->
               </div>
                <div id="sestina-current-envoi-line" class="current-line-section">
                   <label for="envoi-line-input">
                       שורה <span id="envoi-line-num">1</span>:
                       חייבת להכיל את המילה "<strong class="envoi-word1"></strong>" ולהסתיים במילה "<strong class="envoi-word2"></strong>"
                   </label>
                   <input type="text" id="envoi-line-input" size="80" placeholder="כתבו את שורת האנווי כאן...">
                   <button id="add-envoi-line-btn">הוסף שורה</button>
                </div>
           </div>
          <div id="sestina-result" class="poem-result">
               <h3>הססטינה המפוארת שלכם:</h3>
               <pre id="display-sestina"></pre>
              <button id="reset-sestina">🏰 בונים ססטינה חדשה</button>
          </div>
      </div>
  </div>

  <button id="show-explanation-btn">📜 הצג הסבר על מבנים שיריים</button>
  <div id="explanation">
      <h2>הסבר מקיף: הנדסת מילים ומבנים שיריים</h2>
      <h3>מהו מבנה שירי ולמה כדאי להכיר אותו?</h3>
      <p>מבנה שירי הוא כמו מתכון או שרטוט אדריכלי ליצירה פואטית. הוא מפרט כללים לגבי מספר שורות, סדר חריזה, מקצב (משקל), ואפילו מיקום של מילים מסוימות. למה להגביל את עצמכם? כי דווקא המגבלה יכולה להיות זרז מדהים ליצירתיות! היא מאלצת אתכם לחשוב אחרת, למצוא מילים ודימויים מפתיעים, וליצור מוזיקליות וקצב ייחודיים לשיר. מבנים שיריים הם גשר להיסטוריה של השירה, ומאפשרים לנו להצטרף לשיחה רבת דורות עם משוררים שפעלו במסגרות דומות.</p>
      <h3>לימריק: הקצב הקליל והחרוז השובב (AABBA)</h3>
      <p>הלימריק הוא יהלום קטן וקצבי, מושלם להתחלה! מקורו באירלנד והוא אהוב בזכות ההומור והמבנה הפשוט לכאורה:</p>
      <ul>
          <li><strong>שורה 1 (A):</strong> בדרך כלל מציגה דמות ראשית ומיקום. ("היה פעם איש <strong>מפדן</strong>...")</li>
          <li><strong>שורה 2 (A):</strong> מתחרזת עם שורה 1, ומתארת פעולה ראשונה. ("שאהב מאוד לשחק <strong>בקרוקפן</strong>.")</li>
          <li><strong>שורות 3 ו-4 (BB):</strong> קצרות יותר, מתחרזות זו עם זו, ומציגות טוויסט עלילתי או אירוע משעשע. ("קפץ לתוך בור <strong>עמוק</strong>,<br> הרגיש לפתע <strong>חולשה</strong>...")</li>
          <li><strong>שורה 5 (A):</strong> מתחרזת שוב עם 1 ו-2, ולעתים קרובות חוזרת למילת הסיום של שורה 1 או מציגה סיום מפתיע/מצחיק. ("ונשאר שם כל היום ב<strong>מפדן</strong>.")</li>
      </ul>
      <p>שימו לב למקצב! נסו לקרוא לימריקים בקול ותחושו את הקפיצה השמחה של המשקל.</p>
      <h3>ססטינה: מסע מילים מחזורי</h3>
      <p>הססטינה היא אתגר אלגנטי שנולד בפרובנס של המאה ה-12. היא דורשת דיוק, סבלנות, ויכולת ריקוד עם מילים! שמה מגיע מהמספר שש (Sesta באיטלקית), המפתח למבנה.</p>
      <h3>מבנה הססטינה: 6 בתים x 6 שורות + בית סיום (אנווי)</h3>
      <p>הלב הפועם של הססטינה הוא שש מילות הסיום של הבית הראשון. אותן מילים בדיוק יופיעו בסוף השורות בכל ששת הבתים הבאים, אך הן ינועו וישנו את מקומן לפי תבנית מתמטית קבועה. אחרי ששת הבתים, מגיע בית סיום קצרצר בן 3 שורות, ה"אנווי" (Envoi), שמרכז את כל שש מילות המפתח.</p>
      <h3>איך המילים רוקדות? תבנית הסיבוב (Permutations)</h3>
      <p>נסמן את מילות הסיום בבית הראשון במספרים 1 עד 6. סדר המילים בסוף השורות בכל בית יהיה כך (קוראים מימין לשמאל):</p>
      <ul>
          <li>בית 1: 1, 2, 3, 4, 5, 6</li>
          <li>בית 2: 6, 1, 5, 2, 4, 3</li>
          <li>בית 3: 3, 6, 4, 1, 2, 5</li>
          <li>בית 4: 5, 3, 2, 6, 1, 4</li>
          <li>בית 5: 4, 5, 1, 3, 6, 2</li>
          <li>בית 6: 2, 4, 6, 5, 3, 1</li>
      </ul>
      <p>התבנית הזו, שנקראת לעיתים "סיבוב ההחלפות", מבטיחה שכל מילה תופיע בכל פוזיציה (ראשונה, שנייה, וכו') לאורך הבתים, ומאלצת את המשורר לחשוב על קשרים חדשים בין המילים שחוזרות.</p>
      <h3>האנווי: הסיום המתוק (או המר...)</h3>
      <p>בית הסיום (אנווי) בן 3 השורות אוסף את כל שש מילות הסיום. לרוב, כל שורה באנווי מכילה שתיים ממילות המקור: אחת בתוך השורה ואחת בסופה. לדוגמה (מילות הסיום המקוריות: 1, 2, 3, 4, 5, 6):</p>
      <ul>
          <li>שורה 1: מכילה את מילה 1, מסתיימת במילה 2.</li>
          <li>שורה 2: מכילה את מילה 3, מסתיימת במילה 4.</li>
          <li>שורה 3: מכילה את מילה 5, מסתיימת במילה 6.</li>
      </ul>
      <p>האנווי הוא רגע של איסוף, של ראיית התמונה הגדולה, ומקום לסיכום או טוויסט סופי המשלב את כל המילים החוזרות.</p>
      <h3>כיצד מגבלה מולידה יצירה?</h3>
      <p>המבנים השיריים אינם כבלים אלא מסלולי המראה ליצירה. הססטינה, במיוחד, מראה איך הצורך להשתמש במילים מסוימות שוב ושוב יכול לחשוף רבדים חדשים של משמעות במילים האלה, או להוביל את השיר לכיוונים מפתיעים רק כדי לעמוד בדרישה המבנית. זה ריקוד בין הצורה לתוכן, שבו כל אחד מעשיר את השני.</p>
  </div>
</div>

<script>
    let currentPoemType = null;

    // Limerick State
    let limerickLineCount = 0;
    let limerickLines = [];
    const limerickRhymeScheme = ['A', 'A', 'B', 'B', 'A'];
    const limerickInfoHints = [
        '(ארוכה יותר, חרוז A - הציגו דמות ומקום)',
        '(ארוכה יותר, חרוז A - תארו פעולה או מאפיין)',
        '(קצרה יותר, חרוז B - אירוע מפתיע/מצחיק)',
        '(קצרה יותר, חרוז B - תוצאה של האירוע)',
        '(ארוכה יותר, חרוז A - סיום מפתיע או חזרה למקור)'
    ];

    // Sestina State
    let sestinaStanzaCount = 0;
    let sestinaLineCount = 0;
    let envoiLineCount = 0;
    let sestinaEndWords = [];
    let sestinaWordPermutations = []; // Stores the *indices* of the end words for each line
    let sestinaLines = []; // Array of arrays: sestinaLines[stanzaIndex][lineIndex]
    let envoiLines = [];
    // Pattern represents the index of the *original* end word list (0-5)
    const sestinaPermutationPattern = [
        [0, 1, 2, 3, 4, 5], // Stanza 1 (initial) - we just capture words here
        [5, 0, 4, 1, 3, 2], // Stanza 2
        [2, 5, 3, 0, 1, 4], // Stanza 3
        [4, 2, 1, 5, 0, 3], // Stanza 4
        [3, 4, 0, 2, 5, 1], // Stanza 5
        [1, 3, 5, 4, 2, 0]  // Stanza 6
    ];
    const envoiWordPairs = [[0, 1], [2, 3], [4, 5]]; // Indices of original end words for envoi lines

    // Get elements
    const choiceScreen = document.getElementById('choice-screen');
    const limerickApp = document.getElementById('limerick-app');
    const sestinaApp = document.getElementById('sestina-app');
    const limerickBtn = document.getElementById('limerick-btn');
    const sestinaBtn = document.getElementById('sestina-btn');

    // Limerick elements
    const limerickStanzaDiv = document.getElementById('limerick-stanza');
    const limerickCurrentLineDiv = document.getElementById('limerick-current-line');
    const limerickLineNumSpan = document.getElementById('limerick-line-num');
    const limerickRhymeSpan = document.getElementById('limerick-rhyme');
    const limerickLineInput = document.getElementById('limerick-line-input');
    const addLimerickLineBtn = document.getElementById('add-limerick-line-btn');
    const limerickInfoDiv = document.getElementById('limerick-info');
    const limerickResultDiv = document.getElementById('limerick-result');
    const displayLimerickPre = document.getElementById('display-limerick');
    const resetLimerickBtn = document.getElementById('reset-limerick');
    const limerickErrorDiv = document.getElementById('limerick-error');


    // Sestina elements
    const sestinaInfoDiv = document.getElementById('sestina-info');
    const sestinaEndWordsDisplayDiv = document.getElementById('sestina-end-words-display');
    const displaySestinaEndWordsSpan = document.getElementById('display-sestina-end-words');
     const sestinaPermutationInfoSpan = document.querySelector('.sestina-info-permutation');
    const sestinaStanzaDiv = document.getElementById('sestina-stanza');
    const sestinaCurrentLineDiv = document.getElementById('sestina-current-line');
    const sestinaStanzaNumSpan = document.getElementById('sestina-stanza-num');
    const sestinaLineNumSpan = document.getElementById('sestina-line-num');
    const sestinaLineInstructionSpan = document.getElementById('sestina-line-instruction');
    const sestinaLineInput = document.getElementById('sestina-line-input');
    const addSestinaLineBtn = document.getElementById('add-sestina-line-btn');
    const sestinaEnvoiDiv = document.getElementById('sestina-envoi');
    const envoiLinesDiv = document.getElementById('envoi-lines');
    const sestinaCurrentEnvoiLineDiv = document.getElementById('sestina-current-envoi-line');
    const envoiLineNumSpan = document.getElementById('envoi-line-num');
    const envoiWord1Spans = document.querySelectorAll('.envoi-word1');
    const envoiWord2Spans = document.querySelectorAll('.envoi-word2');
    const envoiLineInput = document.getElementById('envoi-line-input');
    const addEnvoiLineBtn = document.getElementById('add-envoi-line-btn');
    const sestinaResultDiv = document.getElementById('sestina-result');
    const displaySestinaPre = document.getElementById('display-sestina');
    const resetSestinaBtn = document.getElementById('reset-sestina');
    const sestinaErrorDiv = document.getElementById('sestina-error');


    const showExplanationBtn = document.getElementById('show-explanation-btn');
    const explanationDiv = document.getElementById('explanation');

    // Helper: Clean word for comparison (remove punctuation, lowercase)
    function cleanWord(word) {
        if (!word) return '';
        return word.trim().replace(/[.,!?;:'"״׳-]+$/, '').toLowerCase();
    }

    // Helper: Get the last word of a line (after basic cleaning)
    function getLastWord(line) {
         if (!line) return '';
         const words = line.trim().split(/\s+/);
         return words.length > 0 ? words[words.length - 1] : '';
    }

     // Helper: Show error message
     function showError(element, message) {
         element.textContent = message;
         element.style.display = 'block';
     }

     // Helper: Hide error message
     function hideError(element) {
         element.textContent = '';
         element.style.display = 'none';
     }


     // Show/Hide screens with transitions
    function showScreen(screenId) {
        // Hide all poem apps first
        [limerickApp, sestinaApp].forEach(app => {
             app.style.opacity = 0;
             app.style.display = 'none';
        });
         choiceScreen.style.opacity = 0;
         choiceScreen.style.display = 'none';


        // Show the chosen screen
        let targetScreen;
        if (screenId === 'choice') targetScreen = choiceScreen;
        else if (screenId === 'limerick') targetScreen = limerickApp;
        else if (screenId === 'sestina') targetScreen = sestinaApp;

         if (targetScreen) {
             targetScreen.style.display = 'block';
             // Use requestAnimationFrame to ensure display: block is applied before starting transition
             requestAnimationFrame(() => {
                 requestAnimationFrame(() => {
                      targetScreen.style.opacity = 1;
                 });
             });
         }
    }

    // Limerick Functions
    function startLimerick() {
        currentPoemType = 'limerick';
        limerickLineCount = 0;
        limerickLines = [];
        limerickStanzaDiv.innerHTML = '';
        hideError(limerickErrorDiv);
        limerickResultDiv.style.display = 'none';
        resetLimerickBtn.style.display = 'none';
        limerickCurrentLineDiv.style.display = 'flex'; // Use flex for layout

        updateLimerickUI();
        showScreen('limerick');
    }

    function updateLimerickUI() {
        hideError(limerickErrorDiv);
        if (limerickLineCount < 5) {
            limerickLineNumSpan.textContent = limerickLineCount + 1;
            limerickRhymeSpan.textContent = `חרוז ${limerickRhymeScheme[limerickLineCount]}`;
            limerickInfoDiv.textContent = limerickInfoHints[limerickLineCount];
             limerickLineInput.disabled = false;
             addLimerickLineBtn.disabled = false;
        } else {
            limerickCurrentLineDiv.style.display = 'none';
            limerickInfoDiv.textContent = 'סיימתם את הלימריק! קראו אותו למטה.';
            displayPoem('limerick');
        }
         limerickLineInput.value = '';
         limerickLineInput.focus();
    }

    function addLimerickLine() {
        hideError(limerickErrorDiv);
        const line = limerickLineInput.value.trim();
        if (!line) {
            showError(limerickErrorDiv, '⚠️ אנא כתבו שורה כלשהי.');
            return;
        }

        limerickLines.push(line);

        // Add line to display with animation
        const lineElement = document.createElement('p');
        lineElement.textContent = `${limerickLineCount + 1}. ${line}`;
        limerickStanzaDiv.appendChild(lineElement);
         // Trigger fade-in animation
         requestAnimationFrame(() => {
              lineElement.classList.add('fade-in');
         });


        limerickLineCount++;
        updateLimerickUI();
    }

     // Display finished poem
     function displayPoem(type) {
         if (type === 'limerick') {
             displayLimerickPre.textContent = limerickLines.join('\n');
             limerickResultDiv.style.display = 'block';
             resetLimerickBtn.style.display = 'block';
         } else if (type === 'sestina') {
             let poemText = '';
             sestinaLines.forEach((stanza, sIndex) => {
                 poemText += `***\nבית ${sIndex + 1}:\n`; // Add a clear separator for stanzas
                 stanza.forEach(line => {
                     poemText += `${line}\n`;
                 });
                 // poemText += '\n'; // Add extra space between stanzas in pre
             });
              if (envoiLines.length === 3) {
                  poemText += `\n***\nבית הסיום (אנווי):\n`;
                  envoiLines.forEach(line => {
                       poemText += `${line}\n`;
                  });
              }
             displaySestinaPre.textContent = poemText;
             sestinaResultDiv.style.display = 'block';
             resetSestinaBtn.style.display = 'block';
         }
     }

    // Sestina Functions
     // Generates the order of *indices* for each stanza based on the initial words
     function generateSestinaPermutations(words) {
         if (words.length !== 6) return []; // Should not happen if logic is correct
         let permutations = [];
         // The pattern defines the order of the *original indices* (0-5)
         sestinaPermutationPattern.forEach(pattern => {
             // Map the indices from the pattern to the actual words array order
             // This step is actually redundant if we use the pattern directly to pick words,
             // but keeping it conceptually clear. The pattern *is* the permutation of indices.
         });
         return sestinaPermutationPattern; // The pattern itself is the list of index orders
     }


    function startSestina() {
        currentPoemType = 'sestina';
        sestinaStanzaCount = 0;
        sestinaLineCount = 0;
        envoiLineCount = 0;
        sestinaEndWords = [];
        sestinaWordPermutations = [];
        sestinaLines = [];
        envoiLines = [];

        sestinaStanzaDiv.innerHTML = '';
        sestinaEndWordsDisplayDiv.style.display = 'none';
        sestinaResultDiv.style.display = 'none';
        resetSestinaBtn.style.display = 'none';
        sestinaEnvoiDiv.style.display = 'none';
        sestinaCurrentLineDiv.style.display = 'flex'; // Use flex for layout
        hideError(sestinaErrorDiv);


        updateSestinaUI();
        showScreen('sestina');
    }

    function updateSestinaUI() {
        hideError(sestinaErrorDiv);
        sestinaLineInput.disabled = false;
        addSestinaLineBtn.disabled = false;

        if (sestinaStanzaCount < 6) {
            sestinaStanzaNumSpan.textContent = sestinaStanzaCount + 1;
            sestinaLineNumSpan.textContent = sestinaLineCount + 1;

            let instruction = 'כתוב שורה';
            let infoText = '';

            if (sestinaStanzaCount > 0) { // Stanzas 2-6
                 if (sestinaWordPermutations.length === 0) { // Should not happen after stanza 1
                     showError(sestinaErrorDiv, 'שגיאה פנימית: לא נמצאו מילות סיום.');
                     sestinaLineInput.disabled = true;
                     addSestinaLineBtn.disabled = true;
                     return;
                 }
                 const requiredWordIndex = sestinaWordPermutations[sestinaStanzaCount][sestinaLineCount];
                 const requiredWord = sestinaEndWords[requiredWordIndex];
                 instruction = `חייבת להסתיים במילה: <strong style="color: var(--primary-color);">${requiredWord}</strong>`;

                 // Display the permutation for the current stanza
                 const currentStanzaWords = sestinaWordPermutations[sestinaStanzaCount].map(idx => sestinaEndWords[idx]);
                 infoText = `🔄 סדר מילות הסיום בבית ${sestinaStanzaCount + 1}: ${currentStanzaWords.join(', ')}`;
                 sestinaInfoDiv.textContent = infoText;
                 sestinaPermutationInfoSpan.textContent = infoText; // Update display below end words

            } else { // First stanza (Stanza 1)
                 instruction = `(מילת הסיום בשורה זו תילכד כמילת מפתח מס' ${sestinaLineCount + 1}).`;
                 infoText = `📍 בבית הראשון, מילות הסיום של שש השורות שתכתוב (${sestinaEndWords.length}/6) יהפכו למילות המפתח של כל הססטינה.`;
                 sestinaInfoDiv.textContent = infoText;
                 sestinaPermutationInfoSpan.textContent = ''; // No permutation info yet
                 sestinaEndWordsDisplayDiv.style.display = 'none'; // Hide until 6 words are captured
            }
             sestinaLineInstructionSpan.innerHTML = instruction;

            sestinaLineInput.value = '';
            sestinaLineInput.focus();

        } else if (sestinaStanzaCount === 6) { // Start Envoi after 6 stanzas
             sestinaCurrentLineDiv.style.display = 'none';
             sestinaInfoDiv.textContent = 'עוברים לבית הסיום...';
             // Animate Envoi section appearance
             sestinaEnvoiDiv.style.opacity = 0;
             sestinaEnvoiDiv.style.display = 'block';
             requestAnimationFrame(() => {
                  requestAnimationFrame(() => {
                       sestinaEnvoiDiv.style.opacity = 1;
                  });
             });
             startEnvoi();
        }
    }

    function addSestinaLine() {
        hideError(sestinaErrorDiv);
        const line = sestinaLineInput.value.trim();
        if (!line) {
            showError(sestinaErrorDiv, '⚠️ אנא כתבו שורה כלשהי.');
            return;
        }

        const submittedLastWord = getLastWord(line);
         if (!submittedLastWord && sestinaStanzaCount > 0) { // Require non-empty last word in subsequent stanzas
              showError(sestinaErrorDiv, '⚠️ השורה לא יכולה להסתיים ברווחים בלבד. אנא ודאו שיש מילה בסוף השורה.');
              return;
         }


        if (sestinaStanzaCount === 0) { // First stanza - capture end words
             if (!submittedLastWord) {
                  showError(sestinaErrorDiv, '⚠️ בבית הראשון, כל שורה חייבת להסתיים במילה כדי שנוכל ללכוד את מילות המפתח.');
                  return;
             }
            sestinaEndWords.push(submittedLastWord); // Store raw word, clean for comparison/display later
            if (sestinaEndWords.length === 6) {
                 sestinaWordPermutations = generateSestinaPermutations(sestinaEndWords);
                 displaySestinaEndWordsSpan.textContent = sestinaEndWords.join(', ');
                 sestinaEndWordsDisplayDiv.style.display = 'block';
                 // Add fade-in to the display div itself
                  sestinaEndWordsDisplayDiv.style.opacity = 0;
                 requestAnimationFrame(() => {
                      requestAnimationFrame(() => {
                           sestinaEndWordsDisplayDiv.style.opacity = 1;
                      });
                 });
            }

        } else { // Subsequent stanzas - validate end word
             const requiredWordIndex = sestinaWordPermutations[sestinaStanzaCount][sestinaLineCount];
             const requiredWord = sestinaEndWords[requiredWordIndex];
             const cleanedSubmittedLastWord = cleanWord(submittedLastWord);
             const cleanedRequiredWord = cleanWord(requiredWord);


             if (cleanedSubmittedLastWord !== cleanedRequiredWord) {
                 showError(sestinaErrorDiv, `❌ שגיאת מילת סיום: השורה חייבת להסתיים במילה "${requiredWord}". המילה האחרונה שכתבת (אחרי ניקוי) היא "${submittedLastWord}".`);
                 return;
             }
        }

        // Add line to stanza structure
        if (!sestinaLines[sestinaStanzaCount]) {
            sestinaLines[sestinaStanzaCount] = [];
        }
        sestinaLines[sestinaStanzaCount].push(line);

        // Display line
         const lineElement = document.createElement('p');
         lineElement.textContent = `${sestinaStanzaCount + 1}.${sestinaLineCount + 1}. ${line}`;
         sestinaStanzaDiv.appendChild(lineElement);
         // Trigger fade-in animation
         requestAnimationFrame(() => {
              lineElement.classList.add('fade-in');
         });


        sestinaLineCount++;

        if (sestinaLineCount === 6) { // Stanza finished
             sestinaStanzaCount++;
             sestinaLineCount = 0;
             if (sestinaStanzaCount < 6) {
                 // Add a separator with animation? HR doesn't animate well. Maybe a div?
                 // For now, just add HR.
                 const stanzaSeparator = document.createElement('hr'); // Add a separator between stanzas
                 sestinaStanzaDiv.appendChild(stanzaSeparator);
             }
        }

        updateSestinaUI();
    }

     // Envoi Functions
     function startEnvoi() {
         envoiLineCount = 0;
         envoiLines = [];
         envoiLinesDiv.innerHTML = '';
         sestinaCurrentEnvoiLineDiv.style.display = 'flex'; // Use flex for layout
         hideError(sestinaErrorDiv);

         updateEnvoiUI();
     }

     function updateEnvoiUI() {
         hideError(sestinaErrorDiv);
          envoiLineInput.disabled = false;
          addEnvoiLineBtn.disabled = false;

         if (envoiLineCount < 3) {
              envoiLineNumSpan.textContent = envoiLineCount + 1;
              const word1 = sestinaEndWords[envoiWordPairs[envoiLineCount][0]];
              const word2 = sestinaEndWords[envoiWordPairs[envoiLineCount][1]];
              envoiWord1Spans.forEach(span => span.textContent = word1);
              envoiWord2Spans.forEach(span => span.textContent = word2);

              envoiLineInput.value = '';
              envoiLineInput.focus();
         } else { // Envoi finished
              sestinaCurrentEnvoiLineDiv.style.display = 'none';
              sestinaInfoDiv.textContent = 'סיימתם את הססטינה המפוארת!';
              displayPoem('sestina');
         }
     }

     function addEnvoiLine() {
         hideError(sestinaErrorDiv);
         const line = envoiLineInput.value.trim();
         if (!line) {
              showError(sestinaErrorDiv, '⚠️ אנא כתבו שורה כלשהי.');
              return;
         }
         const submittedLastWord = getLastWord(line);

         const requiredWord1 = sestinaEndWords[envoiWordPairs[envoiLineCount][0]];
         const requiredWord2 = sestinaEndWords[envoiWordPairs[envoiLineCount][1]];

         // Validate envoi line: Must contain word1 and end with word2
          const cleanedLine = cleanWord(line);
          const cleanedWord1 = cleanWord(requiredWord1);
          const cleanedWord2 = cleanWord(requiredWord2);
          const cleanedSubmittedLastWord = cleanWord(submittedLastWord);


         if (cleanedSubmittedLastWord !== cleanedWord2) {
               showError(sestinaErrorDiv, `❌ שגיאת מילת סיום: שורת האנווי חייבת להסתיים במילה "${requiredWord2}". המילה האחרונה שכתבת היא "${submittedLastWord}".`);
               return;
         }

          // Check if word1 is included anywhere in the line (case-insensitive, ignore punctuation)
          // Need to check for word boundary to avoid matching "apple" in "pineapple"
          const word1Regex = new RegExp(`\\b${cleanedWord1}\\b`, 'i'); // Use \b for word boundary, i for case-insensitive
          if (!word1Regex.test(cleanedLine)) {
               showError(sestinaErrorDiv, `❌ שגיאת מילה חסרה: שורת האנווי חייבת להכיל את המילה "${requiredWord1}".`);
               return;
          }


         envoiLines.push(line);

         // Display line
         const lineElement = document.createElement('p');
         lineElement.textContent = `אנווי ${envoiLineCount + 1}. ${line}`;
         envoiLinesDiv.appendChild(lineElement);
         // Trigger fade-in animation
         requestAnimationFrame(() => {
              lineElement.classList.add('fade-in');
         });

         envoiLineCount++;
         updateEnvoiUI();
     }


     // Reset function
     function resetApp() {
         currentPoemType = null;
         limerickLineCount = 0;
         limerickLines = [];
         sestinaStanzaCount = 0;
         sestinaLineCount = 0;
         envoiLineCount = 0;
         sestinaEndWords = [];
         sestinaWordPermutations = [];
         sestinaLines = [];
         envoiLines = [];

         limerickStanzaDiv.innerHTML = '';
         sestinaStanzaDiv.innerHTML = '';
         envoiLinesDiv.innerHTML = '';

         limerickResultDiv.style.display = 'none';
         sestinaResultDiv.style.display = 'none';
         hideError(limerickErrorDiv);
         hideError(sestinaErrorDiv);

         showScreen('choice');
         // Hide explanation when resetting
          explanationDiv.style.display = 'none';
          showExplanationBtn.textContent = '📜 הצג הסבר על מבנים שיריים';
     }


    // Event Listeners
    limerickBtn.addEventListener('click', startLimerick);
    sestinaBtn.addEventListener('click', startSestina);
    addLimerickLineBtn.addEventListener('click', addLimerickLine);
     resetLimerickBtn.addEventListener('click', resetApp);
    addSestinaLineBtn.addEventListener('click', addSestinaLine);
     addEnvoiLineBtn.addEventListener('click', addEnvoiLine);
     resetSestinaBtn.addEventListener('click', resetApp);

    // Allow pressing Enter to add line
    limerickLineInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault(); // Prevent default form submission
            addLimerickLineBtn.click();
        }
    });
     sestinaLineInput.addEventListener('keypress', function(event) {
         if (event.key === 'Enter') {
             event.preventDefault();
             addSestinaLineBtn.click();
         }
     });
      envoiLineInput.addEventListener('keypress', function(event) {
          if (event.key === 'Enter') {
              event.preventDefault();
              addEnvoiLineBtn.click();
          }
      });


    showExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        // Use requestAnimationFrame for smoother toggle
        if (isHidden) {
             explanationDiv.style.display = 'block';
             requestAnimationFrame(() => {
                 explanationDiv.style.opacity = 0; // Start invisible
                  requestAnimationFrame(() => {
                       explanationDiv.style.opacity = 1; // Fade in
                       explanationDiv.style.transition = 'opacity 0.5s ease-in-out';
                  });
             });
        } else {
             explanationDiv.style.opacity = 0;
             explanationDiv.style.transition = 'opacity 0.5s ease-in-out';
             // Hide after transition completes
             explanationDiv.addEventListener('transitionend', function handler() {
                  explanationDiv.style.display = 'none';
                   explanationDiv.style.transition = ''; // Remove listener after one use
                  explanationDiv.removeEventListener('transitionend', handler);
             });
        }
        showExplanationBtn.textContent = isHidden ? '🙈 הסתר הסבר' : '📜 הצג הסבר על מבנים שיריים';
    });


    // Initial state
    showScreen('choice');

</script>
---
```