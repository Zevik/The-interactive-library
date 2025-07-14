---
title: "קולות עמוקים: הצלילים הנסתרים של פילים"
english_slug: deep-voices-the-hidden-sounds-of-elephants
category: "מדעי החיים / ביולוגיה"
tags: זואולוגיה, התנהגות בעלי חיים, תקשורת בעלי חיים, אינפרה-סאונד, אקוסטיקה
---
# קולות עמוקים: הצלילים הנסתרים של פילים
האם אי פעם תהיתם איך פילים מצליחים לתקשר אחד עם השני למרחקים עצומים, לפעמים מעבר לאופק הראייה? הסוד שלהם מסתתר בצלילים שאוזן אדם כלל אינה מסוגלת לשמוע. בואו נחקור את זה!

<div id="simulation-container">
    <div class="sky-background"></div>
    <div class="ground-foreground"></div>
    <div id="elephants">
        <div id="sender-elephant" class="elephant">🐘</div>
        <div id="wave-path">
             <div id="obstacle-representation"></div>
        </div>
        <div id="receiver-elephant" class="elephant">🐘</div>
    </div>

    <div id="controls">
        <h2>חוקרים תקשורת פילים</h2>
        <p class="instruction">בחר את סוג האות והמרחק, ובדוק אם ההודעה תגיע!</p>
        <div class="control-group">
            <label for="frequency">סוג האות הקולי:</label>
            <select id="frequency">
                <option value="high">קול אנושי גבוה (כמו דיבור, 2 ק"ה)</option>
                <option value="low">צליל נמוך (שמיע לאדם, 100 ה"צ)</option>
                <option value="infrasound">אינפרה-סאונד (לא שמיע לאדם, 20 ה"צ)</option>
            </select>
        </div>
        <div class="control-group">
            <label for="distance">מרחק בין פילים:</label>
            <input type="range" id="distance" min="100" max="15000" value="1000">
            <span id="distance-value">1000</span> מטרים
        </div>
         <div class="control-group">
            <label for="obstacle">הוספת מכשול?</label>
            <input type="checkbox" id="obstacle">
            <span> (למשל גבעה או יער סבוך)</span>
        </div>
        <button id="send-sound">שגר אות!</button>
    </div>

    <div id="simulation-results">
        <p class="initial-message">מוכנים לשגר את האות הראשון?</p>
    </div>
</div>

<style>
    /* General Styles */
    #simulation-container {
        font-family: 'Arial', sans-serif;
        border: 1px solid #d3b899; /* Earthy border */
        padding: 0; /* Remove padding here, add to inner elements */
        margin-bottom: 30px;
        background-color: #eaddca; /* Light sandy background */
        border-radius: 12px;
        overflow: hidden; /* Contain background/foreground */
        position: relative;
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
    }

    .sky-background {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 60%; /* Sky takes top part */
        background: linear-gradient(to bottom, #a0c4ff, #baffc9); /* Gradient sky */
        z-index: 0;
    }

     .ground-foreground {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 50%; /* Ground takes bottom part, overlaps sky slightly */
        background: linear-gradient(to top, #8a5a44, #a98467); /* Gradient ground */
        z-index: 1;
     }

    #elephants {
        display: flex;
        align-items: flex-end; /* Align elephants to the ground */
        justify-content: space-between;
        margin: 0 40px 10px 40px; /* Adjust margins */
        position: relative;
        min-height: 150px; /* Give space for wave animation */
        z-index: 3; /* Ensure elephants are above everything */
    }

    .elephant {
        font-size: 5em; /* Slightly larger */
        cursor: pointer;
        transition: transform 0.3s ease;
        position: relative;
        padding-bottom: 5px; /* Lift slightly off the absolute bottom */
        filter: drop-shadow(2px 4px 6px rgba(0,0,0,0.3)); /* Subtle shadow */
    }

     #sender-elephant {
        transform: translateX(-5px);
     }

     #receiver-elephant {
        transform: translateX(5px);
     }

    #wave-path {
        position: absolute;
        left: 100px; /* Position between elephants */
        right: 100px; /* Position between elephants */
        bottom: 45%; /* Vertically centered slightly above ground */
        height: 30px; /* Height of the path visualization */
        z-index: 2; /* Below elephants, above ground */
        /* Optional: add a subtle visual for the path */
        /* background: rgba(255, 255, 255, 0.2); */
        /* border-radius: 5px; */
    }

    #obstacle-representation {
        position: absolute;
        bottom: 0; /* Align to bottom of wave-path */
        left: 50%; /* Centered */
        transform: translateX(-50%); /* Center horizontally */
        width: 100px; /* Width of obstacle visual */
        height: 60px; /* Height of obstacle visual */
        background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 60"><path d="M0 60 Q 25 0 50 30 T 100 60 Z" fill="%236d5a4a"/></svg>'); /* Simple hill shape */
        background-size: contain;
        background-repeat: no-repeat;
        opacity: 0; /* Hidden by default */
        transition: opacity 0.5s ease;
        z-index: 3; /* Above the wave */
    }


    .sound-wave {
        position: absolute;
        left: 0;
        top: 50%; /* Vertically center wave line within wave-path */
        transform: translateY(-50%); /* Adjust for its own height */
        height: 6px; /* Base height of wave line */
        background: rgba(0, 123, 255, 0.8); /* Base color */
        opacity: 0;
        transform-origin: left center;
        width: 0; /* Start with no width */
        transition: width linear, opacity linear, height linear; /* Animate all properties */
        filter: blur(1px); /* Soften the wave line */
        z-index: 2;
    }

    .wave-high { background: linear-gradient(to right, #ff6b6b, rgba(255, 107, 107, 0)); height: 4px;} /* Reddish, thinner */
    .wave-low { background: linear-gradient(to right, #4ecdc4, rgba(78, 205, 196, 0)); height: 8px;} /* Teal, thicker */
    .wave-infrasound { background: linear-gradient(to right, #45b7d1, rgba(69, 183, 209, 0)); height: 12px;} /* Bluish, thickest */


    #controls {
        background-color: #f4eacd; /* Lighter sandy background */
        padding: 20px;
        border-radius: 0 0 12px 12px; /* Round only bottom corners */
        border-top: 1px solid #d3b899;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); /* Responsive grid */
        gap: 15px; /* Space between grid items */
        align-items: center;
    }

    #controls h2 {
        grid-column: 1 / -1; /* Span all columns */
        text-align: center;
        color: #5a4a3b; /* Darker earthy tone */
        margin-top: 0;
        margin-bottom: 10px;
    }

    .instruction {
        grid-column: 1 / -1; /* Span all columns */
        text-align: center;
        margin-bottom: 15px;
        color: #6d5a4a;
    }

    .control-group {
        display: flex;
        flex-direction: column; /* Stack label and input */
        gap: 5px; /* Space between label and input */
    }

    .control-group label {
        font-weight: bold;
        color: #5a4a3b;
    }

     .control-group select,
     .control-group input[type="range"],
     .control-group input[type="checkbox"] {
         padding: 8px;
         border: 1px solid #d3b899;
         border-radius: 5px;
         background-color: #fff;
         font-size: 1em;
     }

     .control-group input[type="range"] {
        padding: 0; /* Adjust padding for range */
        height: 25px; /* Make range slider look better */
        cursor: grab;
     }

      .control-group input[type="range"]::-webkit-slider-thumb {
          -webkit-appearance: none;
          appearance: none;
          width: 20px;
          height: 20px;
          background: #5a4a3b;
          cursor: grab;
          border-radius: 50%;
          border: 2px solid #fff;
          box-shadow: 0 2px 5px rgba(0,0,0,0.2);
      }

       .control-group input[type="range"]::-moz-range-thumb {
          width: 20px;
          height: 20px;
          background: #5a4a3b;
          cursor: grab;
          border-radius: 50%;
          border: 2px solid #fff;
          box-shadow: 0 2px 5px rgba(0,0,0,0.2);
       }


    #send-sound {
        grid-column: 1 / -1; /* Span all columns */
        width: fit-content; /* Button size based on content */
        margin: 10px auto 0 auto; /* Center the button */
        padding: 12px 25px;
        background-color: #4a90e2; /* Blue like elephant communication */
        color: white;
        border: none;
        border-radius: 25px; /* Pill shape */
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    #send-sound:hover {
        background-color: #357abd;
    }
     #send-sound:active {
        transform: scale(0.98);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
     }


    #simulation-results {
        grid-column: 1 / -1; /* Span all columns */
        margin-top: 15px;
        padding: 10px;
        text-align: center;
        font-weight: bold;
        min-height: 1.5em; /* Reserve space */
    }

    .initial-message { color: #6d5a4a; }
    .success-message { color: #28a745; } /* Green */
    .failure-message { color: #dc3545; } /* Red */


    /* Explanation Section Styles */
    #toggle-explanation {
        display: block;
        width: fit-content;
        margin: 20px auto;
        padding: 10px 20px;
        background-color: #28a745; /* Green */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    #toggle-explanation:hover {
        background-color: #218838;
    }

    #explanation-content {
        display: none; /* Hidden by default */
        border: 1px solid #ccc;
        padding: 25px;
        background-color: #f9f9f9;
        border-radius: 8px;
        line-height: 1.6;
        color: #333;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    #explanation-content h2 {
        color: #0056b3;
        margin-top: 0;
        border-bottom: 2px solid #eee;
        padding-bottom: 10px;
    }

    #explanation-content h3 {
         color: #007bff;
         margin-top: 20px;
         margin-bottom: 8px;
         border-bottom: 1px dotted #ddd;
         padding-bottom: 3px;
    }

     #explanation-content ul {
        list-style: disc;
        margin-left: 25px;
        padding-left: 0;
     }
      #explanation-content li {
        margin-bottom: 8px;
      }

</style>

<button id="toggle-explanation">הצג הסבר מפורט על אינפרה-סאונד</button>

<div id="explanation-content">
    <h2>הצלילים הנסתרים של פילים: אינפרה-סאונד</h2>

    <h3>מהו אינפרה-סאונד?</h3>
    אינפרה-סאונד מתייחס לגלי קול שתדרם נמוך מדי כדי להישמע על ידי אוזן אדם טיפוסית. בעוד שבני אדם שומעים בדרך כלל בטווח של 20 הרץ עד 20 קילוהרץ, אינפרה-סאונד נמצא מתחת ל-20 הרץ. גלי אינפרה-סאונד יכולים להיות מיוצרים על ידי תופעות טבע רבות, כמו רעידות אדמה, הרי געש, רוח, סופות ואפילו פעילות לב וכלי דם של יצורים גדולים.

    <h3>הפקת אינפרה-סאונד אצל פילים</h3>
    פילים הם בין היונקים היבשתיים הגדולים ביותר, וגודלם מאפשר להם להפיק צלילים בתדרים נמוכים במיוחד. בדומה לאופן שבו בני אדם מפיקים קול על ידי רעידות מיתרי הקול, פילים מפיקים צלילי אינפרה-סאונד (המכונים "רום" - Rumbles) על ידי רעידות איטיות ועמוקות של קפלי הקול הגדולים והכבדים שלהם בחלק התחתון של הגרון. קפלי קול אלו מתפקדים בדומה למיתרי הקול האנושיים, אך בשל גודלם ומסתם, הם רועדים בתדרים נמוכים בהרבה.

    <h3>קליטת אינפרה-סאונד אצל פילים</h3>
    פילים יכולים לקלוט צלילי אינפרה-סאונד לא רק דרך האוזניים הגדולות והרגישות שלהם, אלא גם דרך הרגליים והגוף. גלי קול בתדרים נמוכים מאוד יכולים לעבור דרך הקרקע כרעידות. לפילים יש רפידות שומניות מיוחדות ברגליהם ועצמות רגישות המאפשרות להם לחוש ברעידות אלו ולהעביר את המידע לאוזן הפנימית. יכולת זו, המכונה אולי "שמיעה דרך הרגליים", מאפשרת להם לזהות צלילים שמגיעים מרחקים גדולים במיוחד.

    <h3>יתרונות אינפרה-סאונד לתקשורת לטווח ארוך</h3>
    היתרון העיקרי של שימוש באינפרה-סאונד לתקשורת הוא יכולתו לעבור מרחקים גדולים עם הנחתה (החלשת העוצמה) מינימלית באוויר לעומת תדרים גבוהים יותר. גלים ארוכים (תדרים נמוכים) פחות מושפעים מחסימות פיזיות כמו עצים, שיחים או גבעות קטנות, ויכולים לעקוף או לעבור דרכם ביתר קלות מאשר גלים קצרים (תדרים גבוהים). בנוסף, רעשי רקע רבים בסביבה טבעית (כמו ציוץ ציפורים, קולות חרקים, או רשרוש עלים ברוח) הם לרוב בתדרים גבוהים יותר, כך שתקשורת באינפרה-סאונד מפחיתה את ההפרעה מרעשי רקע אלו. שילוב זה מאפשר לפילים לתקשר ביעילות למרחקים של קילומטרים רבים, לעיתים עד 10 ק"מ או יותר בתנאים אופטימליים.

    <h3>שימושים של פילים בתקשורת אינפרה-סאונד</h3>
    פילים משתמשים בתקשורת אינפרה-סאונד למגוון רחב של מטרות חברתיות והישרדותיות:
    <ul>
        <li>**שמירה על קשר בתוך העדר:** למרות שפילים מטיילים לרוב בקבוצות קטנות, עדרים גדולים יותר יכולים להתפרש על פני שטח נרחב מאוד. אינפרה-סאונד מאפשר לחברי העדר, גם כשהם מחוץ לטווח ראייה או שמיעה של תדרים גבוהים, לשמור על קשר, לדעת את מיקום הקבוצה העיקרית, ולהתעדכן במתרחש.</li>
        <li>**קריאה לעזרה או התרעה על סכנה:** פיל שנתקל בסכנה או נפרד מהקבוצה יכול לשלוח קריאות מצוקה באינפרה-סאונד שיכולות להישמע על ידי פילים אחרים במרחקים עצומים.</li>
        <li>**מציאת בני זוג:** זכרים ונקבות יכולים להשתמש באינפרה-סאונד כדי לאתר זה את זה, במיוחד בתקופת הייחום, ולהתכנס למטרות רבייה.</li>
        <li>**ניווט וקביעת כיוון:** ישנן השערות כי פילים עשויים להשתמש ביכולתם לחוש רעידות קרקע מרוחקות, כולל אלו שאינן בהכרח צלילי תקשורת מפילים אחרים (כמו רעם או תנועת בעלי חיים גדולים אחרים), כדי לנווט ולהבין את הסביבה סביבם.</li>
    </ul>

    <h3>השוואה לתקשורת קולית של בעלי חיים אחרים</h3>
    בעלי חיים רבים משתמשים בצלילים לתקשורת, אך השימוש הנרחב והקריטי של פילים באינפרה-סאונד לתקשורת לטווח ארוך הוא ייחודי בקרב יונקים יבשתיים. בעלי חיים ימיים גדולים כמו לווייתנים כחולים ולווייתנים גבן גם כן משתמשים בתדרים נמוכים מאוד (שבחלקם גולשים לטווח האינפרה-סאונד) לתקשורת על פני אוקיינוסים שלמים, שם תנאי הסביבה שונים לגמרי מאשר ביבשה. על היבשה, מעט יצורים גדולים מספיק כדי להפיק אינפרה-סאונד בעוצמה משמעותית כמו פילים, ופחותים אף יותר אלו המסתמכים עליו כתקשורת יומיומית חיונית לטווח ארוך.

    <h3>האתגרים והמחקר בתחום</h3>
    חקר תקשורת אינפרה-סאונד אצל פילים הוא מאתגר מכיוון שהצלילים אינם נשמעים לאדם. חוקרים מסתמכים על ציוד הקלטה מיוחד (מיקרופונים רגישים לתדרים נמוכים) וניתוח ספקטרוגרפי של ההקלטות כדי לזהות, לתעד ולפענח את "שפת" האינפרה-סאונד של הפילים. מעקב אחר קבוצות פילים בשטח והקלטה מתמשכת מאפשרים לקשר דפוסי קול להתנהגויות ספציפיות. האתגרים כוללים גם הבחנה בין צלילי אינפרה-סאונד שמקורם בפילים לבין רעשי רקע טבעיים אחרים בתדרים נמוכים, וכן הבנת המסלולים המדויקים שבהם הקולות עוברים דרך הקרקע והאוויר בסביבות שונות. למרות האתגרים, מחקר זה חושף שכבה נסתרת ומורכבת של החיים החברתיים של הפילים ואת יכולות התקשורת המדהימות שלהם.
</div>

<script>
    const sender = document.getElementById('sender-elephant');
    const receiver = document.getElementById('receiver-elephant');
    const wavePath = document.getElementById('wave-path');
    const obstacleRepresentation = document.getElementById('obstacle-representation');
    const frequencySelect = document.getElementById('frequency');
    const distanceInput = document.getElementById('distance');
    const distanceValueSpan = document.getElementById('distance-value');
    const obstacleCheckbox = document.getElementById('obstacle');
    const sendButton = document.getElementById('send-sound');
    const resultsDiv = document.getElementById('simulation-results');
    const toggleButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation-content');

    // Map frequency values to visual class and base attenuation
    const frequencyConfig = {
        high: { class: 'wave-high', attenuation: 0.0008, obstacleEffect: 0.6 }, // Higher att, high obstacle effect
        low: { class: 'wave-low', attenuation: 0.0002, obstacleEffect: 0.2 },  // Lower att, moderate obstacle effect
        infrasound: { class: 'wave-infrasound', attenuation: 0.00005, obstacleEffect: 0.08 } // Very low att, minimal obstacle effect
    };

    const receptionThreshold = 0.2; // Needs at least 20% strength to be 'received'

    // Update distance value display and obstacle visibility
    distanceInput.addEventListener('input', () => {
        distanceValueSpan.textContent = distanceInput.value;
    });

     // Show/hide obstacle based on checkbox
    obstacleCheckbox.addEventListener('change', () => {
         obstacleRepresentation.style.opacity = obstacleCheckbox.checked ? 1 : 0;
     });


    // Toggle explanation visibility
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר מפורט על אינפרה-סאונד' : 'הצג הסבר מפורט על אינפרה-סאונד';
    });

    // Simulation logic
    sendButton.addEventListener('click', () => {
        const frequency = frequencySelect.value;
        const distance = parseInt(distanceInput.value);
        const hasObstacle = obstacleCheckbox.checked;
        const config = frequencyConfig[frequency];

        // Disable button during animation
        sendButton.disabled = true;
        sendButton.textContent = 'משגר...';


        // Clear previous wave and results
        wavePath.querySelectorAll('.sound-wave').forEach(wave => wave.remove());
        resultsDiv.className = ''; // Clear previous state classes
        resultsDiv.textContent = 'הפיל השולח משגר אות...';
        resultsDiv.classList.add('initial-message');


        // --- Animation: Sender Elephant Action ---
        sender.style.transform = 'scale(0.95)'; // Simulate 'rumble' contraction
        setTimeout(() => {
             sender.style.transform = 'scale(1.0)'; // Return to normal
        }, 300);


        // --- Simulation: Calculate Signal Strength ---
        let signalStrength = 1.0; // Start at max strength (100%)

        // Attenuation over distance (exponential decay)
        signalStrength = signalStrength * Math.exp(-config.attenuation * distance);

        // Attenuation due to obstacle
        if (hasObstacle) {
             signalStrength -= config.obstacleEffect;
             signalStrength = Math.max(0, signalStrength); // Strength cannot be negative
        }

        // Clamp signal strength to be between 0 and 1
        signalStrength = Math.max(0, Math.min(1, signalStrength));


        // --- Animation: Wave Propagation ---
        const wave = document.createElement('div');
        wave.classList.add('sound-wave', config.class);
        wavePath.appendChild(wave);

        // Calculate animation duration based on distance (adjust speed as needed)
        // Make infrasound slightly slower visually? Or just vary duration by distance.
        const baseSpeed = 5000; // meters per second (conceptual)
        const animationDuration = distance / baseSpeed; // Duration in seconds

         // Animate width and opacity over time
         wave.style.transition = `width ${animationDuration}s linear, opacity ${animationDuration}s linear`;


         // Trigger the animation
        requestAnimationFrame(() => {
             // After a short delay to ensure element is in DOM
             setTimeout(() => {
                 wave.style.width = '100%'; // Wave travels the full visual path width
                 // Opacity fades out as it travels, reflecting attenuation
                 // Simple linear fade-out for visual effect, final strength handled later
                 wave.style.opacity = 0.8; // Start visible
             }, 50); // Small delay
         });


        // --- Animation: Visual Attenuation Effect on Wave ---
        // This is harder to tie directly to distance + obstacle *during* the CSS animation easily.
        // Instead, we will calculate the final visual state and set it after the animation finishes,
        // OR, simulate it by adjusting opacity/height over time with JS steps (more complex).
        // Let's stick to setting the final appearance based on calculated strength.
        // A simpler visual attenuation during travel: opacity reduces, height shrinks.
        // Need JS for steps or CSS keyframes if complex attenuation pattern needed.
        // Let's keep it simple: wave fades/shrinks *conceptually* as it travels. Final state is key.


        // --- Result & Animation: Receiver Elephant Reaction & Message ---
        const animationDurationMs = animationDuration * 1000;

        setTimeout(() => {
            // Remove the wave element or finalize its state
            wave.style.opacity = 0; // Fade out the wave after it arrives or dissipates


            if (signalStrength >= receptionThreshold) {
                resultsDiv.textContent = `הגל (${frequencySelect.options[frequencySelect.selectedIndex].text}) הגיע לפיל השני בעוצמה מספקת! (חוזק: ${(signalStrength * 100).toFixed(1)}%)`;
                resultsDiv.className = 'success-message';

                // Animate receiver elephant reaction
                receiver.style.transform = 'scale(1.1) translateY(-5px)'; // Jumps slightly
                 setTimeout(() => {
                     receiver.style.transform = 'scale(1.0) translateY(0)'; // Return to normal
                 }, 400); // Reaction duration
                  // Maybe add a subtle "pulse" animation at the receiver?
                 const pulse = document.createElement('div');
                 pulse.style.cssText = `
                     position: absolute;
                     bottom: 10px; /* Relative to elephant base */
                     right: 10px; /* Relative to elephant */
                     width: 30px;
                     height: 30px;
                     background-color: rgba(40, 167, 69, 0.5); /* Greenish pulse */
                     border-radius: 50%;
                     animation: pulse-receive 1s ease-out forwards;
                     z-index: 4;
                 `;
                 receiver.style.position = 'relative'; // Ensure pulse is positioned relative to elephant
                 receiver.appendChild(pulse);
                  setTimeout(() => pulse.remove(), 1000); // Remove pulse after animation

            } else {
                resultsDiv.textContent = `הגל (${frequencySelect.options[frequencySelect.selectedIndex].text}) נחלש מדי בדרך ולא הגיע לפיל השני. (חוזק: ${(signalStrength * 100).toFixed(1)}%)`;
                 resultsDiv.className = 'failure-message';
                 // Subtle 'missed' animation?
                 receiver.style.transform = 'translateX(5px) rotate(2deg)'; // Tilt slightly
                 setTimeout(() => {
                      receiver.style.transform = 'translateX(5px) rotate(0deg)';
                 }, 300);

            }

             // Re-enable button
            sendButton.disabled = false;
            sendButton.textContent = 'שגר אות!';

             // Clean up wave element completely after a delay
             setTimeout(() => {
                 if(wave && wave.parentElement) wave.remove();
             }, 1000); // Ensure it's gone after results are shown
        }, animationDurationMs);
    });

     // CSS for the receiver pulse animation
     const styleSheet = document.styleSheets[0];
     const pulseKeyframes = `@keyframes pulse-receive {
         0% { transform: scale(0.5); opacity: 0.8; }
         50% { transform: scale(1.5); opacity: 0.4; }
         100% { transform: scale(2.5); opacity: 0; }
     }`;
     styleSheet.insertRule(pulseKeyframes, styleSheet.cssRules.length);


    // Initial state setup
    explanationDiv.style.display = 'none';
    obstacleRepresentation.style.opacity = obstacleCheckbox.checked ? 1 : 0;

</script>
```