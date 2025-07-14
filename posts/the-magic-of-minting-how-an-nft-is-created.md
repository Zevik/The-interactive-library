---
title: "קסם המינטור: כך נוצר NFT"
english_slug: the-magic-of-minting-how-an-nft-is-created
category: "מדעי המחשב"
tags:
  - NFT
  - בלוקצ'יין
  - קריפטו
  - מינטור
  - נכסים דיגיטליים
---
# קסם המינטור: כך נוצר NFT

יש לכם קובץ דיגיטלי? כל אחד יכול להעתיק אותו בלחיצת כפתור. אבל מה הופך יצירה דיגיטלית אחת – תמונה, שיר, סרטון – לייחודית באמת, לכזו שרק *אתם* הבעלים המוכחים שלה? התשובה טמונה בתהליך המרתק שנקרא מינטור. בואו נפעיל את מכונת המינטור שלנו ונראה איך זה קורה!

<div class="minting-simulation">
    <h2>מכונת המינטור הקסומה</h2>
    <p class="intro-text">הזינו פרטים עבור היצירה הדיגיטלית שלכם (דמה) ולחצו "מנטט!" כדי לצפות בתהליך.</p>

    <div class="input-section">
        <label for="digitalFile">היצירה הדיגיטלית שלכם (דמה):</label>
        <input type="text" id="digitalFile" value="יצירת-מופת-דיגיטלית.png" readonly title="זהו ייצוג דמה לקובץ הדיגיטלי שלכם. הוא לא באמת נטען לכאן.">

        <label for="nftName">שם נכס ה-NFT:</label>
        <input type="text" id="nftName" placeholder="לדוגמה: 'דיוקן בחשיכה דיגיטלית'">

        <label for="nftDescription">תיאור קצר:</label>
        <textarea id="nftDescription" placeholder="לדוגמה: 'דיוקן עוצר נשימה נוצר באמצעות AI גנרטיבי.'"></textarea>
    </div>

    <div class="gas-fee-section">
        <h3><i class="icon-gas">⛽</i> עלות "גז" משוערת למינטור:</h3>
        <p id="gasFeeDisplay">...מחשב עלויות רשת...</p>
        <p class="gas-note">עלות זו משולמת לרשת הבלוקצ'יין עבור עיבוד הטרנזקציה.</p>
    </div>

    <button id="mintButton" class="action-button">הפעל את המינטור!</button>

    <div id="simulationArea" class="simulation-area hidden">
        <div class="process-flow">
             <div class="step-container">
                <div class="step-icon" id="icon1">📦</div>
                <div class="step-label">1. נתונים נארזים</div>
             </div>
             <div class="arrow right" id="arrow1"></div>
             <div class="step-container">
                 <div class="step-icon" id="icon2">✍️</div>
                 <div class="step-label">2. טרנזקציה נוצרת</div>
             </div>
             <div class="arrow right" id="arrow2"></div>
             <div class="step-container">
                 <div class="step-icon" id="icon3">📡</div>
                 <div class="step-label">3. נשלח לרשת</div>
             </div>
             <div class="arrow right" id="arrow3"></div>
             <div class="step-container">
                 <div class="step-icon" id="icon4">⛓️</div>
                 <div class="step-label">4. אומת בבלוקצ'יין</div>
             </div>
              <div class="arrow right" id="arrow4"></div>
             <div class="step-container">
                 <div class="step-icon" id="icon5">✨</div>
                 <div class="step-label">5. NFT נולד!</div>
             </div>
        </div>
         <div id="processingIndicator" class="processing-indicator"></div>
    </div>

    <div id="resultsArea" class="results-area hidden">
        <h3>🎉 ברכות! ה-NFT נוצר בהצלחה! 🎉</h3>
        <p><i class="icon-id">🆔</i> מזהה (Token ID): <span id="tokenIDDisplay">...</span></p>
        <p><i class="icon-owner">👤</i> כתובת הבעלים הראשוני: <span id="ownerAddressDisplay">...</span></p>
        <p class="note">זכרו: ה-NFT עצמו הוא הרשומה הייחודית בבלוקצ'יין המצביעה על היצירה שלכם ומאשרת את הבעלות, לא קובץ המדיה המקורי.</p>
    </div>
</div>

<button id="toggleExplanation" class="secondary-button">רוצים להבין איך זה עובד לעומק? הצגת הסבר טכני מפורט</button>

<div id="explanation" class="explanation-section hidden">
    <h2>🕵️‍♂️ מאחורי הקלעים: הסבר מפורט על תהליך המינטור</h2>

    <h3>מה זה בכלל מינטור (Minting) של NFT?</h3>
    דמיינו מפעל שמטביע מטבעות חדשים. מינטור NFT הוא התהליך הדיגיטלי שבו יצירה דיגיטלית הופכת לנכס דיגיטלי ייחודי ומוכח בעלות על גבי רשת בלוקצ'יין. במקום מטבע פיזי, אנחנו "טובעים" נכס דיגיטלי ייחודי שאי אפשר לשכפל באופן זהה ברמת הבעלות והמקוריות. זה כמו להפוך קובץ זמין לכולם לפריט אספנות דיגיטלי עם "תעודת מקוריות" בלתי ניתנת לשינוי.

    <h3>למה המינטור הוא המפתח לייחודיות דיגיטלית?</h3>
    בעולם הדיגיטלי, העתקה היא קלה ומיידית. מינטור פותר את בעיית ה"העתק-הדבק" הזו עבור נכסים דיגיטליים. הוא יוצר רשומה קבועה ופומבית על הבלוקצ'יין שמאשרת *אתם* הבעלים של *אותה* גרסה ספציפית של היצירה. זה מעניק ליצירה "נדירות" ו"מקומית" דיגיטלית, מאפשר לעקוב אחרי הבעלות עליה ולהפוך אותה לנכס בר-מכירה ובר-העברה בעל ערך.

    <h3>צעד אחר צעד: מה קורה מבחינה טכנית?</h3>
    <p>תהליך המינטור מורכב מכמה שלבים קריטיים:</p>
    <ol>
        <li>**איסוף החומרים (נתונים נארזים):** אוספים את כל המידע הדרוש - היצירה הדיגיטלית עצמה (שמאוחסנת לרוב מחוץ לבלוקצ'יין, בדרך כלל במערכות אחסון מבוזרות כמו IPFS), המטה-דאטה שלה (שם, תיאור, קישורים, מאפיינים מיוחדים) וכתובת הארנק הדיגיטלי שלכם, שתהפוך לכתובת הבעלים הראשוני.</li>
        <li>**מילוי טופס הבקשה (טרנזקציה נוצרת):** כל המידע הזה נאגד יחד ומוכנס לתוך "טופס" דיגיטלי מיוחד שנקרא טרנזקציית בלוקצ'יין. טרנזקציה זו מפעילה קוד תוכנה חכם שרשום על הבלוקצ'יין (Smart Contract), והוא יודע בדיוק איך ליצור NFT חדש.</li>
        <li>**שידור ברשת הבלוקצ'יין (נשלח לרשת):** "טופס הבקשה" - הטרנזקציה - נשלח לאוויר, לכל המחשבים המחוברים לרשת הבלוקצ'יין (כמו רשת את'ריום, פוליגון, סולאנה וכו').</li>
        <li>**אישור וחותמת (אומת בבלוקצ'יין):** כורים (בשיטות ישנות יותר) או מאמתים (בשיטות חסכוניות יותר כמו Proof-of-Stake) ברשת בודקים שוב שהטרנזקציה תקינה, שהיא לא ניסיון לרמות, ומוסיפים אותה ל"דף" הבא בספר החשבונות המבוזר - הבלוק החדש בשרשרת.</li>
        <li>**הנכס הדיגיטלי נולד (NFT נולד!):** ברגע שהטרנזקציה אושרה והוכנסה לבלוק, ה-Smart Contract "טובע" באופן רשמי את ה-NFT החדש. הוא מקצה לו מספר מזהה ייחודי (Token ID) שלא היה קיים קודם תחת החוזה הזה, ורושם את כתובת הארנק שלכם כבעלים הראשוני. מעכשיו, ה-NFT הזה קיים על הבלוקצ'יין והבעלות עליו מתועדת באופן פומבי ושקוף.</li>
    </ol>

    <h3>מי משתתף בחגיגה? רכיבים קריטיים במינטור:</h3>
    <ul>
        <li>**היצירה הדיגיטלית:** המקור - התמונה, הסרטון, האודיו וכו' - שה-NFT מייצג.</li>
        <li>**מטה-דאטה (Metadata):** המידע הנלווה על היצירה (כותרת, תיאור, קישור לקובץ, שם היוצר, תאריך). זה חלק בלתי נפרד מזהות ה-NFT.</li>
        <li>**Smart Contract (חוזה חכם):** קוד שפועל על הבלוקצ'יין כמו "בית חרושת" או "מנהל" עבור סדרת NFTs. הוא קובע את הכללים לטביעה, העברה וניהול של NFTs מסוג ספציפי (לרוב עומד בסטנדרטים כמו ERC-721).</li>
        <li>**Gas Fees (עמלות גז):** העלות שאתם משלמים לרשת הבלוקצ'יין כדי שהיא תבצע את הפעולה בשבילכם. זוהי עמלה למאמתים/כורים, לא ליוצר ה-Smart Contract או לפלטפורמה. העלות משתנה לפי עומס הרשת ומורכבות הפעולה.</li>
        <li>**ארנק דיגיטלי:** הכרחי כדי ליזום את תהליך המינטור (כי ממנו משולמות עמלות הגז) וכדי לקבל את הבעלות על ה-NFT שזה עתה נטבע.</li>
    </ul>

    <h3>רגע, הקובץ שלי *באמת* על הבלוקצ'יין?</h3>
    זו נקודה חשובה! ברוב המקרים, הקובץ הדיגיטלי עצמו (תמונה גדולה, סרטון כבד) *אינו* נשמר ישירות על הבלוקצ'יין. בלוקצ'יינים יקרים ולא מתאימים לאחסון קבצים גדולים. במקום זאת, ה-NFT על הבלוקצ'יין הוא למעשה **רשומה קטנה וקבועה** הכוללת:
    <ul>
        <li>**מזהה ייחודי (Token ID):** המספר הסידורי של ה-NFT הזה בתוך החוזה החכם שלו.</li>
        <li>**כתובת ה-Smart Contract:** הפניה לחוזה החכם שמנהל את סדרת ה-NFT הזו.</li>
        <li>**כתובת הבעלים הנוכחי:** מי מחזיק כרגע ב-NFT (אתם, במקרה של מינטור ראשוני).</li>
        <li>**"מצביע" (Pointer) למטה-דאטה:** לרוב כתובת URL או URI שמפנה לקובץ המטה-דאטה, שבתורו מכיל את הקישור *האמיתי* לקובץ היצירה הדיגיטלית המקורי (שנמצא במקום אחר, כמו IPFS).</li>
    </ul>
    אז ה-NFT הוא בעצם "תעודת המקוריות והבעלות" הדיגיטלית, והיא מצביעה על היצירה.

    <h3>כמה זה עולה? סיפור ה-"גז" (Gas Fees)</h3>
    Gas Fees הן העמלה שאתם משלמים למשתתפי הרשת שמקדישים את כוח המחשוב שלהם כדי לאמת ולהכניס את הטרנזקציה שלכם לבלוקצ'יין. זו העלות התפעולית של השימוש ברשת. עלויות הגז יכולות להשתנות דרמטית בגלל:
    <ul>
        <li>**עומס תנועה ברשת:** כמו פקק בכביש, ככל שיש יותר אנשים שמנסים לבצע פעולות, המחיר לעמלה "מהירה" עולה.</li>
        <li>**מורכבות הפעולה:** מינטור בדרך כלל דורש יותר משאבים (ויותר גז) מפעולה פשוטה כמו שליחת מטבעות.</li>
        <li>**"מחיר הדלק" (מחיר יחידת הגז):** המחיר הבסיסי ליחידת גז נקבע לפי ביקוש והיצע ברשת בזמן אמת.</li>
        <li>**רשת הבלוקצ'יין הספציפית:** רשתות שונות בנויות בצורה שונה ועלויות התפעול בהן משתנות. את'ריום (Ethereum), למשל, ידועה בעלויות גז גבוהות יותר בזמני עומס לעומת רשתות כמו פוליגון (Polygon) או סולאנה (Solana) שהן בדרך כלל זולות ומהירות יותר.</li>
    </ul>
    הבנת עלויות הגז חיונית לפני שמתחילים למנטט!

</div>

<style>
    body {
        font-family: 'Heebo', sans-serif; /* Use a modern Hebrew font */
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        direction: rtl; /* Ensure right-to-left for Hebrew */
        text-align: right;
        background: linear-gradient(135deg, #f0f4f8 0%, #d9e2ec 100%); /* Soft gradient background */
        color: #333;
        min-height: 100vh; /* Full viewport height */
    }

    h1, h2, h3 {
        color: #0d47a1; /* Darker blue */
        text-align: center;
        margin-bottom: 25px;
        font-weight: bold;
    }

    h1 {
        font-size: 2.5em;
        margin-top: 0;
        padding-bottom: 15px;
        border-bottom: 2px solid #0d47a1;
    }

    h2 {
         font-size: 2em;
         margin-top: 30px;
         border-bottom: 1px solid #e0e0e0;
         padding-bottom: 10px;
    }

     h3 {
        font-size: 1.4em;
        margin-top: 20px;
        margin-bottom: 12px;
        color: #1565c0; /* Medium blue */
        text-align: right; /* Ensure right alignment for explanation headings */
     }


    .minting-simulation, .explanation-section {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.15); /* More pronounced shadow */
        margin: 30px auto;
        max-width: 800px; /* Limit width for better readability */
        border: 1px solid #e0e0e0;
        transition: all 0.3s ease-in-out; /* Smooth transitions */
    }

    .minting-simulation h2 {
        color: #007bff;
        margin-bottom: 15px;
    }

    .intro-text {
        text-align: center;
        margin-bottom: 30px;
        color: #555;
        font-size: 1.1em;
    }

    .input-section, .gas-fee-section, .results-area {
        margin-bottom: 25px;
        padding-bottom: 25px;
        border-bottom: 1px dashed #cfd8dc; /* Light dashed line */
    }

     .gas-note {
        font-size: 0.9em;
        color: #666;
        margin-top: 8px;
        text-align: center;
     }

     .results-area .note {
        font-size: 0.95em;
        color: #555;
        margin-top: 20px;
        border-top: 1px solid #eceff1;
        padding-top: 15px;
        line-height: 1.5;
     }

    label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        color: #455a64; /* Dark grey-blue */
    }

    input[type="text"], textarea {
        width: calc(100% - 24px); /* Adjust for padding and border */
        padding: 12px;
        margin-bottom: 18px;
        border: 1px solid #b0bec5; /* Lighter border */
        border-radius: 6px;
        font-size: 1em;
        box-sizing: border-box; /* Include padding in width */
        background-color: #f8f9fa; /* Light background */
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    input[type="text"]:focus, textarea:focus {
        border-color: #007bff;
        box-shadow: 0 0 8px rgba(0, 123, 255, 0.2);
        outline: none;
    }

    textarea {
        height: 100px; /* Slightly taller textarea */
        resize: vertical;
    }

    #gasFeeDisplay {
        font-size: 1.2em;
        font-weight: bold;
        color: #ff9800; /* Orange */
        text-align: center;
         min-height: 1.5em; /* Prevent layout shifts during calculation */
    }

     .icon-gas, .icon-id, .icon-owner {
        display: inline-block;
        margin-left: 8px;
        color: #007bff; /* Match button color */
        font-size: 1.2em;
     }


    button {
        display: block;
        width: 100%;
        padding: 14px; /* Larger padding */
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 6px; /* More rounded corners */
        font-size: 1.3em;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        margin-bottom: 20px;
        font-weight: bold;
    }

    button:hover:not(:disabled) {
        background-color: #0056b3;
        transform: translateY(-2px); /* Slight lift effect */
    }

     button:active:not(:disabled) {
        transform: translateY(0);
     }

    button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
    }

     .secondary-button {
        width: auto;
        padding: 10px 20px;
        background-color: #6c757d;
        margin: 20px auto;
        display: block;
        font-size: 1.1em;
        font-weight: normal;
        border-radius: 4px;
     }
     .secondary-button:hover:not(:disabled) {
         background-color: #5a6268;
          transform: none; /* No lift for secondary button */
     }

     .simulation-area {
        min-height: 250px; /* Increased height */
        border: 2px dashed #b0bec5;
        padding: 20px;
        margin-top: 30px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-color: #e3f2fd; /* Light blue background */
        position: relative;
        overflow: hidden;
        border-radius: 8px;
         opacity: 0; /* Start hidden */
         transition: opacity 0.5s ease-in-out;
    }

    .simulation-area.visible {
        opacity: 1;
    }

    .hidden {
        display: none;
    }


     .process-flow {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        padding: 0 10px;
        box-sizing: border-box;
     }

     .step-container {
         display: flex;
         flex-direction: column;
         align-items: center;
         margin: 10px; /* Add some margin */
         text-align: center;
         flex-shrink: 0; /* Prevent shrinking */
         width: 80px; /* Fixed width for step container */
     }

    .step-icon {
        font-size: 2.5em; /* Larger icons */
        margin-bottom: 8px;
        padding: 15px;
        border: 3px solid #b0bec5;
        border-radius: 50%;
        background-color: #ffffff;
        width: 60px; /* Icon background size */
        height: 60px;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        transition: all 0.5s ease-out;
        color: #0d47a1; /* Default icon color */
        opacity: 0.3; /* Start dimmed */
         transform: scale(0.8); /* Start smaller */
    }

     .step-icon.active {
         opacity: 1;
         transform: scale(1);
         border-color: #28a745; /* Green border for active */
         color: #28a745; /* Green color for active */
         box-shadow: 0 0 15px rgba(40, 167, 69, 0.4); /* Green glow */
     }

     .step-icon#icon5.active {
        border-color: #ffc107; /* Gold border for final step */
        color: #ffc107; /* Gold color for final step */
         box-shadow: 0 0 15px rgba(255, 193, 7, 0.6); /* Gold glow */
     }

     .step-label {
        font-size: 0.9em;
        color: #546e7a; /* Dark grey */
         font-weight: bold;
         transition: color 0.5s ease-out;
     }

     .step-icon.active + .step-label {
         color: #28a745; /* Green label for active step */
     }

     .arrow {
        width: 40px; /* Width of the arrow */
        height: 3px;
        background-color: #b0bec5;
        margin: 0 5px; /* Spacing between steps and arrows */
        position: relative;
        transition: background-color 0.5s ease-out;
         flex-shrink: 0; /* Prevent shrinking */
     }

     .arrow.right::after {
        content: '▶'; /* Unicode arrow */
        position: absolute;
        left: 100%;
        top: 50%;
        transform: translateY(-50%);
        color: #b0bec5;
        font-size: 1.2em;
         transition: color 0.5s ease-out;
     }

     .arrow.active {
        background-color: #28a745; /* Green arrow when active */
     }

     .arrow.active::after {
        color: #28a745; /* Green arrowhead when active */
     }


     .processing-indicator {
         width: 50px;
         height: 50px;
         border: 5px solid #007bff;
         border-top-color: transparent;
         border-radius: 50%;
         animation: spin 1s linear infinite;
         margin-top: 20px;
         display: none; /* Initially hidden */
     }

     @keyframes spin {
         0% { transform: rotate(0deg); }
         100% { transform: rotate(360deg); }
     }


    .results-area {
        margin-top: 25px;
        padding-top: 25px;
        border-top: 2px solid #007bff; /* Stronger separator */
        text-align: center;
         opacity: 0; /* Start hidden */
         transform: translateY(20px); /* Start below */
         transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    }

     .results-area.visible {
         opacity: 1;
         transform: translateY(0);
     }


    .results-area h3 {
        color: #28a745; /* Green for success */
        margin-bottom: 20px;
    }
    .results-area p {
        font-size: 1.15em;
        margin-bottom: 12px;
        color: #495057;
    }
    .results-area p span {
        font-weight: bold; /* Make results stand out */
        color: #007bff;
         word-break: break-all; /* Prevent overflow for long addresses */
    }

    .explanation-section {
         transition: all 0.5s ease-in-out;
         max-width: 800px;
         margin: 20px auto;
    }

     .explanation-section h3 {
        margin-top: 25px;
        margin-bottom: 10px;
        color: #1565c0;
        text-align: right;
        border-bottom: 1px dotted #b0bec5;
        padding-bottom: 5px;
     }
     .explanation-section p, .explanation-section ul, .explanation-section ol {
         margin-bottom: 15px;
         text-align: right;
         color: #444;
         line-height: 1.8;
     }
     .explanation-section ul, .explanation-section ol {
         padding-right: 25px; /* Indent lists */
     }
     .explanation-section li {
        margin-bottom: 10px;
        line-height: 1.6;
     }

     /* Responsive adjustments */
     @media (max-width: 600px) {
         .process-flow {
             flex-direction: column; /* Stack elements vertically */
             align-items: stretch;
         }
          .step-container {
             width: 100%; /* Full width on small screens */
             margin: 8px 0;
         }
         .arrow {
             width: 3px;
             height: 40px; /* Vertical arrow */
             margin: 5px 0;
         }
         .arrow.right::after {
            content: '▼'; /* Down arrow */
             left: 50%;
             top: 100%;
            transform: translate(-50%, 0); /* Adjust position for down arrow */
         }
         .step-icon {
             width: 50px;
             height: 50px;
             font-size: 2em;
             padding: 10px;
         }
          .step-label {
             font-size: 0.85em;
          }
         button {
             font-size: 1.1em;
             padding: 12px;
         }
         .minting-simulation, .explanation-section {
             padding: 20px;
         }
     }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const mintButton = document.getElementById('mintButton');
        const gasFeeDisplay = document.getElementById('gasFeeDisplay');
        const simulationArea = document.getElementById('simulationArea');
        const resultsArea = document.getElementById('resultsArea');
        const tokenIDDisplay = document.getElementById('tokenIDDisplay');
        const ownerAddressDisplay = document.getElementById('ownerAddressDisplay');
        const toggleExplanationButton = document.getElementById('toggleExplanation');
        const explanationDiv = document.getElementById('explanation');
        const stepIcons = simulationArea.querySelectorAll('.step-icon');
        const arrows = simulationArea.querySelectorAll('.arrow');
        const processingIndicator = document.getElementById('processingIndicator');

        // Simulate Gas Fee calculation with a bit more variation and animation
        function calculateGasFee() {
             gasFeeDisplay.textContent = `...מחשב עלויות רשת...`;
             // Simulate calculation delay
             setTimeout(() => {
                 const minGas = 0.003; // Lower minimum for more realistic variation
                 const maxGas = 0.05; // Higher max for high traffic simulation
                 // Add some fluctuation based on a pseudo-random network state
                 const networkFactor = Math.sin(Date.now() / 10000) * 0.01 + 0.015; // Fluctuates between ~0.005 and ~0.025
                 const gas = (Math.random() * (maxGas - minGas) + minGas + networkFactor).toFixed(4);

                 // Determine a pseudo-network state message
                 let networkStatus = 'רגועה';
                 let feeColor = '#ff9800'; // Orange
                 if (parseFloat(gas) > 0.025) {
                      networkStatus = 'עמוסה';
                      feeColor = '#d32f2f'; // Red
                 } else if (parseFloat(gas) > 0.01) {
                     networkStatus = 'סבירה';
                     feeColor = '#ffb300'; // Darker Orange
                 }

                 gasFeeDisplay.textContent = `~${gas} ETH (רשת ${networkStatus} - סימולציה)`;
                 gasFeeDisplay.style.color = feeColor; // Change color based on fee
             }, 800); // Simulate a short calculation time
        }

        // Initial state setup: Hide elements that are not visible initially
        simulationArea.classList.add('hidden');
        resultsArea.classList.add('hidden');
        explanationDiv.classList.add('hidden'); // Hide explanation initially
        // Hide all animation steps and arrows initially
        stepIcons.forEach(icon => icon.classList.remove('active'));
        arrows.forEach(arrow => arrow.classList.remove('active'));


        calculateGasFee(); // Initial calculation on page load

        mintButton.addEventListener('click', async () => {
            // Basic validation (can be enhanced)
            const nftName = document.getElementById('nftName').value;
            const nftDescription = document.getElementById('nftDescription').value;
            if (!nftName || !nftDescription) {
                 alert('בבקשה הכניסו שם ותיאור לנכס ה-NFT.');
                 return;
            }


            // Reset simulation area and results before starting
            stepIcons.forEach(icon => icon.classList.remove('active'));
            arrows.forEach(arrow => arrow.classList.remove('active'));
            resultsArea.classList.add('hidden');
            resultsArea.classList.remove('visible');
            tokenIDDisplay.textContent = '...';
            ownerAddressDisplay.textContent = '...';
            simulationArea.classList.remove('hidden');
            simulationArea.classList.add('visible'); // Show simulation area during simulation
            processingIndicator.style.display = 'block'; // Show spinner


            // Simulate Minting Process
            mintButton.disabled = true; // Disable button during process
            mintButton.textContent = 'מנטט... נא להמתין...';
             mintButton.style.backgroundColor = '#ff9800'; // Change button color while processing

            const stepDelay = 1200; // milliseconds between steps
             const arrowDelay = stepDelay / 2; // Arrow halfway between steps

            // Animation sequence
             // Step 1: Data Packing
             await new Promise(resolve => setTimeout(resolve, stepDelay));
             stepIcons[0].classList.add('active');
             processingIndicator.style.display = 'none'; // Hide spinner

             // Arrow 1
             await new Promise(resolve => setTimeout(resolve, arrowDelay));
             arrows[0].classList.add('active');

             // Step 2: Transaction Created
             await new Promise(resolve => setTimeout(resolve, arrowDelay));
             stepIcons[1].classList.add('active');

             // Arrow 2
             await new Promise(resolve => setTimeout(resolve, arrowDelay));
             arrows[1].classList.add('active');

             // Step 3: Sent to Network
             await new Promise(resolve => setTimeout(resolve, arrowDelay));
             stepIcons[2].classList.add('active');
             processingIndicator.style.display = 'block'; // Show spinner again for network process

             // Arrow 3
             await new Promise(resolve => setTimeout(resolve, arrowDelay));
             arrows[2].classList.add('active');

             // Step 4: Verified on Blockchain
             await new Promise(resolve => setTimeout(resolve, arrowDelay * 2)); // Longer delay for blockchain confirmation
             stepIcons[3].classList.add('active');
             processingIndicator.style.display = 'none'; // Hide spinner

             // Arrow 4
             await new Promise(resolve => setTimeout(resolve, arrowDelay));
             arrows[3].classList.add('active');

             // Step 5: NFT is Born!
             await new Promise(resolve => setTimeout(resolve, arrowDelay));
             stepIcons[4].classList.add('active'); // Final step active

            // Simulate results appearance after animation
            await new Promise(resolve => setTimeout(resolve, stepDelay));

            const simulatedTokenID = Math.floor(Math.random() * 9999999999) + 100000; // Larger range
            const simulatedOwnerAddress = '0x' + Array(40).fill(0).map(() => Math.random().toString(16).charAt(2)).join(''); // Simulate ETH address

            tokenIDDisplay.textContent = simulatedTokenID;
            ownerAddressDisplay.textContent = simulatedOwnerAddress;
            resultsArea.classList.remove('hidden');
            resultsArea.classList.add('visible'); // Show results area with animation

            mintButton.disabled = false;
            mintButton.textContent = 'הפעל את המינטור!';
            mintButton.style.backgroundColor = '#007bff'; // Restore button color


            // Simulate a new gas fee for the next potential mint
             calculateGasFee();
        });

        // Toggle explanation visibility
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.classList.contains('hidden');
            if (isHidden) {
                explanationDiv.classList.remove('hidden');
                explanationDiv.classList.add('visible');
                toggleExplanationButton.textContent = 'הסתר הסבר טכני מפורט';
            } else {
                 // Add transition out effect if needed, currently instant hide
                explanationDiv.classList.add('hidden');
                 explanationDiv.classList.remove('visible');
                toggleExplanationButton.textContent = 'רוצים להבין איך זה עובד לעומק? הצגת הסבר טכני מפורט';
            }
        });
    });
</script>
```