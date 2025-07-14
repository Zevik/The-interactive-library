---
title: "הבחירה האולימפית: דינמיקה של החלטה קבוצתית"
english_slug: olympic-choice-group-decision-dynamics
category: "מדעי החברה / כלכלה התנהגותית"
tags: ["קבלת החלטות", "דינמיקה קבוצתית", "כלכלה התנהגותית", "ועד אולימפי", "בחירה אסטרטגית"]
---
<div class="olympic-container">
    <h1>הבחירה האולימפית: דינמיקה של החלטה קבוצתית</h1>
    <p class="intro-text">דמיינו שאתם חברים בוועד האולימפי הבינלאומי (IOC), אמונים על בחירת העיר המארחת למשחקים. האם ההחלטה מתבססת אך ורק על נתונים אובייקטיביים והצעה כלכלית? הצטרפו לסימולציה וגלו את הכוחות הנסתרים שבאמת משפיעים על תהליך הבחירה המורכב.</p>

    <div id="olympic-app">
        <section id="step1" class="app-step active-step">
            <h2>שלב 1: קביעת סדרי עדיפויות אישיים</h2>
            <p>כחבר ועד, לפני שאתם בוחנים את ההצעות, מהם הקריטריונים החשובים לכם ביותר? דרגו את חשיבות כל קריטריון עבורכם (1 - הכי חשוב, 6 - הכי פחות חשוב). ודאו שכל מספר משומש פעם אחת בלבד.</p>
            <div class="criteria-ranking">
                <div class="criterion-item" data-criterion="infra">
                    <label for="rank-infra">תשתיות קיימות ומוכנות:</label>
                    <select id="rank-infra" class="criterion-rank">
                        <option value="">דרג</option>
                        <option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option>
                    </select>
                </div>
                <div class="criterion-item" data-criterion="budget">
                    <label for="rank-budget">תקציב ומוכנות פיננסית:</label>
                    <select id="rank-budget" class="criterion-rank">
                        <option value="">דרג</option>
                        <option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option>
                    </select>
                </div>
                <div class="criterion-item" data-criterion="security">
                    <label for="rank-security">היבטים ביטחוניים ובטיחות:</label>
                    <select id="rank-security" class="criterion-rank">
                        <option value="">דרג</option>
                        <option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option>
                    </select>
                </div>
                <div class="criterion-item" data-criterion="support">
                    <label for="rank-support">תמיכה ציבורית ומקומית:</label>
                    <select id="rank-support" class="criterion-rank">
                        <option value="">דרג</option>
                        <option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option>
                    </select>
                </div>
                 <div class="criterion-item" data-criterion="legacy">
                    <label for="rank-legacy">מורשת צפויה והשפעה ארוכת טווח:</label>
                    <select id="rank-legacy" class="criterion-rank">
                         <option value="">דרג</option>
                        <option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option>
                    </select>
                </div>
                 <div class="criterion-item" data-criterion="experience">
                    <label for="rank-experience">ניסיון קודם באירוח אירועים גדולים:</label>
                    <select id="rank-experience" class="criterion-rank">
                         <option value="">דרג</option>
                        <option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option>
                    </select>
                </div>
            </div>
            <button onclick="nextStep(2)">המשך: סקירת הצעות הערים</button>
        </section>

        <section id="step2" class="app-step">
            <h2>שלב 2: בחינת הצעות הערים המתמודדות</h2>
            <p>לפניכם נתונים עיקריים מהצעות הערים המתמודדות, עיר א' ועיר ב'. שקלו אותם לאור סדרי העדיפויות שקבעתם בשלב הקודם.</p>
            <div class="cities-data">
                <div class="city-card city-a">
                    <h3><span class="city-icon">🏙️</span> עיר א'</h3>
                    <ul>
                        <li><strong><span class="list-icon">🏗️</span> תשתיות קיימות:</strong> מצוינות, אצטדיונים ומתקנים רבים מוכנים.</li>
                        <li><strong><span class="list-icon">💰</span> תקציב מוצע:</strong> גבוה (20 מיליארד דולר), אך שאפתני - מעלה חשש לגידול בעלויות.</li>
                        <li><strong><span class="list-icon">🛡️</span> היבטים ביטחוניים:</strong> טובים בסך הכל, נדרשים חיזוקים באזורים ספציפיים המפורטים בהצעה.</li>
                        <li><strong><span class="list-icon">🤝</span> תמיכה ציבורית:</strong> גבוהה מאוד (85% בסקרים) - מעיד על מוכנות ציבורית.</li>
                        <li><strong><span class="list-icon">🌳</span> מורשת צפויה:</strong> פיתוח תשתיות מסיבי, חיבור אזורים מרוחקים, אך קיים סיכון לחוב ציבורי גדול.</li>
                        <li><strong><span class="list-icon">🏅</span> ניסיון קודם:</strong> אירוחה בהצלחה אליפויות עולם ואירועי ספורט גדולים אחרים, אך לא אולימפיאדה מלאה.</li>
                    </ul>
                </div>
                <div class="city-card city-b">
                     <h3><span class="city-icon">🌇</span> עיר ב'</h3>
                    <ul>
                        <li><strong><span class="list-icon">🏗️</span> תשתיות קיימות:</strong> בינוניות, נדרשות השקעות גדולות לבנייה חדשה של אצטדיון מרכזי וכפר אולימפי.</li>
                        <li><strong><span class="list-icon">💰</span> תקציב מוצע:</strong> מתון (15 מיליארד דולר), נתפס כריאלי יותר ומבוסס על שימוש חוזר במבנים קיימים.</li>
                        <li><strong><span class="list-icon">🛡️</span> היבטים ביטחוניים:</strong> מצוינים, מערך אבטחה מתקדם ביותר קיים ומתורגל היטב.</li>
                        <li><strong><span class="list-icon">🤝</span> תמיכה ציבורית:</strong> בינונית (60% בסקרים), ישנן קבוצות התנגדות מקומיות פעילות.</li>
                        <li><strong><span class="list-icon">🌳</span> מורשת צפויה:</strong> התמקדות בשיקום שכונות, השקעה בפארקים ציבוריים וקיימות סביבתית. נתפסת כמודל "רזה" יותר.</li>
                        <li><strong><span class="list-icon">🏅</span> ניסיון קודם:</strong> אירוחה בהצלחה את האולימפיאדה לפני 20 שנה וזכתה לשבחים על ארגון.</li>
                    </ul>
                </div>
            </div>
             <button onclick="nextStep(3)">המשך: העדפה ראשונית</button>
        </section>

         <section id="step3" class="app-step">
            <h2>שלב 3: גיבוש העדפה ראשונית</h2>
            <p>לאחר שסקרתם את נתוני הערים ואת דירוג הקריטריונים האישי שלכם, לאן נוטה ליבכם בשלב זה? בחרו את העדפתכם הראשונית.</p>
            <div class="initial-preference choice-buttons">
                <label class="choice-button">
                    <input type="radio" name="initial-choice" value="A">
                    <span class="choice-text">עיר א'</span>
                </label>
                <label class="choice-button">
                    <input type="radio" name="initial-choice" value="B">
                    <span class="choice-text">עיר ב'</span>
                </label>
                <label class="choice-button">
                    <input type="radio" name="initial-choice" value="Undecided">
                    <span class="choice-text">עדיין לא החלטתי</span>
                </label>
            </div>
             <button onclick="nextStep(4)">המשך: שמיעת דעות עמיתים</button>
        </section>

        <section id="step4" class="app-step">
            <h2>שלב 4: חשיפה לדעות עמיתים בוועד</h2>
            <p>אתם לא לבד בוועד. כעת, היחשפו לדירוגי הקריטריונים וההעדפות הראשוניות של כמה מחבריכם האחרים בוועד. שימו לב לשונות בגישות ובתפיסות.</p>
            <div id="others-opinions" class="opinions-reveal">
                <!-- Content will be generated by JS -->
            </div>
             <button onclick="nextStep(5)">המשך: ההצבעה הסופית</button>
        </section>

        <section id="step5" class="app-step">
            <h2>שלב 5: ההצבעה הסופית</h2>
            <p>שקללתם את הנתונים, בחנתם את העדפתכם הראשונית, ונחשפתם לדעות עמיתיכם. הגיע רגע ההכרעה. מהי הצבעתכם הסופית לבחירת העיר המארחת לאולימפיאדה?</p>
            <div class="final-vote choice-buttons">
                 <label class="choice-button">
                    <input type="radio" name="final-choice" value="A">
                    <span class="choice-text">מצביע/ה עבור עיר א'</span>
                </label>
                <label class="choice-button">
                    <input type="radio" name="final-choice" value="B">
                    <span class="choice-text">מצביע/ה עבור עיר ב'</span>
                </label>
            </div>
             <button onclick="showResults()">שלח את הצבעתי</button>
        </section>

         <section id="results" class="app-step">
            <h2>סיכום ההתנסות האישית שלך</h2>
            <div id="user-summary" class="summary-card">
                <!-- User summary will be generated by JS -->
            </div>
            <div id="group-dynamic-insights" class="insights-card">
                <h3>תובנות על דינמיקה של החלטה קבוצתית:</h3>
                <p>כפי שחוויתם בסימולציה, ההחלטה על בחירת עיר מארחת אולימפית רחוקה מלהיות טכנית או אובייקטיבית בלבד. היא מושפעת משילוב מורכב של גורמים:</p>
                <ul>
                    <li><strong>שונות בסדרי עדיפויות:</strong> ראיתם כיצד חברי ועד שונים נותנים משקל שונה באופן מהותי לקריטריונים זהים, גם כשהם בוחנים את אותם נתונים. זהו הבסיס לדיון ולהתמקחות בתוך הקבוצה.</li>
                    <li><strong>השפעת האחרים:</strong> חשיפה לדעות והעדפות של עמיתים יכולה להשפיע על ההחלטה הסופית שלכם, לעיתים באופן בלתי מודע. מנגנונים כמו הטיה חברתית או לחץ קונפורמיות משחקים תפקיד בדינמיקה קבוצתית.</li>
                    <li><strong>שיקולים מעבר לנתונים היבשים:</strong> החלטות מושפעות גם מתפיסות אישיות, תחושת אמון, היסטוריה קודמת (כמו ניסיון מוצלח של עיר ב' באירוח), ואפילו פוליטיקה פנימית או אינטרסים אישיים בתוך הפורום המקבל את ההחלטה.</li>
                    <li><strong>תהליך ההכרעה:</strong> האם הצבעתכם הסופית נשארה זהה להעדפתכם הראשונית, או שהשתנתה בעקבות חשיפה לדעות האחרים? תהליך זה מדגים כיצד דיון קבוצתי (אפילו סימולטיבי) יכול לעצב מחדש עמדות ראשוניות.</li>
                </ul>
                 <p>תהליכי קבלת החלטות קבוצתיים, במיוחד בפורומים בעלי פרופיל גבוה כמו הוועד האולימפי, הם דוגמה קלאסית לאופן שבו כלכלה התנהגותית ודינמיקה חברתית מתנגשים עם מודלים רציונליים, ויוצרים תוצאה שהיא לרוב תוצר מורכב של כל הגורמים.</p>
            </div>
        </section>

    </div>

    <button id="toggleExplanation" class="toggle-button">הצג הסבר מלא ומעמיק</button>

    <div id="fullExplanation">
        <h2>ההבחירה האולימפית: דינמיקה של החלטה קבוצתית - הסבר מעמיק</h2>
        <h3>האתגר הייחודי של בחירת עיר מארחת אולימפית:</h3>
        <p>בחירת עיר מארחת למשחקים האולימפיים היא מההחלטות המורכבות והבעייתיות ביותר הניצבות בפני הוועד האולימפי הבינלאומי (IOC). מעבר לאתגר הלוגיסטי והפיננסי העצום הכרוך באירוח, ההחלטה משקפת שקלול של אינספור גורמים אובייקטיביים וסובייקטיביים כאחד. ה-IOC, גוף המורכב מחברים ממדינות שונות, בעלי רקעים מגוונים (ספורטאים לשעבר, מנהלים, פוליטיקאים), חייב להגיע להכרעה משותפת שתוביל לאירוח מוצלח תוך הבטחת מורשת חיובית לתנועה האולימפית ולעיר הנבחרת.</p>

        <h3>קבלת החלטות: בין הפרט לקבוצה:</h3>
        <p>בעוד החלטה אישית מתבססת על סדרי העדיפויות וההטיות הקוגניטיביות של אדם יחיד, החלטה קבוצתית היא פועל יוצא של אינטראקציה דינמית בין מספר פרטים. כל אחד מהם מגיע לתהליך עם מערכת אמונות, ידע, אינטרסים גלויים ונסתרים, וסדרי עדיפויות אישיים שונים. התוצאה הסופית של דיון והצבעה קבוצתיים אינה בהכרח ממוצע פשוט או סכום של ההעדפות האישיות, אלא תוצר של תהליכים מורכבים הכוללים משא ומתן, שכנוע, היווצרות קואליציות, ולעיתים גם השפעות פחות רציונליות.</p>

        <h3>הגורמים המעצבים את בחירת חברי הוועד:</h3>
        <ul>
            <li><strong>משקל שונה לקריטריונים אובייקטיביים:</strong> הצעות הערים מציגות נתונים על תשתיות, תקציב, תכנון ביטחוני, וכדומה. אולם, חברים שונים בוועד יתייחסו לנתונים אלו בצורה שונה. עבור חבר אחד, רמת הביטחון היא קו אדום וחשובה מכל; עבור אחר, היקף התקציב והסיכון הכלכלי הם השיקול המרכזי; וחבר שלישי יעדיף עיר עם תמיכה ציבורית רחבה שתבטיח "חגיגה עממית". שונות זו, שהודגמה בשלב 1 של הסימולציה, היא קריטית להבנת תוצאות ההצבעה.</li>
            <li><strong>הטיות קוגניטיביות והתנהגותיות:</strong> גם חברי ועד מנוסים אינם חסינים בפני הטיות התנהגותיות הנחקרות בכלכלה התנהגותית. למשל:
                <ul>
                    <li>**Anchoring (היצמדות לעוגן):** הנתונים הראשונים המוצגים (למשל, גובה התקציב המוצע) עשויים להשפיע באופן לא פרופורציונלי על הערכת ההצעה כולה.</li>
                    <li>**Framing Effect (אפקט המסגור):** הצגת אותם נתונים באופן שונה (למשל, הצגת תקציב גבוה כ"שאפתני" מול הצגתו כ"מסוכן כלכלית") יכולה לשנות את התפיסה.</li>
                    <li>**Overconfidence:** ביטחון יתר ביכולת העיר לעמוד בהבטחותיה, במיוחד על בסיס רושם ראשוני או הצגה מרשימה.</li>
                </ul>
            </li>
            <li><strong>השפעה חברתית (Social Proof & Conformity):</strong> כאמור, בני אדם מושפעים מסביבתם. בשלב 4 של הסימולציה, נחשפתם לדעות עמיתיכם. למידע זה יכולה להיות השפעה משמעותית. אם רוב החברים נוטים לכיוון מסוים, הדבר עשוי לגרום לחשיבה מחודשת ("אולי הם רואים משהו שאני מפספס?"), או אפילו ללחץ בלתי מודע להתיישר עם דעת הרוב כדי לא לבלוט או להישאר במיעוט (קונפורמיות).</li>
            <li><strong>אינטרסים אישיים ואסטרטגיים:</strong> למרות שחברי הוועד מחויבים לבחור את העיר הטובה ביותר למען התנועה האולימפית, גם שיקולים אישיים ואסטרטגיים יכולים להיכנס לתמונה. הדבר יכול לכלול רצון לתמוך במדינה מסוימת מסיבות פוליטיות/דיפלומטיות, חיזוק קשרים עם חברים אחרים בוועד, או אפילו יצירת הזדמנויות עתידיות (תפקידים, ייעוץ) בעיר שתבחר.</li>
            <li><strong>היסטוריה ונרטיב:</strong> סיפור הרקע של העיר, ניסיונות קודמים (מוצלחים או כושלים), והנרטיב שהיא בונה סביב הצעתה ("המשחקים הירוקים ביותר", "המשחקים שיחברו את העיר") משחקים תפקיד רגשי ותפיסתי חשוב.</li>
        </ul>

        <h3>מדוע התוצאה אינה תמיד צפויה:</h3>
        <p>השילוב של כל הגורמים הללו מסביר מדוע תהליך הבחירה האולימפית (ותהליכי קבלת החלטות קבוצתיים רבים אחרים ברמות הגבוהות) הוא לעיתים בלתי צפוי. הצעה שנראית "מנצחת" על הנייר מבחינה אובייקטיבית עלולה להפסיד להצעה אחרת שקולעת טוב יותר לסדרי העדיפויות המשותפים (והלעיתים נסתרים) של רוב חברי הגוף הבוחר, מושפעת פחות מהטיות קוגניטיביות, או נהנית מתמיכה חברתית או פוליטית רחבה יותר ברגע האמת. הסימולציה מאפשרת לכם לחוות בעצמכם כיצד סדרי העדיפויות האישיים שלכם מתנגשים או מתיישבים עם נתוני ההצעות, וכיצד חשיפה לדעות אחרים עשויה לערער או לחזק את העדפתכם הראשונית, בדרך להחלטה הסופית.</p>
    </div>
</div>

<style>
    /* Overall Container and Body Reset */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6;
        margin: 0;
        padding: 0;
        direction: rtl; /* Ensure right-to-left for Hebrew */
        text-align: right;
    }

    .olympic-container {
        max-width: 850px;
        margin: 30px auto;
        padding: 30px;
        background-color: #fff;
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        overflow: hidden; /* Clear floats/margins */
    }

    .olympic-container h1 {
        text-align: center;
        color: #003366; /* Dark blue, inspired by Olympic rings */
        margin-bottom: 20px;
        font-size: 2em;
        border-bottom: 3px solid #ffcc00; /* Gold color */
        padding-bottom: 15px;
    }

    .intro-text {
        text-align: center;
        font-size: 1.1em;
        color: #555;
        margin-bottom: 40px;
    }

    /* App Steps Styling */
    #olympic-app {
        position: relative;
        min-height: 500px; /* Ensure enough space for step content */
    }

    .app-step {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        padding: 20px 0;
        transition: opacity 0.5s ease-in-out;
        opacity: 0;
        visibility: hidden; /* Hide completely when not active */
        z-index: 1; /* Stack steps */
    }

    .app-step.active-step {
        opacity: 1;
        visibility: visible;
        z-index: 2; /* Bring active step to front */
    }

    .app-step h2 {
        color: #0056b3; /* Medium blue */
        border-bottom: 2px solid #eee;
        padding-bottom: 10px;
        margin-top: 0;
        margin-bottom: 25px;
        font-size: 1.6em;
    }

    .app-step p {
        margin-bottom: 20px;
        color: #444;
    }

    /* Step 1: Ranking */
    .criteria-ranking {
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .criterion-item {
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        border-radius: 6px;
        padding: 12px 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: background-color 0.3s ease;
    }

    .criterion-item:hover {
         background-color: #f0f0f0;
    }

    .criterion-item label {
        flex-grow: 1;
        margin-left: 15px; /* Adjust for RTL */
        font-weight: bold;
        color: #555;
    }

    .criterion-item select {
        padding: 8px 10px;
        border-radius: 4px;
        border: 1px solid #ccc;
        background-color: #fff;
        font-size: 1em;
        cursor: pointer;
        transition: border-color 0.3s ease;
    }
    .criterion-item select:focus {
        outline: none;
        border-color: #0056b3;
        box-shadow: 0 0 0 0.2rem rgba(0, 86, 179, 0.25);
    }

    /* Step 2: City Data */
    .cities-data {
        display: flex;
        gap: 25px;
        margin-top: 20px;
        flex-wrap: wrap;
    }

    .city-card {
        flex: 1;
        min-width: 320px;
        border: 1px solid #ccc;
        border-radius: 10px;
        padding: 20px;
        background-color: #fff;
        box-shadow: 0 3px 8px rgba(0,0,0,0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
     .city-card:hover {
         transform: translateY(-5px);
         box-shadow: 0 8px 20px rgba(0,0,0,0.12);
     }

    .city-card.city-a {
        border-top: 5px solid #007bff; /* City A accent color */
    }
     .city-card.city-b {
        border-top: 5px solid #28a745; /* City B accent color */
    }


    .city-card h3 {
        color: #0056b3;
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.4em;
        display: flex;
        align-items: center;
    }
    .city-card .city-icon {
        margin-left: 10px; /* Adjust for RTL */
        font-size: 1.2em;
    }


    .city-card ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .city-card li {
        margin-bottom: 12px;
        padding-bottom: 10px;
        border-bottom: 1px dashed #eee;
        display: flex;
        align-items: flex-start;
    }
     .city-card li:last-child {
         border-bottom: none;
         margin-bottom: 0;
     }

     .city-card li strong {
         color: #333;
         margin-left: 8px; /* Adjust for RTL */
     }
     .city-card li .list-icon {
         margin-left: 8px; /* Adjust for RTL */
         font-size: 1.1em;
         color: #666;
     }


    /* Steps 3 & 5: Choices (Radio Buttons) */
    .choice-buttons {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        margin-top: 20px;
        justify-content: center; /* Center the choices */
    }

    .choice-button {
        display: block;
        background-color: #f0f0f0;
        border: 2px solid #ddd;
        border-radius: 8px;
        padding: 15px 25px;
        cursor: pointer;
        transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.2s ease;
        font-size: 1.1em;
        color: #555;
        text-align: center;
        flex-grow: 1;
        min-width: 150px;
        max-width: 250px;
    }

    .choice-button:hover {
        background-color: #e9e9e9;
        border-color: #ccc;
    }

     .choice-button input[type="radio"] {
         display: none; /* Hide actual radio button */
     }

     .choice-button input[type="radio"]:checked + .choice-text {
         font-weight: bold;
         color: #0056b3;
     }

    .choice-button input[type="radio"]:checked + .choice-text::before {
         content: '✅ '; /* Add a checkmark */
    }

     .choice-button input[type="radio"]:checked {
         /* Style the container when checked */
         border-color: #0056b3;
         background-color: #eef;
         transform: translateY(-3px);
         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
     }


    /* Step 4: Others Opinions */
    .opinions-reveal {
        margin-top: 20px;
        border: 1px solid #b3e0ff; /* Light blue border */
        border-radius: 8px;
        padding: 20px;
        background-color: #eef2ff; /* Very light blue background */
        box-shadow: inset 0 0 10px rgba(0, 123, 255, 0.1);
    }

    .opinion-item {
        margin-bottom: 25px;
        padding-bottom: 20px;
        border-bottom: 1px dashed #b3e0ff;
    }
    .opinion-item:last-child {
        border-bottom: none;
        margin-bottom: 0;
        padding-bottom: 0;
    }


    .opinion-item h4 {
        margin-top: 0;
        color: #004085; /* Darker blue */
        margin-bottom: 10px;
        font-size: 1.3em;
    }

    .opinion-item .opinion-rankings ul,
    .opinion-item .opinion-preference p {
        margin-bottom: 10px;
    }

    .opinion-item .opinion-rankings ul {
        list-style: disc;
        margin-left: 20px;
        color: #555;
    }
     .opinion-item .opinion-rankings li {
         margin-bottom: 5px;
     }

    .opinion-item .opinion-preference p {
        font-style: italic;
        color: #333;
         margin-top: 15px;
         border-top: 1px dotted #cce;
         padding-top: 10px;
    }


    /* Results Section */
    .summary-card, .insights-card {
        margin-top: 20px;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
    }

    .summary-card {
        border: 1px solid #cce5ff; /* Light blue */
        background-color: #e2f3ff; /* Very light blue */
    }

    .insights-card {
        border: 1px solid #d4edda; /* Light green */
        background-color: #f8f9fa; /* Very light gray */
        margin-top: 30px;
    }


    .summary-card h3, .insights-card h3 {
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.4em;
        border-bottom: 2px solid rgba(0,0,0,0.05);
        padding-bottom: 8px;
    }
    .summary-card h3 { color: #004085; }
    .insights-card h3 { color: #155724; }


    .summary-card p {
        margin-bottom: 10px;
        color: #333;
    }
    .summary-card p strong {
         color: #0056b3;
    }

     .summary-card p i {
         display: block; /* Put comparison note on new line */
         margin-top: 15px;
         padding-top: 10px;
         border-top: 1px dotted #b3d7ff;
         color: #004085;
     }


    .insights-card ul {
        list-style: disc;
        margin-left: 20px;
        margin-bottom: 15px;
        color: #333;
    }
     .insights-card li {
         margin-bottom: 10px;
     }
     .insights-card li strong {
         color: #1e7e34; /* Darker green */
     }


    /* Buttons */
    button {
        display: block;
        margin: 30px auto 10px auto; /* More space above button */
        padding: 12px 25px;
        background-color: #0056b3;
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.2s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    button:hover {
        background-color: #004494;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
     button:active {
         transform: translateY(0);
         box-shadow: 0 1px 3px rgba(0,0,0,0.1);
     }


    .toggle-button {
        display: block;
        margin: 40px auto 20px auto; /* More space around toggle */
        padding: 10px 20px;
        background-color: #6c757d; /* Gray */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease;
    }

    .toggle-button:hover {
        background-color: #5a6268;
    }

    /* Full Explanation Section */
    #fullExplanation {
        max-width: 850px;
        margin: 20px auto;
        padding: 30px;
        border: 1px solid #ddd;
        border-radius: 12px;
        background-color: #fff;
        line-height: 1.7;
        color: #333;
        box-shadow: 0 3px 10px rgba(0,0,0,0.05);
        display: none; /* Initially hidden */
    }

     #fullExplanation h2 {
         text-align: center;
         color: #003366;
         margin-top: 0;
         margin-bottom: 20px;
         border-bottom: 2px solid #eee;
         padding-bottom: 10px;
         font-size: 1.8em;
     }

     #fullExplanation h3 {
         color: #0056b3;
         margin-top: 25px;
         margin-bottom: 12px;
         border-bottom: 1px dashed #ccc;
         padding-bottom: 6px;
         font-size: 1.4em;
     }
    #fullExplanation p {
        margin-bottom: 15px;
        text-align: justify; /* Justify explanation text */
    }
    #fullExplanation ul {
         list-style: disc;
         margin-left: 25px;
         margin-bottom: 15px;
         padding: 0;
    }
     #fullExplanation li {
         margin-bottom: 8px;
         color: #444;
     }
     #fullExplanation li strong {
         color: #004085;
     }
     #fullExplanation ul ul { /* Nested lists */
         margin-top: 8px;
         margin-bottom: 8px;
         list-style: circle;
         margin-left: 20px;
     }


    /* Responsive Adjustments */
    @media (max-width: 768px) {
        .olympic-container {
            margin: 20px;
            padding: 20px;
        }
        .cities-data {
            flex-direction: column;
            gap: 15px;
        }
        .city-card {
             min-width: unset; /* Allow cards to shrink */
             width: 100%;
        }
        .choice-buttons {
            flex-direction: column;
            align-items: stretch; /* Stretch buttons to full width */
        }
        .choice-button {
            min-width: unset;
            max-width: unset;
             width: 100%;
             text-align: center;
        }
        #fullExplanation {
            margin: 20px;
            padding: 20px;
        }
    }

</style>

<script>
    let userRankings = {};
    let userInitialPreference = '';
    let userFinalVote = '';
    const numCriteria = 6; // Total number of criteria for validation

    // Simulated data for other committee members
    const othersOpinions = [
        {
            name: 'חבר ועד אליסון',
            rankings: { infra: 4, budget: 2, security: 1, support: 5, legacy: 3, experience: 6 },
            initialPreference: 'B', // Prioritizes security, lower budget, legacy somewhat
            bio: 'מומחית ביטחון וספורט לשעבר, תמיד מדגישה סיכונים ומוכנות.'
        },
         {
            name: 'חבר ועד קרלוס',
            rankings: { infra: 1, budget: 5, security: 3, support: 2, legacy: 4, experience: 6 },
            initialPreference: 'A', // Prioritizes infra, support, less concerned about budget
            bio: 'מהנדס אזרחי בעבר וראש ועד אולימפי במדינה קטנה, ממוקד בתשתיות וחיבור לציבור.'
        },
         {
            name: 'חברת ועד פטרה',
            rankings: { infra: 6, budget: 4, security: 2, support: 5, legacy: 1, experience: 3 },
            initialPreference: 'B', // Prioritizes security, legacy, experience, least infra
            bio: 'היסטוריונית של התנועה האולימפית, שמה דגש על מורשת ארוכת טווח וניסיון מוכח.'
        }
    ];

    const criterionLabels = {
        'infra': 'תשתיות קיימות ומוכנות',
        'budget': 'תקציב ומוכנות פיננסית',
        'security': 'היבטים ביטחוניים ובטיחות',
        'support': 'תמיכה ציבורית ומקומית',
        'legacy': 'מורשת צפויה והשפעה ארוכת טווח',
        'experience': 'ניסיון קודם באירוח אירועים גדולים'
    };

    // Store selected options for Step 1 validation
    const selectedRanks = new Set();

    // Function to update selectedRanks set and provide immediate feedback
    function updateSelectedRanks(selectElement) {
        // Remove the previous value if it exists in the set
        const previousValue = selectElement.dataset.previousValue;
        if (previousValue && selectedRanks.has(parseInt(previousValue))) {
            selectedRanks.delete(parseInt(previousValue));
        }

        const currentValue = selectElement.value;
        if (currentValue !== "") {
            const rank = parseInt(currentValue);
            selectedRanks.add(rank);
            // Store current value for next change
            selectElement.dataset.previousValue = currentValue;
        } else {
             // If value is reset to empty, remove it from set
             delete selectElement.dataset.previousValue;
        }

        // Optional: Add visual feedback based on selection validity (more complex, skip for strict constraints)
        // For now, the validation check is done in nextStep(2)
    }

    // Add event listeners to ranking selects for immediate feedback (optional but good interaction)
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('#step1 .criterion-rank').forEach(select => {
            select.addEventListener('change', (event) => {
                 updateSelectedRanks(event.target);
            });
        });

         // Add event listeners for styling radio buttons
         document.querySelectorAll('.choice-buttons input[type="radio"]').forEach(radio => {
             radio.addEventListener('change', (event) => {
                 // Remove 'checked' class from all siblings
                 event.target.closest('.choice-buttons').querySelectorAll('.choice-button').forEach(label => {
                     label.classList.remove('checked');
                 });
                 // Add 'checked' class to the parent label of the selected radio
                 event.target.closest('.choice-button').classList.add('checked');
             });
         });

         // Initial check for explanation display state (if page history affects it)
         const explanationDiv = document.getElementById('fullExplanation');
         const toggleButton = document.getElementById('toggleExplanation');
         if (explanationDiv.style.display === 'block') {
             toggleButton.textContent = 'הסתר הסבר מלא ומעמיק';
         } else {
             toggleButton.textContent = 'הצג הסבר מלא ומעמיק';
         }

    });


    function nextStep(step) {
        let currentStep = document.querySelector('.app-step.active-step');

        // Validation before moving from Step 1
        if (step === 2) {
             const ranks = document.querySelectorAll('#step1 .criterion-rank');
             let valid = true;
             const tempSelected = new Set();
             userRankings = {};

             ranks.forEach(select => {
                 if (select.value === "") {
                     valid = false;
                 } else {
                     const rank = parseInt(select.value);
                      if (tempSelected.has(rank)) {
                          valid = false; // Check for duplicate ranks
                      }
                      tempSelected.add(rank);
                     const criterionKey = select.id.replace('rank-', '');
                     userRankings[criterionKey] = rank;
                 }
             });

             // Check if all numbers from 1 to numCriteria are used
             if (tempSelected.size !== numCriteria) {
                 valid = false; // Not all numbers used or duplicates exist preventing size = numCriteria
             } else {
                 for(let i = 1; i <= numCriteria; i++) {
                     if (!tempSelected.has(i)) {
                         valid = false; // A number from 1-6 is missing
                         break;
                     }
                 }
             }


             if (!valid) {
                 alert(`אנא דרג את כל ${numCriteria} הקריטריונים באמצעות המספרים 1 עד ${numCriteria} בדיוק פעם אחת לכל מספר.`);
                 return; // Stop the function if not valid
             }

             // Sort user rankings by rank (from 1 to 6) for display later
             userRankings = Object.entries(userRankings)
                 .sort(([, rankA], [, rankB]) => rankA - rankB)
                 .reduce((obj, [key, value]) => {
                     obj[key] = value;
                     return obj;
                 }, {});

        } else if (step === 4) {
             // Validation before moving from Step 3
             const initialChoiceRadios = document.querySelectorAll('input[name="initial-choice"]');
             let initialChoiceSelected = false;
             for (const radio of initialChoiceRadios) {
                 if (radio.checked) {
                     userInitialPreference = radio.value;
                     initialChoiceSelected = true;
                     break;
                 }
             }
             if (!initialChoiceSelected) {
                 alert("אנא בחר את העדפתך הראשונית.");
                 return; // Stop the function if not valid
             }

             // Populate others' opinions just before showing the step
             displayOthersOpinions();
        }


        // Step transition logic
        const nextStepElement = document.getElementById(`step${step}`);
        if (currentStep) {
            currentStep.classList.remove('active-step');
             // Optional: Add a small delay before showing next step for fade effect
             setTimeout(() => {
                 currentStep.style.display = 'none'; // Hide completely after transition
             }, 500); // Match CSS transition duration
        }

         // Need to make the next step visible (but maybe still transparent) before transitioning opacity
        nextStepElement.style.display = 'block'; // Make it block first
        setTimeout(() => { // Allow display:block to apply
            nextStepElement.classList.add('active-step');
        }, 50); // A small delay is usually enough
    }

    function displayOthersOpinions() {
        const container = document.getElementById('others-opinions');
        container.innerHTML = ''; // Clear previous content

        othersOpinions.forEach(member => {
            const memberDiv = document.createElement('div');
            memberDiv.classList.add('opinion-item');

            memberDiv.innerHTML = `<h4>${member.name}</h4><p>${member.bio}</p>`;

            // Display rankings
            const rankingsSection = document.createElement('div');
            rankingsSection.classList.add('opinion-rankings');
            rankingsSection.innerHTML = `<strong>סדרי עדיפויות (דירוג מהחשוב לפחות חשוב):</strong>`;
            const rankingsList = document.createElement('ul');
             // Sort rankings for display
             const sortedRankings = Object.entries(member.rankings)
                 .sort(([, rankA], [, rankB]) => rankA - rankB);

             sortedRankings.forEach(([key, rank]) => {
                 const listItem = document.createElement('li');
                 listItem.innerHTML = `${rank}. ${criterionLabels[key]}`;
                 rankingsList.appendChild(listItem);
             });
            rankingsSection.appendChild(rankingsList);
            memberDiv.appendChild(rankingsSection);


            // Display initial preference
            const preferenceSection = document.createElement('div');
            preferenceSection.classList.add('opinion-preference');
            const preferencePara = document.createElement('p');
             let initialPrefText = `<strong>העדפה ראשונית:</strong> `;
             if (member.initialPreference === 'Undecided') {
                  initialPrefText += 'עדיין לא החליט/ה';
             } else {
                 initialPrefText += `עיר ${member.initialPreference}`;
             }
             preferencePara.innerHTML = initialPrefText;
             preferenceSection.appendChild(preferencePara);
            memberDiv.appendChild(preferenceSection);


            container.appendChild(memberDiv);
        });
    }


    function showResults() {
         const finalChoiceRadios = document.querySelectorAll('input[name="final-choice"]');
         let finalChoiceSelected = false;
         for (const radio of finalChoiceRadios) {
             if (radio.checked) {
                 userFinalVote = radio.value;
                 finalChoiceSelected = true;
                 break;
             }
         }
         if (!finalChoiceSelected) {
             alert("אנא בחר את הצבעתך הסופית.");
             return; // Stop the function if not valid
         }

        let currentStep = document.querySelector('.app-step.active-step');
        const resultsElement = document.getElementById('results');

        if (currentStep) {
            currentStep.classList.remove('active-step');
             setTimeout(() => {
                 currentStep.style.display = 'none';
             }, 500);
        }

        displayUserSummary(); // Generate summary content

        resultsElement.style.display = 'block';
         setTimeout(() => {
             resultsElement.classList.add('active-step');
         }, 50);
    }

    function displayUserSummary() {
        const summaryDiv = document.getElementById('user-summary');
        summaryDiv.innerHTML = '<h3>סיכום ההתנסות שלך:</h3>';

        // User Rankings
        const userRankingsPara = document.createElement('p');
         let rankingsText = '<strong>דירוג הקריטריונים שלך (מהחשוב לפחות חשוב):</strong><br>';
         // userRankings is already sorted from nextStep(2)
         Object.entries(userRankings).forEach(([key, rank]) => {
            rankingsText += `${rank}. ${criterionLabels[key]}<br>`;
         });
         userRankingsPara.innerHTML = rankingsText;
        summaryDiv.appendChild(userRankingsPara);


        // User Initial Preference
        const initialPrefPara = document.createElement('p');
         let initialPrefText = '<strong>העדפתך הראשונית לאחר סקירת נתוני הערים:</strong> ';
         if (userInitialPreference === 'Undecided') {
              initialPrefText += 'עדיין לא החלטתי';
         } else {
             initialPrefText += `עיר ${userInitialPreference}`;
         }
         initialPrefPara.innerHTML = initialPrefText;
        summaryDiv.appendChild(initialPrefPara);

        // User Final Vote
        const finalVotePara = document.createElement('p');
        finalVotePara.innerHTML = `<strong>הצבעתך הסופית לאחר חשיפה לדעות עמיתים:</strong> עיר ${userFinalVote}`;
        summaryDiv.appendChild(finalVotePara);

         // Comparison
         if (userInitialPreference !== 'Undecided') {
             const comparisonPara = document.createElement('p');
             if (userFinalVote !== userInitialPreference) {
                 comparisonPara.innerHTML = `<i>שימו לב: הצבעתכם הסופית <span style="color: darkred; font-weight: bold;">שונה</span> מהעדפתכם הראשונית. נסו לחשוב מה גרם לשינוי לאחר שנחשפתם לדעות עמיתיכם?</i>`;
             } else {
                 comparisonPara.innerHTML = `<i>שימו לב: הצבעתכם הסופית נשארה <span style="color: darkgreen; font-weight: bold;">זהה</span> להעדפתכם הראשונית.</i>`;
             }
             summaryDiv.appendChild(comparisonPara);
         }
    }


    // Explanation Toggle Logic
    document.getElementById('toggleExplanation').addEventListener('click', function() {
        const explanationDiv = document.getElementById('fullExplanation');
        const button = this;
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            button.textContent = 'הסתר הסבר מלא ומעמיק';
             // Optional: Scroll to explanation smoothly
             explanationDiv.scrollIntoView({ behavior: 'smooth' });
        } else {
            explanationDiv.style.display = 'none';
            button.textContent = 'הצג הסבר מלא ומעמיק';
        }
    });

    // Initialize the first step display (should be done on page load)
    document.addEventListener('DOMContentLoaded', (event) => {
        document.getElementById('step1').classList.add('active-step');
        document.getElementById('step1').style.display = 'block'; // Ensure step 1 is block initially
    });


</script>
```