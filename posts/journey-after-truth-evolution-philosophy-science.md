---
title: "מסע אחר האמת: התפתחות הפילוסופיה של המדע"
english_slug: journey-after-truth-evolution-philosophy-science
category: "מדעי הרוח / פילוסופיה"
tags: [פילוסופיה של המדע, שיטה מדעית, קרל פופר, תומאס קון, היסטוריה של המדע]
---
<h1>מסע אחר האמת: התפתחות הפילוסופיה של המדע</h1>
<p>איך אנו יודעים שמשהו במדע נכון? האם תיאוריה מדעית 'מוכחת' לעולם? האם המדע מתקדם בקו ישר של גילויים, או אולי עובר מהפכות דרמטיות שמשנות את כללי המשחק?</p>
<p>צא למסע מרתק דרך עידנים שונים של המחשבה המדעית וחווה בעצמך את התמורות הגדולות בהבנת טבעו של הידע המדעי!</p>

<div id="science-journey-app">
    <div id="stage-indicator" class="stage-indicator"></div>
    <div id="simulation-output" class="simulation-output"></div>
    <div id="user-input" class="user-input">
        <textarea id="input-text" placeholder="הצע תיאוריה או תחזית..."></textarea>
        <button id="input-button"></button>
    </div>
    <div id="action-buttons" class="action-buttons">
        <button id="start-button">התחל את המסע המדעי שלך</button>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700&display=swap');

    #science-journey-app {
        direction: rtl;
        font-family: 'Heebo', sans-serif;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        padding: 25px;
        margin: 25px 0;
        border-radius: 12px;
        background-color: #ffffff;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
        position: relative;
        overflow: hidden; /* For potential future background animations */
    }

     #science-journey-app::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 6px;
        background: linear-gradient(to right, #007bff, #28a745, #ffc107);
        border-top-left-radius: 12px;
        border-top-right-radius: 12px;
     }

    .stage-indicator {
        font-size: 1.3em;
        font-weight: 700;
        margin-bottom: 20px;
        color: #0056b3;
        text-align: center;
        padding-bottom: 10px;
        border-bottom: 1px solid #eee;
        animation: fadeInDown 0.5s ease-out;
    }

    .simulation-output {
        min-height: 120px;
        border: 1px solid #d0d0d0;
        padding: 20px;
        margin-bottom: 20px;
        background-color: #f8f9fa;
        border-radius: 8px;
        line-height: 1.7;
        white-space: pre-wrap;
        word-wrap: break-word;
        overflow-wrap: break-word;
        font-size: 1.05em;
        color: #333;
        position: relative;
        animation: fadeIn 0.8s ease-out;
    }

     .simulation-output strong {
         color: #0056b3;
     }

     .simulation-output .analysis {
         display: block;
         margin-top: 15px;
         padding-top: 15px;
         border-top: 1px dashed #ccc;
         font-size: 0.95em;
         color: #555;
     }

      .simulation-output .success {
          color: #28a745;
          font-weight: bold;
      }
       .simulation-output .failure {
          color: #dc3545;
          font-weight: bold;
       }
       .simulation-output .anomaly {
           color: #ffc107;
           font-weight: bold;
       }
        .simulation-output .crisis {
            color: #dc3545;
            font-weight: bold;
            font-size: 1.1em;
        }
         .simulation-output .revolution {
             color: #007bff;
             font-weight: bold;
             font-size: 1.2em;
         }


    .user-input {
        margin-bottom: 20px;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    #input-text {
        width: 100%; /* Adjusted to fit container */
        padding: 12px;
        border: 1px solid #ccc;
        border-radius: 6px;
        font-size: 1em;
        font-family: 'Heebo', sans-serif;
        box-sizing: border-box; /* Include padding in element's total width */
        transition: border-color 0.3s ease;
    }

    #input-text:focus {
        border-color: #007bff;
        outline: none;
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.25);
    }

    .action-buttons button,
    #input-button {
        padding: 12px 20px;
        margin: 5px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1em;
        font-family: 'Heebo', sans-serif;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: 500;
    }

    .action-buttons button:hover,
    #input-button:hover {
        opacity: 0.95;
        transform: translateY(-1px);
    }
     .action-buttons button:active,
    #input-button:active {
        transform: translateY(0);
    }


    #start-button {
         background-color: #007bff;
         color: white;
         width: 100%; /* Make start button wider */
         font-size: 1.1em;
         padding: 15px;
    }

     #input-button {
         background-color: #28a745;
         color: white;
         align-self: flex-end; /* Position button to the right */
     }

     .action-buttons {
         display: flex;
         flex-wrap: wrap;
         gap: 10px;
         justify-content: center; /* Center action buttons */
     }

     .action-buttons button {
         background-color: #007bff;
         color: white;
     }

     .action-buttons button.neutral {
        background-color: #6c757d;
        color: white;
     }
      .action-buttons button.negative {
        background-color: #dc3545;
        color: white;
     }
       .action-buttons button.secondary {
        background-color: #ffc107;
        color: #212529;
     }


    #explanation-toggle-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        background-color: #6c757d; /* Neutral color for explanation */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1em;
        font-family: 'Heebo', sans-serif;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: 500;
    }
    #explanation-toggle-button:hover {
        background-color: #5a6268;
         transform: translateY(-1px);
    }
    #explanation-toggle-button:active {
        transform: translateY(0);
    }

    #full-explanation {
        display: none;
        margin-top: 20px;
        padding: 25px;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        background-color: #fefefe;
        line-height: 1.8;
        font-family: 'Heebo', sans-serif;
        color: #333;
    }
     #full-explanation h2 {
        color: #0056b3;
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 2px solid #eee;
        padding-bottom: 5px;
        font-weight: 700;
     }
      #full-explanation p {
          margin-bottom: 15px;
      }


    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
     @keyframes fadeInDown {
         from { opacity: 0; transform: translateY(-10px); }
         to { opacity: 1; transform: translateY(0); }
     }
     @keyframes slideInUp {
         from { opacity: 0; transform: translateY(10px); }
         to { opacity: 1; transform: translateY(0); }
     }

    .simulation-output.fade-in {
        animation: fadeIn 0.5s ease-out;
    }
     .action-buttons button.slide-in {
         animation: slideInUp 0.3s ease-out;
     }


     /* Responsive adjustments */
     @media (max-width: 600px) {
         #science-journey-app {
             padding: 15px;
             margin: 15px 5px;
         }
          .stage-indicator {
              font-size: 1.1em;
          }
         .simulation-output, #full-explanation {
             padding: 15px;
         }
         .action-buttons {
             flex-direction: column;
             gap: 8px;
         }
         .action-buttons button, #start-button, #input-button {
             width: calc(100% - 10px); /* Adjust for margin/gap */
             margin: 0;
         }
         #input-button {
              align-self: stretch; /* Full width on small screens */
         }

     }


</style>

<button id="explanation-toggle-button">הצג הסבר מורחב</button>

<div id="full-explanation">
    <h2>מהי פילוסופיה של המדע?</h2>
    <p>פילוסופיה של המדע היא ענף בפילוסופיה החוקר את היסודות, השיטות וההשלכות של המדע. היא בוחנת שאלות עמוקות כמו: מה מבדיל ידע מדעי מידע שאינו מדעי? מהי שיטת המחקר המדעית המיטבית? האם המדע מגלה את האמת המוחלטת או רק מודלים יעילים לתיאור העולם? וכיצד המדע מתפתח לאורך ההיסטוריה?</p>

    <h2>המודל האריסטוטלי</h2>
    <p>בעת העתיקה, המדע הושפע רבות מפילוסופים כמו אריסטו. המודל האריסטוטלי התבסס על התבוננות ועל הנחות יסוד שהתקבלו כעקרונות ראשוניים, מהם הסיקו מסקנות באמצעות דדוקציה. ההסברים לתופעות טבעיות התבססו לעיתים קרובות על טלאולוגיה (הסבר באמצעות תכלית או מטרה) ועל מהויות פנימיות של הדברים. לדוגמה, אבן נופלת ארצה כי "טבעה" לשאוף למרכז היקום (כדור הארץ). גישה זו הדגישה היגיון ותצפית, אך ללא דגש על ניסוי שיטתי ומבוקר שמטרתו לבחון באופן אקטיבי הנחות יסוד.</p>

    <h2>עליית האמפיריציזם והאינדוקציה</h2>
    <p>בתקופת המהפכה המדעית, הוגים כמו פרנסיס בייקון הדגישו את חשיבות התצפית והניסוי כבסיס לידע מדעי (אמפיריציזם). השיטה האינדוקטיבית הפכה למרכזית: איסוף מספר רב של תצפיות פרטיות על מנת לגזור מהן כלל או חוק כללי. לדוגמה, לאחר צפייה בברבור לבן, ברבור נוסף לבן, וכן הלאה, ניתן להגיע לכלל האינדוקטיבי "כל הברבורים לבנים". שיטה זו קידמה מאוד את איסוף הנתונים ואת ניסוח חוקי טבע כלליים מתוך נתונים אלו.</p>

    <h2>בעיית האינדוקציה (יוּם)</h2>
    <p>הפילוסוף הסקוטי דיוויד יום הציג במאה ה-18 את בעיית האינדוקציה המהותית. הוא טען כי אין בסיס לוגי מוצק להנחה שהעתיד יתנהג כמו העבר, או שכלל שנצפה במספר סופי של מקרים יחול על כל המקרים האפשריים (כולל אלה שטרם נצפו). גם אם ראינו אלף ברבורים לבנים, אין בכך הוכחה מוחלטת שכל הברבורים בעולם לבנים. בעיה זו מערערת על היכולת "להוכיח" חוקי טבע באופן מוחלט באמצעות אינדוקציה בלבד.</p>

    <h2>קרל פופר והפַלְסִיפִיקַצְיָה (הפרכה)</h2>
    <p>כתגובה לבעיית האינדוקציה, הציע הפילוסוף קרל פופר קריטריון אחר להבחנה בין מדע למדע שאינו מדע (פסאודו-מדע): עקרון ההפרכה (פַלְסִיפִיקַצְיָה). לפי פופר, תיאוריה מדעית אינה כזו משום שניתן לאשש אותה, אלא משום שניתן באופן עקרוני להפריך אותה באמצעות ניסוי או תצפית. מדענים צריכים לנסח תיאוריות נועזות ולנסות באופן אקטיבי למצוא להן עדויות סותרות. ככל שתיאוריה עומדת בהצלחה בפני ניסיונות הפרכה רבים וקפדניים, כך היא נחשבת למחוזקת (קורובורציה), אך לעולם אינה נחשבת ל"מוכחת" סופית. המדע מתקדם, לשיטתו, לא על ידי צבירת אישושים, אלא על ידי אלימינציה של תיאוריות שגויות.</p>

    <h2>תומאס קון והמהפכות המדעיות</h2>
    <p>ההיסטוריון והפילוסוף של המדע תומאס קון הציג פרספקטיבה שונה בספרו "המבנה של מהפכות מדעיות". הוא טען שהתפתחות המדע אינה תהליך לינארי של הפרכה ובנייה רציונלית בלבד, אלא כוללת תקופות ארוכות של 'מדע נורמלי' ותקופות קצרות של 'מהפכה מדעית'. 'מדע נורמלי' מתרחש בתוך 'פרדיגמה' קיימת – מסגרת מושגית רחבה הכוללת תיאוריות מקובלות, שיטות מחקר, ואפילו ערכים. מדענים בתקופת מדע נורמלי עוסקים בפתרון 'חידות' בתוך הפרדיגמה. כאשר מצטברות 'אנומליות' (תופעות שלא ניתנות להסבר מספק במסגרת הפרדיגמה הקיימת), נוצר 'משבר'. משבר זה עשוי להוביל ל'מהפכה מדעית' – שינוי דרמטי ורדיקלי שבו פרדיגמה חדשה מחליפה את הישנה. קון טען שלעיתים קשה להשוות באופן אובייקטיבי בין פרדיגמות שונות (חוסר מדידות - incommensurability), וכי שינוי פרדיגמה מושפע גם מגורמים סוציולוגיים ופסיכולוגיים, לא רק רציונליים גרידא.</p>

    <h2>השוואה בין פופר לקון</h2>
    <p>פופר וקון מציעים שתי תמונות שונות, אך לעיתים משלימות, של האופן שבו המדע מתקדם. פופר מתמקד בהיגיון המדעי ובקריטריון ההפרכה ככלי רציונלי לביקורת ולהתקדמות. קון מתמקד במבנה ההיסטורי-סוציולוגי של הקהילה המדעית ובהשפעת הפרדיגמות והמהפכות על התפתחות הידע. בעוד שפופר רואה במדע תהליך מתמיד של ביקורת והפרכה, קון רואה תקופות ארוכות של מדע שמרני יחסית בתוך פרדיגמה, המופרעות על ידי שינויים דרמטיים ולאו דווקא רציונליים לחלוטין. הדיון ביניהם ובין פילוסופים אחרים של המדע ממשיך לעצב את הבנתנו לגבי טבעו של הידע המדעי.</p>

    <h2>השפעתם על הבנתנו את המדע</h2>
    <p>רעיונותיהם של פופר וקון, לצד הוגים נוספים, הדגימו שהמדע אינו מאגר סטטי של 'אמיתות מוכחות'. הוא תהליך דינמי, ביקורתי, וחשוף לשינויים. הבנה זו מסייעת להבין מדוע תיאוריות מדעיות מתעדכנות או נדחות, ומדוע לעיתים קיימים ויכוחים עמוקים בתוך הקהילה המדעית. היא מעודדת גישה ביקורתית לידע מדעי, תוך הכרה בכוחה של השיטה המדעית וגם במגבלותיה.</p>
</div>


<script>
    const app = document.getElementById('science-journey-app');
    const stageIndicator = document.getElementById('stage-indicator');
    const simulationOutput = document.getElementById('simulation-output');
    const inputText = document.getElementById('input-text');
    const inputButton = document.getElementById('input-button');
    const actionButtonsDiv = document.getElementById('action-buttons');
    const startButton = document.getElementById('start-button');
    const explanationButton = document.getElementById('explanation-toggle-button');
    const explanationDiv = document.getElementById('full-explanation');

    let currentStageIndex = -1; // -1 means before start, 0-3 are the stages

    const stages = [
        {
            name: "השלב האריסטוטלי: טבע הדברים והיגיון",
            description: "אתה חוקר בעולם העתיק, שואב השראה מאריסטו. עבודתך מתבססת על התבוננות ישירה והסקה לוגית מתוך הנחות מקובלות. נסה להסביר את העולם סביבך.",
            setup: function() {
                updateOutput("אתה צופה באבן שנפלה מעץ. היא נעה מטה, אל עבר האדמה. למה לדעתך זה קרה? הצע הסבר על בסיס 'הטבע הפנימי' של האבן או היגיון פשוט.", 'normal');
                showInput("הצע הסבר אריסטוטלי (למשל, על בסיס טבעה)", "שלח הסבר", (input) => {
                    if (input.trim().length > 10) {
                        updateOutput(simulationOutput.textContent + `\n\nהסברך: "${input.trim()}"\n\n<span class="analysis">ניתוח הסימולציה: הסבר זה מתבסס על הנחות יסוד או 'מהויות' של אובייקטים. הוא קוהרנטי במסגרת המחשבה העתיקה ונראה הגיוני מתוך ההתבוננות, אך אינו נבדק באופן שניתן למדוד או לכמת בקלות. ברוך הבא לעולם שבו היגיון ופילוסופיה הם הכלים המדעיים העיקריים.</span>`);
                        hideInput();
                        showActionButton("המשך אל עידן התצפיות והאינדוקציה", () => moveToNextStage());
                    } else {
                        updateOutput(simulationOutput.textContent + "\n\n<span class='analysis failure'>אנא הצע הסבר ארוך ומפורט יותר שמתאר את הסיבה לנפילת האבן מנקודת מבט עתיקה.</span>", 'failure');
                    }
                });
                 inputText.placeholder = "הצע הסבר אריסטוטלי (למשל, האבן שואפת למקומה הטבעי)";
                 inputButton.textContent = "שלח הסבר";
            }
        },
        {
            name: "השלב האינדוקטיבי: מצבירת תצפיות לחוקים",
            description: "עברנו למהפכה המדעית! הניסוי והתצפית הם המפתח. צבור נתונים על תופעה מסוימת ונסה להסיק מהם כלל כללי.",
            observations: ["ברבור לבן", "ברבור לבן", "ברבור לבן", "ברבור שחור", "ברבור לבן", "ברבור לבן"], // Sample observations
            currentObsIndex: 0,
            ruleSuggested: false,
            setup: function() {
                this.currentObsIndex = 0;
                this.ruleSuggested = false;
                updateOutput("אתה חוקר בעולם החדש, חמוש בכלים אמפיריים. אתה מתבונן בברבורים באגם.\n<span class='observation'>צפית כעת ב: ברבור לבן.</span>", 'normal');
                showActionButton("בצע תצפית נוספת", () => this.addObservation());
                // Pre-set input area handlers
                inputText.placeholder = "נסח כלל על בסיס התצפיות (למשל, כל הברבורים לבנים)";
                inputButton.textContent = "נסח כלל כללי";
                inputButton.onclick = () => this.handleRuleSuggestion(inputText.value);
            },
            addObservation: function() {
                 if (this.currentObsIndex >= this.observations.length) {
                     updateOutput(simulationOutput.textContent + "\n\n<span class='analysis neutral'>אין עוד תצפיות מיידיות זמינות באגם הזה.</span>");
                     hideActionButtons();
                     if (!this.ruleSuggested) {
                          updateOutput(simulationOutput.textContent + "\n\n<span class='analysis'>אספת את כל התצפיות הזמינות. נסה לנסח כלל על בסיסן.</span>");
                         showInput(inputText.placeholder, inputButton.textContent, inputButton.onclick);
                         this.ruleSuggested = true; // Prevent suggesting rule multiple times this way
                     } else if (!this.contradictoryObserved) {
                          // If rule was suggested and no black swan found yet
                          updateOutput(simulationOutput.textContent + "\n\n<span class='analysis'>צברת תצפיות רבות שתומכות בכללך ('" + this.suggestedRule + "'). אינדוקציה נראית חזקה כעת!</span>");
                           showActionButton("המשך לחשוב על הבעיה", () => {
                                updateOutput(simulationOutput.textContent + "\n\n<span class='analysis'>הבעיה היא: גם אלף תצפיות תומכות לא מבטיחות שהכלל נכון בכל המקרים האפשריים...</span>");
                                showActionButton("חשוף בעיה פילוסופית עמוקה", () => this.revealProblem());
                           });
                     }
                     return;
                 }

                 const obs = this.observations[this.currentObsIndex];
                 simulationOutput.textContent += `\n<span class='observation'>צפית ב: ${obs}.</span>`; // Append observation
                 // Trigger fade-in animation for the new text
                 simulationOutput.classList.remove('fade-in'); // Reset animation
                 void simulationOutput.offsetWidth; // Trigger reflow
                 simulationOutput.classList.add('fade-in');

                 this.currentObsIndex++;

                 hideActionButtons(); // Hide buttons while processing

                 if (obs.includes("שחור") && this.ruleSuggested) {
                     this.contradictoryObserved = true;
                     hideInput(); // Ensure input is hidden if visible
                     updateOutput(simulationOutput.textContent + `\n\n<span class='anomaly'>!!!! תצפית סותרת !!!!</span>\n<span class='analysis'>צפית כעת בברבור שחור. הכלל שניסחת ("${this.suggestedRule || '...'}"), המבוסס על תצפיות קודמות, הופרך על ידי תצפית בודדת זו.</span>\n\n<span class='analysis'>ניתוח הסימולציה: זוהי המחשה ל'בעיית האינדוקציה' של יום. אי אפשר להוכיח חוק כללי על סמך מספר סופי של מקרים, כי תצפית עתידית עלולה לסתור אותו.</span>`, 'failure');
                     showActionButton("המשך לשלב הבא: הפרכה (פופר)", () => moveToNextStage());

                 } else if (this.currentObsIndex >= 3 && !this.ruleSuggested) {
                     updateOutput(simulationOutput.textContent + "\n\n<span class='analysis'>צברת מספר תצפיות. נסה לנסח כלל כללי על בסיסן.</span>");
                     showInput(inputText.placeholder, inputButton.textContent, inputButton.onclick);
                     this.ruleSuggested = true;
                 } else {
                      // Continue adding observations or wait for rule if suggested but no anomaly yet
                      if (!this.contradictoryObserved) { // Only show 'add observation' if no black swan appeared yet
                         showActionButton("בצע תצפית נוספת", () => this.addObservation());
                      }
                      if (this.ruleSuggested && !this.contradictoryObserved) {
                           showActionButton("נסה לנסח כלל מחדש", () => showInput(inputText.placeholder, inputButton.textContent, inputButton.onclick));
                      }
                 }
            },
            handleRuleSuggestion: function(rule) {
                 if (rule.trim().length > 15 && rule.toLowerCase().includes("כל")) { // Basic check for a general rule
                    this.suggestedRule = rule.trim();
                    updateOutput(simulationOutput.textContent + `\n\nהכלל שהצעת: "<span class='success'>${this.suggestedRule}</span>"\n\n<span class='analysis'>מעולה. זוהי היסק אינדוקטיבי. כעת נמשיך לצבור תצפיות כדי לראות אם הכלל עומד במבחן המציאות...</span>`);
                    hideInput();
                    // Check if the rule is immediately falsified by existing observations (if user suggested late)
                    const alreadySeenBlackSwan = this.observations.slice(0, this.currentObsIndex).some(obs => obs.includes("שחור"));
                    if (alreadySeenBlackSwan) {
                        this.contradictoryObserved = true;
                         updateOutput(simulationOutput.textContent + `\n\n<span class='anomaly'>!!!! תצפית סותרת התגלתה עוד לפני ניסוח הכלל !!!!</span>\n<span class='analysis'>נראה שאחד הברבורים בהם כבר צפית היה שחור. הכלל שלך ("${this.suggestedRule}") הופרך מיד עם ניסוחו.</span>\n\n<span class='analysis'>ניתוח הסימולציה: זה מדגים את הפגיעות של כללים אינדוקטיביים. תצפית סותרת אחת מספיקה כדי למוטט אותם.</span>`, 'failure');
                        showActionButton("המשך לשלב הבא: הפרכה (פופר)", () => moveToNextStage());
                    } else {
                       showActionButton("בצע תצפית נוספת", () => this.addObservation());
                    }

                 } else {
                     updateOutput(simulationOutput.textContent + "\n\n<span class='analysis failure'>אנא נסח כלל כללי וברור יותר על בסיס כל הברבורים שראית עד כה. ודא שהוא מתחיל במילה 'כל' או דומה.</span>", 'failure');
                     // Keep input visible
                 }
            },
            revealProblem: function() {
                 hideActionButtons();
                 updateOutput(simulationOutput.textContent + `\n\n<span class='analysis anomaly'>!!!! בעיית האינדוקציה של יום !!!!</span>\n<span class='analysis'>כפי שהראה דיוויד יום, לא משנה כמה תצפיות תומכות צברת (אפילו מיליון ברבורים לבנים), אין בכך הוכחה לוגית מוחלטת שכל הברבורים בעולם לבנים ושלא תצוץ תצפית סותרת בעתיד. אינדוקציה נשענת על הנחת אחידות הטבע (שהעתיד יהיה דומה לעבר), אך הנחה זו עצמה אינה ניתנת להוכחה אינדוקטיבית!</span>\n\n<span class='analysis'>בעיה זו מערערת את היכולת לבסס ידע מדעי על "הוכחה" אינדוקטיבית. זה פתח דלת לחשיבה חדשה...</span>`, 'anomaly');
                 showActionButton("המשך לשלב הפילוסופי הבא: עולם ההפרכה", () => moveToNextStage());
            }
        },
        {
            name: "השלב הפופריאני: מדע של הפרכה (פַלְסִיפִיקַצְיָה)",
            description: "ברוכים הבאים לעידן קרל פופר! מדע לא 'מוכיח' תיאוריות, הוא רק מנסה להפריך אותן. תיאוריה טובה היא כזו שניתן לבדוק באופן שיטתי ולמצוא לה עדויות סותרות. נסח תחזית שבאמצעותה ניתן להפריך תיאוריה נתונה.",
            hypothesis: "כל בני האדם עפים אם הם קופצים מבניין גבוה.", // A clearly false, but testable hypothesis
            setup: function() {
                updateOutput(`לפניך תיאוריה נועזת: "<span class='hypothesis'>${this.hypothesis}</span>"\n\nלפי קרל פופר, תיאוריה זו מדעית לא כי ניתן לאשש אותה, אלא כי ניתן באופן עקרוני <span class='highlight'>להפריך</span> אותה. כדי לעשות זאת, עליך לנסח <span class='highlight'>תחזית ספציפית</span> על תוצאה של ניסוי או תצפית, שאם היא תתברר כשגויה - התיאוריה כולה תיפול. במילים אחרות: מה *לא* אמור לקרות אם התיאוריה נכונה, ושבדיקתו עשויה להוכיח שהיא שגויה?`, 'normal');
                showInput("נסח תחזית ניתנת להפרכה (למשל, אם אדם מסוים יקפוץ מבניין גבוה, הוא לא יעוף).", "בצע 'ניסוי' לבדיקת התחזית", (input) => this.handleFalsificationAttempt(input));
                 inputText.placeholder = "נסח תחזית הניתנת להפרכה...";
                 inputButton.textContent = "בצע 'ניסוי' לבדיקת התחזית";
            },
            handleFalsificationAttempt: function(prediction) {
                const lowerPrediction = prediction.toLowerCase().trim();
                let feedback = `ביצעת 'ניסוי מחשבתי' המבוסס על התחזית:\n"${prediction.trim()}"\n\n`;

                hideInput(); // Hide input while giving feedback

                // Basic check for falsifiability phrasing related to the hypothesis
                const relevantToHypothesis = lowerPrediction.includes("קופץ") || lowerPrediction.includes("בניין") || lowerPrediction.includes("עף") || lowerPrediction.includes("ליפול") || lowerPrediction.includes("ארצה");
                const suggestsFalsification = lowerPrediction.includes("לא יעוף") || lowerPrediction.includes("ייפול") || lowerPrediction.includes("ימות") || lowerPrediction.includes("יתרסק"); // Phrases suggesting the hypothesis is false

                if (lowerPrediction.length < 10 || !relevantToHypothesis) {
                     feedback += `<span class='analysis failure'>ניתוח הסימולציה: התחזית קצרה מדי או לא קשורה מספיק לתיאוריה. כדי להפריך תיאוריה ספציפית, עליך לנסח תחזית ספציפית שנובעת מהתיאוריה וניתנת לבדיקה. נסה שוב.</span>`;
                     updateOutput(simulationOutput.textContent + feedback, 'failure');
                      showInput(inputText.placeholder, inputButton.textContent, inputButton.onclick); // Show input again
                     return;
                }

                if (!suggestsFalsification) {
                    feedback += `<span class='analysis failure'>ניתוח הסימולציה: תחזית זו אינה ניתנת להפרכה בקלות. תחזית טובה להפרכה צריכה לצפות משהו ש *לא* אמור לקרות אם התיאוריה נכונה, ושבדיקתו תמוטט את התיאוריה. נסה לנסח תחזית שמעידה על כישלון התיאוריה ("... הוא לא יעוף", "... הוא ייפול", "... הוא יתרסק").</span>`;
                    updateOutput(simulationOutput.textContent + feedback, 'failure');
                     showInput(inputText.placeholder, inputButton.textContent, inputButton.onclick); // Show input again
                    return; // Stay in the current state
                }


                // Simulate a test result: This hypothesis is clearly false, so the test MUST falsify it in a realistic simulation.
                const falsified = true; // It will always be falsified in reality for this hypothesis

                if (falsified) {
                    feedback += `<span class='success'>תוצאת הניסוי המחשבתי: התצפית סתרה את התחזית!</span> האדם שקפץ מהבניין <span class='failure'>לא עף</span>. הוא נפל ארצה.\n\n<span class='analysis revolution'>ניתוח הסימולציה: מזל טוב! הצלחת לנסח תחזית ניתנת להפרכה, ו'הניסוי' (המציאות) הראה שהתחזית שגויה. מכאן נובע שהתיאוריה המקורית ("כל בני האדם עפים...") <span class='failure'>הופרכה</span>. לפי פופר, תיאוריה זו נדחית.</span>\n<span class='analysis'>זהו כוחה של ההפרכה - ניסוי בודד יכול למוטט תיאוריה, בניגוד לאינדוקציה שאינה יכולה להוכיח אותה לעולם. המדע מתקדם על ידי דחיית תיאוריות שגויות.</span>`;
                    updateOutput(simulationOutput.textContent + feedback, 'revolution');
                    showActionButton("המשך לשלב הבא: משברים ומהפכות (קון)", () => moveToNextStage());

                } else { // This branch theoretically shouldn't be reached with the chosen hypothesis, but kept for robustness
                    feedback += `<span class='analysis neutral'>תוצאת הניסוי המחשבתי: התצפית תאמה את התחזית. לא הצלחת להפריך את התיאוריה בניסיון זה.</span>\n\n<span class='analysis neutral'>ניתוח הסימולציה: ההיפותזה עמדה בפני ניסיון הפרכה קפדני זה. זה נקרא 'קורובורציה' – חיזוק זמני של התיאוריה. אך זכור: כישלון בהפרכה אינו הוכחה מוחלטת לנכונות התיאוריה! ייתכנו ניסויים עתידיים שיפריכו אותה.</span>`;
                     updateOutput(simulationOutput.textContent + feedback, 'neutral');
                     showActionButton("המשך לשלב הבא: פרדיגמות ומהפכות (קון)", () => moveToNextStage());
                }
            }
        },
        {
            name: "השלב הקוהניאני: פרדיגמות, משברים ומהפכות",
            description: "עכשיו נבחן את התפתחות המדע בפרספקטיבה היסטורית רחבה יותר, כפי שהציע תומאס קון. אתה פועל בתוך 'פרדיגמה' מקובלת.",
            state: 'normal', // 'normal', 'anomalies', 'crisis', 'revolution'
            anomaliesCount: 0,
            setup: function() {
                this.state = 'normal';
                this.anomaliesCount = 0;
                updateOutput("<span class='hypothesis'>אתה פועל במסגרת 'פרדיגמה' מדעית מקובלת.</span> חשוב על המודל הגיאוצנטרי (כדור הארץ במרכז היקום) כדוגמה. המדע בתקופה זו מתמקד ב'מדע נורמלי' – פתרון 'חידות' קטנות ושיפור הפרדיגמה הקיימת. לדוגמה, חישוב מדויק יותר של תנועת כוכבי הלכת במסגרת המודל הקיים.", 'normal');
                showActionButton("נסה לפתור 'חידה' במסגרת הפרדיגמה הקיימת (מדע נורמלי)", () => this.handleAction('normal'));
                 showActionButton("חפש תופעות חריגות שקשה להסביר", () => this.handleAction('introduce-anomaly'), 'secondary');
            },
            handleAction: function(action) {
                 hideActionButtons(); // Hide buttons while processing

                if (action === 'normal') {
                     let resultText;
                     if (this.state === 'normal') {
                         resultText = `ניסית לפתור חידה נוספת במסגרת הפרדיגמה.`;
                         updateOutput(simulationOutput.textContent + "\n\n" + resultText, 'normal');
                         setTimeout(() => { // Add a slight delay before showing analysis
                            updateOutput(simulationOutput.textContent + `\n<span class='analysis success'>ניתוח הסימולציה: בשלב 'מדע נורמלי', הכלים של הפרדיגמה יעילים. הצלחת לפתור את החידה! המדע מתקדם בהדרגה בתוך המסגרת הקיימת.</span>`, 'success');
                            showActionButton("המשך לעבוד ב'מדע נורמלי'", () => this.handleAction('normal'));
                            showActionButton("חפש תופעות חריגות (אנומליה)", () => this.handleAction('introduce-anomaly'), 'secondary');
                         }, 1000);

                     } else if (this.state === 'anomalies') {
                         resultText = `ניסית לפתור חידה נוספת, למרות האנומליות שמצטברות.`;
                          updateOutput(simulationOutput.textContent + "\n\n" + resultText, 'normal');
                          setTimeout(() => {
                             const hitAnomaly = Math.random() < 0.6; // Higher chance of issues when anomalies exist
                             if (hitAnomaly) {
                                this.anomaliesCount++;
                                 updateOutput(simulationOutput.textContent + `\n<span class='analysis anomaly'>ניתוח הסימולציה: נתקלת שוב בקשיים! החידה קשה לפתרון, או שהפתרון דורש התאמות מסובכות ומאולצות בתוך הפרדיגמה. זו עוד 'אנומליה'.</span>\n(צברת כעת <span class='anomaly'>${this.anomaliesCount}</span> אנומליות משמעותיות).`, 'anomaly');
                             } else {
                                  updateOutput(simulationOutput.textContent + `\n<span class='analysis neutral'>ניתוח הסימולציה: הצלחת לפתור את החידה, אך נדרשו התאמות מסובכות בתוך הפרדיגמה. האנומליות עדיין קיימות.</span>\n(צברת כעת <span class='anomaly'>${this.anomaliesCount}</span> אנומליות משמעותיות).`, 'neutral');
                             }

                             if (this.anomaliesCount >= 4) { // Higher threshold for crisis
                                this.state = 'crisis';
                                this.handleAction('crisis'); // Transition to crisis automatically
                             } else {
                                showActionButton("המשך לעבוד בתוך הפרדיגמה", () => this.handleAction('normal'));
                                showActionButton("שקול את המשמעות של האנומליות", () => this.handleAction('consider-anomalies'), 'secondary');
                             }
                          }, 1000);

                     } else if (this.state === 'crisis') {
                          resultText = `ניסית לפתור חידה, אך הפרדיגמה עדיין במשבר עמוק.`;
                          updateOutput(simulationOutput.textContent + "\n\n" + resultText, 'crisis');
                           setTimeout(() => {
                               updateOutput(simulationOutput.textContent + `\n<span class='analysis crisis'>ניתוח הסימולציה: בשלב משבר, קשה מאוד, ולעיתים בלתי אפשרי, לפתור חידות חדשות או להסביר תצפיות קיימות באופן מספק באמצעות הפרדיגמה הישנה. הכלים שלה לא עובדים.</span>`, 'crisis');
                               showActionButton("המשך לחפש פתרונות בתוך הפרדיגמה (קשה!)", () => this.handleAction('normal'), 'negative');
                               showActionButton("התחל לחשוב על רעיונות חדשים לחלוטין (פוטנציאל לפרדיגמה חדשה)", () => this.handleAction('seek-new-paradigm'));
                           }, 1000);
                     }
                } else if (action === 'introduce-anomaly') {
                    if (this.state === 'normal' || this.state === 'anomalies') {
                         this.anomaliesCount++;
                         this.state = 'anomalies'; // Ensure state is anomalies if not already
                        updateOutput(simulationOutput.textContent + `\n\n<span class='anomaly'>נתקלת ב'אנומליה'!</span> תופעה שקשה להסביר או לחזות באופן מדויק באמצעות הפרדיגמה הקיימת (למשל, תנועה מוזרה של כוכב לכת שלא מתאימה בקלות למודל הגיאוצנטרי).\n(צברת כעת <span class='anomaly'>${this.anomaliesCount}</span> אנומליות משמעותיות).`, 'anomaly');
                         setTimeout(() => {
                             if (this.anomaliesCount >= 4) {
                                 this.state = 'crisis';
                                 this.handleAction('crisis'); // Transition to crisis automatically
                              } else {
                                 showActionButton("המשך לעבוד בתוך הפרדיגמה (נסה להתאים את האנומליה)", () => this.handleAction('normal'));
                                 showActionButton("שקול את המשמעות של האנומליות", () => this.handleAction('consider-anomalies'), 'secondary');
                             }
                         }, 1000);
                    }
                } else if (action === 'consider-anomalies') {
                     if (this.state === 'anomalies') {
                         updateOutput(simulationOutput.textContent + `\n\n<span class='analysis anomaly'>אתה משקיע מחשבה באנומליות המצטברות. הן יוצרות קושי הולך וגובר בפרדיגמה הקיימת. אם לא יימצא להן פתרון מספק, הן עלולות להוביל למשבר.</span>\n(צברת כעת <span class='anomaly'>${this.anomaliesCount}</span> אנומליות משמעותיות).`, 'anomaly');
                          setTimeout(() => {
                              if (this.anomaliesCount >= 4) {
                                  this.state = 'crisis';
                                  this.handleAction('crisis'); // Transition to crisis automatically
                              } else {
                                showActionButton("המשך לעבוד בתוך הפרדיגמה", () => this.handleAction('normal'));
                                showActionButton("חפש אנומליות נוספות", () => this.handleAction('introduce-anomaly'), 'secondary');
                              }
                          }, 1000);
                     }
                }
                else if (action === 'crisis') {
                     // This state is typically entered automatically when anomalies threshold is met
                     if (this.state === 'crisis') {
                          updateOutput(simulationOutput.textContent + "\n\n<span class='crisis'>!!!! משבר מדעי עמוק !!!!</span>\n<span class='analysis crisis'>הצטברות האנומליות והקשיים הבלתי פתירים יצרו משבר. הפרדיגמה הקיימת אינה מספקת יותר. מדענים רבים מאבדים אמון במסגרת הישנה ומחפשים דרכים חדשות לחשוב על הבעיות.</span>", 'crisis');
                          setTimeout(() => {
                              showActionButton("התחל לחשוב על רעיונות חדשים לחלוטין (פוטנציאל לפרדיגמה חדשה)", () => this.handleAction('seek-new-paradigm'));
                               showActionButton("נסה בכל זאת 'לתקן' את הפרדיגמה הישנה", () => {
                                    updateOutput(simulationOutput.textContent + "\n\n<span class='analysis failure'>ניתוח הסימולציה: ניסית לתקן את הפרדיגמה הישנה, אך המשבר עמוק מדי. טלאי על טלאי לא עוזרים כשמבנה היסוד רעוע.</span>", 'failure');
                                    setTimeout(() => {
                                         showActionButton("התחל לחשוב על רעיונות חדשים לחלוטין", () => this.handleAction('seek-new-paradigm'));
                                    }, 1000);
                               }, 'negative');
                          }, 1000);
                     }
                 } else if (action === 'seek-new-paradigm') {
                      if (this.state === 'crisis') {
                           updateOutput(simulationOutput.textContent + "\n\n<span class='revolution'>אתה מתחיל לגבש רעיונות שונים מהותית, כאלה שלא מתאימים לפרדיגמה הישנה.</span> חשוב על המודל ההליוצנטרי (השמש במרכז) כמודל חדש לחלוטין, המציע דרך אחרת לגמרי להסתכל על תנועת גרמי השמיים ומסביר את האנומליות באופן פשוט ואלגנטי יותר.", 'revolution');
                           setTimeout(() => {
                                this.state = 'revolution';
                                this.handleAction('revolution'); // Transition to revolution
                           }, 1000);
                      }
                 } else if (action === 'revolution') {
                    if (this.state === 'revolution') {
                         updateOutput(simulationOutput.textContent + "\n\n<span class='revolution'>!!!! מהפכה מדעית קוהניאנית !!!!</span>\n<span class='analysis revolution'>הרעיונות החדשים (הפרדיגמה החדשה) צוברים תאוצה ומתחילים להתקבל על ידי חלק גדל והולך מהקהילה המדעית. זוהי 'מהפכה מדעית' – שינוי דרמטי ורדיקלי. הפרדיגמה החדשה מחליפה את הישנה, ומשנה איתה את השאלות הנשאלות, השיטות, ואפילו את ה'עולם' הנצפה.</span>\n<span class='analysis'>כעת המדע עובר שוב לתקופה של 'מדע נורמלי', אך בתוך המסגרת החדשה לחלוטין.</span>", 'revolution');
                         hideActionButtons();
                         setTimeout(() => {
                              updateOutput(simulationOutput.textContent + "\n\n<span class='analysis'>המדע, על פי קון, אינו מתקדם רק בצורה מצטברת או על ידי הפרכה בלבד, אלא גם דרך קפיצות דרמטיות ולא לגמרי רציונליות, המעצבות מחדש את יסודות הידע.</span>");
                              stageIndicator.textContent = "המסע הסתיים!";
                              showActionButton("סיים את הסימולציה והרהר על המסע", () => {
                                  updateOutput(simulationOutput.textContent + "\n\n<span class='analysis'>המסע הסתיים. חווית את ההתפתחות המרכזית של הבנתנו לגבי טבעו של המדע - מהסבר איכותי, דרך אינדוקציה ובעיותיה, אל הפרכה ככלי לקידום, ועד למשברים ומהפכות המשנות את כללי הידע. המדע הוא תהליך דינמי, ביקורתי, ולעיתים מהפכני!</span>");
                                   // Maybe make explanation button more prominent now
                              });
                         }, 2000); // Longer delay for final impact
                    }
                }
            }
        }
    ];

     function updateOutput(text, type = 'normal') {
        simulationOutput.innerHTML = text; // Use innerHTML to allow spans for styling
        // Add animation class
        simulationOutput.classList.remove('fade-in', 'success', 'failure', 'anomaly', 'crisis', 'revolution', 'normal', 'neutral');
        simulationOutput.classList.add('fade-in', type); // Add new animation and type class
     }


    function showInput(placeholder, buttonText, buttonHandler) {
        inputText.placeholder = placeholder;
        inputButton.textContent = buttonText;
        inputButton.onclick = () => { // Wrap handler to hide input on click
            buttonHandler(inputText.value);
            // Input is hidden inside handlers based on logic flow
        };
        inputText.style.display = 'block';
        inputButton.style.display = 'inline-block';
        inputText.focus(); // Give focus to the input field
         // Add animation class to input elements? More complex layout needed maybe.
    }

    function hideInput() {
        inputText.style.display = 'none';
        inputButton.style.display = 'none';
        inputText.value = ''; // Clear input on hide
    }

     function showActionButton(text, handler, className = '') {
         const button = document.createElement('button');
         button.textContent = text;
         button.onclick = () => { // Wrap handler to hide buttons on click/action
             hideActionButtons(); // Hide all buttons immediately on click
             handler(); // Execute the actual handler
         };
         if (className) {
             button.className = className + ' slide-in'; // Add slide-in class for animation
         } else {
             button.className = 'slide-in';
         }
         actionButtonsDiv.appendChild(button);
         // Remove animation class after it's done? Or let CSS handle it.
     }

    function hideActionButtons() {
        actionButtonsDiv.innerHTML = ''; // Clear all action buttons
    }

    function moveToNextStage() {
        currentStageIndex++;
        if (currentStageIndex < stages.length) {
            initStage(currentStageIndex);
        } else {
             // Should not happen if the last stage has a "Finish" button
             updateOutput("הסימולציה הסתיימה.");
             stageIndicator.textContent = "הסתיים";
             hideInput();
             hideActionButtons();
        }
    }

    function initStage(index) {
        const stage = stages[index];
        stageIndicator.textContent = `שלב ${index + 1}/${stages.length}: ${stage.name}`;
        // Optional: add animation to stage indicator
        stageIndicator.classList.remove('fadeInDown');
        void stageIndicator.offsetWidth; // Trigger reflow
        stageIndicator.classList.add('fadeInDown');

        hideInput();
        hideActionButtons(); // Ensure buttons from previous stage are cleared
        stage.setup();
    }

    // Start button handler
    startButton.onclick = () => {
        hideActionButtons(); // Hide the start button
        moveToNextStage();
    };

    // Explanation toggle handler
    explanationButton.onclick = () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר הסבר מורחב' : 'הצג הסבר מורחב';
    };

    // Initial state: only show start button and introductory text
    stageIndicator.textContent = "ברוכים הבאים למסע הפילוסופי";
    updateOutput("לחץ על 'התחל את המסע המדעי שלך' כדי להתחיל את הסימולציה האינטראקטיבית על התפתחות הפילוסופיה של המדע.", 'neutral');
     hideInput(); // Ensure input is hidden initially

</script>
```