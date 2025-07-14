---
title: "מרדפים אחרי השמש: סימולציית היתוך בטוקמק"
english_slug: chasing-the-sun-tokamak-fusion-simulation
category: "פיזיקה"
tags:
  - כור היתוך גרעיני
  - טוקמק
  - היתוך גרעיני
  - פלזמה
  - שדות מגנטיים
  - אנרגיה נקייה
---
# מרדפים אחרי השמש: סימולציית היתוך בטוקמק

דמיינו עתיד שבו אנרגיה נקייה, כמעט בלתי נדלית, מאירה את חיינו. היתוך גרעיני – הכוח שמניע את השמש – הוא המפתח לחזון הזה. אבל איך אפשר לרתום את הכוח העצום הזה כאן, על כדור הארץ? בואו לצלול לתוך הלב של טכנולוגיית הטוקמק ולגלות את הריקוד העדין בין שדות מגנטיים לפלזמה לוהטת!

<div class="app-container">
    <div class="simulation-area">
        <canvas id="tokamakCanvas"></canvas>
        <div class="status-display"><span id="plasmaStatus">מאתחל...</span></div>
    </div>
    <div class="controls-panel">
        <h3 class="controls-title">כווננו את השדות המגנטיים</h3>
        <div class="control-group">
            <label for="toroidalField">שדה מגנטי טורואידי (Bt):</label>
            <input type="range" id="toroidalField" min="10" max="100" value="50" step="1">
            <span id="toroidalValue" class="value-display">50</span> יחידות
        </div>
        <div class="control-group">
            <label for="plasmaCurrent">זרם בפלזמה (Ip - יוצר שדה פולואידי):</label>
            <input type="range" id="plasmaCurrent" min="10" max="100" value="50" step="1">
            <span id="plasmaCurrentValue" class="value-display">50</span> יחידות
        </div>
        <p class="hint">שנו את עוצמות השדות כדי לראות כיצד הן שומרות (או לא שומרות) על הפלזמה כלואה ויציבה. מצאו את הטווח המושלם!</p>
    </div>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --primary-hover-color: #0056b3;
        --background-color: #f4f7f6;
        --card-background: #ffffff;
        --border-color: #dcdcdc;
        --text-color: #333;
        --secondary-text-color: #555;
        --stable-color: #28a745; /* Green */
        --unstable-color: #dc3545; /* Red */
        --warning-color: #ffc107; /* Orange/Yellow */
        --canvas-bg: #1a1a2e; /* Dark background for space/plasma feel */
        --tokamak-outline: #4a4e69; /* Dark greyish blue */
        --plasma-stable: rgba(0, 255, 255, 0.8); /* Cyan */
        --plasma-unstable: rgba(255, 100, 0, 0.7); /* Orange */
        --particle-color-stable: rgba(0, 255, 255, 0.9);
        --particle-color-unstable: rgba(255, 200, 0, 0.8);
    }

    .app-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 30px;
        gap: 30px;
        font-family: 'Arial', sans-serif;
        color: var(--text-color);
        background-color: var(--background-color);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    }

    .simulation-area {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        max-width: 550px;
        background-color: var(--canvas-bg);
        border-radius: 8px;
        overflow: hidden; /* Ensures canvas doesn't overflow rounded corners */
        box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.3);
        position: relative;
    }

    #tokamakCanvas {
        width: 100%;
        max-width: 550px;
        height: 350px; /* Increased height */
        display: block; /* Remove extra space below canvas */
    }

    .status-display {
        margin: 15px 0;
        font-size: 1.2em;
        font-weight: bold;
        color: var(--warning-color); /* Initial color */
        text-align: center;
        width: 100%;
    }

    .status-display span {
         transition: color 0.5s ease;
    }

    .controls-panel {
        background-color: var(--card-background);
        padding: 20px;
        border-radius: 8px;
        width: 100%;
        max-width: 550px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }

    .controls-panel .controls-title {
        text-align: center;
        margin-bottom: 20px;
        color: var(--primary-color);
    }

    .control-group {
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        flex-wrap: wrap; /* Allow wrapping on small screens */
        gap: 10px; /* Space between elements */
    }

    .control-group label {
        flex: 1 1 150px; /* Grow and shrink, minimum 150px width */
        font-weight: bold;
        color: var(--secondary-text-color);
    }

    .control-group input[type="range"] {
        flex: 2 1 200px; /* Grow faster, minimum 200px width */
        -webkit-appearance: none;
        width: auto; /* Override width: 100% from original */
        height: 8px;
        background: #ddd;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 4px;
    }

    .control-group input[type="range"]:hover {
        opacity: 1;
    }

    .control-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid var(--card-background);
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

     .control-group input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid var(--card-background);
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }


    .control-group .value-display {
        flex: 0 0 40px; /* Fixed width */
        text-align: right;
        font-weight: bold;
        color: var(--text-color);
    }


    .hint {
        font-size: 0.95em;
        color: var(--secondary-text-color);
        margin-top: 15px;
        text-align: center;
        padding-top: 15px;
        border-top: 1px dashed var(--border-color);
    }

    #explanationButton {
        margin-top: 20px;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        background-color: var(--primary-color);
        color: white;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    #explanationButton:hover {
        background-color: var(--primary-hover-color);
    }
    #explanationButton:active {
         transform: scale(0.98);
    }

    #explanation {
        margin-top: 30px;
        padding: 25px;
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        max-width: 800px;
        width: 100%;
        text-align: right;
        direction: rtl;
        line-height: 1.7;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }
    #explanation h2 {
        text-align: center;
        margin-bottom: 20px;
        color: var(--primary-color);
        font-size: 1.8em;
    }
    #explanation h3 {
        margin-top: 20px;
        margin-bottom: 10px;
        color: var(--secondary-text-color);
        font-size: 1.3em;
    }
    #explanation p {
        margin-bottom: 15px;
    }
    #explanation ul {
        margin-bottom: 15px;
        padding-right: 25px;
        list-style-type: disc;
    }
    #explanation li {
        margin-bottom: 8px;
    }
</style>

<button id="explanationButton">הצג/הסתר הסבר מקיף על טוקמקים והיתוך</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: חוקרים את ליבת הכוח - היתוך גרעיני וטוקמקים</h2>

    <h3>המסע אל אנרגיית הכוכבים</h3>
    <p>היתוך גרעיני הוא התהליך המרהיב שבו גרעיני אטומים קלים מתמזגים ליצירת גרעין כבד יותר, תוך שחרור כמות אדירה של אנרגיה. זהו ה"מנוע" של השמש ושל אינספור כוכבים ברחבי היקום. על כדור הארץ, אנו שואפים לשחזר תהליך זה, לרוב באמצעות מיזוג איזוטופים של מימן כמו דאוטריום וטריטיום, כדי ליצור מקור אנרגיה נקי, בטוח וכמעט בלתי נדלה שיחליף דלקי מאובנים מזהמים.</p>

    <h3>האתגרים הגדולים: חום וכליאה</h3>
    <p>כדי לגרום לגרעינים חיוביים להתמזג, יש להתגבר על הדחייה החשמלית האדירה ביניהם. זה דורש תנאים קיצוניים:</p>
    <ul>
        <li>**טמפרטורות סופר-לוהטות:** מיליוני מעלות צלזיוס – חמות בהרבה מליבת השמש עצמה! בטמפרטורות אלו, החומר הופך לפלזמה: מצב צבירה רביעי, שבו האלקטרונים נפרדים מהגרעינים והחומר הופך לגז מיונן של חלקיקים טעונים חשמלית.</li>
        <li>**הבעיה הפיזית:** שום חומר רגיל לא יכול להכיל פלזמה בטמפרטורות כאלה. כל מגע עם דפנות הכור יקרר אותה מיידית ויעצור את ההיתוך. הפתרון? להחזיק את הפלזמה "באוויר", הרחק מהדפנות.</li>
    </ul>

    <h3>הפתרון המגנטי: בקבוק בלי דפנות</h3>
    <p>הטבע המיונן של הפלזמה מאפשר לנו לרתום את כוחם של שדות מגנטיים. חלקיקים טעונים נעים לאורך קווי שדה מגנטי, וכך ניתן ליצור "בקבוק מגנטי" דמיוני שמכיל את הפלזמה הלוהטת.</p>

    <h3>טוקמק: המלכודת המגנטית המובילה</h3>
    <p>טוקמק (ראשי תיבות רוסיים: "לשכה טורואידית עם סלילים מגנטיים") הוא המבנה המבטיח ביותר לכליאת פלזמה למטרות היתוך. זהו כלי בצורת סופגנייה (טורוס).</p>
    <p>כדי ללכוד את הפלזמה בתוך הטורוס, הטוקמק משתמש בשני סוגי שדות מגנטיים עיקריים:</p>
    <ul>
        <li>**שדה טורואידי (Bt):** נוצר על ידי סלילים גדולים המקיפים את הטורוס מבחוץ. שדה זה חזק מאוד ומכוון לאורך "החור" של הסופגנייה, סביב הטבעת הגדולה. לבדו, הוא גורם לפלזמה להיסחף החוצה.</li>
        <li>**שדה פולואידי (Bp):** שדה המקיף את טבעת הפלזמה בצורה טבעתית קטנה יותר, בניצב לשדה הטורואידי. חלק מרכזי משדה זה נוצר על ידי זרם חשמלי חזק המושרה *בתוך* הפלזמה עצמה.</li>
    </ul>

    <h3>הסוד הוא ב"פיתול": יצירת השדה הסלילי</h3>
    <p>הקסם מתרחש כששני השדות משולבים. השדה הטורואידי הארוך והשדה הפולואידי הקצר יותר מתאחדים ליצירת שדה מגנטי כולל בעל צורה סלילית (הליקס). קווי השדה לא פשוט מקיפים את הטורוס, אלא מתפתלים סביבו, כמו קפיץ מלופף בתוך הסופגנייה.</p>
    <p>השדה הסלילי הזה הוא ה"בקבוק המגנטי" היציב. חלקיקי הפלזמה נעים לאורך הקווים המתפתלים, מה שמונע מהם לברוח במהירות החוצה או פנימה ולפגוע בדפנות. יציבות הכליאה הזו תלויה באופן קריטי ביחס המדויק בין עוצמת השדה הטורואידי לעוצמת השדה הפולואידי (שליטה בזרם הפלזמה היא אחת הדרכים לשלוט בשדה הפולואידי). יחס נכון יוצר "פיתול" אופטימלי ששומר על הפלזמה דחוסה במרכז הטורוס.</p>

    <h3>מציאת האיזון העדין</h3>
    <p>כפי שניתן לראות בסימולציה, שינוי עוצמות השדות משנה את יציבות הפלזמה. יחסים שאינם אופטימליים יכולים לגרום לפלזמה להפוך לטורבולנטית, להתנגש בדפנות, או פשוט להתפזר – כל אלה עוצרים את תהליך ההיתוך. המטרה היא למצוא את "חלון הפעולה" שבו השדות מאוזנים ומאפשרים לפלזמה להישאר כלואה ויציבה למשך זמן ארוך מספיק, בצפיפות ובטמפרטורה הנדרשות.</p>

    <h3>קריטריון לווסון: הדרך להצתה</h3>
    <p>כדי להשיג תהליך היתוך שמייצר יותר אנרגיה מזו שמושקעת בו (מצב הנקרא "הצתה"), יש לעמוד בשלושה תנאים בו זמנית, המכונים קריטריון לווסון:</p>
    <ul>
        <li>**צפיפות פלזמה גבוהה:** הרבה חלקיקים במקום קטן.</li>
        <li>**טמפרטורת פלזמה גבוהה מאוד:** החלקיקים נעים מהר מספיק להתנגשויות היתוך.</li>
        <li>**זמן כליאה מספיק:** שמירה על התנאים הללו למשך זמן מספק.</li>
    </ul>
    <p>טוקמקים מתוכננים להשיג את שלושת התנאים האלה. הצלחה בתחום זה היא אחד האתגרים המדעיים וההנדסיים הגדולים ביותר של זמננו.</p>

    <h3>העתיד כבר כאן: ITER ופרויקטים נוספים</h3>
    <p>פרויקטים בינלאומיים ענקיים כמו ITER (International Thermonuclear Experimental Reactor) הנבנה בצרפת, ממחישים את ההתקדמות בתחום. מטרתו של ITER היא להדגים הצתה בקנה מידה תעשייתי ולסלול את הדרך לבניית תחנות כוח היתוך עתידיות. במקביל, נחקרות טכנולוגיות כליאה מגנטית נוספות (כמו סטלארטורים) ושיטות היתוך אלטרנטיביות.</p>
    <p>מחקר ההיתוך הגרעיני הוא מרדף אחר האנרגיה האולטימטיבית – אנרגיה נקייה, בטוחה וכמעט אינסופית. הסימולציה שלפניכם היא הצצה קטנה אל הפיזיקה וההנדסה המורכבת שעומדת מאחורי המרדף המדעי המרגש הזה.</p>
</div>

<script>
    const canvas = document.getElementById('tokamakCanvas');
    const ctx = canvas.getContext('2d');
    const toroidalSlider = document.getElementById('toroidalField');
    const toroidalValueSpan = document.getElementById('toroidalValue');
    const plasmaSlider = document.getElementById('plasmaCurrent');
    const plasmaCurrentValueSpan = document.getElementById('plasmaCurrentValue');
    const plasmaStatusSpan = document.getElementById('plasmaStatus');
    const explanationButton = document.getElementById('explanationButton');
    const explanationDiv = document.getElementById('explanation');

    let animationFrameId;
    let particles = [];
    const numParticles = 200; // Increased particles for better visual
    const particleSize = 2;
    const particleSpeed = 0.5; // Base speed

    let centerX, centerY, outerRadius, innerRadius, plasmaRingRadius, plasmaAreaRadius;

    // Function to resize canvas based on container width
    function resizeCanvas() {
        const container = canvas.parentElement;
        canvas.width = container.clientWidth;
        canvas.height = container.clientHeight; // Use container height

        centerX = canvas.width / 2;
        centerY = canvas.height / 2;
        outerRadius = Math.min(canvas.width, canvas.height) * 0.35; // Adjusted radius
        innerRadius = outerRadius * 0.4; // Tokamak hole
        plasmaRingRadius = (outerRadius + innerRadius) / 2; // Center line of the plasma ring
        plasmaAreaRadius = (outerRadius - innerRadius) / 2 * 0.9; // Radius of the plasma cross-section area

        // Reinitialize particles on resize
        initParticles();
    }

    // Initialize particles randomly within the conceptual plasma area circle
    function initParticles() {
        particles = [];
        for (let i = 0; i < numParticles; i++) {
            // Position particles within the cross-section circle (conceptually)
            const angle = Math.random() * Math.PI * 2;
            const r = Math.sqrt(Math.random()) * plasmaAreaRadius; // Distribute evenly within circle
            const x = centerX + r * Math.cos(angle);
            const y = centerY + r * Math.sin(angle);

             // Store position relative to the cross-section center for easier update
             const relX = x - centerX;
             const relY = y - centerY;

            particles.push({
                x: x,
                y: y,
                relX: relX, // Position within the cross-section (local x, y)
                relY: relY,
                // Add properties for motion within the cross-section
                angle: Math.random() * Math.PI * 2, // Angle around the cross-section center
                radius: r, // Distance from the cross-section center
                color: 'var(--particle-color-stable)', // Will be updated based on stability
                opacity: 0.8 + Math.random() * 0.2,
                speed: particleSpeed * (0.8 + Math.random() * 0.4) // Slight speed variation
            });
        }
    }


    function updateParticles(isStable, ratio) {
         const toroidalField = parseInt(toroidalSlider.value);
        const plasmaCurrent = parseInt(plasmaSlider.value);

        particles.forEach(p => {
             if (isStable) {
                 // Simulate helical motion within the cross-section circle
                 // The "twist" depends on the ratio of fields
                 // Higher ratio (more Bt relative to Bp) means less twist per 'long way' turn (higher q)
                 // Lower ratio (more Bp relative to Bt) means more twist per 'long way' turn (lower q)
                 // In this 2D cross-section view, this can be simplified to rotation within the circle.
                 // Let's link rotation speed/direction to the ratio.
                 const rotationSpeed = (ratio - 0.8) * 0.05; // Example: faster rotation for higher ratio (adjust factor)

                p.angle += rotationSpeed * p.speed;

                // Keep angle within 0 to 2*PI
                if (p.angle > Math.PI * 2) p.angle -= Math.PI * 2;
                if (p.angle < 0) p.angle += Math.PI * 2;

                // Update position relative to the cross-section center
                p.relX = p.radius * Math.cos(p.angle);
                p.relY = p.radius * Math.sin(p.angle);

                // Update absolute position (relative to canvas center)
                p.x = centerX + p.relX;
                p.y = centerY + p.relY;

                 // Ensure particles stay within bounds conceptually (they shouldn't hit walls in stable state)
                 const currentDist = Math.sqrt(p.relX * p.relX + p.relY * p.relY);
                 if (currentDist > plasmaAreaRadius) {
                     // If somehow outside, push back towards center
                      const angleToCenter = Math.atan2(p.relY, p.relX);
                      p.relX = plasmaAreaRadius * Math.cos(angleToCenter) * 0.9; // Push back to 90% radius
                      p.relY = plasmaAreaRadius * Math.sin(angleToCenter) * 0.9;
                      p.radius = plasmaAreaRadius * 0.9;
                 }


                 p.color = 'var(--particle-color-stable)';


             } else {
                 // Simulate chaotic, escaping motion
                 // Add random jitter
                 p.relX += (Math.random() - 0.5) * 2 * p.speed;
                 p.relY += (Math.random() - 0.5) * 2 * p.speed;

                 // Add outward drift
                 const angleToCenter = Math.atan2(p.relY, p.relX);
                 const driftSpeed = p.speed * 0.5; // Control drift speed
                 p.relX += Math.cos(angleToCenter) * driftSpeed;
                 p.relY += Math.sin(angleToCenter) * driftSpeed;

                 // Update absolute position
                 p.x = centerX + p.relX;
                 p.y = centerY + p.relY;

                 // Check if particle has escaped the simulation area (or nominal plasma bounds)
                 const currentDist = Math.sqrt(p.relX * p.relX + p.relY * p.relY);
                 if (currentDist > plasmaAreaRadius * 1.5) { // Use a slightly larger radius for 'escape'
                      // Respawn particle near center
                      const angle = Math.random() * Math.PI * 2;
                      const r = Math.sqrt(Math.random()) * plasmaAreaRadius * 0.5; // Respawn closer to center
                      p.relX = r * Math.cos(angle);
                      p.relY = r * Math.sin(angle);
                      p.x = centerX + p.relX;
                      p.y = centerY + p.relY;
                      p.angle = Math.random() * Math.PI * 2;
                      p.radius = r;
                 }

                 p.color = 'var(--particle-color-unstable)';
             }
        });
    }

    function drawSimulation(isStable) {
        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw canvas background (dark space) - although it's already set in CSS
        // ctx.fillStyle = 'var(--canvas-bg)';
        // ctx.fillRect(0, 0, canvas.width, canvas.height);


        // --- Draw Tokamak Outline (Conceptual) ---
        ctx.strokeStyle = 'var(--tokamak-outline)';
        ctx.lineWidth = 10; // Thicker lines
        ctx.lineCap = 'round';

        // Draw outer ring
        ctx.beginPath();
        ctx.arc(centerX, centerY, outerRadius, 0, Math.PI * 2);
        ctx.stroke();

        // Draw inner hole ring
        ctx.beginPath();
        ctx.arc(centerX, centerY, innerRadius, 0, Math.PI * 2);
        ctx.stroke();

        // --- Draw Plasma Representation ---
        ctx.fillStyle = isStable ? 'var(--plasma-stable)' : 'var(--plasma-unstable)';

        if (isStable) {
            // Draw the plasma as a smooth, contained ring
            ctx.beginPath();
             // Outer edge of plasma cross-section ring
            ctx.arc(centerX, centerY, plasmaRingRadius + plasmaAreaRadius, 0, Math.PI * 2);
             // Inner edge of plasma cross-section ring (draw backwards)
            ctx.arc(centerX, centerY, plasmaRingRadius - plasmaAreaRadius, Math.PI * 2, 0, true);
            ctx.closePath(); // Close the path to fill the ring shape
            ctx.fill();

        } else {
             // Draw the plasma as turbulent, perhaps bulging or showing disruptions
             // Simple approach: Draw the ring shape but add some distortion or opacity variations
             ctx.beginPath();
             ctx.arc(centerX, centerY, plasmaRingRadius + plasmaAreaRadius * 1.1, 0, Math.PI * 2); // Slightly larger outer bound
             ctx.arc(centerX, centerY, plasmaRingRadius - plasmaAreaRadius * 0.9, Math.PI * 2, 0, true); // Slightly smaller inner bound
             ctx.closePath();
             ctx.fill();

             // Add some visual noise or distortion (optional, can be complex)
             // For simplicity, let's rely on the particle movement and status text.
        }

        // --- Draw Particles ---
        particles.forEach(p => {
            ctx.fillStyle = p.color;
            ctx.globalAlpha = p.opacity;
            ctx.beginPath();
            ctx.arc(p.x, p.y, particleSize, 0, Math.PI * 2);
            ctx.fill();
        });
        ctx.globalAlpha = 1.0; // Reset alpha
    }


    function animate() {
        const toroidalField = parseInt(toroidalSlider.value);
        const plasmaCurrent = parseInt(plasmaSlider.value);

        // --- Determine Plasma Stability (Improved Model) ---
        // Let's make the stable range more intuitive and visually distinct.
        // Stable often requires q > 1 and not too close to low-order rationals (like 2, 3).
        // q is proportional to Bt / Ip * (a/R)^2. Simplified q ~ Bt / Ip * constant.
        // So stable is roughly when Bt / Ip is in a certain range, maybe slightly higher than 1.
        // Let's define thresholds:
        // Low Ip relative to Bt -> Ratio high -> Kink/External instability
        // High Ip relative to Bt -> Ratio low -> Disruptions/Internal instability
        // Ideal range for Bt/Ip ratio: Maybe 1.2 to 2.5? Let's test some values.
        // Let's say ideal Bt=50, Ip=50 (ratio=1). This should be unstable (q~1 can be problematic).
        // Try Bt=80, Ip=40 (ratio=2). This should be stable.
        // Try Bt=40, Ip=80 (ratio=0.5). Unstable.
        // Let's define stable range for ratio (Bt/Ip) between 1.2 and 2.8 AND both values high enough, e.g., > 25.
        const ratio = toroidalField / plasmaCurrent;
        const isStable = toroidalField > 25 && plasmaCurrent > 25 && ratio > 1.2 && ratio < 2.8;

        // Update status display
        if (toroidalField <= 25 || plasmaCurrent <= 25) {
             plasmaStatusSpan.textContent = 'נדרשים שדות חזקים יותר';
             plasmaStatusSpan.style.color = 'var(--warning-color)';
        } else if (isStable) {
             plasmaStatusSpan.textContent = 'פלזמה יציבה! כליאה מוצלחת.';
             plasmaStatusSpan.style.color = 'var(--stable-color)';
        } else {
             let statusText = 'פלזמה לא יציבה: ';
             if (ratio <= 1.2) {
                 statusText += 'זרם פלזמה גבוה מדי (פיתול יתר)';
             } else if (ratio >= 2.8) {
                  statusText += 'שדה טורואידי גבוה מדי (פיתול חסר)';
             } else {
                 statusText += 'פרמטרים לא מאוזנים';
             }
             plasmaStatusSpan.textContent = statusText;
             plasmaStatusSpan.style.color = 'var(--unstable-color)';
        }

        // Update particle positions based on stability
        updateParticles(isStable, ratio);

        // Draw everything
        drawSimulation(isStable);

        // Request the next frame
        animationFrameId = requestAnimationFrame(animate);
    }

    // Event listeners for sliders
    toroidalSlider.addEventListener('input', () => {
        toroidalValueSpan.textContent = toroidalSlider.value;
        // Animation loop handles the update
    });
    plasmaSlider.addEventListener('input', () => {
        plasmaCurrentValueSpan.textContent = plasmaSlider.value;
        // Animation loop handles the update
    });

    // Event listener for the explanation button
    explanationButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            explanationButton.textContent = 'הסתר הסבר מקיף על טוקמקים והיתוך';
        } else {
            explanationDiv.style.display = 'none';
            explanationButton.textContent = 'הצג/הסתר הסבר מקיף על טוקמקים והיתוך';
        }
    });

    // Initial setup
    resizeCanvas(); // Set initial size and init particles
    window.addEventListener('resize', resizeCanvas); // Add resize listener
    animate(); // Start the animation loop

    // To stop animation if necessary (e.g., cleanup)
    // function stopAnimation() {
    //     cancelAnimationFrame(animationFrameId);
    // }
</script>