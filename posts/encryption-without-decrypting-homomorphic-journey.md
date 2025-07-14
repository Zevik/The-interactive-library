---
title: "הצפנה בלי לפענח? מסע ויזואלי להבנת הצפנה הומומורפית"
english_slug: encryption-without-decrypting-homomorphic-journey
category: "טכנולוגיה / מדעי המחשב"
tags: [הצפנה, אבטחת מידע, קריפטוגרפיה, פרטיות, מחשוב ענן, הומומורפי]
---
# הצפנה בלי לפענח? מסע ויזואלי להבנת הצפנה הומומורפית

תארו לעצמכם תרחיש דרמטי: יש לכם נתונים סופר-סודיים שאתם חייבים לעבד, אבל הכוח החישובי היחיד שעומד לרשותכם נמצא אצל גורם חיצוני (הענן) שאתם לא סומכים עליו מספיק כדי לחשוף בפניו את הנתונים הגלויים. האם יש דרך לבצע חישובים על המידע הרגיש שלכם בזמן שהוא נשאר מוצפן כל הזמן?

כן, יש! הכירו את הצפנה הומומורפית - טכניקה קריפטוגרפית מהפכנית שמאפשרת לעשות בדיוק את זה. במילים פשוטות, היא מאפשרת לבצע פעולות מתמטיות על נתונים מוצפנים, כך שהתוצאה, לאחר פענוח, תהיה זהה לתוצאה שהייתה מתקבלת מביצוע אותן פעולות על הנתונים המקוריים הלא-מוצפנים. השרת שמבצע את החישובים לעולם אינו רואה את הנתונים הגלויים!

בואו נראה איך זה עובד בסימולציה אינטראקטיבית (פשטנית להמחשה):

<div class="homomorphic-demo">
    <div class="client-section">
        <h2>📍 הלקוח (אתם)</h2>
        <div class="input-area">
            <label for="num1">מספר סודי 1:</label>
            <input type="number" id="num1" value="5" min="1" max="10">
            <br>
            <label for="num2">מספר סודי 2:</label>
            <input type="number" id="num2" value="3" min="1" max="10">
            <br>
            <label for="operation">פעולה:</label>
            <select id="operation" disabled> <!-- Disable for simplicity in this demo -->
                <option value="add">חיבור (+)</option>
                <!-- <option value="multiply">כפל (*)</option> -->
            </select>
            <br>
            <button id="calculateBtn">🔐 הצפן ושלח לחישוב בענן</button>
        </div>

        <div class="client-steps">
            <div id="client-step-encrypt" class="step">
                <h3>שלב 1: הצפנה</h3>
                <p>המספרים הסודיים: <span id="client-n1" class="value"></span>, <span id="client-n2" class="value"></span></p>
                <p>מפתח הצפנה פנימי (סודי): <span id="client-offset" class="value key"></span></p>
                <p>הצפנה פשטנית: <span class="math">מספר + מפתח</span></p>
                <p>המספרים המוצפנים (נראים שונים לגמרי!):</p>
                <p>מוצפן 1: <span id="client-c1" class="value encrypted"></span></p>
                <p>מוצפן 2: <span id="client-c2" class="value encrypted"></span></p>
            </div>
            <div id="client-step-send" class="step">
                 <h3>שלב 2: שליחה לענן</h3>
                 <p class="sending">שולח את <span id="client-send-c1" class="value encrypted"></span> ו- <span id="client-send-c2" class="value encrypted"></span> לשרת בענן...</p>
            </div>
             <div id="client-step-receive" class="step">
                 <h3>שלב 5: קבלת תוצאה מוצפנת</h3>
                 <p class="receiving">קולט מהשרת את התוצאה המוצפנת: <span id="client-received-cr" class="value encrypted"></span></p>
            </div>
            <div id="client-step-decrypt" class="step">
                <h3>שלב 6: פענוח אצל הלקוח</h3>
                <p>התוצאה המוצפנת שהתקבלה: <span id="client-cr-decrypt" class="value encrypted"></span></p>
                <p>סכום מפתחות ההצפנה (משמש לפענוח): <span id="client-total-offset" class="value key"></span></p>
                <p>פענוח: <span class="math">תוצאה מוצפנת - סכום מפתחות</span></p>
                <p><strong>התוצאה הגלויה!</strong> <span id="client-dr" class="value result"></span></p>
            </div>
             <div id="client-step-final" class="step">
                <h3>שלב 7: אימות</h3>
                <p>התוצאה שפענחתי (<span id="client-final-dr" class="value result"></span>) אכן זהה לתוצאה שהייתי מצפה לקבל בחישוב רגיל (<span id="client-final-expected" class="value expected"></span> = <span id="client-final-n1" class="value"></span> + <span id="client-final-n2" class="value"></span>).</p>
                <p class="success">✅ המידע עובד בענן מבלי להיחשף!</p>
            </div>
        </div>
    </div>

    <div class="server-section">
        <h2>☁️ השרת (הענן)</h2>
         <div id="server-step-receive" class="step">
             <h3>שלב 3: קליטת נתונים מוצפנים</h3>
             <p class="receiving">קולט מהלקוח: <span id="server-received-c1" class="value encrypted"></span> ו- <span id="server-received-c2" class="value encrypted"></span></p>
             <p class="note">🤫 השרת רואה רק את המספרים המוצפנים. אין לו שום מידע על המספרים המקוריים או מפתח הפענוח!</p>
        </div>
        <div id="server-step-calculate" class="step">
            <h3>שלב 4: ביצוע פעולה על מוצפן בלבד</h3>
            <p class="calculating">מחשב את סכום המספרים ה*מוצפנים*:</p>
            <p><span id="server-calc-c1" class="value encrypted"></span> <span id="server-op-symbol" class="value op-symbol"></span> <span id="server-calc-c2" class="value encrypted"></span> = <span id="server-cr" class="value encrypted"></span></p>
            <p class="note">✨ השרת ביצע את הפעולה על המספרים המוצפנים בלבד, מבלי לפענח אותם לרגע.</p>
        </div>
         <div id="server-step-send" class="step">
             <h3>שלב 4.5: שליחת תוצאה מוצפנת</h3>
             <p class="sending">שולח את התוצאה המוצפנת (<span id="server-send-cr" class="value encrypted"></span>) חזרה ללקוח...</p>
        </div>
    </div>
</div>

<button id="toggleExplanationBtn">👇 מה קרה כאן בעצם? הצג הסבר מלא 👇</button>

<div id="explanation" style="display: none;">
    <h2>הצפנה הומומורפית - ההסבר המלא</h2>

    <h3>מהי הצפנה הומומורפית?</h3>
    הצפנה הומומורפית היא סוג של הצפנה המאפשרת לבצע פעולות חישוביות על מידע מוצפן מבלי לפענח אותו קודם. התוצאה של החישוב על המידע המוצפן תהיה זהה לתוצאה של החישוב על המידע הגלוי, לאחר שתפוענח. פירוש השם "הומומורפית" מגיע מיוונית ומשמעותו "אותה צורה" או "אותה מבנה", המתייחס לכך שמבנה הפעולות (חיבור/כפל) נשמר בין העולם הגלוי לעולם המוצפן.

    <h3>הבעיה שפותרת הצפנה הומומורפית</h3>
    בעידן הביג דאטה ומחשוב הענן, ארגונים ויחידים אוגרים כמויות עצומות של נתונים רגישים (רפואיים, פיננסיים, אישיים) ורוצים לעבד אותם באמצעות שירותי ענן או שירותי צד שלישי כדי לנצל את כוח העיבוד או האנליטיקה שלהם. הבעיה היא ששליחת הנתונים במצב גלוי (לא מוצפן) לצד שלישי חושפת אותם לסיכוני פרטיות ואבטחה חמורים. הצפנה הומומורפית מאפשרת לשלוח את הנתונים מוצפנים, לבצע עליהם את החישוב הנדרש בענן, ולקבל תוצאה מוצפנת בחזרה, אותה הלקוח יכול לפענח ולקבל את התשובה הנכונה - וכל זאת מבלי שהענן יצטרך לראות או לפענח את הנתונים המקוריים או את התוצאה הסופית.

    <h3>השוואה להצפנה רגילה</h3>
    בהצפנה רגילה (כמו AES), אם רוצים לבצע חישוב על נתונים מוצפנים, יש לפענח אותם קודם, לבצע את החישוב על הנתונים הגלויים, ואז להצפין מחדש את התוצאה אם רוצים לשמור על פרטיותה. זה דורש מהשרת או מצד שלישי שמעבד את הנתונים גישה למפתח הפענוח ולנתונים הגלויים בשלב כלשהו של התהליך, מה שפוגע בפרטיות. הצפנה הומומורפית מבטלת את הצורך הזה בשלב העיבוד על ידי שימוש בתכונות מתמטיות מיוחדות של שיטת ההצפנה.

    <h3>הרעיון הבסיסי מאחורי הדמו הפשטני:</h3>
    הדמו שראיתם למעלה מדגים עקרון **הומומורפיות חיבורית פשטנית ביותר**. נניח שיש לנו מספר <span class="math">n</span>. נצפין אותו על ידי הוספת "מפתח" סודי <span class="math">r</span>: <span class="math">E(n) = n + r</span>. אם נצפין שני מספרים, <span class="math">n1</span> ו-<span class="math">n2</span>, עם מפתחות שונים <span class="math">r1</span> ו-<span class="math">r2</span> בהתאמה:
    <span class="math">E(n1) = n1 + r1</span>
    <span class="math">E(n2) = n2 + r2</span>

    עכשיו, בואו נראה מה קורה אם השרת (שרואה רק את הערכים המוצפנים!) מחבר אותם:
    <span class="math">E(n1) + E(n2) = (n1 + r1) + (n2 + r2) = (n1 + n2) + (r1 + r2)</span>

    שימו לב! התוצאה המוצפנת שהשרת מקבל היא בדיוק הסכום של המספרים המקוריים (<span class="math">n1 + n2</span>) בתוספת סכום המפתחות (<span class="math">r1 + r2</span>).
    כשהלקוח מקבל בחזרה את התוצאה המוצפנת, הוא יודע מה היה סכום המפתחות שהשתמש בהם (<span class="math">r1 + r2</span>), ויכול פשוט לחסר אותו מהתוצאה המוצפנת כדי לקבל את הסכום המקורי:
    <span class="math">D(E(n1) + E(n2)) = (n1 + n2) + (r1 + r2) - (r1 + r2) = n1 + n2</span>

    הדמו הפשטני הזה עובד רק עבור חיבור והוא לחלוטין לא מאובטח בפועל (מפתחות אקראיים פשוטים לא מספיקים), אבל הוא ממחיש את הרעיון המרכזי: ניתן לבצע פעולה על ערכים מוצפנים ולקבל תוצאה שניתנת לפענוח לתוצאה הנכונה, מבלי שהגורם המחשב ראה את הערכים המקוריים או את התוצאה הסופית הגלויה. שיטות הומומורפיות אמיתיות משתמשות במתמטיקה מורכבת הרבה יותר, לרוב מבוססת על סריגים (lattices), כדי להשיג אבטחה ופונקציונליות רחבה יותר.

    <h3>סוגי הצפנה הומומורפית</h3>
    ישנם מספר סוגים של הצפנה הומומורפית, הנבדלים בסוג וכמות הפעולות שהם מאפשרים לבצע על נתונים מוצפנים:
    <ul>
        <li>**הצפנה הומומורפית חלקית (Partially Homomorphic Encryption - PHE):** מאפשרת לבצע סוג אחד בלבד של פעולה (או חיבור אינסופי פעמים, או כפל אינסופי פעמים) על הנתונים המוצפנים, אך לא שילוב של שניהם. דוגמאות כוללות את RSA (כפל) ואל-גמאל (ElGamal - כפל) או פאייה (Paillier - חיבור, דומה לעקרון בדמו אך מורכב יותר).</li>
        <li>**הצפנה הומומורפית כלשהי (Somewhat Homomorphic Encryption - SHE):** מאפשרת לבצע מספר מוגבל של סוגי פעולות (חיבור וכפל) על הנתונים המוצפנים, אך קיים גבול לעומק המעגל החישובי (כלומר, כמה פעולות שונות ניתן לשרשר). לאחר מספר מסוים של פעולות, ה"רעש" המתווסף להצפנה הופך גדול מדי ומפריע לפענוח תקין.</li>
        <li>**הצפנה הומומורפית מלאה (Fully Homomorphic Encryption - FHE):** המטרה הקדושה של התחום. מאפשרת לבצע **כל** סוג של פעולה חישובית (כלומר, כל מעגל בוליאני או אריתמטי) על הנתונים המוצפנים, מספר בלתי מוגבל של פעמים. זה מאפשר לבצע חישובים מורכבים מאוד על נתונים מוצפנים לחלוטין. פריצת הדרך המרכזית בתחום היתה עבודתו של קרייג ג'נטרי (Craig Gentry) ב-2009. מערכות FHE מודרניות משתמשות בטכניקה שנקראת "אתחול מחדש" (bootstrapping) כדי להקטין את ה"רעש" (או השגיאה) ולאפשר המשך החישובים.</li>
    </ul>

    <h3>אתגרים וחסרונות</h3>
    למרות הפוטנציאל העצום, הצפנה הומומורפית, ובפרט FHE, סובלת עדיין ממספר אתגרים משמעותיים המעכבים את אימוצה הנרחב:
    <ul>
        <li>**ביצועים:** חישובים על נתונים מוצפנים באמצעות FHE איטיים משמעותית (פי אלפים עד מיליונים) מחישובים על נתונים גלויים. הם דורשים גם נפח זיכרון גדול יותר.</li>
        <li>**מורכבות:** המערכות מורכבות מאוד לתכנון, הטמעה ושימוש נכון.</li>
        <li>**גודל הצפנה:** הטקסטים המוצפנים (ciphertext) גדולים בהרבה מהנתונים הגלויים המקוריים.</li>
    </ul>
    מחקר ופיתוח פעילים מתקיימים כדי לשפר את הביצועים ולהקטין את המורכבות. ישנן ספריות FHE בקוד פתוח (כמו SEAL של מיקרוסופט, HElib של IBM, או PALISADE) המאפשרות למפתחים להתנסות בטכנולוגיה זו.

    <h3>יישומים פוטנציאליים</h3>
    ככל שהטכנולוגיה תשתפר ותהפוך יעילה יותר, הצפנה הומומורפית צפויה להיות חיונית במגוון תחומים בהם פרטיות המידע היא קריטית:
    <ul>
        <li>**מחשוב ענן מאובטח לחלוטין:** עיבוד נתונים רגישים (כמו רשומות רפואיות, נתונים פיננסיים, מידע גנטי) בענן ללא חשיפתם לספק הענן, גם אם השרתים נפרצים.</li>
        <li>**פרטיות ברשתות נוירונים ובינה מלאכותית:** ביצוע אימון או הסקה על נתונים מוצפנים, או שימוש במודלים מוצפנים. מאפשר ניתוח נתונים רגישים ללא פגיעה בפרטיות.</li>
        <li>**ניתוח ביג דאטה תוך שמירה על פרטיות:** ביצוע שאילתות וניתוחים סטטיסטיים על מאגרי נתונים גדולים מוצפנים.</li>
        <li>**שיתוף פעולה מאובטח:** מספר צדדים יכולים לשתף פעולה בחישוב על הנתונים המשולבים שלהם (למשל, סטטיסטיקה על נתונים מכמה בתי חולים) מבלי שצד כלשהו ילמד על הנתונים הגלויים של צד אחר.</li>
        <li>**הצבעה אלקטרונית מאובטחת:** הבטחת פרטיות ההצבעה תוך כדי אפשרות לבצע חישוב על הקולות המוצפנים כדי לקבל את התוצאה הסופית.</li>
    </ul>
    הצפנה הומומורפית היא תחום מחקר פעיל ומרתק שמבטיח עתיד שבו פרטיות המידע והיכולת לעבד אותו אינם סותרים עוד.
</div>

<style>
    /* General Styles */
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        color: #333;
    }

    h1, h2, h3 {
        color: #1a2a3a;
        margin-bottom: 15px;
    }

    p {
        margin-bottom: 10px;
    }

    .math {
        font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
        background-color: #eef;
        padding: 2px 5px;
        border-radius: 3px;
        font-style: normal; /* Override italic for .note */
    }

    /* Demo Layout */
    .homomorphic-demo {
        display: flex;
        justify-content: center;
        align-items: stretch; /* Ensure sections stretch to match height */
        gap: 20px; /* Space between sections */
        padding: 25px;
        background: linear-gradient(to bottom right, #e0f7fa, #f0f4f8); /* Subtle gradient */
        border-radius: 12px;
        margin: 30px 0;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    }

    .client-section, .server-section {
        flex: 1; /* Allows sections to grow */
        min-width: 320px; /* Ensure minimum width for readability */
        padding: 20px;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
        display: flex; /* Use flex to arrange inner content */
        flex-direction: column; /* Stack inner elements */
    }

    .client-section {
        border: 2px solid #007bff; /* Client primary color */
        color: #0056b3;
    }

    .server-section {
        border: 2px solid #28a745; /* Server success color */
         color: #1e7e34;
    }

    .client-section h2, .server-section h2 {
        text-align: center;
        margin-top: 0;
        margin-bottom: 20px;
        color: inherit; /* Use parent color */
    }

    /* Input Area */
    .input-area {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
        border: 1px dashed #ccc;
    }

    .input-area label {
        display: inline-block;
        width: 120px; /* Increased width for labels */
        margin-bottom: 8px;
        font-weight: bold;
        color: #555;
    }

    .input-area input[type="number"],
    .input-area select {
        padding: 8px;
        border: 1px solid #ced4da;
        border-radius: 5px;
        margin-bottom: 8px;
        width: calc(100% - 140px); /* Adjust width considering label */
        box-sizing: border-box; /* Include padding in width */
    }

     .input-area select {
         width: auto; /* Auto width for select */
         min-width: 100px;
     }

    /* Buttons */
    #calculateBtn, #toggleExplanationBtn {
        display: block;
        width: auto; /* Allow button width to adapt */
        margin: 20px auto 10px auto; /* Center button */
        padding: 12px 20px;
        font-size: 1.1em;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    #calculateBtn {
        background-color: #007bff;
        color: white;
    }

    #calculateBtn:hover {
        background-color: #0056b3;
        transform: translateY(-2px);
    }
     #calculateBtn:active {
        transform: translateY(0);
     }


     #toggleExplanationBtn {
        background-color: #6c757d;
        color: white;
        margin: 30px auto; /* Center below demo */
     }

     #toggleExplanationBtn:hover {
         background-color: #5a6268;
         transform: translateY(-2px);
     }
      #toggleExplanationBtn:active {
        transform: translateY(0);
     }


    /* Steps */
    .client-steps {
         margin-top: 20px;
         border-top: 1px solid #eee;
         padding-top: 15px;
    }

    .step {
        background-color: #f8f9fa; /* Light background for steps */
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
        border: 1px solid #e9ecef;
        opacity: 0; /* Start hidden */
        transform: translateY(20px); /* Start slightly below */
        transition: opacity 0.5s ease-out, transform 0.5s ease-out, background-color 0.3s ease;
        position: relative; /* Needed for pseudo-elements or badges */
    }

    .step.active {
         opacity: 1;
         transform: translateY(0);
         background-color: #e2f3ff; /* Highlight active step for client */
    }
    .server-section .step.active {
        background-color: #d4edda; /* Highlight active step for server */
    }


    .step h3 {
        margin-top: 0;
        margin-bottom: 10px;
        color: #0056b3; /* Client color */
        border-bottom: 1px solid #dee2e6;
        padding-bottom: 8px;
    }
     .server-section .step h3 {
        color: #1e7e34; /* Server color */
     }


    .step p {
        margin: 8px 0;
        font-size: 1em;
        color: #555;
    }

    .step p strong {
        color: #333;
    }

    .note {
        font-style: italic;
        color: #666;
        font-size: 0.9em;
        margin-top: 10px;
        padding-top: 5px;
        border-top: 1px dashed #ced4da;
    }

    /* Value Highlighting */
    .value {
        font-weight: bold;
        color: #007bff; /* Client primary color */
        transition: color 0.3s ease;
    }

    .server-section .value {
         color: #28a745; /* Server success color */
    }

    .value.encrypted {
        color: #ffc107; /* Warning/Encrypted color */
    }
     .value.encrypted:hover {
         color: #d39e00;
     }

     .value.key {
         color: #6f42c1; /* Purple for keys/offsets */
     }
     .value.key:hover {
          color: #5a32a1;
     }

     .value.result {
         color: #dc3545; /* Danger/Result color */
         font-size: 1.2em;
     }
      .value.result:hover {
          color: #c82333;
      }

     .value.expected {
          color: #17a2b8; /* Info color for expected value */
     }
      .value.expected:hover {
           color: #138496;
      }

     .value.op-symbol {
         color: #666; /* Gray for operator */
     }


    /* Animation Indicators */
    .sending, .receiving, .calculating {
        position: relative;
        padding-left: 25px; /* Make space for icon */
    }

    .sending::before, .receiving::before, .calculating::before {
        content: '...'; /* Simple indicator */
        position: absolute;
        left: 0;
        font-weight: bold;
        animation: pulse 1.5s infinite ease-in-out;
    }
    .sending::before { content: '➡️'; } /* Sending arrow */
    .receiving::before { content: '⬅️'; } /* Receiving arrow */
    .calculating::before { content: '⚙️'; } /* Gear icon for calculating */


    @keyframes pulse {
        0% { opacity: 0.5; }
        50% { opacity: 1; }
        100% { opacity: 0.5; }
    }


    /* Final Step Success */
    .success {
        font-weight: bold;
        color: #28a745; /* Success color */
        text-align: center;
        font-size: 1.1em;
        margin-top: 20px;
        padding-top: 10px;
        border-top: 2px dashed #28a745;
    }


    /* Explanation Section */
    #explanation {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid #ccc;
        border-radius: 10px;
        background-color: #fff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    }

    #explanation h2, #explanation h3 {
        color: #1a2a3a;
    }

    #explanation ul {
        list-style: disc;
        margin-left: 25px;
        padding-left: 0;
    }

    #explanation li {
        margin-bottom: 8px;
    }

    /* Responsive Adjustments */
    @media (max-width: 768px) {
        .homomorphic-demo {
            flex-direction: column;
            align-items: center;
        }

        .client-section, .server-section {
            width: 100%; /* Full width on small screens */
            margin: 10px 0;
        }

         .input-area label {
             width: 100%;
             margin-bottom: 0;
         }
         .input-area input[type="number"],
         .input-area select {
             width: 100%;
             margin-bottom: 10px;
         }
    }

     /* Initial state - hide all steps */
     .client-steps .step, .server-section .step {
        display: none; /* Managed by JS for animation */
     }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const num1Input = document.getElementById('num1');
        const num2Input = document.getElementById('num2');
        const operationSelect = document.getElementById('operation'); // Disabled in this version
        const calculateBtn = document.getElementById('calculateBtn');
        const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
        const explanationDiv = document.getElementById('explanation');

        // Client elements
        const clientN1 = document.getElementById('client-n1');
        const clientN2 = document.getElementById('client-n2');
        const clientOffset = document.getElementById('client-offset');
        const clientC1 = document.getElementById('client-c1');
        const clientC2 = document.getElementById('client-c2');
        const clientSendC1 = document.getElementById('client-send-c1');
        const clientSendC2 = document.getElementById('client-send-c2');
        const clientReceivedCr = document.getElementById('client-received-cr');
        const clientCrDecrypt = document.getElementById('client-cr-decrypt');
        const clientTotalOffset = document.getElementById('client-total-offset');
        const clientDr = document.getElementById('client-dr');
        const clientFinalDr = document.getElementById('client-final-dr');
        const clientFinalExpected = document.getElementById('client-final-expected');
         const clientFinalN1 = document.getElementById('client-final-n1');
         const clientFinalN2 = document.getElementById('client-final-n2');


        // Server elements
        const serverReceivedC1 = document.getElementById('server-received-c1');
        const serverReceivedC2 = document.getElementById('server-received-c2');
        const serverCalcC1 = document.getElementById('server-calc-c1');
        const serverCalcC2 = document.getElementById('server-calc-c2');
        const serverOpSymbol = document.getElementById('server-op-symbol');
        const serverCr = document.getElementById('server-cr');
        const serverSendCr = document.getElementById('server-send-cr');

        // Step containers
        const clientEncryptStep = document.getElementById('client-step-encrypt');
        const clientSendStep = document.getElementById('client-step-send');
        const clientReceiveStep = document.getElementById('client-step-receive');
        const clientDecryptStep = document.getElementById('client-step-decrypt');
        const clientFinalStep = document.getElementById('client-step-final');
        const serverReceiveStep = document.getElementById('server-step-receive');
        const serverCalculateStep = document.getElementById('server-step-calculate');
        const serverSendStep = document.getElementById('server-step-send');

        const allSteps = [
            { element: clientEncryptStep, delay: 500 },
            { element: clientSendStep, delay: 1500 },
            { element: serverReceiveStep, delay: 1000 },
            { element: serverCalculateStep, delay: 1500 },
            { element: serverSendStep, delay: 1000 },
            { element: clientReceiveStep, delay: 1000 },
            { element: clientDecryptStep, delay: 1500 },
            { element: clientFinalStep, delay: 1000 }
        ];


        function hideAllSteps() {
            document.querySelectorAll('.step').forEach(step => {
                step.style.display = 'none';
                step.classList.remove('active');
                step.style.opacity = '0';
                step.style.transform = 'translateY(20px)';
            });
        }

        function showStep(stepElement) {
             stepElement.style.display = 'block';
             // Force reflow to make transition work on display change
             stepElement.offsetHeight;
             stepElement.classList.add('active');
        }

        function animateSequence(steps) {
            let totalDelay = 0;
            steps.forEach((step, index) => {
                totalDelay += step.delay;
                setTimeout(() => {
                    // Deactivate previous step visually
                    if (index > 0) {
                         steps[index-1].element.classList.remove('active');
                    }
                    showStep(step.element);
                }, totalDelay);
            });
             // Deactivate last step after a brief moment
             setTimeout(() => {
                 if (steps.length > 0) {
                    steps[steps.length-1].element.classList.remove('active');
                 }
             }, totalDelay + steps[steps.length-1].delay + 500);

        }


        calculateBtn.addEventListener('click', () => {
            hideAllSteps();
            calculateBtn.disabled = true; // Prevent double clicking during animation

            const num1 = parseInt(num1Input.value);
            const num2 = parseInt(num2Input.value);
            const operation = operationSelect.value; // Currently only 'add' is an option

            if (isNaN(num1) || isNaN(num2)) {
                alert("Please enter valid numbers.");
                calculateBtn.disabled = false;
                return;
            }

            // Simple additive homomorphic simulation (like Paillier for addition)
            // E(n) = n + r + BASE_OFFSET (simplified)
            // E(n1) + E(n2) = (n1 + r1 + BASE) + (n2 + r2 + BASE) = (n1+n2) + (r1+r2) + 2*BASE
            // Decrypt: EncryptedSum - (r1+r2) - 2*BASE = n1+n2
            // Let's use a consistent large offset and random parts for demonstration

            const BASE_OFFSET_MAGNITUDE = 10000; // A larger base to make encrypted values look significantly different
            const randomPart1 = Math.floor(Math.random() * 1000); // Larger random part
            const randomPart2 = Math.floor(Math.random() * 1000);

            const offset1 = BASE_OFFSET_MAGNITUDE + randomPart1; // Simulate random offset 1
            const offset2 = BASE_OFFSET_MAGNITUDE + randomPart2; // Simulate random offset 2

            const totalOffset = offset1 + offset2; // Total offset needed for decryption (sum of client offsets)


            // --- Client Side: Encryption ---
            // Encrypted value is the original number + its offset
            const encrypted1 = num1 + offset1;
            const encrypted2 = num2 + offset2;

            clientN1.textContent = num1;
            clientN2.textContent = num2;
            clientOffset.textContent = `${offset1} (עבור ${num1}), ${offset2} (עבור ${num2})`; // Show individual offsets
            clientC1.textContent = encrypted1;
            clientC2.textContent = encrypted2;


            // --- Server Side: Calculation on Encrypted Data ---
            let encryptedResult;
            let opSymbol;
            if (operation === 'add') {
                // Homomorphic addition simulation: Add the encrypted values
                encryptedResult = encrypted1 + encrypted2;
                opSymbol = '+';
            }
            // Note: A real Paillier system for addition involves modulo arithmetic and properties
            // related to the public/private key pair. This demo simplifies greatly.

            serverCalcC1.textContent = encrypted1;
            serverCalcC2.textContent = encrypted2;
            serverOpSymbol.textContent = opSymbol;
            serverCr.textContent = encryptedResult;


            // --- Client Side: Decryption ---
            // Decrypting the sum: The server's result is (n1 + offset1) + (n2 + offset2) = (n1+n2) + (offset1+offset2).
            // The client knows offset1 and offset2, so it knows their sum (totalOffset).
            // Decrypted result = EncryptedResult - totalOffset
            const decryptedResult = encryptedResult - totalOffset;


            clientCrDecrypt.textContent = encryptedResult;
            clientTotalOffset.textContent = totalOffset;
            clientDr.textContent = decryptedResult;

            // --- Client Side: Verification ---
            const expectedResult = num1 + num2; // The real answer
            clientFinalDr.textContent = decryptedResult;
            clientFinalExpected.textContent = expectedResult;
            clientFinalN1.textContent = num1;
            clientFinalN2.textContent = num2;


             // --- Animate the sequence ---

             // Populate text for steps before showing
             clientSendC1.textContent = encrypted1;
             clientSendC2.textContent = encrypted2;
             serverReceivedC1.textContent = encrypted1;
             serverReceivedC2.textContent = encrypted2;
             serverSendCr.textContent = encryptedResult;
             clientReceivedCr.textContent = encryptedResult;


            animateSequence(allSteps);

             // Re-enable button after animation finishes (adjust delay based on total animation time)
             const totalAnimationTime = allSteps.reduce((sum, step) => sum + step.delay, 0) + allSteps[allSteps.length - 1].delay + 500;
             setTimeout(() => {
                calculateBtn.disabled = false;
             }, totalAnimationTime);


        });

        toggleExplanationBtn.addEventListener('click', () => {
            if (explanationDiv.style.display === 'none') {
                explanationDiv.style.display = 'block';
                toggleExplanationBtn.textContent = '👆 הסתר הסבר מלא 👆';
            } else {
                explanationDiv.style.display = 'none';
                toggleExplanationBtn.textContent = '👇 מה קרה כאן בעצם? הצג הסבר מלא 👇';
            }
        });

        // Initialize the demo view
         hideAllSteps();
         toggleExplanationBtn.textContent = '👇 מה קרה כאן בעצם? הצג הסבר מלא 👇'; // Set initial button text
         operationSelect.value = 'add'; // Ensure default is add
    });
</script>
```