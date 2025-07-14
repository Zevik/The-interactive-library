---
title: "בנו את שרשרת המזון - משחק אינטראקטיבי"
english_slug: simple-food-chain-assembly
category: "מדעי החיים / ביולוגיה"
tags: [שרשרת מזון, אקולוגיה, אינטראקטיבי, הדמיה, משחק, יסודי, חטיבת ביניים]
---
# בנו את שרשרת המזון

צאו למסע בעולם הטבע והרכיבו שרשרת מזון בסיסית כדי לחשוף כיצד אנרגיה זורמת מיצור ליצור. האם תצליחו לבנות את השרשרת הנכונה?

<div id="app-container">
  <div id="organism-palette">
    <div class="organism-card draggable" id="org-plant" data-type="producer" draggable="true">
      <span class="emoji">🌱</span>
      <span class="label">צמח</span>
    </div>
    <div class="organism-card draggable" id="org-rabbit" data-type="primary" draggable="true">
      <span class="emoji">🐰</span>
      <span class="label">ארנב</span>
    </div>
    <div class="organism-card draggable" id="org-fox" data-type="secondary" draggable="true">
      <span class="emoji">🦊</span>
      <span class="label">שועל</span>
    </div>
     <div class="organism-card draggable" id="org-wolf" data-type="tertiary" draggable="true">
       <span class="emoji">🐺</span>
       <span class="label">זאב</span>
     </div>
  </div>

  <div id="food-chain-zones">
    <div class="zone-container">
      <div class="drop-zone" id="zone-producer" data-accept="producer"></div>
      <p class="zone-label">יצרן</p>
    </div>
    <div class="chain-link" id="link-producer-primary">
      <div class="arrow-line"></div>
      <div class="arrow-head"></div>
    </div>
    <div class="zone-container">
      <div class="drop-zone" id="zone-primary" data-accept="primary"></div>
      <p class="zone-label">צרכן ראשוני</p>
    </div>
      <div class="chain-link" id="link-primary-secondary">
      <div class="arrow-line"></div>
      <div class="arrow-head"></div>
    </div>
    <div class="zone-container">
      <div class="drop-zone" id="zone-secondary" data-accept="secondary"></div>
      <p class="zone-label">צרכן שניוני</p>
    </div>
     <div class="chain-link" id="link-secondary-tertiary">
      <div class="arrow-line"></div>
      <div class="arrow-head"></div>
    </div>
     <div class="zone-container">
      <div class="drop-zone" id="zone-tertiary" data-accept="tertiary"></div>
      <p class="zone-label">צרכן שלישוני</p>
    </div>
  </div>

  <div id="feedback-area"></div>
</div>

<button id="toggle-explanation">הסבר על שרשרת מזון</button>

<div id="explanation-content" class="hidden">
  <h2>מהי שרשרת מזון ולמה היא חשובה?</h2>
  <p>שרשרת מזון היא כמו מסלול אנרגיה בעולם הטבע! היא מראה לנו כיצד אנרגיה עוברת מיצור ליצור דרך אכילה. כל יצור זקוק לאנרגיה כדי לחיות ולגדול, ושרשרת המזון מסבירה לנו מאין הוא מקבל אותה.</p>

  <h3>השחקנים הראשיים בשרשרת:</h3>
  <ul>
    <li><strong>יצרנים:</strong> אלה הם גיבורי הפוטוסינתזה! בדרך כלל צמחים או אצות, הם מייצרים את המזון (אנרגיה) שלהם בעצמם באמצעות אור השמש. הם הבסיס של כל שרשרת מזון.</li>
    <li><strong>צרכנים ראשוניים:</strong> קוראים להם גם אוכלי עשב. הם הראשונים שצורכים את האנרגיה מהיצרנים כשהם אוכלים אותם.</li>
    <li><strong>צרכנים שניוניים:</strong> אלה הם אוכלי בשר (קרניבורים) או אוכלי כל. הם מקבלים את האנרגיה שלהם כשהם אוכלים את הצרכנים הראשוניים.</li>
    <li><strong>צרכנים שלישוניים/רביעוניים:</strong> נמצאים בראש השרשרת, אוכלים צרכנים שניוניים או שלישוניים. גם הם יכולים להיות אוכלי בשר או אוכלי כל.</li>
    <li><strong>מפרקים:</strong> (חיידקים, פטריות ותולעים) הם עובדי הניקיון של הטבע! הם מפרקים חומר אורגני מת ומחזירים חומרים מזינים חזרה לאדמה, עוזרים ליצרנים לגדול וסוגרים מעגל קסמים טבעי. (לפעמים לא מראים אותם בשרשרת פשוטה, אבל הם קריטיים!).</li>
  </ul>

  <p>שימו לב לחצים בשרשרת! הם תמיד מצביעים לכיוון היצור ש'מקבל' את האנרגיה – כלומר, לכיוון מי שאוכל את מי שלפניו בשרשרת.</p>
</div>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Varela+Round&display=swap');

  :root {
    --primary-color: #2E7D32; /* Darker Green */
    --secondary-color: #FFB300; /* Amber */
    --background-color: #E8F5E9; /* Lightest Green */
    --card-background: #FFFFFF;
    --border-color: #A5D6A7; /* Light Green */
    --text-color: #212121; /* Dark Grey */
    --success-color: #4CAF50;
    --error-color: #E53935; /* Red */
    --arrow-color-inactive: #BDBDBD; /* Grey */
    --arrow-color-active: var(--success-color);
    --drop-zone-border: dashed 2px var(--border-color);
    --drop-zone-hover-border: dashed 2px var(--secondary-color);
    --drop-zone-active-border: solid 3px var(--success-color); /* Thicker when correct */
    --zone-background-empty: #E0F7FA; /* Light Cyan */
    --zone-background-filled: #DCEDC8; /* Light Greenish */
    --zone-background-hover: #FFF9C4; /* Light Yellow */
  }

  body {
    font-family: 'Varela Round', sans-serif;
    line-height: 1.7;
    color: var(--text-color);
    background-color: var(--background-color);
    padding: 20px;
    direction: rtl; /* Hebrew support */
    text-align: right;
    overflow-x: hidden; /* Prevent horizontal scroll on shake */
  }

  h1, h2, h3 {
    color: var(--primary-color);
    text-align: center;
    margin-bottom: 15px;
  }

  h1 {
      margin-top: 0;
      font-size: 2em;
  }

   h2 {
       font-size: 1.6em;
   }
    h3 {
       font-size: 1.3em;
       color: var(--secondary-color);
       margin-top: 20px;
       margin-bottom: 8px;
    }


  #app-container {
    background-color: var(--card-background);
    border-radius: 12px;
    padding: 25px;
    margin: 20px auto;
    max-width: 900px; /* Limit width for better readability */
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  #organism-palette {
    display: flex;
    justify-content: center;
    gap: 15px; /* Reduced gap */
    margin-bottom: 40px; /* More space below palette */
    flex-wrap: wrap;
  }

  .organism-card {
    font-size: 45px; /* Slightly larger emoji */
    cursor: grab;
    padding: 15px 20px; /* Increased padding */
    border: 1px solid var(--border-color);
    border-radius: 10px; /* More rounded */
    background-color: #ffffff;
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    display: flex;
    flex-direction: column;
    align-items: center;
    user-select: none;
    min-width: 100px; /* Give cards minimum width */
    text-align: center;
  }

  .organism-card .emoji {
      display: block; /* Stack emoji and label */
      margin-bottom: 8px; /* Space between emoji and label */
      line-height: 1; /* Prevent extra space around emoji */
  }


  .organism-card .label {
    font-size: 1rem; /* Base label size */
    color: var(--text-color);
    font-weight: bold;
  }


  .organism-card:active {
    cursor: grabbing;
    transform: scale(1.05); /* Slightly smaller scale increase */
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
  }

  #food-chain-zones {
    display: flex;
    align-items: center;
    gap: 5px; /* Reduced gap for tighter chain look */
    flex-wrap: wrap; /* Allow wrapping on smaller screens */
    justify-content: center;
    width: 100%; /* Take full width */
  }

  .zone-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      min-width: 100px;
      flex-shrink: 0; /* Prevent shrinking */
  }

  .drop-zone {
    width: 90px; /* Larger zones */
    height: 90px;
    border: var(--drop-zone-border);
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: border-color 0.3s ease-in-out, background-color 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
    position: relative;
    background-color: var(--zone-background-empty);
    margin-bottom: 8px; /* Reduced space */
    box-shadow: inset 0 2px 5px rgba(0,0,0,0.1); /* Inner shadow when empty */
  }

  /* Style for dropped organism inside zone */
  .drop-zone .organism-card {
      font-size: 55px; /* Larger icon when in zone */
      border: none;
      box-shadow: none;
      background-color: transparent;
      cursor: default;
      padding: 0;
      transform: none !important; /* Override drag active transform */
      display: flex; /* Ensure flex layout inside */
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: 100%; /* Take full zone space */
      height: 100%;
  }
   .drop-zone .organism-card .emoji {
       margin-bottom: 4px; /* Less space in zone */
   }
   .drop-zone .organism-card .label {
       font-size: 0.85rem; /* Smaller label in zone */
       font-weight: normal; /* Less bold in zone */
   }


  .drop-zone.drag-over-potential {
     border-color: var(--secondary-color);
     background-color: var(--zone-background-hover);
     box-shadow: 0 0 10px rgba(var(--secondary-color), 0.5); /* Subtle glow */
  }
   .drop-zone.drag-over { /* When an acceptable item is directly over */
     background-color: var(--zone-background-hover);
     border-style: solid; /* Solid border when ready to drop */
  }

  .drop-zone.correct {
     border: var(--drop-zone-active-border);
     background-color: var(--zone-background-filled);
     box-shadow: 0 0 12px rgba(var(--success-color), 0.6); /* Stronger glow when correct */
  }
   /* Style when a zone contains an item */
   .drop-zone:not(:empty) {
       background-color: var(--zone-background-filled);
       box-shadow: 0 2px 8px rgba(0,0,0,0.15); /* Outer shadow when filled */
   }


  .zone-label {
    font-size: 0.9rem; /* Slightly smaller label font */
    color: var(--text-color);
    text-align: center;
    font-weight: bold;
  }

  .chain-link {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 50px; /* Wider arrow area */
      margin: 0; /* No overlap */
      flex-shrink: 0;
      overflow: hidden;
  }

  .arrow-line {
      width: 0;
      height: 6px; /* Thicker line */
      background-color: var(--arrow-color-inactive);
      transition: width 0.4s ease-out, background-color 0.4s ease-out;
      transform-origin: right center;
  }

  .arrow-head {
      width: 0;
      height: 0;
      border-top: 10px solid transparent; /* Larger arrowhead */
      border-bottom: 10px solid transparent;
      border-left: 15px solid var(--arrow-color-inactive); /* Arrowhead color */
      transition: border-left-color 0.4s ease-out;
  }

  .chain-link.active .arrow-line {
      width: 50px; /* Full width */
      background-color: var(--arrow-color-active);
  }

   .chain-link.active .arrow-head {
      border-left-color: var(--arrow-color-active);
   }

  /* Animation for correct arrows/zones */
  .chain-link.active, .drop-zone.correct {
      animation: pulse-correct 1.5s infinite alternate ease-in-out;
  }

  @keyframes pulse-correct {
      0% { transform: scale(1); opacity: 1; }
      100% { transform: scale(1.02); opacity: 0.95; }
  }


  #feedback-area {
    margin-top: 30px;
    font-size: 1.2em; /* Larger feedback text */
    font-weight: bold;
    min-height: 1.8em; /* Reserve more space */
    text-align: center;
    padding: 10px;
    border-radius: 8px;
    transition: color 0.3s ease, background-color 0.3s ease;
    width: 100%; /* Take full width */
  }

  #feedback-area.success {
    color: white;
    background-color: var(--success-color);
     animation: pulse-text 1s ease-out forwards; /* Add pulse animation on final success */
  }
    @keyframes pulse-text {
        0% { transform: scale(0.9); opacity: 0; }
        70% { transform: scale(1.05); opacity: 1; }
        100% { transform: scale(1); opacity: 1; }
    }


   #feedback-area.error {
    color: white;
    background-color: var(--error-color);
    animation: shake 0.5s ease-in-out; /* Shake feedback area on error */
  }

    #feedback-area.partial-feedback {
        color: var(--text-color);
        background-color: #FFF9C4; /* Light yellow background */
        border: 1px solid var(--secondary-color);
    }

  #toggle-explanation {
    display: block;
    margin: 30px auto; /* More space */
    padding: 12px 25px; /* More padding */
    font-size: 1.1em; /* Larger font */
    cursor: pointer;
    background-color: var(--primary-color);
    color: white;
    border: none;
    border-radius: 8px; /* More rounded */
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-family: 'Varela Round', sans-serif;
  }

  #toggle-explanation:hover {
    background-color: #1B5E20; /* Darker Green */
  }
   #toggle-explanation:active {
       transform: scale(0.98);
   }

  #explanation-content {
    background-color: var(--card-background);
    border-radius: 12px;
    padding: 25px;
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
    margin-top: 20px;
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
    transition: opacity 0.5s ease, transform 0.5s ease;
    transform: translateY(20px);
    opacity: 0;
  }

  #explanation-content.hidden {
    display: none;
     transform: translateY(0); /* Reset for transition */
     opacity: 1; /* Reset for transition */
  }
  /* Style for when explanation is shown (after display change) */
   #explanation-content:not(.hidden) {
       transform: translateY(0);
       opacity: 1;
   }


  #explanation-content h2 {
      color: var(--primary-color);
      margin-top: 0;
      margin-bottom: 10px;
      text-align: right; /* Align explanation headings right */
  }

   #explanation-content h3 {
      color: var(--secondary-color);
      margin-top: 15px;
      margin-bottom: 5px;
      text-align: right;
       font-weight: bold;
  }

  #explanation-content ul {
      list-style: disc outside; /* List markers outside */
      padding-right: 20px;
      margin-bottom: 15px;
  }

  #explanation-content li {
      margin-bottom: 10px; /* More space between list items */
      line-height: 1.5;
  }
    #explanation-content strong {
        color: var(--primary-color); /* Highlight terms */
    }

    /* Ensure the draggable item being dragged doesn't render weirdly */
    .organism-card.dragging {
        opacity: 0.01; /* Almost invisible */
    }

    /* Shake animation CSS */
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        20%, 60% { transform: translateX(-8px); }
        40%, 80% { transform: translateX(8px); }
    }
    /* Apply shake to drop zone on incorrect drop */
     .drop-zone.shake {
         animation: shake 0.5s ease-in-out;
     }
    /* Apply shake to organism card on incorrect drop */
     .organism-card.shake {
          animation: shake 0.5s ease-in-out;
     }

     /* Responsive adjustments */
     @media (max-width: 600px) {
        #organism-palette, #food-chain-zones {
            flex-direction: column; /* Stack vertically */
            align-items: center;
            gap: 15px;
        }
        .zone-container {
             min-width: auto; /* Allow shrinking */
        }
        .chain-link {
            width: 1px; /* Vertical chain links need minimal width */
            height: 40px; /* Vertical height */
            flex-direction: column; /* Stack line and head vertically */
            margin: 10px 0; /* Vertical margin */
        }
         .arrow-line {
             width: 6px; /* Vertical line thickness */
             height: 0; /* Start with height 0 */
             transform-origin: bottom center;
             transition: height 0.4s ease-out, background-color 0.4s ease-out;
         }
         .arrow-head {
            border-left: none; /* Remove horizontal head */
            border-top: 15px solid var(--arrow-color-inactive); /* Vertical head */
             border-right: 10px solid transparent;
             border-left: 10px solid transparent;
            transition: border-top-color 0.4s ease-out;
         }
          .chain-link.active .arrow-line {
             width: 6px; /* Maintain thickness */
             height: 40px; /* Full height */
         }
          .chain-link.active .arrow-head {
             border-top-color: var(--arrow-color-active);
         }
     }


</style>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const draggables = document.querySelectorAll('.draggable');
    const dropZones = document.querySelectorAll('.drop-zone');
    const organismPalette = document.getElementById('organism-palette');
    const explanationButton = document.getElementById('toggle-explanation');
    const explanationContent = document.getElementById('explanation-content');
    const feedbackArea = document.getElementById('feedback-area');
    const chainLinks = document.querySelectorAll('.chain-link');

    // Map zone IDs to expected organism types
    const zoneTypeMap = {
        'zone-producer': 'producer',
        'zone-primary': 'primary',
        'zone-secondary': 'secondary',
        'zone-tertiary': 'tertiary'
    };

    draggables.forEach(organism => {
      organism.addEventListener('dragstart', (e) => {
        const draggedOrganism = e.target.closest('.organism-card'); // Ensure we drag the whole card
        e.dataTransfer.setData('text/plain', draggedOrganism.id);
        e.dataTransfer.setData('text/type', draggedOrganism.dataset.type);
        // Add a class for styling while dragging - use timeout
        setTimeout(() => {
             draggedOrganism.classList.add('dragging');
        }, 0); // Timeout allows drag ghost image to be created

         // Add visual cue to valid drop zones during drag
         dropZones.forEach(zone => {
             if (zone.dataset.accept === draggedOrganism.dataset.type) {
                 zone.classList.add('drag-over-potential');
             }
         });
      });

      organism.addEventListener('dragend', (e) => {
         // Remove styling class and restore visibility
         const draggedOrganism = e.target.closest('.organism-card');
         draggedOrganism.classList.remove('dragging');
         // Note: Opacity restoration is handled by CSS on dragging removal

          // Remove visual cue from drop zones
         dropZones.forEach(zone => {
             zone.classList.remove('drag-over-potential');
             zone.classList.remove('drag-over');
         });
      });
    });

    dropZones.forEach(zone => {
      zone.addEventListener('dragover', (e) => {
        e.preventDefault(); // Allow drop
        const draggedItemType = e.dataTransfer.getData('text/type');
        // Check if the zone accepts this type AND if it's currently empty
        if (zone.dataset.accept === draggedItemType && zone.querySelector('.organism-card') === null) {
             zone.classList.add('drag-over');
        } else {
            // Optionally, add a class for invalid drag over
            // zone.classList.add('drag-over-invalid');
        }
      });

      zone.addEventListener('dragleave', () => {
        zone.classList.remove('drag-over');
        // zone.classList.remove('drag-over-invalid');
      });

      zone.addEventListener('drop', (e) => {
        e.preventDefault();
        zone.classList.remove('drag-over');
        // zone.classList.remove('drag-over-invalid'); // Clean up invalid state

        const organismId = e.dataTransfer.getData('text/plain');
        const organism = document.getElementById(organismId);
        const dropZone = e.target.closest('.drop-zone'); // Ensure we get the drop-zone element
        const droppedItemType = organism.dataset.type;
        const acceptedType = dropZone.dataset.accept;

        // Only allow drop if the type matches the zone's accepted type and zone is empty
        if (droppedItemType === acceptedType && dropZone.querySelector('.organism-card') === null) {

          // Remove organism from its original parent (palette or another zone)
           if (organism.parentElement) { // Check if it has a parent
                organism.parentElement.removeChild(organism);
           }

          // Append the dragged organism to the drop zone
          dropZone.appendChild(organism);
          organism.classList.remove('dragging'); // Remove dragging class

          // Clear any previous feedback
          feedbackArea.textContent = '';
          feedbackArea.className = ''; // Remove all classes

          // Check and update arrows and feedback
          updateChainState();

        } else {
             // Incorrect drop logic
             feedbackArea.textContent = 'אופס! היצור הזה לא מתאים לשלב הזה של השרשרת, או שהמקום כבר תפוס.';
             feedbackArea.classList.remove('success', 'partial-feedback');
             feedbackArea.classList.add('error');

             // Animate the incorrect drop zone briefly
             dropZone.classList.add('shake');
             setTimeout(() => {
                dropZone.classList.remove('shake');
             }, 500);

              // Also shake the organism card slightly
              organism.classList.add('shake');
              setTimeout(() => {
                 organism.classList.remove('shake');
              }, 500);
        }
         // Remove visual cue from all drop zones regardless of drop success
         dropZones.forEach(z => {
             z.classList.remove('drag-over-potential');
             z.classList.remove('drag-over');
             // z.classList.remove('drag-over-invalid');
         });
      });
    });

    // Allow dropping back into the palette
    organismPalette.addEventListener('dragover', (e) => {
        e.preventDefault(); // Allow drop
        e.dataTransfer.dropEffect = 'move';
        organismPalette.classList.add('drag-over-potential'); // Optional visual cue for palette
    });

     organismPalette.addEventListener('dragleave', () => {
        organismPalette.classList.remove('drag-over-potential');
     });

    organismPalette.addEventListener('drop', (e) => {
        e.preventDefault();
        organismPalette.classList.remove('drag-over-potential');

        const organismId = e.dataTransfer.getData('text/plain');
        const organism = document.getElementById(organismId);

        // If the organism is currently in a drop zone, remove it
        if (organism && organism.parentElement && organism.parentElement.classList.contains('drop-zone')) {
             const previousZone = organism.parentElement;
             previousZone.removeChild(organism); // Remove from zone
             organismPalette.appendChild(organism); // Add back to palette
             organism.classList.remove('dragging'); // Clean up dragging class
             organism.style.opacity = '1'; // Ensure visibility

             // Update chain state as an organism was removed
             updateChainState();

              // Clear feedback if chain is now incomplete
             feedbackArea.textContent = '';
             feedbackArea.className = '';

        } else if (organism) {
             // If dropped back onto the palette but wasn't in a zone (e.g., dragged within palette)
             organismPalette.appendChild(organism); // Ensure it's in the palette div
             organism.classList.remove('dragging');
             organism.style.opacity = '1';
        }

         // Clean up drag over styles from zones
         dropZones.forEach(z => {
             z.classList.remove('drag-over-potential');
             z.classList.remove('drag-over');
         });

    });


    function updateChainState() {
        const zones = {
            producer: document.getElementById('zone-producer'),
            primary: document.getElementById('zone-primary'),
            secondary: document.getElementById('zone-secondary'),
            tertiary: document.getElementById('zone-tertiary')
        };

        const links = {
            producer_primary: document.getElementById('link-producer-primary'),
            primary_secondary: document.getElementById('link-primary-secondary'),
            secondary_tertiary: document.getElementById('link-secondary-tertiary')
        };

        const state = {
            producer: zones.producer.querySelector('.organism-card[data-type="producer"]') !== null,
            primary: zones.primary.querySelector('.organism-card[data-type="primary"]') !== null,
            secondary: zones.secondary.querySelector('.organism-card[data-type="secondary"]') !== null,
            tertiary: zones.tertiary.querySelector('.organism-card[data-type="tertiary"]') !== null
        };

        // Update zone correctness and animation class
        zones.producer.classList.toggle('correct', state.producer);
        zones.primary.classList.toggle('correct', state.primary);
        zones.secondary.classList.toggle('correct', state.secondary);
        zones.tertiary.classList.toggle('correct', state.tertiary);

        // Update arrow correctness and animation class
        links.producer_primary.classList.toggle('active', state.producer && state.primary);
        links.primary_secondary.classList.toggle('active', state.primary && state.secondary);
        links.secondary_tertiary.classList.toggle('active', state.secondary && state.tertiary);

        // Update feedback message
        feedbackArea.textContent = ''; // Clear previous text
        feedbackArea.className = ''; // Clear previous classes (like error or partial)

        if (state.producer && state.primary && state.secondary && state.tertiary) {
            feedbackArea.textContent = 'מצוין! הרכבתם שרשרת מזון שלמה ונכונה!';
            feedbackArea.classList.add('success');
             // Optional: Add a short celebration effect? (Beyond current scope)
        } else {
             // Check how many are correct to give partial feedback
             const correctCount = Object.values(state).filter(Boolean).length;
             if (correctCount > 0) {
                  feedbackArea.textContent = `השרשרת מתחילה להתחבר! הרכבת נכון ${correctCount} שלבים. המשיכו!`;
                  feedbackArea.classList.add('partial-feedback');
             }
             // If correctCount is 0, feedback remains empty as cleared initially.
        }
    }


    explanationButton.addEventListener('click', () => {
      explanationContent.classList.toggle('hidden');
      if (!explanationContent.classList.contains('hidden')) {
          explanationButton.textContent = 'הסתר הסבר';
          // Optional: Scroll into view smoothly
           explanationContent.scrollIntoView({ behavior: 'smooth', block: 'start' });
      } else {
          explanationButton.textContent = 'הסבר על שרשרת מזון';
      }
    });

     // Initial state update to set initial arrow/zone styles
     updateChainState();

     // Adjust explanation button text initially if explanation is visible by default (though it's hidden by class)
     if (!explanationContent.classList.contains('hidden')) {
         explanationButton.textContent = 'הסתר הסבר';
     }


  });
</script>