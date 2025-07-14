---
title: "חלוקה הוגנת? ג'רימנדרינג בפעולה!"
english_slug: fair-division-gerrymandering-in-action
category: "מדע המדינה"
tags: [ג'רימנדרינג, בחירות, חלוקת מחוזות, דמוקרטיה, הטיה פוליטית]
---
<h1>חלוקה הוגנת? ג'רימנדרינג בפעולה!</h1>
<p>האם ידעתם שהדרך שבה משרטטים את גבולות מחוזות הבחירה יכולה להכריע מי ינצח בבחירות, עוד לפני שנספר קול אחד? זה לא רק על מי מצביע, אלא גם על <strong>איפה</strong> הוא מצביע! בואו נשחק קצת עם המפה ונראה איך מניפולציה של גבולות עובדת.</p>

<div class="gerrymandering-app">
    <div class="controls">
        <div id="voter-counts" class="control-item"></div>
        <div id="district-selection" class="control-item">
            <!-- District selection buttons will be generated here by JS -->
        </div>
         <button id="calculate-results" class="control-item">חשב תוצאות</button>
        <button id="reset-grid" class="control-item secondary-button">התחל מחדש</button>
    </div>
    <div id="grid-container" class="grid-container">
        <!-- Grid cells will be generated here by JS -->
    </div>
    <div id="results-display" class="results-display">
        <!-- Results will be displayed here -->
    </div>
    <div class="instructions">
        <p><strong>המשימה:</strong> לפניכם מפת בחירות וירטואלית עם 36 בוחרים - אדומים וכחולים. עליכם לחלק את כל 36 התאים ל-4 מחוזות בחירה שונים, כאשר בכל מחוז חייבים להיות בדיוק 9 בוחרים.</p>
         <p><strong>איך משחקים:</strong></p>
         <ol>
             <li>בחרו מחוז לעבוד עליו באמצעות הכפתורים למעלה (מחוז 1, מחוז 2 וכו'). הכפתור הנבחר יהיה מודגש.</li>
             <li>לחצו על תאים ריקים במפה כדי להקצות אותם למחוז שבחרתם. שימו לב שהתא ישנה את גבולו ויציג את מספר המחוז אליו הוקצה.</li>
             <li>השלימו את הקצאת 9 התאים לכל אחד מ-4 המחוזות. כפתור המחוז יציג את התקדמותכם.</li>
             <li>לאחר שכל 36 התאים הוקצו, כפתור "חשב תוצאות" יופעל. לחצו עליו לראות מי ניצח בכל מחוז ומה התוצאה הכללית!</li>
         </ol>
        <p class="contiguity-note"><strong>האתגר והתובנה:</strong> האפליקציה מאפשרת לכם להקצות כל תא לכל מחוז, גם אם אינם סמוכים. בחיים האמיתיים, מחוזות חייבים להיות רצופים (צמודים). <strong>נסו בעצמכם</strong> ליצור מחוזות רצופים כדי להבין את האתגר. לאחר מכן, נסו ליצור חלוקות לא רצופות (רק לשם הניסוי וההבנה!) כדי לראות איך פיצול ואיחוד בוחרים (טקטיקות 'פיצול' ו'אריזה') משפיעים על התוצאות הכוללות. האם אפשר לגרום למפלגה עם פחות בוחרים בסך הכל לזכות ברוב המחוזות?</p>
    </div>
</div>

<button id="toggle-explanation" class="secondary-button">הצג הסבר מעמיק על ג'רימנדרינג</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: מהו ג'רימנדרינג ואיך הוא משפיע?</h2>
    <p>ג'רימנדרינג (Gerrymandering) היא טכניקה פוליטית עוצמתית שמשתמשת במניפולציה של גבולות מחוזות בחירה כדי להטות את תוצאות הבחירות לטובת מפלגה או קבוצה מסוימת, לעיתים קרובות בניגוד לרצון הרוב הכולל של הבוחרים. זהו כלי שיכול לערער את יסודות הדמוקרטיה.</p>

    <h3>מקור השם - סיפור מוזר מ-1812</h3>
    <p>המונח נולד במסצ'וסטס, ארה"ב. המושל אלברידג' גרי (Elbridge Gerry) אישר בשנת 1812 חלוקה מחדש של מחוזות הסנאט של המדינה שהיטיבה באופן בוטה עם מפלגתו. אחת המפות שנוצרו קיבלה צורה עקלקלה ומוזרה, ולמי שצפה בה היא הזכירה סלמנדרה (salamander). מישהו שנון חיבר את שם המושל (Gerry) עם צורת החיה (mander) וכך נולד המונח "ג'רימנדרינג".</p>

    <h3>הטקטיקות המרכזיות: 'אריזה' ו'פיצול'</h3>
    <p>איך בדיוק מציירים מפות כדי להטות בחירות? הנה שתי שיטות עיקריות:</p>
    <ul>
        <li><strong>'אריזה' (Packing):</strong> מרכזים כמה שיותר בוחרים מהמפלגה היריבה (למשל, בוחרים כחולים) במחוז בחירה אחד או מספר מחוזות מצומצם. התוצאה? המפלגה היריבה תזכה באותם מחוזות בניצחונות מוחצים (עם רוב אדיר), אבל כוחה ידולל דרמטית במחוזות האחרים. זה מבטיח ניצחונות למפלגה המשרטטת במחוזות רבים עם רוב קטן יותר, ובסך הכל מאפשר לה לזכות ברוב מושבים בפרלמנט, גם אם יש לה פחות קולות כוללים.</li>
        <li><strong>'פיצול' (Cracking):</strong> מפזרים בוחרים מהמפלגה היריבה (למשל, בוחרים כחולים) בין מספר מחוזות בחירה רבים, כך שבאף אחד מהם הם לא יהוו רוב משמעותי. בוחרים אלו "מפוצלים" ולא מצליחים לרכז את כוחם כדי לנצח באף מחוז בודד. זה "מבזבז" את קולותיהם ומאפשר למפלגה המשרטטת לנצח בקלות יחסית במחוזות רבים.</li>
    </ul>

    <h3>השלכות הרסניות על הדמוקרטיה</h3>
    <p>ג'רימנדרינג אינו רק טקטיקה פוליטית; הוא מחליש את עקרונות הייצוג וההגינות:</p>
    <ul>
        <li><strong>מחוזות לא תחרותיים:</strong> נוצרים מחוזות "בטוחים" שבהם תוצאות הבחירות ידועות מראש. זה מקטין את התחרות, את הצורך של מועמדים לפנות למרכז, ואף יכול להפחית את אחוז ההצבעה כי בוחרים מרגישים שקולם אינו משנה.</li>
        <li><strong>הקצנה פוליטית:</strong> מועמדים במחוזות בטוחים חוששים יותר מיריבים בתוך מפלגתם בבחירות המקדימות (פריימריז) מאשר מהיריב מהמפלגה הנגדית בבחירות הכלליות. זה דוחף אותם לאמץ עמדות קיצוניות יותר כדי לרצות את הבסיס המפלגתי שלהם.</li>
        <li><strong>פגיעה בייצוג:</strong> קבוצות מיעוט, אתניות או פוליטיות, עלולות למצוא את עצמן מפוצלות או ארוזות באופן שמפחית את כוחן הפוליטי ואת יכולתן לבחור נציגים שמשקפים את האינטרסים שלהן.</li>
    </ul>

    <h3>התמודדות עם התופעה</h3>
    <p>מדינות וגופים אזרחיים מנסים למצוא דרכים להגביל את הג'רימנדרינג, למשל על ידי העברת סמכויות שרטוט המפות לוועדות עצמאיות ולא-מפלגתיות, שימוש באלגוריתמים אובייקטיביים לשרטוט גבולות, ופסיקות של בתי משפט המגבילות את היקף המניפולציה.</p>
</div>

<style>
    /* Basic Hebrew styling & Global improvements */
    body {
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif; /* More common, safer font */
        line-height: 1.7; /* Increased line height for readability */
        margin: 0; /* Remove default margin */
        padding: 20px;
        background-color: #f8f9fa; /* Lighter background */
        color: #343a40; /* Darker text for contrast */
        font-size: 16px;
    }

    h1, h2, h3 {
        color: #004085; /* A deeper blue */
        margin-top: 25px;
        margin-bottom: 15px;
        line-height: 1.4;
    }

    h1 { font-size: 2em; }
    h2 { font-size: 1.6em; }
    h3 { font-size: 1.3em; }

    p {
        margin-bottom: 15px;
        text-align: justify; /* Justify text */
    }

    ol {
         margin-bottom: 15px;
        padding-inline-start: 25px; /* More padding for list items */
    }

     li {
         margin-bottom: 8px;
     }

    .gerrymandering-app {
        background-color: #ffffff;
        padding: 25px; /* More padding */
        border-radius: 10px; /* More rounded corners */
        box-shadow: 0 4px 10px rgba(0,0,0,0.1); /* Softer, larger shadow */
        margin-top: 25px;
        border: 1px solid #e9ecef; /* Subtle border */
    }

    .controls {
        margin-bottom: 20px;
        display: flex;
        flex-wrap: wrap; /* Allow wrapping */
        gap: 15px; /* Increased gap */
        align-items: center;
        justify-content: center; /* Center controls */
         padding-bottom: 15px;
         border-bottom: 1px solid #e9ecef; /* Separator */
    }

    .control-item {
        /* Base style for control items */
        margin: 0; /* Reset default margin */
    }


    #voter-counts {
        font-weight: bold;
        font-size: 1.1em;
        color: #004085;
        min-width: 220px; /* Give it more space */
        text-align: center;
        padding: 5px;
        border-radius: 5px;
         background-color: #e9ecef; /* Subtle background */
    }

    #district-selection {
        display: flex;
        flex-wrap: wrap; /* Allow buttons to wrap */
        gap: 8px; /* Gap between buttons */
    }

    #district-selection button {
        padding: 10px 15px; /* More padding */
        border: 1px solid #007bff; /* Primary button color */
        background-color: #ffffff; /* White background */
        color: #007bff; /* Primary text color */
        cursor: pointer;
        border-radius: 5px; /* Slightly more rounded */
        transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease, transform 0.1s ease; /* Add transform for press effect */
        font-size: 1em;
    }

    #district-selection button.active {
        background-color: #007bff;
        color: white;
        border-color: #007bff;
        font-weight: bold;
         box-shadow: 0 2px 5px rgba(0, 123, 255, 0.3); /* Add shadow for active */
    }
    
    #district-selection button:hover:not(:disabled):not(.active) {
         background-color: #e9ecef; /* Light hover effect */
    }

    /* General Button Styling */
    button {
         padding: 10px 15px;
         border: 1px solid #007bff;
         background-color: #007bff;
         color: white;
         cursor: pointer;
         border-radius: 5px;
         transition: background-color 0.3s ease, border-color 0.3s ease, opacity 0.3s ease, transform 0.1s ease;
         font-size: 1em;
         font-weight: normal;
    }

    button.secondary-button {
         background-color: #6c757d; /* Greyish color */
         border-color: #6c757d;
         color: white;
    }

    button:hover:not(:disabled) {
        background-color: #0056b3;
        border-color: #004f9e;
        transform: translateY(-1px); /* Subtle lift effect */
    }
    button.secondary-button:hover:not(:disabled) {
         background-color: #545b62;
         border-color: #4a4e53;
    }


     button:active:not(:disabled) {
         transform: translateY(0); /* Press effect */
     }

     button:disabled {
        background-color: #cccccc;
        border-color: #999999;
        cursor: not-allowed;
        opacity: 0.6;
        transform: none; /* No transform when disabled */
     }


    .grid-container {
        display: grid;
        grid-template-columns: repeat(6, 45px); /* Slightly larger cells */
        grid-template-rows: repeat(6, 45px); /* Slightly larger cells */
        gap: 2px; /* Slightly larger gap */
        border: 1px solid #adb5bd; /* Lighter border */
        width: fit-content;
        margin: 20px auto; /* Center the grid */
        background-color: #adb5bd; /* Background for gaps */
        border-radius: 5px;
        overflow: hidden; /* Hide potential overflow from border-radius */
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }

    .grid-cell {
        width: 45px;
        height: 45px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 10px; /* Smaller font for number */
        font-weight: bold;
        cursor: pointer;
        background-color: #e9ecef; /* Default cell background */
        position: relative;
        border: 3px solid transparent; /* Thicker, transparent border */
        box-sizing: border-box;
        transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.1s ease;
    }

     .grid-cell:not(.assigned):hover {
         background-color: #dee2e6; /* Light hover effect on unassigned */
         transform: scale(1.02); /* Subtle grow effect on hover */
     }

     .grid-cell:active:not(.assigned) {
          transform: scale(0.98); /* Press effect */
     }


    .voter-R {
        background-color: #ffadad; /* Softer red */
    }

    .voter-B {
        background-color: #a7c9f7; /* Softer blue */
    }

     /* Styles for assigned districts (border color) - Use distinct, visible colors */
    .district-0 { border-color: #8e44ad; } /* Purple */
    .district-1 { border-color: #e67e22; } /* Orange */
    .district-2 { border-color: #2ecc71; } /* Green */
    .district-3 { border-color: #a0522d; } /* Sienna/Brown */


     /* Animation for assigned cells */
     .grid-cell.assigned {
         animation: cell-assign-pulse 0.4s ease-out; /* Subtle pulse animation */
     }

     @keyframes cell-assign-pulse {
         0% { transform: scale(1); opacity: 0.8; }
         50% { transform: scale(1.05); opacity: 1; }
         100% { transform: scale(1); opacity: 1; }
     }


    .grid-cell.assigned::after {
        content: attr(data-district-id); /* Show district number */
        position: absolute;
        top: 4px; /* Adjust position */
        right: 4px; /* Adjust position */
        font-size: 10px;
        font-weight: bold;
        color: rgba(0,0,0,0.6); /* Darker, slightly transparent text */
        text-shadow: 0 0 2px rgba(255,255,255,0.8); /* Add subtle text shadow for readability */
        z-index: 1;
    }


    .results-display {
        margin-top: 25px;
        padding: 20px;
        background-color: #d4edda; /* Light green background for success */
        border-radius: 8px;
        border: 1px solid #c3e6cb;
        color: #155724; /* Dark green text */
        animation: fadein 0.5s ease-out; /* Animation for results display */
    }

     @keyframes fadein {
         0% { opacity: 0; transform: translateY(10px); }
         100% { opacity: 1; transform: translateY(0); }
     }

    .results-display h3 {
        margin-top: 0;
        color: #155724; /* Match text color */
         border-bottom: 1px solid #c3e6cb;
         padding-bottom: 10px;
         margin-bottom: 15px;
    }
     .results-display h4 {
         color: #155724;
         margin-top: 15px;
         margin-bottom: 10px;
     }

    .results-display p {
        margin: 8px 0; /* More space between paragraphs */
         text-align: right; /* Align results text right */
    }

     .results-display strong {
         font-weight: bold;
         color: #004085; /* Highlight winner color */
     }


    #toggle-explanation {
        display: block;
        width: fit-content;
        margin: 25px auto; /* Center the button */
        padding: 10px 20px;
    }

    #explanation {
        border-top: 1px solid #e9ecef;
        padding-top: 25px;
        margin-top: 25px;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        animation: fadein 0.5s ease-out; /* Animation for explanation toggle */
    }

    #explanation h3 {
        margin-top: 20px;
    }

    .instructions {
        margin-top: 25px;
        padding: 20px;
        background-color: #fff3cd; /* Light yellow */
        border: 1px solid #ffeeba;
        border-radius: 8px;
        text-align: right; /* Instructions text should be right-aligned */
        color: #665005; /* Darker yellow text */
         box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    .instructions p, .instructions ol, .instructions li {
        margin-bottom: 10px;
         color: #665005; /* Ensure all text elements inherit color */
    }

     .instructions ol {
         padding-inline-start: 30px;
     }
      .instructions li {
          text-align: right;
          list-style-position: outside; /* Ensure bullet/number is outside */
      }


    .contiguity-note {
        font-size: 0.95em; /* Slightly larger */
        font-style: italic;
        margin-top: 15px;
        border-top: 1px dashed #ffeeba; /* Separator line */
        padding-top: 10px;
    }

    /* Additional styles for clarity */
    .voter-R::before, .voter-B::before {
         content: ''; /* Add a pseudo-element for potential icons if needed later */
         display: inline-block;
         width: 10px;
         height: 10px;
         border-radius: 50%;
         margin-inline-end: 5px; /* Space after dot */
         vertical-align: middle;
    }

    .voter-R::before { background-color: #dc3545; /* Darker Red */ }
    .voter-B::before { background-color: #007bff; /* Darker Blue */ }
    /* Hide the dots for now, keeping the structure */
    .voter-R::before, .voter-B::before { display: none; }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const gridSize = 6; // 6x6 grid
        const numDistricts = 4; // Target 4 districts
        const cellsPerDistrict = (gridSize * gridSize) / numDistricts; // 36 / 4 = 9

        // Initial voter distribution (fixed for reproducibility, a bit more mixed)
        const initialVoters = [
            ['R', 'R', 'R', 'B', 'B', 'B'],
            ['R', 'R', 'R', 'B', 'B', 'B'],
            ['R', 'R', 'B', 'B', 'R', 'R'],
            ['B', 'B', 'R', 'R', 'B', 'B'],
            ['B', 'B', 'R', 'R', 'B', 'B'],
            ['B', 'R', 'R', 'B', 'B', 'R']
        ];


        let voters = JSON.parse(JSON.stringify(initialVoters)); // Deep copy
        let districts = Array(gridSize).fill(null).map(() => Array(gridSize).fill(null)); // district number (0 to numDistricts-1) or null
        let currentDistrict = 0; // 0, 1, 2, 3
        let districtCellCounts = Array(numDistricts).fill(0); // How many cells assigned to each district

        const gridContainer = document.getElementById('grid-container');
        const voterCountsDiv = document.getElementById('voter-counts');
        const districtSelectionDiv = document.getElementById('district-selection');
        const calculateResultsButton = document.getElementById('calculate-results');
        const resetGridButton = document.getElementById('reset-grid');
        const resultsDisplayDiv = document.getElementById('results-display');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        // Function to count total voters and display
        function countAndDisplayVoters() {
            let redCount = 0;
            let blueCount = 0;
            for (let r = 0; r < gridSize; r++) {
                for (let c = 0; c < gridSize; c++) {
                    if (voters[r][c] === 'R') redCount++;
                    else blueCount++;
                }
            }
            voterCountsDiv.innerHTML = `<span>📊</span> <strong>סה"כ בוחרים:</strong> <span style="color: #dc3545; font-weight: bold;">אדומים ${redCount}</span>, <span style="color: #007bff; font-weight: bold;">כחולים ${blueCount}</span>`;
        }

        // Function to render the grid
        function renderGrid() {
            gridContainer.innerHTML = ''; // Clear previous grid
            gridContainer.style.gridTemplateColumns = `repeat(${gridSize}, 45px)`; /* Match CSS cell size */
            gridContainer.style.gridTemplateRows = `repeat(${gridSize}, 45px)`; /* Match CSS cell size */


            for (let r = 0; r < gridSize; r++) {
                for (let c = 0; c < gridSize; c++) {
                    const cell = document.createElement('div');
                    cell.classList.add('grid-cell');
                    cell.classList.add(`voter-${voters[r][c]}`);
                    cell.dataset.row = r;
                    cell.dataset.col = c;

                    const districtId = districts[r][c];
                    if (districtId !== null) {
                        cell.classList.add('assigned');
                        cell.classList.add(`district-${districtId}`);
                        cell.dataset.districtId = districtId + 1; // Display 1-based index
                    } else {
                         cell.dataset.districtId = ''; // Clear if not assigned
                         // Add a visual cue for unassigned cells if needed, e.g. a dot or outline
                    }

                    // Add click listener to cells
                    cell.addEventListener('click', handleCellClick);

                    gridContainer.appendChild(cell);
                }
            }
        }

        // Function to create district selection buttons
        function createDistrictSelectionButtons() {
            districtSelectionDiv.innerHTML = '';
            for (let i = 0; i < numDistricts; i++) {
                const button = document.createElement('button');
                button.textContent = `מחוז ${i + 1} (${districtCellCounts[i]}/${cellsPerDistrict})`;
                button.dataset.district = i;
                button.addEventListener('click', handleDistrictButtonClick);

                 // Disable buttons for districts that are already full
                 if (districtCellCounts[i] >= cellsPerDistrict) {
                    button.disabled = true;
                    // Optional: Add a class to full buttons for specific styling
                     button.classList.add('full-district');
                 } else {
                      button.classList.remove('full-district');
                 }

                districtSelectionDiv.appendChild(button);
            }
             // Update active button class separately after creating all buttons
            const activeButton = districtSelectionDiv.querySelector(`button[data-district='${currentDistrict}']`);
            if (activeButton) {
                 activeButton.classList.add('active');
                 // Ensure the currently active button is enabled IF its district isn't full
                 if (districtCellCounts[currentDistrict] < cellsPerDistrict) {
                    activeButton.disabled = false;
                 }
            }


             // Disable all selection buttons if all cells are assigned
            if (districts.every(row => row.every(cellDistrict => cellDistrict !== null))) {
                 districtSelectionDiv.querySelectorAll('button').forEach(btn => btn.disabled = true);
            } else {
                 // Re-enable buttons for not-full districts
                 districtSelectionDiv.querySelectorAll('button').forEach(btn => {
                     const districtIndex = parseInt(btn.dataset.district);
                     if (districtCellCounts[districtIndex] < cellsPerDistrict) {
                         btn.disabled = false;
                     }
                 });
            }
        }


        // Handle click on district selection button
        function handleDistrictButtonClick(event) {
            const selectedDistrict = parseInt(event.target.dataset.district);
            // Only allow selecting if the district isn't full
            if (districtCellCounts[selectedDistrict] < cellsPerDistrict) {
                 currentDistrict = selectedDistrict;
                 // Update active button class visually
                 districtSelectionDiv.querySelectorAll('button').forEach(btn => btn.classList.remove('active'));
                 event.target.classList.add('active');

                // Re-create buttons to update counts displayed on them might be too slow,
                // instead, let's just update the active class and re-check button states.
                 createDistrictSelectionButtons(); // Re-creating is simpler with current structure
            } else {
                // Optional: Provide user feedback that district is full
                console.warn(`District ${selectedDistrict + 1} is already full.`);
                 // Could add a visual shake or temporary message here
            }
             // Enable/disable calculate button based on assignment completion
            checkCompletion();
        }

        // Handle click on a grid cell
        function handleCellClick(event) {
            const row = parseInt(event.target.dataset.row);
            const col = parseInt(event.target.dataset.col);

            // Check if cell is already assigned or current district is full
            if (districts[row][col] !== null) {
                console.log(`Cell (${row}, ${col}) is already in District ${districts[row][col] + 1}`);
                // Optional: Add visual feedback (e.g., shake the cell slightly)
                 event.target.style.animation = 'shake 0.3s';
                 event.target.addEventListener('animationend', () => {
                     event.target.style.animation = '';
                 }, { once: true });
                return; // Do nothing if already assigned
            }
             if (districtCellCounts[currentDistrict] >= cellsPerDistrict) {
                console.log(`District ${currentDistrict + 1} is full. Select another district.`);
                // Optional: Add visual feedback (e.g., highlight full district button)
                 const fullButton = districtSelectionDiv.querySelector(`button[data-district='${currentDistrict}']`);
                 if (fullButton) {
                     fullButton.style.animation = 'shake 0.3s';
                      fullButton.addEventListener('animationend', () => {
                         fullButton.style.animation = '';
                     }, { once: true });
                 }
                return; // Do nothing if current district is full
            }

            // Assign cell to the current district
            districts[row][col] = currentDistrict;
            districtCellCounts[currentDistrict]++;

            // Update the specific cell's appearance immediately
            const cell = event.target;
            cell.classList.add('assigned');
            cell.classList.add(`district-${currentDistrict}`);
            cell.dataset.districtId = currentDistrict + 1; // Display 1-based index

             // Trigger the CSS animation
             cell.style.animation = 'cell-assign-pulse 0.4s ease-out';
             cell.addEventListener('animationend', () => {
                 cell.style.animation = ''; // Reset animation property
             }, { once: true });


            // Update district selection buttons state (e.g., update counts, disable if district is full)
             createDistrictSelectionButtons(); // Re-create to update counts displayed on buttons

            // Enable/disable calculate button based on assignment completion
            checkCompletion();
        }

         // Check if all cells are assigned and enable calculate button
        function checkCompletion() {
            const allCellsAssigned = districts.every(row => row.every(cellDistrict => cellDistrict !== null));
            calculateResultsButton.disabled = !allCellsAssigned;

             // Ensure district selection buttons are disabled if complete
             if (allCellsAssigned) {
                 districtSelectionDiv.querySelectorAll('button').forEach(btn => btn.disabled = true);
                 // Optional: Add a class to indicate completion state?
             } else {
                 // Re-enable only if the corresponding district is not full AND it's not the currently active full district (handled in createDistrictSelectionButtons)
                 createDistrictSelectionButtons(); // Simplest way to manage states based on counts
             }
        }


        // Function to calculate results
        function calculateResults() {
             // Prevent calculation if not complete (should be handled by button disabled state)
             if (calculateResultsButton.disabled) return;

            const districtResults = Array(numDistricts).fill(null).map(() => ({ R: 0, B: 0, winner: null }));
            let redDistrictsWon = 0;
            let blueDistrictsWon = 0;

            // Count votes in each district
            for (let r = 0; r < gridSize; r++) {
                for (let c = 0; c < gridSize; c++) {
                    const districtId = districts[r][c];
                    // if (districtId !== null) is guaranteed here if button is enabled
                    if (voters[r][c] === 'R') districtResults[districtId].R++;
                    else districtResults[districtId].B++;
                }
            }

            // Determine winner for each district and build results HTML
            let resultsHTML = '<h3>תוצאות החלוקה:</h3>';
            resultsHTML += '<div class="district-results">';
            for (let i = 0; i < numDistricts; i++) {
                const result = districtResults[i];
                let winnerText = '';
                let winnerClass = '';

                if (result.R > result.B) {
                    result.winner = 'R';
                    redDistrictsWon++;
                    winnerText = '<strong>אדומים</strong>';
                    winnerClass = 'winner-R';
                } else { // result.B > result.R (tie is impossible with 9 cells)
                    result.winner = 'B';
                    blueDistrictsWon++;
                    winnerText = '<strong>כחולים</strong>';
                     winnerClass = 'winner-B';
                }
                resultsHTML += `<p class="district-result-item district-${i} ${winnerClass}">מחוז ${i + 1}: <span style="color: #dc3545;">אדומים ${result.R}</span>, <span style="color: #007bff;">כחולים ${result.B}</span> &mdash; <span>מנצחים: ${winnerText}</span></p>`;
            }
             resultsHTML += '</div>'; // Close district-results

            resultsHTML += `<h4>סך הכל מחוזות שנקבעו:</h4>`;
            resultsHTML += `<p>מחוזות לאדומים: <span style="color: #dc3545; font-weight: bold;">${redDistrictsWon}</span></p>`;
            resultsHTML += `<p>מחוזות לכחולים: <span style="color: #007bff; font-weight: bold;">${blueDistrictsWon}</span></p>`;

            resultsDisplayDiv.innerHTML = resultsHTML;
            // Optional: Add a slight animation or highlight to the results div
        }

        // Function to reset the grid
        function resetGrid() {
            districts = Array(gridSize).fill(null).map(() => Array(gridSize).fill(null));
            currentDistrict = 0; // Reset to District 1
            districtCellCounts = Array(numDistricts).fill(0);
            resultsDisplayDiv.innerHTML = ''; // Clear results

            // Re-render the grid to clear district assignments
            renderGrid();

            // Reset buttons
            createDistrictSelectionButtons(); // Re-create buttons to reset counts and states
            calculateResultsButton.disabled = true; // Initially disabled

             // Ensure District 1 button is active after reset
            const district1Button = districtSelectionDiv.querySelector(`button[data-district='0']`);
            if(district1Button) {
                 districtSelectionDiv.querySelectorAll('button').forEach(btn => btn.classList.remove('active'));
                 district1Button.classList.add('active');
            }
             // Optional: Add a subtle visual effect to the reset grid/container
             gridContainer.style.opacity = '0.5';
             setTimeout(() => { gridContainer.style.opacity = '1'; }, 300);
        }

        // Toggle explanation visibility
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מעמיק על ג'רימנדרינג' : 'הצג הסבר מעמיק על ג'רימנדרינג';
             toggleExplanationButton.classList.toggle('active', isHidden); // Optional: style the button when explanation is shown
        });


        // Initial setup
        countAndDisplayVoters();
        renderGrid();
        createDistrictSelectionButtons();
        calculateResultsButton.addEventListener('click', calculateResults);
        resetGridButton.addEventListener('click', resetGrid);
        calculateResultsButton.disabled = true; // Initially disabled

         // Ensure District 1 button is active initially
        const district1ButtonInitial = districtSelectionDiv.querySelector(`button[data-district='0']`);
        if(district1ButtonInitial) district1ButtonInitial.classList.add('active');


    });
</script>
```