---
title: "מוח על סכין: החלטות קריטיות בחדר הניתוח"
english_slug: brain-on-the-knife-critical-decisions-in-the-operating-room
category: "מדעי המוח"
tags: ["ניתוח מוח", "קבלת החלטות", "רפואה", "סימולציה", "ניהול סיכונים"]
---
# מוח על סכין: החלטות קריטיות בחדר הניתוח

דמיינו שאתם עומדים **מעל מוח אנושי**. חייו של אדם תלויים כעת בידיכם. גידול מאיים נראה בהדמיה, אבל הסרתו עלולה לגרום לנזק בלתי הפיך. איך מנתחי מוח מנוסים ניגשים להחלטות גורליות כאלה, תחת לחץ עצום, עם מידע חלקי וסיכונים ברורים?

## סימולציה: האתגר שעל השולחן הניתוחי

הצטרפו אלינו לרגע לחדר הניתוח. אתם עומדים בפני דילמה קריטית כמנתחי מוח. לפניכם מקרה היפותטי, המבוסס על מקרים מהחיים:

<div id="simulation-app" class="app-container">
    <div class="case-info">
        <h3><i class="icon brain-icon"></i> פרטי המקרה הרפואי:</h3>
        <p><strong>מטופל:</strong> גבר, בן 68.</p>
        <p><strong>מצב כללי:</strong> סובל ממחלות רקע כרוניות המשפיעות על סיכויי החלמה מניתוח גדול.</p>
        <div class="image-placeholder">
            <div class="brain-outline">
                <div class="tumor-location" data-location="frontal"></div>
                <div class="speech-area" data-location="broca"></div>
            </div>
            <p class="image-caption">מיקום הגידול (אדום) בסמוך לאזור הדיבור (צהוב).</p>
        </div>
        <p><strong>הדמיה (MRI):</strong></p>
        <ul>
            <li><strong>גודל הגידול:</strong> בינוני (כ-3 ס"מ).</li>
            <li><strong>מיקום:</strong> באונה הפרונטלית (מצחית), **קרוב מאוד** לאזור האחראי על דיבור מוטורי (Broca's area).</li>
            <li><strong>אופי הגידול (חשד גבוה):</strong> נראה אגרסיבי ובעל פוטנציאל פלישה, אך דרושה ביופסיה לאישור סופי.</li>
        </ul>
        <p><strong>דחיפות:</strong> הגידול גורם לסימפטומים ברורים (קשיי דיבור קלים) ומצבו של המטופל מתדרדר באיטיות. ישנו חלון זמנים סביר לקבלת החלטה מושכלת, אך לא מדובר במקרה חירום שמצריך פעולה מיידית ללא הכנה.</p>
    </div>

    <div class="decision-section">
        <h3><i class="icon scale-icon"></i> הדילמה הכירורגית:</h3>
        <p>בהתחשב במכלול הנתונים – מיקום הגידול הרגיש, מצב המטופל ואופי הגידול המשוער – איזו גישת טיפול תמליצו?</p>
        <div class="options">
            <label class="option-label">
                <input type="radio" name="decision" value="full-removal">
                <span class="option-text">הסרת הגידול בשלמותו:</span><br>
                <span class="option-details">שאיפה לריפוי מלא וסיכויי הישנות נמוכים, אך סיכון **גבוה משמעותית** לנזק נוירולוגי קבוע, בעיקר פגיעה חמורה בדיבור (אפזיה).</span>
            </label>
            <label class="option-label">
                <input type="radio" name="decision" value="partial-removal">
                <span class="option-text">הסרה חלקית (Debulking):</span><br>
                <span class="option-details">הקלה בסימפטומים והאטת קצב הגידול. סיכון **נמוך יותר** לנזק נוירולוגי מיידי, אך סיכוי **גבוה** לחזרת הגידול וצורך ודאי בטיפולים נוספים (הקרנות/כימותרפיה).</span>
            </label>
            <label class="option-label">
                <input type="radio" name="decision" value="conservative">
                <span class="option-text">טיפול שמרני (מעקב בלבד, אולי טיפולים לא ניתוחיים):</span><br>
                <span class="option-details">לא מנסים להסיר את הגידול בניתוח כלל. **נמנעים לחלוטין** מסיכון ניתוחי, אך הגידול צפוי להמשיך לגדול ולהחמיר את הסימפטומים, עם פרוגנוזה **פחות טובה** לטווח הארוך.</span>
            </label>
        </div>
        <button id="submit-decision">קבל החלטה גורלית</button>
    </div>

    <div id="result-section" class="result-section" style="display: none;">
        <h3><i class="icon flask-icon"></i> התוצאה במבחן המציאות:</h3>
        <p id="result-text"></p>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">הצג את חדר המחשבות של המנתח</button>

<div id="explanation" class="explanation-container" style="display: none;">
    <h2>הבנת תהליך קבלת ההחלטות בניתוחי מוח: מעבר לסכין</h2>

    <p>קבלת החלטה על ניתוח מוח אינה רק שאלה של טכניקה כירורגית, אלא תהליך רפואי ואנושי מורכב ביותר. הוא כרוך באיזון עדין ומתוח בין תועלת פוטנציאלית מקסימלית לסיכונים מוחשיים וחמורים. הסימולציה שחוויתם מדגימה את הדילמות האתיות והקליניות העומדות בפני מנתחים וצוותים רפואיים בכל יום.</p>

    <h3><i class="icon brain-outline-icon"></i> אתגר ניתוחי המוח: אדריכלות עדינה ורגישה</h3>
    <p>המוח הוא הפיסגה המורכבת ביותר של הביולוגיה. כל מילימטר מעוקב בו יכול להיות קריטי לתפקודים יסודיים כמו דיבור, תנועה, זיכרון ואף אישיות. ניתוח באזור זה דורש לא רק מיומנות כירורגית יוצאת דופן, אלא גם הבנה מעמיקה של האנטומיה והפיזיולוגיה המוחית, ושימוש בטכנולוגיות העלית החדישות ביותר כדי למזער כל פגיעה אפשרית ברקמה בריאה הסמוכה ל"אזור המטרה" (הגידול, כלי הדם הפגום וכו').</p>

    <h3><i class="icon factors-icon"></i> הגורמים על שולחן הדיונים: מעבר לגידול עצמו</h3>
    <ul>
        <li><strong>מיקום וגודל הגידול:</strong> גידולים הממוקמים באזורים "שקטים" (אזורים שפגיעה בהם פחות קטלנית לטווח הקצר) או כאלה שהם קטנים ומתוחמים, קלים יותר להסרה ועם סיכון נמוך יותר מגידולים גדולים, מפושטים או כאלה הסמוכים למרכזי תפקוד קריטיים (כמו אלו האחראים על שפה, תנועה, ראייה, תפקודים קוגניטיביים).</li>
        <li><strong>סוג הגידול (היסטולוגיה):</strong> האם זה גידול שפיר שצומח לאט ואינו פולש לרקמה סמוכה (לעיתים מספיק מעקב), או גידול ממאיר ואגרסיבי שנוטה להתפשט במהירות ודורש לרוב גישה אגרסיבית יותר המשלבת ניתוח עם טיפולים אונקולוגיים נוספים (הקרנות, כימותרפיה, אימונותרפיה)?</li>
        <li><strong>גיל ומצב בריאות כללי של המטופל:</strong> מטופלים צעירים ובריאים יותר לרוב מגיבים טוב יותר לניתוח ומתאוששים במהירות רבה יותר. מחלות רקע משמעותיות, במיוחד בגיל מבוגר, יכולות להעלות באופן משמעותי את הסיכון הניתוחי הכללי ואת סיכויי ההחלמה.</li>
        <li><strong>מיפוי תפקודי ותפקודים קריטיים בסמוך:</strong> באמצעות טכניקות מתקדמות כמו fMRI, טרקטוגרפיה (הדמיית סיבים עצביים), מיפוי מוחי תוך-ניתוחי (כמו ב-Awake Craniotomy) – בה המטופל ער ומשתף פעולה במהלך חלק מהניתוח – המנתח יכול לזהות במדויק את מיקום האזורים התפקודיים החיוניים ולתכנן את הניתוח כך שימנע (או ימזער ככל האפשר) פגיעה בהם. הקרבה והחשיבות של אזורים אלו משפיעה ישירות על גבולות הניתוח ועל מידת האגרסיביות האפשרית.</li>
    </ul>

    <h3><i class="icon balance-icon"></i> ניתוח סיכונים מול תועלות: הלב הפועם של ההחלטה</h3>
    <p>זוהי ליבת הדילמה, נקודת שיווי המשקל המתוחה. הסרה מלאה של הגידול מציעה את הסיכוי הטוב ביותר לשליטה ארוכת טווח במחלה ואף לריפוי, אך היא טומנת בחובה את הסיכון הגבוה ביותר לגרום לנזק נוירולוגי קבוע שיפגע באופן משמעותי באיכות חייו של המטופל – שיתוק חלקי, אובדן יכולת הדיבור (אפזיה), פגיעה קוגניטיבית או שינויים התנהגותיים. מנגד, הסרה חלקית או טיפול שמרני עשויים להפחית את הסיכון המיידי הזה, אך לרוב מותירים מחלה משמעותית שסביר שתתקדם, תחזור במהירות, ותשאיר את המטופל במצב רפואי גרוע יותר ואף עם סימפטומים חמורים יותר לטווח הארוך. ההחלטה אינה שחור ולבן, אלא איזון עדין זה, המבוסס על כל הנתונים הרפואיים וכן על ערכיו, רצונותיו וסדרי העדיפויות של המטופל ומשפחתו (במידה שהוא שותף בהחלטה).</p>

    <h3><i class="icon uncertainty-icon"></i> התמודדות עם אי-ודאות: ריקוד על חבל דק</h3>
    <p>גם עם כל המידע, הטכנולוגיה והניסיון, תמיד קיימת רמה מסוימת של אי-ודאות בניתוחי מוח. מיפוי מוחי אינו מדויק ב-100%, התנהגות גידולים ספציפיים יכולה להפתיע, והתגובה הייחודית של מוח מסוים לטראומה הניתוחית משתנה מאדם לאדם. מנתחים חייבים לקבל החלטות קריטיות על בסיס המידע הטוב ביותר הקיים באותו רגע, תוך הכרה מפורשת באי-הודאות המובנית, והכנה מנטלית ומעשית לתרחישים בלתי צפויים.</p>

    <h3><i class="icon technology-icon"></i> הטכנולוגיה ככלי עזר, לא תחליף: ניסיון וידע מול מכונות</h3>
    <p>שנים רבות של ניסיון קליני מעצבות את האינטואיציה המנתחית, מאפשרות זיהוי דפוסים, הערכת סיכונים מדויקת יותר, והתמודדות יעילה עם אתגרים מורכבים ולא צפויים בזמן אמת במהלך הניתוח. טכנולוגיות מתקדמות – נוויגציה כירורגית (מעין GPS תלת-ממדי של המוח), הדמיה תוך-ניתוחית (כמו אולטרסאונד או MRI ניתוחי), מיקרוסקופים אופרטיביים מדויקים, וטכניקות מיפוי מוחי – אינן מחליפות את שיקול הדעת האנושי, אלא מספקות למנתח כלים חיוניים לקבלת החלטות מושכלות ומדויקות יותר בזמן אמת ולהגדלת סיכויי ההצלחה תוך מזעור סיכונים.</p>

    <h3><i class="icon ethics-icon"></i> אחריות וכובד משקל: ההיבט האנושי של הניתוח</h3>
    <p>מעבר להיבטים הטכניים והרפואיים היבשים, ישנם היבטים אתיים ופסיכולוגיים בעלי משקל עצום. המנתח נושא באחריות עצומה לגורל המטופל. תהליך קבלת ההחלטה חייב לכלול תקשורת שקופה, אמפתית וכנה עם המטופל ומשפחתו, הסברת הסיכונים והתועלות בצורה ברורה, ומתן אפשרות (ככל שניתן) למטופל עצמו להיות שותף פעיל בהחלטה הנוגעת לגופו וחייו. ההתמודדות האישית של הצוות הרפואי עם הלחץ, הסיכון, וההשלכות הפוטנציאליות של כל החלטה היא חלק בלתי נפרד וקשה מהמקצוע.</p>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.7;
        margin: 0 auto;
        max-width: 800px;
        padding: 30px 20px;
        background-color: #eef2f7; /* Light blue-gray background */
        color: #333;
        direction: rtl; /* Right-to-left for Hebrew */
        text-align: right;
    }

    h1, h2, h3 {
        color: #1a3a5f; /* Darker blue */
        font-weight: 700;
        margin-bottom: 15px;
    }

    h1 {
        font-size: 2em;
        text-align: center;
        margin-bottom: 30px;
    }

    h2 {
        font-size: 1.6em;
        border-bottom: 2px solid #a0c4ff; /* Lighter blue border */
        padding-bottom: 5px;
        margin-top: 30px;
    }

    h3 {
         font-size: 1.3em;
         color: #0056b3; /* Medium blue */
         display: flex;
         align-items: center;
         margin-bottom: 10px;
    }

    h3 .icon {
        margin-left: 10px; /* Space between icon and text */
        font-size: 1.2em; /* Adjust icon size */
    }

    .app-container, .explanation-container {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 30px;
        border: 1px solid #d0d9e6; /* Subtle border */
    }

    .case-info, .decision-section {
        margin-bottom: 25px;
        padding-bottom: 20px;
        border-bottom: 1px solid #eee;
    }

    .case-info ul {
        list-style: none; /* Remove default list style */
        padding: 0;
        margin: 15px 0;
    }

    .case-info li {
        margin-bottom: 8px;
        padding-right: 20px; /* Space for custom bullet */
        position: relative;
    }

    .case-info li:before {
        content: '•'; /* Custom bullet point */
        color: #007bff; /* Blue bullet */
        font-size: 1.2em;
        position: absolute;
        right: 0;
        top: 0;
    }


    .image-placeholder {
        width: 100%;
        max-width: 300px;
        margin: 20px auto;
        position: relative;
        background-color: #f0f4f8; /* Light background for brain */
        border-radius: 8px;
        padding: 20px;
        box-shadow: inset 0 0 8px rgba(0,0,0,0.05);
    }

    .brain-outline {
        width: 100%;
        padding-top: 80%; /* Aspect ratio */
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 160"><path fill="none" stroke="%23a0c4ff" stroke-width="4" d="M100 10 C150 0, 190 40, 190 80 C190 120, 160 155, 100 155 C40 155, 10 120, 10 80 C10 40, 50 0, 100 10 Z M100 10 C100 40, 50 60, 50 80 C50 100, 70 120, 100 120 C130 120, 150 100, 150 80 C150 60, 100 40, 100 10 Z" /></svg>');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        position: absolute;
        top: 0;
        left: 0;
    }

     .tumor-location, .speech-area {
        position: absolute;
        border-radius: 50%;
        opacity: 0.8;
        transform: translate(-50%, -50%); /* Center based on element size */
        animation: pulse 1.5s infinite alternate ease-in-out; /* Pulsing animation */
    }

    .tumor-location[data-location="frontal"] {
        width: 15%; height: 15%;
        background-color: #e74c3c; /* Red */
        top: 30%; right: 40%; /* Approximate frontal location in the simplified SVG */
    }

     .speech-area[data-location="broca"] {
        width: 10%; height: 10%;
        background-color: #f39c12; /* Orange/Yellow */
        top: 35%; right: 45%; /* Approximate Broca's location */
        animation-delay: 0.5s; /* Offset pulse */
    }

    .image-caption {
        text-align: center;
        font-size: 0.9em;
        color: #555;
        margin-top: 160px; /* Push caption below the SVG area */
    }


    .options label.option-label {
        display: block;
        background-color: #f8f9fa; /* Light background for options */
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 12px;
        cursor: pointer;
        transition: all 0.3s ease;
        position: relative;
        padding-right: 40px; /* Space for radio button */
    }

    .options label.option-label:hover {
        background-color: #e9ecef;
        border-color: #007bff;
    }

    .options input[type="radio"] {
        position: absolute;
        right: 15px;
        top: 50%;
        transform: translateY(-50%);
        margin: 0; /* Remove default margin */
        width: 20px; /* Make radio button target larger */
        height: 20px;
        z-index: 1; /* Ensure clickable */
    }

    .options input[type="radio"]:checked + .option-text {
        color: #0056b3;
        font-weight: 700;
    }
     .options input[type="radio"]:checked ~ .option-details {
        color: #007bff;
     }


    .option-text {
        font-weight: 700;
        display: block; /* Ensure text is on its own line */
        margin-bottom: 5px;
    }

    .option-details {
        font-size: 0.9em;
        color: #555;
    }


    #submit-decision, .toggle-button {
        display: inline-block;
        background-color: #007bff;
        color: white;
        padding: 12px 25px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 17px;
        font-weight: 700;
        transition: background-color 0.3s ease, transform 0.1s ease;
        margin-top: 15px;
        text-align: center;
        width: auto; /* Allow button to size to content */
    }

    #submit-decision:hover, .toggle-button:hover {
        background-color: #0056b3;
    }
     #submit-decision:active, .toggle-button:active {
        transform: scale(0.98); /* Press effect */
     }

    .result-section {
        margin-top: 25px;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 8px;
        background-color: #f0f0f0; /* Default background */
        opacity: 0; /* Start hidden for animation */
        transform: translateY(20px); /* Start slightly lower */
        animation: fadeInResult 0.5s ease-out forwards; /* Animation */
    }

     .result-section.success {
        background-color: #d4edda; /* Light green */
        border-color: #c3e6cb;
        color: #155724; /* Dark green */
    }

    .result-section.warning {
        background-color: #fff3cd; /* Light yellow */
        border-color: #ffeeba;
        color: #856404; /* Dark yellow */
    }

    .result-section.danger {
        background-color: #f8d7da; /* Light red */
        border-color: #f5c6cb;
        color: #721c24; /* Dark red */
    }

    .result-section.info {
        background-color: #d0e9ff; /* Light blue */
        border-color: #bddbff;
        color: #004085; /* Dark blue */
    }


    #result-text {
        font-weight: 700;
        font-size: 1.1em;
        line-height: 1.5;
        margin: 0; /* Remove default paragraph margin */
    }

    .explanation-container {
         /* Existing styles for the explanation container */
    }

     .explanation-container p {
        margin-bottom: 15px;
     }

    .explanation-container ul {
        list-style: none;
        padding: 0;
        margin: 15px 0;
    }
    .explanation-container li {
        margin-bottom: 10px;
        padding-right: 20px;
        position: relative;
    }
     .explanation-container li:before {
        content: '★'; /* Custom bullet */
        color: #f39c12; /* Orange bullet */
        font-size: 1em;
        position: absolute;
        right: 0;
        top: 0;
     }


    /* Icon placeholders - use font icons or SVGs in a real app */
    .icon {
        /* Basic styling - ideally replace with actual icons */
        display: inline-block;
        width: 20px;
        height: 20px;
        background-size: contain;
        background-repeat: no-repeat;
        vertical-align: middle;
    }

    .brain-icon { background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="%231a3a5f" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-3.31 0-6-2.69-6-6 0-1.11.31-2.16.85-3.05L12 14l5.15-5.05c.54.89.85 1.94.85 3.05 0 3.31-2.69 6-6 6zm-6.54-7.56L12 6l6.54 6.44C17.16 10.24 14.85 8 12 8c-2.85 0-5.16 2.24-6.54 4.44z"/></svg>'); }
    .scale-icon { background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="%231a3a5f" d="M14 10H2v2h12v-2zm0-4H2v2h12V6zm4 8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3zm0-4c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg>'); }
    .flask-icon { background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="%231a3a5f" d="M15.5 14.5c0-2.8-2.2-5-5-5s-5 2.2-5 5 2.2 5 5 5 5-2.2 5-5zM10.5 16.5c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm-4.5-11V2h-1v3H4v2h2v11c0 2.21 1.79 4 4 4s4-1.79 4-4V7h2V5h-1z"/></svg>'); }
    .brain-outline-icon { background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="%231a3a5f" d="M12 1c-4.97 0-9 4.03-9 9 0 2.48 1 4.73 2.64 6.36L3 20.36V22h1.64l4.09-4.09C10.27 18 12.52 19 15 19c4.97 0 9-4.03 9-9S16.97 1 12 1zm0 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4z"/></svg>'); }
    .factors-icon { background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="%231a3a5f" d="M11 13H9v-2h2v2zm2 2h-2v2h2v-2zm2-2h-2v2h2v-2zm2-2h-2v2h2v-2zm2-2h-2v2h2V9zm-2-2h-2v2h2V7zm-2 0h-2v2h2V7zm-2-2h-2v2h2V5zM5 5h2v2H5V5zm0 2h2v2H5V7zm0 2h2v2H5V9zm0 2h2v2H5v11h14V11h-4zM7 19v-6h10v6H7z"/></svg>'); }
    .balance-icon { background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="%231a3a5f" d="M20 10h-5V4h-2v6H7V4H5v6H0v2h5v10h2V12h8v10h2V12h5v-2z"/></svg>'); }
    .uncertainty-icon { background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="%231a3a5f" d="M12 5.99c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm2 8h-4v-2h4v2zm-2 6c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm8-6c0 5.52-4.48 10-10 10S2 17.52 2 12 6.48 2 12 2s10 4.48 10 10zm-2 0c0-4.42-3.58-8-8-8s-8 3.58-8 8 3.58 8 8 8 8-3.58 8-8z"/></svg>'); }
    .technology-icon { background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="%231a3a5f" d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-8 16H5v-4h6v4zm0-6H5v-4h6v4zm0-6H5V5h6v4zm8 12h-6v-4h6v4zm0-6h-6v-4h6v4zm0-6h-6V5h6v4z"/></svg>'); }
    .ethics-icon { background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="%231a3a5f" d="M12 3L1 9l11 6 9-4.91V17h2V9L12 3zm0 12L3.12 10.37 12 5.73l8.88 4.64L12 15zM5 17h14v2H5z"/></svg>'); }


    /* Animations */
    @keyframes pulse {
        0% { transform: translate(-50%, -50%) scale(1); }
        100% { transform: translate(-50%, -50%) scale(1.05); }
    }

    @keyframes fadeInResult {
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeIn {
        to { opacity: 1; }
    }

    #explanation {
        opacity: 0; /* Start hidden for animation */
        animation: fadeIn 0.8s ease-out forwards;
        /* Remove the initial display: none from inline style once JS sets it,
           or handle initial visibility and subsequent animation purely in JS */
    }

    /* Ensure elements are block level for RTL text-align right to work properly */
    .case-info p, .case-info ul, .decision-section p, .options, .result-section p, .explanation-container p, .explanation-container ul {
        text-align: right;
    }

    /* Adjustments for smaller screens */
    @media (max-width: 600px) {
        body {
            padding: 20px 10px;
        }
        h1 {
            font-size: 1.8em;
        }
         .app-container, .explanation-container {
            padding: 20px;
        }
        .options label.option-label {
             padding: 12px;
             padding-right: 40px;
        }
        .options input[type="radio"] {
             right: 12px;
        }
        #submit-decision, .toggle-button {
            width: 100%;
            text-align: center;
        }
         .image-placeholder {
            max-width: 250px;
         }
    }


</style>

<script>
    document.getElementById('submit-decision').addEventListener('click', function() {
        const selectedDecision = document.querySelector('input[name="decision"]:checked');
        const resultTextElement = document.getElementById('result-text');
        const resultSection = document.getElementById('result-section');

        // Remove previous result classes
        resultSection.classList.remove('success', 'warning', 'danger', 'info');

        if (!selectedDecision) {
            resultTextElement.textContent = 'אנא בחר אחת מהאפשרויות כדי לקבל החלטה קריטית.';
            resultSection.classList.add('info'); // Use info class for instructions
            resultSection.style.display = 'block';
            resultSection.style.opacity = 0; // Reset for animation
            resultSection.style.transform = 'translateY(20px)';
            // Trigger reflow before animation
            void resultSection.offsetWidth;
            resultSection.style.animation = 'fadeInResult 0.5s ease-out forwards';
            return;
        }

        const decision = selectedDecision.value;
        let result = '';
        let resultType = ''; // Use type for class name

        const random = Math.random(); // 0 to 1

        if (decision === 'full-removal') {
            // Probabilities: Success w/o damage (60%), Success w/ damage (35%), Failure (5%)
            if (random < 0.60) {
                result = '<strong>תוצאה: הצלחה!</strong> הגידול הוסר בשלמותו. בנס, אזור הדיבור נשמר, והמטופל התאושש ללא נזק נוירולוגי משמעותי. סיכויי הישנות הגידול נמוכים מאוד. החלטה אמיצה שהשתלמה הפעם.';
                resultType = 'success';
            } else if (random < 0.95) { // 0.60 + 0.35 = 0.95
                result = '<strong>תוצאה: הצלחה חלקית, עם מחיר.</strong> הגידול הוסר בשלמותו כמתוכנן, אך למרבה הצער נגרמה פגיעה באזור הדיבור הסמוך. המטופל סובל כעת מקשיי דיבור קבועים (אפזיה משמעותית) וזקוק לתהליך שיקום ארוך ומורכב.';
                resultType = 'warning'; // Indicates success in removal but damage
            } else { // 0.95 to 1.00
                result = '<strong>תוצאה: סיבוך קשה.</strong> במהלך הניתוח להסרה מלאה, הופיע סיבוך בלתי צפוי וחמור (למשל, דימום משמעותי או שבץ). מצבו של המטופל קשה מאוד ויש סכנה ממשית לחייו או לצורך בהתמודדות עם נזק מוחי נרחב.';
                resultType = 'danger'; // Critical failure/severe outcome
            }
        } else if (decision === 'partial-removal') {
            // Probabilities: Success partial w/o damage (70%), Future growth (25%), Significant damage (5%)
            if (random < 0.70) {
                result = '<strong>תוצאה: הקלה מיידית.</strong> הגידול הוסר חלקית בהצלחה. הסימפטומים (קשיי דיבור) השתפרו מעט, והמטופל התאושש מהניתוח ללא נזק נוירולוגי נוסף. עם זאת, הגידול עדיין קיים, ויהיה צורך במעקב הדוק וטיפולים נוספים (הקרנות/כימותרפיה) בעתיד הקרוב.';
                resultType = 'info'; // Moderate outcome, need for future action
            } else if (random < 0.95) { // 0.70 + 0.25 = 0.95
                result = '<strong>תוצאה: ניהול מחלה, לא ריפוי.</strong> ההסרה החלקית בוצעה, אך ההדמיה לאחר הניתוח מראה ששארית הגידול צפויה לחזור או להמשיך לגדול בהדרגה. הסימפטומים עשויים לחזור או להחמיר בהמשך. יש צורך בהתחלת טיפולים אונקולוגיים מיידית ומעקב לטווח ארוך.';
                resultType = 'warning'; // Indicates less than ideal control, but not disaster
            } else { // 0.95 to 1.00
                 result = '<strong>תוצאה: נזק בלתי צפוי גם בהסרה חלקית.</strong> לצערנו, למרות הגישה הפחות אגרסיבית, גם ההסרה החלקית גרמה לפגיעה בלתי צפויה באזור חיוני סמוך. המטופל סובל כעת מקשיי דיבור חמורים הדורשים שיקום ממושך.';
                 resultType = 'danger'; // Severe unexpected damage
            }
        } else if (decision === 'conservative') {
            // Probabilities: Continued growth (90%), Stable/Slow growth (10%)
             if (random < 0.10) {
                result = '<strong>תוצאה: הפתעה חיובית.</strong> המטופל ממשיך בטיפול שמרני (מעקב בלבד או טיפול לא ניתוחי). באופן מפתיע, קצב גידול הגידול האגרסיבי לכאורה הוא איטי מאוד כעת, והסימפטומים יציבים יחסית. יש בכך הקלה זמנית, ונמשך מעקב צמוד בתקווה שהמצב יישמר.';
                resultType = 'success'; // Unexpected good outcome
             }
            else {
                result = '<strong>תוצאה: התקדמות המחלה.</strong> המטופל ממשיך בטיפול שמרני. כצפוי במקרה של גידול אגרסיבי, הגידול ממשיך לגדול בהדרגה בהדמיות המעקב, והסימפטומים (קשיי דיבור, ואולי גם אחרים) מחמירים. כעת יש לשקול טיפולים פליאטיביים (להקלה על סימפטומים) או טיפולים אונקולוגיים נוספים, אך הפרוגנוזה לטווח ארוך נותרה מאתגרת ללא ניתוח.';
                resultType = 'danger'; // Expected bad outcome when conservative approach fails for aggressive tumor
            }
        }

        resultTextElement.innerHTML = result; // Use innerHTML to allow bold tags
        resultSection.classList.add(resultType);
        resultSection.style.display = 'block';
        resultSection.style.opacity = 0; // Reset for animation
        resultSection.style.transform = 'translateY(20px)';
        // Trigger reflow before animation
        void resultSection.offsetWidth;
        resultSection.style.animation = 'fadeInResult 0.5s ease-out forwards';
    });

    document.getElementById('toggle-explanation').addEventListener('click', function() {
        const explanationDiv = document.getElementById('explanation');
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.opacity === '0';

        if (isHidden) {
            explanationDiv.style.display = 'block';
            // Trigger the CSS animation by changing opacity
            explanationDiv.style.opacity = 1;
            this.textContent = 'הסתר את חדר המחשבות של המנתח';
        } else {
            // Optional: Add a fade-out animation before hiding
             explanationDiv.style.opacity = 0;
             // Wait for animation to finish before hiding
             setTimeout(() => {
                 explanationDiv.style.display = 'none';
             }, 800); // Match animation duration
            this.textContent = 'הצג את חדר המחשבות של המנתח';
        }
    });

    // Initial state for explanation div to ensure CSS animation works
    document.addEventListener('DOMContentLoaded', function() {
        const explanationDiv = document.getElementById('explanation');
        explanationDiv.style.opacity = 0; // Ensure initial opacity is 0
        explanationDiv.style.display = 'none'; // Keep it hidden initially
         document.getElementById('toggle-explanation').textContent = 'הצג את חדר המחשבות של המנתח'; // Ensure button text is correct on load
    });

</script>
```