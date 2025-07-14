---
title: "מגלה שדות: מסע אל הבלתי נראה"
english_slug: magnetic-field-detector-how-a-magnetometer-works
category: "מדעים מדויקים / פיזיקה"
tags: שדה מגנטי, מגנטומטר, מדידה, ניווט, חיישנים, פיזיקה אינטראקטיבית, סימולציה
---
<h1>מגלה שדות: מסע אל הבלתי נראה</h1>
<p>הטלפון הנייד שלכם יודע לזהות שדות מגנטיים ואפילו משמש כמצפן מדויק. איך מכשיר כל כך קטן מסוגל 'לחוש' כוח בלתי נראה כמו שדה מגנטי, וכיצד הידע הזה הופך למפתח לניווט, חקר כדור הארץ ואפילו חיפוש אוצרות? הצטרפו למסע אינטראקטיבי וגלו את הסודות המגנטיים שמקיפים אותנו.</p>

<div id="magnetic-app" class="interactive-simulation-container">
    <h2>התנסות: הצצה אל השדה המגנטי</h2>
    <p>גררו את סמל המגנטומטר במסך כדי למדוד את השדה המגנטי בנקודות שונות. הוסיפו מקורות מגנטיים (מגנטים או חוטי זרם) ושנו את מיקומם כדי לראות כיצד הם מעצבים את השדה המגנטי המרחבי. האם תוכלו למצוא את נקודת השדה החזק ביותר? היכן השדה מתאפס?</p>

    <div class="controls">
        <button id="add-magnet" class="control-button">הוסף מגנט (דו-קוטב)</button>
        <button id="add-wire" class="control-button">הוסף חוט זרם</button>
        <button id="remove-last-source" class="control-button secondary">הסר אחרון</button>
        <button id="toggle-field-lines" class="control-button secondary">הצג/הסתר קווי שדה</button>
    </div>

    <div id="simulation-area" class="simulation-canvas-container">
        <!-- This canvas will be used for drawing the simulation -->
        <canvas id="magnetic-canvas"></canvas>
        <!-- Magnetometer symbol will be draggable -->
        <div id="magnetometer" class="draggable-item">
            <img src="https://cdn.jsdelivr.net/gh/byuphy/byuphy.github.io@main/images/compass_icon.svg" alt="מגנטומטר" title="גרור אותי לחקור את השדה!">
            <div id="field-vector" class="field-vector"></div> <!-- Visual representation of the field vector -->
            <div id="field-display" class="field-display">Bx: 0.00, By: 0.00, עוצמה: 0.00</div> <!-- Numerical display -->
        </div>
        <!-- Magnetic sources will be added here dynamically -->
    </div>
</div>

<button id="toggle-explanation" class="explanation-toggle-button">הצג הסבר מפורט</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2>הסבר: פענוח הצופן המגנטי</h2>

    <h3>מהו שדה מגנטי וכיצד הוא נוצר?</h3>
    <p>דמיינו אזור בלתי נראה במרחב שבו מורגש כוח מגנטי. זהו השדה המגנטי! הוא נוצר על ידי שני גורמים עיקריים: זרמים חשמליים (מטענים חשמליים שנמצאים בתנועה), כמו בחוט שמחובר לסוללה או בברק, ומגנטים קבועים, שבהם מקור השדה הוא תנועה סיבובית של אלקטרונים בתוך האטומים עצמם.</p>

    <h3>למה שדה מגנטי הוא וקטור?</h3>
    <p>בכל נקודה במרחב, לשדה המגנטי יש לא רק <strong>עוצמה</strong> מסוימת (עד כמה הוא "חזק") אלא גם <strong>כיוון</strong> מוגדר. לכן אנו מתארים אותו כ<strong>וקטור</strong>. בסימולציה, החץ האדום היוצא מהמגנטומטר מראה את כיוון השדה בנקודה שבה הוא נמצא, ואורכו מייצג את עוצמת השדה באותה נקודה.</p>

    <h3>המגנטומטר: העיניים הבלתי נראות שלנו לשדה</h3>
    <p>מגנטומטר הוא מכשיר גאוני שמטרתו למדוד במדויק את השדה המגנטי המקומי בנקודה ספציפית. הוא למעשה "מרגיש" את הכוח והכיוון של השדה באותה נקודה ומספק לנו נתונים מספריים ו/או ויזואליים (כמו בסימולציה). ישנם סוגים רבים של מגנטומטרים, הפועלים על עקרונות פיזיקליים שונים, החל מהמצפן הפשוט ועד לחיישנים אלקטרוניים זעירים בטלפון שלכם.</p>

    <h3>שימושים יומיומיים ומדעיים של מגנטומטרים</h3>
    <p>למגנטומטרים מגוון מדהים של יישומים שמשפיעים על חיינו ועל יכולתנו לחקור את העולם והיקום:
    <ul>
        <li><strong>ניווט ומצפן דיגיטלי:</strong> הטלפון החכם שלכם משתמש במגנטומטר כדי לזהות את כיוון השדה המגנטי של כדור הארץ (השדה הגיאומגנטי) ולהראות לכם היכן הצפון.</li>
        <li><strong>חיפוש אוצרות ומתכות:</strong> מגנטומטרים תעשייתיים יכולים לזהות שינויים קטנים בשדה המגנטי הנגרמים מנוכחות מתכות תת-קרקעיות, צנרת, חפצים קבורים ואפילו שרידי בנייה.</li>
        <li><strong>חקר כדור הארץ והחלל:</strong> מדענים משתמשים במגנטומטרים על לוויינים, מטוסים ומכשירי מדידה קרקעיים כדי למפות את השדה הגיאומגנטי, לזהות אנומליות שמעידות על מרבצי מחצבים או מבנים גיאולוגיים תת-קרקעיים, ולחקור את השדות המגנטיים של כוכבי לכת אחרים (כמו מאדים) והשמש.</li>
        <li><strong>בדיקות תעשייתיות:</strong> משמשים לזיהוי פגמים בחומרים מגנטיים או לאפיון תכונותיהם.</li>
        <li><strong>רפואה:</strong> טכנולוגיות הדמיה כמו MRI (הדמיה בתהודה מגנטית) מתבססות על שדות מגנטיים חזקים מאוד ומדידת תגובת רקמות הגוף אליהם.</li>
    </ul></p>

    <h3>איך מגנטומטר עובד? הצצה קצרה</h3>
    <p>אף על פי שהסוגים שונים, העיקרון הבסיסי הוא שמדידת השדה המגנטי מבוססת על השפעת השדה הזה על חומר או רכיב המדידה. לדוגמה, חיישן "אפקט הול" (Hall Effect) - סוג נפוץ במכשירים אלקטרוניים - מפיק מתח חשמלי קטן כשהוא מושפע משדה מגנטי. גודל המתח וכיוונו קשורים ישירות לעוצמת השדה וכיוונו. מגנטומטרים אחרים מודדים את השפעת השדה על חומרים מגנטיים או על תהליכים פיזיקליים עדינים אחרים.</p>

    <h3>לסיכום</h3>
    <p>מגנטומטרים הם כלים מדהימים שמאפשרים לנו לחשוף את הנוף הבלתי נראה של השדות המגנטיים סביבנו. מהמצפן שבלב הטלפון ועד לחקר גלקסיות רחוקות, היכולת למדוד במדויק שדות מגנטיים היא חיונית לטכנולוגיה, למדע ולהבנת היקום.</p>
</div>

<style>
    /* General Page Styles */
    body {
        font-family: 'Arial', sans-serif; /* Use a common, clean font */
        line-height: 1.6;
        margin: 0; /* Remove default body margin */
        padding: 20px;
        background-color: #f4f7f6; /* Light grey background */
        color: #333;
        direction: rtl; /* Hebrew specific */
        text-align: right; /* Hebrew specific */
        overflow-x: hidden; /* Prevent horizontal scroll */
    }

    h1, h2, h3 {
        color: #0056b3; /* Blue shades for headings */
        text-align: center;
        margin-bottom: 1rem; /* Consistent spacing */
        line-height: 1.3;
    }

    h1 { font-size: 2.2em; color: #003366; margin-bottom: 0.5em; }
    h2 { font-size: 1.8em; border-bottom: 2px solid #007bff; padding-bottom: 5px; margin-top: 1.5em; }
    h3 { font-size: 1.4em; color: #007bff; margin-top: 1em; margin-bottom: 0.5em; }

    p {
        margin-bottom: 1em;
    }

    ul {
        list-style: disc inside;
        padding-right: 20px;
        margin-bottom: 1em;
    }

    li {
        margin-bottom: 0.5em;
    }

    /* Simulation Container Styles */
    .interactive-simulation-container {
        background-color: #ffffff; /* White background for the app */
        border: 1px solid #dcdcdc;
        border-radius: 12px; /* More rounded corners */
        padding: 25px;
        margin: 20px auto; /* Center the container */
        max-width: 800px; /* Max width for better readability/layout */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }

    .interactive-simulation-container h2 {
        text-align: right; /* Align section titles to right */
        border-bottom: none;
        padding-bottom: 0;
        margin-bottom: 0.8em;
        color: #333;
    }

    .interactive-simulation-container p {
         text-align: right;
         margin-bottom: 1.5em;
         color: #555;
    }


    /* Controls Styles */
    .controls {
        text-align: center;
        margin-bottom: 20px;
        flex-wrap: wrap; /* Allow buttons to wrap on smaller screens */
        justify-content: center;
    }

    .control-button {
        padding: 12px 20px;
        margin: 5px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 6px; /* Slightly more rounded */
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.2s ease; /* Smooth hover transition */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Button shadow */
    }

    .control-button:hover {
        background-color: #0056b3;
    }

    .control-button.secondary {
        background-color: #6c757d; /* Grey color for secondary actions */
    }
     .control-button.secondary:hover {
        background-color: #5a6268;
    }


    /* Simulation Area Styles */
    .simulation-canvas-container {
        position: relative;
        width: 100%;
        height: 450px; /* Increased height for more space */
        border: 2px solid #007bff; /* Accent border */
        background-color: #e9ecef; /* Light blue-grey background */
        overflow: hidden;
        border-radius: 8px;
        box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.1); /* Inner shadow for depth */
    }

    #magnetic-canvas {
        display: block;
        width: 100%;
        height: 100%;
    }

    /* Draggable Items (Magnetometer, Sources) */
    .draggable-item {
        position: absolute;
        width: 50px; /* Increased size for easier interaction */
        height: 50px;
        cursor: grab;
        z-index: 10; /* Ensure draggables are on top */
        display: flex; /* Use flexbox to center content */
        justify-content: center;
        align-items: center;
        user-select: none; /* Prevent text selection during drag */
    }

    .draggable-item:active {
        cursor: grabbing;
    }

    /* Magnetometer Styles */
    #magnetometer {
        /* Centered initially by JS transform */
    }

    #magnetometer img {
        width: 100%;
        height: 100%;
        pointer-events: none; /* Image does not interfere with dragging the div */
        filter: drop-shadow(0 2px 3px rgba(0,0,0,0.3)); /* Shadow for icon */
    }

    /* Field Vector Styles */
    .field-vector {
        position: absolute;
        bottom: -5px; /* Position relative to magnetometer's bottom edge */
        left: 50%;
        transform-origin: bottom center; /* Rotate around the bottom tip */
        width: 4px; /* Thicker line */
        background-color: #dc3545; /* Red color */
        height: 0; /* Initial height */
        display: none; /* Hidden initially or when field is weak */
        pointer-events: none; /* Does not interfere with drag */
        box-shadow: 0 0 5px rgba(220, 53, 69, 0.5); /* Glow effect */
    }
    /* Arrowhead using pseudo-element */
    .field-vector::after {
        content: '';
        position: absolute;
        bottom: 100%; /* Position at the tip of the line */
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 0;
        border-left: 6px solid transparent; /* Size of arrowhead base */
        border-right: 6px solid transparent;
        border-top: 10px solid #dc3545; /* Size and color of arrowhead */
    }


    /* Field Display Styles */
    .field-display {
        position: absolute;
        bottom: calc(100% + 5px); /* Position above magnetometer, slightly spaced */
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(40, 40, 40, 0.85); /* Darker, more opaque background */
        color: white;
        padding: 5px 10px; /* More padding */
        border-radius: 5px; /* More rounded */
        font-size: 0.9em; /* Slightly larger font */
        white-space: nowrap;
        pointer-events: none; /* Does not interfere with drag */
        min-width: 180px; /* Give it a minimum width */
        text-align: center;
    }


    /* Source Styles (added dynamically) */
    .magnetic-source {
        position: absolute;
        width: 40px; /* Size of source icons */
        height: 40px;
        cursor: grab;
        z-index: 5; /* Sources are below magnetometer */
        display: flex;
        justify-content: center;
        align-items: center;
        user-select: none;
    }
    .magnetic-source:active {
         cursor: grabbing;
    }

    .magnetic-source img {
        width: 100%;
        height: 100%;
        pointer-events: none;
         filter: drop-shadow(0 2px 3px rgba(0,0,0,0.3)); /* Shadow for icon */
    }

    /* Specific source types (using icons instead of shapes) */
    /* Magnet icon source will be set in JS */
    /* Wire icon source will be set in JS */


    /* Explanation Section Styles */
    .explanation-section {
        border-top: 1px solid #dcdcdc;
        padding-top: 20px;
        margin-top: 30px;
        max-width: 800px; /* Align with simulation container width */
        margin-left: auto;
        margin-right: auto;
    }

    .explanation-section h3 {
        text-align: right; /* Hebrew standard */
        color: #007bff;
        margin-top: 1.5em;
    }

    .explanation-section ul {
        padding-right: 25px; /* Adjust indentation */
    }

    .explanation-toggle-button {
        display: block; /* Make it a block element */
        width: fit-content; /* Adjust width to content */
        margin: 20px auto; /* Center the button */
        padding: 10px 20px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.2s ease;
    }
     .explanation-toggle-button:hover {
        background-color: #0056b3;
    }

    /* Responsiveness */
    @media (max-width: 600px) {
        body {
            padding: 10px;
        }
        h1 { font-size: 1.8em; }
        h2 { font-size: 1.5em; }
        h3 { font-size: 1.2em; }
        .interactive-simulation-container {
            padding: 15px;
        }
        .controls {
            flex-direction: column; /* Stack buttons vertically */
        }
        .control-button {
             width: 80%; /* Make buttons wider */
             margin: 5px auto; /* Center stacked buttons */
        }
         .simulation-canvas-container {
            height: 350px; /* Reduce height on smaller screens */
         }
         .draggable-item {
             width: 40px; /* Smaller icons */
             height: 40px;
         }
          .field-display {
             font-size: 0.7em; /* Smaller font */
             min-width: 150px;
             padding: 3px 8px;
         }
          .field-vector {
             width: 3px;
         }
          .field-vector::after {
             border-left-width: 4px;
             border-right-width: 4px;
             border-top-width: 8px;
          }
    }

</style>

<script>
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');
    const simulationArea = document.getElementById('simulation-area');
    const magnetometer = document.getElementById('magnetometer');
    const fieldVector = document.getElementById('field-vector');
    const fieldDisplay = document.getElementById('field-display');
    const canvas = document.getElementById('magnetic-canvas');
    const ctx = canvas.getContext('2d');

    // Constants for physics (simplified units)
    const MU0_OVER_4PI = 1; // Simplified constant
    const DIPOLE_OFFSET = 20; // Distance between poles in the 2-pole magnet model

    let isDraggingMagnetometer = false;
    let isDraggingSource = false;
    let activeSource = null;
    let sources = []; // Array to hold magnetic sources {type: 'magnet'/'wire', x, y, strength, angle (for magnet), element}

    let drawFieldLines = false; // State variable for field line visibility

    // --- Toggle Explanation ---
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר מפורט' : 'הצג הסבר מפורט';
    });

    // --- Simulation Setup ---
    function resizeCanvas() {
        canvas.width = simulationArea.clientWidth;
        canvas.height = simulationArea.clientHeight;
        // Reposition sources and magnetometer if canvas size changes dramatically (optional, might need more complex logic)
        // For now, just redraw
        draw();
        // Update field display at the new magnetometer position
        updateMagnetometerPositionAndField();
    }

    window.addEventListener('resize', resizeCanvas);
    resizeCanvas(); // Initial resize

    // Add Source Buttons
    document.getElementById('add-magnet').addEventListener('click', () => {
        // Position new source near the center, slightly offset if others exist
        const newX = canvas.width / 2 + (sources.length % 3 - 1) * 50;
        const newY = canvas.height / 2 + (Math.floor(sources.length / 3) - 1) * 50;
        const source = {
            type: 'magnet',
            x: newX,
            y: newY,
            strength: 50, // Base strength
            angle: 0, // Default angle (pointing upwards, N pole above S)
            element: null
        };
        addSourceToDOM(source, 'https://cdn.jsdelivr.net/gh/byuphy/byuphy.github.io@main/images/magnet_icon.svg'); // Use magnet icon
        sources.push(source);
        draw();
        updateMagnetometerPositionAndField(); // Update display as field changed
    });

    document.getElementById('add-wire').addEventListener('click', () => {
        const newX = canvas.width / 2 + (sources.length % 3 - 1) * 50;
        const newY = canvas.height / 2 + (Math.floor(sources.length / 3) - 1) * 50;
        const source = {
            type: 'wire',
            x: newX,
            y: newY,
            strength: 50, // Base strength (represents current)
            element: null
        };
         addSourceToDOM(source, 'https://cdn.jsdelivr.net/gh/byuphy/byuphy.github.io@main/images/wire_icon.svg'); // Use wire icon
        sources.push(source);
        draw();
        updateMagnetometerPositionAndField(); // Update display as field changed
    });

     document.getElementById('remove-last-source').addEventListener('click', () => {
        if (sources.length > 0) {
            const removedSource = sources.pop();
            if (removedSource.element && simulationArea.contains(removedSource.element)) {
                 simulationArea.removeChild(removedSource.element);
            }
            // Re-index data attributes? Not strictly needed if we use element reference directly
            draw();
            updateMagnetometerPositionAndField(); // Update display as field changed
        }
    });


    document.getElementById('toggle-field-lines').addEventListener('click', () => {
         drawFieldLines = !drawFieldLines;
         draw(); // Redraw with or without lines
         document.getElementById('toggle-field-lines').textContent = drawFieldLines ? 'הסתר קווי שדה' : 'הצג קווי שדה';
    });


    function addSourceToDOM(source, iconSrc) {
        const sourceElement = document.createElement('div');
        sourceElement.classList.add('magnetic-source');
        // sourceElement.classList.add(source.type); // Add type class for specific styling if needed
        const img = document.createElement('img');
        img.src = iconSrc;
        img.alt = source.type === 'magnet' ? 'מגנט' : 'חוט זרם';
        sourceElement.appendChild(img);

        sourceElement.style.left = `${source.x - sourceElement.clientWidth / 2}px`; // Center element
        sourceElement.style.top = `${source.y - sourceElement.clientHeight / 2}px`; // Center element

        source.element = sourceElement; // Store element reference

        sourceElement.addEventListener('mousedown', (e) => {
             isDraggingSource = true;
             activeSource = source;
             sourceElement.style.cursor = 'grabbing';
             e.preventDefault(); // Prevent default drag behavior
             e.stopPropagation(); // Prevent event bubbling to simulationArea
        });
         sourceElement.addEventListener('touchstart', (e) => {
             isDraggingSource = true;
             activeSource = source;
             sourceElement.style.cursor = 'grabbing';
             e.preventDefault(); // Prevent default drag behavior
             e.stopPropagation(); // Prevent event bubbling to simulationArea
        }, { passive: false });

        simulationArea.appendChild(sourceElement);

        // Position correctly after adding to DOM and getting dimensions
         const rect = sourceElement.getBoundingClientRect();
         sourceElement.style.left = `${source.x - rect.width / 2}px`;
         sourceElement.style.top = `${source.y - rect.height / 2}px`;
    }


    // --- Dragging Logic ---
    magnetometer.addEventListener('mousedown', (e) => {
        isDraggingMagnetometer = true;
        magnetometer.style.cursor = 'grabbing';
        e.preventDefault();
    });
     magnetometer.addEventListener('touchstart', (e) => {
        if (e.touches.length === 1) {
            isDraggingMagnetometer = true;
            magnetometer.style.cursor = 'grabbing';
            e.preventDefault();
        }
    }, { passive: false });


    document.addEventListener('mousemove', (e) => {
        if (isDraggingMagnetometer) {
            moveMagnetometer(e.clientX, e.clientY);
        } else if (isDraggingSource && activeSource && activeSource.element) {
            moveSource(activeSource, e.clientX, e.clientY);
        }
    });
    document.addEventListener('touchmove', (e) => {
         if (e.touches.length === 1) {
            if (isDraggingMagnetometer) {
                moveMagnetometer(e.touches[0].clientX, e.touches[0].clientY);
            } else if (isDraggingSource && activeSource && activeSource.element) {
                moveSource(activeSource, e.touches[0].clientX, e.touches[0].clientY);
            }
         }
    }, { passive: false });

    document.addEventListener('mouseup', () => {
        if (isDraggingMagnetometer) {
            isDraggingMagnetometer = false;
            magnetometer.style.cursor = 'grab';
        }
         if (isDraggingSource && activeSource && activeSource.element) {
            isDraggingSource = false;
            activeSource.element.style.cursor = 'grab';
            activeSource = null;
        }
    });
     document.addEventListener('touchend', () => {
        if (isDraggingMagnetometer) {
            isDraggingMagnetometer = false;
            magnetometer.style.cursor = 'grab';
        }
         if (isDraggingSource && activeSource && activeSource.element) {
            isDraggingSource = false;
            if (activeSource.element) activeSource.element.style.cursor = 'grab';
            activeSource = null;
        }
    });


    function moveMagnetometer(clientX, clientY) {
        const rect = simulationArea.getBoundingClientRect();
        // Calculate position relative to simulation area's top-left corner
        let x = clientX - rect.left;
        let y = clientY - rect.top;

        // Clamp to bounds of simulation area
        x = Math.max(0, Math.min(canvas.width, x));
        y = Math.max(0, Math.min(canvas.height, y));

        // Update magnetometer position (element position is center-based)
        magnetometer.style.left = `${x}px`;
        magnetometer.style.top = `${y}px`;

        // Update the displayed field at the new position
        updateFieldDisplay(x, y);
    }

     function moveSource(source, clientX, clientY) {
        const rect = simulationArea.getBoundingClientRect();
        // Calculate position relative to simulation area's top-left corner
        let x = clientX - rect.left;
        let y = clientY - rect.top;

         // Clamp to bounds of simulation area
        x = Math.max(0, Math.min(canvas.width, x));
        y = Math.max(0, Math.min(canvas.height, y));

        // Update source's internal position data
        source.x = x;
        source.y = y;

        // Update source element position (element position is center-based)
         const sourceRect = source.element.getBoundingClientRect(); // Get current size
        source.element.style.left = `${x - sourceRect.width / 2}px`;
        source.element.style.top = `${y - sourceRect.height / 2}px`;

        // Redraw simulation including field lines if visible
        draw();
        // Also update the field display at the magnetometer's *current* position
        updateMagnetometerPositionAndField();
    }

    function updateMagnetometerPositionAndField() {
        // Get the magnetometer's current position relative to the simulation area
        const magRect = magnetometer.getBoundingClientRect();
        const simAreaRect = simulationArea.getBoundingClientRect();
        const magX = magRect.left + magRect.width / 2 - simAreaRect.left;
        const magY = magRect.top + magRect.height / 2 - simAreaRect.top;
        updateFieldDisplay(magX, magY);
    }


    // --- Field Calculation (Improved Physics) ---

    // Calculate field at (px, py) from all sources
    function calculateTotalField(px, py) {
        let totalBx = 0;
        let totalBy = 0;

        sources.forEach(source => {
            const dx = px - source.x;
            const dy = py - source.y;
            const r2 = dx * dx + dy * dy;
            const r = Math.sqrt(r2);

             // Avoid calculation if point is too close to source center
            if (r < 2) return; // Minimal distance to avoid division by zero or extreme values

            if (source.type === 'magnet') {
                // Simple 2D approximation of a dipole using two poles
                // N pole at (source.x, source.y - DIPOLE_OFFSET/2), S pole at (source.x, source.y + DIPOLE_OFFSET/2)
                // Let's rotate the poles based on source.angle
                const angleRad = source.angle * Math.PI / 180;
                const cosA = Math.cos(angleRad);
                const sinA = Math.sin(angleRad);

                // Pole positions relative to source center (0,0)
                const poleN_rel_x = -DIPOLE_OFFSET / 2 * sinA; // Rotate (0, -DIPOLE_OFFSET/2)
                const poleN_rel_y = -DIPOLE_OFFSET / 2 * cosA;
                const poleS_rel_x = DIPOLE_OFFSET / 2 * sinA;  // Rotate (0, DIPOLE_OFFSET/2)
                const poleS_rel_y = DIPOLE_OFFSET / 2 * cosA;

                // Absolute pole positions
                const poleN_x = source.x + poleN_rel_x;
                const poleN_y = source.y + poleN_rel_y;
                const poleS_x = source.x + poleS_rel_x;
                const poleS_y = source.y + poleS_rel_y;

                // Calculate field from North pole (repulsive)
                const dxN = px - poleN_x;
                const dyN = py - poleN_y;
                const rN2 = dxN * dxN + dyN * dyN;
                const rN = Math.sqrt(rN2);
                 if (rN > 1) { // Avoid extreme values near pole
                    const magnitudeN = source.strength / rN2; // Inverse square law for pole field
                    totalBx += magnitudeN * (dxN / rN); // Field points away from N
                    totalBy += magnitudeN * (dyN / rN);
                 }


                // Calculate field from South pole (attractive)
                const dxS = px - poleS_x;
                const dyS = py - poleS_y;
                const rS2 = dxS * dxS + dyS * dyS;
                const rS = Math.sqrt(rS2);
                if (rS > 1) { // Avoid extreme values near pole
                    const magnitudeS = source.strength / rS2; // Inverse square law for pole field
                    totalBx += magnitudeS * (-dxS / rS); // Field points towards S
                    totalBy += magnitudeS * (-dyS / rS);
                }


            } else if (source.type === 'wire') {
                // Field around a wire (current out of screen is positive strength)
                // Magnitude B = k * I / r (decreases with 1/r)
                // Direction is tangent to circle centered at wire, CCW for positive current
                const magnitude = source.strength / (r + 1e-6); // Add epsilon for stability
                totalBx += magnitude * (-dy / r); // Vector perpendicular to (dx, dy), scaled
                totalBy += magnitude * (dx / r);
            }
        });

        return { Bx: totalBx, By: totalBy };
    }

    function updateFieldDisplay(magX, magY) {
        const field = calculateTotalField(magX, magY);
        const magnitude = Math.sqrt(field.Bx * field.Bx + field.By * field.By);

        // Update numerical display (show in mT or some scaled unit if preferred)
        // Let's assume our strength units result in a display unit of "micro-Teslas" (µT) after scaling
        const scaleFactor = 0.1; // Arbitrary scale factor for display readability
        fieldDisplay.textContent = `Bx: ${(field.Bx * scaleFactor).toFixed(2)} µT, By: ${(field.By * scaleFactor).toFixed(2)} µT, עוצמה: ${(magnitude * scaleFactor).toFixed(2)} µT`;

        // Update vector arrow visual
        const vectorLength = Math.min(magnitude * 0.5, 60); // Scale vector length, cap at 60px
        fieldVector.style.height = `${vectorLength}px`;

        if (magnitude > 0.1) { // Only show vector if field is significant
            const angle = Math.atan2(field.By, field.Bx); // Angle in radians (0=right, pi/2=up, pi=left, -pi/2=down)
            // CSS transform rotate(angle) rotates clockwise. We want the arrow to point in the field direction.
            // The vector div is positioned at the bottom center of the magnetometer and rotates around its bottom.
            // The arrow tip is at the *top* of the vector div.
            // An angle of 0 (right) in physics vector should correspond to 90deg rotation in CSS (if pointing up initially) + angle correction.
            // If our vector div initially points UP (height>0, bottom-aligned, no rotation), its angle is -pi/2.
            // We want to rotate it by `angle + pi/2` radians (CCW).
            // CSS rotates CW. So rotate by `-(angle + pi/2)` radians.
            const cssAngleRad = -(angle + Math.PI / 2);
            const cssAngleDeg = cssAngleRad * (180 / Math.PI);

            fieldVector.style.display = 'block';
            fieldVector.style.transform = `translateX(-50%) rotate(${cssAngleDeg}deg)`;

        } else {
            fieldVector.style.display = 'none'; // Hide vector if field is too weak
        }
    }

    // --- Drawing on Canvas (for field lines) ---
    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear canvas

        if (drawFieldLines) {
            drawFieldLinesLogic();
        }

        // Optional: Draw sources on canvas as well (behind DOM elements) for consistency
        // This is not strictly necessary if DOM elements handle visuals and interaction
    }

    // Field line drawing logic (using numerical integration)
    function drawFieldLinesLogic() {
        ctx.strokeStyle = 'rgba(0, 123, 255, 0.6)'; // Blue lines, semi-transparent
        ctx.lineWidth = 1;
        const stepSize = 8; // Distance between points along a line (pixels)
        const maxSteps = 300; // Max points per line
        const minFieldForLine = 0.05; // Don't draw lines in very weak fields
        const maxFieldForStep = 20; // Cap field strength for step calculation to avoid tiny steps near sources

        // Strategy: Start lines near source perimeters
        const startPoints = [];
        sources.forEach(source => {
            if (source.type === 'magnet') {
                 // Start points around the poles
                 const angleRad = source.angle * Math.PI / 180;
                 const cosA = Math.cos(angleRad);
                 const sinA = Math.sin(angleRad);
                 const offset = DIPOLE_OFFSET / 2 + 10; // Start slightly further out
                 const poleN_x = source.x - offset * sinA;
                 const poleN_y = source.y - offset * cosA;
                 const poleS_x = source.x + offset * sinA;
                 const poleS_y = source.y + offset * cosA;

                // Distribute start points in arcs around the poles
                const numPoleLines = 8; // Lines per pole
                for(let i = 0; i < numPoleLines; i++) {
                    const arcAngleN = angleRad + Math.PI/2 + (i / (numPoleLines-1) - 0.5) * Math.PI; // Arc around N
                    startPoints.push({ x: poleN_x + 10 * Math.cos(arcAngleN), y: poleN_y + 10 * Math.sin(arcAngleN) });
                    const arcAngleS = angleRad - Math.PI/2 + (i / (numPoleLines-1) - 0.5) * Math.PI; // Arc around S
                     startPoints.push({ x: poleS_x + 10 * Math.cos(arcAngleS), y: poleS_y + 10 * Math.sin(arcAngleS) });
                }

            } else if (source.type === 'wire') {
                // Start points in a circle around the wire
                const numWireLines = 16; // Lines per wire
                const radius = 30; // Start slightly away from the wire icon
                for (let i = 0; i < numWireLines; i++) {
                    const angle = (i / numWireLines) * 2 * Math.PI;
                    startPoints.push({ x: source.x + radius * Math.cos(angle), y: source.y + radius * Math.sin(angle) });
                }
            }
        });

        // Fallback: If no sources, draw some lines from edges (less common use case)
        if (sources.length === 0) {
            const numEdgeLines = 15;
             for (let i = 0; i < numEdgeLines; i++) {
                 startPoints.push({ x: (i / numEdgeLines) * canvas.width, y: 0 });
                 startPoints.push({ x: 0, y: (i / numEdgeLines) * canvas.height });
             }
        }


        // Trace each field line
        startPoints.forEach(startPoint => {
            // Trace forward
            traceLine(startPoint.x, startPoint.y, maxSteps, stepSize, 1, minFieldForLine, maxFieldForStep);
            // Trace backward (unless it's a wire source which has closed loops)
            let isNearWireSource = sources.some(s => s.type === 'wire' && Math.sqrt((startPoint.x - s.x)**2 + (startPoint.y - s.y)**2) < 40);
            if (!isNearWireSource) {
                 traceLine(startPoint.x, startPoint.y, maxSteps, stepSize, -1, minFieldForLine, maxFieldForStep);
            }

        });

        function traceLine(startX, startY, steps, step, direction, minField, maxField) {
            ctx.beginPath();
            ctx.moveTo(startX, startY);

            let currentX = startX;
            let currentY = startY;

            for (let i = 0; i < steps; i++) {
                const field = calculateTotalField(currentX, currentY);
                const magnitude = Math.sqrt(field.Bx * field.Bx + field.By * field.By);

                if (magnitude < minField) break; // Stop if field is too weak

                // Normalize field vector and apply direction
                const dirX = (field.Bx / magnitude) * direction;
                const dirY = (field.By / magnitude) * direction;

                // Calculate step magnitude, cap if field is very strong
                const currentStepSize = Math.min(step, step * maxField / magnitude);

                // Move along the field direction
                currentX += dirX * currentStepSize;
                currentY += dirY * currentStepSize;

                // Stop if line goes out of bounds
                if (currentX < 0 || currentX > canvas.width || currentY < 0 || currentY > canvas.height) break;

                // Stop if line gets too close to a source center (prevent crowding/instability)
                 let tooCloseToSource = false;
                 for(const source of sources) {
                    const dist2 = (currentX - source.x)**2 + (currentY - source.y)**2;
                    if (dist2 < (source.type === 'magnet' ? DIPOLE_OFFSET/2 : 15)**2 ) { // If closer than specific radius
                        tooCloseToSource = true;
                        break;
                    }
                 }
                 if (tooCloseToSource) break;

                ctx.lineTo(currentX, currentY);
            }
            ctx.stroke();
        }
    }

    // Initial state: Update field display based on initial magnetometer position
    // Done automatically by resizeCanvas on load

</script>
```