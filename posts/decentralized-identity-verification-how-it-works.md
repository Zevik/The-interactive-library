---
title: "אימות זהות מבוזר: מסע אישור (Verifiable Credential)"
english_slug: decentralized-identity-verification-how-it-works
category: "מדעי המחשב"
tags: זהות מבוזרת, DID, Verifiable Credentials, בלוקצ'יין, קריפטוגרפיה, Web3, SSI
---
# אימות זהות מבוזר: מסע אישור (Verifiable Credential)

האם ידעת שבעולם הדיגיטלי המתפתח, ניתן להוכיח שאתה בן 18 מבלי לחשוף את תאריך הלידה המדויק שלך, ואף מבלי שהגורם המאמת יצטרך לפנות לגורם המנפיק את התעודה המקורית? זהות מבוזרת (DID) ואישורים ניתנים לאימות (VC) מאפשרים בדיקת מידע אישי בצורה חדשנית: בטוחה יותר, שומרת פרטיות, ונמצאת בשליטתך המלאה!

<div id="did-verification-app" class="interactive-simulation">
    <div class="simulation-header">
        <h2>סימולציה: מסע אישור (Verifiable Credential)</h2>
        <p>היכנסו לנעלי ה"מאמת" (Verifier) ולוו אישור גיל בדרכו לאימות מלא.</p>
    </div>

    <div class="actors-container">
        <div class="actor-card" id="holder">
            <div class="actor-title">
                <span class="actor-icon">👤</span>
                <h3>מחזיק (Holder)</h3>
            </div>
            <div class="data-card vc-card" id="holder-vc">
                <div class="card-title">אישור גיל (VC)</div>
                <div class="card-content">
                    <div class="vc-representation">
                        <span class="icon">📄</span>
                        <span class="label">Proof of Age VC</span>
                    </div>
                </div>
                <p class="status" id="holder-status">מוכן לשליחה</p>
            </div>
             <button id="send-vc-from-holder" class="action-button">שלח אישור</button>
        </div>

        <div class="flow-arrow right-arrow vc-flow"></div>

        <div class="actor-card" id="verifier">
            <div class="actor-title">
                <span class="actor-icon">🏢</span>
                <h3>מאמת (Verifier)</h3>
            </div>
             <div class="data-card received-vc-card" id="verifier-vc">
                <div class="card-title">אישור שהתקבל</div>
                <div class="card-content placeholder">
                    <span class="icon">⏳</span>
                    <span class="label">ממתין לאישור...</span>
                </div>
                 <div class="card-content received-data" style="display: none;">
                     <div class="vc-representation">
                        <span class="icon">📄</span>
                        <span class="label">קיבל VC</span>
                     </div>
                     <p class="data-summary">מאת: [DID מנפיק]</p>
                 </div>
             </div>
             <div class="data-card received-did-doc-card" id="verifier-did-doc" style="display: none;">
                 <div class="card-title">מסמך DID</div>
                 <div class="card-content placeholder">
                     <span class="icon">⏳</span>
                     <span class="label">ממתין למסמך DID...</span>
                 </div>
                 <div class="card-content received-data" style="display: none;">
                      <div class="did-doc-representation">
                         <span class="icon">🔑</span>
                         <span class="label">DID Document</span>
                      </div>
                      <p class="data-summary">כולל מפתח ציבורי למנפיק</p>
                 </div>
             </div>
            <div class="actions">
                <button id="step1-receive-vc" class="action-button" disabled>1. קבל אישור (VC)</button>
                <button id="step2-request-did-doc" class="action-button" disabled>2. בקש מסמך DID</button>
                <button id="step3-verify-signature" class="action-button" disabled>3. אמת חתימה</button>
                <button id="step4-additional-checks" class="action-button" disabled>4. בדיקות נוספות</button>
            </div>
            <div class="verification-status">
                 <p class="current-step-text" id="explanation-text">לחץ על 'שלח אישור' (אצל המחזיק) כדי להתחיל!</p>
                 <div id="verification-result" class="result"></div>
            </div>
        </div>

        <div class="flow-arrow left-arrow did-flow"></div>

        <div class="actor-card" id="did-network">
            <div class="actor-title">
                <span class="actor-icon">🌐</span>
                <h3>רשת DID (DID Network)</h3>
            </div>
            <div class="data-card" id="did-network-data">
                <div class="card-title">מאגר מסמכי DID</div>
                <div class="card-content placeholder">
                    <span class="icon">📁</span>
                    <span class="label">ממתין לבקשה...</span>
                </div>
                 <div class="card-content received-data" style="display: none;">
                     <span class="icon">🔄</span>
                     <span class="label">מעבד בקשה...</span>
                 </div>
                 <div class="card-content processed-data" style="display: none;">
                      <span class="icon">✅</span>
                      <span class="label">מוצא מסמך DID</span>
                 </div>
            </div>
        </div>
    </div>

     <button id="reset-simulation" class="action-button reset-button">התחל מחדש</button>

</div>

<button id="toggle-explanation" class="toggle-button">הצג/הסתר הסבר מורחב</button>

<div id="full-explanation" class="explanation-section" style="display: none;">
    <h2>אימות זהות מבוזר: הסבר מעמיק</h2>

    <h3>העולם הדיגיטלי של היום: למה צריך שינוי?</h3>
    <p>במציאות הדיגיטלית שאנו חיים בה, הזהות שלנו מפוזרת בין אינספור גופים ריכוזיים: בנקים, חברות אשראי, רשתות חברתיות, משרדי ממשלה ועוד. כל אחד מהם מחזיק חלק מהמידע עלינו. מודל זה יוצר בעיות מהותיות:</p>
    <ul>
        <li>**סיכוני אבטחה:** ריכוז מידע רגיש הופך גופים אלו למטרות אטרקטיביות להאקרים (נקודות כשל יחידות). דליפת מידע בגוף אחד יכולה לחשוף מיליוני משתמשים.</li>
        <li>**פגיעה בפרטיות:** לעיתים קרובות אנו נדרשים לחשוף מידע רב יותר מהנדרש בפועל (למשל, להציג תעודת זהות מלאה כדי להוכיח גיל). אין לנו שליטה על מידע זה לאחר ששיתפנו אותו.</li>
        <li>**חוסר שליטה של המשתמש:** הנתונים שלנו אינם בבעלותנו האמיתית, אלא בבעלות החברות והגופים. קשה להעביר מידע זה בין שירותים או למחוק אותו.</li>
        <li>**מורכבות וחיכוך:** כל אינטראקציה דיגיטלית הדורשת הוכחת זהות (פתיחת חשבון, הגשת בקשה) כרוכה בתהליכים מסורבלים ובדיקות הדדיות בין גופים.</li>
    </ul>

    <h3>הבסיס: זהות מבוזרת (DID) ואישורים ניתנים לאימות (VC)</h3>
    <p>המערכת של זהות מבוזרת (Self-Sovereign Identity - SSI), שמיושמת באמצעות תקני W3C כמו Decentralized Identifiers (DIDs) ו-Verifiable Credentials (VCs), מציעה אלטרנטיבה רדיקלית. במקום שהזהות תשב אצל גורם מרכזי, היא מנוהלת על ידי המשתמש עצמו (או הישות - אדם, ארגון, מכשיר IoT).</p>
    <ul>
        <li>**DID (Decentralized Identifier):** מזהה ייחודי, גלובלי, ובעיקר - בשליטת המשתמש. ה-DID אינו קשור לאף ארגון מרכזי והוא עמיד בפני צנזורה. כל DID מקושר ל"מסמך DID".</li>
        <li>**DID Document:** מסמך פומבי (לרוב מאוחסן ברשת מבוזרת) שמכיל מידע חיוני לאינטראקציה עם ה-DID, ובראש ובראשונה: המפתחות הציבוריים המשמשים לאימות חתימות הקשורות ל-DID, וכן נקודות קצה לשירותים רלוונטיים (Endpoints).</li>
        <li>**VC (Verifiable Credential):** הצהרה (Claim) על נושא ספציפי (ה"מחזיק"), שחתום דיגיטלית על ידי "מנפיק" מהימן. לדוגמה: תעודת בגרות, רישיון נהיגה, אישור עבודה, או במקרה שלנו - אישור גיל מעל 18. ה-VC עצמו אינו מכיל את כל המידע עליך, אלא רק את הטענה הרלוונטית, והוא מקושר ל-DID של המחזיק ול-DID של המנפיק.</li>
    </ul>

    <h3>השחקנים במערכת (כמו בסימולציה):</h3>
    <ul>
        <li>**מחזיק (Holder):** האדם או הישות שמחזיקים ב-VC (באמצעות ארנק דיגיטלי מאובטח) ורוצים להציג אותו למאמת. השליטה ב-VC וב-DID נמצאת אצל המחזיק.</li>
        <li>**מנפיק (Issuer):** הגורם המוסמך שמנפיק את ה-VC וחותם עליו דיגיטלית. זה יכול להיות ממשלה, אוניברסיטה, בנק, או אפילו אתר אינטרנט. לכל מנפיק יש DID משלו.</li>
        <li>**מאמת (Verifier):** הגורם שרוצה לוודא את אמיתות הטענה שב-VC. זה יכול להיות שירות מקוון שדורש הוכחת גיל, בנק שדורש אישור KYC, או אפילו אדם אחר. המאמת אינו צריך לפנות למנפיק באופן ישיר כדי לאמת את ה-VC.</li>
        <li>**רשת DID (DID Network/Ledger):** התשתית המבוזרת (לרוב בלוקצ'יין או מערכת דומה) שמשמשת לאחסון ואחזור מסמכי ה-DID באופן עמיד בפני שינויים וזמין גלובלית.</li>
    </ul>

    <h3>תהליך אימות אישור (VC Verification Flow): צעד אחר צעד</h3>
    <p>התהליך מדגים איך מאמת יכול לוודא ש-VC תקף ואמין, מבלי תלות ישירה במנפיק בזמן האימות:</p>
    <ol>
        <li>**המחזיק שולח VC למאמת:** המחזיק בוחר איזה VC לשתף עם המאמת ושולח לו אותו (לרוב דרך ערוץ מאובטח). ה-VC מכיל את הטענה (למשל, גיל > 18), את DID המחזיק, את DID המנפיק, וחתימה דיגיטלית של המנפיק.</li>
        <li>**המאמת מזהה את DID המנפיק:** המאמת מקבל את ה-VC ומזהה את ה-DID של הגורם שמנפיק אותו, כפי שרשום ב-VC.</li>
        <li>**המאמת מאחזר את מסמך ה-DID של המנפיק:** כדי לאמת את חתימת המנפיק על ה-VC, המאמת זקוק למפתח הציבורי של המנפיק. המאמת פונה לרשת ה-DID (באמצעות "רזולבר") כדי לאחזר את מסמך ה-DID של המנפיק, שמקושר ל-DID הספציפי.</li>
        <li>**רשת ה-DID מספקת את המסמך:** רשת ה-DID מאתרת את מסמך ה-DID המבוקש ושולחת אותו למאמת.</li>
        <li>**המאמת מאמת את חתימת המנפיק:** המאמת משתמש במפתח הציבורי של המנפיק (שקיבל במסמך ה-DID) כדי לאמת את החתימה הדיגיטלית על ה-VC. אם החתימה תקינה, המאמת יכול להיות בטוח שה-VC הונפק על ידי המנפיק המוצהר ולא שונה מאז הנפקתו.</li>
        <li>**בדיקות ולידציה נוספות:** המאמת מבצע בדיקות קריטיות נוספות, כמו בדיקת תאריך התפוגה של ה-VC, ובדיקה האם המנפיק ביטל את ה-VC (למשל, אם הרישיון נשלל). מידע על שירותי ביטול (Revocation) ניתן למצוא במסמך ה-DID של המנפיק.</li>
        <li>**האישור תקף:** אם כל הבדיקות עוברות בהצלחה, המאמת קובע שה-VC תקף והטענה שבו אמינה (למשל, שהמחזיק אכן מעל גיל 18).</li>
    </ol>
    <p>כל התהליך הזה מתרחש לרוב באופן אוטומטי בתוכנה של המאמת (או בארנק הדיגיטלי), והמחזיק רק נדרש לאשר את השיתוף הראשוני.</p>

    <h3>מדוע המודל הזה פורץ דרך?</h3>
    <ul>
         <li>**פרטיות משופרת:** המחזיק חושף רק את המינימום ההכרחי של המידע (למשל, רק שהגיל מעל סף מסוים, לא תאריך לידה מדויק).</li>
         <li>**שליטה בידי המשתמש:** אתה שולט ב-DID שלך ובאילו אישורים לשתף ומתי.</li>
         <li>**אבטחה חזקה:** מתבסס על יסודות קריפטוגרפיים מוצקים ועל תשתית מבוזרת.</li>
         <li>**עמידות וזמינות:** מסמכי ה-DID ברשת המבוזרת מבטיחים שהמערכת עמידה בפני נקודות כשל יחידות.</li>
         <li>**הפחתת חיכוך:** תהליכי אימות יכולים להיות מהירים ויעילים בהרבה לעומת המודלים המסורתיים.</li>
    </ul>

    <h3>יישומים פוטנציאליים:</h3>
    <p>הפוטנציאל של DID ו-VCs עצום ונוגע כמעט בכל תחום הדורש הוכחת זהות או תכונה:</p>
    <ul>
        <li>**חינוך:** תעודות ודיפלומות שניתן לאמת באופן מיידי וגלובלי.</li>
        <li>**פיננסים:** תהליכי KYC/AML יעילים, פתיחת חשבונות, בקשות אשראי.</li>
        <li>**בריאות:** ניהול רשומות רפואיות, מרשמים, אישורי חיסון.</li>
        <li>**ממשל:** זהות דיגיטלית לאזרח, שירותים ממשלתיים מקוונים, הצבעה.</li>
        <li>**נסיעות:** כרטיסי עלייה למטוס, אישורי כניסה למדינות.</li>
        <li>**רשתות חברתיות:** אימות פרופילים, מניעת בוטים.</li>
        <li>**IoT:** זיהוי מאובטח של מכשירים ותקשורת ביניהם.</li>
    </ul>
    <p>מערכות DID/VC הן אבן יסוד באינטרנט של העתיד, המאפשרות לנו לנווט בעולם הדיגיטלי עם יותר פרטיות, אבטחה ושליטה על הזהות שלנו.</p>
</div>

<style>
    /* Global Styles */
    :root {
        --primary-color: #007bff;
        --secondary-color: #28a745;
        --accent-color: #ffc107;
        --text-color: #343a40;
        --bg-light: #f8f9fa;
        --bg-dark: #e9ecef;
        --border-color: #dee2e6;
        --success-color: #28a745;
        --failure-color: #dc3545;
        --info-color: #17a2b8;
        --card-bg: #ffffff;
        --box-shadow: rgba(0, 0, 0, 0.1);
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        direction: rtl;
        text-align: right;
        background-color: #f4f7f6;
        padding: 20px;
    }

    h1, h2, h3, h4 {
        color: var(--primary-color);
        margin-bottom: 15px;
    }

    h1 { font-size: 2.5em; }
    h2 { font-size: 2em; border-bottom: 2px solid var(--border-color); padding-bottom: 10px; }
    h3 { font-size: 1.5em; }
    h4 { font-size: 1.2em; }

    p { margin-bottom: 15px; }

    ul {
        padding-right: 25px;
        margin-bottom: 15px;
    }

    li {
        margin-bottom: 8px;
    }

    .action-button {
        padding: 10px 20px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease, opacity 0.3s ease;
        margin-top: 10px;
    }

    .action-button:hover:not(:disabled) {
        background-color: #0056b3;
    }

    .action-button:disabled {
        background-color: #ccc;
        cursor: not-allowed;
        opacity: 0.6;
    }

     .toggle-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        background-color: var(--secondary-color);
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease;
     }

     .toggle-button:hover {
         background-color: #218838;
     }

    /* Simulation Specific Styles */
    .interactive-simulation {
        max-width: 1000px;
        margin: 20px auto;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--bg-light);
        box-shadow: 0 4px 15px var(--box-shadow);
        position: relative; /* Needed for absolute positioning of arrows */
    }

    .simulation-header {
        text-align: center;
        margin-bottom: 30px;
    }

    .actors-container {
        display: flex;
        justify-content: space-around;
        align-items: flex-start; /* Align items to the top */
        flex-wrap: wrap; /* Allow wrapping */
        gap: 20px; /* Space between actor cards */
        position: relative;
        padding: 20px 0; /* Add padding for potential absolute elements */
    }

    .actor-card {
        flex: 1; /* Allow cards to grow */
        min-width: 250px; /* Minimum width for each card */
        max-width: 300px;
        border: 2px solid var(--primary-color);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        background-color: var(--bg-dark);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }

    .actor-card:hover {
        transform: translateY(-5px);
    }

    .actor-title {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 15px;
    }

    .actor-icon {
        font-size: 1.8em;
        margin-left: 10px;
    }

    .actor-card h3 {
        margin: 0;
        color: var(--primary-color);
    }

    .data-card {
        border: 1px dashed var(--info-color);
        border-radius: 8px;
        padding: 15px;
        margin-top: 15px;
        min-height: 80px;
        background-color: var(--card-bg);
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        overflow: hidden; /* Hide overflow during content transitions */
    }

     .data-card .card-title {
         font-weight: bold;
         color: var(--text-color);
         margin-bottom: 10px;
         border-bottom: 1px solid var(--border-color);
         padding-bottom: 5px;
         width: 100%;
     }

    .data-card .card-content {
         display: flex;
         flex-direction: column;
         align-items: center;
         justify-content: center;
         width: 100%;
     }

    .data-card .placeholder {
         color: #6c757d;
         font-style: italic;
     }

     .data-card .icon {
         font-size: 2em;
         color: var(--info-color);
         margin-bottom: 5px;
         transition: transform 0.5s ease;
     }

     .data-card .label {
         font-size: 0.9em;
         color: var(--text-color);
         font-weight: bold;
     }

     .data-card .data-summary {
         font-size: 0.8em;
         color: #555;
         margin-top: 5px;
     }

     .data-card .status {
         font-weight: bold;
         margin-top: 10px;
         font-size: 0.9em;
         transition: color 0.5s ease;
     }

     .data-card .status.success { color: var(--success-color); }
     .data-card .status.failure { color: var(--failure-color); }
     .data-card .status.pending { color: var(--accent-color); }
     .data-card .status.info { color: var(--info-color); }


    #verifier .actions {
        margin-top: 20px;
        display: flex;
        flex-direction: column;
        gap: 8px; /* Space between buttons */
    }

    #verifier .action-button {
        width: 100%; /* Make buttons full width */
        text-align: center;
    }

    .verification-status {
        margin-top: 25px;
        padding: 15px;
        border: 1px dashed var(--border-color);
        border-radius: 8px;
        background-color: var(--bg-light);
        min-height: 60px; /* Reserve space */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }

     .current-step-text {
         margin: 0;
         font-style: italic;
         color: #555;
         transition: opacity 0.5s ease;
     }

    .result {
        margin-top: 10px;
        font-weight: bold;
        padding: 10px;
        border-radius: 5px;
        width: 100%;
        text-align: center;
        opacity: 0; /* Start hidden */
        transform: translateY(10px);
        transition: opacity 0.5s ease, transform 0.5s ease;
    }

    .result.show {
        opacity: 1;
        transform: translateY(0);
    }

    #verification-result.success {
        background-color: #d4edda;
        color: var(--success-color);
        border: 1px solid #c3e6cb;
    }

    #verification-result.failure {
        background-color: #f8d7da;
        color: var(--failure-color);
        border: 1px solid #f5c6cb;
    }

    /* Flow Arrows (Conceptual, requires JS to position/animate) */
     .flow-arrow {
         position: absolute;
         width: 50px; /* Adjust size as needed */
         height: 20px;
         background: var(--info-color); /* Placeholder color */
         z-index: 10;
         top: 50%;
         transform: translateY(-50%);
         opacity: 0; /* Start hidden */
         transition: opacity 0.5s ease, transform 0.5s ease, background-color 0.5s ease;
         display: none; /* Hide by default */
     }

     .flow-arrow.show {
         display: block;
         opacity: 1;
     }

     .vc-flow {
         left: calc(25% + 150px); /* Approx right of Holder, left of Verifier */
         background: var(--success-color); /* VC flow color */
     }

     .did-flow {
         right: calc(25% + 150px); /* Approx right of DID Network, left of Verifier */
         background: var(--primary-color); /* DID flow color */
     }

    /* Specific box content animations */
     .data-card .received-data {
         opacity: 0; /* Start hidden */
         transform: translateY(10px);
         transition: opacity 0.5s ease, transform 0.5s ease;
     }

     .data-card .received-data.show {
         opacity: 1;
         transform: translateY(0);
     }

    .data-card .card-content.placeholder.hide {
        opacity: 0;
        height: 0;
        overflow: hidden;
        transition: opacity 0.5s ease, height 0.5s ease;
    }


    /* Explanation Section Styles */
    .explanation-section {
        margin: 30px auto;
        max-width: 1000px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--bg-light);
        box-shadow: 0 4px 15px var(--box-shadow);
    }

     .explanation-section h2, .explanation-section h3 {
         color: var(--primary-color);
         border-bottom: 1px solid var(--border-color);
         padding-bottom: 8px;
         margin-bottom: 15px;
     }

     .explanation-section p, .explanation-section ul {
         line-height: 1.7;
         margin-bottom: 18px;
     }

     .explanation-section ul {
         padding-right: 25px;
     }

     .explanation-section li {
         margin-bottom: 10px;
     }

    /* Reset Button */
    .reset-button {
        display: block;
        margin: 20px auto 0;
        background-color: var(--failure-color);
    }
     .reset-button:hover:not(:disabled) {
        background-color: #c82333;
     }

    /* Responsiveness */
    @media (max-width: 768px) {
        .actors-container {
            flex-direction: column;
            align-items: center;
        }
        .actor-card {
            width: 90%;
            max-width: 400px;
        }
         .flow-arrow {
             display: none !important; /* Hide arrows on small screens */
         }
    }


</style>

<script>
    const holderVcBox = document.getElementById('holder-vc');
    const verifierVcBox = document.getElementById('verifier-vc');
    const verifierDidDocBox = document.getElementById('verifier-did-doc');
    const didNetworkData = document.getElementById('did-network-data');
    const explanationText = document.getElementById('explanation-text');
    const verificationResult = document.getElementById('verification-result');

    const btnSendVcFromHolder = document.getElementById('send-vc-from-holder');
    const btnReceiveVc = document.getElementById('step1-receive-vc');
    const btnRequestDidDoc = document.getElementById('step2-request-did-doc');
    const btnVerifySignature = document.getElementById('step3-verify-signature');
    const btnAdditionalChecks = document.getElementById('step4-additional-checks');
    const btnToggleExplanation = document.getElementById('toggle-explanation');
    const fullExplanation = document.getElementById('full-explanation');
    const btnReset = document.getElementById('reset-simulation');

    const vcFlowArrow = document.querySelector('.vc-flow');
    const didFlowArrow = document.querySelector('.did-flow');

    const simulatedVCContent = {
         summary: "אישור גיל (VC) מונפק ע״י המנפיק X",
         details: "Claims: age > 18, Issuer: DID:issuerABC, Holder: DID:holder123, Signature: [Digital Signature]"
    };
    const simulatedDIDDocumentContent = {
        summary: "מסמך DID עבור DID:issuerABC",
        details: "Public Key: [XYZ...], Service Endpoints: { RevocationList2020: 'https://...' }"
    };

    function updateExplanation(text, type = 'info') {
         explanationText.textContent = text;
         explanationText.className = `current-step-text status ${type}`;
    }

     function updateDataCard(cardElement, content, statusText, statusType = 'info') {
         const placeholder = cardElement.querySelector('.placeholder');
         const receivedData = cardElement.querySelector('.received-data');
         const statusElement = cardElement.querySelector('.status');

         if (content) {
             placeholder.classList.add('hide');
             // Assuming content is an object with summary and details
             receivedData.querySelector('.label').textContent = content.label;
             receivedData.querySelector('.icon').textContent = content.icon;
             receivedData.querySelector('.data-summary').textContent = content.summary; // Added summary field
             receivedData.style.display = 'flex'; // Show received data
             setTimeout(() => { receivedData.classList.add('show'); }, 50); // Animate in
         } else {
              // Revert to placeholder
             receivedData.classList.remove('show');
              receivedData.style.display = 'none';
              placeholder.classList.remove('hide');
         }


         if (statusElement) {
             statusElement.textContent = statusText;
             statusElement.className = `status ${statusType}`;
         }
     }

    function resetSimulation() {
         // Reset Data Boxes
         holderVcBox.querySelector('.status').textContent = 'מוכן לשליחה';
         holderVcBox.querySelector('.status').className = 'status info';
         holderVcBox.querySelector('.card-content.received-data')?.classList.remove('show');
         holderVcBox.querySelector('.card-content.placeholder')?.classList.remove('hide');


         verifierVcBox.querySelector('.card-content.received-data')?.classList.remove('show');
         verifierVcBox.querySelector('.card-content.placeholder')?.classList.remove('hide');
         verifierVcBox.querySelector('.card-content.placeholder .label').textContent = 'ממתין לאישור...';
         verifierVcBox.querySelector('.card-content.placeholder .icon').textContent = '⏳';
         verifierVcBox.querySelector('.status')?.classList.remove('show');


         verifierDidDocBox.style.display = 'none';
         verifierDidDocBox.querySelector('.card-content.received-data')?.classList.remove('show');
         verifierDidDocBox.querySelector('.card-content.placeholder')?.classList.remove('hide');
         verifierDidDocBox.querySelector('.card-content.placeholder .label').textContent = 'ממתין למסמך DID...';
         verifierDidDocBox.querySelector('.card-content.placeholder .icon').textContent = '⏳';
         verifierDidDocBox.querySelector('.status')?.classList.remove('show');


         didNetworkData.querySelector('.card-content.received-data')?.classList.remove('show');
         didNetworkData.querySelector('.card-content.processed-data')?.classList.remove('show');
         didNetworkData.querySelector('.card-content.placeholder')?.classList.remove('hide');
         didNetworkData.querySelector('.card-content.placeholder .label').textContent = 'ממתין לבקשה...';
         didNetworkData.querySelector('.card-content.placeholder .icon').textContent = '📁';


         // Reset Buttons
         btnSendVcFromHolder.disabled = false;
         btnReceiveVc.disabled = true;
         btnRequestDidDoc.disabled = true;
         btnVerifySignature.disabled = true;
         btnAdditionalChecks.disabled = true;

         // Reset Explanation and Result
         updateExplanation('לחץ על "שלח אישור" (אצל המחזיק) כדי להתחיל!', 'info');
         verificationResult.textContent = '';
         verificationResult.className = 'result'; // Remove success/failure classes
         verificationResult.classList.remove('show');

         // Reset Arrows
         vcFlowArrow.classList.remove('show');
         didFlowArrow.classList.remove('show');
    }


    // --- Simulation Flow ---

    // Initial state setup handled by resetSimulation
    resetSimulation();


    // Step 0: Holder sends VC (User clicks)
    btnSendVcFromHolder.addEventListener('click', () => {
        btnSendVcFromHolder.disabled = true;
        updateExplanation('המחזיק שולח את אישור הגיל למאמת...', 'pending');
        holderVcBox.querySelector('.status').textContent = 'שולח אישור...';
        holderVcBox.querySelector('.status').className = 'status pending';

        // Simulate VC sending animation
        vcFlowArrow.classList.add('show');

        setTimeout(() => {
            vcFlowArrow.classList.remove('show');
            updateExplanation('האישור הגיע למאמת! כעת, בתפקיד המאמת, לחץ על "קבל אישור".', 'info');
            btnReceiveVc.disabled = false;
            holderVcBox.querySelector('.status').textContent = 'אישור נשלח';
             holderVcBox.querySelector('.status').className = 'status success';
        }, 1500); // Simulate sending time
    });


    // Step 1: Verifier receives VC (User clicks)
    btnReceiveVc.addEventListener('click', () => {
        btnReceiveVc.disabled = true;
        updateExplanation('המאמת קיבל את האישור. הוא מזהה את המנפיק מהאישור ומתחיל בתהליך האימות.', 'pending');

        // Update Verifier VC box content
        updateDataCard(verifierVcBox, { icon: '📄', label: 'אישור גיל (VC)', summary: 'מאת: DID:issuerABC' }, 'אישור התקבל.', 'success');


        setTimeout(() => {
            updateExplanation('כעת המאמת צריך את המפתח הציבורי של המנפיק. לחץ על "בקש מסמך DID" כדי לקבל אותו מרשת ה-DID.', 'info');
            btnRequestDidDoc.disabled = false;
        }, 1000); // Allow time for visual update
    });

    // Step 2: Verifier requests DID Document (User clicks)
    btnRequestDidDoc.addEventListener('click', () => {
        btnRequestDidDoc.disabled = true;
        updateExplanation('המאמת שולח בקשה לרשת ה-DID עבור מסמך ה-DID של המנפיק...', 'pending');

        // Simulate network request animation
        didNetworkData.querySelector('.placeholder').classList.add('hide');
        didNetworkData.querySelector('.received-data').style.display = 'flex';
        setTimeout(() => { didNetworkData.querySelector('.received-data').classList.add('show'); }, 50);

        didFlowArrow.classList.add('show');

        setTimeout(() => {
             // Simulate network response
             didFlowArrow.classList.remove('show');
             didNetworkData.querySelector('.received-data').classList.remove('show');
             didNetworkData.querySelector('.processed-data').style.display = 'flex';
             setTimeout(() => { didNetworkData.querySelector('.processed-data').classList.add('show'); }, 50);

             updateExplanation('רשת ה-DID מצאה את מסמך המנפיק ושולחת אותו למאמת...', 'pending');

             setTimeout(() => {
                  didNetworkData.querySelector('.processed-data').classList.remove('show');
                  didNetworkData.querySelector('.placeholder').classList.remove('hide');
                  didNetworkData.querySelector('.placeholder .label').textContent = 'מוכן לבקשות';
                  didNetworkData.querySelector('.placeholder .icon').textContent = '📁';


                 // Update Verifier DID Doc box content
                 verifierDidDocBox.style.display = 'flex'; // Show the box
                 updateDataCard(verifierDidDocBox, { icon: '🔑', label: 'מסמך DID', summary: 'מפתח ציבורי למנפיק' }, 'מסמך התקבל.', 'success');


                 updateExplanation('המאמת קיבל את מסמך ה-DID של המנפיק. כעת הוא יכול לאמת את חתימת המנפיק על ה-VC באמצעות המפתח הציבורי.', 'info');
                 btnVerifySignature.disabled = false;
             }, 1000); // Simulate network transfer time

        }, 2000); // Simulate network processing time
    });

    // Step 3: Verifier verifies signature (User clicks)
    btnVerifySignature.addEventListener('click', () => {
        btnVerifySignature.disabled = true;
        updateExplanation('המאמת משתמש במפתח הציבורי כדי לאמת את חתימת המנפיק...', 'pending');

        // Simulate verification process visually (optional: add animation class)
        verifierVcBox.querySelector('.icon').style.transform = 'scale(1.2) rotate(10deg)'; // Simple visual cue
        verifierDidDocBox.querySelector('.icon').style.transform = 'scale(1.2) rotate(-10deg)';

        setTimeout(() => {
             verifierVcBox.querySelector('.icon').style.transform = 'scale(1) rotate(0deg)';
             verifierDidDocBox.querySelector('.icon').style.transform = 'scale(1) rotate(0deg)';

            const signatureVerified = true; // Simulate successful verification

            if (signatureVerified) {
                updateDataCard(verifierVcBox, null, 'חתימה אומתה בהצלחה!', 'success'); // Update status only
                 updateExplanation('החתימה על האישור אומתה! המאמת יכול להיות בטוח שהאישור הונפק על ידי המנפיק המוצהר.', 'success');
                btnAdditionalChecks.disabled = false;
            } else {
                updateDataCard(verifierVcBox, null, 'אימות חתימה נכשל.', 'failure');
                 updateExplanation('שגיאה: אימות החתימה נכשל. האישור אינו תקף.', 'failure');
                 verificationResult.textContent = 'אימות נכשל: חתימת המנפיק אינה תקינה.';
                 verificationResult.className = 'result failure show';
                 // Stop flow on failure
            }
        }, 1500); // Simulate verification time
    });

    // Step 4: Additional Checks (User clicks)
    btnAdditionalChecks.addEventListener('click', () => {
        btnAdditionalChecks.disabled = true;
        updateExplanation('המאמת מבצע בדיקות נוספות: תוקף, ביטול (revocation), ולידציה של הנתונים (האם הגיל אכן מעל 18?).', 'pending');

         // Simulate additional checks visually (optional: add animation class)
         verifierVcBox.style.border = '2px solid var(--accent-color)'; // Highlight during checks

        setTimeout(() => {
             verifierVcBox.style.border = ''; // Remove highlight

            const additionalChecksPassed = true; // Simulate successful checks

            if (additionalChecksPassed) {
                updateExplanation('כל הבדיקות עברו בהצלחה! האישור תקף וניתן לסמוך עליו.', 'success');
                verificationResult.textContent = 'אימות הושלם בהצלחה! האישור תקף.';
                verificationResult.className = 'result success show';
            } else {
                updateExplanation('שגיאה: בדיקות נוספות נכשלו. האישור אינו תקף (אולי בוטל או פג תוקף).', 'failure');
                verificationResult.textContent = 'אימות נכשל: האישור אינו תקף (בוטל/פג תוקף/נתונים לא תואמים).';
                verificationResult.className = 'result failure show';
            }
        }, 2000); // Simulate checks time
    });

    // Toggle Explanation
    btnToggleExplanation.addEventListener('click', () => {
        if (fullExplanation.style.display === 'none') {
            fullExplanation.style.display = 'block';
            btnToggleExplanation.textContent = 'הסתר הסבר מורחב';
        } else {
            fullExplanation.style.display = 'none';
             btnToggleExplanation.textContent = 'הצג הסבר מורחב';
        }
    });

    // Reset Button
    btnReset.addEventListener('click', resetSimulation);

    // Initial state setup
    // Done via resetSimulation call at the start
</script>
```