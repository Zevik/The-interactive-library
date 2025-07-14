---
title: "הכוח והשם: פלונטר בוועדת שמות רחובות עירונית"
english_slug: the-power-and-the-name-managing-an-urban-street-naming-committee
category: "כלכלה התנהגותית"
tags:
  - קבלת החלטות
  - תכנון עירוני
  - ועדות ציבוריות
  - הטיה קוגניטיבית
  - קונצנזוס
  - ממשל מקומי
---
# הכוח והשם: פלונטר בוועדת שמות רחובות עירונית

נתבקשתם להצטרף לוועדת שמות הרחובות העירונית. המשימה הראשונה שלכם: להחליט על שם לרחוב חדש בשכונה מתפתחת, בקרבת אתר ארכיאולוגי קטן. נשמע קל? היכנסו לנעלי חברי הוועדה וגלו איך אינטרסים, דעות קדומות ולחצים חיצוניים הופכים החלטה פשוטה למסע מורכב של פשרות (וכאבי ראש).

<div id="app-container">
    <header class="app-header">
        <h2 class="header-title">דיון סוער בוועדת שמות הרחובות</h2>
        <p class="header-subtitle">עליכם לגבש המלצה לשם רחוב חדש. שקלו את הגורמים השונים לפני שתכריעו!</p>
    </header>

    <section class="info-section committee-section">
        <h3 class="section-title">חברי הוועדה (חוץ מכם):</h3>
        <div id="committee-members" class="cards-grid">
            <!-- Members will be loaded here by JS -->
        </div>
    </section>

    <section class="info-section feedback-section">
        <h3 class="section-title">משוב ציבורי ראשוני (מדגם מהיר מהרשתות):</h3>
        <ul id="public-feedback" class="feedback-list">
            <!-- Feedback will be loaded here by JS -->
        </ul>
    </section>

    <section class="info-section proposals-section">
        <h3 class="section-title">הצעות לשמות הרחוב (עם נימוקים ונקודות למחשבה):</h3>
        <div id="proposals" class="cards-grid">
            <!-- Proposals will be loaded here by JS -->
        </div>
    </section>

    <section class="user-decision-section">
        <h3 class="section-title">ההמלצה האישית שלכם לוועדה:</h3>
        <p class="decision-prompt">בחרו את השם המועדף עליכם. נסו לחשוב אילו טיעונים תשמיעו בוועדה כדי לשכנע את חבריה, תוך התייחסות לגורמים השונים.</p>
        <div id="name-selection" class="selection-options">
            <!-- Radio buttons will be loaded here by JS -->
        </div>
        <label for="justification" class="justification-label">נימוק להמלצה (חשבו על טקטיקת השכנוע שלכם):</label>
        <textarea id="justification" rows="4" placeholder="האם תתמקדו בהיסטוריה? בפרקטיקה? בדעת הקהל? איך תתמודדו עם ההטיות של חברים אחרים?"></textarea>
        <button id="submit-decision" class="action-button">הגשת ההמלצה לדיון הוועדה</button>
    </section>

    <section id="result-area" class="info-section result-section" style="display: none;">
        <h3 class="section-title">הכרעת הוועדה הסופית:</h3>
        <div id="final-decision" class="result-content">
            <!-- Final decision will be displayed here by JS -->
        </div>
         <button id="explanation-button" class="secondary-button">מאחורי הקלעים: איך התקבלה ההחלטה?</button>
    </section>

     <section id="explanation-section" class="info-section explanation-section" style="display: none;">
        <h2 class="section-title">מאחורי הקלעים של קבלת החלטות בוועדות</h2>

        <p><strong>פלונטר קבוצתי: יתרונות, אתגרים ו... הטיות!</strong><br>
        קבלת החלטות בוועדה, כמו זו שבה 'השתתפתם', מביאה אמנם שפע דעות וידע לשולחן. זה יכול להוליד פתרונות יצירתיים יותר ולהפחית סיכונים. אבל היי, ברוכים הבאים לפוליטיקה קטנה: דיונים מתארכים, קונפליקטים צצים, ודינמיקות חברתיות (כמו הלחץ להסכים עם ה"בוס" או הנטייה של כולם לחשוב אותו דבר) משפיעות לא פחות מהעובדות היבשות.</p>

        <p><strong>לכל אחד יש אג'נדה (גלויה או נסתרת)</strong><br>
        זוכרים את חברי הוועדה? לכל אחד יש סדר עדיפויות משלו, ערכים שחשובים לו, ולעיתים גם אינטרסים שאינם קשורים ישירות לשם הרחוב (למשל, רצון לרצות קבוצת מצביעים מסוימת או לקדם אג'נדה אישית). כוח ההשפעה של כל אחד תלוי במעמדו, בכריזמה שלו, וביכולתו לגייס תמיכה. ההחלטה הסופית היא תבשיל שבו מתערבבים כל אלה – הרבה פשרות, קצת מאבקי כוח, ולפעמים פשוט עייפות שמביאה להסכמה (או כניעה) לרוב.</p>

        <p><strong>הציבור איתנו? או נגדנו?</strong><br>
        ועדה ציבורית לא פועלת בריק. תגובות תושבים (אפילו אם הן רק מדגם אקראי מהפייסבוק), לחץ פוליטי, כותרות בעיתון – כל אלה נמצאים ברקע ומשפיעים. לפעמים הוועדה תבחר שם כדי 'לעשות לציבור טוב', ולפעמים היא תתעלם לחלוטין מדעתו אם היא סבורה שהוא 'לא מבין' או אם יש אינטרס חזק יותר באוויר.</p>

        <p><strong>המוח מקצר תהליכים: הטיות קוגניטיביות בעבודה</strong><br>
        אפילו האנשים הכי מתוחכמים בוועדה חשופים להטיות שמעוותות את שיקול הדעת:
        <ul>
            <li><strong>הטיית אישור:</strong> נטייה לחפש רק מידע שתומך בדעה הקיימת (אהבתם שם מסוים? פתאום תראו רק את היתרונות שלו).</li>
            <li><strong>עוגן:</strong> ההצעה הראשונה שהוצגה, או הדעה של חבר הוועדה החשוב ביותר, הופכות ל"עוגן" שממנו קשה להתרחק.</li>
            <li><strong>קונפורמיות (לחץ חברתי):</strong> לפעמים קל יותר להסכים עם הרוב, גם אם זה מנוגד לדעתכם האמיתית. זה קורה כדי לא לעורר ויכוחים או להישאר 'בצד הטוב' של קבוצה חזקה בוועדה. כשכולם מתחילים לחשוב אותו הדבר כדי להימנע מקונפליקט - זו "חשיבת יחד" (Groupthink) קלאסית.</li>
             <li><strong>הטיית זמינות:</strong> מידע שקפץ לכם מול העיניים לאחרונה (פוסט זועם בפייסבוק, כתבה על דמות היסטורית) מקבל משקל יתר בקבלת ההחלטה.</li>
        </ul>
        ההטיות האלה יכולות לגרום לוועדה לפסול הצעה מצוינת על סמך נימוק חלש שקיבל בטעות משקל יתר, או לאמץ הצעה בעייתית רק כי היא התאימה לאג'נדה של חבר דומיננטי.</p>

        <p><strong>קריטריונים? רק על הנייר (בערך)</strong><br>
        ועדות מנסחות קריטריונים 'אובייקטיביים' (היסטוריה, גאוגרפיה, קלות הגייה), וזה חשוב כדי לייצר שיח רציונלי. אבל איך משקללים אותם? האם היסטוריה חשובה יותר מפרקטיקה? כאן נכנסים לתמונה כל הגורמים האנושיים והפוליטיים. לכן, לעיתים קרובות, ההחלטה בפועל סוטה מהשקלול התיאורטי של הקריטריונים.</p>

        <p><strong>רוב, קונצנזוס, או מי שצועק חזק יותר?</strong><br>
        איך מכריעים? הצבעה (רוב רגיל? מיוחס?), דיון אינסופי עד שכולם מסכימים (נדיר!), או החלטה של יושב הראש. כל שיטה מייצרת דינמיקה שונה ומובילה לתוצאה אחרת. הסימולציה שחוויתם נועדה להראות שלא תמיד הדרך ה'הגיונית' או 'הרציונלית' היא זו שמנצחת. הרבה פעמים, קבלת החלטה היא ריקוד מורכב בין היגיון, רגש, אינטרסים וסתם מזל.</p>
    </section>
</div>

<style>
    :root {
        --primary-color: #0056b3; /* Deep Blue */
        --secondary-color: #007bff; /* Bright Blue */
        --accent-color: #28a745; /* Green for Pros */
        --danger-color: #dc3545; /* Red for Cons */
        --background-color: #f8f9fa; /* Light Grey */
        --card-background: #ffffff; /* White */
        --border-color: #e9ecef; /* Lighter Grey Border */
        --text-color: #343a40; /* Dark Grey Text */
        --light-text-color: #6c757d; /* Muted Text */
        --shadow: rgba(0, 0, 0, 0.08);
    }

    #app-container {
        font-family: 'Heebo', sans-serif; /* Or any modern Hebrew-friendly font */
        line-height: 1.7;
        color: var(--text-color);
        max-width: 800px;
        margin: 30px auto;
        padding: 25px;
        background-color: var(--background-color);
        border-radius: 12px;
        box-shadow: 0 8px 16px var(--shadow);
        direction: rtl;
        text-align: right;
    }

    .app-header {
        text-align: center;
        margin-bottom: 30px;
        padding-bottom: 20px;
        border-bottom: 1px solid var(--border-color);
    }

    .header-title {
        color: var(--primary-color);
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 1.8em;
        font-weight: bold;
    }

    .header-subtitle {
        color: var(--light-text-color);
        font-size: 1.1em;
    }

    .section-title {
        color: var(--secondary-color);
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.4em;
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 5px;
        display: inline-block;
    }

    .info-section {
        background-color: var(--card-background);
        padding: 20px;
        margin-bottom: 25px;
        border-radius: 8px;
        border: 1px solid var(--border-color);
        box-shadow: 0 4px 8px var(--shadow);
        opacity: 0; /* Start hidden for animation */
        transform: translateY(20px); /* Start slightly lower */
        transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    }
     .info-section.is-visible {
         opacity: 1;
         transform: translateY(0);
     }


    .cards-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
    }

    .member, .proposal {
        background-color: var(--background-color);
        padding: 15px;
        border-radius: 6px;
        border: 1px solid var(--border-color);
        box-shadow: 0 2px 4px var(--shadow);
    }

    .member strong, .proposal strong {
        color: var(--primary-color);
        font-size: 1.1em;
        display: block;
        margin-bottom: 5px;
    }

     .member p, .proposal p {
         font-size: 0.95em;
         margin-bottom: 5px;
         color: var(--text-color);
     }


    .feedback-list {
        list-style: none; /* Remove default bullets */
        padding-left: 0;
    }

    .feedback-list li {
        margin-bottom: 12px;
        padding-right: 15px;
        position: relative;
        color: var(--text-color);
    }

     .feedback-list li::before {
         content: "💬"; /* Chat bubble icon */
         position: absolute;
         right: 0;
         top: 0;
         font-size: 0.9em;
         color: var(--secondary-color);
     }

    .proposal h4 {
        margin-top: 0;
        margin-bottom: 8px;
        color: var(--primary-color);
        font-size: 1.2em;
    }

    .proposal p {
        font-size: 0.9em;
        margin-bottom: 8px;
    }

    .proposal .pros {
        color: var(--accent-color);
        font-weight: bold;
    }

    .proposal .cons {
        color: var(--danger-color);
        font-weight: bold;
    }

    .user-decision-section {
        margin-top: 30px;
        padding-top: 25px;
        border-top: 1px dashed var(--border-color);
        background-color: var(--card-background);
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px var(--shadow);
         opacity: 0; /* Start hidden for animation */
         transform: translateY(20px); /* Start slightly lower */
         transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    }

     .user-decision-section.is-visible {
         opacity: 1;
         transform: translateY(0);
     }


    .decision-prompt {
        font-size: 1.1em;
        color: var(--text-color);
        margin-bottom: 20px;
    }

    .selection-options label {
        display: block;
        margin-bottom: 12px;
        cursor: pointer;
        font-size: 1em;
        color: var(--text-color);
        transition: color 0.2s ease-in-out;
    }

     .selection-options label:hover {
         color: var(--primary-color);
     }

     .selection-options input[type="radio"] {
         margin-left: 8px;
         accent-color: var(--secondary-color); /* Style radio button */
     }


    .justification-label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        color: var(--text-color);
    }

    #justification {
        width: 100%; /* Make it truly full width */
        padding: 10px;
        margin-bottom: 20px;
        border: 1px solid var(--border-color);
        border-radius: 4px;
        font-size: 1em;
        line-height: 1.5;
        resize: vertical; /* Allow vertical resize */
        box-sizing: border-box; /* Include padding in width */
    }

    .action-button, .secondary-button {
        display: inline-block; /* Changed to inline-block */
        padding: 12px 20px;
        background-color: var(--secondary-color);
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        text-decoration: none; /* Remove underline */
        text-align: center;
        margin-right: 10px; /* Add margin between buttons */
    }

    .action-button:hover {
        background-color: var(--primary-color);
        transform: translateY(-2px); /* Lift effect on hover */
    }

    .secondary-button {
         background-color: var(--light-text-color);
     }

     .secondary-button:hover {
         background-color: #5a6268;
         transform: translateY(-2px);
     }


    .result-section {
        margin-top: 30px;
        padding: 20px;
        background-color: #d4edda; /* Light Green for Success/Result */
        color: #155724; /* Dark Green Text */
        border-color: #c3e6cb; /* Green Border */
        border: 1px solid;
        border-radius: 8px;
        opacity: 0; /* Start hidden for animation */
        transform: translateY(20px); /* Start slightly lower */
        transition: opacity 0.6s ease-out, transform 0.6s ease-out;
    }
     .result-section.is-visible {
         opacity: 1;
         transform: translateY(0);
     }


    .result-content strong {
        color: #0f3b1e; /* Even darker green */
        font-size: 1.2em;
    }

    .result-content ul {
        margin-top: 15px;
        padding-right: 20px;
        list-style: disc;
    }

    .result-content li {
        margin-bottom: 8px;
    }

    .explanation-section {
        margin-top: 20px; /* Added margin between result and explanation */
        padding: 25px;
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        border-radius: 8px;
         opacity: 0; /* Start hidden for animation */
         max-height: 0; /* Start with no height */
         overflow: hidden; /* Hide overflowing content */
         transition: opacity 0.6s ease-out, max-height 0.6s ease-out;
    }

     .explanation-section.is-visible {
         opacity: 1;
         max-height: 2000px; /* Large enough height to transition to */
     }

     .explanation-section h2 {
         margin-top: 0;
         color: var(--primary-color);
         font-size: 1.6em;
         border-bottom: 2px solid var(--secondary-color);
         padding-bottom: 10px;
         margin-bottom: 20px;
     }

     .explanation-section p {
         margin-bottom: 18px;
         line-height: 1.7;
     }

     .explanation-section strong {
         color: var(--secondary-color);
     }

     .explanation-section ul {
         margin-top: 10px;
         padding-right: 20px;
         list-style: disc;
     }

     .explanation-section li {
         margin-bottom: 8px;
     }

     /* Animation keyframes */
    @keyframes fadeInScale {
        0% { opacity: 0; transform: scale(0.95); }
        100% { opacity: 1; transform: scale(1); }
    }

    .result-section.animated {
        animation: fadeInScale 0.5s ease-out forwards;
    }


</style>

<script>
    // Data representing the committee members, proposals, and initial public feedback
    const committeeData = {
        members: [
            { name: "פרופ' אילנה כהן", bias: "מומחית להיסטוריה מקומית. דגש על קשר לאתר ארכיאולוגי ולהיסטוריה של ההתיישבות באזור." },
            { name: "אברהם לוי", bias: "נציג בעלי העסקים. דגש על פרקטיקה: שם קליט, קל לזכירה ולניווט, שאינו יוצר בלבול." },
            { name: "רחל מזרחי", bias: "פעילת ציבור. רגישות גבוהה לדעת הקהל ולצורך בקונצנזוס רחב. נטייה להימנע משמות שנויים במחלוקת." },
            { name: "דוד שמחון", bias: "סגן ראש העיר. דגש על הנצחת דמויות ציבוריות או לאומיות מוכרות. פחות רגיש לקשר המקומי הספציפי, יותר לאג'נדה עירונית רחבה." }
        ],
        proposals: [
            {
                name: "רחוב תל עתיקות",
                description: "שם המתייחס ישירות לאתר הארכיאולוגי הסמוך.",
                pros: ["קשר מקומי והיסטורי ברור.", "שם בעל צליל מקומי אותנטי.", "קל יחסית לזכירה."],
                cons: ["עשוי להישמע גנרי או חסר יוקרה.", "אולי לא מספיק מכובד לרחוב ראשי בשכונה חדשה."],
                influence: { committee: { "פרופ' אילנה כהן": 3 }, public: { positive: 2, negative: 0 } }
            },
            {
                name: "רחוב שרה אהרונסון",
                description: "הנצחת דמות היסטורית חשובה מימי ניל\"י וההתיישבות בארץ ישראל.",
                pros: ["הנצחת גיבורה לאומית.", "שם מוכר ובעל משמעות סימבולית רחבה."],
                cons: ["פחות קשר ישיר למיקום הגיאוגרפי הספציפי.", "אישים היסטוריים עלולים לעורר דיון ציבורי או פוליטי רגיש.", "חלק מהציבור אינו מכיר את הדמות לעומק."],
                 influence: { committee: { "דוד שמחון": 3 }, public: { positive: 1, negative: 1 } }
            },
             {
                name: "רחוב שמשון",
                description: "שם בעל הד היסטורי-תנ\"כי, קצר וקליט.",
                pros: ["שם קצר וקליט.", "בעל הד תנ\"כי שמתחבר לסביבה ההיסטורית הרחבה.", "קל להגייה וזכירה - פרקטי."],
                cons: ["עשוי להישמע מיושן לחלק מהאנשים.", "לא מתייחס ספציפית לאתר הארכיאולוגי אלא יותר כללי.", "השם יכול לעורר קונוטציות אחרות (כוח, גיבור)."],
                influence: { committee: { "אברהם לוי": 2 }, public: { positive: 1, negative: 1, mixed: 1 } } // Slight bias for practicality
            },
             {
                name: "רחוב דרך העמק",
                description: "שם גאוגרפי תיאורי וניטרלי.",
                pros: ["שם תיאורי המתייחס למיקום הפיזי (אם כי האזור הוא יותר גבעה מאשר עמק...).", "שם ניטרלי, לא מעורר מחלוקות.", "קל לזכירה וניווט - פרקטי."],
                cons: ["חסר משמעות היסטורית או תרבותית עמוקה.", "עשוי להישמע גנרי מדי ולא ייחודי.", "לא מדויק גאוגרפית."],
                 influence: { committee: { "אברהם לוי": 3, "רחל מזרחי": 2 }, public: { positive: 2, negative: 0 } } // Practicality & avoids controversy
            }
        ],
         publicFeedback: [
             { text: "רחוב תל עתיקות נשמע אותנטי! מתאים מאוד לקרבת האתר.", sentiment: "positive" },
             { text: "למה לא שם של מדען או אמן פורץ דרך? תמיד גיבורי מלחמה גברים...", sentiment: "negative" },
             { text: "רחוב שמשון? קצת מוזר לרחוב חדש. יש קונוטציות אלימות.", sentiment: "negative" },
             { text: "דרך העמק הכי הגיוני וקל לזכור. העיקר שאנשים ימצאו את הכתובת בקלות בלי להתברבר.", sentiment: "positive" },
             { text: "לא מכיר את שרה אהרונסון. עדיף משהו שכולם מכירים ויכולים להתחבר אליו.", sentiment: "neutral" },
             { text: "כל שם שקל לזכור ולקרוא! בבקשה לא שמות מסובכים או ארוכים.", sentiment: "positive" },
             { text: "אני בעד שם שמנציח משהו מקומי, כמו תל עתיקות.", sentiment: "positive" },
              { text: "דרך העמק נשמע הכי נעים ושקט.", sentiment: "positive" },
              { text: "שמשון זה שם חזק, אולי מתאים לשדרה ראשית?", sentiment: "mixed" },
              { text: "עוד רחוב על שם דמות היסטורית? משעמם.", sentiment: "negative" },
         ]
    };

    // Shuffle function for feedback display
     function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]]; // Swap elements
        }
        return array;
    }


    function displayCommitteeMembers() {
        const container = document.getElementById('committee-members');
        container.innerHTML = committeeData.members.map(member => `
            <div class="member">
                <strong>${member.name}</strong>
                <p><em>נטייה/העדפה:</em> ${member.bias}</p>
            </div>
        `).join('');
         // Animate cards in
         setTimeout(() => {
             document.querySelectorAll('.committee-section .member').forEach((el, i) => {
                 el.style.transitionDelay = `${i * 0.1}s`;
                 el.parentElement.parentElement.classList.add('is-visible'); // Animate parent section
             });
         }, 100); // Small delay to allow elements to be added
    }

     function displayPublicFeedback() {
        const container = document.getElementById('public-feedback');
        // Display a shuffled subset (e.g., 6 random feedbacks)
        const feedbackSubset = shuffleArray([...committeeData.publicFeedback]).slice(0, 6);
        container.innerHTML = feedbackSubset.map(feedback => `<li>${feedback.text}</li>`).join('');
        setTimeout(() => {
            document.querySelector('.feedback-section').classList.add('is-visible');
        }, 200); // Stagger animation
    }

    function displayProposals() {
        const container = document.getElementById('proposals');
        const selectionContainer = document.getElementById('name-selection');

        container.innerHTML = committeeData.proposals.map(proposal => `
            <div class="proposal">
                <h4>${proposal.name}</h4>
                <p>${proposal.description}</p>
                <p><strong>יתרונות:</strong> <span class="pros">${proposal.pros.join(', ')}</span></p>
                <p><strong>נקודות למחשבה/קשיים:</strong> <span class="cons">${proposal.cons.join(', ')}</span></p>
            </div>
        `).join('');

         selectionContainer.innerHTML = committeeData.proposals.map(proposal => `
            <label class="selection-label">
                <input type="radio" name="chosen_name" value="${proposal.name}">
                ${proposal.name}
            </label>
         `).join('');

         setTimeout(() => {
             document.querySelector('.proposals-section').classList.add('is-visible');
             document.querySelector('.user-decision-section').classList.add('is-visible');
         }, 300); // Stagger animation
    }

    // --- Simulation Logic ---
    function calculateProposalScore(proposal) {
        let score = 0;

        // Base score (simple - more pros = better)
        score += proposal.pros.length * 1.5;
        score -= proposal.cons.length * 1;

        // Influence from committee members (weighted by their bias strength)
        for (const memberName in proposal.influence.committee) {
            score += proposal.influence.committee[memberName]; // Add influence points
        }

        // Influence from public feedback (weighted)
         const publicInfluence = proposal.influence.public;
         score += (publicInfluence.positive || 0) * 2; // Positive feedback is powerful
         score += (publicInfluence.mixed || 0) * 0.5; // Mixed is slightly positive/neutral
         score -= (publicInfluence.negative || 0) * 1.5; // Negative feedback is detrimental

        // Add a small random factor to make it less predictable (simulating discussion flow)
        score += Math.random() * 2; // Add up to 2 points randomly

        console.log(`Calculated score for ${proposal.name}: ${score.toFixed(2)}`);
        return score;
    }

    function simulateCommitteeDecision(userChoice, userJustification) {
        const proposalScores = {};
        committeeData.proposals.forEach(p => {
            proposalScores[p.name] = calculateProposalScore(p);
        });

        // Simulate committee dynamics: weighted random selection based on scores
        // This makes the outcome feel less deterministic than just picking the max score,
        // reflecting the unpredictability of group discussions.
        let totalScoreSum = 0;
        for (const name in proposalScores) {
            totalScoreSum += Math.max(0.1, proposalScores[name]); // Ensure scores are positive for weighting
        }

        let randomPoint = Math.random() * totalScoreSum;
        let winningName = null;

        for (const name in proposalScores) {
            randomPoint -= Math.max(0.1, proposalScores[name]);
            if (randomPoint <= 0) {
                winningName = name;
                break;
            }
        }

        // Fallback just in case (shouldn't happen with the weighting logic)
        if (!winningName) winningName = committeeData.proposals[0].name;

        // --- Determine reason for winning (simplified) ---
        let winningProposal = committeeData.proposals.find(p => p.name === winningName);
        let winReason = "לאחר דיון מעמיק ושקלול מגוון שיקולים."; // Default

        // Check dominant influences
        let maxCommitteeInfluence = 0;
        let influentialMember = null;
        for (const memberName in winningProposal.influence.committee) {
             if (winningProposal.influence.committee[memberName] > maxCommitteeInfluence) {
                 maxCommitteeInfluence = winningProposal.influence.committee[memberName];
                 influentialMember = memberName;
             }
        }

         let publicSentimentInfluence = (winningProposal.influence.public.positive || 0) - (winningProposal.influence.public.negative || 0);

        if (maxCommitteeInfluence > 1 && influentialMember) {
             winReason = `לאחר שהטיעונים של חבר הוועדה ${influentialMember} (המייצג את הגישה של "${committeeData.members.find(m => m.name === influentialMember).bias}") זכו לתמיכה רחבה.`;
        } else if (publicSentimentInfluence > 1.5) {
             winReason = `בעקבות המשוב הציבורי החיובי יחסית שהתקבל בנוגע להצעה זו.`;
        } else if (winningProposal.pros.length >= winningProposal.cons.length + 2 && maxCommitteeInfluence <= 1 && publicSentimentInfluence <= 1.5) {
             winReason = `על בסיס היתרונות המובהקים יחסית של ההצעה והיותה פרקטית או מקובלת.`;
        } else {
             winReason = `כתוצאה משקלול מורכב של אינטרסים שונים ופשרות שהושגו בדיון.`;
        }


        const resultArea = document.getElementById('final-decision');
        resultArea.innerHTML = ''; // Clear previous result

        let explanationText = `לאחר דיון סוער והצבעה (או הגעה להסכמה קשה), ועדת שמות הרחובות החליטה לבחור בשם: <strong>${winningName}</strong>.`;

        if (userChoice && winningName !== userChoice) {
            explanationText += `<br>שימו לב, ההמלצה האישית שלכם הייתה ${userChoice}, והכרעת הוועדה שונה.`;
        } else if (userChoice && winningName === userChoice) {
             explanationText += `<br>המלצתכם האישית (${userChoice}) התקבלה בוועדה!`;
        }


        explanationText += `<p>${winReason}</p>`; // Add the specific reason

        explanationText += `<p>קבלת החלטה בוועדה ציבורית מושפעת משילוב מורכב של נתונים, אינטרסים, לחצים חיצוניים (כמו דעת קהל), ויחסי כוחות פנימיים. לעיתים קרובות, התוצאה הסופית היא תוצר של דינמיקה קבוצתית והטיות קוגניטיביות, ולא רק שקלול 'רציונלי' של היתרונות והחסרונות.</p>`;


        resultArea.innerHTML = explanationText;
        const resultSection = document.getElementById('result-area');
        resultSection.style.display = 'block';

        // Trigger animation
        setTimeout(() => {
             resultSection.classList.add('is-visible');
         }, 10); // Small delay after display block

        // Disable submit after decision
        document.getElementById('submit-decision').disabled = true;
        document.getElementById('justification').disabled = true;
        document.querySelectorAll('#name-selection input').forEach(input => input.disabled = true);

         // Show explanation button if needed (it's already there, just make sure it's part of the visible flow)
         document.getElementById('explanation-button').style.display = 'inline-block'; // Ensure button is visible within result section
    }


    document.getElementById('submit-decision').addEventListener('click', function() {
        const selectedRadio = document.querySelector('input[name="chosen_name"]:checked');
        const justification = document.getElementById('justification').value.trim();

        if (!selectedRadio) {
            alert("אנא בחרו שם מועדף כדי להגיש את המלצתכם.");
            return;
        }
         if (justification.length < 10) {
             alert("אנא נמקו את בחירתכם בקצרה (לפחות 10 תווים).");
             return;
         }

        const userChoice = selectedRadio.value;
        console.log("User choice:", userChoice);
        console.log("User justification:", justification);

        // Simulate the committee process and display result
        simulateCommitteeDecision(userChoice, justification);
    });

    // Toggle explanation section visibility
    document.getElementById('explanation-button').addEventListener('click', function() {
        const explanationSection = document.getElementById('explanation-section');
        const button = this;
        if (explanationSection.style.display === 'none' || !explanationSection.classList.contains('is-visible')) {
             explanationSection.style.display = 'block'; // Ensure display is not 'none' for transition
            setTimeout(() => { // Add class after display block
                explanationSection.classList.add('is-visible');
                button.textContent = 'הסתר את ההסבר המלא';
                button.style.backgroundColor = '#dc3545'; /* Red color for hide */
                 button.style.borderColor = '#dc3545';
            }, 10);
        } else {
            explanationSection.classList.remove('is-visible');
             setTimeout(() => { // Hide display after transition
                 explanationSection.style.display = 'none';
                 button.textContent = 'מאחורי הקלעים: איך התקבלה ההחלטה?';
                 button.style.backgroundColor = var(--light-text-color); /* Back to secondary color */
                  button.style.borderColor = var(--light-text-color);
             }, 600); // Match transition duration
        }
    });

    // Function to make elements visible with delay
    function animateSections() {
        const sections = document.querySelectorAll('.info-section, .user-decision-section');
        sections.forEach((section, index) => {
            setTimeout(() => {
                section.classList.add('is-visible');
            }, index * 150); // Stagger delay
        });
    }


    // Initial display and animation sequence
     function initializeApp() {
         displayCommitteeMembers();
         displayPublicFeedback();
         displayProposals();
         // The animation call is now within the display functions themselves for staggering.
     }


    initializeApp();

</script>