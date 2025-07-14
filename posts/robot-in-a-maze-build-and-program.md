---
title: "רובוט במבוך: מסע מתוכנת"
english_slug: robot-in-a-maze-build-and-program
category: "מדעי המחשב"
tags:
  - רובוטיקה
  - תכנות
  - מבוכים
  - חיישנים
  - אלגוריתמים
---
# רובוט במבוך: מסע מתוכנת

האם אי פעם תהיתם איך רובוטים מנווטים בעולם שלנו? איך הם 'רואים' את דרכם ו'מחליטים' לאן לפנות? הצטרפו אלינו למסע מרתק שבו נגלה איך אוסף פקודות פשוט הופך להתנהגות 'חכמה' שיכולה לפלס דרך במבוך מסתורי. בואו נתכנת רובוט!

<div id="app-container">
    <div id="maze-area">
        <div id="maze-container">
            <!-- Maze grid will be rendered here by JavaScript -->
            <div id="robot">
                <div id="robot-direction"></div>
            </div>
        </div>
    </div>

    <div id="controls-area">
        <div class="code-input-section">
            <textarea id="program-code" rows="12" placeholder="כתוב את קוד הרובוט כאן...

פקודות קסם:
קדימה
שמאלה
ימינה
אם קדימה חסום:
  -- פקודות בתוך ה'אם'
סוף אם
חזור [מספר]:
  -- פקודות בתוך ה'חזור'
סוף חזרה
"></textarea>
            <div class="button-row">
                <button id="run-button" class="control-button"><i class="fas fa-play"></i> הרץ תוכנית</button>
                <button id="reset-button" class="control-button"><i class="fas fa-sync-alt"></i> אפס רובוט</button>
            </div>
        </div>
         <div id="status-area">
            <div id="status-title">יומן פעולות:</div>
            <div id="messages">הרובוט ממתין לפקודות...</div>
        </div>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">הצג מה קורה פה באמת!</button>

<div id="explanation">
    <h2>המשימה של הרובוט</h2>
    <p>המטרה של הרובוט שלנו פשוטה: למצוא את הדרך מנקודת ההתחלה הירוקה (S) לנקודת הסיום האדומה (E) בתוך המבוך, תוך הימנעות מהקירות השחורים (W). הוא עושה זאת אך ורק על ידי ביצוע מדויק של הפקודות שתכתבו לו.</p>

    <h2>פקודות יסוד לרובוט</h2>
    <p>הרובוט שלנו מבין שפה פשוטה. הנה הפקודות שהוא מכיר:</p>
    <ul>
        <li><strong>קדימה:</strong> הרובוט מנסה לזוז צעד אחד בכיוון שאליו הוא פונה כרגע. אם יש קיר, הוא נתקל ולא זז.</li>
        <li><strong>שמאלה:</strong> הרובוט מסתובב 90 מעלות שמאלה.</li>
        <li><strong>ימינה:</strong> הרובוט מסתובב 90 מעלות ימינה.</li>
    </ul>

    <h2>חיישנים וקבלת החלטות (תנאים)</h2>
    <p>כדי שהרובוט יוכל להגיב לסביבה, יש לו "חיישן" פשוט: הוא יודע לזהות אם יש מכשול (קיר או גבול המבוך) ממש לפניו. בעזרת זה, אנו יכולים להשתמש בפקודת <strong>'אם'</strong>:</p>
    <ul>
        <li><strong>אם קדימה חסום:</strong> -- רק אם התנאי הזה מתקיים (יש קיר מקדימה), הרובוט יבצע את כל הפקודות שנמצאות מיד אחרי שורה זו, עד לפקודה <strong>'סוף אם'</strong>. אם אין קיר, הוא ידלג על כל הבלוק הזה וימשיך לפקודה שאחרי 'סוף אם'.</li>
        <li><strong>סוף אם:</strong> מסמן את סופה של קבוצת פקודות בתוך 'אם'.</li>
    </ul>
     <p>שימו לב לנקודתיים בסוף שורת ה'אם' - הן חשובות!</p>


    <h2>לחזור על פעולות (לולאות)</h2>
    <p>הרבה משימות ברובוטיקה דורשות חזרה על פעולות. במקום לכתוב אותה פקודה שוב ושוב, אנו משתמשים בפקודת <strong>'חזור'</strong>:</p>
    <ul>
        <li><strong>חזור [מספר]:</strong> הרובוט יחזור על כל הפקודות שמופיעות מיד אחרי שורה זו, עד לפקודה <strong>'סוף חזרה'</strong>, בדיוק את ה'[מספר]' שציינתם.</li>
         <li><strong>סוף חזרה:</strong> מסמן את סופה של קבוצת פקודות בתוך 'חזור'.</li>
    </ul>
     <p>גם כאן, חשוב לציין מספר אחרי 'חזור' ולסיים ב'סוף חזרה' תואם.</p>

    <h2>בונים אלגוריתם</h2>
    <p>השילוב של פקודות יסוד, תנאים ולולאות מאפשר לנו לבנות <strong>אלגוריתם</strong> - סדרה מדויקת של צעדים שהרובוט מבצע כדי לפתור בעיה (במקרה שלנו, למצוא את היציאה מהמבוך). תכנות הוא בעצם כתיבת אלגוריתמים בשפה שהרובוט מבין.</p>

     <h2>טיפים למתכנת המתחיל</h2>
     <ul>
         <li>תכננו את המסלול שלכם מראש.</li>
         <li>השתמשו ב'חזור' כדי לחסוך בכתיבה.</li>
         <li>השתמשו ב'אם קדימה חסום' כדי לגרום לרובוט להגיב לקירות במקום להתקע בהם.</li>
         <li>קראו את ה"יומן פעולות" כדי להבין איזו פקודה בוצעה ומדוע הרובוט פעל כפי שפעל (או עצר).</li>
         <li>אל תפחדו לטעות! תכנות הוא תהליך של ניסוי וטעייה. תקנו את הקוד והריצו שוב.</li>
     </ul>

    <h2>אתגרים נוספים</h2>
    <p>בעולם האמיתי, רובוטים משתמשים בחיישנים מורכבים יותר (ראייה ממוחשבת, לייזרים, GPS) ומבצעים חישובים מסובכים כדי לנווט. המבוך שלנו הוא מודל פשוט, אבל העקרונות של רצף, תנאים ולולאות הם הבסיס לכל תוכנה רובוטית, החל משואבי אבק אוטונומיים ועד רכבים ללא נהג ורובוטים בחלל.</p>
     <p>עכשיו, חזרו לחלק האינטראקטיבי ונסו לכתוב תוכנית משלכם!</p>
</div>

<style>
    /* General styles */
    #app-container {
        font-family: 'Heebo', sans-serif; /* Using a modern Hebrew-friendly font */
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px; /* More space between sections */
        padding: 30px;
        background-color: #f0f4f8; /* Light background */
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }

    #maze-area {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 15px;
        background-color: #c2d6e0; /* Slightly different background for maze area */
        border-radius: 8px;
        box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    #maze-container {
        position: relative;
        display: grid;
        /* grid-template-columns and rows will be set by JS */
        background-color: #aabcc5; /* Base path color */
        border: 4px solid #5a6a76; /* Stronger border */
        border-radius: 4px;
        overflow: hidden; /* Keep robot within bounds visually */
    }

    .maze-cell {
        width: 40px; /* Cell size */
        height: 40px; /* Cell size */
        box-sizing: border-box; /* Include border in size */
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 0.8em;
        font-weight: bold;
        user-select: none; /* Prevent text selection */
    }

    .wall {
        background-color: #4a5568; /* Darker wall color */
        border: 1px solid #333a47;
        box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
    }

    .path {
        background-color: #e2e8f0; /* Lighter path color */
        border: 1px solid #cbd5e0;
    }

    .start {
        background-color: #9ae6b4; /* Gentle green */
        border: 1px solid #68d391;
        color: #22543d; /* Dark green text */
    }

    .end {
        background-color: #feb2b2; /* Gentle red */
        border: 1px solid #fc8181;
        color: #742a2a; /* Dark red text */
    }

    #robot {
        position: absolute;
        width: 36px; /* Slightly smaller than cell for padding */
        height: 36px; /* Slightly smaller than cell */
        background-color: #3182ce; /* Vibrant blue robot */
        border: 2px solid #2b6cb0;
        border-radius: 8px; /* Rounded corners for robot */
        transition: all 0.4s ease-in-out, background-color 0.1s ease; /* Smooth movement and rotation, quick color change */
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 10; /* Ensure robot is above maze */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

     .robot-sensing {
        background-color: #ecc94b !important; /* Yellow flash for sensing */
     }
    .robot-success {
        background-color: #38a169 !important; /* Green for success */
        border-color: #2f855a !important;
    }
    .robot-failure {
        background-color: #e53e3e !important; /* Red for failure */
        border-color: #c53030 !important;
    }


     #robot-direction {
        width: 0;
        height: 0;
        border-left: 10px solid transparent; /* Larger arrow */
        border-right: 10px solid transparent;
        border-bottom: 20px solid #fff; /* White arrow */
        position: absolute;
        top: -5px; /* Position above center */
        transform-origin: bottom center; /* Rotate around bottom point */
        transition: transform 0.4s ease-in-out; /* Smooth rotation */
    }


    #controls-area {
        display: flex;
        gap: 30px; /* Space between code/buttons and status */
        flex-wrap: wrap;
        justify-content: center;
        width: 100%; /* Take full width */
        max-width: 700px; /* Max width for controls */
    }

    .code-input-section {
        display: flex;
        flex-direction: column;
        gap: 15px;
        flex-grow: 1; /* Allow textarea to grow */
        min-width: 300px; /* Minimum width */
    }


    #program-code {
        width: 100%; /* Full width within parent */
        padding: 15px;
        border: 1px solid #cbd5e0;
        border-radius: 8px;
        font-family: 'Consolas', 'Monaco', 'Andale Mono', 'Ubuntu Mono', monospace;
        font-size: 0.9em;
        resize: vertical;
        min-height: 200px; /* Minimum height */
        background-color: #fff;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .button-row {
        display: flex;
        gap: 10px;
        justify-content: center;
    }

    .control-button {
        padding: 12px 25px; /* More padding */
        font-size: 1em;
        border-radius: 6px;
        transition: background-color 0.2s ease, transform 0.1s ease;
        display: flex;
        align-items: center;
        gap: 5px;
    }

    .control-button:hover {
        background-color: #0056b3;
        transform: translateY(-1px); /* Subtle hover effect */
    }
     .control-button:active {
         transform: translateY(0); /* Press effect */
     }

     .control-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        box-shadow: none;
        transform: none;
     }

    #status-area {
        width: 220px; /* Wider status area */
        border: 1px solid #cbd5e0;
        padding: 15px;
        overflow-y: auto;
        max-height: 250px; /* Keep status area height reasonable */
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        display: flex;
        flex-direction: column;
    }

    #status-title {
        font-weight: bold;
        margin-bottom: 8px;
        color: #2d3748; /* Darker text for title */
    }

     #messages {
        font-size: 0.85em; /* Slightly smaller font for messages */
        line-height: 1.5;
         white-space: pre-wrap; /* Preserve line breaks */
         word-wrap: break-word; /* Break long words */
         color: #4a5568; /* Dark grey message text */
     }

    .toggle-button {
        display: block;
        margin: 20px auto;
        padding: 10px 20px;
        font-size: 1em;
        background-color: #6366f1; /* Purple-ish color */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.2s ease, transform 0.1s ease;
    }
     .toggle-button:hover {
        background-color: #4f46e5;
        transform: translateY(-1px);
     }

    #explanation {
        background-color: #e2e8f0; /* Light background for explanation */
        border: 1px solid #cbd5e0;
        padding: 25px; /* More padding */
        margin-top: 20px;
        border-radius: 8px;
        color: #2d3748; /* Dark text */
        line-height: 1.7;
    }

    #explanation h2 {
        color: #2d3748;
        margin-top: 1.5em; /* More space above headings */
        margin-bottom: 0.8em;
        border-bottom: 1px solid #cbd5e0;
        padding-bottom: 5px;
    }

    #explanation p, #explanation ul {
        margin-bottom: 1.2em;
    }

    #explanation ul {
        padding-left: 25px; /* More indent */
    }
     #explanation ul li {
         margin-bottom: 0.5em;
     }

     /* Add FontAwesome for icons (requires external script or CDN) */
     /* For this example, we'll assume it's loaded elsewhere or omit the <i> tags if not */
</style>

<script>
    // Maze definition: 'W' for Wall, 'P' for Path, 'S' for Start, 'E' for End
    const mazeGrid = [
        ['W', 'W', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'S', 'P', 'P', 'P', 'P', 'W'],
        ['W', 'W', 'W', 'P', 'W', 'P', 'W'],
        ['W', 'P', 'P', 'P', 'W', 'P', 'W'],
        ['W', 'P', 'W', 'P', 'W', 'P', 'W'],
        ['W', 'P', 'W', 'P', 'P', 'P', 'W'],
        ['W', 'P', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'P', 'P', 'P', 'E', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'W', 'W']
    ];

    const gridSize = 40; // px per cell
    const robotSize = 36; // px (slightly smaller than cell)

    let robot = { x: 0, y: 0, dir: 1 }; // dir: 0: Up, 1: Right, 2: Down, 3: Left
    const directions = [
        { dx: 0, dy: -1, angle: 0 },   // Up
        { dx: 1, dy: 0, angle: 90 },  // Right
        { dx: 0, dy: 1, angle: 180 }, // Down
        { dx: -1, dy: 0, angle: 270 } // Left
    ];

    let programLines = [];
    let pc = 0; // Program Counter
    let repeatStack = []; // [{ startIndex, endIndex, count, currentIteration }]
    let ifSkip = false; // Are we currently skipping commands inside an if block?
    let ifEndPc = -1; // The program counter index where the current if block ends

    let simulationRunning = false;
    const simulationSpeed = 400; // ms per step (slightly slower for visibility)

    const mazeContainer = document.getElementById('maze-container');
    const robotElement = document.getElementById('robot');
    const robotDirectionElement = document.getElementById('robot-direction');
    const programCodeTextarea = document.getElementById('program-code');
    const runButton = document.getElementById('run-button');
    const resetButton = document.getElementById('reset-button');
    const messagesDiv = document.getElementById('messages');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    function logStatus(msg, isError = false) {
        const lineNum = pc < programLines.length ? ` (שורה ${pc + 1})` : '';
        const message = `<span style="color: ${isError ? '#e53e3e' : '#4a5568'};">${msg}${lineNum}</span><br>`;
        messagesDiv.innerHTML += message;
        messagesDiv.scrollTop = messagesDiv.scrollHeight; // Auto-scroll
    }

    function clearStatus() {
         messagesDiv.innerHTML = '<span style="color: #4a5568;">הרובוט ממתין לפקודות...</span><br>';
    }

    function findStart() {
        for (let y = 0; y < mazeGrid.length; y++) {
            for (let x = 0; x < mazeGrid[y].length; x++) {
                if (mazeGrid[y][x] === 'S') {
                    return { startX: x, startY: y };
                }
            }
        }
        return { startX: -1, startY: -1 }; // Should not happen in valid maze
    }

    function renderMaze() {
        mazeContainer.innerHTML = ''; // Clear previous maze
        const mazeWidth = mazeGrid[0].length;
        const mazeHeight = mazeGrid.length;

        mazeContainer.style.gridTemplateColumns = `repeat(${mazeWidth}, ${gridSize}px)`;
        mazeContainer.style.gridTemplateRows = `repeat(${mazeHeight}, ${gridSize}px)`;
        mazeContainer.style.width = `${mazeWidth * gridSize}px`;
        mazeContainer.style.height = `${mazeHeight * gridSize}px`;


        for (let y = 0; y < mazeHeight; y++) {
            for (let x = 0; x < mazeWidth; x++) {
                const cell = document.createElement('div');
                cell.classList.add('maze-cell');
                let cellType = 'path';
                let cellText = '';
                if (mazeGrid[y][x] === 'W') {
                    cellType = 'wall';
                } else if (mazeGrid[y][x] === 'S') {
                    cellType = 'start';
                    cellText = 'S';
                } else if (mazeGrid[y][x] === 'E') {
                    cellType = 'end';
                    cellText = 'E';
                }
                cell.classList.add(cellType);
                cell.innerText = cellText;
                cell.dataset.x = x; // Store coordinates for potential future use
                cell.dataset.y = y;
                mazeContainer.appendChild(cell);
            }
        }
         mazeContainer.appendChild(robotElement); // Add robot back to the container
    }

    function updateRobotPosition() {
        const cellCenterX = robot.x * gridSize + gridSize / 2;
        const cellCenterY = robot.y * gridSize + gridSize / 2;
        robotElement.style.left = `${cellCenterX}px`;
        robotElement.style.top = `${cellCenterY}px`;
        robotElement.style.transform = `translate(-50%, -50%)`; // Ensure it's centered on the cell
        robotDirectionElement.style.transform = `translateY(-50%) rotate(${directions[robot.dir].angle}deg)`;
    }

    function resetRobot() {
        const startPos = findStart();
        robot.x = startPos.startX;
        robot.y = startPos.startY;
        robot.dir = 1; // Start facing Right
        updateRobotPosition();
        pc = 0;
        repeatStack = [];
        ifSkip = false;
        ifEndPc = -1;
        simulationRunning = false;
        runButton.disabled = false;
        resetButton.disabled = false;
        clearStatus();
        // Remove any previous success/failure states
        robotElement.classList.remove('robot-success', 'robot-failure');
        logStatus('הרובוט אופס לנקודת ההתחלה הירוקה.');
    }

    function isValidMove(x, y) {
        if (y < 0 || y >= mazeGrid.length || x < 0 || x >= mazeGrid[y].length) {
            return false; // Out of bounds
        }
        return mazeGrid[y][x] !== 'W'; // Not a wall
    }

    function isFrontBlocked() {
        const nextX = robot.x + directions[robot.dir].dx;
        const nextY = robot.y + directions[robot.dir].dy;
        return !isValidMove(nextX, nextY);
    }

    function findMatchingEnd(startIndex, startKeyword, endKeyword) {
        let depth = 0;
        for (let i = startIndex + 1; i < programLines.length; i++) {
            const line = programLines[i].trim();
            if (line.startsWith(startKeyword)) {
                depth++;
            } else if (line.startsWith(endKeyword)) {
                if (depth === 0) {
                    return i;
                }
                depth--;
            }
        }
        return -1; // Error: No matching end found
    }

    function parseProgram() {
        const code = programCodeTextarea.value;
        // Split lines, trim whitespace, and remove empty lines
        programLines = code.split('\n').map(line => line.trim()).filter(line => line !== '' && !line.startsWith('--')); // Ignore comments starting with --
        logStatus('תוכנית נטענה...');
        pc = 0;
        repeatStack = [];
        ifSkip = false;
        ifEndPc = -1;
        return programLines.length > 0;
    }

    async function executeProgram() {
        simulationRunning = true;
        runButton.disabled = true;
        resetButton.disabled = false; // Keep reset enabled

        // Clear previous run highlights/states
        robotElement.classList.remove('robot-success', 'robot-failure');

        while (pc < programLines.length && simulationRunning) {
            const line = programLines[pc];
            let commandExecuted = false; // Flag to check if the current line was processed

             // Check if simulation was stopped by reset button
             if (!simulationRunning) break;

            // Handle skipping inside 'if' block
            if (ifSkip) {
                 if (pc === ifEndPc) {
                     ifSkip = false; // Reached the end of the skipped if block
                     ifEndPc = -1;
                     logStatus(`סוף אם (דילוג הסתיים).`);
                 }
                 pc++; // Always advance PC when skipping
                 continue; // Skip execution of commands within the block
            }

            // Process commands
            if (line === 'סוף חזרה') {
                logStatus('סוף חזרה.');
                if (repeatStack.length > 0) {
                    const currentLoop = repeatStack[repeatStack.length - 1];
                    currentLoop.currentIteration++;
                    if (currentLoop.currentIteration < currentLoop.count) {
                        pc = currentLoop.startIndex + 1; // Jump back to the start of the loop body
                        logStatus(`חוזר על לולאה... ${currentLoop.currentIteration + 1}/${currentLoop.count}`);
                    } else {
                        repeatStack.pop(); // End loop
                        pc++;
                        logStatus('לולאה הסתיימה.');
                    }
                } else {
                    logStatus('שגיאה: סוף חזרה ללא חזור תואם.', true);
                    simulationRunning = false; // Error state
                }
                 commandExecuted = true;

            } else if (line === 'סוף אם') {
                 logStatus('סוף אם.');
                 ifEndPc = -1; // Reset end marker
                 pc++;
                 commandExecuted = true;

            } else if (line.startsWith('חזור ')) {
                const parts = line.split(' ');
                const count = parseInt(parts[1]);
                if (!isNaN(count) && count > 0) {
                    const endIndex = findMatchingEnd(pc, 'חזור', 'סוף חזרה');
                    if (endIndex !== -1) {
                        repeatStack.push({ startIndex: pc, endIndex: endIndex, count: count, currentIteration: 0 });
                        logStatus(`התחלת לולאה: חוזר על ${count} פעמים.`);
                        pc++; // Move into the loop body
                    } else {
                        logStatus('שגיאה: חזור ללא סוף חזרה תואם.', true);
                        simulationRunning = false;
                    }
                } else {
                    logStatus('שגיאה: מספר חזרות לא תקין בפקודת חזור.', true);
                    simulationRunning = false;
                }
                 commandExecuted = true;

            } else if (line === 'אם קדימה חסום:') {
                 logStatus('בודק: אם קדימה חסום...');
                 robotElement.classList.add('robot-sensing'); // Visual cue for sensing
                 await new Promise(resolve => setTimeout(resolve, simulationSpeed / 2)); // Brief pause for sensing cue
                 robotElement.classList.remove('robot-sensing');

                const conditionMet = isFrontBlocked();
                ifEndPc = findMatchingEnd(pc, 'אם', 'סוף אם'); // Find where this if block ends
                 if (ifEndPc === -1) {
                     logStatus('שגיאה: אם ללא סוף אם תואם.', true);
                     simulationRunning = false;
                     commandExecuted = true; // Mark as handled to break loop
                 } else {
                     if (conditionMet) {
                         logStatus('התנאי מתקיים. מבצע בלוק אם.');
                         ifSkip = false; // Don't skip
                         pc++; // Enter the if block
                     } else {
                         logStatus('התנאי לא מתקיים. מדלג על בלוק אם.');
                         ifSkip = true; // Skip the block
                         pc = ifEndPc + 1; // Jump directly to after the end of the block
                     }
                      commandExecuted = true;
                 }

            } else { // Handle basic movement commands if not skipping
                 switch (line) {
                    case 'קדימה':
                        logStatus('פקודה: קדימה!');
                        const nextX = robot.x + directions[robot.dir].dx;
                        const nextY = robot.y + directions[robot.dir].dy;
                        if (isValidMove(nextX, nextY)) {
                            robot.x = nextX;
                            robot.y = nextY;
                            updateRobotPosition();
                            // Check for goal after moving
                            if (mazeGrid[robot.y][robot.x] === 'E') {
                                logStatus('מטרה הושגה! הרובוט הגיע ליציאה! 🎉');
                                robotElement.classList.add('robot-success');
                                simulationRunning = false; // Stop simulation on success
                            }
                             pc++; // Move to next command only if move was valid
                        } else {
                            logStatus('התנגשות! המסלול חסום.', true);
                            robotElement.classList.add('robot-failure'); // Indicate failure
                            simulationRunning = false; // Stop simulation on collision
                        }
                        commandExecuted = true;
                        break;
                    case 'שמאלה':
                        logStatus('פקודה: שמאלה.');
                        robot.dir = (robot.dir + 3) % 4; // 0 -> 3 -> 2 -> 1 -> 0
                        updateRobotPosition();
                        pc++;
                        commandExecuted = true;
                        break;
                    case 'ימינה':
                        logStatus('פקודה: ימינה.');
                        robot.dir = (robot.dir + 1) % 4; // 0 -> 1 -> 2 -> 3 -> 0
                        updateRobotPosition();
                        pc++;
                        commandExecuted = true;
                        break;
                    default:
                         // If we reach here and the line wasn't handled, it's an unknown command
                         if (!commandExecuted) {
                             logStatus(`שגיאה: פקודה לא מוכרת "${line}".`, true);
                             robotElement.classList.add('robot-failure');
                             simulationRunning = false; // Error state
                             commandExecuted = true;
                         }
                        break;
                }
            }


            // Wait for the next step, unless simulation stopped
            if (simulationRunning) {
                 await new Promise(resolve => setTimeout(resolve, simulationSpeed));
            }
        } // End of while loop

        // Final state check after loop finishes
        if (simulationRunning && pc >= programLines.length) {
            logStatus('סוף התוכנית. הרובוט לא הגיע למטרה.');
            robotElement.classList.add('robot-failure'); // Indicate failure if program ended before goal
        } else if (!simulationRunning && !robotElement.classList.contains('robot-success') && !robotElement.classList.contains('robot-failure')) {
             // Simulation was stopped manually (e.g., reset button)
             logStatus('הסימולציה הופסקה.');
        }


        // Ensure buttons are re-enabled after simulation ends
        runButton.disabled = false;
        resetButton.disabled = false;
    }

    runButton.addEventListener('click', () => {
        if (!simulationRunning) {
            clearStatus();
            if (parseProgram()) {
                resetRobot(); // Start from scratch for each run
                executeProgram();
            } else {
                logStatus('אין פקודות להרצה.', true);
            }
        }
    });

    resetButton.addEventListener('click', () => {
         simulationRunning = false; // Signal simulation to stop
         // The executeProgram loop will break and buttons will be re-enabled
         resetRobot();
    });

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.innerText = isHidden ? 'הסתר את ההסבר' : 'הצג מה קורה פה באמת!';
         // Scroll to the explanation if showing it
         if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });

    // Initial setup
    renderMaze();
    resetRobot();
    // Add Font Awesome (optional, requires CDN in header or local files)
    // const link = document.createElement('link');
    // link.rel = 'stylesheet';
    // link.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css';
    // document.head.appendChild(link);

</script>
```