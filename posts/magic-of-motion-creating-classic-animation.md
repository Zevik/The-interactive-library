---
title: "קסם התנועה: יצירת סרט אנימציה קלאסי"
english_slug: magic-of-motion-creating-classic-animation
category: "אמנות ועיצוב / אמנות דיגיטלית"
tags:
  - אנימציה
  - אנימציה קלאסית
  - צלולואיד
  - תהליך יצירה
  - קולנוע
---
<h1>קסם התנועה: איך מפיחים חיים בציורים?</h1>
<p class="subtitle">הצצה לעולם הקסום של האנימציה הקלאסית, שבו כל תנועה הייתה מלאכת יד מדויקת ומרובת שכבות. גלו את הסוד מאחורי האשליה שגרמה לדמויות האהובות עלינו לקפץ, לרקוד ולרוץ על המסך!</p>

<div id="animation-app" class="interactive-module">
    <h2>בואו נרכיב את הסצנה!</h2>
    <p class="instructions">כדי ליצור תנועה, עלינו לסדר את השכבות השקופות (הנקראות 'צלולואידים') בסדר הנכון מעל הרקע הקבוע. גררו את שכבות הצלולואיד מפס האוסף למטה, אל המקומות המיועדים בשורה העליונה. כשתסיימו לסדר, לחצו "צפו בקסם!"</p>

    <div id="animation-area">
        <div id="background" class="scene-layer">
            <span class="layer-label">רקע קבוע</span>
        </div>
        <div id="sequence-slots" class="drop-area">
            <div class="cel-slot drop-target" data-slot-index="0">
                <span class="slot-label">פריים 1</span>
            </div>
            <div class="cel-slot drop-target" data-slot-index="1">
                <span class="slot-label">פריים 2</span>
            </div>
            <div class="cel-slot drop-target" data-slot-index="2">
                <span class="slot-label">פריים 3</span>
            </div>
            <div class="cel-slot drop-target" data-slot-index="3">
                <span class="slot-label">פריים 4</span>
            </div>
        </div>
        <div id="animated-preview" class="scene-layer">
            <!-- Cloned cel images will be placed and animated here -->
        </div>
    </div>

    <div id="cel-selection" class="drag-area drop-target">
        <p class="area-label">פס האוסף</p>
        <div class="cel-container">
            <div class="draggable-cel cel-card" data-cel-id="cel-4" draggable="true">
                <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48Y2lyY2xlIGN4PSI4MCIgY3k9IjUwIiByPSIxNSIgZmlsbD0iIzM0OWFkYiIvPjwvc3ZnPg==" alt="Cel 4 - כדור ימין">
                <span class="cel-label">שכבה 4</span>
            </div>
            <div class="draggable-cel cel-card" data-cel-id="cel-2" draggable="true">
                <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48Y2lyY2xlIGN4PSI1MCIgY3k9IjUwIiByPSIxNSIgZmlsbD0iIzM0OWFkYiIvPjwvc2NnPg==" alt="Cel 2 - כדור מרכז-שמאל">
                 <span class="cel-label">שכבה 2</span>
            </div>
            <div class="draggable-cel cel-card" data-cel-id="cel-1" draggable="true">
                <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48Y2lyY2xlIGN4PSIzMCIgY3k9IjUwIiByPSIxNSIgZmlsbD0iIzM0OWFkYiIvPjwvc3ZnPg==" alt="Cel 1 - כדור שמאל">
                 <span class="cel-label">שכבה 1</span>
            </div>
            <div class="draggable-cel cel-card" data-cel-id="cel-3" draggable="true">
                <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48Y2lyY2xlIGN4PSI2NSIgY3k9IjUwIiByPSIxNSIgZmlllD0iIzM0OWFkYiIvPjwvc3ZnPg==" alt="Cel 3 - כדור מרכז-ימין">
                 <span class="cel-label">שכבה 3</span>
            </div>
        </div>
    </div>

    <div id="controls">
        <button id="play-button" class="interactive-button primary">צפו בקסם!</button>
        <p id="message" class="feedback-message"></p>
    </div>
</div>

<button id="toggle-explanation" class="interactive-button secondary">גלו את הסוד: קראו עוד על אנימציה קלאסית</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2>מהי אנימציה קלאסית (אנימציית צלולואיד)?</h2>
    <p>לפני עידן הקסמים הדיגיטליים, עולם האנימציה נברא באמצעות עבודת יד קפדנית, פריים אחר פריים. שיטת "צלולואיד" הייתה הלב הפועם של אולפנים כמו דיסני, ומפיחה חיים במיליוני ציורים סטטיים.</p>

    <h2>המרכיבים הסודיים: רקעים ושכבות שקופות</h2>
    <p>כל סצנה קלאסית היא יצירת פאזל מורכבת: שכבת <strong>רקע</strong> יחידה, ציור קבוע של הסביבה (יער, חדר, עיר), ומעליה מונחות בזהירות שכבות <strong>צלולואיד</strong>. הצלולואיד הוא יריעת פלסטיק שקופה לחלוטין, שעליה צוירו הדמויות הנעות או אובייקטים משתנים. הקסם נוצר כשמניחים כמה צלולואידים זה על זה - הצופה רואה דרכם את כל השכבות יחד, כולל הרקע שמתחת, כאילו היו ציור אחד שלם!</p>

    <h2>מסע היצירה: משריטה על נייר לתנועה על המסך</h2>
    <p>הדרך אל הסרט המוגמר הייתה ארוכה ומרתקת:
        <br><strong>תכנון קפדני:</strong> סטוריבורד מפורט, עיצוב דמויות ואיתור התנועות המרכזיות ('קי-פריימס').
        <br><strong>אמנות התנועה:</strong> אנימטורים מומחים ציירו את תנועות המפתח, ואמני 'אינביטואין' מילאו את הפערים בציורים מדויקים שבין תנועה לתנועה, כדי שהתנועה תיראה חלקה וטבעית.
        <br><strong>מעבר לצלולואיד:</strong> קווי המתאר של הדמויות הועתקו ביד מנייר לצלולואידים בעזרת דיו מיוחד (שלב ה-'Inking').
        <br><strong>הצבעה קסומה:</strong> הצד האחורי של הצלולואידים נצבע בצבעים אטומים, שהפיחו חיים בצורות וקווי המתאר.</p>

    <h2>רגע האמת: צילום הפרימים</h2>
    <p>כאשר כל הצלולואידים לפריים מסוים (תמונה בודדת בסרט) היו מוכנים, הם סודרו על כן צילום מיוחד, אחד מעל השני ומעל הרקע. מצלמה ענקית צילמה תמונה יחידה של כל הערימה. התהליך חזר על עצמו שוב ושוב, עבור כל 24 פרימים של כל שנייה בסרט! בעידן המודרני, הסריקה הדיגיטלית החליפה את הצילום על פילם.</p>

    <h2>הסוד לאשליה: רצף מהיר</h2>
    <p>המוח האנושי "מתעתע" בנו: כשאנחנו רואים רצף מהיר של תמונות סטטיות שמשתנות מעט מאוד ביניהן (24 פרימים בשנייה, למשל), אנחנו מפרשים את השינויים כתנועה חלקה ורציפה. זו האשליה שמאפשרת לקסם לקרות!</p>

    <h2>היקף העבודה: סיזיפוס עם מכחולים</h2>
    <p>יצירת סרט אנימציה קלאסי הייתה פרויקט ענק ומונומנטלי. דקה אחת בלבד של סרט דרשה ציור וצביעה של 1440 פרימים, כשכל פריים מורכב ממספר שכבות צלולואיד שונות. זה דרש צוותי אמנים ענקיים שעבדו ללא הפסקה במשך שנים על סרט אחד. הערכה: כ-10-15 צלולואידים שימשו בממוצע לכל פריים בסרטים הגדולים!</p>
</div>

<style>
    :root {
        --primary-color: #3498db; /* Blue */
        --secondary-color: #9b59b6; /* Purple */
        --success-color: #2ecc71; /* Green */
        --error-color: #e74c3c; /* Red */
        --background-light: #ecf0f1; /* Light Grey */
        --surface-color: #ffffff; /* White */
        --border-color: #bdc3c7; /* Lighter Grey */
        --text-color: #34495e; /* Dark Blue Grey */
        --soft-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        --hover-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        --transition-duration: 0.3s;
    }

    /* General Styles */
    #animation-app {
        direction: rtl;
        font-family: 'Arial', sans-serif; /* Use a common sans-serif font */
        max-width: 850px; /* Slightly wider */
        margin: 20px auto;
        background-color: var(--background-light);
        border-radius: 12px; /* More rounded corners */
        padding: 30px; /* More padding */
        box-shadow: var(--soft-shadow);
        color: var(--text-color);
        line-height: 1.6;
    }

    h1 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 10px;
        font-size: 2em; /* Larger heading */
    }

     .subtitle {
         text-align: center;
         margin-bottom: 30px;
         color: #555; /* Slightly darker than main text color */
         font-size: 1.1em;
     }

    h2 {
        color: var(--text-color);
        margin-top: 20px;
        margin-bottom: 15px;
        font-size: 1.5em;
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 5px;
    }

     .instructions {
         margin-bottom: 20px;
         font-size: 1.05em;
         color: #555;
     }


    /* Animation Area (Scene) */
    #animation-area {
        position: relative;
        width: 100%;
        height: 300px; /* Increased height for scene */
        border: 2px solid var(--border-color);
        margin-bottom: 25px;
        border-radius: 8px;
        overflow: hidden;
        background: linear-gradient(to bottom, #87ceeb 0%, #e0f2f7 50%, var(--success-color) 50%, var(--success-color) 100%); /* Sky to ground gradient */
        box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.1);
    }

     #background {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 50%; /* Ground covers bottom half */
        background-color: transparent; /* Background is handled by parent gradient */
        z-index: 1;
        display: flex; /* Use flex for label */
        justify-content: center;
        align-items: flex-end; /* Align label to bottom */
         padding-bottom: 10px;
     }
      #background .layer-label {
          color: var(--surface-color);
          background-color: rgba(0, 0, 0, 0.3);
          padding: 3px 8px;
          border-radius: 4px;
          font-size: 0.8em;
      }


    #sequence-slots {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 50%; /* Slots cover top half (sky area) */
        display: flex;
        justify-content: space-around;
        align-items: center;
        padding: 10px 0;
        z-index: 2; /* Slots above background ground part */
        box-sizing: border-box;
         background-color: rgba(255, 255, 255, 0.2); /* Slight transparency for slot area */
    }

    .cel-slot {
        width: 20%; /* Adjust width for better spacing */
        height: 95%; /* Fill available height */
        border: 2px dashed rgba(var(--text-color), 0.5); /* More prominent dashed border */
        border-radius: 8px;
        text-align: center;
        color: var(--text-color);
        font-size: 0.9em;
        background-color: rgba(var(--surface-color), 0.5); /* Semi-transparent white background */
        position: relative;
        box-sizing: border-box;
        padding-top: 10px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        transition: background-color var(--transition-duration), border-color var(--transition-duration);
         overflow: hidden; /* Hide cel image overflow */
    }
     .cel-slot .slot-label {
         opacity: 0.8;
         font-weight: bold;
     }

    .cel-slot.drag-over {
        background-color: rgba(var(--primary-color), 0.3); /* Highlight on drag over */
        border-color: var(--primary-color);
        transform: scale(1.05); /* Subtle scale effect */
    }

    /* Cel Selection Area */
    #cel-selection {
        display: flex;
        justify-content: center;
        gap: 20px; /* More space between cels */
        margin-bottom: 25px;
        padding: 20px;
        border: 1px dashed var(--border-color);
        background-color: var(--surface-color);
        min-height: 120px; /* Ensure area is substantial */
        align-items: center;
        flex-wrap: wrap;
        border-radius: 8px;
        box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.05);
        position: relative; /* Needed for area-label */
    }
     #cel-selection .area-label {
        position: absolute;
        top: 5px;
        right: 10px;
        font-size: 0.8em;
        color: #777;
     }
      #cel-selection .cel-container {
          display: flex;
          justify-content: center;
          gap: 20px;
          flex-wrap: wrap;
      }


    .draggable-cel {
        width: 80px; /* Larger draggable cels */
        height: 80px;
        border: 1px solid var(--border-color);
        background-color: rgba(var(--surface-color), 0.9); /* Almost opaque white */
        border-radius: 8px; /* Rounded corners for cels */
        cursor: grab;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        font-size: 0.9em;
        position: relative;
        box-sizing: border-box;
        padding: 8px; /* More padding */
        transition: transform var(--transition-duration), box-shadow var(--transition-duration);
        box-shadow: var(--soft-shadow);
    }
    .draggable-cel:hover {
         transform: translateY(-5px); /* Lift slightly on hover */
         box-shadow: var(--hover-shadow);
    }
     .draggable-cel.dragging {
         opacity: 0.5; /* Make the original element semi-transparent while dragging */
         transform: scale(0.9); /* Slightly shrink while dragging */
         box-shadow: none;
     }

    .draggable-cel img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
        pointer-events: none; /* Critical for drag and drop */
        display: block;
        margin-bottom: 5px; /* Space between image and label */
    }
     .cel-label {
         font-size: 0.8em; /* Smaller label */
         color: #555;
         font-weight: bold;
     }

    /* Styling for the cel once dropped into a slot */
    .cel-slot .draggable-cel {
        width: 100%; /* Fill the slot */
        height: 100%;
        border: none;
        background-color: transparent;
        position: absolute; /* Position absolutely within the slot */
        top: 0;
        left: 0;
        cursor: default;
        padding: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        /* The image inside needs to be positioned to look like it's on the ground */
        justify-content: flex-end; /* Align cel image to the bottom of the slot */
        z-index: 3; /* Cels above background */
        box-shadow: none; /* Remove shadow when in slot */
         transition: none; /* No transform/shadow transition in slot */
    }
     .cel-slot .draggable-cel img {
         max-width: 80%; /* Image smaller in slot */
         max-height: 80%;
         object-fit: contain;
         pointer-events: none;
         display: block;
         margin-bottom: 0; /* No margin below image in slot */
     }
      .cel-slot .cel-label {
          display: none; /* Hide label when in slot */
      }
       .cel-slot .slot-label {
           display: none; /* Hide slot label when a cel is placed */
       }


    /* Animation Preview Area - Contains images to be animated */
    #animated-preview {
        position: absolute;
        top: 50%; /* Position relative to the top edge of the ground area */
        left: 0;
        width: 100%;
        height: 50%; /* Covers the ground area where animation happens */
        z-index: 4;
        pointer-events: none;
        overflow: hidden;
    }
     #animated-preview img {
         position: absolute;
         bottom: 10px; /* Position slightly above the very bottom of the ground */
         transform: translateX(-50%); /* Center horizontally based on image's own width */
         max-height: 80%;
         object-fit: contain;
         display: none; /* Hidden by default */
         /* Positioning properties will be set by JS */
         /* transition: opacity 0.05s linear; /* Add a small transition for smoother frame changes */
     }

    /* Controls */
    #controls {
        text-align: center;
        margin-top: 25px;
    }

    .interactive-button {
        padding: 12px 25px; /* Larger padding */
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px; /* Slightly more rounded */
        margin: 0 10px 15px; /* Space between buttons, bottom margin */
        transition: background-color var(--transition-duration), transform 0.1s ease-in-out, box-shadow var(--transition-duration);
         font-weight: bold;
         box-shadow: var(--soft-shadow);
    }
     .interactive-button.primary {
         background-color: var(--primary-color);
         color: white;
     }
     .interactive-button.primary:hover {
         background-color: #2980b9; /* Darker blue */
         transform: translateY(-2px);
         box-shadow: var(--hover-shadow);
     }
      .interactive-button.secondary {
          background-color: var(--border-color);
          color: var(--text-color);
      }
       .interactive-button.secondary:hover {
           background-color: #b0b6ba; /* Darker grey */
           transform: translateY(-2px);
           box-shadow: var(--hover-shadow);
       }


    .feedback-message {
        min-height: 1.5em; /* Reserve space */
        font-weight: bold;
        margin-top: 10px;
        color: var(--success-color); /* Default success color */
         text-align: center;
    }
     .feedback-message.error {
         color: var(--error-color);
     }


    /* Explanation Section */
    #toggle-explanation {
        display: block;
        margin: 30px auto 20px; /* More margin */
         box-shadow: var(--soft-shadow);
    }
     #toggle-explanation:hover {
          box-shadow: var(--hover-shadow);
     }


    .explanation-section {
        margin-top: 30px;
        padding: 30px; /* More padding */
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--surface-color);
        box-shadow: var(--soft-shadow);
    }
    .explanation-section h2 {
        color: var(--primary-color); /* Explanation headings use primary color */
        margin-top: 0; /* No top margin if it's the first element */
        border-bottom-color: var(--primary-color); /* Match border color */
    }
    .explanation-section p {
        line-height: 1.7; /* More space between lines */
        color: var(--text-color);
        margin-bottom: 20px;
    }
     .explanation-section p strong {
         color: var(--secondary-color); /* Highlight key terms */
     }

     /* Ensure drop area is visually distinct and clickable */
     .drop-area {
         /* Add styles */
     }
     .drag-area {
         /* Add styles */
     }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const celSelectionArea = document.getElementById('cel-selection');
        const celContainer = celSelectionArea.querySelector('.cel-container'); // Select the container within the selection area
        const slots = document.querySelectorAll('.cel-slot');
        const playButton = document.getElementById('play-button');
        const messageDiv = document.getElementById('message');
        const animatedPreview = document.getElementById('animated-preview');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        let draggedCel = null;
        // The correct order corresponds to the ball moving from left to right based on original SVG cx
        const correctOrder = ["cel-1", "cel-2", "cel-3", "cel-4"];
        // Map cel-id to a relative horizontal position (left percentage) in the preview area
        const celPositions = {
            "cel-1": "15%", // Based on cx=30
            "cel-2": "35%", // Based on cx=50
            "cel-3": "55%", // Based on cx=65
            "cel-4": "75%"  // Based on cx=80
        };

        const placedCels = {}; // Store which cel-id is in which slot-index { slotIndex: celId, ... }

        // --- Drag and Drop Logic ---

        // Make cels draggable
        const draggableCels = document.querySelectorAll('.draggable-cel');
        draggableCels.forEach(cel => {
            cel.addEventListener('dragstart', (event) => {
                draggedCel = event.target;
                event.dataTransfer.setData('text/plain', event.target.dataset.celId);
                event.dataTransfer.effectAllowed = 'move'; // Visual cue for move operation

                // Add a class to indicate dragging, hide original slightly
                setTimeout(() => {
                    draggedCel.classList.add('dragging');
                }, 0); // Timeout allows browser to capture the drag image before hiding
            });

             cel.addEventListener('dragend', () => {
                 // Remove dragging class from the original element
                 if(draggedCel) {
                    draggedCel.classList.remove('dragging');
                    draggedCel = null; // Reset draggedCel
                 }
             });
        });

        // Make slots drop targets
        slots.forEach(slot => {
            slot.addEventListener('dragover', (event) => {
                event.preventDefault(); // Necessary to allow dropping
                event.dataTransfer.dropEffect = 'move'; // Visual cue
                 slot.classList.add('drag-over'); // Visual cue
            });

            slot.addEventListener('dragleave', () => {
                 slot.classList.remove('drag-over'); // Remove visual cue
            });

            slot.addEventListener('drop', (event) => {
                event.preventDefault();
                 slot.classList.remove('drag-over'); // Remove visual cue

                const celId = event.dataTransfer.getData('text/plain');
                const droppedCel = document.querySelector(`.draggable-cel[data-cel-id="${celId}"]`);
                const slotIndex = parseInt(slot.dataset.slotIndex);

                if (droppedCel) {
                    // Check if the slot already contains a cel
                    const existingCelInSlot = slot.querySelector('.draggable-cel');

                    if (existingCelInSlot) {
                       // If slot has a cel, move it back to the selection area
                       celContainer.appendChild(existingCelInSlot);
                       // Remove it from placedCels tracking
                       for(const idx in placedCels) {
                           if(placedCels[idx] === existingCelInSlot.dataset.celId) {
                               delete placedCels[idx];
                               break;
                           }
                       }
                    }

                    // Append the dragged cel to the current slot
                    slot.appendChild(droppedCel);
                     // Add a class to indicate it's in a slot for styling
                    droppedCel.classList.add('in-slot');


                    // Store the placement
                    placedCels[slotIndex] = celId;

                     messageDiv.textContent = ''; // Clear message on placement change
                     resetPreview(); // Reset preview state
                }
                // dragend handler will reset draggedCel and remove '.dragging'
            });
        });

         // Handle dropping a cel back onto the selection area
         celSelectionArea.addEventListener('dragover', (event) => {
              event.preventDefault(); // Allow drop
              event.dataTransfer.dropEffect = 'move';
              celSelectionArea.classList.add('drag-over'); // Visual cue for selection area
         });
         celSelectionArea.addEventListener('dragleave', () => {
             celSelectionArea.classList.remove('drag-over');
         });

         celSelectionArea.addEventListener('drop', (event) => {
             event.preventDefault();
             celSelectionArea.classList.remove('drag-over');

             const celId = event.dataTransfer.getData('text/plain');
             const droppedCel = document.querySelector(`.draggable-cel[data-cel-id="${celId}"]`);

             // Check if the dropped cel is coming from a slot (i.e., its parent is a cel-slot)
             if (droppedCel && droppedCel.parentElement && droppedCel.parentElement.classList.contains('cel-slot')) {
                const oldSlot = droppedCel.parentElement;

                // Move the cel back to the selection area container
                celContainer.appendChild(droppedCel);
                // Remove the 'in-slot' class
                droppedCel.classList.remove('in-slot');

                // Remove the cel from placedCels based on its original slot index
                const oldSlotIndex = parseInt(oldSlot.dataset.slotIndex);
                if(placedCels[oldSlotIndex] === celId) {
                    delete placedCels[oldSlotIndex];
                }

                 messageDiv.textContent = ''; // Clear message
                 resetPreview(); // Reset preview
             }
             // dragend handler will reset draggedCel and remove '.dragging'
         });


        // --- Animation and Control Logic ---

        // Play button logic
        playButton.addEventListener('click', () => {
            // Check if all slots are filled
            if (Object.keys(placedCels).length !== slots.length) {
                messageDiv.textContent = 'רגע, חסרות שכבות! גררו את כל 4 השכבות למקומות המיועדים.';
                messageDiv.className = 'feedback-message error';
                resetPreview();
                return;
            }

            // Get the order from the slots based on their index
            const currentOrder = Array.from(slots)
                .sort((a, b) => parseInt(a.dataset.slotIndex) - parseInt(b.dataset.slotIndex)) // Ensure order is by slot index 0, 1, 2, 3
                .map(slot => {
                     const cel = slot.querySelector('.draggable-cel');
                     return cel ? cel.dataset.celId : null; // Get celId or null
                 });

             // Double check: if any slot is empty (shouldn't happen due to first check, but good practice)
             if(currentOrder.some(id => id === null)) {
                 messageDiv.textContent = 'שגיאה בהרכבה. נסו לסדר מחדש.';
                 messageDiv.className = 'feedback-message error';
                 resetPreview();
                 return;
             }

            // Check if the order is correct
            const isCorrect = currentOrder.every((id, index) => id === correctOrder[index]);

            if (isCorrect) {
                messageDiv.textContent = 'מעולה! הסדר נכון! צפו בקסם התנועה!';
                messageDiv.className = 'feedback-message'; // Default success class
                animateSequence(currentOrder); // Run the animation
            } else {
                messageDiv.textContent = 'אופס! הסדר שגוי. נסו לסדר את השכבות שוב כדי ליצור תנועה חלקה.';
                messageDiv.className = 'feedback-message error';
                resetPreview();
            }
        });

        // Animation function
        let animationTimer = null; // Keep track of the animation timer
        const frameDuration = 150; // Milliseconds per frame (adjust for speed)
        const loopCount = 3; // How many times to loop the animation

        function animateSequence(order) {
            resetPreview(); // Hide all preview images initially

            let frameIndex = 0;
            let currentLoop = 0;

            function showNextFrame() {
                // Hide all images in the preview area
                animatedPreview.querySelectorAll('img').forEach(img => img.style.display = 'none');

                if (currentLoop < loopCount) {
                    if (frameIndex < order.length) {
                        const celIdToShow = order[frameIndex];
                        // Find the corresponding image in the animatedPreview area
                        const imgToShow = animatedPreview.querySelector(`img[data-cel-id="${celIdToShow}"]`);

                        if (imgToShow) {
                            imgToShow.style.display = 'block'; // Show current frame
                            // Positioning is already set by setupPreviewImages
                        } else {
                             console.error(`Preview image not found for celId: ${celIdToShow}`);
                        }

                        frameIndex++;
                        animationTimer = setTimeout(showNextFrame, frameDuration); // Schedule next frame

                    } else {
                        // End of one sequence pass
                        currentLoop++;
                        if (currentLoop < loopCount) {
                            frameIndex = 0; // Reset index for the next loop
                             // Add a small delay before restarting the loop visually
                            animationTimer = setTimeout(showNextFrame, frameDuration * 2);
                        } else {
                            // Animation finished after all loops
                             messageDiv.textContent = 'האנימציה הסתיימה!'; // Final message after animation
                            // Keep the last frame visible for a moment, then hide
                             setTimeout(resetPreview, frameDuration * 3); // Hide after a short delay
                        }
                    }
                } else {
                     // Animation finished (redundant check, but safe)
                     messageDiv.textContent = 'האנימציה הסתיימה!';
                     setTimeout(resetPreview, frameDuration * 3);
                }
            }

            // Stop any ongoing animation before starting a new one
            if (animationTimer) {
                clearTimeout(animationTimer);
            }
            showNextFrame(); // Start the animation loop
        }

        function resetPreview() {
             // Hide all images in the preview area
            animatedPreview.querySelectorAll('img').forEach(img => {
                img.style.display = 'none';
            });
             // Clear the "ended" message if any, unless it's a new error/success message
            if (!messageDiv.classList.contains('error') && messageDiv.textContent.includes('הסתיימה')) {
                 messageDiv.textContent = '';
            }
        }

        // --- Explanation Toggle Logic ---
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתירו את ההסבר על אנימציה קלאסית' : 'גלו את הסוד: קראו עוד על אנימציה קלאסית';
             // Optional: Scroll to the explanation section after opening
             if (isHidden) {
                 explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
             }
        });

         // --- Initial Setup ---

         // Clone images to the animatedPreview area and position them absolutely
         function setupPreviewImages() {
             // Clear existing preview images
             animatedPreview.innerHTML = '';

             draggableCels.forEach(cel => {
                 const celId = cel.dataset.celId;
                 const celImg = cel.querySelector('img').cloneNode(true);
                 celImg.dataset.celId = celId; // Copy data attribute
                 celImg.style.position = 'absolute';
                 celImg.style.bottom = '10px'; // Position slightly above the ground
                 // Set horizontal position based on the defined mapping
                 celImg.style.left = celPositions[celId];
                 celImg.style.transform = 'translateX(-50%)'; // Center horizontally based on the left position
                 celImg.style.display = 'none'; // Hide initially
                 animatedPreview.appendChild(celImg);
             });
         }

         // Run initial setup
         setupPreviewImages();
         resetPreview(); // Ensure initial state is clean

    });
</script>
---