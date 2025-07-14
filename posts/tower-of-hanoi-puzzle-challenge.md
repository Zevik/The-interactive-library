---
title: "אתגר מגדלי האנוי: מסע אל עולם הלוגיקה והאלגוריתמים"
english_slug: tower-of-hanoi-puzzle-challenge
category: "מתמטיקה"
tags:
  - פאזל
  - מגדלי האנוי
  - לוגיקה
  - אלגוריתם
  - משחק
  - רקורסיה
---
# אתגר מגדלי האנוי: מסע אל עולם הלוגיקה והאלגוריתמים

נראה פשוט, נכון? רק להעביר ערימת דיסקיות ממקום למקום. אבל אל תתנו לפשטות להטעות אתכם! הפאזל העתיק הזה מסתיר בתוכו עקרונות יסוד של יעילות, אסטרטגיה ואפילו את אחד הרעיונות היפים והחשובים ביותר במדעי המחשב – הרקורסיה. האם תצליחו לעמוד באתגר ולגלות את המסע המינימלי?

<div id="hanoi-app">
    <div class="controls">
        <label for="disk-count">בחר מספר דיסקיות:</label>
        <select id="disk-count">
            <option value="3">3 דיסקיות</option>
            <option value="4">4 דיסקיות</option>
             <option value="5">5 דיסקיות</option>
        </select>
        <button id="reset-button">התחל מחדש</button>
        <div id="moves-counter">מהלכים: 0</div>
    </div>
    <div class="game-area">
        <div class="peg-container" data-peg-id="1">
            <div class="peg"></div>
            <div class="disks"></div>
        </div>
        <div class="peg-container" data-peg-id="2">
            <div class="peg"></div>
            <div class="disks"></div>
        </div>
        <div class="peg-container" data-peg-id="3">
            <div class="peg"></div>
            <div class="disks"></div>
        </div>
        <div class="base"></div> <!-- Added base element -->
    </div>
    <div id="message-area"></div>
</div>

<style>
/* Basic reset and body styles */
body {
    margin: 0;
    padding: 0;
    background-color: #e0f7fa; /* Light cyan background */
    font-family: 'Arial', sans-serif;
    direction: rtl; /* Ensure RTL for Hebrew */
    text-align: right;
}

#hanoi-app {
    font-family: 'Arial', sans-serif;
    text-align: center;
    padding: 25px;
    background: linear-gradient(to bottom, #ffffff, #f0f0f0); /* Subtle gradient background */
    border-radius: 12px;
    margin: 20px auto;
    max-width: 900px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15); /* Softer, deeper shadow */
    border: 1px solid #dcdcdc;
    overflow: hidden; /* Clear floats/margins if needed */
    position: relative; /* For absolute positioning of elements inside */
}

h1 {
    color: #004d40; /* Dark teal */
    margin-top: 0;
    margin-bottom: 25px;
    font-size: 1.8rem;
}

p {
    color: #333;
    line-height: 1.7;
    margin-bottom: 15px;
}


.controls {
    margin-bottom: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    flex-wrap: wrap;
}

.controls label {
    font-weight: bold;
    color: #00796b; /* Teal */
    font-size: 1.1rem;
}

.controls select, .controls button {
    padding: 10px 15px;
    font-size: 1rem;
    border: 1px solid #b2dfdb; /* Light teal border */
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.3s ease, border-color 0.3s ease;
}

.controls select {
     background-color: #e0f2f7; /* Very light blue */
     color: #004d40;
}

.controls button {
    background-color: #4db6ac; /* Medium teal */
    color: white;
    font-weight: bold;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.controls button:hover {
    background-color: #26a69a; /* Darker teal */
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

#moves-counter {
    font-weight: bold;
    font-size: 1.3rem;
    color: #004d40; /* Dark teal */
    min-width: 100px; /* Give it some minimum width */
    text-align: left; /* Keep counter aligned */
}

.game-area {
    display: flex;
    justify-content: space-around;
    align-items: flex-end;
    height: 300px; /* Increased height for more visual space */
    margin-bottom: 20px;
    position: relative; /* For positioning pegs absolutely */
    padding: 0 20px; /* Padding on sides */
}

.base {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 25px; /* Thicker base */
    background-color: #8d6e63; /* Brown */
    border-top: 2px solid #6d4c41;
    z-index: 1; /* Below pegs and disks */
    border-radius: 0 0 8px 8px; /* Rounded corners at bottom */
}

.peg-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-end;
    height: calc(100% - 25px); /* Height above the base */
    width: 30%;
    position: absolute; /* Position pegs absolutely within game-area */
    bottom: 25px; /* Position above the base */
    z-index: 2;
     /* Distribute pegs horizontally */
    transition: transform 0.3s ease; /* Add transition for potential future use */
}

.peg-container[data-peg-id="1"] { left: 5%; }
.peg-container[data-peg-id="2"] { left: 50%; transform: translateX(-50%); }
.peg-container[data-peg-id="3"] { right: 5%; }


.peg {
    width: 12px; /* Thicker pegs */
    height: 100%;
    background-color: #5d4037; /* Darker brown */
    border-radius: 6px 6px 0 0; /* Rounded top */
    box-shadow: inset 0 0 5px rgba(0,0,0,0.2);
    position: relative; /* For peg features */
    z-index: 1;
}

.disks {
    position: absolute; /* Disks are positioned absolutely within game-area */
    bottom: 0; /* Disks stack from the base */
    left: 50%; /* Center disks on peg */
    transform: translateX(-50%); /* Center disks on peg */
    width: 100%; /* Disks use the peg container width */
    display: flex; /* Use flex to manage disk stacking */
    flex-direction: column-reverse; /* Stack bottom-up */
    align-items: center;
    gap: 3px; /* Increased gap */
    z-index: 3; /* Above peg and base */
    height: 100%; /* Allow disks to take up height */
    padding-bottom: 0; /* No padding needed here with absolute positioning */
}

.disk {
    height: 28px; /* Slightly taller disks */
    border: 2px solid rgba(0,0,0,0.2); /* Subtle border */
    border-radius: 8px; /* More rounded corners */
    cursor: grab;
    transition: background-color 0.2s ease, transform 0.3s ease, box-shadow 0.3s ease, top 0.3s ease, left 0.3s ease; /* Add transitions for movement */
    box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* Default shadow */
    position: absolute; /* Start positioned absolutely */
    left: 50%; /* Center initially */
    transform: translateX(-50%); /* Center initially */
}

/* Disk sizes - use a more vibrant palette */
.disk-1 { width: 70%; background-color: #ef5350; } /* Red */
.disk-2 { width: 60%; background-color: #ffb300; } /* Amber */
.disk-3 { width: 50%; background-color: #8bc34a; } /* Light green */
.disk-4 { width: 40%; background-color: #03a9f4; } /* Light blue */
.disk-5 { width: 30%; background-color: #ab47bc; } /* Purple */


.disk:hover {
    box-shadow: 0 4px 10px rgba(0,0,0,0.2); /* Highlight on hover */
    cursor: grab;
}

/* Style for the top disk on each peg - indicates it's draggable */
.disks .disk:last-child {
    cursor: grab; /* Only the top disk is grab-able */
    /* Optional: Add a subtle visual cue */
    /* box-shadow: 0 0 8px rgba(0,255,255,0.5); */
}


.disk.dragging {
    opacity: 0.9;
    cursor: grabbing;
    z-index: 1000; /* Bring to front */
    box-shadow: 0 8px 20px rgba(0,0,0,0.3); /* Prominent shadow when dragging */
}

/* Styles for animating disk movement - applied via JS */
.disk.moving {
     transition: top 0.5s ease-in-out, left 0.5s ease-in-out; /* Smooth move animation */
}

.peg-container.highlight .peg {
    box-shadow: 0 0 15px rgba(0,255,255,0.8); /* Cyan glow on potential drop target */
}


#message-area {
    margin-top: 20px;
    min-height: 25px; /* Ensure space even when empty */
    color: #d32f2f; /* Red */
    font-weight: bold;
    font-size: 1.1rem;
    text-align: center; /* Center messages */
    min-height: 1.5em; /* Give it enough height for a line */
}

#explanation-button {
    display: block;
    margin: 30px auto 20px auto; /* More space */
    padding: 12px 25px;
    font-size: 1.1rem;
    cursor: pointer;
    border: 1px solid #b2dfdb;
    border-radius: 6px;
    background-color: #e0f2f7; /* Light blue */
    color: #004d40;
    font-weight: bold;
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

#explanation-button:hover {
    background-color: #b2ebf2; /* Lighter blue */
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}


#explanation {
    margin-top: 30px;
    padding-top: 25px;
    border-top: 2px solid #b2dfdb; /* Teal border top */
    text-align: right; /* Align text right for RTL */
    display: none; /* Start hidden */
    direction: rtl;
    color: #333;
    line-height: 1.8;
}

#explanation h2 {
    color: #004d40; /* Dark teal */
    margin-bottom: 20px;
    font-size: 1.6rem;
}

#explanation h3 {
     color: #00796b; /* Teal */
     margin-top: 20px;
     margin-bottom: 10px;
     font-size: 1.3rem;
}

#explanation p {
    margin-bottom: 15px;
}

#explanation ul {
    margin-bottom: 15px;
    padding-right: 25px; /* Adjust padding for RTL list */
}

#explanation li {
    margin-bottom: 10px;
    line-height: 1.6;
}

#explanation strong {
    color: #004d40;
}


/* Responsive adjustments */
@media (max-width: 768px) {
    .game-area {
        flex-direction: column;
        align-items: center;
        height: auto; /* Allow height to adjust */
        gap: 30px; /* Space between peg containers when stacked */
        padding: 0 10px;
        min-height: 400px; /* Ensure minimum height */
    }
     .base {
         display: none; /* Hide the single base in stacked view, pegs have their own base feel */
     }
    .peg-container {
        position: relative; /* Revert to relative positioning */
        bottom: auto;
        left: auto;
        right: auto;
        transform: none;
        width: 80%; /* Wider pegs */
        height: 150px; /* Fixed height for each peg area */
        border-bottom: 15px solid #8d6e63; /* Add base to each peg container */
        border-radius: 8px;
    }
     .peg {
        height: calc(100% - 15px); /* Adjust peg height based on new base */
         bottom: 15px; /* Position peg slightly above the new base */
     }
     .disks {
         bottom: 15px; /* Position disks slightly above the new base */
         height: calc(100% - 15px);
     }

     .disk {
         /* Re-calculate disk position based on new container */
         /* JS needs to handle positioning relative to the peg-container */
     }

    .controls {
        gap: 10px;
    }

    .controls select, .controls button {
        padding: 8px 10px;
        font-size: 0.9rem;
    }

    #moves-counter {
        font-size: 1.2rem;
    }
     h1 {
         font-size: 1.6rem;
     }
}

</style>

<button id="explanation-button">מה זה מגדלי האנוי ולמה זה מעניין?</button>

<div id="explanation">
    <h2>הסבר על פאזל מגדלי האנוי</h2>

    <h3>מה זה פאזל מגדלי האנוי?</h3>
    <p>מגדלי האנוי (Tower of Hanoi) הוא פאזל מתמטי קלאסי שהומצא בשנת 1883 על ידי המתמטיקאי הצרפתי אדוארד לוקאס. האגדה המפורסמת מספרת על מקדש בבנארס ובו 64 דיסקיות זהב ענקיות על שלושה מוטות. הנזירים במקדש עובדים לילות כימים להעביר את הדיסקיות ממוט אחד לאחר, בהתאם לחוקי המשחק הנוקשים. לפי האגדה, כאשר יסתיים הפאזל, העולם יגיע לסופו. הפאזל הזה, על אף פשטותו, מדגים עקרונות עמוקים בלוגיקה, תכנון אלגוריתמי וחשיבה חישובית.</p>

    <h3>חוקי המשחק הפשוטים (אבל המחייבים!)</h3>
    <p>לפאזל שלושה חוקים ברורים בלבד:</p>
    <ol>
        <li>מותר להזיז דיסקית אחת בלבד בכל פעם.</li>
        <li>מותר להזיז רק את הדיסקית העליונה ביותר על כל מוט.</li>
        <li>אסור (אבל ממש אסור!) להניח דיסקית גדולה על דיסקית קטנה יותר.</li>
    </ol>

    <h3>המטרה הגדולה</h3>
    <p>להעביר את כל ערימת הדיסקיות, בשלמותה ובסדר הנכון (הגדולה למטה, הקטנה למעלה), ממוט ההתחלה (השמאלי ביותר) למוט היעד (הימני ביותר).</p>

    <h3>פתרון אופטימלי ומספר מהלכים מינימלי</h3>
    <p>נראה שלוש דיסקיות זה קל, נכון? נסו ותגלו! מספר המהלכים המינימלי הדרוש לפתרון פאזל מגדלי האנוי עם **N** דיסקיות ניתן לחישוב באמצעות נוסחה אלגנטית במיוחד: **2<sup>N</sup> - 1**.</p>
    <ul>
        <li>עבור N=3 דיסקיות: 2<sup>3</sup> - 1 = 8 - 1 = **7 מהלכים**. נסו לפתור את זה ב-7! זה לא טריוויאלי.</li>
        <li>עבור N=4 דיסקיות: 2<sup>4</sup> - 1 = 16 - 1 = **15 מהלכים**. כמעט פי שניים מהלכים על דיסקית אחת נוספת!</li>
         <li>עבור N=5 דיסקיות: 2<sup>5</sup> - 1 = 32 - 1 = **31 מהלכים**. האתגר גדל משמעותית.</li>
        <li>ועבור N=64 הדיסקיות האגדיות במקדש: 2<sup>64</sup> - 1. זהו מספר פנטסטי, גדול מ-18 קווינטיליון (18,446,744,073,709,551,615)! גם אם הנזירים יזיזו דיסקית אחת בכל שנייה, זה ייקח להם מעל 584 מיליארד שנים – זמן ארוך יותר מגיל היקום. לא פלא שהאגדה מקשרת את סוף המשחק לסוף העולם.</li>
    </ul>

    <p>הנוסחה הזו מדגימה את הקפיצה העצומה בכמות המהלכים הנדרשת עם כל דיסקית נוספת. זהו גידול מעריכי, שמלמד אותנו על סוגי בעיות שנעשות קשות מאוד לפתרון ככל שהקלט גדל (מושג חשוב במדעי המחשב).</p>


    <h3>הקשר העמוק למדעי המחשב: רקורסיה</h3>
    <p>מעבר להיותו פאזל מהנה, מגדלי האנוי הוא דוגמה מושלמת לרעיון מתמטי וחישובי יסודי: **רקורסיה**. רקורסיה היא שיטה להגדרת פתרון לבעיה באמצעות פתרון של מקרים פשוטים יותר של אותה הבעיה. נשמע מורכב? חשבו על זה כך:</p>
    <ul>
        <li>כדי להעביר N דיסקיות ממוט המקור למוט היעד...</li>
        <li>...אתם צריכים קודם כל להעביר את N-1 הדיסקיות העליונות ממוט המקור למוט העזר. (זו בעיה קטנה יותר, מאותו סוג!)</li>
        <li>אחרי שסילקתם את N-1 הדיסקיות הקטנות יותר, אתם יכולים להזיז את הדיסקית הגדולה ביותר (N) ממוט המקור למוט היעד הפנוי. (זה מהלך קל).</li>
        <li>ולבסוף, אתם צריכים להעביר את אותן N-1 דיסקיות שנמצאות על מוט העזר... למוט היעד. (שוב, אותה בעיה, רק קטנה יותר!)</li>
    </ul>
    <p>הפתרון המינימלי של מגדלי האנוי בנוי בצורה רקורסיבית טבעית. הבנת איך לפרק בעיה גדולה לבעיות קטנות יותר מאותו סוג, ולפתור את המקרים הבסיסיים ביותר (כמו להזיז דיסקית אחת), היא אבן יסוד בתכנון אלגוריתמים ובכתיבת קוד.</p>

    <p>נסו לפתור את הפאזל, שימו לב למהלכים שלכם, והרגישו בעצמכם איך האתגר גדל במהירות. זהו לא סתם משחק, אלא שער כניסה לחשיבה לוגית ואלגוריתמית מרתקת!</p>
</div>


<script>
document.addEventListener('DOMContentLoaded', () => {
    const appContainer = document.getElementById('hanoi-app');
    const gameArea = appContainer.querySelector('.game-area');
    const pegContainers = gameArea.querySelectorAll('.peg-container'); // The full peg containers including peg and disks div
    const pegsDisksDivs = gameArea.querySelectorAll('.peg-container .disks'); // The containers for disks on each peg
    const movesCounter = document.getElementById('moves-counter');
    const messageArea = document.getElementById('message-area');
    const diskCountSelect = document.getElementById('disk-count');
    const resetButton = document.getElementById('reset-button');
    const explanationButton = document.getElementById('explanation-button');
    const explanationDiv = document.getElementById('explanation');

    let numberOfDisks = parseInt(diskCountSelect.value);
    let moves = 0;
    let draggingDisk = null; // Keep track of the disk being dragged
    let originalPegElement = null; // The .disks div the disk came from
    let currentPegContainer = null; // The .peg-container the disk is currently conceptually on
    let dragStartX, dragStartY; // Mouse/touch position when drag started
    let diskOffsetX, diskOffsetY; // Offset from disk top-left to drag start point

    // Function to initialize or reset the game
    function initializeGame() {
        moves = 0;
        movesCounter.textContent = `מהלכים: ${moves}`;
        messageArea.textContent = '';
        numberOfDisks = parseInt(diskCountSelect.value);

        // Clear all disks from pegs
        pegsDisksDivs.forEach(peg => {
            peg.innerHTML = '';
            peg.parentElement.classList.remove('highlight'); // Remove any highlights
        });

        // Add disks to the first peg (.disks div within peg-container[data-peg-id="1"])
        const firstPegDisksDiv = appContainer.querySelector('.peg-container[data-peg-id="1"] .disks');
        for (let i = numberOfDisks; i >= 1; i--) {
            const disk = document.createElement('div');
            disk.classList.add('disk', `disk-${i}`);
            disk.dataset.diskSize = i;
            // Add initial position styles (calculated dynamically below)
             disk.style.width = `${(100 / numberOfDisks) * i * 0.8 + 20}%`; // Example: dynamic width based on number of disks

            // Disks are positioned absolutely within the peg container
            disk.style.position = 'absolute';
            disk.style.left = '50%';
            disk.style.transform = 'translateX(-50%)';
            // Calculate and set initial vertical position
            const bottomPosition = (numberOfDisks - i) * (getDiskHeight() + getDiskGap());
            disk.style.bottom = `${bottomPosition}px`;


            // Add event listeners for starting drag
            disk.addEventListener('mousedown', startDrag);
            disk.addEventListener('touchstart', startDrag, { passive: false }); // passive: false needed for preventDefault

            firstPegDisksDiv.appendChild(disk);
        }

        updateDraggableDisks(); // Make only top disks draggable/grabbable
    }

    // Helper to get disk height (read from CSS)
    function getDiskHeight() {
        // Create a dummy disk to measure its computed height
        const dummy = document.createElement('div');
        dummy.classList.add('disk');
        dummy.style.visibility = 'hidden';
        dummy.style.position = 'absolute'; // Avoid layout impact
        appContainer.appendChild(dummy); // Append to a visible part of the DOM
        const height = dummy.offsetHeight;
        appContainer.removeChild(dummy); // Remove the dummy
        return height > 0 ? height : 28; // Default if measurement fails
    }

     // Helper to get disk gap (read from CSS)
    function getDiskGap() {
         // Get the gap value from the CSS of .disks (flexbox gap)
         // This is tricky to get directly from CSS. A simpler approach is to hardcode it
         // or measure the difference between disk bottoms, but hardcoding is simpler here
         return 3; // Matches the CSS .disks gap property
    }


    // Enable/Disable drag on top disks only
    function updateDraggableDisks() {
        pegsDisksDivs.forEach(peg => {
            // First, remove grab cursor and pointer events from all disks on this peg
            peg.querySelectorAll('.disk').forEach(d => {
                d.style.pointerEvents = 'none';
                d.style.cursor = 'default'; // Reset cursor
                d.classList.remove('top-disk'); // Remove visual cue class
            });

            const topDisk = peg.lastElementChild;
            if (topDisk) {
                // Enable pointer events and set grab cursor only for the top disk
                topDisk.style.pointerEvents = 'auto';
                topDisk.style.cursor = 'grab';
                topDisk.classList.add('top-disk'); // Add class for potential visual cue in CSS
            }
        });
    }

    // Start drag event handler
    function startDrag(e) {
        const diskElement = e.target;
        const parentPegDisksDiv = diskElement.parentElement;

        // Ensure it's the top disk using the class added by updateDraggableDisks
         if (!diskElement.classList.contains('top-disk')) {
             messageArea.textContent = "ניתן להזיז רק את הדיסקית העליונה!";
             // Clear message after a short delay
             setTimeout(() => { messageArea.textContent = ''; }, 1500);
             return; // Not the top disk
         }

        e.preventDefault(); // Prevent default browser drag behavior (especially for touch)

        messageArea.textContent = ''; // Clear previous messages on drag start

        draggingDisk = diskElement;
        originalPegElement = parentPegDisksDiv; // Keep reference to the .disks div it came from
        currentPegContainer = originalPegElement.parentElement; // And the .peg-container

        draggingDisk.classList.add('dragging');

        // Remove the disk from its current peg container temporarily
        // This allows absolute positioning relative to a higher parent (gameArea)
        // without being constrained by the peg's smaller size/positioning.
        // We'll re-append it later after the move/reset animation.
        originalPegElement.removeChild(draggingDisk);
        gameArea.appendChild(draggingDisk); // Append to gameArea for absolute positioning relative to it


        // Calculate initial position and offset relative to the gameArea
        const gameAreaRect = gameArea.getBoundingClientRect();
        const diskRect = draggingDisk.getBoundingClientRect();

        if (e.type === 'mousedown') {
            dragStartX = e.clientX;
            dragStartY = e.clientY;
        } else if (e.type === 'touchstart') {
            const touch = e.touches[0];
            dragStartX = touch.clientX;
            dragStartY = touch.clientY;
        }

        // Calculate offset from the disk's top-left corner to the mouse/touch point
        diskOffsetX = dragStartX - diskRect.left;
        diskOffsetY = dragStartY - diskRect.top;


        // Set the initial absolute position relative to gameArea
        draggingDisk.style.position = 'absolute';
        draggingDisk.style.left = (dragStartX - gameAreaRect.left - diskOffsetX) + 'px';
        draggingDisk.style.top = (dragStartY - gameAreaRect.top - diskOffsetY) + 'px';
        draggingDisk.style.bottom = 'auto'; // Clear bottom style when dragging
        draggingDisk.style.transform = 'none'; // Clear transform when dragging

        // Add global event listeners for moving and ending drag
        document.addEventListener('mousemove', duringDrag);
        document.addEventListener('touchmove', duringDrag, { passive: false });
        document.addEventListener('mouseup', endDrag);
        document.addEventListener('touchend', endDrag);

         // Temporarily disable pointer events on other elements to avoid interference
         appContainer.style.pointerEvents = 'none';
         draggingDisk.style.pointerEvents = 'auto'; // Keep the dragging disk interactive
    }

    // During drag event handler
    function duringDrag(e) {
        if (!draggingDisk) return;

        e.preventDefault(); // Prevent scrolling/zooming on touch move

        let clientX, clientY;
        if (e.type === 'mousemove') {
            clientX = e.clientX;
            clientY = e.clientY;
        } else if (e.type === 'touchmove') {
            const touch = e.touches[0];
            clientX = touch.clientX;
            clientY = touch.clientY;
        } else {
             return; // Should not happen
        }

        const gameAreaRect = gameArea.getBoundingClientRect();

        // Update disk position relative to gameArea
        draggingDisk.style.left = (clientX - gameAreaRect.left - diskOffsetX) + 'px';
        draggingDisk.style.top = (clientY - gameAreaRect.top - diskOffsetY) + 'px';

        // Highlight potential drop targets
        const targetPegContainer = getPegContainerUnder(clientX, clientY);
        pegContainers.forEach(peg => {
             // Remove highlight from all except potentially the current one
             if (peg !== targetPegContainer) {
                peg.classList.remove('highlight');
             }
         });
        if (targetPegContainer && targetPegContainer !== currentPegContainer) {
             // Only highlight if it's a different peg than the origin
             targetPegContainer.classList.add('highlight');
        }
    }

    // Helper to find which peg container is under the cursor
     function getPegContainerUnder(clientX, clientY) {
         let targetPeg = null;
         // Iterate through peg containers to check if point is inside
         pegContainers.forEach(pegContainer => {
             const rect = pegContainer.getBoundingClientRect();
             // Expand the hit area slightly to make dropping easier
             const hitAreaPadding = 15; // pixels
             if (clientX > rect.left - hitAreaPadding && clientX < rect.right + hitAreaPadding &&
                 clientY > rect.top - hitAreaPadding && clientY < rect.bottom + hitAreaPadding) {
                 targetPeg = pegContainer; // Found a peg container under the point
             }
         });
         return targetPeg;
     }


    // End drag event handler
    function endDrag(e) {
        if (!draggingDisk) return;

        e.preventDefault(); // Prevent click after touch end etc.

         // Re-enable pointer events on app container
         appContainer.style.pointerEvents = 'auto';


        // Remove global event listeners
        document.removeEventListener('mousemove', duringDrag);
        document.removeEventListener('touchmove', duringDrag);
        document.removeEventListener('mouseup', endDrag);
        document.removeEventListener('touchend', endDrag);

        // Determine drop target based on cursor position
        let clientX, clientY;
        if (e.type === 'mouseup') {
            clientX = e.clientX;
            clientY = e.clientY;
        } else if (e.type === 'touchend' && e.changedTouches.length > 0) {
            const touch = e.changedTouches[0];
            clientX = touch.clientX;
            clientY = touch.clientY;
        } else {
            // If end event doesn't provide coordinates (e.g., touchcancel), reset
            resetDiskPosition(draggingDisk, originalPegElement, currentPegContainer);
             return;
        }


        const targetPegContainer = getPegContainerUnder(clientX, clientY);
        const targetPegDisksDiv = targetPegContainer ? targetPegContainer.querySelector('.disks') : null;

        // Remove highlight from all pegs
        pegContainers.forEach(peg => { peg.classList.remove('highlight'); });


        // Check if drop is on a valid different peg
        if (targetPegContainer && targetPegContainer !== currentPegContainer) {
            const diskSize = parseInt(draggingDisk.dataset.diskSize);
            const topDiskOnTarget = targetPegDisksDiv.lastElementChild;
            const topDiskSizeOnTarget = topDiskOnTarget ? parseInt(topDiskOnTarget.dataset.diskSize) : Infinity; // Infinity if peg is empty

            // Check if the move is valid according to game rules
            if (diskSize < topDiskSizeOnTarget) {
                // Valid move! Animate to target peg
                animateDiskMove(draggingDisk, targetPegContainer, targetPegDisksDiv, () => {
                    // Animation complete callback
                    moves++;
                    movesCounter.textContent = `מהלכים: ${moves}`;
                    checkWinCondition(); // Check win after successful move
                    updateDraggableDisks(); // Re-evaluate draggable disks
                });
            } else {
                // Invalid move: Larger disk on smaller one
                messageArea.textContent = "מהלך לא חוקי: אסור להניח דיסקית גדולה על דיסקית קטנה!";
                 // Clear message after a short delay
                 setTimeout(() => { messageArea.textContent = ''; }, 2000);
                // Animate disk back to original peg
                resetDiskPosition(draggingDisk, originalPegElement, currentPegContainer);
            }
        } else {
            // Dropped outside valid peg or on the original peg
             if (!targetPegContainer) {
                messageArea.textContent = "נא לשחרר את הדיסקית מעל אחד המוטות.";
                 // Clear message after a short delay
                 setTimeout(() => { messageArea.textContent = ''; }, 1500);
             }
            resetDiskPosition(draggingDisk, originalPegElement, currentPegContainer);
        }

        // Reset dragging state variables
        draggingDisk = null;
        originalPegElement = null;
        currentPegContainer = null;
    }

    // Animates the disk moving from its current temp position to a target peg position
    function animateDiskMove(disk, targetPegContainer, targetPegDisksDiv, callback) {
         const gameAreaRect = gameArea.getBoundingClientRect();
         const targetPegRect = targetPegContainer.getBoundingClientRect();
         const numDisksOnTarget = targetPegDisksDiv.children.length;

         // Calculate target position relative to gameArea
         // The target position is centered horizontally on the target peg
         // and stacked vertically based on the number of disks already there + the base height
         const targetLeft = targetPegRect.left + (targetPegRect.width / 2) - gameAreaRect.left;
         const targetBottom = (numDisksOnTarget * (getDiskHeight() + getDiskGap())) + parseInt(gameArea.querySelector('.base').offsetHeight); // Stack disks + position above base


         disk.style.transition = 'none'; // Disable transition for immediate positioning adjustment
         disk.style.left = (targetLeft - disk.offsetWidth / 2) + 'px'; // Set horizontal center
         disk.style.top = 'auto'; // Use bottom for vertical stacking
         disk.style.bottom = `${targetBottom}px`; // Set vertical position relative to gameArea bottom


        // Now enable transition and let CSS animate to this position
        // We need a tiny delay for the style change to register before the transition is enabled
        requestAnimationFrame(() => {
             requestAnimationFrame(() => { // Double rAF for guaranteed repaint
                 disk.style.transition = 'bottom 0.3s ease-in-out, left 0.3s ease-in-out, transform 0.3s ease-in-out';
                 disk.classList.remove('dragging'); // Remove dragging styles immediately
                 disk.classList.add('moving'); // Add moving class for animation

                 // Listen for the transition to end
                 const onTransitionEnd = () => {
                     disk.removeEventListener('transitionend', onTransitionEnd);

                     // After animation, reset position styles and re-append to the target peg's .disks div
                     disk.style.position = '';
                     disk.style.left = '';
                     disk.style.top = '';
                     disk.style.bottom = '';
                     disk.style.transform = '';
                     disk.classList.remove('moving');

                     // Append to the target peg's .disks div. This is crucial for
                     // the DOM structure to reflect the game state and for last-child selector.
                     // We need to ensure it's inserted in the correct order if needed,
                     // but since we only move the top disk, simple appendChild works for stacking order.
                     targetPegDisksDiv.appendChild(disk);

                     if (callback) {
                         callback();
                     }
                 };
                 disk.addEventListener('transitionend', onTransitionEnd);
             });
         });
    }

    // Animates the disk returning to its original peg position
     function resetDiskPosition(disk, originalPegDisksDiv, originalPegContainer) {
         const gameAreaRect = gameArea.getBoundingClientRect();
         const originalPegRect = originalPegContainer.getBoundingClientRect();
         const numDisksOnOriginal = originalPegDisksDiv.children.length; // Disks still on the original peg

         // Calculate original position relative to gameArea
         const originalLeft = originalPegRect.left + (originalPegRect.width / 2) - gameAreaRect.left;
         const originalBottom = (numDisksOnOriginal * (getDiskHeight() + getDiskGap())) + parseInt(gameArea.querySelector('.base').offsetHeight);

         // Temporarily re-parent to gameArea if it was moved away
         if (disk.parentElement !== gameArea) {
              originalPegDisksDiv.removeChild(disk); // Remove from potential wrong place
              gameArea.appendChild(disk); // Add back to gameArea for positioning
              disk.style.position = 'absolute'; // Ensure it's absolute for positioning
         }


         disk.style.transition = 'none'; // Disable transition for immediate snap back before animate
         // Snap the disk's current position visually close to the target before animating
         // This prevents weird jumps if the user dragged far away
          disk.style.left = (originalLeft - disk.offsetWidth / 2) + 'px';
          disk.style.top = 'auto';
          disk.style.bottom = `${originalBottom + 50}px`; // Position slightly above final position
         disk.style.transform = 'none';


         // Now enable transition and animate it returning
         requestAnimationFrame(() => {
             requestAnimationFrame(() => {
                disk.style.transition = 'bottom 0.4s ease-in-out, left 0.4s ease-in-out, transform 0.4s ease-in-out';
                 disk.classList.remove('dragging'); // Remove dragging styles
                 disk.classList.add('moving'); // Add moving class for animation

                 // Animate to the correct final position
                 disk.style.bottom = `${originalBottom}px`; // Final vertical position

                 // Listen for the transition to end
                const onTransitionEnd = () => {
                    disk.removeEventListener('transitionend', onTransitionEnd);

                    // After animation, reset position styles and re-append to the original peg's .disks div
                    disk.style.position = '';
                    disk.style.left = '';
                    disk.style.top = '';
                    disk.style.bottom = '';
                    disk.style.transform = ''; // Restore original transform if any
                    disk.classList.remove('moving');

                    // Append back to the original peg's .disks div.
                    originalPegDisksDiv.appendChild(disk); // Append to correct parent

                    updateDraggableDisks(); // Re-evaluate draggable disks
                };
                disk.addEventListener('transitionend', onTransitionEnd);
             });
         });
     }


    // Check if the win condition is met
    function checkWinCondition() {
        const targetPegDisksDiv = appContainer.querySelector('.peg-container[data-peg-id="3"] .disks');
        if (targetPegDisksDiv.children.length === numberOfDisks) {
            // Check if all disks are on the target peg
             const minimumMoves = Math.pow(2, numberOfDisks) - 1;
            messageArea.textContent = `כל הכבוד! פתרת את הפאזל ב-${moves} מהלכים. ${moves === minimumMoves ? 'זוהי כמות המהלכים המינימלית!' : `ניתן לפתור במינימום ${minimumMoves} מהלכים.`}`;

            // Optionally disable further moves
             pegsDisksDivs.forEach(peg => {
                peg.querySelectorAll('.disk').forEach(d => d.style.pointerEvents = 'none');
             });
        }
    }

    // Event listeners for controls
    diskCountSelect.addEventListener('change', initializeGame);
    resetButton.addEventListener('click', initializeGame);

    // Event listener for explanation button
    explanationButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
            explanationDiv.style.display = 'block';
            explanationButton.textContent = 'הסתר הסבר על מגדלי האנוי';
        } else {
            explanationDiv.style.display = 'none';
            explanationButton.textContent = 'מה זה מגדלי האנוי ולמה זה מעניין?';
        }
    });


    // Initial setup when page loads
    initializeGame();
});
</script>
```