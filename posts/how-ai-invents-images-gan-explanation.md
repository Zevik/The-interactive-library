---
title: "איך בינה מלאכותית 'ממציאה' תמונות? מסע אל עולם GANs"
english_slug: how-ai-invents-images-gan-explanation
category: "טכנולוגיה / מדעי המחשב"
tags: [בינה מלאכותית, למידת מכונה, רשתות נוירונים, יצירת תמונות, GAN, למידה עמוקה]
---
# איך בינה מלאכותית 'ממציאה' תמונות? מסע אל עולם GANs

דמיינו עולם שבו מחשבים לא רק מעבדים מידע, אלא גם *יוצרים* אותו מאפס – תמונות פנים ריאליסטיות של אנשים שמעולם לא התקיימו, ציורי נוף סוריאליסטיים, או אפילו מוזיקה חדשה. נשמע כמו מדע בדיוני? זו המציאות של רשתות GAN (Generative Adversarial Networks), אחת ההתפתחויות המסעירות והיצירתיות ביותר בעולם הבינה המלאכותית.

איך זה עובד? בואו נצלול לסימולציה אינטראקטיבית שממחישה את ה"משחק" שמתרחש בלב מודל GAN.

<div class="gan-simulator">
    <h2>המשחק: היצרן נגד המבחין</h2>
    <div class="simulator-area">
        <div class="real-images-section">
            <h3>ה'אמת': תמונות מקוריות</h3>
            <div class="real-images-grid">
                <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='60' viewBox='0 0 60 60'%3E%3Ccircle cx='30' cy='30' r='25' fill='%23FF6F61'/%3E%3C/svg%3E" alt="Real Target 1">
                <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='60' viewBox='0 0 60 60'%3E%3Crect x='10' y='10' width='40' height='40' fill='%235CACE0'/%3E%3C/svg%3E" alt="Real Target 2">
                <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='60' viewBox='0 0 60 60'%3E%3Cpath d='M30 5 L55 55 L5 55 Z' fill='%23FFD166'/%3E%3C/svg%3E" alt="Real Target 3">
            </div>
            <p class="section-label">מה שהיצרן שואף לחקות</p>
        </div>

        <div class="gan-process">
            <div class="generator-section">
                <h3>היצרן (Generator) <span>הזייפן</span></h3>
                 <div class="process-flow">
                    <div class="input-noise"><i class="fas fa-random"></i> רעש התחלתי</div>
                     <div class="arrow">→</div>
                    <div class="generator-output">
                         <img id="generated-image" src="" alt="Generated Image">
                         <div class="realism-score">
                             <span class="score-label">כמה ריאליסטי?</span>
                             <div class="score-bar-container"><div id="realism-bar" class="score-bar"></div></div>
                             <span id="realism-percentage">0%</span>
                         </div>
                     </div>
                 </div>
                 <p class="section-label">מנסה ליצור זיוף מושלם</p>
            </div>

            <div class="arrow arrow-down">↓</div>

            <div class="discriminator-section">
                <h3>המבחין (Discriminator) <span>הבלש</span></h3>
                 <div class="process-flow">
                     <div class="discriminator-input"><img id="discriminator-input-image" src="" alt="Discriminator Input"></div>
                      <div class="arrow">→</div>
                     <div class="discriminator-output">
                         <div id="discriminator-judgment" class="judgment">...בדיקה...</div>
                         <div class="confidence-score">
                             <span class="score-label">ביטחון המבחין</span>
                             <div class="score-bar-container"><div id="confidence-bar" class="score-bar"></div></div>
                             <span id="confidence-percentage">0%</span>
                         </div>
                     </div>
                 </div>
                 <p class="section-label">מנסה לזהות אם התמונה מזויפת או אמיתית</p>
            </div>
        </div>
    </div>

    <div class="controls">
        <div id="iteration-counter">אימון: 0</div>
        <button id="next-iteration-button">
             צא לסיבוב אימון! <i class="fas fa-play"></i>
        </button>
         <button id="reset-button" class="secondary-button">
             אתחל סימולציה <i class="fas fa-sync-alt"></i>
        </button>
    </div>

     <div class="feedback-area" id="feedback-area">
         <!-- Feedback messages will appear here -->
     </div>
</div>

<button id="toggle-explanation" class="toggle-button">
     הצגת הסבר מעמיק על GANs <i class="fas fa-chevron-down"></i>
</button>

<div id="full-explanation" style="display: none;">
    <h2>הסבר מעמיק: רשתות יריבות יוצרות (GANs)</h2>

    <h3>מהי רשת GAN (Generative Adversarial Network)?</h3>
    <p>GANs, או רשתות יריבות יוצרות, הן סוג מהפכני של מודל בינה מלאכותית המסוגל **לייצר נתונים חדשים לגמרי** שנראים כאילו נלקחו מתוך מאגר אימון קיים. חשבו על זה: במקום רק לנתח תמונות, הן יכולות *להמציא* אותן! לאחר אימון על אלפי תמונות של פרחים, GAN יכול ליצור תמונות של פרחים חדשים, ייחודיים לחלוטין, אך ריאליסטיים. ליבת הרעיון היא **תחרות** בלתי פוסקת בין שני "שחקנים" עיקריים.</p>

    <h3>השחקנים הראשיים: היוצר (Generator) והמבחין (Discriminator)</h3>
    <p>מודל GAN מורכב משתי רשתות נוירונים עצמאיות שפועלות זו נגד זו, כמו במשחק חתול ועכבר:</p>
    <ul>
        <li><strong>הרשת היוצרת (Generator - G):</strong> זהו ה"אמן" או ה"זייפן". תפקידה הוא לקבל קלט אקראי (מכונה לרוב "רעש" או "וקטור לטנטי") **ולייצר ממנו נתון שנראה אמיתי**. בהתחלה, התוצר יהיה חסר צורה ומשמעות. מטרת היצרן: לשפר את היצירות שלו כך שהן יצליחו "לעבור" את המבחין.</li>
        <li><strong>הרשת המבחינה (Discriminator - D):</strong> זהו ה"בלש" או ה"מבקר". תפקידה הוא לקבל נתון כלשהו (או תמונה, בדוגמה שלנו) **ולהחליט אם הוא מקורי ("אמיתי") או נוצר על ידי היצרן ("מזויף")**. מטרת המבחין: להיות טוב יותר בזיהוי זיופים.</li>
    </ul>

    <h3>העיקרון של התחרות והלמידה המשותפת</h3>
    <p>הקסם של GAN טמון באופן האימון. שתי הרשתות מאומנות יחדיו, במין "משחק סכום אפס": כשהיצרן משתפר בזיוף, המבחין נהיה טוב יותר בזיהוי, מה שדוחף את היצרן לזייף טוב יותר, וחוזר חלילה. התהליך נמשך עד שהיצרן מסוגל לייצר נתונים כה ריאליסטיים, שהמבחין כבר לא מצליח להבדיל ביניהם לבין המקור, אלא אם מנחש.</p>

    <h3>איך נראה סיבוב אימון יחיד?</h3>
    <p>בכל איטרציה (סיבוב) של האימון, מתבצעים בדרך כלל שני שלבים:</p>
    <ol>
        <li><strong>אימון המבחין (D):</strong>
            <ul>
                <li>מציגים למבחין **דוגמאות אמיתיות** ממאגר האימון (ומסמנים אותן כ"אמיתיות").</li>
                <li>מציגים למבחין **דוגמאות מזויפות** שנוצרו כרגע על ידי היצרן (ומסמנים אותן כ"מזויפות").</li>
                <li>ה-Discriminator לומד לשפר את היכולת שלו לסווג נכון את הדוגמאות הללו (להגיד "אמיתי" לאמיתי ו"מזויף" למזויף).</li>
            </ul>
        </li>
        <li><strong>אימון היצרן (G):</strong>
            <ul>
                <li>היצרן יוצר דוגמאות מזויפות חדשות.</li>
                <li>מציגים את הדוגמאות המזויפות האלה למבחין, **אבל הפעם לא נותנים למבחין ללמוד או לשנות את עצמו**.</li>
                <li>היצרן מקבל "פידבק" מהמבחין: עד כמה ה"בלש" השתכנע שהזיוף אמיתי.</li>
                <li>ה-Generator לומד לשנות את עצמו כך שבפעם הבאה ה"בלש" **יטעה ויחשוב שהזיוף הוא אמיתי**. המטרה שלו היא "להכניע" את המבחין.</li>
            </ul>
        </li>
    </ol>
    <p>האימון ממשיך, כשהיצרן משתפר בזיוף והמבחין משתפר בזיהוי, עד שהיצרן מגיע לרמה שבה הוא יכול ליצור נתונים שמבלבלים את המבחין באופן עקבי.</p>

    <h3>איפה פוגשים GANs ביומיום?</h3>
    <p>GANs הן הבסיס ליצירות דיגיטליות מדהימות:</p>
    <ul>
        <li>**יצירת תמונות פנים ריאליסטיות:** האתר ThisPersonDoesNotExist.com שמראה פנים של אנשים שאינם קיימים.</li>
        <li>**שינוי סגנון תמונות:** להפוך תמונה לתמונה שנראית כאילו צייר אותה צייר מפורסם.</li>
        <li>**שיפור רזולוציה:** להפוך תמונה מטושטשת וקטנה לחדה וגדולה.</li>
        <li>**השלמת תמונות:** למלא חלקים חסרים בתמונה באופן שנראה טבעי.</li>
        <li>**יצירת תוכן:** מעבר לתמונות, GANs יכולות ליצור וידאו, אודיו ונתונים מורכבים נוספים.</li>
    </ul>

    <h3>אתגרים בדרך לזיוף המושלם</h3>
    <p>למרות הכוח הרב, אימון GANs אינו פשוט:</p>
    <ul>
        <li>**יציבות אימון:** קשה לגרום לשני המודלים להתאמן יחד בצורה יציבה מבלי שאחד ישתלט על השני מוקדם מדי.</li>
        <li>**כישלון מצבים (Mode Collapse):** לעיתים, היצרן מוצא דרך "קלה" לרמות את המבחין ומתמקד רק ביצירת סוג מצומצם מאוד של נתונים, במקום את כל המגוון האפשרי.</li>
        <li>**הערכה:** קשה למדוד באופן אובייקטיבי כמה הנתונים שנוצרו "טובים" או "ריאליסטיים" באמת.</li>
    </ul>
</div>

<script>
    const generatedImage = document.getElementById('generated-image');
    const discriminatorInputImage = document.getElementById('discriminator-input-image'); // New element for visual flow
    const discriminatorJudgment = document.getElementById('discriminator-judgment');
    const realismBar = document.getElementById('realism-bar');
    const realismPercentage = document.getElementById('realism-percentage');
    const confidenceBar = document.getElementById('confidence-bar');
    const confidencePercentage = document.getElementById('confidence-percentage');
    const nextButton = document.getElementById('next-iteration-button');
    const resetButton = document.getElementById('reset-button');
    const iterationCounter = document.getElementById('iteration-counter');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const fullExplanation = document.getElementById('full-explanation');
    const feedbackArea = document.getElementById('feedback-area');

    let iteration = 0;
    const maxIterations = 15; // Cap iterations for simulation clarity

    // Simulate improvement stages of the generated image (more complex SVGs)
    const generatedImages = [
        "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%23f0f0f0'/%3E%3Ccircle cx='20' cy='20' r='5' fill='%23ccc'/%3E%3Ccircle cx='80' cy='80' r='5' fill='%23ccc'/%3E%3Ccircle cx='20' cy='80' r='5' fill='%23ccc'/%3E%3Ccircle cx='80' cy='20' r='5' fill='%23ccc'/%3E%3Ctext x='50' y='50' font-family='Arial' font-size='14' fill='%23757575' text-anchor='middle' alignment-baseline='middle'%3Eרעש%3C/text%3E%3C/svg%3E", // Iteration 0: Noise
        "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%23e0e0e0'/%3E%3Ccircle cx='30' cy='30' r='10' fill='%23bdbdbd'/%3E%3Crect x='55' y='55' width='20' height='20' fill='%23bdbdbd'/%3E%3Ctext x='50' y='50' font-family='Arial' font-size='14' fill='%23616161' text-anchor='middle' alignment-baseline='middle'%3Eצורה מטושטשת%3C/text%3E%3C/svg%3E", // Iteration 1: Blurry shape attempt
        "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%23d0d0d0'/%3E%3Ccircle cx='35' cy='35' r='15' fill='%239e9e9e'/%3E%3Crect x='50' y='50' width='30' height='30' fill='%239e9e9e'/%3E%3Cpath d='M20 80 L50 20 L80 80 Z' fill='%239e9e9e' opacity='0.5'/%3E%3Ctext x='50' y='50' font-family='Arial' font-size='14' fill='%23424242' text-anchor='middle' alignment-baseline='middle'%3Eקצת יותר ברור%3C/text%3E%3C/svg%3E", // Iteration 2: Basic shapes emerging
        "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%23c0c0c0'/%3E%3Ccircle cx='30' cy='30' r='20' fill='%23ef9a9a'/%3E%3Crect x='45' y='45' width='40' height='40' fill='%2390caf9'/%3E%3Cpath d='M25 75 L50 25 L75 75 Z' fill='%23ffe082'/%3E%3Ctext x='50' y='50' font-family='Arial' font-size='14' fill='%23212121' text-anchor='middle' alignment-baseline='middle'%3Eניסיון לחקות%3C/text%3E%3C/svg%3E", // Iteration 3: Attempting specific colors/shapes
        "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%23b0b0b0'/%3E%3Ccircle cx='30' cy='30' r='22' fill='%23ef5350'/%3E%3Crect x='40' y='40' width='50' height='50' fill='%2342a5f5'/%3E%3Cpath d='M20 80 L50 20 L80 80 Z' fill='%23ffca28'/%3E%3Ctext x='50' y='50' font-family='Arial' font-size='14' fill='%23000' text-anchor='middle' alignment-baseline='middle'%3Eמתחיל להצליח%3C/text%3E%3C/svg%3E", // Iteration 4: Closer match
         "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%23a0a0a0'/%3E%3Ccircle cx='30' cy='30' r='25' fill='%23e53935'/%3E%3Crect x='35' y='35' width='55' height='55' fill='%232196f3'/%3E%3Cpath d='M15 85 L50 15 L85 85 Z' fill='%23ffb300'/%3E%3Ctext x='50' y='50' font-family='Arial' font-size='14' fill='%23000' text-anchor='middle' alignment-baseline='middle'%3Eכמעט שם...%3C/text%3E%3C%2Fsvg%3E", // Iteration 5
         "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%23909090'/%3E%3Ccircle cx='30' cy='30' r='25' fill='%23ef5350'/%3E%3Crect x='40' y='40' width='50' height='50' fill='%2342a5f5'/%3E%3Cpath d='M20 80 L50 20 L80 80 Z' fill='%23ffca28'/%3E%3Ctext x='50' y='50' font-family='Arial' font-size='14' fill='%23000' text-anchor='middle' alignment-baseline='middle'%3Eנראה די אמיתי%3C/text%3E%3C/svg%3E", // Iteration 6
         "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%23808080'/%3E%3Ccircle cx='30' cy='30' r='25' fill='%23f44336'/%3E%3Crect x='40' y='40' width='50' height='50' fill='%232196F3'/%3E%3Cpath d='M20 80 L50 20 L80 80 Z' fill='%23FFC107'/%3E%3Ctext x='50' y='50' font-family='Arial' font-size='14' fill='%23000' text-anchor='middle' alignment-baseline='middle'%3Eקשה לבלש!%3C/text%3E%3C/svg%3E", // Iteration 7
        "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%23707070'/%3E%3Ccircle cx='30' cy='30' r='25' fill='%23ef5350'/%3E%3Crect x='40' y='40' width='50' height='50' fill='%2342a5f5'/%3E%3Cpath d='M20 80 L50 20 L80 80 Z' fill='%23ffca28'/%3E%3Ctext x='50' y='50' font-family='Arial' font-size='14' fill='%23000' text-anchor='middle' alignment-baseline='middle'%3Eכמעט מושלם!%3C/text%3E%3C/svg%3E", // Iteration 8+
    ];


    // Simulate Discriminator's performance over iterations
    // [realism_score, discriminator_confidence, judgment_text_template, feedback_message_template, judgment_class]
    const simulationSteps = [
        [0, 95, "זיהה: מזויף!", "הבלש בטוח שזה זיוף. היצרן צריך להשתפר!", "judgment-fake"], // Iteration 0
        [10, 90, "זיהה: מזויף!", "הבלש מזהה בקלות. היצרן משנה אסטרטגיה.", "judgment-fake"],    // Iteration 1
        [30, 80, "זיהה: מזויף.", "הבלש עדיין מזהה, אבל בפחות ביטחון.", "judgment-fake"],          // Iteration 2
        [50, 65, "חושד שזה מזויף.", "הזיוף כבר לא גרוע. הבלש מתחיל להתלבט.", "judgment-suspect"],       // Iteration 3
        [65, 50, "לא בטוח...", "הבלש מתקשה להחליט. הזיוף מתקרב לאמת!", "judgment-unsure"],            // Iteration 4
        [80, 35, "יכול להיות אמיתי!", "הזיוף כמעט מושלם! הבלש טועה לראשונה (מבחינת היצרן זה ניצחון!)", "judgment-real-guess"], // Iteration 5 (Generator fools Discriminator)
        [90, 60, "קשה להבדיל...", "הבלש לומד מהטעויות שלו, ונהיה טוב יותר.", "judgment-suspect"],   // Iteration 6 (Discriminator catches up)
        [95, 75, "זיהה: מזויף!", "הבלש משפר את הזיהוי, היצרן חייב להיות יצירתי יותר.", "judgment-fake"], // Iteration 7
        [97, 55, "לא סגור על זה...", "היצרן שוב מבלבל את הבלש. התחרות נמשכת!", "judgment-unsure"], // Iteration 8+
    ];

    function updateSimulation(currentIteration) {
        const stepIndex = Math.min(currentIteration, simulationSteps.length - 1);
        const [realism, confidence, judgmentTextTemplate, feedbackTextTemplate, judgmentClass] = simulationSteps[stepIndex];

        // Animate Generator
        generatedImage.style.opacity = 0; // Start fade out
        setTimeout(() => {
            generatedImage.src = generatedImages[Math.min(currentIteration, generatedImages.length - 1)];
            generatedImage.style.opacity = 1; // Fade in new image
            // Animate image moving to discriminator input
            discriminatorInputImage.src = generatedImage.src;
            discriminatorInputImage.classList.add('fade-in');
             setTimeout(() => {
                 discriminatorInputImage.classList.remove('fade-in');
             }, 500);

             // Animate Discriminator judgment
             discriminatorJudgment.textContent = "...בדיקה...";
             discriminatorJudgment.className = 'judgment'; // Reset class
             confidenceBar.style.width = `0%`; // Reset bar
             confidencePercentage.textContent = `0%`;

            setTimeout(() => {
                 discriminatorJudgment.textContent = judgmentTextTemplate;
                 discriminatorJudgment.classList.add(judgmentClass); // Add specific class for styling
                 confidenceBar.style.width = `${confidence}%`;
                 confidencePercentage.textContent = `${confidence}%`;

                 // Update Realism (this improves based on Generator's success over iterations)
                 realismBar.style.width = `${realism}%`;
                 realismPercentage.textContent = `${realism}%`;

                 // Display feedback
                 displayFeedback(feedbackTextTemplate);

                 // Enable button after animation
                 nextButton.disabled = false;
                  nextButton.innerHTML = 'צא לסיבוב אימון! <i class="fas fa-play"></i>';

            }, 700); // Short delay for discriminator "thinking"
        }, 300); // Short delay for generator "generating" animation

        // Update Iteration Counter
        iterationCounter.textContent = `אימון: ${currentIteration}`;

        // Handle max iterations
        if (currentIteration >= maxIterations) {
             nextButton.textContent = "האימון הסתיים!";
             nextButton.disabled = true;
             displayFeedback("הגענו לסוף הסימולציה. היצרן השתפר משמעותית, והבלש מתקשה להבדיל!");
        }
    }

    function displayFeedback(message) {
        feedbackArea.textContent = message;
        feedbackArea.classList.add('show');
        setTimeout(() => {
            feedbackArea.classList.remove('show');
        }, 3000); // Message disappears after 3 seconds
    }

    function resetSimulation() {
         iteration = 0;
         updateSimulation(iteration);
         nextButton.disabled = false;
         nextButton.textContent = 'צא לסיבוב אימון! <i class="fas fa-play"></i>';
          feedbackArea.textContent = ""; // Clear feedback
    }


    nextButton.addEventListener('click', () => {
        if (iteration < maxIterations) {
             iteration++;
             nextButton.disabled = true; // Disable button during animation
             nextButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> אימון...'; // Loading spinner
             updateSimulation(iteration);
        }
    });

    resetButton.addEventListener('click', resetSimulation);

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = fullExplanation.style.display === 'none';
        fullExplanation.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.innerHTML = isHidden ? 'הסתר הסבר מעמיק <i class="fas fa-chevron-up"></i>' : 'הצגת הסבר מעמיק על GANs <i class="fas fa-chevron-down"></i>';
         if (isHidden) {
             fullExplanation.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });

    // Add FontAwesome for icons (assuming it's loaded globally or via CDN elsewhere)
    // If not loaded, add a script tag to the HTML head or footer.
    // <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/js/all.min.js"></script>


    // Initial state
    updateSimulation(iteration);

</script>

<style>
     /* Add FontAwesome support */
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');


    .gan-simulator {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        border: 1px solid #e0e0e0;
        padding: 25px;
        border-radius: 12px;
        margin: 25px 0;
        background-color: #ffffff;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }

    .gan-simulator h2 {
        text-align: center;
        color: #333;
        margin-top: 0;
        font-size: 1.8em;
        margin-bottom: 20px;
    }

     .gan-simulator h3 {
        text-align: center;
        color: #555;
        font-size: 1.3em;
         margin-top: 0;
         margin-bottom: 10px;
     }

    .gan-simulator h3 span {
        font-size: 0.8em;
        color: #777;
        font-weight: normal;
        display: block;
        margin-top: 5px;
    }


    .simulator-area {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px;
        margin-bottom: 30px;
    }

    .real-images-section, .generator-section, .discriminator-section {
        background-color: #f8f8f8;
        padding: 20px;
        border-radius: 10px;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
        text-align: center;
        width: 100%;
        max-width: 500px; /* Adjust max width */
    }

    .section-label {
        font-size: 0.85em;
        color: #777;
        margin-top: 15px;
    }

    .real-images-grid {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 15px;
    }

    .real-images-grid img {
        width: 55px; /* Slightly larger */
        height: 55px;
        border: 2px solid #ddd;
        border-radius: 8px; /* More rounded */
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    .gan-process {
        display: flex;
        flex-direction: column; /* Stack Generator and Discriminator vertically */
        align-items: center;
        gap: 20px;
        width: 100%;
    }

    .process-flow {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        flex-wrap: wrap; /* Allow wrapping within flow if needed */
    }

    .input-noise i {
        color: #673AB7; /* Purple icon */
        font-size: 1.5em;
        margin-inline-end: 5px;
    }

    .generator-output img, .discriminator-input img {
        width: 120px; /* Larger image */
        height: 120px;
        border: 2px solid #bbb;
        margin: 0; /* Remove margin-bottom */
        border-radius: 8px;
         object-fit: cover; /* Ensure SVG scales correctly */
         transition: opacity 0.3s ease-in-out; /* Animation for new image */
    }

    .discriminator-input img {
        border-color: #2196F3; /* Blue border for discriminator input */
        box-shadow: 0 0 10px rgba(33, 150, 243, 0.3);
    }

    .arrow {
        font-size: 2em; /* Larger arrow */
        color: #777;
        font-weight: bold;
    }

    .arrow-down {
        transform: rotate(90deg); /* Point down */
    }

    .judgment {
        font-size: 1.2em;
        font-weight: bold;
        min-height: 1.5em; /* Ensure space */
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 5px 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        transition: background-color 0.5s ease, color 0.5s ease;
    }

    .judgment-fake {
        background-color: #ffcdd2; /* Light red */
        color: #c62828; /* Dark red */
    }

    .judgment-suspect {
        background-color: #ffecb3; /* Light yellow */
        color: #fbc02d; /* Dark yellow */
    }

     .judgment-unsure {
        background-color: #e0e0e0; /* Light gray */
        color: #616161; /* Gray */
    }

     .judgment-real-guess {
         background-color: #c8e6c9; /* Light green */
         color: #388e3c; /* Dark green */
         animation: pulse 1s infinite ease-in-out alternate; /* Highlight correct guess (for Generator) */
     }

     @keyframes pulse {
         from { transform: scale(1); }
         to { transform: scale(1.05); }
     }


    .realism-score, .confidence-score {
        margin-top: 10px;
        font-size: 0.9em;
        color: #555;
        display: flex;
        align-items: center;
        gap: 8px; /* Increased gap */
        width: 100%; /* Take full width */
    }

     .score-label {
         flex-shrink: 0; /* Don't shrink label */
     }

    .score-bar-container {
        flex-grow: 1;
        height: 12px; /* Taller bar */
        background-color: #eee;
        border-radius: 6px; /* More rounded */
        overflow: hidden;
        text-align: right; /* RTL direction */
        border: 1px solid #ccc;
    }

    .score-bar {
        height: 100%;
        background: linear-gradient(to left, #81C784, #4CAF50); /* Green gradient for realism */
        transition: width 0.8s ease-in-out; /* Slower, smoother transition */
        direction: ltr; /* Bar fills from left conceptually */
    }

    .confidence-score .score-bar {
         background: linear-gradient(to left, #64B5F6, #2196F3); /* Blue gradient for confidence */
    }

    .controls {
        text-align: center;
        margin-top: 30px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
    }

    #next-iteration-button, .secondary-button {
        padding: 12px 25px; /* More padding */
        font-size: 1.1em; /* Larger text */
        cursor: pointer;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    #next-iteration-button {
        background-color: #4CAF50;
        color: white;
        box-shadow: 0 4px 8px rgba(76, 175, 80, 0.3);
    }

    #next-iteration-button:hover:not(:disabled) {
        background-color: #45a049;
        transform: translateY(-2px);
         box-shadow: 0 6px 12px rgba(76, 175, 80, 0.4);
    }

     #next-iteration-button:active:not(:disabled) {
         transform: translateY(0);
          box-shadow: 0 4px 8px rgba(76, 175, 80, 0.3);
     }

    #next-iteration-button:disabled {
        background-color: #a5d6a7;
        cursor: not-allowed;
        box-shadow: none;
    }

     .secondary-button {
        background-color: #e0e0e0;
        color: #555;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
     }

     .secondary-button:hover {
         background-color: #d5d5d5;
         transform: translateY(-1px);
          box-shadow: 0 3px 6px rgba(0,0,0,0.15);
     }

      .secondary-button:active {
         transform: translateY(0);
          box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      }


    #iteration-counter {
        font-size: 1.1em;
        color: #555;
        min-height: 1.2em; /* Reserve space */
    }

    .toggle-button {
        display: block;
        width: fit-content;
        margin: 25px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        display: flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
    }

    .toggle-button:hover {
        background-color: #0056b3;
        transform: translateY(-2px);
         box-shadow: 0 6px 12px rgba(0, 123, 255, 0.4);
    }

     .toggle-button:active {
         transform: translateY(0);
          box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
     }


    #full-explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        background-color: #fefefe;
        direction: rtl;
        text-align: right;
         box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    }

    #full-explanation h2, #full-explanation h3 {
        color: #333;
        text-align: right;
         margin-bottom: 10px;
    }

     #full-explanation h2 {
         font-size: 1.6em;
          border-bottom: 1px solid #eee;
          padding-bottom: 10px;
     }
      #full-explanation h3 {
          font-size: 1.3em;
          color: #555;
           margin-top: 20px;
      }


     #full-explanation ul {
        list-style-type: disc;
        margin-right: 20px;
        padding-right: 0; /* Reset padding for RTL */
     }
      #full-explanation li {
        margin-bottom: 10px;
        line-height: 1.6;
        color: #444;
     }
      #full-explanation p {
          line-height: 1.6;
           color: #444;
            margin-bottom: 15px;
      }
      #full-explanation strong {
          color: #333;
      }

     .feedback-area {
         min-height: 20px; /* Reserve space */
         margin-top: 15px;
         font-size: 1em;
         color: #007bff; /* Blue for feedback */
         text-align: center;
         opacity: 0;
         transition: opacity 0.5s ease-in-out;
     }
      .feedback-area.show {
          opacity: 1;
      }


    /* Responsive adjustments */
    @media (max-width: 600px) {
         .simulator-area {
             gap: 20px;
         }
        .process-flow {
            flex-direction: column;
            gap: 10px;
        }
         .arrow {
            transform: rotate(90deg);
         }
        .generator-output img, .discriminator-input img {
            width: 90px;
            height: 90px;
        }
         .real-images-grid img {
             width: 40px;
             height: 40px;
             gap: 8px;
         }
         .gan-simulator h2 {
             font-size: 1.5em;
         }
         .gan-simulator h3 {
              font-size: 1.1em;
         }
         #next-iteration-button, .secondary-button, .toggle-button {
             padding: 10px 20px;
             font-size: 1em;
         }
          .realism-score, .confidence-score {
              flex-direction: column;
              align-items: flex-end; /* Align labels to the right in RTL */
              gap: 5px;
          }
           .score-label {
              width: 100%;
               text-align: center;
           }
           .score-bar-container {
               width: 100%;
           }
            .judgment {
                font-size: 1em;
            }
            #full-explanation ul {
                margin-right: 15px;
            }
    }
</style>
```