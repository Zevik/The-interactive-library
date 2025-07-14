---
title: "למה גשרים רוקדים? סוד התהודה המכנית נחשף!"
english_slug: why-bridges-dance-the-secret-of-mechanical-resonance
category: "מדעים מדויקים / פיזיקה"
tags:
  - פיזיקה
  - תהודה
  - מכניקה
  - גלים
  - מבנים הנדסיים
---

<div class="intro-section">
    <h1>למה גשרים רוקדים? סוד התהודה המכנית נחשף!</h1>
    <p class="lead-paragraph">איך רוח קלה לכאורה יכולה לגרום לגשר ענק להתפתל בפראות עד לקריסתו המרהיבה? ולמה חיילים ממושמעים נדרשים לשבור את הצעד האחיד כשהם עוברים על גשר? התשובה טמונה בסוד פיזיקלי עוצמתי ומרתק: תהודה מכנית. זהו כוח שיכול להפוך דחיפה קטנה להרס עצום, או לחילופין, לשמש אותנו בטכנולוגיה יום-יומית.</p>
</div>

<div id="app">
    <div class="simulation-area">
        <h2>התנסו בעצמכם: סימולציית תהודה</h2>
        <p class="sim-instruction">כוונו את תדר הכוח החיצוני (כמו רוח או צעדים) באמצעות המחוון וצפו בתגובת המבנה. נסו למצוא את התדר שמגדיל את התנודות בצורה דרמטית!</p>
        <div class="structure-container">
             <!-- Adding pillars for better visual -->
            <div class="pillar left"></div>
            <div id="structure" class="structure"></div>
            <div class="pillar right"></div>
        </div>
        <div class="controls">
            <label for="frequency-slider">תדר הכוח החיצוני (הרץ): <span id="current-frequency">0.00</span></label>
            <input type="range" id="frequency-slider" min="0.1" max="5.0" value="0.5" step="0.02"> <!-- Finer control step -->
            <p>תדר תנודה טבעי של המבנה: <span id="natural-frequency-display"></span> הרץ</p>
            <p>אמפליטודת התנודה (עוצמת ה"ריקוד"): <span id="amplitude-display">0.00</span></p>
            <div id="status-message" class="status">המבנה יציב</div>
        </div>
    </div>
</div>

<button id="toggle-explanation">הסבר לי את סוד התהודה!</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מעמיק על תהודה מכנית</h2>
    <p><strong>מהי תהודה מכנית באמת?</strong></p>
    <p>תארו לעצמכם נדנדה. אם תדחפו אותה בדיוק ברגע הנכון (כשהיא מגיעה לשיא הגובה שלה ומתחילה לרדת), גם דחיפה קטנה תגרום לה לעלות גבוה יותר. אם תמשיכו לדחוף בקצב הזה, הנדנדה תגיע לגבהים מרשימים. זוהי תהודה! תהודה מכנית היא תופעה בה גוף או מערכת (כמו גשר, בניין, או אפילו כוס זכוכית) נחשפים לכוח חיצוני מחזורי הפועל בתדר שקרוב מאוד או זהה לתדר התנודה ה"טבעי" של הגוף. במצב זה, כל פעימה של הכוח החיצוני מוסיפה אנרגיה למערכת, והאנרגיה הזו מצטברת, וגורמת לתנודות לגדול באופן דרמטי.</p>

    <p><strong>מהו "תדר תנודה טבעי"?</strong></p>
    <p>לכל גוף או מערכת בעלי מסה וגמישות יש "קצב ריקוד" מועדף משלהם – תדר תנודה טבעי אחד או יותר. זהו התדר שבו הגוף יתנודד מעצמו אם נסיט אותו ממצב שיווי המשקל שלו ונשחרר (חשבו על מיתר גיטרה שפרטתם או פעמון שצלצלתם בו). התדר הטבעי נקבע אך ורק על ידי המאפיינים הפיזיים של הגוף: המסה שלו, החומר ממנו הוא עשוי (שקובע את גמישותו), והמבנה הגיאומטרי שלו.</p>

    <p><strong>למה תהודה כל כך עוצמתית?</strong></p>
    <p>כאשר התדר של הכוח החיצוני ("תדר הכפייה") תואם את התדר הטבעי, הכוח החיצוני למעשה "מסייע" לתנועה הטבעית של הגוף. בכל מחזור, הכוח דוחף בדיוק באותו כיוון שהגוף כבר נע בו. התוספת הקטנה הזו של אנרגיה בכל מחזור אינה מתבזבזת אלא נצברת, וכתוצאה מכך האמפליטודה (עוצמת התנודה, ה"גובה" של הנדנדה) גדלה וגדלה משמעותית. זה כאילו כל דחיפה על הנדנדה מגיעה בתיאום מושלם.</p>

    <p><strong>מה עוצר את התנודה מלגדול לאין סוף? הדעיכה.</strong></p>
    <p>במציאות, שום דבר לא מתנודד לנצח. קיימים כוחות "מדכאים" שנוגדים את התנועה ובולעים אנרגיה – כמו חיכוך פנימי בחומר, התנגדות האוויר, או חיכוך במקומות התמיכה. כוחות אלה נקראים "דעיכה". הדעיכה מונעת מהתנודות לגדול ללא גבול. כאשר יש דעיכה, האמפליטודה המקסימלית בתהודה עדיין מוגבלת, אך היא יכולה להיות פי כמה וכמה גדולה יותר מהאמפליטודה הנגרמת על ידי אותו כוח בתדרים אחרים, הרחק מהתהודה. ככל שהדעיכה במערכת קטנה יותר, כך התהודה חזקה יותר והאמפליטודה המקסימלית שתתקבל בתדר התהודה תהיה גדולה יותר.</p>

    <p><strong>סיפורי אימה וסיפורי הצלחה של תהודה:</strong></p>
    <ul>
        <li><strong>גשר טקומה נארוז ("גאלוֹפּינג גֶרטי"):</strong> הדוגמה המפורסמת והדרמטית ביותר. בשנת 1940, רוח במהירות נמוכה יחסית יצרה מערבולות אוויר שתדרן התאים לאחד מתדרי התנודה הפיתולית (סיבובית) של הגשר. הגשר החל להתפתל ולהתעוות בצורה קיצונית (ומכאן כינויו "גרטי הדוהרת") עד לקריסתו המוחלטת, כפי שניתן לראות בסרטונים היסטוריים. אירוע זה לימד את המהנדסים שיעור חשוב על הצורך להתחשב בתדרי תהודה שונים ולא רק בתנודות אנכיות או אופקיות פשוטות.</li>
        <li><strong>מצעד חיילים על גשר:</strong> סיבה קלאסית לבקש מחיילים "לשבור מסדר" (להפסיק לצעוד בצעד אחיד ומסונכרן) כשהם עוברים על גשר. צעדים מסונכרנים יוצרים כוח מחזורי בתדר קבוע. אם תדר הצעדים הזה יתאים במקרה לתדר טבעי של הגשר, הוא עלול לגרום לו להתנודד בעוצמה מסוכנת.</li>
        <li><strong>שירת סופרן ששוברת כוס זכוכית:</strong> אם זמר אופרה מיומן ישיר תו גבוה בתדר זהה לתדר התנודה הטבעי של כוס זכוכית, גלי הקול (כוח חיצוני מחזורי) יגרמו למולקולות הזכוכית לרטוט באמפליטודה גדולה יותר ויותר עד שהחומר יישבר.</li>
    </ul>
     <p>אבל לא הכל הרס! תהודה היא מנוע מרכזי בטכנולוגיות רבות:</p>
    <ul>
        <li>**כלי נגינה:** תיבת התהודה בגיטרה או בכינור, עמוד האוויר בחליל או חצוצרה - כולם נועדו להגביר צלילים (לגרום למולקולות האוויר לרטוט באמפליטודה גדולה יותר) בתדרים ספציפיים.</li>
        <li>**רדיו וטלוויזיה:** הכוונון לתחנה מסוימת מתבסס על מעגלים חשמליים בתהודה המאפשרים למקלט "לשמוע" רק את אות השידור בתדר הנבחר ולהתעלם מהיתר.</li>
         <li>**דימות תהודה מגנטית (MRI):** מכשיר ה-MRI משתמש בגלי רדיו (כוח חיצוני) בתדרים מדויקים התואמים את תדרי התהודה של אטומי מימן בגוף האדם, כדי לקבל מידע על הרקמות השונות.</li>
    </ul>


    <p><strong>הגנה מפני תהודה: תפקיד המהנדסים.</strong></p>
    <p>מהנדסי מבנים וקונסטרוקציה חייבים להיות מודעים היטב לסכנות התהודה. בתכנון גשרים, בניינים גבוהים, או מטוסים, הם מחשבים בקפדנות את התדרים הטבעיים של המבנה ומוודאים שתדרים אלה יהיו רחוקים ככל הניתן מתדרי הכוחות החיצוניים הצפויים (רוח, רעידות אדמה, תנועת רכבות או כלי רכב כבדים). בנוסף, הם מוסיפים למבנים אלמנטים שמגבירים את הדעיכה המכנית, כמו בולמי זעזועים מסיביים (Dampers), שמטרתם לפזר ולבלוע את האנרגיה של התנודות וכך להקטין את האמפליטודה גם אם מתרחשת תהודה חלקית.</p>
</div>

<style>
    /* כללי */
    body {
        font-family: 'Heebo', sans-serif; /* שימוש בפונט מודרני יותר */
        line-height: 1.7; /* הגדלת מרווח שורות לקריאות משופרת */
        margin: 0;
        padding: 30px 15px; /* הגדלת ריפוד כללי */
        background: linear-gradient(to bottom right, #e0f2f7, #b3e5fc); /* רקע גרדיאנט עדין */
        color: #333;
        direction: rtl;
        text-align: right;
    }

    .intro-section {
        max-width: 800px;
        margin: 0 auto 30px;
        text-align: center; /* מרכז את הכותרת והפסקה */
    }

    h1 {
        color: #01579b; /* כחול עמוק יותר */
        font-size: 2.5rem; /* גודל כותרת גדול יותר */
        margin-bottom: 10px;
        font-weight: 700; /* פונט יותר בולט */
    }

    h2 {
        color: #0277bd; /* כחול בינוני */
        font-size: 1.8rem;
        margin-bottom: 15px;
        text-align: center; /* כותרות הסברים ממורכזות */
    }

    .lead-paragraph {
        font-size: 1.15rem;
        color: #555;
        margin-bottom: 25px;
         text-align: center;
    }

    #app {
        margin: 30px auto;
        padding: 25px; /* הגדלת ריפוד פנימי */
        border: 1px solid #b3e5fc; /* גבול עדין */
        border-radius: 12px; /* פינות עגולות יותר */
        max-width: 750px; /* הגדלת רוחב מקסימלי */
        background-color: #ffffff; /* רקע לבן נקי */
        box-shadow: 0 8px 16px rgba(0,0,0,0.1); /* צל בולט יותר */
    }

    .simulation-area {
        margin-bottom: 30px;
        padding: 20px;
        border: 2px dashed #e1f5fe; /* גבול מקווקו בהיר */
        border-radius: 8px;
        background-color: #f1f8e9; /* רקע בהיר שונה לסימולציה */
        text-align: center; /* מרכז את תוכן הסימולציה */
    }

     .sim-instruction {
         font-size: 1rem;
         color: #666;
         margin-bottom: 20px;
     }

    .structure-container {
        width: 100%;
        height: 120px; /* הגדלת גובה קונטיינר */
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 30px; /* מרווח תחתון גדול יותר */
        position: relative;
        overflow: hidden;
        padding: 0 40px; /* ריפוד גדול יותר לצדדים */
        box-sizing: border-box;
    }

     .pillar {
        position: absolute;
        bottom: 0; /* עוגן לתחתית הקונטיינר */
        width: 30px; /* רוחב עמוד */
        height: 100px; /* גובה עמוד */
        background-color: #78909c; /* צבע אפור כהה לעמודים */
        border-radius: 5px 5px 0 0; /* פינות עגולות למעלה */
        box-shadow: 0 -3px 5px rgba(0,0,0,0.2);
     }

    .pillar.left {
        left: 40px; /* מיקום מצד שמאל (תואם לריפוד) */
    }

    .pillar.right {
        right: 40px; /* מיקום מצד ימין */
    }


    .structure {
        width: 280px; /* רוחב מבנה גדול יותר */
        height: 25px; /* עובי מבנה גדול יותר */
        background-color: #42a5f5; /* כחול בהיר יותר */
        position: absolute;
        top: 50%;
        left: 50%;
        /* transform: translate(-50%, -50%); לא להשתמש בזה כאן כדי שנוכל לשלב טרנספורמציות נוספות ב JS */
        transform: translate(-50%, -50%); /* שמירה על מיקום מרכזי בברירת מחדל */
        transform-origin: center center;
        transition: transform 0.05s linear; /* שמירה על אנימציה חלקה */
        border-radius: 5px;
        box-shadow: 0 0 8px rgba(0,0,100,0.4); /* צל בולט יותר */
         z-index: 1; /* ודא שהמבנה מעל העמודים */
    }

     .structure.collapsed {
        background-color: #e53935; /* אדום לקריסה */
        /* אנימציית קריסה משופרת */
        animation: collapse-shake 0.4s ease-in-out infinite alternate, fade-flash 0.8s ease-in-out infinite alternate;
         box-shadow: 0 0 15px #e53935;
         border: 3px dashed #333;
         transform-origin: center bottom; /* נקודת ציר לקריסה */
    }

     @keyframes collapse-shake {
        0% { transform: translate(-50%, -50%) translateX(0px) rotate(0deg); }
        100% { transform: translate(-50%, -50%) translateX(15px) rotate(6deg); } /* טלטלה וסיבוב חזקים יותר */
    }

    @keyframes fade-flash {
        0% { opacity: 1; }
        50% { opacity: 0.7; }
        100% { opacity: 1; }
    }


    .controls {
        text-align: center;
        background-color: #e8f5e9; /* רקע בהיר יותר לקונטרולס */
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #c8e6c9;
    }

    .controls label {
        display: block;
        margin-bottom: 12px;
        font-weight: bold;
        color: #388e3c; /* ירוק כהה יותר */
        font-size: 1.1rem;
    }

    .controls input[type="range"] {
        width: 95%;
        margin-bottom: 15px;
        cursor: pointer;
        -webkit-appearance: none; /* הסתרת עיצוב דיפולטיבי */
        appearance: none;
        height: 8px; /* עובי סליידר */
        background: #a5d6a7; /* רקע סליידר ירוק בהיר */
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 4px;
    }

    .controls input[type="range"]:hover {
        opacity: 1;
    }

     /* Thumb of the slider */
    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px; /* גודל גולל */
        height: 20px;
        background: #4caf50; /* ירוק לסליידר */
        cursor: pointer;
        border-radius: 50%; /* גולל עגול */
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    .controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #4caf50;
        cursor: pointer;
        border-radius: 50%;
         box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }


    .controls p {
        margin-bottom: 8px;
        color: #555;
        font-size: 1rem;
    }

    #status-message {
        margin-top: 20px;
        padding: 10px;
        font-weight: bold;
        min-height: 1.5em; /* Reserve space for messages */
        border-radius: 5px;
        text-align: center;
        transition: all 0.3s ease; /* מעבר חלק לשינויי סטטוס */
    }

     #status-message.status {
        color: #333; /* צבע ברירת מחדל */
        background-color: transparent;
     }

     #status-message.warning {
        color: #fbc02d; /* צהוב */
        background-color: #fff9c4; /* רקע צהוב בהיר */
        border: 1px solid #fbc02d;
     }

    #status-message.danger {
        color: #d32f2f; /* אדום */
        background-color: #ffcdd2; /* רקע אדום בהיר */
        border: 1px solid #d32f2f;
        animation: pulse-danger 1.5s infinite; /* אנימציית פעימה */
    }

    @keyframes pulse-danger {
        0% { box-shadow: 0 0 0 0 rgba(211, 47, 47, 0.4); }
        70% { box-shadow: 0 0 0 15px rgba(211, 47, 47, 0); }
        100% { box-shadow: 0 0 0 0 rgba(211, 47, 47, 0); }
    }


    #toggle-explanation {
        display: block;
        margin: 30px auto;
        padding: 12px 25px; /* הגדלת כפתור */
        font-size: 1.1rem;
        cursor: pointer;
        border: none;
        border-radius: 25px; /* פינות עגולות לכפתור */
        background-color: #007bff;
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease; /* הוספת טרנספורם למעבר */
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    #toggle-explanation:hover {
        background-color: #0056b3;
        transform: translateY(-2px); /* אפקט ריחוף עדין */
    }
    #toggle-explanation:active {
        transform: translateY(0); /* אפקט לחיצה */
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }


    #explanation {
        margin-top: 30px;
        padding: 20px;
        border: 1px solid #b3e5fc;
        border-radius: 12px;
        background-color: #e1f5fe; /* רקע תכלת בהיר */
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    #explanation h2 {
        margin-top: 0;
        color: #0288d1; /* כחול טורקיז */
        text-align: right;
        border-bottom: 2px solid #b3e5fc; /* קו תחתון לכותרת */
        padding-bottom: 10px;
        margin-bottom: 15px;
    }

    #explanation p {
        margin-bottom: 15px; /* מרווח גדול יותר בין פסקאות */
        text-align: right;
         color: #444;
    }

     #explanation strong {
         color: #01579b; /* כחול עמוק לדגשים */
     }

    #explanation ul {
        margin-top: 15px;
        padding-right: 25px; /* הזחה גדולה יותר לרשימה */
         text-align: right;
         list-style-type: disc;
         color: #444;
    }

    #explanation li {
        margin-bottom: 10px; /* מרווח גדול יותר בין פריטים ברשימה */
         text-align: right;
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const structure = document.getElementById('structure');
        const frequencySlider = document.getElementById('frequency-slider');
        const currentFrequencyDisplay = document.getElementById('current-frequency');
        const naturalFrequencyDisplay = document.getElementById('natural-frequency-display');
        const amplitudeDisplay = document.getElementById('amplitude-display');
        const statusMessage = document.getElementById('status-message');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        // --- Simulation Parameters ---
        const naturalFrequency = 2.0; // Hz (Example: 2 Hz) - תדר התנודה הטבעי של המבנה
        const dampingRatio = 0.04; // Zeta (Example: 4% damping) - כמה מהר התנודות דועכות. ערך נמוך יותר יגרום לתהודה חדה יותר.
        const visualCollapseThreshold = 60; // Pixels of visual displacement to trigger collapse class
        const visualWarningThreshold = 30; // Pixels of visual displacement to trigger warning class
        const baseAmplitudeScale = 80; // Visual scale factor. Higher value means static force causes more displacement, making resonance effects more pronounced visually.

        naturalFrequencyDisplay.textContent = naturalFrequency.toFixed(2);

        let animationFrameId = null;
        let startTime = null;
        let currentCalculatedAmplitude = 0; // The calculated steady-state amplitude for the *current* frequency value
        let currentVisualAmplitude = 0; // The visual amplitude we are animating towards
        let isCollapsed = false;

        // Function to calculate steady-state amplitude based on driven harmonic oscillator formula
        // A = A_static / sqrt((1 - (f_ext/f_nat)^2)^2 + (2*zeta*(f_ext/f_nat))^2)
        // Where A_static is related to baseAmplitudeScale
        function calculateAmplitude(f_external) {
            const f_ratio = f_external / naturalFrequency;
            const f_ratio_squared = Math.pow(f_ratio, 2);
            const damping_term = 2 * dampingRatio * f_ratio;

            const denominator_squared = Math.pow(1 - f_ratio_squared, 2) + Math.pow(damping_term, 2);

             // Handle edge case near zero damping and exact resonance frequency
             if (dampingRatio < 0.005 && Math.abs(f_ratio - 1.0) < 0.01) { // If very low damping and very close to resonance
                 // Approximate peak amplitude near resonance for low damping: A_res ≈ A_static / (2 * zeta)
                 return baseAmplitudeScale / (2 * Math.max(dampingRatio, 0.005)); // Use a minimal damping for calculation stability
             }


            // Prevent division by near zero if damping is extremely low but not zero, or frequency is slightly off resonance
            // A small epsilon or min damping value can help numerical stability
            const safeDenominator = Math.sqrt(Math.max(denominator_squared, 1e-6)); // Ensure denominator is not zero or negative

            return baseAmplitudeScale / safeDenominator; // Scaled amplitude
        }

        function updateSimulation(currentTime) {
            if (!startTime) startTime = currentTime;
            const elapsed = (currentTime - startTime) / 1000; // Time in seconds

            const externalFrequency = parseFloat(frequencySlider.value);

            // Interpolate the visual amplitude smoothly towards the calculated target amplitude
            // This prevents sudden jumps when the slider moves
            currentVisualAmplitude += (currentCalculatedAmplitude - currentVisualAmplitude) * 0.1; // Simple easing

            // The structure oscillates *at* the external frequency.
            // The displacement is based on the current visual amplitude and the phase of the external force cycle.
            // We use a combination of translateX (horizontal movement) and rotate (bending effect)
            const displacementX = currentVisualAmplitude * Math.sin(2 * Math.PI * externalFrequency * elapsed); // Horizontal movement
            const rotationZ = displacementX * 0.1; // Add rotation proportional to displacement (adjust multiplier for effect)

             // Apply displacement and rotation, while keeping the element centered
            structure.style.transform = `translate(-50%, -50%) translateX(${displacementX}px) rotateZ(${rotationZ}deg)`;

            // Request the next frame only if not collapsed
            if (!isCollapsed) {
                animationFrameId = requestAnimationFrame(updateSimulation);
            } else {
                 // If collapsed, just keep the last visual state (or apply collapse animation transform)
                 // The collapse animation is handled by the CSS class
                 cancelAnimationFrame(animationFrameId); // Stop requesting frames when collapsed
            }
        }

        // Start or restart the simulation loop
        function startSimulation() {
             // Reset start time to synchronize animation phase with the current moment
             startTime = null; // This will be set on the first frame of the new loop

             if (animationFrameId) {
                 cancelAnimationFrame(animationFrameId); // Cancel any existing animation frame
             }
             // Start the new animation loop
             isCollapsed = false; // Ensure simulation can restart after collapse
             structure.classList.remove('collapsed'); // Remove collapse class
             animationFrameId = requestAnimationFrame(updateSimulation);
        }

        // Event listener for the slider
        frequencySlider.addEventListener('input', () => {
            const externalFrequency = parseFloat(frequencySlider.value);
            currentFrequencyDisplay.textContent = externalFrequency.toFixed(2);

            // Recalculate the potential maximum amplitude for the *new* frequency
            currentCalculatedAmplitude = calculateAmplitude(externalFrequency);
            // Update the display immediately, even if visual amplitude lags slightly
            amplitudeDisplay.textContent = currentCalculatedAmplitude.toFixed(2);

            // Check for collapse/warning status based on the *calculated* potential amplitude
            if (currentCalculatedAmplitude > visualCollapseThreshold && !isCollapsed) {
                statusMessage.textContent = '!!! סכנה: תהודה קיצונית! המבנה קורס!!!';
                statusMessage.className = 'status danger';
                structure.classList.add('collapsed');
                isCollapsed = true;
                // Optionally pause simulation or change animation style when collapsed
                 cancelAnimationFrame(animationFrameId); // Stop normal oscillation animation
            } else if (currentCalculatedAmplitude <= visualCollapseThreshold && isCollapsed) {
                // Reset from collapsed state if amplitude drops below threshold
                statusMessage.textContent = 'המבנה התאושש'; // Or similar
                statusMessage.className = 'status status'; // Reset class
                isCollapsed = false;
                structure.classList.remove('collapsed');
                 // Restart simulation when recovering from collapse
                 startSimulation();
            } else if (currentCalculatedAmplitude > visualWarningThreshold && currentCalculatedAmplitude <= visualCollapseThreshold) {
                statusMessage.textContent = 'שימו לב: התנודות מתגברות משמעותית!';
                statusMessage.className = 'status warning';
            } else { // Amplitude is below warning threshold
                statusMessage.textContent = 'המבנה יציב';
                statusMessage.className = 'status status'; // Normal status
            }

             // Ensure simulation is running whenever the slider is moved and not collapsed
             if (!animationFrameId && !isCollapsed) {
                 startSimulation();
             }
        });

        // Toggle explanation visibility
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר את ההסבר' : 'הסבר לי את סוד התהודה!';
        });

        // Initial state setup:
        // 1. Set initial display values based on the default slider value.
        // 2. Start the animation loop.
        // We can simulate an 'input' event to set the initial state easily.
        frequencySlider.dispatchEvent(new Event('input'));
    });
</script>
```