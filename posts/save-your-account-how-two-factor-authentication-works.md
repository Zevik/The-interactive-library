---
title: "הצילו את החשבון שלכם: כך פועל אימות דו-שלבי (2FA)"
english_slug: save-your-account-how-two-factor-authentication-works
category: "טכנולוגיה / סייבר ואבטחת מידע"
tags:
  - אבטחת מידע
  - סייבר
  - אימות דו-שלבי
  - 2FA
  - סיסמאות
  - הגנה דיגיטלית
---

# הצילו את החשבון שלכם: כך פועל אימות דו-שלבי (2FA)

<p>האם אי פעם חששתם מה יקרה אם הסיסמה שלכם תיפול לידיים הלא נכונות? האם יש גיבור על דיגיטלי שיכול לעצור פולשים, גם אם יש להם את "מפתח הבית" שלכם? הצטרפו אלינו למסע קצר אל קו ההגנה הנוסף שיכול להציל לכם את החשבונות הדיגיטליים.</p>

<div id="app-container">
    <h2>בואו נשחק אותה התחברות: מבחן ה-2FA</h2>
    <p>נראה איך שכבת האבטחה הנוספת הזו פועלת בפועל. בחרו את שיטת ההתחברות ונסו להיכנס (אפשר גם לדמות סיסמה שנגנבה!)</p>

    <div id="login-form" class="step-container">
        <div class="input-group">
            <label for="username">שם משתמש (לצורך ההדגמה בלבד):</label>
            <input type="text" id="username" value="גיבור_הדיגיטל@האתר_המאובטח.קום" autocomplete="off">
        </div>
        <div class="input-group">
            <label for="password">סיסמה:</label>
            <input type="password" id="password" value="password123" autocomplete="off">
        </div>

        <div class="option-select">
            <p class="option-title">איך תרצו להתחבר הפעם?</p>
            <div class="radio-option">
                <input type="radio" id="no-2fa" name="auth-type" value="no-2fa" checked>
                <label for="no-2fa">התחברות <span>רגילה</span> (ללא אימות דו-שלבי)</label>
            </div>
            <div class="radio-option">
                <input type="radio" id="with-2fa" name="auth-type" value="with-2fa">
                <label for="with-2fa">התחברות <span>מאובטחת</span> (עם אימות דו-שלבי)</label>
            </div>
        </div>

        <div id="simulate-stolen" class="simulate-option hidden">
             <input type="checkbox" id="simulate-stolen-password">
            <label for="simulate-stolen-password"><span class="warning-icon">⚠️</span> דמה מצב שבו <span>הסיסמה שלך נגנבה</span> (בדוק איך 2FA מציל אותך!)</label>
        </div>

        <button id="login-button" class="action-button">התחבר עכשיו</button>
    </div>

    <div id="two-factor-step" class="step-container hidden">
        <div class="step-header">
             <h3>שלב האימות הנוסף נדרש!</h3>
             <p class="step-prompt" id="two-factor-prompt"></p>
        </div>

        <div class="input-group">
            <label for="two-factor-code">קוד האימות:</label>
            <input type="text" id="two-factor-code" maxlength="6" autocomplete="off">
        </div>
        <button id="verify-code-button" class="action-button">אמת את הקוד</button>
    </div>

    <div id="result-area" class="result-container">
        <p id="result-message" class="result-text"></p>
    </div>

     <button id="reset-simulation" class="secondary-button hidden">התחל סימולציה חדשה</button>

</div>

<button id="toggle-explanation" class="action-button explanation-toggle">גלו את הסוד: איך 2FA עובד באמת?</button>

<div id="explanation" class="hidden explanation-section">
    <h2>מהו אימות דו-שלבי (2FA) ומדוע הוא מציל חיים דיגיטליים?</h2>
    <p>תארו לעצמכם את הבית שלכם. מנעול הדלת הוא הסיסמה שלכם. אם פורץ משיג מפתח (או מנחש את הקוד), הוא בפנים. אימות דו-שלבי (Two-Factor Authentication - 2FA) מוסיף דלת נוספת, או שומר בפתח, שדורש הוכחה נוספת לזהותכם – משהו שרק לכם יש. במקום להסתמך רק על "משהו שאתם יודעים" (הסיסמה), 2FA דורש גם "משהו שיש לכם" (כמו הטלפון) או "משהו שאתם" (כמו טביעת אצבע). גם אם הסיסמה שלכם נגנבת, הפורץ עדיין נתקל בחומת מגן נוספת שהוא לא יכול לעבור בקלות.</p>
    <p>בעולם שבו פריצות מידע והתקפות פישינג הן עניין יומיומי, סיסמאות לבד פשוט לא מספיקות. 2FA מספק את שכבת ההגנה הקריטית הזו שמגנה עליכם גם כשההגנה הראשונית נפרצת.</p>

    <h2>הסיכון: למה סיסמה אחת בלבד מסוכנת?</h2>
    <p>הישענות על סיסמה אחת היא כמו להשאיר את דלת הבית פתוחה למחצה. סיסמאות חשופות למגוון איומים:</p>
    <ul>
        <li>**דליפות מידע:** האתר שבו השתמשתם נפרץ, והסיסמה שלכם דלפה לרשת.</li>
        <li>**פישינג:** נפלתם בפח של הודעה מזויפת ומסרתם את הסיסמה בעצמכם.</li>
        <li>**שימוש חוזר בסיסמאות:** השתמשתם באותה סיסמה בכל מקום? פריצה אחת חושפת את כל החשבונות שלכם.</li>
        <li>**ניחוש סיסמאות חלשות:** "123456" או "password" הן הזמנה לפורצים.</li>
    </ul>
    <p>ברגע שלפורץ יש את הסיסמה, הוא נכנס לחשבון שלכם ויכול לגרום נזק אדיר: לרוקן חשבונות בנק, לגנוב זהות, לשלוח הודעות זדוניות בשמכם, ועוד.</p>

    <h2>מפתחות הממלכה: שלושת גורמי האימות</h2>
    <p>כדי להוכיח מי אתם, מערכות אבטחה משתמשות באחד משלושת הסוגים של גורמי אימות:</p>
    <ol>
        <li>**משהו שאתה יודע:** (סיסמה, קוד PIN, תשובה לשאלת אבטחה) - הכי נפוץ, והכי קל לגנוב או לנחש.</li>
        <li>**משהו שיש לך:** (טלפון נייד, אפליקציית אימות, מפתח חומרה, כרטיס חכם) - פריט פיזי או דיגיטלי שנמצא ברשותכם. קשה יותר לפורץ להשיג אותו מרחוק.</li>
        <li>**משהו שאתה:** (טביעת אצבע, סריקת פנים, קול) - מאפיין ביומטרי ייחודי לכם. קשה מאוד (או בלתי אפשרי) לגנוב או לזייף.</li>
    </ol>

    <h2>איך 2FA משלב כוחות?</h2>
    <p>2FA דורש שתשתמשו בשני גורמי אימות לפחות, משתי קטגוריות שונות. השילוב הנפוץ ביותר הוא:</p>
    <ul>
        <li>**משהו שאתה יודע (הסיסמה)**</li>
        <li>**+ משהו שיש לך (קוד שנשלח לטלפון)**</li>
    </ul>
    <p>אבל יש גם שילובים אחרים, כמו סיסמה + ביומטריה, או מפתח חומרה + קוד PIN. הרעיון הוא ליצור שני "מנעולים" שונים. גם אם פורץ פתח את הראשון (גנב את הסיסמה), הוא עדיין צריך לפתוח את השני (להשיג את הקוד מהטלפון שלכם).</p>

    <h2>מסע ההתחברות עם 2FA: צעד אחר צעד</h2>
    <p>כך זה נראה בדרך כלל:</p>
    <ol>
        <li>אתם מזינים שם משתמש וסיסמה (גורם 1: יודעים).</li>
        <li>המערכת מאמתת את הסיסמה.</li>
        <li>במקום להיכנס, המערכת מבקשת את גורם האימות השני.</li>
        <li>היא שולחת קוד לטלפון שלכם, שולחת הודעה לאפליקציה, או מבקשת להשתמש בטביעת אצבע (גורם 2: יש לכם / אתם).</li>
        <li>אתם מזינים את הקוד שקיבלתם או מבצעים את הפעולה הנדרשת.</li>
        <li>המערכת מאמתת את הגורם השני.</li>
        <li>**רק עכשיו**, כשאומתו שני הגורמים, אתם בפנים! בטוחים!</li>
    </ol>

    <h2>סוגי 2FA נפוצים - הכירו את השומרים שלכם</h2>
    <ul>
        <li>**קוד SMS:** הכי פשוט, הכי פחות בטוח (פגיע לגניבת סים). קוד נשלח לטלפון בהודעה.</li>
        <li>**אפליקציות אימות (Authenticator Apps):** כמו Google Authenticator. יוצרות קודים שמתחלפים כל כמה שניות, גם בלי קליטה. בטוח יותר מ-SMS.</li>
        <li>**מפתחות חומרה (YubiKey וכדומה):** התקנים פיזיים קטנים שמתחברים למחשב/טלפון. הכי בטוחים נגד פישינג.</li>
        <li>**אימות דחיפה (Push Notification):** שולח הודעה "האם אתה מנסה להתחבר?" לאפליקציה בטלפון, ואתם מאשרים בלחיצה. נוח מאוד.</li>
        <li>**אימות ביומטרי:** טביעת אצבע או סריקת פנים. משולב לרוב עם סיסמה.</li>
    </ul>

    <h2>בחירת השומר הנכון: יתרונות וחסרונות</h2>
    <p>לכל שיטה יש את היתרונות והחסרונות שלה מבחינת אבטחה, נוחות ודרישות טכניות. ההמלצה לרוב היא להעדיף את השיטות המאובטחות יותר (מפתחות חומרה > אפליקציות אימות > דחיפה) על פני SMS, למרות שגם SMS טוב יותר מלא כלום.</p>

    <h2>שמרו על המפתחות: טיפים לשימוש ב-2FA</h2>
    <ul>
        <li>**הפעילו בכל מקום אפשרי:** במיוחד בחשבונות קריטיים כמו בנק, אימייל ראשי, רשתות חברתיות, מנהלי סיסמאות.</li>
        <li>**עדיפות לאפליקציות אימות או מפתחות חומרה:** אם אפשר, הימנעו מ-SMS.</li>
        <li>**שמרו על קודי הגיבוי:** קבלתם קודים לשחזור? הדפיסו אותם ושמרו במקום בטוח (כמו כספת), לא על המחשב או בענן.</li>
        <li>**היו ערניים:** אם קיבלתם בקשת אימות כשלא ניסיתם להתחבר, זה סימן שמישהו אחר מנסה. אל תאשרו!</li>
        <li>**ודאו שפרטי ההתקשרות שלכם מעודכנים ומאובטחים:** אלו משמשים לעיתים לשחזור חשבון.</li>
    </ul>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --primary-dark: #0056b3;
        --secondary-color: #28a745;
        --secondary-dark: #218838;
        --danger-color: #dc3545;
        --danger-dark: #c82333;
        --warning-color: #ffc107;
        --text-color: #333;
        --border-color: #ccc;
        --background-color: #f8f9fa;
        --container-bg: #ffffff;
        --shadow-light: 0 2px 5px rgba(0, 0, 0, 0.1);
        --shadow-medium: 0 4px 8px rgba(0, 0, 0, 0.15);
        --transition-speed: 0.3s;
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-color);
        padding: 20px;
        direction: rtl; /* Ensure Hebrew direction */
        text-align: right; /* Ensure text aligns right */
    }

    h1, h2, h3 {
        color: var(--primary-dark);
        margin-bottom: 15px;
    }

    #app-container {
        border: 1px solid var(--border-color);
        padding: 20px;
        margin-bottom: 30px;
        border-radius: 12px;
        background-color: var(--container-bg);
        box-shadow: var(--shadow-medium);
        transition: all var(--transition-speed) ease-in-out;
    }

    .step-container {
        border: 1px dashed #ddd;
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 8px;
        background-color: #e9ecef; /* Light grey background for steps */
         transition: all var(--transition-speed) ease-in-out;
    }

     .step-container.hidden {
         opacity: 0;
         height: 0;
         overflow: hidden;
         padding-top: 0;
         padding-bottom: 0;
         margin-top: 0;
         margin-bottom: 0;
     }


    .step-header h3 {
        margin-top: 0;
        color: var(--primary-color);
    }

    .step-prompt {
        font-style: italic;
        color: #555;
        margin-bottom: 15px;
    }

    .input-group {
        margin-bottom: 20px;
    }

    .input-group label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        color: #555;
    }

    .input-group input[type="text"],
    .input-group input[type="password"] {
        width: calc(100% - 24px); /* Adjust for padding/border */
        padding: 12px;
        border: 1px solid var(--border-color);
        border-radius: 6px;
        font-size: 1.1em;
        box-sizing: border-box; /* Include padding and border in element's total width and height */
        transition: border-color var(--transition-speed) ease-in-out;
    }

     .input-group input[type="text"]:focus,
     .input-group input[type="password"]:focus {
        border-color: var(--primary-color);
        outline: none;
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.2);
     }


    .option-select {
        margin-top: 20px;
        margin-bottom: 20px;
        padding: 15px;
        border: 1px dashed var(--primary-color);
        border-radius: 8px;
         background-color: #e9ecef;
    }

    .option-select .option-title {
        font-weight: bold;
        margin-top: 0;
        margin-bottom: 10px;
        color: var(--primary-dark);
    }

    .radio-option {
        margin-bottom: 10px;
        cursor: pointer;
    }
     .radio-option label {
         font-weight: normal;
         cursor: pointer;
         display: inline-block;
     }
      .radio-option label span {
          font-weight: bold;
      }

    .option-select input[type="radio"] {
        margin-right: 5px; /* Adjust spacing for RTL */
        vertical-align: middle;
    }


    .simulate-option {
        margin-top: 15px;
        padding-top: 15px;
        border-top: 1px dashed #ddd;
        color: var(--danger-dark);
        transition: all var(--transition-speed) ease-in-out;
    }

     .simulate-option.hidden {
         opacity: 0;
         height: 0;
         overflow: hidden;
         padding-top: 0;
         margin-top: 0;
     }


    .simulate-option input[type="checkbox"] {
         margin-right: 5px; /* Adjust spacing for RTL */
         vertical-align: middle;
    }

     .simulate-option label {
        font-weight: bold;
        display: inline-block;
        cursor: pointer;
     }
     .simulate-option label span {
         font-weight: normal;
         color: var(--danger-dark);
     }
     .simulate-option label .warning-icon {
        color: var(--warning-color);
        margin-left: 5px; /* Adjust spacing for RTL */
     }


    .action-button {
        padding: 12px 25px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color var(--transition-speed) ease-in-out, opacity var(--transition-speed) ease-in-out, transform 0.1s ease-in-out;
        margin-top: 10px;
        display: inline-block; /* Allow margin/padding */
    }

     .action-button:hover:not(:disabled) {
        background-color: var(--primary-dark);
        transform: translateY(-1px);
     }
      .action-button:active:not(:disabled) {
         transform: translateY(0);
      }
     .action-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.7;
     }

    .secondary-button {
         padding: 10px 20px;
        background-color: #6c757d;
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1em;
         transition: background-color var(--transition-speed) ease-in-out, opacity var(--transition-speed) ease-in-out;
        margin-top: 15px;
        display: inline-block;
    }

    .secondary-button:hover:not(:disabled) {
        background-color: #5a6268;
    }
     .secondary-button.hidden {
         opacity: 0;
         height: 0;
         overflow: hidden;
         padding-top: 0;
         padding-bottom: 0;
         margin-top: 0;
         margin-bottom: 0;
     }


    .explanation-toggle {
        display: block;
        margin: 30px auto 20px auto;
        background-color: var(--secondary-color);
    }
    .explanation-toggle:hover:not(:disabled) {
         background-color: var(--secondary-dark);
    }


    .result-container {
        margin-top: 25px;
        padding: 15px;
        border: 1px solid #ddd;
        border-radius: 8px;
        background-color: #e9ecef;
        min-height: 1.5em;
        text-align: center;
        font-size: 1.2em;
        min-height: 50px; /* Give it some minimum height */
        display: flex;
        align-items: center;
        justify-content: center;
        transition: background-color var(--transition-speed) ease-in-out, border-color var(--transition-speed) ease-in-out;
    }

    .result-text {
        margin: 0;
        font-weight: bold;
        color: var(--text-color);
        transition: color var(--transition-speed) ease-in-out;
    }

    .result-container.success {
        background-color: #d4edda; /* Light green */
        border-color: #c3e6cb;
    }
     .result-container.success .result-text {
        color: #155724; /* Dark green */
     }

     .result-container.failure {
        background-color: #f8d7da; /* Light red */
        border-color: #f5c6cb;
     }
      .result-container.failure .result-text {
        color: var(--danger-dark); /* Dark red */
      }

      .result-container.info {
        background-color: #cce5ff; /* Light blue */
        border-color: #b8daff;
      }
       .result-container.info .result-text {
         color: var(--primary-dark); /* Dark blue */
       }

       .result-container.warning {
           background-color: #fff3cd; /* Light yellow */
           border-color: #ffeeba;
       }
       .result-container.warning .result-text {
           color: #856404; /* Dark yellow */
       }


    .hidden {
        display: none;
    }

    .explanation-section {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--container-bg);
         box-shadow: var(--shadow-light);
        transition: all var(--transition-speed) ease-in-out;
    }

    .explanation-section h2 {
        color: var(--primary-dark);
        margin-top: 20px;
        margin-bottom: 10px;
         padding-bottom: 5px;
         border-bottom: 1px solid #eee;
    }
     .explanation-section h3 {
         color: #555;
         margin-top: 15px;
         margin-bottom: 8px;
     }


    .explanation-section ul, .explanation-section ol {
        margin-bottom: 15px;
        padding-right: 20px; /* Adjust padding for RTL lists */
    }

    .explanation-section li {
        margin-bottom: 8px;
        list-style-type: disc; /* Default list style */
    }
     .explanation-section ol li {
         list-style-type: decimal;
     }


     /* Animation for result messages */
     @keyframes pulse {
         0% { transform: scale(1); }
         50% { transform: scale(1.02); }
         100% { transform: scale(1); }
     }

    .result-container.success,
    .result-container.failure,
    .result-container.warning,
    .result-container.info {
        animation: pulse 0.5s ease-in-out;
    }

    /* Animation for button click */
     .action-button:active:not(:disabled) {
         transform: scale(0.98);
     }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const appContainer = document.getElementById('app-container');
        const loginForm = document.getElementById('login-form');
        const twoFactorStep = document.getElementById('two-factor-step');
        const resultArea = document.getElementById('result-area');
        const resultMessage = document.getElementById('result-message');
        const loginButton = document.getElementById('login-button');
        const verifyCodeButton = document.getElementById('verify-code-button');
        const twoFactorCodeInput = document.getElementById('two-factor-code');
        const twoFactorPrompt = document.getElementById('two-factor-prompt');
        const no2faRadio = document.getElementById('no-2fa');
        const with2faRadio = document.getElementById('with-2fa');
        const simulateStolenCheckbox = document.getElementById('simulate-stolen-password');
        const simulateStolenDiv = document.getElementById('simulate-stolen');
        const resetSimulationButton = document.getElementById('reset-simulation');


        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        let currentTwoFactorCode = ''; // Variable to store the generated code

        // --- Helper Functions for State Management and Animation ---

        function showStep(stepElement) {
            stepElement.classList.remove('hidden');
            // Trigger reflow to make transition work
             stepElement.offsetHeight;
        }

         function hideStep(stepElement) {
             stepElement.classList.add('hidden');
         }

         function setResult(message, type = 'info') {
             resultMessage.textContent = message;
             resultArea.className = 'result-container ' + type; // Reset and add type class
         }

         function resetSimulation() {
            hideStep(twoFactorStep);
            hideStep(resetSimulationButton);
            showStep(loginForm);
            resultMessage.textContent = ''; // Clear result message
            resultArea.className = 'result-container'; // Reset result area style
            twoFactorCodeInput.value = ''; // Clear code input
            twoFactorCodeInput.disabled = false;
            twoFactorCodeInput.placeholder = '';
            verifyCodeButton.disabled = false;
            loginButton.disabled = false; // Enable login button
            // Reset radio buttons and checkbox
             no2faRadio.checked = true;
             simulateStolenCheckbox.checked = false;
             hideStep(simulateStolenDiv); // Hide simulate stolen option
             twoFactorPrompt.textContent = ''; // Clear prompt
         }


        // --- Event Listeners ---

        // Toggle explanation visibility
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.classList.contains('hidden');
            if (isHidden) {
                explanationDiv.classList.remove('hidden');
                toggleExplanationButton.textContent = 'הסתרת ההסבר המלא';
                 explanationDiv.style.maxHeight = explanationDiv.scrollHeight + 'px'; // Animate height
                 explanationDiv.style.opacity = '1';
            } else {
                 explanationDiv.style.maxHeight = '0'; // Collapse height
                 explanationDiv.style.opacity = '0';
                 // Wait for transition to complete before hiding display
                explanationDiv.addEventListener('transitionend', () => {
                     explanationDiv.classList.add('hidden');
                }, { once: true });

                toggleExplanationButton.textContent = 'גלו את הסוד: איך 2FA עובד באמת?';
            }
        });

        // Show/hide simulate stolen option based on 2FA radio button
        no2faRadio.addEventListener('change', () => {
            if (no2faRadio.checked) {
                hideStep(simulateStolenDiv);
                simulateStolenCheckbox.checked = false; // Reset checkbox
            }
        });

        with2faRadio.addEventListener('change', () => {
            if (with2faRadio.checked) {
                showStep(simulateStolenDiv);
            }
        });


        // Handle Login button click
        loginButton.addEventListener('click', () => {
            const is2faEnabled = with2faRadio.checked;
            const simulateStolen = simulateStolenCheckbox.checked;
            // In a real app, you'd use the actual password input value
            const password = document.getElementById('password').value; // Using value for demo purposes only

            // Reset state
            setResult('', 'info'); // Clear previous result
            hideStep(twoFactorStep);
            loginButton.disabled = true; // Disable login button during process
            hideStep(resetSimulationButton); // Hide reset during process


            setResult('מתחבר...', 'info'); // Initial message

            // Simulate password verification delay
            setTimeout(() => {
                 // Simulate password check success (for this demo, assume password is correct if not empty)
                 if (password) { // Basic check
                     setResult('סיסמה אומתה בהצלחה!', 'success');


                     if (!is2faEnabled) {
                         // Scenario 1: No 2FA
                         setTimeout(() => {
                             setResult('התחברות מוצלחת! (אך חשבונך פגיע!)', 'success');
                             // Add warning specifically for stolen password simulation without 2FA
                            if (simulateStolen) {
                                 setResult('התחברות מוצלחת עם סיסמה שנגנבה! חשבונך נפרץ ללא הגנת 2FA.', 'danger');
                            } else {
                                setResult('התחברות מוצלחת ללא 2FA. זכור: חשבונך פגיע יותר!', 'warning');
                            }
                             loginButton.disabled = false;
                              showStep(resetSimulationButton); // Show reset button
                         }, 1500); // Simulate final login delay

                     } else {
                         // Scenario 2/3: With 2FA
                         hideStep(loginForm); // Hide login form
                         showStep(twoFactorStep); // Show 2FA step

                          if (simulateStolen) {
                              // Scenario 3: Simulated Breach with 2FA
                             setResult('מדמה התחברות של פורץ עם סיסמה שנגנבה...', 'warning');
                             setTimeout(() => {
                                 setResult('סיסמה (שנגנבה!) אומתה. המערכת דורשת כעת אימות דו-שלבי.', 'warning');
                                 twoFactorPrompt.textContent = 'כפורץ המדמה התחברות, אין לך את הגורם השני (הקוד מהטלפון!)';
                                 verifyCodeButton.disabled = true; // Prevent entering code in simulation
                                 twoFactorCodeInput.placeholder = "אין לך גישה לקוד...";
                                 twoFactorCodeInput.disabled = true;
                                 showStep(resetSimulationButton); // Show reset button
                                 // Add a clear message about being blocked
                                 setResult('הכניסה נחסמה על ידי 2FA! הפורץ נכשל!', 'success'); // Success for the user!
                             }, 1500);

                         } else {
                             // Scenario 2: Normal login with 2FA
                             setResult('סיסמה אומתה. מחכה לאימות נוסף...', 'info');

                             // Simulate sending 2FA code
                             currentTwoFactorCode = Math.floor(100000 + Math.random() * 900000).toString(); // Generate 6-digit code
                             twoFactorPrompt.textContent = `שלחנו קוד אימות חד פעמי למכשיר שלך. (לצורך ההדגמה, הקוד הוא: ${currentTwoFactorCode})`;
                             twoFactorCodeInput.placeholder = "הזן את הקוד כאן";

                             loginButton.disabled = false; // Re-enable login button (in case user wants to change options)
                             verifyCodeButton.disabled = false;
                              showStep(resetSimulationButton); // Show reset button
                         }

                     }

                 } else {
                     // Basic password validation failure (for demo)
                     setResult('שם משתמש או סיסמה שגויים.', 'failure');
                     loginButton.disabled = false;
                      showStep(resetSimulationButton); // Show reset button
                 }
            }, 1500); // Simulate password verification delay
        });

        // Handle Verify Code button click
        verifyCodeButton.addEventListener('click', () => {
             const enteredCode = twoFactorCodeInput.value.trim();
             setResult('מאמת קוד אימות...', 'info');
             verifyCodeButton.disabled = true; // Disable during verification
             loginButton.disabled = true; // Disable login button

             setTimeout(() => {
                 if (enteredCode === currentTwoFactorCode) {
                     setResult('קוד אימות נכון. התחברות מוצלחת!', 'success');
                     hideStep(twoFactorStep); // Hide 2FA step
                     // Optionally show a "logged-in" state or just allow reset
                      showStep(resetSimulationButton); // Show reset button
                 } else {
                     setResult('קוד אימות שגוי. הגישה נדחתה.', 'failure');
                     verifyCodeButton.disabled = false; // Allow retry
                      loginButton.disabled = false; // Allow user to go back to login form
                      showStep(resetSimulationButton); // Show reset button
                 }
             }, 1500); // Simulate verification delay
        });

         // Handle Reset button click
         resetSimulationButton.addEventListener('click', () => {
            resetSimulation();
         });


         // --- Initial State ---
         hideStep(explanationDiv); // Initially hide explanation
         explanationDiv.style.maxHeight = '0'; // Set initial height to 0 for transition
         explanationDiv.style.opacity = '0'; // Set initial opacity to 0
         hideStep(simulateStolenDiv); // Hide stolen option initially
         hideStep(twoFactorStep); // Hide 2FA step initially
         hideStep(resetSimulationButton); // Hide reset button initially
         resultArea.className = 'result-container'; // Ensure initial state has no specific result class


    });
</script>
```