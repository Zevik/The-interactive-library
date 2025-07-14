---
title: "בונים שרשרת מזון"
english_slug: building-a-food-chain
category: "מדעי החיים / ביולוגיה"
tags: ["שרשרת מזון", "אקולוגיה", "יחסי גומלין", "יצורים חיים", "סביבה"]
---
<h1>בונים שרשרת מזון: מסע בעקבות האנרגיה</h1>
<p class="intro-text">בואו נגלה יחד מי אוכל את מי בטבע! גררו את היצורים החיים בסדר הנכון כדי לבנות שרשרת מזון ולהבין איך אנרגיה זורמת במערכת האקולוגית.</p>

<div class="app-container">
    <div class="cards-area">
        <h2>היצורים שלכם:</h2>
        <div class="card" draggable="true" data-organism="עשב">
            <img src="placeholder-grass.png" alt="עשב" aria-hidden="true" style="display:none;"> <!-- Placeholder for potential image -->
            <span class="organism-name">עשב</span>
            <span class="organism-hint" data-role="יצרן">?</span>
        </div>
        <div class="card" draggable="true" data-organism="ארנב">
             <img src="placeholder-rabbit.png" alt="ארנב" aria-hidden="true" style="display:none;"> <!-- Placeholder for potential image -->
             <span class="organism-name">ארנב</span>
             <span class="organism-hint" data-role="צרכן ראשוני">?</span>
        </div>
        <div class="card" draggable="true" data-organism="שועל">
             <img src="placeholder-fox.png" alt="שועל" aria-hidden="true" style="display:none;"> <!-- Placeholder for potential image -->
             <span class="organism-name">שועל</span>
             <span class="organism-hint" data-role="צרכן שניוני">?</span>
        </div>
        <p class="cards-hint">גררו אותם לכאן →</p>
    </div>
    <div class="drop-zone">
        <h2>בנו את השרשרת כאן</h2>
        <div class="chain" id="food-chain">
            <!-- Dropped cards and arrows will appear here -->
        </div>
        <div class="feedback" id="feedback"></div>
        <button class="reset-button hidden">התחלה מחדש</button>
    </div>
</div>

<button id="toggle-explanation" class="toggle-explanation-button">למה זה קורה? הסבר</button>

<div class="explanation" id="explanation-content" style="display: none;">
    <h2>מהי שרשרת מזון באמת?</h2>
    <p>דמיינו קו המחבר יצורים חיים, ומראה איך אנרגיה עוברת מאחד לשני כשאחד נאכל על ידי השני. זוהי שרשרת מזון! היא חושפת את הקשרים הסודיים בין יצורים שונים במערכת אקולוגית ומסבירה איך האנרגיה של השמש, שנאגרת על ידי צמחים, מתגלגלת הלאה הלאה.</p>

    <h3>השחקנים הראשיים בשרשרת:</h3>
    <ul>
        <li><strong>יצרנים: גיבורי האנרגיה הראשוניים</strong><br>אלו הם לרוב צמחים או אצות מדהימות שיודעות לקחת אנרגיה ישירות מהשמש (בפוטוסינתזה!) ולהפוך אותה למזון. הם כמו תחנת הכוח של השרשרת. בשרשרת שלנו, <strong>העשב הירוק</strong> הוא היצרן.</li>
        <li><strong>צרכנים: אוכלי החיים</strong><br>יצורים שלא יכולים לייצר את האנרגיה שלהם בעצמם, אז הם אוכלים יצורים אחרים. יש להם תפקידים שונים בשרשרת:
            <ul>
                <li><strong>צרכנים ראשוניים: הצמחונים של השרשרת</strong><br>אלו שאוכלים ישירות את היצרנים (אוכלי עשב/צמחים). בסימולציה ששיחקתם, <strong>הארנב המתוק</strong> הוא צרכן ראשוני כי הוא מתבסס על העשב.</li>
                <li><strong>צרכנים שניוניים: הטורפים הראשונים</strong><br>אלו שאוכלים את הצרכנים הראשוניים (בדרך כלל אוכלי בשר). בשרשרת הפשוטה שלנו, <strong>השועל הערמומי</strong> הוא צרכן שניוני כי הוא צד ארנבים.</li>
                <li>ולפעמים, השרשרת ממשיכה עם <strong>צרכנים שלישוניים</strong>, <strong>רביעיוניים</strong> וכן הלאה, אוכלי בשר שאוכלים טורפים אחרים.</li>
            </ul>
        </li>
    </ul>

    <h3>לאן זורמת האנרגיה? עקוב אחר החץ!</h3>
    <p>החץ בשרשרת המזון (← במקרה שלנו, או → בכתיבה לועזית - הוא תמיד מצביע לכיוון זרימת האנרגיה, כלומר <strong>אל</strong> היצור שאוכל! עשב ← ארנב ← שועל. האנרגיה מהעשב עוברת לארנב כשהוא נאכל, והאנרגיה מהארנב עוברת לשועל כשהוא הופך לארוחה.</p>

    <h3>למה שרשרת מזון חשובה כל כך?</h3>
    <p>היא שומרת על האיזון העדין בטבע. היא מוודאת שאף אוכלוסייה לא גדלה מדי או קטנה מדי, ומבטיחה שהאנרגיה של החיים תנוע ותפרנס את כולם. אם חוליה אחת בשרשרת נעלמת, כל השרשרת יכולה להתערער, ממש כמו מגדל קלפים!</p>
</div>

<style>
    :root {
        --primary-color: #4CAF50; /* Green for life/plants */
        --secondary-color: #FF9800; /* Orange for energy/warmth */
        --bg-color: #e8f5e9; /* Light green background */
        --card-bg: #ffffff;
        --card-border: #c8e6c9;
        --drop-zone-bg: #f1f8e9; /* Lighter green */
        --drop-zone-border: #81c784; /* Medium green */
        --success-color: #2e7d32; /* Dark green */
        --success-bg: #e8f5e9;
        --error-color: #c62828; /* Red */
        --error-bg: #ffcdd2;
        --text-color: #212121;
        --hint-color: #558b2f;
    }

    body {
        font-family: 'Arial', sans-serif; /* More modern font */
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--bg-color);
        margin: 0;
        padding: 20px;
        direction: rtl; /* Ensure RTL */
        text-align: right; /* Ensure text alignment */
    }

    h1, h2, h3 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 15px;
    }

    .intro-text {
        text-align: center;
        font-size: 1.1em;
        margin-bottom: 30px;
        color: #333;
    }

    .app-container {
        display: flex;
        flex-direction: row;
        gap: 30px; /* Increased gap */
        margin-top: 20px;
        flex-wrap: wrap;
        justify-content: center; /* Center sections */
    }

    .cards-area, .drop-zone {
        flex: 1;
        min-width: 280px; /* Increased min-width */
        padding: 20px;
        border-radius: 12px; /* Rounded corners */
        box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Soft shadow */
        background-color: var(--drop-zone-bg); /* Use lighter background */
        border: 2px solid var(--drop-zone-border); /* Use medium green border */
        display: flex;
        flex-direction: column;
        align-items: center;
        min-height: 350px; /* Increased minimum height */
    }

    .cards-area {
         background-color: var(--bg-color); /* Slightly different background */
         border: 2px dashed var(--drop-zone-border); /* Dashed border */
    }

    .cards-area h2, .drop-zone h2 {
        margin-top: 0;
        color: var(--hint-color); /* Darker green for section titles */
    }

    .cards-hint {
        font-style: italic;
        color: #555;
        margin-top: auto; /* Push hint to bottom */
    }


    .card {
        background-color: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: 8px; /* Rounded corners for cards */
        padding: 15px 20px; /* More padding */
        margin: 8px 0; /* Vertical margin */
        cursor: grab;
        text-align: center;
        width: 150px; /* Wider cards */
        box-shadow: 0 2px 5px rgba(0,0,0,0.15); /* Card shadow */
        transition: transform 0.2s ease, box-shadow 0.2s ease; /* Smooth transitions */
        font-size: 1.1em; /* Larger text */
        font-weight: bold;
        position: relative; /* Needed for hint */
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .card img {
        width: 50px; /* Style for potential image */
        height: 50px;
        margin-bottom: 5px;
        border-radius: 4px;
    }

     .organism-hint {
         position: absolute;
         top: 5px;
         right: 5px;
         width: 20px;
         height: 20px;
         line-height: 20px;
         border-radius: 50%;
         background-color: rgba(255, 255, 255, 0.8);
         border: 1px solid var(--hint-color);
         color: var(--hint-color);
         font-size: 0.9em;
         font-weight: bold;
         cursor: help;
         text-align: center;
         opacity: 0; /* Start hidden */
         transition: opacity 0.2s ease;
     }

     .card:hover .organism-hint {
         opacity: 1; /* Show on hover */
     }

      .organism-hint::after {
          content: attr(data-role); /* Display role from data attribute */
          position: absolute;
          top: 100%; /* Position below the hint icon */
          right: 50%;
          transform: translateX(50%);
          background-color: rgba(0, 0, 0, 0.8);
          color: white;
          padding: 5px 8px;
          border-radius: 4px;
          font-size: 0.8em;
          white-space: nowrap;
          z-index: 10; /* Above other elements */
          opacity: 0;
          visibility: hidden;
          transition: opacity 0.2s ease, visibility 0.2s ease;
      }

      .organism-hint:hover::after {
          opacity: 1;
          visibility: visible;
      }


    .card:hover {
        transform: translateY(-5px); /* Lift effect on hover */
        box-shadow: 0 4px 10px rgba(0,0,0,0.2); /* More prominent shadow */
    }

    .card:active {
        cursor: grabbing;
        transform: scale(0.95); /* Slight squeeze on active */
        box-shadow: 0 1px 3px rgba(0,0,0,0.3);
    }

    .card.dragging { /* Class added while dragging */
        opacity: 0.6;
        border-style: dashed;
    }


    .drop-zone {
        position: relative; /* For absolute positioning of reset button */
        overflow: hidden; /* Hide overflow during animations */
    }

    .drop-zone.drag-over {
        background-color: #dcedc8; /* Highlight on drag over */
        border-color: var(--primary-color);
        box-shadow: 0 0 15px rgba(76, 175, 80, 0.4);
    }

    .chain {
        display: flex;
        flex-wrap: wrap; /* Allow wrapping */
        align-items: center;
        justify-content: center; /* Center the chain items */
        gap: 10px; /* Adjust gap for visual flow */
        min-height: 100px; /* Ensure space */
        padding: 15px;
        border-bottom: 2px dashed var(--drop-zone-border);
        width: 100%;
        box-sizing: border-box; /* Include padding in width */
    }

    .chain-item {
        background-color: var(--card-bg);
        border: 2px solid var(--primary-color); /* Solid border */
        border-radius: 8px;
        padding: 12px 18px;
        text-align: center;
        font-size: 1.1em;
        font-weight: bold;
        color: var(--text-color);
        position: relative; /* For role display */
        transition: transform 0.4s ease, opacity 0.4s ease; /* Animation */
        animation: pop-in 0.4s ease-out; /* Pop-in animation */
    }

     @keyframes pop-in {
         0% { transform: scale(0.8); opacity: 0; }
         80% { transform: scale(1.05); opacity: 1; }
         100% { transform: scale(1); }
     }

     .chain-item.incorrect-flash {
         animation: flash-error 0.5s ease-in-out 2; /* Flash red */
     }

     @keyframes flash-error {
         0%, 100% { border-color: var(--primary-color); }
         50% { border-color: var(--error-color); background-color: var(--error-bg); }
     }


    .chain-arrow {
        font-size: 2em;
        color: var(--primary-color); /* Green arrows */
        font-weight: bold;
        transition: color 0.5s ease; /* Smooth color change */
        /* Make arrow RTL aware */
         display: inline-block;
         transform: scaleX(-1); /* Flip arrow horizontally for RTL */
         margin: 0 5px; /* Space around arrow */
    }
     html[dir="ltr"] .chain-arrow {
         transform: scaleX(1); /* Normal arrow for LTR */
     }


    .role {
        position: absolute;
        bottom: -25px; /* Position below the item */
        left: 50%;
        transform: translateX(50%); /* Center relative to item in RTL */
        font-size: 0.8em;
        font-weight: normal;
        color: var(--hint-color);
        white-space: nowrap;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 2px 5px;
        border-radius: 4px;
        border: 1px dashed var(--hint-color);
        opacity: 0; /* Start hidden */
        transition: opacity 0.3s ease;
    }

     .chain-item.success .role {
        opacity: 1; /* Show role on success */
     }


    .feedback {
        margin-top: 25px;
        padding: 12px 18px; /* More padding */
        border-radius: 8px;
        min-height: 40px; /* Reserve space */
        text-align: center;
        width: 90%; /* Narrower feedback */
        max-width: 400px;
        opacity: 0; /* Start hidden */
        transform: translateY(10px);
        transition: opacity 0.4s ease, transform 0.4s ease;
        font-size: 1.1em;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-left: auto;
        margin-right: auto;
    }

    .feedback.visible {
         opacity: 1;
         transform: translateY(0);
    }

    .feedback.success {
        background-color: var(--success-bg);
        color: var(--success-color);
        border: 1px solid var(--success-color);
    }

    .feedback.error {
        background-color: var(--error-bg);
        color: var(--error-color);
        border: 1px solid var(--error-color);
    }


    .toggle-explanation-button {
        display: block;
        margin: 40px auto 20px auto; /* More space above/below */
        padding: 12px 25px; /* More padding */
        font-size: 1em;
        cursor: pointer;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.2s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .toggle-explanation-button:hover {
        background-color: #0056b3;
        transform: translateY(-2px);
    }

    .explanation {
        border-top: 2px dashed var(--drop-zone-border); /* Styled border */
        margin-top: 30px;
        padding-top: 30px;
        background-color: #f9f9f9;
        padding: 25px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
    }

    .explanation h2, .explanation h3 {
        color: var(--primary-color);
        margin-top: 20px;
        margin-bottom: 10px;
        text-align: right; /* Align explanation text right */
    }

    .explanation ul {
        margin-top: 15px;
        padding-right: 25px; /* Adjust padding for RTL list */
        list-style: disc; /* Use discs for list items */
    }

    .explanation li {
        margin-bottom: 10px;
        line-height: 1.7;
    }

     .explanation li strong {
         color: var(--hint-color);
     }


    .reset-button {
        position: absolute;
        bottom: 20px;
        left: 50%;
        transform: translateX(50%); /* Center button */
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        background-color: #f44336; /* Red color for reset */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.2s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .reset-button:hover {
        background-color: #d32f2f;
        transform: translateX(50%) translateY(-2px); /* Lift effect */
    }

    .reset-button.hidden {
        display: none;
    }


    /* Responsive adjustments */
    @media (max-width: 768px) {
        .app-container {
            flex-direction: column;
            gap: 20px;
        }
        .cards-area, .drop-zone {
            flex: none;
            width: 100%;
            min-width: unset;
            padding: 15px;
        }
        .chain {
             flex-direction: column; /* Stack items vertically */
             gap: 5px; /* Reduce gap */
             align-items: flex-start; /* Align items to start */
             padding: 10px;
             min-height: 250px; /* Give vertical chain more height */
             border-bottom: none; /* Remove horizontal line */
             border-left: 2px dashed var(--drop-zone-border); /* Add vertical line */
             width: auto; /* Auto width */
             height: 100%; /* Full height of drop zone */
             justify-content: flex-start; /* Align chain items to top */
        }
        .chain-arrow {
             font-size: 1.8em;
             transform: rotate(90deg); /* Rotate arrow down */
             margin: 5px auto; /* Center vertical arrow */
             align-self: center; /* Center the arrow in the flex column */
        }
         html[dir="ltr"] .chain-arrow {
             transform: rotate(90deg); /* Same rotation for LTR vertical */
         }
        .chain-item {
            margin: 5px 0; /* Add margin between items */
            width: 80%; /* Make items take more width */
             max-width: 200px; /* Max width */
            align-self: center; /* Center items in the column */
        }
        .role {
             bottom: auto; /* Reset bottom positioning */
             top: -25px; /* Position above the item */
             transform: translateX(50%); /* Maintain centering */
        }
        .feedback {
             width: 100%;
             max-width: unset;
             padding: 10px;
        }
        .reset-button {
            position: static; /* Change position to static */
            transform: none; /* Remove transform */
            margin-top: 20px; /* Add top margin */
        }
    }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const cardsArea = document.querySelector('.cards-area');
        const cards = cardsArea.querySelectorAll('.card');
        const dropZone = document.getElementById('food-chain');
        const dropZoneContainer = document.querySelector('.drop-zone');
        const feedback = document.getElementById('feedback');
        const explanationButton = document.getElementById('toggle-explanation');
        const explanationContent = document.getElementById('explanation-content');
        const resetButton = dropZoneContainer.querySelector('.reset-button');

        // Organism order and roles - kept consistent
        const organisms = ['עשב', 'ארנב', 'שועל'];
        const roles = {
            'עשב': 'יצרן',
            'ארנב': 'צרכן ראשוני',
            'שועל': 'צרכן שניוני'
        };

        // --- Drag and Drop Handlers ---
        cards.forEach(card => {
            card.addEventListener('dragstart', (event) => {
                event.dataTransfer.setData('text/plain', event.target.dataset.organism);
                event.target.classList.add('dragging'); // Add dragging class for visual feedback
                // Set drag image (optional, often browser default is fine)
                // event.dataTransfer.setDragImage(event.target, event.target.offsetWidth / 2, event.target.offsetHeight / 2);
            });

             card.addEventListener('dragend', (event) => {
                  event.target.classList.remove('dragging'); // Remove dragging class
                  // Card is hidden by JS if successfully dropped, otherwise remains visible.
             });
        });

         function handleDragOver(event) {
             event.preventDefault(); // Necessary to allow dropping
             dropZoneContainer.classList.add('drag-over'); // Highlight drop zone container
         }

         function handleDragLeave() {
             dropZoneContainer.classList.remove('drag-over'); // Remove highlight
         }

         function handleDrop(event) {
              event.preventDefault();
              dropZoneContainer.classList.remove('drag-over'); // Remove highlight

              const organism = event.dataTransfer.getData('text/plain');
              const currentChainItems = Array.from(dropZone.querySelectorAll('.chain-item'));
              const currentChainOrganisms = currentChainItems.map(item => item.dataset.organism);
              const nextIndex = currentChainOrganisms.length;

               // Find the card that was dragged in the original area (check if it's still available)
               const draggedCardInArea = Array.from(cardsArea.querySelectorAll('.card:not([style*="display: none"])'))
                                            .find(card => card.dataset.organism === organism);


              // Prevent dropping if the card is not available in the original area
              if (!draggedCardInArea) {
                 showFeedback('זה היצור הלא נכון או שהוא כבר נמצא בשרשרת!', 'error', 3000);
                 return;
              }


              // Check if the dropped organism is the correct next one in the sequence
              if (nextIndex < organisms.length && organism === organisms[nextIndex]) {
                  // --- Correct Drop ---

                  // Add arrow before the new item if it's not the first item
                  if (nextIndex > 0) {
                       const arrow = document.createElement('div');
                       arrow.classList.add('chain-arrow');
                       arrow.textContent = '←'; // Arrow points from eaten to eater (RTL flow)
                       dropZone.appendChild(arrow); // Append arrow
                   }

                  const newItem = document.createElement('div');
                  newItem.classList.add('chain-item');
                  newItem.dataset.organism = organism;
                  newItem.textContent = organism; // Text content for now, could add image later
                  // Add initial state for animation
                  newItem.style.opacity = '0';
                  newItem.style.transform = 'scale(0.8)';


                   dropZone.appendChild(newItem); // Append the new item

                   // Trigger pop-in animation after adding to DOM
                   requestAnimationFrame(() => { // Use rAF for better animation triggering
                       newItem.style.opacity = '1';
                       newItem.style.transform = 'scale(1)';
                   });


                  showFeedback('נכון! ממשיכים לבנות את השרשרת.', 'success', 2000);

                   // Hide the card from the draggable area immediately
                  draggedCardInArea.style.display = 'none';


                  // Check if the chain is complete and correct
                  if (currentChainOrganisms.length + 1 === organisms.length) {
                      displaySuccess();
                  }

              } else {
                  // --- Incorrect Drop ---
                  let errorMessage = 'שגוי. ';
                  const expected = organisms[nextIndex];

                  if (nextIndex >= organisms.length) {
                       errorMessage = 'השרשרת כבר מלאה! נסו להתחיל מחדש.';
                       // If the chain was already complete, don't reset, just show message.
                       showFeedback(errorMessage, 'error', 3000);
                       return; // Don't reset if already complete
                  } else if (currentChainOrganisms.includes(organism)) {
                       errorMessage += `ה${organism} כבר נמצא בשרשרת.`;
                  } else if (nextIndex === 0) {
                       errorMessage += `שרשרת מזון מתחילה ב<strong>יצרן</strong>. התחילו עם ${expected}.`;
                  } else {
                        const lastOrganism = currentChainOrganisms[currentChainOrganisms.length - 1];
                        errorMessage += `אחרי ה${lastOrganism} אמור להגיע ה${expected}. זכרו, האנרגיה זורמת מהנאכל ← אל האוכל.`;
                  }


                  showFeedback(errorMessage, 'error', 4000); // Show error for a bit longer

                  // Optional: Flash the currently dropped (incorrect) item briefly?
                  // This is complex as the item wasn't added. Better to flash existing chain if any?
                   if (currentChainItems.length > 0) {
                       currentChainItems[currentChainItems.length - 1].classList.add('incorrect-flash');
                       setTimeout(() => {
                           currentChainItems[currentChainItems.length - 1].classList.remove('incorrect-flash');
                       }, 1000); // Flash duration
                   }


                  // Reset the chain after showing the error message
                   setTimeout(resetChain, 4000); // Wait for message to be seen

              }
         }

        // Function to show feedback message with animation
        function showFeedback(message, type, duration = 3000) {
             feedback.innerHTML = message; // Use innerHTML to allow strong tag
             feedback.className = `feedback ${type} visible`; // Add type and visible class

             if (feedback.hideTimeout) { // Clear previous timeout if exists
                  clearTimeout(feedback.hideTimeout);
             }

             feedback.hideTimeout = setTimeout(() => {
                  feedback.classList.remove('visible');
                   // Optional: Clear message content after fading out
                   // setTimeout(() => { feedback.textContent = ''; }, 500); // Match CSS transition duration
             }, duration);
        }


        function displaySuccess() {
            showFeedback('🎉 מעולה! בניתם שרשרת מזון נכונה! 🎉', 'success', 5000);

            // Add roles to the chain items with animation
            const chainItems = dropZone.querySelectorAll('.chain-item');
            chainItems.forEach(item => {
                const organism = item.dataset.organism;
                // Check if role span already exists
                if (!item.querySelector('.role')) {
                    const roleSpan = document.createElement('span');
                    roleSpan.classList.add('role');
                    roleSpan.textContent = `(${roles[organism]})`;
                    item.appendChild(roleSpan);
                     // Trigger role pop-in animation
                     requestAnimationFrame(() => {
                         item.classList.add('success'); // Use class to trigger role visibility via CSS
                     });
                } else {
                    // If role already exists (e.g., after reset), just ensure it's visible
                     item.classList.add('success');
                }

            });

            // Animate arrows for success
             dropZone.querySelectorAll('.chain-arrow').forEach(arrow => {
                 arrow.style.color = var(--success-color); // Use green from CSS var
                 arrow.style.transition = 'color 0.5s ease';
             });

            // Disable further dropping after success
            dropZoneContainer.removeEventListener('dragover', handleDragOver);
            dropZoneContainer.removeEventListener('dragleave', handleDragLeave);
            dropZoneContainer.removeEventListener('drop', handleDrop);

            // Show the reset button
            resetButton.classList.remove('hidden');
        }

        function resetChain() {
            dropZone.innerHTML = ''; // Clear the chain items and arrows
            feedback.classList.remove('visible'); // Hide feedback immediately on reset
            feedback.textContent = ''; // Clear content

            // Show all cards again with animation
            cards.forEach(card => {
                card.style.display = ''; // Make card visible
                // Optional: Add a reset animation to the card in the original area
                 card.style.opacity = '0';
                 card.style.transform = 'scale(0.8)';
                 requestAnimationFrame(() => {
                     card.style.opacity = '1';
                     card.style.transform = 'scale(1)';
                     card.style.transition = 'transform 0.4s ease, opacity 0.4s ease'; // Apply transition
                 });
                 // Remove role hint text that might have been added temporarily
                 const hint = card.querySelector('.organism-hint');
                 if(hint) hint.textContent = '?';

            });


            // Re-attach event listeners (in case of success)
             dropZoneContainer.addEventListener('dragover', handleDragOver);
             dropZoneContainer.addEventListener('dragleave', handleDragLeave);
             dropZoneContainer.addEventListener('drop', handleDrop);

             // Hide the reset button
             resetButton.classList.add('hidden');

             // Restore default styles (like arrow color) - transition handled by CSS
             dropZone.querySelectorAll('.chain-arrow').forEach(arrow => {
                  arrow.style.color = var(--primary-color);
                  // No need to reset transition property if it's defined in CSS
             });

             // Remove success class from items if any lingered (shouldn't happen with innerHTML='')
             dropZone.querySelectorAll('.chain-item').forEach(item => item.classList.remove('success'));
        }

        // --- Explanation Toggle ---
        explanationButton.addEventListener('click', () => {
            const isHidden = explanationContent.style.display === 'none';
            // Use classes for smoother toggle animation via CSS if desired
            if (isHidden) {
                 explanationContent.style.display = 'block';
                 // Add animation class if needed
            } else {
                 // Add fade-out class, then set display: none after transition
                 explanationContent.style.display = 'none';
            }
            explanationButton.textContent = isHidden ? 'הסתר הסבר נוסף' : 'למה זה קורה? הסבר';
        });

         // Add event listener to reset button
         resetButton.addEventListener('click', resetChain);

         // Initial state: Ensure cards are visible and chain is empty on load
         resetChain();

    });
</script>
```