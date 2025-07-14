---
title: "רשתות מבוזרות: למה עמידות עולה על מרכזיות?"
english_slug: decentralized-networks-resilience
category: "טכנולוגיה / מדעי המחשב"
tags:
  - רשתות תקשורת
  - מבוזר
  - מרכזי
  - עמידות
  - בלוקצ'יין
---
# רשתות מבוזרות: מלחמת ההישרדות של הרשת

דמיינו עיר ענקית שכל התקשורת שלה - כל שיחת טלפון, כל אימייל, כל פיסת מידע - חייבת לעבור דרך בניין בודד ומרכזי. הוא מגדלור הידע, הצומת הראשי. מה יקרה אם פתאום... הבניין הזה קורס? חושך. ניתוק. כל התקשורת נעצרת.

עכשיו דמיינו עיר אחרת, גדולה לא פחות, שבה אין בניין מרכזי כזה. במקום זאת, לכל בניין חשוב יש קשרים מרובים עם בניינים חשובים אחרים. נוצרים אלפי נתיבי תקשורת אפשריים. אם בניין אחד קורס, האם העיר כולה תשותק? כנראה שלא. המידע פשוט ימצא נתיבים עוקפים, יזרום דרך קשרים אחרים.

בואו נראה את זה קורה! התנסו בעצמכם בסימולציה האינטראקטיבית:

<div class="network-container">
    <div class="network centralized">
        <h2>רשת מרכזית</h2>
        <svg id="centralized-network" width="400" height="300"></svg>
        <p class="status" id="centralized-status"></p>
    </div>
    <div class="network decentralized">
        <h2>רשת מבוזרת</h2>
        <svg id="decentralized-network" width="400" height="300"></svg>
        <p class="status" id="decentralized-status"></p>
    </div>
</div>
<p class="interaction-prompt">לחצו על צמתים (עיגולים) או קשרים (קווים) כדי "להשבית" אותם ולראות את ההשפעה ההרסנית... או ההישרדותית!</p>
<button id="reset-networks">התחילו מחדש (Reset)</button>

<style>
/* כל הסגנונות כאן - ללא קשר ל-HTML או JS */
:root {
    --color-primary: #007bff; /* כחול */
    --color-secondary: #6c757d; /* אפור */
    --color-success: #28a745; /* ירוק */
    --color-danger: #dc3545; /* אדום */
    --color-warning: #ffc107; /* צהוב */
    --color-info: #17a2b8; /* תכלת */
    --color-light: #f8f9fa; /* אפור בהיר */
    --color-dark: #343a40; /* אפור כהה */
    --color-node-active: var(--color-primary);
    --color-node-isolated: var(--color-info); /* למצב מנותק אבל לא מושבת לחלוטין */
    --color-node-disabled: var(--color-secondary);
    --color-link-active: var(--color-dark);
    --color-link-isolated: var(--color-secondary);
    --color-link-disabled: #ccc;
    --transition-speed: 0.3s;
}

body {
    font-family: 'Arial', sans-serif; /* פונט נקי ומודרני */
    line-height: 1.7; /* רווח שורות נוח לקריאה */
    direction: rtl;
    text-align: right;
    background-color: var(--color-light); /* רקע עדין */
    color: var(--color-dark);
    padding: 20px;
}

h1, h2, h3 {
    text-align: center;
    color: var(--color-dark);
    margin-bottom: 20px;
}

h1 {
    color: var(--color-primary);
    margin-top: 0;
}

.network-container {
    display: flex;
    flex-direction: column; /* עמודות במובייל */
    justify-content: space-around;
    margin-bottom: 20px;
    gap: 20px; /* רווח בין הרשתות */
}

@media (min-width: 768px) { /* שני טורים בדסקטופ */
    .network-container {
        flex-direction: row;
    }
}


.network {
    flex: 1; /* גמישות בגודל */
    border: 1px solid #ddd;
    border-radius: 8px; /* פינות מעוגלות */
    padding: 15px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* צל עדין */
    background-color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.network h2 {
    margin-top: 0;
    margin-bottom: 10px;
    color: var(--color-dark);
}

.network svg {
    display: block;
    margin: 0 auto 10px auto; /* רווח אחרי ה-svg */
    background-color: #fff;
    border-radius: 4px; /* פינות מעוגלות ל-svg */
    width: 100%; /* השתמש ברוחב המקסימלי של הקונטיינר */
    height: auto; /* שמור על יחס גובה רוחב */
    max-height: 300px; /* מגבלת גובה */
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.05); /* צל פנימי קטן */
}

.status {
    text-align: center;
    font-weight: bold;
    color: var(--color-dark);
    min-height: 1.2em; /* שומר מקום שלא יקפוץ תוכן */
}

.node {
    fill: var(--color-node-active);
    stroke: var(--color-dark);
    stroke-width: 1.5;
    cursor: pointer;
    transition: fill var(--transition-speed) ease, r var(--transition-speed) ease, opacity var(--transition-speed) ease;
}

.node:hover {
    fill: var(--color-primary); /* או צבע הדגשה אחר */
    r: 18; /* הגדלה קלה בהעכבר */
}

.node.disabled {
    fill: var(--color-node-disabled);
    stroke: var(--color-secondary);
    pointer-events: none; /* ביטול לחיצות */
    opacity: 0.6; /* שקיפות קלה */
}

.node.isolated {
     fill: var(--color-node-isolated);
     stroke: var(--color-secondary);
     opacity: 0.8; /* פחות שקוף מ-disabled */
}


.link {
    stroke: var(--color-link-active);
    stroke-width: 3; /* קו עבה יותר */
    cursor: pointer;
    transition: stroke var(--transition-speed) ease, opacity var(--transition-speed) ease, stroke-width var(--transition-speed) ease;
}

.link:hover {
    stroke: var(--color-primary); /* או צבע הדגשה אחר */
    stroke-width: 4;
}

.link.disabled {
    stroke: var(--color-link-disabled);
    pointer-events: none;
    opacity: 0.4; /* שקיפות משמעותית יותר */
}

.link.isolated {
    stroke: var(--color-link-isolated);
    opacity: 0.6; /* שקיפות קלה */
}


.interaction-prompt {
    text-align: center;
    margin-top: 10px;
    margin-bottom: 20px;
    font-style: italic;
    color: var(--color-dark);
}

button {
    display: block;
    margin: 20px auto;
    padding: 10px 20px;
    font-size: 1em;
    cursor: pointer;
    border: none;
    border-radius: 5px;
    background-color: var(--color-primary);
    color: white;
    transition: background-color 0.2s ease, opacity 0.2s ease;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

button:hover {
    background-color: #0056b3; /* גוון כחול כהה יותר */
}

button:active {
    background-color: #004085; /* גוון עוד יותר כהה בלחיצה */
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);
}

button#toggle-explanation {
    background-color: var(--color-secondary);
    margin-top: 0; /* סמוך יותר ללחצן הריסט */
}
button#toggle-explanation:hover {
    background-color: #545b62;
}
button#toggle-explanation:active {
     background-color: #3e4146;
}


#explanation {
    margin-top: 30px; /* רווח גדול יותר מהכפתורים */
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #f0f8ff; /* רקע תכלכל בהיר */
    display: none; /* Initially hidden */
    text-align: right;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

#explanation h3 {
    text-align: center;
    margin-top: 0;
    margin-bottom: 20px;
    color: var(--color-primary);
}

#explanation p {
    margin-bottom: 15px;
}

#explanation ul {
    margin-bottom: 15px;
    padding-right: 20px; /* הזחה לרשימה */
}

#explanation li {
    margin-bottom: 8px;
}

</style>

<button id="toggle-explanation">רוצים להבין לעומק? הציצו בהסבר</button>

<div id="explanation">
    <h3>מבט אל המנגנון: מרכזיות מול מבוזרות</h3>
    <p><strong>היסודות:</strong> כל רשת - בין אם זו רשת מחשבים, רשת חברתית, או אפילו מערכת כבישים - מורכבת מ"צמתים" (Nodes) המייצגים ישויות (אנשים, שרתים, ערים) ומ"קשרים" (Links) המחברים אותם ומאפשרים זרימת מידע או תנועה.</p>

    <p><strong>שתי תצורות קלאסיות:</strong> הדרך בה מארגנים את הצמתים והקשרים מגדירה את אופי הרשת. שתי הארכיטקטורות הבסיסיות ביותר הן:</p>

    <p><strong>1. רשת מרכזית (Centralized):</strong> נזכרים בדוגמה של הבניין היחיד בעיר? זוהי רשת מרכזית. יש בה צומת אחד, יחיד ומיוחד, דרכו עוברת (או תלויה בו) רוב התקשורת. שאר הצמתים מחוברים לרוב רק לצומת המרכזי, ולא ישירות זה לזה.
    <ul>
        <li><strong>היתרון הגדול:</strong> קלה לניהול, שליטה ובקרה. אם רוצים לעדכן משהו או לפקח, הכול עובר דרך נקודה אחת.</li>
        <li><strong>החסרון הקריטי:</strong> פגיעות קטלנית. הצומת המרכזי הוא "נקודת כשל יחידה" (Single Point of Failure). אם הוא קורס, נפרץ, או יוצא מכלל פעולה - כל הרשת משותקת או נפגעת אנושות. הסימולציה הראתה זאת בבירור: השבתת הצומת המרכזי מנתקת את כל שאר הצמתים זה מזה.</li>
    </ul>
    </p>

    <p><strong>2. רשת מבוזרת (Decentralized):</strong> כאן אין "מלך" יחיד. צמתים רבים מחוברים זה לזה ברשת סבוכה יחסית, ולכל שני צמתים יש לרוב מספר נתיבים אפשריים לתקשורת.
    <ul>
        <li><strong>היתרון הענק: עמידות (Resilience) וחוסן.</strong> כפי שראיתם בסימולציה, השבתה של צומת או קשר בודד (ואפילו מספר קשרים או צמתים) לרוב אינה ממוטטת את הרשת כולה. המידע יכול למצוא דרכים חלופיות להגיע ליעדו. הרשת קשוחה יותר בפני תקלות נקודתיות, התקפות, או צנזורה.</li>
        <li><strong>החסרון:</strong> מורכבות ניהול גבוהה יותר. שינויים או עדכונים דורשים תיאום מורכב יותר בין צמתים רבים.</li>
    </ul>
    </p>

    <p><strong>הסימולציה בפעולה:</strong> צפיתם כיצד הרשת המרכזית מתפרקת במהירות כשהצומת החשוב מושבת. לעומתה, הרשת המבוזרת ממשיכה לתפקד, גם אם בחלקים קטנים יותר, גם לאחר מספר פגיעות. מדד גודל הרכיב המחובר הגדול ביותר מראה כמה מהר הרשת מתפצלת ומאבדת את יכולת התקשורת הכוללת שלה.</p>

    <p><strong>דוגמאות מהחיים:</strong>
    <ul>
        <li><strong>אינטרנט (במקור):</strong> תוכנן להיות מבוזר חלקית כדי לשרוד התקפה גרעינית (מיתוס פופולרי, אבל ההיגיון של עמידות נכון). למרות שיש היום נקודות ריכוזיות, הארכיטקטורה הבסיסית מבוזרת.</li>
        <li><strong>רשתות P2P (עמית לעמית):</strong> רשתות שיתוף קבצים (כמו ביטורנט) שבהן כל מחשב יכול לדבר ישירות עם אחרים, ללא שרת מרכזי לשיתוף הקבצים עצמם.</li>
        <li><strong>בלוקצ'יין (Bitcoin, Ethereum):</strong> אולי הדוגמה הטהורה ביותר לרשת מבוזרת. אין בנק מרכזי או שרת ראשי. כל עותק של ספר החשבונות מפוזר אצל אלפי משתתפים. זה מה שהופך אותן לעמידות בפני צנזורה, תקלות או ניסיונות השתלטות.</li>
    </ul>
    </p>

    <p><strong>לסיכום:</strong> בעוד שרשתות מרכזיות יעילות לשליטה ובקרה, רשתות מבוזרות עדיפות באופן מובהק כאשר עמידות בפני כשלים או התקפות היא הדרישה העיקרית. בעולם מחובר יותר ויותר, הבנת ההבדל הזה קריטית.</p>
</div>

<script>
// כל קוד ה-JavaScript כאן - ללא קשר ל-HTML או CSS

document.addEventListener('DOMContentLoaded', () => {

    // D3.js assumed to be available globally
    if (typeof d3 === 'undefined') {
        console.error("D3.js library is not loaded. Please ensure D3 is included before this script.");
        return;
    }

    const centralizedSvg = d3.select("#centralized-network");
    const decentralizedSvg = d3.select("#decentralized-network");
    const centralizedStatus = document.getElementById('centralized-status');
    const decentralizedStatus = document.getElementById('decentralized-status');
    const svgWidth = 400; // Used for calculating positions, actual size is responsive
    const svgHeight = 300;

    // --- Initial Network Data ---
    // Use more meaningful positions for decentralized
    const initialCentralizedNodesData = [
        { id: 0, x: svgWidth / 2, y: svgHeight / 2 }, // Center node
        { id: 1, x: svgWidth / 2 + 120 * Math.cos(0 * Math.PI/3), y: svgHeight / 2 + 120 * Math.sin(0 * Math.PI/3) },
        { id: 2, x: svgWidth / 2 + 120 * Math.cos(1 * Math.PI/3), y: svgHeight / 2 + 120 * Math.sin(1 * Math.PI/3) },
        { id: 3, x: svgWidth / 2 + 120 * Math.cos(2 * Math.PI/3), y: svgHeight / 2 + 120 * Math.sin(2 * Math.PI/3) },
        { id: 4, x: svgWidth / 2 + 120 * Math.cos(3 * Math.PI/3), y: svgHeight / 2 + 120 * Math.sin(3 * Math.PI/3) },
        { id: 5, x: svgWidth / 2 + 120 * Math.cos(4 * Math.PI/3), y: svgHeight / 2 + 120 * Math.sin(4 * Math.PI/3) },
        { id: 6, x: svgWidth / 2 + 120 * Math.cos(5 * Math.PI/3), y: svgHeight / 2 + 120 * Math.sin(5 * Math.PI/3) }
    ].map(d => ({ ...d, enabled: true })); // Add enabled state

    const initialCentralizedLinksData = [
        { source: 0, target: 1 },
        { source: 0, target: 2 },
        { source: 0, target: 3 },
        { source: 0, target: 4 },
        { source: 0, target: 5 },
        { source: 0, target: 6 }
    ].map((d, i) => ({ ...d, id: `clink-${d.source}-${d.target}-${i}`, enabled: true }));


    const initialDecentralizedNodesData = [
        { id: 0, x: 80, y: 80 },
        { id: 1, x: 320, y: 80 },
        { id: 2, x: 80, y: 220 },
        { id: 3, x: 320, y: 220 },
        { id: 4, x: 200, y: 50 },
        { id: 5, x: 200, y: 250 },
        { id: 6, x: svgWidth/2, y: svgHeight/2 } // A somewhat central node
    ].map(d => ({ ...d, enabled: true }));

     const initialDecentralizedLinksData = [
        { source: 0, target: 1 },
        { source: 0, target: 2 },
        { source: 1, target: 3 },
        { source: 2, target: 3 },
        { source: 4, target: 0 },
        { source: 4, target: 1 },
        { source: 5, target: 2 },
        { source: 5, target: 3 },
        { source: 6, target: 0 }, // Connect center to others
        { source: 6, target: 1 },
        { source: 6, target: 2 },
        { source: 6, target: 3 },
        { source: 4, target: 6 }, // Connect top/bottom to center
        { source: 5, target: 6 }
    ].map((d, i) => ({ ...d, id: `dlink-${d.source}-${d.target}-${i}`, enabled: true }));

    let centralizedNodes = JSON.parse(JSON.stringify(initialCentralizedNodesData));
    let centralizedLinks = JSON.parse(JSON.stringify(initialCentralizedLinksData));
    let decentralizedNodes = JSON.parse(JSON.stringify(initialDecentralizedNodesData));
    let decentralizedLinks = JSON.parse(JSON.stringify(initialDecentralizedLinksData));


    // --- Connectivity Analysis (Find Largest Connected Component) ---
    function findLargestConnectedComponent(nodes, links) {
        const enabledNodes = nodes.filter(n => n.enabled);
        const enabledLinks = links.filter(l => l.enabled);

        if (enabledNodes.length === 0) {
            return { componentNodes: [], size: 0 };
        }

        // Build adjacency list for the *enabled* subgraph
        const adjacencyList = new Map();
        enabledNodes.forEach(node => adjacencyList.set(node.id, []));
        enabledLinks.forEach(link => {
            if (adjacencyList.has(link.source) && adjacencyList.has(link.target)) {
                 adjacencyList.get(link.source).push(link.target);
                 adjacencyList.get(link.target).push(link.source); // Assuming undirected graph
            }
        });

        const visited = new Set();
        let largestComponent = [];

        function traverse(nodeId, currentComponent) {
            visited.add(nodeId);
            currentComponent.push(nodeId);
            const neighbors = adjacencyList.get(nodeId) || [];
            neighbors.forEach(neighborId => {
                if (!visited.has(neighborId)) {
                    traverse(neighborId, currentComponent);
                }
            });
        }

        // Iterate through all enabled nodes to find all components
        enabledNodes.forEach(node => {
            if (!visited.has(node.id)) {
                const currentComponent = [];
                traverse(node.id, currentComponent);
                if (currentComponent.length > largestComponent.length) {
                    largestComponent = currentComponent;
                }
            }
        });

        return { componentNodes: largestComponent, size: largestComponent.length };
    }


    // --- Drawing and Updating Function ---
    function drawNetwork(svgElement, nodesData, linksData, statusElement) {
        // Clear previous drawing
        svgElement.selectAll("*").remove();

        // Data join for links
        const links = svgElement.selectAll(".link")
            .data(linksData, d => d.id); // Use ID for key function

        // Enter + update links
        const linkEnter = links.enter().append("line")
             .attr("id", d => d.id)
            .attr("class", "link")
             .attr("x1", d => nodesData.find(n => n.id === d.source).x)
            .attr("y1", d => nodesData.find(n => n.id === d.source).y)
            .attr("x2", d => nodesData.find(n => n.id === d.target).x)
            .attr("y2", d => nodesData.find(n => n.id === d.target).y);


        links.merge(linkEnter)
             .classed("disabled", d => !d.enabled)
             .classed("isolated", d => d.enabled && !d.inLargestComponent)
             .transition().duration(300) // Add transition
            .attr("x1", d => nodesData.find(n => n.id === d.source).x)
            .attr("y1", d => nodesData.find(n => n.id === d.source).y)
            .attr("x2", d => nodesData.find(n => n.id === d.target).x)
            .attr("y2", d => nodesData.find(n => n.id === d.target).y);


        // Data join for nodes
        const nodes = svgElement.selectAll(".node")
            .data(nodesData, d => d.id); // Use ID for key function

        // Enter + update nodes
        const nodeEnter = nodes.enter().append("circle")
             .attr("id", d => `node-${d.id}`) // Add ID to nodes as well
            .attr("class", "node")
            .attr("cx", d => d.x)
            .attr("cy", d => d.y)
            .attr("r", 15); // Initial radius

        nodes.merge(nodeEnter)
             .classed("disabled", d => !d.enabled)
             .classed("isolated", d => d.enabled && !d.inLargestComponent)
             .transition().duration(300) // Add transition
            .attr("cx", d => d.x)
            .attr("cy", d => d.y)
            .attr("r", d => d.enabled ? 15 : 12); // Slightly smaller when disabled


        // Update status text
        const largestComponent = findLargestConnectedComponent(nodesData, linksData);
         statusElement.textContent = `רכיב מחובר הגדול ביותר: ${largestComponent.size} מתוך ${nodesData.length} צמתים פעילים (${nodesData.filter(n => n.enabled).length})`;

        // Update data with component status
        nodesData.forEach(node => {
            node.inLargestComponent = largestComponent.componentNodes.includes(node.id);
        });
         linksData.forEach(link => {
             const sourceNode = nodesData.find(n => n.id === link.source);
             const targetNode = nodesData.find(n => n.id === link.target);
             link.inLargestComponent = sourceNode && targetNode && sourceNode.enabled && targetNode.enabled && sourceNode.inLargestComponent && targetNode.inLargestComponent; // Simplified: link is 'in component' if both ends are and enabled
         });


        // Re-select elements to apply updated classes based on inLargestComponent
        svgElement.selectAll(".node")
             .classed("isolated", d => d.enabled && !d.inLargestComponent);

         svgElement.selectAll(".link")
            .classed("isolated", d => d.enabled && !d.inLargestComponent);


        return { nodes: svgElement.selectAll(".node"), links: svgElement.selectAll(".link") };
    }

    // --- Update Network State (after click) ---
    function updateNetworkState(svgElement, nodesData, linksData, statusElement) {
         // Find largest component and update data flags
        const largestComponent = findLargestConnectedComponent(nodesData, linksData);
         nodesData.forEach(node => {
             node.inLargestComponent = largestComponent.componentNodes.includes(node.id);
         });

        // Update link component status based on node status
        linksData.forEach(link => {
            const sourceNode = nodesData.find(n => n.id === link.source);
            const targetNode = nodesData.find(n => n.id === link.target);
            // Link is 'in component' if both ends are enabled AND in the largest component
            link.inLargestComponent = sourceNode && targetNode && sourceNode.enabled && targetNode.enabled && sourceNode.inLargestComponent && targetNode.inLargestComponent;
        });


        // Apply updated classes and transitions
        svgElement.selectAll(".node")
            .classed("disabled", d => !d.enabled)
            .classed("isolated", d => d.enabled && !d.inLargestComponent)
            .transition().duration(300)
            .attr("r", d => d.enabled ? 15 : 12)
             .style("fill", d => {
                 if (!d.enabled) return null; // Let CSS handle disabled color
                 return d.inLargestComponent ? 'var(--color-node-active)' : 'var(--color-node-isolated)';
             })
             .style("stroke", d => !d.enabled ? null : 'var(--color-dark)');


        svgElement.selectAll(".link")
             .classed("disabled", d => !d.enabled)
             .classed("isolated", d => d.enabled && !d.inLargestComponent)
            .transition().duration(300)
             .style("stroke", d => {
                 if (!d.enabled) return null; // Let CSS handle disabled color
                  return d.inLargestComponent ? 'var(--color-link-active)' : 'var(--color-link-isolated)';
             });


        // Update status text
         statusElement.textContent = `רכיב מחובר הגדול ביותר: ${largestComponent.size} מתוך ${nodesData.length} צמתים פעילים (${nodesData.filter(n => n.enabled).length})`;

    }


    // --- Setup Click Handlers ---
    function setupClickHandlers(svgElement, nodesData, linksData, statusElement) {
        // Remove any existing handlers to avoid duplicates on redraw/reset
        svgElement.selectAll(".node").on("click", null);
        svgElement.selectAll(".link").on("click", null);

        svgElement.selectAll(".node").on("click", (event, d) => {
            if (d.enabled) {
                d.enabled = false;
                // Disable all links connected to this node
                linksData.forEach(link => {
                    if (link.enabled && (link.source === d.id || link.target === d.id)) {
                        link.enabled = false;
                    }
                });
                updateNetworkState(svgElement, nodesData, linksData, statusElement);
            }
        });

        svgElement.selectAll(".link").on("click", (event, d) => {
            if (d.enabled) {
                d.enabled = false;
                updateNetworkState(svgElement, nodesData, linksData, statusElement);
            }
        });
    }


    // --- Reset Function ---
    function resetNetworks() {
        centralizedNodes = JSON.parse(JSON.stringify(initialCentralizedNodesData));
        centralizedLinks = JSON.parse(JSON.stringify(initialCentralizedLinksData));
        decentralizedNodes = JSON.parse(JSON.stringify(initialDecentralizedNodesData));
        decentralizedLinks = JSON.parse(JSON.stringify(initialDecentralizedLinksData));

        // Redraw and set up handlers
        const centralizedElements = drawNetwork(centralizedSvg, centralizedNodes, centralizedLinks, centralizedStatus);
        setupClickHandlers(centralizedSvg, centralizedNodes, centralizedLinks, centralizedStatus);

        const decentralizedElements = drawNetwork(decentralizedSvg, decentralizedNodes, decentralizedLinks, decentralizedStatus);
        setupClickHandlers(decentralizedSvg, decentralizedNodes, decentralizedLinks, decentralizedStatus);
    }


    // --- Initial Drawing ---
    resetNetworks(); // Draw initially via reset


    // --- Explanation Toggle ---
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');

    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר' : 'רוצים להבין לעומק? הציצו בהסבר';
    });

    // --- Reset Button ---
    const resetButton = document.getElementById('reset-networks');
    resetButton.addEventListener('click', resetNetworks);

});
</script>
```