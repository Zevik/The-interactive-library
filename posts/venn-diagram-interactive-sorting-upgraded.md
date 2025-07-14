---
title: "מיון קסום: משחק קבוצות וחיתוכים בעזרת דיאגרמת ון"
english_slug: venn-diagram-interactive-sorting-upgraded
category: "מתמטיקה"
tags: ["דיאגרמות ון", "קבוצות", "חיתוך", "סימולציה", "אינטראקטיבי", "משחק"]
---
# מיון קסום: שחקו עם אובייקטים בדיאגרמת ון

ברוכים הבאים למשחק המיון הקסום! בואו נראה אם תוכלו למקם את כל האובייקטים במקום הנכון שלהם בדיאגרמת ון. שימו לב לתכונות של כל אובייקט ולמה שכל אזור בדיאגרמה מייצג. בהצלחה!

<div class="interactive-app">
    <div class="venn-container">
        <!-- Drop zone for Set A only -->
        <div class="venn-circle set-a drop-zone" id="setA" data-set="A">
            <h2>קבוצת 'אדום'</h2>
            <p>✅ אדום בלבד</p>
             <div class="dropped-objects"></div> <!-- Container for dropped objects -->
        </div>
        <!-- Drop zone for Set B only -->
        <div class="venn-circle set-b drop-zone" id="setB" data-set="B">
            <h2>קבוצת 'עגול'</h2>
            <p>✅ עגול בלבד</p>
            <div class="dropped-objects"></div> <!-- Container for dropped objects -->
        </div>
        <!-- Drop zone for Intersection A & B -->
        <div class="venn-intersection drop-zone" id="intersection" data-set="A&B">
             <h2>אדום <span>וגם</span> עגול</h2>
             <p>✅ אדום ✅ עגול</p>
              <div class="dropped-objects"></div> <!-- Container for dropped objects -->
        </div>
         <!-- Drop zone for Neither A nor B -->
         <div class="venn-neither drop-zone" id="neither" data-set="neither">
             <h2>לא אדום <span>ולא</span> עגול</h2>
             <p>❌ אדום ❌ עגול</p>
              <div class="dropped-objects"></div> <!-- Container for dropped objects -->
        </div>
         <!-- Visual background circles - non-interactive -->
         <div class="venn-circle set-a visual-circle"></div>
         <div class="venn-circle set-b visual-circle"></div>
    </div>

    <div class="objects-container" id="objectsContainer">
        <h3>גררו כל אובייקט לאזור הנכון בדיאגרמת ון:</h3>
        <div class="object-card" id="obj1" data-properties="red,circle" draggable="true"><span class="emoji">🔴</span><span class="desc"> מעגל אדום</span></div>
        <div class="object-card" id="obj2" data-properties="blue,square" draggable="true"><span class="emoji">🟦</span><span class="desc"> ריבוע כחול</span></div>
        <div class="object-card" id="obj3" data-properties="red,square" draggable="true"><span class="emoji">🟥</span><span class="desc"> ריבוע אדום</span></div>
        <div class="object-card" id="obj4" data-properties="blue,circle" draggable="true"><span class="emoji">🔵</span><span class="desc"> מעגל כחול</span></div>
        <div class="object-card" id="obj5" data-properties="green,triangle" draggable="true"><span class="emoji"> مثلث</span><span class="desc"> משולש ירוק</span></div>
        <div class="object-card" id="obj6" data-properties="red,triangle" draggable="true"><span class="emoji"> مثلث</span><span class="desc"> משולש אדום</span></div>
         <div class="object-card" id="obj7" data-properties="blue,triangle" draggable="true"><span class="emoji"> مثلث</span><span class="desc"> משולש כחול</span></div>
          <div class="object-card" id="obj8" data-properties="red,circle" draggable="true"><span class="emoji">🔴</span><span class="desc"> מעגל אדום</span></div>
           <div class="object-card" id="obj9" data-properties="green,circle" draggable="true"><span class="emoji">🟢</span><span class="desc"> מעגל ירוק</span></div>
           <div class="object-card" id="obj10" data-properties="red,circle" draggable="true"><span class="emoji">🔴</span><span class="desc"> מעגל אדום</span></div>
    </div>

     <button id="resetBtn">התחלה חדשה עם אובייקטים חדשים</button>
     <div class="feedback-message" id="feedbackMessage"></div>
</div>

<style>
/* General Page Styling */
body {
    font-family: 'Heebo', sans-serif; /* Use a modern Hebrew-friendly font */
    direction: rtl;
    text-align: right;
    line-height: 1.6;
    color: #2c3e50; /* Darker, modern text color */
    background-color: #ecf0f1; /* Light grey background */
    padding: 20px;
    margin: 0; /* Remove default body margin */
}

h1 {
    color: #2980b9; /* Blue heading */
    text-align: center;
    margin-bottom: 30px;
    font-size: 2.5em;
    font-weight: 700;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
}

h2 {
     color: #34495e; /* Dark grey heading */
     margin-bottom: 5px;
     font-size: 1.4em;
     font-weight: 600;
}

p {
    color: #555;
    font-size: 1.1em;
}

/* Interactive App Container */
.interactive-app {
    background-color: #fff;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15); /* More prominent shadow */
    margin: 20px auto; /* Center the block */
    max-width: 900px; /* Max width for better readability */
    text-align: center;
    position: relative; /* Needed for absolute positioning of feedback */
    overflow: hidden; /* Hide overflow from animations */
}

.interactive-app h3 {
     color: #3498db;
     margin-top: 20px;
     font-size: 1.3em;
}

/* Venn Diagram Container */
.venn-container {
    position: relative;
    width: 650px; /* Slightly larger */
    height: 450px; /* Slightly taller */
    margin: 40px auto;
}

/* Visual Circles (Background) */
.venn-container .visual-circle {
     position: absolute;
     width: 300px;
     height: 300px;
     border-radius: 50%;
     border: 3px solid;
     opacity: 0.3; /* Subtle background */
     pointer-events: none; /* Do not interfere with dragging */
     box-sizing: border-box;
}

.venn-container .visual-circle.set-a {
     border-color: #e74c3c; /* Red */
     background-color: rgba(231, 76, 60, 0.05); /* Very light red */
     top: 60px;
     left: 170px;
}

.venn-container .visual-circle.set-b {
     border-color: #3498db; /* Blue */
     background-color: rgba(52, 152, 219, 0.05); /* Very light blue */
     top: 60px;
     left: 300px;
}


/* Drop Zones (Interactive Areas) */
.venn-container .drop-zone {
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 10px; /* Reduced padding */
    box-sizing: border-box;
    transition: background-color 0.3s ease, transform 0.1s ease;
    z-index: 2; /* Above visual circles */
    color: #34495e;
     font-size: 0.9em;
}

.venn-container .drop-zone h2 {
    font-size: 1.3em; /* Slightly smaller in zones */
    margin-bottom: 0;
}
.venn-container .drop-zone p {
    font-size: 0.8em; /* Smaller rule text */
    margin-top: 2px;
     margin-bottom: 10px;
     opacity: 0.8;
}

.venn-container .drop-zone span {
    font-size: 1.1em; /* Emphasize 'and' / 'nor' */
    font-weight: bold;
}


.venn-container .drop-zone#setA {
    width: 250px; /* Adjusted size */
    height: 250px;
    border-radius: 50%;
    top: 80px;
    left: 150px;
    /* The visual circles handle the main look, drop zones are more abstract interaction areas */
     /* We'll just add a subtle hover effect */
}

.venn-container .drop-zone#setB {
    width: 250px; /* Adjusted size */
    height: 250px;
    border-radius: 50%;
    top: 80px;
    left: 350px;
}

.venn-container .drop-zone#intersection {
     width: 150px; /* Smaller, more accurate intersection area */
     height: 150px;
     top: 140px;
     left: 280px;
     /* No border or strong background by default */
     z-index: 3; /* Ensure it's above circles */
}

.venn-container .drop-zone#neither {
     width: 500px; /* Larger area for 'neither' */
     height: 120px;
     border: 2px dashed #bdc3c7; /* Grey dashed border */
     background-color: rgba(189, 195, 199, 0.1); /* Very light grey */
     border-radius: 8px;
    top: 330px; /* Position below circles */
    left: 75px;
    z-index: 1; /* Below circles and intersection */
}

/* Drop Zone Hover/Dragover Feedback */
.drop-zone.drag-over {
    background-color: rgba(46, 204, 113, 0.15); /* Light green for potential drop */
     transform: scale(1.02); /* Subtle growth on hover */
}

.drop-zone.drag-over#setA { background-color: rgba(231, 76, 60, 0.15); } /* Red hover */
.drop-zone.drag-over#setB { background-color: rgba(52, 152, 219, 0.15); } /* Blue hover */
.drop-zone.drag-over#intersection { background-color: rgba(142, 68, 173, 0.15); } /* Purple hover for intersection */
.drop-zone.drag-over#neither { background-color: rgba(189, 195, 199, 0.25); } /* Darker grey hover */


/* Container for draggable objects */
.objects-container {
    margin-top: 30px;
    border-top: 1px solid #ecf0f1; /* Subtle separator */
    padding-top: 20px;
    min-height: 100px; /* Ensure space */
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 12px; /* Reduced gap */
    align-items: center;
}

/* Draggable Object Card */
.object-card {
    cursor: grab;
    padding: 10px 15px; /* Slightly more padding */
    border: 1px solid #bdc3c7; /* Grey border */
    border-radius: 6px;
    background-color: #fefefe; /* Off-white background */
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.08); /* Enhanced shadow */
    transition: transform 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease;
    font-size: 1.1em;
    display: flex;
    align-items: center;
     z-index: 10; /* Ensure it's above other elements while dragging */
}

.object-card .emoji {
    margin-left: 8px; /* Space between emoji and text */
    font-size: 1.3em; /* Larger emoji */
}
.object-card .desc {
    white-space: nowrap; /* Prevent wrapping */
}


.object-card:hover {
    transform: translateY(-4px); /* More noticeable hover lift */
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.12);
    border-color: #3498db; /* Highlight border on hover */
}

.object-card:active {
    cursor: grabbing;
    transform: scale(1.05);
     box-shadow: 0 5px 10px rgba(0, 0, 0, 0.15);
}

/* State styles after dropping */
.object-card.correct {
    background-color: #d4edda; /* Light green */
    border-color: #28a745; /* Green */
    pointer-events: none; /* Cannot drag again if correct */
    opacity: 0.9; /* Slightly less opaque */
     transition: transform 0.5s ease, opacity 0.5s ease; /* Smooth transition to final position */
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); /* Smaller shadow when placed */
}

.object-card.incorrect {
     background-color: #f8d7da; /* Light red */
    border-color: #dc3545; /* Red */
     animation: shake 0.6s cubic-bezier(.36,.07,.19,.97) both; /* Enhanced shake animation */
     box-shadow: 0 3px 8px rgba(0, 0, 0, 0.1);
}

/* Animation for correct placement (subtle pulse) */
@keyframes pulse-correct {
    0% { transform: scale(1); }
    50% { transform: scale(1.03); }
    100% { transform: scale(1); }
}

/* Animation for incorrect placement (shake) */
@keyframes shake {
    10%, 90% { transform: translateX(-5px); }
    20%, 80% { transform: translateX(5px); }
    30%, 50%, 70% { transform: translateX(-5px); }
    40%, 60% { transform: translateX(5px); }
}

/* Style for objects while dragging */
.object-card.dragging {
    opacity: 0.6;
    transform: scale(0.9);
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
}


/* Container within drop zones for dropped objects */
.drop-zone .dropped-objects {
     position: absolute; /* Position relative to the drop zone */
     top: 0;
     left: 0;
     width: 100%;
     height: 100%;
     pointer-events: none; /* Click/drag events should pass through this container */
     z-index: 1; /* Below the drop zone's text/labels */
     overflow: hidden; /* Keep children inside */
}

/* Style for objects *inside* the dropped-objects container */
.drop-zone .dropped-objects .object-card {
     position: absolute; /* Absolute positioning within the dropped-objects container */
     pointer-events: auto; /* Re-enable pointer events for the object itself if needed (e.g., for future features) */
     z-index: auto; /* Reset z-index */
}


/* Reset Button */
#resetBtn {
    display: block;
    margin: 30px auto 10px; /* More space above, less below */
    padding: 12px 25px; /* Larger padding */
    font-size: 1.2em;
    color: #fff;
    background-color: #e74c3c; /* Reddish-orange color */
    border: none;
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.2s ease;
    font-weight: 600;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

#resetBtn:hover {
    background-color: #c0392b; /* Darker red */
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

#resetBtn:active {
    transform: scale(0.98);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Feedback Message */
.feedback-message {
    min-height: 1.5em; /* Reserve space */
    font-size: 1.1em;
    margin-top: 15px;
    font-weight: 600;
    color: #27ae60; /* Green for positive feedback */
    transition: opacity 0.3s ease;
}

.feedback-message.error {
    color: #e74c3c; /* Red for errors */
}


/* Explanation Section Styling */
.explanation-button {
    display: block;
    margin: 30px auto 20px;
    padding: 12px 25px;
    font-size: 1.2em;
    color: #3498db; /* Blue */
    background-color: transparent;
    border: 2px solid #3498db;
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.3s ease, color 0.3s ease, transform 0.1s ease;
    font-weight: 600;
}

.explanation-button:hover {
    background-color: #3498db;
    color: #fff;
}

.explanation-button:active {
     transform: scale(0.98);
}


.explanation-content {
    border-top: 1px dashed #bdc3c7;
    padding-top: 20px;
    margin-top: 20px;
    background-color: #f4f7f6; /* Light grey-blue */
    padding: 20px;
    border-radius: 8px;
    display: none; /* Initially hidden */
    text-align: right;
}

.explanation-content h2 {
    color: #2980b9;
    margin-top: 0;
    font-size: 1.8em;
}

.explanation-content p {
    margin-bottom: 15px;
    line-height: 1.7;
}

.explanation-content ul {
     margin-bottom: 15px;
     padding-right: 20px; /* Indent list */
}

.explanation-content li {
    margin-bottom: 8px;
}

.explanation-content strong {
    color: #2c3e50; /* Darker color for emphasis */
}

/* Responsive considerations (Basic) */
@media (max-width: 768px) {
    .venn-container {
        width: 100%;
        height: 400px; /* Adjust height */
         margin-top: 20px;
    }

    .venn-container .visual-circle,
    .venn-container .drop-zone#setA,
    .venn-container .drop-zone#setB {
        width: 250px;
        height: 250px;
        top: 50px; /* Adjust position */
    }
    .venn-container .visual-circle.set-a, .venn-container .drop-zone#setA { left: calc(50% - 180px); } /* Center-ish */
    .venn-container .visual-circle.set-b, .venn-container .drop-zone#setB { left: calc(50% - 70px); } /* Center-ish */


    .venn-container .drop-zone#intersection {
        width: 120px; /* Smaller */
        height: 120px;
        top: 130px;
        left: calc(50% - 60px); /* Center */
    }

    .venn-container .drop-zone#neither {
        width: 90%; /* Full width */
        left: 5%;
        top: 300px; /* Adjust position */
        height: 80px;
    }

     .objects-container {
         gap: 8px; /* Smaller gap */
     }

    .object-card {
        padding: 8px 10px;
        font-size: 1em;
    }

     .object-card .emoji {
         font-size: 1.2em;
     }

     h1 { font-size: 2em; }
     h2 { font-size: 1.2em; }
      .drop-zone h2 { font-size: 1.1em; }
       .drop-zone p { font-size: 0.7em; }
}

</style>

<button class="explanation-button" id="toggleExplanation">רוצים להבין יותר? לחצו להסבר על דיאגרמות ון</button>

<div class="explanation-content" id="explanationContent">
    <h2>מה מסתתר מאחורי הדיאגרמה?</h2>
    <p>הכלי ששיחקתם איתו הוא הדגמה כיפית של **דיאגרמת ון**! זהו כלי ויזואלי גאוני שמראה לנו איך דברים מתקשרים זה לזה על בסיס תכונות משותפות או שונות. דמיינו שאתם מנהלי אוסף, ורוצים לסדר את הפריטים שלכם לפי כללים שונים.</p>

    <h2>החלקים הסודיים של הדיאגרמה שלנו:</h2>
    <ul>
        <li>🔴 **המעגל האדום (קבוצת 'אדום'):** כאן נכניס את כל האובייקטים שיש להם את התכונה 'אדום' - **ורק אותה** (מבין התכונות שבדקנו כאן). כלומר, הם אדומים, אבל לא עגולים.</li>
        <li>🔵 **המעגל הכחול (קבוצת 'עגול'):** לכאן יגיעו כל האובייקטים שיש להם את התכונה 'עגול' - **ורק אותה**. כלומר, הם עגולים, אבל לא אדומים.</li>
        <li>💜 **אזור החפיפה הקסום (החיתוך):** זה הלב הפועם של הדיאגרמה! האזור שבו שני המעגלים נפגשים. הוא מיועד לכל האובייקטים שמשתייכים **גם** לקבוצת 'אדום' **וגם** לקבוצת 'עגול'. זהו אזור ה**חיתוך**.</li>
        <li>◻️ **האזור שמחוץ למעגלים ('לא ולא'):** המקום האחרון, אבל לא פחות חשוב. לכאן נגרור את כל האובייקטים ש**אינם** אדומים **ואינם** עגולים.</li>
    </ul>

    <h2>למה זה משחק מנצח?</h2>
    <p>דיאגרמות ון עוזרות לנו לחשוב בצורה מסודרת על קבוצות, להבין איפה הן חופפות ואיפה הן נפרדות. הן כלי יסודי במתמטיקה (בעיקר בתורת הקבוצות וההסתברות), בלוגיקה, ואפילו בחיים היום-יום כשרוצים למיין דברים או להבין יחסים בין קטגוריות שונות. הן הופכות רעיונות מורכבים לפשוטים וברורים!</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const objectsContainer = document.getElementById('objectsContainer');
    const dropZones = {
        setA: document.getElementById('setA'), // 'Red only' zone
        setB: document.getElementById('setB'), // 'Circle only' zone
        intersection: document.getElementById('intersection'), // 'Red AND Circle' zone
        neither: document.getElementById('neither') // 'Neither Red NOR Circle' zone
    };
    const explanationContent = document.getElementById('explanationContent');
    const toggleExplanationBtn = document.getElementById('toggleExplanation');
    const resetBtn = document.getElementById('resetBtn');
    const feedbackMessage = document.getElementById('feedbackMessage');

     // Define the rules for sets A and B
    // Set A: Has property 'red'
    // Set B: Has property 'circle'
    const setRules = {
        A: (props) => props.includes('red'),
        B: (props) => props.includes('circle')
    };

    // Store initial objects HTML to reset
    const initialObjectsHTML = objectsContainer.innerHTML;

    // Function to check if an object belongs in a specific zone
    const checkPlacement = (objectProps, targetSet) => {
        const inSetA = setRules.A(objectProps);
        const inSetB = setRules.B(objectProps);

        switch (targetSet) {
            case 'A': // Should be in A, NOT in B
                return inSetA && !inSetB;
            case 'B': // Should be in B, NOT in A
                return !inSetA && inSetB;
            case 'A&B': // Should be in A AND in B (intersection)
                return inSetA && inSetB;
            case 'neither': // Should NOT be in A, NOR in B
                return !inSetA && !inSetB;
            default:
                return false;
        }
    };

    // Function to handle object placement visually
    const placeObjectVisually = (objectElement, targetZoneElement) => {
         const droppedObjectsContainer = targetZoneElement.querySelector('.dropped-objects');
         if (!droppedObjectsContainer) return; // Should not happen with correct HTML structure

         // Append object to the specific container within the zone
         droppedObjectsContainer.appendChild(objectElement);

         // Calculate random position within the dropped-objects container
         // Subtract object size to keep it within bounds
         const containerRect = droppedObjectsContainer.getBoundingClientRect();
         const objectRect = objectElement.getBoundingClientRect();

         // Define margins to keep objects slightly away from edges
         const margin = 5;
         const randomX = Math.random() * (containerRect.width - objectRect.width - 2 * margin) + margin;
         const randomY = Math.random() * (containerRect.height - objectRect.height - 2 * margin) + margin;

         // Apply absolute positioning relative to the dropped-objects container
         objectElement.style.position = 'absolute';
         objectElement.style.left = `${randomX}px`;
         objectElement.style.top = `${randomY}px`;
         objectElement.style.transform = 'none'; // Remove any previous transform like shake/lift
         objectElement.style.zIndex = 'auto'; // Reset z-index after dragging

         // Apply the pulse animation effect (defined in CSS)
         objectElement.style.animation = 'pulse-correct 0.5s ease forwards';
         objectElement.addEventListener('animationend', () => {
              objectElement.style.animation = ''; // Remove animation after it finishes
         }, { once: true });

    };

     // Function to show feedback message
     const showFeedback = (message, isError = false) => {
         feedbackMessage.textContent = message;
         feedbackMessage.classList.toggle('error', isError);
         feedbackMessage.style.opacity = 1;

         // Hide message after a few seconds
         setTimeout(() => {
             feedbackMessage.style.opacity = 0;
         }, 3000);
     };

     // Function to initialize or reset objects
     const initializeObjects = () => {
         objectsContainer.innerHTML = initialObjectsHTML; // Restore initial objects
         objectsContainer.querySelectorAll('.object-card').forEach(object => {
             object.addEventListener('dragstart', (e) => {
                 e.dataTransfer.setData('text/plain', object.id);
                 // Add a class for styling while dragging
                 setTimeout(() => {
                      object.classList.add('dragging');
                 }, 0); // Use setTimeout to allow the drag image to be set before class is added
             });

              object.addEventListener('dragend', (e) => {
                  // Remove the dragging class
                  e.target.classList.remove('dragging');
                   // If the object was not successfully dropped and marked 'correct',
                   // ensure it's back in the objects container visually.
                   // The drop handler will move correct objects. Incorrect ones might briefly shake.
                   // This logic is more complex if objects are removed from container DOM on drag.
                   // With current logic (shake and stay if incorrect), this dragend handler mainly cleans up the 'dragging' class.
              });

             // Reset styles from previous rounds
             object.classList.remove('correct', 'incorrect');
             object.style.position = 'static'; // Or 'relative' if needed for layout
             object.style.left = 'auto';
             object.style.top = 'auto';
             object.style.transform = 'none';
             object.style.opacity = 1;
             object.style.pointerEvents = 'auto'; // Make it draggable
             object.style.animation = ''; // Remove any stuck animation
         });

          // Clear dropped objects from zones
          Object.values(dropZones).forEach(zone => {
               const droppedContainer = zone.querySelector('.dropped-objects');
               if (droppedContainer) {
                   droppedContainer.innerHTML = ''; // Remove all children
               }
          });

          showFeedback("התחלה חדשה! גררו את האובייקטים.");
     };


    // Add event listeners for drop zones
    Object.values(dropZones).forEach(zone => {
        zone.addEventListener('dragover', (e) => {
            e.preventDefault(); // Necessary to allow dropping
            e.stopPropagation(); // Prevent event from bubbling up to parent zones if any
            // Add visual feedback for dragover
             zone.classList.add('drag-over');
        });

        zone.addEventListener('dragleave', (e) => {
             e.stopPropagation();
            // Remove visual feedback
             zone.classList.remove('drag-over');
        });

         zone.addEventListener('drop', (e) => {
            e.preventDefault();
             e.stopPropagation();
            zone.classList.remove('drag-over'); // Remove hover feedback immediately

            const objectId = e.dataTransfer.getData('text/plain');
            const droppedObject = document.getElementById(objectId);

            if (!droppedObject) return; // Should not happen

            const objectProperties = droppedObject.dataset.properties.split(',');
            const targetSet = zone.dataset.set;

            const isCorrect = checkPlacement(objectProperties, targetSet);


            if (isCorrect) {
                // Move the object to the drop zone visually and mark as correct
                droppedObject.classList.add('correct');
                droppedObject.classList.remove('incorrect'); // Remove incorrect if it was previously marked
                droppedObject.setAttribute('draggable', 'false'); // Make it non-draggable once correct
                droppedObject.style.cursor = 'default'; // Change cursor

                 placeObjectVisually(droppedObject, zone); // Place the object nicely

                 showFeedback("מצוין! מיקום נכון.", false);

                 // Check if all objects are correctly placed
                 const remainingObjects = objectsContainer.querySelectorAll('.object-card:not(.correct)');
                 if (remainingObjects.length === 0) {
                     showFeedback("כל הכבוד! מיקמתם את כל האובייקטים נכון!", false);
                 }

            } else {
                // Mark as incorrect and shake
                droppedObject.classList.add('incorrect');
                showFeedback("אופס! נסו שוב. האובייקט הזה לא שייך לכאן.", true);

                 // After the shake animation, remove the 'incorrect' class
                 droppedObject.addEventListener('animationend', () => {
                     droppedObject.classList.remove('incorrect');
                      // You could also return it to the starting container here if desired
                      // objectsContainer.appendChild(droppedObject);
                      // droppedObject.style.position = 'relative';
                      // droppedObject.style.transform = 'none';
                      // droppedObject.style.left = 'auto'; droppedObject.style.top = 'auto';
                 }, { once: true }); // Use { once: true } so the listener is removed after it runs
            }
        });
    });

    // Toggle explanation visibility
    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
        explanationContent.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר על דיאגרמות ון' : 'רוצים להבין יותר? לחצו להסבר על דיאגרמות ון';
    });

    // Reset function
    resetBtn.addEventListener('click', () => {
        initializeObjects(); // Re-initialize objects
    });

     // Initial setup: Ensure explanation is hidden and objects are ready
     explanationContent.style.display = 'none';
     initializeObjects(); // Initialize objects when the page loads
});
</script>
---