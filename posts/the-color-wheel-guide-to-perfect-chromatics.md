---
title: "קסם הצבעים: גלגל הצבעים האינטראקטיבי והסודות ליצירת פלטות מנצחות"
english_slug: the-color-wheel-guide-to-perfect-chromatics
category: "אמנות ועיצוב / עיצוב גרפי"
tags:
  - צבעים
  - גלגל צבעים
  - הרמוניית צבעים
  - תורת הצבע
  - עיצוב
  - UX
---
# קסם הצבעים: גלגל הצבעים האינטראקטיבי והסודות ליצירת פלטות מנצחות

הצבעים מקיפים אותנו בכל מקום – באמנות, בעיצוב, בטבע... אבל איך בוחרים את השילוב הנכון? מה גורם לפלטה אחת להיראות הרמונית ומלאת חיים, בעוד אחרת צורמת בעין? הכירו את גלגל הצבעים – הכלי העוצמתי שיחשוף בפניכם את הסודות שמאחורי בחירות צבע מוצלחות וילמד אתכם ליצור קומפוזיציות צבעוניות שפשוט 'עובדות'.

<div id="color-wheel-app">
    <div class="app-controls">
        <label for="harmony-type" class="control-label">בחרו הרמוניה:</label>
        <div class="select-wrapper">
             <select id="harmony-type" class="control-select">
                <option value="complementary">צבע משלים</option>
                <option value="analogous">צבעים אנלוגיים (סמוכים)</option>
                <option value="triadic">צבעים טריאדיים (משולש)</option>
                <option value="tetradic">צבעים טטרדיים (מרובע)</option>
                <option value="split-complementary">צבעים משלימים מפוצלים</option>
            </select>
        </div>
       <div class="color-display-area">
            <span class="control-label">צבע בסיס:</span>
            <div id="selected-color-display" class="color-swatch large"></div>
            <span class="control-label">פלטת הרמוניה:</span>
            <div id="harmony-colors-display" class="color-swatches-container"></div>
       </div>
    </div>
    <div class="color-wheel-container">
        <svg id="color-wheel-svg" width="400" height="400" viewBox="0 0 400 400">
            <!-- SVG elements will be drawn by JS -->
            <!-- A base circle or layer might be added here for visual structure -->
             <circle cx="200" cy="200" r="195" fill="none" stroke="#ddd" stroke-width="1"></circle>
        </svg>
    </div>
    <button id="toggle-explanation" class="toggle-button">הצג/הסתר הסבר מלא</button>
</div>

<style>
    /* General App Styling */
    #color-wheel-app {
        font-family: 'Heebo', sans-serif; /* More modern Hebrew font */
        direction: rtl; /* Ensure correct direction for Hebrew */
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px; /* Increased gap */
        padding: 30px; /* Increased padding */
        border: 1px solid #e0e0e0; /* Softer border */
        border-radius: 12px; /* More rounded corners */
        background: linear-gradient(to bottom right, #ffffff, #f0f0f0); /* Subtle gradient background */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Deeper shadow */
        max-width: 500px; /* Max width for the app container */
        margin: 20px auto; /* Center the app on the page */
    }

    /* Controls Styling */
    .app-controls {
        display: flex;
        flex-direction: column; /* Stack controls vertically */
        align-items: center;
        gap: 20px; /* Space between control groups */
        width: 100%; /* Controls take full width */
    }

    .control-label {
        font-size: 1rem; /* Standard font size */
        color: #555; /* Softer label color */
        margin-bottom: 5px; /* Space below label */
        display: block; /* Labels on their own line */
        text-align: center; /* Center labels */
    }

    .select-wrapper {
        position: relative;
        display: inline-block;
        width: 200px; /* Fixed width for select */
        background-color: #fff;
        border-radius: 6px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }

    .control-select {
        padding: 10px 15px;
        border-radius: 6px;
        border: 1px solid #ccc;
        background-color: transparent; /* Make actual select background transparent */
        -webkit-appearance: none; /* Remove default arrow */
        -moz-appearance: none;
        appearance: none;
        width: 100%; /* Make select fill wrapper */
        cursor: pointer;
        font-size: 1rem;
        color: #333;
    }

    .select-wrapper::after { /* Custom arrow */
        content: '▼';
        position: absolute;
        top: 50%;
        left: 15px; /* Position arrow on the left for RTL */
        transform: translateY(-50%) scaleX(-1); /* Flip arrow for RTL */
        pointer-events: none;
        color: #888;
        font-size: 0.8rem;
    }

    .color-display-area {
         display: flex;
         align-items: center;
         gap: 10px;
         flex-wrap: wrap; /* Allow wrapping on smaller screens */
         justify-content: center; /* Center color displays */
         width: 100%;
    }

    .color-swatch {
        width: 35px; /* Larger swatches */
        height: 35px;
        border: 2px solid #fff; /* White border for contrast */
        border-radius: 8px; /* More rounded */
        box-shadow: 0 2px 5px rgba(0,0,0,0.15); /* Subtle shadow */
        display: inline-block;
        vertical-align: middle;
        margin: 0 2px; /* Small margin between swatches */
        transition: transform 0.2s ease, box-shadow 0.2s ease; /* Smooth transitions */
        cursor: help; /* Indicate hover for info */
    }

    .color-swatch.large {
        width: 45px; /* Larger size for base color */
        height: 45px;
    }

    .color-swatches-container {
        display: flex;
        gap: 8px; /* Space between small swatches */
        flex-wrap: wrap;
        justify-content: center;
    }

    /* Color Wheel SVG Styling */
    .color-wheel-container {
        position: relative;
        width: 400px;
        height: 400px;
        /* Add subtle rotation animation on load? */
         animation: rotateIn 1s ease-out;
    }

     @keyframes rotateIn {
         from { transform: rotate(180deg); opacity: 0; }
         to { transform: rotate(0deg); opacity: 1; }
     }


    #color-wheel-svg {
        display: block;
        margin: 0 auto;
        cursor: crosshair;
        overflow: visible;
        /* Add a background radial gradient for depth */
        background: radial-gradient(circle at center, #ffffff 0%, #f0f0f0 50%, #e0e0e0 100%);
        border-radius: 50%; /* Make the container background round */
    }

    #color-wheel-svg circle {
         pointer-events: none; /* Base circle shouldn't block clicks */
    }

    .color-slice {
        cursor: pointer;
        transition: transform 0.1s ease-out; /* Smooth hover/click scale */
        stroke: rgba(255, 255, 255, 0.2); /* Subtle white stroke between slices */
        stroke-width: 0.5;
    }

    .color-slice:hover {
        transform: scale(1.05); /* Slightly larger on hover */
        stroke: rgba(255, 255, 255, 0.5);
    }

    .color-slice.selected {
         transform: scale(1.08); /* Larger scale for selected */
         stroke: rgba(0, 0, 0, 0.5); /* Darker stroke for selected */
         stroke-width: 1;
         z-index: 1; /* Bring selected slice to front (might need JS reordering) */
    }


    .harmony-line {
        stroke: rgba(50, 50, 50, 0.8); /* Darker, more visible lines */
        stroke-width: 2.5; /* Thicker lines */
        pointer-events: none;
        /* Add a dash effect? Or just solid */
         /* stroke-dasharray: 5, 5; */
         transition: stroke 0.3s ease-out; /* Smooth transition for color/opacity */
    }

     .harmony-shape {
        fill: none; /* No fill */
        stroke: rgba(50, 50, 50, 0.8); /* Match line color */
        stroke-width: 2.5;
        pointer-events: none;
        /* stroke-dasharray: 5, 5; */
        transition: stroke 0.3s ease-out;
     }

     .selected-color-indicator {
         fill: #333; /* Dark indicator fill */
         stroke: #fff; /* White stroke for contrast */
         stroke-width: 2.5; /* Thicker stroke */
         pointer-events: none;
         /* Add pulse animation */
         animation: pulse 1s infinite alternate;
     }

     @keyframes pulse {
         from { transform: scale(1); opacity: 1; }
         to { transform: scale(1.2); opacity: 0.8; }
     }


    /* Explanation Section Styling */
    #explanation {
        margin-top: 30px;
        border-top: 1px solid #eee;
        padding-top: 30px;
        display: none; /* Initially hidden */
        opacity: 0; /* Start with opacity 0 for fade-in */
        transition: opacity 0.5s ease-out; /* Fade-in transition */
        max-width: 700px; /* Max width for text block */
        text-align: justify; /* Justify text */
        line-height: 1.8; /* Improved readability */
        color: #333;
    }

    #explanation.visible {
        display: block;
        opacity: 1;
    }

    #toggle-explanation {
        display: block;
        margin: 30px auto 0; /* Space below app, center button */
        padding: 12px 25px; /* Larger button */
        font-size: 1.1rem; /* Larger font */
        cursor: pointer;
        border: none;
        border-radius: 6px; /* More rounded */
        background-color: #007bff; /* Primary blue color */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3); /* Blue shadow */
    }

    #toggle-explanation:hover {
        background-color: #0056b3; /* Darker blue on hover */
        transform: translateY(-1px); /* Slight lift effect */
    }

    #toggle-explanation:active {
         transform: translateY(0); /* Press effect */
         box-shadow: 0 2px 4px rgba(0, 123, 255, 0.5);
     }

    #explanation h2 {
        margin-top: 25px;
        margin-bottom: 15px;
        color: #007bff; /* Blue color for headings */
        text-align: center;
        font-size: 1.8rem;
    }

    #explanation h3 {
         margin-top: 20px;
         margin-bottom: 10px;
         color: #555;
         font-size: 1.4rem;
     }

    #explanation p {
        margin-bottom: 15px;
    }

    #explanation ul {
        margin-left: 25px; /* Increased indentation */
        padding-right: 0; /* Remove default right padding */
        list-style-type: disc;
    }

    #explanation li {
        margin-bottom: 10px;
        padding-right: 5px; /* Small padding for bullet points */
    }

     #explanation strong {
         color: #333;
     }

     /* Responsive adjustments */
     @media (max-width: 600px) {
         #color-wheel-app {
             padding: 20px;
             gap: 20px;
         }
         .color-wheel-container, #color-wheel-svg {
             width: 300px;
             height: 300px;
         }
         .color-swatch {
             width: 30px;
             height: 30px;
         }
          .color-swatch.large {
             width: 40px;
             height: 40px;
         }
         .control-select {
             width: 180px;
         }
         #toggle-explanation {
             font-size: 1rem;
             padding: 10px 20px;
         }
         #explanation h2 {
            font-size: 1.5rem;
         }
         #explanation h3 {
             font-size: 1.2rem;
         }
     }
</style>

<div id="explanation">
    <h2>מבוא: מהו גלגל צבעים ולמה הוא מפתח לעיצוב מנצח?</h2>
    <p>גלגל הצבעים הוא הרבה יותר מסתם דיאגרמה יפה. הוא מפה ויזואלית שמציגה את היחסים בין צבעים בצורה מעגלית, ומגלה לנו איך הם מתחברים, מתנגדים או משלימים זה את זה. הבנת הגלגל היא הבסיס הסודי שמאפשר לאמנים ומעצבים לבנות פלטות צבעים לא רק יפות, אלא כאלו שמדברות, מרגשות ויוצרות הרמוניה ויזואלית מושלמת. בואו נצלול לעולם הצבעים!</p>

    <h2>השחקנים הראשיים: צבעי יסוד, משנה ושלישון</h2>
    <ul>
        <li><strong>צבעי יסוד (Primary Colors):</strong> אבני הבניין של עולם הצבע. אי אפשר ליצור אותם מערבוב צבעים אחרים, אבל מהם אפשר ליצור כמעט כל צבע. במודל RYB הקלאסי (ציור ועיצוב פיזי), אלו הם אדום, צהוב וכחול. בגלגל שלנו, מבוסס גוון (Hue), הם ממוקמים במרחקים שווים ומשמשים נקודות עוגן.</li>
        <li><strong>צבעי משנה (Secondary Colors):</strong> קסם שקורה כשמערבבים שני צבעי יסוד בכמויות שוות. במודל RYB: ירוק (כחול+צהוב), כתום (אדום+צהוב), וסגול (אדום+כחול). תמצאו אותם על הגלגל בדיוק באמצע הדרך בין צבעי היסוד שיצרו אותם.</li>
        <li><strong>צבעי שלישון (Tertiary Colors):</strong> השלב הבא של הערבוב – צבע יסוד מתמזג עם צבע משנה סמוך לו. התוצאה היא גוונים עשירים כמו אדום-כתום, כחול-ירוק וצהוב-סגול. אלו הצבעים שמשלימים את גלגל 12 הצבעים המוכר והשימושי ביותר לעבודה.</li>
    </ul>

    <h2>הרמוניות צבעים: הסוד לשילובים בלתי נשכחים</h2>
    <p>הרמוניית צבעים היא שילוב של צבעים שנראה פשוט 'נכון' לעין. גלגל הצבעים מאפשר לנו לגלות את השילובים האלה באמצעות כללים גיאומטריים פשוטים. בחרו צבע בסיס על הגלגל וראו איך הכלי האינטראקטיבי חושף בפניכם את הפלטה המומלצת לפי סוג ההרמוניה שבחרתם:</p>
    <ul>
        <li>
            <h3>צבעים משלימים (Complementary)</h3>
            <p>שני צבעים הנמצאים בדיוק אחד מול השני על הגלגל (180 מעלות הפרש). זהו שילוב שמייצר את הניגודיות הכי דרמטית ועוצמתית שיש! אדום וירוק, כחול וכתום – הם 'קופצים' אחד ליד השני ויוצרים אנרגיה ויזואלית גבוהה. השתמשו בהם בחכמה, אולי צבע אחד דומיננטי והשני כהדגשה, כדי לא להציף.</p>
        </li>
        <li>
            <h3>צבעים אנלוגיים (Analogous)</h3>
            <p>שלושה צבעים או יותר ששוכנים זה ליד זה על הגלגל (טווח של 30-60 מעלות). הרמוניה זו נחשבת לזורמת, רגועה ונעימה במיוחד לעין, מכיוון שהצבעים חולקים גוון משותף או קרובים בגוון. דמיינו את צבעי השקיעה או היער – זו הרמוניה אנלוגית בפעולה. נהדר ליצירת אווירה אחידה ושקטה.</p>
        </li>
        <li>
            <h3>צבעים טריאדיים (Triadic)</h3>
            <p>שלושה צבעים המרוחקים באופן שווה על הגלגל (120 מעלות זה מזה, יוצרים משולש שווה צלעות). זהו שילוב תוסס, מאוזן ואנרגטי שמציע עניין ויזואלי רב מבלי להיות כאוטי. פלטות טריאדיות הן בחירה מצוינת כשרוצים מראה דינמי ושמח, כמו צבעי יסוד: אדום, צהוב, כחול.</p>
        </li>
        <li>
            <h3>צבעים טטרדיים/מרובעים (Tetradic/Square)</h3>
            <p>ארבעה צבעים המרוחקים באופן שווה על הגלגל (90 מעלות זה מזה, יוצרים ריבוע). זהו סוג ההרמוניה העשיר והמורכב ביותר, המציע עושר ויזואלי אדיר אך גם דורש שליטה גבוהה כדי לשמור על איזון. לרוב, כדאי לבחור צבע אחד שיהיה דומיננטי והשאר ישמשו כתמיכה והדגשה.</p>
        </li>
        <li>
            <h3>צבעים משלימים מפוצלים (Split Complementary)</h3>
            <p>קחו צבע בסיס אחד, ו במקום לקחת את המשלים הישיר שלו, קחו את שני הצבעים הסמוכים למשלים. לדוגמה: כחול, ו במקום כתום, קחו צהוב-כתום ואדום-כתום. זוהי פשרת הזהב: מציעה עוצמה ויזואלית מרשימה פחות מהמשלים הישיר, אך נעימה יותר לעין וקלה לשליטה. יוצרת קומפוזיציה הרמונית עם ניגודיות מעניינת.</p>
        </li>
    </ul>

    <h2>מגלגל הצבעים למציאות: איפה תשתמשו בזה?</h2>
    <p>הידע הזה הוא כוח! הוא ישדרג כל פרויקט שתעשו:</p>
    <ul>
        <li><strong>עיצוב גרפי ומיתוג:</strong> יצירת לוגואים בלתי נשכחים, אתרים שמושכים עין, ופרסומות שאי אפשר להתעלם מהן.</li>
        <li><strong>עיצוב פנים:</strong> הפיכת חללים ממקום סתמי לסביבה שמדברת אליכם, באמצעות בחירת צבעי קירות, רהיטים ואביזרים.</li>
        <li><strong>אופנה:</strong> שילוב בגדים ואביזרים ליצירת מראה הרמוני ומלא סטייל.</li>
        <li><strong>אמנות ויזואלית:</strong> ציור, צילום, פיסול – כל מה שדורש יצירת קומפוזיציה צבעונית שתשאיר רושם.</li>
        <li><strong>עיצוב מוצר:</strong> צבע המוצר משפיע ישירות על איך שהוא נתפס ועל מידת האטרקטיביות שלו ללקוח.</li>
    </ul>

    <h2>טיפים ממומחים ליצירת פלטות צבעים מנצחות</h2>
    <ul>
        <li><strong>נקודת מוצא:</strong> בחרו צבע בסיס אחד שיהווה את העוגן של הפלטה שלכם.</li>
        <li><strong>חקרו את ההרמוניות:</strong> השתמשו בגלגל כדי לראות אילו שילובים קלאסיים עובדים עם צבע הבסיס שלכם.</li>
        <li><strong>לא רק גוון:</strong> זכרו שבהירות (Value - כמה הצבע בהיר או כהה) ורוויה (Saturation - כמה הצבע טהור או עמום) קריטיות לא פחות מהגוון (Hue). שילוב חכם של גוונים, בהירויות ורוויות שונות יוצר פלטה עשירה ומעניינת.</li>
        <li><strong>כלל האצבע 60-30-10:</strong> כלל עיצובי פופולרי: השתמשו ב-60% מהשטח לצבע הראשי, ב-30% לצבע משני, וב-10% בלבד לצבע הדגשה. זה יוצר איזון ויזואלי נעים.</li>
        <li><strong>חשבו על המסר והאווירה:</strong> אילו רגשות ורעיונות אתם רוצים שהעיצוב שלכם יעורר? צבעים שונים מעבירים מסרים שונים (כחול = רוגע, אדום = אנרגיה, ירוק = טבע).</li>
        <li><strong>אל תפחדו להתנסות:</strong> גלגל הצבעים הוא כלי מדהים, אבל הוא לא חוק נוקשה. שחקו, ערבבו, שברו כללים (אחרי שהבנתם אותם!) וגלו שילובים ייחודיים משלכם.</li>
    </ul>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const svg = document.getElementById('color-wheel-svg');
        const harmonyTypeSelect = document.getElementById('harmony-type');
        const selectedColorDisplay = document.getElementById('selected-color-display');
        const harmonyColorsDisplay = document.getElementById('harmony-colors-display');
        const explanationDiv = document.getElementById('explanation');
        const toggleButton = document.getElementById('toggle-explanation');

        const width = parseInt(svg.getAttribute('width'));
        const height = parseInt(svg.getAttribute('height'));
        const centerX = width / 2;
        const centerY = height / 2;
        const radius = 180; // Radius for the main color wheel segments

        // Store the last selected angle
        let lastSelectedAngle = null;
        let selectedSliceElement = null;

        // Function to draw the color wheel segments
        function drawColorWheel() {
            // Remove any existing segments and overlays before drawing
            svg.querySelectorAll('.color-slice, .harmony-line, .harmony-shape, .selected-color-indicator').forEach(el => el.remove());

            const numSegments = 360; // 1 segment per degree
            const segmentAngle = 360 / numSegments;

            for (let i = 0; i < numSegments; i++) {
                const startAngle = i * segmentAngle;
                const endAngle = (i + 1) * segmentAngle;

                // Convert angles to radians for SVG path calculation
                // Adjust by -90 degrees to make 0 degrees point upwards (-Y axis in SVG)
                const startRad = (startAngle - 90) * Math.PI / 180;
                const endRad = (endAngle - 90) * Math.PI / 180;

                // Calculate start and end points on the arc
                const startX = centerX + radius * Math.cos(startRad);
                const startY = centerY + radius * Math.sin(startRad);
                const endX = centerX + radius * Math.cos(endRad);
                const endY = centerY + radius * Math.sin(endRad);

                // Use HSL to get the color (Hue changes, Saturation/Lightness fixed)
                const hue = i; // Hue corresponds to angle (0-359)
                const color = `hsl(${hue}, 100%, 50%)`; // Full saturation and 50% lightness

                // Create SVG path for the segment
                // Arc Flags: large-arc-flag (0 or 1), sweep-flag (0 or 1)
                // For 1-degree segments, large-arc-flag is always 0. sweep-flag is 1 for clockwise.
                const largeArcFlag = 0;
                const sweepFlag = 1;

                const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                // Path: Move to center, Line to start point on arc, Arc to end point on arc, Close path back to center
                path.setAttribute('d', `M ${centerX},${centerY} L ${startX},${startY} A ${radius},${radius} 0 ${largeArcFlag} ${sweepFlag} ${endX},${endY} Z`);
                path.setAttribute('fill', color);
                path.classList.add('color-slice');
                path.dataset.hue = hue; // Store the hue value
                svg.appendChild(path); // Add to SVG
            }
             // Re-append the base circle last so it's on top (for its stroke)
             const baseCircle = svg.querySelector('circle');
             if (baseCircle) {
                svg.appendChild(baseCircle);
             }
        }

        // Function to get the angle from coordinates relative to the circle center
        function getAngleFromCoords(x, y) {
             const rect = svg.getBoundingClientRect();
             const mouseX = x - rect.left;
             const mouseY = y - rect.top;

             const deltaX = mouseX - centerX;
             const deltaY = mouseY - centerY;

             // Calculate angle using atan2. Result is in radians, range (-PI, PI].
             // Convert to degrees and map to 0-360 range.
             let angle = Math.atan2(deltaY, deltaX) * 180 / Math.PI;

             // Adjust angle: atan2 0deg is at positive X (right). Color wheel 0deg is usually top (-Y).
             // We want 0deg at top and angle increasing clockwise.
             // atan2 gives angle relative to positive X. To shift 0deg to top (-Y),
             // add 90 degrees. Then ensure it's in 0-360 range.
             angle = (angle + 90 + 360) % 360;

             return angle; // Angle from 0 (top) to 359 (clockwise)
         }


        // Function to calculate HSL color from angle (simple direct mapping)
        function getHSLFromAngle(angle) {
             // Ensure angle is between 0 and 360
            let hue = (angle % 360 + 360) % 360;
            return `hsl(${hue}, 100%, 50%)`; // Use full saturation and 50% lightness for the wheel
        }


         // Function to calculate harmony angles based on a base angle and type
         function calculateHarmonyAngles(baseAngle, type) {
             let angles = [baseAngle]; // Start with the base angle

             // Define offsets in degrees based on harmony type
             const offsets = {
                 complementary: [180],
                 analogous: [-30, 30], // Angles relative to the base
                 triadic: [120, 240],
                 tetradic: [90, 180, 270],
                 split-complementary: [180 - 30, 180 + 30] // Relative to the complementary angle
             };

             const currentOffsets = offsets[type] || [];

             currentOffsets.forEach(offset => {
                 // Calculate the new angle, wrapping around 360
                 let newAngle = (baseAngle + offset + 360) % 360;
                 angles.push(newAngle);
             });

             // Return unique angles and sort them for consistent drawing
             return Array.from(new Set(angles)).sort((a, b) => a - b);
         }

        // Function to draw harmony lines, shapes, and indicators
        function drawHarmonyOverlay(angles) {
            // Remove previous lines, shapes, and indicators
            svg.querySelectorAll('.harmony-line, .harmony-shape, .selected-color-indicator').forEach(el => el.remove());

             if (!angles || angles.length === 0) return; // Should not happen if base color is selected

             // Ensure angles are numbers
             const numericAngles = angles.map(angle => parseFloat(angle));

             // Calculate points on the circumference for each angle
             const points = numericAngles.map(angle => {
                 // Convert angle back to radians for sin/cos. Adjust -90 to align 0deg with -Y axis.
                 const rad = (angle - 90) * Math.PI / 180;
                 return {
                     x: centerX + radius * Math.cos(rad),
                     y: centerY + radius * Math.sin(rad)
                 };
             });

             // Draw lines from center to points
             points.forEach(p => {
                 const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                 line.setAttribute('x1', centerX);
                 line.setAttribute('y1', centerY);
                 line.setAttribute('x2', p.x);
                 line.setAttribute('y2', p.y);
                 line.classList.add('harmony-line');
                 svg.appendChild(line);
             });

             // Draw shapes connecting points on the circumference
             if (points.length > 1) {
                 let shapePath = `M ${points[0].x},${points[0].y}`;
                 for (let i = 1; i < points.length; i++) {
                     shapePath += ` L ${points[i].x},${points[i].y}`;
                 }

                 // Close the shape for Triadic, Tetradic, Split Complementary (forms closed polygons)
                 if (points.length > 2) { // Complementary and Analogous don't typically form closed shapes like this
                    shapePath += ` Z`;
                    const shape = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                    shape.setAttribute('d', shapePath);
                    shape.classList.add('harmony-shape');
                    svg.appendChild(shape);
                 }
                 // Note: For Analogous, a shape connecting them along the arc might be desired,
                 // but drawing complex arcs that follow the wheel curvature in SVG path is complex.
                 // Stick to straight lines for simplicity as per technical constraints.
             }

             // Draw indicator on the selected base color point (first angle in the sorted list is the original base)
             // Use the original base angle before sorting for the indicator placement if possible,
             // or just assume the first angle in the sorted list is the base (which is true if it's the only single angle added first).
             const baseAngleForIndicator = numericAngles[0]; // Assuming the first angle is the base
             const baseRad = (baseAngleForIndicator - 90) * Math.PI / 180;
             const basePoint = {
                 x: centerX + radius * Math.cos(baseRad),
                 y: centerY + radius * Math.sin(baseRad)
             };
             const indicator = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
             indicator.setAttribute('cx', basePoint.x);
             indicator.setAttribute('cy', basePoint.y);
             indicator.setAttribute('r', 8); // Radius of the indicator circle
             indicator.classList.add('selected-color-indicator');
             svg.appendChild(indicator);
        }

        // Function to display harmony colors as swatches
        function displayHarmonyColors(colors) {
             harmonyColorsDisplay.innerHTML = ''; // Clear previous swatches
             colors.forEach(color => {
                 const swatch = document.createElement('div');
                 swatch.classList.add('color-swatch');
                 swatch.style.backgroundColor = color;
                 swatch.title = color; // Show color value on hover
                 harmonyColorsDisplay.appendChild(swatch);
             });
             // Add a subtle animation to swatches appearing
             harmonyColorsDisplay.querySelectorAll('.color-swatch').forEach((swatch, index) => {
                 swatch.style.setProperty('--delay', `${index * 0.05}s`);
                 swatch.style.transform = 'scale(0)';
                 swatch.style.opacity = '0';
                 setTimeout(() => {
                     swatch.style.transform = 'scale(1)';
                     swatch.style.opacity = '1';
                     swatch.style.transition = 'transform 0.3s ease-out var(--delay), opacity 0.3s ease-out var(--delay)';
                 }, 10); // Small delay to ensure transition is applied
             });
        }


        // Event listener for clicking on the SVG color slices
        svg.addEventListener('click', (event) => {
             const clickedElement = event.target;

             // Only process clicks on color slices
             if (clickedElement.classList.contains('color-slice')) {
                 // Remove 'selected' class from previously selected slice
                 if (selectedSliceElement) {
                     selectedSliceElement.classList.remove('selected');
                 }

                 // Add 'selected' class to the new slice
                 clickedElement.classList.add('selected');
                 selectedSliceElement = clickedElement;

                 // Get angle from data attribute or calculate from click position (safer to use click position for accuracy)
                 const angle = getAngleFromCoords(event.clientX, event.clientY);

                 // Store the last clicked angle
                 lastSelectedAngle = angle;

                 const baseColor = getHSLFromAngle(angle);

                 // Display selected base color swatch
                 selectedColorDisplay.style.backgroundColor = baseColor;
                 selectedColorDisplay.title = baseColor;
                 // Add pulse to selected swatch? Maybe just the indicator on the wheel.

                 // Calculate and display harmony
                 const harmonyType = harmonyTypeSelect.value;
                 const harmonyAngles = calculateHarmonyAngles(angle, harmonyType);
                 drawHarmonyOverlay(harmonyAngles);
                 // Map harmony angles back to HSL colors for displaying swatches
                 displayHarmonyColors(harmonyAngles.map(angle => getHSLFromAngle(angle)));
             }
        });

        // Event listener for changing harmony type
        harmonyTypeSelect.addEventListener('change', () => {
             // Check if a base color was previously selected by looking at lastSelectedAngle
             if (lastSelectedAngle !== null) {
                 const baseAngle = lastSelectedAngle; // Use the stored angle
                 const harmonyType = harmonyTypeSelect.value;
                 const harmonyAngles = calculateHarmonyAngles(baseAngle, harmonyType);
                 drawHarmonyOverlay(harmonyAngles);
                 // Map harmony angles back to HSL colors for displaying swatches
                 displayHarmonyColors(harmonyAngles.map(angle => getHSLFromAngle(angle)));

                 // Ensure the previously selected slice remains highlighted if exists
                 if (selectedSliceElement) {
                     // Recalculate the closest slice based on the stored angle and re-add class
                      // A more robust way might be to store the hue value directly
                      const targetHue = lastSelectedAngle;
                      const slices = svg.querySelectorAll('.color-slice');
                      let closestSlice = null;
                      let minDiff = 360;

                      slices.forEach(slice => {
                           const sliceHue = parseFloat(slice.dataset.hue);
                           // Calculate difference considering wrap-around
                           let diff = Math.abs(targetHue - sliceHue);
                           if (diff > 180) diff = 360 - diff;

                           if (diff < minDiff) {
                               minDiff = diff;
                               closestSlice = slice;
                           }
                      });

                      if (selectedSliceElement && selectedSliceElement !== closestSlice) {
                           selectedSliceElement.classList.remove('selected');
                      }
                      if (closestSlice) {
                           closestSlice.classList.add('selected');
                           selectedSliceElement = closestSlice; // Update selected element reference
                      }
                 }
             }
        });


        // Toggle explanation visibility
        toggleButton.addEventListener('click', () => {
            const isHidden = !explanationDiv.classList.contains('visible'); // Check based on class
            if (isHidden) {
                explanationDiv.style.display = 'block'; // First make it display block
                 // Use a small timeout to allow display:block to take effect before animating opacity
                setTimeout(() => {
                     explanationDiv.classList.add('visible');
                 }, 10); // A minimal delay
                toggleButton.textContent = 'הסתר הסבר מלא';
            } else {
                 explanationDiv.classList.remove('visible');
                 // Wait for the opacity transition to finish before hiding
                 explanationDiv.addEventListener('transitionend', function handler() {
                     explanationDiv.style.display = 'none';
                     explanationDiv.removeEventListener('transitionend', handler); // Remove listener after it fires
                 });
                toggleButton.textContent = 'הצג/הסתר הסבר מלא';
            }
        });


        // Initial drawing of the wheel when the page loads
        drawColorWheel();
    });
</script>
```