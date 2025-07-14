---
title: "מסע הקסם של הג'ינס: מהסיב הכחול אל האריג האהוב"
english_slug: the-magic-of-jeans-blue-journey-from-factory
category: "אופנה וטקסטיל"
tags: [ג'ינס, אינדיגו, צביעה, שטיפה, טקסטיל, ייצור, אופנה, סימולציה, אינטראקטיבי]
---
<h1>מסע הקסם של הג'ינס: מהסיב הכחול אל האריג האהוב</h1>
<p>הם שם תמיד, הפריט האולטימטיבי במלתחה, סמל לקלאסיקה ונוחות. אבל מה הופך בד כותנה פשוט לאריג הדנים העמיד והכחול שכולנו מכירים ואוהבים? הצטרפו אלינו למסע ויזואלי מרתק אל סודות הייצור של בד הג'ינס, מהכותנה הגולמית ועד הגימור הסופי!</p>

<div id="jeans-app">
    <h2>תחנת הייצור האינטראקטיבית</h2>
    <div id="fabric-simulation-area">
        <div id="fabric-display">
            <img id="fabric-image" src="" alt="שלב בתהליך ייצור הג'ינס">
            <div id="simulation-overlay"></div> <!-- For vat/air effect -->
        </div>
        <p id="step-text"></p>
    </div>

    <div id="controls">
        <button id="next-step-btn">השלב הבא</button>
        <div id="wash-options" style="display: none;">
            <p>בחרו את גימור השטיפה המועדף עליכם:</p>
            <button class="wash-btn" data-wash-type="raw">ג'ינס גולמי (ללא שטיפה)</button>
            <button class="wash-btn" data-wash-type="stone">סטון ווש (שטיפת אבנים)</button>
            <button class="wash-btn" data-wash-type="acid">אסיד ווש (שטיפת חומצה לכאורה)</button>
            <button class="wash-btn" data-wash-type="enzyme">אנזים ווש (שטיפה ביולוגית)</button>
        </div>
        <button id="restart-btn" style="display: none;">התחילו את המסע מחדש</button>
    </div>
</div>

<style>
    :root {
        --denim-blue-dark: #1f497d;
        --denim-blue-medium: #2a6099;
        --denim-blue-light: #5b9bd5;
        --cotton-white: #f5f5dc;
        --light-grey: #e0e0e0;
        --medium-grey: #c0c0c0;
        --dark-grey: #a0a0a0;
        --accent-green: #28a745;
        --accent-red: #dc3545;
        --button-blue: #007bff;
        --button-blue-hover: #0056b3;
        --button-green: var(--accent-green);
        --button-green-hover: #218838;
        --button-grey: #6c757d;
        --button-grey-hover: #5a6268;
        --vat-color: #add8e6; /* Light blue for the vat liquid */
        --air-color: linear-gradient(to top, #e0f2f7, #ffffff); /* Subtle gradient for air */
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f8f9fa;
        margin: 0;
        padding: 20px;
        direction: rtl; /* Ensure entire body is RTL */
        text-align: right; /* Default text align for explanation */
    }

    h1, h2, h3 {
        color: var(--denim-blue-dark);
        text-align: center;
        margin-bottom: 15px;
    }

    p {
        margin-bottom: 15px;
    }

    #jeans-app {
        text-align: center;
        margin: 30px auto;
        padding: 30px;
        border: 1px solid #ddd;
        border-radius: 12px;
        background: linear-gradient(to bottom right, #ffffff, #f0f0f0);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 700px;
        direction: rtl;
    }

    #fabric-simulation-area {
        margin: 20px auto;
        perspective: 1000px; /* For 3D effects if needed */
    }

    #fabric-display {
        position: relative; /* Needed for absolute overlay */
        width: 280px;
        height: 350px;
        margin: 20px auto;
        border: 3px solid var(--denim-blue-dark);
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        overflow: hidden; /* Ensure image stays within bounds */
        background-color: var(--cotton-white); /* Default background */
        transition: background-color 0.8s ease-in-out, transform 0.5s ease-in-out;
        box-shadow: inset 0 0 15px rgba(0,0,0,0.2);
    }

    #fabric-image {
        display: block; /* Ensure img is displayed */
        max-width: 100%;
        max-height: 100%; /* Allow image to fill area */
        object-fit: cover; /* Cover the area nicely */
        transition: opacity 0.6s ease-in-out, transform 0.6s ease-in-out;
        opacity: 0; /* Start hidden */
    }

    #simulation-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: transparent; /* Default */
        transition: background-color 0.8s ease-in-out, opacity 0.8s ease-in-out;
        pointer-events: none; /* Don't block clicks */
        opacity: 0; /* Start hidden */
    }

    #fabric-display.dipping .simulation-overlay {
         background-color: var(--vat-color);
         opacity: 0.9; /* Make vat visible */
    }
     #fabric-display.oxidizing .simulation-overlay {
         background: var(--air-color);
         opacity: 0.7; /* Make air effect visible */
    }

     #fabric-image.visible {
         opacity: 1;
         transform: scale(1);
     }
      #fabric-image:not(.visible) {
         transform: scale(0.95);
      }


    #step-text {
        margin-top: 15px;
        font-size: 1.1em;
        color: var(--denim-blue-dark);
        min-height: 3em; /* Reserve space to prevent layout shifts */
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 0 10px;
        box-sizing: border-box;
    }

    #controls {
        margin-top: 25px;
    }

    #next-step-btn, .wash-btn, #restart-btn {
        padding: 12px 20px;
        margin: 8px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    #next-step-btn {
        background-color: var(--button-blue);
        color: white;
    }

    #next-step-btn:hover {
        background-color: var(--button-blue-hover);
        transform: translateY(-2px);
    }

     #wash-options {
        margin-top: 20px;
        padding: 15px;
        border: 1px dashed var(--denim-blue-light);
        border-radius: 8px;
        background-color: rgba(var(--denim-blue-light), 0.1);
    }

    #wash-options p {
        margin-bottom: 15px;
        font-size: 1.1em;
        color: var(--denim-blue-dark);
        font-weight: bold;
    }

    #wash-options button {
        display: inline-block; /* Allow buttons to be side-by-side if space allows */
        width: auto; /* Adjust width based on content */
        min-width: 150px;
        background-color: var(--button-green);
        color: white;
    }

    #wash-options button:hover {
        background-color: var(--button-green-hover);
        transform: translateY(-2px);
    }

    #wash-options button[data-wash-type="raw"] {
         background-color: var(--button-grey);
     }
      #wash-options button[data-wash-type="raw"]:hover {
         background-color: var(--button-grey-hover);
         transform: translateY(-2px);
     }

     #restart-btn {
         background-color: var(--accent-red);
         color: white;
         margin-top: 20px;
     }
      #restart-btn:hover {
         background-color: #c82333;
         transform: translateY(-2px);
      }


    #toggle-explanation-btn {
        display: block; /* Button takes full width */
        width: 100%; /* Full width */
        max-width: 700px; /* Match app width */
        margin: 30px auto 20px auto; /* Center below app */
        padding: 12px 20px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: var(--button-grey);
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }
    #toggle-explanation-btn:hover {
        background-color: var(--button-grey-hover);
        transform: translateY(-2px);
    }

    #explanation {
        margin: 20px auto;
        padding: 25px;
        border: 1px solid #ddd;
        border-radius: 12px;
        background-color: #ffffff;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
        text-align: right;
        max-width: 700px; /* Match app width */
    }

    #explanation h2 {
        color: var(--denim-blue-dark);
        margin-top: 15px;
        text-align: right;
    }
     #explanation h3 {
         color: var(--denim-blue-medium);
         margin-top: 20px;
         margin-bottom: 10px;
         text-align: right;
     }

    #explanation p {
        line-height: 1.7;
        margin-bottom: 15px;
    }

    #explanation ul {
        margin-bottom: 15px;
        padding-right: 20px; /* Indent list */
    }

    #explanation li {
        margin-bottom: 8px;
        line-height: 1.6;
    }

    /* Responsive adjustments */
    @media (max-width: 600px) {
        #jeans-app, #toggle-explanation-btn, #explanation {
            padding: 15px;
            margin-left: 10px;
            margin-right: 10px;
        }

        #fabric-display {
            width: 200px;
            height: 250px;
        }

        #next-step-btn, .wash-btn, #restart-btn {
            padding: 10px 15px;
            margin: 5px;
            font-size: 0.9em;
        }

         #wash-options button {
             min-width: 120px;
             display: block;
             margin: 8px auto;
         }
    }

</style>

<button id="toggle-explanation-btn">הצגת/הסתרת סיפור הרקע המלא</button>

<div id="explanation" style="display: none;">
    <h2>סיפור הרקע המלא: מסעו של הג'ינס</h2>

    <h3>חומר הקסם: סיבי כותנה</h3>
    <p>בליבה של כל פיסת ג'ינס עומדים סיבי הכותנה - חומר גלם טבעי, רך ובו זמנית עמיד בצורה יוצאת דופן. הסיבים הללו הם הבסיס האיתן עליו נבנה כל תהליך הייצור, ומספקים את חוזקו ועמידותו המפורסמת של הבד.</p>

    <h3>הפיכה לחוט ואריגה: לידת בד הדנים</h3>
    <p>תהליך קסום נוסף מתחיל כאשר סיבי הכותנה נטווים והופכים לחוטים דקים. החוטים הללו נארגים בטכניקה מיוחדת הנקראת "אריגת טוויל" (Twill Weave). שיטה זו יוצרת את הדפוס האלכסוני המוכר על פני בד הדנים, וחשוב מכך - היא מעניקה לו את הגמישות המאפשרת תנועה לצד עמידותו יוצאת הדופן בפני קריעה ושפשוף. זהו השלב שבו הבד הופך למעשה ל"דנים", אך עדיין בצבעו הטבעי, לבן או קרם בהיר.</p>

    <h3>טבילת הקסם: צביעת האינדיגו העמוקה</h3>
    <p>כאן נכנס לתמונה גיבור הסיפור הכחול: צבע האינדיגו. צבע זה, שבעבר הופק מצמחים וכיום לרוב מסונתז במעבדה, הוא בעל תכונה מרתקת. הוא אינו מסיס במים בצורתו הרגילה. כדי להחדיר אותו לסיבים, צוללים החוטים הלבנים לאמבט מיוחד המכיל את צבע האינדיגו בצורה מסיסה (Leuco-indigo). החוטים סופגים את הצבע, וכשהם נחשפים שוב לאוויר - קורה הקסם! החמצן גורם לצבע להתחמצן בחזרה לצורתו הבלתי-מסיסה והכחולה, שנלכדת בתוך סיבי הכותנה.</p>

    <h3>סוד העומק: טבילות מרובות</h3>
    <p>צבע הג'ינס אינו נוצר בטבילה אחת. כדי להגיע לעומק הצבע הכהה והעשיר שאנו מכירים, החוטים עוברים סדרה של טבילות קצרות באמבט האינדיגו, כאשר בין כל טבילה וחברתה יש תקופת חשיפה לאוויר. כל חשיפה כזו מקבעת שכבה נוספת של צבע על גבי הסיב. ככל שמספר הטבילות עולה (לעיתים עד 10-15 טבילות!), כך הצבע הסופי יהיה כהה ועמוק יותר. זוהי הסיבה שחוטי הדנים נצבעים בצביעת "רינג-דיי" (Ring Dye), כלומר, הצבע נצמד בעיקר לשכבה החיצונית של הסיב, וליבתו נשארת בהירה.</p>

    <h3>הדהייה המפורסמת: סיפור השפשוף</h3>
    <p>תכונת הדהייה הייחודית של הג'ינס נובעת ישירות מתהליך הצביעה. מכיוון שהצבע יושב בעיקר על פני הסיב, כל שפשוף, בלאי או שטיפה גורמים לשחיקה של השכבה החיצונית הצבועה. כאשר שכבה זו יורדת, נחשפת ליבת הסיב הלבנה שמתחתיה. זהו המנגנון שיוצר את הדהיות, השפשופים והמראה ה"חי" והמשתנה של הג'ינס עם הזמן והלבישה. כל זוג ג'ינס מספר את סיפורו האישי של הלובש אותו באמצעות הדפוסים שנוצרים עליו.</p>

    <h3>אמנות הגימור: קסם השטיפות</h3>
    <p>לאחר האריגה והצביעה, רוב בדי הג'ינס עוברים "גימור רטוב" - תהליכי שטיפה מגוונים. תהליכים אלו אינם רק ניקיון, אלא חלק בלתי נפרד מעיצוב המראה הסופי של הבד, וכיום של הבגד. מטרותיהם העיקריות הן:</p>
    <ul>
        <li><strong>ריכוך הבד:</strong> בד דנים גולמי (Raw Denim) הוא נוקשה למדי. שטיפות עוזרות לרכך אותו משמעותית.</li>
        <li><strong>יצירת מראה מעוצב:</strong> תהליכי שטיפה מזרזים את אפקט הדהייה והבלאי, ומאפשרים ליצור מגוון רחב של גוונים וטקסטורות, ממראה וינטג' דהוי ועד מראה מודרני עם ניגודים חדים.</li>
        <li><strong>צמצום הבד:</strong> שטיפה ראשונית עוזרת לצמצם את הבד לפני ייצור הבגד, ובכך להקטין את השינויים שיחולו בו בשטיפות ביתיות מאוחרות יותר.</li>
    </ul>

    <h3>סוגי שטיפה מובילים והאפקטים שלהם</h3>
    <p>עולם השטיפות עשיר ומגוון, וכל טכניקה מותירה חותם ויזואלי שונה לחלוטין:</p>
    <ul>
        <li><strong>סטון ווש (Stone Wash):</strong> שיטה קלאסית בה הבד עובר כביסה עם אבני פומיס טבעיות או סינתטיות. האבנים משפשפות את הבד, מסירות שכבות צבע חיצוניות באופן יחסית אחיד, ויוצרות מראה דהוי ורך יותר מהג'ינס הגולמי.</li>
        <li><strong>אסיד ווש (Acid Wash):</strong> שיטה דרמטית יותר (שלמרות שמה, לרוב אינה משתמשת בחומצה אמיתית אלא בחומרי הלבנה). לרוב משתמשים באבנים ספוגות בחומר מלבין המפוזרות בצורה לא אחידה על הבד במכונה יבשה. האבנים המלבינות יוצרות נקודות ואזורים בהירים מאוד, לעיתים במראה מנומר או "מחוטא", עם ניגודיות גבוהה.</li>
        <li><strong>אנזים ווש (Enzyme Wash):</strong> טכניקה "ידידותית" יותר לבד, המשתמשת באנזימים (כמו צלולאז) התוקפים ומפרקים חלקית את סיבי הכותנה או את מולקולות הצבע. שטיפה זו מעניקה ריכוך לבד ודהייה עדינה ואחידה יותר בהשוואה לסטון ווש, מבלי לגרום נזק מכני גדול.</li>
        <li><strong>סוגי גימור נוספים:</strong> ישנן טכניקות רבות נוספות כמו בְּלִיץ' ווש (Bleach Wash - הלבנה ישירה), סנדבְּלַסְטינג (Sandblasting - ליטוש בחול בלחץ גבוה, פחות נפוץ היום מסיבות בריאותיות), וגימורים מודרניים יותר כמו לייזר שצורב דפוסים ספציפיים על הבד.</li>
    </ul>

    <p>תהליכי השטיפה והגימור הם שמעניקים לכל זוג ג'ינס את ה"אישיות" הייחודית שלו, ויוצרים את המגוון העצום שמאפשר לכל אחד למצוא את הג'ינס המושלם עבורו.</p>
</div>

<script>
    const fabricSimulationArea = document.getElementById('fabric-simulation-area');
    const fabricDisplay = document.getElementById('fabric-display');
    const fabricImage = document.getElementById('fabric-image');
    const simulationOverlay = document.getElementById('simulation-overlay');
    const stepText = document.getElementById('step-text');
    const nextStepBtn = document.getElementById('next-step-btn');
    const washOptionsDiv = document.getElementById('wash-options');
    const washButtons = document.querySelectorAll('.wash-btn');
    const restartBtn = document.getElementById('restart-btn');
    const toggleExplanationBtn = document.getElementById('toggle-explanation-btn');
    const explanationDiv = document.getElementById('explanation');

    let currentStep = 0;

    // Placeholders for images - actual image files would be needed
    const imageAssets = {
        cotton: 'https://placehold.co/300x350/f5f5dc/000?text=Cotton+Fibers', // Placeholder for cotton fibers
        woven: 'https://placehold.co/300x350/ffffff/000?text=Woven+Fabric', // Placeholder for white woven fabric
        dip1: 'https://placehold.co/300x350/e3f2fd/000?text=1st+Dip', // Placeholder for light blue after dip 1
        oxi1: 'https://placehold.co/300x350/bbdefb/000?text=1st+Oxidation', // Placeholder after oxi 1
        dip2: 'https://placehold.co/300x350/90caf9/000?text=2nd+Dip',
        oxi2: 'https://placehold.co/300x350/64b5f6/000?text=2nd+Oxidation',
        dip3: 'https://placehold.co/300x350/42a5f5/000?text=3rd+Dip',
        oxi3: 'https://placehold.co/300x350/2196f3/000?text=3rd+Oxidation',
        dip4: 'https://placehold.co/300x350/1e88e5/000?text=4th+Dip',
        oxi4: 'https://placehold.co/300x350/1976d2/000?text=4th+Oxidation',
        raw: 'https://placehold.co/300x350/0d47a1/fff?text=Raw+Denim', // Placeholder for raw dark denim after many dips
        stone: 'https://placehold.co/300x350/9e9e9e/000?text=Stone+Wash', // Placeholder for stone wash effect
        acid: 'https://placehold.co/300x350/e0e0e0/333?text=Acid+Wash', // Placeholder for acid wash effect
        enzyme: 'https://placehold.co/300x350/bdbdbd/000?text=Enzyme+Wash' // Placeholder for enzyme wash effect
    };


    // Define the steps of the process
    const steps = [
        { text: "1. אוספים את חומר הקסם: סיבי כותנה רכים.", image: imageAssets.cotton, type: 'material' },
        { text: "2. אורגים את הסיבים לחוט, ואז את החוט לבד הדנים הלבן והעמיד.", image: imageAssets.woven, type: 'woven' },
        { text: "3. צלילה ראשונה לאמבט צבע האינדיגו הקסום!", image: imageAssets.dip1, type: 'dip' },
        { text: "4. חשיפה לאוויר: קסם החמצון הופך את הצבע לכחול!", image: imageAssets.oxi1, type: 'oxidation' },
        { text: "5. צלילה שנייה: מוסיפים עוד עומק כחול...", image: imageAssets.dip2, type: 'dip' },
        { text: "6. שוב לאוויר: הצבע מתעצם!", image: imageAssets.oxi2, type: 'oxidation' },
        { text: "7. צלילה שלישית: ממשיכים לבנות את הצבע העשיר...", image: imageAssets.dip3, type: 'dip' },
        { text: "8. חשיפה נוספת: עוד כחול שנלכד בסיבים!", image: imageAssets.oxi3, type: 'oxidation' },
         { text: "9. צלילה רביעית: לקראת השיא הכחול...", image: imageAssets.dip4, type: 'dip' },
        { text: "10. חשיפה אחרונה לתהליך הצביעה הבסיסי: הג'ינס כמעט מוכן!", image: imageAssets.oxi4, type: 'oxidation' },
        { text: "11. זהו בד הדנים הגולמי: כהה, נוקשה, ומלא בפוטנציאל לדהייה ייחודית.", image: imageAssets.raw, type: 'raw_denim' },
        { text: "12. הג'ינס הגולמי מוכן לשלב הגימור! מה תבחרו לעשות איתו?", image: imageAssets.raw, type: 'wash_prep' } // Use raw denim image before wash selection
    ];


    function updateDisplay() {
        // Remove previous simulation classes
        fabricDisplay.classList.remove('dipping', 'oxidizing');
        fabricSimulationArea.classList.remove('wash-selected');


        if (currentStep < steps.length) {
            const step = steps[currentStep];
            stepText.textContent = step.text;
            fabricImage.src = step.image;

            // Add animation for image change
             fabricImage.classList.remove('visible'); // Hide current image
            setTimeout(() => {
                 fabricImage.classList.add('visible'); // Show new image with fade/scale effect
             }, 10); // Small delay to re-trigger animation


            // Handle simulation effects based on step type
            if (step.type === 'dip') {
                 fabricDisplay.classList.add('dipping');
                 fabricDisplay.style.backgroundColor = 'transparent'; // Ensure overlay is visible
            } else if (step.type === 'oxidation') {
                 fabricDisplay.classList.add('oxidizing');
                 fabricDisplay.style.backgroundColor = 'transparent'; // Ensure overlay is visible
            } else {
                // Reset background/overlay for non-simulation steps
                 simulationOverlay.style.opacity = 0;
                 if (step.type === 'cotton') {
                      fabricDisplay.style.backgroundColor = 'var(--cotton-white)';
                 } else if (step.type === 'woven') {
                      fabricDisplay.style.backgroundColor = 'var(--cotton-white)';
                 } else if (step.type === 'raw_denim' || step.type === 'wash_prep') {
                     fabricDisplay.style.backgroundColor = 'transparent'; // Image handles color
                 } else {
                      fabricDisplay.style.backgroundColor = 'transparent'; // Default if image is used
                 }
            }


            if (currentStep === steps.length - 1) {
                // Reached transition to wash
                nextStepBtn.style.display = 'none';
                washOptionsDiv.style.display = 'block';
                restartBtn.style.display = 'none'; // Hide restart until wash selected or finish
            } else {
                nextStepBtn.style.display = 'block';
                washOptionsDiv.style.display = 'none';
                restartBtn.style.display = 'none';
            }
        } else {
            // End of process or after wash selection
            // This state is now handled by handleWashSelection or after wash.
            // If somehow get here without wash, show finish text.
             stepText.textContent = "המסע הושלם! בחרו שטיפה לגימור.";
             nextStepBtn.style.display = 'none';
             washOptionsDiv.style.display = 'block'; // Keep wash options visible
             restartBtn.style.display = 'none';
             fabricImage.src = imageAssets.raw; // Show raw denim until wash selected
             fabricImage.classList.add('visible');
             fabricDisplay.style.backgroundColor = 'transparent';
        }
    }

    function handleWashSelection(washType) {
         washOptionsDiv.style.display = 'none';
         nextStepBtn.style.display = 'none';
         restartBtn.style.display = 'block';

         let washName = '';
         let washImage = '';
         let finalTextColor = 'var(--denim-blue-dark)'; // Default color for final text

         switch(washType) {
             case 'raw':
                 washName = 'ג'ינס גולמי (ללא שטיפה)';
                 washImage = imageAssets.raw;
                 break;
             case 'stone':
                 washName = 'סטון ווש (שטיפת אבנים)';
                 washImage = imageAssets.stone;
                 break;
             case 'acid':
                 washName = 'אסיד ווש (שטיפת חומצה לכאורה)';
                 washImage = imageAssets.acid;
                 finalTextColor = '#5a6268'; // Slightly different color for acid wash result text
                 break;
             case 'enzyme':
                 washName = 'אנזים ווש (שטיפה ביולוגית)';
                 washImage = imageAssets.enzyme;
                 break;
             default:
                 washName = 'גימור לא ידוע';
                 washImage = imageAssets.raw; // Fallback
         }

         stepText.textContent = `תוצאה: זהו בד ג'ינס לאחר גימור מסוג "${washName}".`;
         stepText.style.color = finalTextColor;


         // Animate transition to final wash look
         fabricImage.classList.remove('visible'); // Hide current image
         simulationOverlay.style.opacity = 0; // Hide any vat/air overlay

         // Give a moment for animation out, then change src and animate in
         setTimeout(() => {
             fabricImage.src = washImage;
             fabricDisplay.style.backgroundColor = 'transparent'; // Ensure image is visible
             fabricImage.classList.add('visible');
             fabricSimulationArea.classList.add('wash-selected'); // Optional class for wash state styling
         }, 600); // Match transition duration

         currentStep = steps.length; // Mark process as finished for updateDisplay logic (though not strictly needed here)
    }

    function restartProcess() {
        currentStep = 0;
        stepText.style.color = 'var(--denim-blue-dark)'; // Reset text color
        restartBtn.style.display = 'none';
        fabricImage.classList.remove('visible'); // Hide image before restart
        simulationOverlay.style.opacity = 0; // Hide overlay
         fabricDisplay.classList.remove('dipping', 'oxidizing'); // Remove state classes
         fabricSimulationArea.classList.remove('wash-selected');

        // Small delay before updating display to show restart effect
        setTimeout(() => {
            updateDisplay();
        }, 300);
    }


    nextStepBtn.addEventListener('click', () => {
        currentStep++;
        updateDisplay();
    });

    washButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            const washType = event.target.dataset.washType;
            handleWashSelection(washType);
        });
    });

    restartBtn.addEventListener('click', restartProcess);


    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר סיפור הרקע המלא' : 'הצגת/הסתרת סיפור הרקע המלא';
    });

    // Initialize display
    updateDisplay();

</script>