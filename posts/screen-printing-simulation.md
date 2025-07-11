---
title: "הדמיית הדפסת רשת: קסם השכבות והצבע"
english_slug: screen-printing-simulation
category: "אמנות ועיצוב"
tags: [הדפסה, הדמיה, צבע, עיצוב, גרפיקה, אמנות, יצירה]
---
# הדפסת רשת (Screen Printing): גלו את הקסם של הפרדת צבעים ושכבות!

דמיינו רגע: אתם מעצבים גרפיקה מרהיבה, אבל כדי להדפיס אותה על חולצה או נייר בטכניקת הדפסת רשת, אתם לא פשוט שולחים קובץ למדפסת. במקום זאת, אתם מפרקים את היצירה שלכם לשכבות נפרדות – שכבה לכל צבע! כל שכבה כזו הופכת ל"מסך" או "שבלונה" ייעודית, ורק על ידי הדפסה מדויקת של כל צבע בתורו, שכבה על גבי שכבה, נחשפת התמונה הסופית במלוא הדרה. מוכנים לראות איך הקסם הזה קורה? בואו נתנסה ביחד!

<div class="screen-printing-simulation">
    <div class="simulation-areas">
        <div class="area source-graphic">
            <h3>✨ הגרפיקה הסופית (המטרה!)</h3>
            <div class="graphic-container final-result">
                <!-- Shapes representing the final layered image -->
                <div class="shape yellow-square source-shape"></div>
                <div class="shape magenta-triangle source-shape"></div>
                <div class="shape cyan-circle source-shape"></div>
            </div>
        </div>
        <div class="area color-separations">
            <h3>🎨 הפרדות צבע (ה"מסכים" שלנו)</h3>
            <div class="separation-container">
                 <div class="separation">
                     <h4>ציאן (כחול)</h4>
                     <div class="shape cyan-circle separation-shape"></div>
                 </div>
                 <div class="separation">
                     <h4>מג'נטה (אדום)</h4>
                     <div class="shape magenta-triangle separation-shape"></div>
                 </div>
                 <div class="separation">
                      <h4>צהוב</h4>
                      <div class="shape yellow-square separation-shape"></div>
                 </div>
            </div>
        </div>
        <div class="area printed-result">
            <h3>🖨️ תוצאת ההדפסה (המעבדה שלכם!)</h3>
            <div id="result-container" class="graphic-container print-target">
                <!-- Layers will be added here by JS -->
            </div>
        </div>
    </div>
    <div class="controls">
        <button id="print-cyan" class="print-button cyan">הדפס ציאן</button>
        <button id="print-magenta" class="print-button magenta">הדפס מג'נטה</button>
        <button id="print-yellow" class="print-button yellow">הדפס צהוב</button>
        <button id="reset-print" class="reset-button">התחל מחדש 🔄</button>
    </div>
</div>

<style>
    :root {
        --color-cyan: #00aedb; /* Brighter Cyan */
        --color-magenta: #f60085; /* Brighter Magenta */
        --color-yellow: #fff000; /* Brighter Yellow */
        --color-dark: #2c3e50;
        --color-light: #ecf0f1;
        --color-primary-button: #3498db;
        --color-reset-button: #e74c3c;
        --border-radius: 8px;
        --shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    body { /* Added basic body style for better default rendering */
        margin: 0;
        background-color: #f4f7f6;
        font-family: 'Rubik', sans-serif; /* Using a more modern font (assumes it's available or linked) */
        color: var(--color-dark);
    }

    h1, h3, h4 {
        color: var(--color-dark);
        text-align: center;
    }

    .screen-printing-simulation {
        background-color: var(--color-light);
        padding: 30px;
        border-radius: var(--border-radius);
        box-shadow: var(--shadow);
        max-width: 960px; /* Slightly wider */
        margin: 30px auto;
        direction: rtl;
        text-align: right;
        border: 1px solid #bdc3c7;
    }

    .simulation-areas {
        display: flex;
        flex-wrap: wrap;
        gap: 30px; /* Increased gap */
        margin-bottom: 30px;
        justify-content: center;
        align-items: flex-start; /* Align areas to the top */
    }

    .area {
        background-color: #fff;
        border: 1px solid #ddd;
        border-radius: var(--border-radius);
        padding: 20px; /* Increased padding */
        flex: 1;
        min-width: 280px; /* Slightly wider minimum */
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        transition: transform 0.3s ease; /* Add hover effect */
    }

     .area:hover {
         transform: translateY(-5px);
     }

    .area h3, .separation h4 {
        color: var(--color-dark);
        margin-top: 0;
        margin-bottom: 20px; /* Increased margin */
        font-size: 1.3rem;
    }

    .separation h4 {
         font-size: 1rem;
         margin-bottom: 10px;
         color: #555;
    }


    .graphic-container {
        width: 200px; /* Increased size */
        height: 200px; /* Increased size */
        position: relative;
        border: 2px dashed #bdc3c7; /* Stronger dashed border */
        background-color: #ecf0f1; /* Lighter background */
        overflow: hidden;
        border-radius: var(--border-radius);
    }

    .separation-container {
        display: flex;
        flex-direction: column;
        gap: 15px; /* Increased gap */
        height: auto;
        border: none;
        background-color: transparent;
        align-items: stretch; /* Stretch items to fill container width */
        width: 100%; /* separations take full width of their area */
    }

    .separation {
        background-color: #fefefe; /* Lighter background for separation box */
        border: 1px solid #dde;
        border-radius: var(--border-radius);
        padding: 15px;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: auto; /* Auto width based on container */
        transition: box-shadow 0.2s ease;
    }

    .separation:hover {
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }


    .separation-shape {
        width: 100px; /* Increased size */
        height: 100px; /* Increased size */
        position: static;
        margin: 10px auto 0;
        opacity: 0.9; /* Slight opacity to suggest a screen */
    }


    .shape {
        position: absolute;
        opacity: 1;
    }

    /* Define shapes and colors - using CSS variables */
    .cyan-circle {
        width: 120px; /* Increased size */
        height: 120px; /* Increased size */
        border-radius: 50%;
        background-color: var(--color-cyan);
    }

    .magenta-triangle {
         width: 0;
         height: 0;
         border-left: 70px solid transparent; /* Adjusted size */
         border-right: 70px solid transparent; /* Adjusted size */
         border-bottom: 120px solid var(--color-magenta); /* Adjusted size */
    }

    .yellow-square {
        width: 120px; /* Increased size */
        height: 120px; /* Increased size */
        background-color: var(--color-yellow);
    }

    /* Positioning for the Source Graphic (final result) - Adjusted for larger size */
    .source-graphic .graphic-container .cyan-circle { top: 50px; left: 30px; }
    .source-graphic .graphic-container .magenta-triangle { top: 40px; left: 70px; }
    .source-graphic .graphic-container .yellow-square { top: 80px; left: 90px; }


     /* Positioning for layers added to the Result - Adjusted to match source graphic */
    .printed-result .graphic-container .layer-cyan {
         width: 120px; height: 120px; border-radius: 50%; background-color: var(--color-cyan);
         top: 50px; left: 30px;
         animation: fadeInScale 0.5s ease forwards; /* Add animation */
         mix-blend-mode: multiply; /* Simulate color mixing */
    }
     .printed-result .graphic-container .layer-magenta {
         width: 0; height: 0;
         border-left: 70px solid transparent; border-right: 70px solid transparent; border-bottom: 120px solid var(--color-magenta);
         top: 40px; left: 70px;
         animation: fadeInScale 0.5s ease forwards; /* Add animation */
         mix-blend-mode: multiply; /* Simulate color mixing */
     }
     .printed-result .graphic-container .layer-yellow {
         width: 120px; height: 120px; background-color: var(--color-yellow);
         top: 80px; left: 90px;
         animation: fadeInScale 0.5s ease forwards; /* Add animation */
         mix-blend-mode: multiply; /* Simulate color mixing */
     }

     /* Animation for layers appearing */
     @keyframes fadeInScale {
         from { opacity: 0; transform: scale(0.8); }
         to { opacity: 1; transform: scale(1); }
     }

     /* Animation for button click feedback */
     @keyframes pulse {
         0% { transform: scale(1); }
         50% { transform: scale(1.05); }
         100% { transform: scale(1); }
     }


    .controls {
        text-align: center;
        margin-top: 30px; /* Increased margin */
    }

    .controls button {
        padding: 12px 20px; /* Increased padding */
        margin: 8px; /* Increased margin */
        border: none;
        border-radius: var(--border-radius);
        cursor: pointer;
        font-size: 1.1rem; /* Slightly larger font */
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.2s ease;
        color: white;
        font-weight: bold;
        box-shadow: 0 2px 5px rgba(0,0,0,0.15);
    }

    .controls .print-button {
        background-color: var(--color-primary-button);
    }
    .controls .print-button.cyan { background-color: var(--color-cyan); }
    .controls .print-button.magenta { background-color: var(--color-magenta); }
    .controls .print-button.yellow { background-color: var(--color-yellow); }


    .controls .reset-button {
        background-color: var(--color-reset-button);
    }


    .controls button:hover {
        opacity: 0.9;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

     .controls button:active {
        transform: scale(0.98);
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    /* Class added by JS for click animation */
    .pulsing {
        animation: pulse 0.3s ease;
    }


    #explanationButton {
        display: block;
        margin: 30px auto; /* Increased margin */
        padding: 12px 25px; /* Increased padding */
        border: 2px solid var(--color-primary-button);
        border-radius: var(--border-radius);
        background-color: transparent;
        color: var(--color-primary-button);
        cursor: pointer;
        font-size: 1.1rem; /* Slightly larger font */
        transition: background-color 0.3s ease, color 0.3s ease, box-shadow 0.2s ease;
        font-weight: bold;
    }

    #explanationButton:hover {
        background-color: var(--color-primary-button);
        color: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }

    #explanationContent {
        margin-top: 20px;
        padding: 20px;
        border: 1px dashed var(--color-primary-button);
        border-radius: var(--border-radius);
        background-color: #eef7ff; /* Lighter background */
        display: none; /* Hidden by default */
        direction: rtl;
        text-align: right;
        line-height: 1.7; /* Improved readability */
    }

    #explanationContent h3 {
        margin-top: 0;
        color: var(--color-dark);
        font-size: 1.4rem;
        margin-bottom: 15px;
    }

    #explanationContent p {
        margin-bottom: 15px;
        color: #555;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .simulation-areas {
            flex-direction: column;
            align-items: stretch;
        }
        .area {
            min-width: auto;
        }
        .graphic-container {
            width: 160px;
            height: 160px;
        }
        .source-graphic .graphic-container .cyan-circle,
        .printed-result .graphic-container .layer-cyan { width: 90px; height: 90px; top: 40px; left: 20px; }

        .source-graphic .graphic-container .magenta-triangle,
        .printed-result .graphic-container .layer-magenta { border-left: 50px solid transparent; border-right: 50px solid transparent; border-bottom: 85px solid var(--color-magenta); top: 30px; left: 60px; }

        .source-graphic .graphic-container .yellow-square,
         .printed-result .graphic-container .layer-yellow { width: 90px; height: 90px; top: 60px; left: 70px; }

         .separation-shape {
             width: 70px;
             height: 70px;
         }
         .separation .magenta-triangle {
             border-left: 40px solid transparent; border-right: 40px solid transparent; border-bottom: 70px solid var(--color-magenta);
         }
    }
</style>

<button id="explanationButton">הצגת הסבר מפורט על הדפסת רשת</button>

<div id="explanationContent">
    <h3>מה באמת קורה בהדפסת רשת?</h3>
    <p>הדפסת רשת (המכונה גם Silkscreen או Serigraphy) היא אחת מטכניקות ההדפסה הוותיקות והוורסטיליות ביותר. הרעיון פשוט אך גאוני: דיו נדחף דרך רשת עדינה המתוחה על מסגרת (פעם משי, כיום סיבים סינתטיים עמידים). חלקים מהרשת נאטמים באמצעות אמולסיה רגישה לאור (או שבלונה פיזית), וכך הדיו עובר רק דרך החלקים "הפתוחים" ברשת ומועבר אל המצע שמתחת (טקסטיל, נייר, פלסטיק, עץ – כמעט כל דבר!).</p>

    <h3>הקסם של הפרדת צבעים</h3>
    <p>כדי ליצור תמונה צבעונית ומורכבת, אנו מפרקים אותה לצבעי היסוד המרכיבים אותה (לרוב משתמשים בצבעי CMYK – ציאן, מג'נטה, צהוב, ושחור – או בצבעי ספוט ייעודיים כמו במערכת Pantone). לכל צבע בתמונה מכינים מסך נפרד עם השבלונה הייעודית שלו. תהליך ההדפסה הוא למעשה סדרה של הדפסות, כשהמדפיס (או המכונה) מניח את המצע, מדפיס צבע אחד דרך המסך המתאים לו, מרים את המסך, מייבש את הדיו (לפעמים חלקית), וממשיך לצבע הבא עם המסך שלו. השכבות נבנות בהדרגה, ורק בסוף התהליך נחשפת התמונה השלמה, המורכבת משילובי הצבעים.</p>
    <p><strong>בסימולציה שלנו:</strong> כל כפתור "הדפס" מייצג את הפעולה של לקיחת מסך צבע ספציפי והדפסתו על "המצע" שלכם בתיבת "תוצאת ההדפסה". אתם יכולים להדפיס את הצבעים בכל סדר שתבחרו ולראות כיצד הם נערמים ומתחברים כדי ליצור את התמונה המקורית. שימו לב שאנו משתמשים ב-<code>mix-blend-mode: multiply</code> ב-CSS כדי לדמות באופן ויזואלי איך צבעים חצי שקופים (כמו אלה שבמדפסת הביתית) מתערבבים. הדפסת רשת מקצועית לרוב משתמשת בדיו אטום יותר, והסדר בו מדפיסים את השכבות משפיע על התוצאה הסופית! הסימולציה הזו נותנת טעימה כיצד פירוק הדימוי לשכבות צבע בודדות הוא הצעד הראשון והקריטי בתהליך.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const resultContainer = document.getElementById('result-container');
        const printCyanButton = document.getElementById('print-cyan');
        const printMagentaButton = document.getElementById('print-magenta');
        const printYellowButton = document.getElementById('print-yellow');
        const resetButton = document.getElementById('reset-print'); // Changed variable name for clarity
        const explanationButton = document.getElementById('explanationButton');
        const explanationContent = document.getElementById('explanationContent');

        // HTML strings for the layers to be added
        // Use unique classes for the layers in the result container
        const cyanLayerHtml = '<div class="shape layer-cyan"></div>';
        const magentaLayerHtml = '<div class="shape layer-magenta"></div>';
        const yellowLayerHtml = '<div class="shape layer-yellow"></div>';

        // Map buttons to layer HTML and corresponding separation element for pulsing effect
        const printButtons = [
            { button: printCyanButton, html: cyanLayerHtml, separationSelector: '.separation .cyan-circle' },
            { button: printMagentaButton, html: magentaLayerHtml, separationSelector: '.separation .magenta-triangle' },
            { button: printYellowButton, html: yellowLayerHtml, separationSelector: '.separation .yellow-square' }
        ];

        printButtons.forEach(({ button, html, separationSelector }) => {
            button.addEventListener('click', () => {
                // Add pulsing animation to the corresponding separation shape
                const separationShape = document.querySelector(separationSelector);
                if (separationShape) {
                    separationShape.classList.add('pulsing');
                    // Remove the class after the animation ends
                    separationShape.addEventListener('animationend', () => {
                        separationShape.classList.remove('pulsing');
                    }, { once: true }); // Use { once: true } to remove listener after one trigger
                }

                // Add the layer to the result container
                // We can append multiple times to show the *action* of printing,
                // but the mix-blend-mode makes it look correct for blending simulation.
                resultContainer.innerHTML += html;

                // Optional: Scroll to see the result if it's off-screen
                resultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            });
        });

        resetButton.addEventListener('click', () => {
            resultContainer.innerHTML = ''; // Clear all layers from the result container
        });

        // Explanation button logic
        explanationButton.addEventListener('click', () => {
            const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
            explanationContent.style.display = isHidden ? 'block' : 'none';
            explanationButton.textContent = isHidden ? 'הסתר הסבר על הדפסת רשת' : 'הצגת הסבר מפורט על הדפסת רשת';
        });

         // Initial state for explanation
         explanationContent.style.display = 'none';
         explanationButton.textContent = 'הצגת הסבר מפורט על הדפסת רשת';
    });
</script>