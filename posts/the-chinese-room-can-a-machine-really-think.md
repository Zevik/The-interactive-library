---
title: "החדר הסיני: האם מכונה יכולה באמת לחשוב?"
english_slug: the-chinese-room-can-a-machine-really-think
category: "פילוסופיה"
tags: [פילוסופיה, בינה מלאכותית, סרל, החדר הסיני, תודעה, קוגניציה]
---
<div class="chinese-room-app">
    <h1>החדר הסיני: המשחק</h1>

    <div class="game-intro">
        <p>דמיינו שאתם בחדר סגור ומקבלים פתקים עם סימנים מוזרים שלא הבנתם מעולם. לרשותכם יש "ספר חוקים" שמסביר איך להגיב לסימנים הנכנסים. אם תפעלו לפי הספר, האם מי שמחוץ לחדר - שמבין את הסימנים - יחשוב שגם אתם מבינים אותם?</p>
        <p>נסו זאת בעצמכם! אתם האדם בחדר. השתמשו ב"ספר החוקים" כדי ליצור את הפלט המתאים לפתק הקלט. גררו את הסימנים הנכונים ממאגר הסמלים אל "פתק הפלט".</p>
    </div>

    <div class="game-container">
        <div class="notes-and-rules">
             <div class="note input-note">
                <h3>פתק קלט</h3>
                <div id="input-symbols" class="symbols-container">
                    <!-- Input symbols will be populated by JS -->
                </div>
            </div>

             <div class="rule-book">
                <h3>ספר החוקים</h3>
                <ul id="rules-list">
                    <!-- Rules will be populated by JS -->
                </ul>
            </div>

            <div class="note output-note dropzone" id="output-note">
                <h3>פתק פלט (גררו לכאן)</h3>
                <div id="output-symbols" class="symbols-container">
                    <!-- Dropped symbols will appear here -->
                </div>
                <p class="drop-hint">גררו לכאן את הסימנים המתאימים</p>
            </div>
        </div>

        <div class="actions-area">
            <div id="available-output-symbols" class="symbols-pool">
                <h4>מאגר סמלים לפלט:</h4>
                <div class="symbols-container">
                    <!-- Draggable symbols will be populated by JS -->
                </div>
            </div>
            <div class="game-controls">
                <button id="submit-button">בדוק פלט</button>
                <button id="next-round-button" disabled>סבב הבא</button>
            </div>
        </div>
    </div>

    <div id="evaluation-area" class="evaluation-area">
        <h3>הערכה מבחוץ:</h3>
        <p id="external-evaluation"></p>
         <div class="round-info">
            סבב <span id="current-round">1</span> מתוך <span id="total-rounds">?</span>
        </div>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">הצג הסבר על החדר הסיני</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2>הסבר: ניסוי המחשבה "החדר הסיני" של ג'ון סרל</h2>

    <h3>מהו ניסוי המחשבה "החדר הסיני"?</h3>
    <p>הניסוי הוצע על ידי הפילוסוף ג'ון סרל ב-1980 במטרה להפריך את הטענה שבינה מלאכותית "חזקה" (Strong AI) מסוגלת באמת להבין או לחשוב, באותו מובן שבו בני אדם חושבים ומבינים.</p>
    <p>הניסוי מתאר אדם שאינו דובר סינית הנמצא בחדר סגור. הוא מקבל סדרה של סימנים סיניים דרך פתח אחד, ויש לו ספר חוקים (בדומה לתוכנת מחשב) שמכיל הוראות כיצד לשבץ סימנים סיניים מסוימים בתגובה לסימנים נכנסים. ההוראות הן טהורות סינטקטיות - הן מתייחסות רק לצורת הסימנים ולכללי מניפולציה שלהם, ללא קשר למשמעותם.</p>
    <p>האדם בחדר פשוט עוקב אחר ההוראות, ופולט סדרה של סימנים סיניים דרך פתח אחר. מי שמחוץ לחדר ודובר סינית רואה את הסימנים הנכנסים (שאלות בסינית) ואת הסימנים היוצאים (תשובות בסינית), ומתרשם שהמערכת (האדם והספר ביחד) דוברת סינית בצורה שוטפת ועונה תשובות הגיוניות.</p>

    <h3>מטרת הניסוי: הפרדה בין תחביר (סינטקס) למשמעות (סמנטיקה)</h3>
    <p>סרל טוען שהאדם בחדר, למרות שהוא פועל כמו מחשב (מניפולציה של סמלים לפי חוקים), אינו מבין למעשה את הסינית. הוא רק מבצע מניפולציות תחביריות על הסמלים. לעומת זאת, דובר סינית אמיתי לא רק מזהה את הסמלים ופועל לפי חוקי הדקדוק, אלא גם מבין את המשמעות (הסמנטיקה) של המילים והמשפטים.</p>
    <p>מטרת הניסוי היא להראות שחיקוי חיצוני של הבנה או חשיבה (מעבר מבחן טיורינג, למשל) אינו מוכיח קיום של הבנה או חשיבה פנימית אמיתית. מערכת סינטקטית בלבד אינה מספיקה ליצירת סמנטיקה.</p>

    <h3>הטיעון של סרל: מניפולציה של סמלים לפי חוקים אינה שקולה להבנה</h3>
    <p>הטיעון המרכזי של סרל הוא שמחשבים פועלים בצורה סינטקטית בלבד. הם מעבדים סמלים (ביטים, תוויות) לפי חוקים אלגוריתמיים. אין להם גישה למשמעות של הסמלים הללו. הוא מדמה זאת לאדם בחדר הסיני – המחשב הוא האדם, תוכנת הבינה המלאכותית היא ספר החוקים, והסמלים הם הסימנים הסיניים. המחשב, כמו האדם בחדר, יכול לתת תגובות מתאימות לקלט, אך אינו מבין מה הוא עושה.</p>

    <h3>ביקורת על "בינה מלאכותית חזקה" (Strong AI)</h3>
    <p>סרל מבחין בין "בינה מלאכותית חזקה" (Strong AI) ל"בינה מלאכותית חלשה" (Weak AI).
    "Weak AI" היא הטענה שמחשבים הם כלי רב עוצמה לחקר הנפש ולבניית מודלים שלה, ושניתן לחקות היבטים מסוימים של חשיבה אנושית. עם זה סרל מסכים.
    "Strong AI" היא הטענה שמחשב המריץ תוכנה מתאימה הוא *בעצמו* בעל נפש, תודעה או הבנה, ושפשוט על ידי הרצת התוכנה נוצרת חשיבה ממשית. את הטענה הזו סרל דוחה מכל וכל באמצעות ניסוי החדר הסיני.</p>

    <h3>התנגדויות נפוצות לניסוי</h3>
    <p>הניסוי עורר ויכוחים רבים והוצגו לו התנגדויות שונות:</p>
    <ul>
        <li><strong>טיעון המערכת (The Systems Reply):</strong> הטענה היא שבעוד שהאדם בחדר לבדו אינו מבין סינית, ה*מערכת* כולה (האדם, ספר החוקים, פתקי הקלט/פלט וכו') כן מבינה סינית. סרל משיב שגם אם האדם יזכור את כל החוקים ויתנהל מחוץ לחדר, הוא עדיין רק יבצע מניפולציה סינטקטית ללא הבנה.</li>
        <li><strong>טיעון הרובוט (The Robot Reply):</strong> הטענה היא שבינה מלאכותית תזדקק לגוף ותחושות כדי לרכוש משמעות. רובוט עם חיישנים ומנועים שיקיים אינטראקציה עם העולם יוכל לפתח הבנה. סרל משיב שגם הרובוט יכול להידמות לחדר הסיני, רק מורכב יותר - הסימנים יכולים לייצג קלט מחיישנים ופלט למנועים, והאדם עדיין רק מבצע מניפולציות על סימנים חסרי משמעות עבורו.</li>
        <li><strong>טיעון המוח (The Brain Simulator Reply):</strong> אם ניתן ליצור תוכנה שתחקה בדיוק את פעולת הנוירונים במוח של דובר סינית, האם מערכת כזו לא תבין סינית? סרל עונה שגם כאן, האדם בחדר יכול לדמות את פעולת הנוירונים באמצעות כללים מורכבים, אך עדיין לא תהיה לו הבנה.</li>
        <li>התנגדויות נוספות עוסקות ביעילות הניסוי המחשבתי, בהגדרה של "הבנה", ועוד.</li>
    </ul>

    <h3>השלכות הניסוי על הפילוסופיה של הנפש וחקר הבינה המלאכותית</h3>
    <p>הניסוי הדגיש את הפער בין סינטקס לסמנטיקה והעלה שאלות יסודיות לגבי טבעה של החשיבה והתודעה. הוא השפיע רבות על הדיון הפילוסופי אודות ה"בעיה הקשה" של התודעה (כיצד חוויה סובייקטיבית נובעת מפעילות פיזית) ועל הגישות בחקר הבינה המלאכותית. בעוד שבינה מלאכותית מתקדמת ממשיכה להפגין יכולות מרשימות יותר ויותר, השאלה האם היא באמת "מבינה" או "חושבת" נותרת פתוחה, בחלקה בזכות האתגר שהציב ניסוי החדר הסיני.</p>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;700&display=swap');

    :root {
        --primary-color: #1a535c; /* Deep Teal */
        --secondary-color: #4ecdc4; /* Light Teal */
        --accent-color: #ff6b6b; /* Coral Red */
        --background-color: #f7fff7; /* Light Greenish-White */
        --surface-color: #ffffff; /* White */
        --text-color: #333; /* Dark Grey */
        --rule-bg: #eef; /* Light Blue */
        --note-bg: #fffacd; /* Lemon Chiffon - Paper */
        --symbol-bg: #8d99ae; /* Cool Grey */
        --symbol-text: #fff;
        --dropzone-border: #a0a0a0; /* Grey */
        --dropzone-bg: #eee; /* Light Grey */
        --correct-color: #4CAF50; /* Green */
        --incorrect-color: #f44336; /* Red */
    }

    body {
        font-family: 'Rubik', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-color);
        margin: 0;
        padding: 20px;
        direction: rtl; /* Ensure RTL direction */
        text-align: right;
    }

    h1, h2, h3, h4 {
        color: var(--primary-color);
        margin-bottom: 15px;
    }

     h1 {
        text-align: center;
        color: var(--primary-color);
        margin-bottom: 30px;
     }

     .chinese-room-app {
        max-width: 1000px;
        margin: 20px auto;
        padding: 30px;
        background-color: var(--surface-color);
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        border: 1px solid #ddd;
    }

    .game-intro {
        margin-bottom: 30px;
        padding-bottom: 20px;
        border-bottom: 1px solid #eee;
    }

    .game-container {
        display: flex;
        gap: 30px;
        margin-bottom: 20px;
        flex-wrap: wrap;
    }

    .notes-and-rules {
        flex: 3; /* More space for notes and rules */
        min-width: 400px;
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    .rule-book {
        flex: 1;
        min-width: 250px;
        background-color: var(--rule-bg);
        border: 1px solid #cdd;
        border-radius: 8px;
        padding: 20px;
        overflow-y: auto;
        max-height: 350px; /* Adjusted height */
        box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.05);
    }

    .rule-book h3 {
        margin-top: 0;
        color: var(--primary-color);
        border-bottom: 2px solid var(--secondary-color);
        padding-bottom: 10px;
    }

    #rules-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    #rules-list li {
        background-color: var(--surface-color);
        margin-bottom: 10px;
        padding: 12px;
        border-radius: 6px;
        font-size: 0.95em;
        border: 1px solid #ddd;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    #rules-list li:hover {
         transform: translateY(-2px);
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }

    .note {
        background-color: var(--note-bg);
        border: 1px solid #d4c065; /* Darker yellow border */
        border-radius: 8px;
        padding: 20px;
        min-height: 100px;
        box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.1);
        position: relative; /* For absolute positioning of hint */
    }

    .note h3 {
        margin-top: 0;
        color: #8a7b32; /* Darker yellow color */
        border-bottom: 1px dashed #d4c065;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }

    .symbols-container {
        display: flex;
        flex-wrap: wrap;
        gap: 8px; /* Smaller gap for symbols */
        min-height: 40px;
        align-items: center;
    }

    .symbol {
        display: inline-block;
        padding: 10px 14px; /* Slightly larger padding */
        background-color: var(--symbol-bg);
        color: var(--symbol-text);
        border-radius: 6px; /* More rounded */
        font-size: 1.3em; /* Slightly larger text */
        font-weight: 500; /* Medium font-weight */
        cursor: grab;
        box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s ease, box-shadow 0.2s ease, opacity 0.2s ease;
        user-select: none; /* Prevent text selection */
    }

     .symbol:active {
         cursor: grabbing;
     }

    .symbol.dragging {
        opacity: 0.6;
        transform: scale(1.05);
        box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.3);
    }

    .symbol.draggable {
        background-color: var(--secondary-color); /* Distinct color for draggable */
         color: var(--primary-color);
         font-weight: 700;
         cursor: grab;
    }

    .symbol.draggable:hover {
         transform: translateY(-2px);
         box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.2);
    }

    .output-note .symbol {
         background-color: var(--symbol-bg); /* Grey when dropped */
         color: var(--symbol-text);
         cursor: pointer; /* Cursor indicates it can be removed */
    }

     .output-note .symbol:hover {
         background-color: #7d889e; /* Slightly darker on hover */
     }


    .dropzone {
        border: 2px dashed var(--dropzone-border);
        min-height: 80px; /* Ensure adequate drop area */
        background-color: var(--dropzone-bg);
        display: flex; /* Use flex for dropped symbols */
        flex-wrap: wrap;
        gap: 8px;
        align-content: flex-start; /* Align dropped items to the start */
        position: relative;
    }

    .dropzone.dragover {
        border-color: var(--primary-color);
        background-color: #e0e7e9; /* Lighter secondary */
    }

    .drop-hint {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: #aaa;
        font-size: 1.1em;
        pointer-events: none; /* Don't interfere with drag/drop */
         text-align: center;
    }

     .dropzone .symbol {
         z-index: 1; /* Ensure symbols are above hint */
     }

    .dropzone:not(:empty) .drop-hint {
        display: none; /* Hide hint when symbols are present */
    }


    .actions-area {
        flex: 1;
        min-width: 250px;
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    .symbols-pool {
        background-color: var(--surface-color);
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }

    .symbols-pool h4 {
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 1.1em;
        color: var(--primary-color);
         border-bottom: 1px solid #eee;
         padding-bottom: 8px;
    }

    .symbols-pool .symbols-container {
        gap: 6px; /* Tighter packing in pool */
    }

    .game-controls {
         display: flex;
         flex-direction: column;
         gap: 10px;
    }

    button {
        padding: 12px 20px; /* Larger buttons */
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: var(--primary-color);
        color: white;
        transition: background-color 0.3s ease, opacity 0.3s ease;
        font-weight: 500;
        width: 100%; /* Full width buttons */
        text-align: center;
    }

    button:hover:not(:disabled) {
        background-color: #153f46; /* Darker shade */
    }

    button:disabled {
        background-color: #ccc;
        cursor: not-allowed;
        opacity: 0.7;
    }

    #next-round-button {
        background-color: var(--secondary-color);
        color: var(--primary-color);
    }
     #next-round-button:hover:not(:disabled) {
        background-color: #3aa9a0; /* Darker shade */
    }

     #toggle-explanation {
        display: block;
        margin: 40px auto 20px auto;
        background-color: #6c757d;
        width: auto; /* Auto width for display block */
        max-width: 300px; /* Limit max width */
     }

    #toggle-explanation:hover:not(:disabled) {
        background-color: #5a6268;
    }


    .evaluation-area {
        margin-top: 30px;
        padding: 20px;
        border-top: 2px solid var(--secondary-color);
        background-color: #e9f2f3; /* Light background */
        border-radius: 8px;
        box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.05);
         min-height: 60px; /* Ensure it has height even if empty */
    }

    .evaluation-area h3 {
        margin-top: 0;
        color: var(--primary-color);
         margin-bottom: 10px;
    }

    .evaluation-area p {
        margin-bottom: 10px;
        font-size: 1.15em;
        font-weight: 500;
    }

     .evaluation-area.correct {
         background-color: #e8f5e9; /* Very light green */
         border-color: var(--correct-color);
         color: var(--correct-color);
     }

     .evaluation-area.correct h3 {
         color: var(--correct-color);
     }

      .evaluation-area.incorrect {
         background-color: #ffebee; /* Very light red */
         border-color: var(--incorrect-color);
         color: var(--incorrect-color);
     }

       .evaluation-area.incorrect h3 {
         color: var(--incorrect-color);
     }


    .round-info {
        text-align: left; /* Align to the left in RTL */
        font-size: 0.9em;
        color: #555;
        margin-top: 15px;
        padding-top: 10px;
        border-top: 1px dashed #ccc;
    }

    .explanation-section {
        margin-top: 30px;
        padding: 30px;
        border: 1px solid #ccc;
        border-radius: 12px;
        background-color: var(--surface-color);
        line-height: 1.7;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
    }

    .explanation-section h2, .explanation-section h3 {
        color: var(--primary-color);
        margin-bottom: 15px;
        border-bottom: 1px solid #eee;
        padding-bottom: 8px;
    }

    .explanation-section p, .explanation-section ul {
        margin-bottom: 20px;
    }

    .explanation-section ul {
        padding-left: 25px; /* Adjust padding for RTL if needed, standard works */
    }

    .explanation-section li {
        margin-bottom: 10px;
    }

    /* Animations */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }

    .evaluation-area.correct p, .evaluation-area.incorrect p {
        animation: pulse 0.5s ease-in-out;
    }


    /* Responsive adjustments */
    @media (max-width: 768px) {
        .game-container {
            flex-direction: column;
            gap: 20px;
        }
        .notes-and-rules, .rule-book, .actions-area {
            min-width: unset;
            width: 100%;
            flex: none; /* Remove flex grow */
        }
         .game-controls {
             flex-direction: row; /* Buttons side-by-side on small screens */
             gap: 10px;
         }
          .game-controls button {
             width: auto;
             flex-grow: 1;
          }

          .rule-book {
              max-height: 250px; /* Reduce max height on smaller screens */
          }
    }

    @media (max-width: 480px) {
        .chinese-room-app, .explanation-section {
            padding: 20px;
        }
        .game-controls {
            flex-direction: column;
        }
         .game-controls button {
             width: 100%;
         }
         .symbol {
             padding: 8px 10px;
             font-size: 1.1em;
         }
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const inputSymbolsDiv = document.getElementById('input-symbols');
        const outputSymbolsDiv = document.getElementById('output-symbols'); // Changed from outputNoteDiv for clarity
        const ruleListUl = document.getElementById('rules-list');
        const availableOutputSymbolsContainer = document.querySelector('#available-output-symbols .symbols-container'); // Select container *inside* pool
        const submitButton = document.getElementById('submit-button');
        const nextRoundButton = document.getElementById('next-round-button');
        const externalEvaluationArea = document.getElementById('evaluation-area'); // Use the container
        const externalEvaluationP = document.getElementById('external-evaluation');
        const currentRoundSpan = document.getElementById('current-round');
        const totalRoundsSpan = document.getElementById('total-rounds');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationSection = document.getElementById('explanation');
        const outputNoteDropzone = document.getElementById('output-note'); // The dropzone element itself


        const rules = [
            { id: 1, input: ['Ψ', 'Ω'], output: ['Δ', 'Γ'], meaning: "שלום" }, // Added Hebrew meaning for context
            { id: 2, input: ['Θ', 'Λ', 'Ψ'], output: ['Σ', 'Φ'], meaning: "להתראות" },
            { id: 3, input: ['Δ', 'Θ', 'Γ'], output: ['Ω', 'Λ', 'Φ'], meaning: "מה שלומך?" },
            { id: 4, input: ['Λ', 'Φ', 'Σ'], output: ['Ψ', 'Γ', 'Δ'], meaning: "שלומי טוב" },
            { id: 5, input: ['Γ', 'Δ'], output: ['Θ', 'Λ'], meaning: "כן" },
            { id: 6, input: ['Σ', 'Ω', 'Ψ'], output: ['Δ', 'Φ'], meaning: "לא" },
        ];

        let currentRoundIndex = 0; // Use index to iterate through rules
        const maxRounds = rules.length;

        totalRoundsSpan.textContent = maxRounds;

        let currentRule = null;

        function initializeRound(roundIndex) {
            currentRoundIndex = roundIndex;
            currentRoundSpan.textContent = currentRoundIndex + 1;

            currentRule = rules[currentRoundIndex];

            // Reset UI State
            inputSymbolsDiv.innerHTML = '';
            outputSymbolsDiv.innerHTML = '';
            externalEvaluationP.textContent = '';
            externalEvaluationArea.classList.remove('correct', 'incorrect'); // Clear evaluation colors
            submitButton.disabled = false;
            nextRoundButton.disabled = true;
            outputNoteDropzone.classList.remove('correct', 'incorrect'); // Clear note colors

            // Display Input Symbols
            currentRule.input.forEach(symbol => {
                const span = document.createElement('span');
                span.classList.add('symbol');
                span.textContent = symbol;
                inputSymbolsDiv.appendChild(span);
            });

            // Display Rule Book (all rules visible)
            // Highlight the current rule visually
            ruleListUl.innerHTML = '';
            rules.forEach((rule, index) => {
                const li = document.createElement('li');
                li.innerHTML = `<strong>כלל ${rule.id}:</strong> ${rule.input.join(' ')} &rarr; ${rule.output.join(' ')}`;
                 if (index === currentRoundIndex) {
                     li.style.fontWeight = 'bold';
                     li.style.backgroundColor = '#cfe2ff'; /* Light blue to highlight */
                     li.style.borderColor = '#007bff';
                 }
                ruleListUl.appendChild(li);
            });


            // Prepare Draggable Output Symbols (pool of *all* possible output symbols from all rules)
            const allOutputSymbolsSet = new Set();
             rules.forEach(rule => {
                 rule.output.forEach(symbol => allOutputSymbolsSet.add(symbol));
             });
            const availableSymbolsArray = Array.from(allOutputSymbolsSet);

            availableOutputSymbolsContainer.innerHTML = ''; // Clear previous symbols
            availableSymbolsArray.forEach(symbolText => {
                const span = document.createElement('span');
                span.classList.add('symbol', 'draggable');
                span.textContent = symbolText;
                span.setAttribute('draggable', true);
                span.dataset.symbol = symbolText; // Store symbol text
                availableOutputSymbolsContainer.appendChild(span);
            });

            // Add drag/drop listeners for the new round
            addDragDropListeners();
        }

        function addDragDropListeners() {
            const draggables = availableOutputSymbolsContainer.querySelectorAll('.symbol.draggable');
            const dropzone = outputSymbolsDiv; // The container *inside* the note

            draggables.forEach(symbol => {
                symbol.addEventListener('dragstart', (e) => {
                    e.dataTransfer.setData('text/plain', e.target.dataset.symbol);
                    e.target.classList.add('dragging');
                     e.dataTransfer.effectAllowed = 'move'; // Visual cue
                });
                 symbol.addEventListener('dragend', (e) => {
                    e.target.classList.remove('dragging');
                });
            });

            outputNoteDropzone.addEventListener('dragover', (e) => {
                e.preventDefault(); // Allow dropping
                outputNoteDropzone.classList.add('dragover');
                 e.dataTransfer.dropEffect = 'move';
            });

            outputNoteDropzone.addEventListener('dragleave', () => {
                outputNoteDropzone.classList.remove('dragover');
            });

            outputNoteDropzone.addEventListener('drop', (e) => {
                e.preventDefault();
                outputNoteDropzone.classList.remove('dragover');
                const symbolText = e.dataTransfer.getData('text/plain');

                // Add the dropped symbol to the output note
                const droppedSymbolSpan = document.createElement('span');
                droppedSymbolSpan.classList.add('symbol'); // No need for 'dropped' class now, just 'symbol'
                droppedSymbolSpan.textContent = symbolText;
                 // Add a click listener to remove dropped symbols
                droppedSymbolSpan.addEventListener('click', () => {
                     droppedSymbolSpan.remove();
                });
                outputSymbolsDiv.appendChild(droppedSymbolSpan);
            });
        }

        submitButton.addEventListener('click', () => {
            // Add a brief delay and visual feedback for "processing"
             submitButton.disabled = true;
             submitButton.textContent = 'בדיקה...';
             externalEvaluationArea.classList.remove('correct', 'incorrect');
             externalEvaluationP.textContent = 'מערכת ההערכה החיצונית בודקת...';


            setTimeout(() => {
                const droppedSymbols = Array.from(outputSymbolsDiv.querySelectorAll('.symbol')).map(span => span.textContent);
                const expectedOutput = currentRule.output;
                let evaluationText = '';
                let isCorrect = false;

                if (droppedSymbols.length === 0) {
                    evaluationText = `לא הנחת אף סימן בפתק הפלט.`;
                    isCorrect = false;
                } else if (droppedSymbols.length !== expectedOutput.length) {
                    evaluationText = `מספר הסימנים שגוי. נדרשים ${expectedOutput.length} סימנים לפי הכלל.`;
                    isCorrect = false;
                } else {
                    isCorrect = true;
                    for (let i = 0; i < expectedOutput.length; i++) {
                        if (droppedSymbols[i] !== expectedOutput[i]) {
                            isCorrect = false;
                            break;
                        }
                    }

                    if (isCorrect) {
                        evaluationText = `✅ תשובה מושלמת! מבחינת מי שמחוץ לחדר, זו הייתה תגובה נכונה לחלוטין ל"${currentRule.meaning}" (הקלט). ההערכה החיצונית קובעת: "מבין סינית!".`;
                         externalEvaluationArea.classList.add('correct');
                    } else {
                        evaluationText = `❌ סימנים שגויים או בסדר לא נכון. נסה שוב לפי הכלל. ההערכה החיצונית קובעת: "אינו מבין סינית!".`;
                         externalEvaluationArea.classList.add('incorrect');
                         // Allow retrying this round
                         submitButton.disabled = false;
                         submitButton.textContent = 'בדוק פלט';
                         return; // Don't enable next round
                    }
                }

                externalEvaluationP.textContent = evaluationText;
                 submitButton.textContent = 'בדוק פלט'; // Reset button text

                if (isCorrect) {
                    submitButton.disabled = true;
                    if (currentRoundIndex < maxRounds - 1) {
                        nextRoundButton.disabled = false;
                         externalEvaluationP.textContent += " - לחץ 'סבב הבא' כדי להמשיך.";
                    } else {
                         externalEvaluationP.textContent += " 🎉 סיימת את כל הסבבים בהצלחה!";
                         nextRoundButton.disabled = true; // Ensure disabled on last round completion
                    }
                }

            }, 800); // Simulate processing time
        });

        nextRoundButton.addEventListener('click', () => {
            if (currentRoundIndex < maxRounds - 1) {
                initializeRound(currentRoundIndex + 1);
            }
        });

        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationSection.style.display === 'none';
            explanationSection.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר על החדר הסיני' : 'הצג הסבר על החדר הסיני';
        });


        // Initialize the first round on page load
        if (rules.length > 0) {
            initializeRound(0);
        } else {
            // Handle case with no rules
            inputSymbolsDiv.innerHTML = '<p>אין כללים זמינים להדגמה.</p>';
             availableOutputSymbolsContainer.innerHTML = '<p>אין סמלים זמינים.</p>';
            submitButton.disabled = true;
            nextRoundButton.disabled = true;
             externalEvaluationP.textContent = 'הסימולציה אינה זמינה.';
        }
    });
</script>
---