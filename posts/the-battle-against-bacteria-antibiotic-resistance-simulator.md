---
title: "הקרב הגדול: חיידקים עמידים נגד אנטיביוטיקה"
english_slug: the-battle-against-bacteria-antibiotic-resistance-simulator
category: "מדעי החיים / ביולוגיה"
tags: [חיידקים, אנטיביוטיקה, עמידות לאנטיביוטיקה, אבולוציה, רפואה, סימולציה, משחק]
---
# הקרב הגדול: חיידקים עמידים נגד אנטיביוטיקה

אנטיביוטיקה – התרופה ששינתה את פני הרפואה והצילה אינספור חיים. אך כוחה נמצא תחת איום. בכל רגע, חיידקים מפתחים יכולות עמידות, הופכים לבלתי מנוצחים אל מול טיפולים שאמורים להשמיד אותם. כיצד התופעה הזו מתרחשת, ומה קורה כשאנטיביוטיקה כבר לא עובדת? היכנסו לזירת הקרב המיקרוסקופית וגלו בעצמכם!

<div id="app-container">
    <canvas id="bacteriaCanvas" width="700" height="450"></canvas>
    <div id="controls">
        <button id="startPauseBtn" class="control-btn primary">התחל סימולציה</button>
        <button id="addAntibioticBtn" class="control-btn warning">הוסף אנטיביוטיקה</button>
        <button id="addMutationBtn" class="control-btn info">חולל מוטציה אקראית</button>
         <button id="resetBtn" class="control-btn secondary">התחל מחדש</button>
        <div class="stats-panel">
            <label>ריכוז אנטיביוטיקה:</label>
            <span id="antibioticLevelDisplay" class="stat-value">0</span>
        </div>
        <div class="stats-panel">
            <label>אוכלוסייה כוללת:</label>
            <span id="populationDisplay" class="stat-value">0</span>
        </div>
        <div class="stats-panel">
            <label>אחוז עמידים:</label>
            <span id="resistantDisplay" class="stat-value">0%</span>
        </div>
    </div>
    <canvas id="graphCanvas" width="700" height="200"></canvas>
    <button id="toggleGraphBtn" class="toggle-btn">הצג גרף התפתחות</button>
</div>

<button id="toggleExplanationBtn" class="toggle-btn explanation-toggle">הצג/הסתר סיפור הרקע המלא</button>

<div id="explanation">
    <h2>הקרב הגדול: מאחורי הקלעים של הסימולציה</h2>

    <p>הסימולציה שלפניכם ממחישה את אחד האתגרים הגדולים ביותר של הרפואה המודרנית: עמידות לאנטיביוטיקה. כדי להבין לעומק את מה שראיתם מתרחש על המסך, בואו נצלול לפרטים:</p>

    <h3>מי הם החיידקים ולמה הם גורמים למחלות?</h3>
    חיידקים הם יצורים חד-תאיים זעירים שחיים בכל מקום - באוויר, במים, באדמה, ואפילו בתוכנו. רובם המוחלט ידידותיים ואף חיוניים לקיומנו (חשבו על חיידקי המעיים שעוזרים לעיכול!), אבל מיעוט קטן מהם הם "רעים". חיידקים פתוגניים (גורמי מחלות) פולשים לגוף, פוגעים בתאים שלנו, משחררים רעלים או מעוררים תגובה דלקתית שגורמת לנו להרגיש חולים. הם אחראים למחלות כמו דלקת ריאות, דלקות גרון, זיהומי עור ועוד.

    <h3>איך אנטיביוטיקה נכנסת לתמונה?</h3>
    אנטיביוטיקה היא נשק רב עוצמה נגד חיידקים. היא פועלת על ידי שיבוש תהליכים חיוניים לחיידק, כמו בניית דופן התא שלו, יצירת החלבונים שהוא צריך כדי לתפקד, או שכפול החומר התורשתי שלו. חשוב לזכור: אנטיביוטיקה יעילה רק נגד חיידקים! היא לא עוזרת נגד מחלות ויראליות כמו שפעת או הצטננות.

    <h3>אז מהי עמידות לאנטיביוטיקה?</h3>
    זוהי היכולת של חיידק לשרוד ולהתרבות גם כשהוא חשוף לאנטיביוטיקה שאמורה לחסל אותו. במצב כזה, הזיהום החיידקי ממשיך להתפשט בגוף למרות הטיפול, והופך להיות קשה, ואף בלתי אפשרי, לריפוי עם אותה אנטיביוטיקה.

    <h3>איך חיידקים הופכים לעמידים?</h3>
    לחיידקים יש כמה טריקים גנטיים שמאפשרים להם לפתח עמידות:
    <ol>
        <li>**מוטציות פתע:** בדומה לכל יצור חי, גם חיידקים עוברים מוטציות אקראיות ב-DNA שלהם כשהם מתרבים. רוב המוטציות לא משנות דבר, אבל לעיתים נדירות, מוטציה אחת קטנה יכולה להקנות לחיידק יכולת הישרדות חדשה, למשל: לשנות את צורת "המנעול" שהאנטיביוטיקה מנסה לפתוח, לדעת לפרק את האנטיביוטיקה עצמה, או לשנות את דופן התא כך שהאנטיביוטיקה לא תוכל לחדור פנימה.</li>
        <li>**העברת גנים אקספרס:** חיידקים לא חייבים לחכות למוטציה משלהם; הם יכולים פשוט "לקבל בירושה" או "לשאול" גנים של עמידות מחיידקים אחרים שכבר עמידים! זה קורה בכמה דרכים מדהימות:
            <ul>
                <li>**קוניוגציה:** שני חיידקים מתחברים במין "גשר" ומעבירים ביניהם מקטעי DNA קטנים ועגולים שנקראים פלסמידים, שלעיתים נושאים גנים של עמידות.</li>
                <li>**טרנספורמציה:** חיידק אוסף מקטעי DNA "חופשיים" שנמצאים בסביבה שלו (למשל מחיידק אחר שמת והתפרק) ומשלב אותם ב-DNA שלו.</li>
                <li>**טרנסדוקציה:** וירוסים מיוחדים שתוקפים חיידקים (בקטריופאג'ים) יכולים בטעות "לארוז" בתוכם פיסות DNA חיידקי (כולל גני עמידות) ולהעביר אותן לחיידק אחר כשהם מדביקים אותו.</li>
            </ul>
            תהליכים אלו מאפשרים לעמידות להתפשט במהירות מדהימה בין חיידקים שונים ואפילו בין מיני חיידקים שונים!</li>
    </ol>

    <h3>הברירה הטבעית בפעולה: איך אנטיביוטיקה מאיצה את התהליך?</h3>
    כאן נכנס הלחץ האבולוציוני לתמונה, בדיוק כפי שראיתם בסימולציה:
    <ol>
        <li>כשאנו נוטלים אנטיביוטיקה, היא פועלת כמו "מסננת".</li>
        <li>היא הורגת ביעילות את רוב החיידקים הרגישים שגרמו לזיהום.</li>
        <li>אבל אם באוכלוסיית החיידקים המקורית היו במקרה כמה חיידקים בודדים שהיו עמידים (בזכות מוטציה ספונטנית או גן עמידות שרכשו בעבר), הם שורדים את המתקפה.</li>
        <li>עם רוב המתחרים מחוץ לתמונה, החיידקים העמידים ששרדו מוצאים שטח פנוי ומתחילים להתרבות בקצב מסחרר.</li>
        <li>תוך זמן קצר, אוכלוסיית החיידקים הופכת מורכבת כמעט כולה מחיידקים עמידים.</li>
    </ol>
    זו הסיבה שכל כך חשוב להשתמש באנטיביוטיקה נכון: ליטול אותה רק כשצריך (נגד חיידקים, לא נגד וירוסים!), במינון הנכון, ולהשלים את כל מהלך הטיפול. טיפול קטוע או במינון נמוך מדי עלול להרוג רק את החיידקים הכי פחות עמידים, ולהשאיר "נבחרת" קטנה אך חזקה של עמידים יותר שישרדו ויתרבו.

    <h3>מדוע עמידות לאנטיביוטיקה היא בעיה עולמית חמורה?</h3>
    זוהי סכנה מיידית לבריאות של כולנו. ככל שיותר חיידקים הופכים עמידים ליותר סוגי אנטיביוטיקה, כך הופך קשה יותר (ולעיתים בלתי אפשרי) לטפל בזיהומים שבעבר היו שגרתיים. זיהומים קלים יחסית יכולים להפוך למסכני חיים. זה משפיע במיוחד על אוכלוסיות בסיכון כמו קשישים, תינוקות, אנשים עם מערכת חיסון מוחלשת, חולי סרטן, וחולים שעברו ניתוחים גדולים. עמידות לאנטיביוטיקה מאיימת על עצם היכולת שלנו לבצע הליכים רפואיים רבים שמסתמכים על היכולת לשלוט בזיהומים חיידקיים.

    <h3>מה אנו יכולים לעשות כדי לנצח בקרב?</h3>
    המאבק דורש מאמץ משולב של כולם:
    <ul>
        <li>**שימוש מושכל באנטיביוטיקה:** רק כשיש צורך אמיתי בזיהום חיידקי, בהתאם למרשם רופא, ובשום אופן לא נגד וירוסים! תמיד להשלים את כל ימי הטיפול.</li>
        <li>**מניעת זיהומים:** היגיינה בסיסית (שטיפת ידיים!), חיסונים שמונעים מחלות, היגיינה במזון ובמים.</li>
        <li>**מחקר ופיתוח:** מדענים וחברות תרופות חייבים לפתח בדחיפות סוגי אנטיביוטיקה חדשים ומנגנוני טיפול חלופיים.</li>
        <li>**ניטור ובקרה:** מעקב אחר התפשטות זני חיידקים עמידים.</li>
        <li>**שימוש אחראי בבעלי חיים:** צמצום השימוש באנטיביוטיקה בחקלאות ובחיות משק.</li>
        <li>**חינוך ומודעות:** לוודא שכולם מבינים את הבעיה ואת חשיבות השימוש הנכון באנטיביוטיקה.</li>
    </ul>
    רק על ידי פעולה משותפת נוכל להבטיח שהאנטיביוטיקה תישאר כלי יעיל לטיפול בזיהומים חיידקיים גם בעתיד.
</div>

<script>
    const canvas = document.getElementById('bacteriaCanvas');
    const ctx = canvas.getContext('2d');
    const graphCanvas = document.getElementById('graphCanvas');
    const graphCtx = graphCanvas.getContext('2d');
    const startPauseBtn = document.getElementById('startPauseBtn');
    const addAntibioticBtn = document.getElementById('addAntibioticBtn');
    const addMutationBtn = document.getElementById('addMutationBtn');
    const resetBtn = document.getElementById('resetBtn'); // Added reset button
    const antibioticLevelDisplay = document.getElementById('antibioticLevelDisplay');
    const populationDisplay = document.getElementById('populationDisplay');
    const resistantDisplay = document.getElementById('resistantDisplay');
    const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
    const explanationDiv = document.getElementById('explanation');
    const toggleGraphBtn = document.getElementById('toggleGraphBtn');

    const BAC_RADIUS = 3; // Radius of bacteria circle
    const MAX_BACTERIA = 4000; // Increased limit for slightly larger population
    const INITIAL_POPULATION = 800; // Increased initial population
    const INITIAL_RESISTANT_PERCENT = 1; // Start with a small percentage
    const SENSITIVE_COLOR = '#5cb85c'; // Green
    const RESISTANT_COLOR = '#d9534f'; // Red
    const DYING_COLOR = '#f0ad4e'; // Orange for dying
    const ANTIBIOTIC_KILL_PROB_SENSITIVE = 0.08; // Probability of sensitive bacteria dying per step *at max antibiotic*
    const ANTIBIOTIC_KILL_PROB_RESISTANT = 0.008; // Probability of resistant bacteria dying per step *at max antibiotic* (low)
    const REPRODUCTION_PROB = 0.004; // Probability of a bacterium reproducing per step (if space)
    const ANTIBIOTIC_DECAY_RATE = 0.0015; // Rate at which antibiotic concentration decreases per step
    const MUTATION_RATE_ON_CLICK_PERCENT = 2; // Percentage of sensitive bacteria to mutate on button click
    const MAX_ANTIBIOTIC_LEVEL = 100; // Max level for antibiotic slider/display
    const DYING_DURATION = 30; // Number of steps a bacterium stays in dying state

    let bacteria = [];
    let isRunning = false;
    let antibioticLevel = 0; // 0 to MAX_ANTIBIOTIC_LEVEL
    let stepCount = 0;

    // Graph data
    const graphData = {
        total: [],
        resistant: [] // Storing resistant count directly now
    };
    const MAX_GRAPH_POINTS = 350; // Increased graph points
    const GRAPH_UPDATE_INTERVAL = 8; // Update graph every X steps

    class Bacteria {
        constructor(x, y, isResistant = false) {
            this.x = x;
            this.y = y;
            this.isResistant = isResistant;
            this.color = isResistant ? RESISTANT_COLOR : SENSITIVE_COLOR;
            this.lifespan = 0; // Age tracking for reproduction and potential death
            this.isDying = false;
            this.dyingTimer = 0; // Timer for dying animation
            this.opacity = 1;
            this.dx = (Math.random() - 0.5) * 0.5; // Initial small movement
            this.dy = (Math.random() - 0.5) * 0.5;
        }

        draw() {
            ctx.fillStyle = this.isDying ? DYING_COLOR : this.color;
            ctx.globalAlpha = this.opacity; // Apply opacity for dying animation
            ctx.beginPath();
            ctx.arc(this.x, this.y, BAC_RADIUS, 0, Math.PI * 2);
            ctx.fill();
            ctx.globalAlpha = 1; // Reset opacity
        }

        update() {
            if (this.isDying) {
                this.dyingTimer++;
                this.opacity = 1 - (this.dyingTimer / DYING_DURATION); // Fade out
                if (this.dyingTimer >= DYING_DURATION) {
                    // Mark for removal
                    return false; // Indicate this bacterium should be removed
                }
                 // Continue subtle movement while dying
                this.x += this.dx;
                this.y += this.dy;
            } else {
                this.lifespan++;

                // Movement (random walk with slight momentum)
                this.dx += (Math.random() - 0.5) * 0.8; // Add random impulse
                this.dy += (Math.random() - 0.5) * 0.8;
                 // Limit speed
                const speed = Math.sqrt(this.dx * this.dx + this.dy * this.dy);
                const maxSpeed = 2; // Increased max speed slightly
                if (speed > maxSpeed) {
                    this.dx = (this.dx / speed) * maxSpeed;
                    this.dy = (this.dy / speed) * maxSpeed;
                }

                this.x += this.dx;
                this.y += this.dy;

                // Keep within bounds and bounce
                if (this.x < 0) { this.x = 0; this.dx *= -1; }
                if (this.x > canvas.width) { this.x = canvas.width; this.dx *= -1; }
                if (this.y < 0) { this.y = 0; this.dy *= -1; }
                if (this.y > canvas.height) { this.y = canvas.height; this.dy *= -1; }


                // Attempt to reproduce
                // Reproduce less often at max population
                const currentReproductionProb = bacteria.length < MAX_BACTERIA * 0.9 ? REPRODUCTION_PROB : REPRODUCTION_PROB * 0.5;

                if (this.lifespan > 50 && Math.random() < currentReproductionProb && bacteria.length < MAX_BACTERIA) {
                     // Simple reproduction: create a new bacterium nearby
                    const newBacX = this.x + (Math.random() - 0.5) * BAC_RADIUS * 3; // Spawn closer
                    const newBacY = this.y + (Math.random() - 0.5) * BAC_RADIUS * 3;
                     // Ensure new bacterium is within bounds (approx)
                    const clampedX = Math.max(0, Math.min(canvas.width, newBacX));
                    const clampedY = Math.max(0, Math.min(canvas.height, newBacY));

                     // Child inherits resistance. Lifespan starts low.
                    bacteria.push(new Bacteria(clampedX, clampedY, this.isResistant));
                    this.lifespan = 0; // Reset lifespan after reproducing
                }
            }
             return true; // Indicate bacterium is alive or still dying
        }

        checkAntibioticEffect() {
            if (this.isDying || antibioticLevel <= 0) return false;

            const effectMultiplier = antibioticLevel / MAX_ANTIBIOTIC_LEVEL;
            const killProb = this.isResistant ?
                ANTIBIOTIC_KILL_PROB_RESISTANT * effectMultiplier :
                ANTIBIOTIC_KILL_PROB_SENSITIVE * effectMultiplier;

            if (Math.random() < killProb) {
                this.isDying = true;
                this.dyingTimer = 0;
                this.color = DYING_COLOR; // Change color immediately
                this.opacity = 1; // Start fade from full opacity
                // Give it a slight final push animation? Optional.
                 this.dx = (Math.random() - 0.5) * 1;
                 this.dy = (Math.random() - 0.5) * 1;
                return true; // Indicate it started dying
            }
            return false; // Not killed by antibiotic this step
        }
    }

    function initSimulation() {
        bacteria = [];
        const numResistant = Math.floor(INITIAL_POPULATION * (INITIAL_RESISTANT_PERCENT / 100));
        const numSensitive = INITIAL_POPULATION - numResistant;

        for (let i = 0; i < numSensitive; i++) {
            bacteria.push(new Bacteria(
                Math.random() * canvas.width,
                Math.random() * canvas.height,
                false
            ));
        }
        for (let i = 0; i < numResistant; i++) {
            bacteria.push(new Bacteria(
                Math.random() * canvas.width,
                Math.random() * canvas.height,
                true
            ));
        }
        antibioticLevel = 0;
        stepCount = 0;
        graphData.total = [];
        graphData.resistant = [];
        updateStats();
        drawGraph(); // Draw initial empty graph or first point
        drawSimulation();
         if(isRunning) { // Restart animation loop if it was running
             isRunning = false; // Stop previous loop first
             startPauseBtn.textContent = 'התחל סימולציה';
             // Allow user to click start manually or uncomment below
             // isRunning = true;
             // startPauseBtn.textContent = 'השהה סימולציה';
             // requestAnimationFrame(updateSimulation);
         } else {
             startPauseBtn.textContent = 'התחל סימולציה';
         }
    }

    function drawSimulation() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Add a subtle antibiotic visualization if level is high
        if (antibioticLevel > 10) {
            ctx.fillStyle = `rgba(240, 173, 78, ${antibioticLevel / MAX_ANTIBIOTIC_LEVEL * 0.15})`; // Subtle orange overlay
            ctx.fillRect(0, 0, canvas.width, canvas.height);
        }

        bacteria.forEach(bac => bac.draw());
    }

    function updateSimulation() {
        if (!isRunning) return;

        stepCount++;

        // Decay antibiotic level
        if (antibioticLevel > 0) {
            antibioticLevel -= ANTIBIOTIC_DECAY_RATE * MAX_ANTIBIOTIC_LEVEL;
            if (antibioticLevel < 0) antibioticLevel = 0;
        }

        // Update bacteria positions, apply antibiotic effect, and filter dead/fully faded bacteria
        bacteria.forEach(bac => bac.checkAntibioticEffect()); // Check for kills FIRST
        bacteria = bacteria.filter(bac => bac.update()); // Update position/state, filter out those that finished dying

        updateStats();
        updateGraph();
        drawSimulation();
        requestAnimationFrame(updateSimulation);
    }

    function updateStats() {
        const total = bacteria.length;
        const resistantCount = bacteria.filter(bac => bac.isResistant && !bac.isDying).length; // Count only alive resistant
        const sensitiveCount = bacteria.filter(bac => !bac.isResistant && !bac.isDying).length; // Count only alive sensitive

        const resistantPercent = total > 0 ? (resistantCount / total) * 100 : 0;

        populationDisplay.textContent = total;
        resistantDisplay.textContent = `${resistantPercent.toFixed(1)}%`;
        antibioticLevelDisplay.textContent = `${antibioticLevel.toFixed(0)}`; // Round antibiotic display
    }

    function updateGraph() {
         if (stepCount % GRAPH_UPDATE_INTERVAL === 0) {
            const total = bacteria.length;
            const resistantCount = bacteria.filter(bac => bac.isResistant && !bac.isDying).length;

            graphData.total.push(total);
            graphData.resistant.push(resistantCount); // Store raw resistant count

            // Keep graph points limited
            if (graphData.total.length > MAX_GRAPH_POINTS) {
                graphData.total.shift();
                graphData.resistant.shift();
            }
            drawGraph();
        }
    }

    function drawGraph() {
        graphCtx.clearRect(0, 0, graphCanvas.width, graphCanvas.height);

        // Draw background grid/lines
        graphCtx.strokeStyle = '#eee'; // Lighter grid
        graphCtx.lineWidth = 1;
        // Horizontal lines (optional)
        // for(let i=0; i<=10; i++) {
        //     const y = graphCanvas.height - (i/10) * graphCanvas.height;
        //     graphCtx.beginPath();
        //     graphCtx.moveTo(0, y);
        //     graphCtx.lineTo(graphCanvas.width, y);
        //     graphCtx.stroke();
        // }


        // Draw axes
        graphCtx.strokeStyle = '#ccc';
        graphCtx.beginPath();
        graphCtx.moveTo(0, graphCanvas.height); // X-axis
        graphCtx.lineTo(graphCanvas.width, graphCanvas.height);
        graphCtx.moveTo(0, 0); // Y-axis
        graphCtx.lineTo(0, graphCanvas.height);
        graphCtx.stroke();

        // Draw data
        const dataLength = graphData.total.length;
        if (dataLength < 2) return;

        const xStep = graphCanvas.width / (MAX_GRAPH_POINTS - 1); // X-scaling based on max points
        const maxPopScale = MAX_BACTERIA * 1.1; // Scale Y slightly above max pop for padding

        // Draw Total Population
        graphCtx.strokeStyle = '#337ab7'; // Blue
        graphCtx.lineWidth = 2; // Thicker line
        graphCtx.beginPath();
        graphCtx.moveTo(0, graphCanvas.height - (graphData.total[0] / maxPopScale) * graphCanvas.height);
        for (let i = 1; i < dataLength; i++) {
            const x = (MAX_GRAPH_POINTS - dataLength + i) * xStep; // Align points to the right
            const y = graphCanvas.height - (graphData.total[i] / maxPopScale) * graphCanvas.height;
            graphCtx.lineTo(x, y);
        }
        graphCtx.stroke();

        // Draw Resistant Population (count)
        graphCtx.strokeStyle = RESISTANT_COLOR; // Red
        graphCtx.lineWidth = 2; // Thicker line
        graphCtx.beginPath();
        graphCtx.moveTo(0, graphCanvas.height - (graphData.resistant[0] / maxPopScale) * graphCanvas.height);
        for (let i = 1; i < dataLength; i++) {
             const x = (MAX_GRAPH_POINTS - dataLength + i) * xStep; // Align points to the right
            const y = graphCanvas.height - (graphData.resistant[i] / maxPopScale) * graphCanvas.height;
            graphCtx.lineTo(x, y);
        }
        graphCtx.stroke();

         // Add Y-axis labels (simplified)
        graphCtx.fillStyle = '#000';
        graphCtx.font = '10px Arial';
        graphCtx.fillText(MAX_BACTERIA, 5, 15);
        graphCtx.fillText(0, 5, graphCanvas.height - 5);
        // Add legend
        graphCtx.fillStyle = '#337ab7';
        graphCtx.fillText('אוכלוסייה כוללת', graphCanvas.width - 100, 15);
         graphCtx.fillStyle = RESISTANT_COLOR;
        graphCtx.fillText('חיידקים עמידים', graphCanvas.width - 100, 30);

         // Optional: Add X-axis indicator (time/steps)
         graphCtx.fillStyle = '#000';
         graphCtx.fillText('זמן (צעדי סימולציה)', graphCanvas.width / 2 - 50, graphCanvas.height - 5);
    }


    startPauseBtn.addEventListener('click', () => {
        isRunning = !isRunning;
        startPauseBtn.textContent = isRunning ? 'השהה סימולציה' : 'המשך סימולציה';
        if (isRunning) {
            requestAnimationFrame(updateSimulation);
        }
    });

    addAntibioticBtn.addEventListener('click', () => {
        antibioticLevel = MAX_ANTIBIOTIC_LEVEL; // Set to max level
         // Optional: add visual pulse to canvas border or background for a moment
         canvas.style.transition = 'border-color 0.2s ease-in-out';
         canvas.style.borderColor = DYING_COLOR;
         setTimeout(() => {
             canvas.style.borderColor = '#000';
             canvas.style.transition = '';
         }, 500);
    });

    addMutationBtn.addEventListener('click', () => {
        const sensitiveBacteria = bacteria.filter(bac => !bac.isResistant && !bac.isDying);
        const numToMutate = Math.floor(sensitiveBacteria.length * (MUTATION_RATE_ON_CLICK_PERCENT / 100));
        let mutatedCount = 0;

        // Shuffle sensitive bacteria to mutate random ones
        const shuffledSensitive = sensitiveBacteria.sort(() => 0.5 - Math.random());

        for (let i = 0; i < numToMutate && i < shuffledSensitive.length; i++) {
            const bac = shuffledSensitive[i];
            if (bac) {
                bac.isResistant = true;
                bac.color = RESISTANT_COLOR;
                // Optional: Add a temporary visual cue to highlight mutation
                 // bac.isPulsing = true; // Need to add this property and handle in draw/update
                 mutatedCount++;
            }
        }
        console.log(`Mutated ${mutatedCount} bacteria`); // Debugging
        updateStats(); // Update display immediately after mutation
    });

    resetBtn.addEventListener('click', () => {
        initSimulation();
    });


    toggleExplanationBtn.addEventListener('click', () => {
        const isVisible = explanationDiv.style.display !== 'none';
        explanationDiv.style.display = isVisible ? 'none' : 'block';
        toggleExplanationBtn.textContent = isVisible ? 'הצג סיפור הרקע המלא' : 'הסתר סיפור הרקע המלא';
         // Optional: smooth toggle with CSS
         // explanationDiv.style.transition = 'opacity 0.5s ease-in-out';
         // explanationDiv.style.opacity = isVisible ? 0 : 1;
         // if (!isVisible) explanationDiv.style.display = 'block';
         // setTimeout(() => {
         //     if (isVisible) explanationDiv.style.display = 'none';
         // }, 500);
    });

     toggleGraphBtn.addEventListener('click', () => {
        const isVisible = graphCanvas.style.display !== 'none';
        graphCanvas.style.display = isVisible ? 'none' : 'block';
        toggleGraphBtn.textContent = isVisible ? 'הצג גרף התפתחות' : 'הסתר גרף התפתחות';
         // Optional: smooth toggle with CSS
         // graphCanvas.style.transition = 'opacity 0.5s ease-in-out';
         // graphCanvas.style.opacity = isVisible ? 0 : 1;
         // if (!isVisible) graphCanvas.style.display = 'block';
         // setTimeout(() => {
         //     if (isVisible) graphCanvas.style.display = 'none';
         // }, 500);
    });


    // Initial setup
    initSimulation();

</script>

<style>
    #app-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        font-family: 'Arial', sans-serif;
        background-color: #ffffff; /* Clean background */
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 740px; /* Match canvas width + padding */
        margin: 20px auto;
        box-sizing: border-box;
    }

    #bacteriaCanvas {
        border: 2px solid #333; /* Stronger border */
        background-color: #e9f7ef; /* Pleasant light green */
        box-shadow: inset 0 0 8px rgba(0,0,0,0.05); /* Subtle inner shadow */
        border-radius: 5px;
    }

    #graphCanvas {
        border: 1px solid #ccc;
        margin-top: 20px; /* Increased margin */
        display: none; /* Initial state hidden */
        background-color: #fdfdfd; /* Light graph background */
        border-radius: 5px;
    }

    #controls {
        margin-top: 20px; /* Increased margin */
        display: flex;
        flex-wrap: wrap;
        gap: 15px; /* Increased gap */
        justify-content: center;
        align-items: center;
        padding: 15px; /* Increased padding */
        border: 1px solid #ddd; /* Lighter border */
        border-radius: 8px; /* More rounded corners */
        background-color: #f9f9f9; /* Subtle background */
        width: 100%; /* Take full width */
        box-sizing: border-box;
    }

    .control-btn {
        padding: 10px 20px; /* Larger padding */
        font-size: 1rem; /* Standard size */
        cursor: pointer;
        border: none;
        border-radius: 5px; /* More rounded */
        transition: background-color 0.2s ease, transform 0.1s ease; /* Smooth transitions */
        font-weight: bold;
    }

    .control-btn:hover {
        transform: translateY(-1px); /* Slight lift effect */
    }
    .control-btn:active {
         transform: translateY(0); /* Press effect */
         opacity: 0.9;
    }


    .primary {
        background-color: #007bff; /* Bootstrap primary blue */
        color: white;
    }
     .primary:hover {
        background-color: #0056b3;
    }

    .warning {
        background-color: #ffc107; /* Bootstrap warning yellow */
        color: #212529; /* Dark text for contrast */
    }
     .warning:hover {
        background-color: #e0a800;
    }

    .info {
        background-color: #17a2b8; /* Bootstrap info cyan */
        color: white;
    }
     .info:hover {
        background-color: #138496;
    }

     .secondary {
        background-color: #6c757d; /* Bootstrap secondary gray */
        color: white;
    }
     .secondary:hover {
        background-color: #545b62;
    }


    .stats-panel {
        display: flex;
        align-items: center;
        background-color: #e9ecef; /* Light gray background */
        padding: 8px 12px;
        border-radius: 4px;
         font-size: 0.9rem;
    }

    .stats-panel label {
        font-weight: bold;
        margin-right: 5px;
        color: #495057; /* Dark gray text */
    }

    .stat-value {
        font-weight: normal;
        color: #333;
    }

    #toggleExplanationBtn, #toggleGraphBtn {
        padding: 10px 20px;
        font-size: 1rem;
        cursor: pointer;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #f8f9fa; /* Light neutral background */
        margin-top: 15px; /* Space above toggles */
        transition: background-color 0.2s ease;
    }

     .toggle-btn:hover {
        background-color: #e2e6ea; /* Slightly darker on hover */
    }

     .explanation-toggle {
         margin-bottom: 10px; /* Space below explanation toggle */
     }


    #explanation {
        display: none; /* Initial state hidden */
        margin-top: 20px;
        border-top: 1px solid #eee; /* Lighter border */
        padding-top: 20px;
        line-height: 1.7; /* Improved readability */
        color: #333; /* Darker text */
    }

    #explanation h2, #explanation h3 {
        color: #0056b3; /* Consistent with primary button */
        margin-top: 25px; /* More space above headings */
        margin-bottom: 10px;
         border-bottom: 1px solid #eee; /* Subtle underline */
         padding-bottom: 5px;
    }

     #explanation h2 {
         font-size: 1.8rem;
     }
      #explanation h3 {
         font-size: 1.4rem;
         color: #495057;
     }


    #explanation p, #explanation ul, #explanation ol {
        margin-bottom: 15px; /* More space below paragraphs/lists */
    }

     #explanation ul, #explanation ol {
         padding-left: 25px; /* Increased padding */
     }

     #explanation li {
         margin-bottom: 8px; /* Space between list items */
     }

     #explanation ul li:before { /* Simple custom bullet */
        content: "• ";
        color: #007bff;
        font-weight: bold;
        display: inline-block;
        width: 1em;
        margin-left: -1em;
     }

     #explanation ol li:before { /* Adjust ol numbering style if needed */
         font-weight: bold;
         margin-right: 5px;
     }

     /* Responsive adjustments (basic) */
     @media (max-width: 768px) {
         #app-container {
             padding: 15px;
             margin: 10px auto;
         }
         #bacteriaCanvas, #graphCanvas {
             width: 100%; /* Make canvases responsive */
             height: auto; /* Maintain aspect ratio approx */
         }
         #controls {
             gap: 10px;
             padding: 10px;
         }
         .control-btn, .toggle-btn {
             padding: 8px 15px;
             font-size: 0.9rem;
         }
          .stats-panel {
             padding: 6px 10px;
              font-size: 0.8rem;
         }
     }


</style>
```