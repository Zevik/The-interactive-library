---
title: "גיאומטריה קסומה: הסוד המתמטי של אשר"
english_slug: magical-geometry-eschers-mathematical-secret
category: "מדעים מדויקים / מתמטיקה"
tags:
  - גיאומטריה היפרבולית
  - אשר
  - ריצוף
  - מודל פואנקרה
  - אמנות ומתמטיקה
---
# גיאומטריה קסומה: הסוד המתמטי של אשר

הדפסי הריצוף האינסופיים והמרתקים של מ.ק. אשר ריתקו מיליונים ברחבי העולם. אך האם ידעתם שהם לא רק יצירות אמנות מרהיבות, אלא גם הדגמה ויזואלית של סוג נדיר ומרתק של גיאומטריה? בואו נחקור את העולם המתמטי הנסתר שמאחורי יצירותיו ונשחק עם החוקים המפתיעים של המרחב ההיפרבולי.

<div id="app-container">
    <canvas id="poincareCanvas"></canvas>
    <p id="canvas-instructions">גררו בתוך העיגול כדי לשוטט במרחב ההיפרבולי. השתמשו בגלגלת העכבר לזום פנימה והחוצה.</p>
</div>

<style>
    /* סגנונות כלליים לקונטיינר ולכפתור */
    #app-container {
        text-align: center;
        margin-bottom: 30px;
        padding: 20px;
        background-color: #f0f4f8; /* Light blue background */
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    #poincareCanvas {
        border: 2px solid #a0b0c0; /* Subtle border */
        border-radius: 50%; /* Make canvas look like a disk outline */
        background-color: #ffffff; /* White background for the disk */
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1); /* Inner shadow */
        display: block; /* Center the canvas */
        margin: 0 auto 15px auto;
        cursor: grab; /* Default cursor */
    }

    #poincareCanvas:active {
         cursor: grabbing; /* Cursor when dragging */
    }

    #canvas-instructions {
        font-style: italic;
        color: #555;
        margin-top: 10px;
        font-size: 0.9em;
    }

    #toggleExplanation {
        display: block;
        margin: 20px auto;
        padding: 12px 25px;
        font-size: 1em;
        color: #fff;
        background-color: #007bff; /* Primary blue */
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 123, 255, 0.3);
    }

    #toggleExplanation:hover {
        background-color: #0056b3; /* Darker blue on hover */
    }

    #explanation {
        margin-top: 30px;
        padding: 20px;
        border: 1px solid #d0d0d0;
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        display: none; /* Initially hidden */
        text-align: right; /* Adjust text alignment if needed */
        line-height: 1.7;
        font-family: 'Arial', sans-serif; /* Better font */
        color: #333; /* Darker text color */
    }

    #explanation h2 {
        margin-top: 0;
        margin-bottom: 15px;
        border-bottom: 2px solid #007bff; /* Blue accent */
        padding-bottom: 10px;
        color: #007bff; /* Blue heading */
        font-size: 1.8em;
    }

    #explanation p, #explanation li {
        margin-bottom: 15px;
        font-size: 1.1em;
    }

    #explanation strong {
        color: #0056b3; /* Darker blue for emphasis */
    }
</style>

<button id="toggleExplanation">הצג הסבר על גיאומטריה היפרבולית ואשר</button>

<div id="explanation">
    <h2>הסבר: מסע אל המרחב ההיפרבולי דרך העיניים של אשר</h2>

    <p>ברוב חיינו, אנו פועלים תחת ההנחות של <strong>גיאומטריה אוקלידית</strong> – הגיאומטריה ה"שטוחה" והמוכרת לנו מכדור הארץ (במבט מקומי). בגיאומטריה הזו, ישרים מקבילים לעולם לא ייפגשו, וסכום הזוויות בכל משולש הוא בדיוק 180 מעלות.</p>

    <p>אבל דמיינו לרגע עולם שונה לחלוטין. עולם שבו דרך נקודה אחת מחוץ לישר, עוברים <em>אינסוף</em> ישרים שמקבילים לו! זהו אחד המאפיינים המסקרנים של <strong>גיאומטריה היפרבולית</strong>. בעולם כזה, משולשים מתנהגים אחרת: סכום הזוויות שלהם תמיד <em>קטן</em> מ-180 מעלות, והצורות מתכווצות ככל שמתרחקים ממרכז מסוים, למרות שגודלן ה"אמיתי" (היפרבולי) נשאר זהה.</p>

    <p>קשה לדמיין מרחב היפרבולי באופן ישיר. לכן, מתמטיקאים משתמשים ב<strong>מודלים</strong> – ייצוגים של המרחב ההיפרבולי על משטחים שאנו יכולים לדמיין (כמו מישור אוקלידי). המודל שתראו כאן הוא <strong>מודל דיסק פואנקרה</strong>. במודל זה, המרחב ההיפרבולי הוא החלק הפנימי של עיגול (דיסק). ה"קווים הישרים" ההיפרבוליים מיוצגים על ידי קשתות מעגלים או קטרים החוצים את שפת הדיסק בזווית ישרה. הקסם נוצר מכך שהמרחק בין נקודות בתוך הדיסק מוגדר באופן מיוחד – הוא גדל באופן דרמטי ככל שמתקרבים לשוליים. מבחינה היפרבולית, השוליים נמצאים במרחק אינסופי!</p>

    <p>התוצאה החזותית של הגדרת המרחק הזו היא שצורות בגודל היפרבולי קבוע נראות לנו (בעיניים אוקלידיות) קטנות יותר ויותר ככל שהן מתקרבות לשפת הדיסק. זה מאפשר "לדחוס" אינסוף עותקים של צורה נתונה לתוך הדיסק, במה שנקרא <strong>ריצוף היפרבולי</strong>. שלא כמו במישור האוקלידי, שבו רק ריצופים בסיסיים אפשריים (ריבועים, משולשים שווי צלעות, משושים משוכללים), במרחב היפרבולי ניתן לרצף את המישור באינסוף דרכים ועם אינסוף סוגים של מצולעים (וגם צורות מורכבות יותר!).</p>

    <p>האמן ההולנדי הגאון <strong>מ.ק. אשר (M.C. Escher)</strong> נתקל במושגים הללו דרך קשרים עם מתמטיקאים. למרות שלא היה מתמטיקאי פורמלי, הוא הבין את העיקרון הוויזואלי המדהים של התכווצות צורות לקראת הגבול האינסופי ואת האפשרויות הבלתי-נגמרות של ריצופים במרחב כזה. סדרת יצירותיו "מעגל גבולי" (Circle Limit), ובמיוחד 'מעגל גבולי III' עם הדגים ו-'מעגל גבולי IV' עם העטלפים, הן דוגמאות קלאסיות לריצופים היפרבוליים על דיסק פואנקרה. אשר יצר אותן באמצעות בנייה גיאומטרית אינטואיטיבית, והתוצאה היא לא פחות מקסומה – שילוב מושלם של אמנות, סימטריה ומתמטיקה עמוקה.</p>

    <p>הסימולציה שלפניכם מציגה דוגמה לריצוף היפרבולי בדיסק פואנקרה, בהשראת יצירותיו של אשר. הצורות (כאן מיוצגות על ידי דגים פשוטים) נראות קטנות יותר ככל שהן מתקרבות לקצה העיגול, למרות שגודלן ההיפרבולי זהה. גרירת העכבר בתוך הדיסק משנה את נקודת המבט שלכם במרחב ההיפרבולי ומאפשרת לכם לשוטט ולחקור את הריצוף האינסופי. שימוש בגלגלת העכבר מאפשר "להתקרב" או "להתרחק" מהריצוף.</p>

    <p>שחקו, חקרו, ונסו לדמיין את המרחב המוזר והיפה הזה שריתק את אשר ואת המתמטיקאים כאחד!</p>
</div>


<script>
    const canvas = document.getElementById('poincareCanvas');
    const ctx = canvas.getContext('2d');
    const toggleBtn = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');

    let width = 600;
    let height = 600;
    let radius = Math.min(width, height) / 2 - 10; // Radius of the Poincaré disk in pixels
    let centerX = width / 2;
    let centerY = height / 2;

    canvas.width = width;
    canvas.height = height;

    // Current "center" of the hyperbolic view within the Euclidean disk (complex number)
    // This represents the point in hyperbolic space that is currently at the Euclidean center (0,0)
    // We store this as a complex number {x, y} where x, y are coordinates in the Euclidean disk [-1, 1].
    let viewCenter = { x: 0, y: 0 }; // Initially, the hyperbolic origin is at the Euclidean center.

    // Zoom level (simplistic Euclidean scaling applied after hyperbolic transform)
    let zoom = 1.0;

    // Animation frame ID for render loop
    let animationFrameId = null;

    // --- Math Helpers for Poincaré Disk ---
    // Map Euclidean canvas coordinates (px, py) relative to canvas center, to complex number z within the disk
    function mapCanvasToDisk(px, py) {
        let rx = (px - centerX) / radius;
        let ry = (py - centerY) / radius;
        // Clamp to disk boundary if outside (optional, but good practice)
        let magSq = rx * rx + ry * ry;
        if (magSq > 1) {
             let mag = Math.sqrt(magSq);
             rx /= mag;
             ry /= mag;
        }
        return { x: rx, y: ry }; // Represents complex number rx + i*ry
    }

     // Map complex number z (disk coordinates [-1,1]) back to Euclidean canvas coordinates (px, py)
     // relative to canvas center.
     function mapDiskToCanvas(z) {
         let px = centerX + z.x * radius;
         let py = centerY + z.y * radius;
         return { x: px, y: py };
     }


     // Mobius transform M_a(z) = (z-a)/(1 - conj(a)*z)
     // This transform maps 'a' to 0. Used to bring a point 'z' into the frame centered at 'a'.
     // This is used to transform canonical tile positions into the current view frame (centered at viewCenter).
     // The inverse transform M_a^-1(z) = (z+a)/(1 + conj(a)*z) maps 0 to 'a'.
     // We need to transform the tile's canonical position `z_tile` using the inverse transform
     // that maps the current view center `viewCenter` to 0. This is T_{-viewCenter}(z_tile).
     // Let a = -viewCenter. We apply T_a(z) = (z+a)/(1 + conj(a)*z) to the tile's canonical position.
     function transformPointForView(z, currentViewCenter) {
         // Let a = -currentViewCenter
         let ax = -currentViewCenter.x;
         let ay = -currentViewCenter.y;
         let zx = z.x;
         let zy = z.y;

         // Calculate denominator: (1 + conj(a)*z)
         // conj(a) = (ax - i ay)
         // conj(a)*z = (ax - i ay)(zx + i zy) = (ax*zx + ay*zy) + i(ax*zy - ay*zx)
         let denR = 1 + (ax*zx + ay*zy);
         let denI = ax*zy - ay*zx;

         let denSq = denR*denR + denI*denI;

         if (denSq === 0) return {x: NaN, y: NaN}; // Should not happen unless viewCenter is exactly 1/|z|

         // Calculate numerator: (z + a)
         let numX = zx + ax;
         let numY = zy + ay;

         // Result (numX + i numY) / (denR + i denI)
         // = [(numX + i numY) * (denR - i denI)] / denSq
         // Real part: (numX * denR + numY * denI) / denSq
         // Imaginary part: (numY * denR - numX * denI) / denSq

         let resX = (numX * denR + numY * denI) / denSq;
         let resY = (numY * denR - numX * denI) / denSq;

         return { x: resX, y: resY };
     }

    // Hyperbolic scaling factor based on Euclidean position within the disk
    // Objects at Euclidean position z appear scaled by (1 - |z|^2) relative to their size at the origin
    function getHyperbolicScaleFactor(z) {
        let magSq = z.x * z.x + z.y * z.y;
        return Math.max(0, (1 - magSq) / (1 + magSq)); // Using the correct scaling factor (derivative of Mobius transform)
    }


    // --- Drawing Logic ---
    // Define base fish shape vertices and eye position in its canonical space (centered at origin, size ~0.3)
    const baseFishVertices = [
        { x: 0.25, y: 0 },   // Tail tip
        { x: 0.05, y: 0.08 },
        { x: -0.15, y: 0.08 }, // Body top
        { x: -0.3, y: 0 },   // Nose
        { x: -0.15, y: -0.08 }, // Body bottom
        { x: 0.05, y: -0.08 }
    ];
    const baseEyePos = { x: -0.2, y: 0.03 }; // Position relative to canonical origin

    // Function to draw a fish given its vertices (in Euclidean canvas coordinates) and colors
    function drawFish(vertices, eyePos, fillColor, strokeColor) {
        if (vertices.length < 3) return; // Need at least 3 vertices for a polygon

        ctx.fillStyle = fillColor;
        ctx.strokeStyle = strokeColor;
        ctx.lineWidth = 1.5;

        ctx.beginPath();
        ctx.moveTo(vertices[0].x, vertices[0].y);
        for (let i = 1; i < vertices.length; i++) {
            ctx.lineTo(vertices[i].x, vertices[i].y);
        }
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        // Draw eye as a circle
        if (eyePos) {
            ctx.fillStyle = 'black';
            ctx.beginPath();
            // Approximate the Euclidean size of the tile to scale the eye radius
            let avgScale = 0;
            if (vertices.length > 0) {
                let sumDistSq = 0;
                 let center = {x: 0, y: 0}; // Approximate Euclidean center of the shape on canvas
                 for(const v of vertices) { center.x += v.x; center.y += v.y; }
                 center.x /= vertices.length; center.y /= vertices.length;

                 for(const v of vertices) { sumDistSq += Math.pow(v.x - center.x, 2) + Math.pow(v.y - center.y, 2); }
                 // Use the average distance from center as a proxy for scale
                 let avgDist = Math.sqrt(sumDistSq / vertices.length);
                 avgScale = avgDist / (radius * 0.15); // Compare to base size
            }
            let eyeRadius = Math.max(1, Math.min(4, avgScale * 5)); // Scale eye radius, clamped
            ctx.arc(eyePos.x, eyePos.y, eyeRadius, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    // Store tile definitions: { canonicalPos, colorIndex, rotation }
    let tilesToDraw = [];

    // Function to generate tile positions based on a grid in hyperbolic space
    function generateInitialTiling() {
        tilesToDraw = [];
        const colors = ['#ff6666', '#66b266', '#6666ff', '#ffcc66']; // Fish colors (Red, Green, Blue, Yellow-ish)
        const strokeColor = '#333'; // Outline color

        const hStep = 0.6; // Hyperbolic distance step between rings
        const maxRings = 7; // Max number of rings to generate
        const baseAngularDivisions = 8; // Angular divisions on the first ring

        // Add the central tile (at hyperbolic origin)
        tilesToDraw.push({ canonicalPos: { x: 0, y: 0 }, colorIndex: 0, rotation: 0 });

        for (let k = 1; k <= maxRings; ++k) {
            // Calculate Euclidean radius for this hyperbolic distance
            let r_euc = Math.tanh(k * hStep / 2);

            // Stop if Euclidean radius is too close to the boundary
            if (r_euc > 0.98) break;

            // Determine number of points on this ring. Increase with distance.
            let numPoints = baseAngularDivisions * k; // Simple increase

            for (let j = 0; j < numPoints; ++j) {
                let angle = 2 * Math.PI * j / numPoints;

                // Calculate the hyperbolic position for this point
                let tilePos = { x: r_euc * Math.cos(angle), y: r_euc * Math.sin(angle) };

                // Add the tile definition
                tilesToDraw.push({
                    canonicalPos: tilePos,
                    colorIndex: (k + j) % colors.length, // Vary color
                    rotation: angle // Orient fish outwards
                });
            }
        }

         // Optional: Sort tiles by Euclidean distance from the current view center
         // Drawing nearer tiles last can prevent some rendering artifacts (though clipping helps).
         // Sorting is computationally expensive, might skip for performance.
         // Let's skip for simplicity and rely on canvas clipping.
    }


    function draw() {
        ctx.clearRect(0, 0, width, height);

        // Draw the disk boundary
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
        ctx.strokeStyle = '#a0b0c0';
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.save(); // Save state before clipping
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius - 1, 0, Math.PI * 2); // Clip slightly inside the border
        ctx.clip(); // Clip subsequent drawing to the disk

        // Calculate the inverse transform parameters for the current view center
        // We need to transform tile canonical positions `z_tile` by T_{-viewCenter}(z_tile)
        // to get their positions in the current view.
        let invVC = { x: -viewCenter.x, y: -viewCenter.y };

        // Determine the effective scale multiplier combining zoom and base shape size
        const baseShapeCanvasScale = radius * 0.15; // How large the base shape appears at the origin (Euclidean pixels)

        // Draw tiles
        for (const tile of tilesToDraw) {
            // Get the tile's position in the current view by applying the inverse view transform
            let currentViewPos = transformPointForView(tile.canonicalPos, viewCenter); // Should use viewCenter directly as the 'a' parameter to map viewCenter -> 0

            // Check if the transformed position is outside the Euclidean disk (and visible)
             let euclideanMagSq = currentViewPos.x * currentViewPos.x + currentViewPos.y * currentViewPos.y;
             if (euclideanMagSq >= 1.0) { // Add a small buffer? No, clipping handles it.
                 continue; // Skip drawing if outside the visible disk
             }

            // Calculate the hyperbolic scale factor at this position
            let scaleFactorH = getHyperbolicScaleFactor(currentViewPos);

            // Apply zoom and hyperbolic scaling
            let totalScale = scaleFactorH * zoom * baseShapeCanvasScale;

            // If scale is too small, don't draw (performance optimization)
            if (totalScale * Math.max(baseFishVertices[0].x, baseFishVertices[0].y) < 0.5) continue; // Skip if shape becomes tiny

            // Transform the base shape vertices and eye position for this specific tile
            let transformedVertices = baseFishVertices.map(v => {
                // Apply tile's canonical rotation around its own origin
                let rotatedX = v.x * Math.cos(tile.rotation) - v.y * Math.sin(tile.rotation);
                let rotatedY = v.x * Math.sin(tile.rotation) + v.y * Math.cos(tile.rotation);

                // Scale the rotated vertex and position it based on the tile's current view position (in Euclidean canvas coords)
                // The position `currentViewPos` is in [-1, 1] disk coordinates. Scale by radius to get canvas pixels relative to center.
                let finalX = centerX + currentViewPos.x * radius + rotatedX * totalScale;
                let finalY = centerY + currentViewPos.y * radius + rotatedY * totalScale;

                return { x: finalX, y: finalY };
            });

            // Transform eye position
             let baseEye = baseEyePos;
             let rotatedEyeX = baseEye.x * Math.cos(tile.rotation) - baseEye.y * Math.sin(tile.rotation);
             let rotatedEyeY = baseEye.x * Math.sin(tile.rotation) + baseEye.y * Math.cos(tile.rotation);
             let finalEyeX = centerX + currentViewPos.x * radius + rotatedEyeX * totalScale;
             let finalEyeY = centerY + currentViewPos.y * radius + rotatedEyeY * totalScale;
             let transformedEye = { x: finalEyeX, y: finalEyeY };

            // Get colors
            const colors = ['#ff6666', '#66b266', '#6666ff', '#ffcc66']; // Fish colors
            const strokeColor = '#333'; // Outline color

            // Draw the transformed fish
            drawFish(transformedVertices, transformedEye, colors[tile.colorIndex], strokeColor);
        }

         // Restore canvas state to remove clipping
         ctx.restore();
    }

    // --- Animation Loop ---
    function render() {
        draw();
        animationFrameId = requestAnimationFrame(render);
    }

    // --- Event Handlers ---
    let isDragging = false;
    let lastMousePos = { x: 0, y: 0 };

    canvas.addEventListener('mousedown', (e) => {
        const rect = canvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;
        const distSq = Math.pow(mouseX - centerX, 2) + Math.pow(mouseY - centerY, 2);

        if (distSq <= radius * radius) {
            isDragging = true;
            lastMousePos = { x: mouseX, y: mouseY };
            canvas.style.cursor = 'grabbing';
            if (animationFrameId === null) { // Start rendering only when interaction happens
                 render();
            }
        }
    });

    canvas.addEventListener('mousemove', (e) => {
        if (!isDragging) return;

        const rect = canvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;

        // Convert current and previous mouse positions to disk coordinates
        const currentDiskPos = mapCanvasToDisk(mouseX, mouseY);
        const lastDiskPos = mapCanvasToDisk(lastMousePos.x, lastMousePos.y);

        // We want the viewCenter to be transformed such that the point under the mouse
        // remains under the mouse.
        // Let oldVC be the old viewCenter.
        // The point under the mouse had hyperbolic coordinate Z_mouse_old = T_{oldVC}^-1(lastDiskPos).
        // We want the new viewCenter newVC such that T_{newVC}^-1(currentDiskPos) = Z_mouse_old.
        // This is equivalent to T_{newVC}(Z_mouse_old) = currentDiskPos.
        // T_{newVC}(T_{oldVC}^-1(lastDiskPos)) = currentDiskPos.
        // This is complex. A simpler, visually effective approach is to perform a hyperbolic translation
        // on the viewCenter itself. The Mobius transform that maps A to B is T_B(T_A^-1(z)).
        // We are mapping lastDiskPos to currentDiskPos. The transform is T_{currentDiskPos}(T_{lastDiskPos}^-1(z)).
        // We want to apply this transform to the *inverse* of the current view center? No.
        // We want to move the *origin* (viewCenter) by the amount the mouse moved *in hyperbolic space*.
        // The hyperbolic "movement vector" is essentially a Mobius transform M that maps lastDiskPos to currentDiskPos.
        // We want the new viewCenter to be M applied to the old viewCenter.
        // The Mobius transform mapping a to b is M(z) = ( (b-a) + (1-b conj(a)) z ) / ( (1-conj(b)a) + (conj(b)-conj(a)) z ) -- too complex

        // Let's simplify and use the inverse transform that maps currentPos to lastPos, and apply it to viewCenter.
        // Let a = currentDiskPos, b = lastDiskPos. We want T that maps a to b. T(z) = (z-a)/(1-conj(a)z)? No.
        // The transform that maps a to 0 is M_a(z) = (z-a)/(1-conj(a)z).
        // The transform that maps 0 to b is M_b^-1(z) = (z+b)/(1+conj(b)z).
        // Transform mapping a to b is M_b^-1(M_a(z)) = ( (z-a)/(1-conj(a)z) + b ) / ( 1 + conj(b)*(z-a)/(1-conj(a)z) )
        // This is getting too complex for a simple interaction handler.

        // Back to the simple approach: define a function that maps a delta vector (like mouse move) to a hyperbolic translation.
        // A hyperbolic translation by distance D along the x-axis is T(z) = (z+tanh(D/2))/(1+tanh(D/2)z).
        // This linear delta update was wrong. Let's find the point that WAS at the center.
        // Let vc = viewCenter. The point at the center was vc. Where is it now after the move?
        // The new view center vc' is the point that is now at the Euclidean center.
        // The inverse transform T_vc^-1 maps the center (0) to vc.
        // The points in the old view are z_old = T_vc(z_euclidean).
        // The points in the new view are z_new = T_vc'(z_euclidean).
        // T_vc'(z_euclidean) = T_vc(z_euclidean_prime) where z_euclidean_prime is the *old* euclidean coordinate of the mouse.
        // z_euclidean_prime = lastDiskPos. z_euclidean = currentDiskPos.
        // T_vc'(currentDiskPos) = T_vc(lastDiskPos).
        // Apply T_vc'^-1 to both sides: currentDiskPos = T_vc'^-1(T_vc(lastDiskPos)).
        // Let M be the Mobius transform that maps currentDiskPos to lastDiskPos. M(currentDiskPos) = lastDiskPos.
        // We want newVC = M(oldVC).
        // The transform mapping a to b is M_{a \to b}(z).
        // M_{a \to b}(z) = T_b(T_a^{-1}(z))
        // a = currentDiskPos, b = lastDiskPos.
        // M(z) = T_{lastDiskPos}(T_{currentDiskPos}^{-1}(z)).
        // Need to implement Mobius transform composition and inversion.

        // Mobius transform function T_a(z) = (z+a)/(1 + conj(a)z)
        function mobiusTransform(z, a) {
             let az = a.x, ay = a.y;
             let zx = z.x, zy = z.y;

             let denR = 1 + (az*zx + ay*zy);
             let denI = az*zy - ay*zx;
             let denSq = denR*denR + denI*denI;

             if (denSq === 0) return {x: NaN, y: NaN};

             let numX = zx + az;
             let numY = zy + ay;

             let resX = (numX * denR + numY * denI) / denSq;
             let resY = (numY * denR - numX * denI) / denSq;
             return {x: resX, y: resY};
        }

        // Inverse Mobius transform T_a^-1(z) = (z-a)/(1 - conj(a)z)
        function inverseMobiusTransform(z, a) {
            let az = a.x, ay = a.y;
            let zx = z.x, zy = z.y;

            let denR = 1 - (az*zx + ay*zy); // conj(a) = (ax, -ay). conj(a)z = (ax-i ay)(zx+i zy) = (ax zx + ay zy) + i (ax zy - ay zx). So 1 - conj(a)z has real part 1 - (ax zx + ay zy)
            let denI = -(ax*zy - ay*zx); // Imaginary part of 1 - conj(a)z is -(ax zy - ay zx)
             // Wait, the definition of T_a(z) uses '+a' and '+conj(a)z'. The inverse T_a^-1(z) uses '-a' and '-conj(a)z'.
             // If T_a(z) = (z+a)/(1 + conj(a)z), then T_a^-1(w) is such that w = (z+a)/(1 + conj(a)z). w(1+conj(a)z) = z+a. w + w conj(a) z = z + a. w-a = z(1 - w conj(a)). z = (w-a)/(1 - w conj(a)).
             // So T_a^-1(z) = (z-a)/(1 - z conj(a)).
             // Let a = viewCenter. We applied T_{-a} to canonical points. Let's rename transformPointForView to applyInverseViewTransform.
             // applyInverseViewTransform(z_canonical, viewCenter) applies T_{-viewCenter}(z_canonical). This is correct.

             // Now for drag: mouse moves from m1_euclidean to m2_euclidean.
             // m1_disk = mapCanvasToDisk(m1_euclidean), m2_disk = mapCanvasToDisk(m2_euclidean).
             // We want the point that was at m1_disk (in the old view) to be at m2_disk (in the new view).
             // Let oldVC be old viewCenter, newVC be new viewCenter.
             // Point Z has Euclidean coord m1_disk in old view: m1_disk = T_{-oldVC}(Z). Z = T_{-oldVC}^{-1}(m1_disk) = T_{oldVC}(m1_disk).
             // We want Z to have Euclidean coord m2_disk in new view: m2_disk = T_{-newVC}(Z). Z = T_{-newVC}^{-1}(m2_disk) = T_{newVC}(m2_disk).
             // So T_{oldVC}(m1_disk) = T_{newVC}(m2_disk).
             // Apply T_{m2_disk}^{-1} to both sides: T_{m2_disk}^{-1}(T_{oldVC}(m1_disk)) = newVC.
             // T_a^{-1}(z) = (z-a)/(1 - z conj(a)).
             // T_b(z) = (z+b)/(1 + conj(b)z).
             // T_a^{-1}(T_b(z))
             // Need to implement composition: M_1(M_2(z)).
             // M_{a \to b}(z) = (z-a)/(1 - conj(a)z) followed by (z+b)/(1+conj(b)z) ... this is wrong
             // Transform mapping a to b is T_b(T_a^{-1}(z)) where T_a^{-1}(z) is hyperbolic translation by -a?
             // The transform that moves 'a' to '0' is M_a(z) = (z-a)/(1-conj(a)z).
             // The transform that moves '0' to 'b' is M_b^{-1}(z) = (z+b)/(1+conj(b)z).
             // The transform mapping 'a' to 'b' is M_b^{-1}(M_a(z)). This is it.
             // Let a = lastDiskPos, b = currentDiskPos. We want to apply M_b^{-1}(M_a(z)) to the old viewCenter.
             // newVC = M_b^{-1}(M_a(oldVC)).

             let a = lastDiskPos;
             let b = currentDiskPos;
             let z = viewCenter; // old view center

             // M_a(z) = (z-a)/(1-conj(a)z)
             let conj_a_zR = a.x*z.x + a.y*z.y; // conj(a) = (ax, -ay). conj(a)z = (ax-i ay)(zx+i zy) = (ax zx + ay zy) + i(ax zy - ay zx)
             let conj_a_zI = a.x*z.y - a.y*z.x; // Should be (ax zy - ay zx) if a is not conjugated. Let's assume 'a' is the complex number. conj(a) = {x: a.x, y: -a.y}. conj(a)z = (ax - i ay)(zx + i zy) = (ax zx + ay zy) + i (ax zy - ay zx). Yes.
             let temp_denR = 1 - conj_a_zR;
             let temp_denI = -conj_a_zI;
             let temp_denSq = temp_denR*temp_denR + temp_denI*temp_denI;

             if (temp_denSq === 0) { console.warn("Mobius transform denominator is zero!"); return z; } // Avoid division by zero

             let temp_numX = z.x - a.x;
             let temp_numY = z.y - a.y;

             let intermediate_zX = (temp_numX * temp_denR + temp_numY * temp_denI) / temp_denSq;
             let intermediate_zY = (temp_numY * temp_denR - temp_numX * temp_denI) / temp_denSq;
             let intermediate_z = {x: intermediate_zX, y: intermediate_zY};

             // M_b^{-1}(intermediate_z) = (intermediate_z + b) / (1 + conj(b) * intermediate_z)
             let bzR = b.x * intermediate_z.x + b.y * intermediate_z.y;
             let bzI = b.x * intermediate_z.y - b.y * intermediate_z.x;
             let res_denR = 1 + bzR;
             let res_denI = bzI;
             let res_denSq = res_denR*res_denR + res_denI*res_denI;

             if (res_denSq === 0) { console.warn("Inverse Mobius transform denominator is zero!"); return z; } // Should not happen inside disk

             let res_numX = intermediate_z.x + b.x;
             let res_numY = intermediate_z.y + b.y;

             let newVC_x = (res_numX * res_denR + res_numY * res_denI) / res_denSq;
             let newVC_y = (res_numY * res_denR - res_numX * res_denI) / res_denSq;

             // Clamp newVC to stay within the disk (conceptually, floating point errors)
             let magSq = newVC_x * newVC_x + newVC_y * newVC_y;
              if (magSq > 1) {
                  let mag = Math.sqrt(magSq);
                  newVC_x /= mag;
                  newVC_y /= mag;
              }

             viewCenter = {x: newVC_x, y: newVC_y};

             lastMousePos = { x: mouseX, y: mouseY };
             // Render is called via requestAnimationFrame loop
        }
    });

    canvas.addEventListener('mouseup', () => {
        isDragging = false;
        canvas.style.cursor = 'grab';
         // Stop rendering if no interaction for a while? No, keep loop running for smooth hover effects later maybe.
    });

    canvas.addEventListener('mouseleave', () => {
         isDragging = false;
         canvas.style.cursor = 'grab';
         // Stop rendering if no interaction? No.
    });


    canvas.addEventListener('wheel', (e) => {
        e.preventDefault(); // Prevent page scroll

        const zoomFactor = e.deltaY < 0 ? 1.1 : 0.9; // Zoom in/out speed
        const oldZoom = zoom;
        zoom *= zoomFactor;
        zoom = Math.max(0.5, Math.min(10, zoom)); // Clamp zoom level

        // Optional: Zoom towards the mouse position
        // This requires mapping mouse pos to hyperbolic space, scaling the view, and mapping back.
        // Complex Mobius math involved. Let's do a simpler zoom relative to center for now.
        // If we zoom by factor F, and the point under the mouse was at z_disk, its new pos z'_disk should be related.
        // A hyperbolic scaling by factor S around the origin maps z to tanh(S * atanh(z)).
        // Our zoom isn't a hyperbolic scaling, it's a Euclidean scaling of the rendered tiles.
        // Simple Euclidean zoom relative to center is easiest with current drawing method.

        // If rendering loop is not active, start it
        if (animationFrameId === null) {
            render();
        }
    });


    // --- Initial Setup ---
    generateInitialTiling(); // Generate tile positions once
    render(); // Start the animation loop

    // Toggle explanation visibility
    toggleBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleBtn.textContent = isHidden ? 'הסתר הסבר על גיאומטריה היפרבולית ואשר' : 'הצג הסבר על גיאומטריה היפרבולית ואשר';
    });

    // Optional: Regenerate tiles or redraw on resize
    window.addEventListener('resize', () => {
        // If canvas size changes dynamically, update variables:
        // canvas.width = canvas.clientWidth;
        // canvas.height = canvas.clientHeight;
        // width = canvas.width;
        // height = canvas.height;
        // centerX = width / 2;
        // centerY = height / 2;
        // radius = Math.min(width, height) / 2 - 10;
        // If viewCenter was stored as ratio, update absolute value. If not, it's fine.
        // Redraw happens via the render loop.
        // If using fixed size, resize does nothing to canvas, only layout.
         // Let's stick to fixed size for simplicity as canvas dimensions are set explicitly.
         render(); // Request redraw on window resize (in case container/layout changes)
    });

    // Initial render request
    render();


</script>