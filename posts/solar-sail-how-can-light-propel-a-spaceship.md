---
title: "מפרש סולארי: איך אור יכול להניע חללית?"
english_slug: solar-sail-how-can-light-propel-a-spaceship
category: "מדעים מדויקים / פיזיקה"
tags: ["מפרש סולארי", "הנעת חלליות", "קרינה אלקטרומגנטית", "לחץ קרינה", "פיזיקה בחלל"]
---

# מפרש סולארי: איך אור יכול להניע חללית?

דמיינו את עצמכם מרחפים בחלל העצום. בדרך כלל, חלליות נשענות על מנועים רבי עוצמה ששורפים טונות של דלק כדי להתקדם. אבל מה אם היינו יכולים לרתום את הכוח העצום של אור השמש כדי לשוט בין הכוכבים – בלי טיפת דלק? האם לאור, שמכיל פוטונים קטנטנים ונטולי מסה, באמת יש מספיק 'דחיפה' כדי להניע גוף ענק בחלל? הכירו את המפרש הסולארי, טכנולוגיה שמשנה את כללי המשחק!

**בואו נתנסה רגע לפני ההסבר:** השמש שולחת קרני אור (צבועות כאן בצהוב) לכיוון החללית שלנו. לחללית יש מפרש מיוחד, קל במיוחד ומחזיר אור. השתמשו במחוון למטה כדי לשנות את הזווית של המפרש, וצפו איך כוח הדחיפה (הווקטור הירוק) וכיוון קרני האור המוחזרות (בטורקיז) משתנים. שימו לב איך הכוח מתפצל לרכיב רדיאלי (אדום - דוחף הרחק מהשמש) ולרכיב טנגנציאלי (כחול - מאפשר "לנווט").

<div class="simulation-container">
    <div class="sun"></div>
    <div class="light-rays-container">
        <div class="light-ray"></div>
        <div class="light-ray"></div>
        <div class="light-ray"></div>
        <div class="light-ray"></div>
        <div class="light-ray"></div>
    </div>
    <div class="spaceship">
        <div class="sail-pivot"></div>
        <div class="sail"></div>
        <div class="spaceship-body"></div>

        <!-- Reflected rays -->
        <div class="reflected-rays-container">
            <div class="reflected-ray"></div>
            <div class="reflected-ray"></div>
            <div class="reflected-ray"></div>
            <div class="reflected-ray"></div>
            <div class="reflected-ray"></div>
        </div>

        <!-- Force vectors -->
        <div class="total-force-vector">
             <div class="arrowhead"></div>
        </div>
        <div class="radial-force-component">
             <div class="arrowhead"></div>
        </div>
         <div class="tangential-force-component">
             <div class="arrowhead"></div>
        </div>
    </div>

    <div class="vector-labels">
        <div class="total-label">סה"כ כוח</div>
        <div class="radial-label">רכיב רדיאלי (הרחק מהשמש)</div>
        <div class="tangential-label">רכיב טנגנציאלי (ניווט)</div>
    </div>
</div>

<div class="controls-section">
    <label for="sail-angle">זווית ההתקפה (זווית הנורמל מהאור הנכנס):</label>
    <input type="range" id="sail-angle" min="-90" max="90" value="0">
    <span id="angle-display">0°</span>
    <div class="angle-indicator"></div>
</div>

<button id="show-explanation">הצג הסבר מורחב</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מורחב: הנעת חללית באמצעות מפרש סולארי</h2>

    <h3>מבוא: מהו מפרש סולארי ומדוע הוא שונה מהנעה רגילה</h3>
    שכחו ממנועי רקטה רועשים ופולטי עשן. מפרש סולארי הוא אלגנטי ויעיל: הוא משתמש בלחץ הקרינה של אור הכוכבים (בעיקר השמש שלנו) כדי לדחוף את החללית, ללא צורך בשריפת דלק. זה כמו סירת מפרש בים, אבל במקום רוח, הכוח מגיע מפוטונים של אור! המפרשים הללו עשויים מחומרים קלים, דקים במיוחד (לעתים בעובי של מיקרונים בודדים), בעלי שטח פנים ענק ורמת החזרה כמעט מושלמת, כדי למקסם את הקליטה וההחזרה של פוטוני האור.

    <h3>העיקרון הפיזיקלי: איך קרינת אור (פוטונים) נושאת תנע</h3>
    אף שלעתים אנו מדמיינים אור כגל, בפיזיקה הקוונטית אור מורכב מיחידות אנרגיה דיסקרטיות הנקראות פוטונים. לפוטונים אין מסת מנוחה, אך יש להם תנע – כושר תנועה. כאשר פוטונים אלו פוגעים במשטח, הם מעבירים לו חלק מהתנע שלהם, ובכך מפעילים עליו כוח קטנטן. זהו לחץ הקרינה.

    <h3>לחץ קרינה: איך בליעה והחזרה של פוטונים יוצרים כוח</h3>
    כוח הדחיפה של מפרש סולארי נובע משינוי התנע של הפוטונים הפוגעים במפרש.
    *   **בליעה:** אם פוטון נבלע על ידי המפרש, הוא מעביר את התנע שלו למפרש בכיוון הפגיעה.
    *   **החזרה (חשוב יותר!):** אם פוטון מוחזר מהמפרש (כפי שקורה במפרש סולארי אידיאלי), הוא לא רק מעביר את התנע המקורי שלו למפרש, אלא מקבל תנע בכיוון ההפוך! סך הכל, שינוי התנע של פוטון מוחזר כפול מזה של פוטון נבלע. לפי החוק השלישי של ניוטון, שינוי התנע הזה גורם לכוח כפול המופעל על המשטח בהשוואה לבליעה. לכן, מפרשים סולאריים מתוכננים להיות מחזירי אור ככל הניתן. הכוח הכולל המופעל על המפרש ניצב למשטח המפרש.

    <h3>השוואה לרוח שמש (Solar Wind) - מדוע לחץ קרינה חשוב יותר</h3>
    החלל אינו ריק. השמש פולטת גם זרם רציף של חלקיקים טעונים (בעיקר פרוטונים ואלקטרונים) הנקרא רוח השמש. גם חלקיקים אלו נושאים תנע ויכולים להפעיל כוח על חללית. עם זאת, קרוב לשמש, לחץ הקרינה של הפוטונים חזק משמעותית מהכוח המופעל על ידי רוח השמש. למרות שחלקיקי רוח השמש מסיביים יותר מפוטונים, צפיפות הפוטונים וסך התנע שהם נושאים גדולים יותר, מה שהופך את לחץ הקרינה לכוח המניע העיקרי עבור מפרשים סולאריים.

    <h3>השפעת זווית המפרש: כיצד כיוון המפרש משפיע על כיוון וגודל הכוח המופעל</h3>
    זה היופי של מפרש סולארי! בניגוד לרקטה שרק יכולה לדחוף קדימה (או אחורה), שינוי זווית המפרש ביחס לשמש מאפשר לכם לנווט. הכוח הכולל מלחץ הקרינה תמיד ניצב למשטח המפרש. כאשר המפרש ניצב לקרינה (כמו בסירה שפונה חזיתית לרוח), הכוח מקסימלי ומכוון ישירות הרחק מהשמש (זה הרכיב הרדיאלי). אך אם תטו את המפרש בזווית, הכוח הכולל עדיין יהיה ניצב לו, אך הוא יתפצל לשני רכיבים:
    1.  **רכיב רדיאלי:** דוחף את החללית הרחק מהשמש או לכיוון השמש (תלוי בזווית).
    2.  **רכיב טנגנציאלי:** פועל בניצב לקו המחבר את החללית לשמש. רכיב זה הוא שמאפשר לשנות את המסלול, להאיץ או להאט מסביב לשמש, ולמעשה "לשוט" בין כוכבי הלכת במסלולים מורכבים, בדומה לאופן שבו סירת מפרש יכולה לשוט כנגד כיוון הרוח. גודל הכוח הכולל המופעל על המפרש תלוי בזווית הפגיעה של האור - הוא מקסימלי כשהמפרש ניצב לאור ויורד כשהזווית גדלה.

    <h3>מדוע הנעה סולארית מתאימה למסעות ארוכים (האצה קבועה ואינסופית תיאורטית)</h3>
    היתרון העצום והייחודי של מפרש סולארי הוא שמרגע פריסתו, הוא לא דורש שום דלק. כל עוד יש אור מהשמש או מקור אור אחר, הוא ממשיך להפעיל כוח, גם אם קטן. כוח קבוע (על חללית שמסתה כמעט אינה משתנה) גורם להאצה קבועה. האצה קטנה אך מתמשכת לאורך חודשים ושנים יכולה להביא את החללית למהירויות אדירות, הרבה יותר גבוהות ממה שאפשרי עם מנועים כימיים מוגבלי דלק. זה הופך את המפרשים הסולאריים לאידיאליים למשימות חלל עמוק ארוכות מאוד, כמו הגעה למערכות כוכבים אחרות בעתיד הרחוק.

    <h3>אתגרים וחסרונות (גודל המפרש, כוח קטן קרוב לכבידה)</h3>
    החיים בחלל לא פשוטים, וגם למפרשים סולאריים יש אתגרים. ראשית, הכוח שמפעיל אור השמש הוא חלש מאוד. כדי לייצר דחיפה משמעותית, שטח המפרש צריך להיות עצום – מאות, אלפי ואפילו מיליוני מטרים רבועים! פריסת מבנים כה ענקיים ודקים בחלל ושמירה על שלמותם ויציבותם הם אתגרים הנדסיים עצומים. שנית, הכוח הקטן הזה אינו מספיק כדי להתגבר על כוחות הכבידה החזקים ליד כוכבי לכת גדולים או ירחים. לכן, הנעה סולארית יעילה יותר בחלל הפתוח, הרחק מגופים מסיביים.

    <h3>דוגמאות למשימות ומפרשים סולאריים אמיתיים</h3>
    טכנולוגיית המפרשים הסולאריים כבר אינה מדע בדיוני! המשימה היפנית IKAROS שוגרה ב-2010 והייתה הראשונה להדגים בהצלחה תנועה מבוקרת והאצה באמצעות מפרש סולארי בחלל הבין-פלנטרי. נאס"א וגופים נוספים מפתחים ומנסים טכנולוגיות דומות, כמו משימות NanoSail-D ו-LightSail של The Planetary Society. העתיד של חקר החלל אולי יראה פחות להבות רקטה ויותר "מפרשים" ענקיים המשייטים בשקט על אור הכוכבים.

</div>

<script>
    const sail = document.querySelector('.sail');
    const angleInput = document.getElementById('sail-angle');
    const angleDisplay = document.getElementById('angle-display');
    const angleIndicator = document.querySelector('.angle-indicator');

    const totalForceVector = document.querySelector('.total-force-vector');
    const radialForceComponent = document.querySelector('.radial-force-component');
    const tangentialForceComponent = document.querySelector('.tangential-force-component');

    const totalLabel = document.querySelector('.vector-labels .total-label');
    const radialLabel = document.querySelector('.vector-labels .radial-label');
    const tangentialLabel = document.querySelector('.vector-labels .tangential-label');

    const reflectedRaysContainer = document.querySelector('.reflected-rays-container');
    const reflectedRays = document.querySelectorAll('.reflected-ray');

    const showExplanationButton = document.getElementById('show-explanation');
    const explanationDiv = document.getElementById('explanation');

    const simulationContainer = document.querySelector('.simulation-container');
    const spaceship = document.querySelector('.spaceship');

    // Initial position of spaceship and sail pivot relative to container center (50% 50%)
    const SPACESHIP_CENTER_X = 0; // relative to spaceship's own origin (center)
    const SPACESHIP_CENTER_Y = 0;

    // Pivot position relative to spaceship center (adjust based on your HTML/CSS positioning)
    // The sail-pivot is centered within .spaceship (left: 50%, top: 50%).
    // The sail and vectors rotate around this point.
    const PIVOT_X = 0; // 50% of spaceship width
    const PIVOT_Y = 0; // 50% of spaceship height

    function updateSailAndForce() {
        let angle = parseInt(angleInput.value); // This is the angle of the NORMAL from the incoming light direction (horizontal).
        angleDisplay.textContent = angle + '°';

        let angleInRadians = (angle * Math.PI) / 180; // Angle of Incidence

        // --- Sail Rotation ---
        // Sail surface is perpendicular to the normal.
        // If normal is at 'angle' deg from horizontal (0 deg), sail is at (90 - angle) deg from horizontal.
        // CSS rotate(0deg) is horizontal right.
        // Let's position the sail pivot at the rotation point.
        let sailCssRotation = 90 - angle;
        sail.style.transform = `translate(0, -50%) rotate(${sailCssRotation}deg)`; // transform-origin set in CSS

         // --- Angle Indicator ---
        angleIndicator.style.transform = `translate(-50%, -50%) rotate(${angle}deg)`; // Positioned relative to controls, visualising the normal

        // --- Force Vector (Total) ---
        // Force direction is along the normal, away from the surface. Angle is the angle of the normal from horizontal.
        // Force magnitude is proportional to cos(angle of incidence) assuming perfect reflection (or 2*cos^2, but cos is simpler for visualization).
        // Let's use cos(angle) as it visually represents the component in the direction of the normal relative to the incoming light.
        let forceMagnitude = Math.max(0, Math.cos(angleInRadians)); // 0 to 1
        let totalVectorLength = forceMagnitude * 150; // Max length 150px, scale it

        if (totalVectorLength > 5) { // Show if length is meaningful
            totalForceVector.style.display = 'block';
            totalForceVector.style.width = totalVectorLength + 'px';
            // The vector itself is rotated by the normal angle
            totalForceVector.style.transform = `translate(${PIVOT_X}px, ${PIOT_Y}px) rotate(${angle}deg)`; // Position relative to pivot
            totalLabel.style.cssText = `
                display: block;
                transform: translate(${PIVOT_X + totalVectorLength}px, ${PIVOT_Y}px) rotate(${angle}deg) translate(10px, -50%); /* Position near end, rotate with vector */
            `;
        } else {
            totalForceVector.style.display = 'none';
             totalLabel.style.display = 'none';
        }

        // --- Force Components (Radial and Tangential) ---
        // Radial component is horizontal (angle 0). Tangential is vertical (angle 90 or -90).
        // Total Force Vector has length F_total, at angle `angle` from horizontal.
        // F_radial = F_total * cos(angle)
        // F_tangential = F_total * sin(angle)
        let radialMagnitude = forceMagnitude * Math.cos(angleInRadians);
        let tangentialMagnitude = forceMagnitude * Math.sin(angleInRadians);

        let radialVectorLength = Math.max(0, radialMagnitude * 150); // Scale like total
        let tangentialVectorLength = Math.abs(tangentialMagnitude * 150); // Use absolute length

        if (radialVectorLength > 5) {
             radialForceComponent.style.display = 'block';
             radialForceComponent.style.width = radialVectorLength + 'px';
             radialForceComponent.style.transform = `translate(${PIVOT_X}px, ${PIVOT_Y}px) rotate(0deg)`; // Radial is always horizontal
             radialLabel.style.cssText = `
                display: block;
                transform: translate(${PIVOT_X + radialVectorLength}px, ${PIVOT_Y}px) translate(10px, -50%); /* Position near end */
             `;
        } else {
             radialForceComponent.style.display = 'none';
             radialLabel.style.display = 'none';
        }

        if (tangentialVectorLength > 5) {
             tangentialForceComponent.style.display = 'block';
             tangentialForceComponent.style.width = tangentialVectorLength + 'px';
             // Tangential direction is 90deg up if angle is positive, -90deg down if angle is negative.
             let tangentialCssRotation = (tangentialMagnitude > 0) ? 90 : -90;
             tangentialForceComponent.style.transform = `translate(${PIVOT_X}px, ${PIVOT_Y}px) rotate(${tangentialCssRotation}deg)`;
              tangentialLabel.style.cssText = `
                display: block;
                transform: translate(${PIVOT_X + (tangentialMagnitude > 0 ? 0 : -tangentialVectorLength)}px, ${PIVOT_Y + (tangentialMagnitude > 0 ? -tangentialVectorLength : tangentialVectorLength)}px) rotate(${tangentialCssRotation}deg) translate(10px, -50%); /* Position near end */
             `;
        } else {
             tangentialForceComponent.style.display = 'none';
             tangentialLabel.style.display = 'none';
        }

         // --- Reflected Rays ---
         // Reflected angle = 2 * angle of incidence (measured from the incoming ray direction, which is horizontal).
         // The angle 'angle' from the slider is the angle of the normal from horizontal.
         // Angle of incidence = angle.
         // Reflected angle from horizontal = 2 * angle.
         let reflectedCssRotation = 2 * angle;

         reflectedRaysContainer.style.transform = `translate(${PIVOT_X}px, ${PIVOT_Y}px) rotate(${reflectedCssRotation}deg)`;

         // Show rays only if magnitude is reasonably large and angle is not exactly 90 or -90
         if (forceMagnitude > 0.05 && Math.abs(angle) < 90) { // Adjust threshold if needed
             reflectedRaysContainer.style.display = 'block';
              reflectedRays.forEach(ray => ray.style.opacity = forceMagnitude); // Dim reflected rays slightly at larger angles
         } else {
             reflectedRaysContainer.style.display = 'none';
         }

         // Position labels (Need to refine positioning relative to vectors)
         // Labels should ideally follow the *end* of the vectors.
         // Let's update label positions directly. This might require more complex logic
         // or positioning them relative to the vector divs with CSS.
         // For now, let's use a simpler fixed offset relative to the pivot, rotated.
         // A better approach would be to position labels relative to the arrowheads.
         // Example for total label (moved into the main force block update):
         // totalLabel.style.transform = `translate(${PIVOT_X + totalVectorLength}px, ${PIVOT_Y}px) rotate(${angle}deg) translate(10px, -50%)`;

    }

    angleInput.addEventListener('input', updateSailAndForce);

    showExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        showExplanationButton.textContent = isHidden ? 'הסתר הסבר מורחב' : 'הצג הסבר מורחב';
        showExplanationButton.classList.toggle('active', isHidden); // Add a class for styling
    });

    // Initialize
    updateSailAndForce(); // Set initial state based on default input value
</script>

<style>
    /* General Page Styling */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        color: #e0e0e0; /* Light text for dark background */
        background-color: #1a1a2e; /* Dark, space-like background */
        direction: rtl; /* Right-to-left for Hebrew */
        text-align: right;
        margin: 0;
        padding: 20px;
        overflow-x: hidden; /* Prevent horizontal scroll */
    }

    h1, h2, h3 {
        color: #00bcd4; /* Cyan-like color for headings */
        margin-bottom: 15px;
        line-height: 1.4;
    }
     h1 { font-size: 2em; margin-bottom: 20px; }
     h2 { font-size: 1.6em; border-bottom: 2px solid #00bcd4; padding-bottom: 5px; margin-top: 30px; }
     h3 { font-size: 1.3em; color: #ff9800; margin-top: 25px; margin-bottom: 10px; } /* Orange for subheadings */

    p {
        margin-bottom: 15px;
        font-size: 1.1em;
    }

    /* Simulation Container */
    .simulation-container {
        position: relative;
        width: 100%;
        max-width: 700px; /* Slightly larger container */
        height: 450px; /* Slightly taller */
        background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%); /* Gradient for space effect */
        margin: 30px auto;
        overflow: hidden;
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5); /* Add shadow */
        border: 1px solid #444; /* Subtle border */
    }

    /* Sun */
    .sun {
        position: absolute;
        left: 50px; /* Position further left */
        top: 50%;
        transform: translateY(-50%);
        width: 60px; /* Larger sun */
        height: 60px;
        background: radial-gradient(circle, #ffff00 0%, #ff9800 60%, #ff5722 100%); /* Gradient sun */
        border-radius: 50%;
        box-shadow: 0 0 30px #ffff00, 0 0 50px #ff9800, 0 0 80px #ff5722; /* Add glow */
        z-index: 2; /* Ensure sun is above rays visually */
    }

    /* Light Rays (Incoming) */
    .light-rays-container {
        position: absolute;
        left: 65px; /* Start near the sun's edge */
        top: 50%;
        transform: translateY(-50%);
        width: calc(50% - 65px); /* Extend towards the center */
        height: 50px; /* Container height for ray spacing */
        display: flex;
        flex-direction: column;
        justify-content: space-between; /* Space rays out */
        align-items: flex-end; /* Align rays to the right edge of container */
        z-index: 1;
    }
    .light-ray {
         width: 100%; /* Ray fills container width */
         height: 2px; /* Thicker rays */
         background-color: #ffff00; /* Yellow */
         position: relative; /* For pseudo-elements/animation */
         overflow: hidden; /* Hide animation overflow */
    }
    /* Add animation to light rays */
    .light-ray::after {
        content: '';
        position: absolute;
        top: 0;
        left: -200%; /* Start off screen */
        width: 200%;
        height: 100%;
        background: linear-gradient(to right, transparent, rgba(255, 255, 0, 0.8), transparent);
        animation: light-flow 3s linear infinite;
    }
    @keyframes light-flow {
        0% { left: -200%; }
        100% { left: 100%; }
    }


    /* Spaceship (Container for body, sail, pivot, vectors) */
    .spaceship {
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%); /* Center the spaceship container */
        width: 200px; /* Give it a defined size for positioning internal elements */
        height: 100px;
         /* background-color: rgba(255,0,0,0.1); /* Debug */
        z-index: 3; /* Ensure spaceship elements are on top */
    }

    /* Sail Pivot (Conceptual center of rotation) */
    .sail-pivot {
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%); /* Center it within the spaceship container */
        width: 8px;
        height: 8px;
        background-color: #9e9e9e; /* Grey */
        border-radius: 50%;
        z-index: 10; /* On top of sail and body */
         box-shadow: 0 0 8px rgba(158, 158, 158, 0.5);
    }

    /* Sail */
    .sail {
        position: absolute;
        left: 50%; /* Position relative to spaceship container center */
        top: 50%;
        transform-origin: 0% 50%; /* Rotate around its left end (which aligns with the pivot) */
        width: 180px; /* Longer sail */
        height: 4px; /* Thicker sail line */
        background: linear-gradient(to right, #e0e0e0, #ffffff, #e0e0e0); /* Make it look reflective */
        border-radius: 2px;
        z-index: 5; /* Below pivot, above body */
        transition: transform 0.2s ease-out; /* Smooth rotation */
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.3); /* Subtle glow */
    }

    /* Spaceship Body */
    .spaceship-body {
        position: absolute;
        left: 50%; /* Position relative to spaceship container center */
        top: 50%;
        transform: translate(15px, -50%); /* Position body to the right of the pivot */
        width: 40px; /* Slightly larger body */
        height: 25px;
        background-color: #455a64; /* Blue-grey */
        border-radius: 6px;
        z-index: 6;
        box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5);
    }

    /* Reflected Rays */
     .reflected-rays-container {
        position: absolute;
        left: 50%; /* Relative to spaceship center */
        top: 50%; /* Relative to spaceship center */
        transform-origin: 0% 50%; /* Rotate around the pivot point */
        width: 150px; /* Length of reflected rays */
        height: 50px; /* Container height for spacing */
        display: flex;
        flex-direction: column;
        justify-content: space-between; /* Space rays out */
        align-items: flex-start; /* Align rays to the left edge */
        z-index: 4; /* Below sail, above background */
        transition: transform 0.2s ease-out; /* Smooth rotation */
     }
     .reflected-ray {
        width: 100%; /* Ray fills container width */
        height: 2px; /* Thicker rays */
        background-color: #00e5ff; /* Bright Cyan */
        position: relative;
         overflow: hidden;
     }
      /* Add animation to reflected rays */
    .reflected-ray::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0%; /* Start at the pivot end */
        width: 200%;
        height: 100%;
        background: linear-gradient(to left, transparent, rgba(0, 229, 255, 0.8), transparent);
        animation: reflected-light-flow 3s linear infinite;
    }
     /* Need to adjust animation direction based on ray direction if not horizontal */
     /* Simple left-to-right flow for now */
     @keyframes reflected-light-flow {
        0% { left: 0%; }
        100% { left: -200%; }
    }


    /* Force Vectors */
    .total-force-vector, .radial-force-component, .tangential-force-component {
        position: absolute;
        left: 50%; /* Relative to spaceship center */
        top: 50%; /* Relative to spaceship center */
        transform-origin: 0% 50%; /* Rotate around the pivot point */
        height: 4px; /* Thicker vectors */
        transition: width 0.2s ease-out, transform 0.2s ease-out, background-color 0.2s ease-out; /* Smooth transitions */
        z-index: 7; /* On top of spaceship body */
    }

    .total-force-vector {
        background-color: #76ff03; /* Lime green */
    }
    .radial-force-component {
         background-color: #ff1744; /* Red */
    }
     .tangential-force-component {
         background-color: #2979ff; /* Blue */
     }

    /* Arrowheads */
    .total-force-vector .arrowhead,
    .radial-force-component .arrowhead,
    .tangential-force-component .arrowhead {
        position: absolute;
        right: -8px; /* Position arrowhead at the end */
        top: -6px; /* Center vertically */
        width: 0;
        height: 0;
        border-top: 6px solid transparent;
        border-bottom: 6px solid transparent;
        /* border-left color will match parent vector */
    }
    .total-force-vector .arrowhead { border-left: 12px solid #76ff03; }
    .radial-force-component .arrowhead { border-left: 12px solid #ff1744; }
    .tangential-force-component .arrowhead { border-left: 12px solid #2979ff; }


    /* Vector Labels */
    .vector-labels {
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%); /* Position relative to spaceship container center */
        width: 100%; /* Container to hold labels */
        height: 100%;
         /* background-color: rgba(0,255,0,0.1); /* Debug */
        pointer-events: none; /* Allow clicks to pass through */
        z-index: 8; /* On top of vectors */
    }
    .vector-labels div {
        position: absolute;
        white-space: nowrap;
        font-size: 0.9em;
        font-weight: bold;
        color: #fff;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
        transition: transform 0.2s ease-out, opacity 0.2s ease-out;
        display: none; /* Hidden by default */
    }
     .total-label { color: #76ff03; }
    .radial-label { color: #ff1744; }
    .tangential-label { color: #2979ff; }


    /* Controls Section */
    .controls-section {
        text-align: center;
        margin-top: 25px;
        padding: 15px;
        background-color: #2a2a4a; /* Darker background for controls */
        border-radius: 8px;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        position: relative; /* Needed for angle indicator positioning */
    }

    .controls-section label {
        margin-right: 15px;
        color: #b3e5fc; /* Light blue color */
        font-size: 1.1em;
        vertical-align: middle;
    }

    .controls-section input[type="range"] {
        -webkit-appearance: none; /* Override default appearance */
        appearance: none;
        width: 250px;
        height: 8px;
        background: #555;
        outline: none;
        opacity: 0.9;
        transition: opacity .2s;
        border-radius: 5px;
        vertical-align: middle;
    }

    .controls-section input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #00bcd4;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
    }

    .controls-section input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #00bcd4;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
    }

    .controls-section span#angle-display {
        display: inline-block;
        min-width: 40px;
        margin-left: 15px;
        font-size: 1.1em;
        font-weight: bold;
        color: #fff;
        vertical-align: middle;
    }

     /* Angle Indicator (Visual representation of the normal vector on the control) */
     .angle-indicator {
        position: absolute;
        left: 50%; /* Center horizontally within controls section */
        top: calc(100% - 10px); /* Position below the slider */
        transform: translate(-50%, -50%); /* Center the element itself */
        width: 60px;
        height: 3px;
        background-color: #b3e5fc; /* Light blue */
        border-radius: 2px;
        transition: transform 0.2s ease-out;
        transform-origin: 0% 50%; /* Rotate around its left end */
        /* This needs to be positioned relative to the container, not the spaceship */
        /* Let's move this out of the .spaceship styles if needed */
     }


    /* Explanation Button */
    button#show-explanation {
        display: block;
        margin: 25px auto;
        padding: 12px 25px;
        font-size: 1.2em;
        cursor: pointer;
        background-color: #007bff; /* Blue button */
        color: white;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }

    button#show-explanation:hover {
        background-color: #0056b3;
        transform: translateY(-2px);
    }
     button#show-explanation.active {
         background-color: #dc3545; /* Red when showing explanation */
     }
     button#show-explanation.active:hover {
          background-color: #c82333;
     }

    /* Explanation Section */
    #explanation {
        margin-top: 30px;
        padding-top: 30px;
        border-top: 2px dashed #444; /* Dashed separator */
        color: #c0c0c0; /* Lighter text for explanation */
    }

    #explanation h3 {
        margin-top: 25px;
        margin-bottom: 10px;
        color: #ff9800; /* Orange */
    }

    #explanation p {
        margin-bottom: 15px;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        h1 { font-size: 1.8em; }
        h2 { font-size: 1.4em; }
        h3 { font-size: 1.2em; }
        p { font-size: 1em; }
        .simulation-container { height: 350px; }
        .spaceship { transform: translate(-50%, -50%) scale(0.8); } /* Scale down spaceship elements */
        .controls-section input[type="range"] { width: 200px; }
        button#show-explanation { font-size: 1.1em; padding: 10px 20px; }
    }
</style>
```