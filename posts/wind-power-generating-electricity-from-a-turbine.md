---
title: "כוח הרוח: מייצרים חשמל משבשבת"
english_slug: wind-power-generating-electricity-from-a-turbine
category: "פיזיקה"
tags: [אנרגיה מתחדשת, שבשבת רוח, חשמל, אנרגיה קינטית, המרת אנרגטית]
---
# רותמים את הרוח: מסע אל ייצור חשמל משבשבת

האם אי פעם עצרתם לחשוב איך ייתכן שאוויר שאיננו רואים, המרחף סביבנו, יכול להפוך למקור חשמל שמניע את חיינו? מה קורה באותן 'מניפות' ענקיות, צחורות ויפות, שמוצבות בנוף על גבעות או בים, ולכאורה רק מסתובבות? בואו נצלול לתוך סודותיה של טורבינת הרוח ונגלה כיצד היא לוכדת את הכוח העצום של הרוח והופכת אותו לאנרגיה ירוקה!

<div id="wind-turbine-app">
    <div class="sky"></div>
    <div class="ground"></div>
    <div class="turbine-container">
        <div class="tower"></div>
        <div class="nacelle"></div>
        <div class="blades">
            <div class="blade blade1"></div>
            <div class="blade blade2"></div>
            <div class="blade blade3"></div>
        </div>
    </div>

     <div class="dashboard">
        <div class="controls">
            <label for="wind-speed-slider">עוצמת רוח:</label>
            <input type="range" id="wind-speed-slider" min="0" max="100" value="0">
            <span id="wind-speed-value">0</span>
        </div>

        <div class="meters-power">
            <div class="meters">
                <div class="meter">
                    <div class="meter-label">כוח מיוצר:</div>
                    <div id="power-meter" class="meter-value">0.00 kW</div>
                </div>
                <div class="meter">
                    <div class="meter-label">אנרגיה מצטברת:</div>
                    <div id="energy-meter" class="meter-value">0.00 kWh</div>
                </div>
            </div>
            <div class="power-indicator">
                <div class="power-label">ייצור חשמל:</div>
                <div class="power-bar-container">
                    <div id="power-bar" class="power-bar"></div>
                </div>
            </div>
        </div>
    </div>

</div>

<button id="toggle-explanation">הצג הסבר מעמיק</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מעמיק: כיצד טורבינת רוח מייצרת חשמל</h2>

    <p><strong>מהי רוח ומאין היא באה?</strong> רוח היא פשוט אוויר בתנועה! היא נוצרת בעיקר בשל התחממות לא אחידה של פני כדור הארץ על ידי השמש. אזורים חמים יותר מחממים את האוויר שמעליהם, גורמים לו להתפשט ולעלות, ויוצרים אזורי לחץ נמוך. אוויר קר יותר וצפוף יותר מאזורי לחץ גבוה זורם למלא את החלל הזה, וכך נוצרת הרוח.</p>

    <p><strong>האנרגיה החבויה ברוח:</strong> לכל גוף נע יש אנרגיה קינטית, וכך גם לאוויר הנע. כמות האנרגיה הקינטית ברוח תלויה בשני גורמים עיקריים: מסת האוויר הנע ומהירותו. מכיוון שקשה למדוד את המסה באופן ישיר, נוח יותר לחשוב במונחי נפח אוויר שפוגע בטורבינה. אך הגורם המשפיע ביותר הוא ללא ספק <strong>מהירות הרוח</strong>. שימו לב שכמות האנרגיה הקינטית פרופורציונלית לריבוע המהירות (E = 0.5 * m * v²), ובהמשך נראה שלכוח המיוצר יש קשר חזק אף יותר למהירות.</p>

    <p><strong>המבנה המתוחכם של טורבינת הרוח המודרנית:</strong> טורבינה טיפוסית שאנו רואים כיום כוללת כמה חלקים מרכזיים:
    <ul>
        <li><strong>הלהבים (Blades):</strong> לרוב שלושה, מעוצבים בצורה אווירודינמית דומה לכנף מטוס. הם קולטים את אנרגיית הרוח.</li>
        <li><strong>הראש (Nacelle):</strong> ממוקם בראש המגדל ומכיל את הרכיבים הקריטיים: ציר הסיבוב, תיבת הילוכים (שמגבירה את מהירות הסיבוב מהלהבים הנעים יחסית לאט למהירות גבוהה יותר המתאימה לגנרטור), ובעיקר - ה<strong>גנרטור</strong>.</li>
        <li><strong>המגדל (Tower):</strong> מחזיק את הראש והלהבים בגובה רב, שם הרוח בדרך כלל חזקה ויציבה יותר וללא מכשולים קרקעיים.</li>
        <li><strong>המערכת האופקית (Yaw System):</strong> מאפשרת לכל ראש הטורבינה להסתובב על ציר המגדל כדי לפנות תמיד אל כיוון הרוח בצורה המיטבית.</li>
    </ul>
    </p>

    <p><strong>הקסם שבטורבינה: המרת אנרגיה קינטית לאנרגיה חשמלית:</strong> כאשר הרוח פוגעת בלהבים המעוצבים, נוצר כוח עילוי הגורם להם להסתובב (בדומה למפרש או כנף). תנועה סיבובית זו היא אנרגיה מכאנית. ציר הלהבים מסובב ציר נוסף בתוך הנאשל (לעיתים קרובות דרך תיבת הילוכים המגבירה את המהירות). הציר המהיר מסובב את הליבה המגנטית או הסלילים בתוך הגנרטור החשמלי. גנרטורים פועלים על פי עקרון האינדוקציה האלקטרומגנטית של פאראדיי: תנועה יחסית בין שדה מגנטי למוליך חשמלי (כמו חוטי נחושת) גורמת ליצירת זרם חשמלי - כלומר, חשמל!</p>

    <p><strong>כוחה של הרוח - וגם המגבלות:</strong> כמות החשמל שטורבינה מייצרת מושפעת דרמטית מ<strong>מהירות הרוח</strong>. תיאורטית, הכוח שניתן להפיק פרופורציונלי בערך ל<strong>חזקה השלישית</strong> של מהירות הרוח (v³). כלומר, הכפלת מהירות הרוח מכפילה את ההספק פי שמונה! זו הסיבה שמיקומן של טורבינות נבחר בקפידה באזורים עם רוחות חזקות ויציבות. בהדמיה תוכלו לראות כיצד הגדלת עוצמת הרוח מגדילה באופן משמעותי את ייצור החשמל.
    גורמים נוספים כוללים את קוטר הלהבים (שטח גדול יותר קולט יותר רוח) וצפיפות האוויר. חשוב גם לדעת שלטורבינות יש מגבלות: הן מתחילות לייצר חשמל רק במהירות רוח מינימלית (Cut-in speed) ומפסיקות לפעול במהירות רוח גבוהה מדי (Cut-out speed) כדי למנוע נזק.</p>

    <p><strong>אנרגיית רוח: עתיד ירוק יותר:</strong> אנרגיית רוח היא אחד ממקורות האנרגיה המתחדשים החשובים ביותר בעולם. היא נקייה, אינה פולטת מזהמים או גזי חממה, ומשאב הרוח עצמו בלתי נדלה. הפיתוח וההתייעלות של טורבינות הרוח הם צעד משמעותי במאבק בשינויי האקלים ובמעבר לעולם המונע על ידי אנרגיה בת קיימא.</p>
</div>

<style>
    body {
        font-family: 'Arial', sans-serif;
        margin: 0;
        padding: 20px;
        background-color: #f0f8ff; /* Light, pleasant background */
        color: #333;
        direction: rtl;
        text-align: right;
    }

    h1 {
        text-align: center;
        color: #004085; /* Dark blue */
        margin-bottom: 30px;
    }

    #wind-turbine-app {
        width: 100%;
        max-width: 700px; /* Slightly wider */
        margin: 20px auto;
        padding: 25px; /* More padding */
        border-radius: 15px; /* Softer corners */
        background: linear-gradient(to bottom, #b3e5fc, #81d4fa); /* Gradient sky */
        position: relative;
        overflow: hidden;
        height: 500px; /* Increased height */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 10px 20px rgba(0,0,0,0.15); /* Softer, larger shadow */
        border: none; /* Remove the basic border */
    }

    .sky {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 70%; /* Sky takes upper part */
        background: linear-gradient(to bottom, #87CEEB, #ADD8E6); /* Blue gradient */
        z-index: 0;
    }

    .ground {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 30%; /* Ground takes lower part */
        background: linear-gradient(to top, #A0D293, #C8E6C9); /* Green gradient */
        z-index: 0;
        border-top: 5px solid #558B2F; /* Darker green line */
    }

    .turbine-container {
        position: relative;
        width: 180px; /* Larger turbine */
        height: 300px; /* Taller */
        margin-bottom: 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 1; /* Ensure turbine is above ground/sky */
        margin-top: 30px; /* Push down from top */
    }

    .tower {
        width: 18px; /* Wider tower */
        height: 220px; /* Taller tower */
        background: linear-gradient(to top, #757575, #BDBDBD); /* Gray gradient */
        position: absolute;
        bottom: 0; /* Aligned to the bottom of turbine-container */
        left: 50%;
        transform: translateX(-50%);
        border-top-left-radius: 3px;
        border-top-right-radius: 3px;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.2);
    }

    .nacelle {
        width: 50px; /* Larger nacelle */
        height: 30px; /* Taller */
        background: linear-gradient(to right, #555, #777); /* Darker gray gradient */
        position: absolute;
        top: 210px; /* Position on top of the tower */
        left: 50%;
        transform: translateX(-50%);
        border-radius: 6px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.2);
        z-index: 2;
    }

    .blades {
        position: absolute;
        top: 225px; /* Center on the nacelle front */
        left: 50%;
        transform: translateX(-50%);
        width: 15px; /* Hub size */
        height: 15px; /* Hub size */
        background-color: #222; /* Hub color */
        border-radius: 50%;
        z-index: 3;
        transform-origin: 50% 50%; /* Center of rotation */
        box-shadow: 0 0 8px rgba(0,0,0,0.3);
    }

    .blade {
        width: 130px; /* Longer blade */
        height: 18px; /* Wider blade */
        background: linear-gradient(to right, #f0f0f0, #ddd); /* Light gray gradient */
        position: absolute;
        top: 50%;
        left: 50%;
        transform-origin: 0% 50%; /* Pivot at the hub edge */
        transform: translate(-7.5px, -9px); /* Adjust position to align pivot with hub edge */
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }

    .blade1 { transform: translate(-7.5px, -9px) rotate(0deg); }
    .blade2 { transform: translate(-7.5px, -9px) rotate(120deg); }
    .blade3 { transform: translate(-7.5px, -9px) rotate(240deg); }

    @keyframes rotateBlades {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    .blades.rotating {
        animation-name: rotateBlades;
        animation-timing-function: linear;
        animation-iteration-count: infinite;
        animation-play-state: running; /* Initially running if class is present */
    }

     .blades.rotating.paused {
        animation-play-state: paused;
     }


    .dashboard {
        width: 100%;
        display: flex;
        flex-direction: column; /* Stack controls and meters/power vertically */
        align-items: center;
        gap: 20px;
        z-index: 1; /* Above ground/sky */
    }

    .controls {
        display: flex;
        align-items: center;
        gap: 15px; /* More space */
        background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent background */
        padding: 10px 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .controls label {
        font-weight: bold;
        color: #004085;
    }

    #wind-speed-slider {
        width: 250px; /* Wider slider */
        -webkit-appearance: none; /* Remove default styles */
        appearance: none;
        height: 10px;
        background: linear-gradient(to right, #a8dadc, #457b9d); /* Gradient track */
        outline: none;
        opacity: 0.9;
        -webkit-transition: .2s;
        transition: opacity .2s;
        border-radius: 5px;
    }

    #wind-speed-slider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #1d3557; /* Dark blue thumb */
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    #wind-speed-slider::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #1d3557;
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    #wind-speed-value {
        font-weight: bold;
        color: #1d3557;
        min-width: 30px; /* Prevent text jumping */
        text-align: left;
    }

    .meters-power {
        display: flex;
        width: 100%;
        justify-content: space-around;
        gap: 15px; /* Space between meters and power bar */
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
    }

    .meters {
        display: flex;
        gap: 15px; /* Space between meters */
        flex-grow: 1; /* Allow meters to grow */
        justify-content: center; /* Center meters */
        flex-wrap: wrap;
    }

    .meter {
        text-align: center;
        font-size: 1.2em; /* Larger font */
        background-color: #fff;
        padding: 12px 18px; /* More padding */
        border-radius: 8px; /* Softer corners */
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        min-width: 120px; /* Minimum width */
    }

    .meter-label {
        font-size: 0.9em;
        color: #555;
        margin-bottom: 5px;
        font-weight: normal;
    }

    .meter-value {
         font-weight: bold;
         color: #007bff; /* Blue color for values */
    }


    .power-indicator {
        flex-grow: 2; /* Allow power indicator to take more space */
        min-width: 180px; /* Minimum width for power bar */
        background-color: rgba(255, 255, 255, 0.8);
        padding: 12px 18px;
        border-radius: 8px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .power-indicator .power-label {
        font-size: 0.9em;
        color: #555;
        margin-bottom: 8px;
        font-weight: normal;
    }

    .power-bar-container {
        width: 100%;
        height: 15px; /* Bar height */
        background-color: #eee; /* Empty bar color */
        border-radius: 8px;
        overflow: hidden; /* Hide overflow of the filling bar */
        border: 1px solid #ccc;
    }

    .power-bar {
        height: 100%;
        width: 0%; /* Start empty */
        background: linear-gradient(to right, #a4f0a4, #4CAF50); /* Green gradient for power */
        transition: width 0.3s ease-out; /* Smooth fill animation */
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);
    }


    #toggle-explanation {
        display: block;
        margin: 30px auto; /* More space above/below */
        padding: 12px 20px; /* More padding */
        font-size: 1.1em; /* Larger font */
        cursor: pointer;
        border: none;
        background-color: #007bff; /* Blue background */
        color: white;
        border-radius: 6px;
        transition: background-color 0.3s ease; /* Smooth hover */
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    #toggle-explanation:hover {
        background-color: #0056b3; /* Darker blue on hover */
    }

    #explanation {
        margin-top: 20px;
        padding: 20px; /* More padding */
        border: 1px solid #ddd;
        border-radius: 10px; /* Softer corners */
        background-color: #f9f9f9;
        text-align: right; /* Align text right for Hebrew */
        direction: rtl; /* Set direction right-to-left for Hebrew */
        line-height: 1.7; /* More comfortable reading */
        color: #444;
        box-shadow: 0 5px 10px rgba(0,0,0,0.08);
    }

    #explanation h2 {
        text-align: center;
        margin-top: 0;
        color: #004085;
        border-bottom: 2px solid #007bff;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

    #explanation p {
        margin-bottom: 18px;
    }

    #explanation strong {
        color: #0056b3; /* Darker blue for emphasis */
    }

     #explanation ul {
        margin-bottom: 18px;
        padding-right: 20px; /* Indent list */
     }

    /* Basic responsiveness */
    @media (max-width: 768px) {
        #wind-turbine-app {
            padding: 15px;
            height: 450px; /* Adjust height */
        }
         .turbine-container {
            width: 150px;
            height: 250px;
            margin-top: 20px;
         }
         .tower {
            width: 15px;
            height: 180px;
         }
         .nacelle {
            width: 40px;
            height: 25px;
             top: 170px;
         }
         .blades {
            top: 182.5px;
            width: 12px;
            height: 12px;
         }
         .blade {
            width: 100px;
            height: 15px;
             transform: translate(-6px, -7.5px);
         }
         .blade1 { transform: translate(-6px, -7.5px) rotate(0deg); }
         .blade2 { transform: translate(-6px, -7.5px) rotate(120deg); }
         .blade3 { transform: translate(-6px, -7.5px) rotate(240deg); }


        .dashboard {
            gap: 15px;
        }
        .controls {
            flex-direction: column;
            gap: 10px;
            padding: 8px 15px;
        }
        #wind-speed-slider {
             width: 80%;
        }
        .meters-power {
            flex-direction: column; /* Stack meters and power vertically */
            gap: 10px;
            align-items: center; /* Center stacked items */
        }
        .meters {
             gap: 10px;
             flex-direction: row; /* Keep meters side-by-side if space allows */
             flex-wrap: wrap; /* Allow wrap */
             justify-content: center;
        }
        .meter, .power-indicator {
            width: calc(50% - 10px); /* Adjust width for two items per row (nearly) */
             min-width: 140px;
        }
        .power-indicator {
            width: calc(100% - 30px); /* Power bar takes full width below meters */
             min-width: auto;
        }
    }

     @media (max-width: 480px) {
         .meter, .power-indicator {
            width: 100%; /* Stack all dashboard elements */
            min-width: auto;
         }
          .meters-power {
            gap: 10px;
          }
         .meters {
             flex-direction: column;
             gap: 10px;
         }
     }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const windSpeedSlider = document.getElementById('wind-speed-slider');
        const windSpeedValue = document.getElementById('wind-speed-value');
        const blades = document.querySelector('.blades');
        const powerMeter = document.getElementById('power-meter');
        const energyMeter = document.getElementById('energy-meter');
        const powerBar = document.getElementById('power-bar'); // Added
        const explanationDiv = document.getElementById('explanation');
        const toggleButton = document.getElementById('toggle-explanation');

        let currentWindSpeed = 0; // Slider value 0-100
        let currentPower = 0; // kW
        let accumulatedEnergy = 0; // kWh
        let animationInterval = null;
        const maxTheoreticalPower = 3000; // kW - A reasonable max power for a modern turbine
        // Power output is proportional to the cube of wind speed (v^3)
        // Let's scale power based on slider value (0-100) as a proxy for wind speed
        const powerScaleFactor = maxTheoreticalPower / Math.pow(100, 3); // Power = scale * (slider value)^3
        const updateIntervalMs = 200; // Update interval in milliseconds (slightly slower for energy accum)
        const intervalHours = updateIntervalMs / (1000 * 3600); // Interval in hours

        // Mapping slider value (0-100) to animation duration (seconds)
        // Higher slider value -> shorter duration -> faster rotation
        // Use a non-linear mapping for better feel at low speeds
        const maxAnimDuration = 30; // seconds (slowest rotation)
        const minAnimDuration = 0.3; // seconds (fastest rotation)

        function updateTurbineAndMeters() {
            // Calculate power using cubic relationship
            // Add a small threshold or offset to make low wind (>0) generate *some* power visually
            let effectiveWindSpeed = Math.max(0, currentWindSpeed - 5); // Assume cut-in speed around 5%
            if (currentWindSpeed === 0) effectiveWindSpeed = 0;


            currentPower = powerScaleFactor * Math.pow(effectiveWindSpeed, 3);

            // Clamp power if it somehow exceeds max (shouldn't with 100 as max slider)
            currentPower = Math.min(currentPower, maxTheoreticalPower);

            // Update Power Meter display
            powerMeter.textContent = `${currentPower.toFixed(2)} kW`;

            // Update Power Bar visualization (as a percentage of max theoretical power)
            const powerPercentage = (currentPower / maxTheoreticalPower) * 100;
            powerBar.style.width = `${powerPercentage}%`;

            // Accumulate energy
            // Only accumulate if power is above a minimal threshold to avoid tiny numbers
            if (currentPower > 0.1) { // Accumulate if power is above 100W
                 accumulatedEnergy += currentPower * intervalHours; // Energy = Power * Time
                 energyMeter.textContent = `${accumulatedEnergy.toFixed(2)} kWh`;
            } else if (currentWindSpeed === 0) {
                 // If wind truly stops, accumulated energy should stay, but power resets
                 energyMeter.textContent = `${accumulatedEnergy.toFixed(2)} kWh`; // Keep displaying total
            }


            // Update turbine rotation speed based on actual wind speed (0-100)
            // The mapping is inverse: higher speed -> lower duration
            if (currentWindSpeed > 0) {
                 // Map speed 1-100 to duration from maxAnimDuration down to minAnimDuration
                 const rotationDuration = maxAnimDuration - (currentWindSpeed / 100) * (maxAnimDuration - minAnimDuration);
                 blades.style.animationDuration = `${rotationDuration}s`;
                 blades.classList.add('rotating');
                 blades.classList.remove('paused'); // Ensure animation is running
            } else {
                 // Stop animation when speed is zero
                 blades.classList.remove('rotating');
                 blades.classList.add('paused'); // Explicitly pause
                 blades.style.animationDuration = '0s'; // Reset duration property explicitly
                 powerMeter.textContent = '0.00 kW'; // Reset power display
                 powerBar.style.width = '0%'; // Reset power bar
            }
        }

        function startUpdating() {
             if (animationInterval === null) {
                // Run updateTurbineAndMeters periodically to update meters and energy
                animationInterval = setInterval(updateTurbineAndMeters, updateIntervalMs);
                 // The function itself manages the CSS animation state
             }
        }

        function stopUpdating() {
            if (animationInterval !== null) {
                clearInterval(animationInterval);
                animationInterval = null;
            }
             // Ensure visual state reflects stop immediately
             blades.classList.remove('rotating');
             blades.classList.add('paused');
             blades.style.animationDuration = '0s';
             currentPower = 0; // Reset power conceptually for display
             powerMeter.textContent = '0.00 kW';
             powerBar.style.width = '0%';
             // Accumulated energy stays as is when stopped
        }


        // Slider event listener
        windSpeedSlider.addEventListener('input', (event) => {
            currentWindSpeed = parseInt(event.target.value, 10);
            windSpeedValue.textContent = currentWindSpeed;

            // Update meters and animation speed immediately on slider change
            updateTurbineAndMeters();

            // Start/stop the periodic updates based on wind speed
            if (currentWindSpeed > 0) {
                startUpdating();
            } else {
                stopUpdating();
            }
        });

        // Toggle explanation visibility
        toggleButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleButton.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'הצג הסבר מעמיק';
        });

        // Initial state setup on load
        windSpeedValue.textContent = windSpeedSlider.value; // Should be 0 initially
        updateTurbineAndMeters(); // Set initial meter values (should be 0) and animation state (paused)
        stopUpdating(); // Ensure interval is off and visuals are reset at the start

    });
</script>