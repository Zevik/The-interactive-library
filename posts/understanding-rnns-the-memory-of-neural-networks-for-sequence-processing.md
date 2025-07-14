---
title: "הזיכרון של המחשב: מסע לתוך רשתות RNN"
english_slug: understanding-rnns-the-memory-of-neural-networks-for-sequence-processing
category: "מדעי המחשב"
tags:
  - רשתות עצביות
  - RNN
  - עיבוד שפה טבעית
  - למידה עמוקה
  - מודלים סדרתיים
---
# הזיכרון של המחשב: מסע לתוך רשתות RNN

איך מחשב יכול "לזכור" את תחילת המשפט כדי להבין את סופו? איך הוא מזהה דפוסים בסדרות כמו מוזיקה או קוד גנטי? העולם סביבנו מלא ברצפים, ולמידה מהם דורשת יותר מסתם עיבוד נקודתי. כאן נכנסות לתמונה רשתות עצביות מיוחדות – רשתות בעלות זיכרון. בואו נצלול פנימה ונראה איך הן פועלות!

<div class="rnn-simulation-container">
  <div class="simulation-header">
    <h2>מעבד רצפים: סימולציית RNN פשוטה</h2>
    <p class="simulation-intro">הזינו תו אחד בכל פעם ולחצו "עבד תו". צפו כיצד "הזיכרון" הפנימי של הרשת והפלט שלה משתנים בהתאם לרצף שאתם בונים.</p>
  </div>

  <div class="simulation-controls">
    <div class="input-area">
      <label for="char-input">הזינו תו:</label>
      <input type="text" id="char-input" maxlength="1" autofocus />
      <button id="process-btn" class="action-button">עבד תו</button>
    </div>
     <button id="reset-btn" class="reset-button">התחל מחדש</button>
  </div>

  <div class="rnn-cell-viz">
      <div class="rnn-parts input-layer">
          <h4>קלט נוכחי</h4>
          <div class="viz-box input-viz"><span id="current-input">-</span></div>
          <div class="value-label" id="input-value-label">ערך: -</div>
      </div>

      <div class="rnn-parts processing-unit">
          <div class="connection-arrow prev-state-arrow"></div>
          <div class="connection-arrow input-arrow"></div>
           <div class="cell-body">
              <h4>מעבד RNN</h4>
              <div class="state-display">
                  <label>מצב פנימי (Hidden State):</label>
                  <div class="hidden-state-viz">
                       <div id="hidden-state-bar" class="state-bar"></div>
                       <span id="hidden-state-value" class="state-value">-</span>
                  </div>
                   <div class="value-label state-num-label" id="hidden-state-num-label">ערך: -</div>
              </div>
           </div>
          <div class="connection-arrow output-arrow"></div>
      </div>

      <div class="rnn-parts output-layer">
          <h4>פלט נוכחי</h4>
          <div class="viz-box output-viz"><span id="output-value">-</span></div>
           <div class="value-label" id="output-value-label">ערך: -</div>
      </div>
  </div>


  <div class="simulation-log">
    <h3>יומן עיבוד הרצף:</h3>
    <ul id="log-list"></ul>
  </div>
</div>

<style>
  :root {
      --primary-color: #4a90e2; /* Soft Blue */
      --secondary-color: #50e3c2; /* Teal */
      --accent-color: #f5a623; /* Orange */
      --background-color: #f8f9fa; /* Light Grey */
      --card-background: #ffffff; /* White */
      --text-color: #333; /* Dark Grey */
      --border-color: #e0e0e0; /* Lighter Grey */
      --success-color: #7ed321; /* Green */
      --danger-color: #d0021b; /* Red */
      --animation-duration: 0.5s;
  }

  .rnn-simulation-container {
    direction: rtl;
    font-family: 'Varela Round', sans-serif; /* More modern font */
    max-width: 800px; /* Wider container */
    margin: 30px auto;
    padding: 25px;
    border: 1px solid var(--border-color);
    border-radius: 12px; /* More rounded corners */
    background-color: var(--background-color);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    color: var(--text-color);
  }

  .simulation-header h2, .simulation-header p {
      text-align: center;
      color: var(--primary-color);
      margin-bottom: 10px;
  }

   .simulation-intro {
       font-size: 1.1em;
       color: #555;
       margin-bottom: 25px;
   }

  .simulation-controls {
      display: flex;
      justify-content: center;
      align-items: center;
      margin-bottom: 30px;
      padding: 15px;
      background-color: #e9ecef; /* Slightly darker input area */
      border-radius: 8px;
      box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
  }

  .input-area {
      display: flex;
      align-items: center;
      margin-left: 20px; /* Space between input group and reset */
  }

  .input-area label {
    margin-left: 10px;
    font-weight: bold;
    color: var(--text-color);
  }

  .input-area input[type="text"] {
    padding: 10px;
    border: 1px solid var(--border-color);
    border-radius: 6px;
    width: 60px; /* Wider input */
    text-align: center;
    font-size: 1.2em;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
  }
   .input-area input[type="text"]:focus {
       border-color: var(--primary-color);
       box-shadow: 0 0 5px rgba(74, 144, 226, 0.3);
       outline: none;
   }


  .action-button, .reset-button {
    padding: 10px 20px;
    margin-right: 10px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.1em;
    transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
    font-weight: bold;
  }

  .action-button {
    background-color: var(--secondary-color);
    color: var(--text-color);
     box-shadow: 0 2px 5px rgba(80, 227, 194, 0.3);
  }
  .action-button:hover {
    background-color: #40c1a8;
     box-shadow: 0 3px 7px rgba(80, 227, 194, 0.4);
  }
  .action-button:active {
      transform: scale(0.98);
  }

  .reset-button {
    background-color: var(--danger-color);
    color: white;
    box-shadow: 0 2px 5px rgba(208, 2, 27, 0.3);
  }
   .reset-button:hover {
    background-color: #b00216;
    box-shadow: 0 3px 7px rgba(208, 2, 27, 0.4);
   }
    .reset-button:active {
      transform: scale(0.98);
  }

  .rnn-cell-viz {
      display: flex;
      justify-content: space-around;
      align-items: center;
      margin: 30px 0;
      position: relative; /* For absolute positioning of arrows */
      min-height: 150px; /* Ensure space for visualization */
  }

  .rnn-parts {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      flex-basis: 150px; /* Fixed width for parts */
  }

   .rnn-parts h4 {
       margin-bottom: 10px;
       color: var(--text-color);
   }

   .viz-box {
       width: 80px;
       height: 50px;
       border: 2px dashed var(--primary-color);
       border-radius: 8px;
       display: flex;
       justify-content: center;
       align-items: center;
       font-size: 1.5em;
       font-weight: bold;
       color: var(--primary-color);
       background-color: var(--card-background);
       box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
       transition: transform var(--animation-duration) ease-out; /* Animation */
   }

    .input-viz span, .output-viz span {
        min-width: 20px; /* Prevent layout shifts */
        text-align: center;
    }

   .processing-unit {
       flex-basis: 250px; /* Wider for the main cell */
       position: relative;
   }

   .cell-body {
       background-color: var(--card-background);
       border: 2px solid var(--secondary-color);
       border-radius: 12px;
       padding: 15px;
       box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
       width: 100%;
       box-sizing: border-box;
       transition: transform var(--animation-duration) ease-out; /* Animation */
   }

   .state-display {
       margin-top: 10px;
   }

    .state-display label {
        font-weight: bold;
        display: block;
        margin-bottom: 5px;
        color: var(--text-color);
    }

   .hidden-state-viz {
       width: 100%;
       height: 25px;
       background-color: #eee; /* Background for bar */
       border-radius: 4px;
       overflow: hidden; /* Keep bar inside */
       margin-bottom: 5px;
       position: relative;
   }

   .state-bar {
       height: 100%;
       width: 0%; /* Initial width */
       background-color: var(--primary-color); /* Default color */
       transition: width var(--animation-duration) ease-out, background-color var(--animation-duration) ease-out; /* Smooth transition for width and color */
   }

   .state-value {
       position: absolute;
       top: 0;
       left: 0;
       right: 0;
       bottom: 0;
       display: flex;
       justify-content: center;
       align-items: center;
       color: white; /* Value text color */
       font-weight: bold;
       text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
   }

   .value-label {
       margin-top: 5px;
       font-size: 0.9em;
       color: #555;
       min-height: 1.2em; /* Prevent layout shift */
   }

   /* Animation for parts when processing */
   .viz-box.process-animate, .cell-body.process-animate {
       transform: scale(1.05);
   }

   /* Arrows for data flow visualization */
    .connection-arrow {
        position: absolute;
        width: 60px; /* Length of arrow */
        height: 2px;
        background-color: var(--accent-color);
        z-index: 1;
        transition: background-color var(--animation-duration) ease-out, width var(--animation-duration) ease-out;
    }

    .connection-arrow::after {
        content: '';
        position: absolute;
        width: 0;
        height: 0;
        border-top: 6px solid transparent;
        border-bottom: 6px solid transparent;
        transition: border-color var(--animation-duration) ease-out;
    }

    .prev-state-arrow {
        top: 50%;
        right: calc(100% - 20px); /* Position to the left of cell */
        transform: translateY(-50%);
        width: 60px; /* Base width */
    }
    .prev-state-arrow::after {
        left: 100%;
        top: -6px;
        border-left: 10px solid var(--accent-color);
    }

     .input-arrow {
        top: -15px; /* Position above cell */
        left: 50%;
        transform: translateX(-50%) rotate(90deg); /* Point downwards */
         width: 60px; /* Base width */
     }
     .input-arrow::after {
        left: 100%;
        top: -6px;
        border-left: 10px solid var(--accent-color);
    }


    .output-arrow {
        top: 50%;
        left: calc(100% - 20px); /* Position to the right of cell */
        transform: translateY(-50%);
         width: 60px; /* Base width */
    }
     .output-arrow::after {
        left: 100%;
        top: -6px;
        border-left: 10px solid var(--accent-color);
    }

    /* Animation for arrows */
    .connection-arrow.animate {
        background-color: var(--success-color); /* Highlight color */
        width: 70px; /* Slightly extend */
    }
     .connection-arrow.animate::after {
         border-left-color: var(--success-color);
     }


  .simulation-log {
    margin-top: 30px;
    padding: 20px;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    background-color: var(--card-background);
    max-height: 250px; /* Taller log */
    overflow-y: auto;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
  }

  .simulation-log h3 {
      text-align: right;
      color: var(--primary-color);
      margin-bottom: 15px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--border-color);
  }

  .simulation-log ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .simulation-log li {
    margin-bottom: 12px;
    padding-bottom: 12px;
    border-bottom: 1px dotted #ddd;
    font-size: 1em;
    line-height: 1.5;
  }
   .simulation-log li:last-child {
       border-bottom: none;
       margin-bottom: 0;
       padding-bottom: 0;
   }

   .simulation-log li strong {
       color: var(--secondary-color); /* Highlight key info */
   }


  #toggle-explanation {
    display: block;
    width: fit-content;
    margin: 30px auto;
    padding: 12px 25px;
    border: none;
    border-radius: 8px;
    background-color: var(--primary-color);
    color: white;
    font-size: 1.1em;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
     font-weight: bold;
     box-shadow: 0 3px 8px rgba(0, 123, 255, 0.3);
  }

  #toggle-explanation:hover {
    background-color: #3a83d4;
     box-shadow: 0 4px 10px rgba(0, 123, 255, 0.4);
  }
   #toggle-explanation:active {
      transform: scale(0.98);
   }

  #explanation {
    direction: rtl;
    margin-top: 20px;
    padding: 25px;
    border: 1px solid var(--border-color);
    border-radius: 12px;
    background-color: var(--card-background);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
    display: none; /* Initially hidden */
    color: var(--text-color);
  }

  #explanation h2 {
      text-align: center;
      color: var(--primary-color);
      margin-bottom: 20px;
  }

  #explanation h3 {
      text-align: right;
      color: var(--secondary-color);
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 8px;
      margin-top: 25px;
      margin-bottom: 15px;
  }

  #explanation p {
      line-height: 1.7; /* Improved readability */
      margin-bottom: 18px;
      text-align: justify;
  }

  #explanation ul {
      margin-bottom: 18px;
      padding-right: 20px; /* Indent list */
  }

  #explanation li {
      margin-bottom: 10px;
      line-height: 1.5;
  }

  #explanation code {
      background-color: #e9ecef;
      padding: 2px 5px;
      border-radius: 4px;
      font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
      font-size: 0.9em;
  }


</style>

<button id="toggle-explanation">מה בעצם קורה כאן? (הצג/הסתר הסבר)</button>

<div id="explanation">
    <h2>רשתות עצביות עם זיכרון: RNNs בפעולה</h2>

    <h3>מדוע רשתות רגילות לא מספיקות לרצפים?</h3>
    <p>תחשבו על משפט כמו "לאחר שאכל את התפוח, הוא זרק את <strong>הגלעין</strong>". כדי להבין למה המילה "הגלעין" מתייחסת, המוח שלנו "זוכר" את המילה "תפוח" שהופיעה קודם. רשתות עצביות רגילות (שנקראות Feedforward) פועלות אחרת: הן מקבלות קלט, מעבירות אותו דרך שכבות, ומייצרות פלט – הכל בצעד אחד, בלי לזכור את הקלטים הקודמים. זה מצוין למשימות כמו זיהוי אובייקט בתמונה (כל תמונה עצמאית), אבל כושל כשמדובר בטקסט, דיבור, סדרות עיתיות, או כל דבר שיש בו תלות ברצף ובזמן.</p>

    <h3>הקסם של הזיכרון ברשת RNN</h3>
    <p>כדי להתמודד עם רצפים, RNNs קיבלו יכולת מיוחדת: 'זיכרון' פנימי, שנקרא <strong>מצב נסתר (Hidden State)</strong>. בכל פעם שהרשת מעבדת איבר חדש ברצף (למשל, תו או מילה), היא לא רק מסתכלת על האיבר הנוכחי, אלא גם על המצב הנסתר שלה מהשלב הקודם. היא משתמשת בשני אלו כדי לעדכן את המצב הנסתר החדש ולייצר את הפלט הנוכחי. כך, המצב הנסתר הופך למעין תקציר של כל מה שהרשת ראתה עד כה ברצף!</p>

    <h3>המבנה הפשוט: לולאה בזמן</h3>
    <p>המבנה הבסיסי של RNN נראה כמו תא יחיד שחוזר על עצמו. בואו נפרוש אותו לאורך ציר הזמן:</p>
    <ol>
        <li>בזמן \(t=1\), הרשת מקבלת את האיבר הראשון ברצף (\(X_1\)) ואת מצב התחלתי כלשהו (\(H_0\), לרוב מאופס). היא מחשבת מצב נסתר חדש (\(H_1\)) ופלט (\(Y_1\)).</li>
        <li>בזמן \(t=2\), הרשת מקבלת את האיבר השני (\(X_2\)) ואת המצב הנסתר מהשלב הקודם (\(H_1\)). היא מחשבת מצב נסתר חדש (\(H_2\)) ופלט (\(Y_2\)).</li>
        <li>התהליך נמשך כך: בכל שלב \(t\), הקלט (\(X_t\)) והמצב הנסתר הקודם (\(H_{t-1}\)) נכנסים לתא ה-RNN, מחשבים מצב נסתר חדש (\(H_t\)) ופלט (\(Y_t\)).</li>
    </ol>
    <p>הנוסחאות הבסיסיות הן:</p>
    <p>\(H_t = f(W_{hh} \cdot H_{t-1} + W_{xh} \cdot X_t + b_h)\)</p>
    <p>\(Y_t = g(W_{hy} \cdot H_t + b_y)\)</p>
    <p>שימו לב! המשקלים (\(W\)-ים) וההטיות (\(b\)-ים) זהים בכל שלב זמן. זה מה שמאפשר לרשת ללמוד דפוסים שחוזרים על עצמם לאורך הרצף, לא משנה היכן הם מופיעים.</p>

    <h3>הסימולציה בפעולה</h3>
    <p>בסימולציה למעלה, אתם רואים ייצוג מופשט של התא היחיד הזה הפועל צעד אחר צעד. ה"מצב הפנימי" הוא ה-Hidden State. בכל פעם שאתם מזינים תו, אתם מחקים שלב זמן (\(t\)) ברצף. הרשת (במקרה זה, הסימולציה שלנו) מקבלת את התו (הקלט \(X_t\)) ומשתמשת בערך ה"מצב הפנימי" הקיים (מהשלב \(t-1\)) כדי לחשב את ה"מצב הפנימי" החדש (לשלב \(t\)) ואת ה"פלט" (לשלב \(t\)). הזיכרון הוויזואלי משקף את ערך ה-Hidden State, והוא משתנה כתגובה לשילוב של הקלט החדש והזיכרון הקודם.</p>

    <h3>שימושים נפוצים</h3>
    <ul>
        <li><strong>השלמת טקסט ומודלי שפה:</strong> חיזוי המילה הבאה.</li>
        <li><strong>תרגום מכונה:</strong> עיבוד משפט בשפה אחת ויצירת מקבילה בשפה אחרת.</li>
        <li><strong>זיהוי דיבור:</strong> המרת גלי קול לרצף מילים.</li>
        <li><strong>ניתוח סנטימנט:</strong> הבנת הרגש מאחורי משפט שלם.</li>
        <li><strong>ניתוח סדרות עיתיות:</strong> חיזוי מגמות במניות או נתוני מזג אוויר.</li>
    </ul>

    <h3>מעבר ל-RNN בסיסי: LSTM ו-GRU</h3>
    <p>למרות גאונותן, RNNs בסיסיות מתקשות לזכור מידע חשוב מתחילת רצפים ארוכים מאוד (בעיית Vanishing/Exploding Gradients). כדי לפתור זאת, פותחו ארכיטקטורות מתקדמות יותר כמו LSTM (Long Short-Term Memory) ו-GRU (Gated Recurrent Unit). הן מכילות מנגנוני "שערים" מתוחכמים שמאפשרים להן לשלוט בצורה מדויקת יותר אילו מידע לשמור בזיכרון, אילו לשכוח, ואילו לעדכן, ובכך לשמור על זיכרון ארוך טווח בצורה יעילה יותר.</p>
</div>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const charInput = document.getElementById('char-input');
    const processBtn = document.getElementById('process-btn');
    const resetBtn = document.getElementById('reset-btn');
    const currentInputSpan = document.getElementById('current-input');
    const hiddenStateValueSpan = document.getElementById('hidden-state-value');
    const hiddenStateBarDiv = document.getElementById('hidden-state-bar');
    const hiddenStateNumLabel = document.getElementById('hidden-state-num-label');
    const outputValueSpan = document.getElementById('output-value');
    const outputValueLabel = document.getElementById('output-value-label');
    const inputValueLabel = document.getElementById('input-value-label');
    const logList = document.getElementById('log-list');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    const inputVizBox = document.querySelector('.input-viz');
    const cellBodyViz = document.querySelector('.cell-body');
    const outputVizBox = document.querySelector('.output-viz');
    const prevStateArrow = document.querySelector('.prev-state-arrow');
    const inputArrow = document.querySelector('.input-arrow');
    const outputArrow = document.querySelector('.output-arrow');


    // Simple RNN simulation parameters (fixed for this demo)
    // Mapping characters to simple numerical inputs (arbitrary values scaled)
    const charMap = {
        'a': 0.2, 'b': 0.3, 'c': 0.4, 'd': 0.5, 'e': 0.6, // positive
        'f': 0.7, 'g': 0.8, 'h': 0.9, 'i': 1.0, 'j': 1.1,
        'k': -0.2, 'l': -0.3, 'm': -0.4, 'n': -0.5, 'o': -0.6, // negative
        'p': -0.7, 'q': -0.8, 'r': -0.9, 's': -1.0, 't': -1.1,
        'u': 0.1, 'v': -0.1, 'w': 0.05, 'x': -0.05, 'y': 0.15, 'z': -0.15, // small
        ' ': 0.0, // Neutral
        '.': 1.5, ',': -1.5, '!': 2.0, '?': -2.0, // Punctuation - strong influence
        // Add more characters or handle differently as needed
    };

    // Simple weights and biases (arbitrary values for demonstration)
    // Tweaked slightly to make state changes more noticeable but not explode quickly
    const W_hh = 0.7; // Weight for previous hidden state (slightly less emphasis on past)
    const W_xh = 0.6; // Weight for current input (slightly more emphasis on current)
    const b_h = 0.0;  // Bias for hidden state (centered around 0)
    const W_hy = 1.5; // Weight for hidden state to output (scale output more)
    const b_y = 0.0;  // Bias for output (centered around 0)

    // Activation functions
    const tanh = (x) => Math.tanh(x); // Maps value to [-1, 1]
    const sigmoid = (x) => 1 / (1 + Math.exp(-x)); // Maps value to [0, 1]

    let hiddenState = 0; // Initial hidden state
    const maxLogItems = 10; // Limit log history

    function updateDisplay(inputChar, inputValue, newState, output) {
      // Reset animations
      inputVizBox.classList.remove('process-animate');
      cellBodyViz.classList.remove('process-animate');
      outputVizBox.classList.remove('process-animate');
      prevStateArrow.classList.remove('animate');
      inputArrow.classList.remove('animate');
      outputArrow.classList.remove('animate');


      // Update character display immediately
      currentInputSpan.textContent = inputChar.toUpperCase();
      inputValueLabel.textContent = `ערך: ${inputValue.toFixed(2)}`;
      // Use setTimeout to trigger animations after a brief delay
      setTimeout(() => {
          // Animate input
          inputVizBox.classList.add('process-animate');
          inputValueLabel.classList.add('process-animate');
          inputArrow.classList.add('animate');
          if (logList.children.length > 0) { // Only animate previous state arrow if not first step
             prevStateArrow.classList.add('animate');
          }


          // After input animation, animate cell and state update
          setTimeout(() => {
              cellBodyViz.classList.add('process-animate');
              hiddenStateValueSpan.textContent = newState.toFixed(4); // Update value
              hiddenStateNumLabel.textContent = `ערך: ${newState.toFixed(4)}`; // Update value label
              // Visualize hidden state: Map range [-2, 2] (or more, need to cap) to width [0%, 100%]
              // Let's assume state typically stays within [-2, 2] for scaling color/width
              const cappedState = Math.max(-2, Math.min(2, newState)); // Cap value for visualization
              const vizWidth = ((cappedState + 2) / 4) * 100; // Scale -2..2 to 0..100
              hiddenStateBarDiv.style.width = `${vizWidth}%`;
              // Change color based on value (Hue: 0=red for negative, 120=green for positive)
              const colorHue = ((cappedState + 2) / 4) * 120; // Scale -2..2 to 0..120
              hiddenStateBarDiv.style.backgroundColor = `hsl(${colorHue}, 80%, 45%)`; // Use HSL for vibrancy


              // After cell animation, animate output
              setTimeout(() => {
                   outputVizBox.classList.add('process-animate');
                   outputValueSpan.textContent = output.toFixed(4); // Show output value
                   outputValueLabel.textContent = `ערך: ${output.toFixed(4)}`; // Show output value label
                   outputArrow.classList.add('animate');
                   addLogEntry(inputChar.toUpperCase(), inputValue, newState, output);
              }, var('--animation-duration').replace('s','') * 1000); // Wait for cell animation
          }, var('--animation-duration').replace('s','') * 500); // Wait for arrow animations

      }, 50); // Small delay to see initial state before animation
    }

    function addLogEntry(inputChar, inputValue, newState, output) {
       const listItem = document.createElement('li');
       listItem.innerHTML = `<strong>תו:</strong> '${inputChar}' (קלט מספרי: ${inputValue.toFixed(2)}) &rarr; <strong>מצב פנימי חדש:</strong> ${newState.toFixed(4)} &rarr; <strong>פלט:</strong> ${output.toFixed(4)}`;
       logList.appendChild(listItem);

       // Limit log size
       while (logList.children.length > maxLogItems) {
           logList.removeChild(logList.firstChild);
       }

       // Keep log scroll at bottom
       logList.scrollTop = logList.scrollHeight;
    }


    function processCharacter() {
      const inputChar = charInput.value.toLowerCase().trim(); // Get input, convert to lowercase, trim whitespace
      charInput.value = ''; // Clear input field
      charInput.focus(); // Keep focus on input

      if (!inputChar || !charMap.hasOwnProperty(inputChar)) {
        console.log('Invalid or unmapped input character.');
        // Optional: Add visual feedback for invalid input
        inputVizBox.classList.add('process-animate'); // Simple shake or flash
         inputVizBox.style.borderColor = 'var(--danger-color)';
         setTimeout(() => {
            inputVizBox.classList.remove('process-animate');
            inputVizBox.style.borderColor = var('--primary-color');
         }, var('--animation-duration').replace('s','') * 1000);
        return; // Do nothing if input is empty or not in map
      }

      const inputValue = charMap[inputChar];

      // Calculate new hidden state
      // Ht = tanh(W_hh * Ht-1 + W_xh * Xt + b_h)
      // Using tanh to keep state within a reasonable range [-1, 1], though external factors might push it slightly
      const newHiddenState = tanh(W_hh * hiddenState + W_xh * inputValue + b_h);


      // Calculate output
      // Yt = sigmoid(W_hy * Ht + b_y)
      // Using sigmoid for output, mapping to [0, 1]
      const output = sigmoid(W_hy * newHiddenState + b_y);

      // Update state for next step
      hiddenState = newHiddenState;

      // Update display with animations
      updateDisplay(inputChar, inputValue, hiddenState, output);

    }

    function resetSimulation() {
      hiddenState = 0;
      currentInputSpan.textContent = '-';
      hiddenStateValueSpan.textContent = '-';
      hiddenStateNumLabel.textContent = 'ערך: -';
      hiddenStateBarDiv.style.width = '0%';
      hiddenStateBarDiv.style.backgroundColor = var('--primary-color'); // Reset color
      outputValueSpan.textContent = '-';
      outputValueLabel.textContent = 'ערך: -';
      inputValueLabel.textContent = 'ערך: -';

      logList.innerHTML = ''; // Clear log
      charInput.value = '';
      charInput.focus(); // Put focus back on input

       // Reset animations
      inputVizBox.classList.remove('process-animate');
      cellBodyViz.classList.remove('process-animate');
      outputVizBox.classList.remove('process-animate');
      prevStateArrow.classList.remove('animate');
      inputArrow.classList.remove('animate');
      outputArrow.classList.remove('animate');

      // Optional: Add reset animation
      const container = document.querySelector('.rnn-simulation-container');
      container.style.opacity = 0.8;
      setTimeout(() => {
          container.style.opacity = 1;
      }, 300);
    }

    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מפורט' : 'מה בעצם קורה כאן? (הצג/הסתר הסבר)';
        // Scroll to explanation if showing it for the first time? Optional.
        if(isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }

    // Event listeners
    processBtn.addEventListener('click', processCharacter);
    resetBtn.addEventListener('click', resetSimulation);
    toggleExplanationBtn.addEventListener('click', toggleExplanation);

    // Allow pressing Enter in the input field
    charInput.addEventListener('keypress', (event) => {
      if (event.key === 'Enter') {
        event.preventDefault(); // Prevent default form submission
        processCharacter();
      }
    });

    // Initial state on load
    resetSimulation();
  });
</script>
```