---
title: "אמן בינה מלאכותית: לאמן מודל ליצירת שירה"
english_slug: ai-artist-training-a-model-to-create-poetry
category: "מדעי המחשב"
tags: [בינה מלאכותית, למידת מכונה, עיבוד שפה טבעית, שירה, יצירתיות]
---
<h1>אמן בינה מלאכותית: לרקוד עם מילים וללמד מכונה את הקצב</h1>
<p>האם בינה מלאכותית יכולה לגעת בנשמה של השירה? האם היא מסוגלת ליצור מילים שנוגעות בלב, או לפחות לחקות את הקצב והזרימה שלהן? בואו נצלול לסימולציה קטנה שתראה לנו איך מלמדים מכונה "לרקוד" עם מילים, צעד אחר צעד.</p>

<div class="interactive-container">
    <div class="section-controls card">
        <h2>אוצר המילים שלך (נתוני אימון)</h2>
        <p>כאן אתה הבמאי! הזן קטעי שירה קצרים או טקסטים שישמשו "מורה" למודל. ככל שהטקסט עשיר ומגוון יותר, כך המודל יאסוף יותר "השראה" (דפוסים סטטיסטיים פשוטים).</p>
        <textarea id="training-data" rows="12" placeholder="הקלד או הדבק שירי אימון כאן. כל שורה חדשה היא כמו נשימה בשיר."></textarea>
        <div class="button-group">
             <button id="load-preset-data" class="secondary-button">טען דוגמאות שירה</button>
             <button id="train-button" class="primary-button">אמן צעד אחד (עידן)</button>
        </div>
         <div id="training-status" class="status-message"></div>
        <div id="training-epochs" class="epoch-counter">עידני אימון: 0</div>
    </div>

    <div class="section-visualization card">
        <h2>המפה של המודל (דפוסים שנלמדו)</h2>
        <p>תאר לעצמך מפה שמראה אילו מילים אוהבות לבוא אחרי אילו מילים. זהו הייצוג הפשטני שלנו ל"מוח" של המודל אחרי שלמד מהטקסט שלך. ככל שהמודל מאומן יותר, המפה מתרחבת ומתבהרת (בגבולות הסימולציה).</p>
        <div id="model-state" class="visualization-output">המודל ממתין להשראה. טען נתונים ואמן.</div>
         <div id="model-summary" class="summary-stats"></div>
    </div>

    <div class="section-output card">
        <h2>היצירה של המכונה (שירה שנוצרה)</h2>
        <p>על בסיס המפה שלמד, המודל ינסה עכשיו ליצור "שירה" משלו. זכור, זוהי יצירה סטטיסטית – חיבור מילים על בסיס הסתברויות, לא מתוך רגש או הבנה עמוקה.</p>
        <div id="generated-poetry" class="generated-text">לחץ על 'אמן' כדי שהמודל יתחיל ליצור...</div>
        <h3>הצצה סטטיסטית:</h3>
        <div id="metric-output" class="metric-output">עדיין אין נתונים לניתוח.</div>
    </div>
</div>

<button id="toggle-explanation" class="explanation-button">רוצה לדעת איך הקסם הזה קורה? (הסבר מעמיק)</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2>מסך מאחורי הקלעים: איך המכונה לומדת "לשיר"?</h2>

    <h3>מה זה בכלל בינה מלאכותית יוצרת?</h3>
    <p>בינה מלאכותית יוצרת (Generative AI) היא כמו אמן דיגיטלי. במקום רק לזהות או למיין דברים קיימים (כמו לזהות חתול בתמונה), היא יוצרת משהו חדש לגמרי – טקסט, תמונות, מוזיקה, קוד. הסימולטור שלנו הוא דוגמה פשוטה למודל כזה, שמטרתו לייצר טקסט שנראה כמו שירה, על בסיס מה שלמד. הוא לא ממציא יש מאין, אלא משלב ומרכיב מחדש דפוסים שראה בנתוני האימון, קצת כמו קולאז' של מילים.</p>

    <h3>מודל שפה בסיסי: בונה קשרים בין מילים</h3>
    <p>המודל כאן הוא סוג פשוט של מודל שפה. תחשבו עליו כעל סטטיסטיקאי חרוץ שקורא את שירי האימון ורושם: "אחרי המילה 'ענן' הופיעה המילה 'עבר' 3 פעמים, המילה 'בכה' פעם אחת...". הוא בונה טבלה ענקית של הסתברויות – מהי הסיכוי שכל מילה תופיע אחרי מילה מסוימת. זה נקרא מודל N-gram (במקרה שלנו, Bigram או 2-gram, כי הוא מסתכל רק על הקשר בין זוגות מילים עוקבות).</p>
    <p>בתהליך ה"אימון", המודל פשוט עובר על הטקסט שנתת לו, מילה אחרי מילה, ומעדכן את טבלאות ההסתברות שלו. כל "עידן" אימון הוא פשוט עוד מעבר כזה על כל הטקסט. המודל לא "מבין" את המשמעות או הרגש, הוא רק סופר ומחשב. כדי ליצור שירה, הוא פשוט בוחר מילה התחלתית (למשל, אחרי סימן של סוף שורה או מילה אקראית), ואז בוחר את המילה הבאה לפי ההסתברות שלה להופיע אחרי המילה הנוכחית, וחוזר על התהליך.</p>

    <h3>למה כל כך קשה למכונה ליצור אמנות אמיתית?</h3>
    <p>שירה אנושית היא הרבה יותר מסתם סדרת מילים. היא משלבת:</p>
    <ul>
        <li><strong>רגש ועומק:</strong> למכונה אין רגשות או ניסיון חיים. היא לא יכולה "להרגיש" געגוע או שמחה.</li>
        <li><strong>משמעות וקוהרנטיות:</strong> המודל שלנו יכול ליצור שורה שנראית הגיונית, אבל קשה לו לשמור על רעיון מרכזי, עלילה או רגש אחיד לאורך שיר שלם.</li>
        <li><strong>מבנה וקצב:</strong> לכידת מבנים שיריים מורכבים כמו משקל, חריזה עקיבה, או מבנה בתים ספציפי, דורשת מודלים מתוחכמים הרבה יותר שמסוגלים להסתכל רחוק יותר מקשר בין שתי מילים סמוכות.</li>
        <li><strong>יצירתיות מקורית:</strong> יצירתיות אמיתית כרוכה בהפרה יצירתית של חוקים, שילוב רעיונות לא צפויים וחדשנות פורצת דרך. המודלים הסטטיסטיים נוטים לשחזר דפוסים קיימים ולא ליצור משהו חדש לחלוטין.</li>
    </ul>
    <p>מודלים מתקדמים יותר (כמו אלה שמאחורי מודלים גדולים כמו GPT) משתמשים בארכיטקטורות שונות (טרנספורמרים) ויכולים ללמוד קשרים מורכבים יותר ממאגרי טקסט ענקיים, ולכן התוצר שלהם מרשים הרבה יותר ופעמים רבות נראה "יצירתי". אבל גם הם עדיין מבוססים על זיהוי דפוסים וחיזויים הסתברותיים, ולא על הבנה אנושית.</p>

    <h3>הבינה המלאכותית - כלי יצירתי חדש?</h3>
    <p>למרות המגבלות, AI יוצרת פותחת דלתות חדשות. היא יכולה להיות עוזרת אישית לאמנים – לספק רעיונות ראשוניים, וריאציות, או לשמש כשותפה לדיאלוג יצירתי. היא מאפשרת לנו לחשוב מחדש על מהי יצירתיות, מי יכול להיות "אמן", ומהם הגבולות בין יצירה אנושית ליצירה אלגוריתמית. הסימולטור הפשוט הזה הוא רק הצצה קטנה לעולם מרתק זה.</p>
</div>

<style>
    :root {
        --primary-color: #6A1B9A; /* Deep Purple */
        --primary-dark: #4A148C;
        --secondary-color: #FFC107; /* Amber */
        --secondary-dark: #FFA000;
        --background-color: #F3E5F5; /* Lightest Purple */
        --card-background: #FFFFFF;
        --text-color: #212121; /* Dark Grey */
        --border-color: #E1BEE7; /* Lighter Purple */
        --shadow-light: 0 2px 5px rgba(0,0,0,0.1);
        --shadow-medium: 0 5px 15px rgba(0,0,0,0.15);
    }

    body {
        font-family: 'Arial Hebrew', sans-serif; /* Use a Hebrew-friendly font */
        line-height: 1.7; /* Slightly increased line height */
        color: var(--text-color);
        background-color: var(--background-color);
        margin: 0;
        padding: 20px;
        direction: rtl; /* Right-to-left for Hebrew */
        text-align: right; /* Align text to the right */
        box-sizing: border-box;
    }

    h1, h2, h3 {
        color: var(--primary-dark);
        text-align: center;
        margin-bottom: 15px;
    }

    h1 {
        font-size: 2.2em;
        margin-bottom: 25px;
        text-shadow: var(--shadow-light);
    }

    h2 {
         font-size: 1.6em;
         border-bottom: 2px solid var(--secondary-color);
         padding-bottom: 5px;
         margin-bottom: 15px;
         text-align: right; /* Align section titles right */
    }

    h3 {
        font-size: 1.2em;
        color: var(--primary-color);
        margin-top: 20px;
        margin-bottom: 10px;
        text-align: right; /* Align explanation headings right */
    }

    p {
        margin-bottom: 15px;
    }

    .interactive-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); /* Adjusted min width */
        gap: 25px; /* Increased gap */
        margin-bottom: 30px;
    }

    .card {
        background-color: var(--card-background);
        padding: 25px; /* Increased padding */
        border-radius: 12px; /* More rounded corners */
        box-shadow: var(--shadow-medium); /* Stronger shadow */
        display: flex;
        flex-direction: column;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid var(--border-color); /* Subtle border */
    }

     .card:hover {
         transform: translateY(-5px); /* Lift effect on hover */
         box-shadow: 0 8px 20px rgba(0,0,0,0.2);
     }

    .section-controls, .section-output {
         min-height: 450px; /* Ensure sections have minimal height */
    }

    textarea {
        width: 100%;
        padding: 12px; /* Increased padding */
        margin-bottom: 15px; /* Increased margin */
        border: 1px solid var(--border-color);
        border-radius: 8px; /* More rounded corners */
        font-size: 1.05rem; /* Slightly larger font */
        box-sizing: border-box; /* Include padding in width */
        resize: vertical; /* Allow vertical resize */
        font-family: 'Arial Hebrew', sans-serif; /* Match body font */
        line-height: 1.6;
        transition: border-color 0.3s ease;
    }

    textarea:focus {
        outline: none;
        border-color: var(--primary-color); /* Highlight on focus */
        box-shadow: var(--shadow-light);
    }

    .button-group {
        display: flex; /* Arrange buttons in a row */
        gap: 10px; /* Space between buttons */
        margin-bottom: 15px;
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    button {
        display: inline-block;
        color: white;
        padding: 12px 20px; /* Increased padding */
        border: none;
        border-radius: 8px; /* More rounded corners */
        cursor: pointer;
        font-size: 1rem;
        transition: background-color 0.3s ease, transform 0.1s ease;
        flex-grow: 1; /* Allow buttons to grow */
        text-align: center;
    }

    .primary-button {
         background-color: var(--primary-color);
    }

    .secondary-button {
         background-color: var(--secondary-color);
         color: var(--text-color);
    }

    button:not(:disabled):hover {
        transform: translateY(-2px); /* Subtle lift on hover */
    }

    .primary-button:not(:disabled):hover {
         background-color: var(--primary-dark);
    }

    .secondary-button:not(:disabled):hover {
         background-color: var(--secondary-dark);
    }

     button:disabled {
         background-color: #ccc;
         cursor: not-allowed;
     }


    .status-message {
         margin-top: 5px;
         margin-bottom: 10px;
         font-size: 0.9em;
         color: #555;
         min-height: 1.2em; /* Reserve space */
    }

    .epoch-counter {
        margin-top: 10px;
        font-weight: bold;
        color: var(--primary-color);
        text-align: center;
        font-size: 1.1em;
    }

    .visualization-output, .generated-text {
        flex-grow: 1; /* Fill available space */
        background-color: #FCE4EC; /* Very light pink/purple hint */
        padding: 15px;
        border-radius: 8px;
        white-space: pre-wrap; /* Preserve whitespace and break lines */
        overflow-y: auto; /* Add scroll if content overflows */
        max-height: 200px; /* Limit height for visualization */
        font-family: 'Courier New', Courier, monospace; /* Monospace font for visualization */
        font-size: 0.9em;
        color: #333;
        border: 1px dashed var(--border-color);
    }

     .generated-text {
         font-family: 'Arial Hebrew', sans-serif; /* Non-monospace for poetry */
         font-style: italic;
         max-height: 180px; /* Limit height for generated poetry */
         margin-bottom: 15px;
         background-color: #E8F5E9; /* Very light green hint */
     }


    .summary-stats {
        font-size: 0.9em;
        color: #555;
        margin-top: 10px;
        text-align: center;
    }

    .metric-output {
        font-size: 0.9em;
        color: #555;
        background-color: #FFF3E0; /* Very light orange hint */
        padding: 10px;
        border-radius: 8px;
        border: 1px dashed var(--secondary-color);
    }


    .explanation-button {
        display: block; /* Make it a block button */
        margin: 20px auto; /* Center the button */
        padding: 12px 25px; /* Increased padding */
        font-size: 1.1rem;
        background-color: #7E57C2; /* Medium Purple */
        color: white;
        border-radius: 8px;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

     .explanation-button:hover {
        background-color: #673AB7; /* Darker Purple */
        transform: translateY(-2px);
     }


    .explanation-section {
        background-color: var(--card-background);
        padding: 25px;
        border-radius: 12px;
        box-shadow: var(--shadow-medium);
        margin-top: 20px;
        border: 1px solid var(--border-color);
        line-height: 1.8;
    }

    .explanation-section h2, .explanation-section h3 {
        text-align: right; /* Align explanation headings to the right */
        color: var(--primary-dark);
        border-bottom-color: var(--border-color); /* Subtle border */
    }

    .explanation-section ul, .explanation-section ol {
        list-style-position: inside; /* Bullets/numbers inside padding */
        padding-right: 20px;
        margin-bottom: 15px;
    }
     .explanation-section li {
        margin-bottom: 10px; /* Space list items */
     }

     /* Animation for content update */
     .fade-in {
        animation: fadeIn 0.5s ease-in-out;
     }

     @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
     }

     /* Responsive Adjustments */
     @media (max-width: 768px) {
         .interactive-container {
             grid-template-columns: 1fr; /* Stack columns on smaller screens */
             gap: 20px;
         }

         h1 {
             font-size: 1.8em;
         }
         h2 {
             font-size: 1.4em;
         }
          button {
              padding: 10px 15px;
              font-size: 0.95rem;
          }
           .explanation-button {
              font-size: 1rem;
              padding: 10px 20px;
           }
     }

</style>

<script>
    // Simple N-gram model (N=2, bigram) for demonstration
    let model = {};
    let epochs = 0;
    let isTraining = false; // State variable for training
    const trainingDataTextarea = document.getElementById('training-data');
    const trainButton = document.getElementById('train-button');
    const loadPresetButton = document.getElementById('load-preset-data');
    const modelStateDiv = document.getElementById('model-state');
    const modelSummaryDiv = document.getElementById('model-summary');
    const generatedPoetryDiv = document.getElementById('generated-poetry');
    const metricOutputDiv = document.getElementById('metric-output');
    const trainingEpochsDiv = document.getElementById('training-epochs');
    const trainingStatusDiv = document.getElementById('training-status');
    const explanationSection = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    // Preset training data (Hebrew poetry snippets)
    const presetData = `
ענן עבר בבכי
ושמש צחקה ברקיע
פרח נפתח בשדה
וריחו עלה למרום

ציפור שיר בלב האילן
שרקה לשמיים קריאה
קולה נשאב לרוח
ונבלע בין ענפים

שקט יורד על העמק
צללים נמתחים לאט
יום נגמר בעדינות
לילה עוטף את הכל

בלילות חורף קר
רוח לוחשת סודות
עצים עירומים עומדים
מצפים לאור ראשון

ים כחול עד אין סוף
גלים לוחשים סיפורים
שקיעה צובעת הכל
בצבעי אש וזהב
`; // Added more diverse data


    // --- Model Functions ---

    // Clean and tokenize text
    function tokenize(text) {
        // Replace punctuation with spaces, then split by whitespace including newlines.
        // Keep the newline token '\n'.
         const cleanedText = text.replace(/[.,;!?"'():]/g, '');
         const tokens = cleanedText.toLowerCase().split(/(\s+)/).filter(token => token.length > 0);

         // Replace sequences of whitespace with a single space, but keep '\n' special
         let processedTokens = [];
         tokens.forEach(token => {
             if (token === '\n') {
                 // If the last token added was NOT '\n', add '\n'. Avoid consecutive '\n'.
                 if (processedTokens.length === 0 || processedTokens[processedTokens.length - 1] !== '\n') {
                      processedTokens.push('\n');
                 }
             } else if (token.trim() === '') {
                 // If it's just whitespace (not \n), treat as a single space token
                 if (processedTokens.length === 0 || processedTokens[processedTokens.length - 1] !== ' ') {
                      processedTokens.push(' ');
                 }
             } else {
                 // It's a word, push it
                 processedTokens.push(token.trim());
             }
         });

         // Filter out remaining empty strings from aggressive cleaning/splitting
         return processedTokens.filter(token => token.length > 0);
    }


    // Train the model (build frequency map) - Incremental training
    function trainModel(text) {
        const tokens = tokenize(text);
        if (tokens.length < 2) return; // Need at least two tokens for bigrams

        // Add start-of-text token implicitly, or start lines with '\n' token
         // Let's use '\n' token effectively as start/end of lines

        for (let i = 0; i < tokens.length - 1; i++) {
            const currentWord = tokens[i];
            const nextWord = tokens[i + 1];

            // Treat space as a word separator, but don't train on space -> word or word -> space
             if (currentWord.trim() === '' || nextWord.trim() === '') continue;

            if (!model[currentWord]) {
                model[currentWord] = {};
            }

            if (!model[currentWord][nextWord]) {
                model[currentWord][nextWord] = 0;
            }
            model[currentWord][nextWord]++;
        }
        epochs++;
    }

    // Generate text using the trained model
    function generateText(maxLength = 150, numLines = 7) {
         const validStartWords = Object.keys(model).filter(key => key.trim().length > 0); // Only words, not spaces
        if (validStartWords.length === 0) {
             return "המודל ריק או לא אומן מספיק. אנא ודא שהכנסת טקסט.";
        }

        // Choose a random starting word that is not a newline or space
        let currentWord = validStartWords[Math.floor(Math.random() * validStartWords.length)];

        let generatedTokens = [currentWord];
        let tokensCount = 1;
        let linesGenerated = 0; // We'll count lines only when a '\n' token is added

        // Small improvement: Track current line length to potentially add newlines
        let currentLineLength = 1;
        const avgTrainingLineLength = parseFloat(calculateMetrics(null, trainingDataTextarea.value).match(/אורך שורה ממוצע בנתוני אימון: ([\d\.]+)/)[1]);
        const targetLineLength = isNaN(avgTrainingLineLength) || avgTrainingLineLength === 0 ? 5 : avgTrainingLineLength * 1.2; // Target slightly longer lines


        while (tokensCount < maxLength) {
             const possibleNextWords = model[currentWord];

             if (!possibleNextWords) {
                 // Current word has no followers. Try to end the line or find a new random start.
                 if (generatedTokens.length > 0 && generatedTokens[generatedTokens.length - 1] !== '\n') {
                     generatedTokens.push('\n');
                     linesGenerated++;
                 }
                 // Find a new random start word from the model
                  const restartWord = validStartWords[Math.floor(Math.random() * validStartWords.length)];
                  if (restartWord && model[restartWord]) { // Ensure the new start word also has followers
                       generatedTokens.push(restartWord);
                       currentWord = restartWord;
                       tokensCount++;
                       currentLineLength = 1;
                  } else {
                      // Cannot find a valid start word, break
                      break;
                  }

             } else {
                 // Select next word based on probabilities
                const total = Object.values(possibleNextWords).reduce((sum, count) => sum + count, 0);
                let random = Math.random() * total;
                let nextWord = null;
                for (const [word, count] of Object.entries(possibleNextWords)) {
                    random -= count;
                    if (random <= 0) {
                        nextWord = word;
                        break;
                    }
                }

                if (!nextWord) { // Fallback in case floating point issues or no options
                     const words = Object.keys(possibleNextWords);
                     if (words.length > 0) {
                        nextWord = words[Math.floor(Math.random() * words.length)]; // Pick random from options
                     } else {
                         // No next words available, break or try new line
                         if (generatedTokens.length > 0 && generatedTokens[generatedTokens.length - 1] !== '\n') {
                            generatedTokens.push('\n');
                            linesGenerated++;
                         }
                        break;
                     }
                }

                 // Add the chosen word/token
                 if (nextWord === '\n') {
                      if (generatedTokens.length > 0 && generatedTokens[generatedTokens.length - 1] !== '\n') {
                          generatedTokens.push('\n');
                          linesGenerated++;
                          currentLineLength = 0; // Reset line length
                      }
                 } else if (nextWord.trim().length > 0) { // Avoid adding empty space tokens explicitly in the generated list
                     generatedTokens.push(nextWord);
                     currentLineLength++;
                     tokensCount++;

                     // Add a newline token if the current line is long enough AND we haven't reached max lines
                      if (currentLineLength >= targetLineLength && linesGenerated < numLines -1 ) { // -1 because we might add one at the end
                         // Find a potential place to break, or force one
                          if (model[nextWord] && model[nextWord]['\n'] !== undefined) {
                               // The current word is sometimes followed by a newline in training data - good place to break
                                generatedTokens.push('\n');
                                linesGenerated++;
                                currentLineLength = 0;
                                currentWord = '\n'; // Start the next sequence from the newline token
                                continue; // Skip setting currentWord to nextWord below, as we already set it to '\n'
                          } else {
                               // No natural newline after this word, check if we should force one
                               // Forcing is complex in bigram. Let's rely on the model learning \n transitions.
                               // Just continue if no natural break found yet.
                          }
                      }
                 }
                currentWord = nextWord; // Set the word for the next iteration
            }

             if (linesGenerated >= numLines) break; // Stop if max lines reached
        }

        // Ensure the text ends with a newline if we generated enough lines but didn't naturally end a line
         if (linesGenerated < numLines && generatedTokens.length > 0 && generatedTokens[generatedTokens.length - 1] !== '\n') {
             // Only add if we didn't reach the total line count yet and last token wasn't already newline
              generatedTokens.push('\n');
         }


        // Join tokens into a string, replacing internal space tokens and newline tokens
        return generatedTokens.map(token => token === '\n' ? '\n' : token).join('').replace(/ \n/g, '\n').replace(/\n /g, '\n').trim();
    }


    // Visualize model state (simple: show top N transitions + summary)
    function updateVisualization() {
        const wordPairs = [];
        let totalConnections = 0;
        let uniqueWords = new Set();

        for (const word in model) {
             uniqueWords.add(word);
            const nextWords = model[word];
            const sortedNext = Object.entries(nextWords).sort(([, countA], [, countB]) => countB - countA);
            sortedNext.forEach(([nextWord, count]) => {
                 if (word.trim().length > 0 && nextWord.trim().length > 0) { // Only show word -> word transitions
                    wordPairs.push({ word, nextWord, count });
                    totalConnections++;
                 }
            });
        }

         // Sort all pairs by count descending
         wordPairs.sort((a, b) => b.count - a.count);

         let vizHtml = '<h3>הקשרים החזקים ביותר:</h3><ul>';
         const topN = 10; // Show top 10 connections
         if (wordPairs.length > 0) {
            wordPairs.slice(0, topN).forEach(pair => {
                vizHtml += `<li>"${pair.word}" → "${pair.nextWord}" <span>(${pair.count})</span></li>`;
            });
            vizHtml += '</ul>';
         } else {
             vizHtml = '<p>עוד אין מספיק דפוסים מעניינים ללמידה.</p>';
         }

        modelStateDiv.innerHTML = vizHtml;
        modelSummaryDiv.textContent = `מילים ייחודיות במודל: ${uniqueWords.size}, סך קשרים (Bigrams): ${totalConnections}`;

        // Add fade-in class briefly
        modelStateDiv.classList.add('fade-in');
        setTimeout(() => {
            modelStateDiv.classList.remove('fade-in');
        }, 500);
    }

    // Calculate simple metrics
    function calculateMetrics(generatedText, trainingText) {
        // Use the text from the textarea if generatedText is null (for initial load)
        const currentTrainingText = trainingDataTextarea.value;
        const currentGeneratedText = generatedPoetryDiv.textContent; // Use text actually displayed

        const trainingTokens = tokenize(currentTrainingText).filter(token => token.trim().length > 0 && token !== '\n');
        const generatedTokens = tokenize(currentGeneratedText).filter(token => token.trim().length > 0 && token !== '\n');

        if (trainingTokens.length === 0) {
            return "אין נתוני אימון לחישוב מדדים.";
        }
         if (generatedTokens.length === 0 || currentGeneratedText.trim() === generatedPoetryDiv.dataset.initialText) { // Check against initial message
             return "לא נוצרה שירה לחישוב מדדים.";
         }

        const trainingVocab = new Set(trainingTokens);

        let knownWordsCount = 0;
        generatedTokens.forEach(word => {
            if (trainingVocab.has(word)) {
                knownWordsCount++;
            }
        });

        const knownWordPercentage = generatedTokens.length > 0 ? ((knownWordsCount / generatedTokens.length) * 100).toFixed(1) : 0;


         const generatedLines = currentGeneratedText.split('\n').filter(line => line.trim().length > 0);
         const trainingLines = currentTrainingText.split('\n').filter(line => line.trim().length > 0);

         const avgGeneratedLineLength = generatedLines.length > 0
            ? (generatedLines.reduce((sum, line) => sum + line.split(/\s+/).filter(token => token.length > 0).length, 0) / generatedLines.length).toFixed(1)
            : 0;

         const avgTrainingLineLength = trainingLines.length > 0
            ? (trainingLines.reduce((sum, line) => sum + line.split(/\s+/).filter(token => token.length > 0).length, 0) / trainingLines.length).toFixed(1)
            : 0;


        let metrics = `
            <b>אוצר מילים:</b> ${knownWordPercentage}% מהמילים בשירה שנוצרה הופיעו בנתוני האימון.<br>
            <b>מבנה שורה:</b> אורך שורה ממוצע בשירה שנוצרה: ${avgGeneratedLineLength} מילים (לעומת ${avgTrainingLineLength} במקור).<br>
            <b>אורך יצירה:</b> ${generatedLines.length} שורות, ${generatedTokens.length} מילים.
        `;
        return metrics;
    }


    // --- Event Listeners ---

    loadPresetButton.addEventListener('click', () => {
        trainingDataTextarea.value = presetData.trim();
         // Reset model and epochs when loading new data to simulate starting fresh
         model = {};
         epochs = 0;
         trainingEpochsDiv.textContent = `עידני אימון: 0`;
         modelStateDiv.innerHTML = 'מודל ריק. טען נתונים ואמן.';
         modelSummaryDiv.textContent = '';
         generatedPoetryDiv.textContent = generatedPoetryDiv.dataset.initialText; // Reset generated text to initial prompt
         generatedPoetryDiv.classList.remove('fade-in');
         metricOutputDiv.innerHTML = 'עדיין אין נתונים לניתוח.';
         trainingStatusDiv.textContent = 'דוגמאות שירה נטענו!';
         trainingStatusDiv.classList.add('fade-in');
          setTimeout(() => {
             trainingStatusDiv.classList.remove('fade-in');
             trainingStatusDiv.textContent = '';
         }, 2000);

    });

    trainButton.addEventListener('click', async () => { // Made async for potential future animations
        if (isTraining) return; // Prevent multiple clicks

        const trainingText = trainingDataTextarea.value;
        if (!trainingText.trim()) {
            alert("הכנס טקסט לאימון המודל בבקשה.");
            return;
        }

        isTraining = true;
        trainButton.disabled = true;
        trainButton.textContent = 'מאמן...';
        trainingStatusDiv.textContent = 'המודל לומד את הקצב...';
         trainingStatusDiv.classList.add('fade-in');


        // Simulate training time (for visual effect)
        await new Promise(resolve => setTimeout(resolve, 500)); // Short delay


        trainModel(trainingText);
        trainingEpochsDiv.textContent = `עידני אימון: ${epochs}`;

        // Generate and display
        const generatedPoetry = generateText();
        generatedPoetryDiv.textContent = generatedPoetry;
         generatedPoetryDiv.classList.add('fade-in'); // Add fade-in class
         setTimeout(() => generatedPoetryDiv.classList.remove('fade-in'), 500);


        // Update visualization
        updateVisualization();

        // Calculate and display metrics
        const metrics = calculateMetrics(); // No need to pass text, functions read divs
        metricOutputDiv.innerHTML = metrics;
         metricOutputDiv.classList.add('fade-in');
         setTimeout(() => metricOutputDiv.classList.remove('fade-in'), 500);


        isTraining = false;
        trainButton.disabled = false;
        trainButton.textContent = 'אמן צעד אחד (עידן)';
         trainingStatusDiv.textContent = 'אימון הושלם! נוצרה יצירה חדשה.';
          setTimeout(() => {
             trainingStatusDiv.classList.remove('fade-in');
             trainingStatusDiv.textContent = '';
         }, 2000);
    });

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationSection.style.display === 'none';
        explanationSection.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'רוצה לדעת איך הקסם הזה קורה? (הסבר מעמיק)';
         if(isHidden) {
             explanationSection.classList.add('fade-in');
              setTimeout(() => explanationSection.classList.remove('fade-in'), 500);
         }
    });

    // Initial state display
     modelStateDiv.innerHTML = 'מודל ריק. טען נתונים ואמן.';
     generatedPoetryDiv.textContent = 'לחץ על \'אמן\' כדי שהמודל יתחיל ליצור...';
     // Store initial text for comparison in metrics
     generatedPoetryDiv.dataset.initialText = generatedPoetryDiv.textContent;
     metricOutputDiv.innerHTML = 'עדיין אין נתונים לניתוח.';

</script>
```