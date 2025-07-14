---
title: "מסע בזמן: אבולוציית עין המצלמה"
english_slug: time-travel-evolution-of-the-camera-eye
category: "מדעי הרוח / היסטוריה של המדע"
tags:
  - אופטיקה
  - היסטוריה
  - צילום
  - ביולוגיה
  - טכנולוגיה
---
# מסע בזמן: אבולוציית עין המצלמה

הצטרפו למסע מרתק אל לב ההיסטוריה של יצירת התמונה! איך קופסה חשוכה עם חור זעיר הפכה למצלמה דיגיטלית מתוחכמת בכיס שלנו? ואיך המכניזם המופלא הזה מחקה ואף מתעלה על עין המצלמה הטבעית ביותר - העין האנושית?

גלו את הצעדים האבולוציוניים שעיצבו את הדרך שבה אנו קולטים ומתעדים את העולם. נסו כל שלב במכניזם ובדקו כיצד הוא משפיע על התמונה הסופית!

<div class="app-container">
    <div class="controls">
        <button data-step="0" class="step-button">קמרה אובסקורה</button>
        <button data-step="1" class="step-button">מצלמת עדשה מוקדמת</button>
        <button data-step="2" class="step-button">מצלמת פילם</button>
        <button data-step="3" class="step-button">מצלמה דיגיטלית</button>
    </div>

    <div class="simulation-area">
        <div class="diagram-container">
             <div class="object animate__animated animate__fadeInLeft">עצם</div>
            <div class="camera-box">
                <div class="aperture"></div>
                <div class="lens"></div>
                <div class="sensor-plane"></div>
                <!-- Ray elements -->
                <div class="ray top-ray"></div>
                <div class="ray center-ray"></div>
                <div class="ray bottom-ray"></div>
                 <!-- Image projected inside the box (for visual cue) -->
                <div class="projected-image"></div>
            </div>
        </div>

        <div class="panels-area">
            <div class="info-panel card animate__animated animate__fadeInRight">
                <h3>מאפיינים נוכחיים</h3>
                <p><strong>שם:</strong> <span id="step-name"></span></p>
                <p><strong>פתח כניסה:</strong> <span id="aperture-type"></span></p>
                <p><strong>מנגנון מיקוד:</strong> <span id="focus-mechanism"></span></p>
                <p><strong>משטח קולט:</strong> <span id="sensor-type"></span></p>
                 <button class="focus-button" style="display: none;">התאם מיקוד</button>
            </div>

            <div class="simulated-image-view card animate__animated animate__fadeInUp">
                <h4>תמונה סופית (סימולציה)</h4>
                <div id="simulated-image">
                    <div class="sim-object"></div>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
     /* Add basic animation library reference if allowed, otherwise skip */
    /* @import url('https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css'); */


    .app-container {
        direction: rtl;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        display: flex;
        flex-direction: column;
        gap: 30px;
        margin-bottom: 40px;
        background-color: #f8f9fa; /* Light background */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        overflow: hidden; /* Ensure animations stay within bounds */
    }

    h1, h2, h3, h4 {
        color: #343a40; /* Dark grey headings */
    }

    p {
        color: #5a6268; /* Slightly lighter text */
    }

    .controls {
        display: flex;
        justify-content: center;
        gap: 15px;
        flex-wrap: wrap;
        padding-bottom: 20px;
        border-bottom: 1px solid #e9ecef;
    }

    .step-button {
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        background-color: #e9ecef; /* Light grey */
        color: #495057; /* Dark grey text */
        border-radius: 25px; /* Pill shape */
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
    }

    .step-button:hover {
        background-color: #dee2e6;
        transform: translateY(-2px);
    }

    .step-button.active {
        background-color: #007bff; /* Primary blue */
        color: white;
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
        transform: translateY(-1px);
    }

     .step-button:active {
         transform: translateY(0);
         box-shadow: 0 2px 4px rgba(0, 123, 255, 0.3);
     }

    .simulation-area {
        display: flex;
        flex-direction: column; /* Stack diagram and panels on small screens */
        gap: 30px;
    }

    .diagram-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px; /* Increased gap */
        min-height: 200px; /* Increased height */
        position: relative;
        padding: 20px; /* Add padding */
        background-color: #ffffff; /* White background for diagram */
        border-radius: 8px;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.05); /* Inner shadow */
         overflow: hidden; /* Keep rays inside */
    }

    .object {
        width: 60px; /* Slightly larger object */
        height: 100px;
        background: linear-gradient(to bottom, #e74c3c, #c0392b); /* Gradient */
        color: white;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        position: relative; /* For animation */
    }


    .camera-box {
        width: 250px; /* Wider box */
        height: 120px; /* Taller box */
        border: 3px solid #343a40; /* Darker border */
        background-color: #495057; /* Dark grey camera body */
        position: relative;
        display: flex;
        align-items: center;
        padding: 0 15px; /* More padding */
        box-sizing: border-box;
        border-radius: 8px;
         overflow: hidden; /* Crucial for ray drawing */
         transform-style: preserve-3d; /* For potential 3D hints */
    }

    .aperture, .lens, .sensor-plane {
         position: absolute;
         top: 50%;
         transform: translateY(-50%);
         transition: all 0.5s ease-in-out; /* Smooth transitions for components */
    }


    .aperture {
        width: 8px; /* Base size */
        height: 8px;
        background-color: white; /* Light appears to pass through */
        border-radius: 50%;
        left: 10px; /* Closer to front edge */
         z-index: 2; /* Above rays */
    }

    .lens {
        width: 30px; /* Wider lens */
        height: 80px; /* Taller lens */
        background: linear-gradient(to right, rgba(173, 216, 230, 0.8), rgba(0, 123, 255, 0.6)); /* Gradient blue */
        border: 1px solid #007bff;
        border-radius: 8px;
        left: 10px; /* Default position */
        display: none; /* Hidden by default */
        z-index: 1; /* Below aperture/sensor visual cues */
        box-shadow: 0 0 10px rgba(0, 123, 255, 0.5);
    }

    .sensor-plane {
        width: 15px; /* Wider sensor */
        height: 90px; /* Taller sensor */
        background-color: #ced4da; /* Light grey default */
        border: 2px dashed #6c757d; /* Dashed border */
        right: 10px; /* At the back */
        z-index: 1;
    }

    /* Ray Styling - Using Divs for easier positioning/animation */
    .ray {
        position: absolute;
        height: 2px; /* Thin line */
        background: linear-gradient(to right, rgba(255, 255, 0, 0.8), rgba(255, 255, 0, 0)); /* Yellow light effect */
        transform-origin: left center; /* Rotate from the start point */
        z-index: 0; /* Below camera components */
        pointer-events: none; /* Don't interfere with clicks */
         transition: all 0.5s ease-in-out; /* Animate ray movement/rotation */
    }

    .ray.top-ray { top: 50%; left: 0; } /* Base position */
    .ray.center-ray { top: 50%; left: 0; background: rgba(255, 255, 255, 0.5); /* White for center ray */ }
    .ray.bottom-ray { top: 50%; left: 0; }


    /* Projected Image inside Camera (optional visual aid) */
    .projected-image {
         position: absolute;
         right: 10px; /* Near the sensor */
         top: 50%;
         width: 30px; /* Smaller visual cue */
         height: 50px;
         background-color: rgba(231, 76, 60, 0.5); /* Semi-transparent red */
         transform: translateY(-50%) rotateZ(180deg); /* Always inverted inside */
         opacity: 0.3; /* Subtle */
         transition: all 0.5s ease-in-out;
         display: none; /* Shown when image forms */
    }


     /* --- Step Specific Styles --- */

    /* Step 0: Camera Obscura */
    .camera-box[data-step="0"] .aperture {
        width: 5px; height: 5px; /* Tiny hole */
        background-color: #ffffff;
        left: 15px;
         display: block;
    }
    .camera-box[data-step="0"] .lens { display: none; }
    .camera-box[data-step="0"] .sensor-plane { background-color: #e9ecef; border: 2px dashed #adb5bd; width: 15px; } /* Screen/surface */
     .camera-box[data-step="0"] .projected-image { display: block; } /* Show inner image */

    /* Step 1: Early Lens Camera */
    .camera-box[data-step="1"] .aperture { display: none; } /* Lens acts as aperture */
    .camera-box[data-step="1"] .lens {
        display: block;
        left: 10px; /* At the front */
        width: 30px; height: 80px;
    }
    .camera-box[data-step="1"] .sensor-plane { background-color: #e9ecef; border: 2px dashed #adb5bd; width: 15px; } /* Screen/surface, maybe adjustable position */
     .camera-box[data-step="1"] .projected-image { display: block; } /* Show inner image */

    /* Step 2: Film Camera */
    .camera-box[data-step="2"] .aperture { display: none; }
    .camera-box[data-step="2"] .lens { display: block; left: 10px; width: 30px; height: 80px;}
    .camera-box[data-step="2"] .sensor-plane { background-color: #6f42c1; border: none; width: 15px; } /* Purple for Film */
     .camera-box[data-step="2"] .projected-image { display: block; } /* Show inner image */

    /* Step 3: Digital Camera */
    .camera-box[data-step="3"] .aperture { display: none; }
    .camera-box[data-step="3"] .lens { display: block; left: 10px; width: 30px; height: 80px;}
    .camera-box[data-step="3"] .sensor-plane { background-color: #28a745; border: none; width: 15px; } /* Green for Digital Sensor */
     .camera-box[data-step="3"] .projected-image { display: block; } /* Show inner image */


    /* --- Panels Area --- */
    .panels-area {
        display: flex;
        flex-direction: row; /* Side-by-side on wider screens */
        gap: 20px;
         flex-wrap: wrap; /* Wrap on smaller screens */
         justify-content: center; /* Center panels when wrapped */
    }

    .card {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
         flex-grow: 1; /* Allow cards to grow */
         flex-basis: 0; /* Base size for flex growth */
         min-width: 250px; /* Minimum width before wrapping */
    }

    .info-panel {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

     .info-panel p {
        margin: 0;
        font-size: 0.95em;
        line-height: 1.5;
    }

    .info-panel strong {
        color: #007bff; /* Highlight info titles */
    }

    .focus-button {
        margin-top: 15px;
        padding: 10px 15px;
        font-size: 0.95em;
        cursor: pointer;
        border: none;
        background-color: #ffc107; /* Warning yellow */
        color: #343a40;
        border-radius: 5px;
        transition: background-color 0.3s ease;
        align-self: flex-start; /* Align button left */
    }

    .focus-button:hover {
        background-color: #ffda6a;
    }

    .simulated-image-view {
         display: flex;
         flex-direction: column;
         align-items: center; /* Center image and title */
    }

    #simulated-image {
        width: 180px; /* Size of the simulated output */
        height: 240px; /* Maintain aspect ratio relative to object */
        margin-top: 10px;
        border: 2px solid #343a40; /* Dark border like a screen */
        background-color: #212529; /* Dark screen background */
        position: relative;
        overflow: hidden;
        border-radius: 5px;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.5); /* Inner shadow */
        transition: all 0.6s ease-in-out; /* Smooth transition for image state */
    }

    #simulated-image .sim-object {
        width: 60px; /* Matches object size */
        height: 100px;
        background: linear-gradient(to bottom, #e74c3c, #c0392b); /* Matches object gradient */
        position: absolute;
        /* Initial state (Camera Obscura / Film) - Inverted, blurry, dim */
        bottom: 50%; /* Default to inverted */
        left: 50%;
        transform: translate(-50%, 50%); /* Center while maintaining inversion */
        filter: blur(8px) brightness(40%); /* Default blurry and dim */
        opacity: 0.8;
        transition: all 0.6s ease-in-out; /* Animate position, blur, opacity */
        will-change: transform, filter, opacity; /* Optimize animation */
    }

     /* --- Simulated Image Styling per step --- */

    #simulated-image[data-step="0"] .sim-object {
         bottom: 50%; left: 50%;
         transform: translate(-50%, 50%) scaleY(-1); /* Explicitly scaleY(-1) for clarity */
         filter: blur(8px) brightness(40%); /* Dim and blurry */
         opacity: 0.8;
    }

    #simulated-image[data-step="1"] .sim-object,
    #simulated-image[data-step="2"] .sim-object {
        /* Lens/Film - Inverted, Sharper, Brighter (when focused) */
         bottom: 50%; left: 50%;
         transform: translate(-50%, 50%) scaleY(-1); /* Still inverted */
         filter: blur(0px) brightness(100%); /* Assume focused state via JS/CSS class */
         opacity: 1;
    }

    #simulated-image[data-step="3"] .sim-object {
        /* Digital - Upright, Sharp, Full Brightness */
         top: 50%; left: 50%;
         transform: translate(-50%, -50%) scaleY(1); /* Upright */
         filter: blur(0px) brightness(100%);
         opacity: 1;
         /* Simulate color: Maybe add a border or subtle text? */
         box-shadow: 0 0 15px rgba(40, 167, 69, 0.8); /* Hint of green digital */
    }

    /* --- Focus Simulation State --- */
    #simulated-image.is-blurry .sim-object {
         filter: blur(8px) brightness(100%); /* Blurry but bright (lens) */
         /* Optional: change position slightly to show focus plane mismatch */
         /* transform: translate(-50%, 50%) scaleY(-1) scale(0.9); */
    }


    .explanation-button {
        display: block;
        width: fit-content;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: 1px solid #007bff;
        background-color: #007bff;
        color: white;
        border-radius: 25px;
        transition: background-color 0.3s ease, transform 0.3s ease;
         box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
    }
     .explanation-button:hover {
         background-color: #0056b3;
         transform: translateY(-2px);
     }
     .explanation-button:active {
         transform: translateY(0);
     }

    .explanation {
        border-top: 1px solid #ced4da;
        margin-top: 40px;
        padding-top: 30px;
        display: none; /* Hidden by default */
        background-color: #e9ecef; /* Light grey background */
        padding: 20px;
        border-radius: 8px;
    }

    .explanation h2, .explanation h3 {
        color: #343a40;
        margin-top: 25px;
        margin-bottom: 12px;
        border-bottom: 1px solid #adb5bd; /* Subtle separator */
        padding-bottom: 5px;
    }

    .explanation p {
        line-height: 1.7;
        margin-bottom: 15px;
        color: #5a6268;
    }

    .explanation ul {
        margin-bottom: 15px;
        padding-right: 20px; /* Indent lists */
    }

    .explanation ul li {
        margin-bottom: 8px;
        line-height: 1.6;
         color: #5a6268;
    }

    .explanation ul li strong {
        color: #007bff; /* Highlight key terms in explanation */
    }

    /* --- Responsive Adjustments --- */
    @media (min-width: 768px) {
        .simulation-area {
            flex-direction: row; /* Side-by-side on larger screens */
            align-items: flex-start; /* Align items to the top */
        }
         .diagram-container {
             flex-basis: 60%; /* Diagram takes more space */
             flex-grow: 0;
             min-height: 300px; /* Taller diagram */
         }
         .panels-area {
             flex-direction: column; /* Stack panels */
             flex-basis: 40%; /* Panels take less space */
             flex-grow: 0;
         }
         .card {
             flex-basis: auto; /* Remove base size when stacked */
         }
          .info-panel {
              min-height: 200px; /* Give info panel some height */
          }
           #simulated-image-view {
               align-items: center; /* Ensure simulated image is centered vertically */
           }
    }


</style>

<button class="explanation-button">הצג הסבר מלא</button>

<div class="explanation">
    <h2>הסבר: מסע בזמן - אבולוציית עין המצלמה</h2>

    <h3>מהי מערכת 'עין מצלמה'?</h3>
    <p>בבסיסה, מערכת 'עין מצלמה' היא מכשיר פלאי המאסף אור מהעולם סביבנו, מעבד אותו ליצירת דמות של העצמים, ורושם או קולט את הדמות הזו. זה יכול להיות פלא טבעי כמו העין שלכם, או פלא טכנולוגי כמו מצלמת הטלפון הנייד. העיקרון המרכזי הוא שליטה באור כדי ליצור תמונה ברורה.</p>

    <h3>עיקרון הקמרה אובסקורה: הקסם של הקופסה החשוכה והחור הזעיר</h3>
    <p>המצלמה האובסקורה (בלטינית: "חדר חשוך") היא הדוגמה הפשוטה ביותר. דמיינו חדר אטום לחלוטין, עם חור קטן בקיר אחד. אור מעצמים מחוץ לחדר חודר דרך החור הזה ומקרין תמונה של העולם החיצון על הקיר הנגדי - אבל הפוכה לחלוטין!</p>
    <ul>
        <li><strong>איך נוצרת הדמות?</strong> קרני האור מכל נקודה על העצם החיצוני מתפשטות לכל עבר. רק הקרניים המצליחות לעבור דרך החור הצר ממשיכות פנימה. כשהן מגיעות לקיר הנגדי, הן יוצרות נקודה אחת שתואמת לנקודה המקורית על העצם. הקרניים מחלקו העליון של העצם עוברות דרך החור ופוגעות בחלק התחתון של הקיר הפנימי, ולהיפך. זה גורם לדמות להיות <strong>הפוכה</strong> ומעוותת צדדית.</li>
        <li><strong>האתגר: בהירות מול חדות:</strong> חור קטן מדי מכניס מעט אור, והתמונה עמומה. חור גדול מדי מכניס יותר אור, אבל קרניים מנקודות שונות על העצם יכולות לעבור דרך אזורים שונים של החור ולפגוע באותה נקודה על הקיר הפנימי, מה שיוצר תמונה <strong>מטושטשת</strong>. תמיד יש פשרה, והתמונה בקמרה אובסקורה תמיד תהיה מעט מטושטשת ועמומה.</li>
    </ul>

    <h3>המהפכה: עדשות - לאסוף אור ולמקד אותו כמו קסם</h3>
    <p>הצעד הגדול הבא היה גילוי הכוח של עדשות. עדשה (או מערכת מורכבת יותר של עדשות) מחליפה את החור הזעיר. היא מסוגלת לאסוף כמות גדולה בהרבה של אור מכל נקודה על העצם ולכופף את הקרניים הללו בצורה מדויקת כך שיתמקדו לנקודה אחת חדה על המשטח הקולט.</p>
    <ul>
        <li><strong>אור רב יותר, תמונה בהירה יותר:</strong> עדשה עם קוטר גדול יכולה לאסוף פי כמה וכמה יותר אור מחור קטן, וכך ליצור תמונה בהירה וברורה בהרבה.</li>
        <li><strong>חדות מדהימה:</strong> עדשות מתוכננות באופן אופטי מדויק כדי למקד קרני אור מנקודה אחת בעולם לנקודה אחת (אידיאלית) בתוך המצלמה. זה מאפשר ליצור דמויות <strong>חדות</strong> וברורות.</li>
        <li><strong>הפוקוס מתעורר לחיים:</strong> עדשה ממקדת את האור במישור מסוים. רק עצמים הנמצאים במרחק מסוים מהעדשה (ב"מישור המוקד") ייראו חדים על המשטח הקולט. במצלמות עם עדשות, ניתן לשנות את המיקוד (לרוב על ידי שינוי המרחק בין העדשה למשטח הקולט) כדי לקבל תמונה חדה של עצמים במרחקים שונים.</li>
    </ul>

    <h3>תופסים את הרגע: אמצעי רישום התמונה לאורך הדורות</h3>
    <p>אחרי שהאור עבר דרך הפתח ויצר דמות, איך שומרים אותה לנצח? האתגר הזה הוביל לפיתוחים טכנולוגיים מהפכניים:</p>
    <ul>
        <li><strong>פלטות ופילם רגישים לאור:</strong> המצאת הצילום התבססה על חומרים כימיים המגיבים לאור (כמו מלחי כסף). הדמות האופטית הוקרנה על פלטה או סרט (פילם) מצופים בחומרים אלו. האור יצר שינוי כימי, ולאחר "פיתוח" במעבדה, התקבלה תמונה קבועה. זה היה קסם שאיפשר לתעד רגעים בדיוק מדהים.</li>
        <li><strong>חיישנים דיגיטליים: המהפכה הדיגיטלית:</strong> המצלמה הדיגיטלית מחליפה את הכימיה של הפילם באלקטרוניקה. חיישנים דיגיטליים (כמו CCD או CMOS) מורכבים ממיליוני תאים זעירים (פיקסלים) שכל אחד מהם ממיר אור לאות חשמלי. אותות אלו מעובדים דיגיטלית ומרכיבים את התמונה שאנו רואים על המסך או שומרים כקובץ. היתרונות? מיידיות, קלות שיתוף, אחסון אינסופי ויכולת עריכה כמעט בלתי מוגבלת. הבונוס הגדול: המצלמה הדיגיטלית מסוגלת <strong>לתקן את היפוך התמונה</strong> באופן אוטומטי באמצעות עיבוד תמונה!</li>
    </ul>

    <h3>הדמיון המדהים: העין הביולוגית מול המצלמה הטכנולוגית</h3>
    <p>אל לנו לשכוח את המצלמה המדהימה ביותר שיש - העין שלנו! מבנה העין מקביל באופן מרתק למצלמה טכנולוגית, וממחיש את העקרונות האופטיים האוניברסליים:</p>
    <ul>
        <li><strong>קרנית:</strong> כמו השכבה הקדמית של עדשת מצלמה, שוברת את רוב האור הנכנס.</li>
        <li><strong>אישון:</strong> פתח משתנה בגודלו (נשלט על ידי הקשתית, "הצמצם" של העין) השולט בכמות האור הנכנסת.</li>
        <li><strong>עדשה:</strong> ממש כמו עדשה במצלמה, ממקדת את האור. אך לעדשת העין יכולת מופלאה: היא משנה את צורתה ("אקומודציה") כדי להתמקד אוטומטית על עצמים במרחקים שונים - מנגנון מיקוד אוטומטי ביולוגי!</li>
        <li><strong>רשתית:</strong> המשטח האחורי של העין, המרופד בקולטני אור (פוטורצפטורים) הרגישים לצבע (מדוכים) ולעוצמת אור (קנים). זו המקבילה הביולוגית לפילם או לחיישן הדיגיטלי. האותות מהרשתית נשלחים למוח, שמעבד אותם ויוצר את התמונה התלת-ממדית, הצבעונית והישרה שאנו רואים.</li>
    </ul>
    <p>ההשראה ההדדית בין העין לטכנולוגיה ברורה. הבנת העין עזרה לבנות מצלמות טובות יותר, ופיתוח המצלמות העמיק את ההבנה שלנו על הראייה. זהו סיפור מרתק של טבע וטכנולוגיה משתלבים יחד במסע אחר יצירת התמונה המושלמת.</p>
</div>

<script>
    const steps = [
        {
            name: "קמרה אובסקורה",
            aperture: "חור מחט זעיר",
            focus: "קבוע (חדות נמוכה)",
            sensor: "משטח הקרנה (נייר/מסך)",
            imageSim: { blur: 8, brightness: 0.4, inverted: true, color: false },
            showFocusButton: false
        },
        {
            name: "מצלמת עדשה מוקדמת",
            aperture: "עדשה יחידה",
            focus: "ידני (שינוי מרחק)",
            sensor: "משטח הקרנה / לוח רגיש לאור",
            imageSim: { blur: 0, brightness: 1, inverted: true, color: false },
            showFocusButton: true // Can simulate focus adjustment
        },
        {
            name: "מצלמת פילם",
            aperture: "מערכת עדשות עם צמצם",
            focus: "ידני/אוטומטי",
            sensor: "פילם רגיש לאור",
            imageSim: { blur: 0, brightness: 1, inverted: true, color: false }, // Simulate sharpness/brightness for sim
            showFocusButton: true // Can simulate focus adjustment
        },
        {
            name: "מצלמה דיגיטלית",
            aperture: "מערכת עדשות עם צמצם",
            focus: "אוטומטי מהיר",
            sensor: "חיישן דיגיטלי (CCD/CMOS)",
            imageSim: { blur: 0, brightness: 1, inverted: false, color: true },
             showFocusButton: true // Can simulate focus (auto) or just show it's sharp
        }
    ];

    const buttons = document.querySelectorAll('.step-button');
    const diagramContainer = document.querySelector('.camera-box');
    const simulatedImageDiv = document.getElementById('simulated-image');
    const stepNameSpan = document.getElementById('step-name');
    const apertureTypeSpan = document.getElementById('aperture-type');
    const focusMechanismSpan = document.getElementById('focus-mechanism');
    const sensorTypeSpan = document.getElementById('sensor-type');
    const focusButton = document.querySelector('.focus-button');

    const rayTop = document.querySelector('.ray.top-ray');
    const rayCenter = document.querySelector('.ray.center-ray');
    const rayBottom = document.querySelector('.ray.bottom-ray');
    const diagramObject = document.querySelector('.diagram-container .object');

    const explanationButton = document.querySelector('.explanation-button');
    const explanationDiv = document.querySelector('.explanation');

    let currentStepIndex = -1; // Start with no step active

    function calculateRayPath(stepIndex) {
        const objectRect = diagramObject.getBoundingClientRect();
        const cameraRect = diagramContainer.getBoundingClientRect(); // Use container for positioning context
        const aperture = diagramContainer.querySelector('.aperture');
        const lens = diagramContainer.querySelector('.lens');
        const sensor = diagramContainer.querySelector('.sensor-plane');

        // Calculate positions relative to diagramContainer
        const objX = objectRect.left - cameraRect.left + objectRect.width; // Right edge of object
        const objTopY = objectRect.top - cameraRect.top;
        const objCenterY = objectRect.top - cameraRect.top + objectRect.height / 2;
        const objBottomY = objectRect.top - cameraRect.top + objectRect.height;

        let passageX, passageYCenter; // Point where rays pass through aperture/lens
        const sensorX = sensor.offsetLeft; // Left edge of sensor relative to camera-box
        const cameraBoxLeftRelativeToContainer = diagramContainer.querySelector('.camera-box').offsetLeft;

         // The actual passage point is relative to the camera-box, need to translate its X pos
        const camPassageXRelativeToContainer = cameraBoxLeftRelativeToContainer + (stepIndex === 0 ? aperture.offsetLeft + aperture.offsetWidth/2 : lens.offsetLeft + lens.offsetWidth/2);


        // For simplicity in calculation, let's assume the effective pinhole/lens point is centered vertically
        passageYCenter = cameraRect.height / 2; // Vertical center of diagram container

        const rays = [];

        // Calculate ray paths
        // Ray from top of object through passage to sensor
        let dx_top = sensorX + cameraBoxLeftRelativeToContainer - objX;
        let dy_top = (cameraBoxLeftRelativeToContainer + sensor.offsetTop + sensor.offsetHeight/2) - objTopY; // Approximate sensor center Y relative to obj top Y
         // For pinhole/lens, rays cross. Y on sensor is inverted relative to object Y.
         let sensorTargetY_top = passageYCenter + (passageYCenter - objTopY) * ( (sensorX + cameraBoxLeftRelativeToContainer - camPassageXRelativeToContainer) / (camPassageXRelativeToContainer - objX) );


        // Ray from center of object straight through passage to sensor
        let dx_center = sensorX + cameraBoxLeftRelativeToContainer - objX;
        let dy_center = passageYCenter - objCenterY;
        let sensorTargetY_center = passageYCenter; // Center ray goes straight through center

         // Ray from bottom of object through passage to sensor
        let dx_bottom = sensorX + cameraBoxLeftRelativeToContainer - objX;
        let dy_bottom = (cameraBoxLeftRelativeToContainer + sensor.offsetTop + sensor.offsetHeight/2) - objBottomY;
         let sensorTargetY_bottom = passageYCenter + (passageYCenter - objBottomY) * ( (sensorX + cameraBoxLeftRelativeToContainer - camPassageXRelativeToContainer) / (camPassageXRelativeToContainer - objX) );


        // Calculate total distance and angle for each ray
        const distTop = Math.sqrt(dx_top * dx_top + (sensorTargetY_top - objTopY) * (sensorTargetY_top - objTopY));
        const angleTop = Math.atan2(sensorTargetY_top - objTopY, dx_top) * 180 / Math.PI;

        const distCenter = Math.sqrt(dx_center * dx_center + (sensorTargetY_center - objCenterY) * (sensorTargetY_center - objCenterY));
        const angleCenter = Math.atan2(sensorTargetY_center - objCenterY, dx_center) * 180 / Math.PI;


        const distBottom = Math.sqrt(dx_bottom * dx_bottom + (sensorTargetY_bottom - objBottomY) * (sensorTargetY_bottom - objBottomY));
        const angleBottom = Math.atan2(sensorTargetY_bottom - objBottomY, dx_bottom) * 180 / Math.PI;


         // Position rays at the object's edge
        rayTop.style.top = `${objTopY}px`;
        rayTop.style.left = `${objX}px`;
        rayTop.style.width = `${distTop}px`;
        rayTop.style.transform = `rotate(${angleTop}deg)`;
        rayTop.style.opacity = 1;


        rayCenter.style.top = `${objCenterY}px`;
        rayCenter.style.left = `${objX}px`;
        rayCenter.style.width = `${distCenter}px`;
        rayCenter.style.transform = `rotate(${angleCenter}deg)`;
        rayCenter.style.opacity = 0.7; /* Center ray slightly less prominent */


        rayBottom.style.top = `${objBottomY}px`;
        rayBottom.style.left = `${objX}px`;
        rayBottom.style.width = `${distBottom}px`;
        rayBottom.style.transform = `rotate(${angleBottom}deg)`;
        rayBottom.style.opacity = 1;


         // Position the projected image inside the camera box based on ray crossing
         const projectedImage = diagramContainer.querySelector('.projected-image');
         if (stepIndex === 0 || stepIndex === 1 || stepIndex === 2) {
             // For inverted images (Obscura, Lens, Film), position at sensor
             const sensorCenterYRelativeToContainer = sensor.offsetTop + sensor.offsetHeight/2 + cameraBoxLeftRelativeToContainer - cameraRect.left;
              // Calculate where the image should be vertically centered on the sensor
             const projectedImageCenterY = sensorCenterYRelativeToContainer + (passageYCenter - objCenterY) * ( (sensor.offsetLeft + sensor.offsetWidth/2 + cameraBoxLeftRelativeToContainer - camPassageXRelativeToContainer) / (camPassageXRelativeToContainer - objX) );

             projectedImage.style.right = `${diagramContainer.querySelector('.camera-box').offsetWidth - (sensor.offsetLeft + sensor.offsetWidth/2)}px`; /* Center of sensor relative to camera box right edge */
             projectedImage.style.top = `${projectedImageCenterY}px`; // Position vertically based on calculation
             projectedImage.style.transform = `translateY(-50%) rotateZ(180deg)`;
             projectedImage.style.display = 'block'; // Ensure visible
         } else {
              // Digital - image processed, conceptually upright, maybe hide projected or show processed
              projectedImage.style.display = 'none'; // Hide the raw projected image
         }
    }


    function updateSimulation(stepIndex, isFocusing = false) {
        if (stepIndex === currentStepIndex && !isFocusing) return; // Prevent unnecessary updates if not focusing state change

        const stepData = steps[stepIndex];
        currentStepIndex = stepIndex; // Update current step

        // Update diagram appearance based on step
        diagramContainer.setAttribute('data-step', stepIndex);

        // Update info panel
        stepNameSpan.textContent = stepData.name;
        apertureTypeSpan.textContent = stepData.aperture;
        focusMechanismSpan.textContent = stepData.focus;
        sensorTypeSpan.textContent = stepData.sensor;

         // Update simulated image appearance (CSS handles most visual changes via data-step)
         // Now also handle blur/focus explicitly via class
        simulatedImageDiv.setAttribute('data-step', stepIndex);

         // Handle blur/focus based on step and isFocusing flag
         if (stepIndex === 0) {
             simulatedImageDiv.classList.add('is-blurry'); // Obscura is always blurry
             focusButton.style.display = 'none';
         } else if (stepIndex >= 1) {
             focusButton.style.display = stepData.showFocusButton ? 'block' : 'none';
             if (isFocusing) {
                 simulatedImageDiv.classList.add('is-blurry');
                 focusButton.textContent = 'התאם מיקוד';
             } else {
                 simulatedImageDiv.classList.remove('is-blurry');
                 focusButton.textContent = 'הצג מטושטש';
             }
         } else {
             simulatedImageDiv.classList.remove('is-blurry');
             focusButton.style.display = 'none';
         }


        // Update active button state
        buttons.forEach((btn, index) => {
            if (index === stepIndex) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });

         // Recalculate and draw rays with a slight delay to allow diagram elements to update positions
         setTimeout(() => {
            calculateRayPath(stepIndex);
         }, 50); // Small delay to ensure elements are positioned
    }

    // Add event listeners to buttons
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const stepIndex = parseInt(button.getAttribute('data-step'));
            updateSimulation(stepIndex);
        });
    });

    // Add event listener for focus button
    focusButton.addEventListener('click', () => {
        const isCurrentlyBlurred = simulatedImageDiv.classList.contains('is-blurry');
        updateSimulation(currentStepIndex, !isCurrentlyBlurred);
    });


    // Add event listener for the explanation button
    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר הסבר מלא' : 'הצג הסבר מלא';
         // Scroll to explanation if shown? Optional.
         if (isHidden) {
            explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });

    // Initialize with the first step
    updateSimulation(0);
</script>
---
```