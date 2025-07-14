---
title: "פענוח גרפי שוק ההון: ממוצעים ונרות"
english_slug: deciphering-stock-market-charts-moving-averages-candlesticks
category: "מדעי החברה / כלכלה ופיננסים"
tags: [שוק ההון, ניתוח טכני, גרפים פיננסיים, נרות יפניים, ממוצעים נעים]
---
# לפענח את השוק: מדריך אינטראקטיבי לנרות וממוצעים נעים

האם הסתכלת פעם על גרף מניות ותהית: מה כל הקווים והצורות האלה אומרים? האם הם באמת יכולים לעזור לחזות לאן המחיר הולך? בוא נגלה יחד!

<div id="app-container" dir="rtl">
    <div id="header-area">
        <h2 class="app-title">צלול לגרף: אתגר פענוח תבניות</h2>
        <p class="app-subtitle">אתגר את עצמך לזהות תבניות מפתח ולחזות את המהלך הבא בשוק וירטואלי.</p>
         <div id="progress-area">
            <span id="scenario-counter">תרחיש 1 מתוך 3</span>
         </div>
    </div>


    <div id="chart-area">
        <!-- Interactive Chart Representation -->
        <div id="scenario-description">
            <!-- Scenario text and basic visual representation will be injected here by JS -->
        </div>
         <div id="chart-visual-hint">
             <!-- Simple visual elements added by JS for hints -->
         </div>
    </div>

    <div id="user-input-area">
        <p class="question"><strong>שאלה:</strong> <span id="question-text"></span></p>
        <div class="input-group" id="pattern-selection">
            <label for="pattern-type">זהה את התבנית המרכזית:</label>
            <select id="pattern-type">
                <option value="">בחר תבנית</option>
                <!-- Options populated by JS -->
            </select>
        </div>
        <div class="input-group" id="prediction-selection">
            <label for="price-prediction">חזה את מהלך המחיר הסביר הבא:</label>
            <select id="price-prediction">
                <option value="">בחר חיזוי</option>
                <option value="up">עלייה</option>
                <option value="down">ירידה</option>
                <option value="sideways">דשדוש</option>
            </select>
        </div>
    </div>

    <button id="submit-prediction" class="action-button">שלח את הניתוח שלך</button>

    <div id="feedback-area" class="feedback-box" style="display: none;">
        <!-- Feedback and outcome will appear here -->
        <div id="outcome-description"></div>
        <div id="feedback-text"></div>
        <div id="pattern-explanation"></div>
         <button id="show-prediction-explanation" class="subtle-button">הצג הסבר לחיזוי</button>
         <div id="prediction-explanation" class="hidden"></div>
    </div>

    <div id="navigation-area" class="button-group">
        <button id="next-scenario" class="action-button" style="display: none;">תרחיש הבא &gt;</button>
        <button id="finish-scenarios" class="action-button finish-button" style="display: none;">סיים את האתגר</button>
    </div>

</div>

<style>
    /* General App Styling */
    #app-container {
        font-family: 'Arial', sans-serif; /* Use a clean, standard font */
        max-width: 700px;
        margin: 30px auto; /* More margin */
        padding: 30px; /* More padding */
        border: 1px solid #dcdcdc; /* Subtle border */
        border-radius: 12px; /* More rounded corners */
        background-color: #f8f9fa; /* Light background */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1); /* Soft shadow */
        direction: rtl; /* Ensure RTL */
        color: #333;
    }

    .app-title {
        text-align: center;
        color: #0056b3; /* Primary color */
        margin-bottom: 10px;
        font-size: 1.8em;
        border-bottom: none; /* Remove default border */
        padding-bottom: 0;
    }

    .app-subtitle {
        text-align: center;
        color: #555;
        margin-top: 0;
        margin-bottom: 25px; /* More space below subtitle */
        font-size: 1em;
    }

     #progress-area {
         text-align: center;
         margin-bottom: 25px;
         font-size: 0.9em;
         color: #007bff;
         font-weight: bold;
     }

    /* Chart Area Styling */
    #chart-area {
        min-height: 180px; /* Slightly taller */
        border: 1px solid #ccc;
        margin-bottom: 25px;
        padding: 15px; /* More padding */
        background: linear-gradient(to bottom, #e9ecef, #dee2e6); /* Subtle gradient background */
        border-radius: 8px; /* Rounded corners */
        position: relative; /* For absolute positioning of hints */
        overflow: hidden; /* Clear floats */
         text-align: right; /* Align text to the right */
         line-height: 1.6; /* Better readability */
         white-space: pre-wrap; /* Preserve line breaks in scenario description */
         font-family: 'Courier New', monospace; /* Monospace for text charts */
    }

    #scenario-description {
        color: #333;
        margin-bottom: 10px;
    }

    #chart-visual-hint {
         position: absolute;
         top: 15px; /* Match chart area padding */
         left: 15px; /* Match chart area padding */
         right: 15px;
         bottom: 15px;
         pointer-events: none; /* Allow clicks to pass through */
         z-index: 1; /* Ensure it's above description if needed */
    }


    /* Input Area Styling */
    #user-input-area {
        margin-bottom: 25px; /* More margin */
        background-color: #e9ecef; /* Light contrast background */
        padding: 20px;
        border-radius: 8px;
    }

    .question {
         margin-bottom: 15px;
         font-size: 1.1em;
         color: #0056b3;
    }

    .input-group {
        margin-bottom: 15px;
        display: flex; /* Align label and select */
        align-items: center;
        flex-wrap: wrap; /* Wrap on smaller screens */
    }

    .input-group label {
        margin-left: 10px; /* Space between label and select */
        font-weight: bold;
        color: #555;
        min-width: 120px; /* Ensure labels have some minimum width */
    }

    select {
        flex-grow: 1; /* Allow select to take available space */
        padding: 10px 12px; /* More padding */
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 1em;
        color: #333;
        background-color: #fff;
        cursor: pointer;
        transition: border-color 0.2s ease-in-out;
    }

    select:hover {
        border-color: #007bff;
    }

     select:focus {
         outline: none;
         border-color: #007bff;
         box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
     }

    /* Button Styling */
    .action-button {
        display: block; /* Full width button */
        width: 100%;
        padding: 12px 20px; /* More padding */
        background-color: #007bff; /* Primary blue */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em; /* Larger font */
        font-weight: bold;
        transition: background-color 0.2s ease-in-out, transform 0.1s ease;
        text-align: center;
        margin-top: 15px; /* Space above button */
    }

    .action-button:hover {
        background-color: #0056b3; /* Darker blue on hover */
    }

    .action-button:active {
        transform: scale(0.98); /* Subtle press effect */
    }

     .action-button:disabled {
         background-color: #cccccc;
         cursor: not-allowed;
     }

    .finish-button {
         background-color: #28a745; /* Green for finish */
    }
    .finish-button:hover {
         background-color: #218838; /* Darker green */
    }


     .subtle-button {
        background: none;
        border: none;
        color: #007bff;
        text-decoration: underline;
        cursor: pointer;
        font-size: 0.9em;
        margin-top: 10px;
        padding: 0;
        transition: color 0.2s ease;
     }
     .subtle-button:hover {
         color: #0056b3;
     }


    .button-group {
        display: flex;
        justify-content: space-between; /* Space out buttons if multiple */
         gap: 10px; /* Space between buttons */
    }

     .button-group .action-button {
         width: auto; /* Override full width for group buttons */
         flex-grow: 1; /* Distribute space */
         margin-top: 0;
     }


    /* Feedback Area Styling */
    .feedback-box {
        margin-top: 25px; /* More space above feedback */
        padding: 20px;
        border-left: 6px solid transparent; /* Left border for color coding */
        border-radius: 8px;
        transition: all 0.4s ease-in-out; /* Smooth transition on show/hide and color change */
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    #outcome-description {
         font-weight: bold;
         margin-bottom: 15px;
         color: #333;
    }

    #feedback-text {
        font-weight: bold;
        margin-bottom: 10px;
        line-height: 1.5;
    }

    #pattern-explanation, #prediction-explanation {
        font-style: italic;
        margin-top: 15px;
        line-height: 1.5;
        color: #555;
    }


    .feedback-box.correct {
        border-color: #28a745; /* Green */
        background-color: #d4edda; /* Light green */
        color: #155724; /* Dark green text */
    }

    .feedback-box.incorrect {
        border-color: #dc3545; /* Red */
        background-color: #f8d7da; /* Light red */
        color: #721c24; /* Dark red text */
    }

    .feedback-box.partial {
        border-color: #ffc107; /* Yellow */
        background-color: #fff3cd; /* Light yellow */
        color: #856404; /* Dark yellow text */
    }

    .hidden {
        display: none;
    }

    /* Explanation Area Styling */
    #explanation-area {
        margin-top: 40px;
        padding-top: 30px;
        border-top: 1px solid #eee;
        color: #333;
        direction: rtl;
        line-height: 1.6;
        transition: opacity 0.4s ease-in-out; /* Fade in */
    }

    #explanation-area.hidden {
        opacity: 0;
         height: 0; /* Collapse height */
         overflow: hidden; /* Hide content */
         padding-top: 0;
         margin-top: 0;
         border-top: none;
    }

    #explanation-area h2, #explanation-area h3 {
        color: #0056b3;
        border-bottom: 1px solid #eee;
        padding-bottom: 8px;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    #explanation-area ul {
        margin-bottom: 20px;
    }

    #explanation-area li {
        margin-bottom: 8px;
    }

    #explanation-area strong {
        color: #0056b3; /* Highlight key terms */
    }

    #toggle-explanation {
        display: block;
        width: 100%;
        text-align: center;
        margin-top: 25px; /* Space above button */
        padding: 10px 15px;
        background-color: #6c757d; /* Grey */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.2s ease-in-out;
    }
    #toggle-explanation:hover {
        background-color: #5a6268; /* Darker grey */
    }

</style>

<button id="toggle-explanation">הצג הסבר מלא על נרות וממוצעים נעים</button>

<div id="explanation-area" class="hidden" dir="rtl">
    <hr>
    <h2>הסבר מורחב: עקרונות הניתוח הטכני</h2>

    <p>כלי הניתוח הטכני שניסינו ליישם באתגר הם הלב הפועם של סוחרים רבים שמנסים להבין את תנועות המחיר ההיסטוריות כדי לצפות מהלכים עתידיים.</p>

    <h3>מהם נרות יפניים? - הסיפור מאחורי כל יום מסחר</h3>
    <p>תארו לעצמכם שכל יום מסחר הוא סיפור קצר שמסופר על ידי 'נר'. נרות יפניים (Candlesticks) מסכמים את הסיפור הזה ויזואלית בפרק זמן נתון (דקה, שעה, יום, שבוע וכו'). כל נר מורכב מארבעה נתונים קריטיים:</p>
    <ul>
        <li>**מחיר פתיחה:** איפה שהסיפור התחיל באותו יום (המסחר נפתח).</li>
        <li>**מחיר סגירה:** איפה שהסיפור הסתיים באותו יום (המסחר נסגר).</li>
        <li>**הגבוה של היום:** שיא הגובה שהמחיר הגיע אליו.</li>
        <li>**הנמוך של היום:** שפל התחתית שהמחיר נפל אליו.</li>
    </ul>

    <h3>מבנה הנר ומשמעותו - רגשות השוק בצבע וצורה</h3>
    <p>לנר שני חלקים ויזואליים עיקריים, שמבטאים את מאבק הקונים (השוורים 🐂) והמוכרים (הדובים 🐻) במהלך התקופה:</p>
    <ul>
        <li>**גוף הנר (Body):** החלק הרחב שמחבר את הפתיחה והסגירה. גודלו וצבעו מעידים על עוצמת התנועה וכיוונה:
            <ul>
                <li>**גוף ירוק/לבן (עולה 🟢):** מחיר הסגירה היה *גבוה* ממחיר הפתיחה. הקונים ניצחו בתקופה זו והמחיר עלה!</li>
                <li>**גוף אדום/שחור (יורד 🔴):** מחיר הסגירה היה *נמוך* ממחיר הפתיחה. המוכרים ניצחו בתקופה זו והמחיר ירד!</li>
            </ul>
        </li>
        <li>**צלליות (Shadows/Wicks):** הקווים הדקים שיוצאים מקצוות הגוף. הן מראות את המחיר הגבוה והנמוך ביותר שהושגו באותו פרק זמן, גם אם המחיר לא נסגר שם. צללית ארוכה מראה שהמחיר ניסה לנוע רחוק בכיוון מסוים, אך נהדף בחזרה על ידי הצד השני של השוק.</li>
    </ul>

    <h3>דוגמאות לתבניות נרות בסיסיות - סיפורים קצרים על היפוכי מגמה והמשכה</h3>
    <p>צורות נרות ספציפיות או צירופים שלהן יכולים לרמוז על מה שקורה "מתחת לפני השטח" ולהצביע על שינויים אפשריים:</p>
    <ul>
        <li>**דוז'י (Doji):** נר עם גוף קטן במיוחד (פתיחה וסגירה כמעט זהים). מעיד על <strong style="color: #ffc107;">אי-החלטיות</strong> בשוק - הקונים והמוכרים היו מאוזנים. יכול להופיע עם צלליות שונות ולרמוז על היפוך לאחר מגמה ארוכה.</li>
        <li>**פטיש (Hammer) / איש תלוי (Hanging Man):** גוף קטן וצללית תחתונה ארוכה במיוחד (לפחות פי 2 מהגוף), צללית עליונה קצרה. "פטיש" מופיע אחרי ירידה 📉 ויכול לרמוז על <strong style="color: #28a745;">היפוך שורי (Bullish Reversal)</strong> - הקונים הדפו את המחיר החזק למעלה. "איש תלוי" מופיע אחרי עלייה 📈 ויכול לרמוז על <strong style="color: #dc3545;">היפוך דובי (Bearish Reversal)</strong> - המוכרים החלו להשתלט למרות העלייה.</li>
        <li>**כוכב נופל (Shooting Star):** גוף קטן וצללית עליונה ארוכה במיוחד (לפחות פי 2 מהגוף), צללית תחתונה קצרה. מופיע אחרי עלייה 📈 ויכול לרמוז על <strong style="color: #dc3545;">היפוך דובי</strong> - הקונים ניסו לדחוף למעלה אך המוכרים הדפו את המחיר חזק למטה.</li>
        <li>**בליעה (Engulfing):** תבנית של שני נרות. הנר השני <strong style="color: #0056b3;">"בולע"</strong> לחלוטין את גוף הנר הראשון. <strong style="color: #dc3545;">"בליעה דובית" (Bearish Engulfing)</strong>: אחרי עלייה (נר ירוק קטן) מגיע נר אדום גדול שבולע אותו - <strong style="color: #dc3545;">אות להיפוך לירידה</strong>. <strong style="color: #28a745;">"בליעה שורית" (Bullish Engulfing)</strong>: אחרי ירידה (נר אדום קטן) מגיע נר ירוק גדול שבולע אותו - <strong style="color: #28a745;">אות להיפוך לעלייה</strong>.</li>
    </ul>

    <h3>מהם ממוצעים נעים? - החלקת הרעש וזיהוי המגמה הגדולה</h3>
    <p>ממוצע נע (Moving Average, MA) הוא כמו 'ממוצע רץ' של המחיר לאורך תקופה מסוימת (למשל, 50 יום או 200 יום). הוא מחליק את התנודות היומיומיות ויוצר קו אחד שעוזר לזהות את <strong style="color: #0056b3;">כיוון המגמה הכללית</strong> ולהבין האם המחיר מעליה (שוריות) או מתחתיה (דוביות). ממוצעים קצרים (כמו 20 או 50) מגיבים מהר יותר לשינויים קצרי טווח, וארוכים (100, 200) מזהים מגמות משמעותיות יותר.</p>

    <h3>נקודות חצייה של ממוצעים נעים - אותות גדולים בשוק?</h3>
    <p>כאשר ממוצע נע קצר חוצה ממוצע נע ארוך, זה יכול להיות אירוע משמעותי שסוחרים רבים עוקבים אחריו:</p>
    <ul>
        <li>**"צלב זהב" (Golden Cross 🌟):** ממוצע קצר חוצה את הממוצע הארוך <strong style="color: #28a745;">כלפי מעלה</strong>. נחשב לאות <strong style="color: #28a745;">שורי חזק</strong>, שיכול לבשר על תחילת מגמת עלייה ארוכת טווח.</li>
        <li>**"צלב מוות" (Death Cross 💀):** ממוצע קצר חוצה את הממוצע הארוך <strong style="color: #dc3545;">כלפי מטה</strong>. נחשב לאות <strong style="color: #dc3545;">דובי חזק</strong>, שיכול לבשר על תחילת מגמת ירידה ארוכת טווח.</li>
    </ul>

    <h3>השילוב המנצח - נרות וממוצעים עובדים יחד</h3>
    <p>ניתוח טכני חכם משלב כלים שונים. נרות יכולים לתת רמזים מוקדמים להיפוך קצר טווח (למשל, נר פטיש בדיוק על קו ממוצע נע המשמש כתמיכה!), בעוד שהממוצעים מאשרים את המגמה הגדולה יותר. השילוב עוזר לקבל תמונה מלאה יותר.</p>

    <h3>מילה של זהירות - ניתוח טכני הוא לא קסם!</h3>
    <p>זכרו תמיד: ניתוח טכני הוא כלי <strong style="color: #ffc107;">הסתברותי</strong>, לא ודאי. השוק מושפע מאינספור גורמים (חדשות, כלכלה, פוליטיקה) שלא תמיד רואים בגרף בלבד. תבניות יכולות להיכשל. לכן, תמיד מומלץ לשלב ניתוח טכני עם הבנה רחבה יותר של הנכס והשוק, ולעולם לא להשקיע יותר ממה שאתם יכולים להרשות לעצמכם להפסיד.</p>

</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const appContainer = document.getElementById('app-container');
        const scenarioDescription = document.getElementById('scenario-description');
        const chartVisualHint = document.getElementById('chart-visual-hint'); // Added visual hint div
        const questionText = document.getElementById('question-text');
        const patternSelection = document.getElementById('pattern-selection');
        const patternTypeSelect = document.getElementById('pattern-type');
        const predictionSelection = document.getElementById('prediction-selection');
        const pricePredictionSelect = document.getElementById('price-prediction');
        const submitButton = document.getElementById('submit-prediction');
        const feedbackArea = document.getElementById('feedback-area');
        const outcomeDescription = document.getElementById('outcome-description');
        const feedbackText = document.getElementById('feedback-text');
        const patternExplanation = document.getElementById('pattern-explanation');
        const predictionExplanationDiv = document.getElementById('prediction-explanation'); // New div for prediction explanation
        const showPredictionExplanationButton = document.getElementById('show-prediction-explanation'); // Button to toggle it
        const nextScenarioButton = document.getElementById('next-scenario');
        const finishScenariosButton = document.getElementById('finish-scenarios');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationArea = document.getElementById('explanation-area');
        const scenarioCounter = document.getElementById('scenario-counter'); // Progress indicator

        let currentScenarioIndex = 0;

        // Define the interactive scenarios
        const scenarios = [
            {
                id: 1,
                description: "<strong>תרחיש 1: נר היפוך אפשרי לאחר ירידה</strong><br>המחיר ירד בחדות במשך כמה ימים (📉📉📉). היום מופיע נר שנראה כך:<br><br><code>&nbsp;&nbsp;⚪ (פתיחה)&nbsp;&nbsp;</code><br><code>&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><br><code>&nbsp;&nbsp;▇ (גוף קטן אדום)</code><br><code>&nbsp;&nbsp;█&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><br><code>&nbsp;&nbsp;█&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><br><code>&nbsp;&nbsp;█&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><br><code>&nbsp;&nbsp;▄ (סגירה)&nbsp;&nbsp;</code><br><br>המחיר פתח גבוה יחסית וירד חזק במהלך היום, אך קונים נכנסו והדפו אותו חזרה למעלה לקראת הסגירה, למרות שהוא נשאר מעט מתחת לפתיחה (גוף אדום). הנמוך של היום היה הרבה מתחת לפתיחה/סגירה (צללית תחתונה ארוכה מאוד). המחיר נמצא כרגע מתחת לממוצעים הנעים הארוכים.",
                visual_hint: "<!-- Maybe add a simple visual hint here with CSS later -->", // Placeholder for potential future visual hint
                question: "איזו תבנית נרותית קלאסית מופיעה ביום האחרון, ומה היא עשויה לרמוז על מהלך המחיר הבא?",
                pattern_options: {
                    "hammer": "פטיש (Hammer) 🔨",
                    "shooting-star": "כוכב נופל (Shooting Star) ✨",
                    "doji": "דוז'י (Doji) ⚖️",
                    "bearish-engulfing": "בליעה דובית (Bearish Engulfing) 📉"
                },
                correct_pattern: "hammer",
                prediction_options: ["up", "down", "sideways"],
                correct_prediction: "up", // Hammers after downtrends suggest bullish reversal
                outcome_description: "<strong>התוצאה בפועל:</strong> ביום שאחרי, המחיר פתח גבוה, יצר נר ירוק גדול (🟢), והתחילה תנועת עלייה משמעותית.",
                pattern_explanation: "הנר שזוהה הוא אכן פטיש (Hammer). תבנית זו מאופיינת בגוף קטן (ירוק או אדום) וצללית תחתונה ארוכה במיוחד. כאשר פטיש מופיע לאחר ירידה משמעותית, הוא נחשב לתבנית היפוך שורית פוטנציאלית (Bullish Reversal). הצללית התחתונה הארוכה מעידה על כך שהמוכרים ניסו להוריד את המחיר לשפל חדש, אך קונים רבים נכנסו לשוק בנקודה זו, הדפו את המחיר חזק למעלה וצמצמו את הירידה. זה מרמז על כך שלחץ המכירה נחלש ולחץ הקנייה גובר, מה שיכול להוביל לעליית מחיר בהמשך.",
                prediction_explanation: "החיזוי לעלייה מתבסס על האות השורי החזק שמספק נר הפטיש כאשר הוא מופיע לאחר ירידה. הוא מצביע על כך שלפחות בטווח הקצר מאוד, המוכרים מאבדים שליטה והקונים לוקחים פיקוד, מה שמגדיל את ההסתברות למהלך עולה ביום/ימים הבאים."
            },
            {
                id: 2,
                description: "<strong>תרחיש 2: צלב הזהב - אות של מגמה ארוכת טווח?</strong><br>המניה נמצאת במגמת עלייה הדרגתית מזה חודשים (↗️↗️↗️). המחיר נסחר באופן עקבי מעל ממוצע נע 50 יום וממוצע נע 200 יום, ושני הממוצעים בעלייה. לאחרונה, ממוצע נע 50 יום המהיר (🟠) חצה את ממוצע נע 200 יום האיטי יותר (🔵) <strong style='color: green;'>כלפי מעלה</strong>.<br><br><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📈📈📈📈📈📈 (המחיר עולה)</code><br><code>&nbsp;&nbsp;🟠🟠🟠🟠🟠🟠↘️🔵🔵🔵🔵🔵🔵</code><br><code>&nbsp;&nbsp;🔵🔵🔵🔵🔵🔵↗️🟠🟠🟠🟠🟠🟠</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✨ (נקודת החצייה)</code>", // Using emojis and simple lines
                visual_hint: "", // Placeholder
                question: "זהה את תבנית הממוצעים הנעים הקלאסית שנוצרה, ומה היא מסמלת לרוב?",
                pattern_options: {
                    "golden-cross": "צלב זהב (Golden Cross) 🌟",
                    "death-cross": "צלב מוות (Death Cross) 💀",
                    "doji": "דוז'י (Doji) ⚖️",
                    "support-bounce": "קפיצה מתמיכה 💪"
                },
                correct_pattern: "golden-cross",
                prediction_options: ["up", "down", "sideways"],
                correct_prediction: "up", // Golden cross is bullish
                outcome_description: "<strong>התוצאה בפועל:</strong> לאחר החצייה הזו, מגמת העלייה הקיימת התחזקה והמניה המשיכה לנוע כלפי מעלה בחדות רבה יותר.",
                pattern_explanation: "התבנית שנוצרה כאשר ממוצע נע קצר חצה כלפי מעלה ממוצע נע ארוך נקראת צלב זהב (Golden Cross). תבנית זו נחשבת בדרך כלל לאות <strong style='color: #28a745;'>שורי (Bullish) חזק במיוחד</strong> בניתוח טכני, ולעיתים קרובות מצביעה על תחילתה של מגמת עלייה ארוכת טווח או על אישור והתחזקות של מגמת עלייה קיימת. היא מעידה על כך שלחץ הקנייה בטווח הקצר מספיק חזק כדי להשפיע על הממוצע ארוך הטווח.",
                prediction_explanation: "החיזוי לעלייה מתבסס ישירות על המשמעות המקובלת של תבנית צלב הזהב. למרות שזו אינה ערובה, מבחינה סטטיסטית וחוקי הניתוח הטכני הקלאסיים, תבנית זו מצביעה על סיכוי גבוה להמשך עלייה משמעותית."
            },
            {
                id: 3,
                description: "<strong>תרחיש 3: כוחה של תמיכה (עם רמז מנר)</strong><br>המניה נסחרת במגמת עלייה ברורה (↗️↗️↗️), וממוקמת מעל ממוצע נע 50 יום (🟠) שעולה גם הוא. המחיר עלה, ואז התחיל לתקן מעט וירד עד ש<strong style='color: blue;'>נגע בדיוק בקו של ממוצע נע 50 יום</strong>. ביום המגע הזה, הופיע נר עם גוף ירוק קטן (🟢) וצללית תחתונה ארוכה למדי (<code>█</code>) שירדה עד לממוצע הנע ואף מעט מתחתיו, אך נסגרה גבוה יותר.<br><br><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📈📈📈 (מחיר עולה)</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↘️ (תיקון)</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🟠🟠🟠🟠🟠🟠🟠 (ממוצע 50)</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;👇 (מגע)</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🟢 (נר עם גוף ירוק קטן)</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;█ (צללית תחתונה ארוכה שנגעה/עברה את הממוצע)</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↗️↗️↗️ (המשך עלייה?)</code>", // Using emojis and simple lines
                visual_hint: "", // Placeholder
                question: "איזו אינטראקציה חשובה התרחשה בגרף, ומהו מהלך המחיר הסביר לאחריה?",
                pattern_options: {
                    "support-bounce": "קפיצה חזקה מאזור תמיכה (Support Bounce) 💪",
                    "resistance-rejection": "דחייה חזקה מאזור התנגדות (Resistance Rejection) ✋",
                    "death-cross": "צלב מוות (Death Cross) 💀",
                    "bearish-engulfing": "בליעה דובית (Bearish Engulfing) 📉"
                },
                correct_pattern: "support-bounce",
                prediction_options: ["up", "down", "sideways"],
                correct_prediction: "up", // Bounce off support (MA) combined with a bullish candle
                outcome_description: "<strong>התוצאה בפועל:</strong> המחיר 'קפץ' בחדות כלפי מעלה מרגע המגע עם ממוצע נע 50 יום, ומגמת העלייה נמשכה ואף התחזקה.",
                pattern_explanation: "ממוצעים נעים פעמים רבות משמשים כאזורי <strong style='color: #28a745;'>תמיכה</strong> במגמת עלייה או <strong style='color: #dc3545;'>התנגדות</strong> במגמת ירידה. במקרה זה, ממוצע נע 50 יום פעל כתמיכה. העובדה שהמחיר נגע בו ומיד נהדף כלפי מעלה (באה לידי ביטוי בצללית התחתונה הארוכה והגוף הירוק הקטן של הנר) מעידה על כך שקונים רבים חיכו לרמות מחיר נמוכות יותר כדי להיכנס, והם 'הגנו' על הממוצע הנע. זוהי קפיצה קלאסית מתמיכה, המעידה על חוזק במגמה הקיימת.",
                prediction_explanation: "החיזוי לעלייה מתבסס על השילוב המשמעותי: המחיר נגע בתמיכה משמעותית (ממוצע נע 50) ומיד קיבל אישור כניסת קונים באמצעות צורת הנר הספציפית שנוצרה בנקודת המגע. זהו אות שורי מובהק המצביע על סבירות גבוהה להמשך תנועה בכיוון המגמה המקורית (עלייה)."
            }
        ];

        function populatePatternOptions(scenario) {
            const selectElement = patternTypeSelect;
            selectElement.innerHTML = '<option value="">בחר תבנית</option>'; // Reset
            for (const [key, value] of Object.entries(scenario.pattern_options)) {
                const option = document.createElement('option');
                option.value = key;
                option.textContent = value;
                selectElement.appendChild(option);
            }
        }

        function loadScenario(index) {
            if (index >= scenarios.length) {
                finishScenarios();
                return;
            }

            currentScenarioIndex = index;
            const scenario = scenarios[currentScenarioIndex];

            scenarioCounter.textContent = `תרחיש ${currentScenarioIndex + 1} מתוך ${scenarios.length}`;
            scenarioDescription.innerHTML = scenario.description;
            chartVisualHint.innerHTML = scenario.visual_hint || ''; // Load potential visual hint
            questionText.textContent = scenario.question;
            populatePatternOptions(scenario);
            pricePredictionSelect.value = ""; // Reset prediction selection
            patternTypeSelect.value = ""; // Reset pattern selection

            feedbackArea.style.display = 'none';
            feedbackArea.className = 'feedback-box'; // Reset feedback classes, keep base class
            outcomeDescription.innerHTML = '';
            feedbackText.innerHTML = '';
            patternExplanation.innerHTML = '';
            predictionExplanationDiv.innerHTML = scenario.prediction_explanation; // Load explanation
            predictionExplanationDiv.classList.add('hidden'); // Hide it initially
            showPredictionExplanationButton.style.display = 'inline-block'; // Show button

            submitButton.style.display = 'block';
            submitButton.disabled = false; // Enable submit button
            nextScenarioButton.style.display = 'none';
            finishScenariosButton.style.display = 'none';
            navigationArea.style.display = 'flex'; // Ensure button group is visible

            patternTypeSelect.disabled = false;
            pricePredictionSelect.disabled = false;

            // Hide navigation area initially until needed
             if (currentScenarioIndex === 0) {
                navigationArea.style.display = 'none';
             } else {
                 navigationArea.style.display = 'flex'; // Show for subsequent scenarios
             }

             // Ensure user inputs are visible
             patternSelection.style.display = 'flex';
             predictionSelection.style.display = 'flex';
             document.getElementById('user-input-area').style.display = 'block'; // Ensure the whole input area is visible
        }

        function submitPrediction() {
            const scenario = scenarios[currentScenarioIndex];
            const selectedPattern = patternTypeSelect.value;
            const selectedPrediction = pricePredictionSelect.value;

            if (!selectedPattern || !selectedPrediction) {
                alert("אנא בחר גם תבנית וגם חיזוי לפני השליחה.");
                return; // Prevent submission if options are not selected
            }

            const isPatternCorrect = selectedPattern === scenario.correct_pattern;
            const isPredictionCorrect = selectedPrediction === scenario.correct_prediction;

            outcomeDescription.innerHTML = scenario.outcome_description;
            patternExplanation.innerHTML = `<strong>הסבר על התבנית:</strong><br>${scenario.pattern_explanation}`;


            let feedbackHtml = `<strong>המשוב שלך:</strong><br>`;
            let feedbackClass = '';

            if (isPatternCorrect && isPredictionCorrect) {
                feedbackHtml += `✨ פגש בול! ✨ זיהית נכון את התבנית ("${scenario.pattern_options[scenario.correct_pattern]}") וחזית נכונה את מהלך המחיר הסביר (${selectedPrediction === 'up' ? 'עלייה 📈' : selectedPrediction === 'down' ? 'ירידה 📉' : 'דשדוש 📊'}). ניתוח מעולה!`;
                feedbackClass = 'correct';
            } else if (isPatternCorrect && !isPredictionCorrect) {
                feedbackHtml += `✅ זיהוי התבנית מדויק! ✅ זיהית נכון את התבנית ("${scenario.pattern_options[scenario.correct_pattern]}"), אך הפעם החיזוי שלך לגבי מהלך המחיר לא היה מדויק. זכור שזו הסתברות, לא ודאות.`;
                feedbackClass = 'partial';
            } else if (!isPatternCorrect && isPredictionCorrect) {
                 feedbackHtml += `🎯 החיזוי שלך פגע בול! 🎯 חזית נכון את מהלך המחיר (${selectedPrediction === 'up' ? 'עלייה 📈' : selectedPrediction === 'down' ? 'ירידה 📉' : 'דשדוש 📊'}), אך זיהוי התבנית היה פחות מדויק. התבנית הנכונה היא "${scenario.pattern_options[scenario.correct_pattern]}". חשוב לזהות את התבנית כדי להבין *למה* המחיר עשוי לזוז.`;
                feedbackClass = 'partial';
            }
            else {
                feedbackHtml += `🤔 עדיין לא מדויק הפעם... 🤔 זיהוי התבנית שלך ("${selectedPattern ? scenario.pattern_options[selectedPattern] || selectedPattern : 'לא נבחר'}) והחיזוי שלך לגבי מהלך המחיר לא היו מדויקים. התבנית הנכונה היא "${scenario.pattern_options[scenario.correct_pattern]}". בוא נראה את ההסבר כדי ללמוד.`;
                feedbackClass = 'incorrect';
            }

            feedbackText.innerHTML = feedbackHtml;

            // Show feedback area with animation
            feedbackArea.style.display = 'block';
            // Force reflow to allow transition
            void feedbackArea.offsetHeight;
            feedbackArea.className = `feedback-box ${feedbackClass}`;


            submitButton.style.display = 'none';
            submitButton.disabled = true; // Disable button after submission
            patternTypeSelect.disabled = true;
            pricePredictionSelect.disabled = true;

            navigationArea.style.display = 'flex'; // Show navigation buttons

            if (currentScenarioIndex < scenarios.length - 1) {
                nextScenarioButton.style.display = 'block';
                finishScenariosButton.style.display = 'none'; // Hide finish until last scenario
            } else {
                nextScenarioButton.style.display = 'none'; // Hide next button
                finishScenariosButton.style.display = 'block'; // Show finish button
            }
        }

        function finishScenarios() {
            chartArea.innerHTML = "<div class='app-subtitle' style='font-size: 1.2em; margin-bottom: 0;'>כל הכבוד! סיימת את האתגר בהצלחה! 🎉</div>";
            scenarioDescription.textContent = "";
             chartVisualHint.innerHTML = "";
            questionText.textContent = "";
            document.getElementById('user-input-area').style.display = 'none'; // Hide input area
            submitButton.style.display = 'none';
            nextScenarioButton.style.display = 'none';
            finishScenariosButton.style.display = 'none';
            navigationArea.style.display = 'none'; // Hide navigation buttons
            feedbackArea.style.display = 'none'; // Hide final feedback area
             scenarioCounter.style.display = 'none'; // Hide counter
             document.getElementById('header-area').style.marginBottom = '20px'; // Adjust header margin
        }

        function toggleExplanation() {
            const isHidden = explanationArea.classList.contains('hidden');
            if (isHidden) {
                explanationArea.classList.remove('hidden');
                // Add a slight delay before setting opacity to allow height transition
                 setTimeout(() => { explanationArea.style.opacity = 1; }, 10);
                toggleExplanationButton.textContent = 'הסתר הסבר מלא';
            } else {
                 explanationArea.style.opacity = 0;
                setTimeout(() => {
                    explanationArea.classList.add('hidden');
                    explanationArea.style.height = '0'; // Ensure height collapses after fade
                }, 400); // Match CSS transition duration
                toggleExplanationButton.textContent = 'הצג הסבר מלא על נרות וממוצעים נעים';
            }
        }

         function togglePredictionExplanation() {
             predictionExplanationDiv.classList.toggle('hidden');
              showPredictionExplanationButton.textContent = predictionExplanationDiv.classList.contains('hidden') ? 'הצג הסבר לחיזוי' : 'הסתר הסבר לחיזוי';
         }


        submitButton.addEventListener('click', submitPrediction);
        nextScenarioButton.addEventListener('click', () => {
            loadScenario(currentScenarioIndex + 1);
        });
        finishScenariosButton.addEventListener('click', finishScenarios);
        toggleExplanationButton.addEventListener('click', toggleExplanation);
        showPredictionExplanationButton.addEventListener('click', togglePredictionExplanation);

        // Initialize the first scenario
        loadScenario(0);
    });
</script>
```