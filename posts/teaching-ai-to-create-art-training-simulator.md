---
title: "הסטודיו של ה-AI: סימולטור אימון ליצירת אמנות"
english_slug: teaching-ai-to-create-art-training-simulator
category: "מדעי המחשב"
tags: [בינה מלאכותית, למידת מכונה, למידה עמוקה, אמנות גנרטיבית, מודלים התפשטותיים, יצירה דיגיטלית]
---
<h1>הסטודיו של ה-AI: סימולטור אימון ליצירת אמנות</h1>
<p>איך מודל בינה מלאכותית עובר ממצב של "רעש אקראי" ליכולת מדהימה ליצור תמונות מקוריות ויפהפיות? האם זה קסם, או תהליך אימון מדויק? הסימולטור הזה מאפשר לך להשפיע על תהליך הלימוד ולראות כיצד שינויים קטנים ב"הגדרות הסטודיו" משפיעים על התוצאה הסופית.</p>
<p>התנסו עם ההגדרות השונות, התחילו אימון, צפו בהתקדמות ובתוצאות הביניים, ולבסוף בקשו מהמודל המאומן ליצור יצירה חדשה לגמרי על פי ההנחיות שלכם!</p>

<div id="app">
    <div class="controls panel">
        <h2>⚙️ הגדרות הסטודיו (אימון)</h2>
        <label for="dataset">🖼️ בחירת מוזה (קבוצת נתונים לאימון):</label>
        <select id="dataset">
            <option value="cats">🎨 ציורי חתולים (סגנון אקספרסיבי)</option>
            <option value="stormy-nature">⛰️ נופי טבע סוערים (אווירה דרמטית)</option>
            <option value="realistic-portraits">🧑‍🎨 פורטרטים ריאליסטיים (דיוק מרבי)</option>
        </select>

        <label for="steps">⏳ מספר שלבי לימוד (איטרציות):</label>
        <input type="number" id="steps" value="200" min="50" max="1000" step="50"><br>
        <small>כמה "שיעורים" המודל יקבל. יותר שלבים = פוטנציאל ללמידה עמוקה יותר, אך גם סיכון לאימון יתר.</small>

        <label for="learning-rate">⚡ קצב קליטה (Learning Rate):</label>
        <select id="learning-rate">
            <option value="0.00005">0.00005 (זהיר, יציב, איטי)</option>
            <option value="0.0001" selected>0.0001 (מאוזן)</option>
            <option value="0.0005">0.0005 (אגרסיבי, מהיר, פוטנציאל לאיבוד יציבות)</option>
        </select>
        <small>עד כמה "בתקיפות" המודל משנה את ה"הבנה" שלו בכל שלב. גבוה מדי עלול לזעזע את תהליך הלימוד.</small>

        <button id="start-training">▶️ התחל אימון ה-AI!</button>
         <div id="training-status" class="status-message">מודל ממתין להנחיות האימון...</div>
    </div>

    <div class="training-area panel">
        <h2>📊 התקדמות הלימוד במעבדה</h2>
        <div id="training-progress" class="log-output"></div>
        <div id="simulation-previews">
            <h3>רגעים בסטודיו (הדגמות תוך כדי אימון):</h3>
            <div id="preview-output" class="log-output preview-output">
                <div class="placeholder">אין עדיין הדגמות. התחל אימון כדי לראות את ה-AI לומד.</div>
            </div>
        </div>
    </div>

    <div class="generation-area panel">
        <h2>✨ יצירת האמנות (בגלריה)</h2>
         <div id="generation-controls">
            <label for="prompt">🖌️ בקש מה-AI ליצור (Prompt):</label>
            <input type="text" id="prompt" value="חתול קופץ דרך חלון אל סופת רעמים"><br>
            <small>מה הייתם רוצים שה-AI המאומן יצייר? היו יצירתיים!</small>
            <button id="generate-image" disabled>🎨 צור יצירת אמנות</button>
         </div>
        <div id="generated-image-output">
            <h3>היצירה המוגמרת:</h3>
            <div id="image-result" class="result-display">
                <div class="placeholder">התוצאה תופיע כאן לאחר אימון ויצירה.</div>
            </div>
        </div>
    </div>
</div>

<button id="toggle-explanation" class="explanation-button">הצג/הסתר את הסודות מאחורי הקלעים (הסבר תיאורטי)</button>

<div id="explanation" class="explanation-panel" style="display: none;">
    <h2>הסבר תיאורטי: הניצוץ הדיגיטלי - איך AI לומד ליצור אמנות?</h2>

    <h3>מהו מודל בינה מלאכותית גנרטיבי לאמנות?</h3>
    <p>דמיינו צייר דיגיטלי שלומד לצייר לא על ידי העתקה, אלא על ידי הבנת "המהות" של מיליוני תמונות. מודלים כמו DALL-E, Stable Diffusion או Midjourney אינם רק מנתחים תמונות, הם יוצרים יש מאין! הם מקבלים הנחיית טקסט (Prompt) והופכים אותה ליצירה ויזואלית חדשה וייחודית.</p>

    <h3>מודלים התפשטותיים (Diffusion Models): המסע מרעש ליצירה</h3>
    <p>המודלים החזקים ביותר כיום לעיתים קרובות מבוססים על רעיון שנקרא "התפשטות" (Diffusion). חשבו על זה כמו על פיסול. בשלב האימון, המודל רואה תמונות נקיות, ומוסיפים להן "רעש" באופן הדרגתי עד שהן הופכות לעיסה חסרת צורה (רעש אקראי). אחר כך, החלק המבריק: המודל לומד את התהליך ההפוך - איך להסיר את הרעש הזה, צעד אחר צעד, כדי לשחזר את התמונה המקורית. כשהוא עושה זאת מיליוני פעמים על מיליוני תמונות, הוא לומד לא רק לשחזר, אלא להבין איך אובייקטים, סגנונות וצבעים נראים כשהם "מגיחים" מתוך רעש. בשלב היצירה (Inference), במקום להתחיל מתמונה נקייה, המודל מתחיל מרעש טהור ומפעיל את תהליך ההסרה שלמד, מכוון על ידי ה-Prompt, וכך "מפסל" את התמונה המוגמרת מתוך ה"בלוק" האקראי.</p>

    <h3>חומר הגלם הקריטי: קבוצת נתוני האימון (Dataset) והכתוביות (Captions)</h3>
    <p>איכות היצירה תלויה בחומרי הגלם שהאמן הדיגיטלי קיבל. דאטה-סט ענק, מגוון ואיכותי (תמונות חדות, ברורות, ללא סימני מים או עיוותים) חיוני. מודל שאומן על חתולים בלבד לא יוכל ליצור פורטרטים ריאליסטיים, יהיה גאון בחתולים ככל שיהיה. לא פחות חשובות הן כתוביות הטקסט (Captions) שמלוות כל תמונה בדאטה-סט. התיאור המילולי מלמד את המודל לקשר בין מילים (כמו "חתול שמנמן אפור") לבין מה שנראה בתמונה. כתוביות מדויקות ומפורטות הן המפתח לכך שהמודל יגיב כהלכה ל-Prompts בשלב היצירה.</p>

    <h3>כוונון עדין של מנוע הלימוד: פרמטרים מרכזיים</h3>
    <ul>
        <li><strong>מספר שלבי אימון (Steps):</strong> כמה צעדים המודל לוקח במסע שלו מרעש ליצירה (במהלך האימון). ככל שיש יותר צעדים, הלמידה עמוקה יותר. אך יותר מדי עלול לגרום ל-Overfitting – המודל "שנן" את תמונות האימון במקום להבין עקרונות כלליים, וכתוצאה מכך יתקשה ליצור דברים חדשים או יכניס "זכרונות" מהאימון לתוצאות.</li>
        <li><strong>קצב למידה (Learning Rate):</strong> זהו ה"קצב" בו המודל מעדכן את ה"הבנה" שלו בכל צעד. קצב גבוה מדי יכול לגרום למודל "לקפוץ" מעל הפתרונות הטובים, לאבד יציבות, ולהתדרדר. קצב נמוך מדי יגרום לתהליך להיות איטי להחריד. מציאת הקצב הנכון היא אמנות בפני עצמה!</li>
    </ul>

    <h3>אתגרים בדרך לפיקסל המושלם</h3>
    <ul>
        <li><strong>Overfitting:</strong> המודל גאון בלשחזר תמונות שראה באימון, אבל כושל ביצירת דברים חדשים או מגיב רע ל-Prompts שונים במקצת.</li>
        <li><strong>Mode Collapse:</strong> למרות דאטה-סט מגוון, המודל מייצר רק וריאציות על נושא או סגנון מצומצם מאוד. הוא "קולס" לטווח יצירה צר.</li>
        <li><strong>הטיות בנתונים (Data Bias):</strong> אם הדאטה-סט מכיל הטיות (לדוגמה, רוב התמונות הן בסגנון מסוים, מתארות קבוצה מסוימת וכו'), המודל ישקף ויגביר הטיות אלו ביצירותיו.</li>
    </ul>

    <h3>מאימון ליצירה (Inference): היישום של הידע</h3>
    <p>לאחר שהמודל עבר את שלבי האימון ולמד את הקשר בין טקסט לתמונה ואת הדרך להפוך רעש ליצירה קוהרנטית, הוא מוכן לשלב ה"יצירה" או "הסקה" (Inference). בשלב זה, אנו נותנים לו Prompt טקסטואלי חדש, והוא משתמש בכל הידע שצבר באימון כדי לבצע את תהליך ה-Reverse Diffusion (הסרת הרעש) באופן שמביא ליצירה שתואמת בצורה הטובה ביותר את ה-Prompt שקיבל, בסגנון ש"למד" מהדאטה-סט.</p>
</div>

<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.7;
        max-width: 960px;
        margin: 20px auto;
        padding: 0 20px;
        direction: rtl;
        text-align: right;
        background-color: #f4f7f6; /* Light grey background */
        color: #333;
    }

    h1, h2, h3 {
        color: #004080; /* Darker blue */
        margin-bottom: 15px;
    }

    h1 {
        text-align: center;
        color: #002b5f;
        margin-bottom: 10px;
    }

    p {
        margin-bottom: 15px;
    }

    #app {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 30px; /* Increased gap */
        margin-top: 30px;
    }

    .panel {
        background-color: #ffffff; /* White panel background */
        border: 1px solid #e0e0e0;
        border-radius: 12px; /* More rounded corners */
        padding: 25px; /* Increased padding */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08); /* Subtle shadow */
        display: flex; /* Flex for internal layout */
        flex-direction: column;
    }

    .controls h2, .training-area h2, .generation-area h2 {
        margin-top: 0;
        color: #0056b3; /* Medium blue */
        border-bottom: 1px solid #eee; /* Separator line */
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

    label {
        display: block;
        margin-bottom: 8px; /* Increased spacing */
        font-weight: bold;
        color: #555;
    }

    input[type="number"], input[type="text"], select {
        width: calc(100% - 24px); /* Adjust for padding/border */
        padding: 12px; /* Increased padding */
        margin-bottom: 15px; /* Increased spacing */
        border: 1px solid #ccc;
        border-radius: 6px; /* Slightly more rounded */
        font-size: 1rem;
        box-sizing: border-box; /* Include padding and border in element's total width and height */
    }

    input[type="text"] {
        margin-bottom: 8px; /* Less space before button */
    }

    small {
        display: block;
        margin-top: -10px; /* Pull closer to input */
        margin-bottom: 15px;
        color: #777;
        font-size: 0.85rem;
    }


    button {
        padding: 12px 20px; /* Increased padding */
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 6px; /* Slightly more rounded */
        cursor: pointer;
        font-size: 1rem;
        transition: background-color 0.3s ease, transform 0.1s ease;
        margin-top: 10px; /* Space above buttons */
    }

    button:hover:not(:disabled) {
        background-color: #0056b3;
        transform: translateY(-1px); /* Subtle lift effect */
    }

     button:active:not(:disabled) {
         transform: translateY(0);
     }

    button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.7;
    }

    #start-training {
        background-color: #28a745; /* Green for start */
        margin-top: 20px; /* More space above start button */
        display: block; /* Make button take full width below inputs */
        width: 100%;
    }
     #start-training:hover:not(:disabled) {
        background-color: #218838;
    }

     #generate-image {
         background-color: #ffc107; /* Yellow/Orange for generate */
         color: #333;
          display: block; /* Make button take full width */
         width: 100%;
     }
     #generate-image:hover:not(:disabled) {
         background-color: #e0a800;
         color: white;
     }

    .status-message {
        margin-top: 15px;
        padding: 10px;
        border-radius: 6px;
        background-color: #e9ecef; /* Light grey */
        border: 1px solid #ced4da;
        font-size: 0.9rem;
        color: #495057;
         text-align: center;
    }

    .log-output {
        min-height: 100px;
        max-height: 250px; /* Limit height for scrolling */
        border: 1px dashed #a0a0a0; /* Dashed border */
        padding: 15px;
        margin-top: 15px;
        overflow-y: auto;
        font-size: 0.9rem;
        background-color: #f8f9fa; /* Very light grey */
        border-radius: 6px;
        white-space: pre-wrap; /* Preserve line breaks */
        word-wrap: break-word; /* Break long words */
        color: #444;
         flex-grow: 1; /* Allow it to take available space */
    }

    #simulation-previews h3, #generated-image-output h3 {
        margin-top: 20px;
        margin-bottom: 12px;
        color: #0056b3;
        font-size: 1.1rem;
        border-bottom: 1px dashed #eee;
        padding-bottom: 8px;
    }

     .preview-output {
         max-height: 200px; /* Specific height for previews */
     }

    .preview-item {
        border-bottom: 1px solid #eee;
        padding-bottom: 12px;
        margin-bottom: 12px;
        position: relative;
        background-color: #fff; /* White background for items */
        padding: 10px;
        border-radius: 4px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
     .preview-item:last-child {
         border-bottom: none;
         margin-bottom: 0;
         padding-bottom: 0;
     }
    .preview-item h4 {
        margin: 0 0 6px 0;
        font-size: 1rem;
        color: #007bff; /* Blue */
    }
    .preview-item p {
        margin: 0;
        font-size: 0.95rem;
        color: #333;
    }

    .result-display {
        min-height: 150px; /* Larger area for result */
        border: 2px solid #007bff; /* Accent border */
        padding: 20px;
        background-color: #e9f7ff; /* Very light blue background */
        border-radius: 8px;
        text-align: center; /* Center content initially */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        font-style: italic;
        color: #555;
        word-break: break-word;
         flex-grow: 1; /* Allow it to take available space */
    }

     .result-display .placeholder {
         font-style: italic;
         color: #777;
     }

    #image-result p {
        margin-top: 10px;
        margin-bottom: 0;
        font-style: normal;
        color: #333;
        font-size: 1.05rem;
        text-align: right; /* Align text result right */
        width: 100%; /* Ensure text takes full width */
    }
     #image-result p strong {
         color: #0056b3;
     }

    .explanation-button {
        display: block;
        margin: 40px auto 20px auto; /* Center button with more vertical space */
        background-color: #6c757d; /* Grey button */
         width: auto; /* Auto width based on content */
    }
    .explanation-button:hover:not(:disabled) {
         background-color: #5a6268;
         transform: translateY(-1px);
    }

    .explanation-panel {
        border: 1px solid #ccc;
        padding: 25px;
        margin-top: 20px;
        border-radius: 12px;
        background-color: #ffffff; /* White background */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }
    .explanation-panel h2 {
        color: #004080; /* Darker blue */
        margin-top: 0;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
    }
     .explanation-panel h3 {
        color: #0056b3; /* Medium blue */
        margin-top: 25px;
        margin-bottom: 10px;
         border-bottom: none; /* No border for sub-headings */
         padding-bottom: 0;
    }
     .explanation-panel ul {
         list-style-type: disc;
         margin-right: 20px;
         padding-right: 0;
     }
     .explanation-panel li {
         margin-bottom: 10px;
     }
    .explanation-panel p {
        text-align: justify; /* Justify text for readability */
    }


    @media (max-width: 768px) {
        #app {
            grid-template-columns: 1fr;
            gap: 20px;
        }
         .panel {
             padding: 20px;
         }
         input[type="number"], input[type="text"], select {
             width: calc(100% - 20px);
         }
         .log-output, .preview-output {
             max-height: 200px; /* Adjust height for smaller screens */
         }
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const datasetSelect = document.getElementById('dataset');
        const stepsInput = document.getElementById('steps');
        const learningRateSelect = document.getElementById('learning-rate');
        const startTrainingButton = document.getElementById('start-training');
        const trainingStatusDiv = document.getElementById('training-status');
        const trainingProgressDiv = document.getElementById('training-progress');
        const previewOutputDiv = document.getElementById('preview-output');
        const promptInput = document.getElementById('prompt');
        const generateImageButton = document.getElementById('generate-image');
        const imageResultDiv = document.getElementById('image-result');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        let isTraining = false;
        let currentStep = 0;
        let totalSteps = 0;
        let selectedDataset = '';
        let selectedLearningRate = '';
        let simulatedLoss = 1.0; // Simulate a loss value starting high


        // Mapping for simulated preview results based on dataset, steps, and prompt relevance
        // Descriptions made more vivid and reflect training stages
        const simulatedResults = {
            // Quality levels: 'noise', 'early_features', 'messy_forms', 'coherent', 'refined', 'overfit_mild', 'overfit_severe', 'mismatch'
            'cats': {
                'default': {
                    'noise': '🌊 רעש אקראי לגמרי. לא ניתן לזהות כלום.',
                    'early_features': '🎨 כתמי צבע מעורפלים, רמזים לצבעי פרווה וטקסטורות מעוגלות.',
                    'messy_forms': '🐱 צורות חתוליות מעוותות, חוסר אנטומיה, צבעים מוזרים לפעמים.',
                    'coherent': '✨ ציור ברור יחסית של חתול, עדיין מעט פשטני או רופף.',
                    'refined': '😺 ציור איכותי ומפורט של חתול, בסגנון הדומה לדאטה-סט.',
                    'overfit_mild': '😟 תוצאה טובה אך עם "זכרונות" מוזרים מתמונות ספציפיות באימון, או פגמים ויזואליים קלים.',
                    'overfit_severe': '💥 התוצאה התפרקה לרעש או עיוותים קיצוניים. המודל איבד יציבות!',
                    'mismatch': '❓ ערבוב של אלמנטים חתוליים וצורות לא מוגדרות, לא דומה לנושא המבוקש. המודל לא למד מספיק על הנושא הזה.'
                },
                 // Specific prompt match can lead to better 'refined' description
                 'חתול': {
                     'refined': '🐱✨ ציור איכותי ומפורט של חתול, תואם להנחיה. נראה שהמודל הבין את הנושא!',
                 },
                 'חלון': {
                      'refined': '🖼️😺 ציור איכותי הכולל חתול ואלמנט חלון, תואם להנחיה. המודל למד לקשר נושאים!',
                 },
                 // Mismatch prompt - quality caps lower, description reflects the clash
                 'נוף': {
                     'messy_forms': '🏞️🐱 צורות מופשטות עם טקסטורות חתוליות, לא מזכיר נוף. ניסיון ליצור משהו מחוץ לטווח האימון.',
                     'coherent': '🤔 ערבוב מוזר של חתולים וצורות לא מוגדרות. המודל מנסה, אך הדאטה-סט מגביל אותו בנושא זה.',
                     'refined': '❌ (ראה Mismatch) המודל לא יכול ליצור נוף איכותי מתוך דאטה-סט של חתולים.',
                     'mismatch': '🌵 התוצאה היא ערבוב לא קוהרנטי של חתולים ואלמנטים לא מזוהים. המודל מנסה, אך הדאטה-סט מונע ממנו להצליח בנושא זה.',
                 }
            },
            'stormy-nature': {
                 'default': {
                    'noise': '🌊 רעש אקראי לגמרי.',
                    'early_features': '🌫️ כתמי צבע כהים, רמזים לאווירה סוערת וטקסטורות מחוספסות.',
                    'messy_forms': '⛰️ צורות מעוותות של הרים או עצים, שמיים דרמטיים מטושטשים.',
                    'coherent': '🌩️ נוף סוער מוגדר יחסית, עדיין מעט מטושטש או לא מפורט.',
                    'refined': '⚡ נוף סוער, דרמטי ומפורט היטב, בסגנון הדאטה-סט.',
                    'overfit_mild': '😟 תוצאה טובה אך עם "זכרונות" מוזרים מתמונות ספציפיות, או פגמים קלים בעננים/מים.',
                    'overfit_severe': '💥 התוצאה התפרקה לרעש או עיוותים קיצוניים!',
                     'mismatch': '❓ ערבוב של אלמנטים טבעיים וצורות לא מוגדרות. לא דומה לנושא המבוקש.'
                 },
                 'נוף': {
                    'refined': '⛰️⚡ נוף סוער, דרמטי ומפורט. המודל הבין את הבקשה!',
                 },
                  'ים': {
                    'refined': '🌊🌩️ ים סוער, גלים ורעמים מצוירים בצורה דרמטית ומפורטת. הצלחה!',
                 },
                 'פורטרט': { // Mismatch
                     'messy_forms': '👩‍🎨🌫️ צורות מופשטות עם טקסטורות סוערות, לא מזכיר פנים. ניסיון ליצור מחוץ לטווח האימון.',
                     'coherent': '🤔 ערבוב של אלמנטים טבעיים וכתמי צבע, לא דומה לפורטרט. המודל מנסה, אך הדאטה-סט מגביל אותו בנושא זה.',
                     'refined': '❌ (ראה Mismatch) המודל לא יכול ליצור פורטרט איכותי מתוך דאטה-סט של טבע סוער.',
                     'mismatch': '🌿 התוצאה היא ערבוב לא קוהרנטי של אלמנטים טבעיים וצורות חסרות פשר. המודל מנסה, אך הדאטה-סט מונע ממנו להצליח בנושא זה.',
                 }
            },
            'realistic-portraits': {
                 'default': {
                    'noise': '🌊 רעש אקראי לגמרי.',
                    'early_features': '🖌️ כתמי עור ושיער מעורפלים, רמזים לצבעי עור.',
                    'messy_forms': '👤 פנים אנושיות מעוותות, חוסר פרופורציה, לפעמים "תוספות" מוזרות (יותר מדי אצבעות, עין שלישית וכו').',
                    'coherent': '✨ פורטרט אנושי מוגדר יחסית, עדיין מעט מטושטש או לא ריאליסטי לחלוטין.',
                    'refined': '🧑‍🎨 פורטרט אנושי ריאליסטי, מפורט ובעל הבעה, בסגנון הדאטה-סט.',
                    'overfit_mild': '😟 תוצאה טובה אך עם "זכרונות" מוזרים (סימני מים, אלמנטים חוזרים מתמונות אימון), או פגמים קלים בפנים.',
                    'overfit_severe': '💥 התוצאה התפרקה לרעש או עיוותים קיצוניים בפנים!',
                     'mismatch': '❓ ערבוב של תווי פנים אנושיים וטקסטורות לא ברורות. לא דומה לנושא המבוקש.'
                 },
                 'פורטרט': {
                    'refined': '🧑‍🎨✨ פורטרט אנושי ריאליסטי ומפורט. הצלחה מרשימה!',
                 },
                  'איש': {
                    'refined': '👨‍🎨 פורטרט ריאליסטי של גבר, מפורט ותואם להנחיה.',
                 },
                 'אישה': {
                    'refined': '👩‍🎨 פורטרט ריאליסטי של אישה, מפורט ותואם להנחיה.',
                 },
                 'חתול': { // Mismatch
                     'messy_forms': '🐱👤 צורות מופשטות עם רמזים לעור אנושי, לא מזכיר חתול. ניסיון ליצור מחוץ לטווח האימון.',
                     'coherent': '🤔 ערבוב של תווי פנים אנושיים וטקסטורות לא ברורות, לא דומה לחתול. המודל מנסה, אך הדאטה-סט מגביל אותו בנושא זה.',
                     'refined': '❌ (ראה Mismatch) המודל לא יכול ליצור חתול ריאליסטי מתוך דאטה-סט של פורטרטים.',
                     'mismatch': '🐈 התוצאה היא ערבוב לא קוהרנטי של תווי פנים וטקסטורות פרווה. המודל מנסה, אך הדאטה-סט מונע ממנו להצליח בנושא זה.',
                 }
            }
        };

         // Simple keyword matching for prompts to decide which simulated result key to use
         function getRelevantPromptKey(dataset, prompt) {
             prompt = prompt.toLowerCase();
             if (dataset === 'cats') {
                 if (prompt.includes('חתול') || prompt.includes('אדן החלון') || prompt.includes('חלון') || prompt.includes('פרווה') || prompt.includes('זנב')) return 'חתול';
                 if (prompt.includes('נוף') || prompt.includes('ים') || prompt.includes('פורטרט') || prompt.includes('איש') || prompt.includes('אישה') || prompt.includes('פנים')) return 'נוף'; // Mismatch key
             } else if (dataset === 'stormy-nature') {
                 if (prompt.includes('נוף') || prompt.includes('ים') || prompt.includes('הר') || prompt.includes('שמיים') || prompt.includes('עננים') || prompt.includes('סערה') || prompt.includes('גלים')) return 'נוף';
                  if (prompt.includes('פורטרט') || prompt.includes('איש') || prompt.includes('אישה') || prompt.includes('פנים') || prompt.includes('חתול')) return 'פורטרט'; // Mismatch key
             } else if (dataset === 'realistic-portraits') {
                 if (prompt.includes('פורטרט') || prompt.includes('איש') || prompt.includes('אישה') || prompt.includes('פנים') || prompt.includes('שיער') || prompt.includes('עיניים')) return 'פורטרט';
                 if (prompt.includes('חתול') || prompt.includes('נוף') || prompt.includes('ים') || prompt.includes('הר') || prompt.includes('עננים') || prompt.includes('סערה')) return 'חתול'; // Mismatch key
             }
             return 'default'; // Fallback to default if no specific keywords match dataset or indicate mismatch
         }


         function getSimulatedResultDescription(dataset, stepsDone, totalSteps, learningRate, prompt) {
            const stepPercentage = stepsDone / totalSteps;
            let qualityLevel = 'noise';

            // Determine base quality level based on steps completed
            if (stepsDone === 0) {
                qualityLevel = 'noise';
            } else if (stepPercentage < 0.05) { // Very early
                qualityLevel = 'early_features';
            } else if (stepPercentage < 0.3) { // Early/Mid
                qualityLevel = 'messy_forms';
            } else if (stepPercentage < 0.7) { // Mid/Late
                qualityLevel = 'coherent';
            } else { // Late/Converged
                qualityLevel = 'refined';
            }

            // Simulate instability/overfitting based on Learning Rate and steps
            if (learningRate === '0.0005') { // Aggressive LR
                 if (stepPercentage > 0.5 && stepPercentage <= 0.9) { // Risk of mild overfit later
                     if (Math.random() < 0.3) qualityLevel = 'overfit_mild'; // 30% chance
                 } else if (stepPercentage > 0.9) { // Higher risk of severe overfit very late
                      if (Math.random() < 0.6) qualityLevel = 'overfit_severe'; // 60% chance
                 }
            } else if (learningRate === '0.0001') { // Balanced LR
                 if (stepPercentage > 0.9 && stepsDone > 300) { // Slight risk very late with many steps
                     if (Math.random() < 0.2) qualityLevel = 'overfit_mild'; // 20% chance
                 }
            }
            // Low LR (0.00005) is assumed stable, less likely to overfit severely in simulated steps range

             // If steps are too low, cap quality regardless of percentage
            if (totalSteps < 100 && stepPercentage >= 0.7) {
                 qualityLevel = 'coherent'; // Cannot reach refined with very few steps
            }
            if (totalSteps < 200 && stepPercentage >= 0.8) {
                 if (qualityLevel === 'refined') qualityLevel = 'coherent'; // Harder to reach refined with moderate steps
            }


            const relevantPromptKey = getRelevantPromptKey(dataset, prompt);
            const datasetResults = simulatedResults[dataset];
            const isMismatchKey = (relevantPromptKey === 'נוף' && dataset === 'cats') ||
                                  (relevantPromptKey === 'פורטרט' && dataset === 'stormy-nature') ||
                                  (relevantPromptKey === 'חתול' && dataset === 'realistic-portraits');


             // If it's a mismatch prompt, force the quality to 'mismatch' at reasonable steps
             if (isMismatchKey && stepPercentage > 0.1) { // Once training has progressed a bit
                 qualityLevel = 'mismatch';
             }


            // Get the description based on the determined quality level and prompt key, fallback to default if needed
            let resultDescription = datasetResults[relevantPromptKey]?.[qualityLevel] || datasetResults['default'][qualityLevel] || datasetResults['default']['noise']; // Final fallback


            return resultDescription;
        }

        function updateProgressDisplay(message, loss = null) {
            const p = document.createElement('p');
            p.classList.add('log-item');
            let stepInfo = `[שלב ${currentStep}/${totalSteps}]`;
            let lossInfo = loss !== null ? ` | Loss: ${loss.toFixed(4)}` : '';
            p.innerHTML = `<strong>${stepInfo}</strong>${lossInfo} ${message}`;
            trainingProgressDiv.appendChild(p);
            trainingProgressDiv.scrollTop = trainingProgressDiv.scrollHeight; // Auto-scroll
        }

        function showSimulationPreview() {
             if (currentStep > 0) {
                const currentPrompt = promptInput.value || "תמונה לדוגמה";
                 const description = getSimulatedResultDescription(selectedDataset, currentStep, totalSteps, selectedLearningRate, currentPrompt);

                const previewDiv = document.createElement('div');
                previewDiv.classList.add('preview-item');
                previewDiv.innerHTML = `
                    <h4>📸 שלב ${currentStep}: נסייר ליצירת "${currentPrompt}"</h4>
                    <p>${description}</p>
                `;
                 // Prepend the new preview so latest is at the top
                 if (previewOutputDiv.querySelector('.placeholder')) {
                     previewOutputDiv.innerHTML = ''; // Clear placeholder
                 }
                 previewOutputDiv.prepend(previewDiv);
                 // previewOutputDiv.scrollTop = previewOutputDiv.scrollHeight; // Auto-scroll to bottom (less useful with prepend)
             }
        }

        async function startTraining() {
            if (isTraining) return;

            isTraining = true;
            currentStep = 0;
            totalSteps = parseInt(stepsInput.value, 10);
            selectedDataset = datasetSelect.value;
            selectedLearningRate = learningRateSelect.value;
            simulatedLoss = 1.0; // Reset simulated loss

            trainingProgressDiv.innerHTML = ''; // Clear previous progress
             previewOutputDiv.innerHTML = '<div class="placeholder">אין עדיין הדגמות. התחל אימון כדי לראות את ה-AI לומד.</div>'; // Reset previews with placeholder
             imageResultDiv.innerHTML = '<div class="placeholder">התוצאה תופיע כאן לאחר אימון ויצירה.</div>'; // Reset result with placeholder


            startTrainingButton.disabled = true;
            generateImageButton.disabled = true; // Disable generation during training
             document.querySelectorAll('.controls select, .controls input').forEach(el => el.disabled = true);
            trainingStatusDiv.textContent = '⏳ מתחיל אימון מודל...';
             trainingStatusDiv.style.backgroundColor = '#ffc107'; // Yellow status
             trainingStatusDiv.style.color = '#333';


            updateProgressDisplay('🔬 מכין את הנתונים ומאתחל את המודל...');

            const previewInterval = Math.max(50, Math.floor(totalSteps / 8)); // Dynamic interval, min 50, roughly 8-10 previews
             const logInterval = Math.max(10, Math.floor(totalSteps/20)); // Log roughly every 5-10%

            for (let i = 1; i <= totalSteps; i++) {
                currentStep = i;

                // Simulate loss decrease, potentially increase with high LR later
                let lossDecrease = 0.005 - parseFloat(selectedLearningRate) * 5; // Faster decrease with higher LR
                 lossDecrease += (1 - (i / totalSteps)) * 0.001; // Larger decrease early on
                simulatedLoss = Math.max(0.05, simulatedLoss - lossDecrease + (Math.random() - 0.5) * 0.01); // Add some noise, keep minimum

                if (selectedLearningRate === '0.0005' && i / totalSteps > 0.7) { // High LR can increase loss late
                     simulatedLoss += (Math.random() * 0.05); // Random spikes
                     simulatedLoss = Math.max(0.1, simulatedLoss); // Ensure it doesn't go too low if unstable
                }


                // Simulate training step
                await new Promise(resolve => setTimeout(resolve, 5)); // Shorter delay for faster simulation

                // Simulate logging progress
                if (i % logInterval === 0 || i === 1 || i === totalSteps) {
                     updateProgressDisplay(`🛠️ מעבד שלב אימון ${i}...`, simulatedLoss);
                }

                // Simulate showing a preview generation
                if (i % previewInterval === 0 || i === totalSteps) { // Also show preview on last step
                     showSimulationPreview();
                }
            }

            isTraining = false;
            startTrainingButton.disabled = false;
            generateImageButton.disabled = false;
             document.querySelectorAll('.controls select, .controls input').forEach(el => el.disabled = false);

             trainingStatusDiv.textContent = '✅ אימון הושלם בהצלחה! המודל מוכן ליצור.';
             trainingStatusDiv.style.backgroundColor = '#d4edda'; // Green status
             trainingStatusDiv.style.color = '#155724';

            updateProgressDisplay('🎉 אימון המודל הושלם!');
             imageResultDiv.innerHTML = '<div class="placeholder">המודל אומן. הכנס Prompt ולחץ \'צור יצירת אמנות\'.</div>'; // Restore structure and placeholder
        }

        function generateImage() {
            if (isTraining || currentStep === 0) {
                 document.getElementById('image-result').innerHTML = '<p class="placeholder">המודל עדיין לא אומן או שהאימון לא הושלם.</p>';
                return;
            }

            const prompt = promptInput.value;
            if (!prompt.trim()) {
                 document.getElementById('image-result').innerHTML = '<p class="placeholder">אנא הכנס טקסט ליצירת תמונה (Prompt).</p>';
                return;
            }

             document.getElementById('image-result').innerHTML = '<p class="placeholder">✨ יוצר תמונה על בסיס המודל המאומן וה-Prompt...</p>';
             generateImageButton.disabled = true; // Disable during generation


            // Simulate generation time
             setTimeout(() => {
                // Simulate result based on final state of training and prompt relevance
                 const description = getSimulatedResultDescription(selectedDataset, currentStep, totalSteps, selectedLearningRate, prompt);
                 document.getElementById('image-result').innerHTML = `<p><strong>Prompt:</strong> "${prompt}"</p><p>${description}</p>`;
                 generateImageButton.disabled = false; // Re-enable button
            }, 2000); // Simulate 2 second generation time
        }

        function toggleExplanation() {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר את הסודות מאחורי הקלעים (הסבר תיאורטי)' : 'הצג את הסודות מאחורי הקלעים (הסבר תיאורטי)';
        }


        // Event Listeners
        startTrainingButton.addEventListener('click', startTraining);
        generateImageButton.addEventListener('click', generateImage);
        toggleExplanationButton.addEventListener('click', toggleExplanation);

        // Initial state setup
        trainingProgressDiv.innerHTML = '<p class="placeholder">התקדמות האימון תופיע כאן...</p>';
        previewOutputDiv.innerHTML = '<div class="placeholder">אין עדיין הדגמות. התחל אימון כדי לראות את ה-AI לומד.</div>';
        imageResultDiv.innerHTML = '<div class="placeholder">התוצאה תופיע כאן לאחר אימון ויצירה.</div>';
        trainingStatusDiv.textContent = 'מודל ממתין להנחיות האימון...';
        trainingStatusDiv.style.backgroundColor = '#e9ecef';
        trainingStatusDiv.style.color = '#495057';

        generateImageButton.disabled = true;

        // Set default prompt based on default dataset
         promptInput.value = "חתול יושב על אדן החלון"; // Initial prompt for cats
        datasetSelect.addEventListener('change', () => {
            if (datasetSelect.value === 'cats') {
                promptInput.value = "חתול יושב על אדן החלון";
            } else if (datasetSelect.value === 'stormy-nature') {
                 promptInput.value = "נוף הרים סוער עם ברקים";
            } else if (datasetSelect.value === 'realistic-portraits') {
                 promptInput.value = "פורטרט ריאליסטי של אישה מבוגרת";
            }
        });
    });
</script>
```