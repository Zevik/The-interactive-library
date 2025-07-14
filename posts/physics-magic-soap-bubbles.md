---
title: "קסם הפיזיקה בבועות סבון"
english_slug: physics-magic-soap-bubbles
category: "מדעים מדויקים / פיזיקה"
tags:
  - פיזיקה
  - בועות סבון
  - מתח פנים
  - אינטראקציה
  - סימולציה
  - חוויה לימודית
---
# קסם הפיזיקה בבועות סבון

בועות סבון - הן מרצדות, צבעוניות, ונעלמות ברגע, ונראות כמו הדבר הכי פשוט שיש. אבל מתחת למעטה הדק והשברירי מסתתר עולם מופלא של כוחות פיזיקליים שפועלים באיזון מושלם. האם אי פעם עצרתם לתהות למה בועה בודדת היא תמיד כדורית? או איך קורה שכאשר בועות נפגשות, הן מתחברות בזוויות מדויקות באופן בלתי רגיל?

התנסו בעצמכם ובואו לגלות את הסוד!

<div id="simulation-container">
    <!-- Placeholder for drawing surface tension lines or junctions dynamically -->
    <svg id="bubble-lines" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 2; pointer-events: none;"></svg>
    <p>לחצו וגררו בעכבר (או געו וגררו באצבע) במרחב הפתוח כדי ליצור בועות בגדלים שונים. גררו בועות קיימות כדי להזיז אותן ולצפות איך הן מגיבות כשהן נפגשות!</p>
    <div id="controls">
        <button id="clear-bubbles">נקה הכל</button>
    </div>
    <!-- Bubbles will be added here by JavaScript -->
</div>

<style>
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

body {
    font-family: 'Heebo', sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f0f8ff; /* Light, airy background */
    padding: 20px;
    max-width: 800px;
    margin: 0 auto;
}

h1, h2, h3 {
    color: #004085; /* Darker blue */
    text-align: center;
}

#simulation-container {
    width: 100%;
    height: 450px; /* Slightly taller */
    border: 3px solid #007bff; /* More prominent border */
    border-radius: 10px; /* Rounded corners */
    position: relative;
    overflow: hidden;
    background: linear-gradient(to bottom right, #e0f7fa, #b3e5fc); /* Gentle gradient */
    cursor: crosshair;
    user-select: none;
    touch-action: none;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    margin-bottom: 20px;
}

#simulation-container p {
    text-align: center;
    margin: 20px auto 10px; /* More space */
    color: #0056b3; /* Blue text */
    font-size: 1.1em;
    font-weight: bold;
    max-width: 80%;
}

#controls {
    position: absolute;
    top: 15px;
    right: 15px;
    z-index: 10;
}

#controls button, #explanation-button {
    padding: 10px 20px;
    cursor: pointer;
    background-color: #007bff; /* Primary blue */
    color: white;
    border: none;
    border-radius: 25px; /* Pill shape */
    font-size: 1em;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    font-family: 'Heebo', sans-serif;
    font-weight: 400;
}

#controls button:hover, #explanation-button:hover {
    background-color: #0056b3; /* Darker blue on hover */
    transform: translateY(-1px); /* Slight lift */
}

#controls button:active, #explanation-button:active {
    background-color: #004085; /* Even darker on active */
    transform: translateY(0);
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}


.bubble {
    position: absolute;
    border-radius: 50%;
    /* Enhanced bubble appearance */
    background: radial-gradient(circle at 25% 25%, rgba(255, 255, 255, 0.8), rgba(173, 216, 230, 0.6), rgba(0, 102, 204, 0.4));
    border: 2px solid rgba(0, 102, 204, 0.8);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2), inset 0 0 10px rgba(255, 255, 255, 0.5); /* Multiple shadows for depth */
    cursor: grab;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 0.8em;
    color: #333;
    z-index: 3; /* Bubbles above lines */
    transition: transform 0.2s ease-out, left 0.05s linear, top 0.05s linear; /* Faster position, smoother scale */
    will-change: transform, left, top; /* Hint for performance */
}

.bubble:active {
    cursor: grabbing;
    transform: scale(1.05); /* Slight scale up when dragging */
    z-index: 10; /* Bring dragged bubble to front */
}

/* Visual indicator for overlapping bubbles - not full simulation */
.bubble.overlapping {
    border-color: #ff9800; /* Orange border */
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3), inset 0 0 15px rgba(255, 255, 255, 0.7), 0 0 10px #ffb74d; /* Glow effect */
    animation: pulse-border 1s infinite alternate;
}

@keyframes pulse-border {
    from { border-color: rgba(0, 102, 204, 0.8); }
    to { border-color: rgba(255, 152, 0, 1); }
}


/* Style for the simulated "walls" between bubbles */
/* Using SVG lines drawn by JS for better visual control */
#bubble-lines line {
    stroke: rgba(0, 102, 204, 0.8); /* Blue lines */
    stroke-width: 3;
    stroke-linecap: round;
    transition: stroke-dashoffset 0.3s ease-out; /* For draw effect */
}

/* Style for junction markers */
.junction-marker {
    position: absolute;
    width: 15px;
    height: 15px;
    background-color: #ffeb3b; /* Bright yellow */
    border: 2px solid #fbc02d; /* Darker yellow border */
    border-radius: 50%;
    z-index: 5; /* Above lines, below dragged bubble */
    transform: translate(-50%, -50%); /* Center the div on the point */
    box-shadow: 0 0 8px rgba(255, 235, 59, 0.8); /* Glow */
    pointer-events: none; /* Don't interfere with mouse events */
}


#explanation-button {
    display: block;
    width: fit-content;
    margin: 20px auto;
    background-color: #28a745; /* Green button */
    transition: background-color 0.3s ease, transform 0.1s ease;
}

#explanation-button:hover {
     background-color: #218838; /* Darker green */
}

#explanation-button:active {
     background-color: #1e7e34; /* Even darker */
}


#explanation {
    margin-top: 20px;
    padding: 20px; /* More padding */
    border: 1px solid #b3e5fc; /* Light blue border */
    background-color: #e1f5fe; /* Very light blue background */
    border-radius: 8px;
    display: none; /* Initially hidden */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

#explanation h2 {
    color: #0277bd; /* A different shade of blue */
    margin-top: 0; /* Remove top margin for first heading */
    margin-bottom: 10px;
    border-bottom: 2px solid #b3e5fc; /* Underline heading */
    padding-bottom: 5px;
}

#explanation h3 {
    color: #03a9f4; /* Lighter blue for subheadings */
    margin-top: 15px;
    margin-bottom: 8px;
}

#explanation p {
    line-height: 1.7; /* Increased line height */
    margin-bottom: 12px;
    color: #333;
}

#explanation ul {
    margin-bottom: 12px;
    padding-left: 25px; /* More indent */
}

#explanation li {
    margin-bottom: 6px;
    color: #333;
}
</style>

<button id="explanation-button">גלו את סודות הפיזיקה של בועות הסבון</button>

<div id="explanation">
    <h2>הקסם מתגלה: הפיזיקה שמאחורי הבועות</h2>

    <p>האינטראקציה שחוויתם בסימולציה מדגימה עקרונות יסוד בעולם הנוזלים, ובעיקר את כוחו של **מתח פנים**.</p>

    <h3>מתח פנים: יריעה בלתי נראית</h3>
    <p>דמיינו את פני השטח של הנוזל כ"יריעה" דקה ומתוחה. זהו מתח הפנים! הוא נובע מהמשיכה החזקה יותר בין מולקולות הנוזל לבין עצמן, לעומת המשיכה שלהן למולקולות האוויר שמסביב. מולקולות בפנים הנוזל נמשכות לכל הכיוונים, אך מולקולות על פני השטח נמשכות בעיקר פנימה ולצדדים. כוח נטו זה גורם לפני השטח להתכווץ ככל הניתן - בדומה לבלון שמנסה להתכווץ.</p>

    <h3>צורת הכדור: המינימום המושלם</h3>
    <p>עקרון מפתח שפועל בבועות סבון הוא **מינימליזציית שטח פנים**. בהינתן נפח מסוים של אוויר הלכוד בתוך קרום הסבון (שכבת מים דקה בין שתי שכבות סבון), מתח הפנים גורם לקרום הזה לשאוף לצורה בעלת שטח הפנים הקטן ביותר עבור אותו נפח. באופן מדהים, הצורה הגיאומטרית שבעלת שטח פנים מינימלי לנפח נתון היא... **כדור**! זו הסיבה הפשוטה והאלגנטית לכך שבועת סבון בודדת תמיד מקבלת צורה כדורית.</p>

    <h3>הריקוד המשותף: מפגש בועות וכלל 120 המעלות</h3>
    <p>כאשר שתי בועות נפגשות ומתמזגות, הן יוצרות דופן משותפת. גם כאן, הפיזיקה דורשת שמערכת הבועות השלמה תמזער את שטח הפנים הכולל שלה. אם בסימולציה הצלחתם להפגיש שלוש בועות שיצרו נקודת מפגש משותפת, ייתכן ושמתם לב (או שתשימו לב בניסיון הבא!) שהקירות המשותפים שלהן נוטים להיפגש בנקודה אחת, ושהזוויות בין שלושת הקירות הללו הן תמיד, אבל תמיד, **120 מעלות בדיוק**! זהו כלל גיאומטרי הנובע ישירות מעקרון מינימליזציית שטח הפנים, ומבטיח את התצורה היציבה ביותר מבחינה אנרגטית.</p>
    <ul>
        <li>**שתי בועות:** נפגשות ויוצרות קיר ישר (לרוב).</li>
        <li>**שלוש בועות:** יוצרות צומת יחיד בו שלושה קירות נפגשים בזוויות של 120°.</li>
        <li>**ארבע בועות ומעלה:** יתארגנו במהירות לצמתים של שלוש בועות בלבד, כל אחת בזווית 120°. זו הסיבה שמבני קצף מורכבים בנויים מרשת של צמתים כאלה.</li>
    </ul>

    <h3>מדוע בועות קטנות "נבלעות" על ידי גדולות?</h3>
    <p>הלחץ בתוך בועת סבון תמיד גבוה יותר מהלחץ מחוצה לה. ההפרש הזה תלוי במתח הפנים וברדיוס הבועה (זהו חוק לאפלאס). ככל שהבועה קטנה יותר (רדיוס קטן יותר), כך הלחץ הפנימי בה **גבוה יותר**. כאשר בועה קטנה ובועה גדולה מתחברות עם דופן משותפת, נוצר חיבור בין אזור לחץ גבוה (הבועה הקטנה) לאזור לחץ נמוך (הבועה הגדולה). האוויר זורם מהבועה הקטנה לגדולה דרך הדופן המשותפת, עד שהבועה הקטנה "נעלמת" ומתמזגת לחלוטין עם הבועה הגדולה יותר. נסו ליצור בועה קטנה סמוך לגדולה ולראות מה קורה!</p>

    <h3>פיזיקה בטבע</h3>
    <p>עקרונות אלו של מינימליזציית שטח פנים ונטייה לזוויות 120 מעלות אינם ייחודיים לבועות סבון. הם מופיעים גם במבנים טבעיים אחרים, כמו התאים המשושים המפורסמים בחלת דבש של דבורים. מבנה זה מאפשר לרצף את המישור (למלא שטח) ביעילות מירבית תוך שימוש מינימלי בחומר (שעווה לדפנות), ושוב, בכל קודקוד של חלת הדבש נפגשות שלוש דפנות בזווית של 120 מעלות!</p>

    <p>אז בפעם הבאה שאתם רואים בועת סבון, זכרו שאתם עדים להדגמה יומיומית ויפהפייה של עקרונות פיזיקליים אלגנטיים!</p>
</div>


<script>
document.addEventListener('DOMContentLoaded', () => {
    const simulationContainer = document.getElementById('simulation-container');
    const bubbleLinesSVG = document.getElementById('bubble-lines');
    const clearButton = document.getElementById('clear-bubbles');
    const explanationButton = document.getElementById('explanation-button');
    const explanationDiv = document.getElementById('explanation');

    let isDragging = false;
    let currentBubble = null; // The bubble being created or dragged
    let startX, startY; // Initial mouse/touch position
    let initialBubbleX, initialBubbleY; // Initial position of existing bubble

    // --- Utility Functions ---
    function getBubbleData(bubbleElement) {
        const rect = bubbleElement.getBoundingClientRect();
        const containerRect = simulationContainer.getBoundingClientRect();
        return {
            element: bubbleElement,
            x: rect.left + rect.width / 2 - containerRect.left,
            y: rect.top + rect.height / 2 - containerRect.top,
            radius: rect.width / 2 // Assuming width == height
        };
    }

    function distance(b1, b2) {
        return Math.sqrt(Math.pow(b1.x - b2.x, 2) + Math.pow(b1.y - b2.y, 2));
    }

     function areOverlapping(b1, b2, threshold = 5) { // Add a small threshold for detecting overlap
        // Overlap if distance between centers is less than sum of radii minus a threshold
        return distance(b1, b2) < (b1.radius + b2.radius - threshold);
    }

     function getCentroid(points) {
        let xSum = 0, ySum = 0;
        points.forEach(p => {
            xSum += p.x;
            ySum += p.y;
        });
        return { x: xSum / points.length, y: ySum / points.length };
    }


    // --- Visuals Update ---
    function updateVisualizations() {
        // Clear previous lines and markers
        bubbleLinesSVG.innerHTML = '';
        simulationContainer.querySelectorAll('.junction-marker').forEach(marker => marker.remove());
        simulationContainer.querySelectorAll('.bubble').forEach(bubble => bubble.classList.remove('overlapping'));


        const bubbles = Array.from(simulationContainer.querySelectorAll('.bubble'));
        if (bubbles.length < 2) return;

        const bubbleData = bubbles.map(getBubbleData);
        const overlappingPairs = [];
        const overlappingBubblesSet = new Set(); // To add 'overlapping' class

        // Detect pairwise overlaps and add overlapping class
        for (let i = 0; i < bubbleData.length; i++) {
            for (let j = i + 1; j < bubbleData.length; j++) {
                if (areOverlapping(bubbleData[i], bubbleData[j], 10)) { // Use a slightly larger threshold for visual overlap
                    overlappingPairs.push([i, j]);
                    overlappingBubblesSet.add(bubbleData[i].element);
                    overlappingBubblesSet.add(bubbleData[j].element);

                    // Basic line representation between centers (simplified wall hint)
                    // This is a visual hint, not a physics simulation of the wall curve
                     const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
                     line.setAttribute('x1', bubbleData[i].x);
                     line.setAttribute('y1', bubbleData[i].y);
                     line.setAttribute('x2', bubbleData[j].x);
                     line.setAttribute('y2', bubbleData[j].y);
                     bubbleLinesSVG.appendChild(line);
                }
            }
        }

        overlappingBubblesSet.forEach(bubble => bubble.classList.add('overlapping'));

        // --- Simplified Triple Junction Detection & Marker ---
        // This is a heuristic, not a physics-based detection of the exact 120-degree point.
        // We look for groups of 3 bubbles that are pairwise overlapping and relatively close to each other.
        const potentialJunctions = new Set(); // Store string representations like "idx1,idx2,idx3"

        for (let i = 0; i < bubbleData.length; i++) {
            for (let j = i + 1; j < bubbleData.length; j++) {
                 for (let k = j + 1; k < bubbleData.length; k++) {
                     // Check if all three pairs overlap
                     const overlaps_ij = areOverlapping(bubbleData[i], bubbleData[j], 5);
                     const overlaps_ik = areOverlapping(bubbleData[i], bubbleData[k], 5);
                     const overlaps_jk = areOverlapping(bubbleData[j], bubbleData[k], 5);

                     if (overlaps_ij && overlaps_ik && overlaps_jk) {
                         // Check if their centers form a relatively small triangle (suggesting a common meeting point)
                         const maxPairwiseDistance = Math.max(
                             distance(bubbleData[i], bubbleData[j]),
                             distance(bubbleData[i], bubbleData[k]),
                             distance(bubbleData[j], bubbleData[k])
                         );
                         const avgRadius = (bubbleData[i].radius + bubbleData[j].radius + bubbleData[k].radius) / 3;

                         // Heuristic: if max distance between centers is less than, say, 1.5 times average radius,
                         // they are likely forming a junction point. Adjust factor as needed.
                         if (maxPairwiseDistance < avgRadius * 1.5) {
                             const indices = [i, j, k].sort((a, b) => a - b);
                             const junctionKey = indices.join(','); // Use sorted indices as key

                             if (!potentialJunctions.has(junctionKey)) {
                                 potentialJunctions.add(junctionKey);
                                 // Place a marker at the centroid of the three bubble centers
                                 const centroid = getCentroid([bubbleData[i], bubbleData[j], bubbleData[k]]);
                                 const marker = document.createElement('div');
                                 marker.classList.add('junction-marker');
                                 marker.style.left = `${centroid.x}px`;
                                 marker.style.top = `${centroid.y}px`;
                                 simulationContainer.appendChild(marker);
                             }
                         }
                     }
                 }
            }
        }
    }


    // --- Event Handlers ---

    // Toggle explanation visibility
    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר הסבר פיזיקלי' : 'גלו את סודות הפיזיקה של בועות הסבון';
    });

    // Start creating/dragging
    simulationContainer.addEventListener('mousedown', (e) => {
        // Only start if clicking inside the container, not on a bubble or control
        if (e.target === simulationContainer || e.target.tagName === 'P' || e.target.tagName === 'svg') {
            // Start creating a new bubble
            isDragging = true;
            startX = e.clientX;
            startY = e.clientY;

            const bubble = document.createElement('div');
            bubble.classList.add('bubble');
            // Position at start of drag (will be updated on move)
            const containerRect = simulationContainer.getBoundingClientRect();
            bubble.style.left = `${e.clientX - containerRect.left - 30}px`; // Initial rough center guess
            bubble.style.top = `${e.clientY - containerRect.top - 30}px`; // Initial rough center guess
            bubble.style.width = '0px';
            bubble.style.height = '0px';
            bubble.style.opacity = '0.8'; // Subtle initial opacity


            simulationContainer.appendChild(bubble);
            currentBubble = bubble;

            document.addEventListener('mousemove', onMouseMove);
            document.addEventListener('mouseup', onMouseUp);
            // Prevent default behavior like text selection
            e.preventDefault();

        } else if (e.target.classList.contains('bubble')) {
            // Start dragging an existing bubble
            isDragging = true;
            currentBubble = e.target;
            startX = e.clientX;
            startY = e.clientY;
            initialBubbleX = currentBubble.offsetLeft;
            initialBubbleY = currentBubble.offsetTop;

            // Add a class or style to indicate dragging (e.g., active state handles transform/z-index)
            currentBubble.classList.add('active');


            document.addEventListener('mousemove', onMouseMove);
            document.addEventListener('mouseup', onMouseUp);

            // Prevent default drag behavior on the bubble itself
            e.preventDefault();
        }
    });

     // Handle touch events for creating/dragging
     simulationContainer.addEventListener('touchstart', (e) => {
         // Only start if touching inside the container, not on a bubble or control
         if (e.target === simulationContainer || e.target.tagName === 'P' || e.target.tagName === 'svg') {
             const touch = e.touches[0];
              // Start creating a new bubble
             isDragging = true;
             startX = touch.clientX;
             startY = touch.clientY;

             const bubble = document.createElement('div');
             bubble.classList.add('bubble');
             const containerRect = simulationContainer.getBoundingClientRect();
             bubble.style.left = `${touch.clientX - containerRect.left - 30}px`;
             bubble.style.top = `${touch.clientY - containerRect.top - 30}px`;
              bubble.style.width = '0px';
              bubble.style.height = '0px';
              bubble.style.opacity = '0.8';

             simulationContainer.appendChild(bubble);
             currentBubble = bubble;

             document.addEventListener('touchmove', onTouchMove);
             document.addEventListener('touchend', onTouchEnd);
             e.preventDefault(); // Prevent scrolling
         } else if (e.target.classList.contains('bubble')) {
              const touch = e.touches[0];
              // Start dragging an existing bubble
              isDragging = true;
              currentBubble = e.target;
              startX = touch.clientX;
              startY = touch.clientY;
              initialBubbleX = currentBubble.offsetLeft;
              initialBubbleY = currentBubble.offsetTop;

              currentBubble.classList.add('active');

              document.addEventListener('touchmove', onTouchMove);
              document.addEventListener('touchend', onTouchEnd);
              e.preventDefault(); // Prevent scrolling/default touch actions
         }
     });


    function onMouseMove(e) {
        if (!isDragging || !currentBubble) return;

        const containerRect = simulationContainer.getBoundingClientRect();
        const currentX = e.clientX;
        const currentY = e.clientY;

        // Check if we are resizing a newly created bubble or moving an existing one
        // We know it's a new bubble if its size is still 0x0
        const isCreating = currentBubble.offsetWidth === 0 && currentBubble.offsetHeight === 0;


        if (isCreating) {
            // Resizing a new bubble
            const dx = currentX - startX;
            const dy = currentY - startY;
            const size = Math.sqrt(dx * dx + dy + dy); // Use distance from start point
            // Set size, ensuring it doesn't go below a minimum or exceed container bounds
            const minSize = 30;
            const maxSize = Math.min(containerRect.width, containerRect.height) / 2; // Don't exceed half container size
            const finalSize = Math.max(minSize, Math.min(size * 2, maxSize)); // Scale size based on drag distance

            currentBubble.style.width = `${finalSize}px`;
            currentBubble.style.height = `${finalSize}px`;
            // Position the bubble so its center is near the start point
            currentBubble.style.left = `${startX - containerRect.left - finalSize / 2}px`;
            currentBubble.style.top = `${startY - containerRect.top - finalSize / 2}px`;


        } else {
            // Moving an existing bubble
            const dx = currentX - startX;
            const dy = currentY - startY;

            let newX = initialBubbleX + dx;
            let newY = initialBubbleY + dy;

            // Keep bubble within container bounds
            const bubbleSize = currentBubble.offsetWidth; // Assuming width and height are equal
             const containerWidth = containerRect.width;
             const containerHeight = containerRect.height;


            newX = Math.max(0, Math.min(newX, containerWidth - bubbleSize));
            newY = Math.max(0, Math.min(newY, containerHeight - bubbleSize));

            currentBubble.style.left = `${newX}px`;
            currentBubble.style.top = `${newY}px`;
        }
    }

    function onTouchMove(e) {
         if (!isDragging || !currentBubble) return;
         const touch = e.touches[0];
         const containerRect = simulationContainer.getBoundingClientRect();
         const currentX = touch.clientX;
         const currentY = touch.clientY;

         const isCreating = currentBubble.offsetWidth === 0 && currentBubble.offsetHeight === 0;


         if (isCreating) {
             // Resizing a new bubble
             const dx = currentX - startX;
             const dy = currentY - startY;
             const size = Math.sqrt(dx * dx + dy * dy);
             const minSize = 30;
             const maxSize = Math.min(containerRect.width, containerRect.height) / 2;
             const finalSize = Math.max(minSize, Math.min(size * 2, maxSize));


             currentBubble.style.width = `${finalSize}px`;
             currentBubble.style.height = `${finalSize}px`;
             currentBubble.style.left = `${startX - containerRect.left - finalSize / 2}px`;
             currentBubble.style.top = `${startY - containerRect.top - finalSize / 2}px`;
         } else {
             // Moving an existing bubble
             const dx = currentX - startX;
             const dy = currentY - startY;

             let newX = initialBubbleX + dx;
             let newY = initialBubbleY + dy;

             const bubbleSize = currentBubble.offsetWidth;
             const containerWidth = containerRect.width;
             const containerHeight = containerRect.height;

             newX = Math.max(0, Math.min(newX, containerWidth - bubbleSize));
             newY = Math.max(0, Math.min(newY, containerHeight - bubbleSize));

             currentBubble.style.left = `${newX}px`;
             currentBubble.style.top = `${newY}px`;
         }
         e.preventDefault(); // Prevent scrolling
    }

    function onMouseUp() {
        if (!isDragging) return;
        isDragging = false;

        if (currentBubble) {
             // If it was a click (size is 0), create a default size bubble
             if (currentBubble.offsetWidth < 30) { // Check against minSize
                 const size = 60; // Default size for a quick click
                 const containerRect = simulationContainer.getBoundingClientRect();
                 currentBubble.style.width = `${size}px`;
                 currentBubble.style.height = `${size}px`;
                 // Center it where the click occurred (based on initial startX/startY)
                 currentBubble.style.left = `${startX - containerRect.left - size / 2}px`;
                 currentBubble.style.top = `${startY - containerRect.top - size / 2}px`;
             }

             // Ensure opacity is 1 after creation
             currentBubble.style.opacity = '1';

            // Remove active state/class
            currentBubble.classList.remove('active');


            // Check for overlaps and update visualizations
            updateVisualizations();

            currentBubble = null;
        }

        document.removeEventListener('mousemove', onMouseMove);
        document.removeEventListener('mouseup', onMouseUp);
    }

    function onTouchEnd() {
        if (!isDragging) return;
        isDragging = false;

         if (currentBubble) {
              // If it was a quick touch (size is 0), create a default size bubble
              if (currentBubble.offsetWidth < 30) {
                 const size = 60; // Default size for a quick touch
                 const containerRect = simulationContainer.getBoundingClientRect();
                 currentBubble.style.width = `${size}px`;
                 currentBubble.style.height = `${size}px`;
                  // Center it where the touch occurred (based on initial startX/startY)
                  currentBubble.style.left = `${startX - containerRect.left - size / 2}px`;
                  currentBubble.style.top = `${startY - containerRect.top - size / 2}px`;
              }

              // Ensure opacity is 1 after creation
              currentBubble.style.opacity = '1';

             currentBubble.classList.remove('active');

             // Check for overlaps and update visualizations
             updateVisualizations();

             currentBubble = null;
         }
         document.removeEventListener('touchmove', onTouchMove);
         document.removeEventListener('touchend', onTouchEnd);
    }


    // Clear all bubbles and visualizations
    clearButton.addEventListener('click', () => {
        simulationContainer.querySelectorAll('.bubble').forEach(bubble => bubble.remove());
        updateVisualizations(); // Clear lines and markers as well
    });

     // Initial visualization update in case there are pre-existing bubbles (though none in this setup)
     // updateVisualizations(); // No needed as container starts empty
});
</script>
```