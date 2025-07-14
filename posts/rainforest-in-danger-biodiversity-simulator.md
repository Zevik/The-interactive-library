---
title: "יער הגשם שותק: גלו איך כריתת עצים פוגעת בלב הטבע"
english_slug: rainforest-in-danger-biodiversity-simulator
category: "אקולוגיה"
tags: [יער גשם, מגוון ביולוגי, כריתת יערות, סימולציה, אקולוגיה, אינטראקטיבי]
---
<h1>יער הגשם שותק: גלו איך כריתת עצים פוגעת בלב הטבע</h1>
<p>דמיינו עולם תוסס, מלא חיים נסתרים, שבו כל עץ הוא עיר שלמה לאינספור מינים. זהו יער הגשם הטרופי. הוא מכסה פחות מ-3% משטח כדור הארץ, ובכל זאת הוא בית ליותר ממחצית ממיני הצמחים ובעלי החיים בעולם! אבל מה קורה למארג החיים המדהים הזה כשאנחנו מסירים לבנה אחת - או מאות לבנים - מתוכו? הסימולטור הזה מזמין אתכם לצלול לתוך הדינמיקה העדינה של יער הגשם ולגלות בעצמכם את ההשלכות המרחיקות לכת של כריתת העצים על המגוון הביולוגי העשיר והחיוני כל כך.</p>

<div id="app-container">
    <div id="rainforest-grid">
        <!-- Grid cells will be inserted here by JS -->
    </div>
    <div id="controls">
        <div id="biodiversity-display">
            <span class="label">מגוון ביולוגי:</span> <span id="biodiversity-value">...</span>
        </div>
        <p class="instruction">
            <strong>פעולה:</strong>
            <br>
            לחצו על עץ <span>🌳</span> כדי 'לכרות' אותו.
            <br>
            לחצו על אזור 'ריק' <span>🟫</span> כדי לנסות ולשקם צמחייה ראשונית <span>🌿</span>.
        </p>
        <button id="reset-button">התחילו מחדש</button>
    </div>
</div>

<style>
    /* גופנים בסיסיים - ניתן להתאים בהתאם לפלטפורמה */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
    }

    h1, h2 {
        color: #2e7d32; /* ירוק כהה יותר לכותרות */
        text-align: center;
    }

    p {
        text-align: right;
        margin-bottom: 1em;
    }

    #app-container {
        display: flex;
        flex-direction: column; /* Stack grid and controls vertically */
        align-items: center;
        gap: 30px; /* Increased space */
        margin-top: 30px;
        padding: 30px;
        background-color: #e8f5e9; /* Very light green background */
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }

    #rainforest-grid {
        display: grid;
        border: none; /* Remove main border */
        background-color: #fff; /* White background for the grid area */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05); /* Subtle shadow for grid */
         /* Grid columns will be set by JS based on grid size */
    }

    .grid-cell {
        width: 30px; /* Slightly larger cells */
        height: 30px; /* Slightly larger cells */
        box-sizing: border-box; /* Include border/padding in dimensions */
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.4em; /* Larger emoji */
        user-select: none; /* Prevent selecting emoji text */
        transition: background-color 0.4s ease, transform 0.2s ease, opacity 0.4s ease; /* Smooth transitions */
        border: 1px solid rgba(255, 255, 255, 0.5); /* Subtle light border */
    }

    /* Cell type styles */
    .cell-type-0 { /* Empty / Clearing */
        background-color: #d4c29b; /* Light brown/soil */
        border-color: #c0ae8c;
    }

    .cell-type-1 { /* Vegetation / Undergrowth */
        background-color: #a2c585; /* Soft green */
         border-color: #8ea375;
    }

    .cell-type-2 { /* Tree / Canopy */
        background-color: #5a923f; /* Rich forest green */
        border-color: #4a7d34;
    }

    /* Hover effect */
    .grid-cell:hover {
        transform: scale(1.05); /* Grow slightly on hover */
        box-shadow: 0 0 8px rgba(0, 0, 0, 0.2); /* Add shadow on hover */
        z-index: 1; /* Bring hovered cell to front */
    }

     /* Animation class for cutting */
    .grid-cell.cutting {
        transform: scale(0.8); /* Shrink slightly */
        opacity: 0.5; /* Fade slightly */
    }

     /* Animation class for growing */
    .grid-cell.growing {
        transform: scale(1.1); /* Grow slightly */
        opacity: 0.8; /* Fade in */
    }


    #controls {
        text-align: center;
        background-color: #ffffff; /* White background for controls */
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }

    #biodiversity-display {
        font-size: 1.5em; /* Larger font */
        font-weight: bold;
        margin-bottom: 15px; /* More space */
        color: #1b5e20; /* Dark green */
    }

    #biodiversity-display .label {
         font-weight: normal; /* Label is not bold */
         font-size: 0.8em; /* Label slightly smaller */
         color: #424242; /* Dark grey */
         margin-left: 5px;
    }

    #biodiversity-value {
        color: #388e3c; /* Medium green */
         transition: color 0.5s ease, transform 0.3s ease; /* Animation for value change */
         display: inline-block; /* Needed for transform */
    }

    /* Animation for biodiversity value change */
    #biodiversity-value.changed {
        color: #c62828; /* Red color on decrease */
         transform: scale(1.1);
    }

    .instruction {
        font-size: 1em;
        color: #555;
        margin-bottom: 20px;
    }

    #reset-button {
        display: inline-block;
        margin-top: 10px;
        padding: 12px 25px; /* Larger padding */
        font-size: 1.1em; /* Larger text */
        cursor: pointer;
        background-color: #4caf50; /* Green */
        color: white;
        border: none;
        border-radius: 5px; /* Rounded button */
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    #reset-button:hover {
        background-color: #388e3c; /* Darker green on hover */
        transform: translateY(-1px); /* Lift button slightly */
    }

    #reset-button:active {
         transform: translateY(0); /* Press button */
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    }


    #toggle-explanation {
        display: block;
        margin: 30px auto 20px auto; /* Adjust margin */
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        background-color: #e0e0e0; /* Light grey */
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }

     #toggle-explanation:hover {
        background-color: #d5d5d5; /* Darker grey on hover */
     }


    #explanation {
        margin-top: 20px;
        padding: 25px; /* More padding */
        background-color: #e1f5fe; /* Very light blue background */
        border-left: 6px solid #03a9f4; /* Cyan border */
        border-radius: 8px;
        direction: rtl; /* Ensure text is right-to-left */
        text-align: right; /* Align text to the right */
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }

    #explanation h2 {
        color: #0277bd; /* Dark blue */
        border-bottom: 1px solid #b3e5fc; /* Lighter cyan border */
        padding-bottom: 8px; /* More padding */
        margin-top: 15px;
        margin-bottom: 15px; /* More margin */
        text-align: right; /* Align explanation headers right */
    }

     #explanation p {
        margin-bottom: 12px; /* More space between paragraphs */
        line-height: 1.7; /* More comfortable line height */
        color: #444; /* Slightly softer text color */
     }

     #explanation p strong {
         color: #01579b; /* Darker blue for emphasis */
     }

      .grid-cell .emoji {
         display: inline-block; /* Needed for transform */
         transition: transform 0.3s ease;
      }


</style>

<button id="toggle-explanation">על יערות הגשם והסימולטור - מידע נוסף</button>

<div id="explanation" style="display: none;">
    <h2>יער גשם טרופי - מערכת אקולוגית תוססת</h2>
    <p>יערות הגשם הטרופיים הם פלא טבעי - אזורים ספוגי גשם, שופעי חום וירוק, המכסים פחות משלושה אחוזים מכדור הארץ אך מהווים משכן ליותר ממחצית המגוון הביולוגי העולמי! תנאי האקלים היציבים לאורך מיליוני שנים אפשרו התפתחות של רשת קשרים מורכבת בין מינים, היוצרים מערכת אקולוגית יציבה ועמידה להפליא - כל עוד היא שלמה.</p>

    <h2>רשת החיים המורכבת</h2>
    <p>ביער גשם, אין מין שחי לבדו. עצים ענקיים מספקים לא רק חמצן, אלא גם מזון, מחסה, אתרי קינון ורבייה לאלפי מיני חיות, חרקים וצמחים אחרים. צמחים אפיפיטיים כמו סחלבים ושרכים נצמדים לגזעי העצים, בעלי חיים תלויים בפירות או בפרחים ספציפיים, וכל שרשרת מזון קשורה בסופו של דבר לצמחייה העשירה. אפילו הקרקע התוססת מתחת לעצים, העשירה בפטריות וחיידקים, תלויה בחומר האורגני שמגיע מהם. הסימולטור שלנו מדגים, בפשטות, איך הסרת עץ אחד יכולה להשפיע על מינים רבים שתלויים בו או בסביבה שהוא יוצר.</p>

    <h2>הסכנה: כריתת יערות</h2>
    <p>לצערנו, יערות הגשם נעלמים בקצב מדאיג. שטחים עצומים נכרתים או נשרפים כדי לפנות מקום לחקלאות (בעיקר גידול בקר וגידולי שמן דקלים וסויה), כרייה, כריתת עצים לתעשיית העץ, ובניית דרכים ותשתיות. ההרס הפיזי הזה הוא רק ההתחלה. כאשר העצים נעלמים, המיקרו-אקלים משתנה דרמטית - הטמפרטורה עולה, הלחות יורדת, והאדמה נחשפת לשמש ולגשמים חזקים, מה שמוביל לשחיקה מהירה. מחזורי המים והחומרים המזינים משתבשים. פתאום, סביבה שהייתה מושלמת למינים רבים הופכת להיות עוינת.</p>

    <h2>מה קורה למגוון הביולוגי?</h2>
    <p>התוצאה הישירה של ההרס הזה היא אובדן דרמטי של מגוון ביולוגי. מינים רבים, במיוחד אלו המומחים לסביבה ספציפית (כמו עכבישים החיים רק על סוג מסוים של עלה, או קופים הניזונים רק מפירות עץ מסוים), מאבדים את ביתם ומקור מחייתם ונכחדים מקומית או אפילו גלובלית. גם מינים פחות ספציפיים נפגעים כאשר שטח היער מתכווץ ומתפצל לאזורים קטנים ומבודדים (פירגמנטציה). אוכלוסיות מינים מצטמצמות, מה שהופך אותן לפגיעות יותר למחלות ושינויים סביבתיים. הסמולטור ממחיש איך כל "נקודה" ירוקה על המפה היא פוטנציאל לקיום של מספר מינים, ואיך הסרתה פוגעת באופן מיידי בפוטנציאל הזה.</p>

    <h2>חשיבות השימור</h2>
    <p>שמירה על יערות הגשם אינה רק עניין של אהבת טבע. יערות אלו ממלאים תפקיד קריטי בוויסות האקלים העולמי, הם מאגר ענק של פחמן, והם משפיעים על דפוסי גשם גם באזורים מרוחקים. הם גם מספקים משאבים יקרים מפז - ממזון ותרופות ועד ידע מסורתי של עמים ילידים. אובדן יערות הגשם והמגוון הביולוגי שלהם הוא איום ישיר על יציבות כדור הארץ כפי שאנו מכירים אותה.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const gridContainer = document.getElementById('rainforest-grid');
        const biodiversityValueSpan = document.getElementById('biodiversity-value');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');
        const resetButton = document.getElementById('reset-button');

        const GRID_SIZE = 20; // 20x20 grid
        const CELL_SIZE = 30; // Pixels - Matches CSS
        const CELL_TYPES = {
            EMPTY: 0, // Clearing / Soil
            VEGETATION: 1, // Undergrowth / Bushes
            TREE: 2 // Canopy / Mature Tree
        };
        let grid = []; // 2D array to store cell types

        // Define species habitat rules (simplified & potentially expanded slightly)
        // Each function returns true if the cell at (r, c) contributes to the habitat
        // of an abstract "species group" based on local conditions.
        const speciesRules = [
            // Species Group 1: Deep Forest Dwellers (Need Tree cell)
            (r, c, currentGrid) => currentGrid[r][c] === CELL_TYPES.TREE,
            // Species Group 2: Canopy Specialists (Need Tree + at least one Tree neighbor)
            (r, c, currentGrid) => currentGrid[r][c] === CELL_TYPES.TREE && countNeighbors(r, c, CELL_TYPES.TREE, currentGrid) >= 1,
            // Species Group 3: Undergrowth & Edge (Need Vegetation + at least one Tree neighbor & one Vegetation neighbor)
            (r, c, currentGrid) => currentGrid[r][c] === CELL_TYPES.VEGETATION && hasNeighbor(r, c, CELL_TYPES.TREE, currentGrid) && hasNeighbor(r, c, CELL_TYPES.VEGETATION, currentGrid),
             // Species Group 4: Shrubland/Clearing proximity (Need Vegetation or Empty + adjacent to both Empty and Vegetation)
             (r, c, currentGrid) => (currentGrid[r][c] === CELL_TYPES.EMPTY || currentGrid[r][c] === CELL_TYPES.VEGETATION) && hasNeighbor(r, c, CELL_TYPES.EMPTY, currentGrid) && hasNeighbor(r, c, CELL_TYPES.VEGETATION, currentGrid),
             // Species Group 5: Large Canopy Ecosystem (Need Tree + at least two Tree neighbors)
            (r, c, currentGrid) => currentGrid[r][c] === CELL_TYPES.TREE && countNeighbors(r, c, CELL_TYPES.TREE, currentGrid) >= 2,
             // Species Group 6: Pioneer Species (Need Empty + adjacent to Vegetation) - colonize clearings
             (r, c, currentGrid) => currentGrid[r][c] === CELL_TYPES.EMPTY && hasNeighbor(r, c, CELL_TYPES.VEGETATION, currentGrid),
        ];

        // Helper function to get neighbors (includes diagonals)
        function getNeighbors(r, c, currentGrid) {
            const neighbors = [];
            for (let dr = -1; dr <= 1; dr++) {
                for (let dc = -1; dc <= 1; dc++) {
                    if (dr === 0 && dc === 0) continue; // Skip the cell itself
                    const nr = r + dr;
                    const nc = c + dc;
                    // Check bounds
                    if (nr >= 0 && nr < GRID_SIZE && nc >= 0 && nc < GRID_SIZE) {
                        neighbors.push({ r: nr, c: nc, type: currentGrid[nr][nc], element: getCellElement(nr, nc) }); // Include element reference
                    }
                }
            }
            return neighbors;
        }

         // Helper function to check if a cell has a neighbor of a specific type
        function hasNeighbor(r, c, type, currentGrid) {
             const neighbors = getNeighbors(r, c, currentGrid);
             return neighbors.some(neighbor => neighbor.type === type);
        }

        // Helper function to count neighbors of a specific type
        function countNeighbors(r, c, type, currentGrid) {
             const neighbors = getNeighbors(r, c, currentGrid);
             return neighbors.filter(neighbor => neighbor.type === type).length;
        }

        // Helper function to get a cell's DOM element
        function getCellElement(r, c) {
             return gridContainer.querySelector(`.grid-cell[data-row="${r}"][data-col="${c}"]`);
        }


        // Function to calculate biodiversity index
        function calculateBiodiversity(currentGrid) {
            let totalBiodiversity = 0;
            for (let r = 0; r < GRID_SIZE; r++) {
                for (let c = 0; c < GRID_SIZE; c++) {
                    // For each cell, check which species groups can exist there based on the rules
                    speciesRules.forEach(rule => {
                        if (rule(r, c, currentGrid)) {
                            totalBiodiversity++; // Increment for every potential species group 'spot'
                        }
                    });
                }
            }
            return totalBiodiversity;
        }

        // Function to render the initial grid
        function renderGrid() {
            gridContainer.innerHTML = ''; // Clear existing grid
            gridContainer.style.gridTemplateColumns = `repeat(${GRID_SIZE}, ${CELL_SIZE}px)`;

            for (let r = 0; r < GRID_SIZE; r++) {
                for (let c = 0; c < GRID_SIZE; c++) {
                    const cell = document.createElement('div');
                    cell.classList.add('grid-cell', `cell-type-${grid[r][c]}`);
                    cell.dataset.row = r;
                    cell.dataset.col = c;

                     // Add a nested span for emoji/content to control animations
                    const cellContent = document.createElement('span');
                    cellContent.classList.add('emoji');
                    if (grid[r][c] === CELL_TYPES.TREE) cellContent.textContent = '🌳';
                    else if (grid[r][c] === CELL_TYPES.VEGETATION) cellContent.textContent = '🌿';
                     else cellContent.textContent = '🟫'; // Use brown square for empty
                     cell.appendChild(cellContent);


                    cell.addEventListener('click', handleCellClick);
                    gridContainer.appendChild(cell);
                }
            }
        }

        // Function to update a single cell's appearance
        // This function is now called when a cell changes AND when its neighbor changes
        function updateCellAppearance(r, c) {
            const cellElement = getCellElement(r, c);
            if (cellElement) {
                const currentType = grid[r][c];
                 const cellContent = cellElement.querySelector('.emoji');

                // Remove all previous type classes
                cellElement.classList.remove(
                    `cell-type-${CELL_TYPES.EMPTY}`,
                    `cell-type-${CELL_TYPES.VEGETATION}`,
                    `cell-type-${CELL_TYPES.TREE}`
                );
                // Add the current type class
                cellElement.classList.add(`cell-type-${currentType}`);

                 // Update emoji with transition
                 cellContent.style.transform = 'scale(0.5)'; // Shrink before changing
                 cellContent.style.opacity = '0.5';
                 setTimeout(() => { // Allow transition to happen before changing content
                      if (currentType === CELL_TYPES.TREE) cellContent.textContent = '🌳';
                      else if (currentType === CELL_TYPES.VEGETATION) cellContent.textContent = '🌿';
                      else cellContent.textContent = '🟫';
                      cellContent.style.transform = 'scale(1)'; // Grow back to normal size
                      cellContent.style.opacity = '1';
                 }, 200); // Half of the CSS transition duration


                // Add temporary animation classes if needed (currently handled by CSS transitions on default classes)
                // If more complex animations were needed, add class here and remove after timeout
            }
        }


        // Handle cell click
        function handleCellClick(event) {
            const cellElement = event.target.closest('.grid-cell'); // Ensure we get the cell div
            if (!cellElement) return; // Safeguard

            const r = parseInt(cellElement.dataset.row);
            const c = parseInt(cellElement.dataset.col);
            const originalType = grid[r][c];
            let typeChanged = false;


            // Interaction logic:
            // Click Tree (2) -> Empty (0) [Cut]
            // Click Empty (0) -> Vegetation (1) [Limited regrowth]
            // Click Vegetation (1) -> Vegetation (1) [No change on click for now, could add decay?]

            if (grid[r][c] === CELL_TYPES.TREE) {
                grid[r][c] = CELL_TYPES.EMPTY; // Cut the tree
                cellElement.classList.add('cutting'); // Add animation class
                setTimeout(() => cellElement.classList.remove('cutting'), 400); // Remove class after animation
                typeChanged = true;

            } else if (grid[r][c] === CELL_TYPES.EMPTY) {
                 grid[r][c] = CELL_TYPES.VEGETATION; // Allow some regrowth in empty areas
                 cellElement.classList.add('growing'); // Add animation class
                 setTimeout(() => cellElement.classList.remove('growing'), 400); // Remove class after animation
                 typeChanged = true;
            }
            // If Vegetation, do nothing on click.

            if (typeChanged) {
                // Update the clicked cell visually
                updateCellAppearance(r, c);

                // Update appearance of neighbors as their 'context' might have changed
                const neighbors = getNeighbors(r, c, grid); // Use the *updated* grid state
                neighbors.forEach(neighbor => {
                     updateCellAppearance(neighbor.r, neighbor.c);
                });

                 // Recalculate and update biodiversity for the entire grid
                 updateBiodiversityDisplay();
            }
        }

        // Update biodiversity display
        function updateBiodiversityDisplay() {
            const oldBiodiversity = parseInt(biodiversityValueSpan.textContent) || 0;
            const newBiodiversity = calculateBiodiversity(grid);

            biodiversityValueSpan.textContent = newBiodiversity;

            // Add animation class if biodiversity decreased significantly
            if (newBiodiversity < oldBiodiversity) {
                 biodiversityValueSpan.classList.add('changed');
                 setTimeout(() => {
                      biodiversityValueSpan.classList.remove('changed');
                      // Optional: Add a class for increase animation too if desired
                      // else if (newBiodiversity > oldBiodiversity) { biodiversityValueSpan.classList.add('increased'); }
                 }, 600); // Animation duration
            } else {
                // Ensure no animation class if no significant change or increased
                 biodiversityValueSpan.classList.remove('changed');
                 // biodiversityValueSpan.classList.remove('increased');
            }
        }

        // Initialize grid
        function initializeGrid() {
            grid = [];
            // Fill the grid mostly with trees (type 2) and some vegetation (type 1)
            // Use a simple random distribution biased towards trees, but ensuring some variability
            const treeRatio = 0.75; // 75% trees initially
            const vegetationRatio = 0.2; // 20% vegetation
            // The rest will be empty (0.05)

            for (let r = 0; r < GRID_SIZE; r++) {
                grid[r] = [];
                for (let c = 0; c < GRID_SIZE; c++) {
                    const rand = Math.random();
                    if (rand < treeRatio) {
                        grid[r][c] = CELL_TYPES.TREE;
                    } else if (rand < treeRatio + vegetationRatio) {
                        grid[r][c] = CELL_TYPES.VEGETATION;
                    } else {
                        grid[r][c] = CELL_TYPES.EMPTY;
                    }
                }
            }
             // Ensure at least a few empty spots and vegetation spots exist if purely random resulted in none
             let emptyCount = 0;
             let vegCount = 0;
             for(let r=0; r<GRID_SIZE; r++) {
                 for(let c=0; c<GRID_SIZE; c++) {
                     if (grid[r][c] === CELL_TYPES.EMPTY) emptyCount++;
                     if (grid[r][c] === CELL_TYPES.VEGETATION) vegCount++;
                 }
             }
             if (emptyCount < 5) { grid[Math.floor(GRID_SIZE/2)][Math.floor(GRID_SIZE/2)] = CELL_TYPES.EMPTY; }
             if (vegCount < 5) { grid[Math.floor(GRID_SIZE/4)][Math.floor(GRID_SIZE/4)] = CELL_TYPES.VEGETATION; }

        }

        // Reset simulation
        function resetSimulation() {
             initializeGrid();
             renderGrid(); // Full re-render on reset is fine
             updateBiodiversityDisplay(); // Initial biodiversity display
        }

        // Toggle explanation visibility
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר מידע נוסף' : 'על יערות הגשם והסימולטור - מידע נוסף';
        });

        // Add reset button listener
        resetButton.addEventListener('click', resetSimulation);


        // Initial setup on load
        resetSimulation(); // Call reset to initialize and render
    });
</script>
```