---
title: "פריונים: הריקוד הקטלני של שינוי צורה"
english_slug: prions-lethal-structure-and-spread-simulation
category: "מדעי החיים / ביולוגיה"
tags:
  - פריונים
  - חלבונים
  - מחלות זיהומיות
  - מודלים ביולוגיים
  - סימולציה
  - מבנה חלבון
---
<h1>פריונים: הריקוד הקטלני של שינוי צורה</h1>
<p>האם ייתכן שמולקולה פשוטה, ללא כל מידע גנטי, מסוגלת לגרום למחלות חשוכות מרפא ואף להרוס רקמות שלמות? הכירו את הפריונים – חלבונים ש"התקלקלו" והפכו לסוכני הדבקה בלתי רגילים. בואו לחזות מקרוב בתהליך ההתפשטות המסתורי שלהם.</p>

<div id="app-container">
    <h2>סימולציית התפשטות פריונים</h2>
    <p class="simulation-intro">צפו כיצד פריונים בודדים (המסומנים באדום) ממירים חלבונים תקינים (בירוק) סביבם, ואיך התהליך האוטו-קטליטי מוביל להתפשטות מהירה ברקמה.</p>
    <div class="simulation-controls card">
        <div class="control-group">
            <label for="grid-size">גודל הרקמה (תאים):</label>
            <input type="number" id="grid-size" value="25" min="10" max="50" step="5">x
            <input type="number" id="grid-size-y" value="25" min="10" max="50" step="5">
        </div>
        <div class="control-group">
            <label for="initial-prions">מספר פריונים התחלתי:</label>
            <input type="number" id="initial-prions" value="5" min="1" max="20">
        </div>
        <div class="control-group">
            <label for="conversion-rate">הסתברות הדבקה במגע (%):</label>
            <input type="number" id="conversion-rate" value="60" min="10" max="100" step="5">
        </div>
         <div class="button-group">
            <button id="start-simulation" class="action-button">צעד סימולציה</button>
            <button id="run-simulation" class="action-button primary">הפעל אוטומטית</button>
            <button id="stop-simulation" class="action-button" disabled>עצור</button>
            <button id="reset-simulation" class="action-button secondary">אפס הכל</button>
         </div>
          <p class="reset-hint">לחצו על כפתור 'אפס הכל' או שנה פרמטר כדי להתחיל סימולציה חדשה.</p>
    </div>

    <div class="simulation-area">
        <div id="protein-grid" class="protein-grid">
            <!-- Grid cells will be generated here by JS -->
        </div>
        <div class="simulation-info card">
            <h3>מצב נוכחי:</h3>
            <p>זמן (צעדי סימולציה): <span id="simulation-time">0</span></p>
            <p>חלבונים תקינים (ירוק): <span id="normal-count">0</span></p>
            <p>פריונים (אדום): <span id="prion-count">0</span></p>
            <!-- Basic chart area -->
            <div class="chart-container">
                 <canvas id="spreadChart"></canvas>
            </div>
             <p class="chart-hint">עקבו אחר התפשטות הפריונים לאורך זמן.</p>
        </div>
    </div>
</div>

<style>
    :root {
        --primary-color: #3498db; /* Blue */
        --primary-dark: #2980b9;
        --secondary-color: #9b59b6; /* Purple */
        --secondary-dark: #8e44ad;
        --normal-protein: #2ecc71; /* Emerald green */
        --prion-protein: #e74c3c; /* Alizarin red */
        --background-color: #ecf0f1; /* Light grey */
        --card-background: #ffffff; /* White */
        --text-color: #333;
        --border-color: #bdc3c7; /* Silver */
        --grid-border: #7f8c8d; /* Asbestos */
    }

    #app-container {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        margin: 20px auto;
        max-width: 960px; /* Increased max-width slightly */
        direction: rtl;
        text-align: right;
        padding: 20px;
        background-color: var(--background-color);
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }

    h1, h2, h3 {
        text-align: center;
        color: var(--text-color);
        margin-bottom: 15px;
    }

    h1 {
        font-size: 2em;
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 10px;
    }

    h2 {
         font-size: 1.6em;
         margin-top: 20px;
    }

     .simulation-intro {
         text-align: center;
         margin-bottom: 30px;
         font-size: 1.1em;
         color: #555;
     }

    .card {
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
    }

    .simulation-controls {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        justify-content: center;
        align-items: center;
    }

    .control-group {
        display: flex;
        align-items: center;
        gap: 8px;
        background-color: #f5f5f5;
        padding: 8px 12px;
        border-radius: 5px;
        border: 1px solid #ddd;
    }

    .simulation-controls label {
        font-weight: bold;
        color: var(--text-color);
        font-size: 0.95em;
    }

    .simulation-controls input[type="number"] {
        width: 55px;
        padding: 6px;
        border: 1px solid var(--border-color);
        border-radius: 4px;
        font-size: 1em;
        text-align: center;
        -moz-appearance: textfield; /* Remove Firefox spinner */
    }
     .simulation-controls input[type="number"]::-webkit-outer-spin-button,
     .simulation-controls input[type="number"]::-webkit-inner-spin-button {
        -webkit-appearance: none; /* Remove Chrome/Safari spinner */
        margin: 0;
     }

    .button-group {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        justify-content: center;
    }

    .action-button {
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        min-width: 120px; /* Ensure consistent button width */
        text-align: center;
    }

    .action-button:hover:not(:disabled) {
        transform: translateY(-1px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
    }

    .action-button:active:not(:disabled) {
        transform: translateY(0);
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }

     .primary {
         background-color: var(--primary-color);
         color: white;
     }
     .primary:hover:not(:disabled) {
         background-color: var(--primary-dark);
     }

     .secondary {
         background-color: var(--border-color);
         color: var(--text-color);
     }
      .secondary:hover:not(:disabled) {
         background-color: #aeb6bf;
     }


     .action-button:disabled {
        background-color: #cccccc;
        color: #666666;
        cursor: not-allowed;
        box-shadow: none;
        transform: none;
     }

    .simulation-area {
        display: flex;
        flex-direction: column;
        gap: 30px;
        align-items: center;
    }

    .protein-grid {
        display: grid;
        border: 2px solid var(--grid-border);
        margin: 0 auto;
        background-color: var(--card-background);
        box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.1);
        transition: border-color 0.3s ease;
    }

     .protein-grid:hover {
         border-color: var(--primary-color);
     }

    .grid-cell {
        width: 18px; /* Slightly larger cells */
        height: 18px; /* Slightly larger cells */
        border: 1px dotted #eee; /* Subtle separator */
        box-sizing: border-box;
        cursor: pointer; /* Indicate interactivity */
        transition: background-color 0.5s ease, transform 0.2s ease; /* Smooth color change + pulse effect */
    }

    .grid-cell.normal {
        background-color: var(--normal-protein);
    }

    .grid-cell.prion {
        background-color: var(--prion-protein);
    }

     .grid-cell.converting {
         animation: pulse-prion 0.6s ease-out; /* Animation for conversion */
     }

     @keyframes pulse-prion {
         0% { transform: scale(1); opacity: 1; }
         50% { transform: scale(1.2); opacity: 0.8; background-color: orange; } /* Temporary color during conversion */
         100% { transform: scale(1); opacity: 1; }
     }


    .simulation-info {
        text-align: center;
        font-size: 1.05em;
        width: 100%;
        max-width: 400px; /* Limit info box width */
    }

    .simulation-info p {
        margin: 8px 0;
        padding: 3px;
        border-bottom: 1px dashed #eee;
    }
     .simulation-info p:last-child {
         border-bottom: none;
     }

    .simulation-info span {
        font-weight: bold;
        color: var(--primary-dark);
    }

    .chart-container {
        margin-top: 20px;
        width: 100%; /* Use full width of info box */
        max-width: 380px; /* Max width for the chart itself */
        margin-left: auto;
        margin-right: auto;
        background-color: #fff;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
     .chart-hint {
         font-size: 0.9em;
         color: #666;
         margin-top: 15px;
         text-align: center;
     }
      .reset-hint {
         font-size: 0.9em;
         color: #666;
         margin-top: 10px;
         text-align: center;
         width: 100%; /* Take full width in flex container */
      }


    #explanation-button {
        display: block;
        width: fit-content;
        margin: 30px auto 20px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        border: none;
        border-radius: 25px; /* Pill shape */
        cursor: pointer;
        background-color: var(--secondary-color);
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15);
    }

    #explanation-button:hover {
        background-color: var(--secondary-dark);
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
     #explanation-button:active {
         transform: translateY(0);
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
     }


    #explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: var(--card-background);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
        display: none; /* Initially hidden */
    }

    #explanation h3 {
        color: var(--primary-dark);
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 5px;
        font-size: 1.3em;
    }
    #explanation h3:first-child {
         margin-top: 0;
    }

     #explanation p {
         margin-bottom: 15px;
         color: #555;
     }

    @media (min-width: 768px) {
        .simulation-area {
            flex-direction: row;
            align-items: flex-start; /* Align items to the top */
            justify-content: center;
        }

        .protein-grid {
            flex-shrink: 0; /* Prevent grid from shrinking */
        }

        .simulation-info {
             flex-grow: 1; /* Allow info box to take remaining space */
             margin-right: 20px; /* Add space between grid and info */
             max-width: 300px; /* Smaller info box on wider screens */
        }
         .chart-container {
             max-width: none; /* Allow chart to use info box width */
         }
         .control-group {
             flex-grow: 1; /* Allow controls to grow */
             justify-content: center;
         }
          .button-group {
             width: 100%; /* Buttons take full width */
          }
           .reset-hint {
             text-align: right;
           }
    }

     @media (max-width: 767px) {
         .simulation-area {
             flex-direction: column;
         }
          .simulation-info {
             width: 100%;
             max-width: none; /* Remove max width on small screens */
          }
     }


</style>

<button id="explanation-button">הצג/הסתר את סיפור הפריונים המלא</button>

<div id="explanation">
    <h3>מהו פריון? מולקולה רגילה שהפכה למשנה צורה קטלני.</h3>
    <p>פריונים (Prions) הם חלבונים שאיבדו את צורתם התקינה וקיבלו מבנה מרחבי שגוי, שהופך אותם למסוכנים במיוחד. בניגוד לווירוסים או חיידקים שמכילים חומר גנטי, פריונים הם "אנומליה ביולוגית" – הם גורמים למחלות קטלניות אך ורק באמצעות שינוי צורתם. דמיינו מפתח ששינה את צורתו ומסוגל כעת "לשבור" מנעולים אחרים במקום לפתוח אותם, וגרוע מכך – לגרום למפתחות תקינים ליד ל"הישבר" גם כן.</p>

    <h3>החלבון התמים PrP: מבנה תקין (PrP<sup>C</sup>) מול מבנה פתולוגי (PrP<sup>Sc</sup>).</h3>
    <p>מקור הפריונים הוא חלבון טבעי, PrP (Prion Protein), שנמצא בגופנו ובגופי יונקים רבים, בעיקר בתאי מוח ועצב. במצבו התקין והמועיל (PrP<sup>C</sup>), יש לו מבנה מסוים הכולל "סלילים" (אלפא-הליקס). אולם, בתנאים מסוימים (שעדיין נחקרים), חלבון זה יכול לשנות את צורתו למבנה פתולוגי (PrP<sup>Sc</sup>), הכולל בעיקר "משטחים מקופלים" (בטא-שיטס). רצף חומצות האמינו בשני המצבים זהה, רק הקיפול שונה לגמרי. שינוי זה לא רק הורס את תפקוד החלבון המקורי, אלא הופך אותו לעמיד במיוחד לפירוק ומעניק לו יכולת "להדביק".</p>

    <h3>מנגנון ההמרה: כיצד פריון אחד בורא "צבא" של פריונים אחרים.</h3>
    <p>כאן טמונה הייחודיות המפחידה של הפריונים. כאשר פריון פתולוגי (PrP<sup>Sc</sup>) בא במגע פיזי עם חלבון PrP תקין (PrP<sup>C</sup>), הוא כופה עליו שינוי צורה. ה-PrP<sup>C</sup> התמים משנה את הקיפול שלו והופך גם הוא לפריון (PrP<sup>Sc</sup>). התהליך הוא אוטו-קטליטי: כל פריון חדש שנוצר מסוגל כעת להמיר חלבונים תקינים נוספים. זהו אפקט דומינו מולקולרי בלתי ניתן לעצירה, ללא צורך בחומר גנטי כלשהו.</p>

    <h3>התפשטות ונזק: אגרגטים קטלניים והרס המוח.</h3>
    <p>כשהפריונים מתרבים, הם לא רק ממירים חלבונים תקינים, אלא גם נוטים להתאגד יחד ליצירת מצבורים (אגרגטים או פיברילים) גדולים ועמידים במיוחד. מצבורים אלו גדלים ומתפשטים בתוך התא ובין תאים. הצטברות אגרגטים פריוניים, בעיקר בתאי מוח, גורמת נזק קשה: היא פוגעת בתפקוד התקין של התא, מובילה להיווצרות חללים מיקרוסקופיים ברקמה (מה שמעניק לה מראה ספוגי אופייני), גורמת לאובדן תאי עצב ולתגובה דלקתית. הנזק המצטבר פוגע במערכת העצבים ומוביל לתסמינים נוירולוגיים קשים ופטאליים.</p>

    <h3>דוגמאות למחלות פריוניות: מ"פרה משוגעת" למחלת קרויצפלד-יעקב.</h3>
    <p>מחלות פריוניות, הידועות גם בשם TSEs (Transmissible Spongiform Encephalopathies), הן נדירות באדם אך תמיד קטלניות. המוכרת ביותר היא מחלת קרויצפלד-יעקב (CJD), שיכולה להופיע באופן ספורדי, גנטי או נרכש. וריאנט חדש של CJD (vCJD) קושר בסוף המאה ה-20 למחלת הפרה המשוגעת (BSE) בבקר, שנגרמה ככל הנראה מאכילת מזון שהכיל רקמות מבעלי חיים נגועים. מחלות פריוניות נוספות כוללות סקרפי בכבשים ו-CWD באיילים.</p>

    <h3>האתגר הגדול: מדוע פריונים כמעט בלתי ניתנים לעצירה ולריפוי.</h3>
    <p>הטיפול במחלות פריוניות הוא אתגר עצום: הפריונים מבוססים על חלבון טבעי של הגוף, ולכן מערכת החיסון לא מזהה אותם כ"זרים" ואינה תוקפת אותם ביעילות. הם עמידים להפליא בפני שיטות סטנדרטיות לחיטוי (חום, קרינה, כימיקלים רבים) שמחסלות חיידקים ווירוסים. ברגע שהתסמינים מופיעים, הנזק המוחי לרוב בלתי הפיך. נכון להיום, אין טיפול יעיל שיכול לעצור את התקדמות המחלה, והיא מובילה בהכרח למוות.</p>

    <h3>סימולציות ומודלים: הצצה אל הדינמיקה הנסתרת.</h3>
    <p>כמו הסימולציה שבה התנסיתם, מודלים חישוביים עוזרים לנו להמחיש ולהבין את הדינמיקה של התפשטות הפריונים בקנה מידה גדול יותר. הם מדגימים כיצד שינויים בפרמטרים התחלתיים (כמו מספר פריונים ראשוני או קצב ההמרה) יכולים להשפיע דרמטית על מהירות ההתפשטות ועל הסיכוי להגיע למצב בו כל הרקמה נגועה. זוהי דרך עוצמתית לדמיין תהליכים מולקולריים מורכבים שאינם נראים לעין.</p>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    const gridContainer = document.getElementById('protein-grid');
    const simulationTimeSpan = document.getElementById('simulation-time');
    const normalCountSpan = document.getElementById('normal-count');
    const prionCountSpan = document.getElementById('prion-count');
    const startButton = document.getElementById('start-simulation');
    const runButton = document.getElementById('run-simulation');
    const stopButton = document.getElementById('stop-simulation');
    const resetButton = document.getElementById('reset-simulation');
    const gridSizeInput = document.getElementById('grid-size');
    const gridSizeYInput = document.getElementById('grid-size-y');
    const initialPrionsInput = document.getElementById('initial-prions');
    const conversionRateInput = document.getElementById('conversion-rate');
    const explanationButton = document.getElementById('explanation-button');
    const explanationDiv = document.getElementById('explanation');
    const chartCanvas = document.getElementById('spreadChart');

    let grid = [];
    let gridSizeX = 25; // Increased default size
    let gridSizeY = 25; // Increased default size
    let initialPrions = 5; // Increased default initial prions
    let conversionRate = 0.6; // probability 0-1 (default 60%)
    let simulationTime = 0;
    let normalCount = 0;
    let prionCount = 0;
    let isRunning = false;
    let simulationInterval = null;
    let chart = null;
    let chartData = {
        labels: [],
        datasets: [
            {
                label: 'פריונים',
                data: [],
                borderColor: 'var(--prion-protein)', /* Use CSS variable */
                backgroundColor: 'rgba(231, 76, 60, 0.2)', /* Semi-transparent fill */
                fill: true, /* Fill area under the line */
                tension: 0.3, /* Add some curve to the line */
            },
            {
                label: 'תקינים',
                data: [],
                borderColor: 'var(--normal-protein)', /* Use CSS variable */
                backgroundColor: 'rgba(46, 204, 113, 0.2)',
                fill: true,
                 tension: 0.3,
            }
        ]
    };

    // Initialize or update Chart
    function initializeChart() {
         if (chart) {
             chart.destroy();
         }
         chartData.labels = [];
         chartData.datasets[0].data = [];
         chartData.datasets[1].data = [];

        chart = new Chart(chartCanvas, {
            type: 'line',
            data: chartData,
            options: {
                responsive: true,
                maintainAspectRatio: false,
                animation: {
                    duration: 500, // Animation duration for chart updates
                    easing: 'linear'
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'כמות חלבונים',
                            font: { size: 14 }
                        },
                        stacked: true, /* Stacked area chart */
                         max: gridSizeX * gridSizeY /* Max Y is total cells */
                    },
                    x: {
                         title: {
                            display: true,
                            text: 'זמן (צעדי סימולציה)',
                            font: { size: 14 }
                         }
                    }
                },
                 plugins: {
                    legend: {
                        labels: {
                            usePointStyle: true,
                            font: { size: 12 },
                             boxWidth: 10, /* Smaller legend box */
                        },
                         rtl: true,
                         textDirection: 'rtl',
                    },
                    tooltip: {
                        rtl: true,
                         textDirection: 'rtl',
                         callbacks: { /* Custom tooltips */
                             label: function(context) {
                                 let label = context.dataset.label || '';
                                 if (label) {
                                     label += ': ';
                                 }
                                 if (context.parsed.y !== null) {
                                     label += context.parsed.y.toLocaleString();
                                 }
                                 return label;
                             }
                         }
                    },
                     title: { /* Add chart title */
                         display: true,
                         text: 'התפשטות פריונים לאורך זמן',
                         font: { size: 16 },
                         padding: { bottom: 15 }
                     }
                },
                hover: {
                    mode: 'nearest',
                    intersect: true
                }
            }
        });
         chartCanvas.style.height = '250px'; // Adjusted height for better look
         chartCanvas.style.width = '100%'; // Use container width
    }


    function createGrid() {
        gridContainer.innerHTML = '';
        gridSizeX = parseInt(gridSizeInput.value);
        gridSizeY = parseInt(gridSizeYInput.value);
        initialPrions = parseInt(initialPrionsInput.value);
        conversionRate = parseInt(conversionRateInput.value) / 100;

         // Validation: Max initial prions is total cells
        const totalCells = gridSizeX * gridSizeY;
        if (initialPrions > totalCells) {
            initialPrions = totalCells;
            initialPrionsInput.value = initialPrions; // Update input field
        }
         // Validation: Min grid size
         if (gridSizeX < 10) gridSizeX = 10; gridSizeInput.value = gridSizeX;
         if (gridSizeY < 10) gridSizeY = 10; gridSizeYInput.value = gridSizeY;
         // Validation: Min initial prions
         if (initialPrions < 1) initialPrions = 1; initialPrionsInput.value = initialPrions;
         // Validation: Conversion rate
          if (conversionRate < 0.1) conversionRate = 0.1; conversionRateInput.value = conversionRate * 100;


        gridContainer.style.gridTemplateColumns = `repeat(${gridSizeX}, 1fr)`;
        gridContainer.style.gridTemplateRows = `repeat(${gridSizeY}, 1fr)`;

        grid = [];
        normalCount = totalCells;
        prionCount = 0;
        simulationTime = 0;

        for (let i = 0; i < totalCells; i++) {
            const cell = document.createElement('div');
            cell.classList.add('grid-cell', 'normal');
             cell.dataset.index = i; // Store index for click handling
             cell.addEventListener('click', handleCellClick); // Add click listener
            gridContainer.appendChild(cell);
            grid.push({ element: cell, isPrion: false });
        }

        // Add initial prions randomly
        let prionIndices = new Set();
        while (prionIndices.size < initialPrions) {
            let randomIndex = Math.floor(Math.random() * totalCells);
            // Ensure the cell is initially normal before making it a prion
            if (!grid[randomIndex].isPrion) {
                 setCellAsPrion(randomIndex); // Use helper function
                 prionIndices.add(randomIndex);
            }
        }

        // Recalculate counts based on final state
         normalCount = 0;
         prionCount = 0;
         grid.forEach(cell => {
             if(cell.isPrion) prionCount++;
             else normalCount++;
         });


        updateDisplay();
        initializeChart();
        updateChart(); // Add initial state to chart
    }

     function setCellAsPrion(index) {
        if (!grid[index].isPrion) {
            grid[index].isPrion = true;
            grid[index].element.classList.remove('normal');
            grid[index].element.classList.add('prion');
             // Add animation class briefly
            grid[index].element.classList.add('converting');
            setTimeout(() => {
                 grid[index].element.classList.remove('converting');
            }, 600); // Match animation duration
        }
     }

      function setCellAsNormal(index) {
         if (grid[index].isPrion) {
             grid[index].isPrion = false;
             grid[index].element.classList.remove('prion');
             grid[index].element.classList.add('normal');
              // No 'converting' animation for going back to normal in this model
         }
      }


    function updateDisplay() {
        simulationTimeSpan.textContent = simulationTime;
        normalCountSpan.textContent = normalCount.toLocaleString(); // Add formatting
        prionCountSpan.textContent = prionCount.toLocaleString(); // Add formatting
    }

    function updateChart() {
         // Only add point if time has passed or this is the first point (time 0)
         if (simulationTime > 0 || chartData.labels.length === 0) {
             chartData.labels.push(simulationTime);
             chartData.datasets[0].data.push(prionCount);
             chartData.datasets[1].data.push(normalCount);
             chart.update();
         }
    }

    function getNeighbors(index) {
        const neighbors = [];
        const x = index % gridSizeX;
        const y = Math.floor(index / gridSizeX);

        // Using delta arrays for cleaner neighbor finding (including diagonals if desired, but sticking to 4-way)
        const dx = [-1, 1, 0, 0];
        const dy = [0, 0, -1, 1];

        for (let i = 0; i < dx.length; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (nx >= 0 && nx < gridSizeX && ny >= 0 && ny < gridSizeY) {
                const neighborIndex = ny * gridSizeX + nx;
                neighbors.push(grid[neighborIndex]);
            }
        }
        return neighbors;
    }

    function simulationStep() {
        if (prionCount === gridSizeX * gridSizeY || normalCount === 0) {
             stopSimulation();
             return;
        }

        const conversionsThisStep = []; // Store indices to convert

        grid.forEach((cell, index) => {
            // Only normal proteins can be converted, and only if simulation is running (for safety)
            if (!cell.isPrion && isRunning || (!cell.isPrion && !isRunning)) { // Allow step-by-step when not running
                const neighbors = getNeighbors(index);
                const hasPrionNeighbor = neighbors.some(neighbor => neighbor.isPrion);

                if (hasPrionNeighbor) {
                    // Probability of conversion if adjacent to a prion
                    if (Math.random() < conversionRate) {
                        conversionsThisStep.push(index);
                    }
                }
            }
        });

        // Apply changes after checking all cells
        conversionsThisStep.forEach(index => {
            setCellAsPrion(index);
        });

        // Update counts
        prionCount += conversionsThisStep.length;
        normalCount -= conversionsThisStep.length;
        simulationTime++;

        updateDisplay();
        updateChart();

        // Check for end condition again after updates
         if (normalCount <= 0) { // Check if normal proteins are depleted
             stopSimulation();
         }
    }

    function startAutoSimulation() {
        if (isRunning) return;
        isRunning = true;
        startButton.disabled = true;
        runButton.disabled = true;
        stopButton.disabled = false;
        // Adjust interval for perceived speed, lower is faster
        simulationInterval = setInterval(simulationStep, 80); // Run step every 80ms for slightly faster auto
    }

    function stopSimulation() {
        isRunning = false;
        clearInterval(simulationInterval);
        startButton.disabled = false;
        runButton.disabled = false;
        stopButton.disabled = true;
    }

    function resetSimulation() {
        stopSimulation();
        createGrid(); // Re-initialize the grid and counts
         // Ensure buttons are enabled after reset
        startButton.disabled = false;
        runButton.disabled = false;
        stopButton.disabled = true;
    }

     // Handle clicks on grid cells (for manual interaction)
     function handleCellClick(event) {
         if (isRunning) return; // Don't allow changes during auto run

         const index = parseInt(event.target.dataset.index);
         if (grid[index].isPrion) {
             // Option: Turn prion back to normal (simplification for interaction)
             setCellAsNormal(index);
             prionCount--;
             normalCount++;
         } else {
             // Option: Turn normal into a prion
             setCellAsPrion(index);
             prionCount++;
             normalCount--;
         }
         updateDisplay();
         // Don't update chart on individual clicks unless simulation step happens
         // The click is primarily for setting initial state or manual exploration in step mode
     }


    // Event Listeners
    startButton.addEventListener('click', () => {
        if (!isRunning) { // Only step if not in auto mode
            simulationStep();
        }
    });
    runButton.addEventListener('click', startAutoSimulation);
    stopButton.addEventListener('click', stopSimulation);
    resetButton.addEventListener('click', resetSimulation);

     // Reset simulation when parameters change
     gridSizeInput.addEventListener('change', resetSimulation);
     gridSizeYInput.addEventListener('change', resetSimulation);
     initialPrionsInput.addEventListener('change', resetSimulation);
     conversionRateInput.addEventListener('change', resetSimulation);


    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        // Smoothly toggle visibility (optional, can be done with CSS transitions)
         if (isHidden) {
             explanationDiv.style.opacity = 0;
             explanationDiv.style.height = 'auto'; // Allow height calculation
             const height = explanationDiv.clientHeight; // Get height
             explanationDiv.style.height = 0; // Reset height for transition
             explanationDiv.style.overflow = 'hidden';
             explanationDiv.style.transition = 'height 0.5s ease-out, opacity 0.5s ease-out';
             setTimeout(() => {
                 explanationDiv.style.height = height + 'px';
                 explanationDiv.style.opacity = 1;
             }, 50); // Small delay to allow height reset
              explanationButton.textContent = 'הסתר את סיפור הפריונים המלא';
         } else {
             explanationDiv.style.height = explanationDiv.clientHeight + 'px'; // Set current height
             setTimeout(() => {
                  explanationDiv.style.height = 0;
                  explanationDiv.style.opacity = 0;
             }, 50);
              explanationButton.textContent = 'הצג את סיפור הפריונים המלא';
         }

         explanationDiv.addEventListener('transitionend', function handler() {
             if (explanationDiv.style.height === '0px') {
                 explanationDiv.style.display = 'none';
                 explanationDiv.style.removeProperty('overflow');
             } else {
                  explanationDiv.style.removeProperty('height'); // Remove fixed height after opening
             }
              explanationDiv.style.removeProperty('transition');
             explanationDiv.removeEventListener('transitionend', handler);
         });
    });


    // Initial setup
    createGrid();

</script>
```