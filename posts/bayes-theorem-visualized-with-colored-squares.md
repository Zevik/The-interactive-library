---
title: "מסע ויזואלי למשפט בייס: עדכון אמונות באמצעות ראיות"
english_slug: bayes-theorem-visualized-with-colored-squares
category: "מתמטיקה"
tags: ["בייס", "הסתברות", "סטטיסטיקה", "ויזואליזציה", "למידה בייסיאנית", "אינטראקטיבי"]
---
# מסע ויזואלי למשפט בייס: עדכון אמונות באמצעות ראיות

החיים רצופים באי-ודאות. בכל פעם שאנו מקבלים פיסת מידע חדשה, עלינו לשקול כיצד היא משפיעה על ההבנה הנוכחית שלנו על העולם. האם המידע הזה מחזק את האמונה שלנו, מחליש אותה, או אולי מפתיע אותנו לגמרי? מסתבר שהאינטואיציה שלנו לא תמיד משרתת אותנו נכון בעדכון אמונות מבוססות ראיות.

כאן נכנס לתמונה משפט בייס – כלי מתמטי אלגנטי ועוצמתי שמאפשר לנו לעדכן הסתברויות בצורה מדויקת ורציונלית. בואו נחקור אותו באמצעות סימולציה ויזואלית שקופה ואינטואיטיבית. דמיינו עולם של ריבועים צבעוניים, שבו כל ריבוע מייצג אפשרות או מצב מסוים.

<div class="bayes-app-container">
    <h1>הגדר את העולם שלך</h1>
    <p class="intro-text">השתמש במחוונים כדי לקבוע את המאפיינים של אוכלוסיית הריבועים שלך (סך הכל 100 ריבועים).</p>

    <div class="controls">
        <div class="control-group">
            <label for="prior-prob">האמונה ההתחלתית שלך (P(A)): <br>אחוז הריבועים ה<strong>כחולים</strong> מתוך כולם</label>
            <input type="range" id="prior-prob" min="1" max="99" value="10" step="1">
            <span id="prior-prob-value">10%</span>
        </div>
        <div class="control-group">
            <label for="sensitivity">"רגישות" הראיה (P(B|A)): <br>אחוז הריבועים עם <strong>עיגול צהוב</strong> מתוך הריבועים ה<strong>כחולים</strong></label>
            <input type="range" id="sensitivity" min="1" max="99" value="80" step="1">
            <span id="sensitivity-value">80%</span>
        </div>
        <div class="control-group">
            <label for="false-positive-rate">"חיובי שגוי" של הראיה (P(B|לא A)): <br>אחוז הריבועים עם <strong>עיגול צהוב</strong> מתוך הריבועים ה<strong>לא-כחולים</strong></label>
            <input type="range" id="false-positive-rate" min="1" max="99" value="10" step="1">
            <span id="false-positive-rate-value">10%</span>
        </div>
    </div>

    <button id="generate-grid" class="action-button">צור את עולם הריבועים</button>

    <div class="probabilities calculation-results">
        <h2>החישובים לפי הפרמטרים</h2>
        <p>הסתברות מוקדמת (P(A)): <span id="display-prior"></span></p>
        <p>רגישות הראיה (P(B|A)): <span id="display-sensitivity"></span></p>
        <p>שיעור חיובי שגוי (P(B|לא A)): <span id="display-false-positive"></span></p>
        <p class="evidence-prob">הסתברות לקבלת הראיה (P(B)): <span id="display-evidence"></span></p>
        <p class="bayes-posterior-prob">הסתברות מאוחרת (P(A|B)) לפי בייס: <span id="display-posterior-bayes"></span></p>
    </div>

    <h2 class="visual-grid-title">הרשת הוויזואלית שלך (10x10 = 100 ריבועים)</h2>
     <div class="grid-container">
        <div id="bayes-grid" class="bayes-grid">
            <!-- Squares will be generated here by JavaScript -->
        </div>
     </div>

    <div class="actions">
        <button id="show-evidence" class="action-button" disabled>קבל ראיה: חשוף רק ריבועים עם עיגול צהוב</button>
        <button id="reset-simulation" class="secondary-button" disabled>התחל מחדש</button>
    </div>

    <div class="probabilities visual-posterior-results">
        <h2>הסתברות מאוחרת - לפי הויזואליזציה</h2>
        <p>P(A|B) ויזואלי:<br> (מספר ריבועים כחולים עם עיגול צהוב) / (מספר כלל הריבועים עם עיגול צהוב)</p>
        <p class="visual-posterior-prob"><span id="display-posterior-visual">N/A</span></p>
    </div>

</div>

<style>
    :root {
        --primary-color: #007bff;
        --primary-dark: #0056b3;
        --secondary-color: #28a745;
        --secondary-dark: #218838;
        --grey-blue: #e9ecef;
        --light-grey: #f8f9fa;
        --border-color: #ccc;
        --blue-square: #a0c4ff; /* Lighter blue */
        --not-blue-square: #e0e0e0; /* Muted grey */
        --yellow-circle: #ffda8a; /* Softer yellow */
        --orange-border: #f9a620; /* Warm orange */
        --highlight-blue: #6699ee; /* Brighter blue for highlight */
    }

    .bayes-app-container {
        font-family: 'Arial', sans-serif;
        max-width: 700px; /* Slightly narrower */
        margin: 30px auto;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px; /* More rounded */
        direction: rtl;
        text-align: right;
        background-color: #fff;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }

    h1, h2 {
        color: var(--primary-dark);
        text-align: center;
        margin-bottom: 20px;
    }

    .intro-text {
        text-align: center;
        margin-bottom: 30px;
        color: #555;
        font-size: 1.1em;
    }

    .controls {
        margin-bottom: 30px;
        padding: 20px;
        background-color: var(--light-grey);
        border-radius: 8px;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
    }

    .control-group {
        margin-bottom: 20px;
        display: flex; /* Use flexbox for better alignment */
        align-items: center;
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .control-group label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        color: #333;
        flex-basis: 100%; /* Label takes full width */
    }

    .control-group input[type="range"] {
        flex-grow: 1; /* Slider takes available space */
        margin-inline-end: 15px;
        /* Basic styling improvements for range input */
        -webkit-appearance: none;
        appearance: none;
        width: auto; /* Allow flex-grow to control width */
        height: 8px;
        background: var(--grey-blue);
        border-radius: 5px;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
    }

    .control-group input[type="range"]:hover {
        opacity: 1;
    }

    .control-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    .control-group input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    .control-group span {
        display: inline-block;
        width: 50px; /* Slightly wider for value */
        text-align: center;
        font-weight: bold;
        color: var(--primary-dark);
        font-size: 1.1em;
    }

    button.action-button, button.secondary-button {
        padding: 12px 20px;
        margin: 8px; /* Increased margin */
        color: white;
        border: none;
        border-radius: 6px; /* More rounded buttons */
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.2s ease, opacity 0.2s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    button.action-button {
         background-color: var(--primary-color);
    }
     button.action-button:hover:not(:disabled) {
        background-color: var(--primary-dark);
    }

    button.secondary-button {
         background-color: var(--secondary-color);
    }
     button.secondary-button:hover:not(:disabled) {
        background-color: var(--secondary-dark);
    }


    button:disabled {
        background-color: #cccccc !important; /* Override hover */
        cursor: not-allowed;
        opacity: 0.6;
        box-shadow: none;
    }

    .probabilities {
        margin-top: 30px;
        padding: 20px;
        background-color: var(--grey-blue);
        border-radius: 8px;
        font-size: 1.1em;
        line-height: 1.8; /* Increased line spacing */
    }

    .probabilities h2 {
         margin-top: 0;
         margin-bottom: 15px;
         font-size: 1.3em;
         color: #333;
         text-align: right; /* Align title to the right */
    }

    .probabilities p {
        margin: 8px 0;
        color: #555;
    }

     .probabilities p span {
        font-weight: bold;
        color: var(--primary-dark);
        font-size: 1.2em;
     }

     .bayes-posterior-prob span, .visual-posterior-prob span {
         color: var(--secondary-dark);
         font-size: 1.4em;
     }


    .grid-container {
        text-align: center; /* Center the grid */
        margin: 30px 0;
    }

    .visual-grid-title {
        margin-bottom: 15px;
        font-size: 1.3em;
        color: #333;
         text-align: right;
    }

    .bayes-grid {
        display: grid;
        grid-template-columns: repeat(10, 1fr);
        gap: 3px; /* Slightly larger gap */
        width: 250px; /* Make grid slightly larger */
        height: 250px;
        margin: 0 auto; /* Center the grid */
        border: 2px solid var(--border-color); /* Thicker border */
        box-sizing: content-box;
        padding: 3px;
        background-color: #fff; /* White background behind grid */
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }

    .square {
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        box-sizing: border-box;
        border: 0.5px solid #ddd; /* Finer border for squares */
        position: relative;
        transition: opacity 0.5s ease, transform 0.5s ease; /* Animation for show evidence */
         opacity: 1; /* Default state */
    }

    .square.blue {
        background-color: var(--blue-square);
    }

    .square.not-blue {
        background-color: var(--not-blue-square);
    }

    .square .yellow-circle {
        width: 65%; /* Slightly larger circle */
        height: 65%;
        background-color: var(--yellow-circle);
        border-radius: 50%;
        border: 1.5px solid var(--orange-border); /* Slightly thicker border */
        box-sizing: border-box;
        display: block; /* Ensure it's a block element */
    }

     /* Animation class for blue squares after filtering */
    .square.blue.has-yellow.highlight {
         animation: pulse 1.5s infinite ease-in-out;
         box-shadow: 0 0 8px var(--highlight-blue); /* Add glow effect */
    }

    @keyframes pulse {
      0% { transform: scale(1); }
      50% { transform: scale(1.05); }
      100% { transform: scale(1); }
    }

    /* Styles for showing only evidence */
    .bayes-grid.show-evidence .square:not(.has-yellow) {
        opacity: 0; /* Fade out */
        transform: scale(0.8); /* Shrink slightly */
        pointer-events: none; /* Make them non-interactive */
    }

     /* After animation, hide them fully */
    .bayes-grid.show-evidence .square:not(.has-yellow).hidden {
        display: none;
    }


    .actions {
        text-align: center;
        margin-top: 30px;
        margin-bottom: 20px;
    }

    #explanation-toggle {
        display: block;
        margin: 40px auto 20px auto; /* More space above */
        padding: 12px 25px;
        background-color: #5a6268; /* Muted color */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
         transition: background-color 0.2s ease;
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    #explanation-toggle:hover:not(:disabled) {
         background-color: #4e555b;
    }


    #explanation {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: var(--light-grey);
        display: none; /* Initially hidden */
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
    }

    #explanation h2 {
        margin-top: 0;
        margin-bottom: 20px;
        color: var(--primary-dark);
        font-size: 1.4em;
         text-align: right;
    }

    #explanation h3 {
        margin-top: 25px;
        margin-bottom: 10px;
        color: #555;
        font-size: 1.2em;
        border-bottom: 1px solid #ddd;
        padding-bottom: 5px;
    }

    #explanation p {
        margin-bottom: 15px;
        line-height: 1.7;
        color: #444;
    }

     #explanation p dir[dir="ltr"] {
         text-align: center;
     }

    #explanation ul {
        margin-bottom: 15px;
        padding-inline-start: 25px;
        color: #444;
    }

    #explanation li {
        margin-bottom: 8px;
        line-height: 1.6;
    }

     .visual-posterior-results {
         text-align: center;
     }
     .visual-posterior-results h2 {
         text-align: center;
          color: #333;
     }


    /* Mobile responsiveness */
    @media (max-width: 650px) {
         .bayes-app-container {
             padding: 20px;
             margin: 20px auto;
         }
         .bayes-grid {
             width: 200px;
             height: 200px;
             gap: 2px;
             padding: 2px;
         }
          .bayes-grid .square {
              border: 0.5px solid #eee;
          }
         .control-group {
             flex-direction: column;
             align-items: flex-start;
         }
         .control-group label {
             flex-basis: auto;
             margin-bottom: 5px;
         }
         .control-group input[type="range"] {
              width: 100%;
             margin-inline-end: 0;
             margin-bottom: 5px;
         }
         .control-group span {
             width: 100%;
             text-align: left;
             margin-top: 5px;
         }

         button.action-button, button.secondary-button {
             width: calc(100% - 16px); /* Adjust for margin */
             margin: 8px 8px;
             box-sizing: border-box;
         }

         .probabilities, #explanation {
             padding: 15px;
         }
         .probabilities h2, #explanation h2, #explanation h3 {
             text-align: right !important; /* Ensure text aligns right even on small screens */
         }
         .visual-posterior-results h2 {
              text-align: center !important; /* Center this specific title */
         }

    }

</style>

<button id="explanation-toggle">הצג/הסתר הסבר על משפט בייס</button>

<div id="explanation">
    <h2>הסבר מעמיק: כיצד פועל משפט בייס?</h2>

    <h3>מהו הרעיון המרכזי?</h3>
    <p>משפט בייס הוא לא רק נוסחה, אלא מסגרת חשיבה לעדכון ההבנה שלנו על העולם כשאנו נתקלים במידע חדש. הוא מאפשר לנו לשלב ידע קודם (ה"אמונה" שלנו לפני הראיה) עם עוצמת הראיה עצמה, כדי להגיע לאמונה מעודכנת ומבוססת יותר.</p>
    <p>נניח שאנו חוקרים תופעה מסוימת (נקרא לה מאורע A) ומקבלים פיסת מידע חדשה (נקרא לה ראיה B). אנו רוצים לדעת: מה הסיכוי שמאורע A נכון, **בהינתן** שראינו את ראיה B? זו ההסתברות המותנית P(A|B).</p>

    <h3>הנוסחה הקסומה של בייס:</h3>
    <p>הדרך לחשב את P(A|B) ניתנת על ידי הנוסחה:</p>
    <p dir="ltr" style="text-align: center; font-size: 1.3em; font-weight: bold; color: var(--primary-dark);">P(A|B) = [P(B|A) * P(A)] / P(B)</p>
    <p>בואו נפענח את הרכיבים:</p>
    <ul>
        <li><strong>P(A): ההסתברות המוקדמת (Prior Probability)</strong> - זו ההסתברות שייחסת למאורע A לפני שקיבלת את הראיה B. זו "האמונה" ההתחלתית שלך. בסימולציה שלנו, זהו אחוז הריבועים הכחולים בכלל האוכלוסייה.</li>
        <li><strong>P(B|A): הרגישות / אמינות הראיה (Likelihood)</strong> - זו ההסתברות לראות את ראיה B, בהינתן שמאורע A אכן התרחש. כמה סביר שהראיה תופיע בעולם שבו A נכון? בסימולציה, זהו אחוז הריבועים עם העיגול הצהוב *מתוך* הריבועים הכחולים.</li>
        <li><strong>P(B): הסתברות הראיה (Evidence Probability)</strong> - זו ההסתברות לראות את ראיה B באופן כללי, ללא קשר אם A נכון או לא. כיצד מחשבים זאת? ראיה B יכולה להופיע בשני מצבים: כאשר A קורה (ואז נקבל B עם הסתברות P(B|A)) או כאשר A לא קורה (P(לא A) נכון, ואז נקבל B עם הסתברות P(B|לא A), שזהו שיעור ה"חיובי שגוי"). לכן, P(B) שווה לסכום ההסתברויות הללו: <br> <p dir="ltr" style="text-align: center; font-size: 1.1em;">P(B) = P(B|A) * P(A) + P(B|לא A) * P(לא A)</p> בסימולציה, P(B) הוא אחוז כלל הריבועים עם עיגול צהוב מתוך ה-100.</li>
        <li><strong>P(A|B): ההסתברות המאוחרת (Posterior Probability)</strong> - וזו התוצאה שאותה אנו מחפשים! זו ההסתברות שמאורע A נכון, **לאחר** שקיבלת את הראיה B. זו "האמונה" המעודכנת שלך. בסימולציה, זו ההסתברות שהריבוע הוא כחול, בהינתן שחשפנו רק את הריבועים עם עיגול צהוב.</li>
    </ul>

    <h3>הקשר המופלא בין הויזואליזציה לנוסחה:</h3>
    <p>רשת 100 הריבועים היא מרחב המדגם המלא שלנו. כל ריבוע הוא יחידה אחת מתוך 100, המייצגת הסתברות של 1%.</p>
    <ul>
        <li>הריבועים ה<strong>כחולים</strong> מייצגים את מאורע A. מספרם הוא בקירוב P(A) * 100.</li>
        <li>הריבועים ה<strong>לא-כחולים</strong> מייצגים את מאורע 'לא A'. מספרם הוא בקירוב P(לא A) * 100.</li>
        <li>הריבועים עם <strong>עיגול צהוב</strong> מייצגים את ראיה B. מספרם הוא בקירוב P(B) * 100.</li>
        <li>הריבועים הכחולים <strong>עם עיגול צהוב</strong> מייצגים את המצב בו גם A קרה וגם B נצפה (A וגם B). מספרם הוא בקירוב P(B|A) * P(A) * 100. זהו בעצם **מונה** הנוסחה של בייס, כפול 100.</li>
        <li>כאשר לחצת על "חשוף רק ריבועים עם עיגול צהוב", בעצם צמצמת את מרחב המדגם שלך לקבוצה של ריבועים שיש בהם את ראיה B - כלומר, אתה מתמקד רק ב-P(B).</li>
    </ul>
    <p>כעת שים לב: מתוך קבוצת הריבועים שהוצגה (כל הריבועים עם עיגול צהוב), מה אחוז הריבועים שהם גם <strong>כחולים</strong>? זה בדיוק מספר הריבועים הכחולים עם עיגול צהוב, חלקי מספר כלל הריבועים עם עיגול צהוב.</p>
    <p dir="ltr" style="text-align: center; font-size: 1.1em; font-weight: bold;">אחוז כחולים מתוך קבוצת הראיה = (מספר ריבועים כחולים וגם עם עיגול צהוב) / (מספר כלל הריבועים עם עיגול צהוב)</p>
    <p>אם נחליף את המספרים בהסתברויות (על ידי חלוקה ב-100), נקבל בדיוק:</p>
     <p dir="ltr" style="text-align: center; font-size: 1.2em; font-weight: bold;">P(A|B) = P(A וגם B) / P(B)</p>
     <p>והיות ש-P(A וגם B) שווה ל-P(B|A) * P(A), קיבלנו שוב את הנוסחה של בייס!</p>
      <p dir="ltr" style="text-align: center; font-size: 1.2em; font-weight: bold;">P(A|B) = [P(B|A) * P(A)] / P(B)</p>

    <h3>הטיית שיעור הבסיס (Base Rate Fallacy) - והתיקון של בייס:</h3>
    <p>אחת הטעויות הנפוצות בחשיבה הסתברותית היא להתמקד רק ברגישות הראיה (P(B|A)) ולהתעלם מההסתברות המוקדמת (P(A)) ומשיעור ה"חיובי שגוי" (P(B|לא A)). לדוגמה, אם בדיקה רפואית למחלה נדירה היא מדויקת ב-95% (כלומר, P(B|A) גבוה מאוד), האינטואיציה שלנו עשויה לומר שתוצאה חיובית פירושה כמעט בוודאות שהאדם חולה. אולם, אם המחלה נדירה ביותר (P(A) נמוך מאוד) ושיעור החיובי שגוי (P(B|לא A)) אינו אפס (למשל, 5%), אז רוב התוצאות החיוביות שתקבלו בפועל יגיעו מהאוכלוסייה הגדולה של האנשים הלא-חולים, למרות הרגישות הגבוהה!</p>
    <p>הסימולציה מדגימה זאת בצורה ויזואלית. כשההסתברות המוקדמת נמוכה וה"חיובי שגוי" אינו אפסי, תראו שגם לאחר חשיפת הריבועים עם העיגול הצהוב, עדיין יישארו לא מעט ריבועים **לא-כחולים** עם עיגול צהוב לצד הריבועים הכחולים עם עיגול צהוב. זה ממחיש מדוע ההסתברות המאוחרת (P(A|B)) נמוכה משמעותית מרגישות הראיה (P(B|A)) במקרים כאלה.</p>

    <h3>איפה פוגשים את בייס בחיים?</h3>
    <ul>
        <li><strong>אבחון:</strong> הערכת הסיכוי למחלה, תקלה במכונה, או כל מצב אחר, לאחר קבלת תוצאות בדיקה או אינדיקטורים שונים.</li>
        <li><strong>סינון ספאם:</strong> אלגוריתמים רבים לזיהוי ספאם משתמשים בשיטות בייסיאניות כדי לחשב את הסיכוי שמייל הוא ספאם בהינתן המילים שהוא מכיל וההיסטוריה של המשתמש.</li>
        <li><strong>למידת מכונה:</strong> מודלים בייסיאניים מאפשרים למחשבים "ללמוד" מנתונים ולעדכן את ההבנה שלהם על העולם ככל שמצטבר מידע חדש.</li>
        <li><strong>פיננסים:</strong> עדכון הערכות סיכון להשקעות או אירועים כלכליים על בסיס נתונים חדשים.</li>
    </ul>
</div>


<script>
    const priorProbSlider = document.getElementById('prior-prob');
    const priorProbValueSpan = document.getElementById('prior-prob-value');
    const sensitivitySlider = document.getElementById('sensitivity');
    const sensitivityValueSpan = document.getElementById('sensitivity-value');
    const falsePositiveRateSlider = document.getElementById('false-positive-rate');
    const falsePositiveRateValueSpan = document.getElementById('false-positive-rate-value');

    const generateGridButton = document.getElementById('generate-grid');
    const bayesGridDiv = document.getElementById('bayes-grid');
    const showEvidenceButton = document.getElementById('show-evidence');
    const resetSimulationButton = document.getElementById('reset-simulation');

    const displayPrior = document.getElementById('display-prior');
    const displaySensitivity = document.getElementById('display-sensitivity');
    const displayFalsePositive = document.getElementById('display-false-positive');
    const displayEvidence = document.getElementById('display-evidence');
    const displayPosteriorBayes = document.getElementById('display-posterior-bayes');
    const displayPosteriorVisual = document.getElementById('display-posterior-visual');

    const explanationToggle = document.getElementById('explanation-toggle');
    const explanationDiv = document.getElementById('explanation');

    const totalSquares = 100; // For a 10x10 grid

    let squaresData = []; // Array to hold the square properties ({isBlue: bool, hasYellow: bool})

    // Update slider span values
    priorProbSlider.oninput = () => {
        priorProbValueSpan.textContent = priorProbSlider.value + '%';
        // Auto-generate grid on slider change for immediate feedback
        generateGrid();
    }
    sensitivitySlider.oninput = () => {
        sensitivityValueSpan.textContent = sensitivitySlider.value + '%';
        // Auto-generate grid on slider change
        generateGrid();
    }
    falsePositiveRateSlider.oninput = () => {
        falsePositiveRateValueSpan.textContent = falsePositiveRateSlider.value + '%';
        // Auto-generate grid on slider change
        generateGrid();
    }


    function calculateAndDisplayProbabilities() {
        const pA = parseFloat(priorProbSlider.value) / 100;
        const pB_given_A = parseFloat(sensitivitySlider.value) / 100;
        const pB_given_notA = parseFloat(falsePositiveRateSlider.value) / 100;
        const pNotA = 1 - pA;

        // Calculate P(B) using the Law of Total Probability
        const pB = (pB_given_A * pA) + (pB_given_notA * pNotA);

        // Calculate P(A|B) using Bayes' Theorem
        let pA_given_B = 0;
        if (pB > 0) {
            pA_given_B = (pB_given_A * pA) / pB;
        }

        // Display probabilities with better formatting
        displayPrior.textContent = pA.toFixed(3);
        displaySensitivity.textContent = pB_given_A.toFixed(3);
        displayFalsePositive.textContent = pB_given_notA.toFixed(3);
        displayEvidence.textContent = pB.toFixed(3);
        displayPosteriorBayes.textContent = pA_given_B.toFixed(3);

        return { pA, pB_given_A, pB_given_notA, pB, pA_given_B };
    }

    function generateGrid() {
        bayesGridDiv.innerHTML = ''; // Clear previous grid
        squaresData = []; // Reset squares data

        const params = calculateAndDisplayProbabilities();
        const { pA, pB_given_A, pB_given_notA } = params;

        // Calculate exact counts for each category for deterministic generation
        const numBlue = Math.round(totalSquares * pA);
        const numBlueWithYellow = Math.round(numBlue * pB_given_A);
        const numNotBlue = totalSquares - numBlue;
        const numNotBlueWithYellow = Math.round(numNotBlue * pB_given_notA);

        // Create square data based on counts
        const squareTypes = [];
        for(let i = 0; i < numBlueWithYellow; i++) squareTypes.push({isBlue: true, hasYellow: true});
        for(let i = 0; i < numBlue - numBlueWithYellow; i++) squareTypes.push({isBlue: true, hasYellow: false});
        for(let i = 0; i < numNotBlueWithYellow; i++) squareTypes.push({isBlue: false, hasYellow: true});
        for(let i = 0; i < numNotBlue - numNotBlueWithYellow; i++) squareTypes.push({isBlue: false, hasYellow: false});

        // Shuffle the array to randomize placement
        shuffleArray(squareTypes);

        // Generate and append squares to the grid
        squareTypes.forEach(squareData => {
             const squareDiv = document.createElement('div');
            squareDiv.classList.add('square');
            if (squareData.isBlue) squareDiv.classList.add('blue');
            else squareDiv.classList.add('not-blue');

            if (squareData.hasYellow) {
                const yellowCircle = document.createElement('div');
                yellowCircle.classList.add('yellow-circle');
                squareDiv.appendChild(yellowCircle);
                squareDiv.classList.add('has-yellow');
            } else {
                squareDiv.classList.add('no-yellow');
            }

            bayesGridDiv.appendChild(squareDiv);
        });

        // Store the actual square elements added to the DOM
        squaresData = Array.from(bayesGridDiv.children);


        // Calculate and display visual posterior probability based on *counts*
        const actualTotalWithYellow = numBlueWithYellow + numNotBlueWithYellow;
        const actualBlueWithYellow = numBlueWithYellow;
        const visualPosterior = actualTotalWithYellow > 0 ? actualBlueWithYellow / actualTotalWithYellow : 0;
        displayPosteriorVisual.textContent = actualTotalWithYellow > 0 ? visualPosterior.toFixed(3) : 'N/A (אין ראיות)';

        // Enable/Disable buttons
        showEvidenceButton.disabled = actualTotalWithYellow === 0; // Cannot show evidence if none exists
        resetSimulationButton.disabled = true; // Reset disabled until evidence is shown
        generateGridButton.disabled = false; // Can regenerate grid
        enableControls();
        bayesGridDiv.classList.remove('show-evidence'); // Ensure all squares are visible initially
        bayesGridDiv.classList.remove('visual-highlighted'); // Remove highlight class
        removeAllHighlights(); // Remove previous highlights
    }

     // Fisher-Yates Shuffle algorithm
    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]]; // Swap elements
        }
        return array;
    }


    function showEvidence() {
        // Start fade out animation
        bayesGridDiv.classList.add('show-evidence');
        showEvidenceButton.disabled = true;
        // Reset is enabled after animation is complete
        generateGridButton.disabled = true; // Cannot regenerate while showing evidence
        disableControls();

        // After animation, set display: none and highlight
        setTimeout(() => {
             const visibleSquares = squaresData.filter(s => s.classList.contains('has-yellow'));
             visibleSquares.forEach(s => s.classList.add('highlight')); // Add highlight to remaining blue+yellow
             // Hide squares that are not visible (after opacity transition)
            squaresData.forEach(s => {
                if (!s.classList.contains('has-yellow')) {
                     s.classList.add('hidden'); // Add hidden class
                }
            });
            resetSimulationButton.disabled = false; // Enable reset after hiding is complete
        }, 500); // Match this duration to CSS transition time

        // Recalculate and display visual posterior based on actual counts (already calculated in generateGrid)
        // This value is already set by generateGrid, no need to recalculate counts here
    }

    function resetSimulation() {
         bayesGridDiv.classList.remove('show-evidence');
         bayesGridDiv.classList.remove('visual-highlighted');
         removeAllHighlights(); // Remove any active highlights

         // Remove the 'hidden' class to make all squares visible again
        squaresData.forEach(s => s.classList.remove('hidden'));

        showEvidenceButton.disabled = false; // Re-enable show evidence button
        resetSimulationButton.disabled = true; // Disable reset until evidence is shown again
        generateGridButton.disabled = false; // Re-enable generate button
        enableControls();
         // Reset visual posterior display
        displayPosteriorVisual.textContent = 'N/A'; // Will be updated on generateGrid

        // Regeneration is handled by clicking generateGridButton or changing sliders again
        // Let's regenerate the grid automatically on reset for a clean start state
        generateGrid();
    }

    function removeAllHighlights() {
         squaresData.forEach(s => s.classList.remove('highlight'));
    }


    function disableControls() {
        priorProbSlider.disabled = true;
        sensitivitySlider.disabled = true;
        falsePositiveRateSlider.disabled = true;
    }

    function enableControls() {
        priorProbSlider.disabled = false;
        sensitivitySlider.disabled = false;
        falsePositiveRateSlider.disabled = false;
    }


    // Event Listeners - Sliders now trigger generateGrid automatically
    // priorProbSlider.addEventListener('input', generateGrid);
    // sensitivitySlider.addEventListener('input', generateGrid);
    // falsePositiveRateSlider.addEventListener('input', generateGrid);
    generateGridButton.addEventListener('click', generateGrid); // Still keep explicit button click
    showEvidenceButton.addEventListener('click', showEvidence);
    resetSimulationButton.addEventListener('click', resetSimulation);

    explanationToggle.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationToggle.textContent = isHidden ? 'הסתר הסבר על משפט בייס' : 'הצג/הסתר הסבר על משפט בייס';
    });


    // Initial grid generation on page load
    generateGrid();

</script>
---
```