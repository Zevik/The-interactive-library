---
title: "איך צמתי דרכים יוצרים ערים?"
english_slug: how-road-intersections-create-cities
category: "גאוגרפיה"
tags:
  - ערים
  - צמתים
  - דרכים
  - התפתחות עירונית
---
# איך צמתי דרכים יוצרים ערים?

האם עצרתם פעם לחשוב למה ערים גדולות ממוקמות דווקא היכן שהן ממוקמות? האם זו אקראיות, או שיש לכך סיבה עמוקה ומרתקת? בואו לגלות איך חיבורים פשוטים בין נתיבי תנועה יכולים לחולל מהפכה ולהוביל לצמיחה עירונית אדירה - כמעט כמו קסם!

<div class="app-container">
    <canvas id="citySimulationCanvas"></canvas>
    <div class="controls">
        <p>ציירו דרכים: לחצו וגררו מנקודה לנקודה (או סתם בחלל). נסו לחבר דרכים קיימות! <br> הזיזו מקורות: לחצו על עיגול כחול וגררו אותו.</p>
        <button id="resetButton" class="control-button">איפוס המפה</button>
    </div>
    <div id="tooltip" class="tooltip" style="display: none;"></div>
</div>

<style>
    :root {
        --primary-color: #4a90e2; /* A pleasant blue */
        --secondary-color: #50e3c2; /* A greenish-blue accent */
        --background-light: #f0f4f7; /* Very light blue-gray */
        --surface-color: #ffffff; /* White for containers */
        --text-color: #333333; /* Dark gray text */
        --border-color: #e0e6ed; /* Light border */
        --road-color: #a0a0a0; /* Gray for roads */
        --source-color: var(--primary-color);
        --meeting-color: #ff6b6b; /* Reddish */
        --settlement-color: #feca57; /* Orangish */
        --town-color: #1dd1a1; /* Greenish */
        --city-color: #8854d0; /* Purplish */
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-light);
        margin: 0;
        padding: 20px;
    }

    h1, h2 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 20px;
    }

     p {
         text-align: justify;
         margin-bottom: 15px;
     }

    .app-container {
        direction: rtl;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px; /* Increased gap */
        margin: 30px auto; /* Center the container */
        padding: 20px; /* Increased padding */
        background-color: var(--surface-color);
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 8px 15px rgba(0,0,0,0.1); /* Stronger shadow */
        max-width: 800px; /* Max width for better presentation */
        width: 95%; /* Responsive width */
    }

    #citySimulationCanvas {
        border: 1px solid var(--border-color);
        background-color: #ebf4f8; /* Slightly blue background for canvas */
        width: 100%;
        max-width: 760px; /* Slightly smaller than container */
        height: 450px; /* Slightly increased height */
        cursor: crosshair;
        border-radius: 8px; /* Match container corners */
    }

    .controls {
        display: flex;
        flex-direction: column; /* Stack controls vertically on small screens */
        align-items: center;
        gap: 15px; /* Gap between stacked items */
        width: 100%;
    }

    .controls p {
        margin: 0;
        font-size: 1em; /* Slightly larger font */
        color: var(--text-color);
        text-align: center;
    }

    .control-button {
        padding: 12px 25px; /* Larger padding */
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 6px; /* Rounded buttons */
        background-color: var(--primary-color);
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        flex-shrink: 0; /* Prevent shrinking */
    }

    .control-button:hover {
        background-color: #357ABD; /* Darker blue on hover */
    }

     .control-button:active {
         transform: scale(0.98); /* Subtle press effect */
     }

    .tooltip {
        position: absolute;
        background-color: rgba(0, 0, 0, 0.7);
        color: white;
        padding: 8px 12px; /* More padding */
        border-radius: 6px;
        font-size: 0.9em;
        pointer-events: none;
        z-index: 1000;
        white-space: nowrap; /* Prevent text wrapping */
        transform: translate(-50%, -110%); /* Position above cursor */
        opacity: 0; /* Start hidden */
        transition: opacity 0.2s ease; /* Fade in/out */
    }

    .tooltip.visible {
         opacity: 1;
    }


    #explanationButton {
        display: block;
        margin: 30px auto; /* More margin */
        padding: 12px 25px; /* Larger padding */
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: var(--secondary-color); /* Different color for explanation */
        color: var(--text-color); /* Dark text on light background */
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    #explanationButton:hover {
        background-color: #41c0a8; /* Darker green-blue */
    }

     #explanationButton:active {
         transform: scale(0.98);
     }


    #explanation {
        display: none;
        margin-top: 20px;
        padding: 20px;
        background-color: var(--surface-color);
        border-radius: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        line-height: 1.7; /* Increased line height */
        max-width: 800px; /* Match container width */
        width: 95%;
        margin: 20px auto; /* Center the explanation block */
    }

    #explanation h2 {
        color: var(--primary-color);
        border-bottom: 2px solid var(--border-color); /* Stronger border */
        padding-bottom: 10px;
        margin-bottom: 15px;
        text-align: right; /* RTL */
    }

     #explanation h3 {
         color: #555;
         margin-top: 20px;
         margin-bottom: 10px;
         text-align: right; /* RTL */
     }

    #explanation p {
        margin-bottom: 15px;
        text-align: justify;
    }

    #explanation ul {
        margin-bottom: 15px;
        padding-right: 30px; /* RTL padding */
        list-style: disc inside; /* Add bullet points */
    }

    #explanation li {
        margin-bottom: 8px;
         text-align: justify;
    }

     @keyframes pulse {
         0% { transform: scale(1); opacity: 1; }
         50% { transform: scale(1.1); opacity: 0.8; }
         100% { transform: scale(1); opacity: 1; }
     }

     .point-pulse {
          animation: pulse 1.5s infinite ease-in-out;
     }

</style>

<button id="explanationButton">הצגת הכוח הנסתר: הסבר מורחב</button>

<div id="explanation">
    <h2>הכוח הנסתר: צמתים, דרכים והתפתחות עירונית</h2>
    <p>
        שאלת המיקום של ערים גדולות מסתירה בתוכה סיפור מרתק על כוחם של חיבורים ונגישות. זו לא מקריות! פעמים רבות, הסיפור מתחיל בנקודת מפגש פשוטה, שהופכת בהדרגה ללב פועם של פעילות אנושית.
    </p>
    <h3>עיר - הרבה יותר מסתם אוסף של מבנים</h3>
    <p>
        חשבו על עיר כעל מגנט אנושי. היא מרכזת אליה אנשים, רעיונות, סחורות ושירותים בקנה מידה עצום. למה שאנשים יבחרו לחיות בצפיפות כזו? הסיבות עמוקות: הזדמנויות כלכליות שפשוט לא קיימות במקומות מבודדים, גישה מרוכזת לשירותים חיוניים כמו בתי חולים ואוניברסיטאות, שוק גדול יותר לרעיונות ויצירה, וכמובן, הצורך האנושי הבסיסי בקשרים חברתיים ותרבותיים. עיר היא במה למפגש וחילוף, והנגישות היא המפתח לכך.
    </p>
    <h3>הסיפור מתחיל בנהר או בנמל...</h3>
    <p>
        בעבר הרחוק, ה"דרכים" החשובות ביותר היו נתיבי מים - נהרות וימים. ערים עתיקות רבות צמחו במיקומים אסטרטגיים על גדות נהרות (כמו קהיר על הנילוס, לונדון על התמזה) או ליד נמלים טבעיים (כמו אתונה, רומא, יפו העתיקה). מקורות מים חיוניים לחיים, לחקלאות וגם לתחבורה וסחר קדום.
    </p>
    <h3>...וממשיך בדרכים יבשתיות</h3>
    <p>
        עם התפתחות טכנולוגיות התחבורה היבשתית (סוסים, עגלות, ואז רכבות ומכוניות), כוח המשיכה של נתיבי היבשה גדל דרמטית. דרכים סלולות אפשרו תנועה מהירה ויעילה יותר של אנשים וסחורות, וחיברו אזורים מרוחקים מהחוף. פתאום, נקודות מפגש יבשתיות הפכו למשמעותיות לא פחות, ולעתים אף יותר, מנקודות מפגש ימיות.
    </p>
    <h3>צומת: הלב הפועם של הנגישות</h3>
    <p>
        דמיינו צומת דרכים. זהו המקום בו נתיבים שונים נפגשים. אנשים שמגיעים מכיוונים שונים חייבים לעבור דרך הנקודה הזו. זהו מקום טבעי לעצירה, למפגש אקראי, להחלפת חדשות, לסחר חליפין, או פשוט למנוחה ותדלוק (אז היו פונדקים, היום תחנות דלק וקניונים). ככל שיותר דרכים נפגשות, כך התנועה וה"מפגש הפוטנציאלי" גדלים. הנקודה הזו הופכת באופן טבעי לאטרקטיבית לפעילות כלכלית: סוחרים פותחים דוכנים, בעלי מלאכה מתיישבים בסמוך, ושירותים נדרשים צצים כדי לשרת את זרם העוברים ושבים.
    </p>
    <h3>לולאת הקסם: ככל שגדלים - כך גדלים עוד יותר!</h3>
    <p>
        התפתחות עיר סביב צומת היא דוגמה קלאסית ל"לולאת משוב חיובית". זה תהליך שמזין את עצמו:
    </p>
    <ul>
        <li>**יותר דרכים, יותר תנועה:** חיבור דרכים חדשות לצומת מגביר את זרם האנשים והסחורות.</li>
        <li>**תנועה מביאה הזדמנויות:** היכן שיש אנשים עוברים, יש פוטנציאל לסחר ושירותים. עסקים נפתחים כדי לשרת את ה"לקוחות הפוטנציאליים" האלה.</li>
        <li>**הזדמנויות מושכות אנשים:** ככל שיש יותר עסקים ושירותים, כך המקום הופך אטרקטיבי יותר להתיישבות קבע של אנשים שמחפשים עבודה, גישה לשירותים, או פשוט להיות חלק ממרכז פעיל.</li>
        <li>**התיישבות מגבירה את התנועה (שוב!):** גידול האוכלוסייה במקום עצמו מוסיף עוד שכבה של תנועה (אנשים שחיים ועובדים במקום) שמגבירה עוד יותר את הפעילות בצומת.</li>
        <li>**צמיחה מהירה:** הלולאה הזו - תנועה -> הזדמנויות -> התיישבות -> עוד תנועה - מאיצה את עצמה, והצומת הפשוט יכול לצמוח מנקודת מפגש קטנה ליישוב, עיירה, ואף לעיר שוקקת חיים.</li>
    </ul>
    <h3>מצמתי רכבת ל"ערי שדה תעופה"</h3>
    <p>
        העיקרון הזה נכון בכל התקופות. שיקגו, למשל, הפכה לעיר ענקית בזכות מיקומה כצומת מרכזי של מסילות ברזל. בישראל, ערים כמו באר שבע או עפולה צמחו באופן משמעותי בזכות מיקומן בצמתי דרכים היסטוריים וחדשים. וגם היום? שדות תעופה בינלאומיים הם הצמתים החדשים! הם מרכזים תנועה עולמית של אנשים וסחורות, והופכים ל"ערי שדה תעופה" (Aerotropolis) שמושכות סביבן עסקים, תעשייה ומגורים בקצב מסחרר. אפילו בעולם הדיגיטלי, פלטפורמות כמו רשתות חברתיות או אתרי מכירות ענקיים הן סוג של "צמתים דיגיטליים" - הן מצליחות בזכות הריכוז העצום של אנשים ומידע.
    </p>
    <p>
        הסימולציה שלפניכם מציגה את העיקרון הזה בצורה פשוטה: חברו עוד ועוד דרכים וצפו בנקודות המפגש צומחות והופכות למרכזים עירוניים! זהו כוחם של החיבור והנגישות בפעולה.
    </p>
</div>


<script>
    const canvas = document.getElementById('citySimulationCanvas');
    const ctx = canvas.getContext('2d');
    const tooltip = document.getElementById('tooltip');
    const explanationDiv = document.getElementById('explanation');
    const explanationButton = document.getElementById('explanationButton');
    const resetButton = document.getElementById('resetButton');

    let points = [];
    let roads = [];
    let drawing = false;
    let currentRoad = null;
    let draggingSource = null;
    let dragOffset = { x: 0, y: 0 };
    let animationFrameId = null; // To manage the animation loop

    const SOURCE_RADIUS = 10;
    const POINT_RADIUS = 5;
    const INTERSECTION_TOLERANCE = 15; // How close road segments must be to be considered an intersection
    const CONNECT_TOLERANCE = 20; // How close mouse must be to connect to an existing point

    // Potential thresholds for growth stages
    const POTENTIAL_THRESHOLD_MEETING = 1; // Base potential from being on roads
    const POTENTIAL_THRESHOLD_SETTLEMENT = 4;
    const POTENTIAL_THRESHOLD_TOWN = 10;
    const POTENTIAL_THRESHOLD_CITY = 20;

    const GROWTH_FACTOR = 0.015; // How much potential increases per road *segment* passing through an intersection (lower value for finer growth)

    // Color definitions (matching CSS variables)
    const COLORS = {
        source: '#4a90e2',
        road: '#a0a0a0',
        drawingRoad: '#666',
        meeting: '#ff6b6b',
        settlement: '#feca57',
        town: '#1dd1a1',
        city: '#8854d0',
        defaultIntersection: '#cccccc', // Lighter gray before reaching meeting threshold
        text: 'white',
        sourceText: 'white'
    };

    // Initial source points
    function initializePoints() {
        points = [
            { x: 100, y: 100, type: 'source', potential: 0, id: 'A', originalPos: { x: 100, y: 100 } },
            { x: 600, y: 100, type: 'source', potential: 0, id: 'B', originalPos: { x: 600, y: 100 } },
            { x: 350, y: 350, type: 'source', potential: 0, id: 'C', originalPos: { x: 350, y: 350 } }
        ];
        roads = [];
        findIntersections(); // Calculate initial state
        calculatePotential();
        redrawCanvas();
    }

    function draw() {
        // Set canvas size for high DPI displays and responsiveness
        const rect = canvas.parentElement.getBoundingClientRect();
        canvas.width = rect.width * window.devicePixelRatio;
        canvas.height = 450 * window.devicePixelRatio;
        ctx.scale(window.devicePixelRatio, window.devicePixelRatio);

        ctx.clearRect(0, 0, canvas.width / window.devicePixelRatio, canvas.height / window.devicePixelRatio);

        // Draw roads
        ctx.strokeStyle = COLORS.road;
        ctx.lineWidth = 4; // Thicker roads
        ctx.lineCap = 'round'; // Round road caps
        roads.forEach(road => {
            ctx.beginPath();
            ctx.moveTo(road.p1.x, road.p1.y);
            ctx.lineTo(road.p2.x, road.p2.y);
            ctx.stroke();
        });

        // Draw current road being drawn
        if (currentRoad) {
             ctx.strokeStyle = COLORS.drawingRoad;
             ctx.lineWidth = 4;
             ctx.beginPath();
             ctx.moveTo(currentRoad.p1.x, currentRoad.p1.y);
             ctx.lineTo(currentRoad.p2.x, currentRoad.p2.y);
             ctx.stroke();
        }


        // Draw points (sources, intersections)
        points.forEach(point => {
            ctx.beginPath();
            let radius = POINT_RADIUS;
            let color = COLORS.defaultIntersection;
            let label = null;
            let showPotentialText = false;

            if (point.type === 'source') {
                radius = SOURCE_RADIUS;
                color = COLORS.source;
                label = point.id; // Label sources A, B, C
                ctx.fillStyle = color;
                ctx.arc(point.x, point.y, radius, 0, Math.PI * 2);
                ctx.fill();
                // Draw source ID
                ctx.fillStyle = COLORS.sourceText;
                ctx.font = '12px Arial';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText(label, point.x, point.y);

            } else if (point.type === 'intersection') {
                // Determine size, color, and label based on potential
                if (point.potential >= POTENTIAL_THRESHOLD_CITY) {
                    radius = 25; // City
                    color = COLORS.city;
                    label = 'עיר';
                    showPotentialText = true;
                } else if (point.potential >= POTENTIAL_THRESHOLD_TOWN) {
                    radius = 18; // Town
                    color = COLORS.town;
                    label = 'עיירה';
                     showPotentialText = true;
                } else if (point.potential >= POTENTIAL_THRESHOLD_SETTLEMENT) {
                    radius = 12; // Settlement
                    color = COLORS.settlement;
                    label = 'יישוב';
                     showPotentialText = true;
                } else if (point.potential > 0) { // Meeting point (potential > 0 but below settlement)
                     radius = 8;
                     color = COLORS.meeting;
                     label = 'מפגש';
                } else { // Bare intersection point
                     radius = POINT_RADIUS;
                     color = COLORS.defaultIntersection;
                }

                ctx.fillStyle = color;
                ctx.arc(point.x, point.y, radius, 0, Math.PI * 2);
                ctx.fill();

                 // Draw label for larger settlements
                 if (label && point.potential >= POTENTIAL_THRESHOLD_SETTLEMENT) {
                     ctx.fillStyle = COLORS.text;
                     ctx.font = `bold ${radius * 0.7}px Arial`; // Bold and scaled font
                     ctx.textAlign = 'center';
                     ctx.textBaseline = 'middle';
                     ctx.fillText(label, point.x, point.y - radius - 5); // Position label above point
                 }

                // Draw potential number for larger settlements
                 if (showPotentialText) {
                     ctx.fillStyle = COLORS.text;
                     ctx.font = `${radius * 0.6}px Arial`; // Smaller font for potential number
                     ctx.textAlign = 'center';
                     ctx.textBaseline = 'middle';
                     ctx.fillText(Math.floor(point.potential), point.x, point.y + radius + 5); // Position number below point
                 }


            } else { // Basic point (shouldn't really have any now, sources and intersections cover it)
                 // Maybe draw a small dot or skip? Let's skip for cleaner look unless needed.
            }
        });

        // No complex traffic animation for now, focusing on point growth visual.
        // Could add simple pulsating effect via CSS class handled by JS based on growth level.
        // However, drawing animations on canvas directly is smoother for pulsing/scaling.
        // Let's add a simple scaling pulse effect via JS for points with potential > 0
         points.filter(p => p.type === 'intersection' && p.potential > 0).forEach(point => {
              // Calculate current pulse scale based on time (simplified)
              const scale = 1 + Math.sin(Date.now() / 300) * 0.05; // Subtle pulse 5%

               let radius = POINT_RADIUS;
                if (point.potential >= POTENTIAL_THRESHOLD_CITY) radius = 25;
                else if (point.potential >= POTENTIAL_THRESHOLD_TOWN) radius = 18;
                else if (point.potential >= POTENTIAL_THRESHOLD_SETTLEMENT) radius = 12;
                else if (point.potential > 0) radius = 8;

              ctx.beginPath();
              ctx.fillStyle = ctx.fillStyle; // Use the color already set
              ctx.arc(point.x, point.y, radius * scale, 0, Math.PI * 2);
              ctx.fill();
         });


         animationFrameId = requestAnimationFrame(draw); // Keep the animation loop running
    }


    function redrawCanvas() {
         // Just call draw which handles sizing and drawing
         // Cancel any existing animation frame before requesting a new one
         if (animationFrameId) {
             cancelAnimationFrame(animationFrameId);
         }
         draw();
    }


    function getMousePos(canvas, evt) {
        const rect = canvas.getBoundingClientRect();
        return {
            x: (evt.clientX - rect.left) / window.devicePixelRatio,
            y: (evt.clientY - rect.top) / window.devicePixelRatio
        };
    }

    function isNearPoint(pos, point, tolerance) {
         return Math.sqrt((pos.x - point.x)**2 + (pos.y - point.y)**2) < tolerance;
    }

    function getNearestPoint(pos) {
        let nearest = null;
        let minDist = Infinity;
        points.forEach(point => {
            const dist = Math.sqrt((pos.x - point.x)**2 + (pos.y - point.y)**2);
            // Check against connecting tolerance, but prioritize sources if very close
            let currentTolerance = CONNECT_TOLERANCE;
            if (point.type === 'source') currentTolerance = SOURCE_RADIUS + 5; // Be more generous for sources

            if (dist < minDist && dist < currentTolerance) {
                minDist = dist;
                nearest = point;
            }
        });
        return nearest;
    }

    function findIntersections() {
        const newIntersections = [];
        // Keep sources, reset intersections
        points = points.filter(p => p.type === 'source');

        // Naive intersection finding: check every road pair
        for (let i = 0; i < roads.length; i++) {
            for (let j = i + 1; j < roads.length; j++) {
                const p1 = roads[i].p1;
                const q1 = roads[i].p2;
                const p2 = roads[j].p1;
                const q2 = roads[j].p2;

                const intersection = getLineIntersection(p1, q1, p2, q2);

                if (intersection) {
                    // Check if this intersection point is already found (within tolerance)
                    let alreadyExists = newIntersections.some(int =>
                        Math.sqrt((int.x - intersection.x)**2 + (int.y - intersection.y)**2) < INTERSECTION_TOLERANCE
                    );
                     // Also check against existing sources (a road ending near a source is not a new intersection)
                    let nearSource = points.filter(p => p.type === 'source').some(source =>
                         Math.sqrt((source.x - intersection.x)**2 + (source.y - intersection.y)**2) < SOURCE_RADIUS
                    );


                    if (!alreadyExists && !nearSource) {
                         newIntersections.push({
                            x: intersection.x,
                            y: intersection.y,
                            type: 'intersection',
                            potential: 0 // Potential calculated later
                         });
                    }
                }
            }
        }

        // Add new intersections to the points list
        points.push(...newIntersections);
    }

     // Helper function to find intersection point of two line segments
     // Returns point {x, y} or false if no intersection or collinear
    function getLineIntersection(p1, q1, p2, q2) {
        // Calculate direction vectors
        const v1 = { x: q1.x - p1.x, y: q1.y - p1.y };
        const v2 = { x: q2.x - p2.x, y: q2.y - p2.y };
        const v3 = { x: p1.x - p2.x, y: p1.y - p2.y };

        // Calculate determinant
        const det = v1.x * v2.y - v1.y * v2.x;

        // If determinant is zero, lines are parallel (or collinear)
        if (Math.abs(det) < 1e-6) {
            return false; // No unique intersection or collinear
        }

        // Calculate parameters t and u
        const t = (v2.y * v3.x - v2.x * v3.y) / det;
        const u = (v1.x * v3.y - v1.y * v3.y) / det; // Fixed typo here? Should be v1.y * v3.x, not v1.y * v3.y

         // Let's re-calculate t and u using cross product method
         const s = (-v1.y * v3.x + v1.x * v3.y) / det;
         const t_param = ( v2.x * v3.y - v2.y * v3.x) / det;


        // Check if intersection point lies within both segments (0 <= s <= 1 and 0 <= t_param <= 1)
        // Using corrected s and t_param calculation from standard line segment intersection
        if (s >= 0 && s <= 1 && t_param >= 0 && t_param <= 1) {
            // Calculate intersection point using t_param along segment 2
            const intersectionX = p2.x + t_param * v2.x;
            const intersectionY = p2.y + t_param * v2.y;

             // Ensure the point is actually *between* the endpoints, not just on the infinite line
             // This check is usually redundant if 0 <= t, u <= 1 but can help with floating point issues near endpoints
             const isBetweenEndpoints1 = (intersectionX >= Math.min(p1.x, q1.x) && intersectionX <= Math.max(p1.x, q1.x) && intersectionY >= Math.min(p1.y, q1.y) && intersectionY <= Math.max(p1.y, q1.y));
             const isBetweenEndpoints2 = (intersectionX >= Math.min(p2.x, q2.x) && intersectionX <= Math.max(p2.x, q2.x) && intersectionY >= Math.min(p2.y, q2.y) && intersectionY <= Math.max(p2.y, q2.y));

             if(isBetweenEndpoints1 && isBetweenEndpoints2) {
                 return {
                    x: intersectionX,
                    y: intersectionY
                 };
             }
        }

        return false; // Intersection is outside segments or not truly between endpoints
    }

    // Check if a point lies on a line segment within a tolerance
    function isPointOnSegment(point, p1, p2, tolerance) {
        const dist_p1_point = Math.sqrt((p1.x - point.x)**2 + (p1.y - point.y)**2);
        const dist_p2_point = Math.sqrt((p2.x - point.x)**2 + (p2.y - point.y)**2);
        const dist_p1_p2 = Math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2);

        // If the sum of distances from the point to the endpoints is close to the distance between endpoints,
        // the point is on the segment.
        return Math.abs(dist_p1_point + dist_p2_point - dist_p1_p2) < tolerance;
    }


    function calculatePotential() {
        // Reset potential for all points (sources don't accumulate potential in this model, they generate traffic)
        points.forEach(point => {
            if (point.type === 'intersection') {
                point.potential = 0; // Reset before recalculating
            }
        });

        // Simple potential model: potential increases for each road segment passing through the intersection.
        // A road segment is defined by the intersection points and the original road endpoints.

        points.filter(p => p.type === 'intersection').forEach(intersection => {
             // Find all road segments that contain this intersection point
             roads.forEach(road => {
                  if (isPointOnSegment(intersection, road.p1, road.p2, 1)) { // Use a small tolerance
                       // Add potential for each road it lies on
                       intersection.potential += GROWTH_FACTOR;
                  }
             });
        });

        // This basic model counts how many original road lines *pass through* the intersection point.
        // A more complex model could count segments *between* intersection points on the same original line,
        // or simulate traffic flow from sources. Sticking to the simpler "roads passing through" interpretation for now.
    }


    // --- Event Listeners ---

    canvas.addEventListener('mousedown', (e) => {
        const pos = getMousePos(canvas, e);
        const clickedPoint = getNearestPoint(pos);

        if (clickedPoint && clickedPoint.type === 'source') {
            draggingSource = clickedPoint;
             // Store original position for road re-linking
            if (!draggingSource.originalPos) {
                 draggingSource.originalPos = { x: draggingSource.x, y: draggingSource.y };
            }
            dragOffset = { x: pos.x - clickedPoint.x, y: pos.y - clickedPoint.y };
            canvas.style.cursor = 'grabbing';
        } else {
             drawing = true;
             // Start from nearest point if close, otherwise start from click position
             const startPoint = clickedPoint ? { x: clickedPoint.x, y: clickedPoint.y } : { x: pos.x, y: pos.y };
             currentRoad = { p1: startPoint, p2: { x: pos.x, y: pos.y } };
             canvas.style.cursor = 'none'; // Hide default cursor while drawing
        }
         redrawCanvas(); // Redraw immediately on mousedown to show drawing start or drag
    });

    canvas.addEventListener('mousemove', (e) => {
        const pos = getMousePos(canvas, e);

        // Handle dragging
        if (draggingSource) {
            draggingSource.x = pos.x - dragOffset.x;
            draggingSource.y = pos.y - dragOffset.y;
            // Update road endpoints connected to this source if necessary (handled implicitly by recalculation later)
             redrawCanvas();
            findIntersections(); // Recalculate intersections and potential as source moves
            calculatePotential();
             redrawCanvas(); // Redraw continuously while dragging
            return; // Stop processing other mousemove events
        }

        // Handle drawing
        if (drawing && currentRoad) {
             // Check if near an existing point to snap the drawing line
             const endPoint = getNearestPoint(pos);
             if (endPoint) {
                  currentRoad.p2 = { x: endPoint.x, y: endPoint.y };
                  canvas.style.cursor = 'pointer'; // Indicate snapping
             } else {
                  currentRoad.p2 = { x: pos.x, y: pos.y };
                  canvas.style.cursor = 'none'; // Back to none if not near point
             }
             redrawCanvas();
        }

        // Handle tooltips for intersections
        const hoveredPoint = getNearestPoint(pos);
        if (hoveredPoint && hoveredPoint.type === 'intersection' && hoveredPoint.potential > 0) {
             tooltip.classList.add('visible');
             // Position tooltip relative to the mouse, accounting for potential point size
             const pointRadius = hoveredPoint.potential >= POTENTIAL_THRESHOLD_CITY ? 25
                                 : hoveredPoint.potential >= POTENTIAL_THRESHOLD_TOWN ? 18
                                 : hoveredPoint.potential >= POTENTIAL_THRESHOLD_SETTLEMENT ? 12
                                 : hoveredPoint.potential > 0 ? 8 : POINT_RADIUS;

             tooltip.style.left = `${hoveredPoint.x * window.devicePixelRatio}px`;
             tooltip.style.top = `${hoveredPoint.y * window.devicePixelRatio}px`; // Position relative to the point itself
            //  tooltip.style.left = `${e.clientX + 10}px`; // Position relative to mouse
            //  tooltip.style.top = `${e.clientY + 10}px`;

             let tooltipText = `פוטנציאל: ${Math.floor(hoveredPoint.potential)}`;
             if (hoveredPoint.potential >= POTENTIAL_THRESHOLD_CITY) tooltipText += ' (עיר!)';
             else if (hoveredPoint.potential >= POTENTIAL_THRESHOLD_TOWN) tooltipText += ' (עיירה)';
             else if (hoveredPoint.potential >= POTENTIAL_THRESHOLD_SETTLEMENT) tooltipText += ' (יישוב)';
             else if (hoveredPoint.potential > 0) tooltipText += ' (נקודת מפגש)';
             tooltip.textContent = tooltipText;

        } else {
             tooltip.classList.remove('visible');
        }

        // Change cursor if near a draggable source
        if (!drawing && !draggingSource) {
            const pointNearMouse = getNearestPoint(pos);
            if (pointNearMouse && pointNearMouse.type === 'source') {
                 canvas.style.cursor = 'grab';
            } else {
                 canvas.style.cursor = 'crosshair';
            }
        }

    });

    canvas.addEventListener('mouseup', (e) => {
         if (draggingSource) {
              // Update road endpoints connected to the dragged source
              roads.forEach(road => {
                  // Check if p1 or p2 is the draggingSource object reference
                  if (road.p1 === draggingSource) {
                      road.p1 = { x: draggingSource.x, y: draggingSource.y }; // Update endpoint coordinates
                  }
                   if (road.p2 === draggingSource) {
                       road.p2 = { x: draggingSource.x, y: draggingSource.y }; // Update endpoint coordinates
                   }
              });
             // Update the original position for the next drag
             draggingSource.originalPos = { x: draggingSource.x, y: draggingSource.y };

             draggingSource = null; // Stop dragging
             canvas.style.cursor = 'crosshair'; // Reset cursor
              // Re-calculate everything after dragging ends
             findIntersections();
             calculatePotential();
             redrawCanvas();
             return;
         }

        if (drawing && currentRoad) {
            const endPos = getMousePos(canvas, e);
            const endPoint = getNearestPoint(endPos);

            // If snapped to an existing point, use its coordinates. Otherwise, use the exact mouse release coordinates.
            currentRoad.p2 = endPoint ? { x: endPoint.x, y: endPoint.y } : { x: endPos.x, y: endPos.y };

            // Don't add zero-length roads
            if (currentRoad.p1.x !== currentRoad.p2.x || currentRoad.p1.y !== currentRoad.p2.y) {
                // Add the new road
                roads.push(currentRoad);

                // Ensure endpoints that snapped to existing points use the point object reference
                // This is important so moving the source point updates the road endpoint
                if (endPoint) {
                    roads[roads.length-1].p2 = endPoint;
                }
                 const startPoint = getNearestPoint(currentRoad.p1); // Check if start was on a point
                 if(startPoint) {
                      roads[roads.length-1].p1 = startPoint;
                 }
            }


            currentRoad = null; // Stop drawing
            drawing = false;
            canvas.style.cursor = 'crosshair'; // Reset cursor

            // Find new intersections, recalculate potential, and redraw
            findIntersections();
            calculatePotential();
            redrawCanvas();
        }
         tooltip.classList.remove('visible'); // Hide tooltip on mouseup
    });

     // Prevent context menu on right-click
    canvas.addEventListener('contextmenu', (e) => {
        e.preventDefault();
    });


    // Handle window resize to make canvas responsive
    window.addEventListener('resize', redrawCanvas);

    // Explanation toggle button
    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר הסבר על הכוח הנסתר' : 'הצגת הכוח הנסתר: הסבר מורחב';
    });

    // Reset button
    resetButton.addEventListener('click', initializePoints);

    // Initialize the simulation on page load
    initializePoints();

    // Start the animation loop
    redrawCanvas();


</script>
```