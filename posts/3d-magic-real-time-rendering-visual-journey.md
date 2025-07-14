---
title: "קסם התלת-ממד: מסע ויזואלי אל תהליך הרינדור בזמן אמת"
english_slug: 3d-magic-real-time-rendering-visual-journey
category: "טכנולוגיה / מדעי המחשב"
tags:
  - גרפיקה ממוחשבת
  - תלת-ממד
  - רינדור
  - מנועי משחק
  - Pipeline
  - GPU
---
# קסם התלת-ממד: מסע ויזואלי אל תהליך הרינדור בזמן אמת

איך קורה שדמות תלת-ממדית מורכבת מופיעה על המסך הדו-ממדי שלכם תוך אלפיות שנייה? מאחורי הקלעים של משחקי מחשב, סרטי אנימציה וסימולציות גרפיות עומד תהליך מדהים, מהיר ומדויק שנקרא 'Pipeline הרינדור'. בואו נצלול לתוך הקסם הזה ונראה שלב אחר שלב איך מודל וירטואלי הופך לתמונה חיה על המסך.

<div class="app-container">
    <div class="viewer">
        <canvas id="renderCanvas"></canvas>
    </div>
    <div class="controls">
        <h2>שלבי Pipeline הרינדור - צפו והתנסו!</h2>

        <div class="control-step">
            <h3>1. Model Transformation<span class="step-label"> (העולם והאובייקט)</span></h3>
            <p>מקמו, סובבו ושנו גודל לאובייקט בעולם התלת-ממדי. זהו המודל מטריקס (Model Matrix).</p>
            <div class="controls-grid">
                <div><label for="posX">מיקום X:</label> <input type="range" id="posX" min="-5" max="5" value="0" step="0.1"></div>
                <div><label for="posY">מיקום Y:</label> <input type="range" id="posY" min="-5" max="5" value="0" step="0.1"></div>
                <div><label for="posZ">מיקום Z:</label> <input type="range" id="posZ" min="-15" max="0" value="-5" step="0.1"></div>
                <div><label for="rotX">סיבוב X:</label> <input type="range" id="rotX" min="0" max="360" value="0" step="1"></div>
                <div><label for="rotY">סיבוב Y:</label> <input type="range" id="rotY" min="0" max="360" value="0" step="1"></div>
                <div><label for="rotZ">סיבוב Z:</label> <input type="range" id="rotZ" min="0" max="360" value="0" step="1"></div>
                <div><label for="scale">קנה מידה:</label> <input type="range" id="scale" min="0.1" max="5" value="1" step="0.1"></div>
             </div>
        </div>

        <div class="control-step">
            <h3>2. View Transformation<span class="step-label"> (מנקודת מבט המצלמה)</span></h3>
            <p>מקמו את המצלמה בעולם. זהו המבט מטריקס (View Matrix) - היפוך מטריצת המודל של המצלמה.</p>
            <div class="controls-grid">
                 <div><label for="camPosX">מיקום מצלמה X:</label> <input type="range" id="camPosX" min="-10" max="10" value="0" step="0.1"></div>
                <div><label for="camPosY">מיקום מצלמה Y:</label> <input type="range" id="camPosY" min="-10" max="10" value="0" step="0.1"></div>
                <div><label for="camPosZ">מיקום מצלמה Z:</label> <input type="range" id="camPosZ" min="-20" max="-1" value="-10" step="0.1"></div>
                <div><label for="camLookY">מבט מצלמה Y:</label> <input type="range" id="camLookY" min="-2" max="2" value="0" step="0.05"></div>
            </div>
        </div>

         <div class="control-step">
            <h3>3. Projection Transformation<span class="step-label"> (אל מסך דו-ממדי)</span></h3>
            <p>החליטו איך למפות את העולם התלת-ממדי למסך הדו-ממדי (Projection Matrix).</p>
             <div class="controls-grid">
                 <div>
                     <label for="projectionType">סוג היטל:</label>
                     <select id="projectionType">
                         <option value="perspective">Perspective (פרספקטיבה)</option>
                         <option value="orthographic">Orthographic (אורתוגרפי)</option>
                     </select>
                 </div>
                 <div id="perspectiveControls" class="grid-col-span-2">
                    <label for="fov">שדה ראייה (FOV):</label> <input type="range" id="fov" min="30" max="120" value="75" step="1">
                 </div>
                 <div id="orthographicControls" class="grid-col-span-2" style="display: none;">
                     <label for="orthoSize">גודל אורתוגרפי:</label> <input type="range" id="orthoSize" min="1" max="20" value="5" step="0.1">
                 </div>
                 <div class="grid-col-span-2"><button id="highlightClipping">הצג שדה ראייה (Frustum)</button></div>
             </div>
        </div>

        <div class="control-step">
            <h3>4. Clipping & Rasterization<span class="step-label"> (הפיכה לפיקסלים)</span></h3>
            <p>גאומטריה מחוץ לשדה הראייה נחתכת. מה שנשאר הופך לאוסף פיקסלים על המסך. </p>
             <p><small>(שלבים אלו מתרחשים "מאחורי הקלעים", האפליקציה מציגה את התוצאה הדו-ממדית הסופית)</small></p>
        </div>

         <div class="control-step">
            <h3>5. Fragment Processing & Depth Testing<span class="step-label"> (צבע סופי ונראות)</span></h3>
            <p>חשבו את הצבע הסופי של כל פיקסל (Shading, Texturing) וקבעו מי גלוי (Z-buffer).</p>
             <div class="controls-grid">
                 <div><label for="enableShading">הפעל תאורה:</label> <input type="checkbox" id="enableShading" checked></div>
                 <div><label for="enableTexture">הפעל טקסטורה:</label> <input type="checkbox" id="enableTexture"></div>
                 <div class="grid-col-span-2"><label for="enableDepthTest">הפעל בדיקת עומק (Z-Test):</label> <input type="checkbox" id="enableDepthTest" checked></div>
                 <div class="grid-col-span-2"><small>(כבה בדיקת עומק כדי לראות אובייקטים מרוחקים מסתירים קרובים!)</small></div>
            </div>
        </div>

    </div>
</div>

<button id="toggleExplanation">הצג / הסתר הסבר מפורט</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מפורט: Pipeline הרינדור בזמן אמת</h2>

    <h3>מבוא: מהו Pipeline הרינדור ולמה הוא קריטי?</h3>
    דמיינו שאתם בונים עולם וירטואלי. יש בו אובייקטים תלת-ממדיים, מצלמה, ותאורה. איך כל זה הופך לתמונה שנראית לכם על המסך? זה התפקיד של Pipeline הרינדור! זוהי סדרת שלבים מוגדרת מראש, המבוצעת במהירות מסחררת (בעיקר ע"י כרטיס המסך - GPU), שלוקחת נתונים תלת-ממדיים גולמיים והופכת אותם לפיקסלים צבעוניים. הבנת ה-Pipeline היא המפתח ליצירת גרפיקה מרהיבה, אופטימיזציה של ביצועים ויזואליים, ופתרון בעיות תצוגה בגרפיקה ממוחשבת בזמן אמת (משחקים, VR, AR, סימולציות).

    <h3>מסע הקודקודים והפיקסלים ב-Pipeline</h3>
    ה-Pipeline מחולק לשלבים המשפיעים על גאומטריה (קודקודי האובייקטים) ושלבים המשפיעים על רסטריזציה (פיקסלים).

    <h3>World Space & Model Transformation: המודל נכנס לעולם</h3>
    כל אובייקט תלת-ממדי נוצר במקור במרחב "שלו" (Local Space), עם ראשית צירים בנקודת ייחוס פנימית. שלב **Model Transformation** מעביר את קודקודי האובייקט ממרחב מקומי זה אל "מרחב העולם" (World Space), שהוא המרחב הכללי שבו נמצאים כל האובייקטים, המצלמה והתאורה. זה נעשה באמצעות הכפלת קודקודי האובייקט ב-**Model Matrix**, מטריצה המייצגת את פעולות המיקום (Translate), הסיבוב (Rotate) ושינוי הגודל (Scale) של האובייקט בעולם. *באפליקציה למעלה, הזזת הסליידרים תחת שלב זה משנה את ה-Model Matrix של הקובייה.*

    <h3>World Space to View Space: המבט מהמצלמה</h3>
    עכשיו כשהאובייקטים נמצאים בעולם, עלינו להבין איפה הם נמצאים *ביחס למצלמה*. שלב **View Transformation** מעביר את כל האובייקטים ואת שאר העולם ממרחב העולם למרחב חדש שנקרא "מרחב מבט" (View Space or Camera Space). במרחב זה, המצלמה ממוקמת תמיד בראשית הצירים (0,0,0), והיא מביטה בכיוון מוסכם (לרוב ציר Z השלילי). הטרנספורמציה נעשית על ידי הכפלת הקודקודים ב-**View Matrix**, שהיא למעשה ההופכית של מטריצת המודל של המצלמה עצמה. *באפליקציה, הזזת סליידרי המצלמה משנה את ה-View Matrix.*

    <h3>View Space to Projection Space: הפיכה לדו-ממד (כמעט)</h3>
    זהו שלב מרכזי שבו אנו מתחילים להכין את הנתונים למסך הדו-ממדי. שלב **Projection Transformation** ממפה את נפח העולם הגלוי מנקודת המבט של המצלמה (שנקרא **Frustum** בהיטל פרספקטיבי או **Box** בהיטל אורתוגרפי) אל נפח קנוני קבוע (לרוב קוביית NDC - Normalised Device Coordinates), ללא קשר לגודל המסך. הטרנספורמציה נעשית על ידי הכפלת הקודקודים ב-**Projection Matrix**. ישנם שני סוגי היטלים עיקריים:
    *   **היטל פרספקטיבי (Perspective)**: יוצר תחושת עומק וריאליזם; אובייקטים קרובים נראים גדולים יותר. המטריצה לוקחת בחשבון את שדה הראייה (FOV) ויחסי המסך.
    *   **היטל אורתוגרפי (Orthographic)**: שומר על גודל אובייקטים ללא קשר למרחק; קווים מקבילים נשארים מקבילים. משמש לשרטוטים טכניים או משחקים עם מבט עילי/צד קבוע.
    *באפליקציה, בחירת סוג היטל והגדרותיו משנה את ה-Projection Matrix. לחיצה על "הצג שדה ראייה" מציגה ויזואלית את ה-Frustum/Box הנחתך.*

    <h3>Clipping & Rasterization: חיתוך והפיכה לרשת פיקסלים</h3>
    *   **Clipping**: כל הגאומטריה (קודקודים, קווים, משולשים) שנמצאת *מחוץ* לנפח ההיטל (ה-Frustum/Box) נחתכת ונזרקת. זה חוסך זמן עיבוד יקר בשלבים הבאים. רק מה שגלוי נשאר.
    *   **Rasterization**: השלב המרעיש בו גאומטריה תלת-ממדית הופכת לאוסף פיקסלים פוטנציאליים על המסך הדו-ממדי. כל משולש שעבר Clipping הופך לאוסף של "פרגמנטים" (Fragments) - מועמדים להיות פיקסלים. לכל פרגמנט יש מיקום (X,Y) על המסך ומידע נוסף (עומק Z, קואורדינטות טקסטורה UV, נורמלים ועוד) שנגזר מקודקודי המשולש המקוריים.

    <h3>Fragment Processing (Shading & Texturing) & Depth Testing: צבע וסדר סופי</h3>
    כעת, עבור כל פרגמנט, ה-GPU מריץ תוכנה קטנה (Fragment Shader) כדי לחשב את הצבע הסופי שלו:
    *   **Shading (הצללה/תאורה)**: חישוב אינטראקציית אור עם המשטח בנקודת הפרגמנט, בהתבסס על מקורות אור, צבע החומר, כיוון המשטח (נורמל), ונתונים נוספים. *באפליקציה, כיבוי "הפעל תאורה" יציג את האובייקט בצבע אחיד ללא השפעת אור.*
    *   **Texturing (הוספת טקסטורה)**: שימוש בטקסטורה (תמונה דו-ממדית) כדי לקבוע את צבע הפרגמנט, בהתבסס על קואורדינטות ה-UV שלו. *באפליקציה, הפעלת טקסטורה תכסה את הקובייה בתמונה.*
    *   **Depth Testing (בדיקת עומק)**: זהו שלב קריטי לקביעת אילו פיקסלים גלויים. לכל פיקסל על המסך יש גם ערך עומק (Z) שנשמר בחוצץ מיוחד (Z-buffer). כשרסטרייזר מייצר פרגמנט חדש לאותו פיקסל, ערך ה-Z שלו נבדק מול ערך ה-Z הקיים ב-Z-buffer. אם הפרגמנט החדש קרוב יותר (Z קטן יותר), צבעו וערך ה-Z שלו מחליפים את הקיימים. כך רק האובייקט הקרוב ביותר נראה. *באפליקציה, נסה לכבות את בדיקת העומק ותראה איך האובייקט המרוחק שהוספנו מופיע על גבי הקובייה, למרות שהוא מאחוריה!*

    <h3>Output: התמונה המוכנה על המסך</h3>
    השלב האחרון. לאחר שכל הפרגמנטים עובדו, נבדקו לעומק, ועברו שילובים סופיים (כמו שקיפות - Alpha Blending, או אפקטים פוסט-עיבוד), הצבע הסופי של כל פיקסל נכתב ל-**Frame Buffer**, שהוא זיכרון התמונה המוכן לתצוגה. התמונה השלמה מוצגת על המסך - פריימים רבים בשנייה, ליצירת אשליה של תנועה חלקה.

    <h3>סיכום: למה זה חשוב?</h3>
    הבנת ה-Pipeline מאפשרת למפתחים וגרפיקאים לדבר "בשפה" של ה-GPU, לנצל את כוחו המדהים, ליצור עולמות וירטואליים מורכבים, לפתח אפקטים ויזואליים חדשניים, ולהבטיח שהחוויה הגרפית תהיה חלקה, מהירה ויפה. זהו הבסיס לכל מה שאתם רואים במשחקי מחשב ובאפליקציות גרפיות מודרניות.
</div>


<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        background-color: #eef4f8; /* Softer background */
        color: #333;
    }

    h1, h2, h3 {
        color: #0056b3; /* Deep blue */
        margin-top: 0;
        margin-bottom: 10px;
    }

    h1 {
        text-align: center;
        color: #003366; /* Darker blue */
        margin-bottom: 20px;
    }

    p {
        margin-bottom: 15px;
    }

    .app-container {
        display: flex;
        flex-direction: column;
        gap: 30px; /* More space */
        margin-bottom: 30px;
        background-color: #ffffff;
        padding: 25px; /* More padding */
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* Deeper shadow */
    }

    @media (min-width: 768px) {
        .app-container {
            flex-direction: row;
        }

        .viewer {
            flex: 2;
        }

        .controls {
            flex: 1;
            min-width: 350px; /* Slightly wider controls */
        }
    }

    .viewer {
        width: 100%;
        aspect-ratio: 16 / 9;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #f0f0f0; /* Lighter placeholder */
        border: 1px solid #dcdcdc; /* Softer border */
        border-radius: 8px;
        overflow: hidden;
        position: relative; /* Needed for potential absolute elements */
    }

    #renderCanvas {
        width: 100%;
        height: 100%;
        display: block;
    }

    .controls {
        padding: 20px;
        border-radius: 8px;
        background-color: #f8f9fa; /* Very light background */
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05); /* Subtle inner shadow */
    }

    .control-step {
        margin-bottom: 25px; /* More space between steps */
        padding-bottom: 15px;
        border-bottom: 1px solid #e9ecef; /* Lighter separator */
    }

    .control-step:last-child {
        border-bottom: none;
        margin-bottom: 0;
        padding-bottom: 0;
    }

    .control-step h3 {
         margin-bottom: 5px;
         color: #007bff; /* Bright blue */
         font-size: 1.1em;
         display: flex;
         align-items: center;
         justify-content: space-between;
    }

    .step-label {
        font-size: 0.8em;
        color: #555;
        font-weight: normal;
    }

    .controls-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); /* Responsive grid */
        gap: 10px; /* Gap between grid items */
        align-items: center;
    }

    .controls-grid > div {
         display: flex;
         flex-direction: column;
    }

    .controls-grid label {
        display: block; /* Label above input */
        margin-bottom: 3px;
        font-size: 0.9em;
        color: #555;
         width: auto; /* Remove fixed width */
    }

     .controls-grid input[type="range"],
     .controls-grid select {
         width: 100%; /* Full width within grid item */
         margin-bottom: 0; /* Remove margin */
         vertical-align: middle;
         -webkit-appearance: none; /* Style range inputs */
         appearance: none;
         height: 8px;
         background: #d3d3d3;
         outline: none;
         opacity: 0.7;
         transition: opacity .2s;
         border-radius: 5px;
     }

     .controls-grid input[type="range"]:hover {
         opacity: 1;
     }

    .controls-grid input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 15px;
        height: 15px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
    }

    .controls-grid input[type="range"]::-moz-range-thumb {
        width: 15px;
        height: 15px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
    }


     .controls-grid input[type="checkbox"] {
        vertical-align: middle;
        margin-right: 5px;
     }

     .controls-grid select {
         padding: 5px;
         border: 1px solid #ccc;
         border-radius: 4px;
         background-color: #fff;
     }


    .controls button {
        display: block;
        width: 100%; /* Make button full width in grid */
        margin-top: 10px;
        padding: 10px 15px;
        font-size: 0.9em;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px; /* Slightly more rounded */
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .controls button:hover {
        background-color: #0056b3;
         box-shadow: 0 3px 7px rgba(0,0,0,0.15);
    }

     .controls button:active {
         transform: translateY(1px);
     }

    .controls small {
        display: block; /* Ensure small text is on its own line */
        margin-top: 5px;
        font-size: 0.8em;
        color: #666;
    }

     .grid-col-span-2 {
         grid-column: span 2; /* Make element span two columns in the grid */
     }


    #toggleExplanation {
        display: block;
        margin: 30px auto; /* More margin */
        padding: 12px 25px; /* More padding */
        font-size: 1.1em;
        background-color: #28a745; /* Green button */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: 0 3px 8px rgba(0,0,0,0.2);
    }

    #toggleExplanation:hover {
        background-color: #218838;
        box-shadow: 0 4px 10px rgba(0,0,0,0.25);
    }
     #toggleExplanation:active {
         transform: translateY(1px);
     }


    #explanation {
        margin-top: 20px;
        padding: 25px;
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #007bff; /* Highlight explanation section */
    }

    #explanation h2, #explanation h3 {
        color: #0056b3;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    #explanation h3 {
        font-size: 1.1em;
        border-bottom: 1px dashed #e9ecef;
        padding-bottom: 5px;
    }

    #explanation p {
        margin-bottom: 15px;
        text-align: justify;
    }

    #explanation strong {
        color: #007bff;
    }

    #explanation small {
        font-size: 0.9em;
        color: #666;
        display: block; /* Ensure small text is on its own line in explanation */
        margin-top: -10px; /* Pull it closer to the previous paragraph */
        margin-bottom: 10px;
    }

    /* Helper styles for visualization */
    .frustum-helper-visible canvas {
         outline: 2px dashed rgba(0, 123, 255, 0.5); /* Visual cue around canvas */
    }


</style>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r137/three.min.js"></script> <!-- Updated Three.js version -->
<script>
    let scene, camera, renderer;
    let cube, secondObject; // Use different name for clarity
    let frustumHelper;
    let frustumVisible = false;
    let perspectiveCamera, orthographicCamera;

    const canvas = document.getElementById('renderCanvas');

    function initThreeJS() {
        // Renderer
        renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true });
        renderer.setPixelRatio(window.devicePixelRatio); // Handle high-DPI screens
        resizeCanvas(); // Set initial size

        // Scene
        scene = new THREE.Scene();
        scene.background = new THREE.Color(0xeef4f8); // Match body background or light neutral

        // Cameras
        const aspectRatio = canvas.clientWidth / canvas.clientHeight;
        perspectiveCamera = new THREE.PerspectiveCamera(75, aspectRatio, 0.1, 100); // Adjusted far plane for demo size
        orthographicCamera = new THREE.OrthographicCamera(-aspectRatio * 5, aspectRatio * 5, 5, -5, 0.1, 100); // Adjusted far plane

        // Start with perspective
        camera = perspectiveCamera;
        camera.position.set(0, 0, -10); // Initial camera position
        camera.lookAt(0, 0, 0); // Default lookat center

        // Geometry - Main Cube
        const geometry = new THREE.BoxGeometry(1, 1, 1);
        const material = new THREE.MeshStandardMaterial({ color: 0x00ff00 }); // Start with lighting enabled
        cube = new THREE.Mesh(geometry, material);
        cube.position.z = -5; // Initial cube position in world space
        scene.add(cube);

         // Geometry - Second object for Depth Test demo
         const planeGeometry = new THREE.PlaneGeometry(8, 8); // Larger plane
         const planeMaterial = new THREE.MeshBasicMaterial({ color: 0xff0000, side: THREE.DoubleSide });
         secondObject = new THREE.Mesh(planeGeometry, planeMaterial);
         secondObject.position.set(0, 0, -10); // Placed behind the cube initially
         secondObject.name = 'demoPlane'; // Name for easy lookup
         secondObject.visible = false; // Hide initially, only show when depth test is off
         scene.add(secondObject);


        // Lighting
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.6); // Brighter ambient
        scene.add(ambientLight);
        const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8); // Brighter directional
        directionalLight.position.set(5, 8, 5).normalize();
        scene.add(directionalLight);

        // Frustum Helper
        frustumHelper = new THREE.CameraHelper(camera);
        frustumHelper.visible = false; // Hide initially
        scene.add(frustumHelper);

        // Initial state sync for controls
        syncControlsToMesh();

        // Render loop
        animate();
    }

    function animate() {
        requestAnimationFrame(animate);

        // Update frustum helper if visible
        if(frustumVisible) {
           // The helper needs its camera matrix World updated before update()
            frustumHelper.update();
        }

        renderer.render(scene, camera);
    }

    function resizeCanvas() {
        const parent = canvas.parentElement;
        const width = parent.clientWidth;
        const height = parent.clientHeight;

        if (canvas.width !== width || canvas.height !== height) {
            renderer.setSize(width, height, false);
            const aspectRatio = width / height;

            // Update cameras with new aspect ratio
            perspectiveCamera.aspect = aspectRatio;
            perspectiveCamera.updateProjectionMatrix();

            const orthoSize = parseFloat(document.getElementById('orthoSize').value);
            orthographicCamera.left = -aspectRatio * orthoSize;
            orthographicCamera.right = aspectRatio * orthoSize;
            orthographicCamera.top = orthoSize;
            orthographicCamera.bottom = -orthoSize;
            orthographicCamera.updateProjectionMatrix();

            // Ensure the current camera is updated if needed
             if (camera === perspectiveCamera) {
                 camera.aspect = aspectRatio; // Already done above, but good for clarity
             } else { // orthographic
                 const currentOrthoSize = parseFloat(document.getElementById('orthoSize').value);
                 camera.left = -aspectRatio * currentOrthoSize;
                 camera.right = aspectRatio * currentOrthoSize;
                 camera.top = currentOrthoSize;
                 camera.bottom = -currentOrthoSize;
             }
             camera.updateProjectionMatrix();

             // Update or recreate frustum helper if camera type or size changes
             scene.remove(frustumHelper); // Remove old helper
             frustumHelper = new THREE.CameraHelper(camera); // Create new helper for current camera
             frustumHelper.visible = frustumVisible;
             scene.add(frustumHelper);
             if(frustumVisible) {
                 // Add visual cue class to viewer
                 canvas.parentElement.classList.add('frustum-helper-visible');
             } else {
                  canvas.parentElement.classList.remove('frustum-helper-visible');
             }
        }
    }

    // --- Event Listeners for Controls ---

    // Model Matrix (Object Position, Rotation, Scale)
    document.getElementById('posX').addEventListener('input', (e) => cube.position.x = parseFloat(e.target.value));
    document.getElementById('posY').addEventListener('input', (e) => cube.position.y = parseFloat(e.target.value));
    document.getElementById('posZ').addEventListener('input', (e) => cube.position.z = parseFloat(e.target.value));
    document.getElementById('rotX').addEventListener('input', (e) => cube.rotation.x = THREE.MathUtils.degToRad(parseFloat(e.target.value)));
    document.getElementById('rotY').addEventListener('input', (e) => cube.rotation.y = THREE.MathUtils.degToRad(parseFloat(e.target.value)));
    document.getElementById('rotZ').addEventListener('input', (e) => cube.rotation.z = THREE.MathUtils.degToRad(parseFloat(e.target.value)));
    document.getElementById('scale').addEventListener('input', (e) => cube.scale.setScalar(parseFloat(e.target.value)));

    // View Matrix (Camera Position & LookAt)
    document.getElementById('camPosX').addEventListener('input', (e) => camera.position.x = parseFloat(e.target.value));
    document.getElementById('camPosY').addEventListener('input', (e) => camera.position.y = parseFloat(e.target.value));
    document.getElementById('camPosZ').addEventListener('input', (e) => camera.position.z = parseFloat(e.target.value));

    document.getElementById('camLookY').addEventListener('input', (e) => {
         // Adjust camera target's Y position for 'look up/down' effect
          const lookTarget = new THREE.Vector3(0, parseFloat(e.target.value) * 3, 0); // Multiply for sensitivity
          camera.lookAt(lookTarget);
          if(frustumVisible) frustumHelper.update(); // Update helper when camera transform changes
    });


    // Projection Matrix (Type and Parameters)
    const projectionTypeSelect = document.getElementById('projectionType');
    const perspectiveControlsDiv = document.getElementById('perspectiveControls');
    const orthographicControlsDiv = document.getElementById('orthographicControls');
    const fovInput = document.getElementById('fov');
    const orthoSizeInput = document.getElementById('orthoSize');

    projectionTypeSelect.addEventListener('change', (e) => {
        const aspectRatio = renderer.domElement.clientWidth / renderer.domElement.clientHeight;
         const oldCamera = camera;

        if (e.target.value === 'perspective') {
            camera = perspectiveCamera;
            perspectiveControlsDiv.style.display = 'flex'; // Use flex for grid layout
            orthographicControlsDiv.style.display = 'none';
            // Apply current values
            camera.fov = parseFloat(fovInput.value);
            camera.aspect = aspectRatio;
        } else { // orthographic
            camera = orthographicCamera;
            perspectiveControlsDiv.style.display = 'none';
            orthographicControlsDiv.style.display = 'flex'; // Use flex for grid layout
            // Apply current values
            const orthoSize = parseFloat(orthoSizeInput.value);
            camera.left = -aspectRatio * orthoSize;
            camera.right = aspectRatio * orthoSize;
            camera.top = orthoSize;
            camera.bottom = -orthoSize;
        }

        camera.updateProjectionMatrix();
        camera.position.copy(oldCamera.position); // Keep same position
        camera.quaternion.copy(oldCamera.quaternion); // Keep same rotation/lookat

        // Update frustum helper when camera changes
         scene.remove(frustumHelper); // Remove old helper
         frustumHelper = new THREE.CameraHelper(camera); // Create new helper for current camera
         frustumHelper.visible = frustumVisible;
         scene.add(frustumHelper);
         if(frustumVisible) frustumHelper.update(); // Update helper visual
    });

    fovInput.addEventListener('input', (e) => {
        perspectiveCamera.fov = parseFloat(e.target.value);
        perspectiveCamera.updateProjectionMatrix();
         if(frustumVisible && camera === perspectiveCamera) frustumHelper.update(); // Update frustum helper visually if perspective
    });

     orthoSizeInput.addEventListener('input', (e) => {
          const aspectRatio = renderer.domElement.clientWidth / renderer.domElement.clientHeight;
          const orthoSize = parseFloat(e.target.value);
          orthographicCamera.left = -aspectRatio * orthoSize;
          orthographicCamera.right = aspectRatio * orthoSize;
          orthographicCamera.top = orthoSize;
          orthographicCamera.bottom = -orthoSize;
          orthographicCamera.updateProjectionMatrix();
          if(frustumVisible && camera === orthographicCamera) frustumHelper.update(); // Update frustum helper visually if ortho
     });


    // Clipping Visualization Toggle
    document.getElementById('highlightClipping').addEventListener('click', () => {
        frustumVisible = !frustumVisible;
        frustumHelper.visible = frustumVisible;

        // Toggle visual cue on canvas container
        if(frustumVisible) {
            canvas.parentElement.classList.add('frustum-helper-visible');
        } else {
             canvas.parentElement.classList.remove('frustum-helper-visible');
        }

         if(frustumVisible) frustumHelper.update(); // Ensure helper is updated when shown
    });


    // Shading, Texturing, Depth Testing
    const enableShadingCheckbox = document.getElementById('enableShading');
    const enableTextureCheckbox = document.getElementById('enableTexture');
    const enableDepthTestCheckbox = document.getElementById('enableDepthTest');

    // Load a simple texture
    const textureLoader = new THREE.TextureLoader();
    let loadedTexture = null; // Store the loaded texture
    const texturePath = 'https://threejs.org/examples/textures/crate.gif';

    textureLoader.load(texturePath,
         // onLoad callback
        (texture) => {
            loadedTexture = texture;
            console.log('Texture loaded successfully.');
            // Check if texture checkbox is already checked and apply if so
            if (enableTextureCheckbox.checked) {
                 applyTexture();
            }
             // Enable texture checkbox if it was disabled due to load attempt
            enableTextureCheckbox.disabled = false;
             enableTextureCheckbox.parentElement.querySelector('label').style.textDecoration = 'none';
        },
        // onProgress callback
        undefined, // No progress handling needed for this demo
        // onError callback
        (error) => {
            console.error('An error happened loading texture:', error);
            // Disable texture controls if texture fails to load
            enableTextureCheckbox.disabled = true;
            enableTextureCheckbox.checked = false; // Ensure it's unchecked
            enableTextureCheckbox.parentElement.querySelector('label').style.textDecoration = 'line-through';
             alert('Failed to load texture. Texture option disabled.'); // Notify user
        }
    );

     function applyTexture() {
         if (cube.material.map !== loadedTexture) { // Only update if changing
             cube.material.map = loadedTexture;
             cube.material.needsUpdate = true; // Important!
         }
     }

    function removeTexture() {
        if (cube.material.map !== null) { // Only update if changing
            cube.material.map = null;
            cube.material.needsUpdate = true; // Important!
        }
    }


    enableShadingCheckbox.addEventListener('change', (e) => {
        const currentMap = cube.material.map; // Preserve current texture map
        const oldMaterial = cube.material;

        if (e.target.checked) {
            // Enable Shading: Switch to MeshStandardMaterial
            cube.material = new THREE.MeshStandardMaterial({ color: oldMaterial.color, map: currentMap });
             // Ensure lights are contributing (they are always in scene, but basic material ignores them)
             scene.traverse((obj) => { if (obj instanceof THREE.Light) obj.visible = true; });
        } else {
            // Disable Shading: Switch to MeshBasicMaterial (ignores lighting)
            cube.material = new THREE.MeshBasicMaterial({ color: oldMaterial.color, map: currentMap });
             // Optionally hide lights for visual feedback when shading is off
             scene.traverse((obj) => { if (obj instanceof THREE.Light) obj.visible = false; });
        }
         oldMaterial.dispose(); // Clean up old material
         cube.material.needsUpdate = true; // Essential after changing material
    });

    enableTextureCheckbox.addEventListener('change', (e) => {
        if (e.target.checked) {
            if (loadedTexture) { // Check if texture is actually loaded
                 applyTexture();
            } else {
                 console.warn("Texture not loaded yet or failed to load. Cannot apply.");
                 e.target.checked = false; // Uncheck if texture isn't ready
                 alert('Texture not ready. Please wait or check console for errors.');
            }
        } else {
            removeTexture();
        }
    });

    enableDepthTestCheckbox.addEventListener('change', (e) => {
        // This toggle primarily affects how the renderer handles drawing order.
        // Three.js renderer usually handles depth testing automatically based on render order and camera.
        // Disabling depth test often means turning off depth writes and tests.
        // The most visual way to show this is by having overlapping objects.
        // We will control the visibility of the second object here for demonstration.

         if (e.target.checked) {
             // Depth test ON: Objects nearer to camera hide objects further away.
             // Hide the second object as it behaves normally.
             secondObject.visible = false;
             // Ensure renderer's depth test is enabled (usually default)
             // renderer.getContext().enable(renderer.getContext().DEPTH_TEST); // Less common to toggle directly
         } else {
             // Depth test OFF: Rendering order determines visibility, NOT distance.
             // The second object will render *after* the cube (because it was added later)
             // and will appear on top regardless of its actual Z position behind the cube.
             secondObject.visible = true;
             // To force the visual issue, we might need to manually control render order
             // or disable the renderer's internal depth handling.
             // A common way to visually break depth is by using material properties.
             // However, the simplest way for demonstration is to show the plane
             // which, if rendered *after* the cube, will draw over it when depth is off.
             // Three.js handles render order, so just showing the plane suffices for the demo.
             // A more explicit way might be to disable depthWrite and depthTest on materials,
             // but toggling object visibility and relying on render order is simpler for this demo.
         }
         // Note: Explicitly disabling renderer's depth test is complex and often breaks rendering.
         // Toggling `secondObject.visible` is the clear way to demonstrate the EFFECT of Z-testing failure.
    });


    // Explanation Toggle
    document.getElementById('toggleExplanation').addEventListener('click', () => {
        const explanationDiv = document.getElementById('explanation');
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        if (isHidden) {
            explanationDiv.style.display = 'block';
        } else {
            explanationDiv.style.display = 'none';
        }
    });

    // Initial state sync for controls
     function syncControlsToMesh() {
          // Sync cube properties based on initial Three.js object state
          document.getElementById('posX').value = cube.position.x.toFixed(1);
          document.getElementById('posY').value = cube.position.y.toFixed(1);
          document.getElementById('posZ').value = cube.position.z.toFixed(1);
          document.getElementById('rotX').value = THREE.MathUtils.radToDeg(cube.rotation.x).toFixed(0);
          document.getElementById('rotY').value = THREE.MathUtils.radToDeg(cube.rotation.y).toFixed(0);
          document.getElementById('rotZ').value = THREE.MathUtils.radToDeg(cube.rotation.z).toFixed(0);
          document.getElementById('scale').value = cube.scale.x.toFixed(1); // Assuming uniform scale

          // Sync camera position based on initial Three.js object state
          document.getElementById('camPosX').value = camera.position.x.toFixed(1);
          document.getElementById('camPosY').value = camera.position.y.toFixed(1);
          document.getElementById('camPosZ').value = camera.position.z.toFixed(1);
           // Sync camera lookAt is complex via angles/sliders, relying on initial camera.lookAt(0,0,0) match

          // Sync projection type and parameters
          const isPerspective = (camera === perspectiveCamera);
          document.getElementById('projectionType').value = isPerspective ? 'perspective' : 'orthographic';
           perspectiveControlsDiv.style.display = isPerspective ? 'flex' : 'none';
           orthographicControlsDiv.style.display = isPerspective ? 'none' : 'flex';

          if (isPerspective) {
               document.getElementById('fov').value = camera.fov.toFixed(0);
          } else { // orthographic
              // Sync ortho size based on bounds.
              // Assuming initial setup with size 5 relative to aspect ratio for simplicity.
               document.getElementById('orthoSize').value = 5; // Default value, requires manual sync if changed programmatically
          }

          // Sync shading/texture/depth test states based on initial Three.js state
          // Shading: Check material type
          document.getElementById('enableShading').checked = cube.material.type === 'MeshStandardMaterial';
           // Texture: Checked if material has a map (texture loading is async, might be null initially)
           // This state is better handled after texture loads.
           enableTextureCheckbox.checked = (cube.material.map !== null);
            // Depth Test: Check visibility of the second object used for demo
           document.getElementById('enableDepthTest').checked = !secondObject.visible;

            // Correct initial state for depth test object visibility
            if (!document.getElementById('enableDepthTest').checked) {
                 secondObject.visible = true;
            } else {
                 secondObject.visible = false;
            }


     }


    // Initialize on window load
    window.addEventListener('load', initThreeJS);
    window.addEventListener('resize', resizeCanvas);


</script>
---