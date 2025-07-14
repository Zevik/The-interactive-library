---
title: "טלסקופים של חלקיקי רפאים: הצצה לעולם הנייטרינו"
english_slug: ghost-particle-telescopes-neutrino-world
category: "פיזיקה"
tags: [נייטרינו, אסטרופיזיקה, פיזיקת חלקיקים, טלסקופים, IceCube]
---
<h1>טלסקופים של חלקיקי רפאים: הצצה לעולם הנייטרינו</h1>
<p>כיצד אנו יכולים 'לראות' חלקיקים קוסמיים שמגיעים אלינו מיליארדי שנות אור ושבקושי מקיימים אינטראקציה עם חומר? הם עוברים דרך כוכבים, כוכבי לכת, ואפילו דרכנו - מיליוני טריליונים מהם בכל שנייה - מבלי להשאיר סימן. גלו כיצד מדענים בונים מכשירים בגודל של ערי ענק כדי ללכוד את האותות הנדירים שלהם ולגלות את סודות היקום האנרגטי ביותר!</p>

<div id="app">
    <h2>הפעל את גלאי הנייטרינו!</h2>
    <p>לחץ על הכפתור למטה כדי לשלוח נייטרינו ונסה לזהות אינטראקציה נדירה בתוך הגלאי.</p>
    <canvas id="detectorCanvas"></canvas>
    <div class="controls">
        <button id="sendNeutrinoBtn">שלח נייטרינו!</button>
        <div id="stats">
            <span id="neutrinosSent">נייטרינו שנשלחו: 0</span> | <span id="interactionsDetected">אינטראקציות זוהו: 0</span>
        </div>
        <div id="message">צפה כאן בהתקדמות... רובם יעברו דרך!</div>
    </div>
</div>

<style>
    /* גלובלי וגוף */
    body {
        font-family: 'Arial Hebrew', Arial, sans-serif;
        direction: rtl;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6;
        margin: 0;
        padding: 20px;
        text-align: right;
    }

    h1, h2, h3 {
        color: #0e4d61;
        text-align: center;
    }

    p {
        margin-bottom: 1em;
    }

    /* מיכל האפליקציה */
    #app {
        background-color: #ffffff;
        border: 1px solid #cfe2f3;
        border-radius: 12px;
        padding: 25px;
        margin: 20px auto;
        max-width: 700px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center; /* ליישור מרכיבי ה app למרכז */
    }

    #app h2, #app p {
        text-align: center; /* לוודא כותרות ופסקאות בתוך האפליקציה ממורכזים */
        margin-bottom: 10px;
    }

    /* קנבס הגלאי */
    #detectorCanvas {
        width: 100%;
        max-width: 600px; /* גודל מקסימלי נוח לצפייה */
        height: 400px; /* גובה קבוע ליציבות */
        border: 2px solid #0e4d61;
        background: linear-gradient(to bottom, #e0f7fa, #b2ebf2); /* רקע קרח/מים מדורג */
        margin-bottom: 20px;
        border-radius: 8px;
        box-sizing: border-box;
        box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.2); /* הצללה פנימית */
    }

    /* איזור הבקרות והסטטיסטיקות */
    .controls {
        width: 100%;
        max-width: 600px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    button {
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #26a69a; /* צבע ירוק-כחול */
        color: white;
        border: none;
        border-radius: 6px;
        margin-bottom: 15px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    button:hover {
        background-color: #00897b;
        transform: translateY(-2px);
    }

    button:active {
         background-color: #00796b;
         transform: translateY(0);
    }

     button:disabled {
         background-color: #cccccc;
         cursor: not-allowed;
     }

    #stats {
        font-size: 0.95em;
        color: #555;
        margin-bottom: 10px;
    }

    #message {
        font-size: 1em;
        color: #0e4d61;
        min-height: 1.5em; /* לשמור מקום לטקסט */
        font-weight: bold;
    }

    /* כפתור ההסבר */
    #explanationButton {
         padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        background-color: #0277bd; /* כחול עמוק */
        color: white;
        border: none;
        border-radius: 5px;
        margin-top: 20px;
        transition: background-color 0.3s ease;
        display: block; /* לוודא שהכפתור הוא בלוק נפרד */
        margin-left: auto;
        margin-right: auto;
    }

    #explanationButton:hover {
        background-color: #01579b;
    }

    /* איזור ההסבר */
    #explanation {
        display: none; /* מוסתר בתחילה */
        margin-top: 30px;
        padding: 25px;
        border: 1px solid #cfe2f3;
        border-radius: 12px;
        background-color: #e3f2fd; /* רקע כחול בהיר */
        text-align: right; /* טקסט RTL */
        direction: rtl;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
    }

    #explanation h2, #explanation h3 {
        color: #0e4d61;
        margin-bottom: 10px;
        border-bottom: 1px solid #bbdefb; /* קו הפרדה עדין */
        padding-bottom: 5px;
    }

    #explanation p {
        margin-bottom: 15px;
        line-height: 1.7;
        color: #444;
    }

    #explanation ul {
        margin-bottom: 15px;
        padding-right: 25px;
    }
    #explanation li {
        margin-bottom: 8px;
        color: #444;
    }

    /* אנימציות וסגנונות דינמיים (דרך JS בעיקר) */
    .dom-hit {
         fill: #ffeb3b !important; /* צהוב בוהק */
         stroke: #fbc02d !important; /* כתום כהה יותר */
         animation: dom-pulse 0.5s ease-out forwards; /* אנימציית פעימה */
    }

    @keyframes dom-pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.3); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
    }

    .interaction-flash {
        animation: flash 0.3s ease-out;
    }

    @keyframes flash {
        0% { opacity: 1; background-color: rgba(255, 0, 0, 0.5); }
        100% { opacity: 0; background-color: rgba(255, 0, 0, 0); }
    }

</style>

<button id="explanationButton">הצג הסבר מפורט</button>

<div id="explanation">
    <h2>הסבר מפורט: הצצה לעולם הנייטרינו וגלאי IceCube</h2>

    <h3>מהם נייטרינו ולמה קוראים להם 'חלקיקי רפאים'?</h3>
    <p>נייטרינו הם חלקיקים אלמנטריים מיסתוריים. הם דומים לאלקטרונים אך חסרי מטען חשמלי ובעלי מסה זעירה ביותר (או אולי אפסית - זאת עדיין שאלה פתוחה!). התכונה המדהימה והמאתגרת ביותר שלהם היא שהם כמעט ולא מקיימים אינטראקציה עם חומר. תארו לכם: בכל שנייה, טריליוני נייטרינו שנוצרו עמוק בליבת השמש או באזורים אלימים בחלל עוברים דרך גופכם, דרך בניינים, ואפילו דרך כדור הארץ כולו - ללא כל השפעה מורגשת!</p>
    <p>בשל התכונה הזו, המדענים כינו אותם 'חלקיקי רפאים' (Ghost Particles). קשה מאוד ללכוד אותם, אבל דווקא בגלל שהם כמעט ולא מושפעים מסביבתם, הם נושאים מידע יקר מפז ממקומות ביקום שאליהם לא יכולים להגיע חלקיקים או קרינה אחרת.</p>

    <h3>מדוע הם כה קשים לגילוי ואיך בכל זאת עושים את זה?</h3>
    <p>הקושי בגילויים נובע ישירות מחולשת האינטראקציה שלהם. כדי שיקרה אירוע בודד שבו נייטרינו "יפגע" באטום וייצור סימן שניתן לזהות, נדרש נפח עצום לחלוטין של חומר. זה כמו לנסות לתפוס גרגיר אבק בטורנדו - צריך רשת ענקית!</p>
    <p>כאן נכנסים לתמונה גלאי הנייטרינו הענקיים, כמו גלאי IceCube (קוביית קרח) הממוקם בקוטב הדרומי. הרעיון גאוני בפשטותו, אך מימושו מורכב: משתמשים בחומר שקוף ועצום שכבר קיים בטבע - קרח עמוק או מים טהורים - כחומר יעד לגילוי.</p>

    <h3>עקרון הפעולה של גלאי IceCube: לראות את האור הכחול</h3>
    <p>גלאי IceCube הוא למעשה קילומטר מעוקב של קרח טהור, הממוקם בעומק של 1.5 עד 2.5 קילומטרים מתחת לפני השטח באנטארקטיקה. בתוך נפח הקרח העצום הזה, פרוסים כ-5,160 חיישנים אופטיים (הנקראים DOMs - Digital Optical Modules) המחוברים בכבלים אל פני השטח.</p>
    <p>והנה מה שקורה (באירועים הנדירים שבהם זה קורה):</p>
    <ol>
        <li><strong>אינטראקציה נדירה:</strong> נייטרינו שעובר דרך הקרח מקיים, לעיתים נדירות ביותר, אינטראקציה גרעינית או אלקטרונית עם אטום קרח.</li>
        <li><strong>נוצר חלקיק משני טעון:</strong> מאינטראקציה זו נוצר חלקיק טעון חדש, לרוב אלקטרון, מיואון או חלקיק אחר.</li>
        <li><strong>מהירות על-אורית בתוך הקרח:</strong> החלקיק הטעון הזה מקבל אנרגיה גבוהה מהנייטרינו והוא עשוי לנוע מהר יותר ממהירות האור <strong>בתוך הקרח</strong> (זכרו, מהירות האור בתווך שקוף איטית יותר ממהירות האור בריק!).</li>
        <li><strong>קרינת צ'רנקוב: "בום על-קולי" של אור:</strong> כאשר חלקיק טעון נע מהר יותר ממהירות האור בתווך, הוא פולט קרינת צ'רנקוב - מעין 'בום על-קולי', אבל של אור כחול. קרינה זו נפוצה בצורת חרוט של אור מסביב למסלול החלקיק הטעון.</li>
        <li><strong>קליטת האור על ידי החיישנים:</strong> פוטונים של קרינת צ'רנקוב נעים בתוך הקרח ונקלטים על ידי חיישני ה-DOM. כל חיישן רושם את עוצמת האור שהגיע אליו ואת זמן ההגעה המדויק, ברמת דיוק של ננו-שניות!</li>
        <li><strong>שחזור האירוע:</strong> על ידי ניתוח המידע מכל החיישנים שנפגעו - מיקומם המדויק, עוצמת האור ובעיקר <strong>ההפרשים הקטנים בזמני ההגעה</strong> - המדענים יכולים לשחזר לאחור את מסלול החלקיק הטעון, וממנו להסיק על נקודת האינטראקציה המקורית, כיוון ההגעה של הנייטרינו, ואף את האנרגיה שלו!</li>
    </ol>
    <p>גלאי IceCube משמש כ'טלסקופ' עצום, שמסתכל דרך כדור הארץ וצד נייטרינו שמגיעים בעיקר מחצי הכדור הצפוני (כדור הארץ מסנן את רעש הרקע של חלקיקים אחרים). גילוי נייטרינו באנרגיות גבוהות שמגיעים ממקורות ספציפיים בחלל פותח בפנינו חלון חדש לחקר תופעות אסטרופיזיות אלימות וקיצוניות שאותן קשה לחקור באור רגיל.</p>

    <h3>מה גילינו ומה הלאה?</h3>
    <p>IceCube זיהה לראשונה נייטרינו קוסמיים באנרגיות גבוהות מאוד והצליח אף לאתר מקור אפשרי אחד (בלייזר, סוג של גלקסיה פעילה) באמצעות שילוב מידע נייטרינו עם תצפיות אסטרונומיות אחרות. עתיד המחקר כולל שדרוג IceCube (ל-IceCube-Gen2) והקמת גלאים גדולים אף יותר, במטרה ללכוד יותר נייטרינו, לאתר מקורות נוספים ולהבין טוב יותר את החידות הגדולות של היקום האנרגטי ביותר.</p>
</div>

<script>
    const canvas = document.getElementById('detectorCanvas');
    const ctx = canvas.getContext('2d');
    const messageDiv = document.getElementById('message');
    const sendButton = document.getElementById('sendNeutrinoBtn');
    const explanationButton = document.getElementById('explanationButton');
    const explanationDiv = document.getElementById('explanation');
    const neutrinosSentSpan = document.getElementById('neutrinosSent');
    const interactionsDetectedSpan = document.getElementById('interactionsDetected');

    let detectorWidth;
    let detectorHeight;
    const domRadius = 6; // רדיוס גדול יותר לחיישנים
    const doms = []; // מערך לחיישנים

    const numDomsX = 10; // יותר חיישנים לרוחב
    const numDomsY = 8; // יותר חיישנים לגובה
    const paddingX = 20; // ריפוד קטן יותר
    const paddingY = 20; // ריפוד קטן יותר

    // פרמטרים לסימולציה
    const neutrinoSpeed = 3; // מהירות נייטרינו פיקסלים/פרים
    const secondarySpeed = 4; // מהירות חלקיק משני (מהיר יותר)
    const interactionProbabilityPerStep = 0.0008; // הסתברות אינטראקציה (מכווננת)
    const cherenkovSpeedFactor = 1.2; // מהירות אור צ'רנקוב יחסית למהירות החלקיק (בתווך)
    const cherenkovMaxRadius = 60; // גודל מקסימלי של גל אור יחיד בסימולציה
    const cherenkovEmitInterval = 8; // לפלוט גל אור כל X צעדים של החלקיק המשני

    let animationFrameId = null;
    let simulationState = 'idle'; // 'idle', 'neutrino', 'interaction', 'light', 'hits_highlight'
    let neutrino = null;
    let interactionPoint = null;
    let secondaryParticle = null;
    let cherenkovWavefronts = []; // Stores { start: {x, y}, emittedAt: timestamp, id: unique_id }
    let hitDomsQueue = []; // Stores { domIndex: index, hitTime: timestamp } for ordered highlighting
    let neutrinosSentCount = 0;
    let interactionsDetectedCount = 0;
    let hitHighlightAnimationStartTime = null;
    const hitHighlightDuration = 800; //ms per DOM highlight animation

     // Get a unique ID for Cherenkov wavefronts
    let wavefrontIdCounter = 0;
    function getWavefrontId() { return wavefrontIdCounter++; }


    function setupCanvas() {
        const canvasContainer = document.getElementById('app');
        const containerWidth = canvasContainer.clientWidth - 50; // Account for app padding
        detectorWidth = Math.min(containerWidth, 600);
        detectorHeight = 400; // Keep height fixed
        canvas.width = detectorWidth;
        canvas.height = detectorHeight;

        // Recalculate DOM positions based on new canvas size
        const spacingX = (detectorWidth - 2 * paddingX) / (numDomsX > 1 ? numDomsX - 1 : 1);
        const spacingY = (detectorHeight - 2 * paddingY) / (numDomsY > 1 ? numDomsY - 1 : 1);
        doms.length = 0; // Clear existing DOMs
        for (let i = 0; i < numDomsX; i++) {
            for (let j = 0; j < numDomsY; j++) {
                doms.push({
                    x: paddingX + i * spacingX,
                    y: paddingY + j * spacingY,
                    hit: false,
                    earliestHitTime: Infinity, // Store the calculated earliest light arrival time
                    element: null // Placeholder for potential future DOM element representation or class toggle
                });
            }
        }
    }

    function drawDetector(timestamp) {
        ctx.clearRect(0, 0, detectorWidth, detectorHeight);
        // Draw gradient background
        const gradient = ctx.createLinearGradient(0, 0, 0, detectorHeight);
        gradient.addColorStop(0, '#e0f7fa'); // Light blue at top
        gradient.addColorStop(1, '#b2ebf2'); // Slightly darker blue at bottom
        ctx.fillStyle = gradient;
        ctx.fillRect(0, 0, detectorWidth, detectorHeight);


        // Draw DOMs
        doms.forEach((dom, index) => {
            ctx.beginPath();
            ctx.arc(dom.x, dom.y, domRadius, 0, Math.PI * 2);

            // Determine DOM color based on hit state and highlight animation
            let domColor = '#555'; // Default dark gray
            let strokeColor = '#333';
            let isHighlighted = false;

             if (simulationState === 'hits_highlight' && hitHighlightAnimationStartTime !== null) {
                const elapsedTime = timestamp - hitHighlightAnimationStartTime;
                // Check if this DOM is in the queue and its highlight time has passed
                const queueItem = hitDomsQueue.find(item => item.domIndex === index);
                if (queueItem) {
                     // Start highlight animation slightly before its hit time
                     const highlightStartOffset = 100; // ms before theoretical hit time
                     if (elapsedTime >= queueItem.relativeHighlightTime - highlightStartOffset) {
                        isHighlighted = true;
                        // Simple pulse effect based on elapsed time relative to its highlight start
                         const pulseTime = elapsedTime - (queueItem.relativeHighlightTime - highlightStartOffset);
                         const pulsePhase = (pulseTime % hitHighlightDuration) / hitHighlightDuration;
                         const scale = 1 + Math.sin(pulsePhase * Math.PI) * 0.3; // Scale between 1 and 1.3
                         const opacity = 0.7 + Math.sin(pulsePhase * Math.PI) * 0.3; // Opacity between 0.7 and 1

                        ctx.save(); // Save canvas state
                        ctx.translate(dom.x, dom.y); // Move origin to DOM center
                        ctx.scale(scale, scale); // Apply scaling
                        ctx.globalAlpha = opacity; // Apply opacity

                        domColor = '#ffeb3b'; // Yellow
                        strokeColor = '#fbc02d'; // Orange
                     }
                }
            } else if (dom.hit) {
                 // If not in sequential highlight mode, just show hit state
                 domColor = '#ffeb3b'; // Yellow if hit
                 strokeColor = '#fbc02d';
             }

            ctx.fillStyle = domColor;
            ctx.fill();
            ctx.strokeStyle = strokeColor;
            ctx.lineWidth = 1.5; // Slightly thicker stroke
            ctx.stroke();

            if (isHighlighted) {
                 ctx.restore(); // Restore canvas state
            }

        });

        ctx.strokeStyle = '#0e4d61';
        ctx.lineWidth = 3;
        ctx.strokeRect(0, 0, detectorWidth, detectorHeight); // Detector boundary
    }

    function drawNeutrino(pos) {
        ctx.beginPath();
        ctx.arc(pos.x, pos.y, 3, 0, Math.PI * 2); // Slightly larger neutrino dot
        ctx.fillStyle = '#616161'; // Dark gray
        ctx.fill();
    }

    function drawSecondaryParticle(path) {
         if (!path || path.length < 2) return;
         ctx.beginPath();
         // Draw the path as a thicker, more visible line
         ctx.moveTo(path[0].x, path[0].y);
         for(let i = 1; i < path.length; i++) {
             // Add smoothing? For now, straight lines are fine.
             ctx.lineTo(path[i].x, path[i].y);
         }
         ctx.strokeStyle = '#e53935'; // Red color for particle track
         ctx.lineWidth = 4; // Thicker line
         ctx.stroke();
    }

    function drawCherenkovWavefronts(wavefronts, timestamp) {
        wavefronts.forEach(wave => {
            const elapsedTime = timestamp - wave.emittedAt;
            // Calculate radius and opacity based on time and speed
            const radius = (elapsedTime / 16) * cherenkovSpeedFactor; // Divide by ~16ms for 60fps
            const opacity = Math.max(0, 0.7 - (radius / cherenkovMaxRadius)); // Fade out as it expands

            if (radius > cherenkovMaxRadius) return; // Stop drawing if too large/faded

            ctx.beginPath();
            ctx.arc(wave.start.x, wave.start.y, radius, 0, Math.PI * 2);
            ctx.strokeStyle = `rgba(3, 169, 244, ${opacity})`; // Light blue, fading
            ctx.lineWidth = 2;
            ctx.stroke();
        });
    }

     function getDistance(p1, p2) {
        return Math.sqrt(Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2));
    }

     function checkLineCircleIntersection(p1, p2, center, radius) {
        // Simplified check: Does the line segment [p1, p2] pass close enough to the circle center?
        // This is not perfect line-segment-to-circle intersection but simpler for visualization.
        // Check distance from circle center to the line defined by p1, p2.
        // If the points are the same, use point-circle distance.
        if (p1.x === p2.x && p1.y === p2.y) {
            return getDistance(p1, center) <= radius;
        }
        const dx = p2.x - p1.x;
        const dy = p2.y - p1.y;
        const lenSq = dx * dx + dy * dy; // Squared length of line segment

        // Project circle center onto the line (p1, p2)
        const t = ((center.x - p1.x) * dx + (center.y - p1.y) * dy) / lenSq;

        // Clamp t to [0, 1] to ensure the projection point is within the segment
        const tClamped = Math.max(0, Math.min(1, t));

        const projectionX = p1.x + tClamped * dx;
        const projectionY = p1.y + tClamped * dy;

        // Distance from circle center to the closest point on the line segment
        const distance = getDistance(center, { x: projectionX, y: projectionY });

        return distance <= radius; // Check if distance is within radius
     }


    function animateSimulation(timestamp) {
        drawDetector(timestamp); // Draw with potential DOM highlighting animation

        if (simulationState === 'neutrino') {
            drawNeutrino(neutrino.pos);

            // Move neutrino
            neutrino.pos.x += neutrino.dir.x * neutrinoSpeed;
            neutrino.pos.y += neutrino.dir.y * neutrinoSpeed;

            // Check boundaries (slightly outside to ensure it clears)
            if (neutrino.pos.x < -domRadius * 2 || neutrino.pos.x > detectorWidth + domRadius * 2 || neutrino.pos.y < -domRadius * 2 || neutrino.pos.y > detectorHeight + domRadius * 2) {
                // Neutrino left detector without interaction
                messageDiv.textContent = 'נייטרינו עבר דרך הגלאי ללא אינטראקציה. רובם עוברים ככה!';
                simulationState = 'idle'; // End simulation segment
                sendButton.disabled = false; // Re-enable button
            } else {
                // Check for interaction
                if (Math.random() < interactionProbabilityPerStep) {
                    interactionPoint = { x: neutrino.pos.x, y: neutrino.pos.y };
                    messageDiv.textContent = '🔥 אינטראקציה נדירה התרחשה! נוצר חלקיק משני.';
                    interactionsDetectedCount++;
                    interactionsDetectedSpan.textContent = `אינטראקציות זוהו: ${interactionsDetectedCount}`;

                     // Visual flash at interaction point
                    const flashDiv = document.createElement('div');
                    flashDiv.classList.add('interaction-flash');
                    flashDiv.style.position = 'absolute';
                    flashDiv.style.width = '30px';
                    flashDiv.style.height = '30px';
                    flashDiv.style.borderRadius = '50%';
                    flashDiv.style.backgroundColor = 'rgba(255, 0, 0, 0.5)';
                     // Position relative to canvas container, need to convert canvas coords
                     const canvasRect = canvas.getBoundingClientRect();
                     const appRect = document.getElementById('app').getBoundingClientRect();
                    flashDiv.style.left = `${canvasRect.left - appRect.left + interactionPoint.x - 15}px`;
                    flashDiv.style.top = `${canvasRect.top - appRect.top + interactionPoint.y - 15}px`;
                    flashDiv.style.pointerEvents = 'none'; // Don't block clicks

                    document.getElementById('app').style.position = 'relative'; // Make app container position relative for absolute children
                    document.getElementById('app').appendChild(flashDiv);
                     setTimeout(() => { flashDiv.remove(); }, 400); // Remove flash after animation


                    // Generate random direction for secondary particle
                    const angle = Math.random() * Math.PI * 2; // Random angle
                     // Small offset from interaction point to avoid drawing over it initially
                     const offsetDist = 5;
                    secondaryParticle = {
                        pos: { x: interactionPoint.x + Math.cos(angle) * offsetDist, y: interactionPoint.y + Math.sin(angle) * offsetDist },
                        dir: { x: Math.cos(angle), y: Math.sin(angle) },
                        path: [ { x: interactionPoint.x, y: interactionPoint.y }, { x: interactionPoint.x + Math.cos(angle) * offsetDist, y: interactionPoint.y + Math.sin(angle) * offsetDist } ],
                        steps: 0 // To control light emission points
                    };
                    // Reset DOMs and lights for new event
                    cherenkovWavefronts = [];
                    doms.forEach(dom => { dom.hit = false; dom.earliestHitTime = Infinity; });
                    hitDomsQueue = []; // Clear previous hits
                    simulationState = 'interaction'; // Move to next state
                }
            }
        }

        if (simulationState === 'interaction' || simulationState === 'light') {
             if (secondaryParticle) {
                 // Store previous position before moving
                 const prevPos = { x: secondaryParticle.pos.x, y: secondaryParticle.pos.y };

                 // Move secondary particle
                secondaryParticle.pos.x += secondaryParticle.dir.x * secondarySpeed;
                secondaryParticle.pos.y += secondaryParticle.dir.y * secondarySpeed;
                secondaryParticle.path.push({ x: secondaryParticle.pos.x, y: secondaryParticle.pos.y });
                secondaryParticle.steps++;

                // Emit Cherenkov light wavefront periodically along path from the *previous* point
                if (secondaryParticle.steps > 0 && secondaryParticle.steps % cherenkovEmitInterval === 0) {
                     const emitPoint = prevPos; // Emit from the position *before* the current move
                     cherenkovWavefronts.push({
                         start: { x: emitPoint.x, y: emitPoint.y },
                         emittedAt: timestamp,
                         id: getWavefrontId()
                     });
                }

                 // Check if secondary particle left detector
                if (secondaryParticle.pos.x < -domRadius * 2 || secondaryParticle.pos.x > detectorWidth + domRadius * 2 || secondaryParticle.pos.y < -domRadius * 2 || secondaryParticle.pos.y > detectorHeight + domRadius * 2) {
                    messageDiv.textContent += ' החלקיק המשני עזב את הגלאי. ממתינים לאותות אור...';
                    secondaryParticle = null; // End secondary particle phase
                    simulationState = 'light'; // Only light animation continues
                }
             }

            // Draw secondary particle path if still active
            if(secondaryParticle) {
                 drawSecondaryParticle(secondaryParticle.path);
            }


            // Move, draw and check hits for Cherenkov light wavefronts
            if (cherenkovWavefronts.length > 0) {
                 cherenkovWavefronts = cherenkovWavefronts.filter(wave => {
                    // Calculate current radius based on elapsed time
                    const elapsedTime = timestamp - wave.emittedAt;
                    const radius = (elapsedTime / 16) * cherenkovSpeedFactor; // ms to pixels per frame

                    // Check for DOM hits with this expanding wavefront
                    doms.forEach((dom, index) => {
                         // Check if the current wavefront's edge has reached or passed this DOM
                         // Distance from wavefront origin to DOM center
                         const distToDOM = getDistance(wave.start, dom);
                         // The light wavefront arrives at the DOM when its radius equals this distance.
                         // Calculated arrival time for *this specific wavefront* at this DOM
                         const theoreticalArrivalTime = wave.emittedAt + (distToDOM / cherenkovSpeedFactor) * 16; // Convert speed factor back to ms/pixel

                         // If this wavefront has reached the DOM radius AND it's the earliest hit for this DOM
                         if (radius >= distToDOM - domRadius && theoreticalArrivalTime < dom.earliestHitTime) {
                             dom.earliestHitTime = theoreticalArrivalTime; // Record the earliest time
                             if (!dom.hit) {
                                 dom.hit = true; // Mark as hit immediately for visual feedback
                                 // Add to potential hit queue for sequential highlighting AFTER simulation
                                 // Remove any older entries for this DOM before adding the new one
                                 hitDomsQueue = hitDomsQueue.filter(item => item.domIndex !== index);
                                 hitDomsQueue.push({ domIndex: index, hitTime: theoreticalArrivalTime });
                             }
                         }
                    });


                    // Remove wavefronts that are too large or far outside detector bounds
                    return radius <= cherenkovMaxRadius &&
                           wave.start.x + radius > -domRadius && wave.start.x - radius < detectorWidth + domRadius &&
                           wave.start.y + radius > -domRadius && wave.start.y - radius < detectorHeight + domRadius;
                 });

                 drawCherenkovWavefronts(cherenkovWavefronts, timestamp);

                 // Check if all light wavefronts have faded/left and secondary particle is gone
                 if (cherenkovWavefronts.length === 0 && secondaryParticle === null && simulationState === 'light') {
                      if (hitDomsQueue.length > 0) {
                         messageDiv.textContent = '💡 אותות קרינת צ\'רנקוב זוהו! מנתחים זמני הגעה...';
                         // Sort hit DOMs by their earliest arrival time
                         hitDomsQueue.sort((a, b) => a.hitTime - b.hitTime);

                         // Calculate relative highlight times based on the first hit time
                         const firstHitTime = hitDomsQueue[0].hitTime;
                         hitDomsQueue.forEach(item => {
                             item.relativeHighlightTime = item.hitTime - firstHitTime;
                         });

                         simulationState = 'hits_highlight'; // Move to highlight state
                         hitHighlightAnimationStartTime = timestamp; // Start the highlight timer
                         // The drawDetector function will handle the timed highlighting animation
                     } else {
                         // Should not happen if secondary particle interacted, but as a fallback
                          messageDiv.textContent += ' האותות דעכו ללא זיהוי ברור.';
                          simulationState = 'idle';
                           sendButton.disabled = false; // Re-enable button
                     }
                 }
            }
        }

        if (simulationState === 'hits_highlight') {
             const elapsedTime = timestamp - hitHighlightAnimationStartTime;

             // Check if highlighting is complete for all DOMs in the queue
             // The last DOM's highlight animation finishes after its relative time + duration
             const lastDomHighlightEndTime = hitDomsQueue[hitDomsQueue.length - 1].relativeHighlightTime + hitHighlightDuration;

             if (elapsedTime >= lastDomHighlightEndTime) {
                 messageDiv.textContent = `✅ אירוע שוחזר בהצלחה! (${hitDomsQueue.length} חיישנים הגיבו).`;
                 simulationState = 'idle'; // End highlighting phase
                 sendButton.disabled = false; // Re-enable button
                 // Reset DOM colors *after* animation ends
                 doms.forEach(dom => { dom.hit = false; });
             }
             // The actual drawing and highlighting is handled by drawDetector based on hitDomsQueue and timestamp
        }


        // Continue animation loop if any particle/light/highlight is active
        if (simulationState !== 'idle') {
             animationFrameId = requestAnimationFrame(animateSimulation);
        }
    }

    function resetSimulation() {
         cancelAnimationFrame(animationFrameId);
         animationFrameId = null;
         simulationState = 'idle';
         neutrino = null;
         interactionPoint = null;
         secondaryParticle = null;
         cherenkovWavefronts = [];
         hitDomsQueue = [];
         hitHighlightAnimationStartTime = null;
         doms.forEach(dom => { dom.hit = false; dom.earliestHitTime = Infinity; }); // Reset DOM state
         messageDiv.textContent = 'צפה כאן בהתקדמות... רובם יעברו דרך!';
         // Remove any lingering flash elements
         document.querySelectorAll('.interaction-flash').forEach(el => el.remove());
         drawDetector(); // Draw initial state
    }

    sendButton.addEventListener('click', () => {
        if (simulationState !== 'idle') return; // Prevent multiple simulations

        resetSimulation(); // Reset before starting a new one
        sendButton.disabled = true; // Disable button during simulation
        neutrinosSentCount++;
        neutrinosSentSpan.textContent = `נייטרינו שנשלחו: ${neutrinosSentCount}`;

        // Start neutrino from a random point just outside the top edge
        const startX = Math.random() * detectorWidth;
        const startY = -30; // Start further above the canvas
        // Aim towards a random point on the bottom edge
        const targetX = Math.random() * detectorWidth;
        const targetY = detectorHeight + 30; // Target further below canvas

        const dx = targetX - startX;
        const dy = targetY - startY;
        const distance = Math.sqrt(dx * dx + dy * dy);

        neutrino = {
            pos: { x: startX, y: startY },
            dir: { x: dx / distance, y: dy / distance } // Normalized direction vector
        };

        messageDiv.textContent = 'שולח נייטרינו קוסמי...';
        simulationState = 'neutrino'; // Start the neutrino phase
        // Start the animation loop
        animateSimulation(performance.now()); // Use high-resolution timestamp
    });

    // Toggle explanation visibility
    explanationButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            explanationButton.textContent = 'הסתר הסבר מפורט';
        } else {
            explanationDiv.style.display = 'none';
            explanationButton.textContent = 'הצג הסבר מפורט';
        }
    });

    // Initial setup and drawing
    setupCanvas();
    drawDetector(performance.now()); // Draw initial state


     // Make canvas responsive on window resize
     window.addEventListener('resize', () => {
         // Always reset on resize for simplicity, especially since positions change
         resetSimulation();
         setupCanvas(); // Adjust dimensions and DOM positions
         drawDetector(performance.now()); // Redraw static state
     });

      // Set initial explanation button text
     explanationButton.textContent = explanationDiv.style.display === 'none' ? 'הצג הסבר מפורט' : 'הסתר הסבר מפורט';


</script>
```