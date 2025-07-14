---
title: "סוד המים: תכנן מערכת השקיה קדומה"
english_slug: secret-of-water-plan-ancient-irrigation-system
category: "ארכאולוגיה"
tags:
  - השקיה
  - היסטוריה עתיקה
  - הנדסה קדומה
  - ארכיאולוגיה
  - מאיה
---
# סוד המים: תכנן מערכת השקיה קדומה

איך הצליחו תרבויות עתיקות לשגשג באזורים צחיחים יחסית, ללא משאבות או טכנולוגיה מודרנית? התשובה טמונה ביכולת ההנדסית המדהימה שלהן לבנות מערכות תעלות שהובילו מים למרחקים ארוכים. האם תצליח לפצח את סוד העורקים האלו ולתכנן בעצמך מערכת השקיה שתחייה את השדות החקלאיים?

<div id="irrigation-app">
    <h2>בנה את התעלה</h2>
    <div id="map-container">
        <canvas id="irrigationCanvas"></canvas>
        <div id="feedback" class="message"></div>
        <div id="slope-feedback" class="message"></div>
        <div id="elevation-legend">
            <h3>מפתח גבהים:</h3>
            <div class="legend-item">
                <div class="color-box" style="background-color: #1A4F23; border-color: #0A3B0A;"></div>
                <div class="label">שדות חקלאיים (יעד - נמוך)</div>
            </div>
             <div class="legend-item">
                <div class="color-box" style="background-color: #387C44; border-color: #228B22;"></div>
                <div class="label">עמק</div>
            </div>
             <div class="legend-item">
                <div class="color-box" style="background-color: #8FBC8F; border-color: #90EE90;"></div>
                <div class="label">מורדות</div>
            </div>
             <div class="legend-item">
                <div class="color-box" style="background-color: #CD5C5C; border-color: #F08080;"></div>
                <div class="label">רמה</div>
            </div>
             <div class="legend-item">
                <div class="color-box" style="background-color: #A52A2A; border-color: #B22222;"></div>
                <div class="label">הר (גבוה)</div>
            </div>
             <div class="legend-item">
                <div class="color-box" style="background-color: #4682B4; border-color: #1E90FF;"></div>
                <div class="label">מקור מים (התחלה)</div>
            </div>
        </div>
         <div id="instructions">
             <p>לחץ על <strong style="color: #4682B4;">מקור המים</strong> הכחול כדי להתחיל לשרטט את התעלה.</p>
             <p>הוסף נקודות נוספות כדי לנתב את התעלה דרך השטח.</p>
             <p>המטרה: להגיע אל <strong style="color: #1A4F23;">השדות החקלאיים</strong> הירוקים כהים.</p>
             <p><strong style="color: red;">טיפ קדום:</strong> מים זורמים רק במורד, ובשיפוע עדין מספיק! ודא שהתעלה שלך יורדת בהדרגה.</p>
         </div>
    </div>
    <div class="button-container">
        <button id="simulate-btn" disabled>הפעל סימולציה</button>
        <button id="clear-btn">נקה תעלה</button>
    </div>
</div>

<button id="show-explanation-btn">הצג/הסתר סיפור וסודות ההנדסה הקדומה</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: הנדסת מים קדומה</h2>
    <p>תרבויות חקלאיות עתיקות, רבות מהן באזורים צחיחים או עם עונתיות גדולה של גשמים, תלויות לחלוטין באספקת מים יציבה ליבולים שלהן. ללא יכולת לשלוט במים, התפתחותן הייתה מוגבלת ביותר. הצורך הזה הוליד פתרונות הנדסיים מדהימים שהתבססו על הבנה עמוקה של הטבע והשטח.</p>

    <h3>דוגמאות למערכות השקיה קדומות מופלאות</h3>
    <p>ברחבי העולם הקדום התפתחו מערכות השקיה מרשימות ביותר, ששינו את פני התרבויות שבנו אותן:</p>
    <ul>
        <li>**תרבות המאיה (מרכז אמריקה):** למרות שחיו באזורים עם גשמים עונתיים, המאיה בנו מאגרי מים ענקיים ותעלות מתוחכמות כדי לאגור מים לעונה היבשה ולהבטיח יבול רציף. הם התאימו את המערכות לטופוגרפיה המאתגרת של גבעות וקרקע נקבובית, תוך שימוש בחומרים מקומיים ובטכניקות בנייה מדויקות.</li>
        <li>**תרבות האינקה (הרי האנדים):** האינקה היו אדוני השטח. הם בנו מערכות טרסות אדירות בגודלן והשקיה מורכבות להפליא במורדות ההרים התלולים של הרי האנדים. הם השתמשו בתעלות אבן מסותתות בדייקנות יוצאת דופן כדי להוביל מים ממקורות גבוהים (אגמים ושלגים נמסים) אל השדות המדורגים, לעיתים למרחקים של עשרות קילומטרים.</li>
        <li>**מסופוטמיה ומצרים הקדומה:** בערי המדינה של מסופוטמיה שבין הנהרות פרת וחידקל, וסביב נהר הנילוס במצרים, נבנו מערכות תעלות ובריכות השקיה בקנה מידה עצום. הצפות העונתיות של הנהרות נוצלו לא רק להשקיה אלא גם להעשרת הקרקע בסחף פורה, שאיפשר חקלאות אינטנסיבית.</li>
        <li>**מערכת הפוגארות (איראן וצפון אפריקה):** זוהי מערכת גאונית של תעלות תת-קרקעיות (קאנאט) שמובילה מים ממעיינות או אקוויפרים בהרים למרחקים ארוכים באזורים מדבריים ויבשים, תוך צמצום דרמטי של אידוי המים. המערכות האלו, שנבנו בעבודה ידנית קשה, עדיין פעילות בחלקן עד היום.</li>
    </ul>

    <h3>העקרונות הפיזיקליים הבסיסיים: כבידה ושיפוע מדויק</h3>
    <p>ללא משאבות או טכנולוגיה מודרנית, הדרך היחידה להוביל מים לאורך זמן בתעלה פתוחה היא באמצעות ניצול קפדני של כוח הכבידה. זה מחייב שהתעלה תהיה תמיד בשיפוע ירידה עדין ועקבי ממקור המים ועד ליעד (השדה החקלאי). שיפוע תלול מדי יגרום למים לזרום מהר מדי, לשחוק ולפגוע בתעלה ואף לגרום להצפות נקודתיות; שיפוע מתון מדי (או אפילו עלייה קלה) יגרום למים לעמוד, להתאדות, או לזרום אחורנית, ולא להגיע ליעד כלל.</p>
    <p>האתגר האמיתי בהנדסה הקדומה היה לא רק למצוא נתיב ירידה, אלא לשמור על שיפוע מדויק ונכון לאורך קילומטרים רבים של שטח משתנה, לעיתים עם ירידה כוללת של מטרים בודדים בלבד על פני עשרות קילומטרים. זה דרש הבנה עמוקה של הטופוגרפיה ויכולת מדידה מדויקת, יחסית לכלים שעמדו לרשותם.</p>

    <h3>אתגרים הנדסיים ובנייה חכמה</h3>
    <p>בניית תעלות במערכות עתיקות כללה אתגרים רבים שדרשו יצירתיות והתמדה:</p>
    <ul>
        <li>**מעבר מכשולים טופוגרפיים:** היה צורך לתכנן נתיבים ארוכים ומפותלים לעקיפת גבעות, לחצות עמקים באמצעות גשרים מרשימים (אמות מים, אקוודוקטים), או לחצוב בסלע קשה.</li>
        <li>**מניעת איבוד מים:** התעלות היו צריכות להיות אטומות יחסית כדי למנוע ספיגה מוגזמת בקרקע או אידוי בשמש הקופחת. השתמשו בחומרים זמינים כמו חימר כבוש, אבנים מסותתות עם מלט (הרומאים היו מומחים בכך), ואף טיח מיוחד.</li>
        <li>**תחזוקה שוטפת:** תעלות פתוחות נוטות להתמלא במהירות בסחף, אבק, צמחייה ואף בעלי חיים קטנים. ניקוי ותיקון שוטפים היו קריטיים לתפקוד המערכת ולא נפסקו לעולם.</li>
        <li>**שליטה על זרימת המים:** היה צורך לבנות שערים, מדרגות ומנגנוני ויסות מים פשוטים אך יעילים כדי לשלוט בכמות המים הזורמת, לפתוח ולסגור יובלים, ולהפנות את המים לשדות הנכונים בזמן הנכון, בהתאם לצרכים ולעונות.</li>
    </ul>

    <h3>שיטות וכלים פשוטים לבנייה</h3>
    <p>אז איך בנו את כל זה ללא טרקטורים ומכשירי לייזר? בעיקר באמצעות עבודה ידנית אינסופית וכלים פשוטים אך מתוחכמים לזמנם:</p>
    <ul>
        <li>**כלי חפירה:** אתי חפירה מעץ ועצם, מעדרים, מכושים, סלי נשיאה עשויים קש או עור, מריצות פרימיטיביות.</li>
        <li>**כלי מדידה:** ככל הנראה השתמשו במכשירי פלס פשוטים ביותר המבוססים על כבידה וקווים ישרים, כמו "פלס A" (בצורת האות A עם חוט ומשקולת), מיתר מתוח עם משקולת (עבור אנך ושיפוע), וכלים למדידת זווית וכיוון יחסיים בשטח.</li>
        <li>**חומרי בנייה:** אדמה מקומית, חימר, חול, אבנים (שנאספו או נחצבו וסותתו), עץ, סיבים צמחיים (לקשירה), ולעיתים גם מלט עשוי סיד ואפר וולקני (כמו הפוצולנה הרומית).</li>
    </ul>

    <h3>השפעה על התפתחות וחוסן חברתי</h3>
    <p>היכולת לשלוט, לנהל ולחלק את משאבי המים הייתה גורם קריטי להתפתחות חברות אנושיות מורכבות. מערכות השקיה גדולות דרשו ארגון חברתי מסועף, שיתוף פעולה רחב היקף בין כפרים ואזורים, ותיאום מרכזי לבנייה, תחזוקה וחלוקה. זה תרם ליצירת מבנים שלטוניים וביורוקרטיים מרכזיים. הצלחת החקלאות המבוססת על השקיה אפשרה גידול דרמטי באוכלוסייה, התפתחות ערים גדולות, ואף תמיכה בצבאות ובמבני ציבור מונומנטליים (מקדשים, פירמידות ועוד). לעומת זאת, קריסת מערכות המים, בין אם עקב אסונות טבע, מלחמות או הזנחה, יכלה להוביל במהירות לרעב כבד, סכסוכים אלימים, ואף קריסה מוחלטת של החברה כולה.</p>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Alef:wght@400;700&display=swap');

    #irrigation-app {
        font-family: 'Alef', sans-serif;
        max-width: 900px;
        margin: 20px auto;
        padding: 25px;
        border: 1px solid #d3d3d3;
        border-radius: 10px;
        background-color: #eef4f7;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        position: relative;
        overflow: hidden; /* Ensure absolute positioned elements stay within app */
    }

    #irrigation-app h2 {
        text-align: center;
        color: #333;
        margin-top: 0;
        margin-bottom: 20px;
        font-weight: 700;
    }

    #map-container {
        position: relative;
        width: 100%;
        padding-bottom: 60%; /* Maintain aspect ratio */
        height: 0; /* Required for padding-bottom hack */
        background-color: #eee; /* Base color before drawing terrain */
        border: 2px solid #aaa;
        margin-bottom: 20px;
        border-radius: 8px;
        overflow: hidden; /* Hide anything drawn outside borders */
    }

    #irrigationCanvas {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: block;
        cursor: crosshair;
    }

    .message {
        position: absolute;
        top: 15px;
        background-color: rgba(255, 255, 255, 0.95);
        padding: 8px 15px;
        border-radius: 5px;
        font-size: 0.9em;
        z-index: 10; /* Ensure it's above canvas */
        min-width: 150px;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
         border: 1px solid #ccc;
    }

     #feedback {
        right: 15px;
        color: #333;
     }

    #slope-feedback {
         left: 15px;
         color: #333;
     }

    #elevation-legend {
        position: absolute;
        bottom: 15px;
        left: 15px;
        background-color: rgba(255, 255, 255, 0.95);
        padding: 10px 15px;
        border-radius: 5px;
        font-size: 0.8em;
        z-index: 10;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        border: 1px solid #ccc;
    }
    #elevation-legend h3 {
        margin-top: 0;
        margin-bottom: 8px;
        font-size: 1em;
        color: #555;
        border-bottom: 1px solid #eee;
        padding-bottom: 5px;
    }
    .legend-item {
        display: flex;
        align-items: center;
        margin-bottom: 4px;
    }
    .legend-item .color-box {
        width: 18px;
        height: 18px;
        margin-right: 8px;
        border: 1px solid #333;
        border-radius: 3px;
        box-shadow: inset 0 0 3px rgba(0,0,0,0.1);
    }
     .legend-item .label {
         color: #555;
     }

     #instructions {
         position: absolute;
         top: 15px;
         left: 15px;
         background-color: rgba(255, 255, 255, 0.95);
         padding: 15px;
         border-radius: 5px;
         font-size: 0.9em;
         max-width: 40%; /* Prevent instructions from covering too much map */
         z-index: 10;
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
         border: 1px solid #ccc;
         text-align: right;
     }
     #instructions p {
         margin: 8px 0;
         line-height: 1.4;
         color: #444;
     }
      #instructions strong {
          font-weight: 700;
      }


    .button-container {
        text-align: center;
        margin-top: 15px;
    }

    button {
        padding: 12px 20px;
        margin: 0 8px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        background-color: #007bff;
        color: white;
        font-size: 1em;
        font-weight: 700;
        transition: background-color 0.3s ease, opacity 0.3s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    button:disabled {
        background-color: #ccc;
        cursor: not-allowed;
        opacity: 0.7;
        box-shadow: none;
    }
    button:hover:not(:disabled) {
        background-color: #0056b3;
    }

    #show-explanation-btn {
        display: block;
        width: fit-content;
        margin: 20px auto;
        background-color: #6c757d;
        padding: 10px 15px;
        font-size: 0.9em;
    }
     #show-explanation-btn:hover {
         background-color: #5a6268;
     }


    #explanation {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid #ccc;
        font-family: 'Alef', sans-serif;
        line-height: 1.6;
        color: #333;
    }
    #explanation h2, #explanation h3 {
        color: #0056b3;
        margin-bottom: 10px;
        font-weight: 700;
    }
     #explanation h3 {
         margin-top: 20px;
         font-size: 1.2em;
     }
    #explanation p, #explanation ul {
        margin-bottom: 15px;
    }
    #explanation ul {
        padding-left: 20px;
    }
    #explanation li {
        margin-bottom: 8px;
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const canvas = document.getElementById('irrigationCanvas');
        const ctx = canvas.getContext('2d');
        const feedbackDiv = document.getElementById('feedback');
        const slopeFeedbackDiv = document.getElementById('slope-feedback');
        const simulateBtn = document.getElementById('simulate-btn');
        const clearBtn = document.getElementById('clear-btn');
        const showExplanationBtn = document.getElementById('show-explanation-btn');
        const explanationDiv = document.getElementById('explanation');
        const instructionsDiv = document.getElementById('instructions');

        let drawing = false;
        let path = []; // Store points: [{x, y, elevation, valid}, ...]
        let terrain = []; // 2D array representing elevation
        const mapSize = 120; // Grid size (increased for smoother terrain)
        const waterSource = { x: 100, y: 20, elevation: 100 }; // Coordinates in grid units
        const farmArea = { x: 30, y: 100, elevation: 15 }; // Coordinates in grid units
        const maxSlope = 0.1; // Maximum acceptable slope (e.g., 10% drop over distance)
        const minSlope = 0.008; // Minimum acceptable slope (must drop slightly, adjusted for smoother flow)
        const pointSnapRadius = 15; // Radius in canvas pixels to snap to water/farm points

        // --- Terrain Generation and Drawing ---
        function generateTerrain(size) {
            const data = [];
            // Simple Perlin/Simplex noise base (conceptually, simplified here with gradients and bumps)
            function noise(nx, ny) {
                // Basic procedural terrain: combine gradients, bumps, and randomness
                let elevation = 70 - (ny * 0.4 + nx * 0.15) + Math.random() * 8; // General slope + base noise

                // Add main hill/mountain feature
                const hillCenterX = size * 0.6;
                const hillCenterY = size * 0.4;
                const hillRadius = size * 0.4;
                const distToHill = Math.sqrt(Math.pow(nx - hillCenterX, 2) + Math.pow(ny - hillCenterY, 2));
                if (distToHill < hillRadius) {
                    elevation += (1 - distToHill / hillRadius) * 40 * (1 + Math.random() * 0.2); // Higher, more varied hill
                }

                 // Add a valley feature
                 const valleyCenterX = size * 0.3;
                 const valleyCenterY = size * 0.7;
                 const valleyRadius = size * 0.35;
                 const distToValley = Math.sqrt(Math.pow(nx - valleyCenterX, 2) + Math.pow(ny - valleyCenterY, 2));
                 if (distToValley < valleyRadius) {
                     elevation -= (1 - distToValley / valleyRadius) * 20 * (1 + Math.random() * 0.1); // Lower in valley
                 }


                 // Ensure water source is high and farm is low relative to surroundings and fixed points
                 if (nx > waterSource.x - 5 && nx < waterSource.x + 5 && ny > waterSource.y - 5 && ny < waterSource.y + 5) {
                     elevation = waterSource.elevation + (Math.random() * 5 - 2.5); // Slightly vary elevation around source
                 }
                 if (nx > farmArea.x - 5 && nx < farmArea.x + 5 && ny > farmArea.y - 5 && ny < farmArea.y + 5) {
                     elevation = farmArea.elevation + (Math.random() * 5 - 2.5); // Slightly vary elevation around farm
                 }


                return Math.max(5, elevation); // Ensure minimum elevation
            }

            for (let y = 0; y < size; y++) {
                data[y] = [];
                for (let x = 0; x < size; x++) {
                    data[y][x] = noise(x, y);
                }
            }

             // Refine exact points for water source and farm area for easy snapping
             data[waterSource.y][waterSource.x] = waterSource.elevation;
             data[farmArea.y][farmArea.x] = farmArea.elevation;


            return data;
        }

        // Function to get elevation from grid based on canvas coordinates
        function getElevation(canvasX, canvasY) {
            const gridX = Math.max(0, Math.min(mapSize - 1, Math.floor(canvasX / canvas.width * mapSize)));
            const gridY = Math.max(0, Math.min(mapSize - 1, Math.floor(canvasY / canvas.height * mapSize)));
            // Use bilinear interpolation for smoother elevation lookup (optional but improves realism)
            // For simplicity, using nearest neighbor for now.
            return terrain[gridY][gridX];
        }

        // Function to draw the terrain using color mapping
        function drawTerrain() {
            const imgData = ctx.createImageData(canvas.width, canvas.height);
            const data = imgData.data;
            const maxElev = Math.max(...terrain.flat());
            const minElev = Math.min(...terrain.flat());

            // Define richer color palette matching legend
            const colors = [
                { elev: farmArea.elevation, color: [26, 79, 35] }, // Dark Green (Farm Target) - base
                { elev: minElev, color: [26, 79, 35] }, // Dark Green (lowest)
                { elev: 30, color: [34, 139, 34] }, // Forest Green (lowland)
                { elev: 60, color: [143, 188, 143] }, // Dark Sea Green (mid ground)
                { elev: 80, color: [240, 128, 128] }, // Light Coral (high ground)
                { elev: 120, color: [165, 42, 42] }  // Brown (high peaks)
            ];

            for (let y = 0; y < canvas.height; y++) {
                for (let x = 0; x < canvas.width; x++) {
                    const gridX = Math.floor(x / canvas.width * mapSize);
                    const gridY = Math.floor(y / canvas.height * mapSize);
                    const elevation = terrain[gridY][gridX];
                    // Basic color interpolation based on elevation
                    let color = [0, 0, 0];
                    for(let i = 0; i < colors.length - 1; i++) {
                         if (elevation >= colors[i].elev && elevation <= colors[i+1].elev) {
                             const range = colors[i+1].elev - colors[i].elev;
                             const blend = (elevation - colors[i].elev) / range;
                             color[0] = colors[i][0] + (colors[i+1][0] - colors[i][0]) * blend;
                             color[1] = colors[i][1] + (colors[i+1][1] - colors[i][1]) * blend;
                             color[2] = colors[i][2] + (colors[i+1][2] - colors[i][2]) * blend;
                             break;
                         } else if (elevation < colors[0].elev) {
                              color = colors[0].color; break;
                         } else if (elevation > colors[colors.length - 1].elev) {
                             color = colors[colors.length - 1].color; break;
                         }
                    }

                    // Simple check if point is within any color range before defaulting (fallback)
                     if (color[0] === 0 && color[1] === 0 && color[2] === 0) {
                         // Fallback to simplified ranges if interpolation fails
                         if (elevation < 25) color = [26, 79, 35];
                         else if (elevation < 50) color = [34, 139, 34];
                         else if (elevation < 75) color = [143, 188, 143];
                         else if (elevation < 90) color = [240, 128, 128];
                         else color = [165, 42, 42];
                     }


                     // Highlight water source area
                     const waterCanvasX = waterSource.x / mapSize * canvas.width;
                     const waterCanvasY = waterSource.y / mapSize * canvas.height;
                     const distToWater = Math.sqrt(Math.pow(x - waterCanvasX, 2) + Math.pow(y - waterCanvasY, 2));
                     const waterRadius = canvas.width * 0.04;
                     if (distToWater < waterRadius) {
                          // Simple gradient to blue for water source
                          const waterBlend = (waterRadius - distToWater) / waterRadius;
                          color[0] = color[0] * (1 - waterBlend) + 30 * waterBlend; // Blend with blue
                          color[1] = color[1] * (1 - waterBlend) + 144 * waterBlend;
                          color[2] = color[2] * (1 - waterBlend) + 255 * waterBlend;
                     }

                     // Highlight farm area
                     const farmCanvasX = farmArea.x / mapSize * canvas.width;
                     const farmCanvasY = farmArea.y / mapSize * canvas.height;
                     const distToFarm = Math.sqrt(Math.pow(x - farmCanvasX, 2) + Math.pow(y - farmCanvasY, 2));
                     const farmRadius = canvas.width * 0.04;
                      if (distToFarm < farmRadius) {
                          // Simple blend to target farm color
                          const farmBlend = (farmRadius - distToFarm) / farmRadius;
                           color[0] = color[0] * (1 - farmBlend) + 0 * farmBlend;
                           color[1] = color[1] * (1 - farmBlend) + 100 * farmBlend;
                           color[2] = color[2] * (1 - farmBlend) + 0 * farmBlend;
                     }


                    const index = (y * canvas.width + x) * 4;
                    data[index] = color[0];
                    data[index + 1] = color[1];
                    data[index + 2] = color[2];
                    data[index + 3] = 255; // Alpha
                }
            }
            ctx.putImageData(imgData, 0, 0);
        }

        // Draw the current path and potential next segment preview
        function drawPath(previewPoint = null) {
            ctx.lineWidth = 6; // Thicker line for the canal
            ctx.lineCap = 'round';
            ctx.lineJoin = 'round';

            // Draw existing path segments
            if (path.length > 0) {
                 ctx.beginPath();
                 ctx.moveTo(path[0].x, path[0].y);
                for (let i = 1; i < path.length; i++) {
                    const p1 = path[i - 1];
                    const p2 = path[i];
                    ctx.strokeStyle = p2.valid ? '#28a745' : '#dc3545'; // Green for valid, Red for invalid
                    ctx.lineTo(p2.x, p2.y);
                    ctx.stroke();
                    // Start a new path for the next segment to apply correct color
                    ctx.beginPath();
                    ctx.moveTo(p2.x, p2.y);
                }
            }

             // Draw preview segment if drawing and mouse is over canvas
             if (drawing && path.length > 0 && previewPoint) {
                 const lastPoint = path[path.length - 1];
                 const currentElevation = getElevation(previewPoint.x, previewPoint.y);
                 const deltaElevation = currentElevation - lastPoint.elevation;
                 const distance = Math.sqrt(Math.pow(previewPoint.x - lastPoint.x, 2) + Math.pow(previewPoint.y - lastPoint.y, 2));
                 let isValid = false;
                 if (distance > 0) {
                      const slope = deltaElevation / distance;
                      isValid = slope < -minSlope && slope > -maxSlope;
                 }

                 ctx.beginPath();
                 ctx.moveTo(lastPoint.x, lastPoint.y);
                 ctx.strokeStyle = isValid ? 'rgba(40, 167, 69, 0.7)' : 'rgba(220, 53, 69, 0.7)'; // Semi-transparent preview color
                 ctx.lineTo(previewPoint.x, previewPoint.y);
                 ctx.stroke();

                 // Update slope feedback
                 if (distance > 0) {
                      const slopePercent = (-deltaElevation / distance * 100).toFixed(1); // Positive for downhill
                      slopeFeedbackDiv.textContent = `שיפוע למקטע הבא: ${slopePercent}% ירידה. ${isValid ? 'תקין!' : 'לא מתאים.'}`;
                      if(isValid) slopeFeedbackDiv.style.color = '#28a745';
                      else slopeFeedbackDiv.style.color = '#dc3545';
                 } else {
                     slopeFeedbackDiv.textContent = 'הזז עכבר לשרטט מקטע.';
                      slopeFeedbackDiv.style.color = '#333';
                 }

             } else if (!drawing) {
                 slopeFeedbackDiv.textContent = ''; // Clear slope feedback when not drawing
             }


             // Draw dots at points (larger, more prominent)
             path.forEach(p => {
                 ctx.fillStyle = p.valid ? '#1a73e8' : '#dc3545'; // Blue for valid points, Red for points following invalid segment
                 ctx.beginPath();
                 ctx.arc(p.x, p.y, 7, 0, Math.PI * 2);
                 ctx.fill();
                 ctx.strokeStyle = '#fff'; // White outline
                 ctx.lineWidth = 2;
                 ctx.stroke();
             });

             // Highlight start (Water) and End (Farm) points specifically if path is empty or complete
             if (!drawing || (drawing && path.length === 0)) {
                 drawHighlightCircle(waterSource.x / mapSize * canvas.width, waterSource.y / mapSize * canvas.height, pointSnapRadius, 'rgba(30, 144, 255, 0.4)');
             }
             if (!drawing || (drawing && isNearFarmArea(path[path.length-1]?.x, path[path.length-1]?.y))) { // Highlight farm if not drawing or if path ends near farm
                  drawHighlightCircle(farmArea.x / mapSize * canvas.width, farmArea.y / mapSize * canvas.height, pointSnapRadius, 'rgba(0, 100, 0, 0.4)');
             }
        }

        function drawHighlightCircle(x, y, radius, color) {
             ctx.fillStyle = color;
             ctx.beginPath();
             ctx.arc(x, y, radius, 0, Math.PI * 2);
             ctx.fill();
        }


        // Check if a point is close to the water source (canvas coordinates)
         function isNearWaterSource(canvasX, canvasY) {
             const waterCanvasX = waterSource.x / mapSize * canvas.width;
             const waterCanvasY = waterSource.y / mapSize * canvas.height;
             const dist = Math.sqrt(Math.pow(canvasX - waterCanvasX, 2) + Math.pow(canvasY - waterCanvasY, 2));
             return dist < pointSnapRadius;
         }

          // Check if a point is close to the farm area (canvas coordinates)
          function isNearFarmArea(canvasX, canvasY) {
               if (canvasX === undefined || canvasY === undefined) return false; // Handle case where path is empty
              const farmCanvasX = farmArea.x / mapSize * canvas.width;
              const farmCanvasY = farmArea.y / mapSize * canvas.height;
              const dist = Math.sqrt(Math.pow(canvasX - farmCanvasX, 2) + Math.pow(canvasY - farmCanvasY, 2));
              return dist < pointSnapRadius;
          }


        // Handle canvas click
        canvas.addEventListener('click', (event) => {
            const rect = canvas.getBoundingClientRect();
            const x = event.clientX - rect.left;
            const y = event.clientY - rect.top;
            const elevation = getElevation(x, y);

            if (!drawing) { // Start drawing sequence
                if (isNearWaterSource(x, y)) {
                     // Snap to exact water source canvas coordinates
                     const waterCanvasX = waterSource.x / mapSize * canvas.width;
                     const waterCanvasY = waterSource.y / mapSize * canvas.height;
                     path.push({ x: waterCanvasX, y: waterCanvasY, elevation: getElevation(waterCanvasX, waterCanvasY), valid: true }); // Start at water source's actual elevation
                    drawing = true;
                    feedbackDiv.textContent = 'מעולה! התחלת ממקור המים. המשך לשרטט לעבר השדות.';
                    feedbackDiv.style.color = '#333';
                    instructionsDiv.style.display = 'none'; // Hide instructions after starting
                    simulateBtn.disabled = true; // Disable simulate while drawing
                } else {
                    feedbackDiv.textContent = 'עליך להתחיל מנקודת מקור המים הכחולה.';
                    feedbackDiv.style.color = '#dc3545';
                }
            } else { // Continue drawing
                 // Check if the last point is the same as the current point (or very close)
                 const lastPoint = path[path.length - 1];
                 const distToLast = Math.sqrt(Math.pow(x - lastPoint.x, 2) + Math.pow(y - lastPoint.y, 2));
                 if (distToLast < 15) { // Prevent adding points too close (adjust tolerance)
                      feedbackDiv.textContent = 'הנקודה קרובה מדי לנקודה הקודמת. בחר נקודה רחוקה יותר.';
                       feedbackDiv.style.color = '#dc3545';
                      return;
                 }

                // Check slope for the new segment BEFORE adding
                const prevPoint = path[path.length - 1];
                const currentElevation = getElevation(x, y);
                const deltaElevation = currentElevation - prevPoint.elevation;
                const distance = Math.sqrt(Math.pow(x - prevPoint.x, 2) + Math.pow(y - prevPoint.y, 2));

                let isValidSegment = false;
                if (distance > 0) {
                    const slope = deltaElevation / distance; // Negative for downhill
                     // Slope must be negative (downhill), not too steep, and not too flat
                    isValidSegment = slope < -minSlope && slope > -maxSlope;
                }

                const newPoint = { x: x, y: y, elevation: currentElevation, valid: isValidSegment };

                // If the PREVIOUS segment was invalid, this segment is also invalid
                 if (path.length > 1 && !path[path.length-1].valid) {
                     newPoint.valid = false;
                 }


                path.push(newPoint);

                if (newPoint.valid) {
                    feedbackDiv.textContent = 'מקטע תעלה תקין! המשך לשרטט.';
                    feedbackDiv.style.color = '#28a745';
                } else {
                    feedbackDiv.textContent = `אופס! שיפוע לא מתאים במקטע זה. נסה לבחור נקודה נמוכה יותר או רחוקה יותר.`;
                    feedbackDiv.style.color = '#dc3545';
                }

                // Check if the path reached the farm area with a VALID last segment
                 if (newPoint.valid && isNearFarmArea(x, y)) {
                     drawing = false; // Stop drawing
                     simulateBtn.disabled = false;
                     feedbackDiv.textContent = 'מעולה! התעלה הגיעה בהצלחה לשדות! כעת הפעל את הסימולציה ובדוק את הזרימה.';
                     feedbackDiv.style.color = '#0056b3';
                      // Snap the last point to the farm area for a clean finish
                     const farmCanvasX = farmArea.x / mapSize * canvas.width;
                     const farmCanvasY = farmArea.y / mapSize * canvas.height;
                     path[path.length - 1].x = farmCanvasX;
                     path[path.length - 1].y = farmCanvasY;
                     path[path.length - 1].elevation = getElevation(farmCanvasX, farmCanvasY); // Use actual farm elevation
                 } else if (!newPoint.valid) {
                     // If an invalid segment was added, disable the simulate button
                     simulateBtn.disabled = true;
                 }
            }
            drawCanvas(); // Redraw everything
        });

        // Add mousemove listener for drawing preview
        canvas.addEventListener('mousemove', (event) => {
            if (drawing && path.length > 0) {
                const rect = canvas.getBoundingClientRect();
                const x = event.clientX - rect.left;
                const y = event.clientY - rect.top;
                drawCanvas({x: x, y: y}); // Redraw with preview
            }
        });

        canvas.addEventListener('mouseout', () => {
            if(drawing) {
                drawCanvas(); // Redraw without preview when mouse leaves
                slopeFeedbackDiv.textContent = ''; // Clear slope feedback
                 slopeFeedbackDiv.style.color = '#333';
            }
        });


        // Draw everything on the canvas
        function drawCanvas(previewPoint = null) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            drawTerrain();
            drawPath(previewPoint);
        }

        // --- Simulation Animation ---
        let animationFrameId = null;
        let startTime = null;
        let waterPosition = 0; // Progress along the path (0 to 1)
        const waterSpeed = 0.05; // Speed factor (percentage of total path per second)

        function simulateWaterFlow(timestamp) {
            if (!startTime) startTime = timestamp;
            const elapsedTime = timestamp - startTime;
            const totalPathLength = calculateTotalPathLength();
            const distanceCovered = (elapsedTime / 1000) * (totalPathLength * waterSpeed); // distance based on elapsed time and speed factor

            waterPosition = distanceCovered;

            drawCanvas(); // Redraw terrain and static path

            // Draw the water flow
            ctx.strokeStyle = '#4682B4'; // Steel Blue for water
            ctx.lineWidth = 6; // Same width as canal
            ctx.lineCap = 'round';

            ctx.beginPath();

            let currentDistance = 0;
            let reachedEndOfWater = false; // Flag to stop drawing water past the current position

            if (path.length > 0) {
                ctx.moveTo(path[0].x, path[0].y);
                for (let i = 1; i < path.length; i++) {
                    if (reachedEndOfWater) break;

                    const p1 = path[i - 1];
                    const p2 = path[i];
                    const segmentDist = Math.sqrt(Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2));

                    if (currentDistance + segmentDist < waterPosition) {
                        // Draw the whole segment
                        ctx.lineTo(p2.x, p2.y);
                    } else {
                        // Draw only part of the segment
                        const remainingDist = waterPosition - currentDistance;
                        if (remainingDist > 0) {
                             const progress = remainingDist / segmentDist;
                             const waterX = p1.x + (p2.x - p1.x) * progress;
                             const waterY = p1.y + (p2.y - p1.y) * progress;
                             ctx.lineTo(waterX, waterY);
                        }
                        reachedEndOfWater = true; // Water ends within this segment
                    }
                    currentDistance += segmentDist;
                }
            }

            ctx.stroke(); // Draw the blue water line

            // Draw a moving circle at the head of the water
             if (!reachedEndOfWater && path.length > 1) {
                 // Find the segment where the water head is
                 let distSoFar = 0;
                 let waterHeadX = path[0].x;
                 let waterHeadY = path[0].y;
                 for(let i=1; i < path.length; i++) {
                     const p1 = path[i-1];
                     const p2 = path[i];
                     const segmentDist = Math.sqrt(Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2));
                     if (distSoFar + segmentDist >= waterPosition) {
                          const progressInSegment = (waterPosition - distSoFar) / segmentDist;
                          waterHeadX = p1.x + (p2.x - p1.x) * progressInSegment;
                          waterHeadY = p1.y + (p2.y - p1.y) * progressInSegment;
                          break;
                     }
                     distSoFar += segmentDist;
                 }

                 ctx.fillStyle = 'rgba(100, 180, 255, 0.9)'; // Lighter blue for the head
                 ctx.beginPath();
                 ctx.arc(waterHeadX, waterHeadY, 8, 0, Math.PI * 2); // Slightly larger circle
                 ctx.fill();
             }


            // Continue animation or finish
            if (waterPosition < totalPathLength) {
                animationFrameId = requestAnimationFrame(simulateWaterFlow);
            } else {
                // Animation finished
                feedbackDiv.textContent = 'המים הגיעו לשדות! הצלחת לבנות מערכת השקיה!';
                feedbackDiv.style.color = '#0056b3';
                startTime = null; // Reset timer
                waterPosition = 0; // Reset position for next run

                // Draw the full path and terrain one last time
                drawCanvas();
                 // Optional: Add a visual effect at the farm?
             }
        }

        // Helper to calculate total path length for simulation timing
         function calculateTotalPathLength() {
             let total = 0;
             for(let i=1; i < path.length; i++) {
                 const p1 = path[i-1];
                 const p2 = path[i];
                 total += Math.sqrt(Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2));
             }
             return total;
         }


        // Clear path and reset state
        function clearPath() {
            if (animationFrameId) {
                cancelAnimationFrame(animationFrameId);
                animationFrameId = null;
            }
            path = [];
            drawing = false;
            simulateBtn.disabled = true;
            feedbackDiv.textContent = '';
            slopeFeedbackDiv.textContent = '';
            instructionsDiv.style.display = 'block'; // Show instructions again
            startTime = null;
            waterPosition = 0;
            drawCanvas();
        }

         // Toggle explanation visibility
         showExplanationBtn.addEventListener('click', () => {
             const isHidden = explanationDiv.style.display === 'none';
             explanationDiv.style.display = isHidden ? 'block' : 'none';
             showExplanationBtn.textContent = isHidden ? 'הסתר סיפור וסודות ההנדסה הקדומה' : 'הצג/הסתר סיפור וסודות ההנדסה הקדומה';
         });


        simulateBtn.addEventListener('click', () => {
             // Before starting simulation, check if the LAST segment is valid AND the end point is near the farm
             const lastPoint = path[path.length - 1];
             const isPathCompleteAndValid = path.length > 1 && lastPoint.valid && isNearFarmArea(lastPoint.x, lastPoint.y);

             if (isPathCompleteAndValid) {
                 simulateBtn.disabled = true; // Disable button during simulation
                 feedbackDiv.textContent = 'המים מתחילים לזרום...';
                 feedbackDiv.style.color = '#0056b3';
                 startTime = null; // Reset start time for animation
                 simulateWaterFlow(performance.now()); // Start animation loop
             } else {
                  feedbackDiv.textContent = 'התעלה לא הושלמה בהצלחה לשדות, או שמכילה מקטעים לא תקינים.';
                  feedbackDiv.style.color = '#dc3545';
             }
         });

        clearBtn.addEventListener('click', clearPath);

        // Initialize canvas size based on container and draw initial state
        function resizeCanvas() {
            const container = document.getElementById('map-container');
            canvas.width = container.clientWidth;
            canvas.height = container.clientHeight;
            // Generate terrain only once on initial load
            if (terrain.length === 0) {
                 terrain = generateTerrain(mapSize);
            }
            drawCanvas(); // Draw initial state or redraw after resize
        }

        // Initial setup
        resizeCanvas();
        // Add resize listener to keep canvas responsive
        window.addEventListener('resize', resizeCanvas);

    });
</script>
```