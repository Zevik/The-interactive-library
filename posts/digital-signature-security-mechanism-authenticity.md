---
title: "חתימה דיגיטלית: מנגנון האבטחה שמבטיח אמיתות"
english_slug: digital-signature-security-mechanism-authenticity
category: "מדעי המחשב"
tags: [חתימה דיגיטלית, קריפטוגרפיה, אבטחת מידע, אימות מסמכים, מפתח ציבורי]
---
# חתימה דיגיטלית: המגן הדיגיטלי של האמת

קיבלתם מסמך חשוב באימייל או בוואטסאפ. איך אתם באמת יכולים להיות בטוחים שהוא נשלח על ידי האדם הנכון ושהתוכן שלו לא שונה אפילו במעט מאז שהוא נוצר? בניגוד לחתימה פיזית שניתן לראות, מנגנון האבטחה הדיגיטלי שמבטיח זאת הוא בלתי נראה לעין - אך ניתן לאימות קריפטוגרפי. בואו נצלול יחד למסע מרתק שמגלה איך חתימה דיגיטלית עובדת מאחורי הקלעים.

<div class="interactive-app" dir="rtl">
    <h2 class="app-title">מסע החתימה הדיגיטלית: מיצירה לאימות</h2>
    <p class="app-intro">הכניסו טקסט, חתמו דיגיטלית, ואז בדקו איך שינוי קטן משפיע על האימות.</p>

    <div class="app-section" id="signing-section">
        <h3 class="section-title">שלב 1: יוצרים את החתימה</h3>
        <label for="document-text" class="input-label">תוכן המסמך שלך:</label>
        <textarea id="document-text" rows="4" cols="50" placeholder="כתוב כאן את הטקסט שהיית רוצה לחתום עליו דיגיטלית..."></textarea>
        <button id="sign-button" class="app-button">חתום דיגיטלית עכשיו!</button>

        <div class="process-flow" id="signing-flow">
            <div class="flow-step step-document">
                <span class="step-label">המסמך המקורי</span>
                <div class="step-content" id="signing-text-input">...</div>
            </div>
            <div class="flow-arrow step-arrow">➔</div>
            <div class="flow-step step-hash">
                <span class="step-label">טביעת אצבע (פונקציית Hash)</span>
                <span class="step-icon">#️⃣</span>
                <div class="step-content" id="calculated-hash-display">...</div>
            </div>
            <div class="flow-arrow step-arrow">➔</div>
            <div class="flow-step step-encrypt">
                <span class="step-label">הצפנה (עם המפתח הפרטי שלך 🔒)</span>
                <span class="step-icon">🔑</span>
                <div class="step-content" id="encrypted-hash-display">...</div>
            </div>
            <div class="flow-arrow step-arrow">➔</div>
            <div class="flow-step result-box step-signature">
                <span class="step-label">וזו החתימה הדיגיטלית!</span>
                <div class="step-content" id="digital-signature-display">...</div>
            </div>
        </div>

        <div class="signed-document-output" id="signed-document-output">
            <h3 class="section-title">המסמך החתום: מוכן לשליחה!</h3>
            <p>המסמך המקורי נשאר גלוי, והחתימה מצורפת אליו.</p>
            <div class="output-item">
                <strong>טקסט המסמך:</strong> <span id="output-text">...</span>
            </div>
            <div class="output-item">
                <strong>החתימה הדיגיטלית:</strong> <span id="output-signature">...</span>
            </div>
        </div>
    </div>

    <div class="app-section" id="verification-section">
        <h3 class="section-title">שלב 2: מאמתים את החתימה</h3>
        <p>דמיינו שקיבלתם עכשיו את המסמך החתום. <strong>נסו לשנות את הטקסט בשדה למעלה</strong> לפני הלחיצה על "אמת" - תראו איך אפילו שינוי קל ביותר משפיע על האימות!</p>
        <button id="verify-button" class="app-button">אמת את החתימה!</button>

        <div class="process-flow verification-flow" id="verification-flow">
             <div class="flow-step step-input-verify">
                <span class="step-label">קבלת המסמך והחתימה</span>
                <div class="step-content" id="verification-input">...</div>
            </div>
            <div class="flow-arrow step-arrow down">↓</div>
            <div class="flow-step-group">
                <div class="flow-step step-hash-recalc">
                    <span class="step-label">מחשבים טביעת אצבע חדשה מהטקסט</span>
                    <span class="step-icon">#️⃣</span>
                    <div class="step-content" id="new-calculated-hash-display">...</div>
                </div>
                <div class="flow-arrow step-arrow side">➔</div>
                <div class="flow-step step-decrypt">
                    <span class="step-label">מפענחים חתימה (עם המפתח הציבורי 🔓)</span>
                    <span class="step-icon">🔑</span>
                    <div class="step-content" id="decrypted-hash-display">...</div>
                </div>
            </div>
            <div class="flow-arrow step-arrow down">↓</div>
            <div class="flow-step result-box compare-box step-compare">
                <span class="step-label">משווים את טביעות האצבע</span>
                 <div class="step-content" id="hash-comparison-display">
                     Hash שחושב מחדש: <span id="compare-new" class="compare-value">...</span><br>
                     Hash שחולץ מהחתימה: <span id="compare-original" class="compare-value">...</span>
                 </div>
            </div>
        </div>

        <div class="verification-result" id="verification-result">
            <h3 class="section-title">תוצאת האימות:</h3>
            <p id="result-message" class="result-message"></p>
        </div>
    </div>
</div>

<style>
:root {
    --primary-color: #007bff; /* Blue */
    --secondary-color: #28a745; /* Green */
    --accent-color: #6f42c1; /* Purple */
    --warning-color: #ffc107; /* Yellow */
    --danger-color: #dc3545; /* Red */
    --light-bg: #f8f9fa; /* Light Grey */
    --dark-text: #343a40; /* Dark Grey */
    --border-color: #dee2e6; /* Grey Border */
    --box-shadow: rgba(0, 0, 0, 0.08);

    --animation-duration: 0.6s;
    --animation-delay-step: 0.4s; /* Delay between sequential steps */
}

.interactive-app {
    font-family: 'Arial', sans-serif;
    background-color: var(--light-bg);
    padding: 30px;
    border-radius: 12px;
    max-width: 900px;
    margin: 30px auto;
    direction: rtl;
    text-align: right;
    box-shadow: 0 8px 16px var(--box-shadow);
    border: 1px solid var(--border-color);
}

.app-title {
    color: var(--dark-text);
    text-align: center;
    margin-bottom: 15px;
    font-size: 2em;
    font-weight: bold;
}

.app-intro {
    text-align: center;
    color: #6c757d;
    margin-bottom: 30px;
    font-size: 1.1em;
}

.app-section {
    background-color: #fff;
    padding: 25px;
    margin-bottom: 30px;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
}

.section-title {
    color: var(--dark-text);
    text-align: right;
    margin-bottom: 20px;
    font-size: 1.5em;
    font-weight: bold;
    border-bottom: 2px solid var(--primary-color);
    padding-bottom: 10px;
}

.input-label {
    display: block;
    margin-bottom: 8px;
    font-weight: bold;
    color: var(--dark-text);
}

textarea {
    width: calc(100% - 24px);
    padding: 12px;
    margin-bottom: 20px;
    border: 1px solid var(--border-color);
    border-radius: 6px;
    resize: vertical;
    direction: rtl;
    text-align: right;
    font-size: 1em;
    line-height: 1.5;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.08);
}

textarea:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 5px rgba(0, 123, 255, 0.25);
}

.app-button {
    background-color: var(--primary-color);
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.1em;
    margin-bottom: 20px;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.app-button:hover:not(:disabled) {
    background-color: #0056b3;
    transform: translateY(-1px);
}

.app-button:active:not(:disabled) {
    transform: translateY(0);
    box-shadow: 0 1px 2px rgba(0,0,0,0.1);
}

.app-button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
    box-shadow: none;
}

.process-flow {
    display: flex;
    justify-content: center;
    align-items: flex-start; /* Align items to the top */
    flex-wrap: wrap;
    margin-top: 20px;
    min-height: 150px; /* Ensure space for animation */
    position: relative; /* For absolute positioning of future lines */
    padding: 10px 0;
}

.verification-flow {
    flex-direction: column;
    align-items: center; /* Center items for vertical flow */
}

.flow-step, .result-box {
    border: 2px solid var(--border-color);
    padding: 15px;
    margin: 10px;
    border-radius: 8px;
    text-align: center;
    min-width: 150px;
    max-width: 250px;
    word-break: break-all;
    background-color: var(--light-bg);
    color: var(--dark-text);
    opacity: 0;
    transform: translateY(20px);
    transition: opacity var(--animation-duration) ease-out, transform var(--animation-duration) ease-out, border-color 0.3s ease, box-shadow 0.3s ease;
    position: relative; /* For step-specific animations/indicators */
}

.flow-step.visible, .result-box.visible {
     opacity: 1;
     transform: translateY(0);
}

.flow-step.active-step {
    border-color: var(--accent-color);
    box-shadow: 0 0 8px rgba(111, 66, 193, 0.3);
    background-color: #f3ebff; /* Lighter purple */
}


.step-label {
    display: block;
    font-weight: bold;
    margin-bottom: 8px;
    color: var(--primary-color);
    font-size: 1.1em;
}

.flow-step.active-step .step-label {
    color: var(--accent-color);
}


.step-icon {
    font-size: 2em;
    margin-bottom: 8px;
    display: block;
    color: var(--secondary-color);
}

.flow-arrow {
    margin: 0 15px;
    font-size: 2em;
    color: #adb5bd; /* Grey */
    align-self: center; /* Vertically center arrows in horizontal flow */
    opacity: 0;
    transition: opacity var(--animation-duration) ease-out;
}
.flow-arrow.visible {
     opacity: 1;
}

.flow-arrow.down {
    display: block;
    margin: 15px auto;
    transform: rotate(90deg);
}

.flow-arrow.side {
     display: inline-block;
     transform: rotate(0deg);
     margin: 0 15px;
}

.flow-step-group {
    display: flex;
    align-items: flex-start; /* Align steps at the top */
    margin: 15px 0;
    width: 100%; /* Make group take full width in column layout */
    justify-content: center; /* Center the group content horizontally */
}

.flow-step-group .flow-step {
     margin: 5px 15px; /* Adjust margin within group */
}

.compare-box {
    background-color: var(--warning-color); /* Light yellow */
    border-color: #d39e00; /* Darker yellow */
    color: #664d03; /* Darker yellow text */
    box-shadow: 0 4px 8px rgba(255, 193, 7, 0.3);
}

.compare-box.match {
    background-color: var(--secondary-color);
    border-color: #1e7e34;
    color: #0f381d;
    box-shadow: 0 4px 8px rgba(40, 167, 69, 0.3);
}

.compare-box.mismatch {
     background-color: var(--danger-color);
     border-color: #bd2130;
     color: #491217;
     box-shadow: 0 4px 8px rgba(220, 53, 69, 0.3);
}


.compare-box .step-label {
    color: inherit; /* Use parent color */
    border-bottom: 1px dashed inherit;
    padding-bottom: 5px;
    margin-bottom: 10px;
}

.compare-value {
    font-weight: normal;
    font-family: 'Courier New', monospace;
    word-break: break-all;
}


.signed-document-output {
    margin-top: 30px;
    padding: 20px;
    border: 2px solid var(--secondary-color); /* Green */
    background-color: #e9f5ee; /* Light green */
    border-radius: 8px;
    opacity: 0;
    transform: translateY(20px);
    transition: opacity var(--animation-duration) ease-out, transform var(--animation-duration) ease-out;
    color: #155724; /* Dark green text */
}

.signed-document-output.show {
     opacity: 1;
     transform: translateY(0);
}

.signed-document-output .output-item {
    margin-bottom: 10px;
    word-break: break-all;
    line-height: 1.4;
}
.signed-document-output .output-item strong {
    color: #0c341c;
}


.verification-result {
    margin-top: 30px;
    padding: 20px;
    border-radius: 8px;
    text-align: center;
    opacity: 0;
    transform: translateY(20px);
    transition: opacity var(--animation-duration) ease-out, transform var(--animation-duration) ease-out;
}
.verification-result.show {
    opacity: 1;
    transform: translateY(0);
}


.result-message {
    font-size: 1.3em;
    font-weight: bold;
    margin: 0;
}

.verification-result.success {
    border: 2px solid var(--secondary-color); /* Green */
    background-color: #d4edda; /* Light green */
    color: #155724; /* Dark green */
}

.verification-result.failure {
    border: 2px solid var(--danger-color); /* Red */
    background-color: #f8d7da; /* Light red */
    color: #721c24; /* Dark red */
}

/* Hide sections initially using max-height and overflow for smooth reveal */
/* This allows content within to be hidden and then revealed by changing max-height/opacity/visibility */
.process-flow:not(.show),
.signed-document-output:not(.show),
#verification-section:not(.show),
.verification-result:not(.show) {
    visibility: hidden;
    max-height: 0;
    overflow: hidden;
    opacity: 0;
    padding-top: 0;
    padding-bottom: 0;
    margin-top: 0;
    margin-bottom: 0;
    transition: visibility 0s linear var(--animation-duration), max-height var(--animation-duration) ease-out, opacity var(--animation-duration) ease-out, padding var(--animation-duration) ease-out, margin var(--animation-duration) ease-out;
}

.process-flow.show,
.signed-document-output.show,
#verification-section.show,
.verification-result.show {
     visibility: visible;
     max-height: 1000px; /* Sufficiently large value */
     overflow: visible; /* Allow content to be visible */
     opacity: 1;
     padding: initial; /* Restore original padding/margin */
     margin: initial;
     transition-delay: 0s;
     transition: visibility 0s linear 0s, max-height var(--animation-duration) ease-out, opacity var(--animation-duration) ease-out, padding var(--animation-duration) ease-out, margin var(--animation-duration) ease-out;
}


.explanation-toggle {
    display: block;
    width: fit-content;
    margin: 30px auto 20px auto;
    background-color: #6c757d; /* Grey */
    padding: 10px 20px;
    border: none;
    border-radius: 6px;
    color: white;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease;
}
.explanation-toggle:hover {
    background-color: #5a6268;
}

.explanation-content {
    background-color: #e9ecef; /* Light grey */
    padding: 25px;
    border-radius: 8px;
    margin-top: 20px;
    display: none; /* Initially hidden */
    direction: rtl;
    text-align: right;
    color: var(--dark-text);
}

.explanation-content h3 {
    text-align: right;
    color: #495057;
    border-bottom: 1px solid #ced4da;
    padding-bottom: 8px;
    margin-top: 15px;
    font-size: 1.3em;
}

.explanation-content ul {
    list-style-type: disc;
    padding-right: 25px;
}

.explanation-content li {
    margin-bottom: 12px;
    line-height: 1.6;
}

.explanation-content p {
     line-height: 1.6;
     margin-bottom: 15px;
}

</style>

<button class="explanation-toggle" id="toggle-explanation">הצג הסבר מעמיק על חתימות דיגיטליות</button>

<div class="explanation-content" id="explanation">
    <h3>מהי חתימה דיגיטלית? מעבר לסימולציה</h3>
    <p>חתימה דיגיטלית היא הרבה יותר מ"הקלדת שם" דיגיטלית. זוהי טכניקה קריפטוגרפית מתוחכמת המשתמשת במתמטיקה כדי לקשר מסמך דיגיטלי לזהות ספציפית ולהבטיח שאף אחד לא שינה אותו מאז שהוא נחתם. חשבו על זה כעל "טביעת אצבע קריפטוגרפית" של המסמך, המוצפנת באמצעות "חותמת אישית סודית" של החותם.</p>

    <h3>למה זה חשוב? המטרות הקריטיות</h3>
    <ul>
        <li><strong>אימות מקוריות (Authenticity):</strong> האם המסמך באמת הגיע ממי שטוען ששלח אותו? החתימה הדיגיטלית מאשרת את זהות החותם בוודאות גבוהה.</li>
        <li><strong>שלמות (Integrity):</strong> האם המסמך שקיבלתי זהה לחלוטין למסמך שהחותם יצר? החתימה חושפת כל שינוי, ולו הקטן ביותר, שנעשה במסמך לאחר החתימה.</li>
        <li><strong>אי-התכחשות (Non-Repudiation):</strong> לאחר שהחותם יצר חתימה דיגיטלית תקפה על מסמך, קשה לו מאוד (ולמעשה, קריפטוגרפית, בלתי אפשרי) לטעון מאוחר יותר שהוא לא חתם עליו.</li>
    </ul>

    <h3>איך קסם האבטחה הזה קורה? עקרון הפעולה</h3>
    <p>הבסיס הוא <strong>קריפטוגרפיה במפתח ציבורי (קריפטוגרפיה א-סימטרית)</strong>. לכל משתמש שרוצה לחתום או לאמת יש זוג מפתחות ייחודיים:</p>
    <ul>
        <li><strong>מפתח פרטי (Private Key):</strong> הסוד השמור ביותר של החותם. משמש אך ורק ליצירת החתימה. כמו החותמת האישית שרק לכם יש.</li>
        <li><strong>מפתח ציבורי (Public Key):</strong> מפתח זה ניתן לפרסום לכל העולם. משמש אך ורק לאימות חתימה שנוצרה עם המפתח הפרטי התואם. כמו חותמת ציבורית שמאפשרת לכל אחד לבדוק שהחותמת האישית שלכם אכן תואמת.</li>
    </ul>

    <h3>פירוט התהליך: יצירה ואימות</h3>
    <p>כפי שראיתם בסימולציה, התהליך מתחלק לשני שלבים עיקריים:</p>
    <h4>יצירת החתימה (עושה זאת השולח):</h4>
    <ol>
        <li><strong>חישוב טביעת אצבע (Hash):</strong> המסמך כולו מוזן לפונקציית Hash חד-כיוונית (כמו SHA-256). הפונקציה "מעכלת" את המסמך ומייצרת מחרוזת קצרה וקבועה בגודלה, שהיא "טביעת האצבע הדיגיטלית" הייחודית של תוכן המסמך הזה. שינוי של תו אחד במסמך ישנה לחלוטין את טביעת האצבע הזו.</li>
        <li><strong>הצפנת טביעת האצבע עם המפתח הפרטי:</strong> החותם לוקח את טביעת האצבע שחישב ומצפין אותה באמצעות המפתח הפרטי שלו. הפלט של ההצפנה הזו הוא **החתימה הדיגיטלית**. שימו לב: מצפינים רק את טביעת האצבע הקצרה, לא את המסמך הגדול כולו.</li>
        <li><strong>שליחת המסמך והחתימה:</strong> השולח שולח למקבל את המסמך המקורי הגלוי יחד עם החתימה הדיגיטלית שנוצרה.</li>
    </ol>
    <h4>אימות החתימה (עושה זאת המקבל):</h4>
    <ol>
        <li><strong>קבלת המסמך והחתימה:</strong> המקבל מקבל את המסמך ואת החתימה הדיגיטלית שצורפה.</li>
        <li><strong>חישוב טביעת אצבע חדשה:</strong> המקבל מריץ את **המסמך שקיבל בפועל** דרך אותה פונקציית Hash ששימשה ליצירה, ומקבל "טביעת אצבע" חדשה למסמך (כפי שהוא קיים אצלו).</li>
        <li><strong>פענוח החתימה עם המפתח הציבורי:</strong> המקבל משתמש במפתח הציבורי של השולח (שלצורך העניין קיבל אותו בצורה מהימנה) כדי לפענח את החתימה הדיגיטלית שקיבל. אם המפתח הציבורי אכן תואם למפתח הפרטי ששימש להצפנה, הפענוח יחשוף את **טביעת האצבע המקורית** שהשולח חישב וחתם עליה.</li>
        <li><strong>השוואת טביעות האצבע:</strong> השלב המכריע! המקבל משווה בין טביעת האצבע החדשה שחישב מהמסמך שקיבל, לבין טביעת האצבע המקורית שחילץ על ידי פענוח החתימה.</li>
    </ol>

    <h3>מה התוצאה מספרת לנו?</h3>
    <ul>
        <li><strong>התאמה מלאה! (אימות הצליח):</strong> זהו רגע האמת. אם שתי טביעות האצבע זהות, אנו יכולים להיות בטוחים בשני דברים: <strong>שלמות</strong> - תוכן המסמך לא השתנה כלל מאז החתימה (כי טביעת האצבע המחושבת תואמת את זו שהחותם יצר), ו<strong>מקוריות</strong> - החתימה אכן נוצרה על ידי בעל המפתח הפרטי התואם למפתח הציבורי ששימש לפענוח (כי רק מפתח פרטי ספציפי יכול לייצר חתימה שניתנת לפענוח ע"י המפתח הציבורי הזוגי שלו).</li>
        <li><strong>אי התאמה! (אימות נכשל):</strong> אם טביעות האצבע שונות, סימן שמשהו אינו כשורה. או שהמסמך שונה (לו בסימן אחד!) לאחר החתימה, או שהחתימה עצמה אינה תקפה (למשל, היא מזויפת, נוצרה עם מפתח אחר, או נפגמה). במקרה כזה, המסמך אינו נחשב מקורי או אמין.</li>
    </ul>

    <h3>ולבסוף - רשויות אישורים (CA)</h3>
    <p>עכשיו אתם מבינים שהאימות עובד רק אם אתם בטוחים שהמפתח הציבורי בו השתמשתם שייך באמת לאדם הנכון. כאן נכנסות לתמונה רשויות אישורים (Certificate Authorities - CAs). אלו גופים מהימנים שמנפיקים "תעודות דיגיטליות". תעודה כזו היא למעשה מסמך אלקטרוני שמקשר בין מפתח ציבורי לבין זהות ספציפית (שם של אדם, שם של חברה, שם של אתר אינטרנט), והיא עצמה חתומה דיגיטלית על ידי רשות האישורים. מערכות הפעלה ודפדפני אינטרנט מגיעים מראש עם רשימה של רשויות אישורים שהם "סומכים" עליהן. כך, כאשר אתם מאמתים מסמך או גולשים באתר מאובטח, אתם למעשה בודקים את חתימת רשות האישורים על התעודה הדיגיטלית כדי לוודא שהמפתח הציבורי אכן שייך לגורם הנכון, וזאת באמצעות שרשרת אמון.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    // Get elements
    const documentTextarea = document.getElementById('document-text');
    const signButton = document.getElementById('sign-button');
    const verifyButton = document.getElementById('verify-button');

    // Flow containers
    const signingFlowDiv = document.getElementById('signing-flow');
    const verificationFlowDiv = document.getElementById('verification-flow');
    const signedDocumentOutput = document.getElementById('signed-document-output');
    const verificationSection = document.getElementById('verification-section');
    const verificationResult = document.getElementById('verification-result');
    const resultMessage = document.getElementById('result-message');

    // Signing step displays
    const signingTextInputDisplay = document.getElementById('signing-text-input');
    const calculatedHashDisplay = document.getElementById('calculated-hash-display');
    const encryptedHashDisplay = document.getElementById('encrypted-hash-display');
    const digitalSignatureDisplay = document.getElementById('digital-signature-display');

    // Signed document output displays
    const outputTextDisplay = document.getElementById('output-text');
    const outputSignatureDisplay = document.getElementById('output-signature');

    // Verification step displays
    const verificationInputDisplay = document.getElementById('verification-input');
    const newCalculatedHashDisplay = document.getElementById('new-calculated-hash-display');
    const decryptedHashDisplay = document.getElementById('decrypted-hash-display');
    const hashComparisonDisplay = document.getElementById('hash-comparison-display');
    const compareNewHashDisplay = document.getElementById('compare-new');
    const compareOriginalHashDisplay = document.getElementById('compare-original');

    // Explanation toggle
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationContent = document.getElementById('explanation');

    // Store state
    let originalText = '';
    let originalHash = '';
    let digitalSignature = '';
    let isSigningProcessRunning = false;
    let isVerificationProcessRunning = false;


    // Simulate a simple hash function (NOT CRYPTOGRAPHICALLY SECURE)
    function simulateHash(text) {
        if (!text) return 'Hash: (ריק)';
        // A simple, non-cryptographic simulation for demonstration
        let hash = 0;
        for (let i = 0; i < text.length; i++) {
            const char = text.charCodeAt(i);
            hash = ((hash << 5) - hash) + char;
            hash = hash & hash; // Convert to 32bit integer
        }
        // Use a combination of length and a simple transformation
        const simpleHash = Math.abs(hash).toString(16).substring(0, 8);
        // Add a bit more complexity simulation
        const complexifier = text.length > 10 ? 'abc' : 'xyz';
        return `H-${text.length}-${simpleHash}-${complexifier}`;
    }

    // Simulate private key encryption (just wraps the hash)
    function simulateEncryptWithPrivateKey(hash) {
        if (!hash || hash === 'Hash: (ריק)') return 'חתימה: (ריק)';
        // Simulation: just a marker around the hash
        return `SIG[PK:${hash}:ENDSIG]`;
    }

    // Simulate public key decryption (just extracts the hash)
    function simulateDecryptWithPublicKey(signature) {
         if (!signature || signature === 'חתימה: (ריק)') return 'Hash שחולץ: (ריק)';
        // Simulation: extract the hash string from the simulated signature format
        const match = signature.match(/^SIG\[PK:(.*):ENDSIG\]$/);
        if (match && match[1]) {
            return match[1]; // Simulation: extract the hash string
        }
        return 'פענוח נכשל!'; // Simulate a decryption failure if format is wrong
    }

    // Function to hide and reset individual steps and arrows within a flow
     function resetFlowAnimation(flowElement) {
        if (!flowElement) return;
        flowElement.querySelectorAll('.flow-step, .flow-arrow, .result-box').forEach(el => {
            el.classList.remove('visible', 'active-step', 'match', 'mismatch');
             // Reset content placeholders if they are empty or default
             if (el.querySelector('.step-content')) {
                 const contentEl = el.querySelector('.step-content');
                 if (contentEl.textContent === '...' || contentEl.textContent.includes('(ריק)')) {
                    // Optional: Reset specific known elements based on ID if needed
                    // For now, rely on the main logic setting content
                 }
             }
        });
         // Reset specific comparison spans
         compareNewHashDisplay.textContent = '...';
         compareOriginalHashDisplay.textContent = '...';
         hashComparisonDisplay.classList.remove('match', 'mismatch');
    }


    // Function to reset app state
    function resetApp() {
        originalText = '';
        originalHash = '';
        digitalSignature = '';

        documentTextarea.value = '';
        verifyButton.disabled = true;
        signButton.disabled = false; // Ensure sign is enabled

        // Hide all process/result containers smoothly
        signingFlowDiv.classList.remove('show');
        signedDocumentOutput.classList.remove('show');
        verificationSection.classList.remove('show');
        verificationFlowDiv.classList.remove('show');
        verificationResult.classList.remove('show');

         // Reset individual flow step animations immediately
        resetFlowAnimation(signingFlowDiv);
        resetFlowAnimation(verificationFlowDiv);


        // Reset display texts immediately
        signingTextInputDisplay.textContent = '...';
        calculatedHashDisplay.textContent = '...';
        encryptedHashDisplay.textContent = '...';
        digitalSignatureDisplay.textContent = '...';
        outputTextDisplay.textContent = '...';
        outputSignatureDisplay.textContent = '...';
        verificationInputDisplay.textContent = '...';
        newCalculatedHashDisplay.textContent = '...';
        decryptedHashDisplay.textContent = '...';
        resultMessage.textContent = '';
        verificationResult.className = 'verification-result'; // Remove success/failure classes

        isSigningProcessRunning = false;
        isVerificationProcessRunning = false;
    }

    // Initial state setup
    resetApp();

    // Animation utility function for sequence
    function animateStepsSequentially(steps, arrows, elementContents, resultElement, callback = () => {}) {
        let delay = 0;
        const stepDelay = varToMs('--animation-delay-step');
        const stepDuration = varToMs('--animation-duration');

        steps.forEach((step, index) => {
            setTimeout(() => {
                // Hide previous active step indicator
                if (index > 0) steps[index - 1].classList.remove('active-step');
                // Show current step and make it active
                step.classList.add('visible', 'active-step');
                // Update text content if provided
                if (elementContents && elementContents[index] !== undefined) {
                    step.querySelector('.step-content').textContent = elementContents[index];
                }

                // Show arrow AFTER the step appears, if it's not the last step
                if (index < arrows.length) {
                     // Small delay for arrow to appear after step content updates
                     setTimeout(() => {
                          arrows[index].classList.add('visible');
                     }, stepDuration * 0.5); // Half duration delay after step starts showing
                }

                // Special handling for the last step/result
                if (index === steps.length - 1 && resultElement) {
                     setTimeout(() => {
                         steps[index].classList.remove('active-step'); // Remove active state from last step
                         resultElement.classList.add('visible'); // Make result box visible with its own animation
                         // The container (.signed-document-output or .verification-result) is shown separately
                         // The result message text and class (.success/.failure) will be set by the caller
                         callback(); // Execute callback after the last step/result animates
                     }, stepDuration); // Wait for the last step's visibility transition
                } else if (index === steps.length - 1 && !resultElement) {
                    // Case where the last step is not a dedicated result box, just remove active
                     setTimeout(() => {
                         steps[index].classList.remove('active-step');
                          callback(); // Execute callback after the last step animates
                     }, stepDuration);
                }

            }, delay);
            delay += stepDelay; // Increase delay for the next step
        });
         // If steps is empty or callback needs to run after all steps, call it after total delay
         if (steps.length === 0) {
             setTimeout(callback, delay);
         }
    }

    // Helper to convert CSS var time (e.g., '0.4s') to milliseconds
    function varToMs(varName) {
        const style = getComputedStyle(document.documentElement);
        const value = style.getPropertyValue(varName).trim();
        if (value.endsWith('ms')) {
            return parseFloat(value);
        } else if (value.endsWith('s')) {
            return parseFloat(value) * 1000;
        }
        return 0; // Default
    }


    // Event Listener for Sign Button
    signButton.addEventListener('click', async () => {
        if (isSigningProcessRunning) return;
        isSigningProcessRunning = true;
        signButton.disabled = true;
        verifyButton.disabled = true; // Disable verify while signing

        originalText = documentTextarea.value;
        if (!originalText.trim()) {
            alert('אנא הכנס טקסט למסמך לפני החתימה.');
             isSigningProcessRunning = false;
             signButton.disabled = false;
            return;
        }

        // Reset verification section and previous signing flow animations
        verificationSection.classList.remove('show');
        verificationFlowDiv.classList.remove('show');
        verificationResult.classList.remove('show');
        resetFlowAnimation(verificationFlowDiv);
        resetFlowAnimation(signingFlowDiv);


        // Show signing process area containers smoothly
        signingFlowDiv.classList.add('show');
        // signedDocumentOutput will be shown after process animation

        // Get flow elements for animation
        const signingSteps = Array.from(signingFlowDiv.querySelectorAll('.flow-step, .result-box'));
        const signingArrows = Array.from(signingFlowDiv.querySelectorAll('.flow-arrow'));

        // Prepare content for steps
        originalHash = simulateHash(originalText);
        digitalSignature = simulateEncryptWithPrivateKey(originalHash);

        const stepContents = [
            originalText,           // Step 1: Document Text
            originalHash,           // Step 2: Calculated Hash
            digitalSignature,       // Step 3: Encrypted Hash (Signature)
            digitalSignature        // Step 4: Digital Signature Result
        ];

        // Animate steps sequentially
        animateStepsSequentially(signingSteps, signingArrows, stepContents, digitalSignatureDisplay.closest('.result-box'), () => {
             // Callback after signing flow animation finishes

             // Display signed document output block and enable verification
             outputTextDisplay.textContent = originalText;
             outputSignatureDisplay.textContent = digitalSignature;
             signedDocumentOutput.classList.add('show'); // Show output block

             verificationSection.classList.add('show'); // Show verification section container
             verifyButton.disabled = false; // Enable verification button
             signButton.disabled = false; // Re-enable sign button
             isSigningProcessRunning = false;

             // Prepare verification input display with current values
             verificationInputDisplay.textContent = `טקסט: "${originalText.substring(0, 50) + (originalText.length > 50 ? '...' : '')}" | חתימה: "${digitalSignature.substring(0, 50) + (digitalSignature.length > 50 ? '...' : '')}"`;
             // The text area content is implicitly the "received" text for verification
        });

    });

    // Event Listener for Verify Button
    verifyButton.addEventListener('click', async () => {
        if (isVerificationProcessRunning) return;
        isVerificationProcessRunning = true;
        verifyButton.disabled = true;
        signButton.disabled = true; // Disable sign while verifying

        const receivedText = documentTextarea.value;
        const receivedSignature = digitalSignature; // Use the stored signature from signing

        if (!receivedText.trim() || !receivedSignature || receivedSignature === 'חתימה: (ריק)') {
            alert('אין מסמך חתום לאימות. אנא חתום על מסמך קודם.');
             isVerificationProcessRunning = false;
             verifyButton.disabled = false;
             signButton.disabled = false;
            return;
        }

        // Reset previous verification flow animations
        verificationResult.classList.remove('show', 'success', 'failure');
        resetFlowAnimation(verificationFlowDiv);
         resultMessage.textContent = '...';
         hashComparisonDisplay.classList.remove('match', 'mismatch');


        // Show verification process container smoothly
        verificationFlowDiv.classList.add('show');
        // verificationResult will be shown after process animation

        // Get flow elements for animation
        const verificationSteps = Array.from(verificationFlowDiv.querySelectorAll('.flow-step, .result-box'));
        const verificationArrows = Array.from(verificationFlowDiv.querySelectorAll('.flow-arrow'));

        // Note: Steps 3 & 4 (Calculate New Hash and Decrypt) happen in parallel visually (group)
        // Step 1: Input (already set above)
        setTimeout(() => {
            verificationSteps[0].classList.add('visible', 'active-step');
             // Add a small delay before next arrow
             setTimeout(() => {
                verificationSteps[0].classList.remove('active-step'); // Remove active class
                 verificationArrows[0].classList.add('visible'); // Arrow down
             }, varToMs('--animation-duration'));

        }, varToMs('--animation-delay-step')); // Initial delay for first step

        // Step 2 & 3 (Group: Calculate Hash & Decrypt)
        setTimeout(() => {
            const group = verificationFlowDiv.querySelector('.flow-step-group');
            if (group) {
                 const newHashStep = group.querySelector('.flow-step:first-child');
                 const decryptStep = group.querySelector('.flow-step:last-child');
                 const sideArrow = group.querySelector('.flow-arrow.side');

                // Calculate New Hash (Left side of group in RTL visual)
                const newHash = simulateHash(receivedText);
                newCalculatedHashDisplay.textContent = newHash;
                compareNewHashDisplay.textContent = newHash; // Update comparison area early
                newHashStep.classList.add('visible', 'active-step');


                 // Decrypt Signature (Right side of group in RTL visual)
                const extractedHash = simulateDecryptWithPublicKey(receivedSignature);
                decryptedHashDisplay.textContent = extractedHash;
                compareOriginalHashDisplay.textContent = extractedHash; // Update comparison area early


                // Animate decrypt step and side arrow shortly after new hash step appears
                setTimeout(() => {
                     decryptStep.classList.add('visible', 'active-step');
                     sideArrow.classList.add('visible');
                 }, varToMs('--animation-delay-step') * 0.8); // Slightly faster delay

                 // Remove active state after group animation finishes
                 setTimeout(() => {
                     newHashStep.classList.remove('active-step');
                     decryptStep.classList.remove('active-step');
                     // Show arrow after group
                     verificationArrows[1].classList.add('visible'); // Arrow after group
                 }, varToMs('--animation-delay-step') + varToMs('--animation-duration')); // Wait for both steps + their animation
            }
        }, varToMs('--animation-delay-step') * 2); // Delay for group after first step + arrow

        // Step 4: Compare Hashes and show result
        setTimeout(() => {
            const compareBox = verificationFlowDiv.querySelector('.compare-box');
            if(compareBox) {
                compareBox.classList.add('visible', 'active-step'); // Show comparison box and make active

                // Retrieve hashes for comparison
                const newHash = compareNewHashDisplay.textContent; // Get current displayed values
                const extractedHash = compareOriginalHashDisplay.textContent;

                // Update comparison box appearance based on result
                let comparisonResult = false;
                if (newHash && extractedHash && newHash === extractedHash) {
                    compareBox.classList.add('match');
                    comparisonResult = true;
                } else {
                    compareBox.classList.add('mismatch');
                }

                // Display final result message after a short delay
                setTimeout(() => {
                    compareBox.classList.remove('active-step'); // Remove active state
                    verificationResult.classList.add('show', comparisonResult ? 'success' : 'failure');
                    resultMessage.textContent = comparisonResult
                        ? '✅ אימות הצליח! המסמך לא שונה והחתימה תקפה.'
                        : '❌ אימות נכשל! המסמך שונה או שהחתימה אינה תקפה.';

                     isVerificationProcessRunning = false;
                     verifyButton.disabled = false; // Re-enable buttons
                     signButton.disabled = false;

                }, varToMs('--animation-duration')); // Wait for comparison box to become visible
            } else {
                 // Fallback if comparison box not found
                 isVerificationProcessRunning = false;
                 verifyButton.disabled = false;
                 signButton.disabled = false;
            }
        }, varToMs('--animation-delay-step') * 3.5); // Delay after group arrow

    });

    // Event Listener for Explanation Toggle
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
        if (isHidden) {
            explanationContent.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר הסבר מעמיק';
        } else {
            explanationContent.style.display = 'none';
            toggleExplanationButton.textContent = 'הצג הסבר מעמיק על חתימות דיגיטליות';
        }
    });

     // --- Initial setup: hide verification section and signed output ---
     // These are handled by the CSS :not(.show) rule and resetApp function
     // Ensure verification button is disabled on load
     verifyButton.disabled = true;
     signButton.disabled = false;
     // --- End Initial setup ---

});
</script>
```