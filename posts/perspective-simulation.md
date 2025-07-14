---
title: "אשליות של עומק: חוויית פרספקטיבה אינטראקטיבית"
english_slug: "perspective-simulation"
category: "אמנות ועיצוב / כללי"
tags: [פרספקטיבה, גרפיקה, רישום, הדמיה אינטראקטיבית]
---
# אשליות של עומק: חוויית פרספקטיבה אינטראקטיבית

מכירים את התחושה הזו, כשאתם עומדים ברחוב ארוך או מול מסילת רכבת, והקווים המקבילים מתחילים להיראות כאילו הם נפגשים בנקודה רחוקה באופק? זו לא קסם – זו פרספקטיבה! היא הכלי הסודי של אמנים, אדריכלים ומעצבים ליצור עולם תלת-ממדי שקופץ אליכם מתוך משטח דו-ממדי.

כאן תוכלו לשחק בעצמכם עם העקרונות הבסיסיים של פרספקטיבה – נקודות המגוז והקווים שרצים אליהן – ולראות בזמן אמת איך הזזת נקודות אלה משנה את נקודת המבט ויוצרת אשליה של עומק בחלל. בואו נצלול פנימה ונבנה עולם משלכם!

<div id="app">
    <canvas id="perspectiveCanvas"></canvas>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        background: linear-gradient(to bottom right, #f0f4f8, #e0e7ef); /* Softer background */
        padding: 20px;
        margin: 0;
        color: #333;
        line-height: 1.7;
    }

    h1 {
        color: #2c3e50; /* Darker, more professional blue-grey */
        margin-bottom: 15px;
        text-align: center;
        font-weight: 700;
    }

    p {
        text-align: center; /* Keep center aligned for intro */
        color: #555;
        max-width: 700px;
        margin-bottom: 30px;
        line-height: 1.8; /* More space for readability */
         font-weight: 300; /* Lighter font weight for body */
    }

    #app {
        width: 100%;
        max-width: 800px;
        aspect-ratio: 4/3; /* Maintain aspect ratio */
        background-color: #ffffff;
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15); /* Softer, larger shadow */
        overflow: hidden;
        margin-bottom: 30px;
        position: relative;
        cursor: grab; /* Indicate draggable interaction */
        border: 1px solid #dcdcdc; /* Subtle border */
         transition: box-shadow 0.3s ease;
    }

    #app:hover {
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    }


    #app.dragging {
         cursor: grabbing;
         box-shadow: 0 12px 30px rgba(0, 0, 0, 0.25); /* More prominent shadow when dragging */
    }

     /* Cursor styling handled mostly in JS now for precision */
    #perspectiveCanvas {
        width: 100%;
        height: 100%;
        display: block;
    }

    #toggle-explanation {
        background-color: #3498db; /* Vibrant blue */
        color: white;
        border: none;
        padding: 14px 30px; /* Slightly larger padding */
        font-size: 1.1rem; /* Slightly larger font */
        border-radius: 8px; /* More rounded corners */
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        margin-bottom: 20px;
        font-weight: 400;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    #toggle-explanation:hover {
        background-color: #2980b9; /* Darker blue on hover */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

    #toggle-explanation:active {
        transform: scale(0.98);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    #explanation {
        background-color: #ecf0f1; /* Light grey/blue background */
        border-left: 6px solid #3498db; /* Matching blue border */
        padding: 25px; /* More padding */
        max-width: 700px;
        margin-top: 20px;
        border-radius: 8px;
        color: #333;
        line-height: 1.8;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
        animation: fadeIn 0.5s ease-out;
        text-align: right; /* Align text right for Hebrew */
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(15px); } /* More pronounced slide-in */
        to { opacity: 1; transform: translateY(0); }
    }

    #explanation h2 {
        color: #2980b9; /* Darker blue */
        margin-top: 0;
        margin-bottom: 18px; /* More space below heading */
        font-weight: 700;
        text-align: right;
    }

    #explanation p {
        text-align: right; /* Ensure paragraphs are right-aligned */
        margin-bottom: 15px; /* More space between paragraphs */
        color: #333;
        font-weight: 300;
    }

    #explanation p strong {
        font-weight: 400; /* Bold for emphasis */
        color: #2c3e50;
    }


    /* Responsive adjustments */
    @media (max-width: 768px) {
        body {
            padding: 15px;
        }
        #app {
            margin-bottom: 25px;
        }
        #explanation {
            padding: 20px;
            margin-top: 15px;
        }
        #toggle-explanation {
             padding: 12px 25px;
             font-size: 1rem;
        }
         h1 {
            font-size: 1.8em;
         }
         p {
            font-size: 0.95em;
         }
         #explanation h2 {
            font-size: 1.3em;
         }
         #explanation p {
            font-size: 0.9em;
         }
    }

    @media (max-width: 480px) {
        body {
            padding: 10px;
        }
        #app {
             border-radius: 8px;
        }
         #explanation {
            padding: 15px;
            border-radius: 5px;
        }
        #toggle-explanation {
             padding: 10px 20px;
             font-size: 0.9rem;
        }
         h1 {
            font-size: 1.5em;
         }
         p {
            font-size: 0.9em;
         }
         #explanation h2 {
            font-size: 1.2em;
         }
         #explanation p {
            font-size: 0.85em;
         }
    }

</style>

<button id="toggle-explanation">הסבר לי פרספקטיבה!</button>

<div id="explanation" style="display: none;">
    <h2>אז מה בעצם קורה פה?</h2>
    <p><strong>פרספקטיבה</strong> היא האופן שבו אנו רואים את העולם בתלת-ממד, כשהוא "מתכווץ" כשהוא מתרחק. כדי לצייר או לבנות סצנה בפרספקטיבה, אנחנו משתמשים בנקודות מפתח וקווים מנחים:</p>
    <ul>
        <li><strong>קו האופק:</strong> זהו למעשה גובה העיניים שלכם. כל דבר מעל קו האופק אתם רואים מלמטה, וכל דבר מתחתיו אתם רואים מלמעלה. שימו לב בהדמיה איך כל הנקודות הרחוקות מתכנסות אליו. <strong>גררו את קו האופק מעלה ומטה וראו איך נקודת המבט משתנה!</strong></li>
        <li><strong>נקודות מגוז (Vanishing Points):</strong> אלו הנקודות על קו האופק שאליהן נראה שכל הקווים המקבילים (כמו פסי רכבת או קווי בניין) "בורחים" ונפגשים כשהם נעלמים במרחק. ההדמיה מציגה פרספקטיבה של שתי נקודות מגוז – מצב נפוץ כשמסתכלים על פינה של בניין או רחוב. <strong>גררו את נקודות המגוז שמאלה וימינה (ושימו לב שהן נשארות על קו האופק!) וראו איך "הקירות" או "הרצפה" בהדמיה משנים צורה לחלוטין, כאילו אתם מסתובבים סביב הפינה המרכזית.</strong></li>
    </ul>
    <p>הכלי הזה מדמה את התהליך שבו אמנים חושבים כשהם בונים סצנה עם עומק. הזזת הנקודות האלו מאפשרת לכם להבין אינטואיטיבית איך מיקום הצופה ביחס לסצנה משפיע על מה שהוא רואה. נסו לשים את שתי הנקודות קרוב זו לזו, או רחוק זו מזו, אחת בקצה המסך, או אפילו שתיהן מחוץ למסך (פרספקטיבה של נקודה אחת). שחקו עם גובה האופק ושנו את זווית ה"מצלמה" הוירטואלית שלכם!</p>
</div>

<script>
    const canvas = document.getElementById('perspectiveCanvas');
    const ctx = canvas.getContext('2d');
    const appContainer = document.getElementById('app');
    const toggleButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    let vanishingPoints = [
        { x: 0, y: 0, radius: 10, isDragging: false }, // Left VP
        { x: 0, y: 0, radius: 10, isDragging: false }  // Right VP
    ];

    let horizonY = 0; // Y position of the horizon line

    let draggingPointIndex = -1; // -1: no drag, 0/1: dragging VP, -2: dragging horizon
    let offsetX, offsetY;

    // --- Drawing Parameters ---
    const pointColor = '#007bff';
    const pointStrokeColor = '#0056b3';
    const pointRadius = 10;
    const pointHitRadius = pointRadius + 15; // Larger area for click detection

    const horizonColor = '#555';
    const horizonWidth = 2;
    const horizonHitRadius = 15;

    const gridColor = '#888';
    const gridWidth = 1;
    const gridLineDash = [4, 4];

    const cornerColor = '#444';
    const cornerWidth = 2;

    const numGridLines = 10; // Number of lines on each plane

    // Define the "front" edge/corner - using a fixed vertical line as the anchor
    const cornerBaseOffset = 50; // px from bottom
    const cornerHeight = 150; // px tall
    let cornerX = 0; // Will be calculated based on canvas width

    // --- Resize canvas and initialize positions ---
    function resizeCanvas() {
        const rect = appContainer.getBoundingClientRect();
        canvas.width = rect.width;
        canvas.height = rect.height;

        // Initialize or update positions based on new size
        if (vanishingPoints[0].x === 0 || isNaN(vanishingPoints[0].x)) { // Check if not initialized or NaN
            horizonY = canvas.height * 0.5; // Start horizon in the middle
            vanishingPoints[0].x = canvas.width * 0.2; // Start left VP
            vanishingPoints[0].y = horizonY;
            vanishingPoints[1].x = canvas.width * 0.8; // Start right VP
            vanishingPoints[1].y = horizonY;
        } else {
            // Adjust positions proportionally on resize
             const widthRatio = rect.width / (canvas.width || 1); // Prevent division by zero
             const heightRatio = rect.height / (canvas.height || 1);

             vanishingPoints[0].x *= widthRatio;
             vanishingPoints[1].x *= widthRatio;
             horizonY *= heightRatio;

             // Ensure VPs stay on the *new* horizon
             vanishingPoints[0].y = horizonY;
             vanishingPoints[1].y = horizonY;

             // Constrain VPs and horizon to new bounds
             vanishingPoints[0].x = Math.max(0, Math.min(canvas.width, vanishingPoints[0].x));
             vanishingPoints[1].x = Math.max(0, Math.min(canvas.width, vanishingPoints[1].x));
             horizonY = Math.max(canvas.height * 0.1, Math.min(canvas.height * 0.9, horizonY)); // Keep horizon visible
        }

        cornerX = canvas.width * 0.5; // Keep corner roughly in the middle

        draw(); // Redraw after resize
    }

    // --- Drawing function ---
    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // --- Draw Background (Subtle Sky/Ground Gradient) ---
        const skyGradient = ctx.createLinearGradient(0, 0, 0, horizonY);
        skyGradient.addColorStop(0, '#a9d2ff'); // Light blue sky
        skyGradient.addColorStop(1, '#e9f5ff'); // Lighter blue near horizon
        ctx.fillStyle = skyGradient;
        ctx.fillRect(0, 0, canvas.width, horizonY);

        const groundGradient = ctx.createLinearGradient(0, horizonY, 0, canvas.height);
        groundGradient.addColorStop(0, '#d0d0d0'); // Light grey near horizon
        groundGradient.addColorStop(1, '#b0b0b0'); // Darker grey floor
        ctx.fillStyle = groundGradient;
        ctx.fillRect(0, horizonY, canvas.width, canvas.height - horizonY);


        // --- Draw Horizon Line ---
        ctx.strokeStyle = horizonColor;
        ctx.lineWidth = horizonWidth;
        ctx.setLineDash([]); // Ensure no dashes
        ctx.beginPath();
        ctx.moveTo(0, horizonY);
        ctx.lineTo(canvas.width, horizonY);
        ctx.stroke();

        // --- Draw Horizon Drag Indicator (if dragging) ---
        if (draggingPointIndex === -2) {
             ctx.strokeStyle = 'rgba(255, 165, 0, 0.6)'; // Orange indicator
             ctx.lineWidth = horizonWidth + 3; // Thicker
             ctx.beginPath();
             ctx.moveTo(0, horizonY);
             ctx.lineTo(canvas.width, horizonY);
             ctx.stroke();
        }

        // --- Define Central Vertical Line Points ---
        const centralBase = { x: cornerX, y: canvas.height - cornerBaseOffset };
        const centralTop = { x: cornerX, y: canvas.height - cornerBaseOffset - cornerHeight };

        // --- Draw Receding Lines from Central Corner (Defining the planes) ---
        ctx.strokeStyle = gridColor;
        ctx.lineWidth = gridWidth;
        ctx.setLineDash(gridLineDash); // Dashed lines for structure

        // Lines from centralTop to VPs
        ctx.beginPath();
        ctx.moveTo(centralTop.x, centralTop.y);
        ctx.lineTo(vanishingPoints[0].x, vanishingPoints[0].y);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(centralTop.x, centralTop.y);
        ctx.lineTo(vanishingPoints[1].x, vanishingPoints[1].y);
        ctx.stroke();

        // Lines from centralBase to VPs
        ctx.beginPath();
        ctx.moveTo(centralBase.x, centralBase.y);
        ctx.lineTo(vanishingPoints[0].x, vanishingPoints[0].y);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(centralBase.x, centralBase.y);
        ctx.lineTo(vanishingPoints[1].x, vanishingPoints[1].y);
        ctx.stroke();

        // --- Add more lines for grid effect on the planes ---
        // Lines receding towards VP1 (on the right plane) and VP2 (on the left plane)
        for(let i = 1; i < numGridLines; i++) {
            const factor = i / numGridLines; // Interpolation factor

            // Interpolate points along the central vertical line
            const interY = centralBase.y + (centralTop.y - centralBase.y) * factor;
            const interPoint = { x: cornerX, y: interY };

            // Draw lines from interpolated points to VPs
            ctx.beginPath();
            ctx.moveTo(interPoint.x, interPoint.y);
            ctx.lineTo(vanishingPoints[0].x, vanishingPoints[0].y); // Receding to VP1 (left)
            ctx.stroke();

            ctx.beginPath();
            ctx.moveTo(interPoint.x, interPoint.y);
            ctx.lineTo(vanishingPoints[1].x, vanishingPoints[1].y); // Receding to VP2 (right)
            ctx.stroke();
        }

        // --- Draw the Central Vertical Line (solid line representing the corner) ---
         ctx.strokeStyle = cornerColor;
         ctx.lineWidth = cornerWidth;
         ctx.setLineDash([]);
         ctx.beginPath();
         ctx.moveTo(centralBase.x, centralBase.y);
         ctx.lineTo(centralTop.x, centralTop.y);
         ctx.stroke();


        // --- Draw Vanishing Points ---
        vanishingPoints.forEach((vp, index) => {
             // Glow effect when dragging this point
            if(draggingPointIndex === index) {
                 ctx.beginPath();
                 ctx.arc(vp.x, vp.y, pointRadius + 10, 0, Math.PI * 2); // Larger glow area
                 ctx.fillStyle = 'rgba(0, 123, 255, 0.4)'; // Soft blue glow
                 ctx.fill();
             }

            // Outer circle/outline
             ctx.strokeStyle = pointStrokeColor;
             ctx.lineWidth = 3;
             ctx.beginPath();
             ctx.arc(vp.x, vp.y, pointRadius + 4, 0, Math.PI * 2);
             ctx.stroke();

            // Main VP circle
            ctx.beginPath();
            ctx.arc(vp.x, vp.y, pointRadius, 0, Math.PI * 2);
            ctx.fillStyle = pointColor;
            ctx.fill();

            // White center dot
            ctx.beginPath();
            ctx.arc(vp.x, vp.y, pointRadius / 2, 0, Math.PI * 2);
            ctx.fillStyle = 'white';
            ctx.fill();
        });
    } // End draw() function

    // --- Helper to get mouse/touch position relative to canvas ---
    function getPos(event) {
        const rect = canvas.getBoundingClientRect();
        const clientX = event.clientX || event.touches[0].clientX;
        const clientY = event.clientY || event.touches[0].clientY;
        return {
            x: clientX - rect.left,
            y: clientY - rect.top
        };
    }

    // --- Mouse/Touch Down Handler ---
    function handleDown(event) {
        // Prevent default touch events (like scrolling) only if a draggable element is hit
         if (event.touches && event.touches.length > 1) return; // Ignore multi-touch

        const pos = getPos(event);

        // Check VPs first
        for (let i = 0; i < vanishingPoints.length; i++) {
            const vp = vanishingPoints[i];
            const dist = Math.sqrt((pos.x - vp.x) ** 2 + (pos.y - vp.y) ** 2);
            if (dist < pointHitRadius) {
                draggingPointIndex = i;
                offsetX = pos.x - vp.x;
                offsetY = pos.y - vp.y;
                appContainer.classList.add('dragging');
                canvas.style.cursor = 'grabbing';
                 if(event.touches) event.preventDefault();
                return; // Found a VP, stop searching
            }
        }

         // If no VP was clicked, check near horizon
         if (Math.abs(pos.y - horizonY) < horizonHitRadius) {
             draggingPointIndex = -2; // Dragging horizon
             offsetY = pos.y - horizonY;
             appContainer.classList.add('dragging');
             canvas.style.cursor = 'ns-resize'; // Vertical resize cursor for horizon
             if(event.touches) event.preventDefault();
              return; // Found horizon, stop
         }

         // If nothing draggable was hit, set cursor to grab (or default)
         canvas.style.cursor = 'grab';
    }

    // --- Mouse/Touch Move Handler ---
    function handleMove(event) {
        if (draggingPointIndex === -1) return; // Not dragging anything

         if (event.touches && event.touches.length > 1) return; // Ignore multi-touch

        const pos = getPos(event);

        if (draggingPointIndex === -2) { // Dragging horizon
            horizonY = pos.y - offsetY;
            // Constrain horizon within canvas bounds (with padding)
            horizonY = Math.max(canvas.height * 0.05, Math.min(canvas.height * 0.95, horizonY));

             // Keep VPs locked onto the horizon line
            vanishingPoints.forEach(vp => vp.y = horizonY);

        } else if (draggingPointIndex !== -1) { // Dragging a VP (0 or 1)
            const vp = vanishingPoints[draggingPointIndex];
            vp.x = pos.x - offsetX;
            // VPs are constrained to the horizon line, so their Y is always horizonY
            vp.y = horizonY;

            // Constrain VP X within canvas bounds
             vp.x = Math.max(0, Math.min(canvas.width, vp.x));
             // Y is already constrained by horizonY

        }

         if(event.touches) event.preventDefault(); // Prevent scrolling while dragging
        requestAnimationFrame(draw); // Redraw for smooth movement
    }

    // --- Mouse/Touch Up Handler ---
    function handleUp() {
        draggingPointIndex = -1;
        appContainer.classList.remove('dragging');
        canvas.style.cursor = 'grab'; // Reset cursor after drag
    }

    // --- Event Listeners ---
    window.addEventListener('resize', resizeCanvas);

    // Mouse listeners
    canvas.addEventListener('mousedown', handleDown);
    document.addEventListener('mousemove', handleMove);
    document.addEventListener('mouseup', handleUp);

     // Touch listeners
    canvas.addEventListener('touchstart', handleDown);
    document.addEventListener('touchmove', handleMove);
    document.addEventListener('touchend', handleUp);
    document.addEventListener('touchcancel', handleUp); // Handle cases where touch ends unexpectedly


    // Toggle explanation visibility
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר' : 'הסבר לי פרספקטיבה!'; /* Updated text */

        // Scroll to explanation if revealed on smaller screens
         if (isHidden && window.innerWidth < 768) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });


    // Initial setup
    resizeCanvas(); // Set initial size and draw
</script>