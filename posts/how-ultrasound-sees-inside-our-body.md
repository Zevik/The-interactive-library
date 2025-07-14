---
title: "איך אולטרסאונד 'רואה' את גופנו מבפנים?"
english_slug: how-ultrasound-sees-inside-our-body
category: "פיזיקה"
tags: ["אולטרסאונד", "דימות רפואי", "פיזיקה", "גלי קול", "טכנולוגיה רפואית"]
---
# איך אולטרסאונד 'רואה' את גופנו מבפנים?

אי פעם תהיתם איך רופאים יכולים להציץ פנימה לגוף שלנו – לראות איברים, כלי דם ואפילו תינוק מתפתח ברחם – בלי שום חיתוך או ניתוח? האם זה דורש קרני רנטגן מסוכנות, או שיש טכנולוגיה אחרת, מדהימה ובטוחה, שמבוססת על משהו פשוט כמו קול? בואו נגלה איך גלי קול בלתי נשמעים מצליחים 'לצייר' לנו תמונה של מה שמתרחש עמוק בפנים!

<div class="ultrasound-container">
    <div class="ultrasound-simulation">
        <div class="organ-model">
            <!-- Layers represent different tissues -->
            <div class="tissue-layer layer-skin">עור</div>
            <div class="tissue-layer layer-fat">שומן</div>
            <div class="tissue-layer layer-muscle">שריר</div>
            <div class="tissue-layer layer-organ">איבר (רקמה רכה)</div>
            <div class="tissue-layer layer-stone">אבן קשה</div>
            <div class="tissue-layer layer-liquid">נוזל</div>
            <div class="tissue-layer layer-bone">עצם</div>

            <div class="transducer" id="transducer">
                <div class="transducer-tip"></div>
            </div>
            <canvas id="pulse-canvas" class="pulse-canvas"></canvas>
        </div>
        <div class="display-area">
            <div class="amode-display">
                <h2>A-Mode (הד לפי עומק)</h2>
                <canvas id="amode-canvas"></canvas>
            </div>
            <div class="bmode-display">
                <h2>B-Mode (תמונה דו-ממדית)</h2>
                <canvas id="bmode-canvas"></canvas>
                <div class="bmode-scan-line"></div>
            </div>
        </div>
         <div class="instructions">גרור את המתמר (Transducer) לרוחב ה'איבר' כדי לסרוק אותו!</div>
    </div>
</div>

<button id="toggle-explanation">הצג הסבר מלא על טכנולוגיית אולטרסאונד</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מעמיק: מסע גלי הקול בתוך הגוף</h2>
    <p>טכנולוגיית האולטרסאונד הרפואי היא פלא מודרני שמאפשר לרופאים להביט עמוק לתוך הגוף שלנו מבלי להשתמש בקרינה מזיקה, בניגוד לשיטות כמו צילום רנטגן או CT. הכל מבוסס על עיקרון פשוט אך גאוני: שימוש בגלי קול בתדרים כל כך גבוהים, שאוזן אנושית פשוט לא מסוגלת לשמוע אותם.</p>

    <h3>מהו 'אולטרסאונד' באמת?</h3>
    <p>אולטרסאונד מתייחס לכל גל קול שתדרו עולה על 20 קילוהרץ (20,000 הרץ) - מעבר לסף השמיעה שלנו. בשימושים רפואיים, התדרים הרבה יותר גבוהים, ונמצאים בטווח של 2 עד 18 מגהרץ (מיליון הרץ!).</p>

    <h3>הצוות שעובד מאחורי הקלעים: מרכיבי מכשיר האולטרסאונד</h3>
    <ul>
        <li><strong>המתמר (Transducer / Probe):</strong> ה'קסם' קורה כאן! זה החלק שהטכנאי או הרופא מניחים על העור, לרוב עם ג'ל מיוחד. המתמר הוא גם השולח שמפיק את גלי הקול וגם המקלט שממתין להדים החוזרים.</li>
        <li><strong>המעבד (Processor):</strong> המוח של המכשיר. הוא מקבל את האותות החשמליים העדינים מהמתמר, מנתח אותם במהירות מסחררת והופך את כל המידע הזה לתמונה ויזואלית שאנחנו יכולים להבין.</li>
        <li><strong>המסך (Display):</strong> הבמה שבה מוצגת התמונה שנוצרה על ידי המעבד, ומאפשרת לצוות הרפואי לראות מה קורה בפנים.</li>
    </ul>

    <h3>איך המתמר עושה את זה? הקסם הפיאזואלקטרי</h3>
    <p>בליבת המתמר נמצאים חומרים מיוחדים הנקראים גבישים פיאזואלקטריים. לגבישים אלו תכונה מדהימה: כאשר מפעילים עליהם זרם חשמלי, הם מתכווצים ומתרחבים במהירות עצומה, ויוצרים בכך גלי קול הנשלחים החוצה. להפך, כאשר גלי קול פוגעים בהם (כמו הדים שחוזרים מהגוף), הם רועדים ומייצרים בעצמם זרם חשמלי זעיר. כך, המתמר פועל באופן כפול: הוא שולח "פעימות" (פולסים) של גלי קול לתוך הגוף, ולאחר מכן עובר למצב הקשבה, קולט את ההדים שחוזרים וממיר אותם בחזרה לאותות חשמליים שהמעבד יכול לפרש.</p>

    <h3>המסע פנימה וההדים שחוזרים: תהליך הדימות</h3>
    <p>המכשיר שולח פולסים קצרים וחזקים של גלי קול מהמתמר היישר לתוך רקמות הגוף. גלי הקול הללו טסים קדימה, חודרים דרך שכבות שונות של עור, שומן, שרירים ואיברים. המפתח הוא מה שקורה כשהגל נתקל ב"גבול" או "ממשק" בין שתי רקמות שונות בתכונותיהן האקוסטיות – למשל, המעבר משריר לאיבר רך, או מאיבר רך לאבן צפופה, או סתם שינוי קטן בצפיפות או בגמישות. בממשק כזה, חלק מהגל פשוט "קופץ" חזרה לכיוון שממנו הגיע – זהו ה'הד' (Echo) שאותו המתמר קולט. חלק אחר מהגל ממשיך הלאה לעומק רב יותר.</p>

    <h3>לא רק קופצים בחזרה: מה עוד גלי הקול עושים בתוך הגוף?</h3>
    <p>מלבד ההחזרה (Reflection) שיוצרת את ההדים החיוניים לתמונה, גלי הקול מקיימים אינטראקציות נוספות עם הרקמות:
    <ul>
        <li><strong>בליעה (Absorption):</strong> הרקמות 'בולעות' חלק מהאנרגיה של הגל וממירות אותה לחום זעיר. זו אחת הסיבות מדוע אולטרסאונד בטוח – רמת האנרגיה נמוכה ומתפזרת. ככל שהגל חודר עמוק יותר או שתדרו גבוה יותר, הבליעה גדולה יותר.</li>
        <li><strong>פיזור (Scattering):</strong> כשהגל פוגש מבנים קטנים מאוד בתוך הרקמה (כמו כדוריות דם), הוא מתפזר לכל הכיוונים, כמו אור שפוגע באבק. חלק קטן מהאנרגיה המפוזרת עשוי במקרה לחזור גם הוא למתמר.</li>
        <li><strong>שבירה (Refraction):</strong> שינוי קטן בכיוון הגל כשהוא עובר בין רקמות במהירויות קול שונות. זה פחות משפיע על התמונה המרכזית לעומת ההדים.</li>
    </ul>
    עוצמת ההד שחוזר תלויה במידה רבה ב"הבדל האקוסטי" בין שתי הרקמות בממשק – ככל שהן שונות יותר (למשל, רקמה רכה מול עצם קשה), כך ההד יהיה חזק יותר.</p>

    <h3>איך המידע הופך לתמונה? זמן ועוצמת ההד</h3>
    <p>המעבד במכשיר מודד שני פרטים קריטיים עבור כל הד שחוזר למתמר, מיליוני פעמים בשנייה:
    <ul>
        <li><strong>זמן חזרת ההד:</strong> כמה זמן עבר מרגע שהפולס נשלח ועד שההד חזר. מכיוון שמהירות הקול ברקמות רכות יחסית קבועה (כ-1540 מטר לשנייה), המכשיר יודע לחשב במדויק את העומק של הממשק שממנו ההד חזר (מרחק = מהירות * זמן הלוך-חזור / 2).</li>
        <li><strong>עוצמת ההד:</strong> כמה "חזק" ההד שחזר. הד חזק יותר (שמגיע מממשק עם הבדל אקוסטי גדול, כמו רקמה מול עצם) יתורגם לאות חשמלי חזק יותר.</li>
    </ul>
    על ידי סריקה מהירה של אזור בגוף (כפי שאתם עושים עם המתמר בסימולציה) ושליחת אינספור פולסים, המכשיר אוסף מפה תלת-ממדית של נקודות הדים. כל נקודה כזו מתורגמת לנקודה על המסך: המיקום האופקי (X) של הנקודה תלוי במיקום המתמר, המיקום האנכי (Y) תלוי בעומק הממשק (מחושב מזמן חזרת ההד), והבהירות או הצבע של הנקודה (בדרך כלל בסולם גווני אפור) תלויים בעוצמת ההד שחזר מאותה נקודה. כך נבנית התמונה!</p>

    <h3>מבט על המסך: סוגי דימות עיקריים</h3>
    <ul>
        <li><strong>A-Mode (Amplitude Mode):</strong> שיטה פשוטה שמציגה גרף חד-ממדי. ציר ה-X מייצג את עוצמת ההד שחזר, וציר ה-Y (או אנכי) מייצג את העומק (לפי זמן חזרת ההד). כל 'פסגה' בגרף מצביעה על ממשק חזק או מבנה מחזיר קול בעומק מסוים. הסימולציה שלנו מציגה גרף דומה ל-A-Mode כדי להמחיש את הרעיון הבסיסי של הד לפי עומק ועוצמה.</li>
        <li><strong>B-Mode (Brightness Mode):</strong> זהו סוג הדימות הנפוץ ביותר, ומה שאנחנו בדרך כלל רואים בתמונות אולטרסאונד. הוא בונה תמונה דו-ממדית של 'פרוסה' מהגוף. כל פיקסל בתמונה מייצג נקודה ספציפית בגוף. מיקום הפיקסל קובע את מיקום הנקודה בסריקה, והבהירות (או גוון האפור) שלו קובעת את עוצמת ההד שחזר מאותה נקודה. כך נוצרת תמונה עשירה המציגה את צורת וגבולות האיברים. הסימולציה מדגימה כיצד תמונת B-Mode בסיסית נוצרת על ידי איסוף הדים מנקודות סריקה רבות זו לצד זו.</li>
    </ul>

    <h3>למה אולטרסאונד כל כך בטוח?</h3>
    <p>הוא לא משתמש בקרינה מייננת! זו הסיבה שהוא הבחירה המועדפת לבדיקות שגרתיות, מעקבי הריון (גם לאם וגם לעובר), בדיקות ילדים ועוד, ואפשר לחזור עליו פעמים רבות ללא חשש.</p>

    <h3>איפה פוגשים אולטרסאונד? שימושים קליניים נפוצים</h3>
    <p>טכנולוגיית האולטרסאונד היא כלי אבחנתי רב-גוני וחיוני:
    <ul>
        <li><strong>מעקב הריון וגינקולוגיה:</strong> בדיקות אגן, מעקב אחר התפתחות העובר לאורך כל ההריון.</li>
        <li><strong>קרדיולוגיה:</strong> בדיקת לב (אקו לב) להערכת מבנה, תפקוד וזרימת דם.</li>
        <li><strong>אברי בטן:</strong> סריקת כבד, כיס מרה, כליות, לבלב, טחול לאיתור מגוון מצבים.</li>
        <li><strong>כלי דם:</strong> בדיקת עורקים וורידים (בטכניקת דופלר) להערכת זרימת הדם.</li>
        <li><strong>אורולוגיה:</strong> הערכת ערמונית, אשכים.</li>
        <li><strong>מבנים שטחיים:</strong> בלוטת התריס, שדיים, בלוטות לימפה, שרירים, גידים, פרקים.</li>
    </ul>
    </p>
</div>

<script>
    const transducer = document.getElementById('transducer');
    const organModel = document.querySelector('.organ-model');
    const amodeCanvas = document.getElementById('amode-canvas');
    const bmodeCanvas = document.getElementById('bmode-canvas');
    const pulseCanvas = document.getElementById('pulse-canvas');
    const bmodeScanLine = document.querySelector('.bmode-scan-line');
    const toggleButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const instructionsDiv = document.querySelector('.instructions');

    const organRect = organModel.getBoundingClientRect();
    let isDragging = false;
    let currentX = 0; // Center X position of the transducer relative to organ model

    // Canvas contexts
    const amodeCtx = amodeCanvas.getContext('2d');
    const bmodeCtx = bmodeCanvas.getContext('2d');
    const pulseCtx = pulseCanvas.getContext('2d');

    // Simulation Parameters
    const pulseSpeed = 1.54; // Simulated speed of sound in pixels per millisecond (roughly matched to visual)
    const scanInterval = 30; // Milliseconds between pulse updates for animation effect

    // Re-calculate organ structure based on visual layer heights for simulation
    const visualLayers = organModel.querySelectorAll('.tissue-layer');
    const simulationStructure = [];
    let currentSimDepth = 0;
    visualLayers.forEach((layer, index) => {
        const layerHeight = layer.offsetHeight;
        // Add an interface at the bottom of this layer
        currentSimDepth += layerHeight;

        if (index < visualLayers.length - 1) { // Don't add interface after the very last layer
             const nextLayer = visualLayers[index + 1];
             let currentType = layer.className.replace('tissue-layer layer-', '');
             let nextType = nextLayer.className.replace('tissue-layer layer-', '');

             // Simple logic: reflection is stronger if the types are very different
             let interfaceReflection = 0.15; // Default general tissue interface
             if ((currentType === 'organ' && nextType === 'stone') || (currentType === 'organ' && nextType === 'bone') || (currentType === 'stone' && nextType === 'organ') || (currentType === 'bone' && nextType === 'organ')) {
                 interfaceReflection = 0.7; // Organ to hard object / hard object back to organ
             } else if (nextType === 'liquid' || currentType === 'liquid') {
                 interfaceReflection = 0.05; // Fluid interfaces are usually weak
             } else if (nextType === 'bone' || currentType === 'bone') {
                 interfaceReflection = 0.95; // Interfaces involving bone are very strong
             } else if ((currentType === 'fat' && nextType === 'muscle') || (currentType === 'muscle' && nextType === 'organ')) {
                 interfaceReflection = 0.25; // Muscle/Organ interfaces
             } else if (currentType === 'skin' && nextType === 'fat') {
                 interfaceReflection = 0.1; // Skin/Fat interface
             }


             // Add the interface location and its reflection property
             simulationStructure.push({
                 depth: currentSimDepth, // Depth in pixels relative to top of model
                 reflection: interfaceReflection, // Reflection amplitude (0 to 1)
                 interfaceType: `${currentType}-to-${nextType}`
             });
         }
    });


    // Resize canvases
    function resizeCanvases() {
        const organWidth = organModel.offsetWidth;
        const organHeight = organModel.offsetHeight;
        const displayHeight = organHeight; // Match height for visual consistency

        amodeCanvas.width = 150; // Fixed width for A-mode
        amodeCanvas.height = displayHeight;

        bmodeCanvas.width = organWidth; // B-mode width matches organ width (scan area)
        bmodeCanvas.height = displayHeight;

        pulseCanvas.width = organWidth;
        pulseCanvas.height = organHeight;

        // Clear canvases after resize
        clearCanvases();

         // Recalculate organ model position after resize
         Object.assign(organRect, organModel.getBoundingClientRect());

         // Adjust transducer position if it was out of bounds
         updateScanPosition(currentX + organRect.left); // Use last logical X position
    }

    function clearCanvases() {
        amodeCtx.clearRect(0, 0, amodeCanvas.width, amodeCanvas.height);
        bmodeCtx.clearRect(0, 0, bmodeCanvas.width, bmodeCanvas.height);
        pulseCtx.clearRect(0, 0, pulseCanvas.width, pulseCanvas.height);

        // Draw initial A-mode axis
        amodeCtx.beginPath();
        amodeCtx.moveTo(20, 0); // Start a bit right for the label
        amodeCtx.lineTo(20, amodeCanvas.height);
        amodeCtx.strokeStyle = '#ccc';
        amodeCtx.lineWidth = 1;
        amodeCtx.stroke();
        amodeCtx.fillStyle = '#555';
        amodeCtx.font = '12px Arial';
        amodeCtx.textAlign = 'center';
        amodeCtx.fillText('עומק', amodeCanvas.width / 2, 15);
        amodeCtx.textAlign = 'right';
        amodeCtx.fillText('עוצמה', amodeCanvas.width - 5, amodeCanvas.height / 2);
    }


    function simulateScan(xPos) {
        const echoes = [];
        const maxDepth = organModel.offsetHeight;

        simulationStructure.forEach(interface => {
            if (interface.depth <= maxDepth) {
                 const depth = interface.depth;
                 const time = (depth / pulseSpeed) * 2; // Time for round trip
                 const amplitude = interface.reflection; // Reflection strength

                 // Simulate some attenuation based on depth (simple linear model)
                 const attenuationFactor = 1 - (depth / maxDepth) * 0.5; // Max 50% attenuation at max depth
                 const attenuatedAmplitude = amplitude * attenuationFactor;

                 echoes.push({ depth: depth, time: time, amplitude: attenuatedAmplitude });
            }
        });

        return echoes;
    }

    function drawAmode(echoes) {
        // amodeCtx.clearRect(0, 0, amodeCanvas.width, amodeCanvas.height); // Don't clear axis
         amodeCtx.fillStyle = '#fff'; // Clear just the graph area
         amodeCtx.fillRect(21, 0, amodeCanvas.width - 21, amodeCanvas.height);

         // Redraw axis
         amodeCtx.beginPath();
         amodeCtx.moveTo(20, 0);
         amodeCtx.lineTo(20, amodeCanvas.height);
         amodeCtx.strokeStyle = '#ccc';
         amodeCtx.lineWidth = 1;
         amodeCtx.stroke();
         amodeCtx.fillStyle = '#555';
         amodeCtx.font = '12px Arial';
         amodeCtx.textAlign = 'center';
         amodeCtx.fillText('עומק', amodeCanvas.width / 2, 15);
         amodeCtx.textAlign = 'right';
         amodeCtx.fillText('עוצמה', amodeCanvas.width - 5, amodeCanvas.height / 2);


        const originX = 20; // Offset from the left edge for the graph base
        const maxAmplitudeWidth = amodeCanvas.width - originX - 5; // Max width for the amplitude peak

        amodeCtx.strokeStyle = '#007bff'; // Blue for A-mode
        amodeCtx.lineWidth = 2;

        echoes.forEach(echo => {
            const y = echo.depth; // Y position on canvas is depth
            const peakWidth = echo.amplitude * maxAmplitudeWidth; // Amplitude determines horizontal extent

            amodeCtx.beginPath();
            amodeCtx.moveTo(originX, y);
            amodeCtx.lineTo(originX + peakWidth, y);
            amodeCtx.stroke();

            // Draw a small circle or marker at the peak
            amodeCtx.fillStyle = '#007bff';
            amodeCtx.beginPath();
            amodeCtx.arc(originX + peakWidth, y, 3, 0, Math.PI * 2);
            amodeCtx.fill();
        });
    }

     function drawBmodeLine(xPos, echoes) {
         const bmodeX = xPos; // X position on B-mode canvas matches transducer X

         echoes.forEach(echo => {
             const bmodeY = echo.depth; // Y position on B-mode canvas is depth
             const intensity = echo.amplitude; // Amplitude determines brightness

             // Draw a dot or small rectangle for this echo
             // Size and alpha can also represent strength for visual flair
             const dotSize = Math.max(1, intensity * 4); // Size based on amplitude
             const alpha = Math.max(0.1, intensity * 1.5); // Transparency based on amplitude (cap at 1)

             const colorValue = Math.floor(intensity * 255); // Scale amplitude to grayscale (0-255)
             const grayscale = `rgb(${colorValue}, ${colorValue}, ${colorValue})`;

             bmodeCtx.fillStyle = `rgba(${colorValue}, ${colorValue}, ${colorValue}, ${alpha})`;
             // Draw a small circle
             bmodeCtx.beginPath();
             bmodeCtx.arc(bmodeX, bmodeY, dotSize / 2, 0, Math.PI * 2);
             bmodeCtx.fill();

             // Or draw a small rectangle (maybe better for line appearance)
             // bmodeCtx.fillRect(bmodeX - dotSize/2, bmodeY - dotSize/2, dotSize, dotSize);
         });
     }

    let animationFrameId = null;
    let pulseAnimationStartTime = null;
    let currentEchoAnimations = [];

    function drawPulseAnimation(xPos, echoes) {
        pulseCtx.clearRect(0, 0, pulseCanvas.width, pulseCanvas.height);

        const pulseStartX = xPos;
        const pulseStartY = 0; // Starts at the top of the organ model

         // Draw the simulated pulse traveling and echoes returning
         const now = Date.now();
         if (!pulseAnimationStartTime) {
             pulseAnimationStartTime = now;
             // Initialize echo animations - set their start times relative to pulse start
             currentEchoAnimations = echoes.map(echo => ({
                 ...echo,
                 animationStartTime: now + (echo.depth / pulseSpeed) // Time when echo should appear to return
             }));
         }

         const elapsedTime = now - pulseAnimationStartTime;
         const pulseHeadDepth = pulseStartY + (elapsedTime * pulseSpeed);

         // Draw the outgoing pulse line segment (animating downwards)
         if (pulseHeadDepth < organModel.offsetHeight + 10) { // Go slightly past the end
              pulseCtx.strokeStyle = 'rgba(0, 180, 255, 0.9)'; // Brighter Blue
              pulseCtx.lineWidth = 3;
              pulseCtx.beginPath();
              pulseCtx.moveTo(pulseStartX, pulseStartY);
              pulseCtx.lineTo(pulseStartX, Math.min(pulseHeadDepth, organModel.offsetHeight));
              pulseCtx.stroke();
         }


         // Draw animated echoes returning
         pulseCtx.strokeStyle = 'rgba(255, 100, 50, 0.9)'; // Orange-red for echoes
         pulseCtx.lineWidth = 2;
         const echoSpeed = pulseSpeed; // Echoes return at the same speed

         currentEchoAnimations.forEach(echo => {
             // Time elapsed since this echo should have started returning
             const echoElapsedTime = now - echo.animationStartTime;

             if (echoElapsedTime > 0) { // Only animate echoes that have started returning
                 // Calculate the current position of the echo as it travels back up
                 const echoCurrentDepth = echo.depth - (echoElapsedTime * echoSpeed);

                 if (echoCurrentDepth > pulseStartY - 5) { // Ensure it's still visible near the top
                      const echoAmplitude = echo.amplitude;
                      const echoLength = Math.max(5, echoAmplitude * 15); // Visual representation of strength, min length 5

                      // Draw a short horizontal line segment for the echo
                      pulseCtx.beginPath();
                      pulseCtx.moveTo(pulseStartX - echoLength / 2, echoCurrentDepth);
                      pulseCtx.lineTo(pulseStartX + echoLength / 2, echoCurrentDepth);
                      pulseCtx.stroke();

                      // Add a small dot at the center for emphasis
                       pulseCtx.fillStyle = 'rgba(255, 100, 50, 0.9)';
                       pulseCtx.beginPath();
                       pulseCtx.arc(pulseStartX, echoCurrentDepth, Math.max(1, echoAmplitude * 3), 0, Math.PI * 2);
                       pulseCtx.fill();
                 }
             }
         });


        // Request next frame for animation
        if (pulseHeadDepth < organModel.offsetHeight + 10 || currentEchoAnimations.some(e => (now - e.animationStartTime) > 0 && (e.depth - (now - e.animationStartTime) * echoSpeed > pulseStartY - 5))) {
             animationFrameId = requestAnimationFrame(() => drawPulseAnimation(xPos, echoes));
         } else {
             // Animation finished, reset time for the next pulse
             pulseAnimationStartTime = null;
             currentEchoAnimations = [];
             // Optionally, clear the pulse canvas or leave the last frame for a moment
              setTimeout(() => pulseCtx.clearRect(0, 0, pulseCanvas.width, pulseCanvas.height), 500);
         }
    }


    function updateScanPosition(clientX) {
        const newX_relativeToOrgan = clientX - organRect.left - transducer.offsetWidth / 2;
        const boundedX = Math.max(0, Math.min(newX_relativeToOrgan, organRect.width - transducer.offsetWidth));

        transducer.style.left = `${boundedX}px`;
        currentX = boundedX + transducer.offsetWidth / 2; // Center X of the transducer relative to organModel left edge

        // Run simulation and update displays
        const echoes = simulateScan(currentX);

        // Update A-mode
        drawAmode(echoes);

        // Update B-mode - add a new scan line
        drawBmodeLine(currentX, echoes);

        // Animate pulse and echoes - restart animation loop for the new position
         if (animationFrameId) {
             cancelAnimationFrame(animationFrameId);
         }
         pulseAnimationStartTime = null; // Reset timer for a new pulse
         drawPulseAnimation(currentX, echoes);


         // Position the B-mode scan line indicator
        bmodeScanLine.style.left = `${currentX}px`;
        bmodeScanLine.style.height = `${bmodeCanvas.height}px`;

        // Hide instructions after the first drag
        instructionsDiv.style.opacity = 0;
    }

    // Transducer drag functionality
    transducer.addEventListener('mousedown', (e) => {
        isDragging = true;
        transducer.style.cursor = 'grabbing';
        instructionsDiv.style.transition = 'opacity 0.5s ease-out';
        // Prevent default to avoid selecting text etc.
        e.preventDefault();
    });

    document.addEventListener('mousemove', (e) => {
        if (isDragging) {
            updateScanPosition(e.clientX);
        }
    });

    document.addEventListener('mouseup', () => {
        isDragging = false;
        transducer.style.cursor = 'grab';
    });

    // Allow touch dragging
    transducer.addEventListener('touchstart', (e) => {
        isDragging = true;
        instructionsDiv.style.transition = 'opacity 0.5s ease-out';
        e.preventDefault(); // Prevent scrolling
    }, { passive: false }); // Use passive: false to allow preventDefault

    document.addEventListener('touchmove', (e) => {
        if (isDragging && e.touches.length > 0) {
            updateScanPosition(e.touches[0].clientX);
        }
    });

    document.addEventListener('touchend', () => {
        isDragging = false;
    });


    // Initial setup
    window.addEventListener('resize', resizeCanvases);
    resizeCanvases(); // Set initial sizes
    // clearCanvases(); // Called by resizeCanvases

    // Set initial transducer position and perform first scan
     // Start in the middle and trigger the first scan
     const initialX = organRect.left + organRect.width / 2;
     updateScanPosition(initialX);


    // Toggle explanation visibility
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר מלא על טכנולוגיית אולטרסאונד' : 'הצג הסבר מלא על טכנולוגיית אולטרסאונד';
    });

    // Initial instructions state
     instructionsDiv.style.opacity = 1; // Ensure it's visible initially
     instructionsDiv.style.transition = 'none'; // No transition on initial load


</script>

<style>
    .ultrasound-container {
        direction: rtl; /* Allow Hebrew text within the container */
        font-family: 'Arial', sans-serif;
        max-width: 1000px;
        margin: 20px auto;
        padding: 20px;
        border: 1px solid #d0e0f0; /* Softer border */
        border-radius: 12px;
        background: linear-gradient(to bottom, #eef5ff, #d0e9ff); /* Subtle gradient background */
        box-shadow: 0 8px 16px rgba(0,0,0,0.1); /* Softer, larger shadow */
        overflow: hidden;
        color: #333;
    }

    .ultrasound-simulation {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 25px; /* Increased gap */
    }

    .organ-model {
        width: 98%; /* Takes almost full width */
        height: 250px; /* Slightly increased height */
        border: 2px solid #5a677d; /* Deeper border color */
        border-radius: 8px;
        position: relative;
        overflow: hidden;
        background: linear-gradient(to bottom, #e0e0eb, #c0c0d0); /* Base background - cool grey */
        box-shadow: inset 0 0 15px rgba(0,0,0,0.3); /* Deeper inner shadow */
        display: flex;
        flex-direction: column; /* Stack layers vertically */
        cursor: grab; /* Indicate it's part of the interaction area */
    }
     .organ-model:active {
         cursor: grabbing;
     }


    .tissue-layer {
        width: 100%;
        text-align: center;
        padding: 8px 0; /* More padding */
        box-sizing: border-box;
        color: #222; /* Darker text */
        font-size: 1em; /* Slightly larger font */
        font-weight: bold;
        border-bottom: 1px solid rgba(0,0,0,0.1); /* Softer separator */
        flex-shrink: 0; /* Prevent shrinking */
        display: flex;
        align-items: center;
        justify-content: center;
         /* Use flex-basis to ensure heights are respected proportionally if needed, or rely on explicit height */
    }

    /* Specific layer styling - using height and more distinct colors */
    .layer-skin { background-color: #f7e7d3; height: 30px; } /* Lighter peach */
    .layer-fat { background-color: #fff7c0; height: 35px; } /* Softer yellow */
    .layer-muscle { background-color: #c44a4a; height: 45px; color: white; } /* Richer red */
    .layer-organ { background-color: #7ab87a; height: 60px; } /* More vibrant green */
    .layer-stone { background-color: #8c8c8c; height: 25px; color: white; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); } /* Medium gray, text shadow for readability */
    .layer-liquid { background-color: #b0e0e6; height: 25px; } /* Powder blue */
    .layer-bone { background-color: #e0e0d0; height: 30px; color: #333; text-shadow: 1px 1px 2px rgba(255,255,255,0.5);} /* Light bone color, text shadow */


    .transducer {
        position: absolute;
        top: 0;
        width: 50px; /* Wider transducer */
        height: 20px; /* Taller transducer */
        background-color: #4a4a4a; /* Darker grey */
        border: 1px solid #222;
        border-top: none; /* No top border */
        cursor: grab;
        z-index: 10; /* Above layers */
        border-bottom-left-radius: 8px; /* Rounded bottom corners */
        border-bottom-right-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2); /* Shadow below */
        display: flex;
        justify-content: center;
        align-items: flex-end;
        transition: box-shadow 0.1s ease-in-out; /* Smooth shadow transition */
    }
     .transducer:hover {
         box-shadow: 0 6px 12px rgba(0,0,0,0.3);
     }
     .transducer:active {
         cursor: grabbing;
         box-shadow: 0 2px 4px rgba(0,0,0,0.4); /* Pressed state */
     }

     .transducer-tip {
         width: 100%;
         height: 8px; /* Taller tip */
         background: linear-gradient(to top, #666, #888); /* Gradient for tip */
         border-bottom-left-radius: 6px;
         border-bottom-right-radius: 6px;
     }

    .pulse-canvas {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none; /* Allow clicks/drags on elements below */
        z-index: 5; /* Below transducer */
    }

    .display-area {
        display: flex;
        width: 98%; /* Match organ model width */
        gap: 25px; /* Increased gap */
        justify-content: space-between;
        min-height: 200px; /* Ensure display area has minimum height */
    }

    .amode-display, .bmode-display {
        border: 1px solid #b0c4de; /* Softer border */
        border-radius: 8px;
        background-color: #f8f8ff; /* Lighter background */
        padding: 15px; /* More padding */
        box-sizing: border-box;
        text-align: center;
        display: flex;
        flex-direction: column;
    }

    .amode-display {
        width: 180px; /* Fixed width for A-mode */
        flex-shrink: 0; /* Prevent shrinking */
    }

    .bmode-display {
        flex-grow: 1; /* B-mode takes remaining space */
        position: relative;
        overflow: hidden;
        background-color: #0a0a0a; /* Very dark background for B-mode */
    }

     .bmode-scan-line {
         position: absolute;
         top: 0;
         width: 2px; /* Thicker marker line */
         background-color: rgba(255, 255, 0, 0.5); /* Yellowish marker */
         pointer-events: none;
         z-index: 2;
     }


    .amode-display h2, .bmode-display h2 {
        font-size: 1.1em; /* Slightly larger font */
        margin-top: 0;
        margin-bottom: 15px; /* More space below header */
        color: #1a1a1a; /* Darker header color */
    }

    #amode-canvas {
        border: 1px solid #a0a0a0; /* Darker border */
        background-color: #fff;
        width: 100%;
        flex-grow: 1; /* Allow canvas to fill container height */
    }

    #bmode-canvas {
        border: 1px solid #a0a0a0; /* Darker border */
        background-color: #000; /* Black background */
        width: 100%;
        flex-grow: 1; /* Allow canvas to fill container height */
    }

    .instructions {
        margin-top: 10px;
        font-size: 1.1em;
        color: #0056b3; /* Blue color for instructions */
        font-weight: bold;
        text-align: center;
        min-height: 1.5em; /* Reserve space */
        transition: opacity 0.5s ease-out;
    }


    #toggle-explanation {
        display: block;
        margin: 30px auto 10px auto; /* More margin top/bottom */
        padding: 12px 25px; /* More padding */
        font-size: 1.1em; /* Slightly larger font */
        cursor: pointer;
        border: none;
        border-radius: 6px; /* Slightly more rounded */
        background-color: #007bff;
        color: white;
        transition: background-color 0.2s ease-in-out, transform 0.1s ease-in-out;
    }

    #toggle-explanation:hover {
        background-color: #0056b3;
    }
     #toggle-explanation:active {
         transform: scale(0.98);
     }


    #explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #b0c4de; /* Softer border */
        border-radius: 8px;
        background-color: #f0f8ff; /* Alice blue */
        line-height: 1.7; /* More line spacing */
        direction: rtl; /* Hebrew text direction */
        text-align: right; /* Align text to the right */
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.05); /* Subtle inner shadow */
    }

    #explanation h2, #explanation h3 {
        color: #004085; /* Darker blue for headers */
        border-bottom: 1px solid #cfe2ff; /* Lighter blue border */
        padding-bottom: 8px; /* More padding below */
        margin-bottom: 15px; /* More space below header */
        text-align: right;
    }

    #explanation p {
        margin-bottom: 18px; /* More space below paragraphs */
    }

    #explanation ul {
        margin-bottom: 18px;
        padding-right: 25px; /* More padding for list markers */
        list-style-type: disc;
    }

    #explanation li {
        margin-bottom: 10px; /* More space between list items */
    }
</style>
```