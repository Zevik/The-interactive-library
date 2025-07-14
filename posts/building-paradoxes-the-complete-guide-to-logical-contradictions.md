---
title: "בונים פרדוקסים: המדריך המלא לסתירות לוגיות"
english_slug: building-paradoxes-the-complete-guide-to-logical-contradictions
category: "מדעים מדויקים / מתמטיקה"
tags:
  - פרדוקס
  - לוגיקה
  - כשל לוגי
  - סתירה עצמית
  - פילוסופיה של הלוגיקה
  - אינטראקטיבי
---
# בונים פרדוקסים: המדריך המלא לסתירות לוגיות

צאו למסע מרתק אל גבולות ההיגיון! האם ייתכן שטענה תהיה אמיתית ושקרית באותו נשימה? פרדוקסים לוגיים הם נקודות שבר מסקרנות במבנה המחשבה שלנו, החושפות את האתגרים והמגבלות של השפה וההיגיון הפורמלי. היכנסו למעבדת הפרדוקסים האינטראקטיבית ובנו בעצמכם את המבנים המדהימים והמבלבלים הללו.

## סימולטור פרדוקסים: בנה ונתח

בחרו תבנית לפרדוקס, השלימו את החסר, וצפו כיצד ההיגיון מתפתל ומוביל לסתירה... או שלא!

<div class="paradox-app">
    <div class="input-area">
        <label for="template-select" class="input-label">בחרו את תבנית הפרדוקס:</label>
        <select id="template-select" class="template-select">
            <option value="liar-basic">פרדוקס השקרן הקלאסי: "משפט זה הוא [______]"</option>
            <option value="self-descriptive">פרדוקס ראסל (גרסה מילולית): על טענות המתארות את עצמן</option>
             <option value="catalog">פרדוקס הספרן/קטלוג: על קטלוג שמפרט קטלוגים אחרים</option>
        </select>
        <div id="liar-basic-input" class="template-input">
            <label for="liar-adjective" class="input-label">השלימו את המשפט:</label>
            <input type="text" id="liar-adjective" placeholder="למשל: שקרי, אמיתי, לא ניתן להוכחה">
             <p class="input-hint">המשפט יהיה: "משפט זה הוא <span class="placeholder-text">______</span>."</p>
        </div>
         <div id="self-descriptive-input" class="template-input" style="display:none;">
            <label for="self-descriptive-term" class="input-label">הגדירו את המושג המרכזי:</label>
             <input type="text" id="self-descriptive-term" value="טענות המתארות את עצמן" disabled>
              <p class="input-hint">ננתח את הטענה: "טענה המתארת את כל ה<span class="placeholder-text">[מושג]</span> שאינן <span class="placeholder-text">[מושג]</span> את עצמן."</p>
        </div>
         <div id="catalog-input" class="template-input" style="display:none;">
            <label for="catalog-term" class="input-label">הגדירו את סוג האובייקט והפעולה:</label>
             <input type="text" id="catalog-term" value="קטלוג שמפרט את עצמו" disabled>
              <p class="input-hint">ננתח את הקטלוג: "קטלוג המפרט את כל ה<span class="placeholder-text">[סוג אובייקט]</span> שאינם <span class="placeholder-text">[הפעולה]</span> את עצמם."</p>
        </div>
        <button id="build-paradox-btn" class="action-button">בנה ונתח את הפרדוקס!</button>
    </div>

    <div class="output-area" style="display: none;">
        <h3>הטענה/אובייקט שיצרת:</h3>
        <p id="generated-statement" class="statement"></p>

        <h3>ניתוח צעד אחר צעד:</h3>
        <div id="analysis-steps">
            <!-- Analysis steps will be injected here -->
        </div>
         <p id="analysis-conclusion" class="conclusion"></p>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">לחצ/י כאן להסבר המלא על פרדוקסים</button>

<div id="explanation" style="display: none;">
    <h2>הצלילה לעומק: מבנה ופתרון פרדוקסים</h2>

    <h3>מהו פרדוקס לוגי? דוגמאות ראשונות.</h3>
    פרדוקס לוגי הוא מצב שבו הנחות שנראות תקפות מובילות למסקנה שהיא סתירה, או שטענה יחידה מובילה לסתירה פנימית (כמו גם אמיתית וגם שקרית). פרדוקסים אינם רק חידות, אלא אתגרים ליסודות הלוגיקה והשפה שלנו. דוגמה ידועה (אך לא לוגית פורמלית) היא פרדוקס זנון על התנועה. פרדוקסים לוגיים טהורים יותר נוגעים לערכי אמת (אמיתי/שקרי) ולתורת הקבוצות.

    <h3>פרדוקס השקרן: המקרה הקלאסי.</h3>
    פרדוקס השקרן, שמוכר עוד מימי יוון העתיקה, מתמקד במשפט כמו: "משפט זה הוא שקרי". הבה נפרק אותו:
    1.  **נניח שהוא אמיתי:** אם המשפט "משפט זה הוא שקרי" אמיתי, אז מה שהוא אומר נכון. הוא אומר שהוא שקרי. מכאן, שאם הוא אמיתי, הוא שקרי. זו <span class="contradiction-inline">סתירה</span>!
    2.  **נניח שהוא שקרי:** אם המשפט "משפט זה הוא שקרי" שקרי, אז מה שהוא אומר אינו נכון. הוא אומר שהוא שקרי. אם הטענה "המשפט שקרי" אינה נכונה, אזי המשפט חייב להיות אמיתי. מכאן, שאם הוא שקרי, הוא אמיתי. גם זו <span class="contradiction-inline">סתירה</span>!
    קיבלנו שהמשפט אמיתי אם ורק אם הוא שקרי – מצב בלתי אפשרי בלוגיקה קלאסית.

    <h3>הפניה עצמית (Self-reference): לב הפרדוקס?</h3>
    מאפיין בולט בפרדוקסים רבים הוא שהם מתייחסים לעצמם. פרדוקס השקרן קובע תכונה (שקריות) על עצמו. פרדוקס ראסל (עליו בנינו וריאציה בסימולטור) עוסק בקבוצה שהגדרתה תלויה בשאלה האם היא חברה בעצמה. הפניה עצמית אינה בעייתית תמיד ("הפסקה הזו מוסברת בעברית" אינו פרדוקס), אך כאשר היא משולבת עם שלילה או הגדרה עצמית ביקורתית, היא יכולה ליצור את הלולאה הלוגית הבעייתית.

    <h3>סוגים נוספים של פרדוקסים לוגיים ופילוסופיים.</h3>
    -   **סמנטיים:** קשורים למשמעות והגדרה (שקרן, גְרֵלִינְג).
    -   **מסטיים (תורת הקבוצות):** קשורים לחברות בקבוצות (ראסל, קנטור). אלו היו קריטיים לפיתוח יסודות המתמטיקה.
    -   **אפיסטמיים:** קשורים לידע ואמונה (פרדוקס הידען).

    <h3>היכן הכשל? ניתוח והתמודדות.</h3>
    פרדוקסים מאלצים אותנו לשאול: האם הבעיה בשפה? בלוגיקה שלנו? בהנחות הסמויות? הניתוח לרוב מצביע על שילוב של הפניה עצמית עם שלילה או קביעה ביקורתית, בתוך מערכת (לוגית או לשונית) שאינה מגבילה מספיק את התופעה הזו.

    <h3>פתרונות קלאסיים: לבנות מחדש את היסודות.</h3>
    כדי לפתור את הפרדוקסים שערערו על המתמטיקה, הוצעו פתרונות כמו:
    -   **תיאוריית הטיפוסים:** יצירת היררכיה בה אובייקט מטיפוס מסוים אינו יכול להכיל (או להתייחס באופן מסוכן) לאובייקטים מטיפוס גבוה יותר, ובכך למנוע הפניה עצמית "מסוכנת".
    -   **מערכות אקסיומטיות מחמירות:** כמו תורת הקבוצות של צרמלו-פרנקל (ZFC), שמגבילות את האפשרות להגדיר קבוצות באופן שרירותי ומונעות פרדוקס ראסל.
    -   **לוגיקות לא-קלאסיות:** מערכות לוגיות שמכירות באפשרות של טענות שאינן רק אמיתיות או שקריות לחלוטין, או שמקבלות סתירות בתוך מערכת (לוגיקות פרא-קונסיסטנטיות).

    <h3>השפעה על המתמטיקה והלוגיקה המודרנית.</h3>
    פרדוקס ראסל היה זרז מרכזי בפיתוח תורת הקבוצות האקסיומטית. עבודותיו של קורט גדל, ובפרט משפטי אי-השלמות, הראו קשר עמוק בין מבנים דמויי פרדוקס השקרן (משפטים המתייחסים ליכולת ההוכחה שלהם) לבין מגבלות יסודיות של כל מערכת לוגית פורמלית עשירה מספיק. הפרדוקסים, שהיו תחילה כאב ראש לפילוסופים ולוגיקנים, הפכו לכלי חשוב להבנת עומקם ומגבלותיהם של מערכות פורמליות.

</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.6;
        color: #333;
        margin: 0;
        padding: 20px;
        background-color: #f0f4f8; /* Softer background */
        direction: rtl;
        text-align: right;
    }

    h1, h2, h3 {
        color: #1a374d; /* Dark blue */
        margin-bottom: 15px;
    }

    h1 {
        text-align: center;
        font-size: 2.5rem;
        margin-top: 0;
        margin-bottom: 30px;
        font-weight: 700;
    }

    h2 {
        font-size: 1.8rem;
        border-bottom: 2px solid #4a90e2; /* Blue underline */
        padding-bottom: 5px;
        margin-top: 30px;
    }

    h3 {
        font-size: 1.4rem;
        color: #2a5b84; /* Medium blue */
        margin-top: 20px;
    }

    .paradox-app, #explanation {
        max-width: 750px;
        margin: 20px auto;
        padding: 25px;
        border: 1px solid #d0dce6; /* Light blue border */
        border-radius: 12px; /* More rounded corners */
        background-color: #ffffff; /* White background */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        transition: all 0.5s ease-in-out; /* Smooth transition for reveal */
    }

    .input-area {
        margin-bottom: 20px;
    }

    .input-label {
        display: block;
        margin-bottom: 8px;
        font-weight: 700;
        color: #1a374d;
        font-size: 1.1rem;
    }

    .template-select,
    .template-input input[type="text"] {
        width: calc(100% - 24px); /* Account for padding */
        padding: 12px;
        margin-bottom: 15px;
        border: 1px solid #d0dce6;
        border-radius: 6px;
        font-size: 1rem;
        box-sizing: border-box; /* Include padding and border in element's total width */
        transition: border-color 0.3s ease;
    }

     .template-select:focus,
     .template-input input[type="text"]:focus {
         border-color: #4a90e2; /* Highlight on focus */
         outline: none;
         box-shadow: 0 0 5px rgba(74, 144, 226, 0.5);
     }

     .template-input p.input-hint {
        margin-top: -10px;
        margin-bottom: 15px;
        font-size: 0.9rem;
        color: #666; /* Darker hint text */
        font-style: italic;
     }
     .placeholder-text {
         color: #4a90e2; /* Blue placeholder */
         font-weight: 400;
     }


    .action-button, .toggle-button {
        display: block;
        width: 100%;
        padding: 12px;
        background-color: #4a90e2; /* Blue button */
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 1.1rem;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        margin-bottom: 15px;
        font-weight: 700;
    }

    .action-button:hover, .toggle-button:hover {
        background-color: #357ABD; /* Darker blue on hover */
    }
     .action-button:active, .toggle-button:active {
         transform: scale(0.98); /* Press effect */
     }


    .output-area {
        margin-top: 20px;
        border-top: 1px solid #e0e6eb; /* Lighter border */
        padding-top: 20px;
         opacity: 0; /* Start hidden for animation */
         transform: translateY(20px); /* Start below for slide-in */
         transition: opacity 0.6s ease-out, transform 0.6s ease-out;
    }
    .output-area.visible {
         opacity: 1;
         transform: translateY(0);
    }


    .statement {
        font-weight: 700;
        color: #1a374d; /* Dark blue */
        font-size: 1.3rem;
        margin-bottom: 25px;
        text-align: center;
        padding: 15px;
        background-color: #eef4f8; /* Very light blue background */
        border-left: 4px solid #4a90e2; /* Blue left border */
        border-radius: 4px;
    }

    #analysis-steps {
        margin-top: 20px;
    }

    .analysis-step {
        background-color: #f8fafd; /* Lightest blue */
        border: 1px solid #e0e6eb;
        border-radius: 8px; /* Rounded corners */
        padding: 15px;
        margin-bottom: 12px;
        display: flex;
        align-items: flex-start; /* Align content to the top */
        font-size: 1rem;
        color: #333;
        opacity: 0; /* Start hidden for animation */
        transform: translateX(-20px); /* Start left for slide-in */
        transition: opacity 0.5s ease-out, transform 0.5s ease-out;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05); /* Subtle shadow for steps */
    }

     .analysis-step.visible {
         opacity: 1;
         transform: translateX(0);
     }


     .step-number {
        font-weight: 700;
        margin-left: 15px; /* Space from text */
        color: #4a90e2; /* Blue number */
        flex-shrink: 0;
        font-size: 1.2rem;
        position: relative;
        top: -3px; /* Adjust alignment */
     }

     .step-content {
        flex-grow: 1;
     }

     .contradiction-inline {
         color: #d0021b; /* Red */
         font-weight: 700;
     }

    .analysis-step.contradiction {
        background-color: #fdeded; /* Light red background */
        border-color: #d0021b; /* Red border */
         animation: contradiction-flash 0.8s ease-in-out 3; /* Flash animation */
    }

     @keyframes contradiction-flash {
         0%, 100% { background-color: #fdeded; }
         50% { background-color: #ffcccc; } /* Lighter red flash */
     }


     .conclusion {
        font-weight: 700;
        margin-top: 20px;
        padding: 15px;
        border: 2px dashed;
        border-radius: 8px;
        text-align: center;
        font-size: 1.1rem;
         opacity: 0; /* Start hidden for animation */
         transform: translateY(20px); /* Start below for slide-in */
         transition: opacity 0.6s ease-out 0.5s, transform 0.6s ease-out 0.5s; /* Delayed animation */
     }
      .conclusion.visible {
          opacity: 1;
          transform: translateY(0);
      }


     .conclusion.paradox {
        border-color: #d0021b; /* Red for paradox */
        background-color: #fff5f5; /* Lighter red background */
        color: #d0021b;
     }

     .conclusion.no-paradox {
        border-color: #7ed321; /* Green for no paradox */
        background-color: #f8fff5; /* Lighter green background */
        color: #417505; /* Darker green text */
     }

    #explanation {
        margin-top: 30px;
    }
    #explanation p {
        margin-bottom: 15px;
        line-height: 1.7; /* Improved readability */
        color: #555;
    }
     #explanation span.contradiction-inline {
         color: #d0021b;
         font-weight: 700;
     }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        h1 { font-size: 2rem; }
        h2 { font-size: 1.6rem; }
        h3 { font-size: 1.3rem; }
        .paradox-app, #explanation {
            padding: 15px;
            margin: 15px auto;
        }
        .template-select,
        .template-input input[type="text"],
        .action-button, .toggle-button {
            font-size: 1rem;
        }
        .analysis-step {
            padding: 10px;
        }
         .step-number {
            font-size: 1.1rem;
            margin-left: 10px;
         }
        .statement, .conclusion {
            font-size: 1.1rem;
            padding: 10px;
        }
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const templateSelect = document.getElementById('template-select');
        const liarBasicInput = document.getElementById('liar-basic-input');
        const selfDescriptiveInput = document.getElementById('self-descriptive-input');
        const catalogInput = document.getElementById('catalog-input');
        const liarAdjectiveInput = document.getElementById('liar-adjective');
        const buildButton = document.getElementById('build-paradox-btn');
        const appOutputArea = document.querySelector('.paradox-app .output-area');
        const generatedStatement = document.getElementById('generated-statement');
        const analysisStepsContainer = document.getElementById('analysis-steps');
        const analysisConclusion = document.getElementById('analysis-conclusion');
        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationButton = document.getElementById('toggle-explanation');

        // Toggle explanation visibility
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
             // Use CSS classes for animated show/hide
             if (isHidden) {
                 explanationDiv.style.display = 'block';
                  // Force reflow to make transition work
                 explanationDiv.offsetHeight;
                 explanationDiv.classList.add('visible');
             } else {
                  explanationDiv.classList.remove('visible');
                   // Hide after transition
                  explanationDiv.addEventListener('transitionend', function handler() {
                      explanationDiv.style.display = 'none';
                      explanationDiv.removeEventListener('transitionend', handler);
                  });
             }

            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מפורט' : 'לחצ/י כאן להסבר המלא על פרדוקסים';
        });

        // Show/hide input fields based on template selection
        templateSelect.addEventListener('change', (event) => {
            liarBasicInput.style.display = 'none';
            selfDescriptiveInput.style.display = 'none';
             catalogInput.style.display = 'none';

            if (event.target.value === 'liar-basic') {
                liarBasicInput.style.display = 'block';
            } else if (event.target.value === 'self-descriptive') {
                selfDescriptiveInput.style.display = 'block';
            } else if (event.target.value === 'catalog') {
                 catalogInput.style.display = 'block';
            }
        });

        // Build and analyze paradox
        buildButton.addEventListener('click', () => {
            // Reset output area for animation
            appOutputArea.classList.remove('visible');
            appOutputArea.style.display = 'none';
            analysisStepsContainer.innerHTML = ''; // Clear previous analysis
            analysisConclusion.textContent = '';
            analysisConclusion.classList.remove('paradox', 'no-paradox', 'visible');


            const selectedTemplate = templateSelect.value;
            let statementText = '';
            let analysisResult = {};

            if (selectedTemplate === 'liar-basic') {
                const adjective = liarAdjectiveInput.value.trim();
                if (!adjective) {
                    generatedStatement.textContent = 'אנא מלא את החסר כדי לבנות את המשפט.';
                    appOutputArea.style.display = 'block';
                    appOutputArea.classList.add('visible');
                    analysisStepsContainer.innerHTML = '';
                    analysisConclusion.textContent = '';
                    return;
                }
                statementText = `משפט זה הוא ${adjective}.`;
                analysisResult = analyzeLiarBasic(adjective);

            } else if (selectedTemplate === 'self-descriptive') {
                 const term = selfDescriptiveInput.querySelector('input').value; // Use value from disabled input
                 statementText = `טענה המתארת את כל ה${term} שאינן ${term} את עצמן.`;
                 analysisResult = analyzeSelfDescriptive(term);
            } else if (selectedTemplate === 'catalog') {
                 const term = catalogInput.querySelector('input').value; // Use value from disabled input
                 statementText = `קטלוג המפרט את כל ה${term} שאינם ${term} את עצם.`;
                 analysisResult = analyzeCatalog(term);
            }

             // Show output area and statement immediately
            appOutputArea.style.display = 'block';
            appOutputArea.classList.add('visible');
            generatedStatement.textContent = statementText;

            // Display analysis steps sequentially with animation
            displayAnalysisStepsSequentially(analysisResult);
        });

        function analyzeLiarBasic(adjective) {
             const steps = [];
             let isParadox = false;
             let conclusion = '';
             const adj = adjective.toLowerCase();

             // Analysis if the statement is True
             steps.push({ type: 'step', content: 'שלב 1: נניח שהטענה אמיתית.' });
             steps.push({ type: 'step', content: `אם הטענה "${generatedStatement.textContent}" אמיתית, אזי מה שהיא טוענת נכון.` });
             steps.push({ type: 'step', content: `הטענה טוענת שהיא עצמה היא "${adjective}".` });

             if (adj === 'שקרי' || adj === 'false') {
                 steps.push({ type: 'step', content: `לכן, אם הטענה אמיתית, היא שקרית.`, highlight: 'contradiction' });
                 steps.push({ type: 'contradiction', content: 'הגעה לסתירה: אמיתי ← שקרי.' });
                 isParadox = true;
             } else if (adj === 'אמיתי' || adj === 'true') {
                 steps.push({ type: 'step', content: `לכן, אם הטענה אמיתית, היא אמיתית.` });
                 steps.push({ type: 'step', content: 'אין סתירה בשלב זה.' });
             } else {
                  steps.push({ type: 'step', content: `לכן, אם הטענה אמיתית, היא "${adjective}". מסקנה זו תלויה במשמעות המדויקת של "${adjective}".` });
             }

            // Analysis if the statement is False
            steps.push({ type: 'step', content: 'שלב 2: נניח שהטענה שקרית.' });
            steps.push({ type: 'step', content: `אם הטענה "${generatedStatement.textContent}" שקרית, אזי מה שהיא טוענת אינו נכון.` });
            steps.push({ type: 'step', content: `הטענה טוענת שהיא עצמה היא "${adjective}".` });

            if (adj === 'שקרי' || adj === 'false') {
                 steps.push({ type: 'step', content: `אם הטענה שקרית, אזי הטענה שהיא שקרית אינה נכונה. לכן, הטענה חייבת להיות אמיתית.`, highlight: 'contradiction' });
                 steps.push({ type: 'contradiction', content: 'הגעה לסתירה: שקרי ← אמיתי.' });
                 isParadox = true; // Confirm paradox if both sides contradict
            } else if (adj === 'אמיתי' || adj === 'true') {
                 steps.push({ type: 'step', content: `אם הטענה שקרית, אזי הטענה שהיא אמיתית אינה נכונה. לכן, הטענה חייבת להיות שקרית.` });
                 steps.push({ type: 'step', content: 'אין סתירה בשלב זה.' });
            } else {
                 steps.push({ type: 'step', content: `אם הטענה שקרית, אזי הטענה שהיא "${adjective}" אינה נכונה. מסקנה זו תלויה בהגדרת ה"${adjective}".` });
            }

             if (isParadox) {
                 conclusion = 'מסקנה: הטענה מובילה לסתירה לוגית בין אם מניחים שהיא אמיתית ובין אם מניחים שהיא שקרית. הצלחנו לבנות פרדוקס!';
             } else if (adj === 'אמיתי' || adj === 'true') {
                 conclusion = 'מסקנה: הטענה "משפט זה הוא אמיתי" אינה מובילה לסתירה פנימית במערכת לוגית רגילה.';
             } else {
                  conclusion = 'מסקנה: ניתוח זה תלוי במשמעות המדויקת של המילה "'+adjective+'" וכיצד היא מתייחסת לערך האמת של המשפט. ייתכן שזהו פרדוקס, כשל לוגי אחר, או פשוט טענה חסרת משמעות במערכת זו.';
             }

             return { steps, conclusion, isParadox };
        }

         function analyzeSelfDescriptive(term) {
            const steps = [];
            const termDisplay = term.replace('טענות ה', 'ה').replace('טענות ש', 'ש').replace('ה', '').replace('ש', '').trim(); // Improve term display
             const conclusion = 'מסקנה: הטענה מובילה לסתירה לוגית, בדומה לפרדוקס ראסל. אם נניח שהטענה '+termDisplay+' את עצמה, אז לפי ההגדרה היא לא אמורה '+termDisplay+' את עצמה (סתירה). אם נניח שהיא אינה '+termDisplay+' את עצמה, אז לפי ההגדרה היא אמורה '+termDisplay+' את כל הטענות שאינן '+termDisplay+' את עצמן, ולכן היא אמורה '+termDisplay+' את עצמה (סתירה). הצלחנו לבנות פרדוקס מסטי!';
            let isParadox = true;

            steps.push({ type: 'step', content: 'הטענה (S): "טענה המתארת את כל ה'+term+' שאינן '+termDisplay+' את עצמן."' });
            steps.push({ type: 'step', content: 'שלב 1: נניח שהטענה S כן '+termDisplay+' את עצמה.' });
            steps.push({ type: 'step', content: 'אם S '+termDisplay+' את עצמה, אזי היא מקיימת את התנאי ללהיות מתוארת על ידי הטענה S.' });
            steps.push({ type: 'step', content: 'התנאי ללהיות מתוארת על ידי S הוא "להיות טענה שאינה '+termDisplay+' את עצמה".' });
            steps.push({ type: 'step', content: 'לכן, אם S '+termDisplay+' את עצמה, אזי S אינה '+termDisplay+' את עצמה.', highlight: 'contradiction' });
            steps.push({ type: 'contradiction', content: 'הגעה לסתירה: S כן '+termDisplay+' את עצמה ← S אינה '+termDisplay+' את עצמה.' });

            steps.push({ type: 'step', content: 'שלב 2: נניח שהטענה S אינה '+termDisplay+' את עצמה.' });
            steps.push({ type: 'step', content: 'אם S אינה '+termDisplay+' את עצמה, אזי היא מקיימת את התנאי ללהיות מתוארת על ידי הטענה S (שהיא "מתארת את כל הטענות שאינן '+termDisplay+' את עצמן").' });
            steps.push({ type: 'step', content: 'לכן, אם S אינה '+termDisplay+' את עצמה, אזי S כן '+termDisplay+' את עצמה.', highlight: 'contradiction' });
            steps.push({ type: 'contradiction', content: 'הגעה לסתירה: S אינה '+termDisplay+' את עצמה ← S כן '+termDisplay+' את עצמה.' });


             return { steps, conclusion, isParadox };
         }

         function analyzeCatalog(term) {
             const steps = [];
             const termParts = term.split(' שמפרט ');
             const objectType = termParts[0]; // "קטלוג"
             const action = termParts.length > 1 ? termParts[1].replace('את עצמו', '').trim() : 'מפרט'; // "מפרט"
             const conclusion = 'מסקנה: ה'+objectType+' המדובר מוביל לסתירה לוגית, בדומה לפרדוקס הספרן שהוא וריאציה של פרדוקס ראסל. אם ה'+objectType+' '+action+' את עצמו, אז לפי ההגדרה הוא לא אמור '+action+' את עצמו (סתירה). אם ה'+objectType+' אינו '+action+' את עצמו, אז לפי ההגדרה הוא אמור '+action+' את כל ה'+objectType+'ים שאינם '+action+' את עצמם, ולכן הוא אמור '+action+' את עצמו (סתירה). הצלחנו לבנות פרדוקס מסטי!';
             let isParadox = true;


            steps.push({ type: 'step', content: 'האובייקט (C): "'+generatedStatement.textContent+'"' });
            steps.push({ type: 'step', content: 'שלב 1: נניח שה'+objectType+' C כן '+action+' את עצמו.' });
            steps.push({ type: 'step', content: 'אם C '+action+' את עצמו, אזי הוא מקפיד על הכלל ללהיות מפורט ב'+objectType+' C.' });
            steps.push({ type: 'step', content: 'הכלל ללהיות מפורט ב'+objectType+' C הוא "להיות '+objectType+' שאינו '+action+' את עצמו".' });
            steps.push({ type: 'step', content: 'לכן, אם C '+action+' את עצמו, אזי C אינו '+action+' את עצמו.', highlight: 'contradiction' });
            steps.push({ type: 'contradiction', content: 'הגעה לסתירה: C כן '+action+' את עצמו ← C אינו '+action+' את עצמו.' });

            steps.push({ type: 'step', content: 'שלב 2: נניח שה'+objectType+' C אינו '+action+' את עצמו.' });
            steps.push({ type: 'step', content: 'אם C אינו '+action+' את עצמו, אזי הוא מקפיד על הכלל ללהיות מפורט ב'+objectType+' C (שהוא "מפרט את כל ה'+objectType+'ים שאינם '+action+' את עצמם").' });
            steps.push({ type: 'step', content: 'לכן, אם C אינו '+action+' את עצמו, אזי C כן '+action+' את עצמו.', highlight: 'contradiction' });
            steps.push({ type: 'contradiction', content: 'הגעה לסתירה: C אינו '+action+' את עצמו ← C כן '+action+' את עצמו.' });


             return { steps, conclusion, isParadox };
         }


         function displayAnalysisStepsSequentially(analysisResult) {
             analysisStepsContainer.innerHTML = ''; // Ensure empty
             let delay = 0;
             const stepDelay = 700; // Milliseconds between steps

             analysisResult.steps.forEach((step, index) => {
                 setTimeout(() => {
                     const stepDiv = document.createElement('div');
                     stepDiv.classList.add('analysis-step');
                      if (step.highlight) {
                           stepDiv.classList.add(step.highlight);
                      }

                     // Add step number only for 'step' type, not 'contradiction' type
                     if (step.type === 'step') {
                          const stepNumberSpan = document.createElement('span');
                          stepNumberSpan.classList.add('step-number');
                          stepNumberSpan.textContent = (index - analysisResult.steps.filter(s => s.type !== 'step').length + 1) + '.'; // Adjust numbering for non-step types
                           // Better numbering: Count only actual steps
                           const actualStepNumber = analysisResult.steps.filter((s, i) => i <= index && s.type === 'step').length;
                            stepNumberSpan.textContent = actualStepNumber + '.';


                          stepDiv.appendChild(stepNumberSpan);
                     }


                     const stepContentSpan = document.createElement('span');
                     stepContentSpan.classList.add('step-content');
                     stepContentSpan.innerHTML = step.content; // Use innerHTML to allow for <span class="contradiction-inline">
                     stepDiv.appendChild(stepContentSpan);

                     analysisStepsContainer.appendChild(stepDiv);

                     // Trigger visibility animation
                     setTimeout(() => stepDiv.classList.add('visible'), 10); // Small delay to allow DOM attachment


                 }, delay);
                 delay += stepDelay;
             });

             // Display conclusion after all steps
             setTimeout(() => {
                 analysisConclusion.textContent = analysisResult.conclusion;
                 if (analysisResult.isParadox) {
                      analysisConclusion.classList.add('paradox');
                      analysisConclusion.classList.remove('no-paradox');
                 } else {
                      analysisConclusion.classList.add('no-paradox');
                      analysisConclusion.classList.remove('paradox');
                 }
                  // Trigger conclusion visibility animation
                  analysisConclusion.classList.add('visible');

             }, delay); // Add extra delay after last step animation
         }


         // Initial display setup - trigger change event once on load
         templateSelect.dispatchEvent(new Event('change'));
    });
</script>
---