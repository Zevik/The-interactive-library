---
title: "מנהל קרן גידור לרגע: האם תצליח לגבור על השוק והפסיכולוגיה?"
english_slug: hedge-fund-manager-decision-simulator
category: "מדעי החברה / כלכלה התנהגותית"
tags:
  - קרן גידור
  - קבלת החלטות
  - סיכון
  - כלכלה התנהגותית
  - השקעות
  - פסיכולוגיה
---
# מנהל קרן גידור לרגע: האם תצליח לגבור על השוק והפסיכולוגיה?

דמיינו את עצמכם יושבים בלב המרכז הפיננסי, מול מסכים מהבהבים, כשמיליוני דולרים של משקיעים נסמכים על שיקול דעתכם. כל החלטה יכולה להקפיץ את הפורטפוליו שלכם לגבהים חדשים - או לנפץ אותו לרסיסים. האם תצליחו לשמור על קור רוח ולקבל החלטות רציונליות תחת לחץ, או שהטיות פסיכולוגיות ישפיעו על שיקול דעתכם? היכנסו לנעליו של מנהל קרן גידור ובדקו את עצמכם בסימולטור אינטראקטיבי!

<div id="app-container" class="game-font">
  <div id="game-area" class="card">
    <div class="game-header">
      <h2>הפורטפוליו שלך: <span id="portfolio-value" class="value-display"></span></h2>
      <div class="round-info">
          <div id="timer-area">זמן לסיבוב: <span id="time-left" class="value-display"></span> שניות</div>
          <div id="round-area">סיבוב <span id="current-round" class="value-display"></span> מתוך <span id="total-rounds" class="value-display"></span></div>
      </div>
    </div>
    
    <div id="scenario-area">
      <h3>תרחיש נוכחי:</h3>
      <p id="scenario-text" class="scenario-desc"></p>
      <div id="potential-outcomes" class="card outcomes-card">
        <h4>תוצאות פוטנציאליות (מוערך):</h4>
      </div>
    </div>
    
    <div id="decision-area">
      <h3>החלטה גורלית:</h3>
      <div class="decision-options">
        <button data-decision="invest" class="btn btn-invest">השקע סכום נבחר</button>
        <button data-decision="no-invest" class="btn btn-no-invest">אל תשקיע הפעם</button>
        <!-- <button data-decision="hedge" class="btn btn-hedge">גדר סיכון</button> <!-- Hedge option is less common in basic sims -->
      </div>
      <div id="investment-input" class="card input-card" style="display: none;">
        <label for="invest-amount">סכום השקעה (עד ערך הפורטפוליו):</label>
        <input type="number" id="invest-amount" min="1000" step="5000" placeholder="לדוגמה: 100000">
        <button id="submit-decision" class="btn btn-submit">אשר השקעה</button>
      </div>
    </div>
    
    <div id="result-area" class="card result-card" style="display: none;">
      <h3>תוצאת הסיבוב: <span id="result-icon"></span></h3>
      <p id="result-text"></p>
      <button id="next-round-button" class="btn btn-next">המשך לסיבוב הבא</button>
    </div>

    <div id="final-result-area" class="card final-result-card" style="display: none;">
      <h3>סימולציה הסתיימה!</h3>
      <p id="final-portfolio" class="final-value"></p>
      <h4>ניתוח סגנון קבלת ההחלטות שלך:</h4>
      <p id="analysis-text" class="analysis-text"></p>
      <button id="restart-button" class="btn btn-restart">שחק שוב</button>
    </div>
     <div class="bias-hint" id="bias-hint" style="display: none;">
        <p>רמז להטיה פסיכולוגית רלוונטית:</p>
        <p class="hint-text" id="hint-text"></p>
    </div>
  </div>

  <button id="toggle-explanation" class="btn btn-toggle-explanation">הצג הסבר תיאורטי והטיות נפוצות</button>

  <div id="explanation-area" class="card explanation-card" style="display: none;">
    <h2>הסבר תיאורטי: מאחורי ההחלטות בקרן גידור</h2>
    <p>קבלת החלטות בשוק ההון, במיוחד בקרנות גידור המנהלות סכומים עצומים תחת לחץ ותנודתיות גבוהה, היא תהליך מורכב ביותר. הוא אינו מושתת רק על ניתוח אנליטי ורציונלי של נתונים, אלא מושפע עמוקות מפסיכולוגיה אנושית ומגוון הטיות קוגניטיביות.</p>

    <h3>מהי קרן גידור ומדוע קבלת החלטות בה כה מורכבת?</h3>
    <p>קרן גידור היא שותפות השקעה פרטית המשתמשת במגוון אסטרטגיות השקעה, כולל שימוש במינוף (הלוואות להגדלת פוזיציה) ופוזיציות שורט (מכירה בחסר מתוך ציפייה לירידת מחיר), במטרה להשיג תשואות אבסולוטיות (רווח ללא תלות בכיוון השוק הכללי) ולגדר סיכונים. המורכבות נובעת מכך שמנהלים נדרשים לקבל החלטות מהירות תחת אי-ודאות גבוהה, עם השלכות כספיות מיידיות ומשמעותיות, תוך כדי ניהול סיכונים מורכבים.</p>

    <h3>מודלים רציונליים מול התנהגות אנושית בשווקים פיננסיים</h3>
    <p>מודלים כלכליים קלאסיים מניחים שהשחקנים בשוק ההון הם רציונליים לחלוטין ומקבלים החלטות על בסיס אופטימיזציה של תועלת מול סיכון. עם זאת, תחום הכלכלה ההתנהגותית, שחוקר את ההשפעה של גורמים פסיכולוגיים, חברתיים ורגשיים על החלטות כלכליות, הראה בעקביות שבפועל, החלטות אנושיות סוטות מהמודל הרציונלי עקב הטיות קוגניטיביות ורגשיות.</p>

    <h3>הטיות קוגניטיביות נפוצות אצל משקיעים:</h3>

    <h4>הטיית האישור (Confirmation Bias)</h4>
    <p>הנטייה לחפש, לפרש, לזכור ולהעדיף מידע שמאשר את האמונות או ההשערות הקיימות שלנו, ולהתעלם ממידע הסותר אותן. מנהל קרן גידור עשוי, לדוגמה, לחפש רק כתבות או נתונים שתומכים בהשקעה שהוא כבר נוטה לבצע, ולהתעלם מאזהרות או אינדיקטורים שליליים.</p>

    <h4>הטיית העיגון (Anchoring Bias)</h4>
    <p>מתרחשת כאשר אנו מסתמכים יתר על המידה על פיסת המידע הראשונה שקיבלנו ("העוגן") בעת קבלת החלטות, גם אם מידע זה אינו רלוונטי. לדוגמה, הערכת שווי ראשונית של נכס (אפילו שגויה) עשויה להוות עוגן שישפיע על כל הערכות השווי והחלטות ההשקעה העתידיות לגביו.</p>

    <h4>שנאת הפסד (Loss Aversion)</h4>
    <p>הנטייה הפסיכולוגית לכך שכאב הפסד מרגיש חזק יותר מהנאת רווח בסדר גודל שווה. נטייה זו יכולה לגרום למשקיעים להימנע מנטילת סיכונים (אף כאלו הכרוכים בסיכוי גבוה לרווח) כאשר הם חוששים מהפסד קטן, או להחזיק בהשקעות מפסידות זמן רב מדי בתקווה שיתאוששו ("לרדוף אחרי ההפסד"), במקום למכור ולהכיר בהפסד.</p>

    <h4>אופוריית יתר והתנהגות עדר (Overconfidence & Herd Behavior)</h4>
    <p>אופוריית יתר היא הערכת יתר של היכולות או הסיכויים שלנו. התנהגות עדר היא הנטייה ללכת בעקבות הרוב, גם כשהמידע הפרטי שלנו מצביע על כיוון אחר. שילוב של השתיים יכול להוביל להשקעות בנכסים "חמים" רק בגלל שהם עולים וכולם משקיעים בהם, תוך התעלמות מסימני אזהרה.</p>
     <h4>היסק נגישות (Availability Heuristic)</h4>
    <p>הנטייה לבסס החלטות על המידע שהכי נגיש לזיכרון, לרוב מידע טרי ובולט (כמו כתבה אחרונה שקראתם או ניסיון אישי קרוב). זה יכול להוביל להתעלמות מסטטיסטיקה רחבה יותר או נתונים היסטוריים.</p>

    <h3>השפעת לחץ וזמן על איכות קבלת ההחלטות</h3>
    <p>קבלת החלטות תחת לחץ זמן ועם סכומים גדולים על הכף עלולה לפגוע ביכולת החשיבה הרציונלית. לחץ יכול להגביר את ההשפעה של הטיות קוגניטיביות, להוביל לקבלת החלטות אימפולסיביות ולהפחית את היכולת לעבד מידע מורכב ביעילות.</p>

    <h3>אסטרטגיות לשיפור קבלת החלטות פיננסיות באמצעות מודעות להטיות</h3>
    <p>המודעות להטיות קוגניטיביות היא הצעד הראשון להתמודדות איתן. אסטרטגיות נוספות כוללות: פיתוח תהליך קבלת החלטות שיטתי, שימוש ברשימות בדיקה (Checklists), קבלת חוות דעת מגוונות (גם כאלו המאתגרות את העמדה הראשונית), הגדרת יעדים וכללי יציאה מראש, והתבוננות עצמית רציפה לאחר קבלת ההחלטות (Post-mortem analysis).</p>
  </div>
</div>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700&display=swap');

  .game-font {
      font-family: 'Heebo', sans-serif;
  }

  #app-container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background: linear-gradient(to bottom right, #eef2f7, #c4d7eb); /* Soft gradient background */
    border-radius: 12px; /* More rounded corners */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    direction: rtl;
    text-align: right;
    color: #333;
  }

  h1, h2, h3, h4 {
    color: #1a3a5a; /* Darker blue for headings */
    text-align: center;
    margin-bottom: 15px;
  }

  h1 {
      font-size: 2em;
      margin-bottom: 25px;
      border-bottom: 2px solid #1a3a5a;
      padding-bottom: 10px;
  }

   h2 {
       font-size: 1.6em;
   }
   h3 {
       font-size: 1.3em;
       margin-top: 20px;
   }

  .card {
    margin-top: 20px;
    padding: 20px; /* Increased padding */
    border: 1px solid #c4d7eb;
    border-radius: 8px;
    background-color: #ffffff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
  }

  .game-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap; /* Allow wrapping on smaller screens */
      margin-bottom: 20px;
      padding-bottom: 10px;
      border-bottom: 1px solid #eee;
  }

  .game-header h2 {
      margin: 0;
      text-align: right; /* Align portfolio left */
      flex-grow: 1; /* Allow it to take space */
  }

  .round-info {
      display: flex;
      gap: 15px; /* Space between timer and round */
      align-items: center;
      font-size: 1em;
      color: #555;
  }
    #timer-area, #round-area {
        display: flex;
        align-items: center;
        gap: 5px;
    }

  .value-display {
    font-weight: 700;
    color: #007bff; /* Blue color for values */
    font-size: 1.1em;
     min-width: 50px; /* Ensure consistent width */
     display: inline-block;
     text-align: left; /* Align values left */
  }
    #portfolio-value {
        font-size: 1.4em;
        color: #28a745; /* Green for portfolio value */
        min-width: 150px;
    }

  #scenario-area h3 {
    margin-top: 0;
    text-align: right;
    color: #1a3a5a;
  }
    .scenario-desc {
        line-height: 1.6;
        color: #555;
        font-size: 1.1em;
    }

  .outcomes-card {
      margin-top: 15px;
      background-color: #f8f9fa; /* Lighter background for outcomes */
      border: 1px dashed #a0b9d6;
      font-size: 0.95em;
      color: #444;
  }
   .outcomes-card h4 {
       margin: 0 0 10px 0;
       font-size: 1.1em;
       color: #1a3a5a;
       text-align: right;
       border-bottom: 1px dashed #a0b9d6;
       padding-bottom: 5px;
   }
    .outcomes-card p {
        margin: 5px 0;
    }

  .decision-options {
      display: flex; /* Arrange buttons horizontally */
      justify-content: center; /* Center buttons */
      gap: 15px; /* Space between buttons */
      margin-top: 20px;
      flex-wrap: wrap; /* Allow wrapping on smaller screens */
  }

  .btn {
    padding: 12px 25px; /* Larger padding */
    font-size: 1.1em; /* Larger font */
    cursor: pointer;
    border: none;
    border-radius: 6px; /* Slightly more rounded */
    transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.2s ease;
    font-weight: 500;
    text-align: center;
     min-width: 150px; /* Minimum width for buttons */
  }

  .btn:hover {
    opacity: 0.95;
    transform: translateY(-2px); /* Subtle lift effect */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
    .btn:active {
        transform: translateY(0); /* Press effect */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }


  .btn-invest { background-color: #28a745; color: white; } /* Green */
  .btn-no-invest { background-color: #dc3545; color: white; } /* Red */
  .btn-hedge { background-color: #ffc107; color: #212529; } /* Yellow/Orange */
  .btn-submit { background-color: #007bff; color: white; } /* Blue */
   .btn-next { background-color: #17a2b8; color: white; } /* Cyan/Teal */
   .btn-restart { background-color: #6f42c1; color: white; } /* Purple */
   .btn-toggle-explanation {
       background-color: #6c757d; /* Grey */
        color: white;
        display: block;
        margin: 30px auto 10px auto; /* Center button */
        padding: 10px 20px;
        font-size: 1em;
        width: auto; /* Adjust width based on content */
        min-width: 200px;
   }

  .btn:disabled {
      opacity: 0.6;
      cursor: not-allowed;
      transform: none;
      box-shadow: none;
  }

  .decision-options .btn.selected {
      border: 2px solid #000; /* Highlight selected button */
       box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  }


  .input-card {
    margin-top: 15px;
    padding: 15px;
    background-color: #f0f0f0;
    display: flex; /* Align items horizontally */
    align-items: center;
    gap: 15px; /* Space between elements */
    flex-wrap: wrap;
    justify-content: center;
  }

  #investment-input label {
    font-weight: 500;
    color: #333;
  }

  #investment-input input[type="number"] {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    width: 150px; /* Wider input field */
    text-align: left; /* Numbers align left */
    font-size: 1em;
  }

  .result-card {
    margin-top: 20px;
    padding: 20px;
    text-align: center;
     transition: background-color 0.5s ease; /* Smooth color transition */
  }
    .result-card h3 {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        margin-top: 0;
    }

    #result-area.win {
        background-color: #d4edda; /* Light green */
        border-color: #c3e6cb;
    }
    #result-area.loss {
        background-color: #f8d7da; /* Light red */
        border-color: #f5c6cb;
    }
    #result-area.neutral {
        background-color: #e9ecef; /* Light grey */
        border-color: #dee2e6;
    }

    #result-icon {
        font-size: 1.8em;
        line-height: 1;
    }
     #result-area.win #result-icon { color: #28a745; content: '📈'; }
     #result-area.loss #result-icon { color: #dc3545; content: '📉'; }
     #result-area.neutral #result-icon { color: #6c757d; content: '⚖️'; }


  .final-result-card {
      margin-top: 30px;
      padding: 25px;
      text-align: center;
      background-color: #fff3cd; /* Light yellow for final analysis */
      border-color: #ffeeba;
  }
    .final-result-card h3 {
        color: #856404; /* Dark yellow */
    }
    .final-value {
        font-size: 1.5em;
        font-weight: 700;
        color: #1a3a5a;
        margin-bottom: 20px;
    }
    .analysis-text {
        white-space: pre-wrap; /* Preserve line breaks from JS */
        text-align: right;
        line-height: 1.7;
        color: #555;
    }

  .explanation-card h3 {
      text-align: right;
      margin-top: 20px;
      border-bottom: 1px solid #eee;
      padding-bottom: 5px;
       color: #1a3a5a;
       font-size: 1.2em;
  }

  .explanation-card p {
      line-height: 1.6;
      color: #444;
      margin-bottom: 15px;
  }

    .bias-hint {
        margin-top: 20px;
        padding: 10px 15px;
        border: 1px solid #007bff; /* Blue border */
        border-left: 5px solid #007bff; /* Emphasize border */
        border-radius: 5px;
        background-color: #e9f5ff; /* Light blue background */
        color: #0056b3; /* Darker blue text */
        font-size: 0.95em;
    }
     .bias-hint p { margin: 5px 0 0 0;}
     .bias-hint p:first-child { font-weight: bold; margin-top: 0;}
     .bias-hint .hint-text { font-style: italic; }


  /* Basic Responsiveness */
  @media (max-width: 600px) {
    #app-container {
      padding: 15px;
    }
    .game-header {
        flex-direction: column;
        align-items: flex-end;
    }
    .game-header h2 {
        width: 100%;
        text-align: center;
        margin-bottom: 10px;
    }
    .round-info {
        width: 100%;
        justify-content: center;
    }
    .decision-options {
        flex-direction: column;
        align-items: stretch;
        gap: 10px;
    }
    .btn {
        width: 100%; /* Full width buttons on small screens */
        min-width: auto;
    }
    .input-card {
        flex-direction: column;
        gap: 10px;
        align-items: stretch;
    }
    #investment-input label {
        text-align: center;
    }
    #investment-input input[type="number"] {
        width: 100%;
        box-sizing: border-box; /* Include padding and border in element's total width */
        text-align: center;
    }
    #submit-decision {
         width: 100%;
         box-sizing: border-box;
    }
  }
</style>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const portfolioValueEl = document.getElementById('portfolio-value');
    const timeLeftEl = document.getElementById('time-left');
    const currentRoundEl = document.getElementById('current-round');
    const totalRoundsEl = document.getElementById('total-rounds');
    const scenarioTextEl = document.getElementById('scenario-text');
    const potentialOutcomesEl = document.getElementById('potential-outcomes');
    const decisionAreaEl = document.getElementById('decision-area');
    const investmentInputEl = document.getElementById('investment-input');
    const investAmountInput = document.getElementById('invest-amount');
    const submitDecisionButton = document.getElementById('submit-decision');
    const resultAreaEl = document.getElementById('result-area');
    const resultTextEl = document.getElementById('result-text');
    const resultIconEl = document.getElementById('result-icon'); // New element for icon
    const nextRoundButton = document.getElementById('next-round-button');
    const finalResultAreaEl = document.getElementById('final-result-area');
    const finalPortfolioEl = document.getElementById('final-portfolio');
    const analysisTextEl = document.getElementById('analysis-text');
    const restartButton = document.getElementById('restart-button');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationAreaEl = document.getElementById('explanation-area');
    const decisionButtons = document.querySelectorAll('.decision-options button');
    const biasHintAreaEl = document.getElementById('bias-hint');
    const biasHintTextEl = document.getElementById('hint-text');


    let portfolio = 1000000; // Starting portfolio value
    let currentRound = 0;
    const totalRounds = 5; // Number of game rounds
    let timer;
    const roundDuration = 25; // seconds (slightly less pressure)
    let timeRemaining;
    let userDecision = null;
    let investmentAmount = 0;
    const decisionHistory = [];

     // Store original scenarios to avoid modifying probabilities during play
    const originalScenarios = [
      {
        description: "יש שמועות חזקות על תרופת פלא שחברה קטנה מפתחת. הסיכוי לאישור גבוה, אבל גם הסיכון לכישלון מלא קיים. אנליסט מוביל פרסם יעד מחיר אופטימי במיוחד, שמשגע את השוק.",
        outcomes: [
          { label: "אישור מוצלח - עלייה חדה", value: 0.8, probability: 0.4 }, // 80% gain
          { label: "אישור חלקי - עלייה מתונה", value: 0.2, probability: 0.3 }, // 20% gain
          { label: "כישלון מוחלט - צלילה", value: -0.5, probability: 0.3 } // 50% loss
        ],
        biasHint: "הטיית העיגון (התמקדות ביעד המחיר הגבוה) והטיית האישור (חיפוש מידע חיובי על השמועות)"
      },
      {
        description: "מניית ענק טכנולוגיה ירדה משמעותית לאחרונה עקב חששות רגולטוריים כבדים. נראה שהשוק מגיב בפאניקה, אך הנתונים הפיננסיים היבשים של החברה עדיין חזקים מאוד. הסיכון קיים, אך האם זו הזדמנות קנייה נדירה, או 'סכין נופלת'?",
        outcomes: [
          { label: "החששות מתפוגגים והשוק מתאושש - עלייה חזרה", value: 0.3, probability: 0.4 }, // 30% gain
          { label: "המצב נשאר מעורפל - סטגנציה/ירידה קלה", value: -0.05, probability: 0.3 }, // 5% loss
          { label: "רגולציה קשה מתממשת - ירידה נוספת ועמוקה", value: -0.2, probability: 0.3 } // 20% loss
        ],
        biasHint: "שנאת הפסד (פחד להפסיד עוד על מניה יורדת) והיסק נגישות (זכרון ההפסד הטרי)"
      },
       {
        description: "ממשלה גדולה הודיעה במפתיע על שינוי מדיניות סחר דרמטי שעשוי לפגוע קשות או להיטיב משמעותית עם סקטור תעשייתי ספציפי. הניתוחים הראשונים סותרים, ויש אי-ודאות קיצונית לגבי ההשפעה הסופית.",
        outcomes: [
          { label: "ההשפעה חיובית מהצפוי - עלייה משמעותית", value: 0.15, probability: 0.35 }, // 15% gain
          { label: "ההשפעה שלילית מהצפוי - ירידה משמעותית", value: -0.15, probability: 0.35 }, // 15% loss
          { label: "ההשפעה מינורית מהצפוי - שינוי קטן מאוד", value: 0.02, probability: 0.3 } // 2% gain
        ],
        biasHint: "הימנעות מאי-ודאות (Ambiguity Aversion)"
      },
       {
        description: "חברת סטארטאפ מבטיחה בתחום האנרגיה הנקייה מנפיקה לראשונה בבורסה ב"הייפ" תקשורתי עצום. לחברה עדיין אין הכנסות משמעותיות והיא שורפת מזומנים, אך הפוטנציאל הטכנולוגי נראה ענק. הסיכון גבוה מאוד, אך מה עם הפוטנציאל לתשואה אגדית?",
        outcomes: [
          { label: "הנפקה מוצלחת והמשך טיסה - עלייה עצומה", value: 1.5, probability: 0.2 }, // 150% gain
          { label: "מסחר סביר ותחילת דרך יציבה - עלייה מתונה", value: 0.1, probability: 0.3 }, // 10% gain
          { label: "הייפ מתפוגג והמציאות מכה - צלילה חדה", value: -0.6, probability: 0.5 } // 60% loss
        ],
        biasHint: "אופוריית יתר (Overconfidence Bias) והתעלמות משיעור הבסיס (התעלמות מסטטיסטיקות כישלון סטארטאפים)"
      },
      {
        description: "מטבע קריפטוגרפי אלמוני צבר תאוצה ויראלית מפתיעה בשבועות האחרונים, ללא סיבה כלכלית נראית לעין. אין לו יסודות ברורים, והוא נסחר רק בבורסות קטנות ופרועות, אך התשואה האחרונה מסחררת. האם זה בועה שתתנפץ או רק ההתחלה של 'הדבר הבא'?",
        outcomes: [
          { label: "בול רחב נוסף - עלייה מטורפת", value: 2.0, probability: 0.1 }, // 200% gain
          { label: "התייצבות ומימוש רווחים - שינוי קטן", value: 0.05, probability: 0.2 }, // 5% gain
          { label: "קריסה מוחלטת ואיבוד ערך - ירידה קיצונית", value: -0.9, probability: 0.7 } // 90% loss
        ],
        biasHint: "התנהגות עדר (הרצון 'להיות בפנים') והיסק נגישות (התמקדות בתשואות האחרונות)"
      }
    ];

    // Use a copy of scenarios for runtime, keep original pristine
    let scenarios = JSON.parse(JSON.stringify(originalScenarios));


    function formatCurrency(value) {
        return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 }).format(value);
    }

    function startGame() {
      portfolio = 1000000;
      currentRound = 0;
      decisionHistory.length = 0; // Clear history
      // Reset scenarios to original state for a new game
      scenarios = JSON.parse(JSON.stringify(originalScenarios));

      portfolioValueEl.textContent = formatCurrency(portfolio);
      totalRoundsEl.textContent = totalRounds;

      finalResultAreaEl.style.display = 'none';
      resultAreaEl.style.display = 'none';
      decisionAreaEl.style.display = 'block';
      investmentInputEl.style.display = 'none';
      biasHintAreaEl.style.display = 'none'; // Hide hint at start
      decisionButtons.forEach(btn => btn.disabled = false);
      submitDecisionButton.style.display = 'none';

      startRound();
    }

    function startRound() {
      currentRound++;
      if (currentRound > totalRounds) {
        endGame();
        return;
      }

      currentRoundEl.textContent = currentRound;
      resultAreaEl.style.display = 'none';
      decisionAreaEl.style.display = 'block';
      investmentInputEl.style.display = 'none';
      submitDecisionButton.style.display = 'none';
      resultAreaEl.className = 'card result-card'; // Reset result card class
      resultIconEl.textContent = ''; // Clear icon

      decisionButtons.forEach(btn => {
        btn.disabled = false;
        btn.classList.remove('selected');
      });
      investAmountInput.value = '';
      userDecision = null;
      investmentAmount = 0;

      const scenario = scenarios[currentRound - 1];
      scenarioTextEl.textContent = scenario.description;
      potentialOutcomesEl.innerHTML = '<h4>תוצאות פוטנציאליות (מוערך):</h4>'; // Clear previous outcomes
      scenario.outcomes.forEach(outcome => {
          const outcomeEl = document.createElement('p');
          const outcomeValue = outcome.value > 0 ? `+${(outcome.value*100).toFixed(0)}%` : `${(outcome.value*100).toFixed(0)}%`;
          outcomeEl.textContent = `- ${outcome.label}: שינוי של ${outcomeValue}`;
          potentialOutcomesEl.appendChild(outcomeEl);
      });

      // Display bias hint for the scenario
      biasHintTextEl.textContent = scenario.biasHint;
      biasHintAreaEl.style.display = 'block';


      timeRemaining = roundDuration;
      timeLeftEl.textContent = timeRemaining;
      // Add a visual cue for the timer if needed (CSS transition or animation)
      document.getElementById('timer-area').style.color = '#007bff'; // Reset timer color
      timer = setInterval(updateTimer, 1000);
    }

    function updateTimer() {
      timeRemaining--;
      timeLeftEl.textContent = timeRemaining;

      // Change timer color as time runs out
      if (timeRemaining <= 10) {
          document.getElementById('timer-area').style.color = '#ffc107'; // Warning color
      }
      if (timeRemaining <= 5) {
           document.getElementById('timer-area').style.color = '#dc3545'; // Danger color
      }

      if (timeRemaining <= 0) {
        clearInterval(timer);
         // Default decision if no decision is made within time
        if (userDecision === null) {
            userDecision = 'timeout-no-invest'; // Mark as timeout decision
            investmentAmount = 0;
            processDecision(); // Process with default decision
        }
      }
    }

    function handleDecisionClick(event) {
        if (timeRemaining <= 0) return; // Prevent decisions after timer runs out

        userDecision = event.target.dataset.decision;
        decisionButtons.forEach(btn => {
            btn.classList.remove('selected');
            btn.disabled = true; // Disable all decision buttons immediately
        });
        event.target.classList.add('selected');

        if (userDecision === 'invest' || userDecision === 'hedge') {
            investmentInputEl.style.display = 'block';
            submitDecisionButton.style.display = 'inline-block';
            // Suggest a reasonable amount, maybe 10% or 20% of portfolio
            const suggestedAmount = Math.max(10000, Math.floor(portfolio * 0.1 / 10000) * 10000); // Suggest min 10k, rounded
            investAmountInput.value = suggestedAmount;
            investAmountInput.max = portfolio;
            investAmountInput.min = 1000; // Prevent investing tiny amounts
            investAmountInput.focus();
        } else { // No Invest
            investmentAmount = 0;
            processDecision(); // Process "No Invest" immediately
        }
    }

    function handleSubmitDecision() {
        const amount = parseInt(investAmountInput.value, 10);
        // Validate amount
        if (isNaN(amount) || amount <= 0 || amount > portfolio) {
             alert(`סכום השקעה לא תקין. אנא הזן סכום חיובי (מינימום ${formatCurrency(1000)}) שאינו עולה על ערך הפורטפוריו (${formatCurrency(portfolio)}).`);
             // Re-enable buttons and reset if validation fails
             decisionButtons.forEach(btn => btn.disabled = false);
             document.querySelector(`.decision-options button[data-decision="${userDecision}"]`).classList.remove('selected');
             investmentInputEl.style.display = 'none';
             submitDecisionButton.style.display = 'none';
             userDecision = null; // Reset decision state
             return;
         }
         investmentAmount = amount;
         processDecision(); // Process valid investment/hedge decision
    }

    function processDecision() {
        clearInterval(timer); // Stop the timer
        biasHintAreaEl.style.display = 'none'; // Hide hint after decision is made
        decisionAreaEl.style.display = 'none';
        investmentInputEl.style.display = 'none'; // Hide input area

        const scenario = scenarios[currentRound - 1];
        let outcome = 0;
        let outcomeDescription = "";
        let profitLoss = 0;
        let decisionTextDisplay = userDecision; // Store original user decision string for display

        if (userDecision === 'timeout-no-invest') {
             outcomeDescription = "לא התקבלה החלטה בזמן.";
             decisionTextDisplay = "פסק זמן - אין השקעה";
             profitLoss = 0;
             resultTextEl.textContent = outcomeDescription + " הפורטפוליו נשאר ללא שינוי מסיבוב זה.";
             resultAreaEl.classList.add('neutral');
             resultIconEl.textContent = '⏳'; // Timeout icon
        } else if (userDecision === 'no-invest') {
            outcomeDescription = "החלטת לא להשקיע.";
            profitLoss = 0;
            resultTextEl.textContent = outcomeDescription + " הפורטפוליו נשאר ללא שינוי מסיבוב זה.";
             resultAreaEl.classList.add('neutral');
             resultIconEl.textContent = '🛡️'; // Shield icon for avoiding risk
        } else if (userDecision === 'invest' || userDecision === 'hedge') {
             // Determine actual outcome based on probabilities
             let random = Math.random();
             let cumulativeProbability = 0;
             let chosenOutcome = null;

             // Note: The original code attempted to bias outcome probability based on user decision.
             // This is complex to do realistically and risks making the simulation unfair.
             // A better approach for learning is to stick to the *stated* probabilities
             // and analyze the *user's pattern* vs the *bias hint* after the fact.
             // So, we'll use the original probabilities from the scenario.

             const currentScenarioOutcomes = scenarios[currentRound - 1].outcomes; // Use current scenario outcomes

             for (const out of currentScenarioOutcomes) {
                 cumulativeProbability += out.probability;
                 if (random <= cumulativeProbability) {
                     chosenOutcome = out;
                     break;
                 }
             }

             if (chosenOutcome) {
                 outcome = chosenOutcome.value;
                 outcomeDescription = chosenOutcome.label;
                 profitLoss = investmentAmount * outcome;
                 portfolio += profitLoss;

                 const profitLossText = profitLoss >= 0 ? `רווח של ${formatCurrency(profitLoss)}` : `הפסד של ${formatCurrency(Math.abs(profitLoss))}`;
                 const portfolioChangeText = outcome > 0 ? `עלה ב-${(outcome*100).toFixed(0)}%` : `ירד ב-${(outcome*100).toFixed(0)}%`;


                 resultTextEl.textContent = `החלטת ${userDecision === 'invest' ? 'להשקיע' : 'לגדר סיכון'} ${formatCurrency(investmentAmount)}. התוצאה בפועל: "${outcomeDescription}", המניה ${portfolioChangeText}. סך הכל: ${profitLossText}.`;

                 if (profitLoss >= 0) {
                     resultAreaEl.classList.add('win');
                     resultIconEl.textContent = '✅'; // Win icon
                 } else {
                     resultAreaEl.classList.add('loss');
                     resultIconEl.textContent = '❌'; // Loss icon
                 }

             } else {
                 // Fallback in case of probability issues (should not happen)
                 console.error("Failed to select outcome based on probability. Random:", random, "Cumulative:", cumulativeProbability, "Scenario:", scenario);
                 resultTextEl.textContent = `אירעה שגיאה פנימית בסימולציה. לא בוצעה השקעה או גידור.`;
                 profitLoss = 0;
                 userDecision = 'error'; // Mark decision as error state
                 resultAreaEl.classList.add('neutral');
                 resultIconEl.textContent = '⚠️'; // Warning icon
             }

             decisionTextDisplay = `${userDecision} (${formatCurrency(investmentAmount)})`;

        }


        decisionHistory.push({
            round: currentRound,
            scenarioDescription: scenario.description, // Store full description
            decision: userDecision, // Store the processed decision type (e.g., 'no-invest', 'invest')
            decisionTextDisplay: decisionTextDisplay, // Store formatted text for history display
            amount: investmentAmount,
            outcomeDescription: outcomeDescription,
            outcomeValue: outcome, // Store percentage change
            profitLoss: profitLoss,
            portfolioBefore: portfolio - profitLoss, // Calculate portfolio before
            portfolioAfter: portfolio,
            biasHint: scenario.biasHint // Store the bias hint for analysis
        });

        portfolioValueEl.textContent = formatCurrency(portfolio);
        resultAreaEl.style.display = 'block';

        // Hide/show appropriate buttons
        if (currentRound < totalRounds) {
            nextRoundButton.style.display = 'inline-block';
            restartButton.style.display = 'none';
        } else {
            nextRoundButton.style.display = 'none';
            restartButton.style.display = 'inline-block';
        }
    }

    function endGame() {
      decisionAreaEl.style.display = 'none';
      resultAreaEl.style.display = 'none';
      finalResultAreaEl.style.display = 'block';
      finalPortfolioEl.textContent = `ערך פורטפוליו סופי: ${formatCurrency(portfolio)}.`;

      analyzeDecisions();
    }

    function analyzeDecisions() {
        let analysis = "";
        let totalInvestedAmount = 0;
        let roundsInvested = 0;
        let totalProfit = 0;
        let totalLoss = 0;
        let timeoutCount = 0;

        // Calculate overall stats
        decisionHistory.forEach(entry => {
            if (entry.decision === 'invest' || entry.decision === 'hedge') {
                roundsInvested++;
                totalInvestedAmount += entry.amount;
                if (entry.profitLoss > 0) totalProfit += entry.profitLoss;
                if (entry.profitLoss < 0) totalLoss += entry.profitLoss;
            } else if (entry.decision === 'timeout-no-invest') {
                 timeoutCount++;
            }
        });

        const netResult = totalProfit + totalLoss; // totalLoss is already negative
        const finalPortfolioChange = portfolio - 1000000;

        analysis += `## סיכום ביצועים: ##\n`;
        analysis += `- התחלת עם ${formatCurrency(1000000)} וסיימת עם ${formatCurrency(portfolio)}.\n`;
        analysis += `- שינוי כולל בפורטפוליו: ${formatCurrency(finalPortfolioChange)} (${(finalPortfolioChange / 1000000 * 100).toFixed(1)}%).\n`;

        analysis += `\n## ניתוח החלטות: ##\n`;
        analysis += `- ביצעת השקעה ב-${roundsInvested} מתוך ${totalRounds} סיבובים.\n`;
        if (roundsInvested > 0) {
             analysis += `- סך הכל השקעת/גידרת סכום מצטבר של ${formatCurrency(totalInvestedAmount)}.\n`;
        }
         if (timeoutCount > 0) {
             analysis += `- ב-${timeoutCount} סיבובים לא קיבלת החלטה בזמן המוקצב.\n`;
         }


        analysis += `\n## התמודדות עם הטיות פסיכולוגיות (משוער): ##\n`;

        // Analyze patterns related to biases
        const biasObservations = {};

        decisionHistory.forEach(entry => {
            const biasHint = entry.biasHint;
            if (!biasHint) return; // Skip if no hint

            if (!biasObservations[biasHint]) {
                 biasObservations[biasHint] = {
                     totalRounds: 0,
                     investDecisions: 0,
                     noInvestDecisions: 0,
                     positiveOutcomesWhenInvested: 0,
                     negativeOutcomesWhenInvested: 0,
                     investedAmount: 0,
                     profitLoss: 0
                 };
            }
            biasObservations[biasHint].totalRounds++;
            if (entry.decision === 'invest' || entry.decision === 'hedge') {
                biasObservations[biasHint].investDecisions++;
                biasObservations[biasHint].investedAmount += entry.amount;
                biasObservations[biasHint].profitLoss += entry.profitLoss;
                if (entry.profitLoss > 0) biasObservations[biasHint].positiveOutcomesWhenInvested++;
                if (entry.profitLoss < 0) biasObservations[biasHint].negativeOutcomesWhenInvested++;
            } else if (entry.decision === 'no-invest' || entry.decision === 'timeout-no-invest') {
                 biasObservations[biasHint].noInvestDecisions++;
            }
        });

        for (const bias in biasObservations) {
             const data = biasObservations[bias];
             analysis += `\n**${bias}:**\n`;
             analysis += `- בסיטואציה זו, בחרת ${data.investDecisions} פעמים להשקיע (או לגדר) ו-${data.noInvestDecisions + (data.totalRounds - data.investDecisions - data.noInvestDecisions)} פעמים לא להשקיע (או שהזמן אזל).\n`;

             if (data.investDecisions > 0) {
                 analysis += `  בפעמים שהשקעת: ${data.positiveOutcomesWhenInvested} תוצאות חיוביות, ${data.negativeOutcomesWhenInvested} תוצאות שליליות. סך הכל רווח/הפסד בהשקעות אלו: ${formatCurrency(data.profitLoss)}.\n`;
                 // Add specific bias-related insights based on patterns
                 if (bias.includes("הטיית העיגון") && data.investDecisions > data.noInvestDecisions && data.profitLoss < 0) {
                     analysis += "  ייתכן שהתמקדות בנתון 'עוגן' (כמו יעד מחיר גבוה) השפיעה יתר על המידה על החלטת ההשקעה שלך, למרות הסיכון.\n";
                 }
                 if (bias.includes("הטיית האישור") && data.investDecisions > data.noInvestDecisions && data.negativeOutcomesWhenInvested > data.positiveOutcomesWhenInvested) {
                     analysis += "  ייתכן שחיפשת והתמקדת במידע שתמך בהחלטת ההשקעה שלך, והתעלמת מסימני אזהרה, מה שהוביל להפסדים.\n";
                 }
                  if (bias.includes("שנאת הפסד") && data.noInvestDecisions > data.investDecisions && portfolio < 1000000) {
                     analysis += "  הימנעות מהשקעה במקרה זה (גם אם היו בו סיכויים לרווח) עשויה לנבוע משנאת הפסד, שמונעת נטילת סיכונים גם כשהם מוצדקים סטטיסטית (או פשוט בגלל ההפסד הקודם).\n";
                  }
                  if (bias.includes("שנאת הפסד") && data.investDecisions > data.noInvestDecisions && data.profitLoss < 0 && data.negativeOutcomesWhenInvested > data.positiveOutcomesWhenInvested) {
                      analysis += "  השקעה במקרה זה למרות הסיכון המפורש, ואף שחוית הפסד, עשויה להצביע על נטייה 'לרדוף אחרי ההפסד' בתקווה להחזיר אותו במהירות.\n";
                  }
                 if (bias.includes("אופוריית יתר") && data.investDecisions > data.noInvestDecisions && data.negativeOutcomesWhenInvested > data.positiveOutcomesWhenInvested) {
                      analysis += "  ייתכן שאופוריית יתר והייפ סביב ההזדמנות גרמו לך להעריך יתר על המידה את סיכויי ההצלחה ולהתעלם מהסיכון המשמעותי שהתממש.\n";
                  }
                 if (bias.includes("התנהגות עדר") && data.investDecisions > data.noInvestDecisions && data.negativeOutcomesWhenInvested > data.positiveOutcomesWhenInvested) {
                      analysis += "  ההשקעה במקרה זה, במיוחד אם נבעה מהתלהבות סביב ההזדמנות, עשויה להצביע על נטייה להתנהגות עדר - להצטרף ל'רכבת' גם כשהסיכון גבוה.\n";
                  }
                  if (bias.includes("היסק נגישות") && data.investDecisions > data.noInvestDecisions && data.negativeOutcomesWhenInvested > data.positiveOutcomesWhenInvested) {
                       analysis += "  ייתכן שהחלטתך הושפעה יותר מדי מתוצאות טריות (כמו התשואה המסחררת האחרונה) במקום להסתכל על סיכוני הבסיס הסטטיסטיים.\n";
                   }

             } else if (data.noInvestDecisions > 0) {
                  // Analyze avoidance when the outcome *was* positive (if we knew it)
                  const scenario = originalScenarios.find(s => s.biasHint === bias);
                  if (scenario) {
                       const bestOutcomeValue = Math.max(...scenario.outcomes.map(o => o.value));
                       // This part is tricky - we don't know if the *actual* outcome was positive if they didn't invest.
                       // Let's phrase it around the *potential* missed opportunity based on probabilities.
                       const probOfPositiveOutcome = scenario.outcomes.filter(o => o.value > 0).reduce((sum, o) => sum + o.probability, 0);
                        if (probOfPositiveOutcome > 0.5 && data.noInvestDecisions > data.investDecisions) { // Avoided despite reasonable probability of positive outcome
                            analysis += `  בחרת לא להשקיע, למרות שסיטואציה זו כללה פוטנציאל לרווח עם הסתברות סבירה (${(probOfPositiveOutcome*100).toFixed(0)}% סיכוי לרווח). ייתכן שההטיה הובילה להימנעות יתר.\n`;
                        }
                  }
             }
        }


        analysis += `\nזכור, זהו סימולטור פשטני! בעולם האמיתי, זיהוי הטיות דורש מודעות עמוקה, ניתוח רטרואקטיבי קפדני ותהליך קבלת החלטות מובנה. מודעות להטיות אלו היא צעד חשוב לשיפור ביצועיך הפיננסיים והיכולת שלך לנווט בשווקים מורכבים.\n`;
         analysis += `\nרשומות ההחלטות שלך:\n`;
        decisionHistory.forEach(entry => {
            analysis += `- סיבוב ${entry.round}: החלטה: ${entry.decisionTextDisplay}. תוצאה: "${entry.outcomeDescription}". רווח/הפסד: ${formatCurrency(entry.profitLoss)}. פורטפוליו: ${formatCurrency(entry.portfolioAfter)}.\n`;
        });


        analysisTextEl.textContent = analysis;
    }


    // Event Listeners
    decisionButtons.forEach(button => {
      button.addEventListener('click', handleDecisionClick);
    });

    submitDecisionButton.addEventListener('click', handleSubmitDecision);
    nextRoundButton.addEventListener('click', startRound);
    restartButton.addEventListener('click', startGame);

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationAreaEl.style.display === 'none';
        explanationAreaEl.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר תיאורטי' : 'הצג הסבר תיאורטי והטיות נפוצות';
    });


    // Initial start
    startGame();
  });
</script>
```