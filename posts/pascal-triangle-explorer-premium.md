---
title: "מסע מרתק למשולש פסקל: חשוף את הסודות והתבניות!"
english_slug: pascal-triangle-explorer-premium
category: "מתמטיקה"
tags: ["משולש פסקל", "פיבונאצ'י", "חזקות של 2", "סירפינסקי", "הדמיה", "אינטראקטיבי", "כיף במתמטיקה"]
---
<h1>מסע מרתק למשולש פסקל: חשוף את הסודות והתבניות!</h1>
<p>היכנסו לעולם הקסום של משולש פסקל וגלו את האוצרות המתמטיים החבויים בו. הכלי האינטראקטיבי שלנו הוא מגרש המשחקים שלכם - בנו את המשולש, צבעו את המספרים וחשפו קשרים מפתיעים לסדרות מתמטיות מפורסמות, הכל בחוויה ויזואלית וכיפית!</p>

<div class="pascal-explorer">
    <div class="controls">
        <label for="rows">כמה שורות נגלה?</label>
        <input type="number" id="rows" value="12" min="1" max="30"> <!-- Increased max rows slightly for more exploration -->
        <label><input type="checkbox" id="highlight-sum"> הדגשת שורות (קסם חזקות 2)</label>
        <label><input type="checkbox" id="highlight-fib"> הדגשת אלכסונים (חידת פיבונאצ'י)</label>
        <label><input type="checkbox" id="highlight-sierpinski"> הדגשת זוגיים/אי-זוגיים (פלא סירפינסקי)</label>
    </div>
    <div id="pascal-triangle" class="triangle-container">
        <!-- Triangle will be rendered here with flair by JS -->
    </div>
</div>

<button id="toggle-explanation" class="explanation-button">הצגת/הסתרת סיפור הרקע והתבניות</button>

<div id="explanation" class="explanation-content" style="display: none;">
    <h2>משולש פסקל: מעבר למספרים</h2>
    <p>משולש פסקל הוא יותר מסתם טבלה של מספרים; הוא מפה ויזואלית לתגליות מתמטיות רבות. כל מספר בו הוא התוצאה הפשוטה של חיבור שני המספרים שמעליו, אבל התבניות שנוצרות מתוך הכלל הפשוט הזה מדהימות. השורה ה-n (הספירה מתחילה מ-0, השורה העליונה היא 0) מכילה את המקדמים של הביטוי האלגברי (x+y) בחזקת n. בואו נצלול לכמה מהסודות החבויים!</p>
    <h3>תבניות קסומות מחכות להתגלות:</h3>
    <h4>כוחן של חזקות 2:</h4>
    <p>קחו שורה כלשהי במשולש וחשבו את סכום כל המספרים בה. התוצאה? תמיד תהיה חזקה של 2! סכום השורה ה-0 הוא 1 (2<sup>0</sup>), סכום השורה ה-1 הוא 2 (2<sup>1</sup>), סכום השורה ה-2 הוא 4 (2<sup>2</sup>) וכן הלאה. סכום השורה ה-n הוא בדיוק 2<sup>n</sup>. סוג של קסם, לא?</p>
    <h4>היופי של סדרת פיבונאצ'י:</h4>
    <p>סדרת פיבונאצ'י (1, 1, 2, 3, 5, 8, 13...) מסתתרת גם היא כאן! אספו את המספרים לאורך האלכסונים "העולים" (לא בדיוק אלכסונים יורדים כמו שצוין קודם, אלא אלכסונים שבהם הולכים שורה למטה ותא שמאלה/ימינה, או פורמלית, סכום אינדקס השורה והאינדקס בתוך השורה קבוע). סכום המספרים בכל אחד מהאלכסונים האלה ייתן לכם את המספרים של סדרת פיבונאצ'י. נסו את זה בכלי האינטראקטיבי ותראו!</p>
    <h4>התגלית הגיאומטרית של סירפינסקי:</h4>
    <p>עוד תבנית ויזואלית מהממת מתגלה כשמסתכלים רק על המספרים הזוגיים והאי-זוגיים. אם נצבע את התאים האי-זוגיים בצבע אחד ואת הזוגיים בצבע אחר, נקבל תמונה שדומה מאוד לפרקטל המפורסם, משולש סירפינסקי. זה מראה איך מתמטיקה פשוטה יכולה לייצר יופי גיאומטרי מורכב.</p>
</div>

<style>
    /* General Body & Typography */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7; /* Slightly increased line height */
        padding: 20px;
        background: linear-gradient(to bottom right, #e0f2f7, #b3e5fc); /* Gentle gradient background */
        color: #333;
        direction: rtl; /* Right-to-left for Hebrew */
        text-align: right;
        min-height: 100vh; /* Ensure gradient covers viewport */
        margin: 0;
    }

    h1, h2, h3, h4 {
        color: #0277bd; /* Deeper blue */
        text-align: center;
        margin-bottom: 15px;
    }

    h1 {
        font-size: 2.5em; /* Larger main title */
        margin-bottom: 10px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    h2 {
        font-size: 2em;
        border-bottom: 2px solid #0277bd; /* Underline for section titles */
        padding-bottom: 5px;
        margin-top: 30px;
    }

     h3 {
        font-size: 1.6em;
        color: #01579b; /* Even deeper blue */
        margin-top: 20px;
     }

    h4 {
        font-size: 1.3em;
        color: #00838f; /* Teal */
        margin-top: 15px;
    }

    p {
        margin-bottom: 18px; /* Increased margin */
        text-align: justify;
        font-size: 1.1em;
    }

    /* Pascal Explorer Container */
    .pascal-explorer {
        margin-top: 40px; /* More space */
        background-color: #ffffff;
        padding: 30px; /* More padding */
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.15); /* Deeper shadow */
        border: 1px solid #b0bec5; /* Subtle border */
    }

    /* Controls Area */
    .controls {
        margin-bottom: 30px; /* More space below controls */
        display: flex;
        flex-wrap: wrap;
        gap: 25px; /* Increased gap */
        align-items: center;
        justify-content: center; /* Center controls */
        background-color: #e3f2fd; /* Light blue background for controls */
        padding: 15px 25px;
        border-radius: 8px;
        border: 1px dashed #90caf9;
    }

    .controls label {
        margin-left: 15px; /* Adjusted margin */
        cursor: pointer;
        font-size: 1.1em;
        color: #01579b;
        display: flex; /* Align checkbox and text */
        align-items: center;
    }

     .controls label input[type="checkbox"] {
        margin-left: 8px; /* Space between checkbox and text */
        transform: scale(1.2); /* Slightly larger checkbox */
     }


    .controls input[type="number"] {
        padding: 8px 12px; /* Increased padding */
        border: 1px solid #90caf9; /* Blue border */
        border-radius: 6px; /* More rounded */
        width: 70px; /* Wider input */
        text-align: center;
        font-size: 1.1em;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    .controls input[type="number"]:focus {
        border-color: #0277bd;
        box-shadow: 0 0 8px rgba(2, 119, 189, 0.4);
        outline: none;
    }


    /* Triangle Display */
    .triangle-container {
        overflow-x: auto; /* Allow horizontal scrolling if needed */
        padding-bottom: 20px; /* Space for scrollbar */
        margin-top: 20px;
    }

    .pascal-row {
        display: flex;
        justify-content: center; /* Center the triangle */
        margin-bottom: 8px; /* More space between rows */
        white-space: nowrap; /* Prevent wrapping */
        transition: transform 0.5s ease, opacity 0.5s ease; /* Animation for rows appearing */
        opacity: 1; /* Default state */
        transform: translateY(0);
    }

    .pascal-row.fade-in {
        opacity: 0;
        transform: translateY(20px);
    }

    .pascal-row.visible {
        opacity: 1;
        transform: translateY(0);
    }


    .pascal-cell {
        display: inline-block;
        padding: 10px 15px; /* More padding */
        margin: 0 4px; /* More margin */
        border-radius: 6px; /* More rounded */
        background-color: #e1f5fe; /* Very light blue */
        transition: background-color 0.3s ease, transform 0.15s ease, box-shadow 0.3s ease; /* Smoother transitions */
        min-width: 35px; /* Slightly wider cells */
        text-align: center;
        cursor: pointer;
        user-select: none;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
        font-weight: normal; /* Default font weight */
        color: #000; /* Default text color */
    }

    .pascal-cell:hover {
        background-color: #b3e5fc; /* Lighter blue on hover */
        transform: scale(1.1); /* More pronounced scale effect */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.12);
    }

    .pascal-cell.calculating {
        background-color: #fff9c4; /* Light yellow for calculation */
        box-shadow: 0 0 10px rgba(255, 235, 59, 0.7);
        transform: scale(1.1);
        font-weight: bold;
    }

     .pascal-cell.highlighted-parent {
        background-color: #a5d6a7; /* Light green for parents */
        box-shadow: 0 0 8px rgba(139, 195, 74, 0.6);
        font-weight: bold;
     }


    /* Highlight styles */
    /* Sum of Rows highlight - pulses and highlights all cells in row */
    .pascal-cell.highlight-row-sum {
        background-color: #81c784 !important; /* Greenish - !important to override other highlights */
        font-weight: bold;
        animation: pulse-green 1.5s infinite ease-in-out; /* Animation */
    }

    @keyframes pulse-green {
        0% { box-shadow: 0 0 0 0 rgba(129, 199, 132, 0.7); }
        70% { box-shadow: 0 0 0 15px rgba(129, 199, 132, 0); }
        100% { box-shadow: 0 0 0 0 rgba(129, 199, 132, 0); }
    }


    /* Fibonacci highlight - cycling colors based on anti-diagonal */
    .pascal-cell.fib-diag-color-0 { background-color: #ffecb3; } /* Light Amber */
    .pascal-cell.fib-diag-color-1 { background-color: #c8e6c9; } /* Light Green */
    .pascal-cell.fib-diag-color-2 { background-color: #bbdefb; } /* Light Blue */
    .pascal-cell.fib-diag-color-3 { background-color: #ffccbc; } /* Light Deep Orange */
    .pascal-cell.fib-diag-color-4 { background-color: #f8bbd0; } /* Light Pink */
    /* Add more colors if needed, but 5 is usually sufficient for visual distinction */
     .pascal-cell[class*="fib-diag-color-"].fib-diag-color-animated {
         animation: pulse-color 1.5s ease-in-out; /* Animation on first highlight */
     }
    @keyframes pulse-color {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }


    /* Sierpinski highlight - based on parity */
    .pascal-cell.highlight-sierpinski-odd {
        background-color: #e57373 !important; /* Light Red */
        color: white; /* White text for contrast */
        font-weight: bold;
    }
    .pascal-cell.highlight-sierpinski-even {
        background-color: #ffffff !important; /* White (or light background) */
        color: #333; /* Dark text */
        font-weight: normal;
        box-shadow: inset 0 0 5px rgba(0,0,0,0.1); /* Subtle inner shadow */
    }
     .pascal-cell[class*="highlight-sierpinski-"].sierpinski-animated {
         animation: flip-sierpinski 0.6s ease-out;
     }
     @keyframes flip-sierpinski {
        0% { transform: rotateY(0); opacity: 0.5; }
        100% { transform: rotateY(360deg); opacity: 1; }
     }


    /* Explanation Section */
    .explanation-button {
        display: block;
        margin: 30px auto; /* More space */
        padding: 12px 25px; /* More padding */
        background-color: #009688; /* Teal button color */
        color: white;
        border: none;
        border-radius: 8px; /* More rounded */
        cursor: pointer;
        font-size: 1.2em; /* Larger font */
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    .explanation-button:hover {
        background-color: #00796b; /* Darker teal */
        transform: translateY(-2px); /* Lift effect */
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }

    .explanation-button:active {
         transform: translateY(0);
         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    .explanation-content {
        margin-top: 30px; /* More space */
        padding: 25px; /* More padding */
        background-color: #e0f7fa; /* Very light cyan background */
        border-right: 6px solid #00bcd4; /* Cyan border on right */
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        transition: all 0.4s ease-in-out; /* Smooth show/hide transition */
    }

    .explanation-content h2, .explanation-content h3, .explanation-content h4 {
        color: #00838f; /* Darker teal */
    }

</style>

<script>
    const rowsInput = document.getElementById('rows');
    const triangleContainer = document.getElementById('pascal-triangle');
    const highlightSumCheckbox = document.getElementById('highlight-sum');
    const highlightFibCheckbox = document.getElementById('highlight-fib');
    const highlightSierpinskiCheckbox = document.getElementById('highlight-sierpinski'); // New checkbox
    const explanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    let triangleData = []; // Store triangle data globally
    let calculatingCells = []; // Keep track of cells involved in calculation display

    // Function to generate Pascal's Triangle values
    function generatePascalTriangle(numRows) {
        const triangle = [];
        for (let i = 0; i < numRows; i++) {
            triangle[i] = [];
            for (let j = 0; j <= i; j++) {
                if (j === 0 || j === i) {
                    triangle[i][j] = 1;
                } else {
                    // Ensure indices are valid
                    const val1 = (triangle[i - 1] && triangle[i - 1][j - 1]) ? triangle[i - 1][j - 1] : 0;
                    const val2 = (triangle[i - 1] && triangle[i - 1][j]) ? triangle[i - 1][j] : 0;
                    triangle[i][j] = val1 + val2;
                }
            }
        }
        return triangle;
    }

    // Function to render the triangle in the DOM with animations
    function renderTriangle(triangleDataToRender) {
        triangleContainer.innerHTML = ''; // Clear previous triangle
        triangleData = triangleDataToRender; // Update global data

        triangleData.forEach((row, rowIndex) => {
            const rowElement = document.createElement('div');
            rowElement.classList.add('pascal-row');
            rowElement.classList.add('fade-in'); // Add fade-in class initially

            row.forEach((cellValue, cellIndex) => {
                const cellElement = document.createElement('span');
                cellElement.classList.add('pascal-cell');
                cellElement.textContent = cellValue;
                cellElement.dataset.rowIndex = rowIndex; // Add data attribute
                cellElement.dataset.cellIndex = cellIndex; // Add data attribute

                // Add click listener to each cell for calculation hint
                cellElement.addEventListener('click', handleCellClick);

                rowElement.appendChild(cellElement);
            });
            triangleContainer.appendChild(rowElement);

             // Trigger fade-in animation with delay
            setTimeout(() => {
                rowElement.classList.remove('fade-in');
                rowElement.classList.add('visible');
            }, rowIndex * 50); // Stagger animation by row index
        });

        // Apply highlights after rendering
        // Use a slight delay to allow initial rendering animation
        setTimeout(applyHighlights, triangleData.length * 50 + 100);
    }

     // Function to handle cell click - show how it's calculated
    function handleCellClick(event) {
        // Clear any previous calculation highlights
        clearCalculationHighlight();

        const clickedCell = event.target;
        const rowIndex = parseInt(clickedCell.dataset.rowIndex, 10);
        const cellIndex = parseInt(clickedCell.dataset.cellIndex, 10);
        const cellValue = parseInt(clickedCell.textContent, 10);

        // Only show calculation for cells other than the top row or edges (which are always 1)
        if (rowIndex > 0 && cellIndex > 0 && cellIndex < rowIndex) {
            const parentRowIndex = rowIndex - 1;
            const parentCellIndex1 = cellIndex - 1;
            const parentCellIndex2 = cellIndex;

            const parentCells = triangleContainer.querySelectorAll(
                `.pascal-row[data-row-index="${parentRowIndex}"] .pascal-cell[data-cell-index="${parentCellIndex1}"],
                 `.pascal-row[data-row-index="${parentRowIndex}"] .pascal-cell[data-cell-index="${parentCellIndex2}"]`
            );

            clickedCell.classList.add('calculating');
            parentCells.forEach(cell => cell.classList.add('highlighted-parent'));
            calculatingCells = [clickedCell, ...Array.from(parentCells)]; // Store elements to clear later

            // Optional: Display calculation text temporarily (could be complex to manage positioning, sticking to highlights for now)
            // console.log(`${clickedCell.textContent} = ${parentCells[0].textContent} + ${parentCells[1].textContent}`);

            // Set a timeout to clear the highlight
            setTimeout(clearCalculationHighlight, 2000); // Clear after 2 seconds
        } else {
             // Maybe a different effect for edge/top cells? Or do nothing.
             // For now, do nothing for edge/top cells.
             clickedCell.classList.add('calculating'); // Briefly highlight the clicked cell itself
             calculatingCells = [clickedCell];
              setTimeout(clearCalculationHighlight, 1000);
        }
    }

    // Function to clear calculation highlights
    function clearCalculationHighlight() {
        calculatingCells.forEach(cell => {
            cell.classList.remove('calculating');
            cell.classList.remove('highlighted-parent');
        });
        calculatingCells = []; // Clear the stored list
    }


    // Function to apply current highlight settings
    function applyHighlights() {
        const cells = triangleContainer.querySelectorAll('.pascal-cell');

        // Remove existing highlights and animations
        cells.forEach(cell => {
            cell.classList.remove('highlight-row-sum');
            cell.classList.remove('highlight-sierpinski-odd', 'highlight-sierpinski-even');
            // Remove all fib-diag-color-* and associated animation class
            cell.classList.forEach(cls => {
                if (cls.startsWith('fib-diag-color-')) {
                    cell.classList.remove(cls);
                }
            });
            cell.classList.remove('fib-diag-color-animated', 'sierpinski-animated'); // Remove animation classes
            cell.style.animation = ''; // Clear any specific animation styles
        });

        // Apply Sum of Rows highlight
        if (highlightSumCheckbox.checked) {
             cells.forEach(cell => {
                cell.classList.add('highlight-row-sum');
            });
        }

        // Apply Fibonacci highlight
        if (highlightFibCheckbox.checked) {
            cells.forEach(cell => {
                const rowIndex = parseInt(cell.dataset.rowIndex, 10);
                const cellIndex = parseInt(cell.dataset.cellIndex, 10);
                const diagonalIndex = rowIndex + cellIndex; // This is the index of the anti-diagonal
                const numColors = 5; // Number of colors to cycle
                const colorClass = `fib-diag-color-${diagonalIndex % numColors}`;
                cell.classList.add(colorClass);
                 // Add animation class for a brief effect when applied
                cell.classList.add('fib-diag-color-animated');
            });
        }

         // Apply Sierpinski highlight
        if (highlightSierpinskiCheckbox.checked) {
            cells.forEach(cell => {
                const cellValue = parseInt(cell.textContent, 10);
                if (cellValue % 2 !== 0) { // Odd
                    cell.classList.add('highlight-sierpinski-odd');
                } else { // Even
                    cell.classList.add('highlight-sierpinski-even');
                }
                // Add animation class for a brief effect when applied
                 cell.classList.add('sierpinski-animated');
            });
        }
    }

    // Function to handle input changes
    function handleInput() {
        const numRows = parseInt(rowsInput.value, 10);
        // Basic validation for input range
        if (isNaN(numRows) || numRows < 1) {
             rowsInput.value = 1; // Reset to minimum if invalid
        } else if (numRows > 30) { // Check against the new max
             rowsInput.value = 30; // Reset to maximum if invalid
        }

        const validNumRows = parseInt(rowsInput.value, 10); // Get the potentially corrected value
        // Clear current triangle immediately or with a fade-out effect
        triangleContainer.innerHTML = ''; // Simple clear for now

        const triangleData = generatePascalTriangle(validNumRows);
        renderTriangle(triangleData);
    }

    // Function to handle checkbox changes
    function handleHighlightChange() {
        clearCalculationHighlight(); // Clear calculation hint if highlights change
        applyHighlights();
    }

    // Function to toggle explanation visibility
    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none';
        // Use opacity and height transition for a smoother effect if desired,
        // but sticking to display for strict adherence unless animation via CSS is trivial.
        // display: block/none is the simplest and respects the original structure.
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתרת סיפור הרקע והתבניות' : 'הצגת/הסתרת סיפור הרקע והתבניות';
         // Optional: scroll to explanation if showing it
        if (isHidden) {
            explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }


    // Event listeners
    rowsInput.addEventListener('input', handleInput);
    highlightSumCheckbox.addEventListener('change', handleHighlightChange);
    highlightFibCheckbox.addEventListener('change', handleHighlightChange);
    highlightSierpinskiCheckbox.addEventListener('change', handleHighlightChange); // Add listener for new checkbox
    explanationButton.addEventListener('click', toggleExplanation);


    // Initial render on page load
    handleInput(); // Render triangle with default/initial rows value
</script>