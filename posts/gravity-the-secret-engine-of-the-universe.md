---
title: "כוח הכבידה: המנוע הסודי של היקום"
english_slug: gravity-the-secret-engine-of-the-universe
category: "מדעים מדויקים / פיזיקה"
tags: כבידה, פיזיקה, ניוטון, משיכה, חלל, יקום
---

<div class="learning-container">

    <h1>כוח הכבידה: המנוע הסודי של היקום</h1>

    <p class="intro-text">מנפילת תפוח על ראשו של ניוטון ועד מסלול הכוכבים בגלקסיות ענק - כוח הכבידה הוא הכוח הבלתי נראה שמעצב את היקום שלנו. אבל איך בדיוק הוא עובד? מה גורם לעצמים למשוך זה את זה? והאם הוא באמת נעלם בחלל? בואו נגלה יחד!</p>

    <div class="interactive-app">
        <h2>גלו את כוח הכבידה בפעולה</h2>
        <p>שנו את הגדלים (מסות) של הגופים והמרחק ביניהם כדי לראות כיצד כוח המשיכה ביניהם משתנה באופן דרמטי.</p>
        <div class="controls">
            <div class="control-group">
                <label for="mass1-input">גוף א' (מסה בק"ג):</label>
                <input type="range" id="mass1-input" min="1e11" max="1e12" value="5e11" step="1e10">
                <span id="mass1-value" class="value-display"></span>
            </div>
            <div class="control-group">
                <label for="mass2-input">גוף ב' (מסה בק"ג):</label>
                <input type="range" id="mass2-input" min="1e11" max="1e12" value="5e11" step="1e10">
                <span id="mass2-value" class="value-display"></span>
            </div>
            <div class="control-group">
                <label for="distance-input">מרחק בין מרכזי הגופים (מטר):</label>
                <input type="range" id="distance-input" min="200" max="1500" value="800" step="20">
                <span id="distance-value" class="value-display"></span>
            </div>
        </div>
        <div id="simulation-area">
            <div id="object1" class="object">א</div>
            <div id="object2" class="object">ב</div>
             <!-- Force arrows represent the force on each object -->
            <div id="force-arrow1" class="force-arrow"></div>
            <div id="force-arrow2" class="force-arrow"></div>
        </div>
        <div id="force-display">עוצמת הכוח: <span id="force-value-span">0</span> ניוטון</div>
    </div>

    <button id="toggle-explanation-button" class="toggle-button">על כוח הכבידה - ההסבר המלא!</button>

    <div id="explanation-content" style="display: none;">
        <h2>מה מסתתר מאחורי כוח הכבידה?</h2>
        <p>כוח הכבידה הוא אחד הכוחות היסודיים שפועלים ביקום, והוא אחראי למשיכה ההדדית בין כל שני עצמים שיש להם מסה. דמיינו רשת ענקית ובלתי נראית שמחברת בין הכל - מכוכבי לכת ועד אבק קוסמי. ככל שהעצם כבד יותר (בעל מסה גדולה יותר), כך "הרשת" סביבו מתעקלת חזק יותר, ומושכת עצמים אחרים אליו.</p>

        <h3>עקרונות הכבידה המרכזיים (במילים פשוטות):</h3>
        <ul>
            <li><strong>כולם מושכים את כולם:</strong> כל גוף עם מסה מושך כל גוף אחר עם מסה. אין דחייה, רק משיכה!</li>
            <li><strong>ככל שיותר מסה, המשיכה חזקה יותר:</strong> לגוף ענק כמו כדור הארץ יש כבידה חזקה בהרבה מאשר לאבן קטנה. הכוח פרופורציונלי למכפלת המסות - אם תכפילו את המסה של אחד הגופים, הכוח יוכפל.</li>
            <li><strong>ככל שיותר רחוק, המשיכה חלשה בהרבה:</strong> מרחק הוא הגורם המשפיע ביותר! הכוח יורד בצורה מהירה מאוד כשהמרחק גדל. הוא פרופורציונלי הפוך לריבוע המרחק. זה אומר שאם תכפילו את המרחק פי 2, הכוח ירד פי $2^2=4$. אם תרחיקו פי 3, הכוח ירד פי $3^2=9$.</li>
        </ul>

        <h3>חוק הכבידה האוניברסלי של ניוטון: הנוסחה שמסבירה הכל!</h3>
        <p>סר אייזק ניוטון, גאון הפיזיקה, היה הראשון שסיפק לנו נוסחה אלגנטית שמסבירה כיצד לחשב את כוח הכבידה בין כל שני גופים. הנוסחה נראית כך:</p>
        <p class="formula">$$F = G \frac{m_1 m_2}{r^2}$$</p>
        <p>בואו נפרק אותה:</p>
        <ul>
            <li>$F$: עוצמת כוח הכבידה שפועל בין שני הגופים (נמדדת בניוטונים).</li>
            <li>$G$: קבוע הכבידה האוניברסלי - מספר קבוע שנקבע בניסויים (בערך $6.674 \times 10^{-11} \text{ N} \cdot (\text{m/kg})^2$). הוא מספר קטן מאוד, ולכן הכבידה מורגשת רק כשיש מסות ענקיות (כמו כוכבי לכת).</li>
            <li>$m_1$ ו-$m_2$: המסות של שני הגופים המושכים (בקילוגרמים).</li>
            <li>$r$: המרחק בין מרכזי שני הגופים (במטרים).</li>
        </ul>
        <p>הנוסחה הזו היא בדיוק מה שאתם רואים קורה בסימולציה למעלה! ככל ש- $m_1$ או $m_2$ גדלים, $F$ גדל. ככל ש- $r$ גדל, $F$ קטן, והוא קטן מהר כי $r$ במכנה בריבוע.</p>

        <h3>אז רגע... למה אסטרונאוטים "צפים" בחלל?</h3>
        <p>זו אחת הטעויות הנפוצות! זה *לא* בגלל שאין כבידה בחלל. כוח הכבידה של כדור הארץ עדיין חזק מאוד בגובה שבו מסתובבת תחנת החלל הבינלאומית. הסיבה שהם מרגישים חוסר משקל היא שהם, התחנה, וכל מה שבתוכה, נמצאים בנפילה חופשית מתמדת סביב כדור הארץ. הם "נופלים" לעבר הארץ, אבל בו זמנית הם נעים כל כך מהר הצידה (במהירות עצומה של כ-28,000 קמ"ש!) שהם מפספסים אותה כל הזמן ונשארים במסלול. זו אותה תחושה שהייתם מרגישים במעלית שצונחת (לפני הפגיעה, כמובן!) או בקצה מסלול רכבת הרים - אתם נופלים יחד עם הסביבה שלכם, ולכן מרגישים "חסרי משקל".</p>

        <h3>כבידה מסביבנו וביקום הרחוק:</h3>
        <ul>
            <li><strong>רגליים על הקרקע:</strong> כוח הכבידה של כדור הארץ הוא ששומר אותנו מלהתעופף לחלל.</li>
            <li><strong>הירח סביבנו:</strong> כבידת הארץ מחזיקה את הירח במסלולו.</li>
            <li><strong>אנחנו סביב השמש:</strong> כבידת השמש העצומה מחזיקה את כל כוכבי הלכת (כולל כדור הארץ!) במסלוליהם.</li>
            <li><strong>גלקסיות ענק:</strong> כבידה היא הכוח העיקרי שמחזיק מיליארדי כוכבים יחד בגלקסיות.</li>
            <li><strong>גאות ושפל:</strong> המשיכה הכבידתית של הירח והשמש גורמת לתנועת מי הים ויוצרת גאות ושפל.</li>
        </ul>

        <h3>בחזרה לסימולציה:</h3>
        <p>הסימולציה נותנת לכם הזדמנות לשחק עם הגורמים המשפיעים על כוח הכבידה - מסה ומרחק - ולראות במו עיניכם כיצד הנוסחה של ניוטון באה לידי ביטוי. שימו לב במיוחד כמה מהר הכוח נחלש כשהמרחק גדל, וכמה עוצמתי הוא יכול להיות כשהמסות גדולות!</p>
    </div>

</div> <!-- End learning-container -->

<style>
    /* General Page Styling */
    body {
        font-family: 'Arial', sans-serif; /* Use a common, clean font */
        line-height: 1.7; /* Improved readability */
        margin: 0;
        padding: 0; /* Remove padding from body */
        background: linear-gradient(135deg, #eef2f7 0%, #e0eafc 100%); /* Soft gradient background */
        color: #333;
        direction: rtl; /* Hebrew direction */
        text-align: right; /* Align text right */
        min-height: 100vh; /* Ensure gradient covers full viewport height */
        display: flex; /* Use flexbox for centering container */
        justify-content: center;
        align-items: flex-start; /* Align to the top */
        padding: 20px; /* Add padding to the flex container */
        box-sizing: border-box; /* Include padding in element's total width and height */
    }

    .learning-container {
        background-color: #ffffff; /* White content background */
        padding: 30px; /* More generous padding */
        border-radius: 12px; /* Rounded corners */
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1); /* Softer, larger shadow */
        max-width: 800px; /* Max width for readability */
        width: 100%; /* Ensure it takes full width on smaller screens */
        box-sizing: border-box;
    }

    h1, h2, h3 {
        color: #1a2a3a; /* Darker, more elegant headings */
        text-align: center;
        margin-bottom: 20px; /* Increased spacing */
        line-height: 1.4;
    }

    h1 {
        color: #4a0e9c; /* Primary color for main title */
        margin-bottom: 30px;
        font-size: 2em; /* Larger main title */
    }

    .intro-text {
        font-size: 1.1em;
        color: #555;
        margin-bottom: 30px;
        text-align: center;
    }

    p, ul {
        margin-bottom: 20px; /* Increased spacing */
        font-size: 1em;
    }

    ul {
        padding-right: 25px; /* Slightly more padding for list items */
    }

    li {
        margin-bottom: 8px; /* Space between list items */
    }

    .formula {
        font-size: 1.4em; /* Slightly larger formula */
        text-align: center;
        margin: 30px 0; /* More space around formula */
        background-color: #f8f9fa; /* Light background for formula */
        padding: 15px;
        border-radius: 8px;
        overflow-x: auto; /* Add scroll for long formulas on small screens */
    }

    /* Interactive App Styling */
    .interactive-app {
        border: 1px solid #dcdcE0; /* Subtle border */
        padding: 25px; /* More padding */
        margin-bottom: 30px; /* More space below */
        background-color: #ffffff; /* White background for the app section */
        border-radius: 10px;
        box-shadow: inset 0 1px 5px rgba(0, 0, 0, 0.05); /* Subtle inner shadow */
    }

    .interactive-app h2 {
        color: #0056b3; /* A distinct color for app title */
        margin-top: 0;
        margin-bottom: 15px;
    }

    .interactive-app p {
        text-align: center;
        margin-bottom: 20px;
        color: #555;
    }

    .controls {
        margin-bottom: 30px; /* More space below controls */
        display: flex; /* Use flexbox for controls */
        flex-direction: column; /* Stack controls vertically */
        align-items: stretch; /* Make items fill width */
    }

    .control-group {
        margin: 10px 0;
        padding: 10px 15px; /* Add padding to control groups */
        background-color: #f0f4f8; /* Light background for each control group */
        border-radius: 8px;
        display: flex; /* Flex for label, input, span */
        justify-content: space-between; /* Space out elements */
        align-items: center;
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .control-group label {
        font-weight: bold;
        color: #444;
        margin-bottom: 5px; /* Space below label if wrapping */
        flex-basis: 100%; /* Label takes full width on wrap */
        text-align: right; /* Align label right */
    }

    .control-group input[type="range"] {
        flex-grow: 1; /* Slider takes available space */
        margin: 0 10px; /* Space around slider */
        cursor: pointer;
        -webkit-appearance: none; /* Remove default appearance */
        appearance: none;
        background: #d3d3d3;
        outline: none;
        height: 8px; /* Make slider track thicker */
        border-radius: 5px;
        transition: background 0.2s ease-in-out;
    }

    .control-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px; /* Thumb size */
        height: 20px; /* Thumb size */
        border-radius: 50%;
        background: #007bff; /* Blue thumb */
        cursor: pointer;
        transition: background 0.2s ease-in-out, transform 0.1s ease-in-out;
    }

    .control-group input[type="range"]::-webkit-slider-thumb:hover {
         background: #0056b3; /* Darker blue on hover */
         transform: scale(1.1); /* Slightly larger thumb on hover */
    }


    .control-group input[type="range"]::-moz-range-thumb {
         width: 20px; /* Thumb size */
        height: 20px; /* Thumb size */
        border-radius: 50%;
        background: #007bff; /* Blue thumb */
        cursor: pointer;
        transition: background 0.2s ease-in-out, transform 0.1s ease-in-out;
    }
     .control-group input[type="range"]::-moz-range-thumb:hover {
         background: #0056b3; /* Darker blue on hover */
         transform: scale(1.1); /* Slightly larger thumb on hover */
    }

    .value-display {
        min-width: 100px; /* Reserve space for value */
        text-align: left; /* Align value left */
        font-weight: bold;
        color: #007bff; /* Match thumb color */
        font-family: 'Courier New', monospace; /* Monospaced for numbers */
    }


    #simulation-area {
        position: relative;
        width: 100%;
        height: 250px; /* Slightly taller simulation area */
        margin-bottom: 20px;
        background: linear-gradient(135deg, #2a0845 0%, #6441A5 100%); /* Space gradient */
        border-radius: 8px;
        overflow: hidden; /* Ensure objects/arrows stay inside */
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.2);
    }

    .object {
        position: absolute;
        width: 50px; /* Base size */
        height: 50px; /* Base size */
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-weight: bold;
        font-size: 1.2em;
        z-index: 1; /* Ensure objects are above arrows */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3); /* Object shadow */
        transition: left 0.4s ease-out, top 0.4s ease-out, width 0.4s ease-out, height 0.4s ease-out, transform 0.1s ease-out; /* Smooth transitions for movement and size */
         user-select: none; /* Prevent selecting text inside objects */
    }

     #object1 {
         background-color: #00cec9; /* Teal */
     }

     #object2 {
         background-color: #ff6348; /* Coral */
     }

    /* Pulse animation for objects when force updates */
    .object.pulling {
        animation: pulse-pull 0.4s ease-out;
    }

    @keyframes pulse-pull {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); } /* Slightly larger */
        100% { transform: scale(1); }
    }


     .force-arrow {
        position: absolute;
        height: 4px; /* Thicker arrow line */
        background-color: #ffeaa7; /* Bright Yellow */
        z-index: 0; /* Arrows below objects */
        transform-origin: right center; /* Rotate/scale from the point */
        transition: width 0.4s ease-out, left 0.4s ease-out, opacity 0.4s ease-out; /* Smooth transitions */
         filter: drop-shadow(0 0 5px rgba(255, 234, 167, 0.5)); /* Subtle glow */
     }

     /* Arrow head using pseudo-element */
     .force-arrow::after {
        content: '';
        position: absolute;
        width: 0;
        height: 0;
        border-top: 8px solid transparent; /* Larger arrowhead */
        border-bottom: 8px solid transparent; /* Larger arrowhead */
        border-left: 15px solid #ffeaa7; /* Arrowhead color matching line */
        right: -1px; /* Position slightly overlapping the line end */
        top: 50%;
        transform: translateY(-50%);
        filter: drop-shadow(0 0 5px rgba(255, 234, 167, 0.5)); /* Subtle glow for head */
     }

     /* Specific styling for the left-pointing arrow */
     #force-arrow2 {
          transform-origin: left center; /* Rotate/scale from the point */
          /* Arrow head for #force-arrow2 will point left */
     }

     #force-arrow2::after {
         border-left: none; /* Remove default right-pointing head */
         border-right: 15px solid #ffeaa7; /* Add left-pointing head */
         left: -1px; /* Position slightly overlapping the line start */
         right: auto; /* Remove right positioning */
     }

     /* Animation for pulsing arrows when force is active */
     .force-arrow.active {
        animation: pulse-glow 1.5s infinite ease-in-out;
     }

     @keyframes pulse-glow {
         0%, 100% { opacity: 1; filter: drop-shadow(0 0 5px rgba(255, 234, 167, 0.5)); }
         50% { opacity: 0.8; filter: drop-shadow(0 0 15px rgba(255, 234, 167, 1)); } /* Brighter glow in the middle */
     }


    #force-display {
        font-size: 1.4em; /* Larger font for force display */
        font-weight: bold;
        color: #fd7e14; /* Vibrant Orange */
        text-align: center;
        min-height: 1.5em; /* Prevent layout shift when value updates */
    }

    #force-value-span {
         transition: color 0.3s ease-in-out; /* Smooth color transition */
    }


    .toggle-button {
        display: block;
        margin: 25px auto; /* Centered button with more vertical space */
        padding: 12px 25px; /* Larger button */
        font-size: 1.1em;
        cursor: pointer;
        background-color: #007bff; /* Blue button */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.2s ease;
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
    }

    .toggle-button:hover {
        background-color: #0056b3; /* Darker blue on hover */
        box-shadow: 0 6px 12px rgba(0, 123, 255, 0.4);
    }

     .toggle-button:active {
         transform: scale(0.98); /* Slight press effect */
         box-shadow: 0 2px 4px rgba(0, 123, 255, 0.4);
     }

    #explanation-content {
        border-top: 1px solid #eee; /* Separator line */
        padding-top: 20px;
        margin-top: 20px;
        background-color: #fefefe; /* Slightly off-white */
        border-radius: 0 0 12px 12px; /* Round bottom corners if container is rounded */
    }

    /* KaTeX specific CSS - already included, ensuring it looks good with new styles */
    .katex-display {
        text-align: center;
        margin: 1.5em 0; /* More space around equations */
    }

    /* Responsive adjustments */
    @media (max-width: 600px) {
        .learning-container {
            padding: 20px;
        }

        h1 {
            font-size: 1.8em;
        }

        .interactive-app {
            padding: 15px;
        }

        .control-group {
             flex-direction: column; /* Stack elements in control group */
             align-items: flex-start;
        }
        .control-group label {
            margin-bottom: 5px;
        }
        .control-group input[type="range"] {
             margin: 5px 0;
             width: 100%; /* Make slider fill width */
        }
        .value-display {
            min-width: auto;
            text-align: right;
            width: 100%;
        }

        #simulation-area {
             height: 200px; /* Reduce height on small screens */
        }

        .object {
            width: 40px;
            height: 40px;
            font-size: 1em;
        }

        .force-arrow::after {
             border-top-width: 6px;
             border-bottom-width: 6px;
             border-left-width: 10px;
             border-right-width: 10px; /* Adjust arrowhead size */
        }

         .toggle-button {
             font-size: 1em;
             padding: 10px 20px;
         }
    }

</style>

<!-- KaTeX CSS and JS - Keep these as they are required for math rendering -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-zBpiWbeNL6QBTGK6PQA6S1QEyWwTCS/Pfege9RjJxlSmeQo0ZJeopzVWbLTJ/LLJ" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js" integrity="sha384-jUm0W/17f3fFv7vM5Lz+6Ff9qB5O6bFpC2O3V2O7JjN7K2t6fX+QvJ+L7XjLzJt3" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+QDvP/g+ZpQ5zR+Z7qP+o+b+t3hGz2kR2+a2B2M+3+g3+J+z3+Q3+t3+B3+R3+Q3+g3+J+z3+Q3+t3+B3+R3+Q3" crossorigin="anonymous"></script>


<script>
document.addEventListener('DOMContentLoaded', () => {
    // Get elements
    const mass1Input = document.getElementById('mass1-input');
    const mass2Input = document.getElementById('mass2-input');
    const distanceInput = document.getElementById('distance-input');
    const mass1ValueSpan = document.getElementById('mass1-value');
    const mass2ValueSpan = document.getElementById('mass2-value');
    const distanceValueSpan = document.getElementById('distance-value');
    const object1Div = document.getElementById('object1');
    const object2Div = document.getElementById('object2');
    const forceArrow1Div = document.getElementById('force-arrow1');
    const forceArrow2Div = document.getElementById('force-arrow2');
    const forceValueSpan = document.getElementById('force-value-span'); // Span inside force-display
    const simulationArea = document.getElementById('simulation-area');
    const toggleButton = document.getElementById('toggle-explanation-button');
    const explanationContent = document.getElementById('explanation-content');

    // Gravitational constant (for calculation)
    const G = 6.674e-11; // N(m/kg)^2

    // Scaling factor for visual representation of force arrows length
    // Adjust this value to make arrows visible and scale appropriately
    // F = G * m1 * m2 / r^2. With m around 10^12 and r around 10^3, F is around 10^-11 * 10^24 / 10^6 = 10^7.
    // Arrow length needs to be pixels. Let's scale 10^7 N to maybe 100px. Scale factor ~ 100 / 10^7 = 10^-5
    const forceLengthScale = 5e-6; // Adjusted scale factor based on expected force range

    // Min/Max size for objects in pixels based on mass (visually scaled)
    const minObjectSizePx = 40;
    const maxObjectSizePx = 80; // Allow objects to appear larger
    // Mass range is 10^11 to 10^12. Log scale mapping for size seems more intuitive.
    const minMassLog = Math.log(parseFloat(mass1Input.min));
    const maxMassLog = Math.log(parseFloat(mass1Input.max));

    // Function to map mass to a visual size (pixels)
    function mapMassToSize(mass) {
        const massLog = Math.log(mass);
        // Linear mapping in log scale
        const size = minObjectSizePx + (maxObjectSizePx - minObjectSizePx) * ((massLog - minMassLog) / (maxMassLog - minMassLog));
        return Math.max(minObjectSizePx, Math.min(maxObjectSizePx, size)); // Clamp size
    }

    // Function to update the simulation based on input values
    function updateSimulation() {
        const m1 = parseFloat(mass1Input.value);
        const m2 = parseFloat(mass2Input.value);
        const r = parseFloat(distanceInput.value); // This 'r' is the *meter* distance from input

        // Update displayed values with better formatting (e.g., scientific notation for large masses)
        mass1ValueSpan.textContent = formatMass(m1);
        mass2ValueSpan.textContent = formatMass(m2);
        distanceValueSpan.textContent = `${r} מטר`;

        // Calculate force using Newton's Law
        // Handle potential division by zero if distance is 0 (though range min is >= 200)
        const F = (r > 0) ? (G * m1 * m2) / (r * r) : 0;

        // Update force display - Use toPrecision for controlled decimal places
        forceValueSpan.textContent = F.toPrecision(5); // Display 5 significant digits

        // --- Update Visuals ---
        const simWidth = simulationArea.clientWidth;
        const simHeight = simulationArea.clientHeight;

        // Calculate object sizes based on their masses
        const size1 = mapMassToSize(m1);
        const size2 = mapMassToSize(m2);

        // Map the input *meter* distance (r) to a visual *pixel* separation in the simulation area
        const minInputDistance = parseFloat(distanceInput.min);
        const maxInputDistance = parseFloat(distanceInput.max);
        // Calculate min/max visual separation considering potential max object sizes
        const maxPossibleSize = maxObjectSizePx;
        const minVisualSeparationPx = maxPossibleSize + 30; // Minimum gap between largest objects (px)
        const maxVisualSeparationPx = simWidth - 2 * maxPossibleSize - 30; // Maximum gap (px), leaves margin

        // Ensure range mapping handles potential edge cases and reversed ranges
         let visualSeparation = 0;
         if (maxInputDistance > minInputDistance) {
             // Linear mapping of meter distance to pixel separation
             visualSeparation = minVisualSeparationPx + (maxVisualSeparationPx - minVisualSeparationPx) * ((r - minInputDistance) / (maxInputDistance - minInputDistance));
             visualSeparation = Math.max(minVisualSeparationPx, Math.min(maxVisualSeparationPx, visualSeparation)); // Clamp
         } else { // Should not happen with range inputs, but good practice
             visualSeparation = (minVisualSeparationPx + maxVisualSeparationPx) / 2; // Default to middle
         }


        // Position objects based on the calculated visual separation and sizes
        // Total width occupied: size1 + visualSeparation + size2
        const totalVisualWidth = size1 + visualSeparation + size2;
        // Calculate the starting position for the leftmost object (object 1)
        const obj1Left = (simWidth - totalVisualWidth) / 2;
        const obj2Left = obj1Left + size1 + visualSeparation;

        // Apply object sizes and positions (CSS transitions will handle the animation)
        object1Div.style.width = `${size1}px`;
        object1Div.style.height = `${size1}px`;
        object1Div.style.left = `${obj1Left}px`;
        object1Div.style.top = `${simHeight / 2 - size1 / 2}px`; // Center vertically

        object2Div.style.width = `${size2}px`;
        object2Div.style.height = `${size2}px`;
        object2Div.style.left = `${obj2Left}px`;
        object2Div.style.top = `${simHeight / 2 - size2 / 2}px`; // Center vertically

        // Position and size force arrows
        // Arrows should point from the edge of one object to the edge of the other
        const obj1RightEdge = obj1Left + size1;
        const obj2LeftEdge = obj2Left;
        const spaceBetweenObjectsEdges = obj2LeftEdge - obj1RightEdge; // Space in pixels between the visual objects edges

        // Scale the force F to an arrow length in pixels. Limit the length.
        // Arrow length should ideally scale non-linearly or logarithmically for large force ranges,
        // but a simple linear scale clamped by the available space is a good start.
        const maxArrowLength = Math.max(0, spaceBetweenObjectsEdges / 2 - 5); // Max length is half the gap, with buffer
        const minArrowLength = 5; // Minimum length to display

        // Scale F to a raw pixel length
        let rawArrowLength = F * forceLengthScale;

        // Clamp the arrow length to be within reasonable visual bounds (e.g., 5px to maxArrowLength)
        const arrowLengthPx = Math.max(0, Math.min(maxArrowLength, rawArrowLength)); // Use max(0, ...) to handle negative results if scale is bad

        // Arrow 1: points from object1 towards object2
        // Starts at the right edge of object 1, points right
        forceArrow1Div.style.width = `${arrowLengthPx}px`;
        forceArrow1Div.style.left = `${obj1RightEdge}px`;
        forceArrow1Div.style.top = `${simHeight / 2}px`; // Center vertically
        forceArrow1Div.style.transform = `translateY(-50%)`; // No rotation needed (0 degrees)

        // Arrow 2: points from object2 towards object1
        // Starts at the left edge of object 2, points left
        forceArrow2Div.style.width = `${arrowLengthPx}px`;
        forceArrow2Div.style.left = `${obj2LeftEdge - arrowLengthPx}px`; // Position the left end of the arrow
        forceArrow2Div.style.top = `${simHeight / 2}px`; // Center vertically
        forceArrow2Div.style.transform = `translateY(-50%)`; // No rotation needed (180 degrees implied by positioning and head)

        // Show/Hide arrows based on length
        if (arrowLengthPx < minArrowLength) {
             forceArrow1Div.style.opacity = '0';
             forceArrow2Div.style.opacity = '0';
             // Remove active class to stop animation
             forceArrow1Div.classList.remove('active');
             forceArrow2Div.classList.remove('active');
        } else {
             forceArrow1Div.style.opacity = '1';
             forceArrow2Div.style.opacity = '1';
             // Add active class to start animation
             forceArrow1Div.classList.add('active');
             forceArrow2Div.classList.add('active');
        }

        // Trigger subtle "pull" animation on objects
        object1Div.classList.add('pulling');
        object2Div.classList.add('pulling');
        // Remove the class after the animation duration (0.4s)
        setTimeout(() => {
            object1Div.classList.remove('pulling');
            object2Div.classList.remove('pulling');
        }, 400); // Match CSS animation duration
    }

     // Helper function to format large mass numbers
     function formatMass(mass) {
         if (mass >= 1e12) return (mass / 1e12).toFixed(1) + 'e12';
         if (mass >= 1e9) return (mass / 1e9).toFixed(1) + 'e9';
         return mass.toString(); // Fallback
         // Using toExponential directly might be simpler for consistency with calculation scale
         return mass.toExponential(2);
     }


    // Add event listeners to inputs
    mass1Input.addEventListener('input', updateSimulation);
    mass2Input.addEventListener('input', updateSimulation);
    distanceInput.addEventListener('input', updateSimulation);

    // Initial update to set everything up when the page loads
    updateSimulation();


    // Toggle explanation visibility
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationContent.style.display === 'none';
        explanationContent.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'על כוח הכבידה - הסתרה' : 'על כוח הכבידה - ההסבר המלא!'; // Change button text

        // Render KaTeX only when showing the content for the first time or if needed
        // A simple check if it was just made visible is sufficient here.
        if (isHidden) {
            renderMathInElement(explanationContent, {
                delimiters: [
                    {left: '$$', right: '$$', display: true},
                    {left: '$', right: '$', display: false},
                ],
                throwOnError: false
            });
        }
    });

    // Initial state of the toggle button text
     toggleButton.textContent = explanationContent.style.display === 'none' ? 'על כוח הכבידה - ההסבר המלא!' : 'על כוח הכבידה - הסתרה';

});
</script>
```