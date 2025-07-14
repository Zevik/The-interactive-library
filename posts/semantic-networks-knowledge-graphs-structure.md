---
title: "מבנה הידע: רשתות סמנטיות וגרפי ידע"
english_slug: semantic-networks-knowledge-graphs-structure
category: "מדעי החברה / פסיכולוגיה"
tags: ["רשתות סמנטיות", "גרף ידע", "מבנה נתונים", "קוגניציה", "בינה מלאכותית"]
---
<h1>מבנה הידע: לחבר את הנקודות, תרתי משמע!</h1>

איך המוח הגאוני שלנו (או מחשב מתקדם) מצליח לקשר רעיונות שונים כמו 'חתול', 'יונק' ו'לצוד עכברים'? האם יש דרך מלהיבה לדמיין איך כל פיסת מידע בעולם מתחברת לאחרת ויוצרת תמונה גדולה וברורה? בואו ניצור יחד את מפת הידע האישית שלנו ונחקור איך קשרים פשוטים בונים הבנה עמוקה!

<div id="app-container">
    <div id="controls" class="control-panel">
        <h3>בנו את גרף הידע שלכם:</h3>
        <div class="control-group">
            <label for="newNodeLabel">הוספת מושג חדש (צומת):</label>
            <div class="input-group">
                <input type="text" id="newNodeLabel" placeholder="למשל: 'עץ', 'כדור הארץ'">
                <button id="addNodeButton" class="action-button primary">הוסף מושג</button>
            </div>
        </div>

        <div class="control-group">
             <label for="edgeFromNode">חיבור מושגים (קשת):</label>
             <div class="input-group edge-input-group">
                <select id="edgeFromNode" class="node-select"></select>
                <span class="arrow">&rarr;</span>
                <select id="edgeToNode" class="node-select"></select>
                <input type="text" id="edgeLabel" placeholder="סוג הקשר (למשל: 'נמצא על', 'הוא סוג של')">
                <button id="addEdgeButton" class="action-button secondary">חבר</button>
            </div>
        </div>
         <p class="tip">רחפו עם העכבר על מושג בגרף כדי לראות את שמו המלא!</p>
    </div>
    <div id="graph-area">
        <svg id="knowledge-graph" width="800" height="500" viewBox="0 0 800 500"></svg>
    </div>
</div>

<style>
    /* Basic structure & Layout */
    #app-container {
        display: flex;
        flex-direction: column;
        gap: 30px; /* Increased gap for better separation */
        margin-bottom: 40px;
        font-family: 'Arial', sans-serif; /* Modern font */
        direction: rtl;
        text-align: right;
        background-color: #f8f9fa; /* Light background */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Soft shadow */
    }

    /* Controls Styling */
    .control-panel {
        background-color: #e9ecef; /* Slightly different background */
        padding: 20px;
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    .control-panel h3 {
        margin-top: 0;
        color: #343a40; /* Darker text */
        border-bottom: 1px solid #ced4da; /* Separator line */
        padding-bottom: 10px;
        margin-bottom: 15px;
    }

    .control-group label {
        display: block; /* Label on its own line */
        margin-bottom: 8px;
        font-weight: bold;
        color: #495057;
    }

    .input-group {
        display: flex;
        align-items: center;
        gap: 10px; /* Space between inputs/buttons */
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
    }

    .edge-input-group select {
        flex-grow: 1; /* Allow selects to grow */
        min-width: 100px; /* Minimum width */
    }
     .edge-input-group input[type="text"] {
         flex-grow: 2; /* Allow edge label input to grow more */
         min-width: 120px;
     }


    .control-panel input[type="text"],
    .control-panel select {
        padding: 10px 12px;
        border: 1px solid #ced4da;
        border-radius: 5px;
        font-size: 1rem;
        color: #495057;
        background-color: #fff;
        transition: border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    }

    .control-panel input[type="text"]:focus,
    .control-panel select:focus {
        border-color: #007bff;
        box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
        outline: none;
    }

     .arrow {
         font-size: 1.2rem;
         font-weight: bold;
         color: #6c757d;
     }

    /* Buttons Styling */
    .action-button {
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1rem;
        font-weight: bold;
        transition: background-color 0.2s ease-in-out, opacity 0.2s ease-in-out;
        flex-shrink: 0; /* Prevent buttons from shrinking */
    }

    .action-button.primary {
        background-color: #28a745; /* Green for adding nodes */
        color: white;
    }
    .action-button.primary:hover {
        background-color: #218838;
    }

    .action-button.secondary {
        background-color: #007bff; /* Blue for adding edges */
        color: white;
    }
    .action-button.secondary:hover {
        background-color: #0056b3;
    }

     .action-button:disabled {
         opacity: 0.6;
         cursor: not-allowed;
     }


    .tip {
        font-size: 0.9em;
        color: #6c757d;
        margin-top: 5px;
        text-align: center; /* Center tip text */
    }


    /* Graph Area Styling */
    #graph-area {
        border: 1px solid #ced4da;
        border-radius: 8px;
        background-color: #ffffff;
        overflow: hidden;
        position: relative; /* Needed for tooltip positioning */
         box-shadow: inset 0 1px 3px rgba(0,0,0,0.05); /* Inner shadow */
    }

    #knowledge-graph {
        display: block;
        border-radius: 8px;
        /* The SVG itself has fixed dimensions (800x500) as per original code structure. */
        /* If responsiveness was allowed beyond constraints, this would be width: 100%, height: auto; */
    }

    /* SVG Node & Edge Styling */
    .node circle {
        fill: #17a2b8; /* Teal */
        stroke: #138496; /* Darker Teal */
        stroke-width: 2px; /* Thicker stroke */
        cursor: pointer;
        transition: fill 0.2s ease-in-out, stroke 0.2s ease-in-out; /* Smooth hover transition */
        /* Add transition for transform/opacity for animation */
        transition: fill 0.3s ease-in-out, stroke 0.3s ease-in-out, transform 0.5s ease-out, opacity 0.5s ease-out;
    }

    .node:hover circle {
        fill: #138496; /* Darker on hover */
        stroke: #0f6674;
    }

    .node text {
        font-size: 12px;
        fill: white;
        text-anchor: middle;
        alignment-baseline: central;
        pointer-events: none; /* Allow clicking circle */
        direction: rtl;
        unicode-bidi: embed;
        font-weight: bold; /* Make text bolder */
    }

    /* Animation for new nodes */
    .node.node-new {
        opacity: 0;
        transform: scale(0.5); /* Start smaller */
    }


    .edge line {
        stroke: #6c757d; /* Gray */
        stroke-width: 2px;
        pointer-events: none;
        transition: stroke 0.2s ease-in-out;
    }
     /* Arrowhead color matches edge line */
    #arrowhead polygon {
         fill: #6c757d;
         transition: fill 0.2s ease-in-out;
    }


    .edge text {
        font-size: 10px;
        fill: #343a40; /* Darker text */
        text-anchor: middle;
        direction: rtl;
        unicode-bidi: embed;
        font-weight: bold; /* Make text bolder */
    }

    /* Explanation Section */
    #explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #ced4da;
        border-radius: 8px;
        background-color: #ffffff;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        direction: rtl;
        text-align: right;
    }

    #explanation h2 {
        margin-top: 0;
        color: #343a40;
        border-bottom: 1px solid #ced4da;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }
     #explanation h2:before {
         content: "📚 "; /* Add icon */
     }


    #explanation ul {
        padding-right: 25px; /* Adjusted for RTL */
        list-style-type: disc;
        color: #495057;
        line-height: 1.6; /* Improved readability */
    }
     #explanation ul ul { /* Nested lists */
        margin-top: 5px;
        margin-bottom: 5px;
        padding-right: 20px;
         list-style-type: circle;
     }

     #explanation strong {
         color: #343a40;
     }

    #toggle-explanation {
        padding: 10px 15px;
        background-color: #6c757d; /* Gray button */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 20px;
        display: block; /* Make it a block element */
        width: fit-content; /* Fit width to content */
        margin-left: auto; /* Center or align right in RTL */
        margin-right: auto; /* Center if left/right auto doesn't work */
        transition: background-color 0.2s ease-in-out;
    }
    #toggle-explanation:hover {
        background-color: #5a6268;
    }

     /* Tooltip for node labels on hover */
    .node-tooltip {
        position: fixed; /* Use fixed to avoid issues with SVG container */
        background-color: rgba(52, 58, 64, 0.95); /* Darker, slightly transparent */
        color: white;
        padding: 6px 12px; /* More padding */
        border-radius: 5px;
        pointer-events: none;
        z-index: 100; /* High z-index */
        font-size: 13px; /* Slightly larger font */
        transform: translate(-50%, -110%); /* Position above and center tooltip, slightly higher */
        white-space: nowrap;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Add shadow to tooltip */
    }

    /* Basic Responsiveness (within SVG fixed size limitation) */
    @media (max-width: 850px) {
        #knowledge-graph {
            width: 100%; /* Allow SVG to take full width of its container */
            height: auto; /* Maintain aspect ratio (best effort) */
        }
        .input-group {
             flex-direction: column; /* Stack inputs/buttons vertically */
             align-items: stretch; /* Stretch items to fill width */
        }
         .input-group input,
         .input-group select,
         .input-group button {
             width: 100%; /* Full width on small screens */
             box-sizing: border-box; /* Include padding/border in width */
             margin-left: 0 !important; /* Override previous margin-left */
         }
         .arrow {
             text-align: center; /* Center arrow when stacked */
         }
         .edge-input-group {
             gap: 5px; /* Smaller gap when stacked */
         }
         .tip {
             text-align: right; /* Back to right aligned for tip */
         }
         .control-group label {
             text-align: right;
         }

    }

</style>

<button id="toggle-explanation">הצג/הסתר מבט מעמיק על גרפי ידע</button>

<div id="explanation" style="display: none;">
    <h2>מבט מעמיק: מה עומד מאחורי גרף הידע שיצרתם?</h2>
    <p>הגרף שבניתם הוא הדגמה פשוטה אך עוצמתית לרעיון שמאחורי רשתות סמנטיות וגרפי ידע – שיטות מפתח לייצוג ידע בבינה מלאכותית ובמדעי הקוגניציה.</p>
    <ul>
        <li><strong>מהי בעצם רשת סמנטית או גרף ידע?</strong>
            <ul>
                <li>דמיינו מפה ענקית של רעיונות: רשתות סמנטיות וגרפי ידע הן בדיוק כאלה! מודלים חזותיים שמארגנים מידע בצורת גרף. כל 'נקודה' במפה היא מושג או ישות (צומת), וכל 'קו' שמחבר בין נקודות הוא קשר או יחס ביניהם (קשת). בעוד שרשתות סמנטיות הן מושג קלאסי מתחום הבינה המלאכותית של פעם, גרפי ידע הם הגרסה המשודרגת והמסיבית שלהן, שמהווה את עמוד השדרה של מערכות בינה מלאכותית מודרניות כמו אלו של גוגל ואמזון.</li>
            </ul>
        </li>
        <li><strong>הגיבורים הראשיים: צמתים וקשתות</strong>
            <ul>
                <li><strong>צמתים (Nodes):</strong> אלו ה'דברים' שאנחנו מדברים עליהם – אובייקטים, מושגים, אנשים, מקומות, אירועים. כל דבר שיש לו שם ותכונות יכול להיות צומת. (למשל, 'חתול', 'איינשטיין', 'פריז', 'נחיתה על הירח').</li>
                <li><strong>קשתות (Edges):</strong> אלו ה'קשרים' – הן מראות איך צמתים קשורים זה לזה. הן תמיד מכוונות (יש להן כיוון, ממושג אחד לשני) ולרוב יש להן 'תווית' שמסבירה את סוג הקשר. (למשל, 'הוא סוג של', 'נולד ב-', 'כתב את', 'ממוקם ב-').</li>
            </ul>
        </li>
        <li><strong>דוגמאות ליחסים שמספרים סיפור:</strong>
            <ul>
                <li>'הוא סוג של' (Is-a / subClassOf): חתול &rarr; יונק (חתול הוא מקרה פרטי של יונק)</li>
                <li>'יש לו חלק' (Has-a / hasPart): לחתול &rarr; זנב</li>
                <li>'מאפיין אותו' (Has-property): כלב &rarr; נובח</li>
                <li>'הומצא על ידי' (InventedBy): נורה &rarr; אדיסון</li>
                <li>'קרה בשנת' (HappenedInYear): מלחמת העולם השנייה &rarr; 1939</li>
            </ul>
        </li>
        <li><strong>הקסם: איך המבנה הגרפי מייצג ידע ויוצר הבנה?</strong>
            <ul>
                <li><strong>ויזואליזציה אינטואיטיבית:</strong> המבנה הגרפי מציג קשרים מורכבים בצורה קלה להבנה. במקום טקסט ארוך, אנחנו רואים מפה ויזואלית.</li>
                <li><strong>שליפת מידע חכמה:</strong> אפשר לשאול את הגרף שאלות מתוחכמות (כמו: "מהם כל המושגים שקשורים ל'חתול' ביחס 'יכול ל'?", "מי המציא דברים חשמליים ונולד במילאנו?").</li>
                <li><strong>הסקת מסקנות:</strong> הגרף מאפשר 'לקפוץ' מקשר לקשר. אם יודעים ש'חתול הוא סוג של יונק', ו'ליונקים יש פרווה', אפשר להסיק בקלות (גם בלי ידע מוקדם על חתולים) ש'לחתולים יש פרווה'. זה הבסיס למערכות שמסוגלות 'לחשוב' ולהסיק מסקנות.</li>
            </ul>
        </li>
        <li><strong>גרפי ידע שפוגשים ביום-יום:</strong>
            <ul>
                <li><strong>WordNet:</strong> אולי הגרף הסמנטי המפורסם ביותר של השפה האנגלית, שמקשר בין מילים על בסיס משמעותן.</li>
                <li><strong>Knowledge Graph של גוגל:</strong> זה מה שמאפשר לגוגל להציג לכם קופסת מידע מסודרת בצד תוצאות החיפוש כשאתם מחפשים אדם מפורסם, מקום או עצם – הוא מציג את המידע המרכזי והקשרים הרלוונטיים מתוך גרף ידע עצום.</li>
                <li><strong>Wikidata:</strong> מאגר ידע חופשי וענק שמכיל מיליוני ישויות והקשרים ביניהן, ומהווה מקור מרכזי לגרפי ידע.</li>
            </ul>
        </li>
        <li><strong>יישומים מלהיבים של גרפי ידע:</strong>
            <ul>
                <li><strong>שיפור חיפוש והבנת שפה:</strong> מנועי חיפוש ועוזרים קוליים (כמו Siri או Alexa) משתמשים בגרפי ידע כדי להבין את כוונתכם ולספק תשובות ישירות ולא רק קישורים.</li>
                <li><strong>מערכות המלצה:</strong> נטפליקס, אמזון, ספוטיפיי – כולן משתמשות בקשרים בגרפי ידע (אתם צפיתם ב-X, אנשים שצפו ב-X אהבו גם את Y, Y קשור ל-Z) כדי להמליץ לכם על תוכן חדש.</li>
                <li><strong>רפואה וביולוגיה:</strong> מיפוי קשרים בין גנים, מחלות, תרופות – עוזר בגילויים ובפיתוח טיפולים.</li>
                <li><strong>זיהוי הונאות:</strong> מציאת קשרים חשודים ברשתות פיננסיות או חברתיות.</li>
            </ul>
        </li>
        <li><strong>והקשר למוח שלנו?</strong>
            <ul>
                <li>רשתות סמנטיות וגרפי ידע היו בין הניסיונות המוקדמים לחקות איך אנו מארגנים מידע במוחנו באמצעות אסוציאציות וקישורים. למרות שהמוח שלנו מורכב לאין שיעור, הרעיון הבסיסי של ידע כרשת מחוברת, שבה קשרים הם מרכזיים לא פחות מהמושגים עצמם, הוא רעיון שנשאר משמעותי בחקר הקוגניציה האנושית.</li>
            </ul>
        </li>
    </ul>
    <p>אז בפעם הבאה שתחפשו משהו בגוגל או תקבלו המלצה מגניבה, זכרו – ייתכן שמאחורי הקלעים פועל גרף ידע חכם שמחבר את הנקודות בשבילכם!</p>
</div>

<script>
    // Initial data - Can be expanded
    let nodes = [
        { id: 'node1', label: 'חתול', x: 200, y: 200 },
        { id: 'node2', label: 'יונק', x: 400, y: 200 },
        { id: 'node3', label: 'לצוד עכברים', x: 200, y: 300 },
        { id: 'node4', label: 'כלב', x: 550, y: 300 } // Added another node
    ];

    let edges = [
        { from: 'node1', to: 'node2', label: 'הוא סוג של' },
        { from: 'node1', to: 'node3', label: 'יכול ל' },
        { from: 'node4', to: 'node2', label: 'הוא סוג של' } // Added another edge
    ];

    let nodeCounter = nodes.length;
    const svg = document.getElementById('knowledge-graph');
    const nodeSelectFrom = document.getElementById('edgeFromNode');
    const nodeSelectTo = document.getElementById('edgeToNode');
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');
    const addNodeButton = document.getElementById('addNodeButton');
    const addEdgeButton = document.getElementById('addEdgeButton');
    let tooltip = null; // Variable to hold the tooltip element

    // --- Utility Functions ---

    // Function to update node dropdowns
    function updateNodeSelects() {
        nodeSelectFrom.innerHTML = '';
        nodeSelectTo.innerHTML = '';
        if (nodes.length === 0) {
             // Disable edge buttons if no nodes exist
             addEdgeButton.disabled = true;
             const emptyOption = document.createElement('option');
             emptyOption.textContent = "הוסף מושגים קודם...";
             nodeSelectFrom.appendChild(emptyOption);
             nodeSelectTo.appendChild(emptyOption.cloneNode(true));
             return;
        } else {
             addEdgeButton.disabled = false;
        }


        nodes.forEach(node => {
            const optionFrom = document.createElement('option');
            optionFrom.value = node.id;
            optionFrom.textContent = node.label;
            nodeSelectFrom.appendChild(optionFrom);

            const optionTo = document.createElement('option');
            optionTo.value = node.id;
            optionTo.textContent = node.label;
            nodeSelectTo.appendChild(optionTo);
        });

         // Select the first node by default if nodes exist
         if (nodes.length > 0) {
             nodeSelectFrom.selectedIndex = 0;
             // Select a different one if possible, to make adding edges easier
             nodeSelectTo.selectedIndex = nodes.length > 1 ? 1 : 0;
         }
    }

    // Function to draw the graph
    function drawGraph() {
        svg.innerHTML = ''; // Clear SVG

        // Define arrowhead marker
        const marker = document.createElementNS("http://www.w3.org/2000/svg", "marker");
        marker.setAttribute('id', 'arrowhead');
        marker.setAttribute('markerWidth', '10');
        marker.setAttribute('markerHeight', '7');
        marker.setAttribute('refX', '9'); // Position of arrowhead tip relative to its viewBox
        marker.setAttribute('refY', '3.5'); // Center vertically
        marker.setAttribute('orient', 'auto-start-reverse'); // Orient with path, auto
        marker.setAttribute('markerUnits', 'strokeWidth'); // Scale with stroke width
        const polygon = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
        polygon.setAttribute('points', '0 0, 10 3.5, 0 7');
        polygon.setAttribute('fill', '#6c757d'); // Match edge color
        marker.appendChild(polygon);
        svg.appendChild(marker);


        // Draw edges first
        edges.forEach(edge => {
            const fromNode = nodes.find(n => n.id === edge.from);
            const toNode = nodes.find(n => n.id === edge.to);
            if (fromNode && toNode) {
                // Calculate line endpoints adjusted for circle radius
                const dx = toNode.x - fromNode.x;
                const dy = toNode.y - fromNode.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                const radius = 20; // Assuming node radius is 20

                 // Avoid drawing lines between identical nodes
                 if (fromNode.id === toNode.id) return;

                // Adjust endpoints to start/end at circle edge, not center
                 if (distance > radius * 2 + 5) { // Ensure nodes aren't too close for arrowhead
                     const ratioStart = radius / distance;
                     const ratioEnd = (distance - radius - 5) / distance; // 5 buffer before arrowhead

                     const x1 = fromNode.x + dx * ratioStart;
                     const y1 = fromNode.y + dy * ratioStart;
                     const x2 = fromNode.x + dx * ratioEnd;
                     const y2 = fromNode.y + dy * ratioEnd;

                     const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
                     line.setAttribute('x1', x1);
                     line.setAttribute('y1', y1);
                     line.setAttribute('x2', x2);
                     line.setAttribute('y2', y2);
                     line.setAttribute('stroke', '#6c757d'); // Match edge color
                     line.setAttribute('stroke-width', 2);
                     line.setAttribute('marker-end', 'url(#arrowhead)');
                     line.classList.add('edge');
                     svg.appendChild(line);

                     // Add edge label slightly offset from the center
                     const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
                     // Position label slightly above and centered on the line segment
                     const midX = (x1 + x2) / 2;
                     const midY = (y1 + y2) / 2;

                     // Calculate angle to potentially rotate text (optional, but good practice for diagonal lines)
                     // For simplicity here, we'll just offset vertically
                     text.setAttribute('x', midX);
                     text.setAttribute('y', midY - 5); // Position label slightly above line
                     text.setAttribute('text-anchor', 'middle');
                     text.setAttribute('font-size', '10px');
                     text.setAttribute('fill', '#343a40');
                     text.textContent = edge.label;
                     text.classList.add('edge');
                     svg.appendChild(text);
                 } else {
                      // Nodes are too close - draw a simple line without arrowhead
                      const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
                     line.setAttribute('x1', fromNode.x);
                     line.setAttribute('y1', fromNode.y);
                     line.setAttribute('x2', toNode.x);
                     line.setAttribute('y2', toNode.y);
                      line.setAttribute('stroke', '#ced4da'); // Lighter color for crowded connections
                     line.setAttribute('stroke-width', 1);
                     line.classList.add('edge');
                     svg.appendChild(line);

                      // Add edge label anyway
                     const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
                     text.setAttribute('x', (fromNode.x + toNode.x) / 2);
                     text.setAttribute('y', (fromNode.y + toNode.y) / 2 - 5);
                     text.setAttribute('text-anchor', 'middle');
                     text.setAttribute('font-size', '10px');
                     text.setAttribute('fill', '#555');
                     text.textContent = edge.label;
                     text.classList.add('edge');
                     svg.appendChild(text);
                 }
            }
        });


        // Draw nodes
        nodes.forEach(node => {
            const group = document.createElementNS("http://www.w3.org/2000/svg", "g");
            group.classList.add('node');
            // Apply initial transform for animation if it's a new node
             if (node.isNew) {
                group.classList.add('node-new');
                // Reset isNew flag after adding the class
                node.isNew = false;
             }

            group.setAttribute('transform', `translate(${node.x}, ${node.y})`);
            group.setAttribute('data-node-id', node.id); // Add data attribute for identification

            const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            circle.setAttribute('r', 20); // Radius
            // Fill and stroke are defined in CSS for hover effects

            // Add hover effect (tooltip)
            circle.addEventListener('mouseover', (event) => {
                // Position tooltip relative to the mouse position, adjusting for scroll/page offset
                showTooltip(node.label, event.clientX, event.clientY);
            });
             circle.addEventListener('mousemove', (event) => {
                 moveTooltip(event.clientX, event.clientY);
            });
            circle.addEventListener('mouseout', hideTooltip);


            const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
             // Display first few characters if label is long, full label on hover via tooltip
            text.textContent = node.label.length > 6 ? node.label.substring(0, 5) + '...' : node.label; // Allow slightly longer labels
            text.setAttribute('text-anchor', 'middle');
            text.setAttribute('alignment-baseline', 'middle');
            text.setAttribute('fill', 'white');
            text.setAttribute('font-size', '12px');
            text.style.direction = 'rtl'; // Ensure text direction
            text.style.unicodeBidi = 'embed';
            // text.style.fontWeight = 'bold'; // Moved to CSS

            group.appendChild(circle);
            group.appendChild(text);
            svg.appendChild(group);

             // Trigger animation for new nodes after appending to DOM
             if (group.classList.contains('node-new')) {
                 // Use a small timeout to ensure the initial state is applied before transitioning
                 setTimeout(() => {
                     group.classList.remove('node-new'); // Remove class to trigger transition
                 }, 10); // A very small delay is usually enough
             }
        });
    }

    // --- Tooltip Functions ---
    function showTooltip(text, clientX, clientY) {
         if (tooltip) hideTooltip(); // Hide any existing tooltip

        tooltip = document.createElement('div');
        tooltip.classList.add('node-tooltip');
        tooltip.textContent = text;

        // Position relative to the viewport
        tooltip.style.left = `${clientX}px`;
        tooltip.style.top = `${clientY}px`;

        document.body.appendChild(tooltip);
    }

    function moveTooltip(clientX, clientY) {
        if (tooltip) {
             // Update position relative to the viewport
             tooltip.style.left = `${clientX}px`;
             tooltip.style.top = `${clientY}px`;
        }
    }

    function hideTooltip() {
        if (tooltip && tooltip.parentNode) {
            tooltip.parentNode.removeChild(tooltip);
            tooltip = null;
        }
    }


    // --- Interaction Functions ---

    // Function to add a new node
    function addNode() {
        const labelInput = document.getElementById('newNodeLabel');
        const label = labelInput.value.trim();
        if (label) {
             // Check if node with this label already exists (case-insensitive check)
            if (nodes.find(n => n.label.toLowerCase() === label.toLowerCase())) {
                 alert('מושג "' + label + '" כבר קיים בגרף.');
                 return;
            }

            nodeCounter++;
            // Simple positioning logic: try to place new node somewhat near existing nodes or in a grid
            const svgRect = svg.getBoundingClientRect(); // Get current size of SVG
            const svgWidth = svgRect.width || 800; // Use default if not rendered yet
            const svgHeight = svgRect.height || 500;

            // Simple grid-like positioning based on node count
            const nodesPerRow = Math.floor((svgWidth - 100) / 100); // Approx 100px spacing + padding
            const row = Math.floor((nodeCounter - 1) / nodesPerRow);
            const col = (nodeCounter - 1) % nodesPerRow;
            const startX = 60; // Starting position with padding
            const startY = 60;
            const xOffset = Math.max(100, (svgWidth - 120) / (nodesPerRow > 0 ? nodesPerRow : 1)); // Dynamic spacing
            const yOffset = 80;

            let newX = startX + col * xOffset;
            let newY = startY + row * yOffset;

             // Ensure node is within bounds (basic check)
             const padding = 30; // Node radius + margin
             newX = Math.max(padding, Math.min(newX, svgWidth - padding));
             newY = Math.max(padding, Math.min(newY, svgHeight - padding));


            const newNode = {
                id: 'node' + nodeCounter,
                label: label,
                x: newX,
                y: newY,
                isNew: true // Flag for animation
            };

            nodes.push(newNode);
            labelInput.value = '';
            updateNodeSelects();
            drawGraph(); // Redraw graph with new node
             // Optional: Add a temporary visual confirmation near the input
            // (More complex UI element, sticking to current structure)

        } else {
             alert('אנא הכנס שם למושג חדש.');
        }
    }

    // Function to add a new edge
    function addEdge() {
        const fromId = nodeSelectFrom.value;
        const toId = nodeSelectTo.value;
        const labelInput = document.getElementById('edgeLabel');
        const label = labelInput.value.trim();

        if (!fromId || !toId) {
             alert('אנא בחר צמתי התחלה וסיום לחיבור.');
             return;
        }
         if (fromId === toId) {
             alert('לא ניתן לחבר מושג לעצמו.');
             return;
         }
         if (!label) {
             alert('אנא הכנס תווית או תיאור ליחס בין המושגים.');
             return;
         }

         // Prevent adding duplicate edges
         const edgeExists = edges.some(e => e.from === fromId && e.to === toId && e.label === label);
         if (edgeExists) {
            alert('היחס הספציפי הזה כבר קיים בין המושגים שבחרת.');
            return;
         }

        // Add the new edge
        edges.push({ from: fromId, to: toId, label: label });
        labelInput.value = '';
        drawGraph(); // Redraw graph with new edge
         // Optional: Add a temporary visual confirmation
    }

    // Function to toggle explanation visibility
    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר מבט מעמיק על גרפי ידע' : 'הצג מבט מעמיק על גרפי ידע';

         // Optional: Scroll to the explanation if showing it
         if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    }

    // Initial setup
    document.addEventListener('DOMContentLoaded', () => {
        updateNodeSelects();
        drawGraph();
        toggleButton.addEventListener('click', toggleExplanation);
        addNodeButton.addEventListener('click', addNode);
        addEdgeButton.addEventListener('click', addEdge);

        // Allow adding node by pressing Enter in the input field
        document.getElementById('newNodeLabel').addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                event.preventDefault(); // Prevent default form submission
                addNode();
            }
        });
         // Allow adding edge by pressing Enter in the label field
         document.getElementById('edgeLabel').addEventListener('keypress', function(event) {
             if (event.key === 'Enter') {
                 event.preventDefault();
                 addEdge();
             }
         });
    });

    // Handle window resize - Redraw the graph. Node positions are fixed, but this adjusts the SVG size/viewbox potentially.
    // Note: For a truly responsive graph, a force-directed layout library would be needed.
    window.addEventListener('resize', () => {
         // Update SVG dimensions to fit container on resize if needed
         const graphArea = document.getElementById('graph-area');
         if (graphArea) {
             const rect = graphArea.getBoundingClientRect();
             svg.setAttribute('width', rect.width);
             // Keep height fixed or calculate based on content/aspect ratio
             svg.setAttribute('height', 500); // Keeping fixed height as per original
         }
        drawGraph(); // Redraw to potentially adjust arrow positions based on scaled view
    });


</script>
---
```