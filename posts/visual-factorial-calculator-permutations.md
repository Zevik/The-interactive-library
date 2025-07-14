---
title: "קסם הסידור: מחשבון עצרת ויזואלי - כמה דרכים לסדר הכל?"
english_slug: visual-factorial-calculator-permutations
category: "מדעים מדויקים / מתמטיקה"
tags: ["עצרת", "קומבינטוריקה", "פרמוטציות", "הדמיה אינטראקטיבית", "מתמטיקה כיפית"]
---
# קסם הסידור: כמה דרכים לסדר את הדברים שלך?

האם תהיתם פעם בכמה דרכים שונות אפשר לסדר קבוצה פשוטה של חפצים? בואו נשחק ונגלה יחד את הכוח המדהים של המתמטיקה שמאחורי זה! הכירו את העצרת – פעולה קסומה שמגלה לנו בדיוק כמה אפשרויות סידור קיימות.

<div class="app-container">
    <h2>בואו נסדר! בחרו כמות חפצים:</h2>
    <div class="controls">
        <label for="numObjects">כמה חפצים נסדר הפעם (N)?</label>
        <input type="number" id="numObjects" min="1" max="7" value="3"> <!-- Reduced max slightly for smoother simulation visually -->
    </div>
    <div class="stage-area">
        <div class="objects-shelf" id="objectsShelf">
            <!-- Initial objects will be rendered here -->
        </div>
        <div class="simulation-area">
             <div class="slots-container" id="slotsContainer">
                <!-- Arrangement slots will appear here during simulation -->
             </div>
             <div class="calculation-display" id="calculationDisplay">
                 <!-- Calculation steps will appear here -->
             </div>
        </div>
    </div>
    <div class="result-area">
        <p id="resultText" class="result-text"></p>
    </div>
</div>

<button id="toggleExplanation" class="toggle-button">מה לעזאזל קורה פה? הסבר את הקסם!</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h3>עצרת (n!): הקוד הסודי למספר הסידורים האפשריים</h3>
    <p>המספר המדהים שראיתם בסוף הסימולציה הוא ה"עצרת" של N, שמסומנת בסימן קריאה: N!.</p>
    <p>עצרת N! היא פשוט המכפלה של כל המספרים השלמים החיוביים, החל מ-1 ועד N. כלומר:</p>
    <p class="math-formula">N! = N × (N-1) × (N-2) × ... × 3 × 2 × 1</p>
    
    <h4>אבל למה זה שווה בדיוק למספר הדרכים לסדר N חפצים?</h4>
    <p>תארו לעצמכם שאתם מסדרים N חפצים שונים בשורה, מקום אחר מקום:</p>
    <ul>
        <li>**למקום הראשון:** יש לכם N אפשרויות בחירה! אתם יכולים לשים שם כל אחד מ-N החפצים המקוריים.</li>
        <li>**למקום השני:** אחרי שבחרתם חפץ אחד והצבתם אותו במקום הראשון, נשארו לכם N-1 חפצים פנויים. לכן, למקום השני נותרו לכם N-1 אפשרויות בחירה.</li>
        <li>**המשיכו כך:** למקום השלישי יישארו N-2 אפשרויות, לרביעי N-3, וכן הלאה...</li>
        <li>**למקום האחרון (ה-N-י):** יישאר לכם רק חפץ אחד בודד לבחירה – אפשרות אחת בלבד!</li>
    </ul>
    <p>כדי למצוא את מספר כל הסידורים האפשריים, עלינו להכפיל את מספר האפשרויות בכל שלב. כי על כל בחירה במקום הראשון, יש את כל האפשרויות לבחירה במקום השני, וכן הלאה.</p>
    <p class="math-formula">סה"כ אפשרויות = (אפשרויות למקום 1) × (אפשרויות למקום 2) × ... × (אפשרויות למקום N)</p>
     <p class="math-formula">סה"כ אפשרויות = N × (N-1) × (N-2) × ... × 1</p>
    <p>וזה, חברים וחברות, זה בדיוק (אבל בדיוק!) ההגדרה של N!.</p>
    <p>אז בפעם הבאה שתצטרכו לדעת כמה סידורים שונים קיימים לקבוצת אובייקטים, חשבו עצרת! (תרתי משמע 😉).</p>
</div>


<style>
    @import url('https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;700&display=swap'); /* שימוש בפונט מודרני בעברית */

    body {
        font-family: 'Rubik', sans-serif;
        line-height: 1.6;
        padding: 20px;
        background: linear-gradient(135deg, #f0f4f8 0%, #d9e2ec 100%); /* רקע עם גרדיאנט עדין */
        color: #2d3748; /* צבע טקסט כהה ועשיר יותר */
        direction: rtl; /* כיוון קריאה מימין לשמאל */
        text-align: rtl;
    }

    h1, h2, h3 {
        color: #0056b3; /* כחול עמוק */
        text-align: center;
        margin-bottom: 20px;
    }

    h1 {
        font-size: 2.5rem;
        font-weight: 700;
        color: #004085;
    }

    h2 {
         font-size: 1.8rem;
         font-weight: 500;
         color: #0056b3;
         margin-bottom: 25px;
    }

    h3 {
        font-size: 1.5rem;
        font-weight: 500;
        margin-top: 0;
        color: #004085;
    }

    .app-container {
        background-color: #ffffff;
        padding: 35px;
        border-radius: 15px; /* פינות מעוגלות יותר */
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1); /* צל עשיר יותר */
        margin: 30px auto;
        max-width: 800px; /* הגבלת רוחב לנוחות קריאה/צפייה */
        text-align: center; /* ממורכז */
    }

    .controls {
        margin-bottom: 30px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
    }

    label {
        font-weight: 500;
        font-size: 1.1rem;
        color: #4a5568;
    }

    input[type="number"] {
        padding: 10px;
        border: 1px solid #cbd5e0; /* גבול עדין יותר */
        border-radius: 8px; /* פינות מעוגלות */
        font-size: 1.1rem;
        width: 70px;
        text-align: center;
        -moz-appearance: textfield; /* הסרת חיצים ב-Firefox */
    }

    input[type="number"]::-webkit-outer-spin-button,
    input[type="number"]::-webkit-inner-spin-button {
        -webkit-appearance: none; /* הסרת חיצים ב-Chrome/Safari */
        margin: 0;
    }


    .stage-area {
        min-height: 250px; /* נותן שטח למדף ולאזור הסימולציה */
        display: flex;
        flex-direction: column; /* סידור אנכי: מדף למעלה, סימולציה למטה */
        align-items: center;
        gap: 20px; /* רווח בין המדף לאזור הסימולציה */
    }

    .objects-shelf {
        display: flex;
        justify-content: center;
        gap: 12px; /* רווח בין האובייקטים */
        align-items: center;
        min-height: 70px; /* שומר על גובה גם כשהמדף ריק */
        padding-bottom: 15px; /* רווח קטן מתחת למדף */
        border-bottom: 1px dashed #cbd5e0; /* קו מפריד עדין */
    }

    .object {
        width: 55px; /* גודל קצת יותר גדול */
        height: 55px;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 1.4rem; /* גודל פונט בתוך האובייקט */
        font-weight: 700;
        color: white;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* צל עשיר יותר */
        transition: transform 0.5s ease-in-out, opacity 0.5s ease-in-out; /* הוספת אנימציה לעמעום ותנועה */
        cursor: pointer; /* רמז אינטראקטיבי למרות שכרגע רק ויזואלי */
        user-select: none; /* מונע סימון הטקסט בתוך העיגול */
    }

    /* צבעים עשירים ונעימים יותר */
    .object:nth-child(1) { background-color: #e76f51; } /* Terracotta */
    .object:nth-child(2) { background-color: #2a9d8f; } /* Teal */
    .object:nth-child(3) { background-color: #e9c46a; } /* Ochre */
    .object:nth-child(4) { background-color: #f4a261; } /* Sandy Brown */
    .object:nth-child(5) { background-color: #a8dadc; } /* Powder Blue */
    .object:nth-child(6) { background-color: #457b9d; } /* Cadet Blue */
    .object:nth-child(7) { background-color: #1d3557; } /* Prussian Blue */


     .simulation-area {
         flex-grow: 1; /* תופס את השטח הנותר */
         display: flex;
         flex-direction: column;
         align-items: center;
         justify-content: flex-start; /* מיישר למעלה */
         width: 100%;
     }

    .slots-container {
        display: flex;
        justify-content: center;
        gap: 10px; /* רווח בין הסלוטים */
        min-height: 80px; /* שומר על שטח לסלוטים */
        align-items: center;
        margin-bottom: 20px;
    }

    .slot {
        width: 60px; /* גודל הסלוט */
        height: 60px;
        border: 2px dashed #a0aec0; /* גבול מקווקו לסלוט ריק */
        border-radius: 8px; /* פינות מעוגלות */
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 1rem;
        color: #718096; /* צבע רמז */
        transition: border-color 0.3s ease, background-color 0.3s ease;
        box-sizing: border-box; /* כולל את הגבול במידות */
        position: relative; /* עבור אובייקטים בתוך הסלוט */
    }

    .slot.active {
        border-color: #3182ce; /* גבול צבעוני לסלוט הפעיל */
        background-color: #ebf8ff; /* רקע בהיר לסלוט הפעיל */
    }

     .slot-object {
        width: 50px; /* גודל האובייקט בתוך הסלוט */
        height: 50px;
        border-radius: 50%;
        position: absolute; /* ממוקם בתוך הסלוט */
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%) scale(0); /* מתחיל קטן במרכז הסלוט */
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 1.2rem;
        font-weight: 700;
        color: white;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
        transition: transform 0.5s ease-out, opacity 0.5s ease-out; /* אנימציית כניסה */
     }

    .calculation-display {
        min-height: 40px;
        font-size: 1.2rem;
        font-weight: 500;
        color: #2b6cb0; /* כחול */
        margin-top: 10px;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap; /* מאפשר גלישה בשורות */
        gap: 8px; /* רווח בין רכיבי החישוב */
    }

    .calculation-display .step,
    .calculation-display .operator,
    .calculation-display .current-result {
        transition: transform 0.3s ease, opacity 0.3s ease;
    }

     .calculation-display .current-result {
         font-weight: 700;
         color: #d69e2e; /* צבע הדגשה לתוצאה נוכחית */
     }


    .result-area {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px dashed #cbd5e0;
    }

    .result-text {
        font-size: 1.6rem; /* גודל פונט גדול יותר לתוצאה הסופית */
        font-weight: 700;
        color: #007bff; /* כחול הדגשה */
        min-height: 30px; /* שומר על שטח */
    }

    .toggle-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px; /* ריפוד גדול יותר */
        font-size: 1.1rem; /* גודל פונט גדול יותר */
        color: #fff;
        background-color: #007bff;
        border: none;
        border-radius: 8px; /* פינות מעוגלות יותר */
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease; /* הוספת אנימציית לחיצה קלה */
        font-family: 'Rubik', sans-serif;
        font-weight: 500;
    }

    .toggle-button:hover {
        background-color: #0056b3;
    }

    .toggle-button:active {
        transform: scale(0.98); /* אנימציית לחיצה */
    }


    .explanation-section {
        background-color: #ebf8ff; /* רקע בהיר יותר */
        padding: 25px;
        border-radius: 8px;
        border-right: 5px solid #3182ce; /* גבול ימני מודגש בצבע כחול */
        margin-top: 20px;
        color: #2d3748;
        line-height: 1.8; /* מרווח שורות גדול יותר */
    }

    .explanation-section h3 {
        color: #004085;
        margin-bottom: 15px;
    }

     .explanation-section p {
         margin-bottom: 15px;
     }

    .explanation-section ul {
        margin-bottom: 15px;
        padding-right: 20px; /* ריפוד לרשימה */
    }

    .explanation-section li {
        margin-bottom: 10px;
        line-height: 1.6;
    }

     .math-formula {
         font-family: 'Courier New', monospace; /* פונט מונספייס לנוסחאות */
         font-size: 1.1rem;
         font-weight: 700;
         text-align: center;
         margin: 15px 0;
         color: #004085;
     }

</style>

<script>
    const numObjectsInput = document.getElementById('numObjects');
    const objectsShelf = document.getElementById('objectsShelf');
    const slotsContainer = document.getElementById('slotsContainer');
    const calculationDisplay = document.getElementById('calculationDisplay');
    const resultText = document.getElementById('resultText');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationSection = document.getElementById('explanation');

    // Function to calculate factorial - unchanged logic
    function factorial(n) {
        if (n < 0) return "לא מוגדר"; // Should not happen with min=1
        if (n === 0 || n === 1) return 1;
        let res = 1;
        for (let i = 2; i <= n; i++) {
            res *= i;
        }
        return res;
    }

    // Function to render initial objects on the shelf with entry animation
    function renderInitialObjects(n) {
        objectsShelf.innerHTML = ''; // Clear previous objects
        objectsShelf.style.opacity = '0'; // Prepare for fade in

        // Use a small delay and animate entry
        setTimeout(() => {
             for (let i = 0; i < n; i++) {
                const objectDiv = document.createElement('div');
                objectDiv.classList.add('object');
                objectDiv.textContent = i + 1;
                 // Apply initial state for animation
                objectDiv.style.opacity = '0';
                objectDiv.style.transform = 'scale(0.5) translateY(20px)';
                objectsShelf.appendChild(objectDiv);

                // Animate the object into view with a slight stagger
                setTimeout(() => {
                    objectDiv.style.opacity = '1';
                    objectDiv.style.transform = 'scale(1) translateY(0)';
                }, i * 70 + 100); // Staggered animation
            }
            objectsShelf.style.opacity = '1'; // Final opacity after all added
        }, 100); // Short delay before starting
    }

    // Function to simulate the arrangement process
    async function simulateArrangement(n) {
        slotsContainer.innerHTML = ''; // Clear previous slots
        calculationDisplay.innerHTML = ''; // Clear calculation display
        resultText.textContent = 'מחשב...';

        if (n === 0) { // Special case, 0! = 1 arrangement (empty set)
             resultText.textContent = `ישנה 1 אפשרות שונה לסדר 0 חפצים!`;
             return;
        }

        // Create slots
        for (let i = 0; i < n; i++) {
            const slotDiv = document.createElement('div');
            slotDiv.classList.add('slot');
             // Add a placeholder number for context, maybe
            // slotDiv.textContent = i + 1;
            slotsContainer.appendChild(slotDiv);
        }

        await new Promise(resolve => setTimeout(resolve, 500)); // Short pause

        let currentProduct = 1;
        let calculationSteps = [];

        // Simulate placing objects one by one
        for (let i = 0; i < n; i++) {
            const currentSlot = slotsContainer.children[i];
            currentSlot.classList.add('active'); // Highlight active slot

            const choices = n - i; // Number of choices for this slot

            // Update calculation display step by step
            calculationSteps.push(choices);
            calculationDisplay.innerHTML = calculationSteps.map((step, index) => {
                let part = `<span class="step">${step}</span>`;
                if (index < calculationSteps.length - 1) {
                    part += `<span class="operator"> × </span>`;
                }
                 return part;
            }).join('');

             // Animate chosen object (representatively) moving to the slot
             // Find an object element to "clone" its color/appearance
             const sourceObject = objectsShelf.children[i % objectsShelf.children.length]; // Use existing objects' styles
             const slotObject = document.createElement('div');
             slotObject.classList.add('slot-object');
             slotObject.textContent = '-'; // Placeholder during animation
             slotObject.style.backgroundColor = sourceObject ? sourceObject.style.backgroundColor : '#cccccc'; // Copy color
             currentSlot.appendChild(slotObject);

             // Trigger slot object entry animation
             setTimeout(() => {
                 slotObject.style.transform = 'translate(-50%, -50%) scale(1)';
                 slotObject.textContent = objectsShelf.children[i] ? objectsShelf.children[i].textContent : (i+1); // Set actual number after scale
             }, 50); // Small delay to ensure element is in DOM

            await new Promise(resolve => setTimeout(resolve, 700)); // Pause between steps

            currentSlot.classList.remove('active'); // De-highlight

            // Update the current running result visually after each step's delay
             if (i < n - 1) {
                 currentProduct *= choices;
                  const currentResultSpan = document.createElement('span');
                  currentResultSpan.classList.add('current-result');
                  currentResultSpan.textContent = ` = ${currentProduct}`;
                  calculationDisplay.appendChild(currentResultSpan);
                  // Remove the temporary result after a moment for the next step
                   await new Promise(resolve => setTimeout(resolve, 500)); // Pause for result viewing
                    if (calculationDisplay.lastChild === currentResultSpan) {
                       calculationDisplay.removeChild(currentResultSpan);
                    }
             } else {
                  currentProduct *= choices; // Last step
             }
        }

         await new Promise(resolve => setTimeout(resolve, 500)); // Final pause

         // Show the final result
         const finalResultSpan = document.createElement('span');
         finalResultSpan.classList.add('current-result');
         finalResultSpan.textContent = ` = ${currentProduct}`;
         calculationDisplay.appendChild(finalResultSpan);


        // Show the final result text below
         resultText.textContent = `וואו! ישנן בסך הכל ${currentProduct} אפשרויות שונות לסדר ${n} חפצים!`;
    }


    // Master function to handle the entire update process
    async function handleInputChange() {
        const n = parseInt(numObjectsInput.value, 10);
        const maxN = parseInt(numObjectsInput.max, 10);

        if (isNaN(n) || n < 1 || n > maxN) {
             // Correct invalid input
             if (isNaN(n) || n < 1) numObjectsInput.value = 1;
             if (n > maxN) numObjectsInput.value = maxN;
             handleInputChange(); // Re-run with corrected value
             return;
        }

        // Clear result and prepare stage
        resultText.textContent = '';
        slotsContainer.innerHTML = '';
        calculationDisplay.innerHTML = '';

        // Render initial objects on the shelf
        renderInitialObjects(n);

        // Add a small delay before starting simulation to let objects appear
        await new Promise(resolve => setTimeout(resolve, n * 70 + 300)); // Based on render delay

        // Start the simulation process
        simulateArrangement(n);
    }


    // Event listener for input changes
    numObjectsInput.addEventListener('input', handleInputChange);

    // Initial render on page load
    handleInputChange();

    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationSection.style.display === 'none';
        explanationSection.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'הצג הסבר';
    });

    // Ensure explanation is hidden on load
    explanationSection.style.display = 'none';
    toggleExplanationButton.textContent = 'מה לעזאזל קורה פה? הסבר את הקסם!';


</script>
---