---
title: "הברומטר: המכשיר הפשוט שמנבא את מזג האוויר?"
english_slug: air-pressure-barometer-predicting-the-future
category: "פיזיקה"
tags: ["לחץ אוויר", "ברומטר", "מזג אוויר", "אטמוספרה", "מטאורולוגיה", "סימולציה"]
---
# הברומטר: המכשיר הפשוט שמנבא את מזג האוויר?

בעבר, מלחים, חקלאים וחוקרים היו תלויים בכלי פשוט למראה כדי לזהות סימנים לשינויים קרבים במזג האוויר, לפעמים שעות ואף ימים לפני שהופיעו עננים בשמיים. איך קופסת מתכת זעירה עם מחוג מצליחה "להרגיש" את העתיד? בואו נצלול לתוך העולם הנסתר של לחץ האוויר ונראה זאת בפעולה!

<div class="app-container">
    <div class="barometer-weather-area">
        <div class="barometer">
            <div class="dial">
                <div class="center-pin"></div>
                <div class="needle"></div>
                 <!-- Classic Barometer Labels -->
                <div class="weather-label stormy" style="--angle: -75deg;">סערה</div>
                <div class="weather-label rain" style="--angle: -45deg;">גשם</div>
                <div class="weather-label change" style="--angle: 0deg;">השתנות</div>
                <div class="weather-label fair" style="--angle: 45deg;">בהיר</div>
                <div class="weather-label very-dry" style="--angle: 75deg;">יבש מאוד</div>
                 <!-- Pressure markings - JS will add dynamically or CSS circles -->
            </div>
        </div>
        <div class="weather-display">
            <div class="weather-icon"></div>
            <div class="weather-text">מצב מזג האוויר: ...</div>
             <div class="pressure-readout">
                <span class="pressure-hpa">1013 hPa / mb</span> | <span class="pressure-inhg">29.92 inHg</span>
            </div>
        </div>
    </div>
    <div class="controls">
        <label for="pressure-slider">שנה לחץ אוויר בהדרגה:</label>
        <input type="range" id="pressure-slider" min="950" max="1050" value="1013" step="1">
        <div class="quick-changes">
            <button id="rapid-drop" class="control-button drop">לכיוון סופה (ירידה מהירה)</button>
            <button id="rapid-rise" class="control-button rise">לכיוון שמיים בהירים (עלייה מהירה)</button>
        </div>
    </div>
</div>

<style>
    :root {
        --blue-light: #e3f2fd;
        --blue-med: #90caf9;
        --blue-dark: #2196f3;
        --grey-light: #e0e0e0;
        --grey-med: #9e9e9e;
        --grey-dark: #424242;
        --red-accent: #ef5350;
        --green-accent: #66bb6a;
    }

    body {
        font-family: 'Arial', sans-serif; /* More specific font stack */
        line-height: 1.6;
        color: #333;
        background-color: #f8f8f8; /* Lighter background */
    }

    .app-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 25px; /* More padding */
        border: none; /* Remove standard border */
        border-radius: 12px; /* More rounded */
        margin: 20px auto; /* Center block */
        max-width: 550px; /* Slightly larger max width */
        background: linear-gradient(to bottom right, #ffffff, var(--blue-light)); /* Subtle gradient */
        box-shadow: 0 8px 16px rgba(0,0,0,0.15); /* Nicer shadow */
        overflow: hidden; /* Ensure elements stay within bounds */
    }

    h1 {
         text-align: center;
         color: var(--grey-dark);
         margin-bottom: 25px;
         font-size: 1.8em;
    }

    p:first-of-type { /* Style for intro paragraph */
        text-align: center;
        max-width: 500px;
        margin: 0 auto 30px auto;
        color: #555;
    }


    .barometer-weather-area {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        margin-bottom: 30px; /* More space */
    }

    .barometer {
        width: 240px; /* Larger barometer */
        height: 240px;
        border: 15px solid var(--grey-light); /* Thicker, lighter border */
        border-radius: 50%;
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 25px; /* More space */
        background: linear-gradient(to bottom right, #eceff1, #cfd8dc); /* Subtle grey gradient */
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1), 0 4px 8px rgba(0,0,0,0.1); /* Inner and outer shadow */
    }

    .dial {
        width: 210px; /* Larger dial */
        height: 210px;
        border-radius: 50%;
        position: relative;
        background: radial-gradient(circle at 50% 50%, #ffffff 60%, #f5f5f5 100%); /* Cleaner radial gradient */
        box-shadow: inset 0 0 5px rgba(0,0,0,0.05);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .center-pin {
        position: absolute;
        width: 12px;
        height: 12px;
        background-color: var(--grey-dark);
        border-radius: 50%;
        z-index: 11; /* Above needle */
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }


    .needle {
        position: absolute;
        bottom: 50%;
        left: 50%;
        width: 6px; /* Thicker needle */
        height: 100px; /* Longer needle */
        background: linear-gradient(to right, var(--red-accent), #c62828); /* Red gradient */
        transform-origin: bottom center;
        transform: translateX(-50%) rotate(0deg); /* Initial rotation, adjusted for 950-1050 mapping */
        transition: transform 0.7s cubic-bezier(0.25, 0.8, 0.25, 1); /* Smoother, slightly bouncy transition */
        z-index: 10;
        filter: drop-shadow(1px 1px 2px rgba(0,0,0,0.3)); /* Shadow for needle */
    }

    /* Add tick marks dynamically or via pseudo-elements if simple */
    /* For simplicity and given constraints, we'll rely on the pressure labels positioning */


    .weather-label {
        position: absolute;
        top: 50%;
        left: 50%;
        transform-origin: 0 0; /* Rotate around the center */
        transform: translate(-50%, -50%) rotate(calc(var(--angle) - 90deg)) translate(105px) rotate(90deg); /* Position and orient text */
        font-size: 0.9em;
        font-weight: bold;
        color: #555;
        text-align: center;
        width: 60px; /* Fixed width for better alignment */
    }

    .weather-label.stormy { color: #c62828; } /* Dark Red */
    .weather-label.rain { color: #1565c0; } /* Dark Blue */
    .weather-label.change { color: #fbc02d; } /* Dark Yellow */
    .weather-label.fair { color: #388e3c; } /* Dark Green */
    .weather-label.very-dry { color: #e65100; } /* Dark Orange */


    .weather-display {
        width: 100%;
        min-height: 120px; /* Min height */
        border: none; /* Remove border */
        border-radius: 8px;
        display: flex;
        flex-direction: column; /* Stack elements */
        justify-content: center;
        align-items: center;
        font-size: 1.1em;
        font-weight: bold;
        text-align: center;
        transition: background-color 1s ease-in-out, color 0.8s ease; /* Smoother color transition */
        color: var(--grey-dark);
        padding: 15px; /* More padding */
        box-sizing: border-box;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08); /* Subtle shadow */
         background-color: var(--blue-light); /* Default background */
    }

    .weather-icon {
        width: 40px;
        height: 40px;
        background-color: var(--grey-med); /* Placeholder for potential icon */
        border-radius: 50%;
        margin-bottom: 10px;
        /* Add animation for icon change if needed */
    }

    .weather-text {
        font-size: 1.3em; /* Larger weather description text */
        margin-bottom: 8px;
    }

    .pressure-readout {
         font-size: 0.9em;
         color: #555;
         font-weight: normal;
    }


    .controls {
        width: 100%;
        max-width: 450px;
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 20px;
    }

    .controls label {
        margin-bottom: 12px; /* More space */
        font-weight: bold;
        color: var(--grey-dark);
        font-size: 1.1em;
    }

    #pressure-slider {
        width: 100%;
        margin-bottom: 20px; /* More space */
        cursor: grab; /* Indicate interactivity */
    }
     #pressure-slider:active {
        cursor: grabbing;
     }

    .quick-changes {
        display: flex;
        gap: 20px; /* More space between buttons */
        width: 100%;
        justify-content: center;
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .control-button {
        flex-grow: 1; /* Allow buttons to grow */
        max-width: 200px; /* Max width for buttons */
        padding: 12px 18px; /* More padding */
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 6px; /* More rounded */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    .control-button.drop {
        background: linear-gradient(to right, #f44336, #e57373); /* Red gradient */
    }
     .control-button.drop:hover {
        background: linear-gradient(to right, #e53935, #ef5350);
        box-shadow: 0 6px 10px rgba(0,0,0,0.15);
     }
      .control-button.drop:active {
        transform: scale(0.98);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      }


    .control-button.rise {
         background: linear-gradient(to right, #4CAF50, #81c784); /* Green gradient */
    }
     .control-button.rise:hover {
        background: linear-gradient(to right, #43a047, #66bb6a);
        box-shadow: 0 6px 10px rgba(0,0,0,0.15);
     }
     .control-button.rise:active {
        transform: scale(0.98);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
     }


    /* Explanation styles */
    .explanation {
        margin-top: 40px; /* More space */
        border-top: 2px dashed var(--grey-light); /* Nicer separator */
        padding-top: 30px; /* More padding */
    }

    .explanation h2, .explanation h3 {
        color: var(--grey-dark);
        margin-bottom: 15px;
    }

    .explanation h2 {
        font-size: 1.5em;
        text-align: center;
    }
    .explanation h3 {
        font-size: 1.2em;
        margin-top: 20px;
    }


    .explanation p {
        line-height: 1.7; /* Increased line height */
        margin-bottom: 18px; /* More space */
        color: #555;
    }

    .explanation ul {
        margin-bottom: 18px;
        padding-left: 25px;
        color: #555;
    }
     .explanation li {
        margin-bottom: 8px;
     }
      .explanation li strong {
        color: var(--grey-dark);
     }


    #toggle-explanation {
        display: block;
        margin: 30px auto; /* More space */
        padding: 12px 25px; /* More padding */
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: var(--blue-dark); /* Blue button */
        color: white;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    #toggle-explanation:hover {
        background-color: #1976d2; /* Darker blue */
        box-shadow: 0 6px 10px rgba(0,0,0,0.15);
    }

     #toggle-explanation:active {
        transform: scale(0.98);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
     }

     /* Weather Display Colors & Text */
    .weather-display.stormy {
        background-color: #ffebee; /* Light red */
        color: #b71c1c; /* Dark red text */
    }
     .weather-display.rain {
        background-color: #e3f2fd; /* Light blue */
        color: #0d47a1; /* Dark blue text */
     }
      .weather-display.change {
        background-color: #fffde7; /* Light yellow */
        color: #f57f17; /* Dark yellow text */
     }
     .weather-display.fair {
        background-color: #e8f5e9; /* Light green */
        color: #1b5e20; /* Dark green text */
     }
     .weather-display.very-dry {
        background-color: #fff3e0; /* Light orange */
        color: #e65100; /* Dark orange text */
     }

</style>

<button id="toggle-explanation">גלה את הסוד מאחורי הברומטר</button>

<div class="explanation" style="display: none;">
    <h2>הכוח הנסתר של לחץ האוויר</h2>

    <h3>מהו לחץ אוויר, בעצם?</h3>
    <p>דמיינו את כדור הארץ עטוף בשמיכה ענקית של אוויר – זוהי האטמוספרה שלנו. אוויר, כמו כל חומר, מורכב ממולקולות ויש לו משקל. לחץ האוויר הוא פשוט המשקל הזה, הכוח שעמוד האוויר העצום שמעלינו מפעיל על כל יחידת שטח על פני הקרקע (או הים). אנחנו חיים למעשה בתחתית "אוקיינוס" של אוויר!</p>

    <h3>איך מודדים את ה"משקל" הזה? הברומטר בפעולה</h3>
    <p>ברומטר הוא המאזניים שמודדים את לחץ האוויר. הברומטר האנרואידי הנפוץ (כמו זה שאתם רואים כאן בסימולציה וקיים במכשירים רבים) מכיל קופסת מתכת קטנה, אטומה, שממנה הוצא חלק מהאוויר – מעין "ואקום" חלקי. ככל שלחץ האוויר החיצוני גדל, הוא לוחץ חזק יותר על הקופסה ומכווץ אותה. כשלחץ האוויר יורד, הקופסה מתרחבת קלות בחזרה. התנועה הזעירה הזו של הקופסה מוגברת בעזרת מערכת מנופים חכמה שמזיזה מחוג על סולם לחץ.</p>

    <h3>מדוע לחץ האוויר אף פעם לא נח?</h3>
    <p>לחץ האוויר משתנה כל הזמן, והשינויים האלה הם המפתח לחיזוי מזג האוויר. הסיבות העיקריות לשינויים הן:</p>
    <ul>
        <li><strong>טמפרטורה:</strong> אוויר חם הוא קל ו"קופצני" יותר מאוויר קר והוא עולה למעלה. זה יוצר אזורי לחץ נמוך ליד הקרקע באזורים חמים. אוויר קר הוא כבד יותר ושוקע, יוצר אזורי לחץ גבוה.</li>
        <li><strong>גובה:</strong> ככל שעולים גבוה יותר (לטפס על הר, למשל), כמות האוויר שמעלינו קטנה, ולכן גם הלחץ יורד משמעותית.</li>
        <li><strong>מערכות מזג אוויר:</strong> אלו הדינמיקות הגדולות של תנועת אוויר באטמוספרה, והן הגורם המרכזי לשינויים היומיומיים בלחץ שאנו חווים.</li>
    </ul>

    <h3>הקשר הדרמטי בין לחץ אוויר למזג אוויר</h3>
    <p>השינויים בלחץ האוויר הם לא סתם מספרים; הם מראים לנו מה "מתבשל" באטמוספרה:</p>
    <ul>
        <li><strong>אזור לחץ גבוה (מסומן לעיתים ב-H):</strong> כאן האוויר שוקע. אוויר שוקע מתחמם מעט ונהיה יציב, מה שמקשה על היווצרות עננים ומשקעים. אזורי לחץ גבוה מביאים בדרך כלל לשמיים בהירים, אוויר יבש ומזג אוויר יציב ונעים. חשבו על לחץ גבוה כעל "כיפה" של אוויר שדוחפת את העננים למטה.</li>
        <li><strong>אזור לחץ נמוך (מסומן לעיתים ב-L):</strong> כאן האוויר עולה. אוויר שעולה מתקרר, ואדי המים שבו מתעבים במהירות ויוצרים עננים. אם עליית האוויר חזקה, העננים יתפתחו לענני גשם ואף סופות רעמים. אזורי לחץ נמוך קשורים למזג אוויר מעונן, גשום, רוחות חזקות ולעיתים סוער. חשבו על לחץ נמוך כעל "שקע" ששואב את האוויר למעלה.</li>
    </ul>

    <h3>איך הברומטר עוזר "לחזות" מזג אוויר?</h3>
    <p>הסוד הוא לא בערך הלחץ הרגעי בלבד, אלא ב<strong>מגמת</strong> השינוי. מעקב אחר תנועת המחוג נותן לנו רמזים חשובים:</p>
    <ul>
        <li><strong>לחץ עולה:</strong> בדרך כלל מסמן התקרבות של אזור לחץ גבוה. אם המחוג עולה בהתמדה, צפו לשיפור במזג האוויר ולימים בהירים ויציבים יותר. עלייה מהירה עשויה לבשר על התבהרות מהירה לאחר סערה.</li>
        <li><strong>לחץ יורד:</strong> לרוב מצביע על התקרבות של אזור לחץ נמוך. כשהמחוג יורד, זהו סימן אזהרה להתדרדרות אפשרית: עננות גוברת, גשם, רוחות, ואולי אף סופות. ירידה מהירה היא אינדיקטור חזק להגעת סערה או חזית מזג אוויר משמעותית.</li>
        <li><strong>לחץ יציב:</strong> מצביע על כך שמערכת מזג האוויר הנוכחית (בין אם היא בהירה, מעוננת או גשומה קלות) צפויה להימשך ללא שינויים דרמטיים בטווח הקצר.</li>
    </ul>
    <p>אז הברומטר לא באמת מנבא את העתיד בכוחות על, אלא הוא כלי מדעי גאוני שמודד שינויים פיזיים בסיסיים באטמוספרה. השינויים הללו הם סימנים מוקדמים לתנועת גושי אוויר גדולים, שהם הגורמים האמיתיים לשינויים במזג האוויר שאנו חווים. בפעם הבאה שתראו ברומטר, תזכרו שאתם מסתכלים על "מצפן" שמצביע לאן נושבת רוח השינוי באוויר שסביבכם!</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const needle = document.querySelector('.needle');
        const pressureHpaEl = document.querySelector('.pressure-hpa');
        const pressureInhgEl = document.querySelector('.pressure-inhg');
        const weatherDisplayEl = document.querySelector('.weather-display');
        const weatherTextEl = document.querySelector('.weather-text');
        const pressureSlider = document.getElementById('pressure-slider');
        const rapidDropButton = document.getElementById('rapid-drop');
        const rapidRiseButton = document.getElementById('rapid-rise');
        const explanationDiv = document.querySelector('.explanation');
        const toggleExplanationButton = document.getElementById('toggle-explanation');

        const minPressure = 950; // hPa
        const maxPressure = 1050; // hPa
        // Map pressure range [950, 1050] to angle range [-90, 90] degrees
        // 950 hPa -> -90 deg
        // 1000 hPa -> 0 deg (approx 1013 standard)
        // 1050 hPa -> 90 deg
        const minAngle = -90; // degrees (for min pressure)
        const maxAngle = 90; // degrees (for max pressure)
        const standardPressure = 1013.25; // hPa
        const hpaToInhg = 0.02953;

        let animationFrameId = null; // For rapid change animation

        // Function to map pressure to needle angle
        function pressureToAngle(pressure) {
             // Ensure pressure is within range
            pressure = Math.max(minPressure, Math.min(maxPressure, pressure));
             // Linear mapping: angle = minAngle + (pressure - minPressure) / (maxPressure - minPressure) * (maxAngle - minAngle)
            const angle = minAngle + (pressure - minPressure) / (maxPressure - minPressure) * (maxAngle - minAngle);
            return angle;
        }

        // Function to update the barometer and weather display
        function updateDisplay(pressureHpa) {
            // Update pressure values
            const pressureInhg = pressureHpa * hpaToInhg;
            pressureHpaEl.textContent = `${pressureHpa.toFixed(0)} hPa / mb`;
            pressureInhgEl.textContent = `${pressureInhg.toFixed(2)} inHg`;

            // Calculate needle rotation
            const angle = pressureToAngle(pressureHpa);
            needle.style.transform = `translateX(-50%) rotate(${angle}deg)`;

            // Update weather display based on pressure thresholds
            // Clear previous classes
            weatherDisplayEl.classList.remove('stormy', 'rain', 'change', 'fair', 'very-dry');

            let weatherText = '';
            // Using more defined ranges and classic barometer terms
            if (pressureHpa < 970) {
                weatherText = 'סערה מתקרבת';
                weatherDisplayEl.classList.add('stormy');
            } else if (pressureHpa >= 970 && pressureHpa < 995) {
                weatherText = 'צפוי גשם';
                 weatherDisplayEl.classList.add('rain');
            } else if (pressureHpa >= 995 && pressureHpa < 1015) {
                weatherText = 'השתנות במזג האוויר / יציב';
                 weatherDisplayEl.classList.add('change');
            } else if (pressureHpa >= 1015 && pressureHpa < 1035) {
                weatherText = 'מזג אוויר בהיר';
                 weatherDisplayEl.classList.add('fair');
            } else { // pressureHpa >= 1035
                weatherText = 'בהיר ויבש מאוד';
                 weatherDisplayEl.classList.add('very-dry');
            }
            weatherTextEl.textContent = `מצב נוכחי: ${weatherText}`;
             // Color transition is handled by CSS class transition on background-color
        }

        // Initialize display with the slider's default value
        updateDisplay(parseFloat(pressureSlider.value));

        // Event listener for the slider
        pressureSlider.addEventListener('input', (event) => {
             // Cancel any rapid change animation if slider is moved manually
            cancelAnimationFrame(animationFrameId);
            const currentPressure = parseFloat(event.target.value);
            updateDisplay(currentPressure);
        });

        // Function to smoothly animate pressure change
        function animatePressureChange(startPressure, endPressure, duration) {
            const startTime = performance.now();
            const startAngle = pressureToAngle(startPressure);
            const endAngle = pressureToAngle(endPressure);

            function step(currentTime) {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1); // progress from 0 to 1

                // Use cubic-bezier for easing (same as needle transition)
                const easedProgress = 1 - Math.pow(1 - progress, 3); // simple cubic ease-out

                const currentPressure = startPressure + (endPressure - startPressure) * easedProgress;

                // Update slider position without triggering its input event handler recursively
                pressureSlider.value = currentPressure.toFixed(0); // Update slider position

                 // Update display directly
                const currentAngle = pressureToAngle(currentPressure);
                 needle.style.transform = `translateX(-50%) rotate(${currentAngle}deg)`;

                const currentPressureHpa = parseFloat(pressureSlider.value); // Use value from updated slider
                 const pressureInhg = currentPressureHpa * hpaToInhg;
                 pressureHpaEl.textContent = `${currentPressureHpa.toFixed(0)} hPa / mb`;
                 pressureInhgEl.textContent = `${pressureInhg.toFixed(2)} inHg`;


                // Update weather display (this might be too flickery if updated every frame,
                // let's call updateDisplay at intervals or let CSS transitions handle it)
                 // Option 1: Update weather display only when significant change or at end
                 // For now, update on pressure change. CSS transition handles the color.
                 // updateDisplay(currentPressureHpa); // Avoids re-calculating angle and setting transform

                 // Refined update during animation - only update text/class when crossing threshold
                 let weatherText = '';
                let newClass = '';
                 if (currentPressureHpa < 970) {
                     weatherText = 'סערה מתקרבת'; newClass = 'stormy';
                 } else if (currentPressureHpa >= 970 && currentPressureHpa < 995) {
                     weatherText = 'צפוי גשם'; newClass = 'rain';
                 } else if (currentPressureHpa >= 995 && currentPressureHpa < 1015) {
                     weatherText = 'השתנות במזג האוויר / יציב'; newClass = 'change';
                 } else if (currentPressureHpa >= 1015 && currentPressureHpa < 1035) {
                     weatherText = 'מזג אוויר בהיר'; newClass = 'fair';
                 } else { // pressureHpa >= 1035
                     weatherText = 'בהיר ויבש מאוד'; newClass = 'very-dry';
                 }

                 // Only update if class or text actually changes
                 if (!weatherDisplayEl.classList.contains(newClass)) {
                     weatherDisplayEl.classList.remove('stormy', 'rain', 'change', 'fair', 'very-dry');
                     weatherDisplayEl.classList.add(newClass);
                 }
                 weatherTextEl.textContent = `מצב נוכחי: ${weatherText}`;


                if (progress < 1) {
                    animationFrameId = requestAnimationFrame(step);
                } else {
                    // Ensure final value is set precisely
                    pressureSlider.value = endPressure.toFixed(0);
                    updateDisplay(endPressure); // Final update to ensure correctness
                }
            }

            // Cancel any previous animation
            cancelAnimationFrame(animationFrameId);
            animationFrameId = requestAnimationFrame(step);
        }


        // Event listener for rapid drop button
        rapidDropButton.addEventListener('click', () => {
            let currentPressure = parseFloat(pressureSlider.value);
            const targetPressure = Math.max(minPressure, currentPressure - 30); // Larger drop/rise
            animatePressureChange(currentPressure, targetPressure, 3000); // Animate over 3 seconds
        });

        // Event listener for rapid rise button
        rapidRiseButton.addEventListener('click', () => {
            let currentPressure = parseFloat(pressureSlider.value);
            const targetPressure = Math.min(maxPressure, currentPressure + 30); // Larger drop/rise
             animatePressureChange(currentPressure, targetPressure, 3000); // Animate over 3 seconds
        });


        // Event listener for toggle explanation button
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            // Add a slight transition for display change if possible with max-height or opacity
            // but simple display change is safest with strict constraints.
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר את הסוד מאחורי הברומטר' : 'גלה את הסוד מאחורי הברומטר';
             // Scroll to explanation if showing it? Maybe too complex.
        });
    });
</script>
```