---
title: "הסוד הסימטרי של השימור: משפט נתר"
english_slug: the-symmetric-secret-of-conservation-noethers-theorem
category: "פיזיקה"
tags: [פיזיקה, סימטריה, שימור, משפט נתר, מכניקה אנליטית]
---
# הסוד הסימטרי של השימור: משפט נתר

למה אנרגיה ותנע קווי נשמרים במערכות מסוימות? האם יש עקרון עמוק יותר המאחד את כל חוקי השימור בפיזיקה? צללו איתנו למסע מרתק לגילוי הקשר האלגנטי והרב עוצמה בין סימטריה לחוקי השימור היסודיים ביותר השולטים ביקום.

<div id="app-container">
    <h2>גלו את הקשר בין סימטריה לשימור - בחנו בעצמכם!</h2>
    <p class="intro-text">בחרו מערכת פיזיקלית וטרנספורמציה סימטרית (או לא) כדי לראות במו עיניכם את משפט נתר בפעולה.</p>

    <div class="controls">
        <div class="control-group">
            <label for="system-select">בחרו מערכת פיזיקלית:</label>
            <select id="system-select">
                <option value="free-particle">חלקיק חופשי (1D) 🚀</option>
                <option value="harmonic-oscillator">מתנד הרמוני (1D) 🎢</option>
                <option value="uniform-potential">חלקיק בפוטנציאל אחיד (כוח קבוע, 1D) ↘️</option>
                 <option value="time-dependent-potential">חלקיק בפוטנציאל תלוי-זמן (1D) ⏳</option>
            </select>
        </div>
        <div class="control-group">
            <label for="transform-select">בחרו טרנספורמציה:</label>
            <select id="transform-select">
                <option value="time-translation">הזזת זמן (t → t + δt) 🕰️</option>
                <option value="spatial-translation">הזזת מרחב (x → x + δx) ↔️</option>
            </select>
        </div>
    </div>

    <div id="check-flow">
        <h3>מסע הגילוי: צעד אחר צעד עם משפט נתר</h3>

        <div id="step-lagrangian" class="check-step initial">
            <h4><span class="step-icon">1️⃣</span> המערכת שבחרתם והלגראנז'יאן שלה:</h4>
            <p id="system-desc"></p>
            <div class="lagrangian-display">הלגראנז'יאן (<span class="math">L</span>, פונקציית הפעולה): <span class="math" id="lagrangian-eq"></span></div>
        </div>

        <div id="step-transform" class="check-step">
            <h4><span class="step-icon">2️⃣</span> הטרנספורמציה שבחרתם:</h4>
            <p id="transform-desc"></p>
             <div id="transform-visual" class="visual-cue"></div> <!-- Add a visual cue here -->
        </div>

        <div id="step-apply-transform" class="check-step">
             <h4><span class="step-icon">3️⃣</span> השפעת הטרנספורמציה על הלגראנז'יאן:</h4>
             <p id="transform-effect-text"></p>
             <!-- Could potentially show L' here, but keeping it simpler with explanation -->
        </div>

        <div id="step-invariance" class="check-step">
            <h4><span class="step-icon">4️⃣</span> בדיקת סימטריה (אינווריאנטיות):</h4>
            <p>האם הלגראנז'יאן נשאר ללא שינוי תחת הטרנספורמציה? <span id="invariance-question"></span></p>
            <div id="invariance-result-box" class="result-box">
                 <span class="result-icon"></span><span class="result-text"></span>
            </div>
        </div>

        <div id="step-conservation" class="check-step">
             <h4><span class="step-icon">5️⃣</span> מסקנת שימור (עקרון הזהב של נתר):</h4>
             <p>לפי משפט נתר, אם יש סימטריה רציפה לטרנספורמציה מסוימת, קיים גודל פיזיקלי מתאים שנשמר. אם אין סימטריה, הגודל הזה לא בהכרח נשמר.</p>
             <div id="conservation-result-box" class="result-box">
                  <span class="result-icon"></span><span class="result-text"></span>
             </div>
        </div>
    </div>

     <div id="symmetry-breaking-example">
        <h3><span class="breaking-icon">💥</span> דוגמה לשבירת סימטריה - כשהאנרגיה הולכת לאיבוד (או מרוויחה):</h3>
        <p>נבחן מקרה קלאסי שבו סימטריית הזזת הזמן נשברת: חלקיק בפוטנציאל המשתנה בזמן (<span class="math">V(t)</span>). האם האנרגיה נשמרת?</p>
         <button id="show-breaking-example" class="secondary-button">הצג/הסתר הסבר</button>
         <div id="breaking-example-details" style="display: none;">
             <p><strong>המערכת:</strong> חלקיק בפוטנציאל <span class="math">V(t)</span>. הלגראנז'יאן הוא <span class="math">L = \frac{1}{2}mv^2 - V(t)</span>.</p>
             <p><strong>הטרנספורמציה:</strong> הזזת זמן, <span class="math">t \rightarrow t' = t + \delta t</span>. מיקום ומהירות נבחנים בזמן החדש.</p>
             <p><strong>בדיקת אינווריאנטיות:</strong> כדי שהלגראנז'יאן יהיה אינווריאנטי, הוא לא יכול להיות תלוי ב-<span class="math">t</span> במפורש. במערכת זו, <span class="math">V(t)</span> תלוי בזמן. לכן, <span class="math">\frac{\partial L}{\partial t} = -\frac{\partial V}{\partial t} \ne 0</span> (בדרך כלל). הלגראנז'יאן *אינו* אינווריאנטי תחת הזזת זמן. סימטריית הזזת הזמן *נשברת*.</p>
             <p><strong>המסקנה לפי משפט נתר:</strong> מכיוון שסימטריית הזזת הזמן נשברת, הגודל הפיזיקלי הקשור אליה - *האנרגיה* - אינו נשמר במערכת זו. זה הגיוני: אם הפוטנציאל משתנה עם הזמן (למשל, שדה חשמלי חיצוני שמתחזק), המערכת יכולה לקבל או לאבד אנרגיה מהמקור של הפוטנציאל המשתנה.</p>
         </div>
    </div>

</div>

<button id="toggle-explanation" class="main-explanation-button">הרחבת אופקים: הסבר מעמיק על משפט נתר</button>

<div id="full-explanation" style="display: none;">
    <section>
        <h2>הסבר מורחב: משפט נתר - הלב הפועם של חוקי השימור</h2>
        <p>משפט נתר, פרי מוחה המבריק של המתמטיקאית הגרמנייה אמי נתר (Emmy Noether) בשנת 1915, הוא אבן יסוד בפיזיקה המודרנית. הוא חושף קשר יסודי ומפתיע בין שני מושגים מרכזיים: **סימטריה** ו**חוקי שימור**. במילים פשוטות, המשפט קובע שלכל סימטריה רציפה של חוקי הטבע, קיים גודל פיזיקלי מקביל שנשמר לאורך זמן!</p>

        <h3>מהו גודל נשמר בפיזיקה? 🛡️</h3>
        <p>גודל נשמר הוא כמות פיזיקלית שערכה הכולל נשאר קבוע במערכת מסוימת, כל עוד אין השפעות חיצוניות שמפרות את השימור. דמיינו כספת שהערך הכספי בתוכה נשאר קבוע כל עוד היא סגורה. הדוגמאות הקלאסיות, שכולנו מכירים אינטואיטיבית, הן:</p>
        <ul>
            <li>**אנרגיה כוללת:** במערכות מבודדות שבהן פועלים רק כוחות משמרים (כמו כבידה או כוח קפיץ), סכום האנרגיה הקינטית והפוטנציאלית קבוע. כדור נופל ממיר אנרגיה פוטנציאלית לקינטית, אך הסכום נשמר (בהזנחת חיכוך וגורמים אחרים).</li>
            <li>**תנע קווי:** במערכת שאין עליה כוח חיצוני כולל, התנע הקווי (מסה כפול מהירות) של המערכת נשמר. למשל, בהתנגשות בין שני גופים ללא כוחות חיצוניים, התנע הכולל לפני ההתנגשות שווה לתנע הכולל אחריה.</li>
            <li>**תנע זוויתי:** במערכת שאין עליה מומנט כוח חיצוני כולל, התנע הזוויתי (קשור לסיבוב) שלה נשמר. לדוגמה, מחליק/ה על הקרח מסתובב/ת מהר יותר כשהוא/היא מכנס/ת את הידיים פנימה - התנע הזוויתי נשמר, ולכן המהירות הזוויתית גדלה עם הקטנת רדיוס הסיבוב.</li>
        </ul>
        <p>חוקי השימור הללו אינם רק תצפיות אמפיריות; הם עקרונות יסוד בעלי השלכות עמוקות על אופן פעולת היקום.</p>

        <h3>מהי סימטריה בפיזיקה? ✨</h3>
        <p>בפיזיקה, סימטריה פירושה שהמערכת או חוקי הפיזיקה המתארים אותה אינם משתנים כאשר מבצעים עליהם טרנספורמציה מסוימת. חשבו על כדור: הוא נראה אותו הדבר לא משנה מאיזו זווית מסתכלים עליו (סימטריית סיבוב). בפיזיקה, אנו מתעניינים במיוחד בסימטריות של *חוקי הפיזיקה* או של *הלגראנז'יאן* של המערכת - גודל מתמטי המכיל את כל המידע על דינמיקת המערכת.</p>
         <p>משפט נתר מתמקד בסימטריות "רציפות" - אלו שניתן לבצע בהן שינוי הדרגתי (כמו הזזה קטנה במרחב, או קפיצה קטנה בזמן).</p>

        <h3>הסימטריות ה"אחראיות" לחוקי השימור המוכרים:</h3>
        <p>במכניקה קלאסית, הקשרים המרכזיים שחושף משפט נתר הם:</p>
        <ul>
            <li>**סימטריית הזזת זמן (Time Translation Invariance):** אם חוקי הפיזיקה והלגראנז'יאן של מערכת אינם תלויים במפורש ב"מתי" האירוע מתרחש, אלא רק ב"כמה זמן" הוא לוקח, אזי המערכת סימטרית תחת הזזות זמן. התוצאה? **שימור אנרגיה!** 🕰️↔️🛡️⚡</li>
            <li>**סימטריית הזזת מרחב (Spatial Translation Invariance):** אם חוקי הפיזיקה והלגראנז'יאן של מערכת אינם תלויים ב"היכן" האירוע מתרחש במרחב, אלא רק בתזוזה היחסית, אזי המערכת סימטרית תחת הזזות מרחב (המרחב "הומוגני"). התוצאה? **שימור תנע קווי!** ↔️↔️🛡️➡️</li>
            <li>**סימטריית סיבוב (Rotation Invariance):** אם חוקי הפיזיקה והלגראנז'יאן של מערכת אינם תלויים ב"לאיזה כיוון" המערכת פונה, אזי המערכת סימטרית תחת סיבובים (המרחב "איזוטרופי"). התוצאה? **שימור תנע זוויתי!** 🔄↔️🛡️💫</li>
        </ul>
        <p>שימו לב: סימטריות אלו מתקיימות במערכות "סגורות" או כאלה שאינן תחת השפעת שדות חיצוניים המפרים את הסימטריה. למשל, כבידה ליד כדור הארץ מפרה סימטריית הזזה אנכית (פוטנציאל תלוי גובה) ולכן הרכיב האנכי של התנע אינו נשמר (אלא אם כוללים את כדור הארץ במערכת). שדה מגנטי מפר סימטריית סיבוב.</p>

        <h3>העוצמה והיופי של משפט נתר 💖</h3>
        <p>משפט נתר אינו רק טכניקה לזיהוי גדלים נשמרים; הוא חושף שהסימטריות הן המקור העמוק ביותר לחוקי השימור הבסיסיים. זהו עיקרון מאחד שמפשט ומסביר חלקים עצומים מהפיזיקה, ממכניקה קלאסית וקוונטית, דרך תורת השדות הקוונטית (שם הוא חוזה שימור של מטענים כמו מטען חשמלי כתוצאה מסימטריות "פנימיות" של שדות) ועד קוסמולוגיה. הוא מראה לנו ששמירה על דברים קבועים (שימור) קשורה קשר בל יינתק לכך שדברים אחרים נראים אותו הדבר מנקודות מבט שונות (סימטריה).</p>
         <p>זוהי דוגמה מופלאה לאלגנטיות והעומק של החוקים הפיזיקליים, וכוחה של המתמטיקה לחשוף את המבנים הנסתרים של הטבע.</p>
    </section>
</div>

<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', () => {
        const systemSelect = document.getElementById('system-select');
        const transformSelect = document.getElementById('transform-select');
        const systemDescDiv = document.getElementById('system-desc');
        const lagrangianEqSpan = document.getElementById('lagrangian-eq');
        const transformDescDiv = document.getElementById('transform-desc');
        const transformVisualDiv = document.getElementById('transform-visual'); // Visual cue for transform
        const transformEffectText = document.getElementById('transform-effect-text');
        const invarianceQuestionSpan = document.getElementById('invariance-question');
        const invarianceResultBox = document.getElementById('invariance-result-box');
        const conservationResultBox = document.getElementById('conservation-result-box');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const fullExplanationDiv = document.getElementById('full-explanation');
        const showBreakingExampleButton = document.getElementById('show-breaking-example');
        const breakingExampleDetailsDiv = document.getElementById('breaking-example-details');

        // Helper function to set content and trigger MathJax
        function setMathContent(element, html) {
            element.innerHTML = html;
             // Using MathJax.typesetPromise on the parent container for efficiency
             if (typeof MathJax !== 'undefined') {
                MathJax.typesetPromise([element.parentElement]).catch((err) => console.log('MathJax rendering error: ' + err.message));
             }
        }

        // Helper to update result boxes
        function updateResultBox(boxElement, isPositive, text) {
            const iconSpan = boxElement.querySelector('.result-icon');
            const textSpan = boxElement.querySelector('.result-text');

            if (isPositive) {
                boxElement.classList.remove('negative');
                boxElement.classList.add('positive');
                iconSpan.textContent = '✅';
            } else {
                boxElement.classList.remove('positive');
                boxElement.classList.add('negative');
                 iconSpan.textContent = '❌';
            }
            textSpan.textContent = text;
             // Trigger CSS animation
             boxElement.classList.add('updated');
             setTimeout(() => boxElement.classList.remove('updated'), 500); // Remove class after animation
        }

        function updateApp() {
            const system = systemSelect.value;
            const transform = transformSelect.value;

            let lagrangian = "";
            let systemDescription = "";
            let transformDescription = transformSelect.options[transformSelect.selectedIndex].text;
            let conservedQuantityName = "";
            let isInvariant = false;
            let invarianceExplanation = "";
            let conservationResultText = "";
            let transformVisualHtml = "";

            // Step 1: System Info & Lagrangian
            switch (system) {
                case 'free-particle':
                    systemDescription = "מערכת: חלקיק חופשי הנע בקו ישר (1D). אין כוחות חיצוניים.";
                    lagrangian = String.raw`L = \frac{1}{2} m v^2`;
                    break;
                case 'harmonic-oscillator':
                    systemDescription = "מערכת: חלקיק המחובר לקפיץ אידיאלי, נע ב-1D.";
                    lagrangian = String.raw`L = \frac{1}{2} m v^2 - \frac{1}{2} k x^2`;
                    break;
                case 'uniform-potential':
                    systemDescription = "מערכת: חלקיק הנע ב-1D תחת השפעת כוח קבוע (פוטנציאל ליניארי).";
                     lagrangian = String.raw`L = \frac{1}{2} m v^2 - V_0 x`;
                    break;
                 case 'time-dependent-potential':
                     systemDescription = "מערכת: חלקיק הנע ב-1D תחת השפעת פוטנציאל המשתנה במפורש עם הזמן.";
                     lagrangian = String.raw`L = \frac{1}{2} m v^2 - V(t)`;
                     break;
            }
            setMathContent(systemDescDiv, systemDescription);
            setMathContent(lagrangianEqSpan, lagrangian);

            // Step 2: Transformation Info
            setMathContent(transformDescDiv, `נבחר לבחון את סימטריית ${transformDescription}.`);
             // Simple visual cues
             if (transform === 'time-translation') {
                 transformVisualHtml = '🕰️&nbsp; <span class="transform-arrow">→</span> &nbsp;🕰️';
             } else if (transform === 'spatial-translation') {
                 transformVisualHtml = '↔️&nbsp; <span class="transform-arrow">→</span> &nbsp;↔️';
             }
             transformVisualDiv.innerHTML = transformVisualHtml;


            // Step 3: Effect of Transformation on Lagrangian & Step 4: Invariance Check
            // The check for invariance for continuous transformations boils down to whether L depends explicitly on the variable being transformed (t for time, x for spatial 1D).
            if (transform === 'time-translation') {
                conservedQuantityName = "אנרגיה (האמילטוניאן)";
                invarianceQuestionSpan.textContent = "האם הלגראנז'יאן תלוי במפורש בזמן (∂L/∂t ≠ 0)?";
                if (system === 'time-dependent-potential') {
                    isInvariant = false;
                    invarianceExplanation = `כן, הלגראנז'יאן תלוי ב-${transformDescription} דרך הפוטנציאל ${String.raw`V(t)`}. ${String.raw`\frac{\partial L}{\partial t} = -\frac{\partial V}{\partial t} \ne 0`}.`;
                    transformEffectText.innerHTML = `מכיוון שהפוטנציאל <span class="math">V(t)</span> תלוי בזמן, הלגראנז'יאן <span class="math">L = \frac{1}{2} m v^2 - V(t)</span> משתנה כאשר אנו מזיזים את נקודת ההתחלה של הזמן (<span class="math">t \rightarrow t + \delta t</span>).`;
                } else {
                    isInvariant = true;
                    invarianceExplanation = `לא, הלגראנז'יאן אינו תלוי במפורש ב-${transformDescription} (<span class="math">\\frac{\partial L}{\partial t} = 0</span>).`;
                    transformEffectText.innerHTML = `הלגראנז'יאן <span class="math">${lagrangian}</span> אינו מכיל את <span class="math">t</span> במפורש, ולכן הוא נשאר זהה כאשר אנו מזיזים את נקודת ההתחלה של הזמן (<span class="math">t \rightarrow t + \delta t</span>).`;
                }

            } else if (transform === 'spatial-translation') {
                conservedQuantityName = "תנע קווי";
                 invarianceQuestionSpan.textContent = "האם הלגראנז'יאן תלוי במפורש במיקום (∂L/∂x ≠ 0)?";
                 if (system === 'free-particle' || system === 'time-dependent-potential') { // L = 1/2 mv^2 or 1/2 mv^2 - V(t)
                     isInvariant = true;
                     invarianceExplanation = `לא, הלגראנז'יאן אינו תלוי במפורש ב-${transformDescription} (<span class="math">\\frac{\partial L}{\partial x} = 0</span>).`;
                     transformEffectText.innerHTML = `הלגראנז'יאן <span class="math">${lagrangian}</span> אינו מכיל את <span class="math">x</span> במפורש, ולכן הוא נשאר זהה כאשר אנו מזיזים את נקודת ההתחלה של המרחב (<span class="math">x \rightarrow x + \delta x</span>).`;
                 } else if (system === 'harmonic-oscillator') { // L = 1/2 mv^2 - 1/2 kx^2
                     isInvariant = false;
                     invarianceExplanation = `כן, הלגראנז'יאן תלוי ב-${transformDescription} דרך הפוטנציאל ${String.raw`\frac{1}{2} k x^2`}. ${String.raw`\frac{\partial L}{\partial x} = -kx \ne 0`} (עבור <span class="math">x \ne 0</span>).`;
                     transformEffectText.innerHTML = `הלגראנז'יאן <span class="math">L = \frac{1}{2} m v^2 - \frac{1}{2} k x^2</span> מכיל את <span class="math">x</span> במפורש. כאשר אנו מזיזים את נקודת ההתחלה של המרחב (<span class="math">x \rightarrow x + \delta x</span>), הלגראנז'יאן משתנה.`;
                 } else if (system === 'uniform-potential') { // L = 1/2 mv^2 - V0x
                      isInvariant = false;
                      invarianceExplanation = `כן, הלגראנז'יאן תלוי ב-${transformDescription} דרך הפוטנציאל ${String.raw`V_0 x`}. ${String.raw`\frac{\partial L}{\partial x} = -V_0 \ne 0`} (עבור <span class="math">V_0 \ne 0</span>).`;
                       transformEffectText.innerHTML = `הלגראנז'יאן <span class="math">L = \frac{1}{2} m v^2 - V_0 x</span> מכיל את <span class="math">x</span> במפורש. כאשר אנו מזיזים את נקודת ההתחלה של המרחב (<span class="math">x \rightarrow x + \delta x</span>), הלגראנז'יאן משתנה.`;
                 }
            }

             setMathContent(invarianceResultBox.querySelector('.result-text'), invarianceExplanation);
             updateResultBox(invarianceResultBox, isInvariant, isInvariant ? "כן, המערכת סימטרית תחת טרנספורמציה זו." : "לא, המערכת אינה סימטרית תחת טרנספורמציה זו.");


            // Step 5: Conservation Result
            if (isInvariant) {
                conservationResultText = `🎉 לפי משפט נתר: מכיוון שהמערכת סימטרית תחת טרנספורמציה זו, הגודל הפיזיקלי הקשור - **${conservedQuantityName}** - **נשמר** במערכת זו!`;
                updateResultBox(conservationResultBox, true, conservationResultText);
            } else {
                 conservationResultText = `😟 לפי משפט נתר: מכיוון שהמערכת *אינה* סימטרית תחת טרנספורמציה זו, הגודל הפיזיקלי הקשור - **${conservedQuantityName}** - **אינו נשמר בהכרח** במערכת זו. כוח חיצוני (או פוטנציאל חיצוני תלוי בזמן) גורם לשינוי בגודל זה.`;
                 updateResultBox(conservationResultBox, false, conservationResultText);
            }

            // Re-render all math in the app container after updates
            if (typeof MathJax !== 'undefined') {
                MathJax.typesetPromise([document.getElementById('app-container')]).catch((err) => console.log('MathJax final rendering error: ' + err.message));
            }
        }

        // Event listeners for select changes
        systemSelect.addEventListener('change', updateApp);
        transformSelect.addEventListener('change', updateApp);

        // Toggle explanation button
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = fullExplanationDiv.style.display === 'none';
            fullExplanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'צמצם הסבר' : 'הרחבת אופקים: הסבר מעמיק על משפט נתר';
             if (isHidden) {
                 // Render math inside the explanation when shown (if not already rendered)
                 if (!fullExplanationDiv.dataset.mathRendered) {
                      if (typeof MathJax !== 'undefined') {
                         MathJax.typesetPromise([fullExplanationDiv]).then(() => {
                              fullExplanationDiv.dataset.mathRendered = 'true'; // Mark as rendered
                         }).catch((err) => console.log('MathJax explanation rendering error: ' + err.message));
                      }
                 }
             }
        });

        // Toggle breaking example details
         showBreakingExampleButton.addEventListener('click', () => {
             const isHidden = breakingExampleDetailsDiv.style.display === 'none';
             breakingExampleDetailsDiv.style.display = isHidden ? 'block' : 'none';
              showBreakingExampleButton.textContent = isHidden ? 'הסתר הסבר' : 'הצג/הסתר הסבר';
              if (isHidden) {
                 // Render math inside the example when shown (if not already rendered)
                  if (!breakingExampleDetailsDiv.dataset.mathRendered) {
                       if (typeof MathJax !== 'undefined') {
                         MathJax.typesetPromise([breakingExampleDetailsDiv]).then(() => {
                              breakingExampleDetailsDiv.dataset.mathRendered = 'true'; // Mark as rendered
                         }).catch((err) => console.log('MathJax example rendering error: ' + err.message));
                      }
                  }
              }
         });


        // Initial app load
        updateApp();
        // Initial render for the whole page, including hidden elements math (MathJax handles hidden)
        if (typeof MathJax !== 'undefined') {
             MathJax.typesetPromise().catch((err) => console.log('MathJax initial rendering error: ' + err.message));
        }
    });
</script>

<style>
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7; /* Slightly increased line height */
        margin: 0; /* Remove default margin */
        padding: 20px; /* Add padding instead */
        background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2); /* Soft gradient background */
        color: #333;
        direction: rtl; /* Right-to-left for Hebrew */
        text-align: right;
    }

    h1, h2, h3, h4 {
        color: #004d40; /* Dark teal headings */
        margin-bottom: 15px;
        line-height: 1.4;
    }

    h1 {
        text-align: center;
        color: #00796b; /* Stronger teal for main title */
        margin-bottom: 30px;
    }

    #app-container {
        background-color: #ffffff; /* White background for the app */
        padding: 30px; /* More padding */
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* Stronger, softer shadow */
        margin-bottom: 30px;
        border-top: 5px solid #009688; /* Accent color top border */
    }

     .intro-text {
         text-align: center;
         margin-bottom: 30px;
         font-size: 1.1rem;
         color: #555;
     }

    .controls {
        display: flex;
        gap: 25px; /* Increased gap */
        margin-bottom: 30px;
        flex-wrap: wrap; /* Allow wrapping on small screens */
        justify-content: center; /* Center controls */
    }

    .control-group {
        flex: 1;
        min-width: 280px; /* Wider minimum width */
        background-color: #e0f2f7; /* Light blue background */
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #b2ebf2;
    }

    label {
        display: block;
        margin-bottom: 8px; /* More space below label */
        font-weight: bold;
        color: #004d40; /* Dark teal color for labels */
        font-size: 1rem;
    }

    select {
        width: 100%;
        padding: 10px 12px; /* More padding */
        border: 1px solid #b2ebf2; /* Match group border */
        border-radius: 6px; /* Slightly more rounded */
        font-size: 1rem;
        background-color: #ffffff;
        cursor: pointer;
        appearance: none; /* Remove default select arrow */
        background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23004d40%22%20d%3D%22M287%2C197.9c-3.6%2C3.6-7.8%2C5.4-12.8%2C5.4H18.2c-5%2C0-9.2-1.8-12.8-5.4l-10.9-10.9c-3.6-3.6-5.4-7.8-5.4-12.8s1.8-9.2%2C5.4-12.8L134.2%2C1.4c3.6-3.6%2C7.8-5.4%2C12.8-5.4s9.2%2C1.8%2C12.8%2C5.4l132.9%2C132.9c3.6%2C3.6%2C5.4%2C7.8%2C5.4%2C12.8S290.6%2C194.4%2C287%2C197.9z%22%2F%3E%3C%2Fsvg%3E'); /* Custom arrow */
        background-repeat: no-repeat;
        background-position: left 12px center; /* Position arrow on the left */
        background-size: 12px;
        padding-right: 30px; /* Make space for the arrow */
    }

    select:hover {
         border-color: #00796b;
    }

     #check-flow {
         margin-top: 30px;
         border-top: 2px solid #009688;
         padding-top: 20px;
     }

     #check-flow h3 {
         text-align: center;
         color: #00796b;
         margin-bottom: 25px;
     }

     .check-step {
         background-color: #e0f7fa; /* Lighter blue for steps */
         border: 1px solid #b2ebf2;
         border-radius: 8px;
         padding: 15px 20px;
         margin-bottom: 20px;
         transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
     }

     .check-step:hover {
          transform: translateY(-3px);
          box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
     }

     .check-step h4 {
         color: #006064; /* Even darker teal for step titles */
         margin-top: 0;
         margin-bottom: 10px;
         padding-bottom: 5px;
         border-bottom: 1px dashed #b2ebf2;
     }

     .step-icon {
         margin-left: 10px;
         font-size: 1.2rem;
         vertical-align: middle;
     }

    .lagrangian-display {
        background-color: #ffffff;
        padding: 10px;
        border-left: 4px solid #009688;
        border-radius: 4px;
        font-family: monospace; /* Or keep MathJax default */
        margin-top: 10px;
        overflow-x: auto; /* Allow horizontal scroll for long equations */
        direction: ltr; /* Ensure equation direction is LTR */
        text-align: left;
    }

    .lagrangian-display .math {
        font-family: serif; /* Override monospace for MathJax */
        direction: ltr;
    }


     #transform-visual {
         text-align: center;
         font-size: 1.8rem;
         margin: 15px 0;
         color: #00796b;
     }

     .transform-arrow {
         display: inline-block;
         margin: 0 10px;
         animation: pulse 1.5s infinite; /* Simple animation for emphasis */
     }

     @keyframes pulse {
         0% { opacity: 1; }
         50% { opacity: 0.5; }
         100% { opacity: 1; }
     }


     .result-box {
         margin-top: 15px;
         padding: 15px;
         border-radius: 8px;
         font-weight: bold;
         font-size: 1.1rem;
         display: flex;
         align-items: center;
         gap: 10px;
         opacity: 0; /* Start hidden for animation */
         transform: translateY(10px); /* Start slightly lower */
         transition: opacity 0.5s ease-out, transform 0.5s ease-out, background-color 0.3s ease;
     }

     .result-box.updated {
         opacity: 1;
         transform: translateY(0);
     }


     .result-box.positive {
         background-color: #e8f5e9; /* Light green */
         border: 2px solid #4caf50; /* Green border */
         color: #1b5e20; /* Dark green text */
     }

     .result-box.negative {
         background-color: #ffebee; /* Light red */
         border: 2px solid #f44336; /* Red border */
         color: #b71c1c; /* Dark red text */
     }

     .result-icon {
         font-size: 1.5rem;
         vertical-align: middle;
     }


    button {
        display: inline-block;
        padding: 12px 20px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1rem;
        margin-top: 15px;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

     button:active {
         transform: scale(0.98); /* Press effect */
     }

    .main-explanation-button {
        display: block; /* Make it a block button */
        width: fit-content; /* Fit content width */
        margin: 30px auto; /* Center the button */
        background-color: #00796b; /* Teal color */
        color: white;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .main-explanation-button:hover {
        background-color: #004d40; /* Darker teal */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }

    .secondary-button {
         background-color: #e0f2f7; /* Light blue */
         color: #004d40; /* Dark teal */
         border: 1px solid #b2ebf2;
         margin-top: 5px;
         margin-bottom: 5px;
    }

     .secondary-button:hover {
         background-color: #b2ebf2; /* Slightly darker light blue */
     }


    #full-explanation {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
        margin-top: 30px;
        border-top: 5px solid #009688;
    }

    #full-explanation section {
        margin-bottom: 25px;
        padding-bottom: 20px;
        border-bottom: 1px dashed #eee;
    }
     #full-explanation section:last-child {
         border-bottom: none;
         padding-bottom: 0;
     }


    #full-explanation h3 {
        margin-top: 20px;
        margin-bottom: 15px;
        color: #006064;
        border-bottom: 1px solid #b2ebf2; /* Use a lighter line */
        padding-bottom: 8px;
    }

    #full-explanation ul {
        margin-bottom: 15px;
        padding-right: 20px; /* Indent list items */
    }

    #full-explanation li {
        margin-bottom: 10px; /* More space between list items */
        list-style: disc outside; /* Use disc bullets */
         color: #444;
    }
     #full-explanation li strong {
         color: #004d40; /* Highlight key terms */
     }

    #symmetry-breaking-example {
         background-color: #fff3e0; /* Light orange background */
         border: 1px solid #ffe0b2; /* Orange border */
         color: #e65100; /* Dark orange text */
         padding: 20px;
         border-radius: 8px;
         margin-top: 30px;
         border-left: 5px solid #ff9800; /* Accent border */
     }

     #symmetry-breaking-example h3 {
         color: #e65100; /* Dark orange title */
         margin-top: 0;
         border-bottom: 1px dashed #ffe0b2;
         padding-bottom: 10px;
         display: flex;
         align-items: center;
     }

     .breaking-icon {
         font-size: 1.5rem;
         margin-left: 10px;
     }

     #symmetry-breaking-example button {
         background-color: #ff9800; /* Orange button */
         color: white;
         margin-top: 10px;
     }

     #symmetry-breaking-example button:hover {
         background-color: #f57c00; /* Darker orange */
     }


     #breaking-example-details {
         margin-top: 20px;
         border-top: 1px dashed #ffe0b2;
         padding-top: 15px;
         color: #444; /* Softer text color for details */
     }
      #breaking-example-details strong {
          color: #e65100;
      }


     /* MathJax styling */
     .math {
         font-family: 'Georgia', serif; /* A font that renders mathematical symbols well */
         font-style: italic;
         color: #004d40; /* Match headings color */
     }


     /* Responsive adjustments */
    @media (max-width: 768px) {
        .controls {
            flex-direction: column;
            gap: 15px;
        }

        .control-group {
            min-width: unset; /* Remove min-width on smaller screens */
            width: 100%;
        }

        #app-container, #full-explanation, #symmetry-breaking-example {
            padding: 20px;
        }

         body {
             padding: 10px;
         }
         h1 {
             font-size: 1.8rem;
         }
         h2 {
             font-size: 1.5rem;
         }
         h3 {
             font-size: 1.3rem;
         }
    }

</style>
```