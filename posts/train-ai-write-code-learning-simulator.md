---
title: "לאמן AI לכתוב קוד: סימולטור למידה אינטראקטיבי"
english_slug: train-ai-write-code-learning-simulator
category: "בינה מלאכותית"
tags:
  - בינה מלאכותית
  - למידת מכונה
  - אימון מודלים
  - כתיבת קוד
  - דאטה סיינס
  - חווית משתמש
---
# לאמן AI לכתוב קוד: סימולטור למידה אינטראקטיבי

איך מודל AI רוכש את הכוח לכתוב קוד? הצטרפו למסע אינטראקטיבי לתוך ליבת תהליך האימון, והבינו צעד אחר צעד איך מכונה לומדת ליצור תוכנה. האם זה קסם? לא בדיוק. זה תהליך מבוסס נתונים, פידבק, ואופטימיזציה אינסופית. בואו נצלול!

<div id="simulator">
    <h2>הסימולטור: אימון מודל AI לכתיבת קוד</h2>
    <p class="simulator-intro">הסימולטור מדמה תהליך אימון בסיסי ביותר. נציג למודל בעיה וקוד נכון, נראה את ניסיונו הכושל (בהתחלה!), ניתן לו פידבק, ונצפה בשיפור הביטחון שלו ויכולתו לפתור את הבעיה.</p>

    <div class="stage-container" id="problem-stage">
        <h3>🎯 המשימה הנוכחית:</h3>
        <div class="problem-description">
            <h4>תיאור הבעיה:</h4>
            <p id="problem-description-text"></p>
        </div>
         <button id="start-attempt-btn" class="action-button">בקש מה-AI לנסות לפתור</button>
    </div>

    <div class="stage-container" id="attempt-stage" style="display: none;">
         <h3>🤖 ניסיון ה-AI לפתור:</h3>
         <div class="ai-attempt-code">
             <h4>הקוד שיצר המודל:</h4>
             <pre><code id="ai-code"></code></pre>
             <div id="ai-code-overlay" class="code-overlay"></div> <!-- Overlay for animation -->
         </div>
         <button id="provide-feedback-btn" class="action-button">חשוף את הקוד הנכון (ספק פידבק)</button>
    </div>

    <div class="stage-container" id="feedback-stage" style="display: none;">
        <h3>💡 הפידבק: הקוד הנכון נחשף</h3>
        <div class="correct-code">
            <h4>הקוד הנכון למשימה:</h4>
            <pre><code id="correct-code"></code></pre>
            <div id="correct-code-overlay" class="code-overlay"></div> <!-- Overlay for animation -->
        </div>
        <p class="feedback-explanation">באימון אמיתי, פידבק מגיע דרך "פונקציית הפסד" שמחשבת כמה רחוק המודל מהפתרון הנכון. כאן, אנו מדמים זאת ע"י חשיפת הקוד הנכון, מה שמאפשר למודל (בסימולציה שלנו) "ללמוד" ולעדכן את ה"משקולות" הפנימיות שלו.</p>
        <button id="train-further-btn" class="action-button">אמן את המודל עם הפידבק הזה</button>
    </div>

     <div class="stage-container" id="internal-state-stage" style="display: none;">
        <h3>🧠 מצב פנימי של המודל:</h3>
        <p>ככל שהמודל נחשף ליותר דוגמאות ופידבק, כך גדל "הביטחון" (סימולציה של התאמת פרמטרים) שלו במשימה הספציפית.</p>
        <p>ביטחון המודל במשימה הנוכחית: <span id="ai-confidence"></span>%</p>
        <div class="confidence-bar-container">
            <div id="confidence-bar"></div>
        </div>
        <button id="next-step-btn" class="action-button"></button> <!-- Button text set by JS -->
     </div>

    <div id="simulator-message" class="simulator-message"></div>
</div>

<button id="toggle-explanation-btn" class="toggle-button">הצג הסבר מעמיק</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2>הסבר מעמיק: המסע של AI ללמידת קוד</h2>

    <h3>מבוא: משיק קוד פשוט לעוזר AI מתוחכם</h3>
    <p>בינה מלאכותית שמסייעת, משלימה ואף כותבת קוד נהייתה חלק משגרת יומם של מפתחים רבים. כלים כמו GitHub Copilot, המבוססים על מודלי שפה גדולים (LLMs) כמו GPT, משנים את הדרך שבה מפתחים עובדים. אבל איך בדיוק AI כזה רוכש את היכולת הזו? האם הוא פשוט 'מעתיק' קוד קיים, או עובר תהליך למידה עמוק יותר של תבניות והיגיון תכנותי? בואו נפרק את זה.</p>

    <h3>"הבנת" קוד ע"י LLMs: זיהוי תבניות סטטיסטיות</h3>
    <p>מודלי שפה גדולים לא באמת "מבינים" קוד כמו שבני אדם מבינים לוגיקה, אלגוריתמים או את הכוונה מאחורי הקוד. במקום זאת, הם מצטיינים בזיהוי תבניות מורכבות וקשרים סטטיסטיים בנתוני אימון עצומים. כשהם מאומנים על קורפוס של קוד, הם לומדים את המבנה התחבירי של שפות תכנות (איך פונקציה נראית בפייתון לעומת JavaScript), שמות משתנים נפוצים בהקשרים שונים, ספריות פופולריות ושימושיהן, וכיצד תיאור טקסטואלי של בעיה נוטה להתורגם למבני קוד מסוימים. היכולת שלהם היא לחזות בהסתברות גבוהה מה יהיה הטוקן (מילה, סימן, חלק ממילה/שם משתנה) הבא בקוד, בהינתן הקוד שקדם לו ותיאור הבעיה.</p>

    <h3>אבני היסוד של אימון מודלי קוד:</h3>
    <ul>
        <li><strong>נתוני אימון (Training Data): ה"ספרייה" העצומה של AI.</strong> כדי שמודל יוכל להפיק קוד שימושי, הוא חייב להיחשף לכמויות אדירות של דוגמאות קוד איכותיות, תיעוד, שאלות ותשובות, ומדריכים. מקורות כמו GitHub, Stack Overflow, תיעוד רשמי, ובלוגים טכניים מהווים את הבסיס ללמידה. ככל שהנתונים מגוונים ונקיים יותר, כך המודל יהיה מוכשר יותר.</li>
        <li><strong>ארכיטקטורת המודל: השלד הנוירוני.</strong> מודלים מודרניים לכתיבת קוד (כמו אלה במשפחת ה-GPT) מתבססים לרוב על ארכיטקטורת טרנספורמרים. ארכיטקטורות אלו מורכבות משכבות רבות של "נוירונים" ו"משקולות" (פרמטרים) - ערכים מספריים שמייצגים את הקשרים והידע שהמודל צבר. מודלים חזקים יכולים להכיל מיליארדים או טריליונים של פרמטרים כאלה. תהליך האימון הוא בעצם כוונון מדויק של ערכי המשקולות הללו.</li>
        <li><strong>פונקציית הפסד (Loss Function): מצפן הלמידה.</strong> זוהי נוסחה מתמטית המודדת כמה "רחוק" הקוד שהמודל יצר (הפלט שלו) מהקוד הנכון (ה"אמת" מנתוני האימון). פונקציית הפסד יכולה למדוד הבדלים ברמת התווים, הטוקנים, או אפילו לבדוק האם הקוד עובר בדיקות יחידה. מטרת תהליך האימון כולו היא למזער את ערך פונקציית הפסד.</li>
        <li><strong>אופטימיזציה: מנגנון התיקון העצמי.</strong> אלגוריתמים כמו Gradient Descent וגרסאותיו (אדם, אדאגרד וכו') הם הלב הפועם של הלמידה. הם מקבלים את ערך פונקציית הפסד, מחשבים כיצד כל אחד מהמיליארדים (או טריליונים) של הפרמטרים במודל תרם לשגיאה, ומחשבים כיצד לשנות אותם באופן מזערי (באמצעות "גרדיאנט") כדי שבאופקציה הבאה, הפלט יהיה מדויק יותר וההפסד יקטן.</li>
    </ul>

    <h3>איטרציות אימון (Epoches) ו-Fine-tuning</h3>
    <p>אימון מודל שפה גדול על קוד הוא תהליך ממושך שדורש חזרות רבות. הנתונים מחולקים למנות (batches), והמודל מתעדכן לאחר כל מנה. "אפוק" (Epoch) הוא מעבר אחד של המודל על כל מערך נתוני האימון. מודלים עוברים מאות או אלפי אפוקים כדי "להטמיע" את הידע בצורה עמוקה. לאחר שלב האימון המקדים (pre-training) על קורפוס כללי עצום, ניתן לבצע Fine-tuning - אימון נוסף וממוקד על נתונים רלוונטיים יותר למשימה ספציפית או לתחום דעת מסוים. זה מאפשר למודל להתחדד ולהיות יעיל יותר במשימות נישה מבלי הצורך לאמן אותו מאפס.</p>

    <h3>אתגרים בעולם האמיתי:</h3>
    <p>למרות ההתקדמות המדהימה, קיימים אתגרים משמעותיים: <strong>נכונות לוגית</strong> (קוד יכול להיות תקין תחבירית אך לא לפתור את הבעיה), <strong>יצירתיות וחדשנות</strong> (מודלים נוטים לייצר קוד שדומה לנתוני האימון ופחות טובים ביצירת אלגוריתמים חדשים לחלוטין), <strong>עדכניות ידע</strong> (המודל "קפא בזמן" במועד האימון ואינו יודע על ספריות חדשות או שינויים מאוחרים יותר), <strong>אבטחה והטיות</strong> (מודלים עלולים לשכפל דפוסי קוד לא מאובטחים או להכיל הטיות הקיימות בנתוני האימון).</p>

    <p class="conclusion">הסימולטור שראיתם הוא כמובן פישוט קיצוני של תהליך מורכב ועצום, אך הוא מדגים את העיקרון הבסיסי: AI לומד קוד דרך חשיפה לדוגמאות, ניסיון (שכולל טעויות), קבלת פידבק (שגיאות והשוואה לנכון), ועדכון פנימי של מודל הידע שלו כדי לשפר את הביצועים בניסיונות הבאים.</p>

</div>

<style>
    :root {
        --primary-color: #007bff;
        --primary-dark: #0056b3;
        --secondary-color: #28a745; /* Green */
        --secondary-dark: #218838;
        --background-color: #f8f9fa; /* Light grey background */
        --card-background: #ffffff; /* White cards */
        --border-color: #e9ecef; /* Light border */
        --text-color: #212529; /* Dark grey text */
        --code-background: #f4f4f4; /* Code block background */
        --code-border: #ced4da; /* Code block border */
        --simulator-message-bg: #fff3cd; /* light yellow */
        --simulator-message-border: #ffeeba;
        --simulator-message-text: #856404;
        --error-color: #dc3545;
    }

    body {
        font-family: 'Arial', sans-serif; /* More modern font */
        line-height: 1.7; /* Increased line height */
        margin: 0;
        padding: 30px; /* Increased padding */
        background-color: var(--background-color);
        color: var(--text-color);
        direction: rtl; /* Right-to-left */
        text-align: right; /* Right-align text */
        overflow-x: hidden; /* Prevent horizontal scroll */
    }

    h1, h2, h3, h4 {
        color: var(--primary-dark); /* Primary dark color for headings */
        text-align: right;
        margin-bottom: 15px;
    }
     h1 { font-size: 2.5em; margin-bottom: 20px; }
     h2 { font-size: 2em; border-bottom: 2px solid var(--border-color); padding-bottom: 10px; margin-bottom: 20px; }
     h3 { font-size: 1.5em; margin-bottom: 15px; color: var(--primary-color); }
     h4 { font-size: 1.2em; margin-bottom: 8px; color: #555; }

    p {
      text-align: right;
      margin-bottom: 15px;
    }
     .simulator-intro, .feedback-explanation {
         font-size: 1.1em;
         color: #555;
         margin-bottom: 25px;
     }

    #simulator, .explanation-section {
        background-color: var(--card-background);
        padding: 30px; /* Increased padding */
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Softer, larger shadow */
        margin-bottom: 30px; /* Increased margin */
        border: 1px solid var(--border-color);
    }

    .stage-container {
        margin-bottom: 30px; /* Increased spacing between stages */
        padding-bottom: 25px; /* Increased padding */
        border-bottom: 1px solid var(--border-color);
        opacity: 1; /* Default opacity */
        transition: opacity 0.5s ease-in-out; /* Fade transition */
    }
     .stage-container:last-child { border-bottom: none; padding-bottom: 0; }

    .problem-description, .ai-attempt-code, .correct-code {
        margin-bottom: 20px;
    }

    pre {
        background-color: var(--code-background);
        border-right: 4px solid var(--primary-color); /* Border on right for RTL */
        padding: 15px;
        overflow-x: auto;
        border-radius: 6px; /* Rounded corners for code blocks */
        font-family: 'Courier New', Courier, monospace;
        direction: ltr; /* Left-to-right for code */
        text-align: left; /* Left-align for code */
        white-space: pre-wrap; /* Wrap long lines */
        word-wrap: break-word;
        position: relative; /* Needed for overlay */
        min-height: 50px; /* Ensure block is visible even if empty */
    }

    code {
        font-family: 'Courier New', Courier', monospace;
        tab-size: 4; /* Improve code readability */
    }

    .code-overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: var(--code-background); /* Match background */
        opacity: 1;
        transition: opacity 0.5s ease-in-out; /* Fade out animation */
        pointer-events: none; /* Allow clicks on elements below */
    }
    .code-overlay.hidden {
        opacity: 0;
    }


    .action-button {
        display: inline-block;
        background-color: var(--primary-color);
        color: white;
        padding: 12px 25px; /* Larger padding */
        border: none;
        border-radius: 6px; /* More rounded */
        cursor: pointer;
        font-size: 1.1em; /* Larger font */
        margin-top: 15px;
        transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transitions */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .action-button:hover {
        background-color: var(--primary-dark);
        transform: translateY(-1px); /* Slight lift effect */
    }

    .action-button:active {
         transform: translateY(0); /* Press effect */
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .action-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        transform: none;
        box-shadow: none;
    }

     .toggle-button {
        display: block;
        margin: 30px auto; /* Center button, more margin */
        background-color: #6c757d; /* Grey color */
        color: white;
        padding: 12px 25px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
         transition: background-color 0.3s ease;
     }
     .toggle-button:hover {
         background-color: #545b62;
     }


    .confidence-bar-container {
        width: 100%;
        background-color: var(--border-color);
        border-radius: 5px;
        margin-top: 15px;
        height: 25px; /* Taller bar */
        overflow: hidden;
        direction: ltr; /* LTR for the bar itself */
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.2); /* Inner shadow */
    }

    #confidence-bar {
        height: 100%;
        width: 0%;
        background-color: var(--secondary-color); /* Green */
        border-radius: 5px;
        transition: width 0.8s ease-in-out, background-color 0.8s ease; /* Smoother, longer transition */
        display: flex; /* Use flex to center text if needed later */
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
     #confidence-bar.low { background-color: var(--error-color); } /* Red for low confidence */
     #confidence-bar.mid { background-color: #ffc107; } /* Yellow for mid confidence */
     #confidence-bar.high { background-color: var(--secondary-color); } /* Green for high confidence */


    .simulator-message {
      margin-top: 25px; /* More space */
      padding: 15px; /* More padding */
      background-color: var(--simulator-message-bg);
      border: 1px solid var(--simulator-message-border);
      border-radius: 8px; /* More rounded */
      color: var(--simulator-message-text);
      text-align: center;
      min-height: 20px; /* Reserve space even if empty */
      display: none; /* Initially hidden */
       opacity: 0;
       transition: opacity 0.5s ease-in-out;
    }
     .simulator-message.visible {
         display: block;
         opacity: 1;
     }

     ul {
         list-style: none; /* Remove default bullets */
         padding: 0;
         margin-bottom: 20px;
     }

     li {
         background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"><path fill="%23007bff" d="M9 16.2L4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4L9 16.2z"/></svg>') no-repeat right center; /* Custom SVG bullet */
         background-size: 16px;
         padding-right: 25px; /* Space for bullet */
         margin-bottom: 12px;
         line-height: 1.6;
     }
     li strong { color: var(--primary-dark); } /* Highlight key terms */

     .conclusion {
         font-style: italic;
         color: #555;
         margin-top: 30px;
         padding-top: 15px;
         border-top: 1px dashed var(--border-color);
     }

     /* Responsive adjustments */
     @media (max-width: 768px) {
         body { padding: 15px; }
         h1 { font-size: 2em; }
         h2 { font-size: 1.8em; }
         h3 { font-size: 1.3em; }
         .action-button, .toggle-button {
             padding: 10px 20px;
             font-size: 1em;
         }
         #simulator, .explanation-section {
             padding: 20px;
         }
         pre { padding: 10px; }
     }

</style>

<script>
    const trainingExamples = [
        {
            problem: "כתוב פונקציה בפייתון שמקבלת רשימת מספרים ומחזירה את סכומם.",
            correctCode: "def sum_list(numbers):\n    total = 0\n    for num in numbers:\n        total += num\n    return total"
        },
        {
            problem: "כתוב פונקציה בפייתון שמקבלת מחרוזת ומחזירה אותה כשהיא הפוכה.",
            correctCode: "def reverse_string(text):\n    return text[::-1]"
        },
        {
            problem: "כתוב פונקציה בפייתון שמקבלת מספר שלם ובודקת האם הוא זוגי.",
            correctCode: "def is_even(number):\n    return number % 2 == 0"
        },
         {
            problem: "כתוב פונקציה בפייתון שמקבלת רשימת מספרים ומחזירה את המספר הגדול ביותר.",
            correctCode: "def find_max(numbers):\n    if not numbers:\n        return None # Handle empty list\n    max_num = numbers[0]\n    for num in numbers:\n        if num > max_num:\n            max_num = num\n    return max_num"
        }
    ];

    let currentProblemIndex = 0;
    let aiConfidence = 0; // Start with 0 confidence on the new problem
    let currentAttemptCode = ""; // Store the last generated attempt

    // DOM elements
    const problemStageEl = document.getElementById('problem-stage');
    const attemptStageEl = document.getElementById('attempt-stage');
    const feedbackStageEl = document.getElementById('feedback-stage');
    const internalStateStageEl = document.getElementById('internal-state-stage');

    const problemDescriptionEl = document.getElementById('problem-description-text');
    const correctCodeEl = document.getElementById('correct-code');
    const aiCodeEl = document.getElementById('ai-code');
    const aiConfidenceEl = document.getElementById('ai-confidence');
    const confidenceBarEl = document.getElementById('confidence-bar');

    const startAttemptBtn = document.getElementById('start-attempt-btn');
    const provideFeedbackBtn = document.getElementById('provide-feedback-btn');
    const trainFurtherBtn = document.getElementById('train-further-btn');
    const nextStepBtn = document.getElementById('next-step-btn'); // Unified button for internal state stage

    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationBtn = document.getElementById('toggle-explanation-btn');
    const simulatorMessageEl = document.getElementById('simulator-message');

     const aiCodeOverlayEl = document.getElementById('ai-code-overlay');
     const correctCodeOverlayEl = document.getElementById('correct-code-overlay');


    // --- Helper functions ---

    function simulateAiAttempt(problem, correctCode, confidence) {
        const problemId = trainingExamples.findIndex(ex => ex.correctCode === correctCode); // Use correctCode to find problem index
        let generatedCode = "";

        // Simulate progression based on confidence
        if (confidence < 10) {
            // Very low confidence: Mostly gibberish or completely wrong structure/language
            if (problemId === 0) generatedCode = "func sum(array): val = 0; for i in array do val += i; end func"; // Wrong syntax, wrong language feel
            else if (problemId === 1) generatedCode = "string reverse(str) { return str.reversed; }"; // Wrong syntax, wrong language feel
            else if (problemId === 2) generatedCode = "check_even(num) := num % 3 == 1 ? True : False;"; // Wrong syntax, wrong logic
             else generatedCode = "start program\n  print 'hello world'\nend"; // Generic irrelevant code
        } else if (confidence < 30) {
            // Low confidence: Some keywords might be right, but structure/logic is broken
             if (problemId === 0) generatedCode = "def sum_list(numbers):\n    total = 1 # Initial error\n    for number in numbers:\n        total = total * number # Logic error\n    # Missing return";
             else if (problemId === 1) generatedCode = "def reverse_string(text):\n    reversed = ''\n    for char in text:\n        reversed = reversed + char # Appending instead of prepending\n    return reversed"; // Returns original string
             else if (problemId === 2) generatedCode = "def is_even(number):\n    if number / 2 == 0: # Logic error\n        return True\n    else:\n        return False";
             else generatedCode = "def find_max(list):\n  biggest = 0 # Assumes positive numbers\n  for item in list:\n    if item > biggest:\n      item = biggest # Assignment reversed\n  return biggest";
        } else if (confidence < 60) {
            // Mid confidence: Structure looks similar, but logic or syntax errors are common
             if (problemId === 0) generatedCode = "def sum_list(numbers):\n    total = 0\n    for num in numbers:\n        total += numbers # Wrong variable\n    return total";
             else if (problemId === 1) generatedCode = "def reverse_string(text):\n    return text[1::]"; // Incorrect slicing
             else if (problemId === 2) generatedCode = "def is_even(number):\n    if number % 2 == 0:\n        print(True) # Unnecessary side effect\n    else:\n        return False";
             else generatedCode = "def find_max(numbers):\n  max_val = numbers[0]\n  for n in numbers:\n    if n > max_val:\n      max_val = n\n  # Missing return max_val";
        } else if (confidence < 90) {
            // High confidence: Very close, potential for minor errors, style issues, or missing edge cases
             if (problemId === 0) generatedCode = "def calculate_sum(nums):\n    total = 0\n    for x in nums:\n        total += x\n    return total"; // Correct but different variable names
             else if (problemId === 1) generatedCode = "def reverse_string(s):\n    return s[::-1]\n# done"; // Correct but extra comment/line
             if (problemId === 2) generatedCode = "def check_if_even(number):\n    return number % 2 == 0"; // Correct but different function name
             else generatedCode = "def get_max(list_of_numbers):\n  # Assume non-empty list\n  current_max = list_of_numbers[0]\n  for number in list_of_numbers:\n    if number > current_max:\n      current_max = number\n  return current_max"; // Correct, adds a comment about assumption
        } else { // confidence >= 90 - Simulating near perfection or perfection
            generatedCode = correctCode; // Model gets it right
        }
        return generatedCode;
    }

     function updateConfidenceBar() {
         const roundedConfidence = Math.round(aiConfidence);
         aiConfidenceEl.textContent = roundedConfidence;
         confidenceBarEl.style.width = aiConfidence + '%';

         confidenceBarEl.classList.remove('low', 'mid', 'high');
         if (roundedConfidence < 40) {
             confidenceBarEl.classList.add('low');
         } else if (roundedConfidence < 80) {
              confidenceBarEl.classList.add('mid');
         } else {
              confidenceBarEl.classList.add('high');
         }
         // Optional: Add text inside the bar for better visualization if needed
         // confidenceBarEl.textContent = roundedConfidence > 15 ? roundedConfidence + '%' : '';
     }

     function showStage(stageId) {
         const stages = [problemStageEl, attemptStageEl, feedbackStageEl, internalStateStageEl];
         stages.forEach(stage => {
             if (stage.id === stageId) {
                 stage.style.display = 'block';
                 requestAnimationFrame(() => { // Use rAF to ensure display is set before transition
                     stage.style.opacity = 1;
                 });
             } else {
                 stage.style.opacity = 0;
                 // Use a timeout to hide the stage after the transition ends
                 setTimeout(() => { stage.style.display = 'none'; }, 500); // Match transition duration
             }
         });
     }

    function updateDisplay() {
        const currentExample = trainingExamples[currentProblemIndex];
        problemDescriptionEl.textContent = currentExample.problem;
        correctCodeEl.textContent = currentExample.correctCode;

        updateConfidenceBar();

         // Reset code overlays
         aiCodeOverlayEl.classList.remove('hidden');
         correctCodeOverlayEl.classList.remove('hidden');

         // Manage button/stage visibility and text
         if (aiConfidence === 0) {
             // Initial state for a new problem
             showStage('problem-stage');
             startAttemptBtn.style.display = 'block';
             provideFeedbackBtn.style.display = 'none';
             trainFurtherBtn.style.display = 'none';
             internalStateStageEl.style.display = 'none'; // Hide internal state initially
             simulatorMessageEl.classList.remove('visible');
             aiCodeEl.textContent = ''; // Clear previous code
             correctCodeEl.textContent = currentExample.correctCode; // Set correct code but keep feedback stage hidden
         } else if (aiConfidence < 90 && currentAttemptCode !== '' && !provideFeedbackBtn.disabled) {
              // AI made an attempt, needs feedback
             showStage('attempt-stage');
             aiCodeEl.textContent = currentAttemptCode;
             provideFeedbackBtn.style.display = 'block';
             startAttemptBtn.style.display = 'none';
             trainFurtherBtn.style.display = 'none';
             internalStateStageEl.style.display = 'none';
              requestAnimationFrame(() => aiCodeOverlayEl.classList.add('hidden')); // Fade in AI code
         } else if (aiConfidence < 90 && provideFeedbackBtn.disabled && currentAttemptCode !== '') {
             // Feedback was provided, ready to train further
             showStage('feedback-stage'); // Show feedback stage with correct code
              correctCodeEl.textContent = currentExample.correctCode;
              aiCodeEl.textContent = currentAttemptCode; // Keep showing AI attempt
              provideFeedbackBtn.style.display = 'none';
             startAttemptBtn.style.display = 'none';
             trainFurtherBtn.style.display = 'block';
             internalStateStageEl.style.display = 'block'; // Show confidence update
              requestAnimationFrame(() => {
                   aiCodeOverlayEl.classList.add('hidden'); // AI code shown
                   correctCodeOverlayEl.classList.add('hidden'); // Correct code shown
              });
             nextStepBtn.style.display = 'none'; // Hide next step button initially

         } else if (aiConfidence >= 90 && currentProblemIndex < trainingExamples.length - 1) {
             // Problem solved, move to next
             showStage('internal-state-stage'); // Show final state for this problem
              aiCodeEl.textContent = currentAttemptCode;
              correctCodeEl.textContent = currentExample.correctCode;
              provideFeedbackBtn.style.display = 'none';
              startAttemptBtn.style.display = 'none';
              trainFurtherBtn.style.display = 'none';
              requestAnimationFrame(() => {
                   aiCodeOverlayEl.classList.add('hidden');
                   correctCodeOverlayEl.classList.add('hidden');
              });
              nextStepBtn.style.display = 'block';
              nextStepBtn.textContent = "עבור למשימה הבאה";
              simulatorMessageEl.textContent = `🎉 המודל רכש ביטחון גבוה במשימה ${currentProblemIndex + 1}! מוכן למשימה הבאה.`;
              simulatorMessageEl.classList.add('visible');

         } else if (aiConfidence >= 90 && currentProblemIndex === trainingExamples.length - 1) {
              // All problems solved
              showStage('internal-state-stage'); // Show final state
              aiCodeEl.textContent = currentAttemptCode;
              correctCodeEl.textContent = currentExample.correctCode;
              provideFeedbackBtn.style.display = 'none';
              startAttemptBtn.style.display = 'none';
              trainFurtherBtn.style.display = 'none';
               requestAnimationFrame(() => {
                   aiCodeOverlayEl.classList.add('hidden');
                   correctCodeOverlayEl.classList.add('hidden');
              });
              nextStepBtn.style.display = 'none'; // No more problems
              simulatorMessageEl.textContent = "🏆 כל הכבוד! המודל סיים בהצלחה את כל דוגמאות האימון בסימולטור.";
              simulatorMessageEl.classList.add('visible');
         } else {
             // Fallback/Intermediate state, should not happen often with correct flow
             console.warn("Simulator in unexpected state. Confidence:", aiConfidence, "Problem:", currentProblemIndex);
              showStage('problem-stage'); // Go back to problem stage as a safe fallback
               startAttemptBtn.style.display = 'block';
               provideFeedbackBtn.style.display = 'none';
               trainFurtherBtn.style.display = 'none';
               internalStateStageEl.style.display = 'none';
               simulatorMessageEl.classList.remove('visible');
         }
    }

     function handleStartAttempt() {
         const currentExample = trainingExamples[currentProblemIndex];
         currentAttemptCode = simulateAiAttempt(currentExample.problem, currentExample.correctCode, aiConfidence);
         provideFeedbackBtn.disabled = false; // Enable feedback button
          simulatorMessageEl.textContent = "יוצר ניסיון ראשון לפתרון...";
          simulatorMessageEl.classList.add('visible');
         updateDisplay();
     }

    function handleFeedback() {
        // Simulate increasing confidence after feedback
        aiConfidence = Math.min(100, aiConfidence + (aiConfidence < 50 ? 30 : (aiConfidence < 80 ? 20 : 10))); // Increase more at lower confidence
        provideFeedbackBtn.disabled = true; // Disable feedback until next attempt
        simulatorMessageEl.textContent = "קיבלתי את הקוד הנכון. מעדכן את המודל ומחזק את הקשרים הנכונים...";
        simulatorMessageEl.classList.add('visible');
        updateDisplay();
    }

    function handleTrainFurther() {
         const currentExample = trainingExamples[currentProblemIndex];
         if (aiConfidence >= 90) { // Check again if somehow reached 90+ before button text change
             // This path should ideally be handled by nextStepBtn
             handleNextStep();
             return;
         }

        // Simulate generating a new attempt with increased confidence
        currentAttemptCode = simulateAiAttempt(currentExample.problem, currentExample.correctCode, aiConfidence);
        provideFeedbackBtn.disabled = false; // Enable feedback for the new attempt
         simulatorMessageEl.textContent = "מנסה לפתור את המשימה שוב עם הידע החדש...";
         simulatorMessageEl.classList.add('visible');
        updateDisplay();
    }

     function handleNextStep() {
         currentProblemIndex++;
         if (currentProblemIndex < trainingExamples.length) {
             aiConfidence = 0; // Reset confidence for the new problem
             currentAttemptCode = ""; // Clear previous attempt
             simulatorMessageEl.classList.remove('visible'); // Hide message temporarily
             updateDisplay(); // Move to the problem stage of the next problem
             simulatorMessageEl.textContent = `מתחיל אימון על משימה חדשה (${currentProblemIndex + 1}/${trainingExamples.length})...`;
             simulatorMessageEl.classList.add('visible');
         } else {
             // Finished all problems - updateDisplay already handles the final state
             updateDisplay();
         }
     }


    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
         // Use rAF for transition
         requestAnimationFrame(() => {
             explanationDiv.style.opacity = isHidden ? 1 : 0;
             // Hide fully after transition if hiding
             if (!isHidden) {
                  setTimeout(() => { explanationDiv.style.display = 'none'; }, 500);
             }
         });

        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'הצג הסבר מעמיק';
    }

    // --- Initialization ---

    document.addEventListener('DOMContentLoaded', () => {
        updateDisplay(); // Initial display (shows problem stage)
        startAttemptBtn.addEventListener('click', handleStartAttempt);
        provideFeedbackBtn.addEventListener('click', handleFeedback);
        trainFurtherBtn.addEventListener('click', handleTrainFurther);
        nextStepBtn.addEventListener('click', handleNextStep);
        toggleExplanationBtn.addEventListener('click', toggleExplanation);

        // Ensure initial state opacity is correct for the problem stage
        problemStageEl.style.opacity = 1;
         attemptStageEl.style.opacity = 0;
         feedbackStageEl.style.opacity = 0;
         internalStateStageEl.style.opacity = 0;

         // Add overlay fade-out animation listener once
         aiCodeOverlayEl.addEventListener('transitionend', function() {
             if(aiCodeOverlayEl.classList.contains('hidden')) {
                  // console.log('AI Overlay hidden');
             }
         });
          correctCodeOverlayEl.addEventListener('transitionend', function() {
             if(correctCodeOverlayEl.classList.contains('hidden')) {
                  // console.log('Correct Overlay hidden');
             }
         });
    });

</script>