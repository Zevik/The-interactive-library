---
title: "מים מתאזנים בכלים שונים: סוד הכלים השלובים"
english_slug: water-leveling-different-vessels-communicating-vessels-secret
category: "מדעים מדויקים / פיזיקה"
tags: ["זורמים", "לחץ", "כלים שלובים", "עקרון פסקל", "הידרוסטטיקה"]
---
# גלו את הקסם של כלים שלובים: האם המים תמיד מתאזנים?

הסתכלו סביבכם – במגדל המים בעיר, בבית, ואפילו בתעלות שיט עתיקות. כולם משתמשים בעקרון פיזיקלי פשוט אך מדהים: כלים שלובים. נראה יחד כיצד הנוזל מתנהג במערכת מחוברת של כלים, גם אם הם נראים שונים לחלוטין.

<div class="app-container">
    <div class="vessels-system">
        <div class="pipe-connector"></div> <!-- Visual pipe connecting the bases -->

        <!-- Vessel 1: Straight Cylinder -->
        <div class="vessel-group">
             <div class="vessel straight">
                 <div class="water"></div>
                 <div class="vessel-border"></div>
             </div>
             <div class="vessel-label">גליל</div>
        </div>

        <!-- Vessel 2: Inverted Cone suggestion -->
        <div class="vessel-group">
             <div class="vessel narrow-bottom">
                 <div class="water"></div>
                 <div class="vessel-border"></div>
             </div>
             <div class="vessel-label">חרוט הפוך</div>
         </div>

         <!-- Vessel 3: Wide Cylinder -->
        <div class="vessel-group">
             <div class="vessel wide">
                 <div class="water"></div>
                 <div class="vessel-border"></div>
             </div>
             <div class="vessel-label">רחב</div>
         </div>

         <!-- Vessel 4: Short Curved -->
        <div class="vessel-group">
             <div class="vessel curved">
                 <div class="water"></div>
                 <div class="vessel-border"></div>
             </div>
             <div class="vessel-label">מעוקל קצר</div>
         </div>

         <!-- Vessel 5: Narrow Cylinder -->
        <div class="vessel-group">
             <div class="vessel narrow">
                 <div class="water"></div>
                 <div class="vessel-border"></div>
             </div>
             <div class="vessel-label">צר</div>
         </div>

         <!-- Vessel 6: Tall Curved (U-tube suggestion) -->
        <div class="vessel-group">
             <div class="vessel curved-tall">
                 <div class="water"></div>
                 <div class="vessel-border"></div>
             </div>
             <div class="vessel-label">מעוקל גבוה</div>
         </div>

    </div>
    <div class="controls">
        <label for="water-level-slider">שליטה בכמות המים:</label>
        <input type="range" id="water-level-slider" min="0" max="100" value="30">
        <span id="water-percentage-label">30%</span>
    </div>
</div>

<style>
    /* Add a modern, clean font */
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    .app-container {
        direction: rtl;
        font-family: 'Heebo', sans-serif;
        margin: 20px auto;
        padding: 20px 30px; /* More padding */
        border: none; /* Remove basic border */
        border-radius: 12px; /* Softer corners */
        max-width: 850px; /* Wider container */
        background-color: #ffffff; /* Clean white background */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        overflow: hidden; /* Keep everything inside */
    }

    .vessels-system {
        display: flex;
        align-items: flex-end; /* Align bases */
        justify-content: center;
        gap: 15px; /* More space between vessels */
        height: 250px; /* Taller system display */
        position: relative;
        margin-bottom: 30px; /* Space below system */
        padding-bottom: 30px; /* Space for pipe connection below */
    }

    .pipe-connector {
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 95%; /* Spans across vessels */
        height: 25px; /* Pipe height */
        background-color: #ccc; /* Pipe color */
        border-radius: 8px;
        z-index: 1; /* Below vessels */
        box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.2);
    }

    .vessel-group {
        display: flex;
        flex-direction: column;
        align-items: center;
        position: relative;
        z-index: 2; /* Vessels above pipe */
        flex-shrink: 0; /* Prevent shrinking */
    }

    .vessel {
        display: flex;
        flex-direction: column-reverse; /* Water fills from bottom */
        width: 60px; /* Default width */
        height: 180px; /* Max fillable height above pipe */
        position: relative;
        overflow: hidden; /* Hide water exceeding vessel bounds */
        box-sizing: border-box;
        border-radius: 6px 6px 0 0; /* Softer top corners */
        background-color: rgba(170, 170, 170, 0.2); /* Soft vessel background */
        margin-bottom: -10px; /* Overlap with pipe */
        pointer-events: none; /* Don't interfere with events */
    }

    .vessel-border {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: 2px solid rgba(100, 100, 100, 0.3); /* Visual border */
        border-bottom: none;
        border-radius: 6px 6px 0 0;
        box-sizing: border-box;
        pointer-events: none; /* Border doesn't block clicks */
    }


     .vessel-label {
        position: absolute; /* Position relative to vessel-group */
        bottom: -28px; /* Place below the vessel and pipe */
        width: 100%;
        text-align: center;
        font-size: 0.9em; /* Slightly larger font */
        color: #555;
        font-weight: 400;
     }


    /* Specific vessel shapes and styles */
    .vessel.straight {
        width: 70px;
    }

    .vessel.narrow-bottom {
        width: 80px;
        clip-path: polygon(5% 100%, 25% 0%, 75% 0%, 95% 100%); /* Smoother trapezoid */
        background-color: rgba(170, 170, 170, 0.2); /* Maintain background */
         border-radius: 6px 6px 0 0;
    }
     .vessel.narrow-bottom .vessel-border {
         clip-path: polygon(5% 100%, 25% 0%, 75% 0%, 95% 100%);
          border: 2px solid rgba(100, 100, 100, 0.3);
          border-bottom: none;
     }


    .vessel.wide {
       width: 100px;
    }

     .vessel.curved {
        width: 80px;
        height: 120px; /* Shorter vessel */
        border-radius: 40px 40px 0 0; /* More pronounced curve suggestion */
        clip-path: polygon(0% 100%, 0% 15%, 15% 0%, 85% 0%, 100% 15%, 100% 100%); /* Suggest curve */
         background-color: rgba(170, 170, 170, 0.2);
         border-radius: 6px 6px 0 0; /* Keep top corners consistent */
    }
     .vessel.curved .vessel-border {
         clip-path: polygon(0% 100%, 0% 15%, 15% 0%, 85% 0%, 100% 15%, 100% 100%);
          border: 2px solid rgba(100, 100, 100, 0.3);
          border-bottom: none;
     }


     .vessel.narrow {
        width: 50px;
    }

     .vessel.curved-tall {
        width: 60px;
         height: 180px; /* Height above bend */
          background-color: rgba(170, 170, 170, 0.2);
          border-radius: 6px 6px 0 0;
          /* Represent the bend visually below */
         position: relative;
         margin-bottom: -30px; /* Overlap with pipe */
         padding-bottom: 30px; /* Visual space for bend */
         overflow: visible; /* Allow bend part to render below */
    }
     .vessel.curved-tall .water {
         position: absolute;
         bottom: 30px; /* Water starts filling from the "bend" line */
         left: 0;
         right: 0;
         height: 0; /* Initial height */
         background: linear-gradient(to top, rgba(0, 123, 255, 0.8), rgba(0, 180, 255, 0.8)); /* Gradient water */
         transition: height 1s ease-in-out; /* Smoother animation */
         border-radius: 0 0 4px 4px; /* Slight curve at bottom of water column */
     }
      .vessel.curved-tall .vessel-border {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%; /* Height above bend */
         border: 2px solid rgba(100, 100, 100, 0.3);
         border-bottom: none;
         border-radius: 6px 6px 0 0;
         box-sizing: border-box;
         pointer-events: none;
     }
     /* Add the visual bend part for curved-tall */
     .vessel.curved-tall::after {
        content: '';
        position: absolute;
        bottom: 0; /* Position below the main vessel part */
        left: calc(50% - 30px); /* Centered below */
        width: 60px;
        height: 30px; /* Height of the bend */
        border: 2px solid rgba(100, 100, 100, 0.3);
        border-top: none;
        border-radius: 0 0 30px 30px; /* U shape */
        background-color: rgba(170, 170, 170, 0.2);
        z-index: -1; /* Behind vessel border */
        box-sizing: border-box;
     }


    .water {
        width: 100%;
        height: 0; /* Starts empty */
        background: linear-gradient(to top, rgba(0, 123, 255, 0.8), rgba(0, 180, 255, 0.8)); /* Blue gradient water */
        position: absolute;
        bottom: 0; /* Standard vessels fill from bottom 0 */
        left: 0;
        transition: height 1s ease-in-out; /* Smooth, slightly slower transition */
        border-radius: 0 0 4px 4px; /* Slight curve at bottom of water column */
    }

    /* Adjustments for vessels that use clip-path or special shapes */
    .vessel.narrow-bottom .water,
    .vessel.curved .water {
         left: 0;
         right: 0;
         bottom: 0;
         height: 0;
         position: absolute;
         background: linear-gradient(to top, rgba(0, 123, 255, 0.8), rgba(0, 180, 255, 0.8));
         transition: height 1s ease-in-out;
         border-radius: 0 0 4px 4px;
    }

    .controls {
        text-align: center;
        margin-top: 20px;
        padding: 15px;
        background-color: #eee; /* Light background for controls */
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
    }

    .controls label {
        font-weight: bold;
        color: #333;
    }

    #water-level-slider {
        flex-grow: 1; /* Slider takes available space */
        max-width: 400px;
        cursor: grab; /* Indicate drag-ability */
        /* Basic custom slider styling */
        -webkit-appearance: none;
        appearance: none;
        height: 8px;
        background: #ddd;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 4px;
    }

    #water-level-slider:hover {
        opacity: 1;
    }

    #water-level-slider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

     #water-level-slider::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    #water-percentage-label {
        font-weight: bold;
        color: #007bff;
        min-width: 40px; /* Reserve space */
        text-align: left;
    }


    #toggleExplanation {
        display: block;
        margin: 30px auto; /* More space */
        padding: 12px 25px; /* Larger button */
        font-size: 1.1em;
        cursor: pointer;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 6px;
        text-align: center;
        transition: background-color 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
    }

    #toggleExplanation:hover {
        background-color: #0056b3;
    }

    #explanation {
        margin-top: 30px;
        padding-top: 30px;
        border-top: 1px solid #eee;
        display: none; /* Hidden by default */
        line-height: 1.7; /* Improved readability */
        color: #333;
    }

    #explanation h2 {
        color: #0056b3; /* Matching button color */
        margin-top: 20px;
        margin-bottom: 10px;
        font-weight: 700;
        font-size: 1.4em;
    }

    #explanation p {
        margin-bottom: 15px;
    }

    #explanation ul {
        list-style-type: disc;
        margin-left: 25px; /* More indent */
        padding-left: 0;
    }

    #explanation li {
        margin-bottom: 10px;
    }

    #explanation strong {
        color: #000; /* Stronger black */
    }

</style>

<button id="toggleExplanation">הסבר על כלים שלובים</button>

<div id="explanation">
    <h2>מהם בעצם "כלים שלובים"?</h2>
    <p>דמיינו אוסף של בקבוקים או כלי קיבול שונים לגמרי בצורתם – גלילי, חרוטי, רחב, צר, ואפילו בצורת האות U – כולם מחוברים יחד בחלקם התחתון, כמו צינור משותף. כשתמזגו נוזל (כמו מים) למערכת כזו, יקרה דבר מופלא: הנוזל יזרום ויתאזן עד שמפלסו יהיה זהה בכל אחד מהכלים המחוברים. וזה נכון תמיד, בלי קשר לצורת הכלי או לכמות הנוזל שמזגתם (כל עוד יש מספיק נוזל בכלים).</p>

    <h2>תצפית מרתקת: מפלס המים תמיד שווה</h2>
    <p>כפי שראיתם בסימולציה למעלה, כששיניתם את כמות המים במערכת, המים הסתדרו מחדש. הם לא התמלאו גבוה יותר בכלי הצר או נמוך יותר בכלי הרחב. בכל הכלים שהכילו מים, גובה פני המים היה **אחיד לחלוטין**. מדוע זה קורה?</p>

    <h2>הסוד הפיזיקלי נחשף: לחץ, עומק ושיווי משקל</h2>
    <p>התופעה המפתיעה הזו נובעת משילוב של עקרונות פיזיקליים:</p>
    <ul>
        <li><strong>כוח הכבידה: הנטייה הטבעית מטה</strong>
            <br>כמו כל דבר בעל מסה, גם נוזלים מושפעים מכוח הכבידה שמושך אותם מטה. בכלי סגור או חלקי, הכבידה "מכריחה" את הנוזל למלא את החלקים הנמוכים ביותר ולהתפשט לרוחב ככל האפשר.</li>
        <li><strong>לחץ הידרוסטטי: כובד הנוזל הדוחף</strong>
            <br>בתוך נוזל עומד, קיים לחץ שנובע ממשקל עמוד הנוזל שמעליו. הלחץ הזה, שנקרא לחץ הידרוסטטי, פועל לכל הכיוונים. ככל שצוללים עמוק יותר בנוזל, כך משקל עמוד הנוזל מעל גדול יותר, ולכן גם הלחץ ההידרוסטטי גדל.</li>
        <li><strong>העיקרון המכריע: הלחץ תלוי בעומק בלבד!</strong>
            <br>זוהי נקודת המפתח: הלחץ ההידרוסטטי בנקודה מסוימת בתוך נוזל תלוי רק בעומק הנקודה מפני הנוזל הפתוחים לאוויר (ובצפיפות הנוזל). הוא **אינו מושפע מצורת הכלי או מנפח הנוזל הכולל!** הסיבה נעוצה ב<a href="#" onclick="return false;" title="עקרון פיזיקלי הקובע שלחץ המופעל על נוזל כלוא מועבר באופן אחיד לכל הכיוונים בתוך הנוזל">עקרון פסקל</a>, שקובע שלחץ בנוזל מועבר באופן אחיד. לכן, בכל נקודה באותו גובה בתוך הנוזל המחובר (ובמיוחד בנקודות המחוברות בבסיס הכלים), הלחץ חייב להיות זהה כדי שהנוזל יהיה במנוחה (שיווי משקל).</li>
        <li><strong>שיווי משקל: המים זורמים עד שהלחצים שווים</strong>
            <br>אם לרגע היה מפלס מים גבוה יותר בכלי אחד מאשר באחר, הלחץ ההידרוסטטי בבסיס הכלי הזה היה גבוה יותר. הפרש הלחצים הזה היה דוחף את המים מהכלי עם הלחץ הגבוה לכלי עם הלחץ הנמוך, דרך החיבור שבתחתית. זרימה זו נמשכת עד שהלחץ בנקודת החיבור בבסיס הכלים משתווה. ומכיוון שהלחץ תלוי רק בעומק, השוואת הלחצים בבסיס המחובר יכולה לקרות רק כאשר גובה עמוד הנוזל (מפלס המים) מעל נקודת החיבור זהה בכל הכלים. כשהגבהים שווים, הלחצים שווים, אין יותר כוח דוחף, והמערכת מגיעה לשיווי משקל.</li>
    </ul>

    <h2>כלים שלובים בחיי היום-יום: לא רק בספר לימוד!</h2>
    <p>העיקרון הפשוט הזה שימושי להפליא ומשרת אותנו במגוון תחומים:</p>
    <ul>
        <li><strong>אספקת מים בערים (מגדלי מים):</strong> מגדל המים הגבוה יוצר עמוד מים בעל לחץ גבוה שדוחף את המים דרך צנרת העיר (מערכת כלים שלובים ענקית) לכל הבתים, גם בקומות הגבוהות. הברזים בבתים מקבלים מים בזכות הפרש הגבהים מול המגדל.</li>
        <li><strong>מנעולי מים בתעלות שיט:</strong> במקומות בהם תעלה מחברת שני מקטעים בגבהים שונים (למשל, תעלת פנמה), משתמשים במנעולי מים. זהו חדר אטום שניתן למלא או לרוקן מים, ובכך להשוות את מפלס המים בחדר למקטע התעלה אליו הספינה צריכה להמשיך. הספינה נכנסת, המפלס מושווה, והיא ממשיכה הלאה.</li>
        <li><strong>אינסטלציה ביתית:</strong> מערכת הצינורות שמביאה מים לכיורים, למקלחות ולשירותים בבית היא דוגמה קלאסית לכלים שלובים קטנים. המים מגיעים מנקודת אספקה מרכזית (כמו חיבור לרשת העירונית או מיכל מים), ומתאזנים לגובה מסוים בכל הברזים הסגורים.</li>
        <li><strong>פלס נוזלי (פלס בנאים):</strong> כלי עבודה פשוט הכולל צינור גומי שקוף עם מים. הוא משמש לוודא ששתי נקודות רחוקות זו מזו נמצאות על אותו מישור אופקי. על ידי הצבת קצוות הצינור בשתי הנקודות, מפלס המים בשני הקצוות יהיה זהה, מה שמאפשר לסמן קו ישר ומדויק במרחב.</li>
    </ul>
    <p>פעם הבאה שתראו מים מתאזנים, זכרו את סוד הלחץ והעומק הפועלים יחד כדי ליצור את השיוויון המופלא הזה!</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const slider = document.getElementById('water-level-slider');
        const waterElements = document.querySelectorAll('.vessel .water');
        const percentageLabel = document.getElementById('water-percentage-label'); // Get the new label
        const toggleButton = document.getElementById('toggleExplanation');
        const explanationDiv = document.getElementById('explanation');

        // Function to update water level based on percentage from slider
        function updateWaterLevel(percentage) {
            // Calculate target height relative to the max fillable height of standard vessels (180px)
            const maxStandardFillHeight = 180; // Max height defined in CSS for most vessels
            const targetStandardHeight = (percentage / 100) * maxStandardFillHeight;

             // Height above the bend for the curved-tall vessel (180px container height - 30px bend padding = 150px fillable height)
            const maxCurvedTallFillHeight = 180 - 30; // Corresponds to the vessel's height *above* the bend area

            waterElements.forEach(water => {
                 const vessel = water.closest('.vessel');
                 if (vessel.classList.contains('curved-tall')) {
                     // Calculate height relative to the fillable space above the bend
                     const effectiveTargetHeight = (percentage / 100) * maxCurvedTallFillHeight;
                     water.style.height = `${effectiveTargetHeight}px`;
                     // The bottom position is fixed at 30px by CSS, no need to change here
                 } else {
                     // Standard vessels: fill from the bottom (0px relative to vessel container bottom)
                     water.style.height = `${targetStandardHeight}px`;
                     water.style.bottom = '0'; // Ensure they fill from the bottom
                 }
            });

             // Update the percentage label
             percentageLabel.textContent = `${percentage}%`;
        }

        // Event listener for slider input (while dragging) and change (when released)
        slider.addEventListener('input', (event) => {
            updateWaterLevel(event.target.value);
        });

         // Also listen for 'change' for potentially smoother final update on some mobile browsers
         slider.addEventListener('change', (event) => {
             updateWaterLevel(event.target.value);
         });


        // Initial water level setting on load
        updateWaterLevel(slider.value);

        // Toggle explanation visibility
        toggleButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
            if (isHidden) {
                explanationDiv.style.display = 'block';
                toggleButton.textContent = 'הסתרת הסבר';
                 // Optional: Scroll down to the explanation
                 explanationDiv.scrollIntoView({ behavior: 'smooth' });
            } else {
                explanationDiv.style.display = 'none';
                toggleButton.textContent = 'הסבר על כלים שלובים';
            }
        });

    });
</script>
```