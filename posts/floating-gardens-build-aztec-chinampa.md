---
title: "גנים צפים: בנה צ'ינאמפה אצטקית"
english_slug: floating-gardens-build-aztec-chinampa
category: "היסטוריה של הטכנולוגיה"
tags:
  - אצטקים
  - צ'ינאמפס
  - חקלאות עתיקה
  - טכנולוגיה
  - קיימות
---
# גנים צפים: בנה צ'ינאמפה אצטקית

דמיינו עיר ענקית שצומחת בלב אגם, וצריכה להאכיל מיליוני אנשים - ללא שדות מספיקים! האצטקים פתרו זאת בגאונות: הם הפכו את האגם לשדה יבול. בואו לגלות איך, ולבנות בעצמכם גן צף עתיק!

<div id="app-container">
    <div id="lake-area">
        <div id="water-level"></div>
        <div id="chinampa-area" class="dropzone">
            <div id="chinampa-layers">
                <!-- Layers will be added here -->
            </div>
            <div id="chinampa-outline">גרור חומרים לכאן לבניית הצ'ינאמפה!</div>
             <div id="completion-overlay" class="hidden">🎉 הצ'ינאמפה מוכנה! 🎉</div>
        </div>
        <div id="water-surface"></div>
    </div>
    <div id="tools-area">
        <h2>חומרי בנייה מהאגם:</h2>
        <div class="tool" id="tool-reeds" draggable="true" data-material="reeds">
            <div class="tool-icon" style="background-color: #8B4513;"></div>
            <p>קני סוף וענפים</p>
        </div>
        <div class="tool" id="tool-mud" draggable="true" data-material="mud">
             <div class="tool-icon" style="background-color: #A0522D;"></div>
            <p>בוץ עשיר</p>
        </div>
        <div class="tool" id="tool-compost" draggable="true" data-material="compost">
             <div class="tool-icon" style="background-color: #556B2F;"></div>
            <p>רקבובית וצמחייה</p>
        </div>
        <div class="tool" id="tool-stones" draggable="true" data-material="stones">
             <div class="tool-icon" style="background-color: #A9A9A9;"></div>
            <p>אבנים קטנות</p>
        </div>
    </div>
    <div id="feedback-area">
        <h2>סטטוס בנייה:</h2>
        <div class="feedback-item">
            <label>יציבות:</label>
            <div class="feedback-bar" id="stability-bar"><div class="progress"></div></div>
            <span id="stability-text">0%</span>
        </div>
        <div class="feedback-item">
            <label>גובה (מעל המים):</label>
            <div class="feedback-bar" id="height-bar"><div class="progress"></div></div>
             <span id="height-text">0%</span>
        </div>
        <div id="build-message">נתחיל לבנות! גרור את קני הסוף ראשונים לבסיס יציב.</div>
    </div>
</div>

<style>
/* Google Font - Example, requires linking in head, but keeping structure simple */
/* @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;700&display=swap'); */

:root {
    --aztec-blue: #0077be;
    --aztec-dark-blue: #005a9c;
    --aztec-water-gradient: linear-gradient(to bottom, rgba(0,119,190,0.8), rgba(0,90,156,0.9));
    --aztec-reeds: #8B4513;
    --aztec-mud: #A0522D;
    --aztec-compost: #556B2F;
    --aztec-stones: #A9A9A9;
    --ui-light-grey: #f9f9f9;
    --ui-medium-grey: #eee;
    --ui-dark-grey: #333;
    --success-color: #4CAF50;
    --warning-color: #ff9800;
    --border-radius: 8px;
    --padding: 15px;
}

body {
    font-family: 'Assistant', sans-serif; /* Or other preferred font */
    line-height: 1.6;
    color: var(--ui-dark-grey);
    background-color: #eef2f7; /* Light background */
    padding: 20px;
}

h1, h2, h3 {
    color: var(--aztec-dark-blue);
}

#app-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 25px; /* Increased gap */
    margin-top: 20px;
    width: 100%;
}

#lake-area {
    width: 90%; /* Increased width */
    max-width: 700px;
    height: 400px; /* Increased height */
    background-color: var(--aztec-blue); /* Water color */
    position: relative;
    border-radius: var(--border-radius);
    overflow: hidden;
    border: 3px solid var(--aztec-dark-blue); /* Thicker border */
    box-shadow: inset 0 0 20px rgba(0,0,0,0.3); /* Inner shadow for depth */
}

#water-level {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 80%; /* Represents initial water depth */
    background: var(--aztec-water-gradient);
    z-index: 1;
    transition: height 0.8s ease-out; /* Animation for water level change */
}

#water-surface {
     position: absolute;
    bottom: 80%; /* Should be at top of water-level */
    left: 0;
    right: 0;
    height: 5px; /* Thin line */
    background: linear-gradient(to right, rgba(255,255,255,0.5), rgba(255,255,255,0.1), rgba(255,255,255,0.5)); /* Subtle highlight */
     z-index: 2;
      pointer-events: none;
     transition: bottom 0.8s ease-out; /* Match water-level transition */
}


#chinampa-area {
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 70%; /* Slightly wider */
    height: 15%; /* Starting point for the base - sits *in* the water */
    border: 3px dashed rgba(255, 255, 255, 0.6); /* More subtle dashed border */
    box-sizing: border-box;
    display: flex;
    flex-direction: column-reverse; /* Stack layers from bottom up */
    align-items: center;
    justify-content: flex-start;
    z-index: 2;
    overflow: hidden;
    transition: height 0.8s ease-out; /* Animation for chinampa height growth */
    padding-bottom: 5px; /* Small internal padding */
}

#chinampa-outline {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: rgba(255, 255, 255, 0.9); /* Brighter white */
    font-size: 1.4em; /* Larger font */
    text-align: center;
    pointer-events: none;
    z-index: 0;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
    opacity: 1;
    transition: opacity 0.5s ease-in-out;
}

#chinampa-area.has-layers #chinampa-outline {
    opacity: 0; /* Hide outline when layers are added */
}


#chinampa-layers {
    width: 100%;
    height: 100%; /* Will grow with layers */
    display: flex;
    flex-direction: column-reverse;
    align-items: center;
    justify-content: flex-start;
    position: relative;
    bottom: 0;
}

.chinampa-layer {
    width: 98%; /* Layers almost full width */
    min-height: 10px; /* Minimum height for a layer */
    box-sizing: border-box;
    position: relative;
    opacity: 0; /* Start invisible for animation */
    transform: translateY(10px); /* Start slightly lower */
    animation: layer-fade-in 0.5s ease-out forwards; /* Animation */
    border-radius: 3px; /* Small radius for layers */
    margin-bottom: 2px; /* Small gap between layers */
}

@keyframes layer-fade-in {
    to {
        opacity: 0.9;
        transform: translateY(0);
    }
}


.layer-reeds {
    background-color: var(--aztec-reeds);
    border: 1px solid #5a2c0b;
    background: linear-gradient(to right, var(--aztec-reeds) 0%, #a0643a 50%, var(--aztec-reeds) 100%); /* Simple texture effect */
}

.layer-mud {
    background-color: var(--aztec-mud);
    border: 1px solid #633119;
     background: linear-gradient(to bottom, var(--aztec-mud), #c07c5c); /* Simple texture effect */
}

.layer-compost {
    background-color: var(--aztec-compost);
    border: 1px solid #35451e;
     background: linear-gradient(to bottom, var(--aztec-compost), #7c904f); /* Simple texture effect */
}

.layer-stones {
    background-color: var(--aztec-stones);
    border: 1px solid #696969;
    background: repeating-linear-gradient(45deg, var(--aztec-stones), var(--aztec-stones) 10px, #cccccc 10px, #cccccc 20px); /* Stone texture effect */
}

#tools-area {
    display: flex;
    justify-content: center;
    gap: 25px; /* Increased gap */
    flex-wrap: wrap;
    padding: var(--padding);
    border: 1px solid #ccc;
    border-radius: var(--border-radius);
    background-color: var(--ui-light-grey);
    width: 90%; /* Increased width */
    max-width: 700px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

#tools-area h2 {
    width: 100%;
    text-align: center;
    margin-top: 0;
    margin-bottom: 15px; /* Increased margin */
    color: var(--aztec-dark-blue);
}

.tool {
    text-align: center;
    cursor: grab;
    padding: 12px; /* Increased padding */
    border: 1px solid #ddd;
    border-radius: var(--border-radius); /* Match outer radius */
    background-color: #fff;
    box-shadow: 3px 3px 8px rgba(0,0,0,0.1); /* Stronger shadow */
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    width: 100px; /* Fixed width */
    display: flex; /* Use flex for layout inside tool */
    flex-direction: column;
    align-items: center;
}

.tool:hover {
    transform: translateY(-5px); /* Lift on hover */
    box-shadow: 5px 5px 12px rgba(0,0,0,0.15); /* Stronger shadow on hover */
}

.tool:active {
    cursor: grabbing;
    transform: scale(0.95); /* Shrink slightly when grabbed */
    box-shadow: 1px 1px 4px rgba(0,0,0,0.1);
}

.tool-icon {
    width: 50px;
    height: 50px;
    display: block;
    margin: 0 auto 8px; /* Increased margin */
    border-radius: 4px;
    border: 1px solid rgba(0,0,0,0.1); /* Subtle border */
     box-shadow: inset 0 0 5px rgba(0,0,0,0.2); /* Inner shadow for depth */
}

.tool p {
    margin: 0;
    font-size: 0.9em;
    color: #555;
    font-weight: bold;
}

.dropzone.drag-over {
    background-color: rgba(0, 119, 190, 0.2); /* Water color with transparency */
    border-color: rgba(255, 255, 255, 0.9);
    transform: translateX(-50%) scale(1.02); /* Slightly enlarge dropzone */
    box-shadow: 0 0 20px rgba(255,255,255,0.5); /* Glow effect */
}

#feedback-area {
    width: 90%; /* Increased width */
    max-width: 700px;
    padding: var(--padding);
    border: 1px solid #ccc;
    border-radius: var(--border-radius);
    background-color: var(--ui-light-grey);
    display: flex;
    flex-direction: column;
    gap: 15px; /* Increased gap */
    text-align: center;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

#feedback-area h2 {
     margin-top: 0;
    margin-bottom: 10px; /* Increased margin */
    color: var(--aztec-dark-blue);
}

.feedback-item {
    display: flex;
    align-items: center;
    gap: 15px; /* Increased gap */
    justify-content: center;
}

.feedback-item label {
    font-weight: bold;
    width: 120px; /* Wider label for "גובה (מעל המים)" */
    text-align: right;
    color: #555;
}

.feedback-bar {
    flex-grow: 1;
    height: 25px; /* Thicker bars */
    background-color: var(--ui-medium-grey);
    border-radius: 12px; /* More rounded */
    overflow: hidden;
    max-width: 300px;
    border: 1px solid #ccc;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);
}

.feedback-bar .progress {
    height: 100%;
    width: 0%;
    background-color: var(--success-color); /* Green by default */
    transition: width 0.8s ease-out; /* Slower, smoother animation */
    background: linear-gradient(to right, #8bc34a, var(--success-color)); /* Gradient fill */
}

#stability-bar .progress {
    background-color: var(--warning-color); /* Orange for stability */
    background: linear-gradient(to right, #ffb300, var(--warning-color)); /* Gradient fill */
}

#stability-text, #height-text {
    width: 50px; /* Wider text area */
    text-align: left;
    font-weight: bold;
    color: var(--aztec-dark-blue);
}

#build-message {
    margin-top: 15px; /* Increased margin */
    font-size: 1.2em; /* Larger font */
    color: var(--aztec-dark-blue);
    min-height: 1.8em; /* Reserve space */
    font-weight: bold;
    transition: color 0.5s ease; /* Color transition on message change */
}

#build-message.success {
    color: var(--success-color);
}

#build-message.warning {
     color: var(--warning-color);
}

#completion-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 120, 0, 0.7); /* Semi-transparent green */
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2em;
    font-weight: bold;
    text-shadow: 2px 2px 5px rgba(0,0,0,0.5);
    z-index: 10;
    pointer-events: none; /* Allow interaction underneath */
    opacity: 0;
    transition: opacity 1s ease-in-out;
}

#completion-overlay:not(.hidden) {
    opacity: 1;
}

.hidden {
    display: none; /* Use class to manage visibility */
}


#toggle-explanation {
    margin-top: 30px; /* Increased margin */
    padding: 12px 20px; /* Increased padding */
    font-size: 1.1em; /* Larger font */
    cursor: pointer;
    border: none;
    border-radius: var(--border-radius); /* Match other elements */
    background-color: var(--aztec-blue);
    color: white;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

#toggle-explanation:hover {
    background-color: var(--aztec-dark-blue);
}
#toggle-explanation:active {
    transform: scale(0.98);
}


#explanation {
    margin-top: 25px; /* Increased margin */
    padding: var(--padding);
    border: 1px solid #ccc;
    border-radius: var(--border-radius);
    background-color: var(--ui-light-grey);
    width: 90%; /* Increased width */
    max-width: 700px;
    display: none; /* Initially hidden */
    line-height: 1.7; /* Increased line height */
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    color: #555;
}

#explanation h3 {
    color: var(--aztec-dark-blue);
    margin-top: 15px;
    margin-bottom: 10px;
    border-bottom: 2px solid #eee; /* Separator */
    padding-bottom: 5px;
}

#explanation h3:first-child {
    margin-top: 0;
}

#explanation ul {
    padding-left: 25px; /* Slightly more padding */
    margin-bottom: 15px;
}

#explanation li {
    margin-bottom: 8px;
}

</style>

<button id="toggle-explanation">רוצים לדעת עוד על צ'ינאמפס?</button>

<div id="explanation">
    <h3>קסם על המים: סוד הגנים הצפים של האצטקים</h3>
    <p>נסו לדמיין את טנוצ'טיטלאן, בירת האצטקים המפוארת, צפה על אי בלב אגם טקסקוקו. כשהעיר גדלה והתפתחה להיות אחת הגדולות בעולם, האצטקים נתקלו באתגר עצום: איך להאכיל מיליוני תושבים כשיש כל כך מעט אדמה יבשה? הפתרון שלהם היה מבריק ופשוט כאחד: הם יצרו אדמה חקלאית בתוך האגם עצמו! זוהי הצ'ינאמפה, שיטת חקלאות מהפכנית שהפכה את האגם לשדה יבולים אינסופי.</p>

    <h3>איך בונים אי? שלב אחר שלב</h3>
    <p>בניית צ'ינאמפה לא הייתה קסם, אלא עבודה קשה וחכמה, תוך שימוש בחומרים שהיו זמינים בשפע מסביב לאגם:</p>
    <ul>
        <li><strong>מתחילים בבסיס:</strong> תחילה, תוחמים אזור מלבני רדוד באגם. כמו שראיתם בסימולציה, משתמשים בעיקר בקני סוף, ענפים ושורשים שנקשרים יחד ונועצים אותם בקרקעית הרדודה כדי ליצור גבולות יציבים.</li>
        <li><strong>שכבות של פוריות:</strong> את השטח התחום ממלאים בזהירות בשכבות. השכבה העיקרית היא בוץ עשיר בדשן, שנגרף מקרקעית האגם. בין שכבות הבוץ מוסיפים גם רקבובית, עלים, ענפים וצמחיית מים – כל מה שהופך לאדמה סופר-פורייה.</li>
        <li><strong>ייצוב טבעי:</strong> כדי שהגן הצף לא יתפרק או ייסחף, האצטקים נטעו עצי ערבה (שנקראים Ahuejote) בשולי הצ'ינאמפה. השורשים החזקים של העצים האלה יצרו רשת טבעית שחיזקה את המבנה כולו. לעיתים גם הוסיפו אבנים קטנות לייצוב נוסף, במיוחד בבסיס.</li>
        <li><strong>רשת של חיים ותנועה:</strong> הצ'ינאמפס נבנו בצפיפות, אבל תמיד הושארו ביניהן תעלות מים רחבות מספיק למעבר סירות קאנו. התעלות שימשו לא רק כנתיבי תחבורה יעילים, אלא גם סיפקו לחות מתמדת לאדמה העשירה, בלי צורך להשקות!</li>
    </ul>

    <h3>הקסם ממשיך: יתרונות שקשה לנצח</h3>
    <ul>
        <li><strong>יבולים מטורפים:</strong> השילוב של בוץ עשיר, רקבובית, ודשן טבעי מהאגם, יצר קרקע כה פורייה שהניבה יבולים עצומים.</li>
        <li><strong>חקלאות לאורך כל השנה:</strong> האספקה הקבועה של לחות מהתעלות והטמפרטורה היציבה של המים אפשרו גידולים רצופים. בחלק מהגידולים, האצטקים יכלו לקצור עד 7 פעמים בשנה!</li>
        <li><strong>סופר-קיימא:</strong> הצ'ינאמפס היו מודל מדהים של חקלאות בת קיימא. הם השתמשו בחומרים מקומיים ומתחדשים, יצרו אדמה בעצמם, וניצלו את משאבי האגם ביעילות יוצאת דופן.</li>
    </ul>

    <h3>מורשת חיה</h3>
    <p>למרות שמרבית האגם המקורי יובש עם השנים, עד היום קיימים אזורים כמו שוצ'ימילקו (Xochimilco) ליד מקסיקו סיטי, שבהם עדיין משתמשים בשיטת הצ'ינאמפה. הגנים הצפים הם לא רק שריד היסטורי מרתק, אלא גם השראה חשובה לחקלאות אקולוגית ולחיפוש אחר פתרונות יצירתיים לקיימות בעולם המודרני. האצטקים הראו לנו שאפשר להפוך אתגרים סביבתיים להזדמנויות מדהימות!</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const chinampaArea = document.getElementById('chinampa-area');
    const chinampaLayers = document.getElementById('chinampa-layers');
    const tools = document.querySelectorAll('.tool');
    const stabilityBar = document.getElementById('stability-bar').querySelector('.progress');
    const heightBar = document.getElementById('height-bar').querySelector('.progress');
    const stabilityText = document.getElementById('stability-text');
    const heightText = document.getElementById('height-text');
    const buildMessage = document.getElementById('build-message');
    const chinampaOutline = document.getElementById('chinampa-outline');
    const waterLevel = document.getElementById('water-level');
    const waterSurface = document.getElementById('water-surface');
    const completionOverlay = document.getElementById('completion-overlay');


    let currentStability = 0; // Max 100 (arbitrary points)
    let currentHeight = 0;   // Max height before considered "ready" (arbitrary units)
    const maxHeightNeeded = 100; // Units needed for goal
    const maxStabilityNeeded = 100; // Units needed for goal
    const initialWaterHeightPercent = 80; // CSS percentage

    // Points/Effects per material drop (tuned for progression)
    const materialEffects = {
        reeds: { height: 10, stability: 25, message: "קני סוף וענפים יוצרים בסיס איתן!", colorClass: 'warning' },
        mud: { height: 15, stability: 5, message: "בוץ עשיר מוסיף גובה ופוריות!", colorClass: '' },
        compost: { height: 8, stability: 3, message: "רקבובית מעשירה את האדמה לגנים שופעים!", colorClass: '' },
        stones: { height: 3, stability: 30, message: "אבנים קטנות מוסיפות יציבות קריטית!", colorClass: 'warning' }
    };

    // Initial message state
     buildMessage.textContent = "נתחיל לבנות! גרור את קני הסוף ראשונים לבסיס יציב.";
     buildMessage.className = ''; // Reset class


    // Drag and Drop Handlers
    tools.forEach(tool => {
        tool.addEventListener('dragstart', (e) => {
            e.dataTransfer.setData('text/plain', e.target.dataset.material);
            e.target.classList.add('dragging'); // Not used visually yet, but good practice
             buildMessage.textContent = `משחרר את ${tool.querySelector('p').textContent}...`;
             buildMessage.className = '';
        });

        tool.addEventListener('dragend', (e) => {
            e.target.classList.remove('dragging');
             buildMessage.textContent = "גרור חומרים נוספים לבנייה!";
             buildMessage.className = '';
        });
    });

    chinampaArea.addEventListener('dragover', (e) => {
        e.preventDefault(); // Necessary to allow dropping
        chinampaArea.classList.add('drag-over'); // Visual feedback
    });

    chinampaArea.addEventListener('dragleave', (e) => {
        chinampaArea.classList.remove('drag-over');
    });

    chinampaArea.addEventListener('drop', (e) => {
        e.preventDefault();
        chinampaArea.classList.remove('drag-over');

        const material = e.dataTransfer.getData('text/plain');
        const effect = materialEffects[material];

        if (effect) {
            // Add visual layer
            const layer = document.createElement('div');
            layer.classList.add('chinampa-layer', `layer-${material}`);
            // Optional: make layer height proportional to its effect height, limited by min-height CSS
            // layer.style.minHeight = `${Math.max(10, effect.height * 1.5)}px`;
            chinampaLayers.appendChild(layer);

            // Update state based on effects
            currentHeight += effect.height;
            currentStability += effect.stability;

            // Cap values at max goal for display, allow slight overshoot for actual tracking if needed
            const displayHeight = Math.min(currentHeight, maxHeightNeeded);
            const displayStability = Math.min(currentStability, maxStabilityNeeded);

            const heightPercent = Math.min((currentHeight / maxHeightNeeded) * 100, 100);
            const stabilityPercent = Math.min((currentStability / maxStabilityNeeded) * 100, 100);


            // Update feedback bars
            heightBar.style.width = `${heightPercent}%`;
            stabilityBar.style.width = `${stabilityPercent}%`;

            heightText.textContent = `${Math.round(heightPercent)}%`;
            stabilityText.textContent = `${Math.round(stabilityPercent)}%`;

            // Change bar color based on progress towards goal
            heightBar.parentElement.classList.toggle('success', heightPercent >= 100);
             stabilityBar.parentElement.classList.toggle('success', stabilityPercent >= 100); // Or maybe warning if too low?

            // Adjust chinampa area height visually and water level
            // The chinampa grows *up* from the bottom. The water level visually drops relative to its base.
            const baseHeightPercent = 15; // Initial CSS height of chinampa-area
            const addedHeightPercent = (currentHeight / maxHeightNeeded) * 50; // How much it visually grows *relative* to lake area
            const newChinampaHeightCSS = Math.min(baseHeightPercent + addedHeightPercent, 90); // Don't grow out of lake area

            chinampaArea.style.height = `${newChinampaHeightCSS}%`;

            // Make water level appear lower relative to the structure bottom
            // The bottom of the chinampa-area stays at bottom: 0.
            // The height of the chinampa-area grows.
            // We want the water to seem to recede or the chinampa to emerge.
            // Let's keep water level fixed and show the chinampa rising relative to it.
            // No change to waterLevel height, just the chinampaArea height indicates progress.

             // Ensure chinampa area has layers class
             chinampaArea.classList.add('has-layers');


            // Update message
            buildMessage.textContent = effect.message;
            buildMessage.className = effect.colorClass; // Add specific class for message color/style


            // Check for completion
            if (currentHeight >= maxHeightNeeded && currentStability >= maxStabilityNeeded * 0.7) { // Needs reasonable stability too
                 buildMessage.textContent = "🎉 הצ'ינאמפה נראית יציבה ומוכנה לשתילה!";
                 buildMessage.className = 'success';
                 completionOverlay.classList.remove('hidden'); // Show completion effect
                 // Disable dragging after completion?
                 tools.forEach(tool => tool.draggable = false);
            } else if (currentHeight >= maxHeightNeeded * 0.8 && currentStability < maxStabilityNeeded * 0.7) {
                 buildMessage.textContent = "הצ'ינאמפה כמעט בגובה, אבל חסרה לה יציבות!";
                 buildMessage.className = 'warning';
            } else if (currentStability >= maxStabilityNeeded * 0.8 && currentHeight < maxHeightNeeded * 0.7) {
                  buildMessage.textContent = "הצ'ינאמפה יציבה מאוד, אבל עדיין נמוכה מדי!";
                  buildMessage.className = 'warning';
            } else if (currentHeight > maxHeightNeeded || currentStability > maxStabilityNeeded) {
                // Gentle encouragement if not yet perfect
                buildMessage.textContent = effect.message + " ממשיכים לבנות...";
                 buildMessage.className = '';
            }
        }
    });

    // Explanation toggle functionality
    const toggleButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר' : 'רוצים לדעת עוד על צ'ינאמפס?';
        // Optional: scroll to explanation if shown
        if (!isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});
</script>
```