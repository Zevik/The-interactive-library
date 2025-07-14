---
title: "הדמיית אלגוריתמי מיון: השוואה ויזואלית חווייתית"
english_slug: sorting-algorithm-visualization-bubble-merge-quick
category: "טכנולוגיה / מדעי המחשב"
tags:
  - אלגוריתמים
  - מבני נתונים
  - ויזואליזציה
  - מיון
---
# הדמיית אלגוריתמי מיון: צלילה ויזואלית

ברוכים הבאים למעבדת המיון הוויזואלית! כאן תוכלו לראות במו עיניכם כיצד פועלים שלושה מאלגוריתמי המיון המפורסמים ביותר במדעי המחשב: מיון בועות, מיון מיזוג ומיון מהיר. במקום רק לקרוא עליהם, תוכלו להתנסות, ליצור מערכים בגדלים שונים, לשלוט במהירות ההדמיה ולצפות בזמן אמת ב"ריקוד" האיברים כשהם מסתדרים בסדר הנכון. הכירו את התהליכים הייחודיים של כל אלגוריתם וגלו את האלגוריתם היעיל ביותר למשימה!

<div id="sorting-app">
    <div class="controls">
        <div class="control-group">
            <label for="arraySize">גודל מערך:</label>
            <input type="number" id="arraySize" value="50" min="10" max="200">
        </div>
        <div class="control-group">
            <label for="speed">מהירות:</label>
            <input type="range" id="speed" min="1" max="100" value="50">
        </div>
         <button id="generateArray" class="control-button">צור מערך חדש ✨</button>
         <div class="algo-selection">
            בחר אלגוריתם:
            <button class="algo-button control-button" data-algo="bubble">🎈 בועות</button>
            <button class="algo-button control-button" data-algo="merge">🧬 מיזוג</button>
            <button class="algo-button control-button" data-algo="quick">⚡ מהיר</button>
         </div>
         <button id="startSorting" class="control-button primary">התחל מיון ▶️</button>
         <button id="resetSorting" class="control-button secondary">איפוס 🔄</button>
    </div>
    <div id="actionText" class="action-text">התחל ביצירת מערך ובחירת אלגוריתם.</div>
    <div id="visualizationArea" class="visualization-area"></div>
</div>

<button id="toggleExplanation" class="toggle-button">הסבר על האלגוריתמים 📖</button>

<div id="explanation" style="display: none;">
    <h2>הסבר על אלגוריתמי המיון המודגמים:</h2>

    <h3>1. מיון בועות (Bubble Sort)</h3>
    <p>דמיינו בועות גז עולות למעלה במים. מיון בועות עובד באופן דומה: הוא עובר שוב ושוב על הרשימה, משווה כל זוג איברים סמוכים ומחליף ביניהם אם הם לא בסדר הנכון. האיברים ה"כבדים" (הגדולים יותר, אם ממיינים בסדר עולה) "שוקעים" למטה, וה"קלים" (הקטנים יותר) "צפים" למעלה (או להיפך, תלוי בסדר המיון). התהליך חוזר על עצמו עד שאין יותר החלפות בכל מעבר – סימן שהרשימה ממוינת לחלוטין! למרות פשטותו, האלגוריתם הזה אינו יעיל במיוחד עבור רשימות גדולות (מורכבות זמן של O(n²)) ולכן משמש בעיקר למטרות לימודיות או לרשימות קצרצרות.</p>

    <h3>2. מיון מיזוג (Merge Sort)</h3>
    <p>זהו אלגוריתם מתוחכם יותר, המבוסס על עקרון "חלק וכבוש". הוא מחלק את הרשימה המקורית שוב ושוב לשניים, עד שמגיעים לתת-רשימות קטנות כל כך שהן מכילות איבר בודד (ורשימה של איבר אחד תמיד ממוינת!). לאחר מכן, האלגוריתם מתחיל למזג את תת-הרשימות הממוינות הללו בחזרה, זוג זוג, תוך כדי יצירת רשימות ממוינות גדולות יותר ויותר, עד שכל הרשימה המקורית ממוזגת וממוינת. שלב ה"מיזוג" הוא הלב של האלגוריתם. היתרון הגדול של מיון מיזוג הוא היציבות והיעילות שלו – מורכבות זמן אחידה של O(n log n) בכל המקרים, מה שהופך אותו לבחירה טובה עבור מערכי נתונים גדולים.</p>

    <h3>3. מיון מהיר (Quick Sort)</h3>
    <p>כפי ששמו מרמז, זהו לרוב האלגוריתם המהיר והיעיל ביותר בפועל! גם הוא מבוסס על "חלק וכבוש". האלגוריתם בוחר איבר אחד מהרשימה וקורא לו "ציר" (pivot). לאחר מכן, הוא מארגן מחדש את שאר האיברים כך שכל האיברים הקטנים מהציר יהיו בצד אחד שלו, וכל האיברים הגדולים יהיו בצד השני. זה נקרא שלב ה"חלוקה" (partitioning). לאחר שהציר נמצא במקומו הסופי, האלגוריתם חוזר על התהליך באופן רקורסיבי על שתי תת-הרשימות (זו שמשמאל לציר וזו שמימין לו) עד שכל הרשימה ממוינת. במקרה הממוצע הוא מהיר ביותר (O(n log n)), אך במקרה הגרוע (אם בחירת הציר תמיד גרועה), הוא יכול להגיע למורכבות של O(n²).</p>
    <p>עכשיו שהכרתם את הגיבורים, חזרו למעלה והתחילו לשחק עם ההדמיה! נסו גדלים שונים ומהירויות שונות, ובחנו כיצד כל אלגוריתם מתמודד עם המשימה.</p>
</div>

<style>
    :root {
        /* Define a modern color palette */
        --color-primary: #4a90e2; /* Vibrant Blue for bars */
        --color-secondary: #50e3c2; /* Teal for merging */
        --color-comparing: #f5a623; /* Orange for comparison */
        --color-swapping: #d0021b; /* Red for swapping */
        --color-pivot: #9013fe; /* Purple for pivot */
        --color-sorted: #7ed321; /* Green for sorted */
        --color-background: #f7f9fb; /* Light background */
        --color-card-background: #ffffff; /* White for containers */
        --color-text: #333333; /* Dark grey for text */
        --color-heading: #0e2a47; /* Dark blue for headings */
        --color-border: #e0e6ed; /* Light border */
        --color-button-primary: #007bff; /* Standard blue button */
        --color-button-secondary: #6c757d; /* Grey button */
        --color-button-algo: #28a745; /* Green algo button */
        --color-button-algo-selected: #ffc107; /* Yellow selected algo button */
    }

    body {
        font-family: 'Rubik', sans-serif; /* Use Rubik or similar pleasant Hebrew font */
        direction: rtl;
        text-align: right;
        background-color: var(--color-background);
        color: var(--color-text);
        line-height: 1.7;
        padding: 20px;
        margin: 0;
        font-size: 1.1rem;
    }

    h1, h2, h3 {
        color: var(--color-heading);
        margin-bottom: 15px;
    }

    h1 {
        text-align: center;
        margin-bottom: 30px;
    }

    h2 {
        border-bottom: 2px solid var(--color-primary);
        padding-bottom: 5px;
    }

    #sorting-app, #explanation {
        background-color: var(--color-card-background);
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        margin-bottom: 25px;
        border: 1px solid var(--color-border);
    }

    .controls {
        display: flex;
        flex-wrap: wrap;
        gap: 15px 20px; /* Row gap, Column gap */
        align-items: center;
        margin-bottom: 20px;
        padding-bottom: 20px;
        border-bottom: 1px solid var(--color-border);
    }

     .control-group {
         display: flex;
         align-items: center;
         gap: 8px;
     }

    .controls label {
        font-weight: bold;
        color: var(--color-heading);
    }

    .controls input[type="number"],
    .controls input[type="range"] {
        padding: 10px;
        border: 1px solid var(--color-border);
        border-radius: 6px;
        font-size: 1rem;
        background-color: #fefefe;
    }

    input[type="number"] {
        width: 70px;
    }

    input[type="range"] {
        flex-grow: 1;
        min-width: 120px; /* Ensure it doesn't get too small */
        max-width: 250px;
        -webkit-appearance: none; /* Override default look */
        appearance: none;
        height: 8px;
        background: var(--color-border);
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 4px;
    }

    input[type="range"]:hover {
        opacity: 1;
    }

    input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--color-primary);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid var(--color-card-background);
    }

     input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--color-primary);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid var(--color-card-background);
    }


    .control-button {
        padding: 10px 18px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1rem;
        transition: background-color 0.2s ease, transform 0.1s ease, opacity 0.2s ease;
        color: white;
        font-weight: bold;
        text-align: center;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 5px;
    }

    .control-button:hover:not(:disabled) {
        opacity: 0.9;
    }

    .control-button:active:not(:disabled) {
        transform: scale(0.98);
    }

    .control-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.6;
    }

     .primary {
        background-color: var(--color-button-primary);
     }
     .primary:hover:not(:disabled) {
         background-color: #0056b3;
     }

    .secondary {
         background-color: var(--color-button-secondary);
     }
     .secondary:hover:not(:disabled) {
         background-color: #5a6268;
     }


    .algo-selection {
        display: flex;
        align-items: center;
        gap: 10px;
        flex-wrap: wrap;
        font-weight: bold;
        color: var(--color-heading);
    }

    .algo-button {
        background-color: var(--color-button-algo);
    }

    .algo-button:hover:not(:disabled) {
        background-color: #218838;
    }

    .algo-button.selected {
        background-color: var(--color-button-algo-selected);
        color: var(--color-text);
        border: 2px solid #d39e00;
        box-shadow: 0 0 8px rgba(255, 193, 7, 0.5);
    }

    #startSorting {
        background-color: var(--color-swapping); /* Use red for "go" as it's dynamic */
    }
    #startSorting:hover:not(:disabled) {
        background-color: #c82333;
    }

    #resetSorting {
        background-color: var(--color-button-secondary);
    }
     #resetSorting:hover:not(:disabled) {
         background-color: #5a6268;
    }

    .action-text {
        text-align: center;
        font-size: 1.1em;
        margin-bottom: 15px;
        min-height: 1.5em; /* Reserve space */
        color: var(--color-heading);
        font-weight: bold;
    }


    .visualization-area {
        display: flex;
        align-items: flex-end;
        width: 100%;
        height: 400px; /* Consistent height */
        background-color: var(--color-background);
        border-radius: 8px;
        overflow: hidden;
        margin-top: 15px;
        padding: 5px 0; /* Add vertical padding for bars */
        box-sizing: border-box;
         position: relative; /* Needed if adding absolute positioned elements later */
    }

    .bar {
        width: calc(100% / var(--num-bars)); /* Calculate width based on number of bars */
        background-color: var(--color-primary);
        margin: 0 var(--bar-spacing); /* Small gap between bars, controlled by JS */
        box-sizing: border-box;
        transition: height 0.1s ease, background-color 0.1s ease; /* Smooth transitions */
         border-radius: 3px 3px 0 0; /* Rounded top corners */
    }

    .bar.comparing {
        background-color: var(--color-comparing); /* Yellow/Orange */
    }

    .bar.swapping {
        background-color: var(--color-swapping); /* Red */
    }

    .bar.sorted {
        background-color: var(--color-sorted); /* Green */
    }

    .bar.pivot {
        background-color: var(--color-pivot); /* Purple */
    }

     .bar.merging {
        background-color: var(--color-secondary); /* Teal */
     }

    /* Add a pulse effect for elements being actively compared/swapped */
    .bar.comparing, .bar.swapping {
        animation: pulse 0.5s infinite alternate;
    }

    @keyframes pulse {
        from { transform: scaleY(1); }
        to { transform: scaleY(1.05); } /* Slight scale up */
    }


    .toggle-button {
        display: block;
        width: auto;
        margin: 25px auto;
        background-color: var(--color-secondary);
        color: var(--color-heading);
         padding: 12px 20px;
         font-size: 1.1rem;
         font-weight: bold;
         border-radius: 8px;
         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
     .toggle-button:hover {
         background-color: #138496; /* Darker teal */
         color: white;
     }


    #explanation {
        background-color: var(--color-card-background);
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
         border: 1px solid var(--color-border);
    }

    #explanation h3 {
        margin-top: 20px;
        margin-bottom: 10px;
        color: var(--color-primary);
    }

     @media (max-width: 768px) {
         .controls {
             flex-direction: column;
             align-items: stretch;
         }
         .control-group, .algo-selection {
             width: 100%;
             justify-content: space-between;
             flex-wrap: wrap;
         }
         input[type="number"] {
             width: auto;
             flex-grow: 1;
         }
         input[type="range"] {
             width: auto;
             max-width: none;
             flex-grow: 1;
         }
          .algo-selection .algo-button {
              flex-grow: 1;
              text-align: center;
          }
          .control-button {
               width: 100%;
          }
          .visualization-area {
              height: 300px; /* Reduce height on smaller screens */
          }
     }
</style>

<script>
    const arraySizeInput = document.getElementById('arraySize');
    const speedInput = document.getElementById('speed');
    const generateButton = document.getElementById('generateArray');
    const algoButtons = document.querySelectorAll('.algo-button');
    const startButton = document.getElementById('startSorting');
    const resetButton = document.getElementById('resetSorting');
    const visualizationArea = document.getElementById('visualizationArea');
    const actionTextElement = document.getElementById('actionText');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');

    let array = [];
    let arraySize = parseInt(arraySizeInput.value);
    let animationSpeed = 101 - parseInt(speedInput.value); // Convert range value to delay (lower range = higher speed)
    let selectedAlgorithm = null; // null, 'bubble', 'merge', 'quick'
    let isSorting = false;
    let abortController = null; // For stopping async operations

    // Helper function for delay
    const controlledDelay = async (ms, signal) => {
        return new Promise((resolve, reject) => {
            const timer = setTimeout(resolve, ms);
            signal.addEventListener('abort', () => {
                clearTimeout(timer);
                reject(new Error('Sorting aborted'));
            }, { once: true });
        });
    };

    // Update the text displaying the current action
    function updateActionText(text) {
        actionTextElement.textContent = text;
    }

    // Generate initial array and display bars
    function generateArray() {
        if (isSorting) return; // Prevent regeneration while sorting
        abortSorting(false); // Ensure any pending sort is aborted silently
         resetState(); // Reset buttons and state flags

        arraySize = parseInt(arraySizeInput.value);
        array = [];
        visualizationArea.innerHTML = ''; // Clear previous bars
        visualizationArea.style.setProperty('--num-bars', arraySize); // Set CSS variable for bar width

         // Calculate bar spacing based on size
         const totalSpacing = arraySize > 1 ? Math.max(0.5, 50 / arraySize) : 0; // Adjust spacing based on size
         visualizationArea.style.setProperty('--bar-spacing', `${totalSpacing / 2}px`);


        for (let i = 0; i < arraySize; i++) {
            // Generate numbers from 10 to visualizationArea.clientHeight - 10 (to leave some padding)
            const value = Math.floor(Math.random() * (visualizationArea.clientHeight - 20)) + 10;
            array.push(value);
            const bar = document.createElement('div');
            bar.classList.add('bar');
            bar.style.height = `${value}px`;
             // Set initial color
             bar.style.backgroundColor = 'var(--color-primary)';
            visualizationArea.appendChild(bar);
        }
        updateActionText('מערך חדש נוצר. בחר אלגוריתם והתחל מיון.');
         // Reset button styles and selections
         algoButtons.forEach(btn => btn.classList.remove('selected'));
         selectedAlgorithm = null;
         startButton.disabled = true; // Cannot start until algo is selected
         resetButton.disabled = true; // Cannot reset until sorting starts
    }

    // Update bar heights and colors from the current array state
    function updateBarColors(comparing = [], swapping = [], pivot = null, merging = [], sorted = []) {
        const bars = visualizationArea.querySelectorAll('.bar');
        bars.forEach((bar, index) => {
             // Only update height if the actual array value changed
             const currentHeight = parseFloat(bar.style.height);
             const newHeight = array[index];
             if (currentHeight !== newHeight) {
                 bar.style.height = `${newHeight}px`;
             }


            // Reset specific state classes first
            bar.classList.remove('comparing', 'swapping', 'pivot', 'merging', 'sorted');

            // Add current state classes
            if (comparing.includes(index)) {
                bar.classList.add('comparing');
            }
            if (swapping.includes(index)) {
                bar.classList.add('swapping');
            }
            if (index === pivot) {
                 bar.classList.add('pivot');
            }
            if (merging.includes(index)) {
                 bar.classList.add('merging');
            }
             if (sorted.includes(index)) {
                bar.classList.add('sorted');
            } else if (!comparing.includes(index) && !swapping.includes(index) && index !== pivot && !merging.includes(index)) {
                 // Default color if not in any specific state
                 bar.style.backgroundColor = 'var(--color-primary)';
             }
        });
    }

     // Reset control state
     function resetState() {
         isSorting = false;
         startButton.disabled = true; // Disabled until algorithm selected
         generateButton.disabled = false;
         algoButtons.forEach(btn => {
             btn.disabled = false;
             btn.classList.remove('selected');
         });
         arraySizeInput.disabled = false;
         resetButton.disabled = true;
         selectedAlgorithm = null;
     }

     // Abort sorting process
     function abortSorting(showMessage = true) {
         if (abortController) {
             abortController.abort();
             abortController = null;
              if (showMessage) updateActionText('המיון בוטל.');
         }
     }


    // Bubble Sort Algorithm (Visualized)
    async function bubbleSort(arr, signal) {
        updateActionText('מיון בועות התחיל...');
        const n = arr.length;
        let swapped;
         const sortedIndices = []; // To track elements that are in their final sorted position

        try {
            for (let i = 0; i < n - 1; i++) {
                swapped = false;
                for (let j = 0; j < n - 1 - i; j++) {
                     if (signal.aborted) throw new Error('Aborted');
                    updateActionText(`משווה אלמנטים ${j} ו-${j+1}`);
                    updateBarColors([j, j + 1], [], null, [], sortedIndices); // Highlight comparing
                    await controlledDelay(animationSpeed, signal);

                    if (arr[j] > arr[j + 1]) {
                         if (signal.aborted) throw new Error('Aborted');
                        // Swap elements
                        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
                        updateActionText(`מחליף אלמנטים ${j} ו-${j+1}`);
                        updateBarColors([], [j, j + 1], null, [], sortedIndices); // Highlight swapping
                        await controlledDelay(animationSpeed * 2, signal); // Longer delay for swap
                        swapped = true;
                    }
                }
                // The largest element of this pass is now in its final place
                 sortedIndices.push(n - 1 - i);
                 if (signal.aborted) throw new Error('Aborted');
                 updateBarColors([], [], null, [], sortedIndices); // Mark as sorted
                 await controlledDelay(animationSpeed, signal);


                if (!swapped) break; // If no swaps occurred in a pass, the array is sorted
            }
             // Mark remaining elements as sorted if loop finished early
            while(sortedIndices.length < n) {
                 sortedIndices.push(n - 1 - sortedIndices.length);
            }
            updateBarColors([], [], null, [], sortedIndices);
             updateActionText('מיון בועות הסתיים בהצלחה!');

        } catch (e) {
            if (e.message !== 'Aborted') throw e;
             // Abort handled by caller
        }
    }

    // Merge Sort Algorithm (Visualized)
    async function mergeSort(arr, start, end, signal) {
        if (signal.aborted) throw new Error('Aborted');
        if (start >= end) {
             // Mark single element as sorted (base case visual)
             updateBarColors([], [], null, [], [start]);
             await controlledDelay(animationSpeed / 4, signal);
             return; // Base case
        }

        const mid = Math.floor((start + end) / 2);
        updateActionText(`מחלק: ${start}-${mid} ו- ${mid+1}-${end}`);
         await controlledDelay(animationSpeed / 2, signal);


        await mergeSort(arr, start, mid, signal);
        await mergeSort(arr, mid + 1, end, signal);

        await merge(arr, start, mid, end, signal);
    }

    async function merge(arr, start, mid, end, signal) {
        if (signal.aborted) throw new Error('Aborted');
        const mergedArray = [];
        let left = start;
        let right = mid + 1;
        // Create a copy of the *relevant section* of the array for merging
        const tempArray = arr.slice(start, end + 1);
        let tempLeft = 0; // Index for the left half of tempArray
        let tempRight = mid - start + 1; // Index for the right half of tempArray

         updateActionText(`ממזג טווחים ${start}-${mid} ו ${mid+1}-${end}...`);
         // Mark elements being merged
        const mergingIndices = Array.from({ length: end - start + 1 }, (_, k) => start + k);
        updateBarColors([], [], null, mergingIndices);
        await controlledDelay(animationSpeed, signal);


        let k = start; // Index in the original array

        while (tempLeft < (mid - start + 1) && tempRight < (end - start + 1)) {
             if (signal.aborted) throw new Error('Aborted');
            // Highlight elements being compared during merge
             updateBarColors([start + tempLeft, start + tempRight], [], null, mergingIndices);
            await controlledDelay(animationSpeed, signal);

            if (tempArray[tempLeft] <= tempArray[tempRight]) {
                arr[k] = tempArray[tempLeft];
                tempLeft++;
            } else {
                arr[k] = tempArray[tempRight];
                tempRight++;
            }
            // Visualize element being placed back
             updateBarColors([], [k], null, mergingIndices);
             await controlledDelay(animationSpeed / 2, signal);
            k++;
        }

        // Copy the remaining elements from left half
        while (tempLeft < (mid - start + 1)) {
             if (signal.aborted) throw new Error('Aborted');
             updateBarColors([start + tempLeft], [], null, mergingIndices);
             await controlledDelay(animationSpeed, signal);
            arr[k] = tempArray[tempLeft];
             updateBarColors([], [k], null, mergingIndices);
             await controlledDelay(animationSpeed / 2, signal);
            tempLeft++;
            k++;
        }

        // Copy the remaining elements from right half
        while (tempRight < (end - start + 1)) {
             if (signal.aborted) throw new Error('Aborted');
              updateBarColors([start + tempRight], [], null, mergingIndices);
             await controlledDelay(animationSpeed, signal);
            arr[k] = tempArray[tempRight];
             updateBarColors([], [k], null, mergingIndices);
             await controlledDelay(animationSpeed / 2, signal);
            tempRight++;
            k++;
        }

        // Mark the merged section as sorted
        const sortedIndices = Array.from({ length: end - start + 1 }, (_, k) => start + k);
        updateBarColors([], [], null, [], sortedIndices);
        await controlledDelay(animationSpeed, signal);

    }


    // Quick Sort Algorithm (Visualized)
    async function quickSort(arr, low, high, signal) {
        if (signal.aborted) throw new Error('Aborted');
        if (low < high) {
            const pi = await partition(arr, low, high, signal);

            // Mark pivot as sorted after partition
             updateBarColors([], [], null, [], Array.from({ length: pi - low + 1 }, (_, k) => low + k).filter(i => i === pi).concat(Array.from({ length: low }, (_, k) => k).filter(i => barsAreSortedUpTo(i)))); // Mark current pivot + previous sorted

             await quickSort(arr, low, pi - 1, signal);
            await quickSort(arr, pi + 1, high, signal);
        } else if (low === high) {
             // Mark single element partition as sorted
             updateBarColors([], [], null, [], [low]);
             await controlledDelay(animationSpeed / 4, signal);
        }
    }

     // Helper to check if bars up to index i are sorted (approximation for visual tracking)
     function barsAreSortedUpTo(index) {
         const bars = visualizationArea.querySelectorAll('.bar');
         if (index < 0 || index >= bars.length) return false;
         return bars[index].classList.contains('sorted');
     }


    async function partition(arr, low, high, signal) {
         if (signal.aborted) throw new Error('Aborted');
        const pivotValue = arr[high];
         updateActionText(`בוחר ציר: אלמנט ${high}`);
         updateBarColors([], [], high); // Highlight pivot
         await controlledDelay(animationSpeed, signal);


        let i = (low - 1); // Index of smaller element

        for (let j = low; j <= high - 1; j++) {
             if (signal.aborted) throw new Error('Aborted');
            // Highlight elements being compared to pivot
             updateActionText(`משווה אלמנט ${j} עם ציר ${high}`);
            updateBarColors([j], [], high); // Only highlight current element being compared vs pivot
             await controlledDelay(animationSpeed, signal);

            // If current element is smaller than the pivot
            if (arr[j] < pivotValue) {
                i++;
                // swap arr[i] and arr[j]
                 if (signal.aborted) throw new Error('Aborted');
                 updateActionText(`מחליף אלמנטים ${i} ו-${j}`);
                [arr[i], arr[j]] = [arr[j], arr[i]];
                // Highlight swapping, keep pivot highlighted
                updateBarColors([], [i, j], high);
                 await controlledDelay(animationSpeed * 2, signal);
            }
        }
         if (signal.aborted) throw new Error('Aborted');
        // swap arr[i+1] and arr[high] (pivot)
         updateActionText(`ממקם ציר ${high} במקומו הסופי ${i+1}`);
        [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
        // Highlight swapping, including pivot moving to final place
         updateBarColors([], [i + 1, high], null); // Pivot is no longer "pivot" but being swapped into place
         await controlledDelay(animationSpeed * 2, signal);

         return (i + 1); // Return partition index (pivot's final index)
    }


    // Event Listeners
    generateButton.addEventListener('click', generateArray);

    algoButtons.forEach(button => {
        button.addEventListener('click', () => {
             if (isSorting) return; // Prevent changing algorithm during sort
            algoButtons.forEach(btn => btn.classList.remove('selected'));
            button.classList.add('selected');
            selectedAlgorithm = button.dataset.algo;
             startButton.disabled = false; // Enable start button once algo selected
             updateActionText(`אלגוריתם "${button.textContent.trim()}" נבחר. לחץ התחל מיון.`);
        });
    });

    startButton.addEventListener('click', async () => {
        if (isSorting || !selectedAlgorithm) {
             if (!selectedAlgorithm) alert('אנא בחר אלגוריתם מיון לפני ההתחלה.');
            return;
        }

        isSorting = true;
        startButton.disabled = true;
        generateButton.disabled = true;
        algoButtons.forEach(btn => btn.disabled = true);
         arraySizeInput.disabled = true;
         resetButton.disabled = false; // Enable reset once sorting starts

         abortController = new AbortController();
         const signal = abortController.signal;

        try {
            switch (selectedAlgorithm) {
                case 'bubble':
                    await bubbleSort(array, signal);
                    break;
                case 'merge':
                     updateActionText('מיון מיזוג התחיל...');
                    await mergeSort(array, 0, array.length - 1, signal);
                    break;
                case 'quick':
                     updateActionText('מיון מהיר התחיל...');
                    await quickSort(array, 0, array.length - 1, signal);
                    break;
            }
             // Final state: all bars green
             updateBarColors([], [], null, [], Array.from({ length: array.length }, (_, k) => k));
             updateActionText('המיון הושלם בהצלחה! ✅');

        } catch (e) {
            if (e.message !== 'Aborted') {
                 console.error("Sorting Error:", e);
                 updateActionText("אירעה שגיאה במהלך המיון. ❌");
            }
             // If aborted or error, ensure state is reset visually
             updateBarColors(); // Reset colors to default (removes state classes)
        } finally {
            resetState(); // Reset button states etc.
        }
    });

    resetButton.addEventListener('click', () => {
        abortSorting(); // Abort current sort
        generateArray(); // Generate a new random array
    });


    speedInput.addEventListener('input', (event) => {
        animationSpeed = 101 - parseInt(event.target.value);
         updateActionText(`מהירות אנימציה הוגדרה: ${event.target.value}/100`);
    });

     // Ensure array size change triggers new array generation
     arraySizeInput.addEventListener('change', generateArray);


    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר 📚' : 'הסבר על האלגוריתמים 📖';
         // Scroll to explanation if showing it
         if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });

    // Initial setup
    generateArray();
    resetButton.disabled = true; // Reset is disabled initially
    startButton.disabled = true; // Start is disabled initially until algo is selected

</script>