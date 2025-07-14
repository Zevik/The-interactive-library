---
title: "פרקטלים: הקוד הסודי של הטבע"
english_slug: fractals-repeating-shapes-in-nature
category: "מדע כללי"
tags:
  - פרקטלים
  - גיאומטריה
  - טבע
  - תבניות
  - דמיון עצמי
---
<h1>פרקטלים: הקוד הסודי של הטבע</h1>
<p>האם שמתם לב פעם איך ענפי עץ מתפצלים? או איך עלה שרך בנוי מ"עלעלים" קטנים שדומים לעלה כולו? גלו את התבנית הגיאומטרית המדהימה שהטבע חוזר עליה שוב ושוב, בכל קנה מידה, ויוצר עולם שלם של יופי מורכב מכללים פשוטים.</p>

<div class="interactive-section">
    <h2>צרו פרקטל משלכם</h2>
    <p>שחקו עם הפרמטרים וראו איך שינויים קטנים משפיעים על המבנה המורכב שנוצר.</p>
    <div class="controls">
        <div class="control-group">
            <label for="iterations">עומק (מספר חזרות):</label>
            <input type="number" id="iterations" value="7" min="1" max="12">
            <span class="control-hint">(ככל שעולה, המבנה מפורט יותר אך גם לוקח זמן רב יותר לציור)</span>
        </div>
         <div class="control-group">
            <label for="lengthRatio">יחס אורך ענף:</label>
            <input type="range" id="lengthRatio" value="0.7" min="0.5" max="0.9" step="0.01">
            <span id="lengthRatioValue" class="control-value">0.7</span>
            <span class="control-hint">(יחס האורך של כל ענף חדש לענף שממנו הוא מתפצל)</span>
        </div>
         <div class="control-group">
            <label for="angleSpread">זווית פיצול:</label>
            <input type="range" id="angleSpread" value="45" min="15" max="75" step="1">
            <span id="angleSpreadValue" class="control-value">45°</span>
             <span class="control-hint">(הזווית שבה ענפים חדשים מתפצלים מהענף הראשי)</span>
        </div>
         <div class="control-group">
            <label for="branchCount">מספר ענפים מכל נקודה:</label>
            <input type="number" id="branchCount" value="2" min="2" max="4">
             <span class="control-hint">(כמה ענפים חדשים נוצרים בכל פיצול)</span>
        </div>
         <button id="randomizeParams">פרמטרים אקראיים</button>
    </div>
    <canvas id="fractalCanvas" width="700" height="500"></canvas>

    <div class="natural-examples">
        <h3>פרקטלים סביבנו - דוגמאות מהטבע</h3>
        <div class="examples-grid">
            <div class="example">
                <img src="placeholder_tree.jpg" alt="עץ אמיתי" loading="lazy">
                <p>מבנה עץ (ענפים)</p>
            </div>
            <div class="example">
                <img src="placeholder_fern.jpg" alt="עלה שרך אמיתי" loading="lazy">
                <p>עלה שרך (עלעלים)</p>
            </div>
             <div class="example">
                <img src="placeholder_coastline.jpg" alt="קו חוף" loading="lazy">
                <p>קו חוף (מפרצים ולשונות ים)</p>
            </div>
             <div class="example">
                <img src="placeholder_lightning.jpg" alt="ברק" loading="lazy">
                <p>התפצלות ברק</p>
            </div>
            <div class="example">
                <img src="placeholder_romanesco.jpg" alt="כרובית רומנסקו" loading="lazy">
                <p>כרובית רומנסקו</p>
            </div>
            <div class="example">
                <img src="placeholder_river.jpg" alt="מערכת נהר" loading="lazy">
                <p>מערכת נהר (ערוצים)</p>
            </div>
        </div>
         <p class="examples-note">לחצו על "הצג הסבר מורחב" ללמוד עוד על איך התבניות האלה פועלות בטבע.</p>
    </div>
</div>

<button id="toggleExplanation">הצג את הסיפור המלא מאחורי הפרקטלים</button>

<div id="explanation" class="hidden">
    <h2>הסיפור המלא: עולם הפרקטלים הנסתר</h2>
    <p><strong>מהם פרקטלים?</strong> דמיינו צורה גיאומטרית שיש לה "אינסוף שכבות" של פירוט. כשמתקרבים אליה ומגדילים חלק קטן, מגלים שהוא נראה (בצורה מדויקת או סטטיסטית) בדיוק כמו הצורה השלמה, רק בקטן יותר. זוהי תכונת ה"דמיון העצמי", והיא הלב של הפרקטל. שלא כמו צורות רגילות שיש להן מימד שלם (קו הוא מימד 1, ריבוע הוא מימד 2, קובייה היא מימד 3), לפרקטלים רבים יש "מימד פרקטלי" שאינו שלם!</p>

    <h3>צמחו לבד במעבדה (ובטבע) - דוגמאות קלאסיות</h3>
    <p>מתמטיקאים גילו את הפרקטלים עוד לפני שהיה להם השם הזה. הם נוצרים מיישום חוזר של כללים פשוטים:</p>
    <ul>
        <li><strong>פתית שלג קוך:</strong> מתחיל ממשולש פשוט. בכל שלב, מוסיפים "גבעה" קטנה באמצע כל קטע ישר. חוזרים על זה שוב ושוב. התוצאה? צורה עם היקף אינסופי אך שטח סופי!</li>
        <li><strong>משולש שרפינסקי:</strong> מתחיל ממשולש. מוציאים את המשולש האמצעי. חוזרים על זה בשלושת המשולשים שנשארו. ממשיכים כך לנצח.</li>
         <li><strong>קבוצת מנדלברוט:</strong> יפהפייה ומורכבת להפליא, נוצרת מכלל אלגברי פשוט שחוזר על עצמו. כשמגדילים חלקים בקצה שלה, מגלים עותקים קטנים של הקבוצה כולה, שזורים בדפוסים מסחררים.</li>
    </ul>

    <h3>הקוד הסודי של הטבע: איפה פוגשים פרקטלים?</h3>
    <p>היופי המתמטי הזה אינו נשאר על הנייר. הוא מקיף אותנו! מבנים פרקטליים צצים בכל מקום שבו תהליך פשוט חוזר על עצמו באופן היררכי:</p>
    <ul>
        <li><strong>העולם הירוק:</strong> ענפי עצים (כפי שראיתם בסימולציה), עורקי עלים, שורשים, ואפילו מבנה פרחים מסוימים כמו כרובית רומנסקו - כולם דוגמאות מובהקות.</li>
        <li><strong>פני כדור הארץ:</strong> קווי חוף (ה"אורך" שלהם תלוי ברמת הפירוט שמודדים), נופים הרריים, מערכות נהרות המתפצלות לנחלים קטנים יותר.</li>
        <li><strong>הגוף שלנו:</strong> מערכת כלי הדם המתפצלת מעורקים ראשיים לנימים זעירים, מבנה הסמפונות בריאות (מאפשר מקסימום שטח חילופי גזים), מבנה תאי עצב.</li>
         <li><strong>אפילו בשמיים:</strong> עננים, ברקים, ואף מבנה הגלקסיות ביקום מראים דפוסים המזכירים פרקטלים.</li>
    </ul>

    <h3>למה הטבע "אוהב" פרקטלים? סוד היעילות!</h3>
    <p>מבנים פרקטליים הם לא רק יפים, הם סופר יעילים! הם מספקים פתרונות גאוניים לבעיות הישרדות:</p>
    <ul>
        <li><strong>שטח פנים ענק בנפח קטן:</strong> כמו בריאות או בשורשים - מבנה מסועף ממקסם את שטח המגע עם הסביבה להחלפת חומרים חיוניים (חמצן, מים, מינרלים).</li>
        <li><strong>פיזור אופטימלי:</strong> מאפשר לחלק ביעילות נוזלים (דם, מים) או אנרגיה (אור, ברק) לכל חלקי המבנה.</li>
        <li><strong>מילוי מרחב:</strong> ענפי עץ ממלאים את המרחב כדי למקסם קליטת אור.</li>
        <li><strong>חסכון גנטי:</strong> כללים פשוטים שחוזרים על עצמם דורשים פחות מידע גנטי מאשר תוכנית מפורטת לכל חלק וחלק.</li>
    </ul>

    <h3>הכללים הפשוטים שיוצרים עולם מורכב</h3>
    <p>השיעור הגדול מהפרקטלים הוא שגם מבנים מורכבים ומופלאים בטבע יכולים לצמוח מיישום חוזר של הוראות פשוטות. זהו עיקרון יסודי בגדילה ביולוגית ובמערכות טבעיות רבות. בפעם הבאה שתראו עץ, עלה או אפילו ענן, זכרו שאתם מביטים בביטוי פיזי לקוד גיאומטרי סודי!</p>

    <h3>לסיכום</h3>
    <p>פרקטלים הם יותר מסתם צורות מוזרות - הם שפה שבה הטבע מדבר. הם מראים לנו את הקשר העמוק בין מתמטיקה טהורה לתבניות שמקיפות אותנו, ומלמדים אותנו איך מורכבות אינסופית יכולה לנבוע מפשטות אלגנטית.</p>
</div>

<style>
    /* General styles */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 0;
        direction: rtl; /* Hebrew direction */
        text-align: right;
        background: linear-gradient(to bottom, #e0f2f7, #ffffff); /* Light blue gradient */
        color: #333;
        padding-bottom: 50px; /* Space for footer if needed */
    }

    h1, h2, h3 {
        color: #0056b3; /* Deeper blue for headings */
        text-align: center;
        margin-bottom: 20px;
        font-weight: bold;
    }

    h1 {
        margin-top: 30px;
        font-size: 2.8em;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    h2 {
         font-size: 2.2em;
         margin-top: 30px;
         border-bottom: 2px solid #007bff;
         padding-bottom: 10px;
    }

     h3 {
         font-size: 1.6em;
         margin-top: 25px;
         color: #007bff;
    }

    p {
        margin-bottom: 18px;
    }

    /* Interactive Section */
    .interactive-section {
        margin: 30px auto;
        padding: 30px;
        border: 1px solid #b3e5fc; /* Lighter blue border */
        border-radius: 12px;
        background-color: #ffffff; /* White background */
        max-width: 900px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.15); /* Stronger shadow */
        text-align: initial; /* Reset text alignment */
    }

     .interactive-section h2 {
         text-align: right; /* Align interactive heading right */
         border-bottom: none;
         padding-bottom: 0;
         margin-bottom: 10px;
         color: #0056b3;
     }

     .interactive-section p {
         margin-bottom: 25px;
         font-size: 1.1em;
         color: #555;
     }

    .controls {
        margin-bottom: 30px;
        padding: 20px;
        background-color: #e1f5fe; /* Very light blue */
        border-radius: 8px;
        display: flex;
        flex-wrap: wrap; /* Allow controls to wrap on smaller screens */
        justify-content: center; /* Center controls */
        gap: 15px; /* Space between control groups */
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
    }

    .control-group {
        display: flex;
        flex-direction: column; /* Stack label and input */
        align-items: flex-start; /* Align text to the right within group */
        min-width: 150px; /* Ensure reasonable width */
    }

    .controls label {
        margin-bottom: 8px;
        font-weight: bold;
        color: #01579b; /* Darker blue for labels */
        font-size: 1em;
    }

     .controls input[type="number"],
     .controls input[type="range"] {
        padding: 8px;
        border: 1px solid #b0bec5; /* Greyish-blue border */
        border-radius: 4px;
        font-size: 1em;
        width: 100%; /* Make inputs take full width of group */
        box-sizing: border-box; /* Include padding/border in width */
    }

     .controls input[type="number"] {
         width: 80px; /* Specific width for number input */
         text-align: center;
     }

    .control-value {
        display: inline-block;
        margin-top: 5px;
        font-size: 0.9em;
        color: #0277bd; /* Medium blue */
        font-weight: bold;
    }

     .control-hint {
         font-size: 0.8em;
         color: #546e7a; /* Muted text color */
         margin-top: 4px;
     }

    #randomizeParams {
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 5px;
        background-color: #ff9800; /* Orange button */
        color: white;
        transition: background-color 0.3s ease;
        align-self: center; /* Center button vertically in flex container */
         margin-top: 15px; /* Add some space above button */
    }

    #randomizeParams:hover {
        background-color: #f57c00; /* Darker orange on hover */
    }

    canvas {
        display: block;
        margin: 0 auto 20px auto;
        border: 2px solid #b3e5fc; /* Lighter blue border */
        background-color: #ffffff; /* White background */
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        max-width: 100%; /* Make canvas responsive */
        height: auto; /* Maintain aspect ratio */
    }

    .natural-examples {
        margin-top: 40px;
        padding-top: 30px;
        border-top: 2px dashed #b3e5fc; /* Dashed blue border */
        text-align: center;
    }

    .natural-examples h3 {
        margin-bottom: 20px;
        color: #0056b3;
        text-align: center; /* Center example heading */
    }

    .examples-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); /* Responsive grid */
        gap: 20px; /* Space between grid items */
        justify-items: center; /* Center items in the grid */
        margin-bottom: 20px;
    }

    .example {
        display: flex; /* Use flexbox for internal alignment */
        flex-direction: column; /* Stack image and text */
        align-items: center; /* Center content */
        text-align: center;
        width: 100%; /* Take full width in grid item */
        max-width: 150px; /* Max width for each example */
    }

    .example img {
        display: block;
        margin-bottom: 8px;
        border: 1px solid #e0e0e0;
        border-radius: 8px; /* Rounded corners for images */
        width: 100%; /* Image fills container */
        height: auto;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        transition: transform 0.3s ease; /* Add hover effect */
    }

     .example img:hover {
         transform: scale(1.05); /* Slightly enlarge on hover */
     }

    .example p {
        font-size: 0.9em;
        color: #555;
        margin: 0; /* Remove paragraph margin */
    }

    .examples-note {
        font-size: 0.95em;
        color: #0277bd;
        text-align: center;
        margin-top: 20px;
    }


    /* Explanation Section */
    button#toggleExplanation {
        display: block;
        margin: 40px auto;
        padding: 15px 30px;
        font-size: 1.2em;
        cursor: pointer;
        border: none;
        border-radius: 8px;
        background-color: #007bff; /* Primary blue */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    button#toggleExplanation:hover {
        background-color: #0056b3; /* Darker blue on hover */
    }

     button#toggleExplanation:active {
         transform: scale(0.98); /* Slightly shrink on click */
     }


    #explanation {
        margin: 20px auto;
        padding: 30px;
        border: 1px solid #b3e5fc; /* Lighter blue border */
        border-radius: 12px;
        background-color: #ffffff; /* White background */
        max-width: 900px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.15); /* Stronger shadow */
    }

    #explanation h2, #explanation h3 {
        text-align: right; /* Align explanation headings to the right */
        color: #0056b3;
    }

    #explanation h2 {
         border-bottom: 2px solid #007bff;
         padding-bottom: 10px;
         margin-bottom: 20px;
    }

     #explanation h3 {
         margin-bottom: 15px;
         color: #007bff;
     }

     #explanation ul {
        list-style-type: disc; /* Use disc bullets */
        padding-right: 25px; /* Indent list */
        margin-bottom: 20px;
    }

    #explanation li {
        margin-bottom: 12px;
        line-height: 1.6;
    }

    .hidden {
        display: none;
    }

    /* Placeholder image styles - improve visual cue */
    img[src^="placeholder_"] {
        background-color: #cfd8dc; /* Light grey-blue background for placeholders */
        padding: 10px; /* Add some padding */
        box-sizing: border-box; /* Include padding in width */
        border: 1px dashed #78909c; /* Dashed border */
        display: flex; /* Use flexbox for centering text */
        align-items: center;
        justify-content: center;
        font-size: 0.8em;
        color: #546e7a;
        font-style: italic;
        text-align: center;
    }

     .example img[src^="placeholder_"] {
         /* Override if needed, but the above should work */
     }


     /* Responsive adjustments */
     @media (max-width: 768px) {
         h1 { font-size: 2em; }
         h2 { font-size: 1.6em; }
         h3 { font-size: 1.3em; }

         body { padding: 10px; }
         .interactive-section, #explanation { padding: 20px; }
         .controls { flex-direction: column; align-items: stretch; gap: 10px;}
         .control-group { min-width: auto; }
         .examples-grid { grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); gap: 10px; }
         button#toggleExplanation { padding: 10px 20px; font-size: 1em; }
     }


</style>

<script>
    const canvas = document.getElementById('fractalCanvas');
    const ctx = canvas.getContext('2d');
    const iterationsInput = document.getElementById('iterations');
    const lengthRatioInput = document.getElementById('lengthRatio');
    const lengthRatioValueSpan = document.getElementById('lengthRatioValue');
    const angleSpreadInput = document.getElementById('angleSpread');
    const angleSpreadValueSpan = document.getElementById('angleSpreadValue');
    const branchCountInput = document.getElementById('branchCount');
    const randomizeButton = document.getElementById('randomizeParams');
    const toggleButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');

    // Store default parameters
    const defaultParams = {
        iterations: 7,
        lengthRatio: 0.7,
        angleSpread: 45, // Degrees
        branchCount: 2
    };

    // Function to draw a simple recursive tree branch
    function drawBranch(x1, y1, length, angle, depth, maxDepth) {
        if (depth === 0) {
            return;
        }

        // Calculate endpoint of the branch
        const x2 = x1 + length * Math.cos(angle);
        const y2 = y1 + length * Math.sin(angle);

        // Draw the branch segment
        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);

        // Dynamic styling based on depth
        const hue = 120 - (depth / maxDepth) * 120; // Green to yellow-green color
        const saturation = 50 + (depth / maxDepth) * 50; // More saturated deeper down
        const lightness = 30 + (depth / maxDepth) * 20; // Darker deeper down
        ctx.strokeStyle = `hsl(${hue}, ${saturation}%, ${lightness}%)`;

        ctx.lineWidth = Math.max(0.5, depth / 4); // Thicker near the base, thinner at tips
        ctx.lineCap = 'round'; // Round ends for smoother look
        ctx.stroke();

        // Recursive calls for new branches
        const currentLengthRatio = parseFloat(lengthRatioInput.value);
        const currentAngleSpreadRad = parseFloat(angleSpreadInput.value) * Math.PI / 180; // Convert degrees to radians
        const currentBranchCount = parseInt(branchCountInput.value, 10);

        // Simple branching: 2 branches at fixed angles
        if (currentBranchCount === 2) {
             drawBranch(x2, y2, length * currentLengthRatio, angle + currentAngleSpreadRad, depth - 1, maxDepth);
             drawBranch(x2, y2, length * currentLengthRatio, angle - currentAngleSpreadRad, depth - 1, maxDepth);
        }
        // More branching options (e.g., 3 branches)
        else if (currentBranchCount === 3) {
             drawBranch(x2, y2, length * currentLengthRatio, angle + currentAngleSpreadRad, depth - 1, maxDepth);
             drawBranch(x2, y2, length * currentLengthRatio * 0.9, angle, depth - 1, maxDepth); // Slightly shorter central branch
             drawBranch(x2, y2, length * currentLengthRatio, angle - currentAngleSpreadRad, depth - 1, maxDepth);
        }
         // More branching options (e.g., 4 branches)
         else if (currentBranchCount === 4) {
             drawBranch(x2, y2, length * currentLengthRatio * 0.8, angle + currentAngleSpreadRad * 1.2, depth - 1, maxDepth);
             drawBranch(x2, y2, length * currentLengthRatio, angle + currentAngleSpreadRad * 0.5, depth - 1, maxDepth);
             drawBranch(x2, y2, length * currentLengthRatio, angle - currentAngleSpreadRad * 0.5, depth - 1, maxDepth);
             drawBranch(x2, y2, length * currentLengthRatio * 0.8, angle - currentAngleSpreadRad * 1.2, depth - 1, maxDepth);
         }
         // Add more branching patterns as needed
    }

    // Function to draw the entire tree
    let animationFrameId = null; // To cancel previous animation frames

    function drawTree(currentDepth = null) {
        // Use currentDepth if animating, otherwise use maxDepth from input
        const maxDepth = parseInt(iterationsInput.value, 10);
        const depthToDraw = currentDepth === null ? maxDepth : currentDepth;

        // Clear canvas only once if not animating depth-by-depth
        if (currentDepth === null || currentDepth === maxDepth) {
             ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear canvas
             ctx.fillStyle = '#ffffff'; // Set background color explicitly
             ctx.fillRect(0, 0, canvas.width, canvas.height);
        }


        const startX = canvas.width / 2;
        const startY = canvas.height - 30; // Start slightly above the bottom
        const initialLength = 100; // Initial length of the trunk
        const initialAngle = -Math.PI / 2; // Pointing upwards

        drawBranch(startX, startY, initialLength, initialAngle, depthToDraw, maxDepth);

        // Simple depth animation: Draw depth by depth
        if (currentDepth !== null && currentDepth < maxDepth) {
             animationFrameId = requestAnimationFrame(() => drawTree(currentDepth + 1));
        } else if (currentDepth === null) {
             // If not animating, just draw the full tree once
        }
    }

    // Function to start drawing with animation
    function startDrawingAnimation() {
         if (animationFrameId) {
             cancelAnimationFrame(animationFrameId);
         }
         // Clear canvas before starting animation
         ctx.clearRect(0, 0, canvas.width, canvas.height);
         ctx.fillStyle = '#ffffff'; // Set background color explicitly
         ctx.fillRect(0, 0, canvas.width, canvas.height);
         drawTree(1); // Start drawing from depth 1
    }


    // Update span values when sliders move
    lengthRatioInput.addEventListener('input', () => {
         lengthRatioValueSpan.textContent = parseFloat(lengthRatioInput.value).toFixed(2);
    });

    angleSpreadInput.addEventListener('input', () => {
         angleSpreadValueSpan.textContent = `${angleSpreadInput.value}°`;
    });


    // Event listeners for controls - trigger animation on change/input
    iterationsInput.addEventListener('change', startDrawingAnimation);
    iterationsInput.addEventListener('input', startDrawingAnimation); // Optional: live update while sliding (can be slow for high iterations)

    lengthRatioInput.addEventListener('change', startDrawingAnimation);
    angleSpreadInput.addEventListener('change', startDrawingAnimation);
    branchCountInput.addEventListener('change', startDrawingAnimation);

    // Randomize parameters button
    randomizeButton.addEventListener('click', () => {
        iterationsInput.value = Math.floor(Math.random() * 6) + 5; // 5 to 10 iterations
        lengthRatioInput.value = (Math.random() * 0.2 + 0.6).toFixed(2); // 0.6 to 0.8
        angleSpreadInput.value = Math.floor(Math.random() * 40) + 30; // 30 to 70 degrees
        branchCountInput.value = Math.random() > 0.5 ? (Math.random() > 0.5 ? 3 : 2) : 4; // 2, 3 or 4 branches (biased towards 2)


        // Manually trigger input events to update spans and redraw
        iterationsInput.dispatchEvent(new Event('input'));
        lengthRatioInput.dispatchEvent(new Event('input'));
        angleSpreadInput.dispatchEvent(new Event('input'));
        branchCountInput.dispatchEvent(new Event('change')); // Trigger change for draw

        startDrawingAnimation(); // Start drawing with new parameters
    });


    // Event listener for the toggle button
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.classList.toggle('hidden');
        if (isHidden) {
            toggleButton.textContent = 'הצג את הסיפור המלא מאחורי הפרקטלים';
        } else {
            toggleButton.textContent = 'הסתר את הסיפור המלא מאחורי הפרקטלים';
        }
    });

    // Initial state setup
    // Set initial values for spans
    lengthRatioValueSpan.textContent = parseFloat(lengthRatioInput.value).toFixed(2);
    angleSpreadValueSpan.textContent = `${angleSpreadInput.value}°`;

    // Initial draw with animation
    startDrawingAnimation();

    // Set initial button text based on the hidden state
    if (explanationDiv.classList.contains('hidden')) {
        toggleButton.textContent = 'הצג את הסיפור המלא מאחורי הפרקטלים';
    } else {
         toggleButton.textContent = 'הסתר את הסיפור המלא מאחורי הפרקטלים';
    }

</script>