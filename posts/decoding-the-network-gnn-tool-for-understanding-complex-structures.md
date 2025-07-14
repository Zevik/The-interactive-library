---
title: "לפנח את הרשת: כלי GNN להבנת מבנים מורכבים"
english_slug: decoding-the-network-gnn-tool-for-understanding-complex-structures
category: "טכנולוגיה / מדעי המחשב"
tags: [GNN, רשתות עצביות גרפיות, ניתוח רשתות, למידת מכונה, גרפים]
---
<div id="gnn-app-container" style="display: flex; flex-direction: column; gap: 30px; max-width: 900px; margin: 20px auto; font-family: 'Arial', sans-serif; background-color: #f0f4f8; padding: 20px; border-radius: 12px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <h1 style="text-align: center; color: #2c3e50; margin-top: 0;">מסע אל תוך רשת עצבית גרפית (GNN)</h1>
    <p style="text-align: center; color: #555; font-size: 1.1em;">קליק על צומת כדי לראות איך הוא 'לומד' את סביבתו!</p>

    <div id="graph-area" style="border: 1px solid #dcdcdc; padding: 20px; background-color: #ffffff; border-radius: 8px; box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);">
        <svg id="gnn-graph" width="100%" height="450"></svg>
    </div>

    <div id="info-area" style="display: flex; flex-direction: column; gap: 20px; border: 1px solid #dcdcdc; padding: 20px; background-color: #ffffff; border-radius: 8px; box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);">
        <h2 style="color: #34495e; margin-bottom: 10px;">מה קורה בצומת הנבחר?</h2>
        <div id="node-selection-message" style="text-align: center; color: #e74c3c; font-weight: bold;">
             אנא בחרו צומת בגרף למעלה כדי להתחיל את ההדמיה ולהבין את תהליך ה-GNN.
        </div>

        <div id="simulation-steps" style="display: none; flex-direction: column; gap: 20px;">
            <div id="step-initial" class="sim-step" style="background-color: #ecf0f1; padding: 15px; border-radius: 6px; border-left: 4px solid #3498db;">
                <strong>שלב 1: נקודת ההתחלה - המאפיינים המקוריים</strong><br>
                <span id="initial-attributes" style="display: block; margin-top: 8px; color: #555;"></span>
            </div>

            <div id="step-messages" class="sim-step" style="background-color: #ecf0f1; padding: 15px; border-radius: 6px; border-left: 4px solid #e67e22;">
                <strong>שלב 2: מסע המסרים - השכנים משתפים מידע!</strong><br>
                <span id="message-passing-details" style="display: block; margin-top: 8px; color: #555;"></span>
            </div>

            <div id="step-aggregation" class="sim-step" style="background-color: #ecf0f1; padding: 15px; border-radius: 6px; border-left: 4px solid #2ecc71;">
                <strong>שלב 3: איסוף וסיכום - הצומת אוסף את כל המסרים</strong><br>
                <span id="aggregation-details" style="display: block; margin-top: 8px; color: #555;"></span>
            </div>

            <div id="step-final" class="sim-step" style="background-color: #ecf0f1; padding: 15px; border-radius: 6px; border-left: 4px solid #9b59b6;">
                <strong>הייצוג הסופי - הצומת 'למד' על הסביבה!</strong><br>
                <span id="final-representation" style="display: block; margin-top: 8px; color: #555;"></span>
            </div>
        </div>
         <button id="reset-simulation" style="display: none; padding: 10px 20px; font-size: 1em; cursor: pointer; background-color: #95a5a6; color: white; border: none; border-radius: 5px; margin-top: 10px; align-self: center;">איפוס הדמיה</button>
    </div>
</div>

<style>
    /* General Styling */
    #gnn-app-container {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
    }

    /* SVG Styling */
    .node {
        cursor: pointer;
        stroke: #ffffff;
        stroke-width: 2px;
        transition: r 0.2s ease, fill 0.3s ease, stroke-width 0.3s ease;
        filter: drop-shadow(0 1px 2px rgba(0,0,0,0.2));
    }

    .node:hover {
        r: 22px !important; /* Slightly larger on hover */
        stroke-width: 3px;
    }

    .node-selected {
        stroke: #c0392b; /* Darker red */
        stroke-width: 4px;
        fill: #e74c3c; /* Brighter red */
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
    }

    .node-neighbor {
        stroke: #27ae60; /* Darker green */
        stroke-width: 3px;
        fill: #2ecc71; /* Brighter green */
    }

     .node-initial {
        fill: #3498db; /* Blue */
    }

    .edge {
        stroke: #bdc3c7; /* Light grey */
        stroke-opacity: 0.8;
        stroke-width: 2px;
        transition: stroke-width 0.3s ease, stroke 0.3s ease;
    }

    /* Edge highlighting for selected node's connections */
     .edge-connected {
        stroke: #34495e; /* Darker edge */
        stroke-width: 3px;
     }


    .node-label {
        text-anchor: middle;
        dominant-baseline: central;
        font-family: sans-serif;
        font-size: 12px;
        fill: #34495e; /* Dark text */
        pointer-events: none; /* Prevent label from interfering with node click */
        font-weight: bold;
    }

    .attribute-text {
        text-anchor: middle;
        dominant-baseline: central;
        font-family: monospace;
        font-size: 11px;
        fill: #2c3e50; /* Darker text */
        pointer-events: none;
        font-weight: bold;
    }

    /* Simulation Info Styling */
    .sim-step {
        opacity: 0; /* Start hidden */
        transform: translateY(20px);
        transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    }

    .sim-step.visible {
        opacity: 1;
        transform: translateY(0);
    }

    /* Message Animation Styling */
    @keyframes sendMessage {
        0% { opacity: 1; r: 5; fill: #e67e22; }
        50% { opacity: 1; }
        100% { opacity: 0; transform: translate(0, 0); r: 3; fill: #e67e22;}
    }

    .message-circle {
        r: 5;
        fill: #e67e22; /* Orange */
        opacity: 0;
        pointer-events: none;
    }
    /* Note: SVG animations using SMIL or CSS @keyframes on path are complex within strict style tag.
             Using JS to update position is more feasible here and fits the constraints.
             The @keyframes above is a placeholder if we were doing simple opacity/size, actual movement is via JS. */


    /* Explanation Toggle Button */
    #toggle-explanation {
        display: block;
        margin: 20px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #3498db; /* Blue */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    #toggle-explanation:hover {
        background-color: #2980b9; /* Darker blue */
    }
    #toggle-explanation:active {
        transform: scale(0.98);
    }


    /* Full Explanation Styling */
    #full-explanation {
        display: none;
        max-width: 800px;
        margin: 20px auto;
        line-height: 1.7;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 8px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
        color: #333;
    }

    #full-explanation h2, #full-explanation h3 {
        color: #2c3e50;
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 1px solid #eee;
        padding-bottom: 5px;
    }

     #full-explanation ul, #full-explanation ol {
        margin-bottom: 15px;
     }

     #full-explanation li {
        margin-bottom: 8px;
     }

     #full-explanation code {
        background-color: #eef;
        padding: 2px 5px;
        border-radius: 4px;
        font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
     }
</style>

<button id="toggle-explanation">הצגת/הסתרת הסבר מעמיק על GNNs</button>

<div id="full-explanation">
    # לפנח את הרשת: מסע אל תוך רשתות עצביות גרפיות (GNNs)

    איך בינה מלאכותית מצליחה לפצח את הקשרים הסבוכים שמרכיבים את העולם שלנו - מחברויות בפייסבוק ועד מבנה מולקולות שיכולות לשנות את עתיד הרפואה? הכל מתחיל בהבנה עמוקה של מבנים רשתיים, וכאן נכנסות לתמונה ה-**רשתות העצביות הגרפיות (GNNs)**! הן הגיבורות של ניתוח מבנים מורכבים, והן לומדות לייצג מידע בצורה גאונית שמשקפת לא רק "מי אתה" (המאפיינים שלך), אלא גם "מי לידך ואיך אתה מחובר אליהם" (מבנה הגרף).

    <h2>הסבר מעמיק: חשיפת הקסם שמאחורי GNNs</h2>

    <h3>גרפים סביבנו: עולם של צמתים וקשרים</h3>
    דמיינו את העולם לא כרשימה של דברים, אלא כרשת עצומה של ישויות (צמתים) שמחוברות ביניהן (קשתות). ככה בדיוק עובד גרף! צמתים יכולים להיות אנשים, ערים, מילים, אטומים - כל דבר! קשתות יכולות להיות חברויות, כבישים, קשרי שפה, קשרים כימיים. הגרפים נמצאים בכל מקום:
    <ul>
        <li>**ברשתות חברתיות:** אתם (צומת) וחברים שלכם (עוד צמתים), מחוברים בקשתות של חברות.</li>
        <li>**בעולם הכימיה:** אטומי פחמן, מימן, חמצן (צמתים) מחוברים בקשרים קוולנטיים (קשתות) ויוצרים מולקולות.</li>
        <li>**במפות דרכים:** ערים (צמתים) מחוברות על ידי כבישים ומסילות (קשתות).</li>
        <li>**בעולם האינטרנט:** דפי אינטרנט (צמתים) מקושרים באמצעות לינקים (קשתות).</li>
    </ul>

    <h3>האתגר הגרפי: למה AI רגיל לא מספיק?</h3>
    רשתות עצביות "רגילות" (כמו אלה שמזהות חתולים בתמונות) עובדות מעולה על נתונים מסודרים ומאורגנים כמו תמונות (רשת פיקסלים) או טקסט (סדרת מילים). אבל גרפים? הם כאוטיים ושונים זה מזה לחלוטין! לצומת אחד יש מעט שכנים, לאחר יש המון. אין סדר קבוע. איך נכניס מבנה כזה למודל AI שרגיל לרשתות או סדרות? זה האתגר העיקרי, וה-GNNs נולדו כדי לפתור אותו.

    <h3>הקונספט הגאוני: ייצוגים שלומדים מהשכנים</h3>
    הפילוסופיה של GNN פשוטה ויפה: כדי להבין צומת מסוים, לא מספיק להסתכל רק על המאפיינים שלו. צריך "להקשיב" גם לשכנים שלו - כי הם משפיעים עליו! GNN בונה ייצוג (וקטור מספרים) לכל צומת, והייצוג הזה הוא כמו תמצית מרוכזת של המאפיינים המקוריים של הצומת *ומאפייני השכנים שלו*. איך זה קורה? דרך תהליך קסום שנקרא **'העברת מסרים'**.

    <h3>Message Passing: הלב הפועם של ה-GNN</h3>
    דמיינו את הגרף כרשת חברתית ענקית שבה כולם מדברים עם השכנים הקרובים שלהם. בתהליך ה-Message Passing, בכל "סבב" (שכבה ב-GNN), כל צומת עושה שלושה דברים:

    <ol>
        <li>**יצירת מסר (Message):** כל שכן $u$ של צומת $v$ יוצר "מסר" ($m_{u \to v}$) שמבוסס על ההבנה הנוכחית שלו (הייצוג שלו באותו רגע). אפשר לחשוב על זה כמו "היי, זה מה שאני יודע על עצמי נכון לעכשיו!". ב-GNN אמיתי, זה נעשה עם פונקציה מורכבת שלומדת מנתונים.</li>
        <li>**איסוף וסיכום (Aggregation):** הצומת $v$ מקבל את כל המסרים שנשלחו אליו מכל השכנים שלו. הוא אוסף אותם ומשלב אותם יחד בצורה חכמה (למשל, סוכם אותם, מחשב ממוצע, או לוקח את המקסימום). החוכמה היא שזה עובד בלי קשר לסדר שבו המסרים הגיעו!</li>
        <li>**עדכון (Update):** לבסוף, הצומת $v$ לוקח את המידע המסוכם מהשכנים, ומשלב אותו עם הידע הקודם שלו (הייצוג שלו מלפני השלב הזה). הוא מעדכן את הייצוג הפנימי שלו לגרסה חדשה ועשירה יותר, שמשקפת עכשיו גם את הסביבה המיידית שלו.</li>
    </ol>
    שלב ה-Aggregation (שלב 2) הוא קריטי! הוא חייב להיות פונקציה סימטרית, כזו שלא משנה לה הסדר של השכנים או המסרים (כמו סכום או ממוצע).

    <h3>עומק הרשת: 'לראות' רחוק יותר בגרף</h3>
    מה קורה אם בונים GNN עם כמה שכבות? כל שכבה היא כמו עוד סבב של 'העברת מסרים'. בשכבה הראשונה, צומת לומד מהשכנים במרחק קשת אחת. בשכבה השנייה, הוא מקבל מסרים משכנים שכבר הספיקו לשלב מידע מהשכנים *שלהם*. כלומר, לאחר שתי שכבות, הצומת כבר מקבל מידע משכנים שנמצאים במרחק של עד שתי קשתות ממנו! ככל שהרשת עמוקה יותר, כך הצומת יכול 'לראות' ולהטמיע מידע מסביבה רחבה יותר בגרף.

    <h3>הצלחה מסחררת: איפה GNNs מככבות?</h3>
    GNNs הן לא רק תיאוריה יפה, הן שינו את פני המחקר והפיתוח בתחומים רבים:
    <ul>
        <li>**רשתות חברתיות:** להמליץ לכם על חברים חדשים, לזהות קהילות, או לזהות תוכן זדוני.</li>
        <li>**גילוי תרופות וחקר מולקולות:** לנבא האם מולקולה פוטנציאלית תהיה יעילה כתרופה, או לזהות חלבונים דומים.</li>
        <li>**מערכות המלצה:** להמליץ לכם על סרטים בנטפליקס או מוצרים באמזון על בסיס הרגלי הצפייה/קנייה של אנשים דומים לכם (גרף של משתמשים ופריטים).</li>
        <li>**תחבורה ולוגיסטיקה:** לחזות עומסי תנועה, לתכנן מסלולים אופטימליים.</li>
        <li>**מעבר לתמונות:** לנתח קשרים בין אובייקטים בתמונה (למשל, לזהות ש"אדם" יושב על "כיסא" שנמצא ליד "שולחן").</li>
    </ul>

    <h3>בשורה התחתונה: ללמוד מהקשרים</h3>
    GNNs הן כלי מהפכני שמאפשר למודלים ללמוד לא רק ממאפיינים בודדים אלא גם מהקשרים המורכבים בתוך מבנים רשתיים. תהליך העברת המסרים הייחודי שלהן מאפשר לכל צומת לבנות ייצוג עשיר שמכיל סיכום חכם של כל הסביבה הגרפית הרלוונטית לו. זהו צעד עצום בהתקדמות הבינה המלאכותית לקראת הבנה עמוקה יותר של העולם המחובר שבו אנו חיים.
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const svg = document.getElementById('gnn-graph');
        const nodeSelectionMessage = document.getElementById('node-selection-message');
        const simulationStepsDiv = document.getElementById('simulation-steps');
        const initialAttributesSpan = document.getElementById('initial-attributes');
        const messagePassingDetailsSpan = document.getElementById('message-passing-details');
        const aggregationDetailsSpan = document.getElementById('aggregation-details');
        const finalRepresentationSpan = document.getElementById('final-representation');
        const toggleButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('full-explanation');
        const resetButton = document.getElementById('reset-simulation');

        // Simple Graph Data (Nodes with attributes, Edges) - Positioned for better visibility
        const nodes = [
            { id: 'A', x: 150, y: 100, attribute: 5, initialAttribute: 5 },
            { id: 'B', x: 400, y: 80, attribute: 3, initialAttribute: 3 },
            { id: 'C', x: 650, y: 100, attribute: 7, initialAttribute: 7 },
            { id: 'D', x: 250, y: 250, attribute: 2, initialAttribute: 2 },
            { id: 'E', x: 550, y: 250, attribute: 8, initialAttribute: 8 },
            { id: 'F', x: 300, y: 400, attribute: 4, initialAttribute: 4 },
            { id: 'G', x: 500, y: 400, attribute: 6, initialAttribute: 6 }
        ];

        const edges = [
            { source: 'A', target: 'B' },
            { source: 'A', target: 'D' },
            { source: 'B', target: 'C' },
            { source: 'B', target: 'E' },
            { source: 'C', target: 'E' },
            { source: 'D', target: 'E' },
            { source: 'D', target: 'F' },
            { source: 'E', target: 'G' },
            { source: 'F', target: 'G' }
        ];

        const nodeMap = new Map(nodes.map(node => [node.id, node]));

        // Store SVG elements by node ID
        const svgElements = {}; // { node: { circle, label, attributeText }, edge: { source-target: line } }

        function drawGraph() {
            svg.innerHTML = ''; // Clear previous graph
            svgElements.node = {};
            svgElements.edge = {};

            // Draw Edges first
            edges.forEach(edge => {
                const sourceNode = nodeMap.get(edge.source);
                const targetNode = nodeMap.get(edge.target);
                const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                line.setAttribute('x1', sourceNode.x);
                line.setAttribute('y1', sourceNode.y);
                line.setAttribute('x2', targetNode.x);
                line.setAttribute('y2', targetNode.y);
                line.classList.add('edge');
                line.setAttribute('data-source', edge.source);
                line.setAttribute('data-target', edge.target);
                svgElements.edge[`${edge.source}-${edge.target}`] = line;
                svg.appendChild(line);
            });

            // Draw Nodes second (so they are on top)
            nodes.forEach(node => {
                const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
                circle.setAttribute('cx', node.x);
                circle.setAttribute('cy', node.y);
                circle.setAttribute('r', 20);
                circle.setAttribute('fill', '#3498db'); // Default blue
                circle.setAttribute('data-node-id', node.id);
                circle.classList.add('node', 'node-initial'); // Add initial class

                const textLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                textLabel.setAttribute('x', node.x);
                textLabel.setAttribute('y', node.y - 28);
                textLabel.textContent = `ID: ${node.id}`;
                textLabel.classList.add('node-label');

                const textAttribute = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                textAttribute.setAttribute('x', node.x);
                textAttribute.setAttribute('y', node.y + 5);
                textAttribute.textContent = `${node.attribute}`; // Display attribute
                textAttribute.classList.add('attribute-text');

                svgElements.node[node.id] = { circle, label: textLabel, attributeText: textAttribute };

                svg.appendChild(circle);
                svg.appendChild(textLabel);
                svg.appendChild(textAttribute);

                circle.addEventListener('click', handleNodeClick);
            });
        }

        function getNeighbors(nodeId) {
            const neighbors = new Set();
            edges.forEach(edge => {
                if (edge.source === nodeId) {
                    neighbors.add(edge.target);
                } else if (edge.target === nodeId) {
                    neighbors.add(edge.source);
                }
            });
            return Array.from(neighbors);
        }

        function getEdgesConnectedToNode(nodeId) {
             return edges.filter(edge => edge.source === nodeId || edge.target === nodeId);
        }

        let simulationTimeout = null; // To hold timeout IDs for clearing

        function resetSimulationState() {
            // Clear any ongoing animations or timeouts
            if (simulationTimeout) clearTimeout(simulationTimeout);
             svg.querySelectorAll('.message-circle').forEach(msg => msg.remove()); // Remove message circles

            // Reset node/edge styles
            svg.querySelectorAll('.node').forEach(nodeEl => {
                nodeEl.classList.remove('node-selected', 'node-neighbor');
                 nodeEl.classList.add('node-initial'); // Reset to default fill
                 const nodeId = nodeEl.getAttribute('data-node-id');
                 svgElements.node[nodeId].attributeText.textContent = nodeMap.get(nodeId).initialAttribute; // Reset attribute text
            });
             svg.querySelectorAll('.edge').forEach(edgeEl => {
                 edgeEl.classList.remove('edge-connected');
             });


            // Reset info area
            nodeSelectionMessage.style.display = 'block';
            simulationStepsDiv.style.display = 'none';
            document.querySelectorAll('.sim-step').forEach(step => step.classList.remove('visible'));
            resetButton.style.display = 'none';
        }


        function simulateGNN(selectedNodeId) {
            resetSimulationState(); // Start simulation with a clean slate

            const selectedNode = nodeMap.get(selectedNodeId);
            const neighbors = getNeighbors(selectedNodeId);
            const selectedNodeSvg = svgElements.node[selectedNodeId].circle;

            // Highlight selected node and neighbors immediately
            selectedNodeSvg.classList.remove('node-initial');
            selectedNodeSvg.classList.add('node-selected');
            neighbors.forEach(neighborId => {
                svgElements.node[neighborId].circle.classList.remove('node-initial');
                svgElements.node[neighborId].circle.classList.add('node-neighbor');
            });

            // Highlight relevant edges
            getEdgesConnectedToNode(selectedNodeId).forEach(edge => {
                 const edgeKey = edge.source < edge.target ? `${edge.source}-${edge.target}` : `${edge.target}-${edge.source}`; // Handle undirected
                 const edgeEl = svg.querySelector(`[data-source='${edge.source}'][data-target='${edge.target}'], [data-source='${edge.target}'][data-target='${edge.source}']`); // Find the line element
                 if (edgeEl) edgeEl.classList.add('edge-connected');
            });


            nodeSelectionMessage.style.display = 'none';
            simulationStepsDiv.style.display = 'flex';
             resetButton.style.display = 'block';


            // --- Simulation Steps with Animations ---

            // Step 1: Initial State
            simulationTimeout = setTimeout(() => {
                const initialText = `
                    <span style="color:#3498db; font-weight:bold;">הצומת הנבחר (${selectedNodeId})</span> מתחיל עם המאפיין: <strong style="color:#2c3e50;">${selectedNode.initialAttribute}</strong>.<br>
                    שכניו: ${neighbors.map(id => `<span style="color:#2ecc71; font-weight:bold;">${id}</span> (מאפיין: <strong style="color:#2c3e50;">${nodeMap.get(id).initialAttribute}</strong>)`).join(', ')}.
                `;
                initialAttributesSpan.innerHTML = initialText;
                document.getElementById('step-initial').classList.add('visible');
            }, 500); // Delay for initial highlighting visibility

            // Step 2: Message Passing Animation
            simulationTimeout = setTimeout(() => {
                 messagePassingDetailsSpan.innerHTML = `
                    כל שכן <span style="color:#2ecc71; font-weight:bold;">מעביר את המאפיין שלו</span> לכיוון הצומת הנבחר (${selectedNodeId}):<br>
                    ${neighbors.map(id => `<span style="color:#2ecc71; font-weight:bold;">${id}</span> שולח מסר עם הערך <strong style="color:#2c3e50;">${nodeMap.get(id).initialAttribute}</strong>.`).join('<br>')}
                `;
                document.getElementById('step-messages').classList.add('visible');

                // Animate messages
                neighbors.forEach((neighborId, index) => {
                    const neighborNode = nodeMap.get(neighborId);
                    const msgCircle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
                    msgCircle.setAttribute('cx', neighborNode.x);
                    msgCircle.setAttribute('cy', neighborNode.y);
                    msgCircle.setAttribute('r', 8); // Size of message circle
                    msgCircle.setAttribute('fill', '#e67e22'); // Orange message color
                    msgCircle.classList.add('message-circle');
                    svg.appendChild(msgCircle);

                    // Simple JS animation: Move from neighbor to selected node
                    const start = { x: neighborNode.x, y: neighborNode.y };
                    const end = { x: selectedNode.x, y: selectedNode.y };
                    const duration = 800; // ms
                    const startTime = performance.now();

                    function animateMessage(currentTime) {
                        const elapsed = currentTime - startTime;
                        const progress = Math.min(elapsed / duration, 1);
                        const easedProgress = progress * (2 - progress); // Ease-out effect

                        const currentX = start.x + (end.x - start.x) * easedProgress;
                        const currentY = start.y + (end.y - start.y) * easedProgress;

                        msgCircle.setAttribute('cx', currentX);
                        msgCircle.setAttribute('cy', currentY);
                        msgCircle.style.opacity = 1; // Make visible

                        if (progress < 1) {
                            requestAnimationFrame(animateMessage);
                        } else {
                             // Message reached destination, maybe a small pulse or just remove
                             msgCircle.style.opacity = 0; // Fade out or remove
                             setTimeout(() => msgCircle.remove(), 100); // Remove element after fade
                        }
                    }
                    setTimeout(() => requestAnimationFrame(animateMessage), index * 200); // Stagger message animations
                });

            }, 2000); // Delay after step 1 is visible

            // Step 3: Aggregation & Update Calculation
            simulationTimeout = setTimeout(() => {
                const neighborAttributes = neighbors.map(id => nodeMap.get(id).initialAttribute);
                const aggregatedMessageValue = neighborAttributes.reduce((sum, attr) => sum + attr, 0);
                 const finalValue = aggregatedMessageValue + selectedNode.initialAttribute; // Simplified GCN-like sum

                 aggregationDetailsSpan.innerHTML = `
                    הצומת אוסף את המסרים (<strong style="color:#2c3e50;">${neighborAttributes.join(' + ')}</strong>) ומסכם אותם.<br>
                    סכום המסרים מהשכנים: <strong style="color:#2c3e50;">${aggregatedMessageValue}</strong>.
                    <br>לאחר מכן הוא משלב את הסכום עם המאפיין המקורי שלו (<strong style="color:#2c3e50;">${selectedNode.initialAttribute}</strong>).
                `;
                 document.getElementById('step-aggregation').classList.add('visible');

                 // Optional: Add a visual aggregation cue on the selected node (e.g., pulse)
                 selectedNodeSvg.style.transition = 'transform 0.3s ease-in-out';
                 selectedNodeSvg.style.transform = 'scale(1.1)';
                 setTimeout(() => selectedNodeSvg.style.transform = 'scale(1)', 300);


            }, 4000); // Delay after message passing animation ends

            // Step 4: Final Representation Update (Visual & Text)
            simulationTimeout = setTimeout(() => {
                const neighborAttributes = neighbors.map(id => nodeMap.get(id).initialAttribute);
                const aggregatedMessageValue = neighborAttributes.reduce((sum, attr) => sum + attr, 0);
                const finalValue = aggregatedMessageValue + selectedNode.initialAttribute; // Simplified GCN-like sum

                finalRepresentationSpan.innerHTML = `
                    מאפיין הצומת המעודכן (לאחר 'שכבת' GNN אחת) הוא: <strong style="color:#9b59b6; font-size: 1.2em;">${finalValue}</strong>.
                    <br>הייצוג החדש מכיל מידע גם מהצומת עצמו וגם מהשכנים הישירים שלו!
                `;
                document.getElementById('step-final').classList.add('visible');

                // Visually update the attribute text near the node
                const attributeTextElement = svgElements.node[selectedNodeId].attributeText;
                 attributeTextElement.textContent = finalValue; // Update the text
                 attributeTextElement.style.fill = '#9b59b6'; // Change color
                 attributeTextElement.style.fontWeight = 'bold'; // Make bold
                 attributeTextElement.style.transition = 'fill 0.5s ease-out, font-size 0.5s ease-out';
                 attributeTextElement.style.fontSize = '14px'; // Make slightly larger

                 // Optional: Pulse the node color slightly
                 selectedNodeSvg.style.transition = 'fill 0.5s ease-in-out';
                 selectedNodeSvg.style.fill = '#9b59b6'; // Purple color for final state
                 setTimeout(() => {
                     // Optional: Revert to selected color or keep final
                     selectedNodeSvg.style.transition = 'fill 0.3s ease, stroke 0.3s ease, stroke-width 0.3s ease'; // Reset transition
                     selectedNodeSvg.style.fill = '#e74c3c'; // Back to selected color
                 }, 500);


            }, 6000); // Delay after aggregation step

        }

        // Event handler for node clicks
        function handleNodeClick(event) {
            const clickedCircle = event.target;
            const selectedNodeId = clickedCircle.getAttribute('data-node-id');
            simulateGNN(selectedNodeId);
        }

        // Toggle explanation visibility
        toggleButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleButton.textContent = isHidden ? 'הסתר הסבר מעמיק על GNNs' : 'הצגת/הסתרת הסבר מעמיק על GNNs';
        });

        // Reset button
        resetButton.addEventListener('click', () => {
            resetSimulationState();
            nodeSelectionMessage.style.display = 'block'; // Ensure initial message reappears
             resetButton.style.display = 'none';
        });


        // Initial drawing of the graph
        drawGraph();
    });
</script>
```