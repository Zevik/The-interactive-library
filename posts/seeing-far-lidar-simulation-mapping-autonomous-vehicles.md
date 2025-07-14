---
title: "רואים רחוק: הדמיית לידאר למיפוי ולרכב אוטונומי"
english_slug: seeing-far-lidar-simulation-mapping-autonomous-vehicles
category: "פיזיקה"
tags:
  - לידאר
  - לייזר
  - חיישנים
  - רכב אוטונומי
  - מיפוי תלת ממדי
---
# רואים רחוק: הדמיית לידאר למיפוי ולרכב אוטונומי

האם שאלתם את עצמכם פעם איך רכב אוטונומי "מרגיש" את הדרך והסביבה בדיוק מדהים, גם בחושך מוחלט? או איך נוצרות מפות תלת-ממדיות סופר מדויקות של אזורים שלמים, כולל צמחייה ומבנים, בלי לגעת בכלום? התשובה נמצאת בטכנולוגיה גאונית שמשתמשת במהירות האור: לידאר. הצטרפו אלינו למסע קצר אל ליבה של הטכנולוגיה הבלתי נראית הזו!

<div id="lidar-app">
    <canvas id="lidar-canvas"></canvas>
    <div class="controls">
        <button id="start-scan-button">התחל סריקת לידאר</button>
    </div>
    <div id="scan-progress" class="progress-container">
        <div class="progress-bar" id="progress-bar"></div>
        <span class="progress-text">סריקה: <span id="progress-percent">0%</span></span>
    </div>
</div>

<button id="toggle-explanation-button">הצג לי את הסוד: איך זה עובד?</button>

<div id="explanation" class="hidden">
    <h2>מה זה בעצם לידאר (LIDAR)?</h2>
    <p>תחשבו על לידאר כעל "עיניים" שמבוססות על אור לייזר. זהו חיישן מתקדם לחישה מרחוק (כמו רדאר, רק עם אור במקום גלי רדיו) שנועד למדוד מרחקים ולבנות תמונה תלת-ממדית של הסביבה. השם LIDAR הוא ראשי תיבות של Light Detection and Ranging.</p>

    <h2>קסם המדידה: איך לידאר מחשב מרחק?</h2>
    <p>השיטה הכי נפוצה נקראת Time of Flight (TOF), או "זמן מעוף". זה פשוט גאוני: חיישן הלידאר שולח פולס קצר וחד של אור לייזר. הפולס הזה טס במהירות האור עד שהוא פוגע באובייקט (עץ, מכונית, בניין, הולך רגל). ברגע שהוא פוגע, חלק מהאור מוחזר מיד חזרה אל החיישן. הלידאר מודד במדויק את הזמן המזערי שחלף מרגע שליחת הפולס ועד שנקלט ההד החוזר. מכיוון שאנחנו יודעים בדיוק מהי מהירות האור, חישוב המרחק הופך לפשוט: מרחק = (מהירות האור * זמן ההחזרה) / 2. זהו, יש לנו נקודה במרחב!</p>

    <h2>מה יש בפנים? רכיבי הלידאר</h2>
    <p>כדי שמכונה תוכל "לראות" עם אור, היא צריכה כמה חלקים חיוניים:</p>
    <ul>
        <li><strong>משדר לייזר:</strong> ה"לב" הפועם שפולט אלפי ואף מיליוני פולסים בשנייה. לרוב משתמשים בלייזר אינפרה-אדום, כדי לא לסנוור אנשים.</li>
        <li><strong>מערכת סריקה:</strong> ה"צוואר" וה"עיניים" שמכוונים את קרן הלייזר לכיוונים שונים כדי לסרוק את כל השטח שמסביב. זה יכול להיות מנוע מסתובב גדול (לידאר מכני קלאסי) או מערכות מתוחכמות יותר בלי חלקים נעים (Solid-State).</li>
        <li><strong>מקלט:</strong> ה"אוזן" הרגישה שמחכה לקלוט את האור המוחזר (ההד). הוא יודע לזהות רק את אורך הגל של הלייזר הספציפי כדי להתעלם מרעשי רקע של אור שמש או תאורת רחוב.</li>
        <li><strong>מעבד נתונים:</strong> ה"מוח" המהיר שמחשב את זמן ההחזרה לכל פולס, ממיר אותו למרחק מדויק, ומתחיל לבנות את המפה התלת-ממדית.</li>
    </ul>

    <h2>לידה של מפה: מהו "ענן נקודות" (Point Cloud)?</h2>
    <p>לידאר לא עוצר בנקודה אחת. הוא סורק את הסביבה כולה בזמן שיא, שולח פולסים לאלפי ואפילו מיליוני נקודות שונות. כל פולס כזה שחוזר נהפך לנקודה אחת במרחב התלת-ממדי, עם קואורדינטות X, Y, Z. כשמצרפים את כל הנקודות האלה יחד, מקבלים "ענן נקודות" - עותק דיגיטלי, תלת-ממדי ומאוד צפוף של הסביבה האמיתית. זה נראה לפעמים כמו "שבטים" של נקודות שמרכיבות את האובייקטים השונים.</p>

    <h2>איפה פוגשים לידאר? שימושים מרתקים</h2>
    <p>הטכנולוגיה הזו נמצאת בכל מיני מקומות מפתיעים:</p>
    <ul>
        <li><strong>רכב אוטונומי:</strong> זה אולי השימוש הכי מוכר. לידאר עוזר למכוניות ללא נהג "לראות" ב-360 מעלות, לזהות בדיוק רכבים אחרים, הולכי רגל ומכשולים, ולנווט במדויק.</li>
        <li><strong>מיפוי מודרני:</strong> יצירת מפות טופוגרפיות מדויקות, מודלים תלת-ממדיים של ערים שלמות, תכנון תשתית. אפשר אפילו למפות יערות וצמחייה צפופה!</li>
        <li><strong>רובוטיקה ותעשייה:</strong> רובוטים במחסנים או בפס ייצור משתמשים בלידאר כדי לנווט ולזהות עצמים.</li>
        <li><strong>חקלאות ובנייה:</strong> מיפוי שדות, מעקב אחר התקדמות בנייה, מדידות נפחים.</li>
    </ul>

    <h2>לידאר מול אחרים: יתרונות וחסרונות</h2>
    <p>כמו כל טכנולוגיה, גם ללידאר יש צדדים חזקים יותר וחלשים יותר בהשוואה לחיישנים אחרים (כמו מצלמות או רדאר):</p>
    <ul>
        <li><strong>הפלוסים הגדולים:</strong>
            <ul>
                <li><strong>סופר מדויק:</strong> נותן מדידות מרחק וקואורדינטות תלת-ממדיות ברמה דיוק גבוהה מאוד.</li>
                <li><strong>עובד בחושך:</strong> בניגוד למצלמות רגילות שתלויות באור חיצוני, לידאר מביא את האור של עצמו (הלייזר!).</li>
                <li><strong>מדידת עומק ישירה:</strong> לא צריך לחשב עומק מסובך מתמונות דו-ממדיות - המרחק הוא הנתון הראשוני.</li>
            </ul>
        </li>
        <li><strong>המינוסים:</strong>
            <ul>
                <li><strong>רגישות למזג אוויר קשה:</strong> גשם כבד, ערפל או שלג יכולים להפריע לקרן הלייזר או לגרום להחזרות שווא.</li>
                <li><strong>עלות:</strong> חיישני לידאר איכותיים יכולים להיות יקרים (למרות שהמחירים יורדים בהתמדה).</li>
                <li><strong>הרבה נתונים:</strong> ענני נקודות הם קבצים גדולים שדורשים כוח עיבוד משמעותי כדי לנתח אותם.</li>
            </ul>
        </li>
    </ul>
</div>

<style>
/* כל הגופנים, הריווח והצבעים כווננו ליצירת מראה מודרני ונקי. */
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    line-height: 1.7; /* מעט יותר רווח לשורות */
    margin: 0;
    padding: 30px 20px; /* הגדלת ריפוד כללי */
    background: linear-gradient(to bottom, #f0f4f8, #d9e2ec); /* רקע עם גרדיאנט עדין */
    color: #333;
    direction: rtl;
    text-align: right;
    overflow-x: hidden; /* מניעת גלילה אופקית בטעות */
}

h1, h2, h3 {
    color: #004080; /* כחול עמוק יותר */
    margin-bottom: 15px;
    line-height: 1.4;
}

p {
    margin-bottom: 15px;
    color: #444;
}

ul {
    padding-right: 25px; /* הגדלת ריפוד לרשימות */
    list-style-type: disc;
    margin-bottom: 15px;
}

li {
    margin-bottom: 10px; /* רווח גדול יותר בין פריטי רשימה */
}

#lidar-app {
    margin: 30px auto;
    border: 1px solid #b0c4de; /* גבול עדין יותר */
    border-radius: 12px; /* פינות מעוגלות יותר */
    overflow: hidden;
    background-color: #ffffff;
    padding: 20px; /* הגדלת הריפוד הפנימי */
    max-width: 800px;
    position: relative;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* צל עדין למראה מרחף */
    text-align: center; /* יישור מרכזי לתוכן האפליקציה */
}

#lidar-canvas {
    display: block;
    width: 100%;
    height: 450px; /* הגדלת גובה הקנבס */
    background-color: #eef2f7; /* רקע כחלחל בהיר לקנבס */
    border-radius: 8px; /* פינות מעוגלות לקנבס */
    margin-bottom: 15px; /* רווח מתחת לקנבס */
}

.controls {
    margin-bottom: 15px;
}

button {
    display: inline-block;
    padding: 12px 25px; /* הגדלת הריפוד בכפתור */
    font-size: 1.1rem; /* הגדלת גודל הגופן בכפתור */
    color: #ffffff;
    background-color: #007bff; /* כחול ראשי */
    border: none;
    border-radius: 6px; /* פינות מעוגלות יותר */
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease; /* הוספת טרנזיציה לשינוי גודל */
    font-weight: bold;
    box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3); /* צל לכפתור */
}

button:hover {
    background-color: #0056b3; /* כחול כהה יותר במעבר עכבר */
    transform: translateY(-2px); /* אפקט עדין של "קפיצה" */
}

button:active {
    transform: translateY(0); /* ביטול אפקט הקפיצה בלחיצה */
    box-shadow: 0 2px 4px rgba(0, 123, 255, 0.4); /* צל קטן יותר בלחיצה */
}

button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
    box-shadow: none;
    transform: none;
}

#toggle-explanation-button {
    display: block; /* כפתור הסבר בשורה נפרדת */
    margin: 20px auto; /* ממורכז */
    background-color: #6c757d; /* כחול אפור */
    box-shadow: 0 4px 8px rgba(108, 117, 125, 0.3);
}

#toggle-explanation-button:hover {
    background-color: #5a6268;
    transform: translateY(-2px);
}

#toggle-explanation-button:active {
    transform: translateY(0);
    box-shadow: 0 2px 4px rgba(108, 117, 125, 0.4);
}


.progress-container {
    width: 80%; /* רוחב מוגדר לפס ההתקדמות */
    height: 25px; /* גובה לפס */
    background-color: #e9ecef; /* רקע בהיר לפס */
    border-radius: 12px;
    margin: 15px auto 0; /* ממורכז, רווח למעלה */
    overflow: hidden; /* לוודא שהבר בפנים לא חורג */
    position: relative; /* למיקום הטקסט מעליו */
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.2); /* צל פנימי עדין */
    visibility: hidden; /* הסתרת ברירת מחדל */
    opacity: 0; /* הסתרה עדינה */
    transition: opacity 0.3s ease; /* אנימציית הופעה */
}

.progress-container.visible {
    visibility: visible;
    opacity: 1;
}

.progress-bar {
    height: 100%;
    width: 0%; /* מתחיל מ-0 */
    background-color: #28a745; /* ירוק להתקדמות */
    border-radius: 12px; /* פינות עגולות גם לבר הפנימי */
    transition: width 0.4s ease; /* אנימציה חלקה להתקדמות */
    position: absolute; /* למקם מתחת לטקסט */
    top: 0;
    left: 0; /* RTL adjustment */
}

.progress-text {
    position: absolute; /* מיקום הטקסט מעל הבר */
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%); /* ממורכז בדיוק */
    color: #343a40; /* צבע כהה לטקסט */
    font-weight: bold;
    font-size: 0.95rem;
    text-shadow: 1px 1px 2px rgba(255,255,255,0.5); /* צל לבן עדין כדי שיראו את הטקסט */
}


#explanation {
    margin-top: 30px;
    padding: 25px; /* הגדלת ריפוד */
    background-color: #e9ecef; /* רקע בהיר */
    border: 1px solid #ced4da;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); /* צל עדין */
    transition: opacity 0.5s ease; /* אנימציית הופעה */
    opacity: 1; /* ברירת מחדל גלוי */
}

#explanation.hidden {
    opacity: 0; /* הסתרה עדינה */
    height: 0; /* כיווץ לגובה 0 */
    overflow: hidden; /* הסתרת התוכן המכווץ */
    padding-top: 0; /* ביטול ריפוד */
    padding-bottom: 0; /* ביטול ריפוד */
    margin-top: 0; /* ביטול רווח למעלה */
    border-color: transparent; /* ביטול גבול */
    pointer-events: none; /* מונע לחיצות כשהוא מוסתר */
}

/* התאמות RTL ספציפיות */
body {
    text-align: right;
}
ul {
    padding-right: 2em; /* עקיפה של ברירת המחדל */
    padding-left: 0;
}
.progress-bar {
    left: unset; /* ביטול left */
    right: 0; /* התחלה מימין */
}
.progress-text {
     left: 50%; /* עדיין ממורכז אופקית */
}

</style>

<script type="module">
    // ייבוא ספריות Three.js
    import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.164.1/build/three.module.js';
    import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.164.1/examples/jsm/controls/OrbitControls.js';

    // מזהי אלמנטים מה-HTML
    const canvas = document.getElementById('lidar-canvas');
    const startScanButton = document.getElementById('start-scan-button');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation-button');
    const progressContainer = document.getElementById('scan-progress');
    const progressBar = document.getElementById('progress-bar');
    const progressPercent = document.getElementById('progress-percent');

    // --- הגדרת סצנת תלת מימד (Three.js) ---
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0xcce0ff); // רקע תכלת בהיר יותר
    // הוספת ערפל עדין למראה עומק
    scene.fog = new THREE.Fog(0xcce0ff, 15, 30);

    // הגדרת מצלמה
    const camera = new THREE.PerspectiveCamera(75, canvas.clientWidth / canvas.clientHeight, 0.1, 100); // טווח ראייה קטן יותר
    camera.position.set(8, 5, 8); // מיקום התחלתי מעט רחוק יותר
    camera.lookAt(0, 2, 0); // הסתכלות לכיוון מרכז הסצנה

    // הגדרת מנוע רינדור
    const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true });
    renderer.setSize(canvas.clientWidth, canvas.clientHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.shadowMap.enabled = true; // הפעלת מפות צל (אופציונלי - דורש הגדרת הטלת צל על אובייקטים ותאורה)

    // הגדרת בקרות מצלמה (עכבר/טאצ')
    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true; // תנועה חלקה
    controls.dampingFactor = 0.15; // פחות "החלקה"
    controls.screenSpacePanning = false;
    controls.maxPolarAngle = Math.PI / 2.2; // מניעת מבט ישר למטה לתוך הקרקע
    controls.minDistance = 3; // מרחק זום מינימלי
    controls.maxDistance = 25; // מרחק זום מקסימלי
    controls.target.set(0, 1.5, 0); // מרכז הסיבוב יהיה מעט מעל הקרקע

    // הוספת תאורה - משודרג
    const ambientLight = new THREE.AmbientLight(0x555555); // תאורת סביבה
    scene.add(ambientLight);
    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8); // אור כיווני ראשי
    directionalLight.position.set(10, 15, 10);
    directionalLight.castShadow = true; // הפעלת הטלת צל
    // הגדרות צל
    directionalLight.shadow.mapSize.width = 1024;
    directionalLight.shadow.mapSize.height = 1024;
    directionalLight.shadow.camera.near = 0.5;
    directionalLight.shadow.camera.far = 50;
    directionalLight.shadow.camera.left = -10;
    directionalLight.shadow.camera.right = 10;
    directionalLight.shadow.camera.top = 10;
    directionalLight.shadow.camera.bottom = -10;
    scene.add(directionalLight);

    // --- הוספת אובייקטים לסצנה (סביבה ומטרות) ---

    // משטח הקרקע - משודרג
    const groundGeometry = new THREE.PlaneGeometry(30, 30);
    const groundMaterial = new THREE.MeshStandardMaterial({ color: 0x88aa88, side: THREE.DoubleSide }); // צבע דשא עדין
    const ground = new THREE.Mesh(groundGeometry, groundMaterial);
    ground.rotation.x = -Math.PI / 2;
    ground.receiveShadow = true; // הקרקע מקבלת צל
    scene.add(ground);

    // קיר אחורי - משודרג
    const wallGeometry = new THREE.BoxGeometry(25, 7, 0.3); // קיר גדול יותר
    const wallMaterial = new THREE.MeshStandardMaterial({ color: 0xc0b0a0 }); // צבע לבנה עדין
    const wall = new THREE.Mesh(wallGeometry, wallMaterial);
    wall.position.set(0, 3.5, -12); // מיקום מתוקן
    wall.receiveShadow = true;
    wall.castShadow = true;
    scene.add(wall);

     // אובייקטים נוספים ומגוונים - משודרג
    const boxGeometry = new THREE.BoxGeometry(1.5, 1.5, 1.5); // קופסה גדולה יותר
    const boxMaterial = new THREE.MeshStandardMaterial({ color: 0xff6600, metalness: 0.2, roughness: 0.8 }); // כתום
    const box = new THREE.Mesh(boxGeometry, boxMaterial);
    box.position.set(4, 0.75, -4);
    box.receiveShadow = true;
    box.castShadow = true;
    scene.add(box);

    const personGeometry = new THREE.CylinderGeometry(0.4, 0.5, 2, 32); // גליל דק וארוך יותר
    const personMaterial = new THREE.MeshStandardMaterial({ color: 0x663399, metalness: 0, roughness: 0.5 }); // סגול
    const person = new THREE.Mesh(personGeometry, personMaterial);
    person.position.set(-5, 1, -6);
    person.receiveShadow = true;
    person.castShadow = true;
    scene.add(person);

    const coneGeometry = new THREE.ConeGeometry(1, 2, 32); // חרוט
    const coneMaterial = new THREE.MeshStandardMaterial({ color: 0x0088aa, metalness: 0.1, roughness: 0.6 }); // טורקיז
    const cone = new THREE.Mesh(coneGeometry, coneMaterial);
    cone.position.set(6, 1, -8);
    cone.receiveShadow = true;
    cone.castShadow = true;
    scene.add(cone);

    const sphereGeometry = new THREE.SphereGeometry(1, 32, 32); // כדור
    const sphereMaterial = new THREE.MeshStandardMaterial({ color: 0xcc00cc, metalness: 0.3, roughness: 0.4 }); // ורוד
    const sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);
    sphere.position.set(-7, 1, -3);
    sphere.receiveShadow = true;
    sphere.castShadow = true;
    scene.add(sphere);


    // מערך האובייקטים שהלידאר יכול "לראות"
    const hittableObjects = [wall, box, person, cone, sphere, ground];

    // --- ייצוג הלידאר בסצנה ---
    const lidarGeometry = new THREE.CylinderGeometry(0.3, 0.4, 0.6, 32); // גליל מעט יותר רחב ונמוך
    const lidarMaterial = new THREE.MeshPhongMaterial({ color: 0x3366ff, emissive: 0x1133aa }); // כחול עז עם קצת אור עצמי
    const lidar = new THREE.Mesh(lidarGeometry, lidarMaterial);
    lidar.position.set(0, 0.3, 0); // ממוקם קצת מעל הקרקע
    scene.add(lidar);

    // הוספת גליל דק שמייצג את הראש המסתובב של הלידאר
    const rotatingHeadGeometry = new THREE.CylinderGeometry(0.2, 0.2, 0.2, 32);
    const rotatingHeadMaterial = new THREE.MeshStandardMaterial({ color: 0x1a1a1a }); // ראש שחור
    const rotatingHead = new THREE.Mesh(rotatingHeadGeometry, rotatingHeadMaterial);
    rotatingHead.position.set(0, 0.6, 0); // ממוקם מעל גוף הלידאר
    lidar.add(rotatingHead); // מחובר לגוף הלידאר כך שיסתובב יחד איתו

    // --- הגדרת ענן נקודות ---
    const pointGeometry = new THREE.BufferGeometry();
    // שימוש בחומר PointsMaterial עם צבעים משתנים
    const pointMaterial = new THREE.PointsMaterial({
         size: 0.08, // גודל נקודה
         sizeAttenuation: true, // גודל הנקודה משתנה עם המרחק
         color: 0xffff00, // צבע התחלתי - צהוב
         vertexColors: false // לא משתמשים בצבע לכל קודקוד כרגע, רק צבע אחיד
         });
    const pointCloud = new THREE.Points(pointGeometry, pointMaterial);
    scene.add(pointCloud);

    let points = []; // מערך לאחסון קואורדינטות נקודות [x, y, z, x, y, z...]
    let colors = []; // מערך לאחסון צבעי נקודות [r, g, b, r, g, b...]

    // --- לוגיקת סריקה ורייקאסטינג ---
    const raycaster = new THREE.Raycaster();
    const lidarPosition = new THREE.Vector3(0, 0.6, 0); // עמדת השיגור (ראש הלידאר)

    // פרמטרים של סריקה - משודרג ליצירת ענן צפוף יותר
    const horizontalAngleSteps = 180; // 180 "פרוסות" אופקיות ב-360 מעלות
    const verticalAngleSteps = 60;   // 60 "שכבות" אנכיות
    const maxVerticalAngle = Math.PI / 6; // טווח סריקה אנכי (למשל, 30 מעלות למעלה ולמטה)

    const totalScanSteps = horizontalAngleSteps * verticalAngleSteps;
    let currentScanStep = 0;
    let isScanning = false;

    // אלמנטים ויזואליים לקרן לייזר (אופציונלי אבל מוסיף לאינטראקציה)
    const rayLineMaterial = new THREE.LineBasicMaterial({ color: 0x00ffff, linewidth: 2, transparent: true, opacity: 0.8 });
    let currentRayLine = null;


    function performScanStep() {
        if (!isScanning) return;

        // חישוב הזוויות עבור הצעד הנוכחי בסריקה המשולבת
        const horizontalStepIndex = currentScanStep % horizontalAngleSteps;
        const verticalStepIndex = Math.floor(currentScanStep / horizontalAngleSteps);

        const horizontalAngle = (horizontalStepIndex / horizontalAngleSteps) * Math.PI * 2; // 0 עד 360 מעלות
        // נשתמש בפונקציית סינוס או דומה ליצירת דפוס סריקה אנכי שאינו לינארי לגמרי
        // נסרוק ממינוס maxVerticalAngle עד פלוס maxVerticalAngle
        const verticalAngle = -maxVerticalAngle + (verticalStepIndex / (verticalAngleSteps - 1)) * (2 * maxVerticalAngle);
         // אפשר גם להוסיף תנודת ראש קטנה יותר כמו בלידאר אמיתי
        // const verticalAngle = Math.sin((verticalStepIndex / (verticalAngleSteps-1)) * Math.PI) * maxVerticalAngle; // דפוס גלי

        // חישוב וקטור הכיוון של הקרן
        const direction = new THREE.Vector3(
            Math.cos(horizontalAngle) * Math.cos(verticalAngle),
            Math.sin(verticalAngle),
            Math.sin(horizontalAngle) * Math.cos(verticalAngle)
        );
        direction.normalize();

        // מיקום הלידאר משתנה כעת לפי ראש הלידאר המסתובב
        const rayOrigin = rotatingHead.getWorldPosition(new THREE.Vector3());

        raycaster.set(rayOrigin, direction);
        raycaster.far = 30; // טווח סריקה מקסימלי

        // מציאת חיתוכים עם אובייקטים
        const intersects = raycaster.intersectObjects(hittableObjects, false);

        if (intersects.length > 0) {
            // נקודת החיתוך הראשונה היא הנקודה הנראית
            const intersectionPoint = intersects[0].point;
            const distance = rayOrigin.distanceTo(intersectionPoint); // מרחק לנקודה

            // הוספת הנקודה וצבע (צבע לפי מרחק או סוג אובייקט אופציונלי)
            points.push(intersectionPoint.x, intersectionPoint.y, intersectionPoint.z);

            // הוספת צבע (צהוב קבוע כרגע)
            colors.push(1, 1, 0); // RGB for yellow

            // ויזואליזציה של הקרן (אופציונלי)
            if (currentRayLine) {
                scene.remove(currentRayLine); // הסרת הקרן הקודמת
                currentRayLine.geometry.dispose();
                currentRayLine.material.dispose();
            }
            const rayPoints = [ rayOrigin.clone(), intersectionPoint.clone() ];
            const rayGeometry = new THREE.BufferGeometry().setFromPoints( rayPoints );
            currentRayLine = new THREE.Line( rayGeometry, rayLineMaterial );
            scene.add( currentRayLine );

            // הסרת הקרן לאחר זמן קצר (סימולציית החזרת פולס)
            // השארת הקרן לפרק זמן קצר יותר לכל צעד סריקה
            setTimeout(() => {
                if (currentRayLine) {
                    scene.remove(currentRayLine);
                    currentRayLine.geometry.dispose();
                    currentRayLine.material.dispose();
                    currentRayLine = null;
                }
            }, 10); // זמן קצר יותר לויזואליזציית קרן

        } else {
             // אופציונלי: ויזואליזציה של קרן שלא פגעה בכלום עד הטווח המקסימלי
             if (currentRayLine) {
                scene.remove(currentRayLine);
                currentRayLine.geometry.dispose();
                currentRayLine.material.dispose();
                currentRayLine = null;
            }
            const endPoint = rayOrigin.clone().add(direction.multiplyScalar(raycaster.far));
            const rayPoints = [ rayOrigin.clone(), endPoint.clone() ];
            const rayGeometry = new THREE.BufferGeometry().setFromPoints( rayPoints );
            const missingRayMaterial = new THREE.LineBasicMaterial({ color: 0xff0000, linewidth: 1, transparent: true, opacity: 0.3 }); // אדום שקוף לקרן "אבודה"
            currentRayLine = new THREE.Line( rayGeometry, missingRayMaterial );
             scene.add( currentRayLine );
             setTimeout(() => {
                if (currentRayLine) {
                    scene.remove(currentRayLine);
                     currentRayLine.geometry.dispose();
                    currentRayLine.material.dispose();
                    currentRayLine = null;
                }
            }, 10);
        }


        // עדכון גאומטריית ענן הנקודות בתדירות נמוכה יותר לביצועים טובים
        if (currentScanStep % 10 === 0 || currentScanStep === totalScanSteps - 1) {
            pointGeometry.setAttribute('position', new THREE.Float32BufferAttribute(points, 3));
             // pointGeometry.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3)); // אם משתמשים בצבעים משתנים
            pointGeometry.attributes.position.needsUpdate = true; // סימון לצורך עדכון
            // if (pointGeometry.attributes.color) pointGeometry.attributes.color.needsUpdate = true; // סימון צבע
        }


        // קידום צעד הסריקה ועדכון ההתקדמות
        currentScanStep++;
        const progress = Math.min(100, Math.round((currentScanStep / totalScanSteps) * 100));
        progressPercent.textContent = `${progress}%`;
        progressBar.style.width = `${progress}%`; // עדכון רוחב פס ההתקדמות

        // סיבוב ראש הלידאר הויזואלי בהתאם לזווית האופקית
         rotatingHead.rotation.y = -horizontalAngle; // סיבוב נגדי לזווית הקרן לויזואליזציה נכונה

        if (currentScanStep < totalScanSteps) {
            // המשך סריקה עם דיליי קצר לאנימציה
             requestAnimationFrame(performScanStep); // שימוש ב-requestAnimationFrame ללולאה חלקה יותר
             // setTimeout(performScanStep, 1); // דיליי קצר יותר
        } else {
            // סריקה הסתיימה
            isScanning = false;
            startScanButton.disabled = false;
            startScanButton.textContent = 'התחל סריקה מחודשת';
             // הסרת הקרן האחרונה אם עדיין קיימת
             if (currentRayLine) {
                scene.remove(currentRayLine);
                currentRayLine.geometry.dispose();
                currentRayLine.material.dispose();
                currentRayLine = null;
            }
            // השארת פס ההתקדמות גלוי לכמה שניות ואז הסתרה
            setTimeout(() => {
                 progressContainer.classList.remove('visible');
            }, 2000); // השאר גלוי ל-2 שניות
        }
    }

    function startScan() {
        if (isScanning) return;

        isScanning = true;
        startScanButton.disabled = true;
        startScanButton.textContent = 'סורק... ממפה את העולם...';
        progressContainer.classList.add('visible'); // הצגת פס ההתקדמות עם אנימציה
        progressBar.style.width = '0%'; // איפוס פס ההתקדמות
        progressPercent.textContent = '0%'; // איפוס טקסט ההתקדמות

        currentScanStep = 0;
        points = []; // ניקוי נקודות קודמות
        colors = []; // ניקוי צבעים
        // איפוס גאומטריית ענן הנקודות
        pointGeometry.setAttribute('position', new THREE.Float32BufferAttribute([], 3));
         // pointGeometry.setAttribute('color', new THREE.Float32BufferAttribute([], 3));

        // הסרת הקרן האחרונה מריצה קודמת אם עדיין קיימת
        if (currentRayLine) {
             scene.remove(currentRayLine);
             currentRayLine.geometry.dispose();
             currentRayLine.material.dispose();
             currentRayLine = null;
        }

        performScanStep(); // התחלת הצעד הראשון
    }

    // --- לולאת אנימציה כללית ---
    function animate() {
        requestAnimationFrame(animate); // מבקש מהדפדפן לקרוא לפונקציה שוב ברגע שיהיה מוכן לפריים הבא

        controls.update(); // עדכון בקרות המצלמה (אם יש שינוי)

        // ניתן להוסיף כאן אנימציות נוספות שאינן חלק מהסריקה

        renderer.render(scene, camera); // רינדור הסצנה
    }

    animate(); // התחלת לולאת האנימציה

    // --- מאזינים לאירועים ---
    startScanButton.addEventListener('click', startScan);

    toggleExplanationButton.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
        if (explanationDiv.classList.contains('hidden')) {
            toggleExplanationButton.textContent = 'הצג לי את הסוד: איך זה עובד?';
        } else {
            toggleExplanationButton.textContent = 'הסתר הסבר מפורט';
        }
    });

    // טיפול בשינוי גודל חלון
    window.addEventListener('resize', () => {
        const newWidth = canvas.parentElement.clientWidth;
        const newHeight = 450; // שמירה על גובה קבוע או שינוי פרופורציונלי

        camera.aspect = newWidth / newHeight;
        camera.updateProjectionMatrix();

        renderer.setSize(newWidth, newHeight);
        renderer.setPixelRatio(window.devicePixelRatio);
    });

    // עדכון גודל ראשוני עם טעינת הדף
    window.dispatchEvent(new Event('resize'));

</script>
```