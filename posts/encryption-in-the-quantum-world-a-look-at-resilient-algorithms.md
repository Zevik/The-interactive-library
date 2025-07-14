---
title: "הצפנה בעולם הקוונטי: הצצה לאלגוריתמים עמידים"
english_slug: encryption-in-the-quantum-world-a-look-at-resilient-algorithms
category: "מדעי המחשב"
tags:
  - הצפנה
  - קריפטוגרפיה
  - מחשוב קוונטי
  - אבטחת מידע
  - פוסט-קוונטי
---
# הצפנה בעולם הקוונטי: הצצה לאלגוריתמים עמידים

מה יקרה כשהמחשב הקוונטי יהפוך למציאות ויכולתו לבצע חישובים מורכבים בקלות תאיים על פרוטוקולי ההצפנה הנוכחיים? האם יש לנו כבר פתרונות הצפנה חדשים שיכולים לעמוד בפני האיום הקוונטי? בואו נגלה כיצד פועלים האלגוריתמים המבטיחים את אבטחת המידע בעידן הפוסט-קוונטי.

<div class="interactive-app">
    <h2 class="app-title">סימולציה קונספטואלית: מסע לתוך הצפנה פוסט-קוונטית (מבוססת סריגים)</h2>
    <p class="app-description">הדמיה זו מציגה בצורה מופשטת מאוד את הרעיון מאחורי אלגוריתם הצפנה פוסט-קוונטי מבוסס סריגים. **שימו לב היטב**: זו אינה הצפנה אמיתית, אלא המחשה ויזואלית וקונספטואלית בלבד, שנועדה להראות את העקרונות הבסיסיים!</p>

    <div class="app-section key-generation-section">
        <h3>🔑 שלב 1: לידת המפתחות (ציבורי ופרטי)</h3>
        <p>בלב אלגוריתם מבוסס סריגים עומדת בעיה מתמטית קשה ביותר - למצוא "בסיס טוב" (מפתח פרטי) בתוך מבנה מורכב הנקרא סריג, כשמוצג רק "בסיס רע" (מפתח ציבורי) שלו. זה כמו למצוא את הדרך הקצרה ביותר במבוך ענק ללא מפה, אלא אם יש לך את המפתח הסודי!</p>
        
        <div class="visual-representation lattice-container">
            <div class="lattice-grid">
                <!-- Points will be dynamically generated and animated -->
            </div>
            <div class="lattice-info">
                <p><strong>הבעיה הקשה:</strong> לזהות דפוסים נסתרים או וקטורים קצרים בסריג כשהוא נראה "אקראי" או מורכב (מוצג כאוסף נקודות). עם המפתח הפרטי ("בסיס טוב"), הכל הופך ברור. בלעדיו (רק עם המפתח הציבורי), זו משימה בלתי אפשרית למחשבים קלאסיים, וגם קשה מאוד לקוונטיים.</p>
            </div>
        </div>

        <button id="generateKeysButton" class="action-button primary">צור מפתחות (קונספטואלי)</button>
        <div id="keys-output" class="output-area">
            <p><strong>מפתח ציבורי 🌎:</strong> <span id="publicKey">[... מחכה ליצירה ...]</span></p>
            <p><strong>מפתח פרטי 🔒:</strong> <span id="privateKey">[... מחכה ליצירה ...]</span></p>
             <div class="status-message" id="keyStatus"></div>
        </div>
    </div>

    <div class="app-section encryption-section">
        <h3>🔒 שלב 2: הצפנת ההודעה</h3>
        <p>עכשיו ניקח את ההודעה הסודית שלך, נערבב אותה היטב עם המפתח הציבורי וה"רעש" המתמטי מהסריג, כך שרק מי שמחזיק במפתח הפרטי יוכל להפריד את המרכיבים ולפענח.</p>
        <label for="messageInput">הודעה סודית (קצרה וקלאסית 😉):</label>
        <input type="text" id="messageInput" value="היי עולם קוונטי!" maxlength="50" placeholder="הזן הודעה להצפנה...">
        <button id="encryptButton" class="action-button">הצפן הודעה</button>
        
        <div id="encryption-process" class="process-animation">
            <div class="process-step original-message">הודעה מקורית</div>
            <div class="arrow">➔</div>
            <div class="process-step public-key">מפתח ציבורי + בעיית סריגים</div>
            <div class="arrow">➔</div>
            <div class="process-step animated-transform encryption-transform">הפיכה מוצפנת</div>
            <div class="arrow">➔</div>
            <div class="process-step ciphertext">טקסט מוצפן</div>
        </div>
         <div class="status-message" id="encryptStatus"></div>
        <p><strong>טקסט מוצפן 🤖:</strong> <span id="ciphertextOutput"></span></p>
    </div>

    <div class="app-section decryption-section">
        <h3>🔓 שלב 3: פענוח ההודעה</h3>
        <p>רק המקבל המיועד, שברשותו המפתח הפרטי הסודי ("הבסיס הטוב" לסריג), יכול להתיר את ה"רעש" ולחשוף את ההודעה המקורית מתוך הטקסט המוצפן שנראה חסר משמעות.</p>
        <button id="decryptButton" class="action-button">פענח טקסט מוצפן</button>
         <div id="decryption-process" class="process-animation">
            <div class="process-step ciphertext">טקסט מוצפן</div>
            <div class="arrow">➔</div>
            <div class="process-step private-key">מפתח פרטי</div>
            <div class="arrow">➔</div>
            <div class="process-step animated-transform reverse decryption-transform">הפיכה מפוענחת</div>
            <div class="arrow">➔</div>
            <div class="process-step original-message">הודעה מקורית</div>
        </div>
         <div class="status-message" id="decryptStatus"></div>
        <p><strong>הודעה מפוענחת ✨:</strong> <span id="plaintextOutput"></span></p>
    </div>

    <div class="app-section insight-section">
        <h3>💡 תובנה קוונטית (ולא רק!)</h3>
        <p>אלגוריתמים פוסט-קוונטיים, כמו אלו מבוססי הסריגים, עוברים מלהתבסס על בעיות מתמטיות "קלות" יחסית עבור מחשב קוונטי (כמו פירוק לגורמים ב-RSA) לבעיות מתמטיות שנותרות קשות גם עבור המחשבים הקוונטיים העתידיים ביותר שידועים לנו כיום. זהו שינוי פרדיגמה קריטי באבטחת המידע בעידן הקוונטי המתקרב.</p>
    </div>
</div>

<button id="toggleExplanation" class="toggle-button">הצג הסבר מפורט</button>

<div id="explanation">
    <h2>הסבר מפורט: הצפנה בעולם הפוסט-קוונטי</h2>

    <h3>מבוא: האיום הקוונטי על הצפנה קלאסית</h3>
    <p>הצפנה אסימטרית (עם מפתחות ציבוריים ופרטיים) כיום, כמו RSA ו-ECC, מהווה את עמוד השדרה של אבטחת המידע המודרנית - היא מאפשרת עסקאות מקוונות מאובטחות, חתימות דיגיטליות ותקשורת מוצפנת (SSL/TLS). חוזקם של אלגוריתמים אלו נשען על הקושי בפתרון בעיות מתמטיות מסוימות עבור מחשבים קלאסיים. למשל, RSA מבוססת על הקושי בפירוק מספרים גדולים לגורמים ראשוניים, ו-ECC מבוססת על הקושי בפתרון בעיית הלוגריתם הדיסקרטי על עקומים אליפטיים.</p>
    <p>מחשבים קוונטיים, בעלי יכולת לבצע חישובים במקביל על ידי שימוש בסופרפוזיציה וקשירה קוונטית, מאיימים לשבור את ההגנות הללו. אלגוריתם שור הקוונטי מסוגל לפתור את בעיות הפירוק לגורמים והלוגריתם הדיסקרטי ביעילות אקספוננציאלית יותר מאשר כל אלגוריתם קלאסי ידוע. משמעות הדבר היא שמחשב קוונטי גדול ויציב יוכל לפרק מפתחות RSA ו-ECC בזמן סביר, ובכך לחשוף מידע רגיש מוצפן ולזייף חתימות דיגיטליות.</p>
     <p>גם הצפנה סימטרית (עם מפתח יחיד), כמו AES, פגיעה במידה מסוימת לאלגוריתמים קוונטיים. אלגוריתם גרובר יכול לסייע בהאצת תהליך מציאת המפתח (במקום לחפש את כל המרחב), אך ההאצה היא ריבועית בלבד, ולא אקספוננציאלית כמו אצל שור. לכן, ניתן להגן על הצפנה סימטרית על ידי הגדלת אורך המפתח (למשל, מ-128 ל-256 ביטים), בעוד שהצפנה אסימטרית מבוססת מספרים ראשוניים ועקומים אליפטיים נשארת בסכנה חמורה.</p>

    <h3>מהי קריפטוגרפיה פוסט-קוונטית (PQC)?</h3>
    <p>קריפטוגרפיה פוסט-קוונטית (Post-Quantum Cryptography - PQC), המכונה גם קריפטוגרפיה עמידה-קוונטית (Quantum-Resistant Cryptography), היא תחום מחקר ופיתוח המתמקד ביצירת אלגוריתמים קריפטוגרפיים (הצפנה, חתימות דיגיטליות וכו') שיהיו בטוחים מפני התקפות הן ממחשבים קלאסיים והן ממחשבים קוונטיים עתידיים.</p>
    <p>המטרה אינה להשתמש בעקרונות קוונטיים לצורך הצפנה (זהו תחום הקריפטוגרפיה הקוונטית, כמו הפצת מפתח קוונטי - QKD), אלא לפתח אלגוריתמים קלאסיים לחלוטין שפועלים על מחשבים קלאסיים, אך מבוססים על בעיות מתמטיות חדשות, השונות מאלו שנפתרות ביעילות על ידי אלגוריתם שור או גרובר.</p>
    <p>הצורך באלגוריתמי PQC הוא קריטי. תוקף עתידי עם מחשב קוונטי יוכל לא רק לפרוץ תקשורת בזמן אמת, אלא גם לפענח מידע שהוצפן היום ואוחסן ('harvest now, decrypt later'). תהליך המעבר לאלגוריתמים חדשים הוא מורכב וארוך, ולכן נדרש להתחיל אותו הרבה לפני שמחשבים קוונטיים בקנה מידה גדול יהפכו למציאות.</p>

    <h3>סקירה של משפחות אלגוריתמים פוסט-קוונטיים עיקריות:</h3>
    <p>קהילת הקריפטוגרפיה העולמית חוקרת מספר גישות עיקריות ליצירת אלגוריתמי PQC:</p>
    <ul>
        <li><strong>הצפנה מבוססת סריגים (Lattice-based Cryptography):</strong> מבוססת על בעיות מתמטיות הקשורות למציאת וקטורים קצרים ברשתות נקודות הנקראות סריגים. דוגמאות לבעיות כוללות את Shortest Vector Problem (SVP), Closest Vector Problem (CVP), ובגרסאות מופשטות יותר כמו Learning With Errors (LWE) ו-Short Integer Solution (SIS). אלגוריתמים ממשפחה זו (כמו CRYSTALS-Kyber להצפנה/החלפת מפתח ו-CRYSTALS-Dilithium לחתימות) נחשבים למבטיחים במיוחד בשל יעילותם היחסית וגודל המפתחות הסביר. המודל הפשטני שהודגם באפליקציה למעלה מבוסס באופן קונספטואלי על רעיון זה.</li>
        <li><strong>הצפנה מבוססת Hash (Hash-based Cryptography):</strong> משמשת בעיקר לחתימות דיגיטליות (כמו Lamport, Merkle Signature Scheme - MSS, XMSS, LMS). מבוססת על הביטחון של פונקציות גיבוב (Hash Functions) קריפטוגרפיות, שנחשבות עמידות יחסית לאלגוריתם גרובר. אלגוריתמים אלו מציעים ביטחון מוכח היטב, אך סובלים בדרך כלל מגודל חתימה גדול או דורשים ניהול מצב (stateful).</li>
        <li><strong>הצפנה מבוססת קודים (Code-based Cryptography):</strong> מבוססת על התיאוריה של קודים לתיקון שגיאות, בפרט קודים אקראיים לינאריים (כמו במערכת McEliece המקורית). הבעיה המתמטית הבסיסית היא פענוח קוד לינארי אקראי בנוכחות שגיאות. אלגוריתמים ממשפחה זו מציעים ביטחון גבוה מאוד, אך סובלים בדרך כלל מגודל מפתח ציבורי גדול מאוד.</li>
        <li><strong>משפחות נוספות:</strong>
            <ul>
                <li><strong>הצפנה מבוססת רב-משתנים (Multivariate Cryptography):</strong> מבוססת על קושי בפתרון מערכות משוואות פולינומיות רבות-משתנים מעל שדות סופיים. אלגוריתמים אלו מהירים לחתימות, אך חלקם הוכחו כפגיעים להתקפות.</li>
                <li><strong>הצפנה מבוססת איזוגניות עקומים אליפטיים (Isogeny-based Cryptography):</strong> מבוססת על קושי במציאת מסלול איזוגניות ספציפי בין עקומים אליפטיים. מציעה גודל מפתח קטן יחסית, אך פחות יעילה מבחינה חישובית ונדרש מחקר נוסף על התקפות פוטנציאליות.</li>
            </ul>
        </li>
    </ul>

    <h3>מדוע אלגוריתמים אלו עמידים?</h3>
    <p>האלגוריתמים הפוסט-קוונטיים נחשבים עמידים בפני התקפות קוונטיות (והתקפות קלאסיות כאחד) מכיוון שהם מבוססים על בעיות מתמטיות שלגביהן לא ידועים אלגוריתמים קוונטיים יעילים (כמו שור או גרובר) המסוגלים לפתור אותן בקנה מידה גדול. בעיות כמו SVP/CVP בסריגים, פענוח קודים אקראיים, או פתרון מערכות משוואות רב-משתנים, נחשבות "קשות" גם בעולם הקוונטי על סמך הידע הנוכחי.</p>

    <h3>תהליך הסטנדרטיזציה של אלגוריתמים פוסט-קוונטיים (NIST)</h3>
    <p>המכון הלאומי לתקנים וטכנולוגיה (NIST) בארה"ב הוביל תהליך סטנדרטיזציה גלובלי לבחירת הדור הבא של אלגוריתמי PQC. התהליך החל בשנת 2016 וכלל מספר סבבים של הגשות, ניתוח ובחינה של אלגוריתמים מכל העולם על ידי קהילת המחקר. בסבבים הראשונים נבחנו עשרות הצעות, והתהליך צמצם אותן בהדרגה. ביולי 2022, NIST הכריז על האלגוריתמים הראשונים שנבחרו לסטנדרטיזציה (כמו CRYSTALS-Kyber להקמת מפתח/הצפנה ו-CRYSTALS-Dilithium לחתימות), והמשיך לבחון מועמדים נוספים בסבבים מאוחרים יותר.</p>
    <p>תהליך הסטנדרטיזציה קריטי לאימוץ רחב של PQC על ידי התעשייה והממשלות, ומספק תשתית אמינה למעבר.</p>

    <h3>אתגרים ושיקולים בפריסת PQC בעולם האמיתי</h3>
    <p>המעבר לאלגוריתמי PQC אינו פשוט וכולל אתגרים רבים:</p>
    <ul>
        <li><strong>גודל מפתחות וחתימות:</strong> חלק מאלגוריתמי ה-PQC המבטיחים (במיוחד מבוססי סריגים וקודים) דורשים מפתחות ציבוריים או חתימות גדולים משמעותית מאלו של RSA או ECC. זה משפיע על רוחב פס, אחסון וביצועים.</li>
        <li><strong>יעילות חישובית:</strong> חלק מהאלגוריתמים פחות יעילים חישובית מאלגוריתמים קלאסיים עבור אותה רמת אבטחה.</li>
        <li><strong>הטמעה מאובטחת:</strong> יש לוודא שהאלגוריתמים מוטמעים בצורה נכונה ובטוחה בחומרה ובתוכנה, כולל הגנה מפני התקפות ערוץ צדדי (Side-channel attacks).</li>
        <li><strong>תאימות:</strong> יש לשלב את האלגוריתמים החדשים במערכות קיימות, פרוטוקולים (כמו TLS), ותקנים. זהו תהליך איטרטיבי וארוך.</li>
        <li><strong>מעבר "היברידי":</strong> כשלב ביניים, ארגונים עשויים להשתמש בגישה היברידית המשלבת הגנה קלאסית (RSA/ECC) יחד עם PQC חדש כדי להבטיח ביטחון כפול עד שהטכנולוגיה החדשה תהפוך לבשלה ומאומצת באופן נרחב.</li>
    </ul>

    <h3>הסבר על המודל הקונספטואלי המוצג באפליקציה</h3>
    <p>הסימולציה למעלה מדגימה בצורה מופשטת מאוד את הרעיון מאחורי הצפנה אסימטרית מבוססת סריגים, בפרט את הקונספט של שימוש בבעיה מתמטית קשה ("מציאת הוקטור הקצר ביותר בסריג") לבניית מערכת מפתחות. במציאות, סריגים הם מבנים מתמטיים מורכבים בממדים גבוהים מאוד (מאות או אלפי ממדים!). מפתחות ההצפנה אינם מחרוזות טקסט פשוטות אלא מטריצות או וקטורים גדולים, ותהליכי ההצפנה והפענוח כוללים פעולות אלגברה לינארית מורכבות בהרבה.</p>
    <p>ההדמיה נועדה להעביר את התובנה העיקרית באופן ויזואלי: אלגוריתמי PQC עוברים מבעיות "קלות לקוונטים" (כמו פירוק לגורמים) לבעיות "קשות גם לקוונטים" (כמו בעיות סריגים). השלבים (יצירת מפתחות, הצפנה עם ציבורי, פענוח עם פרטי) דומים מבחינה רעיונית לאלגוריתמים קלאסיים, אך המתמטיקה שמאחוריהם שונה באופן יסודי, והיא זו שמקנה להם את העמידות הקוונטית.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const generateKeysButton = document.getElementById('generateKeysButton');
        const messageInput = document.getElementById('messageInput');
        const encryptButton = document.getElementById('encryptButton');
        const decryptButton = document.getElementById('decryptButton');
        const publicKeySpan = document.getElementById('publicKey');
        const privateKeySpan = document.getElementById('privateKey');
        const ciphertextOutputSpan = document.getElementById('ciphertextOutput');
        const plaintextOutputSpan = document.getElementById('plaintextOutput');
        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationButton = document.getElementById('toggleExplanation');
        const encryptionProcessDiv = document.getElementById('encryption-process');
        const decryptionProcessDiv = document.getElementById('decryption-process');
        const latticeGridDiv = document.querySelector('.lattice-grid');
        const keyStatusDiv = document.getElementById('keyStatus');
        const encryptStatusDiv = document.getElementById('encryptStatus');
        const decryptStatusDiv = document.getElementById('decryptStatus');

        let publicKey = '';
        let privateKey = '';
        let currentCiphertext = '';
        let currentMessage = ''; // Store the message that was encrypted

        // --- Helper Functions ---
        function showStatus(element, message, isError = false) {
            element.textContent = message;
            element.className = isError ? 'status-message error' : 'status-message success';
             element.style.opacity = 1;
             element.style.height = 'auto'; // Allow height to adjust
             element.style.marginTop = '10px'; // Add space
             element.style.padding = '8px'; // Add padding
        }

        function clearStatus(element) {
             element.style.opacity = 0;
             element.style.height = '0'; // Collapse height
             element.style.marginTop = '0'; // Remove space
             element.style.padding = '0'; // Remove padding
            setTimeout(() => { element.textContent = ''; }, 300); // Clear text after transition
        }

        function animateLatticeGeneration() {
            latticeGridDiv.innerHTML = ''; // Clear previous points
            const numPoints = 30; // More points for better visualization
            const gridWidth = latticeGridDiv.offsetWidth;
            const gridHeight = latticeGridDiv.offsetHeight;

            for (let i = 0; i < numPoints; i++) {
                const point = document.createElement('div');
                point.classList.add('grid-point');
                // Initial random position
                const startX = Math.random() * gridWidth;
                const startY = Math.random() * gridHeight;
                // Target lattice-like position (conceptual)
                // We'll use a simple pattern for visualization, not a real lattice
                 const targetX = (i % 6) * (gridWidth / 7) + (gridWidth / 14);
                 const targetY = Math.floor(i / 6) * (gridHeight / 5) + (gridHeight / 10);

                point.style.left = `${startX}px`;
                point.style.top = `${startY}px`;
                point.style.opacity = 0; // Start hidden

                latticeGridDiv.appendChild(point);

                // Animate points moving into a rough grid formation
                setTimeout(() => {
                     point.style.left = `${targetX}px`;
                     point.style.top = `${targetY}px`;
                     point.style.opacity = 1;
                }, i * 30 + 200); // Staggered animation
            }
        }

         function animateLatticeTransform(isEncrypt) {
             const points = latticeGridDiv.querySelectorAll('.grid-point');
             points.forEach((point, index) => {
                 const randomOffsetX = (Math.random() - 0.5) * 40; // Random horizontal shift
                 const randomOffsetY = (Math.random() - 0.5) * 40; // Random vertical shift
                 const randomRotate = (Math.random() - 0.5) * 90; // Random rotation

                 // Apply transform relative to current position
                 const currentX = parseFloat(point.style.left);
                 const currentY = parseFloat(point.style.top);

                 // For encryption, move points away from their structured positions
                 // For decryption, attempt to move them back towards something regular (conceptually)
                 if (isEncrypt) {
                    point.style.transition = 'all 0.8s ease-in-out';
                    point.style.left = `${currentX + randomOffsetX}px`;
                    point.style.top = `${currentY + randomOffsetY}px`;
                     point.style.transform = `translate(-50%, -50%) rotate(${randomRotate}deg)`;
                 } else {
                     // For decryption, we don't have the original 'structured' positions easily.
                     // We can just reverse the animation conceptually, or apply a different 'unscrambling' feel.
                     // Let's just apply a different kind of subtle movement.
                      point.style.transition = 'all 0.8s ease-in-out';
                     // Attempt to move them back slightly towards the center area
                     const centerX = latticeGridDiv.offsetWidth / 2;
                     const centerY = latticeGridDiv.offsetHeight / 2;
                      const moveBackFactor = 0.5; // Move 50% back towards the center
                      const targetBackX = currentX + (centerX - currentX) * moveBackFactor + (Math.random() - 0.5) * 10; // Add small random jitter
                      const targetBackY = currentY + (centerY - currentY) * moveBackFactor + (Math.random() - 0.5) * 10;

                      point.style.left = `${targetBackX}px`;
                      point.style.top = `${targetBackY}px`;
                      point.style.transform = `translate(-50%, -50%) rotate(0deg)`; // Straighten them conceptually
                 }
             });
         }


        // --- Mock PQC Functions (Conceptual Only) ---

        // Simulate Key Generation (Abstract Lattice Problem)
        function generateKeys() {
            showStatus(keyStatusDiv, '... יוצר מפתחות על בסיס בעיית סריגים מורכבת ...');
             clearStatus(encryptStatusDiv);
             clearStatus(decryptStatusDiv);
            animateLatticeGeneration(); // Animate lattice appearance

            setTimeout(() => {
                // In a real PQC lattice scheme, this involves generating a "good basis" (private key)
                // and a "bad basis" or related matrix (public key) based on hard problems like LWE/SIS.
                // Here, we just generate abstract strings.
                publicKey = 'PQC_PubKey_' + Math.random().toString(36).substring(2, 8).toUpperCase();
                privateKey = 'PQC_PrivKey_' + Math.random().toString(36).substring(2, 8).toUpperCase();
                publicKeySpan.textContent = publicKey;
                privateKeySpan.textContent = privateKey;
                ciphertextOutputSpan.textContent = '';
                plaintextOutputSpan.textContent = '';
                currentCiphertext = '';
                currentMessage = '';
                showStatus(keyStatusDiv, '✅ מפתחות נוצרו בהצלחה!');
                console.log("Keys generated (mock):", { publicKey, privateKey });
                encryptButton.disabled = false; // Enable encryption after keys are made
                 decryptButton.disabled = true; // Disable decryption until encryption happens
            }, 1500); // Simulate generation time
        }

        // Simulate Encryption
        function encryptMessage(message, pubKey) {
            if (!pubKey || !privateKey) { // Check if keys exist
                showStatus(encryptStatusDiv, '❌ אנא צור מפתחות קודם!', true);
                return '';
            }
            if (!message) {
                 showStatus(encryptStatusDiv, '❌ אנא הזן הודעה להצפנה.', true);
                return '';
            }

            showStatus(encryptStatusDiv, `... מצפין הודעה "${message}" באמצעות מפתח ציבורי וטרנספורמציית סריג ...`);
            clearStatus(decryptStatusDiv);
             currentMessage = message; // Store message for conceptual decryption

            animateProcess(encryptionProcessDiv, () => {
                // Simulate transformation visually on the lattice
                 animateLatticeTransform(true); // Encrypt transform

                // In a real lattice scheme, this involves transforming the message (often encoded numerically)
                // using the public key and adding "controlled error" based on the hard problem.
                // Here, we just mix the message and key into a seemingly random string.
                // A slightly more complex mock cipher
                 let mockCipher = 'PQC_CIPHER(';
                for(let i = 0; i < message.length; i++) {
                    // Simple substitution + pseudo-random element from key
                     const charCode = message.charCodeAt(i);
                     const keyModifier = pubKey.charCodeAt(i % pubKey.length);
                     const transformedCode = (charCode + keyModifier) % 256; // Simple mock transformation
                     mockCipher += transformedCode.toString(16).padStart(2, '0');
                }
                 // Add a conceptual 'noise' or complexity factor based on the key part
                 mockCipher += '-' + pubKey.substring(5, 10);
                 mockCipher += ')';

                console.log("Mock Ciphertext:", mockCipher);
                currentCiphertext = mockCipher;
                ciphertextOutputSpan.textContent = currentCiphertext;
                plaintextOutputSpan.textContent = '[... עדיין מוצפן ...]'; // Clear previous decryption result
                showStatus(encryptStatusDiv, '✅ הודעה הוצפנה בהצלחה!', false);
                decryptButton.disabled = false; // Enable decryption
            });

            return currentCiphertext; // Return value synchronously, but update span asynchronously
        }

        // Simulate Decryption
        function decryptMessage(ciphertext, privKey, originalMessage) { // originalMessage is ONLY for conceptual demo
             if (!ciphertext) {
                showStatus(decryptStatusDiv, '❌ אין טקסט מוצפן לפענוח. הצפן הודעה קודם.', true);
                return '';
            }
             if (!privKey || !publicKey) { // Check if keys exist
                showStatus(decryptStatusDiv, '❌ מפתחות אינם זמינים. צור מפתחות קודם.', true);
                return '';
            }

            showStatus(decryptStatusDiv, '... מפענח טקסט מוצפן באמצעות מפתח פרטי והפיכה חזרה על הסריג ...');

             animateProcess(decryptionProcessDiv, () => {
                 // Simulate transformation visually on the lattice
                animateLatticeTransform(false); // Decrypt transform

                 // In a real lattice scheme, this involves using the private key (the "good basis")
                // to "round off" or remove the error added during encryption, recovering the original message.
                // Here, we just check if the key conceptually fits and return the original message (for demo purposes).
                // A real decryption algorithm doesn't need the original message as input.

                 // Simple check based on our mock encryption format and expected key part
                 // Check if the ciphertext ends with the public key part used in mock encryption
                 const expectedKeyPart = publicKey.substring(5, 10);
                 const cipherKeyPart = ciphertext.substring(ciphertext.lastIndexOf('-') + 1, ciphertext.length - 1);

                 if (ciphertext.startsWith('PQC_CIPHER(') && cipherKeyPart === expectedKeyPart) {
                      console.log("Mock Decryption Logic check passed.");
                      // In a real scenario, the decryption logic would reverse the transformation.
                      // In this mock, we simply reveal the original message stored from encryption.
                      // This is the *conceptual* outcome.
                     showStatus(decryptStatusDiv, '✅ פענוח הצליח! ההודעה המקורית שוחזרה.', false);
                     return currentMessage; // Return the stored original message
                 } else {
                     console.log("Mock Decryption Logic check failed (key mismatch or invalid ciphertext format).");
                     showStatus(decryptStatusDiv, '❌ פענוח נכשל. ודא שהשתמשת במפתחות הנכונים.', true);
                     return "[[ הודעה מפוענחת נכשלה ]] - מפתח שגוי או טקסט לא תקין";
                 }
             });
             // Return value synchronously, update span asynchronously in animateProcess callback
             return '[... מתבצע פענוח ...]'; // Placeholder while animation runs
        }

        // --- Animation Functions ---
        function animateProcess(processDiv, callback) {
             // Reset animation state
             processDiv.querySelectorAll('.process-step').forEach(el => {
                 el.classList.remove('active', 'completed');
                 el.style.transform = '';
                 el.style.opacity = '';
             });
             processDiv.querySelectorAll('.arrow').forEach(el => el.classList.remove('active'));

             const steps = processDiv.querySelectorAll('.process-step');
             const arrows = processDiv.querySelectorAll('.arrow');

             steps.forEach((step, index) => {
                 setTimeout(() => {
                     step.classList.add('active');
                     if (index > 0) {
                         arrows[index - 1].classList.add('active');
                     }
                     step.style.transform = 'scale(1.05)'; // Slightly enlarge current step
                     step.style.opacity = '1'; // Ensure visibility

                     if (index > 0) {
                          // Animate the previous step completing
                          steps[index - 1].classList.add('completed');
                          steps[index - 1].style.transform = 'scale(1)';
                           // Keep opacity high for completed steps
                     }

                     // Specific animation for the transform step
                     if (step.classList.contains('animated-transform')) {
                          step.style.transform = step.classList.contains('reverse') ? 'rotateY(360deg)' : 'rotateY(360deg)'; // Spin effect
                          step.style.backgroundColor = '#cceeff'; // Highlight transform step
                           setTimeout(() => {
                               step.style.backgroundColor = ''; // Revert highlight
                               step.style.transform = 'scale(1)'; // Revert scale after spin
                           }, 500);
                     }


                     if (index === steps.length - 1) {
                         // Last step completed
                         step.classList.add('completed');
                          step.style.transform = 'scale(1)';
                          setTimeout(() => {
                             // All steps done, execute callback
                             if (callback) callback();
                          }, 500); // Small delay after last step animation
                     }

                 }, index * 600); // Stagger animation start
             });
        }


        // --- Event Listeners ---

        generateKeysButton.addEventListener('click', generateKeys);

        encryptButton.addEventListener('click', () => {
            const message = messageInput.value;
            encryptMessage(message, publicKey);
        });

        decryptButton.addEventListener('click', () => {
            // We pass the original message here ONLY for the mock decryption *output*.
            // A real decrypt function would NOT take the original message as input.
            // The decryptMessage function handles the mock logic and updates outputSpan within its callback.
            const originalMessageValue = messageInput.value; // Get value *before* decrypt call
             const decryptedTextPlaceholder = decryptMessage(currentCiphertext, privateKey, originalMessageValue);
             if (decryptedTextPlaceholder !== '') { // Only update if decryption started
                 plaintextOutputSpan.textContent = decryptedTextPlaceholder;
             }
        });


        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מפורט' : 'הצג הסבר מפורט';
        });

        // Initial state setup
        explanationDiv.style.display = 'none'; // Hide explanation by default
        generateKeysButton.disabled = false; // Enable generate button initially
        encryptButton.disabled = true; // Disable encrypt until keys are made
        decryptButton.disabled = true; // Disable decrypt until encryption happens
         clearStatus(keyStatusDiv); // Hide status messages initially
         clearStatus(encryptStatusDiv);
         clearStatus(decryptStatusDiv);
         animateLatticeGeneration(); // Show initial lattice concept on load

    });
</script>

<style>
    /* General Body and RTL adjustments */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        direction: rtl; /* Hebrew direction */
        text-align: right; /* Align text to the right */
        margin: 0;
        padding: 20px;
        background-color: #eef2f7; /* Light subtle background */
    }

    h1, h2, h3 {
        color: #1a3a6d; /* Deep blue */
        text-align: center; /* Center headings */
         margin-bottom: 20px;
    }

     h1 {
         border-bottom: 2px solid #1a3a6d;
         padding-bottom: 10px;
     }


    /* Interactive App Styling */
    .interactive-app {
        margin: 30px auto; /* Center and add space */
        padding: 30px;
        background-color: #ffffff;
        border: 1px solid #d0d8e2;
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        max-width: 900px; /* Limit max width */
        direction: rtl;
        text-align: right;
    }

    .app-title {
        color: #0056b3; /* Medium blue */
        border-bottom: 2px solid #007bff;
        padding-bottom: 10px;
        margin-bottom: 25px;
        text-align: center;
        font-size: 1.8em;
    }

     .app-description {
         text-align: center;
         color: #555;
         margin-bottom: 30px;
         font-size: 1.1em;
     }

    .app-section {
        margin-bottom: 35px;
        padding: 20px;
        background-color: #f8f9fa; /* Light grey background */
        border: 1px solid #e9ecef;
        border-radius: 8px;
        transition: all 0.3s ease; /* Smooth transitions for hover/focus effects */
    }

     .app-section:hover {
         border-color: #007bff;
     }


    .app-section h3 {
        color: #007bff; /* Blue */
        border-bottom: 1px solid #007bff;
        padding-bottom: 8px;
        margin-bottom: 15px;
        font-size: 1.4em;
         display: flex; /* Align icon */
        align-items: center;
    }

     .app-section h3 i { /* Placeholder for potential icons */
         margin-left: 10px; /* Space between icon and text in RTL */
     }

    .app-section p {
        margin-bottom: 15px;
        color: #444;
    }

    label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        color: #555;
    }

    input[type="text"] {
        width: calc(100% - 130px); /* Adjust width considering button and padding */
        padding: 10px 12px;
        margin-left: 10px; /* Space between input and button */
        border: 1px solid #ced4da;
        border-radius: 5px;
        box-sizing: border-box;
        display: inline-block;
        font-size: 1em;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    input[type="text"]:focus {
        border-color: #007bff;
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.25);
        outline: none;
    }

    .action-button {
        padding: 10px 20px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        display: inline-block;
        vertical-align: top; /* Align with input */
        margin-top: 0; /* Remove potential extra space from display:block */
    }

    .action-button:hover {
        background-color: #0056b3;
    }

     .action-button:active {
         transform: scale(0.98);
     }

    .action-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
    }

    .output-area {
        margin-top: 20px;
        padding: 15px;
        background-color: #e9ecef;
        border: 1px solid #ced4da;
        border-radius: 5px;
    }

    .output-area p {
        margin: 8px 0;
        font-size: 1em;
        color: #343a40;
    }

    .output-area strong {
        color: #004085; /* Dark blue for labels */
    }

    #keys-output span,
    #ciphertextOutput,
    #plaintextOutput {
        font-family: 'Courier New', monospace;
        background-color: #dee2e6; /* Slightly darker background */
        padding: 3px 8px;
        border-radius: 4px;
        word-break: break-all;
        display: inline-block; /* Ensure padding/margin works */
        margin-right: 5px; /* Space after label */
        color: #495057; /* Dark grey for text */
    }

     .status-message {
         margin-top: 10px;
         padding: 8px;
         border-radius: 4px;
         font-size: 0.9em;
         transition: opacity 0.3s ease, height 0.3s ease, margin-top 0.3s ease, padding 0.3s ease;
         opacity: 0;
         height: 0;
         overflow: hidden;
         margin-top: 0;
         padding: 0;
     }

     .status-message.success {
         background-color: #d4edda;
         color: #155724;
         border: 1px solid #c3e6cb;
     }

     .status-message.error {
         background-color: #f8d7da;
         color: #721c24;
         border: 1px solid #f5c6cb;
     }


    /* Visual Representation - Lattice */
    .visual-representation {
        margin-top: 20px;
        margin-bottom: 25px;
        padding: 20px;
        background: linear-gradient(to bottom right, #e0f2f7, #cceeff); /* Gradient background */
        border: 2px dashed #007bff;
        border-radius: 10px;
        text-align: center;
        position: relative;
        overflow: hidden; /* Keep points inside */
    }

    .lattice-grid {
        position: relative;
        width: 90%; /* Make it wider */
        height: 200px; /* Increase height */
        margin: 0 auto;
        background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white */
        border: 1px solid #a0c4ff;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: inset 0 0 8px rgba(0, 123, 255, 0.1);
    }

    .grid-point {
        position: absolute;
        width: 8px; /* Larger points */
        height: 8px; /* Larger points */
        background-color: #007bff;
        border-radius: 50%;
        transform: translate(-50%, -50%); /* Center the point */
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.5); /* Add subtle glow */
        transition: all 0.8s ease-in-out; /* Smooth movement */
    }

    .lattice-info {
        margin-top: 15px;
        font-size: 0.9em;
        color: #333;
        font-style: italic;
    }

    /* Process Animation Styling */
    .process-animation {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 30px 0;
        flex-wrap: wrap;
        min-height: 50px; /* Ensure space even when empty */
    }

    .process-step {
        padding: 12px 18px;
        border: 1px solid #a0c4ff;
        border-radius: 20px; /* Pill shape */
        margin: 8px;
        background-color: #eaf4ff;
        font-size: 1em;
        font-weight: bold;
        color: #004085;
        transition: transform 0.5s cubic-bezier(0.68, -0.55, 0.27, 1.55), /* Pop effect */
                    opacity 0.5s ease-in-out,
                    background-color 0.3s ease;
        opacity: 0.6; /* Dim initially */
         transform: scale(1); /* Base scale */
    }

     .process-step.active {
         opacity: 1;
         background-color: #007bff;
         color: white;
          transform: scale(1.1); /* Pop effect on active */
     }

     .process-step.completed {
         opacity: 0.8;
         background-color: #cceeff; /* Lighter blue when completed */
         color: #0056b3;
          transform: scale(1); /* Return to normal size */
     }

     .process-step.animated-transform.active {
         background-color: #28a745; /* Green highlight during transform */
         color: white;
         /* Transform handled by JS for more control */
     }


     .arrow {
        font-size: 1.8em; /* Larger arrows */
        margin: 0 15px;
        color: #a0c4ff; /* Light blue arrows */
         transition: color 0.5s ease;
     }

     .arrow.active {
         color: #007bff; /* Blue arrows when active */
     }


    /* Explanation Section */
    .toggle-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        background-color: #6c757d;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    .toggle-button:hover {
        background-color: #5a6268;
    }
     .toggle-button:active {
         transform: scale(0.98);
     }


    #explanation {
        margin-top: 20px;
        padding: 30px;
        background-color: #ffffff;
        border: 1px solid #d0d8e2;
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        direction: rtl;
        text-align: right;
        max-width: 900px;
        margin: 20px auto; /* Center like the app */
        /* display: none; Will be handled by JS */
    }

    #explanation h2, #explanation h3 {
        color: #1a3a6d;
        border-bottom: 1px solid #e9ecef;
        padding-bottom: 8px;
        margin-bottom: 15px;
    }

    #explanation ul {
        list-style-type: disc;
        margin-right: 20px; /* Adjust for RTL */
        padding-right: 0; /* Reset default padding */
        margin-bottom: 15px;
    }

     #explanation li {
        margin-bottom: 10px;
         color: #444;
     }

     #explanation li strong {
         color: #1a3a6d;
     }

     /* Responsive adjustments */
     @media (max-width: 768px) {
         .interactive-app {
             padding: 20px;
         }
         .app-section {
             padding: 15px;
         }
          input[type="text"] {
             width: calc(100% - 100px);
             margin-bottom: 10px;
             display: block;
             margin-left: 0;
          }
          .action-button {
              display: block;
              width: 100%; /* Make button full width on small screens */
               margin-top: 10px;
          }
          .process-animation {
              flex-direction: column; /* Stack steps vertically */
              align-items: flex-start;
          }
          .process-step {
              margin: 5px 0; /* Adjust vertical margin */
              width: auto; /* Allow width to shrink */
          }
          .arrow {
               transform: rotate(90deg); /* Rotate arrow down */
               margin: 5px auto; /* Center vertical arrow */
          }
          .lattice-grid {
              width: 100%;
          }
     }

</style>
---
```