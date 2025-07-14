---
title: "פוטוסינתזה: הקסם הירוק שנותן חיים"
english_slug: photosynthesis-plants-secret-kitchen
category: "ביולוגיה"
tags:
  - פוטוסינתזה
  - צמחים
  - אנרגיה
  - ביולוגיה
  - אינטראקטיבי
  - קסם
---

<p>האם עצרתם פעם לחשוב איך צמחים בעצם שורדים וגדלים? אין להם פה לאכול, רגליים לצוד, או כרטיס אשראי לסופר. אז איך הם מייצרים את כל האנרגיה והחומרים שהם צריכים? בואו נגלה את המטבח הסודי והקסום שלהם – הפוטוסינתזה!</p>

<div id="photosynthesis-app">
    <div class="app-container">
        <div class="ingredients">
             <h3>הכניסו למטבח:</h3>
            <div class="ingredient" id="water">💧<span class="label">מים (H₂O)</span></div>
            <div class="ingredient" id="co2">💨<span class="label">פחמן דו-חמצני (CO₂)</span></div>
            <div class="ingredient" id="light">☀️<span class="label">אור שמש</span></div>
        </div>

        <div class="plant-area">
             <!-- Replace with a visually appealing plant image -->
            <img src="https://raw.githubusercontent.com/Schrodinger-Hat/interactive-assets/main/plant.svg" alt="ציור של צמח" id="plant">
            <!-- Drop zones - made subtle/invisible until drag -->
            <div class="drop-zone water-zone" id="water-zone"></div> <!-- Root zone -->
            <div class="drop-zone co2-zone" id="co2-zone"></div>   <!-- Leaf zone -->
            <div class="drop-zone light-zone" id="light-zone"></div> <!-- General plant zone -->
             <div class="animation-layer"></div> <!-- For process animations like light rays or particles -->
        </div>

        <div class="products">
            <h3>יצא מהמטבח:</h3>
            <div class="product" id="glucose">🍬<span class="label">סוכר (גלוקוז)</span></div>
            <div class="product" id="oxygen">🎈<span class="label">חמצן (O₂)</span></div>
        </div>
    </div>
    <div class="message-area">גררו את "המצרכים" אל הצמח כדי להתחיל בפוטוסינתזה!</div>
</div>

<style>
    #photosynthesis-app {
        font-family: 'Heebo', sans-serif; /* Use a modern Hebrew-friendly font */
        max-width: 800px;
        margin: 20px auto;
        padding: 25px;
        border: none; /* Remove basic border */
        border-radius: 12px; /* Softer corners */
        background: linear-gradient(to bottom right, #e0f2f7, #e8f5e9); /* Light, fresh gradient */
        box-shadow: 0 8px 16px rgba(0,0,0,0.1); /* Softer, larger shadow */
        direction: rtl;
        text-align: right;
        position: relative; /* For potential absolute children */
         overflow: hidden; /* Hide overflow from animations */
    }

     #photosynthesis-app h3 {
         text-align: center;
         color: #2e7d32; /* Dark green */
         margin-top: 0;
         font-size: 1.3em;
         margin-bottom: 20px;
     }

    .app-container {
        display: flex;
        justify-content: space-around;
        align-items: flex-start;
        flex-wrap: wrap;
        gap: 20px; /* Add space between columns */
    }

    .ingredients, .products {
        flex: 1;
        min-width: 180px; /* Slightly wider minimum */
        padding: 15px;
        background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white */
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
        text-align: center;
         border: 1px solid rgba(0,0,0,0.05);
    }

     .products {
         background-color: rgba(255, 255, 230, 0.8); /* Light yellow tint for products */
     }

    .plant-area {
        flex: 2;
        min-width: 300px;
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        min-height: 400px; /* More height for larger plant */
        justify-content: center; /* Center plant vertically */
    }

     #plant {
        display: block;
        width: 100%; /* Make plant image responsive within its container */
        max-width: 300px; /* Max size */
        height: auto;
        z-index: 5; /* Ensure plant is above zones */
        filter: drop-shadow(4px 4px 8px rgba(0,0,0,0.1)); /* Subtle shadow for depth */
     }

    .drop-zone {
        position: absolute;
        border: none; /* No visible border normally */
        background-color: rgba(0, 128, 0, 0); /* Fully transparent */
        z-index: 1; /* Below plant image */
        transition: background-color 0.3s ease, border-color 0.3s ease;
        pointer-events: none; /* Do not interfere with plant image interaction */
         border-radius: 50%; /* Make zones roundish */
    }

     .water-zone {
        width: 100px;
        height: 70px;
        bottom: 20px; /* Position near roots */
        left: 50%;
        transform: translateX(-50%);
         border-radius: 20px; /* More root-like shape */
     }

    .co2-zone {
        width: 120px;
        height: 80px;
        top: 80px; /* Position near leaves */
        left: 50%;
        transform: translateX(-50%);
         border-radius: 50%/20px; /* Leaf-like shape */
     }
     .light-zone {
        width: 200px;
        height: 300px;
        top: 0px; /* Position over the whole plant */
        left: 50%;
        transform: translateX(-50%);
         border-radius: 20% 20% 10% 10%; /* Shape covering top of plant */
     }


    .drop-zone.highlight {
        background-color: rgba(144, 238, 144, 0.3); /* Light green highlight */
        border: 2px dashed #2e7d32; /* Dark green dashed border */
    }
    .drop-zone.highlight.light-zone {
         background-color: rgba(255, 255, 0, 0.3); /* Yellow highlight for light */
         border: 2px dashed #fbc02d; /* Dark yellow dashed border */
    }


    .ingredient, .product {
        padding: 12px;
        margin: 10px auto;
        cursor: grab;
        border: 1px solid #b0bec5; /* Light grey border */
        border-radius: 8px;
        background-color: #ffffff;
        text-align: center;
        width: fit-content;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); /* Improved shadow */
        position: relative;
        z-index: 10;
        transition: transform 0.2s ease, box-shadow 0.2s ease, opacity 0.5s ease;
    }

    .ingredient:active {
        cursor: grabbing;
        transform: scale(1.1); /* Pop out slightly on drag */
        box-shadow: 0 8px 12px rgba(0,0,0,0.2);
    }

    .ingredient .label, .product .label {
        margin-right: 8px; /* Space between emoji and text */
         font-weight: bold;
         color: #455a64; /* Dark grey text */
    }
     .ingredient > span:first-child, .product > span:first-child {
         font-size: 1.5em; /* Larger emoji */
         vertical-align: middle;
     }

    .products-label {
        font-weight: bold;
        margin-bottom: 10px;
        font-size: 1.1em;
    }

    .product {
        opacity: 0; /* Start hidden */
        pointer-events: none;
        transition: opacity 0.8s ease, transform 0.8s ease; /* Smooth appearance */
         background-color: #fff9c4; /* Light yellow */
         border-color: #fbc02d; /* Darker yellow border */
         transform: translateY(20px); /* Start slightly lower */
    }

    .product.visible {
        opacity: 1;
        transform: translateY(0); /* Slide up to final position */
    }

    .message-area {
        text-align: center;
        margin-top: 25px;
        font-size: 1.3em; /* Slightly larger */
        color: #004d40; /* Teal color */
         min-height: 1.8em; /* Reserve more space */
         font-weight: bold;
    }

    /* Animation Layer for effects like light rays or internal process */
    .animation-layer {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: 6; /* Above plant, below ingredients */
        pointer-events: none;
        overflow: hidden; /* Crucial for particle effects */
    }

    /* Styles for ingredient animation */
    .ingredient.animating {
        position: absolute !important; /* Override drag position */
        transition: all 1.5s ease-in; /* Animation duration and timing */
        z-index: 100; /* Stay on top during animation */
    }

     /* Styles for internal process animation */
     @keyframes lightPulse {
         0% { box-shadow: 0 0 10px 5px rgba(255, 255, 0, 0.4); }
         50% { box-shadow: 0 0 20px 10px rgba(255, 255, 0, 0.7); }
         100% { box-shadow: 0 0 10px 5px rgba(255, 255, 0, 0.4); }
     }

     .plant-area.processing #plant {
         animation: lightPulse 2s ease-in-out infinite; /* Pulsing light effect on the plant */
     }


    #explanation-button {
        display: block;
        margin: 30px auto 20px auto; /* More space */
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #4caf50; /* Green button */
        color: white;
        border: none;
        border-radius: 6px;
        text-align: center;
        transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
     #explanation-button:hover {
         background-color: #388e3c; /* Darker green on hover */
     }
     #explanation-button:active {
         transform: scale(0.98); /* Press effect */
         box-shadow: none;
     }

    #explanation-content {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #b2dfdb; /* Light teal border */
        border-radius: 8px;
        background-color: #e0f2f7; /* Light blue background */
        display: none;
        line-height: 1.6; /* Improve readability */
    }

    #explanation-content h2, #explanation-content h3 {
        color: #004d40; /* Dark teal */
        margin-bottom: 10px;
         text-align: right; /* Ensure RTL */
    }
     #explanation-content h2 {
        margin-top: 0;
        font-size: 1.4em;
     }
     #explanation-content h3 {
         font-size: 1.2em;
         margin-top: 15px;
     }
     #explanation-content ul {
        list-style: disc inside;
        padding-right: 20px;
        margin-bottom: 15px;
     }
     #explanation-content li {
        margin-bottom: 8px;
     }
     #explanation-content p {
         margin-bottom: 15px;
     }
      #explanation-content strong {
          color: #2e7d32; /* Green for emphasis */
      }

</style>

<button id="explanation-button">הצג/הסתר הסבר על הפוטוסינתזה</button>

<div id="explanation-content">
    <h2>פוטוסינתזה: הקסם הירוק שבלב הצמח</h2>
    <p>פוטוסינתזה (פוטוס = אור, סינתזה = הרכבה) היא תהליך מדהים המתרחש בצמחים, אצות וחיידקים מסוימים. זהו תהליך כימי שממיר את אנרגיית האור (בעיקר מהשמש) לאנרגיה כימית, אצורה במולקולות סוכר (גלוקוז). במילים פשוטות, זה הדרך של הצמח "לבשל" את המזון שלו!</p>

    <h3>למה פוטוסינתזה כל כך חשובה?</h3>
    <ul>
        <li>**מקור האנרגיה והמזון:** הפוטוסינתזה היא הבסיס של כמעט כל שרשרות המזון על פני כדור הארץ. הצמחים מייצרים את המזון שלהם, ויצורים אחרים (כולל אנחנו!) ניזונים מהצמחים הללו באופן ישיר או עקיף.</li>
        <li>**ייצור החמצן:** תוצר לוואי מדהים של הפוטוסינתזה הוא החמצן (O₂)! כל הנשימה שאנו נושמים, ורוב החמצן באטמוספירה, מגיעים אלינו בזכות הצמחים ויצורים פוטוסינתטיים אחרים. בלעדיהם, לא הייתה לנו אוויר לנשימה.</li>
    </ul>

    <h3>מה הצמח צריך למטבח הפוטוסינתזה? (מרכיבי הקסם)</h3>
    <ul>
        <li>💧 **מים (H₂O):** נקלט בעיקר דרך השורשים מהאדמה, ומטפס דרך הגבעול לעלים. דמיינו את זה כשתיית מים גדולה של הצמח.</li>
        <li>💨 **פחמן דו-חמצני (CO₂):** גז שנמצא באוויר שאנו נושמים ופולטים. הצמח "שואף" אותו דרך פתחים קטנים בעלים שנקראים פיוניות.</li>
        <li>☀️ **אנרגיית אור:** בעיקר מאור השמש. האור הזה נלכד בתוך ה"מטבחים הקטנים" בתאי הצמח, הנקראים כלורופלסטים. הכלורופלסטים מכילים חומר ירוק קסום בשם כלורופיל, שתפקידו "לתפוס" את אנרגיית האור. אנרגיית האור היא הדלק שמניע את כל התהליך.</li>
    </ul>

    <h3>מה נוצר במטבח? (התוצרים הקסומים)</h3>
    <ul>
        <li>🍬 **סוכר (גלוקוז - C₆H₁₂O₆):** זהו המזון של הצמח! הסוכר משמש אותו לאנרגיה מיידית (לגדול, לחיות) וגם נאגר בצורות אחרות (כמו עמילן או תאית) לבניין הגוף של הצמח או כמקור אנרגיה עתידי.</li>
        <li>🎈 **חמצן (O₂):** תוצר לוואי שמשתחרר מהעלים אל האוויר. מזל גדול בשבילנו!</li>
    </ul>

    <h3>הנוסחה הסודית של הקסם (המשוואה הכימית):</h3>
    <p>אפשר לסכם את התהליך במשוואה אלגנטית:</p>
    <p>6CO₂ (פחמן דו-חמצני) + 6H₂O (מים) + אנרגיית אור → C₆H₁₂O₆ (גלוקוז - סוכר) + 6O₂ (חמצן)</p>

    <h3>מי עוד עושה את הקסם הזה?</h3>
    <p>חוץ מצמחי היבשה שכולנו מכירים, גם:</p>
    <ul>
        <li>אצות (ירוקות, חומות ואדומות, בים וגם במים מתוקים).</li>
        <li>חיידקים מסוימים (כמו הציאנובקטריה הכחולות-ירוקות).</li>
    </ul>
    <p>כל אלה יחד הם הריאות הירוקות (והמכחלות הצבעוניות) של כדור הארץ, ומאפשרים את החיים כפי שאנחנו מכירים אותם!</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const ingredients = document.querySelectorAll('.ingredient');
        const dropZones = {
            water: document.getElementById('water-zone'),
            co2: document.getElementById('co2-zone'),
            light: document.getElementById('light-zone')
        };
        const products = document.querySelectorAll('.product');
        const messageArea = document.querySelector('.message-area');
        const plantArea = document.querySelector('.plant-area');
        const animationLayer = document.querySelector('.animation-layer'); // Use the animation layer

        let draggedItem = null;
        let offset = { x: 0, y: 0 };
        let successfullyDropped = {
            water: false,
            co2: false,
            light: false
        };
        let isProcessing = false; // Flag to prevent interaction during animation

        // Reset state
        function resetApp() {
             messageArea.textContent = 'גררו את "המצרכים" אל הצמח כדי להתחיל בפוטוסינתזה!';
             Object.keys(successfullyDropped).forEach(key => successfullyDropped[key] = false);
             products.forEach(product => product.classList.remove('visible'));
             ingredients.forEach(ing => {
                 // Restore original ingredient state (visuals and interactivity)
                 ing.style.position = 'relative';
                 ing.style.left = '0px';
                 ing.style.top = '0px';
                 ing.style.zIndex = '10';
                 ing.style.opacity = '1';
                 ing.style.cursor = 'grab';
                 ing.style.pointerEvents = 'auto';
                 ing.classList.remove('animating'); // Remove animation class if stuck
                 ing.style.transform = 'none'; // Reset transform from drag effect
             });

             // Clean up any lingering animation elements
             animationLayer.innerHTML = '';
             plantArea.classList.remove('processing');
             isProcessing = false;
        }

        // --- Drag functionality ---
        function startDrag(item, clientX, clientY) {
             if (isProcessing || item.style.pointerEvents === 'none') return; // Prevent drag during processing or if already used

             draggedItem = item;
             const rect = draggedItem.getBoundingClientRect();
             offset = {
                 x: clientX - rect.left,
                 y: clientY - rect.top
             };
             draggedItem.style.position = 'absolute';
             draggedItem.style.zIndex = 1000; // Bring to front
             draggedItem.style.transition = 'none'; // Disable transition while dragging
             draggedItem.classList.add('dragging'); // Optional: add dragging class for styling
        }

        function dragMove(clientX, clientY) {
             if (!draggedItem) return;

             const x = clientX - offset.x;
             const y = clientY - offset.y;

             // Constrain movement maybe? Or just let it float. Let's let it float for simplicity.
             draggedItem.style.left = x + 'px';
             draggedItem.style.top = y + 'px';

              // Highlight drop zone on hover
             Object.values(dropZones).forEach(zone => zone.classList.remove('highlight'));
             const targetZone = dropZones[draggedItem.id]; // Get the specific zone for the item
              if (targetZone && isOverlapping(draggedItem, targetZone, 0.5)) { // Check overlap with specific zone
                  targetZone.classList.add('highlight');
              } else if (draggedItem.id === 'light' && isOverlapping(draggedItem, document.getElementById('plant'), 0.3)) {
                   // Light can highlight the light zone even if dragged over the plant image
                   dropZones['light'].classList.add('highlight');
              } else if (draggedItem.id === 'water' && isOverlapping(draggedItem, dropZones.water, 0.5)) {
                   dropZones['water'].classList.add('highlight');
              } else if (draggedItem.id === 'co2' && isOverlapping(draggedItem, dropZones.co2, 0.5)) {
                   dropZones['co2'].classList.add('highlight');
              }
        }

         function endDrag(clientX, clientY) {
             if (!draggedItem) return;

             draggedItem.classList.remove('dragging');
             draggedItem.style.transition = ''; // Re-enable transition

             const elementBelow = document.elementFromPoint(clientX, clientY);
             handleDrop(draggedItem, elementBelow); // Pass item and elementBelow

             draggedItem = null;
             Object.values(dropZones).forEach(zone => zone.classList.remove('highlight')); // Remove highlight on drop
         }


        ingredients.forEach(item => {
            item.addEventListener('mousedown', (e) => {
                startDrag(item, e.clientX, e.clientY);
            });
             item.addEventListener('touchstart', (e) => {
                e.preventDefault(); // Prevent default touch behavior like scrolling
                const touch = e.touches[0];
                startDrag(item, touch.clientX, touch.clientY);
             }, { passive: false }); // Use passive: false to allow preventDefault
        });

        document.addEventListener('mousemove', (e) => {
            dragMove(e.clientX, e.clientY);
        });
         document.addEventListener('touchmove', (e) => {
             e.preventDefault(); // Prevent scrolling while dragging
             const touch = e.touches[0];
             dragMove(touch.clientX, touch.clientY);
         }, { passive: false });


        document.addEventListener('mouseup', (e) => {
            endDrag(e.clientX, e.clientY);
        });
         document.addEventListener('touchend', (e) => {
             // Find the element below the touch end position
             // This is tricky with touchend as e.clientX/Y might be off or not available directly.
             // A common workaround is to store the last touch position from touchmove
             // or use a library, but let's try elementFromPoint at the last touch pos recorded during move if possible,
             // or just rely on the current position if available.
             // For simplicity within constraints, we'll use the touch end coords directly, assuming they are close enough.
             const touch = e.changedTouches[0];
             endDrag(touch.clientX, touch.clientY);
         });


         // Check for overlap, with an optional threshold percentage
        function isOverlapping(element1, element2, threshold = 0.1) {
            if (!element1 || !element2) return false;
            const rect1 = element1.getBoundingClientRect();
            const rect2 = element2.getBoundingClientRect();

             // Calculate overlap area
            const overlapX = Math.max(0, Math.min(rect1.right, rect2.right) - Math.max(rect1.left, rect2.left));
            const overlapY = Math.max(0, Math.min(rect1.bottom, rect2.bottom) - Math.max(rect1.top, rect2.top));
            const overlapArea = overlapX * overlapY;

            // Calculate area of the dragged element
            const element1Area = rect1.width * rect1.height;

            // Check if overlap area is a significant percentage of the dragged element's area
            return element1Area > 0 && (overlapArea / element1Area) >= threshold;
        }


         function handleDrop(item, elementBelow) {
            const itemId = item.id;
            let droppedCorrectly = false;
            const targetZone = dropZones[itemId];

            // Check if dropped directly into the correct zone OR if the correct zone is highlighted (meaning it was over the zone during move)
            // Using the highlight check is more reliable for drop logic than just checking elementBelow
             const wasZoneHighlighted = targetZone && targetZone.classList.contains('highlight');


            if (wasZoneHighlighted && !successfullyDropped[itemId]) {
                 droppedCorrectly = true;
            }


            if (droppedCorrectly) {
                 successfullyDropped[itemId] = true;
                 messageArea.textContent = `${item.querySelector('.label').textContent} נקלט בהצלחה!`;

                 // Animate ingredient moving towards the plant/zone
                 const itemRect = item.getBoundingClientRect();
                 const plantRect = plantArea.getBoundingClientRect(); // Or specific zone rect

                 // Position item absolutely relative to the body or app container
                 item.style.position = 'absolute';
                 item.style.left = itemRect.left + 'px'; // Use current position
                 item.style.top = itemRect.top + 'px';
                 item.style.margin = '0'; // Remove margin influence
                 item.style.transition = 'all 1.5s ease-in, opacity 1.5s ease-in'; // Smooth animation
                 item.style.zIndex = 1000; // Keep on top

                 // Determine target point (e.g., center of the plant area or specific zone)
                 let targetX, targetY;
                  if (itemId === 'water') {
                       const zoneRect = dropZones.water.getBoundingClientRect();
                       targetX = zoneRect.left + zoneRect.width / 2;
                       targetY = zoneRect.top + zoneRect.height / 2;
                  } else if (itemId === 'co2') {
                       const zoneRect = dropZones.co2.getBoundingClientRect();
                        targetX = zoneRect.left + zoneRect.width / 2;
                        targetY = zoneRect.top + zoneRect.height / 2;
                  } else { // Light or general
                       // Aim towards the center-ish of the plant image
                       const plantImg = document.getElementById('plant');
                       const plantImgRect = plantImg.getBoundingClientRect();
                       targetX = plantImgRect.left + plantImgRect.width / 2;
                       targetY = plantImgRect.top + plantImgRect.height / 3; // Upper part for light
                  }


                 // Calculate the movement needed from current position to target position
                 // Need target relative to the *same* coordinate system as the item's absolute position (e.g., viewport)
                 const deltaX = targetX - itemRect.left;
                 const deltaY = targetY - itemRect.top;


                 // Trigger CSS animation
                 item.style.transform = `translate(${deltaX}px, ${deltaY}px) scale(0.5)`; // Move and shrink
                 item.style.opacity = '0'; // Fade out

                 item.style.cursor = 'default';
                 item.style.pointerEvents = 'none'; // Disable further dragging of this item instance

                 // Remove item from DOM after animation finishes
                 item.addEventListener('transitionend', () => {
                      // Keep the original item hidden but in place in the flow? Or truly remove?
                      // Let's just hide it and disable, keeping it in the original flex layout spot.
                      // To do this, we need to move it back to its original position *after* the animation,
                      // and then hide/disable. This is complex.
                      // Simpler: just make it invisible and pointer-events none, leave it positioned absolutely briefly.
                      // The reset function will handle putting it back correctly.
                       item.style.display = 'none'; // Hide it completely after animation

                      // Check if all required ingredients are dropped *after* this one's animation is done
                     if (successfullyDropped.water && successfullyDropped.co2 && successfullyDropped.light && !isProcessing) {
                          isProcessing = true;
                          messageArea.textContent = 'כל המרכיבים במטבח! מתחילים את קסם הפוטוסינתזה...';
                          startPhotosynthesisAnimation();
                      }
                 }, { once: true });


             } else { // Dropped incorrectly
                  messageArea.textContent = `אוופס! 🧐 גרור את "${item.querySelector('.label').textContent}" לאזור המתאים בצמח.`;
                  // Snap item back to its original position
                  // This requires knowing the original position before drag started, or calculating it
                  // based on its parent container. Let's simplify and just revert position/transform.
                   item.style.position = 'relative'; // Revert to flow positioning
                   item.style.left = '0px';
                   item.style.top = '0px';
                   item.style.transform = 'none'; // Reset transform from drag effect
                   item.style.zIndex = '10'; // Reset z-index
             }

             // Remove highlight after any drop attempt
             Object.values(dropZones).forEach(zone => zone.classList.remove('highlight'));
        }


        function startPhotosynthesisAnimation() {
            // Disable all interactions
            ingredients.forEach(ing => ing.style.pointerEvents = 'none');
            isProcessing = true;

            // Add a visual processing state to the plant area
            plantArea.classList.add('processing');

            // Simulate flow/process with simple particles
            createParticles(50); // Create 50 particles

            // Simulate processing time
            setTimeout(() => {
                 messageArea.textContent = 'קסם הושלם! ✨ הצמח ייצר סוכר וחמצן!';
                 products.forEach(product => product.classList.add('visible')); // Show products with animation

                 // Reset for next cycle after a short delay
                 setTimeout(() => {
                    resetApp();
                 }, 4000); // Wait before resetting
            }, 3000); // Animation duration before products appear
        }

        // Function to create simple particle animations
        function createParticles(count) {
            animationLayer.innerHTML = ''; // Clear previous particles
            const plantRect = plantArea.getBoundingClientRect();

            // Define approximate start/end zones relative to plantArea
            const startZones = [
                { x: plantRect.width * 0.5, y: plantRect.height * 0.9, source: 'water' }, // Root zone
                { x: plantRect.width * 0.5, y: plantRect.height * 0.2, source: 'co2' }  // Leaf zone
            ];
             // Define approximate end zones relative to plantArea (sugar/oxygen exit points)
            const endZones = [
                 { x: plantRect.width * 0.3, y: plantRect.height * 0.5, product: 'glucose' }, // Somewhere in plant body
                 { x: plantRect.width * 0.7, y: plantRect.height * 0.1, product: 'oxygen' } // Top/leaves for oxygen
            ];

            for (let i = 0; i < count; i++) {
                const particle = document.createElement('div');
                particle.classList.add('particle');
                // Randomly pick a start zone
                const startZone = startZones[Math.floor(Math.random() * startZones.length)];
                 // Randomly pick an end zone
                 const endZone = endZones[Math.floor(Math.random() * endZones.length)];

                // Randomize start position slightly within the zone
                const startX = startZone.x + (Math.random() - 0.5) * 20;
                const startY = startZone.y + (Math.random() - 0.5) * 20;

                 // Randomize end position slightly within the zone
                 const endX = endZone.x + (Math.random() - 0.5) * 20;
                 const endY = endZone.y + (Math.random() - 0.5) * 20;


                particle.style.width = particle.style.height = `${Math.random() * 5 + 2}px`; // Random size
                particle.style.backgroundColor = startZone.source === 'water' ? '#2196f3' : '#8bc34a'; // Blue for water, green for CO2
                if (Math.random() < 0.3) particle.style.backgroundColor = '#ffeb3b'; // Some yellow for light energy

                particle.style.position = 'absolute';
                particle.style.left = `${startX}px`;
                particle.style.top = `${startY}px`;
                particle.style.borderRadius = '50%';
                particle.style.opacity = Math.random() * 0.5 + 0.5; // Random opacity
                particle.style.zIndex = 7; /* Above plant */

                 // Animate movement and fade out
                const duration = Math.random() * 2 + 2; // Duration between 2s and 4s
                const delay = Math.random() * 1; // Delay up to 1s

                particle.animate([
                    { transform: `translate(0, 0)`, opacity: particle.style.opacity },
                    { transform: `translate(${endX - startX}px, ${endY - startY}px)`, opacity: 0 }
                ], {
                    duration: duration * 1000,
                    delay: delay * 1000,
                    easing: 'ease-in-out',
                    iterations: 1,
                    fill: 'both' // Keep final state
                });

                // Remove particle after animation
                setTimeout(() => {
                    particle.remove();
                }, (duration + delay) * 1000);


                animationLayer.appendChild(particle);
            }
        }


        // --- Explanation Button ---
        const explanationButton = document.getElementById('explanation-button');
        const explanationContent = document.getElementById('explanation-content');

        explanationButton.addEventListener('click', () => {
            const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
            explanationContent.style.display = isHidden ? 'block' : 'none';
            // Scroll to the explanation if showing? Optional.
             if (isHidden) {
                 explanationContent.scrollIntoView({ behavior: 'smooth', block: 'start' });
             }
        });

        // Initial state: hide products, hide explanation, set initial message
        products.forEach(product => product.classList.remove('visible'));
        explanationContent.style.display = 'none';
         messageArea.textContent = 'גררו את "המצרכים" אל הצמח כדי להתחיל בפוטוסינתזה!';

         // Optional: Add a subtle initial pulse or animation to ingredients to hint they are draggable
         ingredients.forEach((item, index) => {
             item.style.animation = `pulseScale 1.5s ease-in-out infinite ${index * 0.1}s`;
         });

         @keyframes pulseScale {
             0% { transform: scale(1); }
             50% { transform: scale(1.02); }
             100% { transform: scale(1); }
         }
          /* Remove pulse animation when dragging starts */
         .ingredient.dragging {
             animation: none !important;
         }

         // Add Heebo font link (should be in head, but adding here within constraints)
        const link = document.createElement('link');
        link.href = 'https://fonts.googleapis.com/css2?family=Heebo:wght@400;700&display=swap';
        link.rel = 'stylesheet';
        document.head.appendChild(link);

         // Small tweak: make drop zones pointer-events none so clicking/dragging plant doesn't hit them
         Object.values(dropZones).forEach(zone => zone.style.pointerEvents = 'none');
         // Exception: maybe light zone should allow interaction? No, the logic relies on highlight.

    });
</script>