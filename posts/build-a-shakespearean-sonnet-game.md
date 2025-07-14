---
title: "משחק הרכבת סונטה שייקספירית"
english_slug: build-a-shakespearean-sonnet-game
category: "מדעי הרוח / ספרות וכתיבה"
tags: סונטה, שייקספיר, שירה, מבנה ספרותי, חרוז
---
# משחק הרכבת סונטה שייקספירית

הצטרפו למסע אל מאחורי הקלעים של גאונות פואטית! כיצד מצליח שייקספיר לרתק אותנו עם שירים מדויקים בני 14 שורות בלבד? גלו את הסוד שמאחורי המבנה המופלא של הסונטה השייקספירית, הרכיבו אותה בעצמכם, ופצחו את הקסם שיוצר את האפקט הדרמטי האופייני. בואו נשחק עם מילים, מבנה וחרוזים!

<div class="sonnet-game-container">
    <div class="source-lines-container">
        <h2>מחסן השורות (גררו מכאן)</h2>
        <div id="source-lines" class="source-lines">
            <!-- Draggable lines will be populated here by JS -->
            <div class="placeholder-text">שורות יופיעו כאן...</div>
        </div>
    </div>
    <div class="sonnet-structure-container">
        <h2>מבנה הסונטה (שבצו כאן)</h2>
        <div class="sonnet-structure">
            <div class="line-slot" data-line-num="1" data-rhyme="A">1 (A)</div>
            <div class="line-slot" data-line-num="2" data-rhyme="B">2 (B)</div>
            <div class="line-slot" data-line-num="3" data-rhyme="A">3 (A)</div>
            <div class="line-slot quatrain-end" data-line-num="4" data-rhyme="B">4 (B)</div>

            <div class="line-slot" data-line-num="5" data-rhyme="C">5 (C)</div>
            <div class="line-slot" data-line-num="6" data-rhyme="D">6 (D)</div>
            <div class="line-slot" data-line-num="7" data-rhyme="C">7 (C)</div>
            <div class="line-slot quatrain-end" data-line-num="8" data-rhyme="D">8 (D)</div>

            <div class="line-slot" data-line-num="9" data-rhyme="E">9 (E)</div>
            <div class="line-slot" data-line-num="10" data-rhyme="F">10 (F)</div>
            <div class="line-slot" data-line-num="11" data-rhyme="E">11 (E)</div>
            <div class="line-slot quatrain-end" data-line-num="12" data-rhyme="F">12 (F)</div>

            <div class="line-slot couplet-start" data-line-num="13" data-rhyme="G">13 (G)</div>
            <div class="line-slot couplet-end" data-line-num="14" data-rhyme="G">14 (G)</div>
        </div>
    </div>
     <div id="completion-message" class="completion-message hidden">
        <div class="message-content">
            <h2>כל הכבוד!</h2>
            <p>הרכבתם בהצלחה את הסונטה השייקספירית!</p>
            <button class="reset-button">למשחק חדש</button>
        </div>
    </div>
</div>

<button class="explanation-button" id="toggle-explanation">הצצה לסוד: מהי סונטה שייקספירית?</button>

<div id="explanation">
    <h2>פענוח המבנה: סוד הסונטה השייקספירית</h2>

    <h3>מה הופך שיר לסונטה?</h3>
    הכירו את הסונטה – צורה פואטית קלאסית בת 14 שורות, שנולדה באיטליה וכבשה את עולם השירה. היא משמשת מסגרת קומפקטית ועוצמתית לחקירת רעיונות ורגשות מורכבים, תמיד עם משקל קבוע ומבנה חרוזים ייחודי.

    <h3>פטרארקה מול שייקספיר: קרב הסונטות הגדול</h3>
    בעולם הסונטות שולטים שני סוגים עיקריים, כל אחד עם אופי שונה לגמרי:
    <ul>
        <li>**הסונטה האיטלקית (פטרארקית):** מחולקת ל"אוקטבה" (8 שורות ראשונות, ABBAABBA) המציגה אתגר או שאלה, ו"ססטט" (6 שורות אחרונות, לרוב CDECDE/CDCDCD) המציע פתרון או שינוי פרספקטיבה ("וולטה" דרמטית).</li>
        <li>**הסונטה האנגלית (שייקספירית):** פיתוח גאוני שהתבסס באנגליה, בעיקר בזכות שייקספיר, ויש לו מבנה פנימי שונה לחלוטין.</li>
    </ul>

    <h3>המבנה המנצח של שייקספיר</h3>
    הסונטה השייקספירית בנויה כארכיטקטורה מילולית מדויקת:
    <ul>
        <li>**14 שורות:** כמובן.</li>
        <li>**חלוקה לבתים:** כאן הסוד – שלושה בתים בני ארבע שורות ("Quatrains") וסיום קצר וקולע של שתי שורות ("Couplet").</li>
        <li>**סכימת החרוזים:** ABAB CDCD EFEF GG. שימו לב למבנה הזוגות החורזים בבתים הראשונים (A עם A, B עם B) ולקופלט החורז החותם (G עם G) – זה המפתח למשחק ששיחקתם!</li>
    </ul>

    <h3>איך המבנה הזה יוצר קסם?</h3>
    המבנה השייקספירי אינו רק כלל משחק, אלא כלי ביטוי עוצמתי:
    <ul>
        <li>**הבתים הראשונים:** מציגים את הנושא, בונים את הטיעון או פורשים תמונות שונות. כל בית יכול להרחיב, לפתח או אפילו ליצור ניגודים, והחריזה המסורגת (ABAB) יוצרת קשר עדין וזורם.</li>
        <li>**בית הסיום (הקופלט):** זה ה"פאנצ'ליין" הדרמטי! שתי השורות האחרונות מסכמות, מפתיעות, או נותנות את המסקנה הסופית. החריזה הצמודה (GG) מדגישה את הסגירה והחשיבות של חלק זה, ויוצרת אפקט סיום חד ובלתי נשכח.</li>
    </ul>

    <h3>שייקספיר בפעולה</h3>
    שייקספיר השתמש במבנה זה במאות סונטות מופתיות, כמו "האם אשווה אותך ליום קיץ?" (סונטה 18) או "עיני אהובתי אינן דומות לשמש" (סונטה 130). כל סונטה שלו היא דוגמה חיה לכך שמסגרת קבועה יכולה להוביל ליצירתיות פורצת דרך וביטוי אנושי עמוק. עכשיו כשאתם מכירים את הסוד, חפשו את המבנה הזה ביצירותיו וגלו שכבות חדשות של משמעות!

</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const sonnetLinesData = [
            { id: 'line1', text: "אוֹר יוֹם דּוֹעֵךְ, הַשֶּׁמֶשׁ בָּא", rhymeGroup: "A", correctLineNum: 1 },
            { id: 'line2', text: "וְרַעַד קַל עוֹבֵר בְּגַן", rhymeGroup: "B", correctLineNum: 2 },
            { id: 'line3', text: "עַל מַעֲרָב, תּוֹלִיךְ נֶחְבָּא", rhymeGroup: "A", correctLineNum: 3 },
            { id: 'line4', text: "בְּלַחַשׁ רוּחַ אֶל כָּאן", rhymeGroup: "B", correctLineNum: 4 },
            { id: 'line5', text: "פְּרָחִים נוֹעִים בְּלַחַשׁ קָר", rhymeGroup: "C", correctLineNum: 5 },
            { id: 'line6', text: "עוֹלֶה נִיחוֹחַ מֵהָעֵץ", rhymeGroup: "D", correctLineNum: 6 },
            { id: 'line7', text: "כְּמוֹ שְׁתִיקָה שֶׁבָּהּ אוֹמֵר", rhymeGroup: "C", correctLineNum: 7 },
            { id: 'line8', text: "סוֹד יָשָׁן, אַךְ לֹא יוֹצֵא", rhymeGroup: "D", correctLineNum: 8 },
            { id: 'line9', text: "צְלִילִים רְחוֹקִים נִגָּרִים לָאֵל", rhymeGroup: "E", correctLineNum: 9 },
            { id: 'line10', text: "הָרֶגַע כֹּה עוֹטֵף שְׁקִיטָה", rhymeGroup: "F", correctLineNum: 10 },
            { id: 'line11', text: "הַלַּיְלָה אֶת יוֹמוֹ גּוֹאֵל", rhymeGroup: "E", correctLineNum: 11 },
            { id: 'line12', text: "בְּמִסְתּוֹרִין, עִם חֲשֵׁכָה", rhymeGroup: "F", correctLineNum: 12 },
            { id: 'line13', text: "וְהַנְּשָׁמָה נִרְגַּעַת לָהּ בִּבְדִידוּת", rhymeGroup: "G", correctLineNum: 13 },
            { id: 'line14', text: "בְּתוֹךְ הַשֶּׁקֶט שֶׁל עוֹלָם וְחִדּוּד", rhymeGroup: "G", correctLineNum: 14 }
        ];

        const sourceLinesDiv = document.getElementById('source-lines');
        const lineSlots = document.querySelectorAll('.line-slot');
        const explanationDiv = document.getElementById('explanation');
        const toggleButton = document.getElementById('toggle-explanation');
        const completionMessage = document.getElementById('completion-message');
        const resetButton = completionMessage.querySelector('.reset-button');

        let isDraggingFromSlot = false; // Flag to track if dragging from a slot

        // Shuffle array (Fisher-Yates algorithm)
        function shuffleArray(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]]; // Swap elements
            }
            return array;
        }

        // Create and initialize a draggable line element
        function createDraggableLine(lineData) {
            const lineElement = document.createElement('div');
            lineElement.classList.add('draggable-line');
            lineElement.setAttribute('draggable', true);
            lineElement.setAttribute('id', lineData.id);
            lineElement.dataset.rhyme = lineData.rhymeGroup;
            lineElement.dataset.correctLine = lineData.correctLineNum; // Store correct position
            lineElement.textContent = lineData.text;

            addDragListeners(lineElement); // Add listeners immediately

            return lineElement;
        }

         // Add drag listeners to a line element
        function addDragListeners(lineElement) {
             lineElement.addEventListener('dragstart', (event) => {
                 event.dataTransfer.setData('text/rhyme', event.target.dataset.rhyme);
                 event.dataTransfer.setData('text/lineId', event.target.id);
                 event.dataTransfer.setData('text/correctLine', event.target.dataset.correctLine); // Pass correct line num
                 event.target.classList.add('dragging');

                 // Check if the parent is a line-slot to set the flag
                 if (event.target.parentElement && event.target.parentElement.classList.contains('line-slot')) {
                      isDraggingFromSlot = true;
                      event.dataTransfer.setData('text/sourceSlotId', event.target.parentElement.id); // Store source slot ID
                 } else {
                      isDraggingFromSlot = false;
                      event.dataTransfer.setData('text/sourceSlotId', ''); // Clear source slot ID
                 }
             });

             lineElement.addEventListener('dragend', (event) => {
                 event.target.classList.remove('dragging');
                 // The flag is primarily used in drop logic, not just dragend
             });
        }


        // Initialize the game
        function initializeGame() {
            // Clear source and slots
            sourceLinesDiv.innerHTML = ''; // Clear existing lines and placeholder
            const placeholder = document.createElement('div');
            placeholder.classList.add('placeholder-text');
            placeholder.textContent = 'גררו את השורות לכאן...';
            sourceLinesDiv.appendChild(placeholder);


            lineSlots.forEach(slot => {
                // Reset slot text to placeholder + number/rhyme
                slot.innerHTML = `<span class="slot-placeholder">${slot.dataset.lineNum} (${slot.dataset.rhyme})</span>`;
                slot.classList.remove('correct', 'incorrect', 'filled'); // Remove feedback/filled classes
                slot.style.backgroundColor = ''; // Reset background
                slot.style.borderColor = ''; // Reset border

                // Remove any previously dropped lines
                const droppedLine = slot.querySelector('.draggable-line');
                if (droppedLine) {
                    droppedLine.remove();
                }
            });

            completionMessage.classList.add('hidden'); // Hide completion message

            const shuffledLines = shuffleArray([...sonnetLinesData]);

            shuffledLines.forEach(lineData => {
                const lineElement = createDraggableLine(lineData); // Create and add listeners
                sourceLinesDiv.appendChild(lineElement);
            });

             // Add drop listener to the source container for putting lines back
             addSourceDropListener();
             addLineSlotListeners(); // Add drop listeners to slots
        }

        // Add drop listener to the source container
        function addSourceDropListener() {
             sourceLinesDiv.addEventListener('dragover', (event) => {
                  event.preventDefault(); // Allow drop
                  // Only allow drop if dragging from a slot
                  const sourceSlotId = event.dataTransfer.getData('text/sourceSlotId');
                  if (sourceSlotId) {
                       event.dataTransfer.dropEffect = 'move';
                       sourceLinesDiv.classList.add('drag-over'); // Add visual feedback
                  } else {
                       event.dataTransfer.dropEffect = 'none'; // Cannot drop here if not from a slot
                  }
             });

             sourceLinesDiv.addEventListener('dragleave', () => {
                  sourceLinesDiv.classList.remove('drag-over');
             });

             sourceLinesDiv.addEventListener('drop', (event) => {
                  event.preventDefault();
                  sourceLinesDiv.classList.remove('drag-over');

                  const sourceSlotId = event.dataTransfer.getData('text/sourceSlotId');
                  const lineId = event.dataTransfer.getData('text/lineId');
                  const draggedElement = document.getElementById(lineId);

                  if (sourceSlotId && draggedElement && draggedElement.parentElement && draggedElement.parentElement.id === sourceSlotId) {
                       const sourceSlot = document.getElementById(sourceSlotId);
                       sourceSlot.innerHTML = `<span class="slot-placeholder">${sourceSlot.dataset.lineNum} (${sourceSlot.dataset.rhyme})</span>`; // Reset slot text
                       sourceSlot.classList.remove('correct', 'incorrect', 'filled'); // Reset slot classes
                       sourceSlot.style.backgroundColor = '';
                       sourceSlot.style.borderColor = '';

                       // Append line back to source
                       sourceLinesDiv.insertBefore(draggedElement, sourceLinesDiv.querySelector('.placeholder-text') || null); // Insert before placeholder if it exists
                       draggedElement.removeAttribute('style'); // Reset any inline styles added when in slot
                       draggedElement.classList.remove('placed-in-slot'); // Remove class used for styling in slot

                       // Re-enable dragging (already done by createDraggableLine)
                       draggedElement.setAttribute('draggable', true);
                       draggedElement.style.cursor = 'grab'; // Restore grab cursor

                       // Re-check completion state (might become incomplete now)
                       checkCompletion();
                  }
                  isDraggingFromSlot = false; // Reset flag after drop attempt
             });
        }


        // Add drag and drop listeners to line slots
        function addLineSlotListeners() {
            lineSlots.forEach(slot => {
                // Ensure listeners are added only once if initializeGame is called multiple times
                // Check if listeners already exist (a bit complex), simpler to just add them
                // or ensure initializeGame only adds them once or removes old ones.
                // Given the current structure, re-adding is likely safe if it overwrites.

                slot.addEventListener('dragover', (event) => {
                    event.preventDefault();
                    // Allow drop only if the slot is empty OR if we are dragging a line *from* the source container
                     const isSlotEmpty = !slot.classList.contains('filled');
                     const isDraggingFromSource = !isDraggingFromSlot; // Check the flag set in dragstart

                    if (isSlotEmpty && isDraggingFromSource) {
                         event.dataTransfer.dropEffect = 'move';
                         slot.classList.add('drag-over');
                    } else if (isSlotEmpty && isDraggingFromSlot) {
                         // Allow dropping a line from another slot ONLY if this slot is empty
                         event.dataTransfer.dropEffect = 'move';
                         slot.classList.add('drag-over');
                    }
                    else {
                         event.dataTransfer.dropEffect = 'none'; // Cannot drop here
                    }
                });

                slot.addEventListener('dragleave', () => {
                    slot.classList.remove('drag-over');
                });

                slot.addEventListener('drop', (event) => {
                    event.preventDefault();
                    slot.classList.remove('drag-over');

                    const droppedRhyme = event.dataTransfer.getData('text/rhyme');
                    const lineId = event.dataTransfer.getData('text/lineId');
                    const droppedCorrectLineNum = parseInt(event.dataTransfer.getData('text/correctLine'));
                    const draggedElement = document.getElementById(lineId);
                    const sourceSlotId = event.dataTransfer.getData('text/sourceSlotId'); // Get source slot ID

                    // Check if the slot is already filled
                    if (slot.classList.contains('filled')) {
                         // If the slot is already filled, and we are dragging *from a slot*
                         // Swap the lines
                         if (isDraggingFromSlot && sourceSlotId && sourceSlotId !== slot.id) {
                              const sourceSlot = document.getElementById(sourceSlotId);
                              const lineInTargetSlot = slot.querySelector('.draggable-line');

                              if(lineInTargetSlot && sourceSlot){
                                   // Temporarily remove listeners to avoid re-triggering drag/drop during swap
                                   removeDragListeners(draggedElement);
                                   removeDragListeners(lineInTargetSlot);

                                   // Swap elements
                                   slot.appendChild(draggedElement);
                                   sourceSlot.appendChild(lineInTargetSlot);

                                   // Update element classes and attributes
                                   draggedElement.classList.add('placed-in-slot');
                                   draggedElement.setAttribute('draggable', true); // Keep draggable for moving out
                                   draggedElement.style.cursor = 'grab'; // Restore grab cursor

                                   lineInTargetSlot.classList.add('placed-in-slot');
                                   lineInTargetSlot.setAttribute('draggable', true);
                                   lineInTargetSlot.style.cursor = 'grab';

                                   // Add listeners back *after* elements are in new parent
                                   addDragListeners(draggedElement);
                                   addDragListeners(lineInTargetSlot);


                                   // Re-check feedback for both slots involved in swap
                                   checkSlotCorrectness(slot);
                                   checkSlotCorrectness(sourceSlot);

                                   checkCompletion(); // Check overall completion after swap
                                   return; // Exit drop function after swap
                              }
                         } else {
                             // Slot is filled, not a valid swap scenario or dragging from source - do nothing
                             return;
                         }
                    }


                    // If here, the target slot is empty OR we successfully handled a swap

                    // If dropping from source container, remove placeholder
                    if (!isDraggingFromSlot) {
                         const placeholder = sourceLinesDiv.querySelector('.placeholder-text');
                         if (placeholder) placeholder.remove(); // Remove source placeholder if needed
                    } else {
                         // If dropping from a source slot (and it wasn't a swap scenario handled above)
                         // Clear the source slot first
                         const sourceSlot = document.getElementById(sourceSlotId);
                         if (sourceSlot) {
                             sourceSlot.innerHTML = `<span class="slot-placeholder">${sourceSlot.dataset.lineNum} (${sourceSlot.dataset.rhyme})</span>`; // Reset slot text
                             sourceSlot.classList.remove('correct', 'incorrect', 'filled'); // Reset classes
                             sourceSlot.style.backgroundColor = '';
                             sourceSlot.style.borderColor = '';
                         }
                    }


                    // Clear previous placeholder text/number from the target slot
                    slot.innerHTML = '';

                    // Append the dragged line to the target slot
                    slot.appendChild(draggedElement);
                    slot.classList.add('filled'); // Mark slot as filled

                    // Add visual indicator that it's now in a slot
                    draggedElement.classList.add('placed-in-slot');
                    draggedElement.setAttribute('draggable', true); // Keep draggable so user can move it back
                    draggedElement.style.cursor = 'grab'; // Keep grab cursor to indicate it can be moved


                    // Check correctness based on line number and rhyme group
                    checkSlotCorrectness(slot, droppedCorrectLineNum, droppedRhyme);

                    isDraggingFromSlot = false; // Reset flag after drop

                    checkCompletion(); // Check overall completion state
                });
            });
        }

        // Function to remove drag listeners (useful before swapping elements)
        function removeDragListeners(lineElement) {
             // Removing specific listeners added with addEventListener is tricky.
             // A simpler approach for this context might be to just remove and re-add the element,
             // or manage the draggable attribute and check flags in listeners.
             // Given the structural constraint, let's rely on the flag `isDraggingFromSlot`
             // and the presence of `data-source-slot-id` attribute (which we add/remove).
             // Or, attach listeners inside `createDraggableLine` which is called on init and when putting back.
             // Let's stick to the simpler approach of checking the flag and sourceSlotId in drop targets.
             // The `setAttribute('draggable', true/false)` and `classList.add/remove('dragging')`
             // combined with `isDraggingFromSlot` flag seem sufficient for the planned interactions (source->slot, slot->source, slot->slot swap).
             // We don't need a separate remove function with this approach.
        }


        // Check correctness for a single slot and update its appearance
        function checkSlotCorrectness(slot, droppedLineNum = null, droppedRhyme = null) {
             const lineElement = slot.querySelector('.draggable-line');
             slot.classList.remove('correct', 'incorrect'); // Clear previous feedback

             if (!lineElement) {
                 // Slot is empty, reset appearance
                 slot.style.backgroundColor = '';
                 slot.style.borderColor = '';
                 slot.classList.remove('filled');
                 // Ensure placeholder is there if slot is empty
                 if (!slot.querySelector('.slot-placeholder')) {
                     slot.innerHTML = `<span class="slot-placeholder">${slot.dataset.lineNum} (${slot.dataset.rhyme})</span>`;
                 }
                 return false; // Slot is not filled
             }

            const correctRhyme = slot.dataset.rhyme;
            // Retrieve correct line number from the line element's data attribute
            const correctLineNum = parseInt(lineElement.dataset.correctLine);
            const currentSlotLineNum = parseInt(slot.dataset.lineNum);

            // Check if the dropped line's correct position matches the current slot's number
            if (correctLineNum === currentSlotLineNum) {
                slot.classList.add('correct');
                slot.style.backgroundColor = '#e0f7e8'; /* Light green */
                slot.style.borderColor = '#4CAF50'; /* Green */
                 return true; // Slot is correct
            } else {
                slot.classList.add('incorrect');
                slot.style.backgroundColor = '#ffebee'; /* Light red */
                slot.style.borderColor = '#F44336'; /* Red */
                 return false; // Slot is incorrect
            }
        }


        // Check if the sonnet is complete and correct
        function checkCompletion() {
            let allCorrect = true;
            let allFilled = true;

            lineSlots.forEach(slot => {
                const lineElement = slot.querySelector('.draggable-line');
                if (!lineElement) {
                    allFilled = false;
                     // Ensure slot is not marked correct/incorrect if empty
                     slot.classList.remove('correct', 'incorrect', 'filled');
                      slot.style.backgroundColor = '';
                      slot.style.borderColor = '';
                     // Ensure placeholder is there
                     if (!slot.querySelector('.slot-placeholder')) {
                         slot.innerHTML = `<span class="slot-placeholder">${slot.dataset.lineNum} (${slot.dataset.rhyme})</span>`;
                     }

                } else {
                    slot.classList.add('filled');
                    // Re-check correctness for filled slots
                    if (!checkSlotCorrectness(slot)) {
                        allCorrect = false;
                    }
                }
            });

            if (allFilled && allCorrect) {
                 // Sonnet is complete and correct!
                 completionMessage.classList.remove('hidden');
                 // Add a celebration animation class to slots
                 lineSlots.forEach(slot => slot.classList.add('celebrate'));

            } else {
                 completionMessage.classList.add('hidden');
                 lineSlots.forEach(slot => slot.classList.remove('celebrate')); // Remove celebration if not complete/correct
            }
        }

        // Toggle explanation visibility
        toggleButton.addEventListener('click', () => {
            const expanded = explanationDiv.classList.toggle('expanded');
             toggleButton.textContent = expanded ? 'סגור הסבר' : 'הצצה לסוד: מהי סונטה שייקספירית?';
             // Add/remove aria-expanded attribute for accessibility
             toggleButton.setAttribute('aria-expanded', expanded);
        });

        // Reset button listener
        resetButton.addEventListener('click', initializeGame);


        // Start the game when the page loads
        initializeGame();
    });
</script>

<style>
    :root {
        --color-primary: #6a1b9a; /* Deep Purple */
        --color-secondary: #fbc02d; /* Amber */
        --color-accent: #ff8f00; /* Dark Orange */
        --color-success: #4CAF50; /* Green */
        --color-success-light: #e0f7e8; /* Light Green */
        --color-error: #F44336; /* Red */
        --color-error-light: #ffebee; /* Light Red */
        --color-bg-light: #f3e5f5; /* Lighter Purple */
        --color-bg-medium: #e1bee7; /* Medium Purple */
        --color-text-dark: #212121; /* Dark Grey */
        --color-text-medium: #424242; /* Medium Grey */
        --color-border: #ab47bc; /* Purple */
        --color-border-light: #e0e0e0; /* Light Grey */

        --spacing-small: 8px;
        --spacing-medium: 16px;
        --spacing-large: 24px;
    }

    body {
        font-family: 'Arial', sans-serif; /* Use a common system font */
        color: var(--color-text-dark);
        line-height: 1.6;
    }

    h1, h2, h3 {
        color: var(--color-primary);
    }

     h1 {
         text-align: center;
         margin-bottom: var(--spacing-large);
     }

    .sonnet-game-container {
        display: flex;
        flex-wrap: wrap;
        gap: var(--spacing-medium);
        justify-content: center;
        direction: rtl; /* Hebrew text direction */
        text-align: right;
        margin: var(--spacing-large) 0;
        position: relative; /* Needed for completion message overlay */
    }

    .source-lines-container, .sonnet-structure-container {
        flex: 1;
        min-width: 300px;
        border: 1px solid var(--color-border);
        padding: var(--spacing-medium);
        border-radius: 12px;
        background-color: var(--color-bg-light);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: box-shadow 0.3s ease;
    }

     .source-lines-container:hover, .sonnet-structure-container:hover {
         box-shadow: 0 6px 12px rgba(0,0,0,0.15);
     }

    .source-lines h2, .sonnet-structure-container h2 {
        margin-top: 0;
        border-bottom: 2px solid var(--color-border-light);
        padding-bottom: var(--spacing-small);
        margin-bottom: var(--spacing-medium);
        font-size: 1.4em;
        color: var(--color-text-medium);
    }

    .source-lines {
        min-height: 300px;
        background-color: #ffffff;
        border: 2px dashed var(--color-border-light);
        padding: var(--spacing-small);
        border-radius: 8px;
        transition: background-color 0.3s ease, border-color 0.3s ease;
    }

    .source-lines.drag-over {
        background-color: var(--color-bg-medium);
        border-color: var(--color-accent);
    }

     .source-lines .placeholder-text {
         text-align: center;
         color: var(--color-text-medium);
         padding-top: var(--spacing-large);
         font-style: italic;
     }


    .sonnet-structure {
        display: grid;
        grid-template-columns: 1fr;
        gap: var(--spacing-small);
    }

    .line-slot {
        border: 2px dashed var(--color-border);
        min-height: 50px; /* Slightly taller */
        display: flex;
        align-items: center;
        /* justify-content: center; /* Remove centering */
        padding: var(--spacing-small);
        background-color: var(--color-bg-medium);
        border-radius: 8px; /* Softer corners */
        font-weight: bold;
        color: var(--color-text-medium);
        position: relative; /* For placeholder positioning */
        overflow: hidden; /* Hide overflowing text */
        transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.1s ease;
    }

     .line-slot .slot-placeholder {
         position: absolute;
         top: 50%;
         left: 50%; /* Center Placeholder */
         transform: translate(-50%, -50%);
         color: rgba(0, 0, 0, 0.3); /* Dim placeholder text */
         font-weight: bold;
         pointer-events: none; /* Ensure it doesn't interfere with drag */
     }

     .line-slot.filled .slot-placeholder {
         display: none; /* Hide placeholder when filled */
     }


    .line-slot.drag-over {
        background-color: var(--color-secondary);
        border-color: var(--color-accent);
         transform: scale(1.02); /* Slight zoom on drag-over */
    }

    .line-slot.correct {
        border-color: var(--color-success);
        background-color: var(--color-success-light);
        box-shadow: 0 0 8px var(--color-success-light);
    }

    .line-slot.incorrect {
        border-color: var(--color-error);
        background-color: var(--color-error-light);
         box-shadow: 0 0 8px var(--color-error-light);
    }

    .line-slot.celebrate {
        animation: pulse-green 1.5s infinite alternate ease-in-out;
    }

    @keyframes pulse-green {
        0% { box-shadow: 0 0 8px var(--color-success); }
        100% { box-shadow: 0 0 15px var(--color-success), 0 0 5px var(--color-success-light); }
    }


    .draggable-line {
        border: 1px solid var(--color-border);
        background-color: #ffffff;
        padding: var(--spacing-small);
        margin-bottom: var(--spacing-small); /* Space between lines in source */
        cursor: grab;
        border-radius: 6px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        text-align: right; /* Hebrew text alignment */
        font-size: 1em;
        color: var(--color-text-dark);
        transition: transform 0.2s ease, box-shadow 0.2s ease, opacity 0.2s ease;
    }

    .draggable-line:hover {
        transform: translateY(-2px);
        box-shadow: 3px 3px 7px rgba(0,0,0,0.15);
    }

     .draggable-line:active {
         cursor: grabbing;
     }

     .draggable-line.dragging {
         opacity: 0.6;
         box-shadow: 5px 5px 10px rgba(0,0,0,0.2);
         transform: scale(1.05);
     }

    .line-slot .draggable-line {
        margin: 0; /* Remove margin when inside a slot */
        box-shadow: none; /* Remove shadow when inside a slot */
        cursor: grab; /* Keep grab cursor to indicate it's movable */
        background-color: transparent; /* Transparent background in slot */
        border: none; /* Remove border in slot */
        padding: 0; /* Remove padding in slot */
        text-align: right; /* Align text right within the slot */
        width: 100%; /* Take full width of the slot */
        font-weight: normal; /* Text weight in slot */
        color: inherit; /* Inherit color from slot feedback */
        transition: none; /* Disable transition when placed */
    }

     /* Specific styling for the line element itself when in a slot */
     .line-slot.correct .draggable-line {
         color: var(--color-success);
     }
     .line-slot.incorrect .draggable-line {
         color: var(--color-error);
     }


    .quatrain-end {
        margin-bottom: var(--spacing-large); /* More space after each quatrain */
    }

     .couplet-start {
         margin-top: var(--spacing-large); /* More space before the couplet */
         border-top: 2px dashed var(--color-border-light); /* Visual separator */
         padding-top: var(--spacing-medium);
     }


    .explanation-button {
        display: block;
        margin: var(--spacing-large) auto;
        padding: var(--spacing-small) var(--spacing-medium);
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        background-color: var(--color-primary);
        color: white;
        border-radius: 8px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .explanation-button:hover {
        background-color: #5a148c; /* Slightly darker purple */
        transform: translateY(-1px);
    }
     .explanation-button:active {
         transform: translateY(0);
     }

    #explanation {
        display: none; /* Hidden by default */
         opacity: 0;
         max-height: 0;
         overflow: hidden;
        margin-top: var(--spacing-medium);
        padding: 0 var(--spacing-medium); /* Adjust padding for animation */
        border: 1px solid var(--color-border-light);
        border-radius: 8px;
        background-color: #fff;
        transition: opacity 0.5s ease-out, max-height 0.5s ease-out, padding 0.5s ease-out;
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

     #explanation.expanded {
         display: block; /* Show block */
         opacity: 1;
         max-height: 1000px; /* Sufficiently large value */
         padding: var(--spacing-medium); /* Restore padding */
     }


    #explanation h2, #explanation h3 {
        color: var(--color-primary);
        border-bottom: 1px dashed var(--color-border-light);
        padding-bottom: var(--spacing-small);
        margin-top: var(--spacing-medium);
        margin-bottom: var(--spacing-small);
    }

     #explanation ul {
         padding-right: var(--spacing-medium); /* Add padding for list */
     }

     #explanation li {
         margin-bottom: var(--spacing-small);
     }

     #explanation p {
         line-height: 1.7;
         color: var(--color-text-medium);
     }


    /* Completion Message Overlay */
    .completion-message {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(255, 255, 255, 0.9);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 10; /* Above other content */
        opacity: 1;
        transition: opacity 0.3s ease;
    }

     .completion-message.hidden {
         opacity: 0;
         pointer-events: none; /* Disable interaction when hidden */
     }

    .message-content {
        text-align: center;
        background-color: var(--color-bg-light);
        padding: var(--spacing-large);
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        transform: scale(1);
        animation: pop-in 0.5s cubic-bezier(0.68, -0.55, 0.27, 1.55);
    }

     @keyframes pop-in {
         0% { transform: scale(0.8); opacity: 0; }
         100% { transform: scale(1); opacity: 1; }
     }


    .message-content h2 {
        color: var(--color-success);
        font-size: 2em;
        margin-bottom: var(--spacing-small);
    }

    .message-content p {
        font-size: 1.2em;
        color: var(--color-text-dark);
        margin-bottom: var(--spacing-medium);
    }

    .reset-button {
         padding: var(--spacing-small) var(--spacing-medium);
         font-size: 1.1em;
         cursor: pointer;
         border: none;
         background-color: var(--color-accent);
         color: white;
         border-radius: 6px;
         transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
     }

     .reset-button:hover {
         background-color: #e67a00; /* Darker orange */
          transform: translateY(-1px);
     }

     .reset-button:active {
         transform: translateY(0);
     }

</style>
```