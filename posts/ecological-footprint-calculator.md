---
title: "מחשבון טביעת רגל אקולוגית - המדריך האינטראקטיבי"
english_slug: ecological-footprint-calculator
category: "כללי"
tags:
  - סביבה
  - אקולוגיה
  - קיימות
  - צריכה
---
# טביעת הרגל האקולוגית שלך: כמה כדור הארץ "עולה" לך?

כל החלטה קטנה בחיי היומיום שלנו מותירה חותם על הפלנטה. מבחירת המזון שאנחנו אוכלים, דרך האופן שבו אנחנו מתנייעים, ועד כמות הדברים שאנחנו רוכשים - לכל פעולה יש השפעה. האם אתה מוכן לגלות מהי טביעת הרגל האקולוגית *שלך* ולראות איך היא משפיעה על כדור הארץ בקנה מידה גדול?

השתמש בסליידרים למטה כדי לבחור את סגנון הצריכה שלך וגלה מיד את התוצאה.

<div class="calculator-container">
    <div class="input-section">
        <h2>התאם את אורח החיים שלך:</h2>
        <div class="input-group">
            <label for="energy">צריכת אנרגיה בבית:</label>
            <div class="slider-control">
                <span class="value-label" id="energy-value">3</span>
                <input type="range" id="energy" min="1" max="5" value="3">
            </div>
            <p class="hint">1 - מינימום צריכה, חיסכון מירבי / 5 - צריכה גבוהה, שימוש אינטנסיבי</p>
        </div>
        <div class="input-group">
            <label for="transport">אופן נסיעה עיקרי:</label>
             <div class="slider-control">
                 <span class="value-label" id="transport-value">3</span>
                 <input type="range" id="transport" min="1" max="5" value="3">
             </div>
            <p class="hint">1 - הליכה, אופניים, תחבורה ציבורית יעילה / 5 - רכב פרטי מזהם, טיסות תכופות</p>
        </div>
        <div class="input-group">
            <label for="diet">סוג תזונה:</label>
             <div class="slider-control">
                <span class="value-label" id="diet-value">3</span>
                <input type="range" id="diet" min="1" max="5" value="3">
             </div>
            <p class="hint">1 - טבעוני, מקומי, עונתי / 5 - בשרי בכמויות גדולות, הרבה מוצרי יבוא</p>
        </div>
        <div class="input-group">
            <label for="goods">צריכת מוצרים וקניות:</label>
             <div class="slider-control">
                <span class="value-label" id="goods-value">3</span>
                <input type="range" id="goods" min="1" max="5" value="3">
             </div>
            <p class="hint">1 - מינימליסטי, יד שנייה, תיקונים / 5 - קניות רבות, מוצרים מתכלים, אופנה מהירה</p>
        </div>
        <!-- Button kept for structure, but calculation is live -->
        <button id="calculate-btn">עדכן טביעת רגל</button>
    </div>
    <div class="output-section">
        <h2>החותם שלך על הכדור:</h2>
        <div id="footprint-bar-container">
            <div id="footprint-bar">
                <span id="footprint-level-text">...</span>
            </div>
        </div>
        <p id="footprint-description"></p>
         <p id="planets-needed"></p>
    </div>
</div>

<style>
    /* Custom Properties for easier theme management */
    :root {
        --primary-color: #3498db; /* Blue */
        --secondary-color: #2ecc71; /* Green */
        --warning-color: #f1c40f; /* Yellow */
        --danger-color: #e74c3c; /* Red */
        --orange-color: #e67e22; /* Orange */
        --background-color: #ecf0f1; /* Light gray-blue */
        --surface-color: #ffffff; /* White */
        --text-color: #2c3e50; /* Dark blue */
        --text-light-color: #7f8c8d; /* Gray */
        --border-radius: 8px;
        --box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        --transition-speed: 0.5s ease-in-out;
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        color: var(--text-color);
        direction: rtl;
        text-align: right;
        margin: 0;
        padding: 20px;
        background-color: var(--background-color);
        overflow-x: hidden; /* Prevent horizontal scroll */
    }

    h1, h2 {
        color: var(--text-color);
        text-align: center;
        margin-bottom: 20px;
    }

    h1 {
         font-size: 2.2em;
         margin-bottom: 30px;
    }

    h2 {
        font-size: 1.6em;
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

    p {
        margin-bottom: 15px;
    }

    .calculator-container {
        display: flex;
        flex-wrap: wrap;
        gap: 40px;
        max-width: 1000px;
        margin: 30px auto;
        background-color: var(--surface-color);
        padding: 40px;
        border-radius: var(--border-radius);
        box-shadow: var(--box-shadow);
        animation: fadeIn 1s ease-out;
    }

     @keyframes fadeIn {
         from { opacity: 0; transform: translateY(20px); }
         to { opacity: 1; transform: translateY(0); }
     }

    .input-section, .output-section {
        flex: 1;
        min-width: 320px; /* Increased min-width for better layout on tablets */
    }

    .input-section {
        border-left: 1px solid #eee; /* Subtle visual separator */
        padding-left: 40px;
         box-sizing: border-box; /* Include padding in width */
    }
    .output-section {
        padding-right: 40px; /* Match padding */
         box-sizing: border-box;
        display: flex;
        flex-direction: column;
        justify-content: center; /* Vertically center content */
        align-items: center; /* Horizontally center content */
        text-align: center;
    }

     /* Adjust padding/border on smaller screens */
    @media (max-width: 768px) {
        .input-section, .output-section {
            padding: 0;
            border-left: none;
        }
        .input-section {
             margin-bottom: 30px;
             border-bottom: 1px solid #eee;
             padding-bottom: 30px;
        }
        .calculator-container {
            padding: 20px;
        }
         h1 { font-size: 1.8em; }
         h2 { font-size: 1.4em; }
    }


    .input-group {
        margin-bottom: 30px; /* Increased spacing */
        padding: 20px; /* Increased padding */
        background-color: var(--background-color);
        border-radius: var(--border-radius);
        border-right: 5px solid var(--primary-color); /* Border on the right for RTL */
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

     .input-group:hover {
         transform: translateY(-5px);
         box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
     }

    .input-group label {
        display: block;
        margin-bottom: 12px; /* Increased spacing */
        font-weight: bold;
        color: var(--text-color);
        font-size: 1.1em;
    }

    .slider-control {
         display: flex;
         align-items: center;
         gap: 15px; /* Space between label and slider */
    }

    .input-group input[type="range"] {
        flex-grow: 1; /* Slider takes available space */
        -webkit-appearance: none; /* Override default slider appearance */
        appearance: none;
        height: 10px;
        background: #d3d3d3;
        outline: none;
        opacity: 0.7;
        transition: opacity var(--transition-speed);
        border-radius: 5px;
    }

    .input-group input[type="range"]:hover {
        opacity: 1;
    }

     /* Thumb styling */
    .input-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        transition: background var(--transition-speed), transform 0.2s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    .input-group input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        cursor: pointer;
        border-radius: 50%;
        transition: background var(--transition-speed), transform 0.2s ease;
         box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    .input-group input[type="range"]:active::-webkit-slider-thumb {
        transform: scale(1.2);
    }

     .input-group input[type="range"]:active::-moz-range-thumb {
        transform: scale(1.2);
    }

    .value-label {
         display: inline-block;
         min-width: 30px; /* Ensure space for 1-5 */
         text-align: center;
         font-weight: bold;
         color: var(--primary-color);
         font-size: 1.2em;
         vertical-align: middle;
         transition: color var(--transition-speed);
    }

    .hint {
        font-size: 0.9em;
        color: var(--text-light-color);
        margin-top: 8px; /* Increased spacing */
        line-height: 1.5;
    }

    #calculate-btn {
        display: block;
        width: 100%;
        padding: 14px; /* Increased padding */
        background-color: var(--secondary-color);
        color: white;
        border: none;
        border-radius: var(--border-radius);
        font-size: 1.2em; /* Increased font size */
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        margin-top: 20px;
        font-weight: bold;
         letter-spacing: 0.5px;
    }

    #calculate-btn:hover {
        background-color: #27ae60; /* Darker green */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }

    #calculate-btn:active {
        transform: scale(0.98);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    #footprint-bar-container {
        width: 90%; /* Adjusted width */
        max-width: 400px; /* Max width for bar */
        height: 50px; /* Increased height */
        background-color: #bdc3c7; /* Light gray background */
        border-radius: 25px; /* Half of height for rounded ends */
        margin: 30px auto; /* Centered with margin */
        overflow: hidden;
        position: relative;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.1); /* Inner shadow for depth */
    }

    #footprint-bar {
        height: 100%;
        width: 0%; /* Initial width */
        border-radius: 25px;
        transition: width var(--transition-speed), background-color var(--transition-speed);
        display: flex;
        align-items: center;
        justify-content: center; /* Center text horizontally */
        color: white;
        font-weight: bold;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.3); /* Stronger shadow for readability */
        font-size: 1.3em;
         position: absolute; /* Allow text to be inside bar */
         top: 0;
         left: 0; /* Bar fills from the right in RTL, needs left:0? Let's test this */
         /* RTL consideration: width increases leftward. Needs careful positioning or text handling */
         /* Alternative: text outside bar but centered above/below */
         /* Let's keep text inside and manage color/position via JS if needed */
    }
     #footprint-bar[style*="width: 0"] #footprint-level-text {
         display: none; /* Hide text when bar is empty */
     }


     #footprint-level-text {
         position: absolute;
         top: 50%;
         left: 50%; /* Center within container */
         transform: translate(-50%, -50%); /* Perfect centering */
         font-size: 1.3em;
         font-weight: bold;
         color: var(--text-color); /* Default color */
         z-index: 2; /* Ensure text is above bar */
         transition: color var(--transition-speed);
         text-shadow: 1px 1px 3px rgba(255,255,255,0.5); /* Shadow for dark text on light bg */
     }

     /* Style text differently when it's over the colored bar */
     #footprint-bar[style*="width:"] > #footprint-level-text {
         color: white; /* White text on colored bar */
         text-shadow: 1px 1px 3px rgba(0,0,0,0.3); /* Dark shadow for light text on dark bg */
     }


    #footprint-description {
        margin-top: 20px;
        font-size: 1.1em;
        color: #555;
        min-height: 4em; /* Reserve more space */
        transition: opacity var(--transition-speed);
        text-align: center;
    }
     #planets-needed {
        margin-top: 10px;
        font-size: 1.1em;
        font-weight: bold;
        color: var(--text-color);
        min-height: 1.5em;
         transition: opacity var(--transition-speed);
         text-align: center;
     }


    .explanation-button {
        display: block;
        margin: 40px auto; /* More space */
        padding: 12px 25px; /* More padding */
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: var(--border-radius);
        font-size: 1.1em;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        font-weight: bold;
    }

    .explanation-button:hover {
        background-color: #2980b9; /* Darker blue */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }
    .explanation-button:active {
        transform: scale(0.98);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }


    .explanation-content {
        display: none; /* Hidden by default */
        margin-top: 20px;
        padding: 30px; /* More padding */
        background-color: var(--background-color);
        border-radius: var(--border-radius);
        border: 1px solid #bdc3c7;
        line-height: 1.8;
        max-width: 900px;
        margin: 20px auto;
        animation: slideDown 0.5s ease-out;
    }

    @keyframes slideDown {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .explanation-content h3 {
        color: var(--text-color);
        margin-top: 0;
        margin-bottom: 15px;
    }

    .explanation-content p {
        margin-bottom: 15px;
    }

    .explanation-content strong {
        color: var(--primary-color);
    }

</style>

<button class="explanation-button" id="toggle-explanation">מהי טביעת רגל אקולוגית? (לחץ להסבר)</button>

<div class="explanation-content" id="explanation">
    <h3>מהי טביעת רגל אקולוגית ומדוע היא חשובה?</h3>
    <p>טביעת רגל אקולוגית היא למעשה המדד לשטח כדור הארץ (יבשה וימים) הדרוש כדי לקיים את אורח החיים של אדם, קהילה, או אומה שלמה. היא כוללת את השטח הדרוש לייצור המזון, אספקת האנרגיה, יערות לקליטת פחמן דו-חמצני, ועוד. המדד הזה מאפשר לנו להבין כמה משאבים אנחנו צורכים ומהי ההשפעה שלנו על המערכות הטבעיות של כדור הארץ.</p>
    <p>המחשבון הפשוט שבו השתמשת למעלה מדגים את הקשר בין מספר בחירות יומיומיות מרכזיות (צריכת אנרגיה, תחבורה, תזונה, וקניית מוצרים) לבין טביעת הרגל האקולוגית המשוערת. ככל שהערכים שאתה בוחר גבוהים יותר, כך טביעת הרגל גדולה יותר – מה שמעיד על צריכה משאבים גבוהה יותר ויצירת יותר פסולת ופליטות.</p>
    <p><strong>הנתון המדאיג:</strong> הקיבולת האקולוגית של כדור הארץ – היכולת שלו לספק משאבים ולקלוט פסולת באופן בר-קיימא – קטנה מטביעת הרגל האקולוגית הקולקטיבית של האנושות. המשמעות היא שאנחנו צורכים משאבים מהר יותר מכפי שכדור הארץ יכול לחדש אותם. כדי לקיים את אורח החיים הנוכחי של כל האנושות, אנו זקוקים כיום לשטח ששווה ערך לכ-<strong>1.7 כדורי ארץ</strong>. אם כל בני האדם בעולם היו חיים כמו האדם הממוצע באזורים הצורכים ביותר (כמו בישראל או בארה"ב), היינו זקוקים למספר כדורי ארץ גדול הרבה יותר!</p>
    <p>המטרה היא לצמצם את טביעת הרגל האקולוגית האישית והגלובלית שלנו כדי להגיע לאיזון עם יכולות ההתחדשות של כדור הארץ. כל בחירה מקיימת חשובה.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // Select all sliders and value labels
        const sliders = document.querySelectorAll('.input-group input[type="range"]');
        const valueLabels = document.querySelectorAll('.value-label');
        const calculateBtn = document.getElementById('calculate-btn'); // Keep button reference
        const footprintBar = document.getElementById('footprint-bar');
        const footprintLevelText = document.getElementById('footprint-level-text');
        const footprintDescription = document.getElementById('footprint-description');
         const planetsNeededText = document.getElementById('planets-needed'); // New element for planets
        const toggleExplanationBtn = document.getElementById('toggle-explanation');
        const explanationContent = document.getElementById('explanation');

        // Map sliders to their value labels
        const sliderValueMap = {};
        sliders.forEach(slider => {
            sliderValueMap[slider.id] = document.getElementById(`${slider.id}-value`);
        });

        // Function to update value labels
        const updateValueLabels = () => {
            sliders.forEach(slider => {
                sliderValueMap[slider.id].textContent = slider.value;
            });
        };

        // Function to calculate and display footprint
        const calculateFootprint = () => {
            let totalFootprintValue = 0;
            sliders.forEach(slider => {
                totalFootprintValue += parseInt(slider.value);
            });

            // Map totalFootprintValue to a percentage (0-100%) for the bar
            // Min total = 4 (1+1+1+1), Max total = 20 (5+5+5+5)
            // Range size = 20 - 4 = 16
            // Percentage = ((total - min) / range) * 100
            const minTotal = 4;
            const maxTotal = 20;
            const percentage = ((totalFootprintValue - minTotal) / (maxTotal - minTotal)) * 100;

            // Update bar width and color with transition
            footprintBar.style.width = `${percentage}%`;

            let barColor, levelText, description, planetsText;

            // Define levels and corresponding texts/colors
            if (percentage < 20) { // More granular levels
                barColor = var_primary_color; // Using CSS variable via JS is tricky, fallback to hex or map explicitly
                barColor = '#2ecc71'; // Green (very low)
                levelText = 'נמוכה מאוד';
                description = 'כל הכבוד! טביעת הרגל האקולוגית שלך מינימלית. אורח החיים שלך קל מאוד על כדור הארץ.';
                 planetsText = 'אם כולם היו חיים כמוך, היינו צריכים פחות מכדור ארץ אחד.';
            } else if (percentage < 40) {
                 barColor = '#9b59b6'; // Amethyst (low)
                 levelText = 'נמוכה';
                 description = 'טביעת הרגל שלך נמוכה. סגנון החיים שלך תומך בקיימות בצורה טובה!';
                 planetsText = 'אם כולם היו חיים כמוך, היינו צריכים בערך כדור ארץ אחד.';
            } else if (percentage < 60) {
                barColor = '#f1c40f'; // Yellow (medium)
                levelText = 'בינונית';
                description = 'טביעת הרגל שלך בינונית. זה המצב של אנשים רבים, ויש הזדמנות מצוינת לשפר ולהפחית את ההשפעה.';
                planetsText = 'אם כולם היו חיים כמוך, היינו צריכים בערך 1.5 כדורי ארץ.';
            } else if (percentage < 80) {
                 barColor = '#e67e22'; // Orange (high)
                 levelText = 'גבוהה';
                 description = 'טביעת הרגל שלך גבוהה יחסית. צריכה גבוהה יותר דורשת משאבים רבים מכדור הארץ. שינויים קטנים יכולים לעשות הבדל גדול.';
                 planetsText = 'אם כולם היו חיים כמוך, היינו צריכים בערך 2 כדורי ארץ.';
            }
             else {
                barColor = '#e74c3c'; // Red (very high)
                levelText = 'גבוהה מאוד';
                description = 'טביעת הרגל האקולוגית שלך גבוהה מאוד. סגנון חיים כזה דורש משאבים עצומים ומכביד מאוד על כדור הארץ. שקול לבחון אפשרויות לצמצום הצריכה.';
                 planetsText = 'אם כולם היו חיים כמוך, היינו צריכים הרבה מעל 2 כדורי ארץ!';
            }

            footprintBar.style.backgroundColor = barColor;
            footprintLevelText.textContent = levelText;
             // Position text - always centered
             footprintLevelText.style.left = '50%';
             footprintLevelText.style.transform = 'translate(-50%, -50%)';
            // Ensure text color contrast (handled via CSS now with text-shadow)

            footprintDescription.textContent = description;
             planetsNeededText.textContent = planetsText;

             // Fade in results text
             footprintDescription.style.opacity = 0;
             planetsNeededText.style.opacity = 0;
             setTimeout(() => {
                 footprintDescription.style.opacity = 1;
                  planetsNeededText.style.opacity = 1;
             }, 500); // Delay fade-in slightly after bar animation starts

        };

        // Add event listeners for live updates and label updates
        sliders.forEach(slider => {
            slider.addEventListener('input', () => {
                updateValueLabels();
                calculateFootprint(); // Calculate and update results live
            });
        });

         // Although calculation is live, keep button listener for redundancy or if structure requires it
         // calculateBtn.addEventListener('click', calculateFootprint);

        // Initial update on page load
        updateValueLabels();
        calculateFootprint();

        // Toggle explanation visibility
        toggleExplanationBtn.addEventListener('click', () => {
            const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
            explanationContent.style.display = isHidden ? 'block' : 'none';
            toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר' : 'מהי טביעת רגל אקולוגית? (לחץ להסבר)';
             // Scroll to explanation when shown
             if (isHidden) {
                 explanationContent.scrollIntoView({ behavior: 'smooth', block: 'start' });
             }
        });

         // Ensure initial state is correct (explanation hidden)
         explanationContent.style.display = 'none'; // Explicitly hide on load

    });
</script>