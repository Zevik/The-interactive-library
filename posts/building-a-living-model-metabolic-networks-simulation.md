---
title: "בונים מודל חי: סימולציה של רשתות מטבוליות"
english_slug: building-a-living-model-metabolic-networks-simulation
category: "ביולוגיה"
tags:
  - מטבוליזם
  - רשתות מטבוליות
  - מודלים ביולוגיים
  - ביולוגיה חישובית
  - ביולוגיה מערכתית
---
# בונים מודל חי: סימולציה של רשתות מטבוליות

דמיינו לרגע את התא - עיר תוססת של פעילות כימית בלתי פוסקת! איך כל המרכיבים הללו עובדים יחד בתיאום מושלם, מגיבים לשינויים חיצוניים ופנימיים, ויוצרים את החיים עצמם? הלב הפועם של המערכת המדהימה הזו הוא **הרשת המטבולית**. אבל רשתות כאלו מורכבות מכדי שנוכל פשוט "לראות" אותן. איך נחקור אותן? איך נחזה מה יקרה כשאנחנו משנים משהו?

צאו למסע לבניית מודל חי! כאן תוכלו ליצור רשת מטבולית משלכם, להזיז את מרכיביה ולראות איך הקשרים ביניהם מתהווים. זו ההתנסות הראשונית שלכם בעולם הביולוגיה החישובית, המאפשרת לנו להפוך את הביולוגיה למשהו שניתן לבנות, לחקור ולשנות בזמן אמת.

<div id="app">
    <div id="toolbar">
        <div class="draggable-item" data-type="metabolite" title="גרור הוספת מולקולה (מטבוליט)">
            <span class="item-icon"></span>
            <span class="item-label">מולקולה</span>
        </div>
        <div class="draggable-item" data-type="reaction" title="גרור להוספת תגובה כימית">
            <span class="item-icon"></span>
            <span class="item-label">תגובה</span>
        </div>
    </div>
    <div id="network-container" style="position: relative; width: 100%; height: 600px; border: 1px solid #e0e0e0; background: linear-gradient(to bottom right, #f8f8f8, #e8e8e8); overflow: hidden; border-radius: 8px; box-shadow: inset 0 0 10px rgba(0,0,0,0.05);">
        <svg id="connection-layer" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none;"></svg>
        <div id="network-area" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
            <!-- Elements will be added here -->
        </div>
        <!-- Controls for elements -->
        <div id="reaction-controls" class="controls-panel" style="display: none;">
            <button data-action="add-reactant" title="קשר מטבוליט כמגיב לתגובה"><span class="control-icon">+</span> מגיב</button>
            <button data-action="add-product" title="קשר מטבוליט כתוצר של התגובה"><span class="control-icon">+</span> תוצר</button>
            <button data-action="remove-element" title="מחק תגובה" class="remove-button"><span class="control-icon">×</span></button>
        </div>
         <div id="metabolite-controls" class="controls-panel" style="display: none;">
             <button data-action="remove-element" title="מחק מולקולה" class="remove-button"><span class="control-icon">×</span></button>
         </div>
         <!-- Connection removal control -->
         <div id="connection-controls" class="controls-panel" style="display: none;">
             <button data-action="remove-connection" title="מחק קשר" class="remove-button"><span class="control-icon">×</span></button>
         </div>
    </div>
</div>
<button id="toggle-explanation" style="margin-top: 25px; padding: 12px 20px; font-size: 1.1em; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; transition: background-color 0.3s ease; font-weight: bold;">
    הצג/הסתר את הסודות של רשתות מטבוליות
</button>
<div id="explanation" style="display: none; margin-top: 20px; padding: 20px; border: 1px solid #e0e0e0; background-color: #f9f9f9; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
    <h2>מבט עמוק לתוך התא: רשתות מטבוליות במודלים חישוביים</h2>
    <p>התא הוא מעבדה ביולוגית מיניאטורית, מדהימה במורכבותה ובדיוקה. רשתות מטבוליות הן מערכת הכבישים הפנימית של המעבדה הזו – כל התגובות הכימיות שמנהלות את הפעילות התאית, החל מהפקת אנרגיה ועד לבניית אבני הבניין של התא.</p>

    <h3>אז מהי בעצם רשת מטבולית?</h3>
    <p>פשוטו כמשמעו, זוהי "מפת דרכים" של אלפי תגובות כימיות שמתרחשות בו-זמנית בתא. הרשת מחברת בין **מטבוליטים** (המולקולות הקטנות המשתתפות בתגובות, כמו סוכרים או חומצות אמינו) באמצעות **תגובות** שהופכות אותם מצורה אחת לאחרת. כל תגובה מקושרת למגיבים (המטבוליטים שנכנסים לתגובה) ולתוצרים (המטבוליטים שנוצרים ממנה). זוהי רשת דינמית שמאפשרת לתא להתקיים, לגדול, להתרבות ולהגיב לסביבה המשתנה.</p>

    <h3>בשביל מה לנו לבנות מודלים כאלה?</h3>
    <p>בניית מודלים חישוביים של רשתות מטבוליות מאפשרת לנו להפוך להיות בלשים מדעיים וחוקרים וירטואליים:</p>
    <ul>
        <li><strong>להבין את המאורג:</strong> לפענח איך מסלולים מטבוליים שונים (כמו ייצור אנרגיה או סינתזת חלבונים) משולבים, מתואמים ומווסתים יחד בתוך התא.</li>
        <li><strong>לחזות את הבלתי צפוי:</strong> לנבא מה יקרה לרשת כולה אם נשנה גורם אחד – למשל, אם חומר מסוים יהפוך לזמין יותר או פחות, או אם אנזים ספציפי ייחסם. זה קריטי בפיתוח תרופות או הבנת מחלות.</li>
        <li><strong>להנדס חיים:</strong> לתכנן שינויים בתא כדי "לתכנת" אותו לייצר חומרים שאנחנו רוצים בכמויות גדולות יותר (כמו דלק ביולוגי או ויטמינים), או לשפר תהליכים תעשייתיים המבוססים על תאים.</li>
    </ul>

    <h3>הגיבורים הראשיים במודל שלנו:</h3>
    <ul>
        <li><strong>מולקולה (מטבוליט):</strong> הן "הסחורה" שעוברת ברשת. זה יכול להיות גלוקוז, ATP, חומצות אמינו – כל חומר פעיל בתא. במודל הגרפי, נציג אותן כצמתים.</li>
        <li><strong>תגובה (כימית):</strong> הן "קווי הייצור" שהופכים מולקולות למולקולות אחרות. כל תגובה מקבלת מגיבים (חומרי מוצא) ומייצרת תוצרים (חומרי יעד). נציג אותן כקשתות או חצים המחברים בין המולקולות.</li>
    </ul>

    <h3>הצגה ויזואלית: הרשת כגרף</h3>
    <p>כדי לפשט את המורכבות, אנו מציגים רשתות מטבוליות כגרפים: המולקולות הן ה"צמתים" (עיגולים), והתגובות הן ה"קשתות" או ה"חצים" המחברים אותן. כיוון החץ מראה אם מולקולה היא מגיב (חץ נכנס לתגובה) או תוצר (חץ יוצא מהתגובה). זהו ייצוג אינטואיטיבי שמסייע מאוד בניתוח.</p>

    <h3>כלי הבנאי הדיגיטלי:</h3>
    <p>קיימים כלים חישוביים רבים ומתוחכמים לבניית וניתוח מודלים כאלה. הסימולציה הפשוטה כאן היא דוגמה מינימלית ואינטראקטיבית לכלי גרפי בסיסי, שנועד לתת לכם תחושה ראשונית של בניית רשת כזו, לראות איך המרכיבים מתחברים, ולעורר סקרנות לחקור הלאה.</p>

    <h3>האתגר: מהמודל לחיים האמיתיים</h3>
    <p>מודלים מדויקים דורשים המון נתונים – ריכוזים מדויקים, קצבי תגובה, מידע על כל האנזימים. לכן, מודלים הם לרוב הפשטה של המציאות התאית המלאה. ובכל זאת, גם מודלים פשוטים מאפשרים לנו לבחון השערות, לגלות דפוסים לא צפויים, ולבנות בהדרגה מודלים מורכבים יותר שמתקרבים לדמות את הדינמיקה הביולוגית האמיתית.</p>
    <p>עכשיו שהבנתם את העקרונות, חזרו למעלה והתחילו לבנות את הרשת המטבולית הדיגיטלית שלכם!</p>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6;
    }

    #app {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
        padding: 20px;
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    #toolbar {
        display: flex;
        gap: 20px;
        padding: 15px 25px;
        border: 1px solid #dcdcdc;
        border-radius: 30px; /* Pill shape */
        background-color: #ffffff;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .draggable-item {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 10px 18px;
        border-radius: 20px;
        cursor: grab;
        user-select: none;
        text-align: center;
        font-size: 1em;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

     .draggable-item:hover {
         transform: translateY(-2px);
         box-shadow: 0 4px 8px rgba(0,0,0,0.15);
     }

    .draggable-item .item-icon {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        display: inline-block;
        vertical-align: middle;
    }

    .draggable-item[data-type="metabolite"] {
        background-color: #e8f5e9; /* Light Green */
        color: #1b5e20; /* Dark Green */
        border: 1px solid #a5d6a7;
    }
     .draggable-item[data-type="metabolite"] .item-icon {
         background-color: #4caf50; /* Green */
     }

    .draggable-item[data-type="reaction"] {
        background-color: #ffebee; /* Light Red */
        color: #b71c1c; /* Dark Red */
        border: 1.5px solid #ef9a9a;
    }
     .draggable-item[data-type="reaction"] .item-icon {
         background-color: #f44336; /* Red */
     }


    .metabolite {
        position: absolute;
        width: 70px;
        height: 70px;
        border-radius: 50%;
        background: linear-gradient(135deg, #4caf50, #81c784); /* Green Gradient */
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: grab;
        border: 3px solid #388e3c; /* Darker Green Border */
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        font-size: 0.9em;
        font-weight: bold;
        text-align: center;
        user-select: none;
        pointer-events: all; /* Allows clicking/dragging */
        transform: translate(-50%, -50%); /* Center element on cursor */
        transition: box-shadow 0.2s ease, transform 0.1s ease;
    }

     .metabolite:hover {
         box-shadow: 0 6px 12px rgba(0,0,0,0.3);
         transform: translate(-50%, -50%) scale(1.05);
     }

    .reaction {
        position: absolute;
        width: 100px;
        height: 40px;
        background: linear-gradient(135deg, #f44336, #e57373); /* Red Gradient */
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: grab;
        border: 3px solid #d32f2f; /* Darker Red Border */
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        font-size: 0.9em;
        font-weight: bold;
        text-align: center;
        user-select: none;
        pointer-events: all; /* Allows clicking/dragging */
        transform: translate(-50%, -50%); /* Center element on cursor */
        transition: box-shadow 0.2s ease, transform 0.1s ease;
    }

     .reaction:hover {
         box-shadow: 0 6px 12px rgba(0,0,0,0.3);
         transform: translate(-50%, -50%) scale(1.05);
     }


    #network-area .dragging {
        opacity: 0.7;
        z-index: 50;
        cursor: grabbing;
    }

    #connection-layer line {
        stroke-width: 3;
        transition: stroke-width 0.2s ease, stroke 0.2s ease;
         /* pointer-events: all; /* Make lines clickable */
         /* cursor: pointer; */ /* Indicate clickability */
    }
    /* Delegation handled in JS for better control */


    #connection-layer line.reactant-line {
         stroke: #2e7d32; /* Dark Green */
         marker-end: url(#arrowhead-reactant);
         fill: none; /* Ensure fill is none for lines */
    }

    #connection-layer line.product-line {
         stroke: #c62828; /* Dark Red */
         stroke-dasharray: 6, 4; /* Dashed for product */
         marker-end: url(#arrowhead-product);
         fill: none; /* Ensure fill is none for lines */
    }

    #connection-layer line:hover {
         stroke-width: 5; /* Thicker on hover */
    }

    /* SVG Markers */
    #connection-layer defs marker polygon {
         stroke: none; /* No border on the arrow itself */
    }

     #arrowhead-reactant polygon { fill: #2e7d32; }
     #arrowhead-product polygon { fill: #c62828; }


    .controls-panel {
        position: absolute;
        background: white;
        border: 1px solid #dcdcdc;
        padding: 8px;
        border-radius: 6px;
        display: flex;
        gap: 5px;
        z-index: 100;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        transition: opacity 0.2s ease, transform 0.2s ease;
        opacity: 0;
        transform: translateY(10px);
        pointer-events: none; /* Initially cannot click */
    }
     .controls-panel.visible {
         opacity: 1;
         transform: translateY(0);
         pointer-events: all; /* Can click when visible */
     }

     .controls-panel button {
        margin: 0; /* Reset default button margin */
        padding: 6px 10px;
        cursor: pointer;
        border: none; /* Use background color for style */
        border-radius: 4px;
        font-size: 0.9em;
        font-weight: bold;
        transition: background-color 0.2s ease, opacity 0.2s ease;
        display: flex;
        align-items: center;
        gap: 3px;
     }

     .controls-panel button:hover {
         opacity: 0.9;
     }

      .controls-panel .control-icon {
          font-size: 1.2em;
      }

     #reaction-controls button[data-action="add-reactant"] {
         background-color: #e8f5e9; /* Light Green */
         color: #1b5e20; /* Dark Green */
     }

     #reaction-controls button[data-action="add-product"] {
         background-color: #ffebee; /* Light Red */
         color: #b71c1c; /* Dark Red */
     }

     .remove-button {
        background-color: #ffcdd2; /* Light Red */
        color: #c62828; /* Dark Red */
         margin-left: 15px !important; /* Space out remove button */
     }

     .remove-button:hover {
         background-color: #ef9a9a;
     }

    #toggle-explanation:hover {
        background-color: #0056b3;
    }

    #explanation {
        line-height: 1.7;
    }

    #explanation h2, #explanation h3 {
        color: #0056b3; /* Dark Blue */
        margin-top: 20px;
        margin-bottom: 10px;
        font-weight: bold;
    }

    #explanation ul {
        margin-bottom: 15px;
        padding-left: 20px;
    }

    #explanation li {
        margin-bottom: 8px;
        list-style: disc;
    }

     /* Connection Mode Visual Feedback */
     body.connecting-mode {
         cursor: crosshair;
     }

     .metabolite.connection-target {
         outline: 3px dashed #007bff;
         outline-offset: 3px;
         animation: pulse-glow 1s infinite alternate;
     }

    @keyframes pulse-glow {
        0% { box-shadow: 0 0 5px rgba(0, 123, 255, 0.4); }
        100% { box-shadow: 0 0 10px rgba(0, 123, 255, 0.8); }
    }

</style>

<script>
    const networkArea = document.getElementById('network-area');
    const connectionLayer = document.getElementById('connection-layer');
    const toolbarItems = document.querySelectorAll('.draggable-item');
    const reactionControls = document.getElementById('reaction-controls');
    const metaboliteControls = document.getElementById('metabolite-controls');
    const connectionControls = document.getElementById('connection-controls'); // New
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    let elements = []; // { id: unique, type: 'metabolite'|'reaction', x: pos, y: pos, label: text, domElement: DOM_element }
    let connections = []; // { id: unique, reactionId: R_id, metaboliteId: M_id, type: 'reactant'|'product', domElement: SVG_line_element }
    let nextMetaboliteId = 1;
    let nextReactionId = 1;
    let draggedElement = null; // The DOM element being dragged
    let dragOffset = { x: 0, y: 0 }; // Offset for dragging existing elements

    let activeConnectionReactionId = null; // Reaction ID waiting for metabolite click
    let activeConnectionType = null; // 'reactant' or 'product'
    let tempConnectionLine = null; // SVG line following cursor

    // Add arrowhead marker to SVG
    connectionLayer.innerHTML = `
        <defs>
            <marker id="arrowhead-reactant" markerWidth="10" markerHeight="7" refX="8" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7, 3 3.5" fill="#2e7d32" />
            </marker>
            <marker id="arrowhead-product" markerWidth="10" markerHeight="7" refX="2" refY="3.5" orient="auto">
                <polygon points="10 0, 0 3.5, 10 7, 7 3.5" fill="#c62828" />
            </marker>
        </defs>
    `; // Improved arrowhead shape

    // --- Drag and Drop from Toolbar ---
    toolbarItems.forEach(item => {
        item.addEventListener('dragstart', (e) => {
            e.dataTransfer.setData('text/plain', item.dataset.type);
            // Create a ghost image for drag
            const dragImg = item.cloneNode(true);
            dragImg.style.position = 'absolute';
            dragImg.style.top = '-100px'; // Off-screen
            dragImg.style.left = '-100px';
             dragImg.style.backgroundColor = 'rgba(255,255,255,0.8)';
             dragImg.style.boxShadow = '0 5px 15px rgba(0,0,0,0.2)';
            document.body.appendChild(dragImg);
            e.dataTransfer.setDragImage(dragImg, dragImg.offsetWidth / 2, dragImg.offsetHeight / 2);
            setTimeout(() => document.body.removeChild(dragImg), 0); // Clean up ghost image
        });
    });

    networkArea.addEventListener('dragover', (e) => {
        e.preventDefault(); // Necessary to allow dropping
        e.dataTransfer.dropEffect = 'copy';
         // Add visual cue to network area?
    });

     networkArea.addEventListener('dragleave', (e) => {
         // Remove visual cue?
     });


    networkArea.addEventListener('drop', (e) => {
        e.preventDefault();
        const type = e.dataTransfer.getData('text/plain');
        const rect = networkArea.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        addElement(type, x, y);
    });

    // --- Add Element Function ---
    function addElement(type, x, y) {
        // Hide any active controls/connections mode
        cancelConnectionMode();
        hideControls();

        const id = type === 'metabolite' ? `M${nextMetaboliteId++}` : `R${nextReactionId++}`;
        const label = id;
        // Store x, y as the intended center for consistency
        const element = { id, type, x, y, label, domElement: null };


        const domElement = document.createElement('div');
        domElement.classList.add(type);
        domElement.textContent = label;
         // Position using the center coordinates
        domElement.style.left = `${x}px`;
        domElement.style.top = `${y}px`;
        domElement.dataset.id = id;
        domElement.dataset.type = type;

        element.domElement = domElement; // Link DOM element back to data object
        elements.push(element); // Add element data to array

        networkArea.appendChild(domElement);

        // Add animation for element creation
         domElement.style.opacity = 0;
         domElement.style.transform = `translate(-50%, -50%) scale(0.8)`;
         requestAnimationFrame(() => {
             domElement.style.transition = 'opacity 0.3s ease-out, transform 0.3s ease-out, box-shadow 0.2s ease, border-color 0.2s ease';
             domElement.style.opacity = 1;
             domElement.style.transform = `translate(-50%, -50%) scale(1)`;
         });


        // Make the new element draggable and clickable
        makeDraggable(domElement, element);

        // Add click listener for controls and potentially initiating connections
        domElement.addEventListener('click', handleElementClick);

        // Ensure controls are hidden after adding
        hideControls();
    }

    // --- Handle Element Click (for Controls or Connection Target) ---
    function handleElementClick(e) {
        e.stopPropagation(); // Prevent network area click

        const clickedElementDom = e.target.closest('.metabolite, .reaction');
        if (!clickedElementDom) return;

        const elementId = clickedElementDom.dataset.id;
        const elementType = clickedElementDom.dataset.type;

        if (activeConnectionReactionId && activeConnectionType) {
            // We are in connection mode, the clicked element MUST be a metabolite
            if (elementType === 'metabolite') {
                const reactionId = activeConnectionReactionId;
                const metaboliteId = elementId;
                const type = activeConnectionType;

                // Check if this connection already exists
                const exists = connections.some(conn =>
                    conn.reactionId === reactionId && conn.metaboliteId === metaboliteId && conn.type === type);

                if (!exists) {
                     // Generate a unique connection ID
                    const connectionId = `conn_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
                    connections.push({ id: connectionId, reactionId, metaboliteId, type, domElement: null }); // Add to data array
                    renderConnections(); // Re-render all connections including the new one
                }

                // Connection attempt finished, exit connection mode
                cancelConnectionMode();

            } else {
                // Clicked a reaction while in connection mode - maybe cancel or show controls for that reaction?
                 // For now, let's just cancel the connection mode.
                 console.log("Clicked a reaction while in connection mode. Cancelling connection.");
                 cancelConnectionMode();
                 // Optionally, show controls for the clicked reaction
                 showControls(clickedElementDom, elementType);
            }

        } else {
            // Not in connection mode, show controls for the clicked element
            showControls(clickedElementDom, elementType);
        }
    }

    // --- Show Controls ---
    function showControls(targetElementDom, elementType) {
        hideControls(); // Hide any currently visible controls

        let controlsElement;
        let datasetIdName; // e.g., 'reactionId' or 'metaboliteId'

        if (elementType === 'reaction') {
            controlsElement = reactionControls;
            datasetIdName = 'reactionId';
        } else if (elementType === 'metabolite') {
            controlsElement = metaboliteControls;
            datasetIdName = 'metaboliteId';
        } else {
            return; // Unknown type
        }

        const elementId = targetElementDom.dataset.id;
        controlsElement.dataset[datasetIdName] = elementId; // Store which element these controls belong to

        // Position controls relative to the element
        positionControls(controlsElement, targetElementDom);

        // Set up remove button listener for THIS element
        const removeBtn = controlsElement.querySelector('button[data-action="remove-element"]');
        if (removeBtn) {
             removeBtn.onclick = () => removeElement(elementId);
        }

        // Add specific listeners for reaction buttons if applicable
        if (elementType === 'reaction') {
            controlsElement.querySelector('button[data-action="add-reactant"]').onclick = () => initiateConnectionMode(elementId, 'reactant');
            controlsElement.querySelector('button[data-action="add-product"]').onclick = () => initiateConnectionMode(elementId, 'product');
        }


        // Display controls with animation
        controlsElement.classList.add('visible');
    }

    // --- Hide All Controls ---
     function hideControls() {
        reactionControls.classList.remove('visible');
        metaboliteControls.classList.remove('visible');
         connectionControls.classList.remove('visible'); // Also hide connection controls
        // Remove dataset IDs
        reactionControls.dataset.reactionId = '';
        metaboliteControls.dataset.metaboliteId = '';
         connectionControls.dataset.connectionId = '';

         // Ensure pointer-events are off when hidden
         reactionControls.style.pointerEvents = 'none';
         metaboliteControls.style.pointerEvents = 'none';
         connectionControls.style.pointerEvents = 'none';

         // Clean up potential click handlers if needed (though onclick reassignment handles this)
     }

    // --- Initiate Connection Mode (Click + Reactant/Product) ---
    function initiateConnectionMode(reactionId, type) {
        activeConnectionReactionId = reactionId;
        activeConnectionType = type;

        // Hide element controls but keep connection mode active
        hideControls(); // Hide the reaction controls that were just used

        document.body.classList.add('connecting-mode'); // Change cursor
        networkArea.querySelectorAll('.metabolite').forEach(metaboliteDom => {
             metaboliteDom.classList.add('connection-target'); // Highlight metabolites
        });

        // Start drawing temporary line
        const reactionElement = elements.find(el => el.id === reactionId);
        if (!reactionElement || !reactionElement.domElement) return;

         // Remove any existing temporary line
         if (tempConnectionLine) {
             tempConnectionLine.remove();
             tempConnectionLine = null;
         }

        tempConnectionLine = document.createElementNS('http://www.w3.org/2000/svg', 'line');
         tempConnectionLine.setAttribute('stroke', type === 'reactant' ? '#1b5e20' : '#b71c1c'); // Match type color
         tempConnectionLine.setAttribute('stroke-width', 3);
         tempConnectionLine.setAttribute('stroke-dasharray', type === 'product' ? '6,4' : '0'); // Dashed for product
         tempConnectionLine.style.pointerEvents = 'none'; // Ignore during drag
        connectionLayer.appendChild(tempConnectionLine);

        // Add mousemove listener to update temporary line
        networkArea.addEventListener('mousemove', updateTempConnectionLine);

        console.log(`Connection mode active: Click a metabolite to connect as ${type} to Reaction ${reactionId}`);
    }

    // --- Update Temporary Connection Line ---
    function updateTempConnectionLine(e) {
         if (!tempConnectionLine || !activeConnectionReactionId) return;

         const reactionElement = elements.find(el => el.id === activeConnectionReactionId);
         if (!reactionElement || !reactionElement.domElement) return;

         const reactionCenter = getElementCenter(activeConnectionReactionId);
         if (!reactionCenter) return;

         const networkRect = networkArea.getBoundingClientRect();
         const mouseX = e.clientX - networkRect.left;
         const mouseY = e.clientY - networkRect.top;

         let x1, y1, x2, y2;

         // Line goes FROM reaction center TO mouse position for reactants,
         // and FROM mouse position TO reaction center for products.
         // This visual feedback feels more intuitive. Let's rethink.

         // More intuitive: line goes from REACTION to MOUSE for PRODUCT, and MOUSE to REACTION for REACTANT.
         // This represents the *potential* flow.

         if (activeConnectionType === 'reactant') {
             // Metabolite (mouse) -> Reaction
             x1 = mouseX;
             y1 = mouseY;
             x2 = reactionCenter.x;
             y2 = reactionCenter.y;
              tempConnectionLine.setAttribute('marker-end', `url(#arrowhead-reactant)`);
         } else { // product
             // Reaction -> Metabolite (mouse)
             x1 = reactionCenter.x;
             y1 = reactionCenter.y;
             x2 = mouseX;
             y2 = mouseY;
              tempConnectionLine.setAttribute('marker-end', `url(#arrowhead-product)`);
         }


         tempConnectionLine.setAttribute('x1', x1);
         tempConnectionLine.setAttribute('y1', y1);
         tempConnectionLine.setAttribute('x2', x2);
         tempConnectionLine.setAttribute('y2', y2);
     }

    // --- Cancel Connection Mode ---
    function cancelConnectionMode() {
        activeConnectionReactionId = null;
        activeConnectionType = null;
        document.body.classList.remove('connecting-mode'); // Reset cursor
         networkArea.querySelectorAll('.metabolite').forEach(metaboliteDom => {
             metaboliteDom.classList.remove('connection-target'); // Remove highlight
        });

        // Remove temporary line
        if (tempConnectionLine) {
            tempConnectionLine.remove();
            tempConnectionLine = null;
        }

        // Remove mousemove listener
        networkArea.removeEventListener('mousemove', updateTempConnectionLine);
        console.log("Connection mode cancelled.");
    }


    // --- Draggable Functionality for Placed Elements ---
    function makeDraggable(domElement, elementData) {
        domElement.addEventListener('mousedown', (e) => {
            // Only allow dragging with left mouse button and not in connection mode
            if (e.button !== 0 || activeConnectionReactionId) return;

            // Don't start drag if clicking a control button within the element (controls are outside now, but good check)
            // if (e.target.tagName === 'BUTTON') return;

            draggedElement = domElement;
            // Calculate offset relative to the element's top-left corner
            const rect = domElement.getBoundingClientRect();
            dragOffset = {
                x: e.clientX - rect.left,
                y: e.clientY - rect.top
            };

            domElement.classList.add('dragging');
            // Cursor handled by CSS :active on body or specific element

             // Bring dragged element to front (basic z-index)
            domElement.style.zIndex = 10;

            // Hide controls if visible when starting drag
            hideControls();
            cancelConnectionMode(); // Also cancel connection mode if active

            document.addEventListener('mousemove', onMouseMove);
            document.addEventListener('mouseup', onMouseUp);

             e.preventDefault(); // Prevent default drag behaviors that might interfere
        });
    }

    function onMouseMove(e) {
        if (!draggedElement) return;

        const networkRect = networkArea.getBoundingClientRect();
         // Calculate new top-left position based on mouse and offset
        let newLeft = e.clientX - networkRect.left - dragOffset.x;
        let newTop = e.clientY - networkRect.top - dragOffset.y;

         // Keep element within network bounds (optional but good)
         newLeft = Math.max(0, Math.min(newLeft, networkArea.offsetWidth - draggedElement.offsetWidth));
         newTop = Math.max(0, Math.min(newTop, networkArea.offsetHeight - draggedElement.offsetHeight));


        // Update element DOM position
        draggedElement.style.left = `${newLeft}px`;
        draggedElement.style.top = `${newTop}px`;

         // Update element data object (store center coordinates)
        const elementData = elements.find(el => el.id === draggedElement.dataset.id);
        if (elementData) {
             elementData.x = newLeft + draggedElement.offsetWidth / 2;
             elementData.y = newTop + draggedElement.offsetHeight / 2;
        }

        // Re-render connections
        renderConnections();
    }

    function onMouseUp() {
        if (!draggedElement) return;

        draggedElement.classList.remove('dragging');
        draggedElement.style.cursor = 'grab'; // Reset cursor (CSS might handle this too)
         draggedElement.style.zIndex = ''; // Remove z-index override

        draggedElement = null;
        dragOffset = { x: 0, y: 0 };

        document.removeEventListener('mousemove', onMouseMove);
        document.removeEventListener('mouseup', onMouseUp);
    }

    // --- Connection Logic ---
     function getElementCenter(elementId) {
        const element = elements.find(el => el.id === elementId);
        if (!element || !element.domElement) return null;
         // Use the stored x, y which represent the center
        return { x: element.x, y: element.y };
    }

    function renderConnections() {
        // Clear previous connections (SVG elements only)
        connectionLayer.querySelectorAll('line').forEach(line => line.remove());

        connections.forEach(conn => {
            const reactionCenter = getElementCenter(conn.reactionId);
            const metaboliteCenter = getElementCenter(conn.metaboliteId);

            if (!reactionCenter || !metaboliteCenter) {
                console.warn(`Could not find centers for connection (will remove data): ${conn.reactionId} <-> ${conn.metaboliteId}`);
                 // Remove connection data if elements no longer exist (basic cleanup)
                connections = connections.filter(c => c.id !== conn.id);
                renderConnections(); // Re-render after cleanup
                return;
            }

             let x1, y1, x2, y2;
             let markerEndId;
             let lineClass;

             if (conn.type === 'reactant') {
                 // Metabolite -> Reaction
                 x1 = metaboliteCenter.x;
                 y1 = metaboliteCenter.y;
                 x2 = reactionCenter.x;
                 y2 = reactionCenter.y;
                 markerEndId = '#arrowhead-reactant'; // Arrow points to reaction
                 lineClass = 'reactant-line';
             } else { // product
                 // Reaction -> Metabolite
                 x1 = reactionCenter.x;
                 y1 = reactionCenter.y;
                 x2 = metaboliteCenter.x;
                 y2 = metaboliteCenter.y;
                 markerEndId = '#arrowhead-product'; // Arrow points to metabolite
                 lineClass = 'product-line';
             }

            const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            line.setAttribute('x1', x1);
            line.setAttribute('y1', y1);
            line.setAttribute('x2', x2);
            line.setAttribute('y2', y2);
             line.classList.add(lineClass);
             line.setAttribute('marker-end', `url(${markerEndId})`);
             line.dataset.connectionId = conn.id; // Store connection ID
            line.style.pointerEvents = 'all'; // Make lines clickable
             line.style.cursor = 'pointer';

             // Add click listener directly to the line for removal
             line.addEventListener('click', handleConnectionClick);

            connectionLayer.appendChild(line);

             // Store DOM element reference in connection data
             conn.domElement = line;
        });
    }

    // --- Handle Connection Line Click (for Removal) ---
    function handleConnectionClick(e) {
        e.stopPropagation(); // Prevent network area click
        cancelConnectionMode(); // Cancel connection mode if active
        hideControls(); // Hide other controls

        const clickedLine = e.target.closest('line');
        if (!clickedLine) return;

        const connectionId = clickedLine.dataset.connectionId;
        const connectionData = connections.find(c => c.id === connectionId);
        if (!connectionData) return;

        // Highlight the clicked connection temporarily? Or just show controls.
        // clickedLine.style.stroke = '#ff0000'; // Example highlight

        // Position connection controls near the click point or the center of the line
        const networkRect = networkArea.getBoundingClientRect();
        const clickX = e.clientX - networkRect.left;
        const clickY = e.clientY - networkRect.top;

        connectionControls.dataset.connectionId = connectionId; // Store which connection
        positionControlsAt(connectionControls, clickX, clickY); // Position at click
        connectionControls.classList.add('visible'); // Show

        // Set up remove button listener for THIS connection
        const removeBtn = connectionControls.querySelector('button[data-action="remove-connection"]');
        if (removeBtn) {
             removeBtn.onclick = () => removeConnection(connectionId);
        }
    }


    // --- Position Controls ---
    function positionControls(controlsElement, targetElementDom) {
        const rect = targetElementDom.getBoundingClientRect();
        const networkRect = networkArea.getBoundingClientRect();
        // Position controls to the right of the element
        let left = rect.right - networkRect.left + 10;
        let top = rect.top - networkRect.top;

         // Adjust if goes off screen (simple check)
         if (left + controlsElement.offsetWidth > networkArea.offsetWidth) {
             left = rect.left - networkRect.left - controlsElement.offsetWidth - 10; // Position to the left
         }
         if (top + controlsElement.offsetHeight > networkArea.offsetHeight) {
              top = networkArea.offsetHeight - controlsElement.offsetHeight - 5; // Align to bottom
         }
          if (top < 0) {
              top = 5; // Align to top if needed
          }


        controlsElement.style.left = `${left}px`;
        controlsElement.style.top = `${top}px`;
    }

    function positionControlsAt(controlsElement, x, y) {
         // Position controls centered around the given point (x, y are relative to networkArea)
         let left = x - controlsElement.offsetWidth / 2;
         let top = y - controlsElement.offsetHeight / 2;

         // Keep within bounds (more robust check needed for edges, but basic is better than none)
         left = Math.max(0, Math.min(left, networkArea.offsetWidth - controlsElement.offsetWidth));
         top = Math.max(0, Math.min(top, networkArea.offsetHeight - controlsElement.offsetHeight));


         controlsElement.style.left = `${left}px`;
         controlsElement.style.top = `${top}px`;
    }


    // --- Remove Element Function ---
    function removeElement(elementId) {
         // Find the element's DOM node before removing from array
        const domElementToRemove = networkArea.querySelector(`[data-id="${elementId}"]`);

         // Remove element from elements array
        elements = elements.filter(el => el.id !== elementId);

         // Remove connections involving this element from data array
        connections = connections.filter(conn =>
            conn.reactionId !== elementId && conn.metaboliteId !== elementId);

         // Remove DOM element with animation
         if (domElementToRemove) {
             domElementToRemove.style.transition = 'opacity 0.3s ease-out, transform 0.3s ease-out';
             domElementToRemove.style.opacity = 0;
             domElementToRemove.style.transform = `translate(-50%, -50%) scale(0.8)`;
             // Remove after animation completes
             domElementToRemove.addEventListener('transitionend', () => {
                 domElementToRemove.remove();
                 renderConnections(); // Re-render connections AFTER element is removed and connections data is updated
             });
         } else {
              // If DOM element wasn't found for some reason, just re-render connections based on updated data
             renderConnections();
         }


         // Hide controls if the removed element's controls were visible
        hideControls();
        cancelConnectionMode();
    }

    // --- Remove Connection Function ---
    function removeConnection(connectionId) {
         // Find the connection's DOM node before removing from array
        const connectionDomToRemove = connectionLayer.querySelector(`[data-connection-id="${connectionId}"]`);

         // Remove connection from connections array
        connections = connections.filter(conn => conn.id !== connectionId);

         // Remove DOM element with animation
         if (connectionDomToRemove) {
              connectionDomToRemove.style.transition = 'stroke-width 0.3s ease, opacity 0.3s ease';
              connectionDomToRemove.style.strokeWidth = 5; /* Thicker briefly */
             connectionDomToRemove.style.opacity = 0;
              // Remove after animation
             connectionDomToRemove.addEventListener('transitionend', () => {
                 connectionDomToRemove.remove();
                  // No need to re-renderConnections here, as only one line was removed
             });
         }

         // Hide connection controls
         hideControls();
    }


    // --- Handle Clicks Outside Elements/Controls to Hide Controls ---
    networkArea.addEventListener('click', (e) => {
        // Check if the click target is NOT inside any element, controls panel, or the connection layer itself (lines)
        const isClickInsideElement = e.target.closest('.metabolite, .reaction');
        const isClickInsideControls = e.target.closest('.controls-panel');
        const isClickOnLine = e.target.closest('line'); // Check if clicked on an SVG line

        if (!isClickInsideElement && !isClickInsideControls && !isClickOnLine) {
            hideControls();
            cancelConnectionMode(); // Also cancel connection mode on empty click
        }
    });

     // Also listen on the document body to catch clicks anywhere outside networkArea (e.g. toolbar)
     document.body.addEventListener('click', (e) => {
         const isClickInsideApp = e.target.closest('#app');
          const isClickOnExplanation = e.target.closest('#explanation');
         if (!isClickInsideApp && !isClickOnExplanation) {
             hideControls();
             cancelConnectionMode();
         }
     });


    // --- Toggle Explanation ---
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        // Smooth toggle effect (optional, requires transition on height/max-height)
        if (isHidden) {
            explanationDiv.style.display = 'block';
             // Simple show
             toggleExplanationButton.textContent = 'הסתר את הסודות של רשתות מטבוליות';
        } else {
             // Simple hide
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'הצג/הסתר את הסודות של רשתות מטבוליות';
        }
    });

     // Ensure controls are hidden on initial load
     hideControls();
     // Initial render (useful if loading pre-defined elements/connections in the future)
     renderConnections();

</script>
---
```