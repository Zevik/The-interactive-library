---
title: "ניהול מוזיאון: האמנות שמאחורי הקלעים"
english_slug: museum-management-curation-vs-preservation-v2
category: "ניהול תרבות ואמנות"
tags:
  - מוזיאונים
  - אצירה
  - שימור
  - ניהול תרבות
  - תערוכות
  - סימולציה
---
<div class="museum-container">
    <header>
        <h1>ניהול מוזיאון: האמנות שמאחורי הקלעים</h1>
        <p class="subtitle">קבלו את ההחלטות הקריטיות שיעצבו את עתיד אוסף אמנות היסטורי. כל שנה מביאה הזדמנויות ואתגרים חדשים. האם תצליחו לאזן בין חשיפה ציבורית הכרחית לשמירה קפדנית על האוצרות?</p>
    </header>

    <div id="museum-app">
        <section id="status" class="game-section">
            <h2>מצב המוזיאון</h2>
            <p><strong>שנה:</strong> <span id="current-year" class="status-value">1</span></p>
            <p><strong>תקציב נוכחי:</strong> <span id="current-budget" class="status-value budget-value"></span> ₪</p>
            <p><strong>מבקרים בשנה שעברה:</strong> <span id="last-year-visitors" class="status-value">0</span></p>
            <p><strong>מצב שימור כללי של האוסף:</strong> <span id="overall-preservation" class="status-value preservation-value"></span>%</p>
        </section>

        <section id="artwork-list" class="game-section">
            <h2>האוסף היקר שלנו</h2>
            <table>
                <thead>
                    <tr>
                        <th>יצירה</th>
                        <th>מצב שימור נוכחי</th>
                        <th><span title="פוטנציאל משיכת מבקרים בתערוכה זמנית">פופולריות</span></th>
                        <th><span title="עלות השקעה חד פעמית לשיפור משמעותי במצב שימור נמוך">עלות שימור דחוף</span></th>
                        <th><span title="עלות השקעה שנתית למניעת התדרדרות ושיפור קל">עלות שימור מניעתי</span></th>
                        <th>בחירה לתערוכה</th>
                        <th>בחירה לשימור</th>
                    </tr>
                </thead>
                <tbody id="artworks-table-body">
                    <!-- Artwork rows will be injected here by JavaScript -->
                </tbody>
            </table>
        </section>

        <section id="decisions" class="game-section">
            <h2>החלטות לשנה הקרובה</h2>
            <div class="decision-block">
                <h3>בחרו יצירות לתערוכה זמנית <span class="limit">(עד 3)</span></h3>
                <p class="description">תערוכה מגדילה משמעותית את מספר המבקרים, אך חשיפה גורמת לבלאי מסוים ליצירות.</p>
                <div id="display-selection" class="selection-area">
                    <!-- Display checkboxes will be injected here -->
                </div>
            </div>
            <div class="decision-block">
                <h3>השקעה בשימור</h3>
                 <p class="description">פעולות שימור חיוניות לשמירת האוסף, אך דורשות תקציב משמעותי. שימור דחוף יעיל יותר אך יקר.</p>
                <div id="preservation-selection" class="selection-area">
                     <!-- Preservation radio buttons will be injected here -->
                </div>
            </div>

            <button id="next-turn" class="game-button">עבור לשנה הבאה</button>
        </section>

        <section id="turn-results" class="game-section results-section" style="display: none;">
            <h2>תוצאות השנה שהסתיימה</h2>
            <p><strong>מבקרים השנה:</strong> <span id="results-visitors" class="results-value"></span></p>
            <p><strong>הכנסות (מבקרים):</strong> <span id="results-income" class="results-value income-value"></span> ₪</p>
            <p><strong>הוצאות שימור:</strong> <span id="results-preservation-cost" class="results-value expense-value"></span> ₪</p>
            <p><strong>הוצאות תצוגה ושיווק:</strong> <span id="results-display-marketing-cost" class="results-value expense-value"></span> ₪</p>
            <p><strong>הוצאות שוטפות (תחזוקה, צוות):</strong> <span id="results-overhead-cost" class="results-value expense-value"></span> ₪</p>
            <p><strong>שינוי בתקציב:</strong> <span id="results-budget-change" class="results-value budget-change-value"></span> ₪</p>
            <p><strong>מצב שימור כללי מעודכן:</strong> <span id="results-overall-preservation" class="results-value preservation-value"></span>%</p>
            <p id="game-over-message" class="game-over-message"></p>
        </section>
    </div>

    <button id="toggle-explanation" class="game-button secondary-button">הצג הסבר מורחב</button>

    <div id="explanation" class="explanation-section" style="display: none;">
        <h2>העקרונות המנחים</h2>
        <div class="explanation-points">
            <div>
                <h3>תפקידי המוזיאון</h3>
                <p>מוזיאונים אוספים, משמרים, חוקרים ומציגים נכסי תרבות. איזון בין תפקידים אלו חיוני.</p>
            </div>
             <div>
                <h3>עקרונות האוצרות</h3>
                <p>אוצרות היא בחירת יצירות ובניית נרטיב לתערוכות מרתקות, תוך התחשבות בשימור ובתקציב.</p>
            </div>
             <div>
                <h3>חשיבות השימור</h3>
                <p>הגנה על האוספים מפני נזקים מבטיחה את קיומם לדורות הבאים. זו השקעה בעתיד התרבותי.</p>
            </div>
             <div>
                <h3>אתגרי השימור</h3>
                <p>פעולות שימור יקרות ומורכבות, דורשות מומחיות ותנאים סביבתיים מבוקרים.</p>
            </div>
             <div>
                <h3>חשיפה מול שימור</h3>
                <p>קיים מתח טבעי: תערוכות מושכות קהל אך עלולות לפגוע ביצירות. נדרש איזון עדין.</p>
            </div>
             <div>
                <h3>ניהול משאבים</h3>
                <p>מוזיאונים פועלים בתקציב מוגבל. החלטות תקציביות משפיעות על כל תחומי הפעילות.</p>
            </div>
             <div>
                <h3>הצלחה מוזיאלית</h3>
                <p>הצלחה היא שילוב של פופולריות (מבקרים, הכנסות) וקיימות לטווח ארוך (שימור האוסף).</p>
            </div>
        </div>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        direction: rtl;
        text-align: right;
        background: linear-gradient(to bottom right, #e0e0e0, #c0c0c0); /* Subtle gradient */
        color: #333;
        min-height: 100vh;
        box-sizing: border-box;
    }

    .museum-container {
        max-width: 1000px;
        margin: 0 auto;
        background-color: #fff;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
        border: 1px solid #ddd;
    }

    header h1 {
        color: #5a2d82; /* Museum purple */
        text-align: center;
        margin-bottom: 10px;
        font-size: 2.5em;
        font-weight: 700;
    }

    .subtitle {
         text-align: center;
         color: #666;
         font-size: 1.1em;
         margin-bottom: 30px;
         padding-bottom: 20px;
         border-bottom: 2px dashed #f0c040; /* Accent gold */
    }

    h2 {
        color: #5a2d82;
        border-bottom: 2px solid #f0c040;
        padding-bottom: 8px;
        margin-top: 25px;
        margin-bottom: 15px;
        font-size: 1.8em;
        font-weight: 700;
    }

    h3 {
        color: #7d4ebc; /* Lighter purple */
        margin-top: 15px;
        margin-bottom: 10px;
        font-size: 1.3em;
        font-weight: 700;
    }

    .game-section {
        margin-bottom: 30px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        background-color: #f9f9f9;
        box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.05);
    }

    #status p, .results-section p {
        margin: 8px 0;
        font-size: 1.1em;
    }

    .status-value, .results-value {
        font-weight: 700;
        color: #333;
        transition: color 0.5s ease, transform 0.5s ease; /* Animation for values */
        display: inline-block; /* Needed for transform */
    }

    .budget-value.positive { color: #28a745; } /* Green */
    .budget-value.negative { color: #dc3545; } /* Red */
    .preservation-value { color: #007bff; } /* Blue */
    .budget-change-value.positive { color: #28a745; }
    .budget-change-value.negative { color: #dc3545; }


    #artwork-list table {
        width: 100%;
        border-collapse: separate; /* Use separate to allow border-spacing */
        border-spacing: 0 8px; /* Space between rows */
        margin-top: 15px;
    }

    #artwork-list th, #artwork-list td {
        padding: 12px 10px;
        text-align: right;
        border: none; /* Remove individual cell borders */
    }

    #artwork-list thead th {
        background-color: #e9ecef; /* Light grey */
        font-weight: 700;
        color: #555;
        border-bottom: 2px solid #dee2e6;
        text-transform: uppercase;
        font-size: 0.9em;
    }

     #artwork-list tbody tr {
        background-color: #fff;
        border-radius: 8px; /* Rounded corners for rows */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        cursor: pointer; /* Indicate interactivity */
     }

     #artwork-list tbody tr:hover {
         transform: translateY(-3px);
         box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
     }

      #artwork-list tbody td:first-child {
          border-top-right-radius: 8px;
           border-bottom-right-radius: 8px;
      }
       #artwork-list tbody td:last-child {
          border-top-left-radius: 8px;
           border-bottom-left-radius: 8px;
      }


    .preservation-status span {
        display: inline-block;
        min-width: 60px;
        text-align: center;
        padding: 4px 8px;
        border-radius: 15px; /* Pill shape */
        font-size: 0.9em;
        font-weight: 700;
        transition: background-color 0.5s ease, color 0.5s ease; /* Animation for preservation status */
    }

    .preservation-high { background-color: #d4edda; color: #155724; }
    .preservation-medium { background-color: #fff3cd; color: #856404; }
    .preservation-low { background-color: #f8d7da; color: #721c24; }
    .preservation-critical { background-color: #6a0000; color: #fff; font-weight: bold; animation: pulse-low 1.5s infinite alternate; } /* Added critical state */

    @keyframes pulse-low {
        from { background-color: #f8d7da; }
        to { background-color: #dc3545; }
    }


    .decision-block {
        margin-bottom: 20px;
        padding: 15px;
        background-color: #e9ecef;
        border-radius: 8px;
    }

    .decision-block h3 {
        margin-top: 0;
        border-bottom: 1px dashed #ced4da;
        padding-bottom: 5px;
         display: flex;
         justify-content: space-between;
         align-items: center;
    }

    .limit {
        font-size: 0.8em;
        font-weight: normal;
        color: #666;
         background-color: #fff;
         padding: 3px 8px;
         border-radius: 10px;
         border: 1px solid #ccc;
    }

     .description {
         font-size: 0.9em;
         color: #555;
         margin-bottom: 15px;
     }

    .selection-area {
        display: flex;
        flex-wrap: wrap;
        gap: 10px 20px; /* Rows gap, columns gap */
    }

    .selection-area label {
        display: flex; /* Use flex for better alignment */
        align-items: center;
        cursor: pointer;
        font-size: 1em;
        transition: color 0.2s ease;
    }

     .selection-area label:hover {
         color: #5a2d82;
     }

    .selection-area input[type="checkbox"],
    .selection-area input[type="radio"] {
        margin-left: 8px; /* Space between text and input */
         transform: scale(1.1); /* Slightly larger checkboxes/radios */
    }

     .selection-area input[type="checkbox"]:disabled + span,
     .selection-area input[type="radio"]:disabled + span {
        color: #999;
        cursor: not-allowed;
     }


    .game-button {
        background-color: #5a2d82;
        color: white;
        padding: 12px 25px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.1em;
        margin-top: 20px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: 700;
        text-align: center;
        display: block; /* Make button take full width in its container */
        width: fit-content; /* Adjust width based on content */
        margin-right: auto; /* Center the button in RTL */
        margin-left: auto;
    }

    .game-button:hover {
        background-color: #7d4ebc;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .game-button:active {
        transform: translateY(0);
        box-shadow: none;
    }

    .game-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        transform: none;
        box-shadow: none;
    }

    .secondary-button {
        background-color: #f0c040; /* Accent gold */
         color: #333;
         margin-top: 15px;
    }
     .secondary-button:hover {
         background-color: #e0b030;
         color: #333;
     }

    .results-section {
        background-color: #e9ffe9; /* Light green for results */
        border-color: #c3e6cb;
    }

     .game-over-message {
         color: #dc3545; /* Red */
         font-weight: bold;
         text-align: center;
         font-size: 1.3em;
         margin-top: 20px;
         padding-top: 15px;
         border-top: 2px dashed #dc3545;
         animation: pulse-error 2s infinite;
     }

    @keyframes pulse-error {
        0% { opacity: 1; }
        50% { opacity: 0.7; }
        100% { opacity: 1; }
    }


    .explanation-section {
        background-color: #fff;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        border: 1px solid #e0e0e0;
        margin-top: 20px;
    }

    .explanation-section h2 {
         border-bottom: 2px solid #5a2d82;
         color: #5a2d82;
         margin-top: 0;
         margin-bottom: 20px;
    }

    .explanation-points {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* Responsive grid */
        gap: 20px;
    }

    .explanation-points > div {
        background-color: #f1f1f1;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
    }

     .explanation-points h3 {
         color: #5a2d82;
         border-bottom: 1px dotted #f0c040;
         padding-bottom: 5px;
         margin-top: 0;
     }

    .explanation-points p {
        font-size: 0.95em;
        color: #555;
    }

    /* Animation for value changes */
    .value-animated {
        animation: valueChange 0.6s ease;
    }

    @keyframes valueChange {
        0% { transform: translateY(0); opacity: 1; }
        50% { transform: translateY(-5px); opacity: 0.8; }
        100% { transform: translateY(0); opacity: 1; }
    }

     /* Animation for row emphasis on display */
     @keyframes highlight-display {
         0% { background-color: #fff; }
         50% { background-color: #fffacd; } /* Light yellow */
         100% { background-color: #fff; }
     }

     .highlight-display {
         animation: highlight-display 1.5s ease;
     }

      /* Animation for row emphasis on preservation */
     @keyframes highlight-preservation {
         0% { background-color: #fff; }
         50% { background-color: #d4edda; } /* Light green */
         100% { background-color: #fff; }
     }

     .highlight-preservation-urgent {
         animation: highlight-preservation 1.5s ease;
     }
      .highlight-preservation-prevent {
         animation: highlight-preservation 1.5s ease;
     }


     /* Responsive adjustments */
     @media (max-width: 768px) {
         body {
             padding: 10px;
         }
         .museum-container {
             padding: 15px;
         }
         h1 {
             font-size: 1.8em;
         }
         h2 {
             font-size: 1.5em;
         }
         .game-button {
             font-size: 1em;
             padding: 10px 20px;
         }
         #artwork-list th, #artwork-list td {
             padding: 8px 5px;
             font-size: 0.9em;
         }
         .explanation-points {
             grid-template-columns: 1fr; /* Stack points on small screens */
         }
          .selection-area label {
             font-size: 0.95em;
          }
          .selection-area {
            gap: 8px 15px;
          }
     }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const artworksTableBody = document.getElementById('artworks-table-body');
        const currentYearSpan = document.getElementById('current-year');
        const currentBudgetSpan = document.getElementById('current-budget');
        const lastYearVisitorsSpan = document.getElementById('last-year-visitors');
        const overallPreservationSpan = document.getElementById('overall-preservation');
        const displaySelectionDiv = document.getElementById('display-selection');
        const preservationSelectionDiv = document.getElementById('preservation-selection'); // Will inject radios here now
        const nextTurnButton = document.getElementById('next-turn');
        const turnResultsDiv = document.getElementById('turn-results');
        const resultsVisitorsSpan = document.getElementById('results-visitors');
        const resultsIncomeSpan = document.getElementById('results-income');
        const resultsPreservationCostSpan = document.getElementById('results-preservation-cost');
        const resultsDisplayMarketingCostSpan = document.getElementById('results-display-marketing-cost');
        const resultsOverheadCostSpan = document.getElementById('results-overhead-cost');
        const resultsBudgetChangeSpan = document.getElementById('results-budget-change');
        const resultsOverallPreservationSpan = document.getElementById('results-overall-preservation');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');
        const gameOverMessage = document.getElementById('game-over-message');

        let currentYear = 1;
        let budget = 60000; // Slightly higher initial budget for more gameplay
        const annualOverhead = 18000; // Fixed cost per year, slightly higher
        const baseDisplayMarketingCost = 6000; // Base cost to set up any exhibition
        const costPerDisplayedItem = 1000; // Extra cost per item for handling/security
        const incomePerVisitor = 12; // Slightly higher income
        const maxDisplayItems = 3; // Limit on items in temporary exhibit
        const naturalDecayRate = 0.8; // Annual preservation loss for non-maintained items

        // Define the artworks - Adjusted values slightly for balance
        let artworks = [
            { id: 'mona', name: 'מונליזה (ציור)', initialPreservation: 95, currentPreservation: 95, popularity: 12, displayWear: 1.5, preservationCostUrgent: 9000, preservationImproveUrgent: 12, preservationCostPrevent: 2500, preservationImprovePrevent: 3 },
            { id: 'venus', name: 'ונוס ממילו (פסל)', initialPreservation: 90, currentPreservation: 90, popularity: 10, displayWear: 0.8, preservationCostUrgent: 6000, preservationImproveUrgent: 10, preservationCostPrevent: 1800, preservationImprovePrevent: 2 },
            { id: 'starrynight', name: 'ליל כוכבים (ציור)', initialPreservation: 85, currentPreservation: 85, popularity: 11, displayWear: 1.8, preservationCostUrgent: 8000, preservationImproveUrgent: 11, preservationCostPrevent: 2000, preservationImprovePrevent: 2.5 },
            { id: 'mask', name: 'מסכת פנים טוטנקאמון (ממצא ארכיאולוגי)', initialPreservation: 75, currentPreservation: 75, popularity: 14, displayWear: 2.5, preservationCostUrgent: 12000, preservationImproveUrgent: 18, preservationCostPrevent: 3500, preservationImprovePrevent: 4 },
            { id: 'rosetta', name: 'אבן רוזטה (אבן מגולפת)', initialPreservation: 98, currentPreservation: 98, popularity: 8, displayWear: 0.5, preservationCostUrgent: 5000, preservationImproveUrgent: 6, preservationCostPrevent: 1200, preservationImprovePrevent: 1.5 },
             { id: 'sistine', name: 'סקטץ\' לתקרת הסיסטינה (ציור על נייר)', initialPreservation: 60, currentPreservation: 60, popularity: 9, displayWear: 3.0, preservationCostUrgent: 15000, preservationImproveUrgent: 25, preservationCostPrevent: 4500, preservationImprovePrevent: 5 },
             { id: 'dinosaur', name: 'שלד דינוזאור (מאובן)', initialPreservation: 80, currentPreservation: 80, popularity: 13, displayWear: 1.0, preservationCostUrgent: 7000, preservationImproveUrgent: 8, preservationCostPrevent: 2200, preservationImprovePrevent: 2 },
        ];

        let lastYearVisitors = 0;

        function updateUI() {
            // Animate budget change
             animateValue(currentBudgetSpan, budget);

            currentYearSpan.textContent = currentYear;
            lastYearVisitorsSpan.textContent = lastYearVisitors;

            const overallPreservation = calculateOverallPreservation();
            animateValue(overallPreservationSpan, overallPreservation, 1); // 1 decimal place
             overallPreservationSpan.className = 'status-value preservation-value ' + getPreservationClass(overallPreservation); // Update class

            artworksTableBody.innerHTML = '';
            displaySelectionDiv.innerHTML = '';
            preservationSelectionDiv.innerHTML = '';

            artworks.forEach(artwork => {
                const row = artworksTableBody.insertRow();
                row.dataset.id = artwork.id; // Add data-id to row for selection sync

                const preservationStatusHtml = `<span class="preservation-status ${getPreservationClass(artwork.currentPreservation)}">${artwork.currentPreservation.toFixed(1)}%</span>`;

                row.innerHTML = `
                    <td>${artwork.name}</td>
                    <td>${preservationStatusHtml}</td>
                    <td>${artwork.popularity}</td>
                    <td>${artwork.preservationCostUrgent.toFixed(0)}</td>
                    <td>${artwork.preservationCostPrevent.toFixed(0)}</td>
                     <td><input type="checkbox" data-id="${artwork.id}" class="display-checkbox table-display-checkbox" ${artwork.currentPreservation < 20 ? 'disabled' : ''}></td>
                     <td class="preservation-radios">
                         <!-- Radio buttons moved to preservationSelectionDiv -->
                     </td>
                `;

                // Add checkbox to display selection div
                const displayLabel = document.createElement('label');
                const displayCheckbox = document.createElement('input');
                displayCheckbox.type = 'checkbox';
                displayCheckbox.dataset.id = artwork.id;
                displayCheckbox.className = 'display-checkbox external-display-checkbox'; // Differentiate checkboxes
                if (artwork.currentPreservation < 20) {
                    displayCheckbox.disabled = true;
                    displayLabel.title = "מצב שימור נמוך מכדי להציג בבטחה";
                }
                const displayName = document.createElement('span');
                displayName.textContent = artwork.name;
                displayLabel.appendChild(displayCheckbox);
                displayLabel.appendChild(displayName);
                displaySelectionDiv.appendChild(displayLabel);


                // Add radio buttons to preservation selection div
                 const preservationFieldSet = document.createElement('fieldset');
                 preservationFieldSet.className = 'preservation-options-fieldset';
                 const legend = document.createElement('legend');
                 legend.textContent = artwork.name;
                 preservationFieldSet.appendChild(legend);

                const urgentLabel = document.createElement('label');
                urgentLabel.innerHTML = `<input type="radio" name="preservation-${artwork.id}" data-id="${artwork.id}" value="urgent" class="preservation-radio" ${artwork.currentPreservation >= 100 ? 'disabled' : ''}> <span>דחוף (${artwork.preservationCostUrgent.toFixed(0)}₪)</span>`;
                 urgentLabel.title = "שיפור משמעותי, עלות גבוהה";
                preservationFieldSet.appendChild(urgentLabel);

                const preventLabel = document.createElement('label');
                preventLabel.innerHTML = `<input type="radio" name="preservation-${artwork.id}" data-id="${artwork.id}" value="prevent" class="preservation-radio" ${artwork.currentPreservation >= 100 ? 'disabled' : ''}> <span>מניעתי (${artwork.preservationCostPrevent.toFixed(0)}₪)</span>`;
                 preventLabel.title = "שמירה מפני הידרדרות ושיפור קל, עלות בינונית";
                preservationFieldSet.appendChild(preventLabel);

                const noneLabel = document.createElement('label');
                noneLabel.innerHTML = `<input type="radio" name="preservation-${artwork.id}" data-id="${artwork.id}" value="none" class="preservation-radio" checked> <span>ללא שימור</span>`;
                 noneLabel.title = "לא יבוצע שימור השנה. מצב השימור עלול להתדרדר באופן טבעי.";
                preservationFieldSet.appendChild(noneLabel);

                preservationSelectionDiv.appendChild(preservationFieldSet);

            });

            // Sync display checkboxes: clicking one updates the other
            const tableDisplayCheckboxes = artworksTableBody.querySelectorAll('.table-display-checkbox');
            const externalDisplayCheckboxes = displaySelectionDiv.querySelectorAll('.external-display-checkbox');

            tableDisplayCheckboxes.forEach(checkbox => {
                checkbox.addEventListener('change', (e) => {
                    const id = e.target.dataset.id;
                    const checked = e.target.checked;
                     // Find the corresponding external checkbox and update its state
                     externalDisplayCheckboxes.forEach(externalCheckbox => {
                         if (externalCheckbox.dataset.id === id) {
                             externalCheckbox.checked = checked;
                         }
                     });
                    enforceDisplayLimit();
                });
            });

             externalDisplayCheckboxes.forEach(checkbox => {
                checkbox.addEventListener('change', (e) => {
                    const id = e.target.dataset.id;
                    const checked = e.target.checked;
                     // Find the corresponding table checkbox and update its state
                     tableDisplayCheckboxes.forEach(tableCheckbox => {
                         if (tableCheckbox.dataset.id === id) {
                             tableCheckbox.checked = checked;
                         }
                     });
                    enforceDisplayLimit();
                });
            });


            // Enforce display limit
            function enforceDisplayLimit() {
                 const selected = displaySelectionDiv.querySelectorAll('.external-display-checkbox:checked').length;
                 if (selected > maxDisplayItems) {
                     // Find the checkbox that was just checked and uncheck it
                     externalDisplayCheckboxes.forEach(checkbox => {
                         if(checkbox.checked && !checkbox.dataset.justChecked) {
                             checkbox.checked = false;
                              // Also uncheck the corresponding table checkbox
                              tableDisplayCheckboxes.forEach(tableCheckbox => {
                                  if (tableCheckbox.dataset.id === checkbox.dataset.id) {
                                       tableCheckbox.checked = false;
                                  }
                              });
                             alert(`ניתן לבחור עד ${maxDisplayItems} יצירות לתערוכה זמנית.`);
                         }
                          delete checkbox.dataset.justChecked; // Clean up the flag
                     });
                 } else {
                      // Add a temporary flag to the checkbox that was just checked
                      externalDisplayCheckboxes.forEach(checkbox => {
                         if(checkbox.checked && !checkbox.dataset.wasChecked) {
                             checkbox.dataset.justChecked = 'true';
                         }
                          checkbox.dataset.wasChecked = checkbox.checked ? 'true' : 'false'; // Track previous state
                      });
                 }
             }
             // Initialize wasChecked state
             externalDisplayCheckboxes.forEach(checkbox => checkbox.dataset.wasChecked = 'false');


        }

        function calculateOverallPreservation() {
            if (artworks.length === 0) return 100;
            const totalPreservation = artworks.reduce((sum, artwork) => sum + artwork.currentPreservation, 0);
            return totalPreservation / artworks.length;
        }

        function getPreservationClass(preservation) {
            if (preservation >= 85) return 'preservation-high';
            if (preservation >= 50) return 'preservation-medium';
            if (preservation >= 20) return 'preservation-low';
            return 'preservation-critical'; // Critical state
        }

         function animateValue(spanElement, newValue, decimals = 0) {
             const currentValue = parseFloat(spanElement.textContent) || 0;
             const start = currentValue;
             const end = newValue;
             const duration = 800; // milliseconds
             let startTime = null;

             function animationStep(timestamp) {
                 if (!startTime) startTime = timestamp;
                 const elapsed = timestamp - startTime;
                 const progress = Math.min(elapsed / duration, 1);
                 const currentValue = start + (end - start) * progress;

                 spanElement.textContent = currentValue.toFixed(decimals);

                 if (progress < 1) {
                     requestAnimationFrame(animationStep);
                 } else {
                     spanElement.textContent = end.toFixed(decimals); // Ensure final value is exact
                 }
             }

             requestAnimationFrame(animationStep);
         }

        function nextTurn() {
            turnResultsDiv.style.display = 'none';
            gameOverMessage.textContent = '';
            nextTurnButton.disabled = true;

             // Clear previous row highlights
             artworksTableBody.querySelectorAll('tr').forEach(row => {
                 row.classList.remove('highlight-display', 'highlight-preservation-urgent', 'highlight-preservation-prevent');
             });


            const selectedForDisplay = Array.from(displaySelectionDiv.querySelectorAll('.external-display-checkbox:checked')).map(cb => cb.dataset.id);
             const selectedForPreservation = {};
             document.querySelectorAll('.preservation-radio:checked').forEach(radio => {
                 if (radio.value !== 'none') {
                     selectedForPreservation[radio.dataset.id] = radio.value;
                 }
             });

            let annualPreservationCost = 0;
            let annualDisplayMarketingCost = 0;

             // Apply natural decay to all artworks first
             artworks.forEach(artwork => {
                 artwork.currentPreservation = Math.max(0, artwork.currentPreservation - naturalDecayRate);
             });


            // Apply decisions and calculate costs/effects
            artworks.forEach(artwork => {
                 const row = artworksTableBody.querySelector(`tr[data-id="${artwork.id}"]`);

                // Apply preservation (improves state AFTER decay)
                if (selectedForPreservation[artwork.id] === 'urgent') {
                    annualPreservationCost += artwork.preservationCostUrgent;
                    artwork.currentPreservation = Math.min(100, artwork.currentPreservation + artwork.preservationImproveUrgent);
                     if(row) row.classList.add('highlight-preservation-urgent');
                } else if (selectedForPreservation[artwork.id] === 'prevent') {
                     annualPreservationCost += artwork.preservationCostPrevent;
                     artwork.currentPreservation = Math.min(100, artwork.currentPreservation + artwork.preservationImprovePrevent);
                      if(row) row.classList.add('highlight-preservation-prevent');
                }

                // Apply display wear if selected for display
                if (selectedForDisplay.includes(artwork.id)) {
                    artwork.currentPreservation = Math.max(0, artwork.currentPreservation - artwork.displayWear);
                     if(row) row.classList.add('highlight-display');
                }
            });

             // Calculate display/marketing cost
             if (selectedForDisplay.length > 0) {
                 annualDisplayMarketingCost = baseDisplayMarketingCost + (selectedForDisplay.length * costPerDisplayedItem);
             }

            // Calculate visitors and income based on displayed popularity AND overall preservation
            let potentialVisitorsBase = selectedForDisplay.reduce((sum, id) => {
                 const artwork = artworks.find(a => a.id === id);
                 return sum + (artwork ? artwork.popularity : 0);
             }, 0);

            const currentOverallPreservation = calculateOverallPreservation();
            // Visitors affected by displayed popularity and overall collection health
             let actualVisitors = potentialVisitorsBase * 1000 * (currentOverallPreservation / 100); // Scale popularity, adjust by overall preservation

             // Add some minor randomness to visitors for realism
             actualVisitors = actualVisitors * (1 + (Math.random() - 0.5) * 0.1); // +/- 5% randomness
             actualVisitors = Math.max(0, Math.round(actualVisitors)); // Ensure non-negative integer

             lastYearVisitors = actualVisitors;
             let income = actualVisitors * incomePerVisitor;

            // Calculate total expenses
            let totalExpenses = annualOverhead + annualPreservationCost + annualDisplayMarketingCost;

            // Update budget
            let budgetChange = income - totalExpenses;
            budget += budgetChange;

            // Check for game over conditions
            let isGameOver = false;
            let gameOverReason = '';

            if (budget < -20000) { // More significant debt threshold
                isGameOver = true;
                gameOverReason = 'פשיטת רגל! המוזיאון אינו יכול להמשיך לתפקד תחת חוב כה גדול.';
            } else if (currentOverallPreservation < 15) { // Higher critical preservation threshold
                 isGameOver = true;
                 gameOverReason = 'האוסף במצב התדרדרות קריטי! המוזיאון נסגר עקב נזק בלתי הפיך לאוצרות.';
            } else if (currentYear > 10) { // Win condition: survive 10 years? Or just keep playing? Let's make it continue but results matter.
                 // No automatic win/loss after year 10, just keep going, performance is the score.
                 // Or, could check for good performance: budget > 0 and preservation > 70% after 10 years?
                 // Let's stick to just game over for failure for simplicity.
            }


            // Display results with animation
             animateValue(resultsVisitorsSpan, actualVisitors, 0);
             animateValue(resultsIncomeSpan, income, 0);
             animateValue(resultsPreservationCostSpan, annualPreservationCost, 0);
             animateValue(resultsDisplayMarketingCostSpan, annualDisplayMarketingCost, 0);
             animateValue(resultsOverheadCostSpan, annualOverhead, 0);
             animateValue(resultsBudgetChangeSpan, budgetChange, 0);
             resultsBudgetChangeSpan.style.color = budgetChange >= 0 ? '#28a745' : '#dc3545'; // Apply color immediately
             animateValue(resultsOverallPreservationSpan, currentOverallPreservation, 1);
             resultsOverallPreservationSpan.className = 'results-value preservation-value ' + getPreservationClass(currentOverallPreservation); // Update class immediately


            turnResultsDiv.style.display = 'block';


            if (isGameOver) {
                gameOverMessage.textContent = `המשחק הסתיים: ${gameOverReason}`;
                 nextTurnButton.disabled = true;
                 displaySelectionDiv.querySelectorAll('input').forEach(input => input.disabled = true);
                 preservationSelectionDiv.querySelectorAll('input').forEach(input => input.disabled = true);
                 artworksTableBody.querySelectorAll('input').forEach(input => input.disabled = true); // Disable table inputs too
                 alert(`המשחק הסתיים!\n${gameOverReason}\nניקוד סופי (מצב שימור + תקציב / 1000): ${(currentOverallPreservation + budget/1000).toFixed(0)}`); // Simple score
            } else {
                currentYear++;
                 // Allow a moment for results animation before next turn UI update
                 setTimeout(() => {
                      updateUI(); // Update UI for the next year
                      nextTurnButton.disabled = false;
                 }, 1000); // Delay UI update slightly
            }
        }

        function toggleExplanation() {
            if (explanationDiv.style.display === 'none') {
                explanationDiv.style.display = 'block';
                toggleExplanationButton.textContent = 'הסתר הסבר מורחב';
            } else {
                explanationDiv.style.display = 'none';
                toggleExplanationButton.textContent = 'הצג הסבר מורחב';
            }
        }


        // Initial setup
        updateUI();
        nextTurnButton.addEventListener('click', nextTurn);
        toggleExplanationButton.addEventListener('click', toggleExplanation);
    });
</script>
```