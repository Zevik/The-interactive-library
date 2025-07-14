---
title: "היברידי נטו: מסע אינטראקטיבי ללב המכונית ההיברידית"
english_slug: hybrid-pure-interactive-journey-to-the-heart-of-the-hybrid-car
category: "הנדסה"
tags: [רכב היברידי, הנעה חשמלית, מנוע בעירה פנימית, חיסכון בדלק, מערכות רכב]
---
# היברידי נטו: מסע אינטראקטיבי ללב המכונית ההיברידית

איך ייתכן שמכונית היברידית, עם שני מקורות כוח שונים לחלוטין, מצליחה להיות גם חסכונית יותר באופן דרמטי וגם לרוב בעלת ביצועים זריזים יותר ממקבילה עם מנוע בנזין בלבד? הסוד העצום טמון בניהול על-אנושי וחכם של מעברי הכוח הדינמיים בין המנועים השונים, בהתאם למצב הנהיגה המשתנה מרגע לרגע. צאו איתנו למסע מרתק לראות איך הקסם ההיברידי עובד בזמן אמת!

<div class="hybrid-simulator-container">
    <h2>מנוע הכוח הפנימי: הדמיית זרימת אנרגיה היברידית</h2>
    <p class="simulator-intro">לחצו על תרחיש נסיעה כדי לראות איך מערכת ההנעה ההיברידית מתאימה את עצמה.</p>
    <div class="simulator-controls">
        <button data-scenario="start-slow">זינוק שקט (חשמל טהור)</button>
        <button data-scenario="acceleration">שחרור הכוח המלא (האצה)</button>
        <button data-scenario="constant-speed">שיוט חסכוני (כביש פתוח)</button>
        <button data-scenario="deceleration">לכידת אנרגיה (האטה/בלימה)</button>
        <button data-scenario="idle">מנוחה שקטה (עמידה בפקק)</button>
        <button data-scenario="charge">אנרגיה למחר (טעינת סוללה)</button>
    </div>
    <div class="hybrid-diagram">
        <div class="component engine">מנוע בנזין<br>⛽</div>
        <div class="component battery">סוללה<br>🔋</div>
        <div class="component emg">מנוע/גנרטור<br>⚡</div>
        <div class="component power-split">מערכת חלוקת כוח<br>⚙️</div>
        <div class="component wheels">גלגלים<br>🚗</div>

        <!-- Arrows representing power flow -->
        <!-- Paths: engine->power-split, engine->emg(gen), battery->emg(motor), emg->power-split, power-split->wheels, wheels->emg(regen) -->
        <div class="flow-arrow engine-to-ps" data-path="engine-to-ps" data-components="engine,power-split,wheels"></div>
        <div class="flow-arrow engine-to-emg" data-path="engine-to-emg" data-components="engine,emg,battery"></div>
        <div class="flow-arrow battery-to-emg" data-path="battery-to-emg" data-components="battery,emg,power-split,wheels"></div>
        <div class="flow-arrow emg-to-ps" data-path="emg-to-ps" data-components="emg,power-split,wheels"></div>
        <div class="flow-arrow ps-to-wheels" data-path="ps-to-wheels" data-components="power-split,wheels"></div>
        <div class="flow-arrow wheels-to-emg" data-path="wheels-to-emg" data-components="wheels,emg,battery"></div>
    </div>
    <div class="scenario-explanation">
        <p>בחרו תרחיש כדי לראות את זרימת הכוח הקסומה בפעולה!</p>
    </div>
</div>

<style>
/* כללי וטיפוגרפיה */
.hybrid-simulator-container {
    font-family: 'Arial', sans-serif;
    direction: rtl;
    text-align: center;
    margin: 20px auto;
    padding: 30px 20px;
    background: linear-gradient(to bottom right, #eef2f7, #dce6f0); /* מעבר צבע רקע עדין */
    border-radius: 12px; /* פינות עגולות יותר */
    border: 1px solid #c3d4e5; /* גבול עדין יותר */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* צל רך ומעודן */
    max-width: 800px; /* הגבלה רוחב מרבית */
    position: relative; /* עבור אפקטים עתידיים אולי */
    overflow: hidden; /* למקרה של אנימציות יוצאות מגבולות */
}

.hybrid-simulator-container h2 {
    color: #0056b3; /* כחול כהה יותר לכותרת */
    margin-bottom: 10px;
    font-size: 1.8rem;
    font-weight: bold;
}

.simulator-intro {
    color: #555;
    margin-bottom: 25px;
    font-size: 1.1rem;
}

/* בקרי סימולטור - כפתורים */
.simulator-controls {
    margin-bottom: 30px;
    display: flex; /* סידור כפתורים בשורה */
    flex-wrap: wrap; /* גלישת כפתורים לשורה חדשה אם אין מקום */
    justify-content: center; /* מרכוז כפתורים */
    gap: 10px; /* רווח בין כפתורים */
}

.simulator-controls button {
    margin: 0; /* הסרת margin שהיה לפני כן */
    padding: 12px 20px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    background-color: #4285f4; /* כחול גוגל-סטייל */
    color: white;
    font-size: 1rem;
    font-weight: 500;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.simulator-controls button:hover {
    background-color: #357ae8; /* כחול כהה יותר במעבר עכבר */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.simulator-controls button:active {
    transform: scale(0.98); /* אפקט לחיצה קל */
}

.simulator-controls button.selected {
     background-color: #0f9d58; /* ירוק גוגל-סטייל לכפתור הנבחר */
     box-shadow: 0 3px 6px rgba(0, 0, 0, 0.2);
     font-weight: bold;
}


/* דיאגרמת המערכת */
.hybrid-diagram {
    position: relative;
    width: 100%;
    max-width: 700px; /* שמירה על רוחב מרבי */
    height: 350px; /* הגדלת גובה ליותר מרווח */
    margin: 20px auto;
    border: 1px solid #ddd;
    background-color: #ffffff; /* רקע לבן לדיאגרמה */
    border-radius: 8px;
    box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.05); /* צל פנימי עדין */
}

/* רכיבי המערכת */
.component {
    position: absolute;
    width: 110px; /* הגדלה קלה */
    height: 70px; /* הגדלה קלה */
    line-height: 1.3; /* שיפור ריווח שורות לטקסט + אייקון */
    padding-top: 10px; /* ריפוד עליון עבור טקסט ואייקון */
    border: 2px solid #666; /* גבול כהה יותר */
    border-radius: 10px; /* פינות עגולות יותר */
    background-color: #f0f0f0; /* רקע אפור בהיר */
    font-size: 0.9rem;
    font-weight: bold;
    text-align: center;
    color: #333;
    z-index: 10; /* לוודא שהרכיבים מעל החצים */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* צל לרכיבים */
    transition: background-color 0.4s ease, box-shadow 0.4s ease, transform 0.2s ease; /* אנימציית מעבר לרכיבים */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.component.active {
     background-color: #c8e6c9; /* רקע ירוק בהיר כשהרכיב פעיל */
     border-color: #388e3c; /* גבול ירוק כהה יותר */
     box-shadow: 0 6px 12px rgba(40, 167, 69, 0.3), 0 0 10px rgba(40, 167, 69, 0.5); /* צל וזוהר ירוק */
     transform: scale(1.05); /* הגדלה קלה כאנימציית פעילות */
}

/* מיקום רכיבים - עדכון מיקומים עבור גודל וגובה חדשים */
.engine { top: 30px; left: 50%; transform: translateX(-110%) translateY(0%); background-color: #ffcc80; } /* כתום למנוע בנזין */
.battery { top: 30px; left: 50%; transform: translateX(10%) translateY(0%); background-color: #a5d6a7; } /* ירוק לסוללה */
.emg { top: 140px; left: 50%; transform: translateX(-50%) translateY(0%); background-color: #81d4fa; } /* תכלת למנוע/גנרטור */
.power-split { top: 140px; left: 50%; transform: translateX(60%) translateY(0%); background-color: #e1bee7; } /* סגול בהיר לחלוקת כוח */
.wheels { top: 250px; left: 50%; transform: translateX(-50%) translateY(0%); background-color: #bdbdbd; } /* אפור לגלגלים */


/* חצים - סטיילינג כללי */
.flow-arrow {
    position: absolute;
    background-color: #b0bec5; /* צבע אפור כסוף כשהלא פעיל */
    transition: background-color 0.4s ease, box-shadow 0.4s ease, opacity 0.4s ease; /* הוספת מעבר עדין */
    z-index: 5; /* לוודא שהחצים מתחת לרכיבים */
    opacity: 0.8; /* שקיפות קלה כשהלא פעיל */
}

.flow-arrow.active {
    background-color: #4caf50; /* ירוק פעיל */
    box-shadow: 0 0 12px #4caf50; /* זוהר ירוק */
    opacity: 1; /* שקיפות מלאה כשהפעיל */
    /* אנימציית זרימה - דורש gradient + keyframes */
    background-image: linear-gradient(to right, #4caf50 0%, #81c784 50%, #4caf50 100%);
    background-size: 200% auto; /* גודל כפול לאפקט זרימה */
    animation: flow 1.5s linear infinite; /* אנימציית זרימה */
}

/* Keyframes לאנימציית זרימה */
@keyframes flow {
    to {
        background-position: 200% 0; /* הזזת הרקע ימינה ליצירת אפקט זרימה */
    }
}

/* מיקום ועיצוב החצים - עובי מוגבר */
.engine-to-ps {
    top: 65px;
    left: calc(50% - 100px);
    width: 170px;
    height: 6px; /* עובי */
    transform-origin: right center;
    transform: translateY(75px) rotate(0deg); /* התאמת מיקום */
     background-image: linear-gradient(to right, #b0bec5 0%, #b0bec5 100%); /* ברירת מחדל ל gradient */
}
.engine-to-emg {
    top: 95px;
    left: calc(50% - 60px);
    width: 6px; /* עובי */
    height: 45px;
     background-image: linear-gradient(to bottom, #b0bec5 0%, #b0bec5 100%);
}

.battery-to-emg {
    top: 95px;
    left: calc(50% + 60px - 6px);
    width: 6px; /* עובי */
    height: 45px;
     background-image: linear-gradient(to bottom, #b0bec5 0%, #b0bec5 100%);
}

.emg-to-ps {
    top: 175px;
    left: calc(50% + 60px);
    width: 70px;
    height: 6px; /* עובי */
     background-image: linear-gradient(to right, #b0bec5 0%, #b0bec5 100%);
}

.ps-to-wheels {
    top: 210px;
    left: calc(50% + 60px - 6px);
    width: 6px; /* עובי */
    height: 40px;
    transform-origin: center top;
    transform: translateX(-60px); /* מרכוז */
     background-image: linear-gradient(to bottom, #b0bec5 0%, #b0bec5 100%);
}

.wheels-to-emg {
     top: 220px; /* מעל הגלגלים */
     left: calc(50% + 60px - 6px);
     width: 6px; /* עובי */
     height: 30px; /* קצר יותר */
     transform-origin: center bottom;
     transform: translateX(-60px); /* מרכוז */
     /* בלימה רגנרטיבית - זרימה הפוכה, gradient הפוך ואנימציה הפוכה */
     background-image: linear-gradient(to top, #b0bec5 0%, #b0bec5 100%);
}

/* אנימציית זרימה הפוכה (לבלימה רגנרטיבית) */
.wheels-to-emg.active {
    background-image: linear-gradient(to top, #4caf50 0%, #81c784 50%, #4caf50 100%);
    background-size: 200% auto;
    animation: flow-reverse 1.5s linear infinite;
}

@keyframes flow-reverse {
    to {
        background-position: -200% 0;
    }
}


/* איזור ההסבר הקצר למטה */
.scenario-explanation {
    margin-top: 25px;
    padding: 15px;
    background-color: #e3f2fd; /* כחול בהיר מאוד */
    border-radius: 8px;
    min-height: 40px; /* שמירת מרווח */
    color: #0277bd; /* כחול עמוק */
    font-size: 1.1rem;
    font-weight: 500;
}

/* כפתור הצגת/הסתרת הסבר מפורט */
.explanation-toggle-button {
    margin-top: 30px;
    padding: 12px 25px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    background-color: #607d8b; /* אפור כחלחל */
    color: white;
    font-size: 1rem;
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.explanation-toggle-button:hover {
    background-color: #546e7a;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* הסבר מפורט */
.full-explanation {
    margin-top: 30px;
    text-align: right;
    line-height: 1.7;
    border-top: 1px solid #c3d4e5;
    padding-top: 25px;
    color: #333; /* צבע טקסט רגיל */
    transition: all 0.5s ease-in-out; /* אנימציית הופעה/הסתרה עדינה */
    opacity: 1; /* גלוי כברירת מחדל אם לא hidden */
    max-height: 2000px; /* גובה מקסימלי גבוה מספיק כדי לאפשר אנימציה */
    overflow: hidden; /* הסתרת גלילה פנימית בזמן האנימציה */
}

.full-explanation.hidden {
    opacity: 0;
    max-height: 0; /* כיווץ לגובה 0 כשהוסתר */
    padding-top: 0; /* הסרת ריפוד עליון כשהוסתר */
    border-top: none; /* הסרת גבול עליון כשהוסתר */
}


.full-explanation h2 {
    margin-top: 15px;
    margin-bottom: 10px;
    color: #0056b3;
    font-size: 1.5rem;
    font-weight: bold;
}

.full-explanation h3 { /* תת כותרות לרכיבים ומצבי פעולה */
    margin-top: 15px;
    margin-bottom: 8px;
    color: #0277bd; /* כחול עמוק יותר */
    font-size: 1.2rem;
    font-weight: bold;
}

.full-explanation p {
    margin-bottom: 15px; /* ריווח גדול יותר בין פסקאות */
}

.full-explanation ul {
    margin-bottom: 15px;
    padding-right: 20px; /* הזחה לרשימות */
}

.full-explanation li {
    margin-bottom: 8px;
}

.full-explanation strong {
    color: #0056b3; /* הדגשת מונחים חשובים בכחול */
}


</style>

<button class="explanation-toggle-button">הצג/הסתר הסבר מפורט</button>

<div class="full-explanation hidden">
    <h2>פיצוח הקוד ההיברידי: איך זה עובד בפועל?</h2>
    <p>מערכת הנעה היברידית אינה סתם שילוב של שני מנועים, אלא תזמורת טכנולוגית מורכבת שבה כל כלי נגינה (רכיב) נכנס לפעולה בזמן הנכון ובמינון המדויק כדי ליצור הרמוניה של יעילות וביצועים. המטרה? לנצל את היתרונות של כל מקור כוח – המומנט המיידי של החשמל והכוח המתמשך של הבנזין – תוך מזעור החסרונות (בזבוז אנרגיה בעמידה, אי יעילות של מנוע בנזין בסל"ד נמוך, טווח מוגבל של חשמל).</p>

    <h3>השחקנים הראשיים במערכה ההיברידית:</h3>
    <p>הכירו את הרכיבים המרכזיים שהופכים את הקסם לאפשרי:</p>
    <ul>
        <li><strong>מנוע בנזין (או דיזל):</strong> הלב הפועם המסורתי. הוא חזק ויעיל במהירויות גבוהות, ומספק טווח נסיעה ארוך ללא צורך בטעינה תכופה. הוא יכול גם לשמש כגנרטור במידת הצורך.</li>
        <li><strong>סוללת מתח גבוה:</strong> בנק האנרגיה החשמלי. היא אוגרת את החשמל שמאפשר נסיעה חשמלית שקטה וחסכונית, ונטענת מחדש כמו קסם בזמן בלימה או ע"י המנוע.</li>
        <li><strong>מנוע חשמלי / גנרטור (MG1/MG2 במערכות מתקדמות):</strong> זהו הרכיב הרבגוני ביותר! הוא יכול להניע את הרכב בכוח חשמלי, לסייע למנוע הבנזין בעת האצה, וגם לפעול כגנרטור – לייצר חשמל מטעינה חיצונית (בפלאג-אין) או מאנרגיית תנועה (בבלימה רגנרטיבית) או אפילו ממנוע הבנזין עצמו! במערכות רבות יש שני מנועים כאלה עם תפקידים מעט שונים.</li>
        <li><strong>מערכת חלוקת כוח (Power Split Device / Planetary Gear):</strong> המוח המכני של המערכת! זהו מכלול גירים מתוחכם (לרוב גיר פלנטרי) שמחלק בצורה חכמה את הכוח המגיע ממנוע הבנזין לשני כיוונים בו זמנית – חלק לגלגלים וחלק להפעלת הגנרטור (מנוע חשמלי בתפקיד גנרטור). הוא גם מערבב את הכוח המגיע מהמנוע החשמלי עם זה של הבנזין לפני שהוא מגיע לגלגלים. זה מה שמאפשר למערכת לעבור בצורה חלקה בין מצבי פעולה שונים.</li>
        <li><strong>יחידת בקרת כוח (PCU):</strong> המנצח של התזמורת! זהו מחשב על שמקבל מידע אינסופי (מהירות, מיקום דוושת הגז, מצב סוללה, עומס על המנוע וכו') ומחליט בזמן אמת מי הרכיב שיעבוד, באיזו עוצמה ואיך האנרגיה תזרום. הוא גם אחראי על המרת מתח DC (סוללה) ל-AC (מנועים חשמליים) ולהיפך.</li>
        <li><strong>גלגלים:</strong> היעד הסופי של כל האנרגיה הזו – הם אלו שמזיזים את הרכב קדימה (או עוזרים לאסוף אנרגיה אחורה בזמן בלימה!).</li>
    </ul>

    <h3>מצבי פעולה – הסימולטור חושף את הסודות:</h3>
    <p>הרכב ההיברידי לא "בוחר" מצב פעולה, אלא מערכת הבקרה מנהלת את זרימת הכוח באלפיות שנייה. הסימולטור למעלה מציג הדמיה של תרחישים אופייניים כדי לפשט את ההבנה:</p>
    <ul>
        <li><strong>זינוק שקט (EV Mode):</strong> חווית חשמל טהור! לחיצה עדינה על דוושת הגז, נסיעה בפקק או תמרון איטי בחניון – הכל מתבצע בכוח חשמלי בלבד, שקט לחלוטין וללא פליטת מזהמים. הסוללה מזינה את המנוע החשמלי, והוא מסובב את הגלגלים. מנוע הבנזין רדום.</li>
        <li><strong>שחרור הכוח המלא (האצה):</strong> כשצריך כוח מיידי לעקיפה או עליה תלולה, המערכת משלבת כוחות! גם מנוע הבנזין נדלק וגם המנוע החשמלי מצטרף. מערכת חלוקת הכוח מערבבת את שניהם ביעילות מקסימלית כדי לספק את התאוצה המרבית אל הגלגלים.</li>
        <li><strong>שיוט חסכוני (כביש פתוח):</strong> במהירות קבועה בכביש מהיר, מנוע הבנזין הוא לרוב השחקן הראשי – הוא היעיל ביותר בעומס יציב. חלק מהכוח שלו הולך ישירות לגלגלים דרך מערכת חלוקת הכוח, וחלק קטן יותר עשוי לשמש להפעלת הגנרטור כדי לטעון את הסוללה "על הדרך" או כדי להזין את המנוע החשמלי שיסייע בקטנה אם יש דרישת כוח רגעית.</li>
        <li><strong>לכידת אנרגיה (האטה/בלימה):</strong> זהו קסם בפני עצמו! במקום לבזבז אנרגיה כחום על הבלמים, המנוע החשמלי הופך לגנרטור. הוא משתמש בתנועת הגלגלים כדי לייצר חשמל, ואוגר אותו בסוללה. זה לא רק חוסך אנרגיה אלא גם שומר על הבלמים המכאניים.</li>
        <li><strong>מנוחה שקטה (עמידה בפקק):</strong> הרכב עומד. מנוע הבנזין כבוי. כל המערכות החשמליות (מיזוג, רדיו) מקבלות כוח מהסוללה. הרכב מוכן לזנק שוב בכוח חשמלי ברגע שהפקק זז. רק אם הסוללה ריקה לחלוטין ונדרש כוח (למשל מיזוג חזק), מנוע הבנזין עשוי להידלק לרגע לטעון אותה.</li>
         <li><strong>אנרגיה למחר (טעינת סוללה ע"י מנוע):</strong> לפעמים, גם ללא דרישת כוח מיידית לגלגלים, המערכת תחליט שהסוללה זקוקה ל"דחיפה". במצב כזה, מנוע הבנזין נדלק ומפעיל את המנוע החשמלי בתפקיד גנרטור, שמטעין את הסוללה. זה קורה לרוב במהירויות נמוכות או בעמידה, ומאפשר לרכב לחזור במהירות למצב EV.</li>
    </ul>

    <h3>למה היברידי? היתרונות שמנצחים:</h3>
    <ul>
        <li><strong>חיסכון דרמטי בדלק:</strong> במיוחד בנהיגה עירונית עם הרבה עצירות והתחלות, ניצול המנוע החשמלי והבלימה הרגנרטיבית חוסך כמות אדירה של דלק.</li>
        <li><strong>ידידותי לסביבה:</strong> פליטות מזהמים נמוכות משמעותית, ובמצב EV אפס פליטות!</li>
        <li><strong>ביצועים משופרים:</strong> המומנט המיידי של המנוע החשמלי מספק "דחיפה" אדירה בהתחלה ובהאצות ביניים.</li>
        <li><strong>נסיעה חלקה ושקטה:</strong> המעברים בין המנועים כמעט בלתי מורגשים, והנסיעה במצב חשמלי שקטה להפליא.</li>
    </ul>

    <h3>מבט לעתיד: היברידיות ומעבר לחשמל מלא</h3>
    <p>מערכות היברידיות הן תחנת מעבר חיונית לעידן הרכב החשמלי. הן מאפשרות ליהנות מרוב היתרונות של הנעה חשמלית (חיסכון, פליטות נמוכות, ביצועים) מבלי לסבול מ"חרדת טווח" או תלות מוחלטת בתשתית טעינה שעדיין בהתהוות. כשהטכנולוגיה מתקדמת, אנו רואים יותר רכבי פלאג-אין היברידיים (PHEV) עם סוללות גדולות יותר וטווח חשמלי משמעותי, המקרבים אותנו יותר ויותר לעולם שבו מנוע הבעירה הפנימית יהפוך לנחלת העבר לטובת הנעה חשמלית מלאה (BEV).</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const simulatorContainer = document.querySelector('.hybrid-simulator-container');
    const scenarioButtons = simulatorContainer.querySelectorAll('.simulator-controls button');
    const flowArrows = simulatorContainer.querySelectorAll('.flow-arrow');
    const components = simulatorContainer.querySelectorAll('.component');
    const scenarioExplanation = simulatorContainer.querySelector('.scenario-explanation p');
    const explanationButton = document.querySelector('.explanation-toggle-button');
    const fullExplanation = document.querySelector('.full-explanation');

    // Define power flow paths and active components for each scenario
    const scenarios = {
        'start-slow': {
            explanation: '⚡ זינוק שקט (חשמל טהור): מונע ע"י המנוע החשמלי בלבד. מנוע הבנזין כבוי לחלוטין.',
            activePaths: ['battery-to-emg', 'emg-to-ps', 'ps-to-wheels'],
            activeComponents: ['battery', 'emg', 'power-split', 'wheels']
        },
        'acceleration': {
            explanation: '🚀 שחרור הכוח המלא (האצה): גם מנוע הבנזין וגם המנוע החשמלי פועלים במקביל כדי לספק את הכוח המרבי לגלגלים.',
            activePaths: ['engine-to-ps', 'battery-to-emg', 'emg-to-ps', 'ps-to-wheels'],
            activeComponents: ['engine', 'battery', 'emg', 'power-split', 'wheels']
        },
        'constant-speed': {
            explanation: '🛣️ שיוט חסכוני (כביש פתוח): מנוע הבנזין מספק את רוב הכוח לגלגלים, ולעיתים טוען את הסוללה על הדרך.',
            activePaths: ['engine-to-ps', 'ps-to-wheels', 'engine-to-emg'], // Engine to PS & Wheels, Engine to EMG (as Gen)
            activeComponents: ['engine', 'emg', 'power-split', 'wheels', 'battery'] // Battery gets charged
        },
        'deceleration': {
            explanation: '🔋 לכידת אנרגיה (האטה/בלימה): המנוע החשמלי הופך לגנרטור, ממיר את אנרגיית התנועה לחשמל ואוגר אותה בסוללה.',
            activePaths: ['wheels-to-emg', 'battery-to-emg'].reverse(), // Representing flow FROM wheels TO battery
            activeComponents: ['wheels', 'emg', 'battery']
        },
        'idle': {
             explanation: '☕ מנוחה שקטה (עמידה בפקק): מנוע הבנזין כבוי. הרכב מוכן לזנק שוב בכוח חשמלי.',
             activePaths: [], // No major power flow
             activeComponents: ['battery'] // Battery is active providing power for accessories
        },
         'charge': {
            explanation: '🔌 אנרגיה למחר (טעינת סוללה): מנוע הבנזין פועל כדי להפעיל את הגנרטור ולטעון את הסוללה.',
            activePaths: ['engine-to-emg', 'battery-to-emg'].reverse(), // Engine to EMG (as gen), charging Battery
            activeComponents: ['engine', 'emg', 'battery']
        }
    };

    function updateDiagram(scenario) {
        // Deactivate all arrows and components
        flowArrows.forEach(arrow => arrow.classList.remove('active'));
        components.forEach(component => component.classList.remove('active'));
        scenarioButtons.forEach(button => button.classList.remove('selected'));


        // Activate relevant elements for the scenario
        if (scenario && scenarios[scenario]) {
            // Activate arrows
            scenarios[scenario].activePaths.forEach(pathId => {
                const arrow = simulatorContainer.querySelector(`.flow-arrow[data-path="${pathId}"]`);
                if (arrow) {
                    arrow.classList.add('active');
                }
            });

            // Activate components
             scenarios[scenario].activeComponents.forEach(componentClass => {
                const component = simulatorContainer.querySelector(`.component.${componentClass}`);
                 if (component) {
                     component.classList.add('active');
                 }
             });

            // Update explanation text
            scenarioExplanation.innerHTML = scenarios[scenario].explanation;

            // Mark selected button
            const selectedButton = simulatorContainer.querySelector(`button[data-scenario="${scenario}"]`);
            if (selectedButton) {
                selectedButton.classList.add('selected');
            }

        } else {
             // Default state
             scenarioExplanation.innerHTML = 'בחרו תרחיש כדי לראות את זרימת הכוח הקסומה בפעולה!';
        }
    }

    // Add event listeners to buttons
    scenarioButtons.forEach(button => {
        button.addEventListener('click', () => {
            const scenario = button.dataset.scenario;
            updateDiagram(scenario);
        });
    });

    // Explanation toggle
    explanationButton.addEventListener('click', () => {
        fullExplanation.classList.toggle('hidden');
         // Optional: Change button text based on state
         explanationButton.textContent = fullExplanation.classList.contains('hidden') ? 'הצג הסבר מפורט' : 'הסתר הסבר מפורט';
    });

    // Set initial state (optional: could simulate 'idle' on load or clear state)
     updateDiagram(null); // Start with no scenario selected, clear all
});
</script>
---