---
title: "מפענחים את 'העין' של המכונה: טרנספורמרים בראייה ממוחשבת"
english_slug: deciphering-vision-transformers-in-images
category: "טכנולוגיה / מדעי המחשב"
tags: ["רשתות עצביות", "טרנספורמרים", "ראייה ממוחשבת", "למידה עמוקה", "בינה מלאכותית הסברתית"]
---
# מפענחים את 'העין' של המכונה: טרנספורמרים בראייה ממוחשבת

דמיינו מכונה שמצליחה לא רק 'לראות' תמונה, אלא באמת *להבין* אותה – לזהות עצמים, להבחין בפרטים עדינים ולקשר בין אזורים מרוחקים בסצנה, ממש כמו מוח אנושי. במשך שנים, רשתות קונבולוציה (CNNs) היו הגיבורות הבלתי מעורערות של התחום, אך כעת, אדריכלות חדשה ומסקרנת, ה'טרנספורמר', מגיעה מעולם הטקסט וכובשת בסערה גם את פסגת הראייה הממוחשבת. בואו נצלול פנימה ונפענח יחד את הסוד מאחורי היכולות החדשות הללו!

<div class="vit-container">
    <div class="vit-controls">
        <label for="layerSelect" class="control-label">בחר שכבת 'הקשב':</label>
        <select id="layerSelect" class="control-select">
            <option value="initial">שכבה התחלתית (מוקד מקומי)</option>
            <option value="intermediate">שכבה בינונית (קשרים בינוניים)</option>
            <option value="deep">שכבה עמוקה (ראייה גלובלית)</option>
        </select>
        <div class="visualization-legend">
            <div class="legend-item"><span class="legend-color" style="background-color: rgba(255, 0, 0, 0.2);"></span>קשב נמוך</div>
            <div class="legend-item"><span class="legend-color" style="background-color: rgba(255, 0, 0, 0.6);"></span>קשב בינוני</div>
            <div class="legend-item"><span class="legend-color" style="background-color: rgba(255, 0, 0, 1);"></span>קשב גבוה</div>
        </div>
    </div>
    <div class="vit-image-container">
        <img id="baseImage" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Everest_North_Face_Tibet_Luca_Galuzzi_2006.jpg/1024px-Everest_North_Face_Tibet_Luca_Galuzzi_2006.jpg" alt="Example image showing a mountain landscape" crossorigin="anonymous">
        <div id="patchesOverlay" class="patches-overlay"></div>
    </div>
    <div id="visualizationInfo" class="visualization-info">
        ✨ לחץ על טלאי כלשהו בתמונה כדי לגלות לאילו חלקים אחרים הוא 'מקשיב' בשכבה זו! ✨
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700&display=swap');

    .vit-container {
        font-family: 'Heebo', sans-serif;
        direction: rtl;
        max-width: 850px; /* Slightly wider */
        margin: 20px auto;
        padding: 20px; /* More padding */
        border: 1px solid #ddd; /* Softer border */
        border-radius: 12px; /* More rounded corners */
        background-color: #ffffff; /* Clean white background */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08); /* Subtle shadow */
    }

    .vit-controls {
        margin-bottom: 20px; /* More space below controls */
        display: flex;
        align-items: center;
        gap: 25px; /* Increased gap */
        flex-wrap: wrap;
        justify-content: center; /* Center controls when wrapped */
    }

    .control-label {
        font-weight: 500; /* Medium weight */
        color: #333;
    }

    .control-select {
        padding: 8px 12px; /* More padding */
        border-radius: 6px; /* More rounded */
        border: 1px solid #ccc;
        font-size: 1em;
        cursor: pointer;
        background-color: #f9f9f9;
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    .control-select:hover {
        border-color: #007bff;
    }

     .control-select:focus {
        outline: none;
        border-color: #007bff;
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.2);
    }


    .visualization-legend {
        display: flex;
        gap: 20px; /* Increased gap */
        font-size: 0.85em;
        color: #555;
    }

    .legend-item {
        display: flex;
        align-items: center;
        gap: 6px; /* Increased gap */
    }

    .legend-color {
        display: inline-block;
        width: 25px; /* Wider color swatch */
        height: 15px; /* Taller color swatch */
        border: 1px solid rgba(0, 0, 0, 0.1); /* Add border for clarity */
        border-radius: 3px;
    }


    .vit-image-container {
        position: relative;
        width: 100%;
        /* Aspect ratio set dynamically by JS */
        height: 0;
        overflow: hidden;
        border-radius: 8px; /* Match container border radius */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .vit-image-container img {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block; /* Remove potential extra space below image */
    }

    .patches-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: grid;
        grid-template-columns: repeat(var(--grid-cols), 1fr);
        grid-template-rows: repeat(var(--grid-rows), 1fr);
        gap: 0;
        z-index: 10; /* Ensure patches are well above the image */
    }

    .patch {
        border: 0.5px solid rgba(255, 255, 255, 0.2); /* Thinner, softer border */
        box-sizing: border-box;
        cursor: pointer;
        position: relative;
        /* Added transition for smooth hover and attention fade */
        transition: background-color 0.3s ease-out, border-color 0.2s ease;
    }

    .patch:hover {
        background-color: rgba(0, 123, 255, 0.15); /* More vibrant hover */
        border-color: rgba(0, 123, 255, 0.5);
    }

    .patch.selected {
         border: 2px solid #ffc107; /* Bright yellow border */
         box-shadow: 0 0 8px #ffc107; /* Matching shadow */
         z-index: 20; /* Bring selected patch forward */
         transform: scale(1.02); /* Slightly enlarge selected patch */
         transition: border-color 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease;
         /* Add a subtle pulse animation */
         animation: pulse-select 1.5s infinite ease-in-out;
    }

    @keyframes pulse-select {
        0% { box-shadow: 0 0 8px rgba(255, 193, 7, 0.8); }
        50% { box-shadow: 0 0 15px rgba(255, 193, 7, 0.4); }
        100% { box-shadow: 0 0 8px rgba(255, 193, 7, 0.8); }
    }

    .visualization-info {
        margin-top: 20px;
        padding: 12px;
        background-color: #e9f7ff; /* Light blue background */
        border: 1px solid #b8daff; /* Blue border */
        border-radius: 6px;
        text-align: center;
        font-size: 1em;
        color: #004085; /* Dark blue text */
    }

    /* Style for attention visualization (applied via JS background-color with rgba) */
    /* The transition on .patch handles the fade effect */


    #explanationButton {
        display: block;
        margin: 30px auto 20px auto; /* More space above and below */
        padding: 12px 25px; /* More padding */
        font-size: 1.1em; /* Slightly larger font */
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #007bff; /* Primary blue */
        color: white;
        text-align: center;
        transition: background-color 0.2s ease, box-shadow 0.2s ease;
        font-weight: 500;
    }

    #explanationButton:hover {
        background-color: #0056b3; /* Darker blue on hover */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

     #explanationButton:active {
        background-color: #003f7f; /* Even darker when active */
     }

    #explanationContent {
        display: none; /* Hidden by default */
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid #eee;
        line-height: 1.7; /* Improved readability */
        color: #333;
    }

    #explanationContent h2 {
        margin-top: 20px;
        margin-bottom: 12px;
        font-size: 1.5em;
        color: #0056b3; /* Match button blue */
        border-bottom: 1px solid #eee; /* Separator */
        padding-bottom: 5px;
    }

     #explanationContent h3 {
        margin-top: 15px;
        margin-bottom: 8px;
        font-size: 1.3em;
        color: #007bff; /* Lighter blue */
    }

    #explanationContent p {
        margin-bottom: 15px;
        line-height: 1.6;
    }

    #explanationContent ul {
        margin-bottom: 15px;
        padding-right: 20px; /* Indent list */
    }

     #explanationContent li {
        margin-bottom: 8px;
     }

</style>

<button id="explanationButton">הצג את ה'סוד' מאחורי הטרנספורמרים</button>

<div id="explanationContent">
    <h2>האתגר של הבנת תמונות על ידי מכונות: לא רק פיקסלים</h2>
    <p>עינינו רואות תמונה כמכלול בעל משמעות, סיפור ויחסים בין חלקיו. עבור מחשב, תמונה היא רק רשת ענקית של מספרים (פיקסלים). האתגר בראייה ממוחשבת הוא ללמד מכונות לתרגם את רשת הפיקסלים הזו להבנה עמוקה, היררכית וקשרית – זיהוי עצמים, סצנות, ואפילו רגשות.</p>

    <h2>מלכת הקונבולוציה: קווים לדמותה של ה-CNN</h2>
    <p>במשך עשורים, רשתות קונבולוציונליות (CNNs) שלטו ללא עוררין בתחום. הן בנויות משכבות שמפעילות מסננים קטנים על התמונה, וכל שכבה לומדת לזהות דפוסים מורכבים יותר בהתבסס על השכבה שקדמה לה – מקצוות וקווים פשוטים בשכבות הראשונות, ועד חלקי עצמים ועצמים שלמים בשכבות העמוקות. הן מצטיינות בלכידת מידע מקומי והיררכי, אך התמודדו עם קושי מובנה ליצור קשרים *ישירים* בין אזורים *מרוחקים* בתמונה ללא מעבר דרך כל ההיררכיה השכבות.</p>

    <h2>מהפכת הטרנספורמר: Attention Is All You Need (לא רק בטקסט!)</h2>
    <p>טרנספורמרים הגיחו לעולם במקור בתחום עיבוד שפה טבעית (NLP), והציגו יכולת חסרת תקדים להבין הקשרים ארוכי טווח במשפטים. במקום לעבד מילים בזו אחר זו, הם מסתמכים על מנגנון ה-Self-Attention (קשב עצמי), המאפשר למודל לשקול את החשיבות של כל מילה ביחס לכל מילה אחרת במשפט בו זמנית, וכך להבין הקשרים מורכבים ומרוחקים. הצלחה זו הדליקה נורה אדומה (או ירוקה!) בקרב חוקרי ראייה ממוחשבת.</p>

    <h2>Vision Transformers (ViT): לראות תמונות כסדרת 'מילים'</h2>
    <p>האתגר הגדול היה לגשר על הפער: טרנספורמרים אוהבים סדרות (של מילים), ותמונות הן רשתות דו-ממדיות. הפתרון הגאוני של מודל ה-Vision Transformer (ViT) היה פשוט: נתייחס לתמונה כאל סדרה של "טלאים" (patches) קטנים, וכל טלאי יהיה ה"מילה" שלנו!</p>

    <h3>המסע הוויזואלי מתחיל: חלוקה לטלאים והפיכה לווקטורים</h3>
    <p>השלב הראשון הוא חלוקת התמונה המקורית לריבועים קטנים ואחידים (נניח, 16x16 פיקסלים). כל טלאי כזה מומר לווקטור מספרי (באמצעות שכבה פשוטה). מכיוון שהטרנספורמר עצמו אינו יודע את הסדר הפיזי של ה"מילים" (הטלאים) שלו, מוסיפים לכל וקטור מידע על המיקום המקורי של הטלאי בתמונה (positional encoding).</p>

    <h3>Self-Attention בפעולה: ה'עיניים' של הטרנספורמר</h3>
    <p>כעת מגיעים הטרנספורמרים לפעולה. סדרת וקטורי הטלאים עוברת דרך שכבות טרנספורמר רבות, ובלב כל שכבה נמצא מנגנון ה-Self-Attention. כאן קורה הקסם: כל טלאי בתמונה שואל את עצמו: "לאילו טלאים אחרים בתמונה אני צריך 'להקשיב' כרגע כדי להבין את עצמי טוב יותר?". המנגנון מחשב עבור כל טלאי יחיד, עד כמה הוא קשור וצריך לשים "קשב" על כל טלאי אחר בתמונה (כולל עצמו). התוצאה היא מערך משקלי קשב - משקל גבוה בין טלאי א' לטלאי ב' אומר שטלאי א' שואב הרבה מידע מטלאי ב' כדי לעדכן את הייצוג הפנימי שלו.</p>

    <h3>מסע אל העומק: בנית הבנה הדרגתית של התמונה</h3>
    <p>היופי ב-ViT הוא המסע דרך השכבות. בשכבות הראשונות, מנגנון הקשב נוטה להיות ממוקד בטלאים קרובים גאומטרית, בדומה לשדות הקליטה הראשוניים של CNNs. אך ככל שמעמיקים לשכבות הטרנספורמר הבאות, מנגנון הקשב מסוגל ליצור קשרים ו"להקשיב" לטלאים מרוחקים יותר ויותר בתמונה. כך, המודל בונה בהדרגה ייצוג מורכב יותר של כל טלאי, תוך שילוב מידע קשרי מכל רחבי התמונה. בשכבות העמוקות, טלאי שמכסה חלק מעין של אדם למשל, יכול "להקשיב" לטלאי שמכסה את הפה או את היד, גם אם הם רחוקים פיזית, וכך לבנות הבנה הוליסטית יותר של האובייקט או הסצנה כולה.</p>

    <h2>ViT מול CNN: קרב על פסגת הראייה</h2>
    <p><strong>למה ViT מצטיין?</strong></p>
    <ul>
        <li><strong>קשרים גלובליים מההתחלה:</strong> יכולת לכידת יחסים ארוכי טווח בין חלקים מרוחקים היא טבעית ל-ViT בזכות ה-Attention.</li>
        <li><strong>מודל אחיד:</strong> אותה אדריכלות טרנספורמר יכולה לעבוד על טקסט ותמונות, מה שמאפשר פיתוח מודלי בסיס גדולים ורב-תכליתיים.</li>
        <li><strong>פחות הנחות מוקדמות:</strong> הטרנספורמר לומד את המבנה והקשרים מהדאטה, במקום להניח מראש מבנה היררכי מקומי כמו ב-CNNs.</li>
    </ul>
    <p><strong>היכן ViT מתקשה?</strong></p>
    <ul>
        <li><strong>רעב לדאטה:</strong> ViT דורשים לרוב כמויות אדירות של נתוני אימון כדי להתעלות על CNNs, במיוחד במשימות בהן יש מעט דאטה. אימון מוקדם על דאטה ענק (Pre-training) הוא לרוב הכרחי.</li>
        <li><strong>עלות חישובית:</strong> חישוב Attention בין כל זוג טלאים יכול להיות יקר עבור תמונות גדולות מאוד. פותחו וריאציות (כמו Swin Transformer) כדי להתמודד עם זה.</li>
    </ul>

    <h2>טרנספורמרים בשטח: מיישומים פורצי דרך</h2>
    <p>ViT וצאצאיו הפכו לכלי עבודה מרכזי ביישומי ראייה ממוחשבת רבים, החל מסיווג תמונות וזיהוי אובייקטים בדיוק שיא, דרך הבנת סצנות מורכבות (סגמנטציה), ועד ליצירת תמונות מדהימות מטקסט (מודלים כמו DALL-E, Midjourney) ויצירת תיאורים מילוליים לתמונות. הם שוברים שיאי ביצועים במשימות רבות ומעצבים את עתיד הראייה הממוחשבת.</p>

    <h2>הכלי האינטראקטיבי בפעולה: מסע חזותי אל ה-Attention</h2>
    <p>הסימולציה שמעליך היא ההזדמנות שלך לחוות את מנגנון ה-Self-Attention ממקור ראשון. בחר שכבה מהתפריט (התחלתית, בינונית, עמוקה) ולחץ על טלאי כלשהו בתמונה. תראה כיצד שאר הטלאים נצבעים באדום בעוצמות שונות. הצבע האדום הבהיר יותר מצביע על "קשב" גבוה יותר שהטלאי שבחרת הקדיש לטלאי הצבוע בשכבה הספציפית שבחרת. שים לב להבדלים בין השכבות: בשכבות הראשונות הקשב מקומי, ובשכבות העמוקות הוא מתפרס על פני אזורים רחוקים יותר ומסייע בבניית ההבנה הגלובלית של התמונה. זוהי הצצה ויזואלית מרתקת לאופן שבו מודלי הטרנספורמר בונים את התובנות הוויזואליות שלהם!</p>
</div>


<script>
    document.addEventListener('DOMContentLoaded', () => {
        const image = document.getElementById('baseImage');
        const patchesOverlay = document.getElementById('patchesOverlay');
        const layerSelect = document.getElementById('layerSelect');
        const visualizationInfo = document.getElementById('visualizationInfo');
        const explanationButton = document.getElementById('explanationButton');
        const explanationContent = document.getElementById('explanationContent');

        const GRID_SIZE = 10; // 10x10 grid of patches
        const NUM_PATCHES = GRID_SIZE * GRID_SIZE;
        const patches = [];
        let attentionData = {}; // Will store simulated attention weights
        let selectedPatchIndex = null;

        // Set CSS variables for grid
        patchesOverlay.style.setProperty('--grid-cols', GRID_SIZE);
        patchesOverlay.style.setProperty('--grid-rows', GRID_SIZE);

        // Helper to convert index to row/col
        const indexToCoords = (index) => ({
            row: Math.floor(index / GRID_SIZE),
            col: index % GRID_SIZE
        });

        // Helper to calculate distance between two patch indices
        const getDistance = (index1, index2) => {
            const c1 = indexToCoords(index1);
            const c2 = indexToCoords(index2);
            const dr = c1.row - c2.row;
            const dc = c1.col - c2.col;
            return Math.sqrt(dr * dr + dc * dc);
        };

        // Simulate attention data - More distinct simulation for layers
        const generateAttentionData = () => {
            const data = {
                initial: Array(NUM_PATCHES).fill(0).map(() => Array(NUM_PATCHES).fill(0)),
                intermediate: Array(NUM_PATCHES).fill(0).map(() => Array(NUM_PATCHES).fill(0)),
                deep: Array(NUM_PATCHES).fill(0).map(() => Array(NUM_PATCHES).fill(0))
            };

            const sigmaInitial = 1.5; // Very local
            const sigmaIntermediate = 3.0; // Wider local + some spread
            const sigmaDeep = 6.0; // Global influence

            // Define some simulated 'semantic' zones (very rough approximation for demo)
            // based on rows (vertical position is a strong cue in landscape)
            const zones = {
                sky: [0, 1],
                upperMountain: [2, 3],
                lowerMountain: [4, 5],
                ground: [6, 7, 8, 9],
            };

             // Simulate a few 'conceptually important' patches that might get global attention regardless of layer (arbitrary indices)
            const conceptualFocusPatches = new Set([
                 Math.floor(GRID_SIZE * 0.5 + GRID_SIZE * 0.4), // Near peak center
                 Math.floor(GRID_SIZE * 2.5 + GRID_SIZE * 0.6), // Feature on mountain side
                 Math.floor(GRID_SIZE * 7.5 + GRID_SIZE * 0.2), // Object on ground
            ]);


            for (let i = 0; i < NUM_PATCHES; i++) {
                let sumInitial = 0;
                let sumIntermediate = 0;
                let sumDeep = 0;

                const coordsI = indexToCoords(i);
                const zoneI = Object.keys(zones).find(key => zones[key].includes(coordsI.row));


                for (let j = 0; j < NUM_PATCHES; j++) {
                    const dist = getDistance(i, j);
                     const coordsJ = indexToCoords(j);
                     const zoneJ = Object.keys(zones).find(key => zones[key].includes(coordsJ.row));


                    // Initial layer: strong local, rapid decay
                    let weightInitial = Math.exp(-dist * dist / (2 * sigmaInitial * sigmaInitial));
                    data.initial[i][j] = weightInitial;
                    sumInitial += weightInitial;

                    // Intermediate layer: wider local + increased attention to patches in the *same* semantic zone
                    let weightIntermediate = Math.exp(-dist * dist / (2 * sigmaIntermediate * sigmaIntermediate));
                    if (zoneI && zoneJ && zoneI === zoneJ) {
                         weightIntermediate *= 1.5; // Boost attention within the same zone
                    }
                    data.intermediate[i][j] = weightIntermediate;
                    sumIntermediate += weightIntermediate;

                    // Deep layer: global attention, less dependent on distance, focuses on conceptual patches and cross-zone connections
                    let weightDeep = Math.exp(-dist / sigmaDeep); // Slower decay, more global base
                     if (conceptualFocusPatches.has(j)) {
                         weightDeep += 0.8; // Significant boost for conceptually important patches
                     }
                     if (zoneI && zoneJ && zoneI !== zoneJ) {
                         weightDeep += 0.3; // Add base attention for cross-zone interactions
                     }
                      // Add some general noise/global connectivity base
                     weightDeep += Math.random() * 0.05;


                    data.deep[i][j] = weightDeep;
                    sumDeep += weightDeep;
                }

                // Normalize weights so they sum (roughly) to 1 for each query patch (softmax-like behavior simulation)
                // Simple normalization by sum is common
                for (let j = 0; j < NUM_PATCHES; j++) {
                     // Add a small epsilon to avoid division by zero, although sums should be > 0
                    data.initial[i][j] /= (sumInitial + 1e-6);
                    data.intermediate[i][j] /= (sumIntermediate + 1e-6);
                    data.deep[i][j] /= (sumDeep + 1e-6);
                }
                 // Re-normalize more strictly to sum to 1 for alpha mapping
                 const finalSumInitial = data.initial[i].reduce((s, w) => s + w, 0);
                 const finalSumIntermediate = data.intermediate[i].reduce((s, w) => s + w, 0);
                 const finalSumDeep = data.deep[i].reduce((s, w) => s + w, 0);

                 for (let j = 0; j < NUM_PATCHES; j++) {
                     data.initial[i][j] /= (finalSumInitial + 1e-6);
                     data.intermediate[i][j] /= (finalSumIntermediate + 1e-6);
                     data.deep[i][j] /= (finalSumDeep + 1e-6);
                 }
            }
            return data;
        };


        // Create patch divs and add event listeners
        const createPatches = () => {
            patchesOverlay.innerHTML = ''; // Clear previous patches
            patches.length = 0; // Clear patches array
            for (let i = 0; i < NUM_PATCHES; i++) {
                const patch = document.createElement('div');
                patch.classList.add('patch');
                patch.dataset.index = i;
                patch.addEventListener('click', handlePatchClick);
                patchesOverlay.appendChild(patch);
                patches.push(patch);
            }
        };

        // Clear any existing visualization
        const clearVisualization = () => {
            patches.forEach(patch => {
                patch.style.backgroundColor = ''; // Remove background color (resets due to transition)
                patch.classList.remove('selected'); // Remove selected class
                 // Remove potential pulse animation class if added directly
                 patch.classList.remove('pulse-selected');
            });
            selectedPatchIndex = null;
            // Reset info text
             visualizationInfo.textContent = '✨ לחץ על טלאי כלשהו בתמונה כדי לגלות לאילו חלקים אחרים הוא \'מקשיב\' בשכבה זו! ✨';
        };

        // Update visualization based on selected patch and layer
        const updateVisualization = (patchIndex, layer) => {
            // Clear existing styles smoothly before applying new ones
            patches.forEach(p => p.style.backgroundColor = ''); // Start transition to transparent
            // Small delay before applying new colors to allow transition to finish
            setTimeout(() => {
                 clearVisualization(); // Clear classes and info text after styles reset

                selectedPatchIndex = patchIndex; // Store selected index
                patches[patchIndex].classList.add('selected'); // Highlight the clicked patch
                 // Add pulse animation class
                 patches[patchIndex].classList.add('pulse-selected');


                const attentionWeights = attentionData[layer][patchIndex];

                // Max weight is 1 because we normalized weights to sum to 1
                const maxWeight = 1; // Or find actual max for finer scaling, but 1 is simple and works with normalization


                patches.forEach((patch, j) => {
                    const weight = attentionWeights[j];
                    // Scale weight to 0-1 range for alpha channel
                    const alpha = Math.min(1, Math.max(0, weight)); // Alpha corresponds directly to weight after normalization

                    // Apply background color with calculated alpha
                    patch.style.backgroundColor = `rgba(255, 0, 0, ${alpha})`; // Red overlay with varying opacity
                });

                const layerText = layerSelect.options[layerSelect.selectedIndex].text;
                visualizationInfo.textContent = `👁️ טלאי נבחר #${patchIndex}. מציג עוצמת 'קשב' בשכבה: ${layerText}`;

            }, 350); // Delay slightly longer than the CSS transition duration

        };

        // Handle click on a patch
        const handlePatchClick = (event) => {
            const clickedPatchIndex = parseInt(event.target.dataset.index, 10);
            const currentLayer = layerSelect.value;
            updateVisualization(clickedPatchIndex, currentLayer);
        };

        // Handle change in layer selection
        const handleLayerChange = (event) => {
             const newLayer = event.target.value;
             if (selectedPatchIndex !== null) {
                 // If a patch is already selected, update the visualization for the new layer
                 updateVisualization(selectedPatchIndex, newLayer);
             } else {
                  // If no patch is selected, update info text
                  visualizationInfo.textContent = '✨ לחץ על טלאי כלשהו בתמונה כדי לגלות לאילו חלקים אחרים הוא \'מקשיב\' בשכבה זו! ✨';
             }
        };

        // Toggle explanation visibility
        const toggleExplanation = () => {
            const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
            explanationContent.style.display = isHidden ? 'block' : 'none';
            explanationButton.textContent = isHidden ? 'הסתר את ה'סוד' המפורט' : 'הצג את ה'סוד' מאחורי הטרנספורמרים';
        };


        // Initial setup
        image.onload = () => {
            // Ensure patches cover the image correctly after load
            const aspectRatio = image.naturalHeight / image.naturalWidth;
            const container = image.parentElement;
            // Set padding-bottom based on image aspect ratio
            container.style.paddingBottom = `${aspectRatio * 100}%`;

            createPatches();
            attentionData = generateAttentionData(); // Generate data once image dimensions are known
            layerSelect.addEventListener('change', handleLayerChange);
        };

        // Handle image load errors
         image.onerror = () => {
             visualizationInfo.textContent = 'שגיאה בטעינת התמונה. הסימולציה אינה זמינה.';
             patchesOverlay.style.display = 'none';
             layerSelect.disabled = true;
         };


        // Check if image is already loaded (cached)
         if (image.complete && image.naturalHeight > 0) {
             image.onload(); // Manually trigger onload if cached
         }


        // Explanation button listener
        explanationButton.addEventListener('click', toggleExplanation);

        // Initial state: Clear visualization in case of refresh with state
        clearVisualization();
    });
</script>