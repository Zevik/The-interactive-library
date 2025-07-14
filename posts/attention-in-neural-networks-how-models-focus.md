---
title: "קשב ברשתות עצביות: כך מודלים 'מתמקדים'"
english_slug: attention-in-neural-networks-how-models-focus
category: "מדעי המחשב"
tags:
  - רשתות עצביות
  - קשב
  - למידת מכונה
  - AI
  - למידה עמוקה
---
<h1><span class="highlight-text">קשב ברשתות עצביות:</span> כך מודלים "מתמקדים"</h1>
<p>דמיינו שאתם קוראים טקסט ארוך או מנתחים תמונה מורכבת. המוח האנושי לא מעבד את הכל בבת אחת באותה מידה של חשיבות. הוא מתמקד – במילים המרכזיות במשפט, באובייקטים החשובים בתמונה. במודלים מתוחכמים של למידת מכונה, מנגנון הקשב (Attention) מעניק למודל יכולת דומה: לזהות ולהקצות "משקלי חשיבות" שונים לחלקים שונים של הקלט או של המצב הפנימי שלו. כך, הוא יודע "להתמקד" במידע הרלוונטי ביותר למשימה הנתונה, ממש כמו שאנחנו עושים.</p>

<div class="attention-demo-container interactive-card">
    <h2><span class="highlight-text">חוויה אינטראקטיבית:</span> קשב על רצף מספרים</h2>
    <p>בואו נדגים את הרעיון בפשטות. הזינו רצף של מספרים מופרדים בפסיקים, ובחרו "משימה". הסימולציה תציג ויזואלית את "משקלי הקשב" שהמודל הדמיוני שלנו מקצה לכל מספר - עד כמה הוא "מתמקד" בו - עבור המשימה שנבחרה.</p>

    <div class="controls">
        <div class="control-group">
            <label for="input-sequence" class="control-label">הזינו מספרים (מופרדים בפסיקים):</label>
            <input type="text" id="input-sequence" value="10, 5, 20, 15, 8, 25, 12" placeholder="לדוגמה: 1, 5, 2, 10, 3">
        </div>
        <div class="control-group">
            <label for="task-select" class="control-label">בחרו "מטרה" (Query):</label>
            <select id="task-select">
                <option value="find-max">המטרה: למצוא את המספר הגבוה ביותר</option>
                <option value="sum-evens">המטרה: לסכום מספרים זוגיים</option>
                <option value="attend-to-first">המטרה: להתמקד במספר הראשון</option>
            </select>
        </div>
        <button id="simulate-button">התמקד עכשיו!</button>
    </div>

    <div class="attention-output">
        <h3>משקלי הקשב (התמקדות המודל)</h3>
        <div id="output-area" class="output-viz">
            <!-- Attention visualization will be rendered here -->
        </div>
         <p id="output-message" class="message-area"></p>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">מה קרה כאן? הסבר על קשב</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2><span class="highlight-text">צלול פנימה:</span> כך עובד מנגנון הקשב</h2>

    <h3><span class="highlight-text">הצורך בקשב:</span> להתמודד עם ים של מידע</h3>
    <p>מודלים מסורתיים לעיבוד רצפים (כמו RNNs) נתקלו באתגר משמעותי כשהתמודדו עם רצפים ארוכים (משפטים ארוכים, סדרות נתונים ארוכות). הם נאלצו "לדחוס" את כל המידע מהרצף כולו לתוך ייצוג פנימי יחיד בגודל קבוע. ככל שהרצף היה ארוך יותר, כך היה קשה יותר למודל "לזכור" ולהשתמש במידע שהופיע בתחילתו כשהוא הגיע לסופו. זה כמו לנסות לזכור את כל הפרטים משיחה ארוכה ומורכבת – קשה לשמור על הכל בראש בו זמנית.</p>

    <h3><span class="highlight-text">הפתרון הגאוני:</span> לאפשר למודל "להביט אחורה"</h3>
    <p>מנגנון הקשב שינה את כללי המשחק. במקום להסתמך רק על הזיכרון הפנימי הנוכחי, הוא מאפשר למודל, בכל רגע נתון (למשל, כשהוא מנסה להחליט מה המילה הבאה בפלט), "להביט אחורה" על כל חלקי קלט המקור ו"להקצות" תשומת לב שונה לכל חלק, בהתאם למידת הרלוונטיות שלו למשימה או למצב הנוכחי. זה מאפשר למודל לגשת ישירות למידע חשוב, גם אם הוא הופיע רחוק בקלט.</p>

    <h3><span class="highlight-text">איך מחשבים את ה"התמקדות"?</span> הרעיון מאחורי משקלי הקשב</h3>
    <p>הליבה של מנגנון הקשב היא חישוב "משקלי קשב" (Attention Weights). זהו תהליך שבו המודל קובע כמה "חזק" הוא צריך להתייחס לכל רכיב בקלט (או במצב פנימי אחר) עבור המשימה הספציפית שהוא מבצע כעת. התהליך הבסיסי כולל:</p>
    <ol>
        <li><b>שאילתה (Query):</b> המודל שואל שאלה, או מתייחס למצב הפנימי הנוכחי שלו – זה הדבר שעבורו אנו רוצים לחשב את הקשב. בדוגמה שלנו, זו ה"מטרה" שבחרתם (למצוא מקסימום, לסכום זוגיים וכו').</li>
        <li><b>מפתחות וערכים (Keys & Values):</b> כל רכיב בקלט (כל מספר ברצף בדוגמה) מיוצג על ידי "מפתח" ו"ערך". במקרים רבים, המפתח והערך זהים או נגזרים מאותו ייצוג. המפתחות משמשים כדי להשוות אותם לשאילתה, והערכים הם המידע שאוספים (בסכום משוקלל) כדי ליצור את הפלט. בדוגמה שלנו, המפתח והערך עבור כל מספר הוא פשוט המספר עצמו.</li>
        <li><b>חישוב התאמה/ציון (Score):</b> מחשבים עד כמה השאילתה "דומה" או "מתאימה" למפתח של כל רכיב בקלט. זהו ה"ציון" הראשוני לרלוונטיות. בדוגמה הפשטנית שלנו, הציון גבוה יותר אם המספר עונה על הקריטריון של המטרה שנבחרה.</li>
        <li><b>חישוב משקלים (Weights):</b> הציון הופך ל"משקל קשב", לרוב באמצעות פונקציית softmax שמבטיחה שכל המשקלים יחד יסכמו ל-1. זה מנרמל את הציונים ומספק התפלגות הסתברותית של חשיבות על פני כל רכיבי הקלט. הויזואליזציה שמודגמת מציגה את המשקלים האלה לאחר נרמול (לרוב בין 0 ל-1).</li>
        <li><b>יצירת וקטור הקשר (Context Vector):</b> לבסוף, לוקחים את הערכים של כל רכיבי הקלט ומסכמים אותם בצורה משוקללת, כאשר כל ערך מוכפל במשקל הקשב שלו. וקטור הקשר הזה "מקבץ" את המידע הרלוונטי ביותר מהקלט, מודגש לפי משקלי הקשב שחושבו. וקטור זה משמש את המודל להמשך העיבוד או ליצירת הפלט.</li>
    </ol>

    <h3><span class="highlight-text">טרנספורמרים וקשב עצמי (Self-Attention):</span> המהפכה הגדולה</h3>
    <p>מודלים מודרניים כמו הטרנספורמרים (הבסיס למודלי שפה כמו GPT, BERT ועוד) מבוססים בעיקר על מנגנון "קשב עצמי". במנגנון זה, המודל לא רק מתמקד בקלט המקור, אלא גם בייצוגים פנימיים של הקלט עצמו. כל רכיב ברצף (כל מילה במשפט, למשל) יכול לחשב את הקשב שלו ביחס לכל שאר הרכיבים באותו רצף. זה מאפשר למודל להבין קשרים מורכבים ותלויות ארוכות טווח בתוך הרצף, בלי התלות בחישוב סדרתי כמו ב-RNNs, ובכך מתאפשר אימון מקבילי ויעיל יותר.</p>

    <h3><span class="highlight-text">למה זה כל כך חשוב?</span> היתרונות המרכזיים</h3>
    <ul>
        <li><b>הבנה עמוקה יותר של הקשר:</b> גישה ישירה לכל חלקי הקלט מאפשרת למודל ללכוד תלויות מרוחקות שקשה היה למודלים קודמים לאתר.</li>
        <li><b>יעילות חישובית:</b> בקשב עצמי, החישובים ניתנים למקביליות רבה, מה שמאיץ משמעותית את האימון וההסקה.</li>
        <li><b>ביצועים פורצי דרך:</b> מודלים מבוססי קשב שברו שיאים כמעט בכל משימה של עיבוד שפה טבעית, ושינו תחומים כמו ראייה ממוחשבת וזיהוי דיבור.</li>
        <li><b>שקיפות (חלקית):</b> משקלי הקשב יכולים לפעמים לשמש ככלי עזר להבנת ה"מחשבה" של המודל - על אילו חלקי קלט הוא "התבסס" בקבלת החלטה מסוימת.</li>
    </ul>

    <h3><span class="highlight-text">יישומים בכל מקום:</span> איפה פוגשים קשב?</h3>
    <p>כיום, מנגנון הקשב הוא אבן בניין יסודית בארכיטקטורות המודרניות ביותר:</p>
    <ul>
        <li><b>מודלי שפה גדולים (LLMs):</b> כל מודלי הטרנספורמר כמו GPT, BERT, LLaMA, ועוד – ליבתם היא מנגנון הקשב.</li>
        <li><b>תרגום מכונה:</b> במודלים מתקדמים, הקשב מאפשר למודל התרגום להתמקד במילים הרלוונטיות בשפת המקור תוך כדי יצירת המילים בשפת היעד.</li>
        <li><b>ראייה ממוחשבת:</b> מודלי Vision Transformers (ViT) משתמשים בקשב כדי להתמקד בחלקים חשובים בתמונה.</li>
        <li><b>יצירת תוכן:</b> ממודלי יצירת תמונות מטקסט (Text-to-Image) ועד סיכום טקסטים או יצירת קוד – קשב הוא המפתח ליכולת של המודל לחבר בין רעיונות שונים ולייצר תוכן קוהרנטי ורלוונטי.</li>
    </ul>
</div>

<style>
    /* הגדרות בסיסיות */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        background-color: #f4f7f6; /* רקע רך */
        color: #333;
        direction: rtl;
        text-align: right;
    }

    h1, h2, h3 {
        color: #2c3e50; /* כותרות כהות יותר */
        text-align: right;
        margin-bottom: 15px;
    }

     h1 {
        font-size: 2.2em;
        margin-bottom: 25px;
    }

    h2 {
        font-size: 1.8em;
        margin-bottom: 20px;
        border-bottom: 2px solid #bdc3c7; /* קו תחתון עדין */
        padding-bottom: 5px;
    }

     h3 {
         font-size: 1.4em;
         margin-top: 20px;
         margin-bottom: 10px;
         color: #34495e;
     }

    p {
        margin-bottom: 15px;
    }

    .highlight-text {
        color: #3498db; /* צבע הדגשה יפה */
        font-weight: bold;
    }


    /* עיצוב כללי לכרטיסים/קונטיינרים */
    .interactive-card, .explanation-section {
        background-color: #ffffff; /* רקע לבן לכרטיסים */
        border: 1px solid #e0e0e0; /* גבול עדין */
        border-radius: 12px; /* פינות מעוגלות יותר */
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); /* צל רך ועדין */
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out; /* אנימציה בריחוף */
    }

    .interactive-card:hover, .explanation-section:hover {
         transform: translateY(-3px); /* אפקט ריחוף קל */
         box-shadow: 0 6px 16px rgba(0, 0, 0, 0.12);
    }


    /* עיצוב פקדים */
    .controls {
        margin-bottom: 30px;
        display: flex;
        flex-direction: column; /* Arrange controls vertically initially */
        gap: 20px; /* Space between control groups */
        align-items: flex-start; /* Align items to the right in RTL */
    }

    @media (min-width: 768px) { /* Arrange controls horizontally on larger screens */
        .controls {
             flex-direction: row;
             align-items: center;
        }
    }


    .control-group {
        display: flex;
        flex-direction: column;
        align-items: flex-start; /* Align label and input */
        gap: 8px;
        min-width: 200px; /* Ensure input groups have minimum width */
    }

    .control-label {
        font-weight: bold;
        color: #555;
        font-size: 1em;
    }

    .controls input[type="text"],
    .controls select {
        padding: 12px 15px; /* הגדלת padding */
        border: 1px solid #ccc;
        border-radius: 6px; /* פינות מעוגלות */
        font-size: 1em;
        min-width: 200px; /* רוחב מינימלי */
        box-sizing: border-box; /* Include padding and border in element's total width/height */
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    .controls input[type="text"]:focus,
    .controls select:focus {
        border-color: #3498db;
        box-shadow: 0 0 8px rgba(52, 152, 219, 0.2);
        outline: none;
    }

    .controls button {
        background-color: #3498db; /* כחול בוהק */
        color: white;
        padding: 12px 25px; /* הגדלת padding */
        border: none;
        border-radius: 6px; /* פינות מעוגלות */
        cursor: pointer;
        font-size: 1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
        margin-top: 10px; /* Add margin top for stacking on small screens */
    }

     @media (min-width: 768px) { /* Remove margin top on larger screens */
        .controls button {
            margin-top: 0;
            align-self: flex-end; /* Align button to the bottom of the flex row */
        }
     }


    .controls button:hover {
        background-color: #2980b9; /* כחול כהה יותר בריחוף */
        transform: translateY(-1px); /* אפקט לחיצה קל */
    }

    .controls button:active {
        transform: translateY(0);
    }


    /* ויזואליזציית הקשב */
    .attention-output h3 {
        margin-top: 0;
        margin-bottom: 15px;
        color: #2c3e50;
    }

    .output-viz {
        display: flex;
        gap: 12px; /* רווח גדול יותר בין פריטים */
        flex-wrap: wrap;
        align-items: flex-end; /* יישור לתחתית */
        min-height: 100px; /* גובה מינימלי */
        padding: 15px 0;
        border-top: 1px dashed #bdc3c7; /* קו מפריד עדין */
        background-color: #ecf0f1; /* רקע עדין לאזור התצוגה */
        border-radius: 8px;
        padding: 20px;
        box-sizing: border-box;
        overflow-x: auto; /* Add scroll for long sequences */
    }

    .attention-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end; /* Align content to the bottom */
        border: 1px solid #bdc3c7;
        border-radius: 6px;
        padding: 8px 10px; /* עדין יותר */
        min-width: 60px; /* רוחב מינימלי גדול יותר */
        text-align: center;
        background-color: #e0e0e0; /* צבע בסיס אפור */
        color: #333;
        font-weight: bold;
        transition: background-color 0.5s ease, height 0.5s ease, transform 0.2s ease; /* אנימציות מעבר חלקות */
        cursor: help; /* Indicate tooltip */
        position: relative; /* Needed for potential pseudo-elements */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05); /* צל קל */
    }

     .attention-item:hover {
         transform: translateY(-5px); /* אפקט ריחוף עדין בריחוף */
     }


     .attention-value {
        font-size: 1.3em; /* הגדלת גודל המספר */
        font-weight: bold;
        margin-bottom: 5px;
     }

     /* סרגל ויזואלי של הקשב - אופציונלי, באמצעות פס בתחתית */
     .attention-bar {
         width: 100%;
         height: 6px; /* עובי הפס */
         background-color: #2ecc71; /* צבע הדגשה ירוק */
         border-radius: 3px; /* פינות מעוגלות לפס */
         margin-top: 5px; /* רווח מהמספר */
         transform-origin: bottom; /* קנה מידה מהתחתית */
         /* Initial state for animation */
         transform: scaleY(0.1); /* Start scaled down */
         opacity: 0; /* Start invisible */
         transition: transform 0.6s ease-out, opacity 0.6s ease-out; /* אנימציית הופעה וגדילה */
     }

     /* State after animation */
     .attention-item.animated .attention-bar {
         transform: scaleY(1); /* Scale to full height */
         opacity: 1; /* Become visible */
     }


    /* אזור הודעות שגיאה/אזהרה */
    .message-area {
        min-height: 20px; /* Reserve space */
        color: #e74c3c; /* צבע שגיאה */
        font-weight: bold;
        margin-top: 10px;
        text-align: right;
    }


    /* עיצוב כפתור הצגת/הסתרת הסבר */
    .toggle-button {
        background-color: #95a5a6; /* אפור ניטרלי */
        color: white;
        padding: 12px 25px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1em;
        font-weight: bold;
        margin-bottom: 25px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        display: block; /* Full width button */
        width: fit-content; /* Adjust width to content */
        margin-left: auto; /* Center or align right in RTL */
        margin-right: auto; /* Center button */
    }

     @media (min-width: 768px) {
         .toggle-button {
             margin-right: 0; /* Align right on larger screens */
             margin-left: auto;
         }
     }

    .toggle-button:hover {
        background-color: #7f8c8d;
        transform: translateY(-1px);
    }
     .toggle-button:active {
        transform: translateY(0);
     }


    /* עיצוב אזור ההסבר */
    .explanation-section {
         /* Styles already defined with .interactive-card */
         margin-top: 20px; /* Add space if following the button */
    }

    .explanation-section ul {
        padding-right: 25px; /* הגדלת הזחה לרשימה */
        list-style-type: disc;
        margin-bottom: 15px;
    }

    .explanation-section li {
        margin-bottom: 12px;
    }

     .explanation-section ol {
         padding-right: 25px; /* הגדלת הזחה לרשימה ממוספרת */
         margin-bottom: 15px;
     }

    .explanation-section ol li {
         margin-bottom: 12px;
     }

     .explanation-section strong {
         color: #34495e; /* הדגשת מילים חשובות */
     }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const inputSequenceEl = document.getElementById('input-sequence');
        const taskSelectEl = document.getElementById('task-select');
        const simulateButtonEl = document.getElementById('simulate-button');
        const outputAreaEl = document.getElementById('output-area');
        const outputMessageEl = document.getElementById('output-message');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationSection = document.getElementById('explanation');

        // --- פונקציית חישוב קשב מפושטת ---
        // מדמה חישוב משקלי קשב על בסיס מטרה (שאילתה) וערכי הקלט (מפתחות/ערכים)
        function calculateAttention(sequence, task) {
            const numbers = sequence.map(Number); // Keep only numbers, NaN for invalid
            const validNumbers = numbers.filter(n => !isNaN(n));

            if (validNumbers.length === 0) {
                return new Array(numbers.length).fill(0); // Return zero weights if no valid numbers
            }

            const weights = new Array(numbers.length).fill(0);

            let rawWeights = []; // Store calculated raw scores

            // Simulate simple raw score calculation based on task (Query vs Keys/Values)
            switch (task) {
                case 'find-max':
                    const maxVal = Math.max(...validNumbers);
                     numbers.forEach((num, index) => {
                          // Raw score: High if equals max, low otherwise. Add small value to others for visual scale.
                          rawWeights[index] = isNaN(num) ? 0 : (num === maxVal ? 100 : 5);
                     });
                    break;
                case 'sum-evens':
                     numbers.forEach((num, index) => {
                         // Raw score: High for even, low for odd.
                         rawWeights[index] = isNaN(num) ? 0 : (num % 2 === 0 ? 100 : 5);
                     });
                    break;
                case 'attend-to-first':
                    numbers.forEach((num, index) => {
                        // Raw score: Highest for the first valid element.
                         rawWeights[index] = isNaN(num) ? 0 : (index === numbers.findIndex(n => !isNaN(n)) ? 100 : 5);
                    });
                    break;
                default:
                    // Default: uniform attention (equal raw scores)
                     rawWeights = new Array(numbers.length).fill(10);
                    break;
            }

            // Simulate Softmax-like normalization to get weights between 0 and 1
            // Find the sum of positive raw weights to handle potential zeros from NaNs or logic
            const positiveRawWeights = rawWeights.filter(w => w > 0);
            const sumRawWeights = positiveRawWeights.reduce((sum, w) => sum + w, 0);


            if (sumRawWeights > 0) {
                 rawWeights.forEach((raw, index) => {
                     // Normalize: weight is raw_score / total_raw_score
                     // Use a small epsilon to prevent division by zero edge cases if somehow sum is zero
                     weights[index] = raw / (sumRawWeights + 1e-9);
                 });
             } else {
                 // If sum is 0 (e.g., all inputs invalid), weights remain 0
                 weights.fill(0);
             }


            return weights; // Return normalized weights (0 to ~1)
        }

        // --- פונקציית ויזואליזציה של הקשב ---
        function renderAttention(sequence, weights) {
            outputAreaEl.innerHTML = ''; // Clear previous output
            outputMessageEl.textContent = ''; // Clear previous message

            const items = sequence.map(s => s.trim()); // Keep original strings for display
            const numbers = items.map(Number);
            const hasInvalidInput = numbers.some(isNaN);

            if (items.length === 0 || items.every(item => item === '')) {
                 outputAreaEl.innerHTML = '<p class="message-area">הזינו רצף של מספרים (מופרדים בפסיקים) כדי להתחיל.</p>';
                 return;
            }

            if (hasInvalidInput) {
                outputMessageEl.textContent = 'אזהרה: הקלט מכיל ערכים לא מספריים. מוצגים הערכים שהוזנו, אך משקלי הקשב עשויים להיות מושפעים או לא ניתנים לחישוב מלא.';
            }


            items.forEach((itemStr, index) => {
                const itemEl = document.createElement('div');
                itemEl.classList.add('attention-item');

                // Determine weight for this item. Use 0 if the input was NaN.
                const weight = isNaN(numbers[index]) ? 0 : weights[index]; // weight is already scaled 0-1 by calculateAttention

                // Use the weight for visual intensity and height
                // Scale weight visually: Minimum intensity/height for visibility, max for highlight
                const visualWeight = Math.max(0.05, weight); // Ensure minimal height/color even if weight is low

                // Color interpolation (Grey to Green)
                const baseColor = [224, 224, 224]; // RGB for #e0e0e0 (light grey)
                const attentionColor = [46, 204, 113]; // RGB for #2ecc71 (emerald green)

                const blendedColor = [
                    Math.round(baseColor[0] * (1 - visualWeight) + attentionColor[0] * visualWeight),
                    Math.round(baseColor[1] * (1 - visualWeight) + attentionColor[1] * visualWeight),
                    Math.round(baseColor[2] * (1 - visualWeight) + attentionColor[2] * visualWeight)
                ];

                itemEl.style.backgroundColor = `rgb(${blendedColor[0]}, ${blendedColor[1]}, ${blendedColor[2]})`;

                 // Set height based on weight - scale from a minimum to a maximum pixel height
                 const minHeight = 50; // base height in px (includes padding etc.)
                 const maxHeight = 150; // max height for visualization bar
                 // The actual bar height is added inside via .attention-bar
                 itemEl.style.height = `${minHeight}px`; // Set item container base height

                itemEl.innerHTML = `<div class="attention-value">${itemStr}</div>`;

                // Add the visual bar element *inside* the item
                const barEl = document.createElement('div');
                barEl.classList.add('attention-bar');
                 // Scale bar height based on the actual weight (0 to 1), not visualWeight minimum
                const barHeight = weight * (maxHeight - minHeight); // Calculate height above minHeight
                barEl.style.height = `${Math.max(0, barHeight)}px`; // Ensure non-negative height

                itemEl.appendChild(barEl);


                // Add tooltip showing normalized weight
                itemEl.setAttribute('title', `משקל קשב מנורמל: ${weight.toFixed(3)}`);

                outputAreaEl.appendChild(itemEl);

                // Trigger animation for the bar after adding to DOM
                 requestAnimationFrame(() => {
                    setTimeout(() => {
                         barEl.parentElement.classList.add('animated');
                     }, index * 50); // Stagger animation slightly
                 });

            });
        }

        // --- מטפל אירועים לכפתור ההדגמה ---
        simulateButtonEl.addEventListener('click', () => {
            const inputText = inputSequenceEl.value;
            const task = taskSelectEl.value;
            const sequence = inputText.split(',').map(s => s.trim());

            // Filter out completely empty strings before processing
            const validSequenceStrings = sequence.filter(s => s !== '');

             // Map to numbers for calculation, keeping track of NaNs
            const numbersForCalculation = validSequenceStrings.map(s => Number(s));


            const weights = calculateAttention(numbersForCalculation, task);

            // Render using the original (possibly invalid) strings but the calculated weights
            renderAttention(validSequenceStrings, weights);
        });

        // --- מטפל אירועים לכפתור הצגת/הסתרת הסבר ---
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationSection.style.display === 'none';
            explanationSection.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר על קשב' : 'מה קרה כאן? הסבר על קשב';
            // Optional: Scroll to the explanation section when shown
            if (isHidden) {
                 explanationSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });

        // --- הדגמה ראשונית בטעינת הדף ---
        // Simulate button click on page load to show the initial state
        simulateButtonEl.click();
    });
</script>
```