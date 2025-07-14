---
title: "לפענח את דוחות האקלים: המשימה האקלימית"
english_slug: deciphering-climate-reports-the-climate-mission
category: "מדעי הסביבה / כללי"
tags: IPCC, שינוי אקלים, קריאת דוחות, הבנת נתונים, מדע האקלים, סימולציה
---
# לפענח את דוחות האקלים: המשימה האקלימית

דוחות הפאנל הבין-ממשלתי לשינוי האקלים (IPCC) הם המצפן המדעי העולמי שלנו להבנת משבר האקלים. הם אוצרים אלפי ממצאים פורצי דרך, אך ניווט בין מאות ואלפי עמודים עמוסים בנתונים ושפה מקצועית יכול להרגיש כמו משימה בלתי אפשרית. האם תוכלו לפענח את הקוד ולמצוא את המידע הקריטי החבוי בתוך הדוחות? קבלו את "המשימה האקלימית"!

<div class="ipcc-game-container" dir="rtl">
    <div class="game-header">
        <h2>המשימה שלכם: צאו למסע בזעיר-דוח IPCC</h2>
        <div id="progress-indicator" class="progress-indicator">
            משימה <span id="current-q">1</span> מתוך <span id="total-q">?</span>
        </div>
    </div>
    <div id="report-snippet" class="report-snippet">
        <!-- Report snippet will be loaded here -->
    </div>
    <div id="question-area">
        <p class="question-prompt">שאלה למשימה הנוכחית:</p>
        <p id="question-text" class="question-text"></p>
        <div id="options-area" class="options-area">
            <!-- Options (multiple choice or input) will be loaded here -->
        </div>
        <button id="submit-answer" class="game-button">בדיקת תשובה</button>
    </div>
    <div id="feedback-area" class="feedback-area" style="display: none;">
        <!-- Feedback will appear here -->
    </div>
    <button id="next-question" class="game-button next-button" style="display: none;">משימה הבאה »</button>
    <div id="game-complete" style="display: none;" class="game-complete-message">
        <h2>כל הכבוד! 🚀</h2>
        <p>סיימתם בהצלחה את כל המשימות בזעיר-דוח. יש לכם את היכולת לפענח מידע מדוחות אקלים חשובים!</p>
        <p>כעת אתם מוזמנים לצלול עמוק יותר ולהעשיר את הידע שלכם בעזרת ההסבר המורחב למטה.</p>
    </div>
</div>

<style>
    /* General Styles */
    .ipcc-game-container {
        font-family: 'Heebo', 'Arial', sans-serif;
        line-height: 1.7;
        max-width: 850px;
        margin: 30px auto;
        padding: 30px;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        background-color: #ffffff;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        text-align: right;
        direction: rtl; /* Ensure RTL layout */
        overflow: hidden; /* Clear floats if any */
        position: relative; /* Needed for absolute positioning of progress */
    }

    /* Header & Progress */
    .game-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
        border-bottom: 2px solid #f0f0f0;
        padding-bottom: 15px;
    }

    .ipcc-game-container h2 {
        color: #004085; /* A deep blue */
        margin: 0;
        font-size: 1.7em;
        flex-grow: 1; /* Allow heading to take space */
    }

    .progress-indicator {
        font-size: 1em;
        color: #5a6268; /* Muted grey */
        background-color: #e9ecef; /* Light grey background */
        padding: 8px 15px;
        border-radius: 20px;
        font-weight: bold;
        min-width: 120px; /* Give it a minimum width */
        text-align: center;
    }

    /* Report Snippet Area */
    .report-snippet {
        border: 1px solid #cce5ff; /* Light blue border */
        padding: 20px;
        margin-bottom: 25px;
        background-color: #eef5ff; /* Very light blue background */
        border-radius: 8px;
        font-size: 0.98em;
        line-height: 1.8;
        color: #333;
        position: relative; /* Needed for potential animations or overlays */
        transition: opacity 0.5s ease-in-out; /* Fade transition */
    }

    .report-snippet h3 {
        color: #0056b3; /* Medium blue */
        margin-top: 0;
        margin-bottom: 15px;
        border-bottom: 1px solid #cce5ff;
        padding-bottom: 8px;
    }

    .report-snippet table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
        font-size: 0.9em;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        background-color: #ffffff; /* White background for table */
    }

    .report-snippet th, .report-snippet td {
        border: 1px solid #dee2e6; /* Bootstrap border color */
        padding: 12px;
        text-align: center;
    }

    .report-snippet th {
        background-color: #007bff; /* Primary blue */
        color: white;
        font-weight: bold;
    }

    .report-snippet tr:nth-child(even) {
        background-color: #f2f2f2; /* Zebra striping */
    }

    .report-snippet ul {
         list-style-type: disc;
         padding-right: 25px; /* Indent lists for RTL */
         margin-top: 10px;
         margin-bottom: 10px;
    }

    .report-snippet li {
        margin-bottom: 8px;
    }


    /* Question Area */
    #question-area {
        margin-bottom: 30px;
        padding: 20px;
        background-color: #f8f9fa; /* Very light grey */
        border-radius: 8px;
        border: 1px solid #e9ecef;
    }

    .question-prompt {
         margin-bottom: 10px;
         font-weight: normal;
         color: #555;
         font-size: 0.95em;
    }

    .question-text {
        margin-bottom: 20px;
        font-weight: bold;
        font-size: 1.1em;
        color: #333;
    }

    .options-area label {
        display: block;
        margin-bottom: 12px;
        cursor: pointer;
        padding: 10px;
        border: 1px solid #ced4da;
        border-radius: 5px;
        transition: background-color 0.3s ease, border-color 0.3s ease;
        background-color: #ffffff;
        color: #495057;
    }

     .options-area label:hover {
        background-color: #e9ecef;
        border-color: #007bff;
        color: #000;
     }

     .options-area input[type="radio"] {
        margin-left: 10px; /* Space after radio button in RTL */
        transform: scale(1.1); /* Slightly larger radio button */
        vertical-align: middle; /* Align with text */
     }

     .options-area input[type="radio"]:checked + span {
         font-weight: bold;
         color: #007bff;
     }

     .options-area input[type="text"] {
        padding: 10px 12px;
        border: 1px solid #ced4da;
        border-radius: 5px;
        margin-top: 10px;
        display: block;
        width: calc(100% - 24px); /* Adjust width */
        font-size: 1em;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
        text-align: right; /* Ensure text input is RTL */
     }

     .options-area input[type="text"]:focus {
         border-color: #007bff;
         box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
         outline: none; /* Remove default outline */
     }


    /* Buttons */
    .game-button {
        display: block;
        width: 100%;
        padding: 12px 20px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        margin-top: 20px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 10px rgba(0, 123, 255, 0.2);
        font-weight: bold;
    }

    .game-button:hover {
        background-color: #0056b3;
        box-shadow: 0 6px 12px rgba(0, 123, 255, 0.3);
    }

    .game-button:active {
        background-color: #004085;
        transform: scale(0.98); /* Subtle press effect */
        box-shadow: 0 2px 5px rgba(0, 123, 255, 0.2);
    }

     .game-button:disabled {
        background-color: #ccc;
        cursor: not-allowed;
        box-shadow: none;
     }

     .next-button {
         background-color: #28a745; /* Green for next */
         box-shadow: 0 4px 10px rgba(40, 167, 69, 0.2);
     }
     .next-button:hover {
         background-color: #218838;
         box-shadow: 0 6px 12px rgba(40, 167, 69, 0.3);
     }
      .next-button:active {
        background-color: #1e7e34;
        transform: scale(0.98);
        box-shadow: 0 2px 5px rgba(40, 167, 69, 0.2);
     }


    /* Feedback Area */
    .feedback-area {
        margin-top: 25px;
        padding: 20px;
        border-radius: 8px;
        font-size: 1.05em;
        line-height: 1.6;
        display: none; /* Managed by JS */
        opacity: 0; /* Initial state for animation */
        transform: translateY(20px); /* Initial state for animation */
        transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    }

    .feedback-area.visible {
         display: block;
         opacity: 1;
         transform: translateY(0);
    }

    .feedback-area.correct {
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
        box-shadow: 0 4px 10px rgba(40, 167, 69, 0.1);
    }

    .feedback-area.incorrect {
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
        box-shadow: 0 4px 10px rgba(220, 53, 69, 0.1);
        animation: shake 0.5s; /* Add shake animation */
    }

    /* Shake animation for incorrect feedback */
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
        20%, 40%, 60%, 80% { transform: translateX(5px); }
    }

    /* Game Complete Message */
    .game-complete-message {
        margin-top: 30px;
        padding: 30px;
        background-color: #e9ffea; /* Light green */
        color: #155724; /* Dark green */
        border: 2px dashed #28a745; /* Green border */
        border-radius: 10px;
        text-align: center;
        font-size: 1.2em;
        font-weight: bold;
        opacity: 0; /* Start hidden */
        transform: scale(0.9); /* Start smaller */
        animation: pop-in 0.6s ease-out forwards; /* Animation */
    }
     .game-complete-message h2 {
         color: #155724;
         margin-top: 0;
         margin-bottom: 15px;
     }

    @keyframes pop-in {
        0% { opacity: 0; transform: scale(0.9); }
        70% { opacity: 1; transform: scale(1.05); }
        100% { opacity: 1; transform: scale(1); }
    }


    /* Explanation Section */
    #explanation-button {
        display: block;
        width: 100%;
        max-width: 850px;
        margin: 20px auto; /* Center the button */
        padding: 12px 20px;
        background-color: #6c757d; /* Grey */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: 0 4px 10px rgba(108, 117, 125, 0.2);
         font-weight: bold;
         text-align: center; /* Center text within button */
    }
    #explanation-button:hover {
        background-color: #545b62;
        box-shadow: 0 6px 12px rgba(108, 117, 125, 0.3);
    }
     #explanation-button:active {
        background-color: #494f54;
        transform: scale(0.98);
        box-shadow: 0 2px 5px rgba(108, 117, 125, 0.2);
     }


    #explanation-content {
        display: none; /* Initially hidden */
        margin: 30px auto; /* Center the content */
        max-width: 850px;
        padding: 30px;
        border: 1px solid #ccc;
        border-radius: 12px;
        background-color: #f9f9f9;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
        text-align: right;
        direction: rtl;
        line-height: 1.7;
    }
     #explanation-content h2, #explanation-content h3 {
        color: #004085;
        margin-bottom: 15px;
     }
    #explanation-content p, #explanation-content ul {
        margin-bottom: 15px;
        text-align: right;
        color: #333;
    }
     #explanation-content ul {
         padding-right: 25px; /* Indent lists */
         list-style-type: disc;
     }
     #explanation-content li {
         margin-bottom: 10px;
     }

</style>

<button id="explanation-button">הצגת הסבר מורחב: לפענח את ה-IPCC</button>

<div id="explanation-content">
    <h2>מהם דוחות ה-IPCC ולמה הם המפתח להבנת האקלים?</h2>
    <p>הפאנל הבין-ממשלתי לשינוי האקלים (IPCC) הוא גוף ייחודי המאגד אלפי מדענים מרחבי העולם. מטרתו אינה לבצע מחקר חדש, אלא לסכם ולהעריך באופן שיטתי את כל הידע המדעי הרלוונטי לשינוי האקלים. הדוחות שלו הם ההסכמה המדעית הרחבה ביותר הקיימת, והם הבסיס עליו ממשלות ברחבי העולם בונות את מדיניות האקלים שלהן.</p>

    <h2>ניווט במבוך המידע: מבנה דוחות ה-IPCC</h2>
    <p>דוחות ה-IPCC, במיוחד דוחות ההערכה הגדולים (Assessment Reports - AR), הם מסמכים אדירים. כדי להפוך אותם לנגישים, הם בנויים בשכבות:</p>
    <ul>
        <li>**סיכום למקבלי מדיניות (Summary for Policymakers - SPM):** זהו ה"שער" לדוח. הוא תמציתי, כתוב בשפה ברורה יחסית (אם כי עדיין מקצועית), ומציג את הממצאים החשובים ביותר ואת רמות הוודאות שלהם. קריאתו חיונית לכל מי שרוצה להבין את הליבה של הדוח.</li>
        <li>**סיכום טכני (Technical Summary - TS):** צעד אחד עמוק יותר. מספק פירוט רב יותר מה-SPM, כולל גרפים ונתונים נוספים, אך עדיין מהווה סיכום מרוכז של החומר המלא.</li>
        <li>**פרקים מלאים (Full Chapters):** אלו הם לב הדוח, שבהם מפורטים הניתוחים המדעיים לעומק. כל פרק מתמקד בנושא ספציפי (כמו פיזיקת האקלים, שינויים נצפים, תחזיות עתידיות, אירועי קיצון), וכולל סקירה מקיפה של הספרות המדעית הרלוונטית. קריאתם דורשת רקע מעמיק יותר.</li>
    </ul>

    <h2>השפה הסודית של ה-IPCC: ודאות והסתברות</h2>
    <p>כדי לתת למקבלי החלטות תמונה מדויקת ככל האפשר, ה-IPCC משתמש בשפה מכוילת בקפידה לתיאור רמות הוודאות של הממצאים. קיימים שני סולמות עיקריים:</p>
    <ul>
        <li>**רמת וודאות (Confidence):** זוהי הערכה איכותית של חוזק הראיות המדעיות (איכות המחקרים, היקף הנתונים, הסכמה בין מומחים). היא נעה על סקאלה מ-Very Low Confidence (וודאות נמוכה מאוד) ל-Very High Confidence (וודאות גבוהה מאוד).</li>
        <li>**הסתברות (Likelihood):** זוהי הערכה כמותית, המבוססת על ניתוח סטטיסטי, של הסיכוי שתוצאה או אירוע מסוים אכן התרחש או יתרחש. מבוטא במונחים כמו:
            <ul>
                <li>Virtually certain: >99% probability (כמעט ודאי)</li>
                <li>Very likely: 90–100% probability (סביר מאוד)</li>
                <li>Likely: 66–100% probability (סביר)</li>
                <li>About as likely as not: 33–66% probability (סיכויים שווים בערך)</li>
                <li>Unlikely: 0–33% probability (לא סביר)</li>
                <li>Very unlikely: 0–10% probability (לא סביר כלל)</li>
                <li>Exceptionally unlikely: 0–1% probability (לא סביר באופן חריג)</li>
            </ul>
            הבנה של ההבדל בין Confidence (חוזק הראיות) לבין Likelihood (סיכוי מחושב) היא קריטית לפענוח נכון של הדוחות.
        </li>
    </ul>

    <h2>לנווט בים הנתונים: פענוח גרפים וטבלאות</h2>
    <p>דוחות ה-IPCC עשירים בייצוגים חזותיים. כדי להבין אותם, שימו לב לנקודות הבאות:</p>
    <ul>
        <li>**כותרת וצירים:** תמיד בדקו מה הגרף/טבלה מציגים (טמפרטורה, פליטות, פני ים וכו'), מהן היחידות, ואיזה טווח זמן הם מכסים.</li>
        <li>**תרחישים עתידיים (Scenarios):** רבים מהגרפים מציגים תחזיות תחת תרחישים שונים של פליטות עתידיות (כמו SSPs - Shared Socioeconomic Pathways). כל תרחיש מיוצג בקו או אזור נפרד, ומשקף עולם שונה מבחינת מדיניות אקלים והתפתחות סוציו-אקונומית.</li>
        <li>**טווחים ואי-ודאות:** מדע האקלים עוסק במערכת מורכבת, ולכן יש אי-ודאות. גרפים רבים מציגים לא רק קו או נקודה בודדת (ההערכה ה'חציונית' או ה'טובה ביותר'), אלא גם אזורים מוצללים המייצגים טווח הסתברות (למשל, הטווח ה'סביר' - 66-100%).</li>
        <li>**נקודת ייחוס (Baseline):** שינויים מוצגים לרוב ביחס לתקופת ייחוס מסוימת (לרוב סוף המאה ה-19 או תחילת המאה ה-20, לפני ההשפעה האנושית המשמעותית על האקלים).</li>
    </ul>

    <h2>מסקנות המפתח מהדוחות האחרונים (במבט על)</h2>
    <p>דוח ההערכה השישי (AR6), שפורסם בין 2021 ל-2023, חיזק והעמיק את המסקנות מהדוחות הקודמים, והוסיף עדויות רבות עוצמה:</p>
    <ul>
        <li>**השפעה אנושית:** קיימת וודאות גבוהה ביותר (Unequivocal) שהאדם הוא הגורם העיקרי להתחממות הגלובלית שנצפתה מאז התקופה הטרום-תעשייתית.</li>
        <li>**קצב שינוי חסר תקדים:** קצב ההתחממות הנוכחי, והשינויים הנלווים במערכת האקלים, הם חסרי תקדים בקנה מידה של מאות ואף אלפי שנים.</li>
        <li>**שינויים בלתי הפיכים:** חלק מהשינויים שנצפים כבר כיום, כמו עליית פני הים או התכווצות יריעות הקרח, הם בלתי הפיכים בקנה מידה של מאות עד אלפי שנים גם תחת תרחישי פליטות נמוכות.</li>
        <li>**אירועי קיצון:** ישנה עדות מחוזקת מאוד לכך שאירועי קיצון רבים (גלי חום, גשמים עזים, בצורות) הפכו תכופים ועוצמתיים יותר עקב ההשפעה האנושית, ורבים מהם מיוחסים כעת בבירור לשינוי האקלים הנגרם על ידי האדם.</li>
        <li>**החשיבות של כל עשירית מעלה:** כל עלייה נוספת בטמפרטורה מגבירה משמעותית את הסיכון ואת העוצמה של אירועי קיצון ואת ההשפעות המסוכנות על בני אדם ומערכות אקולוגיות. הגבלת ההתחממות ל-1.5°C דורשת הפחתות פליטות דרמטיות ומיידיות.</li>
    </ul>
</div>

<script>
    const questions = [
        {
            snippet: `
                <h3>Box 1.1 | Summary of Likelihood Terms</h3>
                <p>The terms used to describe the assessed likelihood of an outcome or result for which a probability estimate can be assigned are based on statistical analysis of observations or model results, or both, and are defined as follows:</p>
                <ul>
                    <li>Virtually certain &gt;99% probability</li>
                    <li>Very likely 90–100% probability</li>
                    <li>Likely 66–100% probability</li>
                    <li>About as likely as not 33–66% probability</li>
                    <li>Unlikely 0–33% probability</li>
                    <li>Very unlikely 0–10% probability</li>
                    <li>Exceptionally unlikely 0–1% probability</li>
                </ul>
                <p>Additional terms (Extremely likely 95–100%, More likely than not >50–100%, Extremely unlikely 0–5%) may also be used when appropriate.</p>
            `,
            question: "על פי סיכום המונחים שבקטע, איזה מונח משמש לתיאור הסתברות בטווח 66–100%?",
            type: "multiple-choice",
            options: ["Very likely", "Likely", "About as likely as not", "Virtually certain"],
            answer: "Likely",
            feedback: "קריאת מונחי ה'Likelihood' היא מיומנות בסיסית! המונח 'Likely' בדוחות IPCC אכן מציין הסתברות של 66–100%. שימו לב שלמרות שהטווח חופף חלקית עם 'Very likely', המונח הספציפי ל-66-100% הוא 'Likely'."
        },
        {
            snippet: `
                <h3>Figure SPM.8 | Future annual global mean surface air temperature change</h3>
                <p>Projections of annual global mean surface air temperature change relative to 1850–1900, across the 2015–2100 period. Shown are projections under five illustrative SSP scenarios (SSP1-1.9, SSP1-2.6, SSP2-4.5, SSP3-7.0, and SSP5-8.5). The lines show the median estimate and shading shows the 5th–95th percentile range.</p>
                <p>[...imagine a graph here showing temperature rise over time for different SSPs, specifically the SSP5-8.5 line peaking highest...]</p>
                <p>Table SPM.1 (excerpt): Projected global surface temperature change relative to 1850-1900</p>
                <table>
                    <tr>
                        <th>Scenario</th>
                        <th>2081–2100 (Median)</th>
                        <th>2081–2100 (likely range)</th>
                    </tr>
                    <tr>
                        <td>SSP1-1.9</td>
                        <td>1.5 °C</td>
                        <td>1.2–1.7 °C</td>
                    </tr>
                     <tr>
                        <td>SSP2-4.5</td>
                        <td>2.7 °C</td>
                        <td>2.1–3.5 °C</td>
                    </tr>
                    <tr>
                        <td>SSP5-8.5</td>
                        <td>4.4 °C</td>
                        <td>3.3–5.7 °C</td>
                    </tr>
                </table>
            `,
            question: "על פי הטבלה המצורפת לקטע, מהי ההערכה החציונית (Median) לשינוי הטמפרטורה הממוצעת העולמית עד שנת 2081–2100 תחת התרחיש SSP5-8.5 (תרחיש 'עסקים כרגיל' עם פליטות גבוהות מאוד)? (הכניסו רק את המספר במעלות צלזיוס, ללא יחידות)",
            type: "text-input",
            answer: "4.4",
            feedback: "מעולה! פענוח טבלאות הוא חיוני. הטבלה מראה שההערכה החציונית (Median) לשינוי הטמפרטורה תחת תרחיש SSP5-8.5, שהוא תרחיש הפליטות הגבוה ביותר, היא 4.4°C עד סוף המאה. שימו לב שהטבלה מציגה גם טווח 'סביר' (likely range) של 3.3-5.7°C, מה שמדגיש את אי-הוודאות אך גם את הפוטנציאל להתחממות קיצונית."
        },
        {
            snippet: `
                 <h3>A.1 The physical science basis (Excerpt from SPM)</h3>
                 <p>A.1.1 It is unequivocal that human influence has warmed the atmosphere, ocean and land. Widespread and rapid changes in the atmosphere, ocean, cryosphere and biosphere have occurred.</p>
                 <p>A.1.2 The scale of recent changes across the climate system as a whole – and the present state of many aspects of the climate system – are unprecedented over many centuries to many thousands of years.</p>
                 <p>A.1.3 The likely range of total human-caused global surface temperature increase from 1850–1900 to 2010–2019 is 0.8°C to 1.3°C, with a best estimate of 1.07°C. It is likely that well-mixed greenhouse gases were the main driver of tropospheric warming since 1979 and extremely likely that anthropogenic aerosol forcing contributed a net negative effect to global surface temperature change since 1850–1900. Observed increases in well-mixed greenhouse gas concentrations since around 1750 are unequivocally caused by human activities.</p>
            `,
            question: "על פי קטע A.1.1, מהי הקביעה המרכזית שה-IPCC מצהיר עליה כ'חד משמעית' (unequivocal) לגבי השפעת האדם?",
            type: "multiple-choice",
            options: ["שפליטת גזי חממה תמשיך לעלות בעשורים הקרובים.", "שהאדם הוא הגורם הדומיננטי להתחממות שנצפתה באטמוספירה, באוקיינוסים וביבשה.", "שעליית פני הים היא כעת בלתי הפיכה.", "שאירועי קיצון הקשורים לחום יתרחשו בתדירות גבוהה יותר בכל האזורים המאוכלסים."],
            answer: "שהאדם הוא הגורם הדומיננטי להתחממות שנצפתה באטמוספירה, באוקיינוסים וביבשה.",
            feedback: "מדויק! זהו אחד הממצאים החשובים ביותר והמבוססים ביותר בדוח AR6: השפעת האדם על חימום כדור הארץ היא 'חד משמעית' (unequivocal). המשמעות היא שהוודאות המדעית בנושא זה גבוהה ביותר. האפשרויות האחרות אומנם נכונות במידה רבה לפי הדוח, אך הן אינן הקביעה ה'חד משמעית' בנקודה A.1.1."
        }
    ];

    let currentQuestionIndex = 0;
    const reportSnippetDiv = document.getElementById('report-snippet');
    const questionTextP = document.getElementById('question-text');
    const optionsAreaDiv = document.getElementById('options-area');
    const submitButton = document.getElementById('submit-answer');
    const feedbackAreaDiv = document.getElementById('feedback-area');
    const nextButton = document.getElementById('next-question');
    const explanationButton = document.getElementById('explanation-button');
    const explanationContentDiv = document.getElementById('explanation-content');
    const progressIndicator = document.getElementById('progress-indicator');
    const currentQSpan = document.getElementById('current-q');
    const totalQSpan = document.getElementById('total-q');
    const gameCompleteMessage = document.getElementById('game-complete');
    const questionAreaDiv = document.getElementById('question-area');


    totalQSpan.textContent = questions.length; // Set total questions count

    function loadQuestion(index) {
        // Hide previous elements with animation/delay
        reportSnippetDiv.style.opacity = 0;
        questionAreaDiv.style.opacity = 0;
        feedbackAreaDiv.classList.remove('visible'); // Hide feedback immediately

        setTimeout(() => { // Delay loading new content for animation effect
            if (index >= questions.length) {
                // End of game flow
                reportSnippetDiv.style.display = 'none';
                questionAreaDiv.style.display = 'none';
                submitButton.style.display = 'none';
                feedbackAreaDiv.style.display = 'none';
                nextButton.style.display = 'none';
                progressIndicator.style.display = 'none'; // Hide progress
                gameCompleteMessage.style.display = 'block'; // Show completion message
                // Trigger animation on game complete message happens via CSS animation on display block

                // Optional: scroll to game complete message
                 gameCompleteMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });

                return;
            }

            const q = questions[index];
            reportSnippetDiv.innerHTML = q.snippet;
            questionTextP.textContent = q.question;
            feedbackAreaDiv.textContent = ''; // Clear feedback
            feedbackAreaDiv.className = 'feedback-area'; // Reset class
            nextButton.style.display = 'none';
            submitButton.style.display = 'block';
            submitButton.disabled = false;
            currentQSpan.textContent = index + 1; // Update progress

            optionsAreaDiv.innerHTML = ''; // Clear previous options

            if (q.type === "multiple-choice") {
                q.options.forEach((option, i) => {
                    const label = document.createElement('label');
                    const input = document.createElement('input');
                    input.type = 'radio';
                    input.name = 'answer';
                    input.value = option;
                    label.appendChild(input);
                    label.appendChild(document.createElement('span')).textContent = option; // Use span for styling text
                    optionsAreaDiv.appendChild(label);
                });
            } else if (q.type === "text-input") {
                const input = document.createElement('input');
                input.type = 'text';
                input.id = 'text-answer';
                input.setAttribute('placeholder', 'הקלד תשובה כאן...'); // Add placeholder
                optionsAreaDiv.appendChild(input);
            }

            // Show new content with animation
             reportSnippetDiv.style.display = 'block';
             questionAreaDiv.style.display = 'block';
             setTimeout(() => { // Small delay before fading in
                 reportSnippetDiv.style.opacity = 1;
                 questionAreaDiv.style.opacity = 1;
             }, 50);


        }, 600); // Delay time matches fade-out transition
    }

    function checkAnswer() {
        const q = questions[currentQuestionIndex];
        let userAnswer = null;

        if (q.type === "multiple-choice") {
            const selectedOption = document.querySelector('input[name="answer"]:checked');
            if (selectedOption) {
                userAnswer = selectedOption.value;
            }
        } else if (q.type === "text-input") {
            const textInput = document.getElementById('text-answer');
             if (textInput) {
                // Basic normalization for text input (case-insensitive, trim whitespace)
                userAnswer = textInput.value.trim().toLowerCase();
                // Normalize correct answer for comparison
                q.normalizedAnswer = q.answer.trim().toLowerCase();
            }
        }

        if (userAnswer === null || userAnswer === "") {
            // Optional: Add a visual cue or small shake to the options/input area
             optionsAreaDiv.style.border = '1px solid red'; // Simple visual cue
             setTimeout(() => optionsAreaDiv.style.border = '1px solid #e9ecef', 1000); // Reset border
            feedbackAreaDiv.textContent = "אופס! נראה שלא בחרת או הכנסת תשובה. אנא נסו שוב.";
            feedbackAreaDiv.className = 'feedback-area incorrect visible';
            return;
        }

        submitButton.disabled = true; // Disable button after submitting

        // Compare normalized answer for text input, original for MC
        const isCorrect = q.type === "text-input" ? (userAnswer === q.normalizedAnswer) : (userAnswer === q.answer);


        if (isCorrect) {
            feedbackAreaDiv.textContent = "מעולה! תשובה נכונה. " + q.feedback;
            feedbackAreaDiv.className = 'feedback-area correct visible';
            nextButton.style.display = 'block';
            // Optional: scroll to feedback
             feedbackAreaDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

        } else {
            feedbackAreaDiv.textContent = "זו לא התשובה הנכונה כרגע. " + q.feedback;
            feedbackAreaDiv.className = 'feedback-area incorrect visible';
            submitButton.disabled = false; // Allow trying again
             // Optional: scroll to feedback
            feedbackAreaDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
    }

    function showNextQuestion() {
        currentQuestionIndex++;
        loadQuestion(currentQuestionIndex);
         // Optional: scroll back to the top of the game container
        document.querySelector('.ipcc-game-container').scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    // Event listeners
    submitButton.addEventListener('click', checkAnswer);
    nextButton.addEventListener('click', showNextQuestion);

    explanationButton.addEventListener('click', () => {
        const isHidden = explanationContentDiv.style.display === 'none' || explanationContentDiv.style.display === '';
        explanationContentDiv.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר הסבר מורחב' : 'הצגת הסבר מורחב: לפענח את ה-IPCC';
        // Optional: scroll to the explanation section if showing it
        if (!isHidden) {
            explanationContentDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

    // Initialize the first question after DOM is ready
    document.addEventListener('DOMContentLoaded', () => {
         // Initial state setting via JS is safer than relying solely on CSS display: none for complex flows
         gameCompleteMessage.style.display = 'none';
         feedbackAreaDiv.style.display = 'none'; // Ensure feedback is hidden initially
         nextButton.style.display = 'none'; // Ensure next is hidden initially
         loadQuestion(currentQuestionIndex);
    });


</script>