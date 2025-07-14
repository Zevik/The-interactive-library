---
title: "המצפן החי: מסע בעקבות המפה המגנטית הנסתרת של כדור הארץ"
english_slug: the-living-compass-navigating-earths-hidden-magnetic-map
category: "ביולוגיה"
tags: נדידה, בעלי חיים, שדה מגנטי, מגנטוצפציה, ניווט ביולוגי, סימולציה, אינטראקטיבי
---
# המצפן החי: מסע בעקבות המפה המגנטית הנסתרת של כדור הארץ

דמיינו צב ים צעיר שבוקע מביצתו על חוף בפלורידה. שנים אחר כך, אחרי מסע של אלפי קילומטרים באוקיינוס העצום, הוא חוזר בדיוק לאותו חוף כדי להטיל את ביציו שלו. או חשבו על ציפור קטנה שחוצה יבשות בלילה מעונן. איך הם עושים את זה? סוד הניווט המופלא שלהם טמון ביכולת לחש את השדה המגנטי של כדור הארץ – חוש נסתר שפועל כמעין GPS טבעי! בואו נצלול לעולם המדהים של הניווט המגנטי ונראה איך בעלי חיים "קוראים" את מפת כדור הארץ הנסתרת.

<div id="app-container">
    <h2 id="simulation-title">התנסות: ניווט על מפה מגנטית מופשטת</h2>
    <p id="simulation-intro">על המפה המופשטת הזו תראו קווים אפורים שמייצגים "עוצמה" (דמיינו שהעוצמה עולה ככל שיורדים למטה) וקווים ירוקים שמייצגים "זווית הטיה" (דמיינו שהזווית עולה ככל שזזים ימינה). לחצו על המפה לבחירת נקודת התחלה כחולה (היכן שהציפור מתחילה) ונקודת יעד אדומה.</p>
    <canvas id="magnetic-map-canvas" width="700" height="450"></canvas>
    <div id="controls">
        <button id="start-migration" disabled>צא למסע!</button>
        <button id="reset-map">התחל מחדש</button>
         <button id="randomize-position" disabled>הסט מהמסלול ובדוק תיקון!</button>
    </div>
     <div id="status-area">
        <p id="status"></p>
        <div id="animal-perception"></div>
    </div>
    <div id="legend">
        <p><b>מקרא מפה:</b></p>
        <p><span class="legend-line intensity"></span> קווי "עוצמה" (עולה כלפי מטה)</p>
        <p><span class="legend-line inclination"></span> קווי "זווית הטיה" (עולה ימינה)</p>
        <p><span class="legend-point blue"></span> נקודת התחלה</p>
        <p><span class="legend-point red"></span> יעד</p>
        <p><span class="legend-animal">🐦</span> בעל החיים הנודד</p>
    </div>
</div>

<style>
    body {
        font-family: 'Arial', sans-serif; /* Use a common, clean font */
        line-height: 1.6;
        margin: 0;
        padding: 0; /* Adjust padding on container instead */
        background-color: #f4f7f6; /* Light background */
        color: #333;
    }
    h1 {
        color: #1a5276; /* Deep blue */
        text-align: center;
        margin-top: 20px;
        font-size: 2em;
    }
     h2 {
        color: #229954; /* Greenish */
        margin-top: 15px;
        border-bottom: 1px solid #eee;
        padding-bottom: 5px;
    }
     h3 {
        color: #5d6d7e; /* Grayish blue */
        margin-top: 10px;
    }

    #app-container {
        background-color: #ffffff; /* White background for the app */
        padding: 30px;
        border-radius: 12px; /* Rounded corners */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1); /* Softer shadow */
        max-width: 750px; /* Limit container width */
        margin: 30px auto; /* Center the container */
        text-align: center;
    }

    #simulation-title {
        text-align: center;
        color: #1a5276;
        margin-bottom: 15px;
    }
    #simulation-intro {
        text-align: center;
        margin-bottom: 20px;
        color: #555;
    }

    #magnetic-map-canvas {
        cursor: crosshair;
        display: block;
        margin: 0 auto;
        border: 1px solid #dcdcdc; /* Lighter border */
        background-color: #eef7ff; /* Very light blue background */
        border-radius: 8px; /* Match container border-radius */
        box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.05); /* Subtle inner shadow */
    }

    #controls {
        margin-top: 20px;
        display: flex; /* Use flexbox for button layout */
        justify-content: center; /* Center buttons */
        gap: 15px; /* Space between buttons */
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
    }

    #controls button {
        padding: 12px 20px; /* More padding */
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 6px; /* Slightly more rounded buttons */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transitions */
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Button shadow */
    }

    #start-migration {
         background-color: #28a745; /* Green */
    }
    #start-migration:hover:not(:disabled) {
         background-color: #218838; /* Darker green */
         transform: translateY(-1px); /* Slight lift effect */
    }

    #reset-map {
         background-color: #dc3545; /* Red */
    }
     #reset-map:hover:not(:disabled) {
        background-color: #c82333; /* Darker red */
        transform: translateY(-1px);
    }

    #randomize-position {
         background-color: #ffc107; /* Yellow/Orange */
         color: #333; /* Dark text for contrast */
    }
     #randomize-position:hover:not(:disabled) {
        background-color: #e0a800; /* Darker yellow */
         transform: translateY(-1px);
    }


     #controls button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        box-shadow: none; /* No shadow when disabled */
        transform: none;
    }

    #status-area {
        margin-top: 20px;
        min-height: 2em; /* Reserve space */
        font-size: 1.1em;
        color: #555;
        text-align: center; /* Center status text */
        display: flex; /* Layout status and perception side by side */
        justify-content: center;
        align-items: center;
        flex-wrap: wrap; /* Allow wrapping */
        gap: 15px; /* Space between status and perception */
    }

     #status {
         margin: 0; /* Remove default margin */
     }

     #animal-perception {
         font-size: 0.9em;
         color: #666;
         /* Removed border/background to integrate better */
     }

    #legend {
        text-align: left;
        margin-top: 25px;
        padding: 15px;
        background-color: #f9f9f9; /* Light background for legend */
        border-radius: 8px;
        border: 1px solid #eee; /* Light border */
        display: inline-block; /* Fit width to content */
         max-width: 100%; /* Prevent overflow */
         text-align: right; /* Align legend text right for Hebrew */
    }

    #legend p {
        margin: 5px 0; /* Space out legend items */
        display: flex; /* Use flex for alignment */
        align-items: center;
        justify-content: flex-end; /* Align items to the right */
    }

     #legend b {
        margin-left: 10px; /* Space after bold title */
     }

    .legend-line {
        display: inline-block;
        width: 30px;
        height: 2px;
        margin-left: 8px; /* Space between line and text */
        vertical-align: middle;
    }
    .legend-line.intensity {
        background-color: gray;
    }
    .legend-line.inclination {
        background-color: darkgreen;
    }

    .legend-point {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        margin-left: 8px;
        vertical-align: middle;
    }
    .legend-point.blue {
        background-color: blue;
    }
    .legend-point.red {
        background-color: red;
    }
     .legend-animal {
         font-size: 24px; /* Keep animal icon large */
         vertical-align: middle;
         line-height: 1; /* Adjust line height for alignment */
         margin-left: 8px;
     }


    #toggle-explanation {
         display: block;
         margin: 25px auto; /* Space above and center */
         padding: 14px 22px; /* More padding */
         font-size: 1.1em;
         cursor: pointer;
         border: none;
         border-radius: 6px;
         background-color: #007bff; /* Blue */
         color: white;
         transition: background-color 0.3s ease, transform 0.1s ease;
         font-weight: bold;
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
     #toggle-explanation:hover {
        background-color: #0056b3; /* Darker blue */
         transform: translateY(-1px);
    }

    #explanation {
        display: none; /* Initially hidden */
        margin-top: 20px;
        padding: 30px; /* More padding */
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
         text-align: right; /* Align text right for Hebrew */
    }

    #explanation h2 {
        color: #1a5276;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px; /* More padding */
        margin-top: 0; /* Remove top margin from first h2 */
        margin-bottom: 15px;
    }
     #explanation h3 {
        color: #229954;
        margin-top: 20px; /* Space above */
        margin-bottom: 10px;
     }


    #explanation p {
        margin-bottom: 15px; /* Space out paragraphs */
        color: #444;
    }
    #explanation ul {
        list-style: disc outside; /* Disc bullets, outside the margin */
        padding-right: 25px; /* Padding for bullets (right for Hebrew) */
        margin-bottom: 15px;
    }
     #explanation ul li {
         margin-bottom: 8px; /* Space out list items */
     }

</style>

<button id="toggle-explanation">הצגת הסבר מורחב: איך המפה המגנטית עובדת?</button>

<div id="explanation">
    <h2>הסבר מורחב: הניווט המגנטי - המפה הנסתרת</h2>

    <h3>מסע חיים: מהי נדידה ומדוע בעלי חיים יוצאים אליה?</h3>
    <p>נדידה היא מסע עונתי מתוזמן של בעלי חיים, שמטרתו לרוב למצוא תנאים טובים יותר להישרדות ולהתרבות. ציפורים עפות לאקלים חם יותר בחורף, צבי ים חוזרים להטיל ביצים בחוף הולדתם, ודגים שוחים למרחקים כדי להגיע לאזורי הטלה מתאימים. זוהי תופעה מדהימה, המצריכה יכולות ניווט יוצאות דופן על פני מרחקים עצומים.</p>

    <h3>האתגר הגדול: איך מוצאים את הדרך ללא GPS?</h3>
    <p>בעלי חיים נודדים חייבים לנווט במדויק כדי לשרוד. הם לא יכולים פשוט לשאול לכיוון או להשתמש בסמארטפון. המחקר גילה שבעלי חיים רבים נעזרים במגוון רמזים סביבתיים: מיקום השמש והכוכבים, ריחות מוכרים, תוואי קרקע, ואפילו שדות חשמליים. אבל אחד הכלים המסתוריים והמרתקים ביותר הוא החוש המגנטי.</p>

    <h3>כדור הארץ כמגנט ענק: הכירו את השדה המגנטי</h3>
    <p>ליבת כדור הארץ הברזלית יוצרת שדה מגנטי עצום המקיף את הכוכב. השדה הזה אינו אחיד, ויש לו שני מאפיינים עיקריים שמשתנים ממיקום למיקום, ויוצרים למעשה 'מפה' ייחודית:</p>
    <ul>
        <li><strong>עוצמת השדה (Intensity):</strong> השדה חזק יותר בקטבים וחלש יותר בקו המשווה. שינויים גיאולוגיים יכולים גם הם להשפיע מקומית על העוצמה.</li>
        <li><strong>זווית ההטיה (Inclination / Dip Angle):</strong> זו הזווית שבה קווי השדה המגנטי "צוללים" אל תוך האדמה. בקו המשווה הם כמעט מקבילים לקרקע (זווית אפס), ובקטבים הם כמעט מאונכים לקרקע (זווית 90 מעלות).</li>
    </ul>
    <p>דמיינו שהמפה שראיתם בסימולציה היא ייצוג מופשט של השדה המגנטי: קווי העוצמה הם הקווים האפורים האופקיים (דמיינו שעוצמה גבוהה יותר ככל שיורדים למטה), וקווי זווית ההטיה הם הקווים הירוקים האנכיים (דמיינו שזווית הטיה גבוהה יותר ככל שזזים ימינה). כל נקודה על המפה מוגדרת על ידי שילוב ייחודי של "עוצמה" ו"זווית הטיה".</p>

    <h3>החוש המגנטי: איך בעלי חיים מרגישים את השדה?</h3>
    <p>'מגנטוצפציה' היא היכולת לחוש את השדה המגנטי. עדיין לא ברור לחלוטין איך זה עובד בכל בעלי החיים, אך קיימות שתי השערות עיקריות:</p>
    <ul>
        <li><strong>מנגנון כימי בעיניים:</strong> אצל ציפורים ובעלי חיים אחרים, חלבונים מסוימים ברשתית העין רגישים לאור ולשדה המגנטי. הם עשויים לפעול כמעין מצפן, שמאפשר לבעל החיים לזהות את כיוון השדה (כלומר, צפון/דרום מגנטי).</li>
        <li><strong>קולטנים מבוססי ברזל:</strong> ייתכן שלבעלי חיים מסוימים (כמו צבי ים, דגים, ואף יונקים) יש גבישי ברזל מיקרוסקופיים ברקמות שונות (למשל באף או במוח). גבישים אלו מסתדרים בהתאם לשדה המגנטי, והתנועה שלהם מפעילה קולטנים עצביים שמאפשרים לחוש הן את כיוון השדה והן את עוצמתו.</li>
    </ul>

    <h3>מהמצפן למפה: ניווט באמצעות קואורדינטות מגנטיות</h3>
    <p>בעלי חיים מסוימים, כמו ציפורים, עשויים להשתמש בשדה המגנטי בעיקר כ"מצפן" - כדי לדעת מהו הכיוון היחסי (צפון, דרום, מזרח, מערב) ולשמור על קו נדידה ישר.</p>
    <p>אבל בעלי חיים אחרים, כמו צבי ים, זקוקים למערכת ניווט מדויקת יותר שמאפשרת להם לחזור לנקודה ספציפית. כאן נכנסת לתמונה יכולת השימוש בשדה המגנטי כ"מפה". ההשערה המובילה היא שהם קולטים את השילוב הייחודי של עוצמת השדה וזווית ההטיה במיקומם הנוכחי, ומשווים אותו ל"חתימה המגנטית" של אזור היעד שלהם (אותה למדו אולי בזמן מסע קודם או שירשו). בדומה לסימולציה שראיתם, אם בעל החיים חש "עוצמה" גבוהה יותר ממה שיש ביעד, הוא "יידע" שעליו לזוז לכיוון אזורים עם עוצמה נמוכה יותר, וכן הלאה עבור זווית ההטיה. שילוב של שני הפרמטרים הללו מאפשר לו לנווט על המפה המגנטית עד שיגיע לאזור עם "הקואורדינטות המגנטיות" של היעד.</p>

    <h3>הניסויים המדהימים שחשפו את הסוד</h3>
    <p>כיצד יודעים כל זאת? ניסויים גאוניים! במעבדות מחקר, מדענים יכולים להציב בעלי חיים (כמו צבי ים קטנים או ציפורים בכלובים) בתוך סלילים מגנטיים המאפשרים שליטה מלאה על השדה המגנטי שהם חשים. כאשר המדענים מדמים שדות מגנטיים התואמים אזורים שונים על פני כדור הארץ, בעלי החיים מכוונים את שחייתם או תנועתם בכיוון הנכון, כאילו הם באמת נמצאים באותם אזורים. ניסויים כאלה, יחד עם הצמדת מגנטים קטנים או שיבוש השדה, מספקים הוכחות חותכות ליכולת הניווט המגנטי.</p>

    <h3>שילוב כוחות: השדה המגנטי ועזרים נוספים</h3>
    <p>חשוב לזכור שהשדה המגנטי הוא כנראה רק כלי אחד מתוך ארגז כלים עשיר של בעלי חיים נודדים. הם משלבים את המידע המגנטי עם ניווט לפי שמש וכוכבים (במיוחד כשרואים אותם), ריחות, קולות, ומראה של תוואי שטח. שילוב זה הופך את מערכת הניווט שלהם לאמינה ועמידה, ומאפשר להם להשלים מסעות מדהימים שאנו רק מתחילים להבין.</p>
</div>

<script>
    const canvas = document.getElementById('magnetic-map-canvas');
    const ctx = canvas.getContext('2d');
    const startMigrationBtn = document.getElementById('start-migration');
    const resetMapBtn = document.getElementById('reset-map');
    const randomizePositionBtn = document.getElementById('randomize-position');
    const statusDiv = document.getElementById('status');
    const animalPerceptionDiv = document.getElementById('animal-perception'); // New element for perception info
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    let startPoint = null;
    let endPoint = null;
    let animalPosition = null;
    let animationFrameId = null;
    const animationSpeed = 0.8; // Pixels per animation frame step (adjust for speed)
    let isMigrationActive = false;
    let isRandomized = false; // Flag indicates if the animal was randomized

    // --- Magnetic Field Model (Simplified) ---
    // Intensity increases linearly from top (0) to bottom (canvas.height)
    // Inclination increases linearly from left (0) to right (canvas.width)
    function getMagneticField(x, y) {
        // Normalize x and y to range [0, 1]
        const normX = x / canvas.width;
        const normY = y / canvas.height;
        // Scale to desired range for simulation, e.g., Intensity 0-1, Inclination 0-1
        const intensity = normY; // 0 at top, 1 at bottom
        const inclination = normX; // 0 at left, 1 at right
        return { intensity, inclination };
    }

    function drawMagneticField() {
        // Draw Intensity lines (gray)
        ctx.strokeStyle = 'rgba(128, 128, 128, 0.4)'; // Slightly more transparent
        ctx.lineWidth = 1;
        const intensityLines = 15; // More lines for denser feel
        for (let i = 0; i <= intensityLines; i++) {
            const y = (canvas.height / intensityLines) * i;
            ctx.beginPath();
            ctx.moveTo(0, y);
            ctx.lineTo(canvas.width, y);
            ctx.stroke();
        }

        // Draw Inclination lines (darkgreen)
        ctx.strokeStyle = 'rgba(0, 100, 0, 0.4)'; // Slightly more transparent
        ctx.lineWidth = 1;
        const inclinationLines = 20; // More lines
        for (let i = 0; i <= inclinationLines; i++) {
            const x = (canvas.width / inclinationLines) * i;
             ctx.beginPath();
            ctx.moveTo(x, 0);
            ctx.lineTo(x, canvas.height);
            ctx.stroke();
        }

        // Optional: Add subtle animation/pulsing to lines (complex, maybe skip for v1)
    }

    function drawMap() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#eef7ff'; // Very light blue background
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        drawMagneticField();

        if (startPoint) {
            drawPoint(startPoint, 'blue', 'התחלה');
        }
        if (endPoint) {
            drawPoint(endPoint, 'red', 'יעד');
        }
        if (animalPosition) {
             drawAnimal(animalPosition);
             updateAnimalPerception(); // Update perceived field info
        } else {
            animalPerceptionDiv.textContent = ''; // Clear perception info if no animal
        }
    }

    function drawPoint(point, color, text) {
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.arc(point.x, point.y, 7, 0, Math.PI * 2); // Slightly larger points
        ctx.fill();
        // Add text label
        ctx.fillStyle = '#333';
        ctx.font = '13px sans-serif'; // Slightly larger font
        ctx.textAlign = 'center';
        ctx.textBaseline = 'bottom';
        ctx.fillText(text, point.x, point.y - 10); // Position label higher
    }

    function drawAnimal(position) {
        ctx.font = '30px sans-serif'; // Larger animal icon
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        // Add a subtle animation effect (e.g., scaling)
        const scale = 1 + Math.sin(Date.now() / 300) * 0.05; // Pulsing effect
        ctx.save(); // Save current context state
        ctx.translate(position.x, position.y); // Move origin to animal position
        ctx.scale(scale, scale); // Apply scaling
        ctx.fillText('🐦', 0, 0); // Draw animal at new origin
        ctx.restore(); // Restore context state
    }

    function updateAnimalPerception() {
         if (!animalPosition || !endPoint) {
             animalPerceptionDiv.textContent = '';
             return;
         }
        const currentField = getMagneticField(animalPosition.x, animalPosition.y);
        const targetField = getMagneticField(endPoint.x, endPoint.y);

        // Format values for display
        const currentInt = currentField.intensity.toFixed(2);
        const currentInc = currentField.inclination.toFixed(2);
        const targetInt = targetField.intensity.toFixed(2);
        const targetInc = targetField.inclination.toFixed(2);

        // Use colors/indicators to show direction needed
        let intIndicator = '';
        if (currentField.intensity < targetField.intensity - 0.01) intIndicator = '↓'; // Needs more intensity (down)
        else if (currentField.intensity > targetField.intensity + 0.01) intIndicator = '↑'; // Needs less intensity (up)
        else intIndicator = '✅'; // Close enough

         let incIndicator = '';
        if (currentField.inclination < targetField.inclination - 0.01) incIndicator = '→'; // Needs more inclination (right)
        else if (currentField.inclination > targetField.inclination + 0.01) incIndicator = '←'; // Needs less inclination (left)
        else incIndicator = '✅'; // Close enough


         animalPerceptionDiv.innerHTML = `<b>בעל החיים חש:</b> עוצמה ${currentInt} ${intIndicator}, הטיה ${currentInc} ${incIndicator}<br><b>יעד חש:</b> עוצמה ${targetInt}, הטיה ${targetInc}`;
    }


    function distance(p1, p2) {
        return Math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2);
    }

    function migrate() {
        if (!animalPosition || !endPoint) {
            isMigrationActive = false;
            statusDiv.textContent = 'חסרה נקודת יעד או מיקום בעל חיים.';
            return;
        }

        const currentDistance = distance(animalPosition, endPoint);

        if (currentDistance < 10) { // Use a small threshold to snap to the target
            animalPosition = {...endPoint}; // Snap to end point
            statusDiv.textContent = isRandomized ? 'הידד! בעל החיים מצא את דרכו חזרה ליעד!' : 'הידד! בעל החיים הגיע ליעד!';
            isMigrationActive = false;
            isRandomized = false; // Reset randomize flag after reaching goal
            randomizePositionBtn.disabled = false; // Enable randomize after completion
            startMigrationBtn.disabled = true; // Disable start until new points or randomize
            drawMap(); // Final draw at destination
            return;
        }


        // --- Improved Field-Based Navigation Logic ---
        const currentField = getMagneticField(animalPosition.x, animalPosition.y);
        const targetField = getMagneticField(endPoint.x, endPoint.y);

        let dx = 0;
        let dy = 0;

        // Determine desired movement based on magnetic field difference
        // This simulates the animal trying to move towards the area with the target field values.
        const fieldTolerance = 0.01; // How close field values need to be to count as 'matching'

        // Movement component based on Intensity difference
        if (currentField.intensity < targetField.intensity - fieldTolerance) dy += 1; // Need more intensity -> move down
        else if (currentField.intensity > targetField.intensity + fieldTolerance) dy -= 1; // Need less intensity -> move up

        // Movement component based on Inclination difference
        if (currentField.inclination < targetField.inclination - fieldTolerance) dx += 1; // Need more inclination -> move right
        else if (currentField.inclination > targetField.inclination + fieldTolerance) dx -= 1; // Need less inclination -> move left

        // Combine field-based movement with a weak pull towards the actual destination point
        // The direct pull ensures the animal eventually reaches the exact point and doesn't get stuck
        // if the field navigation alone isn't precise enough (e.g., on plateaus).
        const directPullStrength = 0.01; // Adjust this value to control direct pull influence
        dx += (endPoint.x - animalPosition.x) * directPullStrength;
        dy += (endPoint.y - animalPosition.y) * directPullStrength;


        // Normalize the combined movement vector and scale by speed
        const magnitude = Math.sqrt(dx*dx + dy*dy);
        const stepX = (magnitude > 0) ? (dx / magnitude) * animationSpeed : 0;
        const stepY = (magnitude > 0) ? (dy / magnitude) * animationSpeed : 0;

        // Ensure step size doesn't overshoot the target
        const actualStepDistance = Math.min(animationSpeed, currentDistance);
        const scaleFactor = actualStepDistance / animationSpeed;

        animalPosition.x += stepX * scaleFactor;
        animalPosition.y += stepY * scaleFactor;

        // Prevent animal from leaving the canvas (edge bouncing not modeled)
        animalPosition.x = Math.max(0, Math.min(canvas.width, animalPosition.x));
        animalPosition.y = Math.max(0, Math.min(canvas.height, animalPosition.y));


        drawMap(); // Redraw map with updated animal position
        if (isMigrationActive) {
            animationFrameId = requestAnimationFrame(migrate); // Continue animation loop
        }
    }

    function startMigration() {
        if (!startPoint || !endPoint) {
            statusDiv.textContent = 'אנא בחר נקודת התחלה ויעד על המפה.';
            return;
        }
        if (isMigrationActive) return; // Prevent multiple animations

        // If starting a new migration from chosen start/end, or after reset
        if (!isRandomized) {
           animalPosition = {...startPoint}; // Start animal at the chosen start point
        }
        // If randomized, animalPosition is already set randomly, we just start the migration logic

        isMigrationActive = true;
        randomizePositionBtn.disabled = true; // Disable randomize during migration
        startMigrationBtn.disabled = true; // Disable start button while migrating
        statusDiv.textContent = isRandomized ? 'בעל החיים מנסה לתקן את המסלול באמצעות השדה המגנטי...' : 'המסע החל! בעל החיים מנווט ליעד...';
        drawMap(); // Draw initial state
        animationFrameId = requestAnimationFrame(migrate); // Start animation
    }

    function resetMap() {
        cancelAnimationFrame(animationFrameId); // Stop any active animation
        isMigrationActive = false;
        startPoint = null;
        endPoint = null;
        animalPosition = null;
        isRandomized = false;
        randomizePositionBtn.disabled = true;
        startMigrationBtn.disabled = true; // Disable start until points are chosen again
        statusDiv.textContent = 'המפה אופסה. לחץ על המפה לבחירת נקודת התחלה כחולה.';
        animalPerceptionDiv.textContent = ''; // Clear perception info
        drawMap();
    }

    function randomizePosition() {
        // Can only randomize if a migration just finished successfully
        if (!animalPosition || distance(animalPosition, endPoint) > 10 || isMigrationActive) return;

         // Move animal to a random position within the canvas (away from start/end)
         let newX, newY;
         const minDistance = 80; // Minimum distance from start/end points
         do {
            newX = Math.random() * canvas.width;
            newY = Math.random() * canvas.height;
         } while ((startPoint && distance({x: newX, y: newY}, startPoint) < minDistance) || (endPoint && distance({x: newX, y: newY}, endPoint) < minDistance));

         animalPosition.x = newX;
         animalPosition.y = newY;

         isRandomized = true; // Mark that the animal was randomized
         statusDiv.textContent = 'אופס! בעל החיים הוסט ממסלולו! לחץ "צא למסע!" שוב כדי לראות איך הוא מתקן מסלול.';
         randomizePositionBtn.disabled = true; // Disable until next correction finishes

         // Re-enable start button for the correction run
         startMigrationBtn.disabled = false;

         drawMap(); // Draw animal in the new random position
    }


    canvas.addEventListener('click', (event) => {
        if (isMigrationActive) {
             statusDiv.textContent = 'המתן שהמסע יסתיים לפני שינוי נקודות.';
             return; // Don't change points during migration
        }

        const rect = canvas.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;

        if (!startPoint) {
            startPoint = { x: x, y: y };
            animalPosition = { x: x, y: y }; // Set initial animal pos
            statusDiv.textContent = 'נקודת התחלה נבחרה. כעת לחץ על המפה לבחירת יעד אדום.';
        } else if (!endPoint) {
            endPoint = { x: x, y: y };
            statusDiv.textContent = 'יעד נבחר. לחץ על "צא למסע!" להתחיל בניווט.';
            startMigrationBtn.disabled = false; // Enable start button
        } else {
             // If both set, clicking again resets and allows picking a new start
             resetMap(); // Reset everything and start over
             startPoint = { x: x, y: y };
             animalPosition = { x: x, y: y };
             statusDiv.textContent = 'נקודת התחלה חדשה נבחרה. כעת לחץ על המפה לבחירת יעד אדום.';
        }
        drawMap(); // Redraw map after point selection
    });

    startMigrationBtn.addEventListener('click', startMigration);
    resetMapBtn.addEventListener('click', resetMap);
    randomizePositionBtn.addEventListener('click', randomizePosition);


    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מורחב' : 'הצגת הסבר מורחב: איך המפה המגנטית עובדת?';
    });


    // Initial setup on page load
    startMigrationBtn.disabled = true; // Disable start until points are chosen
    randomizePositionBtn.disabled = true; // Disable randomize until after first migration
    drawMap();
    statusDiv.textContent = 'ברוכים הבאים! לחץ על המפה לבחירת נקודת התחלה כחולה.';

</script>
---