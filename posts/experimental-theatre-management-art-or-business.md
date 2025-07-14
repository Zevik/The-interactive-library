---
title: "תיאטרון ניסיוני: ניהול במתח שבין אמנות לעסקים"
english_slug: experimental-theatre-management-art-or-business
category: "ניהול ועסקים / ניהול"
tags:
  - ניהול אמנות
  - תיאטרון
  - כלכלה
  - סימולציה
  - קבלת החלטות
  - תרבות
---

# תיאטרון ניסיוני: ניהול במתח שבין אמנות לעסקים

ברוכים הבאים לתפקיד המאתגר ביותר בעולם התרבות: מנהלי תיאטרון ניסיוני חדשני! המשימה שלכם: לנווט בין גלי יצירתיות פורצת דרך לבין שפל תקציבי מאיים. האם תוכלו לשמור על החזון האמנותי שלכם בחיים, או שמא המציאות הכלכלית תכריח אתכם להתפשר? גורל התיאטרון בידיים שלכם.

<div id="theatre-sim-app">
    <div class="app-header">
        <h2>סימולציית ניהול תיאטרון <span class="highlight">ניסיוני</span></h2>
        <p class="subtitle"> איזון עדין בין תשוקה לבמה לשורת רווח</p>
    </div>

    <div id="status" class="card status-card">
        <h3>מצב נוכחי</h3>
        <div class="status-grid">
            <div><span class="status-label">עונה:</span> <span id="season-number" class="status-value">1</span> / <span id="max-seasons" class="status-value">5</span></div>
            <div><span class="status-label">תקציב:</span> <span id="current-money" class="status-value money">0</span> ש"ח</div>
            <div><span class="status-label">מוניטין אמנותי:</span> <span id="current-reputation" class="status-value reputation">0</span> / 100</div>
        </div>
    </div>

    <div id="decisions" class="card decisions-card">
        <h3>קבלת החלטות לעונה <span id="current-decision-season"></span></h3>
        <p class="info-text"> בחרו בקפידה! סך ההוצאות שלכם לעונה לא יכול לעלות על התקציב הקיים.</p>

        <h4>1. בחירת יצירה לבמה:</h4>
        <div class="decision-options">
            <label class="decision-option">
                <input type="radio" name="play-choice" value="avantgarde" checked>
                <span class="option-title">🎬 אוונגרד פורץ דרך:</span> <span class="option-desc">יצירה נועזת ומקורית.</span> <br>
                <span class="option-details">*עלות הפקה בסיסית: <span class="cost">30,000 ש"ח</span>. פוטנציאל מוניטין: <span class="rep-effect">+ גדול (מאוד תנודתי)</span>. פוטנציאל הכנסה: <span class="income-effect">? (לא ודאי)</span>.*</span>
            </label>
            <label class="decision-option">
                <input type="radio" name="play-choice" value="classic-revamp">
                 <span class="option-title">🎭 עיבוד מודרני לקלאסיקה:</span> <span class="option-desc">פרשנות חדשה למחזה מוכר.</span> <br>
                <span class="option-details">*עלות הפקה בסיסית: <span class="cost">20,000 ש"ח</span>. פוטנציאל מוניטין: <span class="rep-effect">+ בינוני (תנודתי)</span>. פוטנציאל הכנסה: <span class="income-effect">$$ (יציב יחסית)</span>.*</span>
            </label>
            <label class="decision-option">
                <input type="radio" name="play-choice" value="popular-comedy">
                <span class="option-title">😂 קומדיה קלילה ופופולרית:</span> <span class="option-desc">מיועדת למשוך קהל רחב.</span> <br>
                <span class="option-details">*עלות הפקה בסיסית: <span class="cost">15,000 ש"ח</span>. פוטנציאל מוניטין: <span class="rep-effect">+ קטן (יציב)</span>. פוטנציאל הכנסה: <span class="income-effect">$$$ (סיכוי גבוה)</span>.*</span>
            </label>
        </div>

        <h4>2. תקציב אמנים (שחקנים ובמאי):</h4>
        <div class="decision-options">
            <label class="decision-option">
                <input type="radio" name="creative-budget" value="low" checked>
                 <span class="option-title">📉 נמוך</span> (<span class="cost">5,000 ש"ח</span>): פשרה על איכות השחקנים והבימוי. <span class="effect-text">אפקט מוניטין: x0.8.</span>
            </label>
            <label class="decision-option">
                <input type="radio" name="creative-budget" value="medium">
                 <span class="option-title">⚖️ בינוני</span> (<span class="cost">10,000 ש"ח</span>): צוות מקצועי סטנדרטי. <span class="effect-text">אפקט מוניטין: x1.0.</span>
            </label>
            <label class="decision-option">
                <input type="radio" name="creative-budget" value="high">
                 <span class="option-title">🌟 גבוה</span> (<span class="cost">20,000 ש"ח</span>): גיוס טאלנטים מובילים. <span class="effect-text">אפקט מוניטין: x1.3.</span>
            </label>
        </div>

         <h4>3. תקציב הפקה (תפאורה, תלבושות, טכני):</h4>
        <div class="decision-options">
            <label class="decision-option">
                <input type="radio" name="production-budget" value="low" checked>
                 <span class="option-title">🛠️ נמוך</span> (<span class="cost">5,000 ש"ח</span>): הפקה מינימליסטית. <span class="effect-text">אפקט הכנסה/מוניטין: x0.8.</span>
            </label>
            <label class="decision-option">
                <input type="radio" name="production-budget" value="medium">
                 <span class="option-title">📐 בינוני</span> (<span class="cost">10,000 ש"ח</span>): הפקה מקצועית ומכובדת. <span class="effect-text">אפקט הכנסה/מוניטין: x1.0.</span>
            </label>
            <label class="decision-option">
                <input type="radio" name="production-budget" value="high">
                 <span class="option-title">✨ גבוה</span> (<span class="cost">20,000 ש"ח</span>): הפקה עשירה ומרשימה. <span class="effect-text">אפקט הכנסה/מוניטין: x1.2.</span>
            </label>
        </div>

        <h4>4. תקציב שיווק ויח"צ:</h4>
        <div class="decision-options">
            <label class="decision-option">
                <input type="radio" name="marketing-budget" value="low" checked>
                <span class="option-title">📣 נמוך</span> (<span class="cost">5,000 ש"ח</span>): מסתמכים על שמועה וקהל נאמן. <span class="effect-text">אפקט הכנסה (קהל): x0.8.</span>
            </label>
            <label class="decision-option">
                <input type="radio" name="marketing-budget" value="medium">
                <span class="option-title">📢 בינוני</span> (<span class="cost">10,000 ש"ח</span>): קמפיין הגעה לקהל רחב יותר. <span class="effect-text">אפקט הכנסה (קהל): x1.0.</span>
            </label>
            <label class="decision-option">
                <input type="radio" name="marketing-budget" value="high">
                <span class="option-title">🚀 גבוה</span> (<span class="cost">20,000 ש"ח</span>): חשיפה מקסימלית, באזז תקשורתי. <span class="effect-text">אפקט הכנסה (קהל): x1.5.</span>
            </label>
        </div>

         <h4>5. מחירי כרטיסים:</h4>
        <div class="decision-options">
            <label class="decision-option">
                <input type="radio" name="ticket-price" value="low" checked>
                 <span class="option-title">💲 נמוכים</span> (כ-80 ש"ח): משיכת קהל המוני. <span class="effect-text">הכנסה לכרטיס: x0.9, כמות קהל: +.</span>
            </label>
            <label class="decision-option">
                <input type="radio" name="ticket-price" value="medium">
                 <span class="option-title">💰 בינוניים</span> (כ-120 ש"ח): מחיר סטנדרטי. <span class="effect-text">הכנסה לכרטיס: x1.0, כמות קהל: 0.</span>
            </label>
            <label class="decision-option">
                <input type="radio" name="ticket-price" value="high">
                 <span class="option-title">💎 גבוהים</span> (כ-180 ש"ח): פוטנציאל הכנסה גבוהה, עלול להרתיע. <span class="effect-text">הכנסה לכרטיס: x1.1, כמות קהל: -.</span>
            </label>
        </div>

        <div class="expenses-summary">
            <span>סך הוצאות צפוי: <span id="total-expenses-display" class="cost">0</span> ש"ח</span>
             <p id="expense-warning" class="warning-text" style="display: none;"><i class="fas fa-exclamation-triangle"></i> אזהרה: סך ההוצאות עולה על התקציב הזמין! אנא שנה את ההחלטות.</p>
        </div>


        <button id="end-season-button" class="btn primary-btn"><i class="fas fa-play-circle"></i> סיים עונה וראה תוצאות</button>

    </div>

    <div id="results" class="card results-card" style="display: none;">
        <h3>תוצאות העונה <span id="season-results-number"></span></h3>
        <div class="results-summary">
            <p id="expenses-summary" class="result-line"></p>
            <p id="income-summary" class="result-line"></p>
             <p id="money-change" class="result-line money-change"></p>
            <p id="current-money-after" class="result-line"></p>
            <p id="reputation-change" class="result-line reputation-change"></p>
            <p id="current-reputation-after" class="result-line"></p>
            <p id="audience-summary" class="result-line"></p>
            <p id="reviews-summary" class="result-line"></p>
             <div id="outcome-message" class="outcome-message"></div>
        </div>

        <button id="next-season-button" class="btn primary-btn"><i class="fas fa-forward"></i> התחל עונה הבאה</button>
        <button id="restart-button" class="btn secondary-btn" style="display: none;"><i class="fas fa-sync-alt"></i> התחל מחדש</button>
    </div>

    <div id="game-over" class="card game-over-card" style="display: none;">
        <h3 id="game-over-title"></h3>
        <p id="game-over-message"></p>
        <button id="restart-button-gameover" class="btn primary-btn"><i class="fas fa-sync-alt"></i> התחל מחדש</button>
    </div>
     <div class="app-footer">
         <p>@2023 סימולציית ניהול תיאטרון. כל הזכויות שמורות (למפתחים האמנותיים)</p>
     </div>
</div>

<button id="show-explanation-button" class="btn secondary-btn toggle-btn">הצג/הסתר הסבר: אמנות מול עסקים בתיאטרון</button>

<div id="explanation" class="card explanation-card" style="display: none;">
    <h3>על ניהול תיאטרון ניסיוני - תובנות מהסימולציה</h3>
    <p>כפי שחוויתם בסימולציה, ניהול תיאטרון, במיוחד כזה השואף להיות חדשני וניסיוני, מציב אתגרים מורכבים. הנה כמה נקודות מרכזיות:</p>
    <ul>
        <li>
            <h4>🎭 מהו ניהול אמנות/תיאטרון?</h4>
            זהו ניהול ייחודי המשלב עקרונות קלאסיים (תקציב, שיווק) עם צרכים אמנותיים (חזון, יצירתיות). המטרה אינה רק רווח, אלא גם יצירת אמנות בעלת ערך והשפעה תרבותית.
        </li>
        <li>
            <h4>⚖️ אתגר המטרות הכפולות: אמנות וכלכלה</h4>
            ארגוני תרבות שואפים למצוינות אמנותית ולקיימות כלכלית ("שורה תחתונה כפולה"). שני היעדים הללו לא תמיד מתיישבים, וקבלת החלטות כרוכה במתח ופשרות.
        </li>
        <li>
            <h4>🔗 חזון אמנותי ומודלים עסקיים</h4>
            החזון האמנותי והמציאות הכלכלית קשורים הדוקות. בחירת רפרטואר, סגנון הפקה, ואמנים משפיעים על עלויות, הכנסות, קהל ויכולת גיוס משאבים. מודל עסקי בר-קיימא חייב לתמוך בחזון.
        </li>
        <li>
            <h4>🎲 קבלת החלטות באי-ודאות (פשרות, עלות הזדמנות)</h4>
            תיאטרון ניסיוני פועל בסביבת אי-ודאות (קהל, ביקורת, סבסוד). תקציב מוגבל מחייב החלטות קשות - האם להשקיע בטאלנט על חשבון תפאורה? כל החלטה היא ויתור על הזדמנות אחרת.
        </li>
        <li>
            <h4>📊 מדדי הצלחה בארגוני אמנות</h4>
            הצלחה אינה רק רווח (שלעיתים אינו קיים). מדדים חשובים: מוניטין אמנותי, נאמנות קהל, השפעה תרבותית, חדשנות, היקף פעילות, ותמיכה ציבורית. איזון בין מדדים אלו הוא מפתח.
        </li>
        <li>
            <h4>🌍 השפעת גורמים חיצוניים</h4>
            תיאטרון ניסיוני תלוי לרוב בתמיכה חיצונית (סבסוד, תרומות). גורמים אלו, יחד עם ביקורות ותגובת הקהל, משפיעים דרמטית על הישרדותו, לעיתים אף יותר מההחלטות הפנימיות.
        </li>
    </ul>
    <p>הסימולציה נועדה להדגיש את המתחים והקשרים בין החלטות אמנותיות, כלכליות ותפעוליות, ואת הצורך באיזון אסטרטגי לקיום ושגשוג ארגון אמנותי.</p>
</div>


<style>
    /* General Styles */
    :root {
        --primary-color: #6a1b9a; /* Deep Purple */
        --secondary-color: #ab47bc; /* Amethyst */
        --accent-color: #e1bee7; /* Lilac */
        --text-color: #333;
        --card-bg: #ffffff;
        --status-bg: #f3e5f5; /* Light Purple */
        --decisions-bg: #e8f5e9; /* Light Green */
        --results-bg: #e0f7fa; /* Light Cyan */
        --explanation-bg: #fffde7; /* Light Yellow */
        --warning-color: #ef5350; /* Red */
        --success-color: #4caf50; /* Green */
        --neutral-color: #2196f3; /* Blue */
        --border-radius: 12px;
        --box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        --transition-speed: 0.3s ease-in-out;
    }

    body {
        font-family: 'Arial', sans-serif;
        background: linear-gradient(to right, var(--accent-color), var(--secondary-color));
        color: var(--text-color);
        line-height: 1.6;
        padding: 20px;
        direction: rtl;
        text-align: right;
    }

    #theatre-sim-app {
        max-width: 800px;
        margin: 20px auto;
        padding: 20px;
        background-color: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--box-shadow);
        overflow: hidden; /* For potential animations */
    }

    .app-header {
        text-align: center;
        margin-bottom: 30px;
        color: var(--primary-color);
    }

    .app-header h2 {
        margin-bottom: 5px;
        font-size: 2em;
        position: relative; /* For underline effect */
        display: inline-block;
    }

     .app-header h2 .highlight {
         color: var(--secondary-color);
     }

    .app-header h2::after {
        content: '';
        display: block;
        width: 50%;
        height: 3px;
        background-color: var(--primary-color);
        margin: 5px auto 0;
        border-radius: 2px;
    }

    .subtitle {
        font-size: 1.1em;
        color: #555;
    }

    .card {
        margin-bottom: 25px;
        padding: 20px;
        border-radius: var(--border-radius);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
    }

    .status-card {
        background-color: var(--status-bg);
        border: 1px solid rgba(171, 71, 188, 0.3);
    }

    .decisions-card {
         background-color: var(--decisions-bg);
         border: 1px solid rgba(76, 175, 80, 0.3);
    }

    .results-card {
         background-color: var(--results-bg);
         border: 1px solid rgba(0, 188, 212, 0.3);
    }

     .explanation-card {
         background-color: var(--explanation-bg);
         border: 1px dashed var(--primary-color);
     }

     .game-over-card {
        border: 3px solid var(--warning-color);
        background-color: #ffebee; /* Very light red */
        text-align: center;
        color: var(--warning-color);
        animation: pulse 1.5s infinite alternate;
     }

     @keyframes pulse {
         0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(239, 83, 80, 0.7); }
         100% { transform: scale(1.02); box-shadow: 0 0 0 10px rgba(239, 83, 80, 0); }
     }


    .card h3 {
        text-align: center;
        color: var(--primary-color);
        margin-top: 0;
        margin-bottom: 20px;
    }

    .card h4 {
        color: var(--secondary-color);
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 1px solid var(--accent-color);
        padding-bottom: 5px;
    }

    .status-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 15px;
        text-align: center;
    }

    .status-label {
        font-weight: bold;
        color: #555;
        display: block;
        margin-bottom: 5px;
    }

    .status-value {
        font-size: 1.4em;
        font-weight: bold;
        color: var(--primary-color);
    }

    .status-value.money { color: var(--success-color); }
    .status-value.reputation { color: var(--neutral-color); }


    .info-text {
        font-style: italic;
        color: #666;
        text-align: center;
        margin-bottom: 20px;
    }

    .decision-options {
        margin-bottom: 15px;
        padding: 15px;
        border: 1px dashed var(--secondary-color);
        border-radius: var(--border-radius);
        background-color: var(--card-bg);
    }

    .decision-option {
        display: block;
        margin-bottom: 12px;
        padding: 10px;
        border: 1px solid #eee;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color var(--transition-speed), border-color var(--transition-speed);
        background-color: #fcfcfc;
    }

     .decision-option:hover {
         background-color: var(--accent-color);
         border-color: var(--secondary-color);
     }

     .decision-option input[type="radio"] {
         margin-left: 10px; /* Adjust margin for RTL */
         vertical-align: middle;
     }

     .decision-option input[type="radio"]:checked + .option-title {
         font-weight: bold;
         color: var(--primary-color);
     }

    .option-title {
        font-weight: normal; /* Reset default bold */
        font-size: 1.1em;
        color: var(--text-color);
        transition: color var(--transition-speed);
    }

    .option-desc {
        font-style: italic;
        color: #555;
        font-size: 0.9em;
    }

    .option-details {
        display: block;
        margin-top: 5px;
        font-size: 0.85em;
        color: #777;
    }
     .option-details .cost { color: var(--warning-color); font-weight: bold;}
     .option-details .rep-effect { color: var(--neutral-color); font-weight: bold;}
     .option-details .income-effect { color: var(--success-color); font-weight: bold;}
     .effect-text { font-size: 0.85em; color: #555; }


     .expenses-summary {
         text-align: center;
         margin-top: 20px;
         padding-top: 15px;
         border-top: 1px dashed #ccc;
     }

     #total-expenses-display {
         font-size: 1.2em;
         font-weight: bold;
         color: var(--warning-color);
     }

     .warning-text {
         color: var(--warning-color);
         font-weight: bold;
         margin-top: 10px;
         font-size: 1em;
     }
      .warning-text i {
          margin-left: 5px;
      }


    .btn {
        display: block;
        width: auto;
        margin: 25px auto 15px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 25px; /* Pill shape */
        transition: background-color var(--transition-speed), transform 0.1s ease, box-shadow var(--transition-speed);
        font-weight: bold;
        text-align: center;
    }

    .primary-btn {
        background-color: var(--primary-color);
        color: white;
         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    }

    .primary-btn:hover {
        background-color: #5a158a; /* Darker purple */
        transform: translateY(-2px);
         box-shadow: 0 6px 8px rgba(0, 0, 0, 0.25);
    }
     .primary-btn:active {
         transform: translateY(0);
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
     }


    .secondary-btn {
        background-color: #e0e0e0; /* Light grey */
        color: #333;
         border: 1px solid #bbb;
    }

     .secondary-btn:hover {
         background-color: #d5d5d5; /* Slightly darker grey */
         transform: translateY(-2px);
     }
      .secondary-btn:active {
         transform: translateY(0);
     }

    .toggle-btn {
         margin-top: 30px;
         margin-bottom: 30px;
    }

    .btn i {
        margin-left: 8px; /* Adjust icon margin for RTL */
    }


    .results-summary {
        padding-top: 10px;
    }

    .result-line {
        margin-bottom: 10px;
        padding: 8px;
        border-bottom: 1px dashed #eee;
        font-size: 1.05em;
    }

     .result-line strong {
         color: var(--primary-color);
     }

    .money-change {
        font-weight: bold;
    }
    .money-change.positive { color: var(--success-color); }
    .money-change.negative { color: var(--warning-color); }

     .reputation-change {
        font-weight: bold;
     }
     .reputation-change.positive { color: var(--neutral-color); }
     .reputation-change.negative { color: var(--warning-color); }


    .outcome-message {
        margin-top: 20px;
        padding: 15px;
        border-radius: 8px;
        font-weight: bold;
        text-align: center;
        font-size: 1.1em;
        border: 2px solid;
        background-color: rgba(255, 255, 255, 0.7);
    }

    .outcome-message.positive {
        border-color: var(--success-color);
        color: var(--success-color);
        background-color: #e8f5e9;
    }
     .outcome-message.negative {
        border-color: var(--warning-color);
        color: var(--warning-color);
        background-color: #ffebee;
    }
     .outcome-message.neutral {
        border-color: var(--neutral-color);
        color: var(--neutral-color);
        background-color: #e1f5fe;
    }


     #game-over h3 {
         font-size: 1.8em;
         margin-bottom: 15px;
     }

     #game-over p {
         font-size: 1.2em;
         margin-bottom: 25px;
     }

      /* Specific game over states */
     #game-over.win h3, #game-over.win p { color: var(--success-color); }
     #game-over.win.game-over-card { border-color: var(--success-color); background-color: #e8f5e9; animation: none; }
     #game-over.lose h3, #game-over.lose p { color: var(--warning-color); }
     #game-over.lose .primary-btn { background-color: var(--warning-color); }
     #game-over.lose .primary-btn:hover { background-color: #c62828; }
     #game-over.lose.game-over-card { border-color: var(--warning-color); background-color: #ffebee; animation: pulse 1.5s infinite alternate; }


    #explanation ul {
        list-style-type: none; /* Remove default bullets */
        padding-right: 0; /* Remove default padding */
    }
    #explanation li {
        margin-bottom: 20px;
        padding: 15px;
        border: 1px solid var(--accent-color);
        border-radius: 8px;
        background-color: var(--card-bg);
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
     #explanation li h4 {
         margin-top: 0;
         color: var(--primary-color);
         border-bottom: none;
         padding-bottom: 0;
         font-size: 1.2em;
         margin-bottom: 8px;
     }
     #explanation li p {
         margin-bottom: 0;
         color: #555;
     }

     #explanation li h4 i {
         margin-left: 8px; /* Adjust icon spacing */
         color: var(--secondary-color);
     }


     .app-footer {
        text-align: center;
        margin-top: 30px;
        font-size: 0.9em;
        color: #777;
     }

     /* Font Awesome Icons (assuming loaded externally) */
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');

    /* Animation for money/reputation update */
    @keyframes countUpdate {
        from { opacity: 0.5; transform: translateY(-5px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .status-value.updating {
        animation: countUpdate 0.5s ease forwards;
    }


    /* Hide radio button actual element, style the label */
    .decision-option input[type="radio"] {
        position: absolute;
        opacity: 0;
        pointer-events: none;
    }

    .decision-option input[type="radio"] + .option-title::before {
        content: '';
        display: inline-block;
        width: 18px;
        height: 18px;
        border-radius: 50%;
        border: 2px solid #ccc;
        margin-left: 8px; /* Adjust spacing */
        vertical-align: middle;
        transition: border-color 0.2s ease-in-out;
         box-sizing: border-box;
    }

     .decision-option input[type="radio"]:checked + .option-title::before {
        border-color: var(--primary-color);
        background-color: var(--primary-color);
        box-shadow: inset 0 0 0 4px white; /* Inner dot effect */
     }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // State variables
        let currentMoney;
        let currentReputation;
        let currentSeason;
        const maxSeasons = 5;
        const startingMoney = 100000;
        const startingReputation = 50; // Out of 100

        // DOM elements
        const seasonNumberSpan = document.getElementById('season-number');
        const maxSeasonsSpan = document.getElementById('max-seasons');
        const currentMoneySpan = document.getElementById('current-money');
        const currentReputationSpan = document.getElementById('current-reputation');
         const currentDecisionSeasonSpan = document.getElementById('current-decision-season'); // Added for decision title
        const decisionsDiv = document.getElementById('decisions');
        const endSeasonButton = document.getElementById('end-season-button');
        const resultsDiv = document.getElementById('results');
        const seasonResultsNumberSpan = document.getElementById('season-results-number');
        const expensesSummaryP = document.getElementById('expenses-summary');
        const incomeSummaryP = document.getElementById('income-summary');
        const moneyChangeP = document.getElementById('money-change');
        const currentMoneyAfterP = document.getElementById('current-money-after');
        const reputationChangeP = document.getElementById('reputation-change');
        const currentReputationAfterP = document.getElementById('current-reputation-after');
        const audienceSummaryP = document.getElementById('audience-summary');
        const reviewsSummaryP = document.getElementById('reviews-summary');
        const outcomeMessageDiv = document.getElementById('outcome-message'); // Added for narrative outcome
        const nextSeasonButton = document.getElementById('next-season-button');
        const restartButtonResults = document.getElementById('restart-button');
        const gameOverDiv = document.getElementById('game-over');
        const gameOverTitle = document.getElementById('game-over-title');
        const gameOverMessage = document.getElementById('game-over-message');
        const restartButtonGameOver = document.getElementById('restart-button-gameover');
        const expenseWarningP = document.getElementById('expense-warning');
         const totalExpensesDisplay = document.getElementById('total-expenses-display'); // Added for live expense display


        const showExplanationButton = document.getElementById('show-explanation-button');
        const explanationDiv = document.getElementById('explanation');

        // Decision costs and effects
        const playOptions = {
            'avantgarde': { name: 'יצירת אוונגרד פורצת דרך', cost: 30000, income: { base: 40000, range: 60000 }, repGain: { base: 30, range: 30 }, risk: 1.5, audienceMultiplier: 0.9 }, // Avantgarde has higher risk, lower guaranteed audience
            'classic-revamp': { name: 'עיבוד מודרני לקלאסיקה', cost: 20000, income: { base: 30000, range: 30000 }, repGain: { base: 15, range: 15 }, risk: 1.0, audienceMultiplier: 1.1 }, // Classic revamp has moderate risk, broader appeal
            'popular-comedy': { name: 'קומדיה קלילה ופופולרית', cost: 15000, income: { base: 25000, range: 10000 }, repGain: { base: 5, range: 5 }, risk: 0.5, audienceMultiplier: 1.3 }, // Comedy has lower risk, high audience appeal
        };

        const budgetOptions = { // Creative budget effect on reputation
            'low': { cost: 5000, effect: 0.8 },
            'medium': { cost: 10000, effect: 1.0 },
            'high': { cost: 20000, effect: 1.3 },
        };

        const productionBudgetOptions = { // Production budget effect on income & reputation
             'low': { cost: 5000, effect: 0.8 },
             'medium': { cost: 10000, effect: 1.0 },
             'high': { cost: 20000, effect: 1.2 },
        };

         const marketingBudgetOptions = { // Marketing budget effect on audience/income
             'low': { cost: 5000, effect: 0.8 },
             'medium': { cost: 10000, effect: 1.0 },
             'high': { cost: 20000, effect: 1.5 }, // High marketing gives significant audience boost
        };

        const ticketPriceOptions = { // Ticket price effect on income per ticket & audience quantity
            'low': { name: 'נמוכים', effectIncome: 0.8, effectAudience: 1.5 }, // Lower price, much higher audience chance, but less per ticket
            'medium': { name: 'בינוניים', effectIncome: 1.0, effectAudience: 1.0 },
            'high': { name: 'גבוהים', effectIncome: 1.2, effectAudience: 0.7 }, // Higher price, higher per ticket, but lower audience chance
        };


        // --- Utility Functions ---

        function getRandomArbitrary(min, max) {
          return Math.random() * (max - min) + min;
        }

         function animateNumber(element, start, end, duration) {
            const range = end - start;
            const startTime = performance.now();
            const isMoney = element.classList.contains('money');
             element.classList.add('updating'); // Add animation class

            function update(currentTime) {
                const elapsedTime = currentTime - startTime;
                const progress = Math.min(elapsedTime / duration, 1);
                const value = start + range * progress;
                element.textContent = isMoney ? Math.round(value).toLocaleString() : Math.round(value);

                if (progress < 1) {
                    requestAnimationFrame(update);
                } else {
                     element.classList.remove('updating'); // Remove animation class after completion
                }
            }

            requestAnimationFrame(update);
         }


        // --- Game Functions ---

        function initGame() {
            currentMoney = startingMoney;
            currentReputation = startingReputation;
            currentSeason = 1;
            maxSeasonsSpan.textContent = maxSeasons;
            gameOverDiv.style.display = 'none';
             gameOverDiv.classList.remove('win', 'lose'); // Reset game over styles
            restartButtonResults.style.display = 'none'; // Hide restart button in results initially
            startSeason();
        }

        function startSeason() {
            seasonNumberSpan.textContent = currentSeason;
             currentDecisionSeasonSpan.textContent = currentSeason; // Update season in decision title
            // Animate initial status display (or just set directly if first season)
             if (currentSeason === 1) {
                 currentMoneySpan.textContent = currentMoney.toLocaleString();
                 currentReputationSpan.textContent = Math.round(currentReputation);
             } else {
                animateNumber(currentMoneySpan, parseInt(currentMoneySpan.textContent.replace(/,/g, '')), currentMoney, 800);
                animateNumber(currentReputationSpan, parseInt(currentReputationSpan.textContent), currentReputation, 800);
             }


            decisionsDiv.style.display = 'block';
            resultsDiv.style.display = 'none';
            gameOverDiv.style.display = 'none';
            expenseWarningP.style.display = 'none';
             outcomeMessageDiv.style.display = 'none'; // Hide outcome message

            // Enable decision inputs and button
            document.querySelectorAll('#decisions input').forEach(input => input.disabled = false);
            endSeasonButton.disabled = false;

             // Ensure one option is checked per category (browser default handles this, but good practice)
             document.querySelector('input[name="play-choice"][checked]').checked = true;
             document.querySelector('input[name="creative-budget"][checked]').checked = true;
             document.querySelector('input[name="production-budget"][checked]').checked = true;
             document.querySelector('input[name="marketing-budget"][checked]').checked = true;
             document.querySelector('input[name="ticket-price"][checked]').checked = true;


             checkTotalExpenses(); // Initial check after resetting radios
        }

         function checkTotalExpenses() {
            const selectedPlayCost = playOptions[document.querySelector('input[name="play-choice"]:checked').value].cost;
            const selectedCreativeCost = budgetOptions[document.querySelector('input[name="creative-budget"]:checked').value].cost;
            const selectedProductionCost = productionBudgetOptions[document.querySelector('input[name="production-budget"]:checked').value].cost;
            const selectedMarketingCost = marketingBudgetOptions[document.querySelector('input[name="marketing-budget"]:checked').value].cost;

            const totalExpenses = selectedPlayCost + selectedCreativeCost + selectedProductionCost + selectedMarketingCost;

            totalExpensesDisplay.textContent = totalExpenses.toLocaleString();

            if (totalExpenses > currentMoney) {
                expenseWarningP.style.display = 'block';
                endSeasonButton.disabled = true;
                 endSeasonButton.classList.add('secondary-btn'); // Make button less prominent
                 endSeasonButton.classList.remove('primary-btn');
            } else {
                expenseWarningP.style.display = 'none';
                endSeasonButton.disabled = false;
                 endSeasonButton.classList.add('primary-btn'); // Make button prominent
                 endSeasonButton.classList.remove('secondary-btn');
            }
        }

        function endSeason() {
            // Get decisions
            const playChoiceKey = document.querySelector('input[name="play-choice"]:checked').value;
            const creativeBudgetChoiceKey = document.querySelector('input[name="creative-budget"]:checked').value;
            const productionBudgetChoiceKey = document.querySelector('input[name="production-budget"]:checked').value;
            const marketingBudgetChoiceKey = document.querySelector('input[name="marketing-budget"]:checked').value;
            const ticketPriceChoiceKey = document.querySelector('input[name="ticket-price"]:checked').value;

            const play = playOptions[playChoiceKey];
            const creative = budgetOptions[creativeBudgetChoiceKey];
            const production = productionBudgetOptions[productionBudgetChoiceKey];
            const marketing = marketingBudgetOptions[marketingBudgetChoiceKey];
            const ticketPrice = ticketPriceOptions[ticketPriceChoiceKey];


            // Calculate expenses
            const totalExpenses = play.cost + creative.cost + production.cost + marketing.cost;

             if (totalExpenses > currentMoney) {
                 // This should be caught by checkTotalExpenses and button disabled, but safe fallback
                alert("לא ניתן לסיים עונה עם הוצאות העולות על התקציב הנוכחי.");
                return;
            }


            // Simulate Income and Reputation Change
            // Introduce more randomness based on play risk and current reputation (higher rep, slightly better chance on avantgarde)
            const outcomeRandomness = getRandomArbitrary(-1, 1); // Base randomness
            const reputationInfluence = (currentReputation / 100 - 0.5) * 0.5; // Between -0.25 and +0.25 based on reputation
            const finalRandomFactor = (outcomeRandomness * play.risk) + reputationInfluence; // Combine risk and reputation influence

            const incomeVariance = play.income.range * finalRandomFactor;
            const reputationVariance = play.repGain.range * finalRandomFactor;

            let simulatedIncome = (play.income.base + incomeVariance) * production.effect * marketing.effect * ticketPrice.effectIncome;
            simulatedIncome = Math.max(0, simulatedIncome); // Income cannot be negative

            let reputationChange = (play.repGain.base + reputationVariance) * creative.effect * production.effect;

            // Add effect of financial performance on reputation (more granular)
            const moneyChange = simulatedIncome - totalExpenses;
            const financialRatio = totalExpenses > 0 ? simulatedIncome / totalExpenses : 1; // Avoid division by zero
             if (financialRatio > 1.8) reputationChange += 7; // Huge success
            else if (financialRatio > 1.3) reputationChange += 4; // Good profit
            else if (financialRatio > 1.0) reputationChange += 1; // Small profit
            else if (financialRatio < 0.9 && financialRatio > 0.5) reputationChange -= 2; // Small loss
            else if (financialRatio <= 0.5 && financialRatio > 0) reputationChange -= 6; // Big loss
            else if (financialRatio <= 0) reputationChange -= 12; // Bankruptcy likely without intervention


            // Simulate Audience (based on outcomes, budgets, ticket price, and reputation)
             const baseAudienceSize = 300; // Assume a base number of potential attendees
             const audienceReach = baseAudienceSize * marketing.effect * ticketPrice.effectAudience * play.audienceMultiplier;
             // Audience size is also affected by reputation and performance quality (creative + production + outcome)
             const performanceQualityFactor = (creative.effect + production.effect) / 2; // Average quality effect
             const audienceActualFactor = (performanceQualityFactor + (currentReputation / 100) + (financialRatio > 1 ? (financialRatio - 1) * 0.5 : 0)) / 3; // Combine factors

             const simulatedAudience = Math.round(audienceReach * audienceActualFactor * getRandomArbitrary(0.8, 1.2)); // Add some final randomness

             const actualAudience = Math.max(0, simulatedAudience); // Audience cannot be negative


            // Update state
            currentMoney += moneyChange;
            currentReputation = Math.max(0, Math.min(100, currentReputation + reputationChange));


            // Simulate Reviews and Outcome Message
            let reviewQualityText;
            let financialReviewText;
            let outcomeMessageText;
            let outcomeClass = 'neutral';

            if (reputationChange > 15) reviewQualityText = "הביקורות היו מצוינות ומהללות, קוראות ליצירה אבן דרך!";
            else if (reputationChange > 5) reviewQualityText = "הביקורות היו טובות וחיוביות, שיבחו את ההשקעה האמנותית.";
            else if (reputationChange > -5) reviewQualityText = "הביקורות היו מעורבות, חלקן התלהבו וחלקן פחות.";
            else reviewQualityText = "הביקורות היו קשות ושליליות, טענו שהיצירה לא עומדת בציפיות.";

            if (moneyChange > totalExpenses * 0.3) financialReviewText = "הצלחה כלכלית גדולה! התיאטרון רשם רווח מרשים.";
            else if (moneyChange > 0) financialReviewText = "סיימנו את העונה ברווח קל, מצב יציב.";
            else if (moneyChange === 0) financialReviewText = "איזון כלכלי, בקושי כיסינו את ההוצאות.";
            else if (moneyChange > totalExpenses * -0.2) financialReviewText = "קושי כלכלי קל, העונה הסתיימה בהפסד צנוע.";
            else financialReviewText = "הפסד כספי משמעותי, המצב הכלכלי דורש שינוי דרסטי.";

             // Combined outcome message
             if (reputationChange > 10 && moneyChange > 0) {
                 outcomeMessageText = `🎉 עונה מדהימה! הצלחה אמנותית וכלכלית! ה${play.name} התקבל בהתלהבות, והקופות מלאו!`;
                 outcomeClass = 'positive';
             } else if (reputationChange > 5 && moneyChange > totalExpenses * -0.1) {
                  outcomeMessageText = `👍 עונה טובה. היצירה זכתה להכרה והניהול הכלכלי היה סביר.`;
                  outcomeClass = 'positive';
             } else if (reputationChange < -10 && moneyChange < totalExpenses * -0.2) {
                 outcomeMessageText = `💀 עונה קטסטרופלית! כישלון אמנותי וכלכלי. ה${play.name} לא הצליח למשוך קהל וגרר הפסדים כבדים.`;
                 outcomeClass = 'negative';
             } else if (reputationChange < -5) {
                 outcomeMessageText = `👎 אכזבה אמנותית. למרות ההשקעה, היצירה לא הותירה רושם חיובי.`;
                 outcomeClass = 'negative';
             } else if (moneyChange < totalExpenses * -0.1) {
                 outcomeMessageText = `📉 אתגר כלכלי. למרות המאמצים, ההוצאות עלו על ההכנסות משמעותית.`;
                 outcomeClass = 'negative';
             } else {
                 outcomeMessageText = `⚖️ עונה מאוזנת. היו עליות ומורדות, אבל התיאטרון ממשיך לפעול.`;
                 outcomeClass = 'neutral';
             }


            // Display results
            decisionsDiv.style.display = 'none';
            resultsDiv.style.display = 'block';
            seasonResultsNumberSpan.textContent = currentSeason;

            expensesSummaryP.innerHTML = `<strong>הוצאות:</strong> ${totalExpenses.toLocaleString()} ש"ח`;
            incomeSummaryP.innerHTML = `<strong>הכנסות:</strong> ${Math.round(simulatedIncome).toLocaleString()} ש"ח`;

            moneyChangeP.innerHTML = `<strong>שינוי תקציב:</strong> ${Math.round(moneyChange).toLocaleString()} ש"ח`;
             moneyChangeP.classList.remove('positive', 'negative');
             moneyChangeP.classList.add(moneyChange >= 0 ? 'positive' : 'negative');

            currentMoneyAfterP.innerHTML = `<strong>תקציב בסוף העונה:</strong> <span class="status-value money">${Math.round(currentMoney).toLocaleString()}</span> ש"ח`;

            reputationChangeP.innerHTML = `<strong>שינוי מוניטין:</strong> ${reputationChange.toFixed(1)}`;
             reputationChangeP.classList.remove('positive', 'negative');
             reputationChangeP.classList.add(reputationChange >= 0 ? 'positive' : 'negative');

            currentReputationAfterP.innerHTML = `<strong>מוניטין אמנותי בסוף העונה:</strong> <span class="status-value reputation">${Math.round(currentReputation)}</span> / 100`;

            audienceSummaryP.innerHTML = `<strong>צופים משוער:</strong> ${actualAudience.toLocaleString()}`;
            reviewsSummaryP.innerHTML = `<strong>סיכום העונה:</strong> ${reviewQualityText} ${financialReviewText}`; // Combine reviews

            outcomeMessageDiv.innerHTML = outcomeMessageText;
            outcomeMessageDiv.className = 'outcome-message ' + outcomeClass; // Set class for styling
            outcomeMessageDiv.style.display = 'block'; // Show the message


            // Animate status updates in results section
            const currentMoneyAfterSpan = currentMoneyAfterP.querySelector('.status-value');
            const currentReputationAfterSpan = currentReputationAfterP.querySelector('.status-value');

            // Use the *actual* current money/reputation value *before* the next season starts
             // Need to store the values from the start of the season OR calculate change and add to previous value
             // Let's just set them directly for simplicity here, animation will be done on startSeason
            // animateNumber(currentMoneyAfterSpan, parseInt(currentMoneyAfterSpan.textContent.replace(/,/g, '') || currentMoney), currentMoney, 800);
            // animateNumber(currentReputationAfterSpan, parseInt(currentReputationAfterSpan.textContent || currentReputation), currentReputation, 800);


            // Disable inputs and button after decision
             document.querySelectorAll('#decisions input').forEach(input => input.disabled = true);
             endSeasonButton.disabled = true;
             endSeasonButton.classList.add('secondary-btn');


            // Check game over or win
            if (currentMoney < 0) {
                endGame(false); // Lose
            } else if (currentSeason >= maxSeasons) {
                 // Wait a moment before showing win to let results sink in
                 // Timeout removed for immediate win/loss check
                 endGame(true); // Win
            } else {
                currentSeason++;
            }
        }

        function endGame(isWin) {
            resultsDiv.style.display = 'none';
            decisionsDiv.style.display = 'none';
            gameOverDiv.style.display = 'block';
             restartButtonGameOver.style.display = 'block'; // Ensure restart button is visible

            gameOverDiv.classList.add(isWin ? 'win' : 'lose'); // Add win/lose class for styling

            if (isWin) {
                gameOverTitle.textContent = "🌟 משימה הושלמה בהצלחה! 🌟";
                gameOverMessage.innerHTML = `ניהלתם את התיאטרון הניסיוני שלכם בהצלחה במשך <span class="highlight">${maxSeasons} עונות</span>!<br> סיימתם את המשחק עם תקציב מרשים של <span class="status-value money">${Math.round(currentMoney).toLocaleString()}</span> ש"ח ומוניטין אמנותי גבוה של <span class="status-value reputation">${Math.round(currentReputation)}</span> / 100.<br> הוכחתם שאפשר לשלב בין אמנות פורצת דרך לקיימות כלכלית!`;
            } else {
                gameOverTitle.textContent = "💔 מסך ירד בטרם עת... 💔";
                gameOverMessage.innerHTML = `נגמר לכם הכסף בעונה <span class="highlight">${currentSeason}</span>. התיאטרון נקלע לקשיים כלכליים ולא הצליח להתאושש.<br> ניהול תיאטרון ניסיוני הוא אכן אתגר לא פשוט.<br> התקציב שלכם ירד מתחת לאפס (<span class="status-value money">${Math.round(currentMoney).toLocaleString()}</span> ש"ח).`;
            }
             restartButtonResults.style.display = 'none'; // Ensure results restart button is hidden
        }

        // --- Event Listeners ---

        endSeasonButton.addEventListener('click', endSeason);
        nextSeasonButton.addEventListener('click', startSeason);
        restartButtonResults.addEventListener('click', initGame);
        restartButtonGameOver.addEventListener('click', initGame);

        // Listen for changes in decision radios to check total expenses
        document.querySelectorAll('#decisions input[type="radio"]').forEach(input => {
            input.addEventListener('change', checkTotalExpenses);
        });


        showExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            showExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'הצג הסבר: אמנות מול עסקים בתיאטרון'; // Toggle button text
             showExplanationButton.classList.toggle('active', isHidden); // Optional: Add active class for styling
        });

        // --- Initial Setup ---
        initGame();
         checkTotalExpenses(); // Initial check on load

    });
</script>
```