---
---
---
title: "מסע אל תוך פרקטלים: יוצרים את משולש שרפינסקי"
english_slug: interactive-sierpinski-fractal
category: "מתמטיקה ויזואלית"
tags: [פרקטלים, גיאומטריה, הדמיה, אינטראקטיבי, משחק הכאוס]
---
<h1>מסע אל תוך פרקטלים: יוצרים את משולש שרפינסקי</h1>

<p>היכנסו לעולם המרתק של פרקטלים - צורות קסומות שחוזרות על עצמן בכל קנה מידה! גלו כיצד אפשר לבנות מורכבות מדהימה מכללים פשוטים שחוזרים על עצמם. במשחק הזה, תוכלו להתנסות בעצמכם ולצייר את משולש שרפינסקי המפורסם באמצעות שיטה מפתיעה ומבוססת אקראיות.</p>

<div class="app-container">
    <canvas id="sierpinskiCanvas" width="600" height="600"></canvas>
    <div class="controls">
        <label for="pointCount">כמה נקודות נצייר?</label>
        <input type="range" id="pointCount" min="1000" max="500000" value="50000" step="1000">
        <span id="currentPointCount">50,000</span>
         <div class="control-buttons">
             <button id="drawButton">צייר מהר</button>
             <button id="animateButton">הצג צעד-אחר-צעד</button>
         </div>

    </div>
     <div id="drawingProgress"></div>
</div>

<style>
    :root {
        --primary-color: #4a90e2; /* Softer Blue */
        --secondary-color: #8d8d8d; /* Muted Grey */
        --background-color: #f0f4f8; /* Light Blue-Grey */
        --card-background: #ffffff;
        --border-color: #d1d8e0; /* Light Grey-Blue */
        --text-color: #333333;
        --accent-color: #50e3c2; /* Teal */
        --success-color: #7ed321; /* Green */
        --danger-color: #e05038; /* Red */
        --vertex-color-1: #f5a623; /* Orange */
        --vertex-color-2: #bd10e0; /* Purple */
        --vertex-color-3: #4a90e2; /* Blue */
    }

    body {
        font-family: 'Varela Round', 'Arial', sans-serif; /* Added Varela Round */
        line-height: 1.8; /* Increased line height */
        color: var(--text-color);
        background-color: var(--background-color);
        margin: 0;
        padding: 20px;
        direction: rtl;
        text-align: right;
        overflow-x: hidden; /* Prevent horizontal scroll */
    }

    h1, h2 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 25px; /* Increased margin */
         font-weight: bold;
    }

    p {
        margin-bottom: 20px; /* Increased margin */
        max-width: 800px; /* Limit text width */
        margin-left: auto;
        margin-right: auto;
    }

    .app-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 25px; /* Increased gap */
        margin-top: 40px; /* Increased margin */
        padding: 30px; /* Increased padding */
        background-color: var(--card-background);
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Stronger shadow */
        max-width: 650px; /* Limit container width */
        margin-left: auto;
        margin-right: auto;
    }

    #sierpinskiCanvas {
        border: 1px solid var(--border-color);
        background-color: #fff;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08); /* Refined shadow */
        display: block;
         border-radius: 8px; /* Match container style */
    }

    .controls {
        width: 100%;
        max-width: 600px;
        display: flex;
        flex-direction: column; /* Stack controls vertically */
        align-items: center;
        gap: 20px; /* Increased gap */
    }

    .controls label {
        font-weight: bold;
        margin-bottom: 5px; /* Space below label */
        display: block; /* Make label block */
        width: 100%;
        text-align: center;
    }

    .controls input[type="range"] {
        width: 100%; /* Full width */
        -webkit-appearance: none;
        appearance: none;
        height: 10px; /* Thicker slider */
        background: var(--border-color);
        outline: none;
        opacity: 0.8; /* Slightly less opaque */
        transition: opacity .2s;
        border-radius: 5px; /* More rounded slider track */
    }

    .controls input[type="range"]:hover {
        opacity: 1;
    }

    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 24px; /* Larger thumb */
        height: 24px; /* Larger thumb */
        background: var(--accent-color);
        cursor: grab; /* Grab cursor */
        border-radius: 50%;
        transition: background 0.3s ease, transform 0.1s ease;
        border: 3px solid var(--card-background); /* White border */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Thumb shadow */
    }

     .controls input[type="range"]::-webkit-slider-thumb:active {
         cursor: grabbing; /* Grabbing cursor */
         transform: scale(1.1); /* Slight scale on press */
     }


    .controls input[type="range"]::-moz-range-thumb {
        width: 24px; /* Larger thumb */
        height: 24px; /* Larger thumb */
        background: var(--accent-color);
        cursor: grab;
        border-radius: 50%;
         transition: background 0.3s ease, transform 0.1s ease;
         border: 3px solid var(--card-background); /* White border */
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Thumb shadow */
    }

     .controls input[type="range"]::-moz-range-thumb:active {
         cursor: grabbing;
         transform: scale(1.1);
     }


    .controls span {
        min-width: 80px; /* Wider span for count */
        text-align: center;
        font-weight: bold;
        font-size: 1.1rem; /* Slightly larger font */
        color: var(--primary-color); /* Use primary color */
    }

    .control-buttons {
        display: flex;
        gap: 15px; /* Space between buttons */
        justify-content: center;
        width: 100%;
    }


    button {
        padding: 12px 24px; /* More padding */
        font-size: 1.05rem; /* Slightly larger font */
        color: white;
        background-color: var(--accent-color);
        border: none;
        border-radius: 6px; /* More rounded */
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.2s ease; /* Added shadow transition */
        font-weight: bold;
        flex-grow: 1; /* Buttons grow */
        max-width: 180px; /* Max width for buttons */
    }

    button:hover {
        background-color: #43b9a2; /* Darker teal */
        transform: translateY(-2px); /* More pronounced lift */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15); /* Add shadow on hover */
    }

    button:active {
         transform: translateY(0);
         background-color: #3a9d87; /* Even darker */
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Smaller shadow on press */
    }

    #animateButton {
        background-color: var(--primary-color); /* Different color for animate */
    }

     #animateButton:hover {
        background-color: #3a7dc2; /* Darker blue */
     }

    #animateButton:active {
        background-color: #326fa8; /* Even darker */
    }

     #drawingProgress {
         margin-top: 15px;
         font-size: 1rem;
         font-weight: bold;
         color: var(--primary-color);
         min-height: 1.2em; /* Reserve space */
         text-align: center;
     }


     #toggleExplanation {
         display: block;
         margin: 30px auto 15px auto;
         background-color: var(--secondary-color);
         width: auto;
         max-width: 250px; /* Wider button */
         font-size: 1rem;
         padding: 10px 20px;
         border-radius: 6px;
         text-align: center;
     }

    #toggleExplanation:hover {
        background-color: #707070;
    }

    #explanation {
        margin-top: 20px;
        padding: 30px; /* Increased padding */
        background-color: var(--card-background);
        border-radius: 12px; /* Match app container */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        border-top: 4px solid var(--success-color); /* Changed border color */
        opacity: 0; /* Start hidden */
        max-height: 0; /* Start collapsed */
        overflow: hidden; /* Hide content overflow during transition */
        transition: opacity 0.6s ease-out, max-height 0.6s ease-out; /* Smooth transition */
    }

    #explanation.visible {
        opacity: 1;
        max-height: 1000px; /* Needs to be large enough to contain content */
    }

    #explanation ol, #explanation ul {
        margin-left: 20px; /* Indent lists */
        padding-right: 0; /* Remove default padding */
    }

     #explanation li {
         margin-bottom: 10px;
     }

    #explanation ul li {
        list-style-type: disc; /* Disc for nested list */
    }

    /* Add specific styles for vertex visualization on canvas if needed */
    /* (Done in JS by drawing shapes) */

</style>

<button id="toggleExplanation">הצג/הסתר את סוד הקסם</button>

<div id="explanation">
    <h2>מהו משולש שרפינסקי ואיך נוצר הקסם?</h2>
    <p>משולש שרפינסקי הוא אחד הפרקטלים המפורסמים והיפים ביותר. הוא דוגמה קלאסית לצורה שמוגדרת על ידי חזרה אינסופית של אותו כלל פשוט - תהליך שנקרא אִיטֶרַצְיָה. בבנייה המסורתית, מתחילים ממשולש שווה צלעות, מחלקים אותו לארבעה משולשים קטנים יותר על ידי חיבור נקודות האמצע של הצלעות, ומסירים את המשולש המרכזי. חוזרים על התהליך הזה שוב ושוב על שלושת המשולשים שנותרו, עד אינסוף!</p>

    <h2>שיטת 'משחק הכאוס' - היופי שבמקריות</h2>
    <p>ההדמיה שלפניך נוצרת בשיטה מפתיעה לחלוטין, שנקראת "משחק הכאוס" (Chaos Game). במקום להסיר משולשים, אנחנו פשוט... מציירים נקודות! והקסם הוא שבעזרת כללים אקראיים לגמרי, הנקודות "מסדרות את עצמן" ויוצרות את הצורה המדויקת של משולש שרפינסקי. ככה זה עובד:</p>
    <ol>
        <li>מתחילים עם שלושה נקודות קבועות בפינות של משולש (הקוד כבר סידר את זה בשבילכם).</li>
        <li>בוחרים נקודת התחלה כלשהי, אפילו מחוץ למשולש - זה לא באמת משנה!</li>
        <li>עכשיו, חוזרים על הדברים הבאים עשרות, מאות ואלפי פעמים:</li>
            <ul>
                <li><strong>צעד אקראי:</strong> הטילו קובייה (או במקרה שלנו, הקוד עושה הגרלה) ובחרו באקראי אחת משלושת נקודות הפינה המקוריות.</li>
                <li><strong>קפיצה:</strong> חשבו את נקודת האמצע המדויקת בין הנקודה שבה אתם נמצאים כרגע לבין נקודת הפינה שנבחרה בהגרלה.</li>
                <li><strong>ציור ומיקום חדש:</strong> ציירו נקודה זעירה על המסך במיקום החדש הזה, והפכו אותה ל"נקודה הנוכחית" עבור הצעד הבא.</li>
            </ul>
    </ol>
    <p>זה נשמע כאוטי לחלוטין, נכון? אבל באופן מדהים, ככל שתציירו יותר נקודות, תראו כיצד הן מתאספות בדיוק במקומות הנכונים כדי לחשוף את המבנה המורכב והאלגנטי של משולש שרפינסקי!</p>
    <p><strong>נסו לשחק:</strong></p>
    <ul>
        <li>הזיזו את המחוון ("כמה נקודות נצייר?") כדי לבחור כמה צעדים במשחק הכאוס יבוצעו.</li>
        <li>לחצו על "צייר מהר" כדי לראות את הצורה מתגלה במהירות.</li>
        <li>לחצו על "הצג צעד-אחר-צעד" כדי לראות ממש את תנועת הנקודה ואיך כל קפיצה אקראית מובילה בסוף ליצירת הצורה המדויקת. זה מרהיב לראות!</li>
    </ul>
</div>

<script>
    const canvas = document.getElementById('sierpinskiCanvas');
    const ctx = canvas.getContext('2d');
    const pointCountInput = document.getElementById('pointCount');
    const currentPointCountSpan = document.getElementById('currentPointCount');
    const drawButton = document.getElementById('drawButton');
    const animateButton = document.getElementById('animateButton'); // New button
    const drawingProgressDiv = document.getElementById('drawingProgress'); // New element for progress
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');

    let animationFrameId = null;
    let isAnimating = false;
    let currentPoint;
    let pointsDrawnCount = 0;
    let totalPointsToDraw = 0;
    let animationSpeed = 1; // Points per frame in animated mode

    // Define the vertices of the initial triangle with associated colors
    const vertices = [
        { x: canvas.width / 2, y: 10, color: 'var(--vertex-color-1)' }, // Top vertex
        { x: 10, y: canvas.height - 10, color: 'var(--vertex-color-2)' }, // Bottom-left vertex
        { x: canvas.width - 10, y: canvas.height - 10, color: 'var(--vertex-color-3)' } // Bottom-right vertex
    ];

    // Function to clear the canvas and draw the initial vertices
    function setupCanvas() {
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear canvas
        // Draw vertices
        vertices.forEach(vertex => {
            ctx.fillStyle = vertex.color;
            ctx.beginPath();
            ctx.arc(vertex.x, vertex.y, 6, 0, Math.PI * 2); // Draw a circle for vertex
            ctx.fill();
        });

         // Optional: Draw initial triangle outline
         /*
        ctx.strokeStyle = var(--border-color);
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(vertices[0].x, vertices[0].y);
        ctx.lineTo(vertices[1].x, vertices[1].y);
        ctx.lineTo(vertices[2].x, vertices[2].y);
        ctx.closePath();
        ctx.stroke();
        */
    }


    // Function to draw a single point
    function drawPoint(x, y, color) {
        ctx.fillStyle = color || '#000'; // Use specified color or default black
        ctx.fillRect(x, y, 1, 1); // Draw a tiny square (1x1 pixel)
    }

     // Function to update progress text
    function updateProgress() {
        if (isAnimating || pointsDrawnCount < totalPointsToDraw) {
             drawingProgressDiv.textContent = `מצייר נקודות: ${pointsDrawnCount.toLocaleString()}`;
        } else {
            drawingProgressDiv.textContent = `הושלם! סה"כ ${totalPointsToDraw.toLocaleString()} נקודות.`;
        }
    }


    // Fast drawing using batches
    function drawSierpinskiFast(numPoints) {
        if (isAnimating) cancelAnimation(); // Stop any ongoing animation

        totalPointsToDraw = numPoints;
        pointsDrawnCount = 0;
        setupCanvas(); // Clear and draw vertices

        currentPoint = {
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height
        };

        ctx.fillStyle = '#000'; // Default color for fast draw if not using vertex colors

        const pointsPerFrame = Math.max(1, Math.floor(numPoints / 200)); // Draw more points per frame for fast mode
        let pointsBatch = 0;

        function fastDrawStep() {
             if (pointsDrawnCount >= totalPointsToDraw) {
                 updateProgress();
                 return; // Stop drawing
             }

            const pointsToDrawThisFrame = Math.min(pointsPerFrame, totalPointsToDraw - pointsDrawnCount);

            for (let i = 0; i < pointsToDrawThisFrame; i++) {
                const randomVertexIndex = Math.floor(Math.random() * vertices.length);
                const randomVertex = vertices[randomVertexIndex];

                currentPoint.x = (currentPoint.x + randomVertex.x) / 2;
                currentPoint.y = (currentPoint.y + randomVertex.y) / 2;

                 // Use vertex color
                drawPoint(currentPoint.x, currentPoint.y, randomVertex.color);
            }

            pointsDrawnCount += pointsToDrawThisFrame;
            updateProgress();
            animationFrameId = requestAnimationFrame(fastDrawStep);
        }

        fastDrawStep(); // Start the fast drawing process
    }


    // Animated step-by-step drawing
    function animateSierpinski(numPoints) {
        if (isAnimating) return; // Prevent starting animation if already running

        cancelAnimation(); // Stop any fast draw
        isAnimating = true;
        totalPointsToDraw = numPoints;
        pointsDrawnCount = 0;
        setupCanvas(); // Clear and draw vertices

         currentPoint = {
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height
        };

         // Optional: Draw initial random point
         // ctx.fillStyle = '#888'; // Grey
         // ctx.beginPath();
         // ctx.arc(currentPoint.x, currentPoint.y, 3, 0, Math.PI * 2);
         // ctx.fill();


        function animationStep() {
            if (pointsDrawnCount >= totalPointsToDraw || !isAnimating) {
                isAnimating = false; // Ensure flag is reset
                updateProgress();
                return; // Stop animation
            }

             // Draw a few points per frame for smoother animation performance
            const pointsToDrawThisFrame = animationSpeed; // Use animationSpeed

            for (let i = 0; i < pointsToDrawThisFrame; i++) {
                 if (pointsDrawnCount >= totalPointsToDraw) break; // Stop if done within the frame

                const randomVertexIndex = Math.floor(Math.random() * vertices.length);
                const randomVertex = vertices[randomVertexIndex];

                // Calculate the midpoint
                currentPoint.x = (currentPoint.x + randomVertex.x) / 2;
                currentPoint.y = (currentPoint.y + randomVertex.y) / 2;

                // Draw the new point with vertex color
                drawPoint(currentPoint.x, currentPoint.y, randomVertex.color);

                pointsDrawnCount++;
            }


            updateProgress();
            animationFrameId = requestAnimationFrame(animationStep);
        }

        animationStep(); // Start the animation
    }

    // Function to cancel any ongoing animation or drawing
    function cancelAnimation() {
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
            animationFrameId = null;
        }
        isAnimating = false; // Reset animation flag
        drawingProgressDiv.textContent = ''; // Clear progress text on cancel
    }

    // Initial setup and draw
    setupCanvas();
    const initialPointCount = parseInt(pointCountInput.value);
    currentPointCountSpan.textContent = initialPointCount.toLocaleString();
    // Don't draw on load, wait for user interaction
    // drawSierpinskiFast(initialPointCount); // Or maybe a small initial draw? Let's wait.


    // Event listener for slider input (updates span live)
    pointCountInput.addEventListener('input', function() {
        currentPointCountSpan.textContent = parseInt(this.value).toLocaleString(); // Format with commas
    });

     // Event listener for slider change or button click
    drawButton.addEventListener('click', function() {
        const numPoints = parseInt(pointCountInput.value);
        drawSierpinskiFast(numPoints);
    });

     animateButton.addEventListener('click', function() {
        const numPoints = parseInt(pointCountInput.value);
        animateSierpinski(numPoints);
     });

    // Stop animation if the slider value is changed while animating
     pointCountInput.addEventListener('change', function() {
         if (isAnimating) {
             cancelAnimation();
             // Optionally start a fast draw after the slider change
             const numPoints = parseInt(this.value);
             drawSierpinskiFast(numPoints);
         }
     });


    // Event listener for toggling explanation
    toggleExplanationButton.addEventListener('click', function() {
        explanationDiv.classList.toggle('visible');
        // Adjust text based on state
        if (explanationDiv.classList.contains('visible')) {
            toggleExplanationButton.textContent = 'הסתר את סוד הקסם';
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' }); // Scroll into view when shown
        } else {
            toggleExplanationButton.textContent = 'הצג את סוד הקסם';
        }
    });


    // Ensure the explanation div is initially hidden (handled by CSS and class)
    // and that max-height is set appropriately on load if content is larger.
    // A common pattern is to calculate height after render or use a large arbitrary value.
    // For simplicity and within constraints, a large max-height is used in CSS.

    // Add initial draw or message
     drawingProgressDiv.textContent = 'בחרו מספר נקודות ולחצו "צייר" או "הצג צעד-אחר-צעד".';


</script>