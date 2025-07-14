---
title: "קריפטו-סריגים: הצפנה עמידה לעתיד המחשוב הקוונטי"
english_slug: lattice-based-crypto-future-proof-encryption
category: "סייבר ואבטחת מידע"
tags:
  - קריפטוגרפיה
  - סריגים
  - פוסט-קוונטי
  - מתמטיקה דיסקרטית
  - הצפנה
---

# קריפטו-סריגים: הצפנה עמידה לעתיד המחשוב הקוונטי

דמיינו לעצמכם מרחב אינסופי, מעוטר ברשת מסתורית של נקודות מסודרות להפליא – סריג מתמטי. מציאת הנקודה 'הטובה ביותר' בתוך המבוך המימדי הזה – אולי הקרובה ביותר למטרה נתונה, או הקצרה ביותר מנקודת ההתחלה – נשמעת כמו חידה פשוטה. אך כשהמימדים מזנקים, החידה הופכת לבלתי-פתירה עבור המחשבים החזקים ביותר כיום. סוד מתמטי עמוק זה הוא הליבה של קריפטוגרפיה מבוססת סריגים, אחד התקווה הגדולות שלנו להגן על המידע שלנו בעידן שאחרי המחשוב הקוונטי.

## צללו לתוך הסריג: סימולציה אינטראקטיבית דו-ממדית

שחקו עם וקטורי הבסיס (v1 ו-v2) באמצעות המחוונים וראו כיצד הסריג כולו מתעצב מחדש בזמן אמת! חקרו את מבנה הנקודות. האם אתם יכולים לזהות את הוקטור הקצר ביותר היוצא מראשית הצירים (SVP)? או למצוא את נקודת הסריג הקרובה ביותר לנקודת המטרה האדומה (CVP)? הפעלת "רעש" ממחישה כיצד קושי קטן מוביל לבעיה קשה בהרבה (בעיית הלמידה עם שגיאות - LWE).

<div class="lattice-app-container">
    <canvas id="latticeCanvas" width="700" height="500"></canvas>
    <div class="controls">
        <h3>עצבו את הסריג: וקטורי בסיס</h3>
        <div class="control-group">
            <h4>וקטור v1:</h4>
            <div>
                <label for="v1x">X:</label>
                <input type="range" id="v1x" min="-250" max="250" value="100">
                <span id="v1xValue">100</span>
            </div>
            <div>
                <label for="v1y">Y:</label>
                <input type="range" id="v1y" min="-250" max="250" value="0">
                <span id="v1yValue">0</span>
            </div>
        </div>
         <div class="control-group">
             <h4>וקטור v2:</h4>
            <div>
                <label for="v2x">X:</label>
                <input type="range" id="v2x" min="-250" max="250" value="0">
                <span id="v2xValue">0</span>
            </div>
            <div>
                <label for="v2y">Y:</label>
                <input type="range" id="v2y" min="-250" max="250" value="100">
                <span id="v2yValue">100</span>
            </div>
         </div>

        <h3>הדגמות קריפטוגרפיות:</h3>
        <button id="modeSVP">בעיית הוקטור הקצר (SVP)</button>
        <button id="modeCVP">בעיית הוקטור הקרוב (CVP)</button>
        <button id="generateTarget">נקודת מטרה אקראית (ל-CVP)</button>

        <div class="noise-option">
            <input type="checkbox" id="addNoise">
            <label for="addNoise">הוסף 'רעש' (המחשת LWE)</label>
        </div>

        <div class="info-area">
            <h4>מה רואים?</h4>
            <p><strong>SVP:</strong> הוקטור האדום הוא הוקטור הקצר ביותר בסריג (לא אפס).</p>
            <p><strong>CVP:</strong> הנקודה הירוקה היא נקודת הסריג הקרובה ביותר למטרה האדומה. הקו הירוק מחבר ביניהן.</p>
            <p><strong>רעש (LWE):</strong> מוסיף שינויים קטנים לוקטורי הבסיס ולנקודת המטרה, מה שמדמה מידע לא מושלם והופך את מציאת הפתרון המדויק לקשה בהרבה (תחושת "ניקוד" עשויה להופיע).</p>
        </div>
    </div>
</div>

<style>
    /* Basic Reset and Typography */
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica Neue, Arial, sans-serif;
        line-height: 1.6;
        color: #333;
    }

    h1, h2, h3, h4 {
        color: #1a1a1a;
        margin-top: 1.5em;
        margin-bottom: 0.5em;
    }

    p, ul {
        margin-bottom: 1em;
    }

    /* Layout and Container */
    .lattice-app-container {
        display: flex;
        flex-wrap: wrap; /* Allows stacking on small screens */
        gap: 25px; /* More space between canvas and controls */
        margin: 30px 0;
        background-color: #f8f8f8; /* Light background for the section */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }

    canvas {
        flex-grow: 1; /* Allows canvas to take up available space */
        min-width: 300px; /* Minimum size */
        border: 1px solid #ccc;
        background-color: #fff; /* White background for drawing area */
        display: block;
        border-radius: 8px;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.05); /* Inner shadow */
    }

    .controls {
        flex-basis: 300px; /* Minimum width for controls */
        flex-grow: 0; /* Don't let controls grow */
        background-color: #eee;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .control-group {
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 1px solid #ddd;
    }

    .control-group h4 {
        margin-top: 0;
        margin-bottom: 10px;
        color: #555;
    }

    .controls div {
        margin-bottom: 10px;
        display: flex; /* Use flex for alignment */
        align-items: center;
    }

    .controls label {
        display: inline-block;
        width: 30px; /* Adjust width */
        font-weight: bold;
        color: #555;
        margin-right: 10px;
    }

    .controls input[type="range"] {
        flex-grow: 1; /* Allows slider to fill space */
        margin-right: 10px;
    }

    .controls span {
        display: inline-block;
        width: 40px; /* Adjust width */
        text-align: right;
        font-variant-numeric: tabular-nums; /* Align numbers */
        color: #333;
    }

    /* Buttons */
    .controls button {
        margin-right: 10px;
        margin-bottom: 10px;
        padding: 10px 15px;
        cursor: pointer;
        border: none;
        border-radius: 5px;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

     .controls button:hover {
        transform: translateY(-1px); /* Subtle lift effect */
     }
     .controls button:active {
        transform: translateY(0);
     }

     #modeSVP {
        background-color: #007bff; /* Blue */
        color: white;
     }
     #modeSVP:hover {
        background-color: #0056b3;
     }

     #modeCVP {
        background-color: #6f42c1; /* Purple */
        color: white;
     }
     #modeCVP:hover {
         background-color: #563d7c;
     }

     #generateTarget {
        background-color: #28a745; /* Green */
        color: white;
     }
     #generateTarget:hover {
        background-color: #218838;
     }

    .noise-option {
        margin-top: 15px;
        padding-top: 15px;
        border-top: 1px solid #ddd;
        display: flex;
        align-items: center;
    }
    .noise-option input[type="checkbox"] {
        margin-right: 8px;
        /* Style checkbox if needed */
    }
     .noise-option label {
        font-weight: bold;
        color: #555;
        width: auto; /* Override label width */
     }


    /* Info Area */
    .info-area {
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid #ccc;
        font-size: 0.9em;
        color: #555;
    }
     .info-area h4 {
         margin-top: 0;
         color: #555;
     }
    .info-area p {
        margin-bottom: 8px;
    }
    .info-area strong {
        color: #333;
    }

    /* Explanation Section */
    #explanationButton {
        display: block;
        margin: 30px auto; /* Center the button */
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 5px;
        background-color: #6c757d; /* Grey */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }
    #explanationButton:hover {
        background-color: #5a6268;
        transform: translateY(-1px);
    }
     #explanationButton:active {
        transform: translateY(0);
     }

    #explanation {
        display: none; /* Initially hidden */
        margin-top: 20px;
        padding: 25px;
        background-color: #f0f0f0;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    #explanation h2 {
        margin-top: 0;
        color: #333;
        border-bottom: 1px solid #ccc;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }
    #explanation h3 {
        margin-top: 20px;
        margin-bottom: 8px;
        color: #555;
    }
     #explanation ul {
         margin-left: 20px;
     }
     #explanation li {
         margin-bottom: 5px;
     }
</style>

<button id="explanationButton">מה עומד מאחורי זה? הצג/הסתר הסבר מורחב</button>

<div id="explanation">
    <h2>מהם קריפטו-סריגים? הסבר מורחב</h2>

    <h3>מהו סריג מתמטי?</h3>
    <p>סריג מתמטי, בהקשר הקריפטוגרפי, הוא למעשה אינסוף נקודות בחלל רב-מימדי, שנוצרות על ידי שילובים שלמים של וקטורי בסיס. דמיינו שיש לכם כמה "צעדי בסיס" מוגדרים (הווקטורים) – הסריג כולל כל נקודה אליה תוכלו להגיע מנקודת ההתחלה (האפס) על ידי ביצוע רק מספר שלם (חיובי או שלילי, כולל אפס) של כל אחד מצעדי הבסיס.</p>
    <p>פורמלית, אם וקטורי הבסיס הם \(v_1, v_2, \dots, v_n\), הסריג הוא כל הנקודות מהצורה \(c_1 v_1 + c_2 v_2 + \dots + c_n v_n\), כאשר \(c_1, c_2, \dots, c_n\) חייבים להיות <strong>מספרים שלמים בלבד</strong>.</p>
    <p>הסימולציה למעלה מציגה סריג דו-ממדי ( \(n=2\) ), שבו הנקודות נוצרות על ידי צירופים שלמים של שני וקטורי בסיס (\(v_1, v_2\)). נקודות הסריג הן מהצורה \(c_1 v_1 + c_2 v_2\) עבור כל שלמים \(c_1, c_2\). עובדה מעניינת היא שסטים שונים של וקטורי בסיס יכולים ליצור בדיוק את אותו אוסף של נקודות סריג!</p>

    <h3>הבעיות הקשות בסריגים: SVP ו-CVP</h3>
    <p>החוזק של קריפטוגרפיה מבוססת סריגים נובע מקיומן של בעיות מתמטיות שנחשבות קשות מאד לפתרון יעיל, במיוחד במימדים גבוהים. שתיים מהחשובות ביותר הן:</p>
    <ul>
        <li><strong>בעיית הוקטור הקצר ביותר (SVP - Shortest Vector Problem):</strong> מצא את הוקטור הקצר ביותר (בעל האורך המינימלי) בסריג, שאינו וקטור האפס.</li>
        <li><strong>בעיית הוקטור הקרוב ביותר (CVP - Closest Vector Problem):</strong> נתונה נקודת מטרה כלשהי בחלל (שאינה בהכרח חלק מהסריג), מצא את נקודת הסריג הקרובה ביותר אליה.</li>
    </ul>
    <p>קיימים קשרים מורכבים בין הבעיות הללו, ופתרון יעיל של האחת לרוב מסייע גם בפתרון השנייה.</p>

    <h3>מדוע הבעיות הללו קשות?</h3>
    <p>כפי שניתן לראות בדוגמה הדו-ממדית, קל יחסית לאתר ויזואלית את הוקטור הקצר ביותר או הנקודה הקרובה ביותר. אך הדברים משתנים דרמטית כשעוברים למימדים רבים – מאות או אפילו אלפי מימדים. בחלל רב-מימדי כזה, מספר נקודות הסריג הפוטנציאליות גדל באופן עצום, והוקטורים "מתפשטים" בצורה שמקשה למצוא את "הקצר ביותר" או "הקרוב ביותר" ביעילות. למרות עשרות שנים של מחקר אינטנסיבי, לא נמצאו אלגוריתמים שיכולים לפתור בעיות אלו במהירות מספקת (בזמן "פולינומיאלי") עבור סריגים אקראיים או סריגים מהסוג המשמש בקריפטוגרפיה, אפילו עבור המחשבים הקלאסיים החזקים ביותר.</p>

    <h3>בעיית הלמידה עם שגיאות (LWE - Learning With Errors)</h3>
    <p>בעיית LWE היא וריאנט של בעיות הסריגים, והיא מהווה אבן פינה באלגוריתמים קריפטוגרפיים מבוססי סריגים. היא ניתנת לתיאור כניסיון לחלץ "סוד" מתוך מערכת משוואות לינאריות, אלא שלכל משוואה מוסף "רעש" קטן ואקראי. הרעש הזה הופך את הבעיה מקשה "במקרה הגרוע ביותר" (מציאת נקודה מדויקת) לקשה "במקרה הממוצע" (מציאת סוד בנוכחות אי-דיוקים) – מה שמתאים יותר לבניית מערכות קריפטוגרפיות שעובדות באמינות.</p>
    <p>הוספת ה"רעש" בסימולציה נועדה לתת תחושה פשטנית כיצד אי-דיוקים קטנים (שיכולים לייצג רעש במערכת או את עצם ההצפנה) יכולים לטשטש את המבנה המדויק של הסריג ולהפוך את מציאת הנקודות המדויקות (או הקרובות ביותר) למשימה הרבה יותר מורכבת, גם במימד נמוך כמו 2D.</p>

    <h3>קריפטוגרפיה מבוססת סריגים: היישום</h3>
    <p>אלגוריתמים קריפטוגרפיים כמו Kyber (להצפנה וחילופי מפתחות) ו-Dilithium (לחתימות דיגיטליות) - שנבחרו שניהם לתקנים פוסט-קוונטיים על ידי NIST - מבוססים על הקושי שבפתרון בעיות דמויות LWE בסריגים במימדים גבוהים. פעולות הצפנה/פענוח או חתימה/אימות מתוכננות כך שמי שמחזיק ב"מפתח" (למשל, בסיס "טוב" לסריג או הסוד בבעיית LWE) יכול לבצע אותן בקלות. לעומת זאת, מי שמנסה "לפרוץ" ללא המפתח נאלץ למעשה לפתור בעיה קשה מאד בסריג המתאים, וזה מה שמבטיח את בטחון המערכת.</p>

    <h3>עמידות פוסט-קוונטית</h3>
    <p>היתרון העיקרי והמרגש ביותר של קריפטו-סריגים הוא עמידותם המשוערת מפני מחשבים קוונטיים בקנה מידה גדול. אלגוריתמים קריפטוגרפיים קלאסיים שנמצאים בשימוש נרחב כיום, כמו RSA ו-ECC, פגיעים לאלגוריתם שור (Shor's algorithm) שמריץ מחשב קוונטי חזק. לעומת זאת, נכון להיום, לא ידוע על אלגוריתם קוונטי שיכול לפתור את בעיות ה-SVP, CVP או LWE במימדים גבוהים באופן יעיל משמעותית מאלגוריתמים קלאסיים. זו הסיבה המרכזית לכך שקריפטו-סריגים נחשבים כמועמדים המובילים להחליף את שיטות ההצפנה הקלאסיות בעתיד, ולהבטיח את פרטיותנו וביטחוננו בעידן המחשוב הקוונטי.</p>
</div>


<script>
    const canvas = document.getElementById('latticeCanvas');
    const ctx = canvas.getContext('2d');
    const v1xInput = document.getElementById('v1x');
    const v1yInput = document.getElementById('v1y');
    const v2xInput = document.getElementById('v2x');
    const v2yInput = document.getElementById('v2y');
    const v1xValue = document.getElementById('v1xValue');
    const v1yValue = document.getElementById('v1yValue');
    const v2xValue = document.getElementById('v2xValue');
    const v2yValue = document.getElementById('v2yValue');
    const modeSVPButton = document.getElementById('modeSVP');
    const modeCVPButton = document.getElementById('modeCVP');
    const generateTargetButton = document.getElementById('generateTarget');
    const addNoiseCheckbox = document.getElementById('addNoise');
    const explanationButton = document.getElementById('explanationButton');
    const explanationDiv = document.getElementById('explanation');

    let originX = canvas.width / 2;
    let originY = canvas.height / 2;
    let scale = 0.8; // Adjust scale
    const maxCombinations = 12; // Limit points drawn for performance and visual clarity

    let v1 = { x: parseInt(v1xInput.value), y: parseInt(v1yInput.value) };
    let v2 = { x: parseInt(v2xInput.value), y: parseInt(v2yInput.value) };
    let targetPoint = null;
    let currentMode = 'SVP';

    let animationFrameId = null;
    let noiseMagnitude = 10; // How much points jiggle with noise
    let noiseOffset = { x: 0, y: 0 }; // For jiggle animation


    function drawGrid() {
        ctx.strokeStyle = '#ddd';
        ctx.lineWidth = 0.5;
        // Draw main axes
        ctx.beginPath();
        ctx.moveTo(0, originY);
        ctx.lineTo(canvas.width, originY);
        ctx.moveTo(originX, 0);
        ctx.lineTo(originX, canvas.height);
        ctx.stroke();

         // Draw origin point
         ctx.fillStyle = '#333';
         ctx.beginPath();
         ctx.arc(originX, originY, 4, 0, Math.PI * 2);
         ctx.fill();
    }

    function addNoiseToVector(vector) {
        if (!addNoiseCheckbox.checked) return { x: vector.x, y: vector.y };
        const noiseMag = 5; // Smaller noise for basis vectors affecting overall structure
        const noiseX = (Math.random() - 0.5) * 2 * noiseMag;
        const noiseY = (Math.random() - 0.5) * 2 * noiseMag;
        return { x: vector.x + noiseX, y: vector.y + noiseY };
    }

     function addNoiseToPoint(point) {
         if (!addNoiseCheckbox.checked) return { x: point.x, y: point.y };
         const noiseMag = 15; // Noise for target point
         const noiseX = (Math.random() - 0.5) * 2 * noiseMag;
         const noiseY = (Math.random() - 0.5) * 2 * noiseMag;
         return { x: point.x + noiseX, y: point.y + noiseY };
     }

    function drawArrowhead(ctx, fromX, fromY, toX, toY, color) {
        const headLength = 10;
        const headWidth = 8;
        const angle = Math.atan2(toY - fromY, toX - fromX);

        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.moveTo(toX, toY);
        ctx.lineTo(toX - headLength * Math.cos(angle - Math.PI / 6), toY - headLength * Math.sin(angle - Math.PI / 6));
        ctx.lineTo(toX - headLength * Math.cos(angle + Math.PI / 6), toY - headLength * Math.sin(angle + Math.PI / 6));
        ctx.closePath();
        ctx.fill();
    }

    function drawLatticePoints() {
        const noisyV1 = addNoiseToVector(v1);
        const noisyV2 = addNoiseToVector(v2);

        ctx.fillStyle = '#00008B'; // Dark blue for lattice points
        ctx.lineWidth = 1;

         const currentTime = Date.now(); // For noise jiggle animation

        // Draw lattice points
        for (let i = -maxCombinations; i <= maxCombinations; i++) {
            for (let j = -maxCombinations; j <= maxCombinations; j++) {
                 const idealPointX = i * noisyV1.x + j * noisyV2.x;
                 const idealPointY = i * noisyV1.y + j * noisyV2.y;

                 let pointX = originX + idealPointX * scale;
                 let pointY = originY - idealPointY * scale; // Y axis is inverted on canvas

                 if (addNoiseCheckbox.checked) {
                     // Add subtle, time-based jiggle for noise effect
                     const jiggleMagnitude = noiseMagnitude * (Math.sin(currentTime / 200 + i * 0.5 + j * 0.7) + 1) / 4; // Varies per point over time
                      pointX += (Math.random() - 0.5) * jiggleMagnitude;
                      pointY += (Math.random() - 0.5) * jiggleMagnitude;
                 }


                 // Check if point is within canvas bounds (with a margin)
                 const margin = 20;
                 if (pointX >= -margin && pointX <= canvas.width + margin && pointY >= -margin && pointY <= canvas.height + margin) {
                    ctx.beginPath();
                    ctx.arc(pointX, pointY, 3, 0, Math.PI * 2);
                    ctx.fill();
                 }
            }
        }
    }

    function drawBasisVectors() {
         const noisyV1 = addNoiseToVector(v1);
         const noisyV2 = addNoiseToVector(v2);

        // Draw basis vectors with arrowheads
        ctx.strokeStyle = '#007bff'; // Blue
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(originX, originY);
        ctx.lineTo(originX + noisyV1.x * scale, originY - noisyV1.y * scale);
        ctx.stroke();
        drawArrowhead(ctx, originX, originY, originX + noisyV1.x * scale, originY - noisyV1.y * scale, '#007bff');


        ctx.strokeStyle = '#ff7f00'; // Orange
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(originX, originY);
        ctx.lineTo(originX + noisyV2.x * scale, originY - noisyV2.y * scale);
        ctx.stroke();
        drawArrowhead(ctx, originX, originY, originX + noisyV2.x * scale, originY - noisyV2.y * scale, '#ff7f00');
    }

    function getLatticePoints() {
         const noisyV1 = addNoiseToVector(v1);
         const noisyV2 = addNoiseToVector(v2);
         const points = [];
         // Calculate points within a wider range for accurate SVP/CVP
         const calcCombinations = 15; // Use a larger range for calculation than drawing
         for (let i = -calcCombinations; i <= calcCombinations; i++) {
             for (let j = -calcCombinations; j <= calcCombinations; j++) {
                 const point = {
                     x: i * noisyV1.x + j * noisyV2.x,
                     y: i * noisyV1.y + j * noisyV2.y
                 };
                 points.push(point);
             }
         }
         return points;
    }


    function drawSVP() {
        const points = getLatticePoints();
        let shortestVector = null;
        let minLengthSq = Infinity;

        // Find the shortest non-zero vector
        points.forEach(p => {
            if (p.x === 0 && p.y === 0) return; // Exclude zero vector
             const lengthSq = p.x * p.x + p.y * p.y;
            if (lengthSq < minLengthSq) {
                minLengthSq = lengthSq;
                shortestVector = p;
            } else if (lengthSq === minLengthSq) {
                // Handle cases with multiple shortest vectors - pick one deterministically
                if (!shortestVector || p.x < shortestVector.x || (p.x === shortestVector.x && p.y < shortestVector.y)) {
                     shortestVector = p;
                }
            }
        });

        if (shortestVector) {
            ctx.strokeStyle = '#dc3545'; // Red
            ctx.lineWidth = 3; // Thicker line for the solution
            ctx.beginPath();
            ctx.moveTo(originX, originY);
            ctx.lineTo(originX + shortestVector.x * scale, originY - shortestVector.y * scale);
            ctx.stroke();
            drawArrowhead(ctx, originX, originY, originX + shortestVector.x * scale, originY - shortestVector.y * scale, '#dc3545');

             // Add a pulsing effect to the end point
             if (animationFrameId) { // Only pulse if animation loop is active
                 const pulseTime = Date.now() / 200; // Adjust speed
                 const pulseSize = 5 + Math.sin(pulseTime) * 2; // Pulsates between 3 and 7
                 ctx.fillStyle = '#dc3545';
                 ctx.beginPath();
                 ctx.arc(originX + shortestVector.x * scale, originY - shortestVector.y * scale, pulseSize, 0, Math.PI * 2);
                 ctx.fill();
             } else { // Draw static larger point if not animating
                 ctx.fillStyle = '#dc3545';
                 ctx.beginPath();
                 ctx.arc(originX + shortestVector.x * scale, originY - shortestVector.y * scale, 5, 0, Math.PI * 2);
                 ctx.fill();
             }
        }
    }

     function drawCVP() {
        if (!targetPoint) return;

        const noisyTarget = addNoiseToPoint(targetPoint);

        // Draw the target point
        ctx.fillStyle = '#dc3545'; // Red
        ctx.beginPath();
        ctx.arc(originX + noisyTarget.x * scale, originY - noisyTarget.y * scale, 6, 0, Math.PI * 2); // Slightly larger
        ctx.fill();
        // Draw a small circle around the target point
         ctx.strokeStyle = '#dc3545';
         ctx.lineWidth = 1.5;
         ctx.beginPath();
         ctx.arc(originX + noisyTarget.x * scale, originY - noisyTarget.y * scale, 9, 0, Math.PI * 2);
         ctx.stroke();


        // Find the closest lattice point
        const points = getLatticePoints();
        let closestPoint = null;
        let minDistSq = Infinity;

        points.forEach(p => {
             const distSq = Math.pow(p.x - noisyTarget.x, 2) + Math.pow(p.y - noisyTarget.y, 2);
             if (distSq < minDistSq) {
                 minDistSq = distSq;
                 closestPoint = p;
             }
        });

        if (closestPoint) {
            ctx.strokeStyle = '#28a745'; // Green
            ctx.lineWidth = 3; // Thicker line
            // Draw line from target to closest point
             ctx.beginPath();
             ctx.moveTo(originX + noisyTarget.x * scale, originY - noisyTarget.y * scale);
             ctx.lineTo(originX + closestPoint.x * scale, originY - closestPoint.y * scale);
             ctx.stroke();

             // Highlight the closest lattice point
             ctx.fillStyle = '#28a745'; // Green
             ctx.beginPath();
             ctx.arc(originX + closestPoint.x * scale, originY - closestPoint.y * scale, 6, 0, Math.PI * 2); // Slightly larger
             ctx.fill();

             // Add a pulsing effect to the closest point
             if (animationFrameId) { // Only pulse if animation loop is active
                 const pulseTime = Date.now() / 200 + 0.2; // Slightly offset pulse
                 const pulseSize = 5 + Math.sin(pulseTime) * 2;
                 ctx.strokeStyle = '#28a745';
                 ctx.lineWidth = 2;
                 ctx.beginPath();
                 ctx.arc(originX + closestPoint.x * scale, originY - closestPoint.y * scale, pulseSize, 0, Math.PI * 2);
                 ctx.stroke();
             } else { // Draw static circle if not animating
                 ctx.strokeStyle = '#28a745';
                 ctx.lineWidth = 2;
                 ctx.beginPath();
                 ctx.arc(originX + closestPoint.x * scale, originY - closestPoint.y * scale, 8, 0, Math.PI * 2);
                 ctx.stroke();
             }

        }
     }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        drawGrid();
        drawBasisVectors();
        drawLatticePoints(); // Draw points after vectors for layering

        // Draw SVP or CVP specific elements
        if (currentMode === 'SVP') {
            drawSVP();
        } else if (currentMode === 'CVP' && targetPoint) {
             drawCVP();
        }

        // If noise is on, request next frame for jiggle/pulse
        if (addNoiseCheckbox.checked || currentMode === 'SVP' || currentMode === 'CVP') {
             animationFrameId = requestAnimationFrame(draw);
        } else {
            animationFrameId = null; // Stop animation if no active animation effect
        }
    }

    function updateValues() {
        v1xValue.textContent = v1xInput.value;
        v1yValue.textContent = v1yInput.value;
        v2xValue.textContent = v2xInput.value;
        v2yValue.textContent = v2yInput.value;

        v1 = { x: parseInt(v1xInput.value), y: parseInt(v1yInput.value) };
        v2 = { x: parseInt(v2xInput.value), y: parseInt(v2yInput.value) };

        // Restart animation loop if it was stopped and noise is on
        if ((addNoiseCheckbox.checked || currentMode === 'SVP' || currentMode === 'CVP') && !animationFrameId) {
             draw();
        } else if (animationFrameId) {
             // If animating, the next frame will pick up the changes
        } else {
             // If not animating and noise is off, just draw static
             draw();
        }
    }

    function generateRandomTarget() {
         // Generate a target point within a reasonable range relative to basis vectors
         const maxCoord = Math.max(
             Math.abs(v1.x * maxCombinations), Math.abs(v1.y * maxCombinations),
             Math.abs(v2.x * maxCombinations), Math.abs(v2.y * maxCombinations),
             canvas.width / (2*scale), canvas.height / (2*scale) // Max display range
         );
         const range = Math.min(maxCoord * 0.7, 300); // Cap the range

         targetPoint = {
             x: (Math.random() - 0.5) * 2 * range,
             y: (Math.random() - 0.5) * 2 * range
         };
         // Restart animation if stopped
         if (!animationFrameId) {
              draw();
         }
     }

    // --- Event Listeners ---
    v1xInput.addEventListener('input', updateValues);
    v1yInput.addEventListener('input', updateValues);
    v2xInput.addEventListener('input', updateValues);
    v2yInput.addEventListener('input', updateValues);

    addNoiseCheckbox.addEventListener('change', () => {
         // Restart animation loop if noise is turned on, or stop if turned off
         if (addNoiseCheckbox.checked || currentMode === 'SVP' || currentMode === 'CVP') {
             if (!animationFrameId) draw();
         } else {
             if (animationFrameId) cancelAnimationFrame(animationFrameId);
             animationFrameId = null;
             draw(); // Draw one final static frame
         }
    });


    modeSVPButton.addEventListener('click', () => {
        currentMode = 'SVP';
        generateTargetButton.style.display = 'none';
        if (!animationFrameId) draw(); // Ensure animation starts for pulse
    });

    modeCVPButton.addEventListener('click', () => {
        currentMode = 'CVP';
        generateTargetButton.style.display = 'inline-block';
        if (!targetPoint) {
             generateRandomTarget();
        }
        if (!animationFrameId) draw(); // Ensure animation starts for pulse
    });

    generateTargetButton.addEventListener('click', generateRandomTarget);

    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר הסבר מורחב' : 'מה עומד מאחורי זה? הצג/הסתר הסבר מורחב';
    });

    // --- Initial Setup ---
    // Adjust scale based on canvas size
    scale = Math.min(canvas.width, canvas.height) / 500 * 0.8; // Dynamic scale adjustment
    originX = canvas.width / 2;
    originY = canvas.height / 2;

    updateValues(); // Draw initial state
    generateRandomTarget(); // Generate initial target for CVP mode

    // Set initial mode and button visibility
    modeSVPButton.click(); // Start in SVP mode


</script>