---
title: "פענוח קוד הבניין: המדריך האינטראקטיבי לשרטוטים אדריכליים"
english_slug: decoding-architectural-language-interactive-guide-to-plans
category: "הנדסה"
tags: תוכניות אדריכלות, קריאת שרטוטים, תוכנית קומה, חתך בניין, שרטוט טכני, אדריכלות למתחילים
---
# פענוח קוד הבניין: המדריך האינטראקטיבי לשרטוטים אדריכליים

נתקלת פעם בתוכנית בניין והרגשת שאתה זקוק למפה? קווים, סמלים ומספרים - עולם שלם שמחכה להתגלות! התכונן לצלול פנימה ולפענח את סודות השרטוט האדריכלי, להפוך את הדו-ממד למציאות תלת-ממדית חיה ונושמת. צאו למסע וגלו את האלמנטים המרכזיים בשרטוטי המבנה.

<div class="interactive-architecture-guide">
    <div class="plan-selector">
        <button id="show-floor-plan">חקור תוכנית קומה</button>
        <button id="show-section">חקור חתך בניין</button>
    </div>

    <div id="floor-plan-view" class="plan-view active">
        <h2>תוכנית קומה - מבט על</h2>
        <div class="plan-container">
            <img src="https://via.placeholder.com/600x400/e0e0e0/333333?text=Floor+Plan+Image+Here" alt="תוכנית קומה אדריכלית" class="architectural-plan" id="floor-plan-img">
            <div class="interactive-layer" id="floor-plan-interactive">
                <!-- Interactive areas for Floor Plan -->
                <div class="interactive-element" style="top: 10%; left: 15%; width: 20%; height: 5%;" data-info="קיר חיצוני - עמוד השדרה של המבנה"></div>
                <div class="interactive-element" style="top: 40%; left: 50%; width: 5%; height: 10%;" data-info="דלת - שער הכניסה או המעבר"></div>
                <div class="interactive-element" style="top: 60%; left: 30%; width: 15%; height: 5%;" data-info="חלון - העיניים של הבית אל העולם החיצון"></div>
                 <div class="interactive-element" style="top: 75%; left: 70%; width: 10%; height: 15%;" data-info="גרם מדרגות - הדרך לקומות אחרות"></div>
                 <div class="interactive-element" style="top: 20%; left: 60%; width: 5%; height: 5%;" data-info="עמוד קונסטרוקטיבי - תומך מבני חיוני"></div>
                 <div class="interactive-element" style="top: 5%; left: 5%; width: 15%; height: 5%;" data-info="סמל מימד - המידה האמיתית במציאות"></div>
                  <div class="interactive-element" style="top: 30%; left: 30%; width: 10%; height: 10%;" data-info="ריהוט מייצג (כיור/שירותים) - שימושים בחלל"></div>
            </div>
             <div class="interactive-tooltip"></div> <!-- Tooltip element -->
        </div>
        <div class="info-box" id="floor-plan-info-box">רחף מעל אלמנט בתרשים כדי לגלות את שמו, לחץ למידע נוסף!</div>
    </div>

    <div id="section-view" class="plan-view">
        <h2>חתך בניין - מבט אל פנים המבנה</h2>
        <div class="plan-container">
            <img src="https://via.placeholder.com/600x400/e0e0e0/333333?text=Section+Image+Here" alt="חתך בניין אדריכלי" class="architectural-plan" id="section-img">
             <div class="interactive-layer" id="section-interactive">
                <!-- Interactive areas for Section -->
                 <div class="interactive-element" style="top: 15%; left: 20%; width: 5%; height: 30%;" data-info="קיר נושא בחתך - עוביו נראה בבירור"></div>
                 <div class="interactive-element" style="top: 45%; left: 30%; width: 40%; height: 5%;" data-info="תקרה/רצפת ביניים - מפריד בין קומות"></div>
                 <div class="interactive-element" style="top: 75%; left: 10%; width: 80%; height: 5%;" data-info="יסודות/רצפת קרקע - הבסיס היציב של המבנה"></div>
                 <div class="interactive-element" style="top: 25%; left: 70%; width: 5%; height: 20%;" data-info="חלון בחתך - מיקום וגובה במבנה"></div>
                 <div class="interactive-element" style="top: 10%; left: 80%; width: 10%; height: 10%;" data-info="גג רעפים - הכתר שמגן מלמעלה"></div>
                  <div class="interactive-element" style="top: 55%; left: 50%; width: 5%; height: 15%;" data-info="גרם מדרגות אנכי בחתך"></div>
            </div>
            <div class="interactive-tooltip"></div> <!-- Tooltip element -->
        </div>
         <div class="info-box" id="section-info-box">רחף מעל אלמנט בתרשים כדי לגלות את שמו, לחץ למידע נוסף!</div>
    </div>

</div>

<button id="toggle-explanation" class="toggle-button">מעוניינים להעמיק? לחצו להסבר מפורט</button>

<div id="detailed-explanation" class="explanation-hidden">
    <h2>פענוח הקוד: מהו תרשים אדריכלי ומדוע הוא המפתח לפרויקט?</h2>
    <p>תרשים אדריכלי הוא לא סתם ציור, הוא שפת קוד עשירה בפרטים, הכרחית לתכנון ולבנייה. זהו הכלי המרכזי המאפשר תקשורת מדויקת בין כל הגורמים המעורבים - מהאדריכל החולם ועד הקבלן המבצע. כל קו, סמל ומספר מספרים סיפור על צורה, גודל, חומר ופונקציה.</p>

    <h2>הכירו את השחקנים הראשיים: סוגי תרשימים נפוצים</h2>
    <h3>תוכנית קומה (Floor Plan) - המפה של הבית</h3>
    <p>דמיינו ש"חתכנו" את המבנה בגובה מטר מעל הרצפה והרמנו את החלק העליון – זהו המבט שתוכנית הקומה מעניקה לכם. היא חושפת את הסידור הפנימי ומציגה:
        <ul>
            <li>**קירות:** עבים או דקים, מלאים או חלולים – כל סימון מגלה את תפקיד הקיר (נושא, מחיצה).</li>
            <li>**דלתות וחלונות:** הסמלים שלהם אינם רק מיקום, אלא גם סוג הפתיחה וכיוונה.</li>
            <li>**אלמנטים קבועים:** כיורים, אמבטיות, ארונות - רמזים לשימושים של החללים.</li>
            <li>**מימדים מדויקים:** המספרים הקטנים לאורך הקווים הם קואורדינטות העולם האמיתי.</li>
            <li>**סמלים נוספים:** גרמי מדרגות, פתחי אוורור, עמודים, סימוני מפלסים – כל פרט חשוב.</li>
        </ul>
    </p>

    <h3>חתך בניין (Section) - הצצה אל תוך הלב</h3>
    <p>כאילו פרסנו את הבניין בסכין חדה אנכית – החתך מראה את המבנה לעומק. הוא חיוני להבנת היחסים הוורטיקליים וחושף:
        <ul>
            <li>**גבהים משמעותיים:** גובה התקרה, גובה החלון מהרצפה, עומק היסודות – מספרים שחיוניים לבנייה.</li>
            <li>**שכבות הרצפה והתקרה:** כיצד הן בנויות ומה מרכיב אותן.</li>
            <li>**קונסטרוקציה פנימית:** קורות, עמודים ורכיבים תומכים שפחות נראים בתוכנית קומה.</li>
            <li>**חומרים:** לעיתים, סמלים גרפיים שונים מעידים על סוג החומרים הנחתכים.</li>
        </ul>
        חתכים הם המפתח להבנת המבנה בתלת-ממד.
    </p>

    <p>עולם השרטוטים רחב וכולל גם חזיתות (מבט חיצוני) ופרטים (הגדלות של חיבורים מורכבים) - כל אחד מהם שכבה נוספת בפאזל הבניין.</p>

    <h2>לומדים את האלף-בית: סמלים בסיסיים שחייבים להכיר</h2>
    <p>כמו כל שפה, גם לשפת האדריכלות יש אוצר מילים ויזואלי:
        <ul>
            <li>**קירות:** עובי הקו, סוג הקו ולעיתים הטחה או מילוי – כולם מעבירים מידע על סוג הקיר ותפקודו.</li>
            <li>**פתחים (דלתות וחלונות):** סמלים קבועים המציגים לא רק את הרוחב אלא גם את כיוון הפתיחה וסוג החלון.</li>
            <li>**מדרגות:** סידרה של מלבנים קטנים, כשלצדם חץ המצביע תמיד על כיוון העלייה (לעולם לא הירידה!).</li>
            <li>**קווי מימד וגבהים:** הקווים הדקים עם המספרים הם המדריך שלכם למידות האמיתיות. סמלי גובה (מפלס) קריטיים להבנת הפרשי גבהים.</li>
            <li>**סימונים גרפיים וטקסט:** הטחות, מילויים, מספור חדרים והערות טקסט - מידע משלים על חומרים, פונקציות ופרטים ייחודיים.</li>
        </ul>
    </p>

    <h2>התמונה השלמה: הקשר בין תוכנית קומה לחתך</h2>
    <p>הבנה אמיתית של מבנה דורשת מבט כפול. תוכנית קומה מספקת את ה"איפה" (הסידור האופקי), בעוד החתך מספק את ה"כמה גבוה" וה"איך זה בנוי לעומק" (המבט האנכי). שניהם יחד, כמו שתי זוויות ראייה שונות, מאפשרים לכם לבנות במוחכם מודל תלת-ממדי מלא ומדויק של הפרויקט.</p>

    <h2>טיפים להפוך למפענחי שרטוטים מצטיינים:</h2>
    <p>
        <ol>
            <li>**התחילו בבסיס:** קראו את הכותרת, הסולם (קנה המידה), מיקומי החתכים והחזיתות המסומנים בתוכנית הקומה.</li>
            <li>**מצאו את הכיוון:** חץ הצפון הוא העוגן שלכם במרחב.</li>
            <li>**הבינו את הסולם:** קנה המידה הוא קסם ההקטנה (או ההגדלה) של המציאות. 1:50, 1:100, 1:200 – כל אחד מספר סיפור אחר.</li>
            <li>**עקבו אחר קווי החתך:** הם כמו סמני דרך המקשרים בין תוכנית הקומה לשרטוטי החתך.</li>
            <li>**כל קו וסמל חשוב:** אל תפספסו פרטים קטנים. חפשו מקרא סמלים אם קיים (לעיתים נמצא בשרטוט נפרד).</li>
            <li>**השוו והצליבו מידע:** עברו הלוך ושוב בין תוכנית הקומה, החתכים והחזיתות כדי לבנות תמונה שלמה ועשירה.</li>
        </ol>
    </p>
    <p>עם קצת תרגול, שפת האדריכלות תהפוך מ"קוד סודי" לכלי רב עוצמה שיאפשר לכם להבין, לנתח ואף לתכנן את המרחב סביבכם.</p>
</div>

<style>
/* כללי */
.interactive-architecture-guide {
    font-family: 'Arial', sans-serif;
    direction: rtl;
    text-align: right;
    margin-top: 20px;
    border: 1px solid #d3dce6; /* Light grey border */
    padding: 20px; /* Increased padding */
    border-radius: 12px; /* More rounded corners */
    background-color: #ffffff; /* White background */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    transition: all 0.3s ease-in-out; /* Smooth transitions */
}

/* בורר תוכניות */
.plan-selector {
    text-align: center;
    margin-bottom: 25px; /* More space below buttons */
}

.plan-selector button {
    margin: 0 8px; /* Slightly less margin */
    padding: 12px 25px; /* Larger padding */
    font-size: 1.1rem; /* Slightly larger font */
    cursor: pointer;
    border: none; /* No border */
    border-radius: 6px; /* More rounded */
    background-color: #f1f3f5; /* Light grey background */
    color: #343a40; /* Dark grey text */
    transition: all 0.3s ease;
    font-weight: bold;
}

.plan-selector button:hover {
    background-color: #e9ecef; /* Slightly darker grey on hover */
    color: #007bff; /* Highlight color on hover */
}

.plan-selector button.active {
    background-color: #007bff; /* Primary blue */
    color: white;
    box-shadow: 0 2px 6px rgba(0, 123, 255, 0.3); /* Shadow for active state */
    transform: translateY(-2px); /* Slight lift */
}

/* תצוגת תוכנית */
.plan-view {
    display: none;
    opacity: 0; /* Start hidden */
    transition: opacity 0.5s ease-in-out; /* Fade transition */
}

.plan-view.active {
    display: block;
    opacity: 1; /* Fade in */
}

.plan-view h2 {
    text-align: center;
    color: #343a40; /* Dark grey */
    margin-bottom: 20px; /* More space below title */
    font-size: 1.6rem; /* Larger title */
    font-weight: normal;
}

.plan-container {
    position: relative;
    width: 100%;
    max-width: 650px; /* Slightly larger max width */
    margin: 0 auto;
    border: 1px solid #ced4da; /* Light border around image */
    border-radius: 8px; /* Rounded corners for container */
    overflow: hidden; /* Hide overflow from border-radius */
}

.architectural-plan {
    display: block;
    width: 100%;
    height: auto;
    background-color: #e9ecef; /* Placeholder background color */
}

.interactive-layer {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    direction: ltr; /* Use LTR for positioning overlays */
    z-index: 10; /* Ensure layer is above image */
}

/* אלמנטים אינטראקטיביים */
.interactive-element {
    position: absolute;
    /* Subtle initial appearance */
    background-color: rgba(0, 123, 255, 0.05); /* Very light blue fill */
    border: 1px dashed rgba(0, 123, 255, 0.3); /* Light dashed border */
    cursor: pointer;
    opacity: 0.01; /* Almost invisible initially */
    transition: opacity 0.3s ease-in-out, transform 0.2s ease-in-out, background-color 0.3s ease;
    z-index: 11; /* Above interactive layer */
}

.interactive-element:hover {
    opacity: 1; /* Fully visible on hover */
    background-color: rgba(0, 123, 255, 0.3); /* More solid fill */
    border-color: rgba(0, 123, 255, 0.7); /* More solid border */
    transform: scale(1.02); /* Subtle scale effect */
}

.interactive-element.clicked {
     background-color: rgba(40, 167, 69, 0.4); /* Greenish background when clicked */
     border-color: rgba(40, 167, 69, 0.8); /* More solid green border */
     opacity: 1; /* Stay visible after click */
}


/* תיבת מידע ראשית */
.info-box {
    text-align: center;
    margin-top: 20px; /* More space above */
    padding: 15px; /* More padding */
    min-height: 40px; /* Reserve more space */
    border: 1px solid #007bff; /* Blue border */
    border-radius: 8px; /* Rounded corners */
    background-color: #e9faff; /* Very light blue background */
    color: #0056b3; /* Darker blue text */
    font-size: 1.1rem; /* Slightly larger font */
    font-weight: bold;
    display: flex; /* Use flexbox for centering */
    align-items: center; /* Vertical center */
    justify-content: center; /* Horizontal center */
}

/* Tooltip (for hover info) */
.interactive-tooltip {
    position: absolute;
    background-color: #343a40; /* Dark background */
    color: white;
    padding: 8px 12px;
    border-radius: 6px;
    font-size: 0.9rem;
    white-space: nowrap; /* Prevent text wrapping */
    z-index: 20; /* Above everything else */
    pointer-events: none; /* Allow clicks to pass through */
    opacity: 0; /* Hidden by default */
    transition: opacity 0.2s ease-in-out;
    transform: translate(-50%, -110%); /* Position above & center */
    text-align: center;
    direction: rtl; /* Ensure RTL text within tooltip */
}

/* Tooltip Arrow (optional but nice) */
.interactive-tooltip::after {
    content: "";
    position: absolute;
    bottom: -5px; /* Position below */
    left: 50%;
    transform: translateX(-50%);
    border-width: 5px;
    border-style: solid;
    border-color: #343a40 transparent transparent transparent; /* Dark arrow pointing down */
}


/* כפתור הצג הסבר */
.toggle-button {
    display: block;
    width: fit-content;
    margin: 30px auto 20px auto; /* More vertical space */
    padding: 12px 25px; /* Larger padding */
    font-size: 1.1rem; /* Larger font */
    cursor: pointer;
    border: none; /* No border */
    border-radius: 6px; /* Rounded */
    background-color: #28a745; /* Green color */
    color: white;
    transition: background-color 0.3s ease, transform 0.2s ease;
    font-weight: bold;
    box-shadow: 0 2px 6px rgba(40, 167, 69, 0.3); /* Subtle shadow */
}

.toggle-button:hover {
    background-color: #218838; /* Darker green on hover */
    transform: translateY(-2px); /* Slight lift */
}

/* אזור ההסבר */
.explanation-hidden {
    display: none;
    margin-top: 20px;
    padding: 20px; /* More padding */
    border: 1px solid #d3dce6; /* Light border */
    border-radius: 12px; /* Rounded corners */
    background-color: #f8f9fa; /* Very light grey background */
    color: #343a40; /* Dark grey text */
    line-height: 1.7; /* Improved readability */
}

.explanation-hidden h2 {
    color: #007bff; /* Primary blue for main heading */
    margin-bottom: 15px;
    font-size: 1.8rem;
    text-align: center;
    border-bottom: 2px solid #007bff; /* Underline heading */
    padding-bottom: 10px;
}

.explanation-hidden h3 {
    color: #343a40; /* Dark grey for subheadings */
    margin-top: 20px;
    margin-bottom: 10px;
    font-size: 1.4rem;
    border-bottom: 1px dashed #adb5bd; /* Dashed underline */
    padding-bottom: 5px;
}

.explanation-hidden p {
    margin-bottom: 15px;
}

.explanation-hidden ul, .explanation-hidden ol {
    margin-bottom: 15px;
    padding-right: 20px; /* For RTL list bullets */
    line-height: 1.6;
}

.explanation-hidden li {
    margin-bottom: 8px;
}

/* אנימציית פעימה עדינה על ריחוף - אופציונלי */
/*
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.03); }
    100% { transform: scale(1); }
}
.interactive-element:hover {
     ... existing styles ...
     animation: pulse 1.5s infinite ease-in-out;
}
*/

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const floorPlanView = document.getElementById('floor-plan-view');
    const sectionView = document.getElementById('section-view');
    const showFloorPlanBtn = document.getElementById('show-floor-plan');
    const showSectionBtn = document.getElementById('show-section');

    const floorPlanInfoBox = document.getElementById('floor-plan-info-box');
    const sectionInfoBox = document.getElementById('section-info-box');

    const floorPlanElements = document.querySelectorAll('#floor-plan-interactive .interactive-element');
    const sectionElements = document.querySelectorAll('#section-interactive .interactive-element');

    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const detailedExplanationDiv = document.getElementById('detailed-explanation');

    // Get the tooltip element. There should be one inside each plan-container.
    const floorPlanTooltip = floorPlanView.querySelector('.interactive-tooltip');
    const sectionTooltip = sectionView.querySelector('.interactive-tooltip');


    // Function to setup interactive elements with hover (tooltip) and click (info box)
    function setupInteractiveElements(elements, infoBox, tooltip) {
        elements.forEach(element => {
            const info = element.getAttribute('data-info');
            if (info) {
                // On hover (show tooltip)
                element.addEventListener('mouseover', (event) => {
                    tooltip.textContent = info;
                    tooltip.style.opacity = '1';
                    // Position the tooltip near the element
                    const elementRect = element.getBoundingClientRect();
                    const containerRect = element.closest('.plan-container').getBoundingClientRect();
                    // Calculate position relative to the container, considering RTL layout for tooltip
                    // Tooltip will be centered above the element
                    tooltip.style.left = (elementRect.left - containerRect.left + elementRect.width / 2) + 'px';
                    tooltip.style.top = (elementRect.top - containerRect.top) + 'px';

                    // Add a visual hover class (optional, if needed for CSS effects)
                    element.classList.add('hovered');

                });

                element.addEventListener('mouseout', () => {
                    tooltip.style.opacity = '0';
                     element.classList.remove('hovered');
                });

                // On click (update main info box and add 'clicked' class)
                 element.addEventListener('click', () => {
                     // Remove 'clicked' class from others in this view
                     elements.forEach(el => el.classList.remove('clicked'));
                     element.classList.add('clicked');
                     infoBox.textContent = `מידע על: ${info}`; // Update info box with clicked element info
                 });
            }
        });

         // Reset info box and highlights when clicking outside interactive elements within the container
         const planContainer = elements.length > 0 ? elements[0].closest('.plan-container') : null;
         if (planContainer) {
             planContainer.addEventListener('click', (event) => {
                 if (!event.target.closest('.interactive-element')) {
                      elements.forEach(el => el.classList.remove('clicked')); // Remove clicked state from all
                      // Reset the info box text
                       const activeView = document.querySelector('.plan-view.active');
                       if (activeView) {
                           const currentInfoBox = activeView.querySelector('.info-box');
                           if (currentInfoBox) {
                               currentInfoBox.textContent = 'רחף מעל אלמנט בתרשים כדי לגלות את שמו, לחץ למידע נוסף!';
                           }
                       }
                 }
             });
         }
    }

    // Setup initial state and events for both plans
    setupInteractiveElements(floorPlanElements, floorPlanInfoBox, floorPlanTooltip);
    setupInteractiveElements(sectionElements, sectionInfoBox, sectionTooltip);


    // Plan selection logic with fade effect
    function switchPlan(planToShow, planToHide, buttonToActivate, buttonToDeactivate, infoBoxToReset, elementsToReset) {
        // Reset info box and highlights in the current active view BEFORE hiding
        const activeView = document.querySelector('.plan-view.active');
         if (activeView) {
             const currentInfoBox = activeView.querySelector('.info-box');
             if (currentInfoBox) {
                 currentInfoBox.textContent = 'רחף מעל אלמנט בתרשים כדי לגלות את שמו, לחץ למידע נוסף!';
             }
             const currentElements = activeView.querySelectorAll('.interactive-element');
             currentElements.forEach(el => el.classList.remove('clicked'));
         }


        planToHide.style.opacity = '0'; // Start fade out
        buttonToDeactivate.classList.remove('active');

        // Use a timeout to wait for the fade out before changing display and fading in
        setTimeout(() => {
            planToHide.classList.remove('active');
            planToHide.style.display = 'none'; // Hide after fade out

            planToShow.classList.add('active');
            planToShow.style.display = 'block'; // Show the new plan
            // Force reflow to ensure display: block is applied before starting fade-in
            planToShow.offsetWidth;
            planToShow.style.opacity = '1'; // Fade in

            buttonToActivate.classList.add('active');

             // Reset info box and highlights *after* the new view is active and displayed
             // This is also handled by the initial reset before hiding the previous view, but doing it again here ensures consistency.
            // infoBoxToReset.textContent = 'רחף מעל אלמנט בתרשים כדי לגלות את שמו, לחץ למידע נוסף!';
            // elementsToReset.forEach(el => el.classList.remove('clicked'));


        }, 500); // Match CSS transition duration
    }


    showFloorPlanBtn.addEventListener('click', () => {
        if (!floorPlanView.classList.contains('active')) {
            switchPlan(floorPlanView, sectionView, showFloorPlanBtn, showSectionBtn, floorPlanInfoBox, floorPlanElements);
        }
    });

    showSectionBtn.addEventListener('click', () => {
         if (!sectionView.classList.contains('active')) {
            switchPlan(sectionView, floorPlanView, showSectionBtn, showFloorPlanBtn, sectionInfoBox, sectionElements);
         }
    });

    // Explanation toggle logic
    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = detailedExplanationDiv.classList.contains('explanation-hidden');
        if (isHidden) {
            detailedExplanationDiv.classList.remove('explanation-hidden');
            detailedExplanationDiv.style.display = 'block'; // Explicitly set display for transition
             // Optional: Add a class for fade-in effect
            setTimeout(() => detailedExplanationDiv.style.opacity = '1', 10); // Small delay to allow display change
            toggleExplanationBtn.textContent = 'הסתר הסבר מפורט';
             toggleExplanationBtn.classList.add('active'); // Style the button when explanation is open
        } else {
            detailedExplanationDiv.style.opacity = '0'; // Start fade-out
            toggleExplanationBtn.classList.remove('active'); // Unstyle the button

            setTimeout(() => {
                detailedExplanationDiv.style.display = 'none'; // Hide after fade-out
                detailedExplanationDiv.classList.add('explanation-hidden');
                toggleExplanationBtn.textContent = 'מעוניינים להעמיק? לחצו להסבר מפורט';
            }, 500); // Match CSS transition duration
        }
    });

     // Ensure only floor plan is visible and styled as active initially
    floorPlanView.classList.add('active');
    floorPlanView.style.display = 'block'; // Ensure initial display
    floorPlanView.style.opacity = '1'; // Ensure initial opacity
    sectionView.classList.remove('active');
    sectionView.style.display = 'none';
    sectionView.style.opacity = '0';
    showFloorPlanBtn.classList.add('active');
    showSectionBtn.classList.remove('active');

     // Set explanation to initially be hidden with transition properties
    detailedExplanationDiv.style.opacity = '0';
    detailedExplanationDiv.style.transition = 'opacity 0.5s ease-in-out';


});
</script>
---