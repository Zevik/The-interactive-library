---
title: "בונים עץ תחבירי: מסע ויזואלי למבנה המשפט"
english_slug: building-a-syntax-tree-practical-guide
category: "בלשנות"
tags:
  - בלשנות
  - תחביר
  - דקדוק
  - עץ תחבירי
  - מבנה משפט
  - NLP
---
<h1>בונים עץ תחבירי: מסע ויזואלי למבנה המשפט</h1>
<p>איך המוח שלנו (או מחשב) מפענח את הסדר המורכב של מילים למשמעות אחת ברורה? הצטרפו אלינו לבנות עץ תחבירי משלכם, ולגלות איך המילים מתחברות ליצירת מבנה היררכי שמגלה את סודות התחביר!</p>

<div id="app-container">
    <div id="sentence-input">
        <label for="sentence" class="input-label">הזן משפט בעברית ובנה לו עץ:</label>
        <input type="text" id="sentence" value="הילד קרא ספר מעניין" placeholder="הזן משפט כאן...">
        <button id="load-sentence" class="action-button">טען משפט</button>
    </div>

    <div id="word-tokens-container">
        <div id="word-tokens-label">גרור מילים לעץ:</div>
        <div id="word-tokens">
            <!-- Words will be loaded here -->
        </div>
    </div>


    <div id="tree-area">
        <svg id="tree-lines"></svg>
        <!-- Nodes will be built here -->
         <div id="tree-placeholder">גרור מילים מהתיבה למעלה לכאן כדי ליצור צמתים.</div>
    </div>

    <div id="controls">
        <button id="add-node" class="action-button">הוסף צומת חדש</button>
        <button id="link-nodes" class="action-button primary">קשר צמתים (הורה ← בן)</button>
        <button id="unlink-nodes" class="action-button secondary">נתק קשר</button>
        <span id="selected-nodes-info" class="info-text">בחר צמתים לקשירה/ניתוק</span>
    </div>
</div>

<button id="toggle-explanation" class="explanation-button">הצג הסבר על עצים תחביריים</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: עצים תחביריים - המבנה הסודי של השפה</h2>

    <h3>מה זה בכלל עץ תחבירי?</h3>
    <p>דמיינו משפט כמבנה לגו ענק. עץ תחבירי הוא כמו השרטוט של המבנה הזה. הוא מציג באופן ויזואלי את הקשרים ההיררכיים בין המילים והקבוצות שהן יוצרות. כל בלוק (צומת) בעץ מייצג יחידה תחבירית (מילה, צירוף), והקווים (ענפים) מראים מי "מכיל" את מי, ומי כפוף למי.</p>

    <h3>למה זה כל כך חשוב (ולא רק לבלשנים)?</h3>
    <ul>
        <li>**לנו, דוברי השפה:** זה עוזר להבין איך אנחנו בכלל מבינים משפטים מורכבים, ואיך מבנה המשפט משפיע על המשמעות. זה חושף את "השלד" הלשוני.</li>
        <li>**למחשבים:** בעידן ה-AI ועיבוד השפה הטבעית (NLP), עצים תחביריים הם הכלי המרכזי ללמד מחשבים "להבין" משפטים. תרגום מכונה, סיכום טקסט, צ'אטבוטים - כולם מסתמכים על היכולת לנתח את מבנה המשפט. בניית עץ היא השלב הבסיסי ב-Parsing (ניתוח תחבירי אוטומטי).</li>
    </ul>

    <h3>השחקנים הראשיים בעץ:</h3>
    <ul>
        <li>**צמתים (Nodes):** אלו העיגולים או הריבועים בעץ. הם יכולים להיות:
            <ul>
                <li>**צמתי עלים (Leaves):** המילים עצמן בתחתית העץ.</li>
                <li>**צמתים פנימיים (Non-terminal Nodes):** מייצגים קבוצות מילים (צירופים) או את המשפט השלם.</li>
            </ul>
        </li>
        <li>**ענפים (Branches):** הקווים שמחברים בין הצמתים. הם מציינים יחסי הורה-ילד (או ראש-תלוי). הצומת העליון הוא ההורה (מכיל), והתחתון הוא הבן (חלק מההורה או תלוי בו).</li>
        <li>**תוויות (Labels):** הכיתובים על הצמתים (למשל: NP, VP, S). הם מציינים את סוג היחידה התחבירית שהצומת מייצג. צמתי עלים יכולים לקבל תווית של סוג מילה (N, V, Adj).</li>
    </ul>

    <h3>תוויות נפוצות שתפגשו:</h3>
    <p>אלו רק כמה דוגמאות נפוצות, יש עוד רבות בהתאם למודל התחבירי:</p>
    <ul>
        <li>**S (Sentence):** צומת השורש, מייצג את המשפט כולו.</li>
        <li>**NP (Noun Phrase):** צירוף שם עצם (למשל: <em>חתול שחור גדול</em>).</li>
        <li>**VP (Verb Phrase):** צירוף פועלי (למשל: <em>אכל מהר את האוכל</em>).</li>
        <li>**PP (Prepositional Phrase):** צירוף יחס (למשל: <em>בגינה</em>).</li>
        <li>**N (Noun):** שם עצם (למשל: <em>בית</em>).</li>
        <li>**V (Verb):** פועל (למשל: <em>רץ</em>).</li>
        <li>**Adj (Adjective):** שם תואר (למשל: <em>יפה</em>).</li>
        <li>**Adv (Adverb):** תואר הפועל (למשל: <em>מאוד</em>).</li>
        <li>**P (Preposition):** מילת יחס (למשל: <em>על</em>).</li>
    </ul>

    <h3>בניית עץ תחבירי בפעולה: צעד אחר צעד (דוגמה: 'הילד קרא ספר מעניין')</h3>
    <ol>
        <li>**מתחילים ב"עלים":** המילים הן הבסיס. גוררים את המילים 'הילד', 'קרא', 'ספר', 'מעניין' ל"שטח העץ". אלו צמתי העלים.</li>
        <li>**מאגדים ל"צירופים":** מזהים יחידות גדולות יותר שמורכבות ממילים. 'הילד' הוא צירוף שמני (NP). 'ספר מעניין' הוא צירוף שמני נוסף (NP), כשהתואר 'מעניין' הוא חלק ממנו. 'קרא ספר מעניין' הוא צירוף פועלי (VP), שכולל את הפועל 'קרא' ואת המושא 'ספר מעניין'. יוצרים צמתים חדשים (לא עלים) וגוררים את הצמתים הקיימים להיות ילדים שלהם ומקשרים אותם.</li>
        <li>**מגיעים ל"משפט":** הצומת הראשי (S) מכיל את כל המשפט. הוא יקשר, למשל, לצירוף השמני של הנושא ('הילד') ולצירוף הפועלי של הנשוא ומושאיו ('קרא ספר מעניין'). יוצרים צומת S ומקשרים אליו את ה-NP וה-VP הרלוונטיים.</li>
        <li>**מסדרים ומתייגים:** מסדרים את הצמתים בצורה היררכית (שורש למעלה, עלים למטה) ומתייגים כל צומת בסוג היחידה התחבירית שהוא מייצג (S, NP, VP, N, V, Adj וכו'). זה מה שעשיתם בפעולת הגרירה והקשירה!</li>
    </ol>
    <p>המבנה שנוצר מראה בבירור מי הנושא של מי, מי המושא של מי, ואילו מילים מרכיבות יחד צירופים שפועלים כיחידה אחת במשפט.</p>

    <h3>יתרונות השיטה:</h3>
    <ul>
        <li>**בהירות ויזואלית:** קל לראות את המבנה המלא במבט אחד.</li>
        <li>**חשיפת קשרים עמוקים:** מגלה יחסים תחביריים שלא תמיד ברורים מסדר המילים לבדו.</li>
        <li>**ניתוח שיטתי:** מאפשר לפרק משפטים מורכבים לחלקים ניתנים לניהול.</li>
        <li>**בסיס לטכנולוגיה:** אבן יסוד לפיתוח מערכות אוטומטיות להבנת שפה.</li>
    </ul>
     <p>עכשיו, חזרו למעלה והתנסו בבניית עצים למשפטים אחרים! נסו להבין מה תפקידה של כל מילה ואיך היא מתחברת לשאר המשפט.</p>
</div>

<style>
    /* General Styles */
    #app-container {
        font-family: 'Arial', sans-serif;
        direction: rtl; /* Hebrew */
        text-align: right;
        padding: 25px;
        border: 1px solid #d3e0ea; /* Light blueish grey */
        border-radius: 10px;
        margin-bottom: 30px;
        background-color: #eef4f8; /* Very light blue */
        display: flex;
        flex-direction: column;
        align-items: stretch;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    }

    h1 {
        color: #1a237e; /* Dark blue */
        text-align: center;
        margin-bottom: 20px;
        font-size: 2em;
    }

    p {
         text-align: center;
         margin-bottom: 25px;
         color: #455a64; /* Dark greyish blue */
         font-size: 1.1em;
    }

    /* Input and Load Button */
    #sentence-input {
        margin-bottom: 25px;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
    }

    .input-label {
        margin-left: 15px;
        font-size: 1.1em;
        color: #37474f; /* Dark grey */
    }

    #sentence {
        padding: 10px 12px;
        border: 1px solid #b0bec5; /* Light grey */
        border-radius: 5px;
        margin-left: 10px;
        width: 300px;
        font-size: 1em;
        transition: border-color 0.3s ease;
        text-align: right; /* Ensure RTL input is right-aligned */
    }

    #sentence:focus {
        outline: none;
        border-color: #0288d1; /* Light blue */
        box-shadow: 0 0 5px rgba(2, 136, 209, 0.3);
    }

    .action-button {
        padding: 10px 20px;
        background-color: #0288d1; /* Light blue */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        margin: 5px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .action-button:hover {
        background-color: #0277bd; /* Slightly darker light blue */
    }

     .action-button:active {
         transform: scale(0.98);
     }

     .action-button.primary {
         background-color: #388e3c; /* Green for primary action */
     }
     .action-button.primary:hover {
          background-color: #2e7d32; /* Darker green */
     }

      .action-button.secondary {
         background-color: #fbc02d; /* Amber for secondary action */
         color: #212121; /* Dark text for contrast */
     }
     .action-button.secondary:hover {
          background-color: #f9a825; /* Darker amber */
     }


    /* Word Tokens */
     #word-tokens-container {
         margin-bottom: 20px;
         padding: 15px;
         border: 1px dashed #b0bec5; /* Light grey dashed */
         border-radius: 8px;
         background-color: #ffffff; /* White background */
         text-align: center;
     }

     #word-tokens-label {
         font-size: 1em;
         color: #546e7a; /* Blue grey */
         margin-bottom: 10px;
         font-weight: bold;
     }

    #word-tokens {
        min-height: 40px;
        padding: 5px;
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        justify-content: center;
        align-items: center;
    }

    .token {
        padding: 6px 12px;
        background-color: #e0f7fa; /* Light cyan */
        border: 1px solid #00bcd4; /* Cyan */
        border-radius: 20px; /* Pill shape */
        cursor: grab;
        font-size: 0.95em;
        color: #006064; /* Dark cyan */
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .token:active {
        cursor: grabbing;
        transform: scale(1.05);
        box-shadow: 0 2px 6px rgba(0, 188, 212, 0.4);
    }

     /* Tree Area */
    #tree-area {
        position: relative;
        min-height: 400px;
        border: 1px solid #b0bec5; /* Light grey */
        background-color: #ffffff; /* White background */
        overflow: hidden; /* Hide anything outside bounds */
        border-radius: 8px;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05);
    }

     #tree-placeholder {
         position: absolute;
         top: 50%;
         left: 50%;
         transform: translate(-50%, -50%);
         color: #b0bec5;
         font-size: 1.2em;
         pointer-events: none;
         text-align: center;
         width: 80%;
     }

    #tree-lines {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none; /* Allow clicking nodes underneath */
         /* Optional: Add marker for arrows */
         /* Needs SVG <defs> inside, complex with just CSS */
    }

    #tree-lines line {
        stroke: #546e7a; /* Blue grey for lines */
        stroke-width: 2;
        transition: stroke 0.3s ease; /* Can't easily animate line position with CSS */
    }

    .tree-node {
        position: absolute;
        background-color: #e1f5fe; /* Very light blue */
        border: 1px solid #03a9f4; /* Blue */
        border-radius: 5px;
        padding: 8px 15px;
        text-align: center;
        min-width: 60px;
        cursor: grab;
        user-select: none; /* Prevent text selection during drag */
        white-space: nowrap;
        display: flex;
        flex-direction: column;
        align-items: center;
        box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease, background-color 0.2s ease;
    }

    .tree-node:active {
         cursor: grabbing;
         transform: scale(1.05);
         box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
         z-index: 1000; /* Bring to front */
    }

    .node-label {
        font-weight: bold;
        margin-bottom: 4px;
        min-height: 1.2em; /* Reserve space */
        color: #1a237e; /* Dark blue */
        cursor: text;
        display: block; /* Ensure it takes full width */
    }

    .tree-node.is-leaf .node-label {
         font-size: 0.9em;
         font-weight: normal;
         color: #006064; /* Dark cyan */
         margin-bottom: 0;
         min-height: 1em;
    }

    .node-word {
        font-size: 1.1em;
        color: #37474f; /* Dark grey */
        font-weight: bold;
    }

     .tree-node.is-leaf .node-word {
         font-size: 1.1em;
         font-weight: bold;
         color: #37474f; /* Dark grey */
         margin-top: 5px; /* Space between label (POS) and word */
     }


    .selected-node {
        border-color: #ff9800; /* Orange */
        box-shadow: 0 0 10px rgba(255, 152, 0, 0.6);
        background-color: #fff3e0; /* Light orange */
    }

    /* Controls */
    #controls {
        margin-top: 20px;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
    }

    #selected-nodes-info {
        margin-right: 25px;
        font-size: 1em;
        color: #546e7a; /* Blue grey */
        min-width: 150px; /* Reserve space */
        text-align: right;
    }

    /* Explanation Section */
    .explanation-button {
        display: block; /* Make it take full width or center it */
        margin: 20px auto;
        padding: 10px 20px;
        background-color: #66bb6a; /* Green */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

     .explanation-button:hover {
         background-color: #558b2f; /* Darker green */
     }

      .explanation-button:active {
         transform: scale(0.98);
      }


    #explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #c8e6c9; /* Light green */
        border-radius: 8px;
        background-color: #e8f5e9; /* Very light green */
        line-height: 1.7;
        color: #333;
    }

    #explanation h2, #explanation h3 {
        color: #388e3c; /* Green */
        border-bottom: 1px solid #a5d6a7; /* Lighter green */
        padding-bottom: 8px;
        margin-bottom: 15px;
    }

    #explanation h2 {
        font-size: 1.8em;
        text-align: center;
        margin-bottom: 20px;
    }
     #explanation h3 {
        font-size: 1.4em;
        margin-top: 20px;
     }


    #explanation ul, #explanation ol {
        margin-right: 25px;
        margin-bottom: 15px;
        padding-right: 0; /* Reset default padding */
    }

    #explanation li {
        margin-bottom: 10px;
         color: #424242; /* Dark grey */
    }

     #explanation ol li {
          list-style-position: outside;
          padding-right: 5px; /* Add some space after number */
     }

     #explanation ul li {
          list-style-position: outside;
          padding-right: 5px; /* Add some space after bullet */
     }

    #explanation em {
        font-style: normal;
        font-weight: bold;
        color: #1a237e; /* Dark blue */
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        #sentence-input {
            flex-direction: column;
            align-items: center;
        }

        #sentence {
            margin: 10px 0;
            width: 80%;
            max-width: 300px;
        }

        .input-label {
             margin: 0 0 10px 0;
        }

        #controls {
             flex-direction: column;
        }

        #selected-nodes-info {
             margin: 10px 0;
             text-align: center;
             min-width: auto;
        }
         .action-button {
              width: 80%;
              max-width: 250px;
         }
          .explanation-button {
               width: 90%;
          }
    }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const sentenceInput = document.getElementById('sentence');
        const loadButton = document.getElementById('load-sentence');
        const wordTokensDiv = document.getElementById('word-tokens');
        const treeArea = document.getElementById('tree-area');
        let treeLinesSvg = document.getElementById('tree-lines'); // Use let as it might be replaced
        const treePlaceholder = document.getElementById('tree-placeholder');
        const addNodeButton = document.getElementById('add-node');
        const linkNodesButton = document.getElementById('link-nodes');
        const unlinkNodesButton = document.getElementById('unlink-nodes');
        const selectedNodesInfo = document.getElementById('selected-nodes-info');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        let nodes = [];
        let selectedNodes = []; // Stores node IDs
        let nextNodeId = 0;
        let isDraggingNode = false; // Flag to distinguish drag from click

        // Utility to get a unique ID
        function generateId() {
            return 'node-' + (nextNodeId++);
        }

        // Update the display of selected nodes
        function updateSelectedNodesInfo() {
            const infoText = selectedNodes.map(id => {
                const node = nodes.find(n => n.id === id);
                if (node) {
                    // Display label if exists, otherwise word for leaves or 'צומת'
                    return node.label && node.label !== 'NODE' ? node.label : (node.isLeaf ? node.text : 'צומת');
                }
                return '?';
            }).join(' ו- ');

            if (selectedNodes.length === 0) {
                selectedNodesInfo.textContent = 'בחר צמתים לקשירה/ניתוק';
            } else {
                selectedNodesInfo.textContent = `נבחרו ${selectedNodes.length} צמתים: ${infoText}`;
            }
        }

        // Load sentence into draggable tokens
        loadButton.addEventListener('click', () => {
            const sentence = sentenceInput.value.trim();
            if (!sentence) {
                 wordTokensDiv.innerHTML = '';
                 // Clear existing tree even if input is empty
                 treeArea.innerHTML = '<svg id="tree-lines"></svg>';
                 treeLinesSvg = document.getElementById('tree-lines');
                 nodes = [];
                 selectedNodes = [];
                 nextNodeId = 0;
                 updateSelectedNodesInfo();
                 treePlaceholder.style.display = 'block';
                 return;
            }

            wordTokensDiv.innerHTML = '';
            const words = sentence.split(/\s+/);
            words.forEach(word => {
                if (word) {
                    const token = document.createElement('div');
                    token.classList.add('token');
                    token.textContent = word;
                    token.setAttribute('draggable', true);
                    token.dataset.word = word;
                    wordTokensDiv.appendChild(token);

                    token.addEventListener('dragstart', (e) => {
                        e.dataTransfer.setData('text/plain', e.target.dataset.word);
                        e.dataTransfer.effectAllowed = 'move';
                        // Add visual cue for dragging token?
                         e.target.classList.add('dragging'); // Add a class for styling
                    });
                     token.addEventListener('dragend', (e) => {
                          e.target.classList.remove('dragging'); // Remove class
                     });
                }
            });

            // Clear existing tree
            treeArea.innerHTML = '<svg id="tree-lines"></svg>'; // Clear content preserving SVG ID
            treeLinesSvg = document.getElementById('tree-lines'); // Re-get reference
            nodes = [];
            selectedNodes = [];
            nextNodeId = 0; // Reset ID counter
            updateSelectedNodesInfo();
            treePlaceholder.style.display = 'block'; // Show placeholder again
        });

        // Drag over tree area
        treeArea.addEventListener('dragover', (e) => {
            e.preventDefault(); // Allow drop
            e.dataTransfer.dropEffect = 'move';
             // Add visual cue to tree area?
             treeArea.style.borderColor = '#03a9f4'; // Highlight border
             treeArea.style.boxShadow = 'inset 0 0 8px rgba(3, 169, 244, 0.4)';
        });

         treeArea.addEventListener('dragleave', (e) => {
             // Reset visual cue
              treeArea.style.borderColor = ''; // Or original color
              treeArea.style.boxShadow = '';
         });


        // Drop word token onto tree area
        treeArea.addEventListener('drop', (e) => {
            e.preventDefault();
            // Reset visual cue
             treeArea.style.borderColor = '';
             treeArea.style.boxShadow = '';

            const word = e.dataTransfer.getData('text/plain');
            if (!word) return; // Only handle word drops for creating leaf nodes

            const treeAreaRect = treeArea.getBoundingClientRect();
            // Calculate drop position relative to treeArea's scroll position if needed
            const dropX = e.clientX - treeAreaRect.left + treeArea.scrollLeft;
            const dropY = e.clientY - treeAreaRect.top + treeArea.scrollTop;

            createNode({ text: word, isLeaf: true, x: dropX, y: dropY });

            treePlaceholder.style.display = 'none'; // Hide placeholder once nodes exist
        });

        // Create a new node element and add it to the DOM
        function createNodeElement(node) {
            const nodeElement = document.createElement('div');
            nodeElement.classList.add('tree-node');
             if (node.isLeaf) {
                 nodeElement.classList.add('is-leaf');
             }
            nodeElement.dataset.id = node.id;
            nodeElement.style.left = `${node.x}px`;
            nodeElement.style.top = `${node.y}px`;

            const labelSpan = document.createElement('span');
            labelSpan.classList.add('node-label');

            // Content editable only for label, not the word itself
            if (!node.isLeaf) {
                 labelSpan.contentEditable = true;
                 labelSpan.spellcheck = false; // Usually labels are codes like NP, VP
                 labelSpan.textContent = node.label || 'NODE';
                 labelSpan.title = 'לחץ לעריכת התווית'; // Tooltip
                 labelSpan.addEventListener('blur', (e) => {
                     const updatedLabel = e.target.textContent.trim() || (node.isLeaf ? 'WORD' : 'NODE');
                     const nodeData = nodes.find(n => n.id === node.id);
                     if (nodeData) {
                         nodeData.label = updatedLabel;
                          e.target.textContent = updatedLabel; // Ensure display matches saved
                     }
                      updateSelectedNodesInfo(); // Update info display if this was selected
                 });
                  // Prevent Enter key from creating new lines in content editable
                 labelSpan.addEventListener('keydown', (e) => {
                    if (e.key === 'Enter') {
                        e.preventDefault();
                        e.target.blur(); // Trigger blur to save
                    }
                });
            } else {
                // For leaves, label is read-only (e.g., POS tag, maybe add editing later)
                 labelSpan.textContent = node.label || 'WORD'; // Default label for leaf (like a POS tag)
                 labelSpan.contentEditable = false;
            }

            nodeElement.appendChild(labelSpan);

            if (node.isLeaf) {
                const wordSpan = document.createElement('span');
                wordSpan.classList.add('node-word');
                wordSpan.textContent = node.text;
                nodeElement.appendChild(wordSpan);
                 // For leaves, the main text is the word below the label (POS tag)
            }

            // Make node draggable and selectable
            let initialMouseX, initialMouseY;
            let dragStartTime;

            nodeElement.addEventListener('mousedown', (e) => {
                 // Ignore clicks on the label contenteditable area specifically for drag START
                 // Allow selection toggle via clicking the label area though
                 if (e.target.closest('.node-label') === labelSpan && labelSpan.contentEditable === 'true') {
                     // If editing the label, let the label handle clicks internally
                     return;
                 }

                // Prevent default browser drag behavior on the element itself
                e.preventDefault();

                isDraggingNode = false;
                initialMouseX = e.clientX;
                initialMouseY = e.clientY;
                dragStartTime = Date.now();

                const nodeRect = nodeElement.getBoundingClientRect();
                const treeRect = treeArea.getBoundingClientRect();
                const dragOffsetX = e.clientX - nodeRect.left;
                const dragOffsetY = e.clientY - nodeRect.top;

                nodeElement.style.cursor = 'grabbing';
                 nodeElement.style.zIndex = '1000'; // Bring to front

                 const onMouseMove = (moveEvent) => {
                     const currentX = moveEvent.clientX;
                     const currentY = moveEvent.clientY;
                     const movedDistance = Math.sqrt(Math.pow(currentX - initialMouseX, 2) + Math.pow(currentY - initialMouseY, 2));

                     // Consider it a drag if moved more than a few pixels or held for a while
                     if (movedDistance > 5 || (Date.now() - dragStartTime > 200 && movedDistance > 2)) {
                         isDraggingNode = true;
                         const newX = currentX - treeRect.left + treeArea.scrollLeft - dragOffsetX;
                         const newY = currentY - treeRect.top + treeArea.scrollTop - dragOffsetY;

                         // Update node data positions
                         node.x = newX;
                         node.y = newY;

                         // Update element position immediately for smooth drag
                         nodeElement.style.left = `${node.x}px`;
                         nodeElement.style.top = `${node.y}px`;

                         redrawLines();
                     }
                 };

                 const onMouseUp = () => {
                     document.removeEventListener('mousemove', onMouseMove);
                     document.removeEventListener('mouseup', onMouseUp);

                     nodeElement.style.cursor = 'grab';
                     nodeElement.style.zIndex = ''; // Reset z-index

                     // If it wasn't a drag (or was a very small drag), toggle selection
                     if (!isDraggingNode) {
                         toggleNodeSelection(node.id);
                     }
                     isDraggingNode = false; // Reset flag
                 };

                 document.addEventListener('mousemove', onMouseMove);
                 document.addEventListener('mouseup', onMouseUp);
            });


            treeArea.appendChild(nodeElement);
            return nodeElement;
        }

        // Add node data to the internal array and create DOM element
        function createNode(config) {
            const newNode = {
                id: generateId(),
                label: config.label || (config.isLeaf ? 'WORD' : 'NODE'),
                text: config.text || '', // Only for leaves
                isLeaf: config.isLeaf || false,
                parentId: null,
                childIds: [],
                x: config.x || 50,
                y: config.y || 50
            };
            nodes.push(newNode);
            createNodeElement(newNode);
            redrawLines(); // Add this to draw lines if parent already exists (unlikely on creation, but good practice)
             treePlaceholder.style.display = 'none'; // Hide placeholder
            return newNode;
        }

         // Toggle node selection
        function toggleNodeSelection(nodeId) {
             const nodeIndex = selectedNodes.indexOf(nodeId);
             const nodeElement = treeArea.querySelector(`.tree-node[data-id="${nodeId}"]`);

             if (nodeIndex > -1) {
                 // Deselect
                 selectedNodes.splice(nodeIndex, 1);
                 if (nodeElement) nodeElement.classList.remove('selected-node');
             } else {
                 // Select (allow max 2)
                 if (selectedNodes.length < 2) {
                     selectedNodes.push(nodeId);
                     if (nodeElement) nodeElement.classList.add('selected-node');
                 } else {
                     // Replace the oldest selection
                     const oldNodeId = selectedNodes.shift();
                     const oldNodeElement = treeArea.querySelector(`.tree-node[data-id="${oldNodeId}"]`);
                     if (oldNodeElement) oldNodeElement.classList.remove('selected-node');
                     selectedNodes.push(nodeId);
                     if (nodeElement) nodeElement.classList.add('selected-node');
                 }
             }
             updateSelectedNodesInfo();
         }

        // Add new generic node button
        addNodeButton.addEventListener('click', () => {
            // Create node near center or last node
             const treeRect = treeArea.getBoundingClientRect();
             const x = treeArea.scrollLeft + treeRect.width / 2 - 50; // Approximate center, minus half node width
             const y = treeArea.scrollTop + treeRect.height / 2 - 30; // Approximate center, minus half node height
            createNode({ isLeaf: false, x: x, y: y });
        });

        // Link selected nodes (Parent to Child)
        linkNodesButton.addEventListener('click', () => {
            if (selectedNodes.length === 2) {
                const parentId = selectedNodes[0]; // Assume first selected is parent
                const childId = selectedNodes[1]; // Assume second selected is child

                // Prevent linking a node to itself
                if (parentId === childId) {
                     alert('לא ניתן לקשר צומת לעצמו.');
                     return;
                }

                const parentNode = nodes.find(n => n.id === parentId);
                const childNode = nodes.find(n => n.id === childId);

                if (!parentNode || !childNode) return; // Should not happen if IDs are valid

                // Prevent linking if child already has a parent
                if (childNode.parentId !== null) {
                     alert(`הצומת "${childNode.label || childNode.text}" כבר מקושר להורה אחר.`);
                     return;
                }

                // Prevent linking if parent is already a child of the child (would create cycle)
                 let current = parentNode;
                 while(current) {
                     if (current.id === childId) {
                          alert('אין ליצור לולאות בעץ! הצומת הראשון (הורה) הוא כבר צאצא של הצומת השני (בן).');
                          return;
                     }
                     current = nodes.find(n => n.id === current.parentId);
                 }

                // Establish the link
                childNode.parentId = parentId;
                if (!parentNode.childIds.includes(childId)) {
                    parentNode.childIds.push(childId);
                }

                redrawLines();

                // Deselect nodes after linking
                deselectAllNodes();
            } else {
                 alert('בחר בדיוק 2 צמתים לקשירה.\nהצומת הראשון שבחרת יהיה ההורה, והשני יהיה הבן.');
            }
        });

         // Unlink selected nodes
        unlinkNodesButton.addEventListener('click', () => {
             if (selectedNodes.length === 1) {
                 const nodeId = selectedNodes[0];
                 const node = nodes.find(n => n.id === nodeId);
                 if (!node || node.parentId === null) {
                      alert('הצומת הנבחר אינו מקושר להורה.');
                      return;
                 }

                 const parentNode = nodes.find(n => n.id === node.parentId);
                 if (parentNode) {
                     // Remove child from parent's children list
                     parentNode.childIds = parentNode.childIds.filter(id => id !== nodeId);
                 }

                 // Remove parent from child
                 node.parentId = null;

                 redrawLines();
                 deselectAllNodes();

             } else if (selectedNodes.length === 2) {
                  // Try to unlink specific parent-child link
                  const potentialParentId = selectedNodes[0];
                  const potentialChildId = selectedNodes[1];

                  const parentNode = nodes.find(n => n.id === potentialParentId);
                  const childNode = nodes.find(n => n.id === potentialChildId);

                  if (!parentNode || !childNode) {
                       alert('אחד או יותר מהצמתים הנבחרים אינם קיימים.');
                       return;
                  }

                  // Check if potentialParent is the actual parent of potentialChild
                  if (childNode.parentId === parentNode.id) {
                      // This is the parent-child pair - unlink child from parent
                      childNode.parentId = null;
                      parentNode.childIds = parentNode.childIds.filter(id => id !== potentialChildId);
                      redrawLines();
                      deselectAllNodes();
                  } else if (parentNode.parentId === childNode.id) {
                       // The other way around - unlink parent from child (less common for unlink button)
                       parentNode.parentId = null;
                       childNode.childIds = childNode.childIds.filter(id => id !== potentialParentId);
                       redrawLines();
                       deselectAllNodes();
                  }
                   else {
                       alert('הצמתים הנבחרים אינם מקושרים זה לזה ישירות.');
                  }

             } else {
                  alert('בחר צומת אחד (כדי לנתק אותו מההורה שלו) או שני צמתים מקושרים (כדי לנתק את הקשר ביניהם).');
             }
        });


        // Deselect all nodes
        function deselectAllNodes() {
             selectedNodes.forEach(nodeId => {
                 const nodeElement = treeArea.querySelector(`.tree-node[data-id="${nodeId}"]`);
                 if (nodeElement) nodeElement.classList.remove('selected-node');
             });
             selectedNodes = [];
             updateSelectedNodesInfo();
        }

        // Recalculate and redraw all lines based on current node positions and parentId/childIds
        function redrawLines() {
            // Clear existing lines efficiently
            while (treeLinesSvg.firstChild) {
                treeLinesSvg.removeChild(treeLinesSvg.firstChild);
            }

            nodes.forEach(node => {
                if (node.parentId) {
                    const parent = nodes.find(n => n.id === node.parentId);
                    if (parent) {
                        const parentEl = treeArea.querySelector(`.tree-node[data-id="${parent.id}"]`);
                        const childEl = treeArea.querySelector(`.tree-node[data-id="${node.id}"]`);

                        if (parentEl && childEl) {
                            // Use stored node coordinates, adding half width/height to find center points
                            // Adjusting for scroll position if treeArea is scrollable
                             const treeRect = treeArea.getBoundingClientRect(); // Use treeArea for scroll offsets

                            // Parent line starts at the bottom center
                             const parentX = parent.x + parentEl.offsetWidth / 2;
                             const parentY = parent.y + parentEl.offsetHeight;

                            // Child line ends at the top center
                             const childX = node.x + childEl.offsetWidth / 2;
                             const childY = node.y;

                            const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                            line.setAttribute('x1', parentX);
                            line.setAttribute('y1', parentY);
                            line.setAttribute('x2', childX);
                            line.setAttribute('y2', childY);
                             // Optional: Add data attribute for easy identification or removal
                             line.setAttribute('data-parent-id', parent.id);
                             line.setAttribute('data-child-id', node.id);
                            treeLinesSvg.appendChild(line);
                        }
                    }
                }
            });
        }

        // --- Initial setup ---
        // Load the default sentence on page load
        loadButton.click();
         updateSelectedNodesInfo(); // Initialize info display

         // Toggle explanation visibility
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'הצג הסבר על עצים תחביריים';
             // Scroll to explanation if showing
             if (isHidden) {
                  explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
             }
        });

         // Add event listener to tree area to deselect nodes when clicking whitespace
         treeArea.addEventListener('click', (e) => {
             // Check if the click target is the tree area itself, not a node within it
             if (e.target.id === 'tree-area' || e.target.id === 'tree-lines') {
                 deselectAllNodes();
             }
         });

          // Handle window resize to redraw lines (nodes keep positions)
          window.addEventListener('resize', redrawLines);

          // Also redraw lines if tree area is scrolled (though node positions are absolute)
          // If node positions were relative, this would be critical. With absolute positioning
          // relative to the top-left of tree-area, lines drawn with absolute positions
          // also relative to top-left of tree-area should update correctly on scroll
          // without explicit redraw. However, adding it doesn't hurt and covers potential quirks.
          treeArea.addEventListener('scroll', redrawLines);

    });
</script>
---