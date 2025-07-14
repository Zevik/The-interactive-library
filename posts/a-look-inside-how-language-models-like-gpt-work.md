---
title: "מבט מבפנים: הצצה קסומה למנוע של מודלי שפה גדולים (LLMs)"
english_slug: a-look-inside-how-language-models-like-gpt-work
category: "טכנולוגיה / מדעי המחשב"
tags: ["מודלי שפה", "בינה מלאכותית", "למידת מכונה", "טרנספורמרים", "GPT", "LLM", "עיבוד שפה טבעית"]
---
# מבט מבפנים: הצצה קסומה למנוע של מודלי שפה גדולים (LLMs)

איך קורה הקסם? איך ייתכן שמכונה מסוגלת ליצור טקסט שמרגיש חי, יצירתי, ולעיתים אפילו מפתיע, כאילו נכתב על ידי בן אנוש? מה בעצם מתרחש 'בתוך' המודל ברגע שהוא מגיב לפקודה או לשאלה שלכם? הצטרפו אלינו למסע קצר אל לב הפעולה של מודלי שפה מתקדמים כמו GPT.

<div id="app-container">
    <h2>הסימולציה האינטראקטיבית: לב העניין</h2>
    <p>הזינו טקסט התחלתי קצר (משפט או שניים). צפו איך המודל 'מנחש' את המילה הבאה, ואיך הוא 'מקשיב' למילים הקודמות כדי לעשות זאת.</p>
    <textarea id="inputText" rows="2" placeholder="דוגמה: החתול ישב על ה..."></textarea>
    <button id="predictButton">חזה והצג את המילה הבאה</button>
    <div id="simulation-area">
        <div id="currentTextDisplay">
            <h3>הטקסט המתהווה:</h3>
            <div class="text-display-content"></div>
        </div>
        <div id="attentionViz">
            <h3>ההתמקדות העיקרית של המודל (מנגנון הקשב):</h3>
            <div class="attention-display-content">התמקדות המודל במילים קודמות תוצג כאן ויזואלית לאחר החיזוי.</div>
        </div>
    </div>
</div>

<button id="toggleExplanation">רוצים להבין את הקסם? לחצו להסבר המלא</button>

<div id="explanation" style="display: none;">
    <h2>מאחורי הקלעים: מסע אל תוך מודלי השפה הגדולים (LLMs)</h2>

    <h3>היסטוריה קצרה: ממודלים סטטיסטיים ל-RNNs</h3>
    תחילת הדרך במודלי שפה הייתה צנועה, מבוססת על סטטיסטיקה פשוטה. הם חישבו הסתברויות - מה הסיכוי שמילה מסוימת תופיע אחרי מילה או שתיים קודמות (N-grams). שיטות אלו היו מוגבלות ביותר בהבנת הקשר מורכב או ארוך טווח. הדור הבא, רשתות נוירונים רקורנטיות (RNNs) ומודלי LSTM, שיפר משמעותית את היכולת להתמודד עם רצפים ולזכור מידע מקדים, אך הן עדיין התקשו בלמידת תלויות ארוכות מאוד וסבלו מקשיי אימון.

    <h3>המהפכה הגדולה: ארכיטקטורת הטרנספורמר ומנגנון ה'קשב'</h3>
    נקודת המפנה הדרמטית הגיעה עם הצגת ארכיטקטורת הטרנספורמר במאמר פורץ דרך ב-2017. הטרנספורמר זנח את העיבוד הסדרתי האיטי לטובת עיבוד מקבילי של רצף שלם בו-זמנית. ליבו הפועם הוא מנגנון ה'קשב' (Attention). במקום להישען רק על המילה האחרונה או על זיכרון קצר מוגבל, הטרנספורמר מאפשר לכל מילה ברצף לשקלל את הרלוונטיות של *כל* המילים האחרות ברצף בעת חישוב הייצוג שלה או חיזוי המילה הבאה. **הסימולציה שראיתם למעלה ממחישה בדיוק את המנגנון הזה - איך המודל 'מקשיב' למילים הקודמות כדי לבחור את המילה הבאה.**

    <h3>מבנה בסיסי: אנקודר, דיקודר, ו-LLMs</h3>
    הטרנספורמר המקורי כולל אנקודר (Encoder) לעיבוד הקלט ודיקודר (Decoder) ליצירת הפלט. מודלים יוצרי טקסט כמו GPT (שם שמבטא את היותם Generative Pre-trained Transformer) מבוססים בעיקר על וריאציות של חלק הדיקודר, המותאמות במיוחד למשימת חיזוי הטקסט הבא ברצף.

    <h3>ה'קשב העצמי' (Self-Attention): כוח ההקשר</h3>
    הקשב העצמי הוא הגאונות מאחורי הטרנספורמר. הוא מאפשר למודל ליצור חיבורים ושיוכי משמעות בין מילים, ללא קשר למרחק הפיזי ביניהן ברצף. לדוגמה, במשפט "הבנק ליד הנהר עלה על גדותיו", מנגנון הקשב העצמי מאפשר למודל לקשר את המילה "בנק" ל"נהר" ולהבין את המשמעות הנכונה, בניגוד למשפט "הבנק נתן הלוואה" שבו "בנק" קשורה למשמעות פיננסית. המודל מחשב ציוני קשב בין כל זוג מילים, ומשתמש בציונים אלו כדי 'לערבב' מידע מכל המילים באופן חכם ודינמי.

    <h3>תהליך יצירת הטקסט: צעד אחר צעד</h3>
    יצירת טקסט במודל כמו GPT היא תהליך איטרטיבי:
    1.  המודל מקבל טקסט התחלתי (ה-Prompt).
    2.  הוא מעבד את הטקסט הקיים (כפי שהוצג בסימולציה).
    3.  שכבת הפלט מחשבת הסתברויות לכל האסימונים (Tokens - מילה או חלק ממנה) האפשריים באוצר המילים שלו, להיות האסימון הבא.
    4.  נבחר האסימון הבא (לרוב זה בעל ההסתברות הגבוהה ביותר, אך לעיתים נבחר אסימון בהתאם להסתברותו ליצירת גיוון).
    5.  האסימון שנבחר מתווסף לטקסט הקיים.
    6.  חוזרים לשלב 2, כשהפעם הטקסט כולל גם את האסימון החדש, וכך נבנה הטקסט צעד אחר צעד.

    <h3>למידה בקנה מידה עצום: סוד היכולות</h3>
    מודלים כמו GPT מאומנים על כמויות מידע טקסטואלי אדירות מכל רחבי האינטרנט והספרות. תהליך האימון הוא למעשה אופטימיזציה של מיליארדי פרמטרים, שבה המודל לומד לחזות את האסימון הבא שוב ושוב. תהליך זה מקנה לו ידע עצום על השפה, על העולם, על סגנונות, ואף יכולות הסקה והיגיון מסוימות, הנובעות לאו דוך מכוח הדפוסים בנתוני האימון.

    <h3>מודלים מוכרים ומגבלות</h3>
    GPT הוא המפורסם ביותר, אך ישנם מודלים רבים נוספים מבוססי טרנספורמר (BERT, T5, LLaMA ועוד). למרות יכולותיהם המרשימות, הם אינם מושלמים: הם עלולים 'להזות' (לייצר מידע שגוי), לשקף הטיות מנתוני האימון, ולהתקשות בהבנה עמוקה אמיתית של העולם או סיבתיות. הם גם דורשים כוח חישוב עצום.

    <p>הסימולציה שראיתם מספקת הצצה פשטנית אך אינטואיטיבית לאחד המנגנונים המרכזיים שמאפשרים למודלים הללו ליצור טקסט - מנגנון הקשב, המאפשר להם 'להתמקד' בחלקים רלוונטיים של הטקסט הקודם בעת יצירת המילה הבאה.</p>
</div>

<style>
    /* הגדרות בסיסיות וגופנים */
    #app-container, #explanation, #toggleExplanation {
        font-family: 'Arial', sans-serif; /* גופן נעים יותר */
        direction: rtl;
        text-align: right;
        max-width: 750px; /* רוחב מרבי מעט גדול יותר */
        margin: 20px auto;
        padding: 25px; /* ריפוד גדול יותר */
        background-color: #ffffff; /* רקע לבן נקי */
        border-radius: 12px; /* פינות עגולות יותר */
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* צל עדין */
        line-height: 1.7; /* מרווח שורות נעים */
    }

    /* כותרות */
    #app-container h2, #explanation h2 {
        color: #004080; /* כחול כהה יותר */
        text-align: center; /* כותרות במרכז */
        margin-bottom: 20px;
        font-size: 1.8em; /* גודל כותרת ראשית */
    }

    #app-container h3, #explanation h3 {
        color: #0056b3; /* כחול מעט בהיר יותר */
        margin-top: 15px;
        margin-bottom: 8px;
        font-size: 1.3em; /* גודל כותרת משנית */
        border-bottom: 1px solid #e0e0e0; /* קו תחתון עדין */
        padding-bottom: 5px;
    }

    /* אזור קלט טקסט */
    #inputText {
        width: 100%;
        padding: 12px;
        margin-bottom: 15px;
        border: 1px solid #cce5ff; /* גבול כחלחל עדין */
        border-radius: 8px;
        box-sizing: border-box;
        font-size: 1rem;
        direction: rtl;
        text-align: right;
        transition: border-color 0.3s ease;
        resize: vertical; /* אפשר שינוי גודל אנכי */
    }

    #inputText:focus {
        border-color: #007bff; /* גבול כחול בהיר בפוקוס */
        outline: none;
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.25); /* צל עדין בפוקוס */
    }

    /* כפתורים */
    #predictButton, #toggleExplanation {
        display: block;
        width: 100%;
        padding: 12px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.1rem; /* גודל גופן גדול יותר */
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease; /* אנימציית מעבר וקליק */
        text-align: center; /* יישור טקסט במרכז הכפתור */
    }

    #predictButton {
        background-color: #007bff; /* כחול ראשי */
        color: white;
        margin-bottom: 20px;
    }

    #predictButton:hover {
        background-color: #0056b3; /* כחול כהה יותר במעבר עכבר */
    }
     #predictButton:active {
        transform: scale(0.98); /* אפקט קליק */
    }

    #toggleExplanation {
        background-color: #6c757d; /* אפור */
        color: white;
        margin-top: 30px; /* מרווח גדול יותר אחרי הסימולציה */
         max-width: 750px;
        margin-left: auto;
        margin-right: auto;
    }

    #toggleExplanation:hover {
        background-color: #5a6268; /* אפור כהה יותר במעבר עכבר */
    }
    #toggleExplanation:active {
        transform: scale(0.98); /* אפקט קליק */
    }

    /* אזורי תצוגה של הסימולציה */
    #simulation-area {
        background-color: #e9ecef; /* רקע אפרפר בהיר לסימולציה */
        padding: 20px;
        border-radius: 8px;
    }

    #currentTextDisplay, #attentionViz {
        margin-top: 15px;
        padding: 15px;
        border: 1px solid #cce5ff; /* גבול עדין */
        border-radius: 8px;
        background-color: #fff; /* רקע לבן לתוכן התצוגה */
        min-height: 60px; /* גובה מינימלי */
        overflow-wrap: break-word; /* שבירת מילים ארוכות */
    }

    #currentTextDisplay .text-display-content {
        min-height: 30px; /* גובה מינימלי לתוכן */
    }

    #currentTextDisplay span.word {
        margin-left: 5px; /* מרווח בין מילים */
        padding: 2px 0; /* ריפוד עדין */
        transition: background-color 0.5s ease, color 0.5s ease; /* אנימציית מעבר להדגשה */
        position: relative; /* למיקום עתידי של קווים או אפקטים */
         display: inline-block; /* כדי ש-padding יעבוד */
    }

    /* אנימציית הופעה של מילה חדשה */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(5px); }
        to { opacity: 1; transform: translateY(0); }
    }
     #currentTextDisplay span.word.new-word {
        animation: fadeIn 0.5s ease forwards; /* החלה האנימציה על מילה חדשה */
     }


    #attentionViz .attention-display-content {
        min-height: 30px;
        color: #666;
        font-style: italic;
    }

     /* הדגשת קשב - מיושמת על מילים בתוך currentTextDisplay */
     /* רמות 0-5, כשהדגשה חזקה יותר מסמלת קשב רב יותר מהמילה החדשה למילה המודגשת */
     .attention-highlight-0 { background-color: transparent; color: inherit; font-weight: normal;} /* אין קשב משמעותי */
     .attention-highlight-1 { background-color: rgba(255, 230, 150, 0.3); } /* קשב נמוך */
     .attention-highlight-2 { background-color: rgba(255, 210, 100, 0.5); } /* קשב בינוני-נמוך */
     .attention-highlight-3 { background-color: rgba(255, 190, 50, 0.7); } /* קשב בינוני */
     .attention-highlight-4 { background-color: rgba(255, 160, 0, 0.9); } /* קשב בינוני-גבוה */
     .attention-highlight-5 { background-color: rgba(255, 140, 0, 1.0); font-weight: bold; } /* קשב גבוה - הדגשה חזקה */


    /* הסבר מעמיק */
    #explanation {
        margin-top: 20px;
        padding: 25px;
        background-color: #eef7ff; /* רקע תכלת בהיר להסבר */
        border: 1px solid #cce5ff; /* גבול כחלחל */
        border-radius: 12px;
        line-height: 1.7;
        direction: rtl;
        text-align: right;
         box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); /* צל עדין גם להסבר */
    }

    #explanation p {
        margin-bottom: 15px;
         color: #333; /* צבע טקסט כהה */
    }

     #explanation strong {
         color: #0056b3; /* הדגשת מונחים חשובים */
     }

    /* הסתרת הסבר */
    #explanation[style*="display: none"] {
        /* שומר על האפשרות להוסיף אנימציית פתיחה/סגירה עתידית */
        /* כרגע רק מסתיר */
    }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const inputText = document.getElementById('inputText');
        const predictButton = document.getElementById('predictButton');
        const currentTextDisplayContent = document.querySelector('#currentTextDisplay .text-display-content');
        const attentionDisplayContent = document.querySelector('#attentionViz .attention-display-content');
        const toggleExplanationButton = document.getElementById('toggleExplanation');
        const explanationDiv = document.getElementById('explanation');

        // --- Simple Simulation Data (Enhanced) ---
        // This object maps the *end* of the current text sequence
        // to a predicted next word and attention scores *from that new word*
        // back to words in the previous sequence.
        const predictionRules = {
            "הכלב רדף אחרי": { word: "החתול", attention_to_previous: { "הכלב": 0.6, "רדף": 0.8, "אחרי": 0.7 } },
            "החתול ישב על ה": { word: "שטיח", attention_to_previous: { "החתול": 0.7, "ישב": 0.8, "על": 0.5, "ה": 0.3 } },
            "השמיים היו": { word: "כחולים", attention_to_previous: { "השמיים": 0.9, "היו": 0.6 } },
            "הספר הזה מאוד": { word: "מעניין", attention_to_previous: { "הספר": 0.7, "הזה": 0.5, "מאוד": 0.9 } },
            "אכלתי תפוח": { word: "מתוק", attention_to_previous: { "אכלתי": 0.4, "תפוח": 0.9 } },
            "נסענו ל": { word: "תל אביב", attention_to_previous: { "נסענו": 0.7, "ל": 0.6 } },
             "על ה": { word: "שולחן", attention_to_previous: { "על": 0.7, "ה": 0.5 } },
            // Fallback/default rules (less specific context)
             "אחרי ה": { word: "עכבר", attention_to_previous: { "אחרי": 0.8, "ה": 0.4 } },
             "מאוד": { word: "טעים", attention_to_previous: { "מאוד": 0.9 } },
             "ה": { word: "בית", attention_to_previous: { "ה": 0.8 } },
            "default": { word: "...", attention_to_previous: {} } // Generic fallback
        };

        // Function to tokenize text into words
        function tokenize(text) {
            // Simple split by spaces and punctuation, filter empty strings
             return text.trim().split(/[\s,.;:!?()"]+/).filter(word => word);
        }

         // Function to get the last N tokens as a string for lookup
         function getLastTokensAsString(text, count = 3) {
             const tokens = tokenize(text);
             if (tokens.length === 0) return "";
             // Get last 'count' tokens and join with spaces (matching rule keys)
             return tokens.slice(Math.max(0, tokens.length - count)).join(' ');
         }

         // Function to find the best matching rule
         function findMatchingRule(currentText) {
             let bestMatch = null;
             let maxMatchLength = 0;

             // Iterate through rules, trying to match longest suffix first
             for (const key in predictionRules) {
                 if (key !== "default") {
                     // Ensure key is a string and normalize spaces
                     const normalizedKey = key.trim().replace(/\s+/g, ' ');
                     // Check if currentText ends with the key
                     if (currentText.trim().endsWith(normalizedKey)) {
                          if (normalizedKey.length > maxMatchLength) {
                              maxMatchLength = normalizedKey.length;
                              bestMatch = predictionRules[key];
                          }
                     }
                 }
             }
              // If no specific rule matched, use default
             return bestMatch || predictionRules.default;
         }


        function predictNextWord() {
            let currentDisplayText = currentTextDisplayContent.textContent.trim();
            const initialInputText = inputText.value.trim();

            // First click logic: Move initial input to display
            if (!currentDisplayText && initialInputText) {
                 const tokens = tokenize(initialInputText);
                 currentTextDisplayContent.innerHTML = tokens.map(word => `<span class="word">${word}</span>`).join(' ');
                 inputText.value = ""; // Clear input after use
                 attentionDisplayContent.textContent = 'לחצו שוב כדי לראות את המודל חוזה את המילה הבאה.';
                 return; // Stop here, wait for next click to predict
            }

            // Prevent prediction if display is empty and input is empty
            if (!currentDisplayText && !initialInputText) {
                 attentionDisplayContent.textContent = 'אנא הזינו טקסט התחלתי קודם.';
                 return;
            }

             // If display has text, proceed with prediction
             const rule = findMatchingRule(currentDisplayText);

            const predictedWord = rule.word;
            const attentionScores = rule.attention_to_previous || {}; // Ensure it's an object

            // Remove any previous attention highlights
             currentTextDisplayContent.querySelectorAll('span.word').forEach(span => {
                 span.className = 'word'; // Reset classes
             });


            // Append the new word to the display with animation class
             const newWordSpan = document.createElement('span');
             newWordSpan.classList.add('word', 'new-word'); // Add animation class
             newWordSpan.textContent = predictedWord;
             currentTextDisplayContent.appendChild(newWordSpan);

            // Trigger reflow to restart animation
             void newWordSpan.offsetWidth;
             newWordSpan.classList.remove('new-word');


            // Visualize attention *from the new word* back to the *previous* words
            visualizeAttention(attentionScores, currentTextDisplayContent.querySelectorAll('span.word:not(:last-child)')); // Highlight previous words

            // Scroll to the end
            currentTextDisplayContent.parentElement.scrollTop = currentTextDisplayContent.parentElement.scrollHeight;
        }

        function visualizeAttention(attentionScores, previousWordSpans) {
             attentionDisplayContent.innerHTML = ''; // Clear previous visualization

            if (Object.keys(attentionScores).length === 0 || previousWordSpans.length === 0) {
                attentionDisplayContent.textContent = 'אין נתוני קשב ספציפי לסימולציה זו או שאין מילים קודמות להתמקד בהן.';
                attentionDisplayContent.style.color = '#666';
                attentionDisplayContent.style.fontStyle = 'italic';
                return;
            }

            const attendedWords = [];

            previousWordSpans.forEach(span => {
                 const wordText = span.textContent.trim(); // Use trimmed text for lookup
                 let score = attentionScores[wordText];

                 if (score !== undefined) {
                      // Determine highlight level (0-5) based on score (0-1)
                      const highlightLevel = Math.min(5, Math.max(0, Math.round(score * 5))); // Ensure level is 0-5
                      if (highlightLevel > 0) { // Only highlight if there's *some* attention
                           span.classList.add(`attention-highlight-${highlightLevel}`);
                            // Add word to list for text explanation
                           if (highlightLevel >= 3) { // Consider words with medium to high attention as 'focused on'
                                attendedWords.push(`<span class="attention-highlight-${highlightLevel}">${wordText}</span>`);
                           }
                      }
                 }
                 // Words not in attentionScores map or with score 0 get class 0 (no visual highlight)
                  if (score === undefined || score === 0) {
                      span.classList.add('attention-highlight-0');
                  }
            });

            // Update the textual explanation
            if (attendedWords.length > 0) {
                 attentionDisplayContent.innerHTML = `המודל התמקד בעיקר במילים: ${attendedWords.join(', ')}.`;
                 attentionDisplayContent.style.color = '#333';
                 attentionDisplayContent.style.fontStyle = 'normal';
             } else {
                  attentionDisplayContent.textContent = 'המודל פיזר את הקשב באופן אחיד או התמקד במשהו אחר בסימולציה מורכבת יותר.';
                  attentionDisplayContent.style.color = '#666';
                  attentionDisplayContent.style.fontStyle = 'italic';
             }
        }


        predictButton.addEventListener('click', predictNextWord);

        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            // Use a smoother toggle effect if desired, for now just display none/block
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'רוצים להבין את הקסם? לחצו להסבר המלא';
        });

         // Initial state setup
        attentionDisplayContent.textContent = 'הזינו טקסט למעלה ולחצו על הכפתור.';
        attentionDisplayContent.style.color = '#666';
        attentionDisplayContent.style.fontStyle = 'italic';


    });
</script>
```