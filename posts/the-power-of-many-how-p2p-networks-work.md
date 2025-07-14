---
title: "כוחם של רבים: איך רשתות P2P מזינות זו את זו"
english_slug: the-power-of-many-how-p2p-networks-work
category: "מדעי המחשב"
tags:
  - רשתות P2P
  - עמית לעמית
  - רשתות מחשב
  - מערכות מבוזרות
  - שיתוף קבצים
---
# כוחם של רבים: איך רשתות P2P מזינות זו את זו?

האם אי פעם הורדתם קובץ ענק בקלות מפתיעה, או נדהמתם מהיציבות של טכנולוגיית הבלוקצ'יין? מאחורי הקסם הזה עומד עיקרון מהפכני ששובר את מודל השרת-לקוח המוכר: רשת עמית לעמית (Peer-to-Peer). ברשת P2P, אין "בוס" מרכזי. כל משתתף ברשת, או "עמית", הוא גם ספק וגם צרכן של משאבים (קובצי מידע, כוח עיבוד). זה כמו פוטלוק עולמי ענקי, שבו כל אחד מביא משהו לשולחן - והשולחן רק הולך וגדל!

אבל איך רשת מבוזרת לחלוטין מצליחה לשתף מידע בצורה יעילה, מהירה, ואפילו עמידה יותר לרעש ותקלות? בואו נצלול לסימולציה שתראה לכם את הקסם בפעולה.

<div id="p2p-app-container">
    <h2>סימולציית רשת P2P דינמית</h2>
    <div class="controls">
        <button id="add-peer-btn">הוסף עמית להורדה</button>
        <button id="start-download-btn" style="display: none;">התחל הורדת קובץ</button>
        <button id="reset-btn">אפס הכל</button>
    </div>
    <div id="network-area">
        <!-- SVG for network visualization -->
        <svg id="p2p-network-svg" width="800" height="450" viewBox="0 0 800 450" preserveAspectRatio="xMidYMid meet"></svg>
    </div>
    <div id="download-status" style="display: none; margin-top: 20px;">
        <h3>סטטוס הורדה לעמית החדש:</h3>
        <div id="parts-container">
            <!-- File parts visualization -->
        </div>
        <div id="progress-bar-container">
            <div id="progress-bar">0%</div>
        </div>
         <p id="download-message" style="text-align: center; font-weight: bold; min-height: 1.2em;"></p>
    </div>
</div>

<style>
#p2p-app-container {
    font-family: 'Arial', sans-serif;
    border: 1px solid #e0e0e0;
    padding: 25px;
    border-radius: 12px;
    max-width: 850px;
    margin: 30px auto;
    background-color: #f5f7fa;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    direction: rtl; /* Ensure RTL layout */
    text-align: right; /* Align text right */
}

#p2p-app-container h2 {
    text-align: center;
    color: #333;
    margin-bottom: 25px;
}

.controls {
    margin-bottom: 30px;
    text-align: center;
}

.controls button {
    padding: 12px 24px;
    margin: 0 8px;
    cursor: pointer;
    border: none;
    border-radius: 6px;
    background-color: #007bff;
    color: white;
    font-size: 1.1rem;
    transition: background-color 0.3s ease, transform 0.1s ease;
    min-width: 150px; /* Ensure consistent button width */
}

.controls button:hover {
    background-color: #0056b3;
}

.controls button:active {
    transform: scale(0.98);
}

.controls button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
}

#network-area {
    position: relative;
    border: 1px solid #ddd;
    background-color: #ffffff;
    border-radius: 8px;
    overflow: hidden; /* Hide potential overflow from SVG animations */
}

#p2p-network-svg {
    display: block; /* Remove extra space below SVG */
}

.node {
    fill: #a0d9ff; /* Default peer - light blue */
    stroke: #4a90e2; /* Blue border */
    stroke-width: 2;
    cursor: pointer;
    transition: fill 0.3s ease, stroke 0.3s ease, transform 0.3s ease;
}

.node.seed {
    fill: #ffebb2; /* Seed peer - light orange */
    stroke: #f5a623; /* Orange border */
}

.node.downloader {
    fill: #c3e6cb; /* Downloader peer - light green */
    stroke: #5cb85c; /* Green border */
    stroke-width: 3; /* Thicker border for emphasis */
}

.node.active {
    /* Pulse effect for nodes actively involved in a transfer */
    animation: pulse 1s infinite alternate;
}

@keyframes pulse {
    from { transform: scale(1); }
    to { transform: scale(1.05); }
}


.node-label {
    text-anchor: middle;
    dominant-baseline: central;
    font-size: 11px; /* Slightly smaller font */
    fill: #333; /* Darker text */
    user-select: none;
    pointer-events: none; /* Allow clicking through text to the circle */
    font-weight: bold;
}

.link {
    stroke: #999;
    stroke-width: 1.5; /* Slightly thicker links */
     transition: stroke 0.3s ease, stroke-width 0.3s ease;
}

.link.transferring {
    stroke: #ff4d4d; /* Red/orange color for active transfer */
    stroke-width: 3;
    /* Dashed line animation */
    stroke-dasharray: 8, 4;
    animation: dash 1s linear infinite;
}

@keyframes dash {
    from { stroke-dashoffset: 12; }
    to { stroke-dashoffset: 0; }
}


#download-status {
     margin-top: 25px;
     padding-top: 20px;
     border-top: 1px dashed #ccc;
     text-align: center;
}

#download-status h3 {
    color: #333;
    margin-bottom: 15px;
}

#parts-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center; /* Center the parts */
    gap: 4px; /* Smaller gap */
    margin-top: 10px;
    padding: 10px;
    background-color: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    min-height: 40px; /* Give it some base height */
}

.file-part {
    width: 24px; /* Slightly larger squares */
    height: 24px;
    background-color: #eee;
    border: 1px solid #ccc;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 10px;
    color: #555;
    position: relative;
    border-radius: 4px; /* Slightly rounded corners */
    transition: background-color 0.5s ease; /* Smooth color change */
}

.file-part.available {
    background-color: #e6f7ff; /* Lighter blue for available */
}

.file-part.downloading {
    background-color: #ffecb3; /* Yellowish for downloading */
    color: #333;
    font-weight: bold;
    /* Add a small animation? */
    animation: pulse-part 0.8s infinite alternate;
}

@keyframes pulse-part {
    from { transform: scale(1); }
    to { transform: scale(1.1); }
}


.file-part.downloaded {
    background-color: #81c784; /* Muted green for downloaded */
    color: white;
    font-weight: bold;
}

#progress-bar-container {
    width: 80%; /* Make progress bar narrower */
    background-color: #e0e0e0;
    border-radius: 10px;
    margin: 20px auto 10px auto; /* Center and add margin */
    overflow: hidden; /* Ensure bar stays within container */
    height: 25px; /* Taller progress bar */
}

#progress-bar {
    width: 0%;
    height: 100%;
    background-color: #4CAF50;
    text-align: center;
    line-height: 25px; /* Center text vertically */
    color: white;
    font-weight: bold;
    transition: width 0.5s ease; /* Smooth progress bar movement */
}

#download-message {
    color: #555;
    font-size: 1em;
    margin-top: 10px;
    min-height: 1.2em; /* Reserve space to prevent layout shifts */
}

#toggle-explanation-btn {
    display: block;
    margin: 30px auto;
    padding: 10px 20px;
    cursor: pointer;
    border: 1px solid #ccc;
    border-radius: 6px;
    background-color: #f0f0f0;
    color: #333;
    font-size: 1rem;
    transition: background-color 0.3s ease;
}

#toggle-explanation-btn:hover {
    background-color: #e0e0e0;
}


#explanation-section {
    margin-top: 25px;
    padding-top: 20px;
    border-top: 1px dashed #ccc;
    direction: rtl; /* Ensure RTL layout */
    text-align: right; /* Align text right */
}

#explanation-section h2,
#explanation-section h3 {
    color: #333;
    margin-bottom: 15px;
    text-align: right;
}

#explanation-section p,
#explanation-section ul {
    color: #555;
    line-height: 1.6;
    margin-bottom: 15px;
}

#explanation-section ul {
    padding-right: 20px; /* Indent list items */
}

#explanation-section li {
    margin-bottom: 8px;
}

</style>

<button id="toggle-explanation-btn" style="display: block; margin: 20px auto; padding: 10px 20px; cursor: pointer;">מה מסתתר מאחורי הסימולציה? (לחץ להסבר)</button>

<div id="explanation-section" style="display: none;">
    <h2>מהי רשת P2P ולמה היא כל כך מיוחדת?</h2>

    <p>דמיינו שאתם רוצים להוריד קובץ גדול. במודל השרת-לקוח המסורתי, הייתם מתחברים לשרת אחד מרכזי, וכל העומס של העלאת הקובץ לכל המשתמשים נופל עליו. אם יש יותר מדי מורידים, השרת נחנק, וההורדה איטית או נכשלת.</p>

    <h3>רשת P2P: כולם עוזרים לכולם</h3>
    <p>ברשת P2P, המצב שונה לחלוטין. כל עמית (Peer) שמוריד חלק מקובץ, הופך מיד גם ל"מקור" (Seeder) עבור החלק הזה עבור עמיתים אחרים. ככל שיותר אנשים מורידים, כך יש יותר מקורות, והרשת הופכת לחזקה ומהירה יותר! במקום עומס על נקודה אחת, העומס מתפזר על פני כל הרשת. זה עיקרון "כוחם של רבים" במיטבו.</p>

    <p>בסימולציה שלנו, ה"עמית המזרע" (Seed) הוא העמית הראשון שיש לו את הקובץ בשלמותו. שאר העמיתים מתחילים עם חלקים אקראיים או כלום, ועם הזמן כולם מורידים ומעלים זה לזה, עד שלעמית החדש (הירוק) יש את כל החלקים.</p>

    <h3>איך עמיתים מוצאים חלקים?</h3>
    <p>ברשת P2P אמיתית יש מנגנוני חיפוש מורכבים (כמו DHT - Distributed Hash Table) שעוזרים לעמית למצוא מי מחזיק בחלקים שהוא צריך. בסימולציה שלנו, העמית החדש פשוט "שואל" את העמיתים אליהם הוא מחובר אם יש להם חלקים חסרים לו. אם יש להם, מתבצעת הורדה. אם לא, הם יכולים לשאול את החברים שלהם וכן הלאה (בסימולציה שלנו החיפוש פשוט יותר ומגיע מהעמיתים המחוברים ישירות).</p>

    <h3>סוגי רשתות P2P (בקצרה):</h3>
    <ul>
        <li>**מובנות (Structured):** יש סדר מסוים, קל למצוא דברים.</li>
        <li>**לא מובנות (Unstructured):** כאוס יחסית, קשה יותר למצוא, אבל עמיד יותר לשינויים.</li>
        <li>**היברידיות:** משלבות שרת מרכזי (לדברים כמו חיפוש ראשוני) עם העברת מידע P2P.</li>
    </ul>

    <h3>למה P2P מנצחת?</h3>
    <ul>
        <li>**סקלאביליות מטורפת:** ככל שגדלה, היא רק נהיית טובה יותר!</li>
        <li>**עמידות:** אין שרת מרכזי שקל להפיל. המידע מפוזר.</li>
        <li>**עלויות נמוכות:** פחות תלויים בשרתים יקרים להעברת נתונים.</li>
    </ul>

    <h3>איפה פוגשים P2P בחיים?</h3>
    <p>הכי מוכר זה שיתוף קבצים (BitTorrent), אבל גם בלוקצ'יין (כמו בביטקוין ואת'ריום), חלק משירותי שיחות וידאו וקול, ופרויקטים של מחשוב מבוזר מבוססים על העקרונות האלה.</p>
    <p>אז בפעם הבאה שאתם מורידים משהו ברשת P2P, זכרו שאתם חלק מרשת גלובלית שבה כולם עוזרים לכולם, יוצרים יחד משהו חזק ועמיד הרבה יותר מכל שרת בודד!</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const svg = document.getElementById('p2p-network-svg');
    const addPeerBtn = document.getElementById('add-peer-btn');
    const startDownloadBtn = document.getElementById('start-download-btn');
    const resetBtn = document.getElementById('reset-btn');
    const downloadStatusDiv = document.getElementById('download-status');
    const partsContainer = document.getElementById('parts-container');
    const progressBar = document.getElementById('progress-bar');
    const downloadMessage = document.getElementById('download-message');
    const toggleExplanationBtn = document.getElementById('toggle-explanation-btn');
    const explanationSection = document.getElementById('explanation-section');

    const SVG_WIDTH = 800;
    const SVG_HEIGHT = 450; // Increased height slightly
    const NODE_RADIUS = 18; // Slightly larger nodes
    const FILE_SIZE_PARTS = 25; // Split file into 25 parts for finer granularity
    const INITIAL_PEERS = 5; // More initial peers
    const MAX_CONNECTIONS_PER_PEER = 5; // More connections
    const SIMULATION_SPEED = 200; // Interval speed in ms for simulation ticks
    const DOWNLOAD_PART_TIME_MS = 1500; // Simulate 1.5 sec per part download

    let nodes = [];
    let links = [];
    let nodeIdCounter = 0;
    let downloaderNode = null;
    let filePartsState = []; // State for the downloader node [0: missing, 1: downloading, 2: downloaded]
    let activeDownloads = new Map(); // Map: partIndex -> { sourcePeerId, endTime, linkElement }
    let simulationInterval = null;

    // --- Network Simulation Logic ---

    // Helper function to get a random position avoiding overlap slightly
    function getRandomPosition(existingNodes) {
        let x, y, attempts = 0;
        const minDistance = NODE_RADIUS * 3; // Minimum distance between nodes
        do {
            x = Math.random() * (SVG_WIDTH - NODE_RADIUS * 2) + NODE_RADIUS;
            y = Math.random() * (SVG_HEIGHT - NODE_RADIUS * 2) + NODE_RADIUS;
            attempts++;
        } while (attempts < 100 && existingNodes.some(node => {
            const dx = x - node.x;
            const dy = y - node.y;
            return Math.sqrt(dx * dx + dy * dy) < minDistance;
        }));
        return { x, y };
    }


    function createNode(x, y, isSeed = false) {
        const id = `peer-${nodeIdCounter++}`;
        const node = {
            id: id,
            x: x,
            y: y,
            isSeed: isSeed,
            fileParts: [], // Parts this peer has (indices 0 to FILE_SIZE_PARTS-1)
            connections: new Set(), // IDs of connected peers
            displayElement: null, // SVG circle element
            labelElement: null // SVG text element
        };
        nodes.push(node);
        return node;
    }

    function addLink(node1, node2) {
        if (node1.id === node2.id) return false;
        const linkId = `${node1.id}-${node2.id}`;
        const reverseLinkId = `${node2.id}-${node1.id}`;
        // Avoid duplicate links and self-connection
        if (links.some(l => l.id === linkId || l.id === reverseLinkId)) return false;

         // Also prevent connecting if either node has reached max connections
         if (node1.connections.size >= MAX_CONNECTIONS_PER_PEER || node2.connections.size >= MAX_CONNECTIONS_PER_PEER) {
            return false;
         }


        links.push({
            id: linkId,
            source: node1.id,
            target: node2.id
        });
        node1.connections.add(node2.id);
        node2.connections.add(node1.id);
        return true;
    }

     // Helper to add a random connection
    function addRandomConnection(node) {
        const possiblePeers = nodes.filter(n => n.id !== node.id && !node.connections.has(n.id) && n.connections.size < MAX_CONNECTIONS_PER_PEER);
        if (possiblePeers.length > 0) {
            const targetNode = possiblePeers[Math.floor(Math.random() * possiblePeers.length)];
            addLink(node, targetNode);
        }
    }


    function removeLink(node1Id, node2Id) {
         links = links.filter(link => !(
            (link.source === node1Id && link.target === node2Id) ||
            (link.source === node2Id && link.target === node1Id)
        ));
        const node1 = nodes.find(n => n.id === node1Id);
        const node2 = nodes.find(n => n.id === node2Id);
        if (node1) node1.connections.delete(node2Id);
        if (node2) node2.connections.delete(node1Id);
    }

    function removeNode(nodeId) {
         // Stop any active downloads involving this node
         if (activeDownloads.size > 0) {
              activeDownloads.forEach((dl, partIndex) => {
                   if (dl.sourcePeerId === nodeId || (downloaderNode && dl.sourcePeerId === downloaderNode.id)) {
                        // If the node being removed is the source or the downloader itself (which shouldn't happen mid-download)
                         // We need to handle this. For simplicity, if source removed, the download fails for that part.
                         if(dl.sourcePeerId === nodeId && downloaderNode) {
                              // Mark the part as missing again if source disappears
                              if (filePartsState[partIndex] === 1) { // Only if it was actively downloading from this source
                                   filePartsState[partIndex] = 0; // Mark as missing again
                                   console.log(`Download of part ${partIndex + 1} failed: Source peer ${nodeId} removed.`);
                             }
                         }
                         // Clean up animation
                         if(dl.linkElement) {
                             dl.linkElement.classList.remove('transferring');
                             if(dl.linkElement._animationInterval) clearInterval(dl.linkElement._animationInterval);
                             dl.linkElement.style.strokeDashoffset = 0;
                         }
                          activeDownloads.delete(partIndex); // Remove from active downloads
                   }
              });
         }


        nodes = nodes.filter(node => node.id !== nodeId);
        // Remove links connected to this node
        links = links.filter(link => link.source !== nodeId && link.target !== nodeId);
        // Remove connections from other nodes
        nodes.forEach(node => node.connections.delete(nodeId));
        // Clear downloader if removed
        if (downloaderNode && downloaderNode.id === nodeId) {
            downloaderNode = null;
            stopSimulation();
            downloadStatusDiv.style.display = 'none';
            startDownloadBtn.style.display = 'none';
            addPeerBtn.disabled = false; // Allow adding new peer
             downloadMessage.textContent = '';
        }
        updateVisualization();
         updateDownloadStatusDisplay(); // Update parts display if downloader removed mid-download
    }


    function initializeNetwork() {
        nodes = [];
        links = [];
        nodeIdCounter = 0;
        downloaderNode = null;
        filePartsState = [];
        activeDownloads = new Map();
        stopSimulation();


        // Create initial peers
        for (let i = 0; i < INITIAL_PEERS; i++) {
             const pos = getRandomPosition(nodes);
            const peer = createNode(pos.x, pos.y, i === 0); // Make the first node a seed
            // Give initial parts to peers (e.g., distribute parts or give all to seed)
            if (peer.isSeed) {
                peer.fileParts = Array.from({ length: FILE_SIZE_PARTS }, (_, i) => i); // Seed has all parts
            } else {
                 // Give non-seed peers 0 parts initially, they join the network empty-handed
                 peer.fileParts = []; // Start with no parts
            }
        }

        // Add some initial random connections
        if (nodes.length > 1) {
            nodes.forEach(node => {
                // Try to add a few connections
                for(let i = 0; i < MAX_CONNECTIONS_PER_PEER / 2; i++) { // Aim for half max connections initially
                     addRandomConnection(node);
                }
            });

            // Ensure the seed is connected to at least one other peer
             const seedNode = nodes.find(n => n.isSeed);
             if (seedNode && seedNode.connections.size === 0 && nodes.length > 1) {
                  addLink(seedNode, nodes.find(n => !n.isSeed)); // Connect seed to a non-seed if isolated
             }
        }


        updateVisualization();
        downloadStatusDiv.style.display = 'none';
        startDownloadBtn.style.display = 'none';
        addPeerBtn.disabled = false;
        downloadMessage.textContent = '';
    }

    function updateVisualization() {
        // Clear SVG
        svg.innerHTML = '';

        // Draw links
        links.forEach(link => {
            const sourceNode = nodes.find(n => n.id === link.source);
            const targetNode = nodes.find(n => n.id === link.target);
            if (sourceNode && targetNode) {
                const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                line.setAttribute('x1', sourceNode.x);
                line.setAttribute('y1', sourceNode.y);
                line.setAttribute('x2', targetNode.x);
                line.setAttribute('y2', targetNode.y);
                line.classList.add('link');
                line.dataset.sourceId = sourceNode.id;
                line.dataset.targetId = targetNode.id;
                // Check if this link is active in a download
                 const isActiveLink = Array.from(activeDownloads.values()).some(dl =>
                     (dl.sourcePeerId === sourceNode.id && dl.downloaderId === targetNode.id) ||
                     (dl.sourcePeerId === targetNode.id && dl.downloaderId === sourceNode.id) // Assuming downloader is target
                 );

                 if (isActiveLink) {
                     line.classList.add('transferring');
                 }

                svg.appendChild(line);
                 // Store link element reference in activeDownloads if needed for animation cleanup
                Array.from(activeDownloads.entries()).forEach(([partIndex, dl]) => {
                     if ((dl.sourcePeerId === sourceNode.id && dl.downloaderId === targetNode.id) ||
                         (dl.sourcePeerId === targetNode.id && dl.downloaderId === sourceNode.id)) {
                          dl.linkElement = line; // Store reference
                     }
                });
            }
        });

        // Draw nodes
        nodes.forEach(node => {
            const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            circle.setAttribute('cx', node.x);
            circle.setAttribute('cy', node.y);
            circle.setAttribute('r', NODE_RADIUS);
            circle.classList.add('node');
            if (node.isSeed) circle.classList.add('seed');
            if (node === downloaderNode) circle.classList.add('downloader');

             // Check if this node is actively sourcing a part for the downloader
             const isSourcing = Array.from(activeDownloads.values()).some(dl => dl.sourcePeerId === node.id);
             if (isSourcing) {
                 circle.classList.add('active'); // Add pulse animation class
             }


            circle.dataset.nodeId = node.id; // Store ID for event listeners

             // Add mouseover/mouseout for potential future tooltip or highlighting
             // circle.addEventListener('mouseover', (event) => { showNodeInfo(node, event); });
             // circle.addEventListener('mouseout', () => { hideNodeInfo(); });


            node.displayElement = circle; // Store reference
            svg.appendChild(circle);

            // Add label (Node ID/Name)
            const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            text.setAttribute('x', node.x);
            text.setAttribute('y', node.y);
            text.textContent = node.id.replace('peer-', 'עמית ');
            text.classList.add('node-label');
            node.labelElement = text; // Store reference
            svg.appendChild(text);
        });

         // Bring nodes to front (draw nodes after links)
         nodes.forEach(node => {
             if(node.displayElement) svg.appendChild(node.displayElement);
             if(node.labelElement) svg.appendChild(node.labelElement);
         });
    }

    function updateDownloadStatusDisplay() {
        partsContainer.innerHTML = '';
        filePartsState.forEach((state, index) => {
            const partDiv = document.createElement('div');
            partDiv.classList.add('file-part');
            partDiv.textContent = index + 1; // Display part number (1-based)
            if (state === 1) {
                partDiv.classList.add('downloading');
            } else if (state === 2) {
                partDiv.classList.add('downloaded');
            }
            partsContainer.appendChild(partDiv);
        });

        const downloadedCount = filePartsState.filter(state => state === 2).length;
        const progressPercent = (downloadedCount / FILE_SIZE_PARTS) * 100;
        progressBar.style.width = progressPercent + '%';
        progressBar.textContent = Math.round(progressPercent) + '%';

        if (progressPercent === 100 && simulationInterval) {
            stopSimulation();
            downloadMessage.textContent = `הורדה הושלמה בהצלחה! עמית ${downloaderNode.id} מחזיק כעת את כל הקובץ.`;
            if (downloaderNode) {
                // Downloader node now has all parts and can seed
                downloaderNode.fileParts = Array.from({ length: FILE_SIZE_PARTS }, (_, i) => i);
                 // Optionally update node color or status visually if needed
            }
            startDownloadBtn.style.display = 'none'; // Download finished
            addPeerBtn.disabled = false; // Allow adding new peer for a new download
        } else if (progressPercent < 100 && simulationInterval) {
             downloadMessage.textContent = `מוריד חלקים... (${downloadedCount} מתוך ${FILE_SIZE_PARTS})`;
        } else if (downloaderNode && !simulationInterval) {
             if (progressPercent === 0) {
                 downloadMessage.textContent = `עמית ${downloaderNode.id} מוכן להורדה.`;
             } else if (progressPercent < 100) {
                 downloadMessage.textContent = `הורדה מושהית. לחץ "התחל הורדת קובץ" להמשך.`;
             }
        }
    }

    // Find connected peers that have specific parts
    function findConnectedPeersWithParts(downloaderId, partsNeededIndices) {
         const downloader = nodes.find(n => n.id === downloaderId);
         if (!downloader) return new Map();

         const potentialSources = new Map(); // Map: partIndex -> Set of peerIds

         downloader.connections.forEach(connectedPeerId => {
              const connectedPeer = nodes.find(n => n.id === connectedPeerId);
              if (connectedPeer) {
                   partsNeededIndices.forEach(partIndex => {
                        // A peer can source a part if it has it AND is not currently the downloader
                       if (connectedPeer.fileParts.includes(partIndex) && connectedPeer.id !== downloaderId) {
                            if (!potentialSources.has(partIndex)) {
                                potentialSources.set(partIndex, new Set());
                            }
                            potentialSources.get(partIndex).add(connectedPeer.id);
                       }
                   });
              }
         });

         return potentialSources; // Returns a Map: partIndex -> Set of peerIds connected to downloader
    }


    function startSimulation() {
        if (!downloaderNode || simulationInterval) return;

        console.log("Starting download simulation for:", downloaderNode.id);
        startDownloadBtn.disabled = true;
         downloadMessage.textContent = 'מחפש חלקים ומוריד...';


        // Simulation loop
        simulationInterval = setInterval(() => {
            const partsNeeded = filePartsState
                .map((state, index) => state === 0 ? index : -1)
                .filter(index => index !== -1);

            if (partsNeeded.length === 0) {
                // All parts downloaded
                stopSimulation();
                updateDownloadStatusDisplay(); // Final update
                return;
            }

            // Remove finished active downloads
            const now = Date.now();
            Array.from(activeDownloads.entries()).forEach(([partIndex, dl]) => {
                if (now >= dl.endTime) {
                    // Download finished for this part
                    filePartsState[partIndex] = 2; // Mark as downloaded
                    // Add the downloaded part to the downloader's fileParts array so it can become a source
                     if (downloaderNode && !downloaderNode.fileParts.includes(partIndex)) {
                         downloaderNode.fileParts.push(partIndex);
                     }

                    console.log(`Finished downloading part ${partIndex + 1}`);
                    // Clean up animation
                    if(dl.linkElement) {
                        dl.linkElement.classList.remove('transferring');
                        if(dl.linkElement._animationInterval) clearInterval(dl.linkElement._animationInterval);
                        dl.linkElement.style.strokeDashoffset = 0;
                    }
                    // Remove 'active' class from source peer if it's no longer sourcing anything
                    const sourcePeer = nodes.find(n => n.id === dl.sourcePeerId);
                    if (sourcePeer && !Array.from(activeDownloads.values()).some(adl => adl.sourcePeerId === sourcePeer.id)) {
                         sourcePeer.displayElement.classList.remove('active');
                    }


                    activeDownloads.delete(partIndex); // Remove from active downloads
                    updateDownloadStatusDisplay(); // Update UI immediately when a part finishes
                }
            });


            // Find available sources for needed parts from connected peers
            const partsCurrentlyDownloading = Array.from(activeDownloads.keys());
            const partsMissingAndNotDownloading = partsNeeded.filter(p => !partsCurrentlyDownloading.includes(p));

            // Prioritize parts from peers with many connections or the seed? For simplicity, pick from available sources.
            const potentialSources = findConnectedPeersWithParts(downloaderNode.id, partsMissingAndNotDownloading);

            // How many parts to download concurrently?
            const concurrentDownloadsLimit = 4; // e.g., up to 4 at a time

            // Attempt to start new downloads if below limit
             let currentConcurrent = activeDownloads.size;
            partsMissingAndNotDownloading.forEach(partIndex => {
                if (currentConcurrent >= concurrentDownloadsLimit) return; // Max concurrent downloads reached

                const availablePeers = potentialSources.get(partIndex);

                if (availablePeers && availablePeers.size > 0) {
                    // Pick one available peer randomly
                    const sourcePeerId = Array.from(availablePeers)[Math.floor(Math.random() * availablePeers.size)];
                    const sourcePeer = nodes.find(n => n.id === sourcePeerId);

                    if (sourcePeer) {
                        // Simulate starting download from sourcePeer for partIndex
                        filePartsState[partIndex] = 1; // Mark as downloading
                         currentConcurrent++;
                        console.log(`Attempting download of part ${partIndex + 1} from ${sourcePeer.id}`);

                        const startTime = now;
                        const endTime = now + DOWNLOAD_PART_TIME_MS;

                        // Find or create the link element for animation
                        let linkElement = svg.querySelector(`.link[data-source-id="${downloaderNode.id}"][data-target-id="${sourcePeer.id}"]`) ||
                                          svg.querySelector(`.link[data-source-id="${sourcePeer.id}"][data-target-id="${downloaderNode.id}"]`);

                         if (!linkElement) {
                              // If link doesn't exist (shouldn't happen if findConnectedPeersWithParts is correct), add it?
                              // For this sim, links are pre-established. If no link, cannot download from that peer.
                              console.warn(`No direct link between ${downloaderNode.id} and ${sourcePeer.id} to download part ${partIndex + 1}.`);
                              filePartsState[partIndex] = 0; // Revert state if link not found
                               return; // Cannot start download
                         }


                        // Mark as actively downloading
                         activeDownloads.set(partIndex, {
                             sourcePeerId: sourcePeer.id,
                             downloaderId: downloaderNode.id,
                             endTime: endTime,
                             linkElement: linkElement // Store reference to animate
                         });

                         // Add animation class to link and source peer
                         linkElement.classList.add('transferring');
                         sourcePeer.displayElement.classList.add('active'); // Add pulse animation

                        // updateDownloadStatusDisplay(); // Update UI when a part starts (optional, less frequent updates are fine too)
                    }
                }
            });

            updateVisualization(); // Redraw links/nodes including active states
            updateDownloadStatusDisplay(); // Update parts UI

        }, SIMULATION_SPEED); // Simulation tick speed
    }

    function stopSimulation() {
        if (simulationInterval) {
            clearInterval(simulationInterval);
            simulationInterval = null;

            // Reset animations and active states
            svg.querySelectorAll('.link').forEach(linkElement => {
                 linkElement.classList.remove('transferring');
                 if(linkElement._animationInterval) clearInterval(linkElement._animationInterval); // Should not happen with CSS animation
                 linkElement.style.strokeDashoffset = 0; // Ensure dash offset resets
            });
             svg.querySelectorAll('.node').forEach(nodeElement => {
                 nodeElement.classList.remove('active');
             });

             activeDownloads.clear(); // Clear any pending downloads

        }
         startDownloadBtn.disabled = false; // Re-enable button if simulation stopped manually
         downloadMessage.textContent = 'הסימולציה מושהית.';
    }

    function resetSimulation() {
        stopSimulation();
        initializeNetwork();
        downloadMessage.textContent = '';
         console.log("Simulation reset.");
    }

    function addPeerForDownload() {
        if (downloaderNode) {
            alert("יש כבר עמית אחד שמוריד. אפס הכל כדי להוסיף עמית חדש.");
            return;
        }
         if (nodes.length === 0) {
             alert("אנא צור עמיתים ראשוניים לפני הוספת עמית להורדה.");
             return;
         }
        if (nodes.length >= 10) { // Limit total peers for visualization clarity
             alert("הסימולציה תומכת בעד 10 עמיתים לבהירות. אפס הכל והתחל מחדש.");
             return;
        }


         const pos = getRandomPosition(nodes);
        const newNode = createNode(pos.x, pos.y, false); // New node is not a seed initially
        downloaderNode = newNode;

        // Connect the new node to a few random existing peers (up to MAX_CONNECTIONS_PER_PEER)
        const existingNodes = nodes.filter(n => n.id !== newNode.id);
        const numConnectionsToAttempt = Math.min(MAX_CONNECTIONS_PER_PEER, existingNodes.length);
        const shuffledNodes = existingNodes.sort(() => 0.5 - Math.random()); // Shuffle to pick randomly
        let connectionsMade = 0;
        for (let i = 0; i < numConnectionsToAttempt; i++) {
             if (addLink(newNode, shuffledNodes[i])) {
                  connectionsMade++;
             }
        }
         if (connectionsMade === 0 && existingNodes.length > 0) {
              // Ensure at least one connection if possible
               addLink(newNode, existingNodes[0]);
         }


        // Initialize file parts state for the new downloader
        filePartsState = Array(FILE_SIZE_PARTS).fill(0); // 0: missing

        updateVisualization();
        updateDownloadStatusDisplay();
        downloadStatusDiv.style.display = 'block';
        startDownloadBtn.style.display = 'block';
        addPeerBtn.disabled = true; // Cannot add another downloader
        downloadMessage.textContent = `עמית ${downloaderNode.id} הצטרף לרשת ומוכן להורדה.`;

        console.log("Added downloader node:", downloaderNode.id);
    }


    // --- Event Listeners ---
    addPeerBtn.addEventListener('click', addPeerForDownload);
    startDownloadBtn.addEventListener('click', startSimulation);
    resetBtn.addEventListener('click', resetSimulation);

    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationSection.style.display === 'none';
        explanationSection.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר' : 'מה מסתתר מאחורי הסימולציה? (לחץ להסבר)';
    });


    // --- Initial Setup ---
    initializeNetwork();
});
</script>
```