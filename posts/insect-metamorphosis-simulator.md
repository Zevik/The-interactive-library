---
title: "מסע הקסם: התגלגלות החיים של החרקים"
english_slug: insect-metamorphosis-simulator
category: "ביולוגיה"
tags: [מטמורפוזה, חרקים, מחזור חיים, זואולוגיה, ביולוגיה]
---
<h1>מסע הקסם: התגלגלות החיים של החרקים</h1>
<p class="subtitle">צאו למסע ויזואלי דרך השינויים המדהימים שחרקים עוברים במחזור חייהם.</p>

<div id="app" class="metamorphosis-simulator">
    <h2>בחרו את שביל ההתפתחות:</h2>
    <div class="insect-selector">
        <button class="action-button full-metamorphosis" data-insect="full">
            <span class="button-icon">🦋</span> מטמורפוזה מלאה (כמו פרפר או חיפושית)
        </button>
        <button class="action-button partial-metamorphosis" data-insect="partial">
            <span class="button-icon">🦗</span> מטמורפוזה חלקית (כמו חרגול או שפירית)
        </button>
    </div>

    <div class="stage-display">
        <div class="visual-stage-container">
             <!-- Visual representation of the stage will appear here -->
             <div id="visual-stage" class="stage-image-placeholder"></div>
        </div>
        <div class="stage-info">
            <h3>שלב נוכחי: <span id="current-stage-name">בחרו מסלול חיים...</span></h3>
            <p id="current-stage-description" class="stage-description"></p>
             <p id="progress-indicator" class="progress-text"></p>
        </div>
    </div>

    <button id="next-stage" class="action-button primary-button" disabled>
        <span class="button-icon">▶️</span> השלב הבא במסע
    </button>
    <button id="restart-cycle" class="action-button secondary-button" style="display: none;">
         <span class="button-icon">🔄</span> התחילו מסע חדש
    </button>
</div>

<button id="toggle-explanation" class="action-button info-button">
    <span class="button-icon">💡</span> למידע נוסף: מהי מטמורפוזה?
</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2>מהי מטמורפוזה? מסע ההתגלגלות הגדול</h2>
    <p>דמיינו יצור קטן שמשנה את צורתו לחלוטין, כמו קוסם ביולוגי! מטמורפוזה (מהמילה היוונית ל"שינוי צורה") היא תהליך התפתחות מרהיב שחרקים עוברים. זה לא סתם גדילה, אלא מהפך אמיתי במבנה הגוף, באורח החיים ולעיתים אפילו בסביבת המחיה. תהליך זה מאפשר לחרקים מגוון אדיר, הפחתת תחרות בין שלבים שונים, וניצול יעיל יותר של העולם מסביב.</p>

    <h3>שני מסלולי קסם עיקריים:</h3>

    <h4>מסלול הקסם המלא (מטמורפוזה מלאה - Holometabola)</h4>
    <p>זהו המהפך הדרמטי ביותר, מסע חיים הכולל ארבע תחנות ברורות, שכל אחת שונה מקודמתה לגמרי:</p>
    <ul>
        <li><strong>ביצה:</strong> נקודת ההתחלה. כאן הכל מתחיל בקפסולה זעירה, מוגנת ובדרך כלל מוסתרת היטב.</li>
        <li><strong>זחל (Larva):</strong> מכונה האכלן הגדול! זהו שלב הגדילה המטורפת. הזחל נראה שונה לחלוטין מהבוגר (חשבו על תולעת קטנה לעומת פרפר מפואר) וכל כולו ממוקד באכילה וגדילה מהירה. הוא משיל את עורו מספר פעמים ("התנשלויות") כדי להכיל את גופו הגדל.</li>
        <li><strong>גולם (Pupa):</strong> תא סודי לשינוי. זהו שלב המנוחה והארגון מחדש. בתוך הגולם מתרחש קסם ביולוגי בלתי נתפס – הגוף הישן נבנה מחדש לגמרי לגוף הבוגר. לרוב אין תנועה או אכילה בשלב זה, מבחוץ שקט, מבפנים מהפכה!</li>
        <li><strong>בוגר (Adult):</strong> השיא! היצור המכונף (לרוב) והמוכן להתרבות מגיח מתוך הגולם. מטרתו העיקרית בשלב זה היא למצוא בן זוג ולהפיץ את הדור הבא. הבוגר כבר לא גדל, אלא מתמקד במעוף, חיפוש מזון מתאים (לעתים שונה ממזון הזחל), והמשך המין.</li>
    </ul>
    <p><strong>אמני המטמורפוזה המלאה:</strong> פרפרים צבעוניים, עשים נחבאים, חיפושיות חסונות, זבובים זריזים, יתושים מזמזמים, נמלים חרוצות, דבורים עסוקות וצרעות מפוארות.</p>

    <h4>מסלול הקסם החלקי (מטמורפוזה חלקית - Hemimetabola)</h4>
    <p>מסע חיים פחות דרמטי, ללא תחנת הגולם. הדרך כוללת שלוש תחנות עיקריות:</p>
    <ul>
        <li><strong>ביצה:</strong> ההתחלה הרגילה, לרוב במים או קרוב אליהם, תלוי בחרק.</li>
        <li><strong>נימפה (Nymph):</strong> ה"בוגר המוקטן". הנימפה דומה במראה הכללי לבוגר, אבל היא קטנה יותר, חסרה כנפיים מפותחות ואיברי רבייה בשלים. היא חיה בדרך כלל באותה סביבה ואוכלת מזון דומה לבוגר. הנימפה גדלה בהדרגה דרך מספר התנשלויות, ובכל פעם מתקרבת יותר במראה ובמבנה לבוגר, מפתחת בהדרגה ניצני כנפיים עד שהן הופכות למפותחות.</li>
        <li><strong>בוגר (Adult):</strong> ההגעה ליעד! זהו השלב המיני, עם כנפיים מלאות (לרוב) ואיברי רבייה מוכנים לפעולה. הבוגר מתמקד ברבייה והמשך קיום המין.</li>
    </ul>
    <p><strong>ההבדל המרכזי בקסם:</strong> ההבדל הגדול הוא היעדר שלב הגולם המבודד ומשנה הצורה לחלוטין במטמורפוזה החלקית. שם, השינוי הדרגתי יותר והשלב הצעיר (נימפה) דומה הרבה יותר לבוגר מאשר הזחל לבוגר במטמורפוזה המלאה.</p>

    <h2>למה המטמורפוזה כל כך חשובה לחרקים?</h2>
    <p>היכולת לשנות צורה בצורה כה קיצונית נתנה לחרקים יתרון אבולוציוני עצום! היא אפשרה להם להתפצל ולהתמחות בניצול סביבות ומשאבים שונים לחלוטין בין שלב הזחל/נימפה לשלב הבוגר. זה הפחית תחרות "משפחתית" על מזון ומרחב, והגדיל את הסיכויים לשרוד ולהתרבות. זהו אחד הגורמים העיקריים למגוון המדהים והעצום של מיני החרקים על פני כדור הארץ!</p>
</div>

<style>
    :root {
        --primary-color: #4CAF50; /* Green - Nature */
        --primary-dark-color: #388E3C;
        --secondary-color: #FF9800; /* Orange - Transformation */
        --secondary-dark-color: #F57C00;
        --info-color: #03A9F4; /* Blue - Info */
        --info-dark-color: #0288D1;
        --background-color: #e8f5e9; /* Light Green */
        --card-background: #ffffff;
        --text-color: #212121;
        --soft-text-color: #757575;
        --border-color: #bdbdbd;
        --shadow-color: rgba(0, 0, 0, 0.1);
        --animation-duration: 0.6s;
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        background-color: var(--background-color);
        color: var(--text-color);
        direction: rtl;
        text-align: right;
        overflow-x: hidden; /* Prevent horizontal scroll from animations */
    }

    h1, h2, h3 {
        color: var(--primary-dark-color);
        text-align: center;
    }

    h1 {
        margin-bottom: 10px;
        font-size: 2em;
    }

    .subtitle {
        text-align: center;
        color: var(--soft-text-color);
        margin-bottom: 30px;
    }

    .metamorphosis-simulator {
        background-color: var(--card-background);
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 20px var(--shadow-color);
        margin-bottom: 30px;
        transition: all 0.5s ease-in-out;
    }

    .insect-selector {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-bottom: 30px;
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .action-button {
        padding: 12px 20px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.1em;
        transition: all 0.3s ease;
        display: inline-flex; /* Align icon and text */
        align-items: center;
        gap: 8px; /* Space between icon and text */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .action-button:hover {
        opacity: 0.9;
        transform: translateY(-2px);
    }

    .action-button:active {
        transform: translateY(0);
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .full-metamorphosis {
        background-color: #9C27B0; /* Purple */
        color: white;
    }

    .partial-metamorphosis {
        background-color: #00BCD4; /* Cyan */
        color: white;
    }

    .insect-selector button[data-selected="true"] {
        outline: 3px solid var(--secondary-dark-color); /* Highlight selected */
        box-shadow: 0 0 10px var(--secondary-color);
    }

    .stage-display {
        display: flex;
        flex-direction: column; /* Stack on mobile */
        align-items: center;
        gap: 20px;
        margin-top: 20px;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        min-height: 200px; /* Ensure space even when empty */
        background-color: #fcfcfc; /* Slightly lighter background */
        box-shadow: inset 0 1px 5px rgba(0, 0, 0, 0.05);
    }
    
    @media (min-width: 768px) {
         .stage-display {
             flex-direction: row; /* Side-by-side on larger screens */
             align-items: flex-start;
         }
         .stage-info {
             flex-grow: 1; /* Take remaining space */
         }
    }


    .visual-stage-container {
         width: 120px; /* Fixed size for visual */
         height: 120px;
         flex-shrink: 0; /* Don't shrink visual */
         display: flex;
         justify-content: center;
         align-items: center;
         border-radius: 50%; /* Circle container */
         background-color: rgba(var(--primary-color), 0.1); /* Light background */
         border: 2px dashed var(--primary-color);
         overflow: hidden; /* Clip anything outside the circle */
         position: relative; /* Needed for child positioning/animation */
    }

    .stage-image-placeholder {
         width: 100%;
         height: 100%;
         background-color: var(--secondary-color); /* Default placeholder color */
         border-radius: 50%;
         display: flex;
         justify-content: center;
         align-items: center;
         font-size: 3em;
         color: white;
         text-shadow: 1px 1px 3px var(--secondary-dark-color);
         transition: transform var(--animation-duration) ease-out, opacity var(--animation-duration) ease-out;
         opacity: 0; /* Start hidden for animation */
         transform: scale(0.5); /* Start small for animation */
         background-size: contain; /* Or cover, depending on image */
         background-position: center;
         background-repeat: no-repeat;
    }

    /* Specific styles for each stage visual - these would ideally be background-images */
    .stage-image-placeholder.stage-0 { background-color: #FFEB3B; content: '🥚'; } /* Egg - Yellow */
    .stage-image-placeholder.stage-1-full { background-color: #795548; content: '🐛'; } /* Larva - Brown */
    .stage-image-placeholder.stage-2-full { background-color: #607D8B; content: '🛡️'; } /* Pupa - Grey */
    .stage-image-placeholder.stage-3-full { background-color: #E91E63; content: '🦋'; } /* Adult Full - Pink */
    .stage-image-placeholder.stage-1-partial { background-color: #8BC34A; content: '🦗'; } /* Nymph - Light Green */
    .stage-image-placeholder.stage-2-partial { background-color: #4CAF50; content: '🌿'; } /* Adult Partial - Green */


    /* Animation for stage change */
    .stage-image-placeholder.active {
        opacity: 1;
        transform: scale(1);
    }
     .stage-image-placeholder.previous {
         opacity: 0;
         transform: scale(1.5) translateY(-20px); /* Fly out */
     }


    .stage-info {
         text-align: center;
         min-height: 100px; /* Prevent layout shifts */
    }


    #next-stage {
        display: block;
        margin-top: 20px;
        background-color: var(--primary-color);
        color: white;
        width: 100%; /* Full width button */
        box-sizing: border-box;
        font-size: 1.2em;
    }

    #next-stage:disabled {
        background-color: #e0e0e0;
        color: var(--soft-text-color);
        cursor: not-allowed;
        transform: none;
        box-shadow: none;
    }

    #restart-cycle {
        display: block;
        margin-top: 15px;
        background-color: var(--secondary-color);
        color: var(--text-color);
        width: 100%;
        box-sizing: border-box;
        font-size: 1.1em;
    }


    #toggle-explanation {
         display: block;
         margin: 20px auto; /* Center the button */
         background-color: var(--info-color);
         color: white;
    }


    .explanation-section {
        background-color: #e3f2fd; /* Very light blue */
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        margin-top: 20px;
        border-right: 5px solid var(--info-dark-color); /* Highlight section */
        transition: all 0.5s ease-in-out;
    }

    .explanation-section h2, .explanation-section h3 {
        color: var(--info-dark-color);
        text-align: right;
        border-bottom: 1px dashed rgba(var(--info-dark-color), 0.3);
        padding-bottom: 5px;
        margin-top: 20px;
    }

    .explanation-section h2:first-child {
        margin-top: 0;
    }

     .explanation-section ul {
         list-style-type: '🌱 '; /* Custom bullet */
         padding-right: 25px;
         margin-top: 15px;
     }

      .explanation-section li {
         margin-bottom: 12px;
         padding-right: 5px; /* Space after bullet */
      }

      .explanation-section strong {
          color: var(--primary-dark-color);
      }

      .progress-text {
          color: var(--soft-text-color);
          font-size: 0.9em;
          margin-top: 10px;
      }

       .button-icon {
           font-size: 1.2em; /* Adjust icon size */
       }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const insectSelector = document.querySelector('.insect-selector');
        const stageNameSpan = document.getElementById('current-stage-name');
        const stageDescriptionPara = document.getElementById('current-stage-description');
        const nextStageButton = document.getElementById('next-stage');
        const restartButton = document.getElementById('restart-cycle');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');
        const insectButtons = insectSelector.querySelectorAll('button');
        const visualStageElement = document.getElementById('visual-stage');
        const progressIndicator = document.getElementById('progress-indicator');

        let currentInsectType = null;
        let currentStageIndex = 0;

        const stages = {
            full: [
                { name: 'ביצה', description: 'נקודת ההתחלה הקטנה והמוגנת. הכל מתחיל כאן, בשקט... עד שהחיים מתעוררים מבפנים.', visualClass: 'stage-0', icon: '🥚' },
                { name: 'זחל', description: 'שלב הגדילה הפראי! היצור הצעיר מתמקד באכילה בלתי פוסקת וגדילה מהירה. הוא שונה מאוד מהבוגר ומשיל את עורו שוב ושוב.', visualClass: 'stage-1-full', icon: '🐛' },
                { name: 'גולם', description: 'תא הקסם לשינוי הגדול! מבחוץ נראה שקט, אך בפנים מתרחש מהפך מדהים - הגוף נבנה מחדש לגמרי לקראת החיים כבוגר.', visualClass: 'stage-2-full', icon: '🛡️' },
                { name: 'בוגר', description: 'השיא! היצור הבוגר מגיח, לרוב בעל כנפיים, ומוכן לממש את ייעודו העיקרי: רבייה והמשך הדור. הוא כבר לא גדל.', visualClass: 'stage-3-full', icon: '🦋' }
            ],
            partial: [
                { name: 'ביצה', description: 'ההתחלה. לרוב מוטלת במים או בסמוך למקור מים, ממתינה לרגע הבקיעה.', visualClass: 'stage-0', icon: '🥚' },
                { name: 'נימפה', description: 'ה"בוגר המוקטן" בתהליך גדילה. הנימפה דומה לבוגר, אך קטנה, חסרת כנפיים מלאות ועדיין לא יכולה להתרבות. היא גדלה בהדרגה דרך התנשלויות.', visualClass: 'stage-1-partial', icon: '🦗' },
                { name: 'בוגר', description: 'ההגעה ליעד! הבוגר עם כנפיים מפותחות ואיברי רבייה בשלים, מוכן להתחיל את פרק הרבייה והפצת המין.', visualClass: 'stage-2-partial', icon: '🌿' }
            ]
        };

        function updateDisplay() {
            // Hide restart button by default
            restartButton.style.display = 'none';

            if (!currentInsectType) {
                stageNameSpan.textContent = 'בחרו מסלול חיים...';
                stageDescriptionPara.textContent = 'כדי להתחיל את המסע, לחצו על אחד הכפתורים למעלה ובחרו סוג חרק.';
                progressIndicator.textContent = '';
                nextStageButton.disabled = true;
                 // Reset visual
                visualStageElement.className = 'stage-image-placeholder';
                visualStageElement.textContent = '';
                return;
            }

            const currentInsectStages = stages[currentInsectType];

            if (currentStageIndex < currentInsectStages.length) {
                // Display current stage
                const currentStage = currentInsectStages[currentStageIndex];
                stageNameSpan.textContent = currentStage.name;
                stageDescriptionPara.textContent = currentStage.description;
                progressIndicator.textContent = `שלב ${currentStageIndex + 1} מתוך ${currentInsectStages.length}`;

                // Update visual placeholder with animation
                visualStageElement.classList.remove('active', 'previous'); // Remove previous animation states
                 // Trigger reflow to restart animation if needed (simple hack)
                 void visualStageElement.offsetWidth;
                visualStageElement.className = 'stage-image-placeholder'; // Reset classes
                visualStageElement.classList.add(currentStage.visualClass, 'active');
                visualStageElement.textContent = currentStage.icon; // Set the icon/emoji

                nextStageButton.disabled = false;
                nextStageButton.style.display = 'block'; // Ensure next button is visible

            } else {
                // Cycle complete
                stageNameSpan.textContent = 'המסע הושלם!';
                stageDescriptionPara.textContent = 'ראיתם את כל שלבי החיים המדהימים של החרק שבחרתם.';
                progressIndicator.textContent = '';

                visualStageElement.classList.remove('active'); // Remove current stage visual
                 visualStageElement.className = 'stage-image-placeholder'; // Reset classes
                 visualStageElement.textContent = '🎉'; // Celebration icon

                nextStageButton.style.display = 'none'; // Hide next button
                restartButton.style.display = 'block'; // Show restart button
            }
        }

        // Function to start a new cycle
        function startNewCycle(insectType) {
             currentInsectType = insectType;
             currentStageIndex = 0; // Start from the first stage
             updateDisplay();
             // Add selected style to button
             insectButtons.forEach(btn => {
                 btn.dataset.selected = btn.dataset.insect === insectType ? 'true' : 'false';
             });
        }


        insectSelector.addEventListener('click', (event) => {
            const target = event.target.closest('button'); // Use closest to handle icon clicks
            if (target && target.dataset.insect) {
                const selectedInsect = target.dataset.insect;
                if (currentInsectType !== selectedInsect || currentStageIndex > 0) {
                    // Only reset/start if changing insect type or if not at the very beginning of the current type
                     startNewCycle(selectedInsect);
                } else {
                    // If already on the first stage of the selected type, just highlight the button
                    insectButtons.forEach(btn => {
                        btn.dataset.selected = btn === target ? 'true' : 'false';
                    });
                }
            }
        });

        nextStageButton.addEventListener('click', () => {
            if (currentInsectType && currentStageIndex < stages[currentInsectType].length) {
                 // Optional: Add outgoing animation class before incrementing stageIndex
                 visualStageElement.classList.add('previous');

                currentStageIndex++;
                // Add a small delay before updating display to allow outgoing animation
                setTimeout(updateDisplay, 300); // Match this with animation duration
            }
        });

        restartButton.addEventListener('click', () => {
            if (currentInsectType) {
                 startNewCycle(currentInsectType); // Restart the current cycle type
            }
        });


        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.innerHTML = isHidden
                 ? '<span class="button-icon">➖</span> הסתר הסבר מורחב'
                 : '<span class="button-icon">💡</span> למידע נוסף: מהי מטמורפוזה?';
        });

        // Initial state - set default text before selection
        updateDisplay();
         // Ensure explanation is hidden initially
         explanationDiv.style.display = 'none';
         toggleExplanationButton.innerHTML = '<span class="button-icon">💡</span> למידע נוסף: מהי מטמורפוזה?';
    });
</script>