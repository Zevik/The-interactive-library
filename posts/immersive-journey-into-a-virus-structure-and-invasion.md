---
title: "מסע סוחף אל תוך וירוס: מבנה סודי ותהליך פלישה מדהים"
english_slug: immersive-journey-into-a-virus-structure-and-invasion
category: "מדעי החיים / ביולוגיה"
tags: [וירוסים, בקטריופאג', מיקרוביולוגיה, מבנה תא, הדבקה ויראלית, ביולוגיה מולקולרית]
---
# מסע סוחף אל תוך וירוס: מבנה סודי ותהליך פלישה מדהים

הם קטנים יותר מחיידק, לא נחשבים ל'חיים' באופן מסורתי, אך חולשים על ממלכת התאים בכוח בלתי נתפס. איך יצור מינימליסטי כל כך מצליח לפרוץ את ההגנות החזקות ביותר, להשתלט על מפעל הייצור התאי ולהפוך אותו למפעל וירוסים פרטי? הצטרפו אלינו למסע ויזואלי מרתק אל לב מבנה הבקטריופאג' - הווירוס שמדביק חיידקים - וגלו את סודות מחזור ההדבקה הליטי המדהים.

<div class="interactive-app">
    <h2 class="app-title">צאו למסע חקר: גלו את מבנה הבקטריופאג'</h2>
    <div class="virus-model-container">
         <!-- Visual representation of a Bacteriophage -->
        <div id="virus-head" class="virus-part virus-head" data-name="ראש/קפסיד" data-description="מעטפת חלבונית חזקה ואלגנטית המגנה על המטען היקר ביותר של הוירוס: החומר הגנטי."></div>
        <div id="virus-genetic-material" class="virus-part virus-genetic-material" data-name="החומר הגנטי (DNA/RNA)" data-description="תוכנית הפעולה המלאה של הוירוס! מכיל את ההוראות הדרושות להשתלטות על התא המארח ולבניית צבא וירוסים חדש."></div>
        <div id="virus-collar" class="virus-part virus-collar" data-name="צווארון" data-description="נקודת מפגש קריטית: מחבר בין הראש עמוס המידע לכלי ההזרקה שמתחתיו."></div>
        <div id="virus-sheath" class="virus-part virus-sheath" data-name="נדן" data-description="מנגנון הזרקה ביולוגי עוצמתי! צינור חלבוני שמתכווץ בחוזקה כדי לדחוף את החומר הגנטי היישר לתוך התא המארח."></div>
        <div id="virus-baseplate" class="virus-part virus-baseplate" data-name="לוח בסיס" data-description="עוגן ונקודת פריצה: החלק התחתון של הנדן, ממנו יוצאים סיבי הזנב. מכיל אנזימים המסייעים בהיצמדות ופילוס דרך דופן התא."></div>
        <div id="virus-tail-fibers" class="virus-part virus-tail-fibers" data-name="סיבי זנב" data-description="זרועות החישה והעגינה של הוירוס! מזהים ספציפית ונקשרים לרצפטורים (דלתות כניסה) על פני השטח של התא המארח."></div>

        <div id="tooltip" class="tooltip">
            <div class="tooltip-name"></div>
            <div class="tooltip-description"></div>
             <div class="tooltip-arrow"></div>
        </div>
    </div>

    <div class="exploration-instructions">
        <i class="fas fa-mouse-pointer"></i> לחצו על כל חלק של הוירוס כדי לחשוף את שמו ותפקידו הסודי!
    </div>

    <h2 class="app-title">צפו בפלישה: מחזור ההדבקה הליטי בפעולה</h2>
    <div class="animation-container">
        <div id="stage-0" class="animation-stage active">
            <p><strong>שלב 0: האיום מתקרב. </strong> וירוס (בקטריופאג') מוכן לתקוף. הוא מרחף בסביבה ומחפש את תא המטרה (חיידק).</p>
            <div class="scene">
                <div class="bacterium"><i class="fas fa-bacteria"></i> חיידק</div>
                <div class="phage approaching"><i class="fas fa-virus"></i> וירוס</div>
            </div>
        </div>
        <div id="stage-1" class="animation-stage">
            <p><strong>שלב 1: עגינה והיקשרות (Attachment). </strong>רגע האמת! סיבי הזנב של הוירוס מזהים במדויק את "דלתות הכניסה" (רצפטורים) על פני החיידק ונקשרים אליהן בחוזקה.</p>
             <div class="scene">
                <div class="bacterium attached"><i class="fas fa-bacteria"></i> חיידק - עוגן!</div>
                <div class="phage attached"><i class="fas fa-virus"></i> וירוס - נצמד!</div>
            </div>
        </div>
        <div id="stage-2" class="animation-stage">
            <p><strong>שלב 2: פלישה והזרקה (Penetration). </strong> הפאג' מפעיל את מנגנון ההזרקה שלו! הנדן מתכווץ בפתאומיות, וכל המטען הגנטי (ה-DNA) מוזרק בכוח אל תוך החיידק. המעטפת הריקה נשארת בחוץ.</p>
             <div class="scene">
                <div class="bacterium penetrated"><i class="fas fa-bacteria"></i> חיידק - נחדר!</div>
                <div class="phage injected"><i class="fas fa-virus-slash"></i> מעטפת ריקה בחוץ</div>
                <div class="genetic-material inside"><i class="fas fa-dna"></i> DNA ויראלי בפנים!</div>
            </div>
        </div>
         <div id="stage-3" class="animation-stage">
            <p><strong>שלב 3: השתלטות ושכפול (Replication). </strong>ה-DNA הוויראלי לוקח פיקוד! הוא משתלט על המנגנונים של החיידק והופך אותו למפעל ענק לייצור חלבונים ויראליים (למעטפות, סיבים וכו') ולשכפול מהיר של עוד ועוד עותקי DNA ויראלי.</p>
             <div class="scene">
                <div class="bacterium replicating"><i class="fas fa-dna"></i> חיידק - תחת שליטה!</div>
                 <div class="viral-components"><i class="fas fa-cogs"></i> ייצור ויראלי מואץ!</div>
            </div>
        </div>
        <div id="stage-4" class="animation-stage">
            <p><strong>שלב 4: בנייה והרכבה (Assembly). </strong> עכשיו מרכיבים את הצבא! החלקים הוויראליים שיוצרו (מעטפות, DNA, סיבים) מתחברים זה לזה במהירות ויוצרים וירוסים שלמים ותקינים - דור חדש של פולשים.</p>
            <div class="scene">
                <div class="bacterium assembling"><i class="fas fa-tools"></i> חיידק - קו הרכבה פעיל!</div>
                <div class="new-phages-forming"><i class="fas fa-viruses"></i> צבא וירוסים חדש נבנה!</div>
            </div>
        </div>
        <div id="stage-5" class="animation-stage">
            <p><strong>שלב 5: פיצוץ ושחרור (Release). </strong>החיידק כבר לא יכול להכיל את כמות הוירוסים! הוא מתפוצץ (עובר ליזיס), וצבא הוירוסים החדש משתחרר לחופשי, מוכן להדביק תאים נוספים ולהמשיך את שרשרת הפלישה.</p>
             <div class="scene">
                <div class="bacterium lysed"><i class="fas fa-burst"></i> חיידק - התפוצץ!</div>
                <div class="new-phages released"><i class="fas fa-viruses"></i> דור חדש של וירוסים משתחרר!</div>
            </div>
        </div>
        <!-- Add more stages as needed -->
    </div>

    <div class="animation-controls">
        <button id="prev-stage" class="control-button"><i class="fas fa-step-backward"></i> שלב קודם</button>
        <button id="next-stage" class="control-button">שלב הבא <i class="fas fa-step-forward"></i></button>
        <button id="play-animation" class="control-button primary-button"><i class="fas fa-play"></i> הפעל אנימציה</button>
        <button id="pause-animation" class="control-button" style="display: none;"><i class="fas fa-pause"></i> השהה</button>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button"><i class="fas fa-info-circle"></i> הצג / הסתר הסבר מעמיק</button>

<div id="explanation" style="display: none;" class="detailed-explanation">
    <h2>הסבר מעמיק על וירוסים: המבנה, הפלישה והאסטרטגיות המדהימות שלהם</h2>

    <h3>וירוסים: לא בדיוק חיים, אבל קטלניים ביותר</h3>
    וירוס הוא חלקיק זיהומי מיקרוסקופי שאינו בעל מבנה תאי ואינו יכול לקיים תהליכים מטבוליים עצמאיים. כדי לשרוד ולהתרבות, וירוסים חייבים לפלוש לתא חי (תא מארח) ולהשתמש במנגנוניו. תכונה זו, המחייבת תלות מוחלטת בתא מארח, גורמת לכך שוירוסים אינם מסווגים בדרך כלל כיצורים חיים, למרות שהם מכילים חומר גנטי ויכולים להתפתח באבולוציה. הם טפילים מוחלטים, הקיימים כמעט בכל מערכת אקולוגית על פני כדור הארץ ומדביקים את כל סוגי האורגניזמים - מחיידקים וארכיאות ועד צמחים, פטריות ובעלי חיים.

    <h3>הארכיטקטורה המינימליסטית של וירוס</h3>
    למרות הגודל הזעיר והפשטות היחסית שלהם, לוירוסים מבנה מוגדר היטב, המותאם למשימתם: פלישה ושכפול. המרכיבים העיקריים הם:
    <ul>
        <li><strong>החומר הגנטי (Genome):</strong> ליבת הוירוס. יכול להיות DNA (חד-גדילי או דו-גדילי) או RNA (חד-גדילי או דו-גדילי). גודל הגנום הוויראלי קטן בהרבה מגנום תאי ומכיל את הגנים החיוניים בלבד - לרוב כאלה המקודדים לחלבונים מבניים של הוירוס ולאנזימים הדרושים להשתלטות ושכפול בתוך התא המארח.</li>
        <li><strong>הקפסיד (Capsid):</strong> מעטפת חלבונית חזקה ואלגנטית המקיפה ומגנה על החומר הגנטי. הקפסיד בנוי מיחידות חלבון זהות או דומות הנקראות קפסומרים, הנארזות בצורה גאומטרית סימטרית (לרוב איקוסהדרלית או הליקלית). הקפסיד חיוני להגנה על הגנום מפירוק ולהובלתו אל התא המארח.</li>
    </ul>
    <h3>שדרוגים אופציונליים: רכיבים נוספים</h3>
    <ul>
        <li><strong>מעטפת ויראלית (Envelope):</strong> וירוסים רבים, במיוחד אלה המדביקים תאי בעלי חיים (כמו וירוס השפעת, HIV, קורונה), עטופים במעטפת חיצונית נוספת. מעטפת זו היא למעשה פיסה של קרום התא המארח (ממברנה ליפידית) שהוירוס "גונב" ביציאתו, ומשובצים בה חלבונים ויראליים ייחודיים (Glycoproteins), המכונים לעתים "ספייקים". מעטפת זו מסייעת לוירוס להתמזג עם קרום התא המארח ולחדור פנימה. בקטריופאג'ים, התוקפים חיידקים בעלי דופן תא קשיחה, לרוב אינם בעלי מעטפת.</li>
        <li><strong>אנזימים:</strong> וירוסים מסוימים נושאים איתם בתוך הויריון (חלקיק הוירוס השלם) אנזימים חיוניים שאינם קיימים בתא המארח או שרמתם אינה מספקת. דוגמאות כוללות רוורס טרנסקריפטאז (ב-HIV) או RNA פולימראז תלוי RNA (בוירוסי RNA מסוימים).</li>
    </ul>

    <h3>בקטריופאג'ים: המומחים בפלישה לחיידקים</h3>
    הבקטריופאג'ים, או פאג'ים, הם קבוצה מרתקת של וירוסים המתמחים בהדבקת חיידקים. לבקטריופאג'ים מורכבים, כמו פאג' T4 (המודל שהצגנו באנימציה), יש מבנה דמוי "נחתת ירח" מתוחכם במיוחד, הכולל:
    <ul>
        <li><strong>ראש איקוסהדרלי:</strong> הקפסיד המכיל את ה-DNA הדו-גדילי.</li>
        <li><strong>צווארון:</strong> מבנה קצר מתחת לראש.</li>
        <li><strong>נדן מתכווץ:</strong> צינור חלבוני ארוך מתחת לצווארון, הפועל כמו מזרק ביולוגי.</li>
        <li><strong>לוח בסיס:</strong> מבנה מורכב בתחתית הנדן, המשמש נקודת עגינה ומכיל "פינים" קצרים ואנזימים (ליזוזים) המסייעים בריכוך או פריצת דופן התא החיידקי.</li>
        <li><strong>סיבי זנב ארוכים:</strong> שישה סיבים חלבונים היוצאים מלוח הבסיס, האחראים לזיהוי הרצפטורים הספציפיים על החיידק וליקשרות הראשונית.</li>
    </ul>
    מבנה ייחודי זה מאפשר לפאג'ים להתגבר על מחסום דופן התא החיידקי ולהזריק את הגנום שלהם פנימה בצורה יעילה ביותר.

    <h3>מחזור החיים הוויראלי: אסטרטגיית ההתרבות הליטית</h3>
    המחזור הליטי הוא אחד משני מסלולי ההדבקה העיקריים של וירוסים (השני הוא המחזור הליזוגני, שבו הוירוס משתלב בגנום המארח). במחזור הליטי, מטרת הוירוס היא להשתלט, לשכפל את עצמו במהירות, ולהרוס את התא המארח כדי לשחרר את הוירוסים החדשים. השלבים במחזור הליטי של בקטריופאג'ים (הדומים עקרונית למחזור הליטי של וירוסים אחרים) הם:
    <ol>
        <li><strong>התקשרות (Attachment / Adsorption):</strong> הוירוס מזהה ונקשר באופן ספציפי לרצפטורים (מולקולות חלבון או סוכר) על פני השטח של התא המארח. ספציפיות זו קובעת אילו תאים הוירוס יכול להדביק. בפאג'ים, סיבי הזנב הם המזהים והנקשרים.</li>
        <li><strong>חדירה (Penetration / Entry):</strong> החומר הגנטי הוויראלי חודר לתוך הציטופלזמה של התא המארח. בפאג'ים מורכבים, הנדן מתכווץ וה-DNA מוזרק דרך דופן התא והממברנה. וירוסים אחרים עשויים להיכנס לתא כולו (למשל, באמצעות אנדוציטוזה) ולאחר מכן לשחרר את הגנום שלהם בתוך התא.</li>
        <li><strong>שכפול (Replication / Biosynthesis):</strong> הגנום הוויראלי משתלט על "מפעל הייצור" של התא המארח. גנים ויראליים מקודדים לחלבונים מוקדמים המנטרלים את הגנות התא ומשנים את פעילותו לטובת הוירוס. לאחר מכן, הגנום הוויראלי משוכפל שוב ושוב תוך שימוש באנזימי התא ובנוקלאוטידים הקיימים בו. במקביל, מיוצרים חלבונים ויראליים מבניים בכמויות גדולות (החלבונים שמרכיבים את הקפסיד, סיבי הזנב וכו').</li>
        <li><strong>הרכבה (Assembly / Maturation):</strong> כמויות גדולות של החומר הגנטי הוויראלי ושל החלבונים הוויראליים מתחברות בתוך התא המארח ליצירת וירוסים שלמים חדשים (ויריונים). תהליך ההרכבה הוא לרוב ספונטני למחצה אך מזורז על ידי חלבונים ויראליים ייעודיים.</li>
        <li><strong>שחרור (Release):</strong> הוירוסים החדשים משתחררים מהתא המארח כדי להדביק תאים נוספים. במחזור הליטי, שלב זה מערב לרוב את הרס (ליזיס) של התא המארח. פאג'ים, למשל, מייצרים אנזימים (כמו ליזין) המפרקים את דופן התא החיידקי, מה שגורם לתא להתפוצץ ולשחרר מאות ואלפי וירוסים חדשים לסביבה.</li>
    </ol>
    מחזור זה, המושלם לעיתים תוך דקות ספורות (בפאג'ים), מדגים את היעילות המדהימה של וירוסים בהתרבות על חשבון התא המארח.

    <p style="font-size: 0.9em; color: #777;">אפליקציה אינטראקטיבית זו נוצרה למטרות לימודיות והיא פישוט של תהליכים ביולוגיים מורכבים. מבנה הוירוסים ותהליכי ההדבקה יכולים להשתנות בין סוגי וירוסים שונים.</p>
</div>

<style>
    /* בסיס לעיצוב - גופנים, צבעים כלליים */
    body {
        direction: rtl;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6; /* רקע עדין */
    }

    h1, h2, h3 {
        color: #2c3e50; /* כחול כהה יותר לכותרות */
        text-align: center;
    }

    h1 {
        margin-top: 30px;
        margin-bottom: 20px;
        font-size: 2em;
    }

    h2.app-title {
        color: #16a085; /* ירוק טורקיז */
        margin-top: 25px;
        margin-bottom: 20px;
        font-size: 1.6em;
    }

    p {
        margin-bottom: 15px;
    }

    /* עיצוב האפליקציה האינטראקטיבית */
    .interactive-app {
        max-width: 850px; /* רוחב מעט גדול יותר */
        margin: 20px auto;
        padding: 30px; /* ריפוד מוגדל */
        border: none; /* ללא גבול סולידי */
        border-radius: 12px; /* פינות עגולות יותר */
        background-color: #ffffff; /* רקע לבן נקי */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* צל עדין */
        text-align: center;
    }

    .virus-model-container {
        position: relative;
        width: 350px; /* מעט גדול יותר */
        height: 450px; /* מעט גדול יותר */
        margin: 30px auto;
        border: 2px dashed #bdc3c7; /* גבול מקווקו עדין */
        border-radius: 15px;
        background: linear-gradient(to bottom, #ecf0f1, #ffffff); /* גרדיאנט עדין */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding-top: 60px; /* התאמה לריכוז */
        box-shadow: inset 0 0 10px rgba(0,0,0,0.05);
    }

    /* עיצוב חלקי הוירוס - שיפור צורות וצבעים */
    .virus-part {
        position: absolute;
        cursor: pointer;
        box-sizing: border-box;
        transition: all 0.3s ease-in-out; /* אנימציה חלקה יותר */
        border: 2px solid transparent; /* גבול בלתי נראה כברירת מחדל */
    }

    .virus-part:hover {
         border-color: #3498db; /* גבול כחול בהובר */
         transform: scale(1.05); /* גדילה קלה */
         box-shadow: 0 0 8px rgba(52, 152, 219, 0.6); /* צל כחול */
    }

    .virus-part.active { /* קלאס לאקטיב אם נרצה להוסיף בעתיד */
        border-color: #e74c3c; /* גבול אדום */
         box-shadow: 0 0 10px rgba(231, 76, 60, 0.8);
    }

    /* צורות ומיקומים משופרים לבקטריופאג' */
    .virus-head {
        width: 90px;
        height: 80px; /* צורה אליפטית קלה */
        background-color: #e74c3c; /* אדום בוהק */
        border-radius: 50%;
        top: 60px;
        left: 50%;
        transform: translateX(-50%);
        box-shadow: 0 3px 8px rgba(0,0,0,0.2);
    }
    .virus-genetic-material {
        width: 50px;
        height: 50px;
        background-color: #9b59b6; /* סגול עמוק */
        border-radius: 50%; /* Representation inside head */
        top: 75px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 1;
        box-shadow: inset 0 0 5px rgba(0,0,0,0.3);
    }
    .virus-collar {
        width: 25px;
        height: 18px;
        background-color: #7f8c8d; /* אפור עדין */
        top: 138px;
        left: 50%;
        transform: translateX(-50%);
         border-radius: 3px;
    }
    .virus-sheath {
        width: 35px;
        height: 90px; /* ארוך יותר */
        background-color: #3498db; /* כחול בהיר */
        top: 156px;
        left: 50%;
        transform: translateX(-50%);
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .virus-baseplate {
        width: 60px; /* רחב יותר */
        height: 25px; /* גבוה יותר */
        background-color: #f39c12; /* כתום עשיר */
        top: 246px;
        left: 50%;
        transform: translateX(-50%);
        border-radius: 8px 8px 20px 20px; /* צורה ברורה יותר */
        box-shadow: 0 3px 8px rgba(0,0,0,0.2);
    }
     .virus-tail-fibers {
        width: 100px; /* רחב יותר */
        height: 60px; /* גבוה יותר */
        background-color: #2ecc71; /* ירוק עז */
        top: 268px; /* מיקום בהתאם לבסיס */
        left: 50%;
        transform: translateX(-50%);
        clip-path: polygon(5% 0%, 95% 0%, 70% 100%, 30% 100%); /* צורת מניפה */
        box-shadow: 0 3px 8px rgba(0,0,0,0.2);
    }


    /* עיצוב Tooltip משופר */
    .tooltip {
        position: absolute;
        bottom: 10px; /* מיקום קבוע בתחתית הקונטיינר */
        left: 50%;
        transform: translateX(-50%);
        background-color: #2c3e50; /* רקע כהה */
        color: #ecf0f1; /* טקסט בהיר */
        padding: 12px 15px;
        border-radius: 8px;
        pointer-events: none;
        opacity: 0;
        transition: opacity 0.4s ease-in-out, transform 0.4s ease-in-out; /* אנימציה עדינה */
        z-index: 10;
        min-width: 200px;
        max-width: 300px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        border: 1px solid #34495e; /* גבול עדין */
    }

     .tooltip.visible {
        opacity: 1;
         transform: translate(-50%, -10px); /* עולה מעט כשמופיע */
    }

    .tooltip-name {
        font-weight: bold;
        font-size: 1.1em;
        margin-bottom: 5px;
        color: #1abc9c; /* ירוק ים */
    }

     .tooltip-description {
         font-size: 0.9em;
         line-height: 1.5;
     }

     .tooltip-arrow { /* חץ קטן בתחתית ה tooltip */
         content: '';
         position: absolute;
         bottom: -10px;
         left: 50%;
         transform: translateX(-50%);
         width: 0;
         height: 0;
         border-left: 10px solid transparent;
         border-right: 10px solid transparent;
         border-top: 10px solid #2c3e50; /* צבע הרקע של ה tooltip */
     }


    .exploration-instructions {
        font-size: 1em;
        color: #555;
        margin-top: 10px;
        margin-bottom: 25px;
        font-style: italic;
    }
    .exploration-instructions i {
        color: #3498db;
        margin-left: 5px;
    }


    /* עיצוב קונטיינר האנימציה */
    .animation-container {
        margin-top: 40px;
        border: none;
        padding: 20px;
        border-radius: 12px;
        background-color: #ecf0f1; /* רקע בהיר יותר לאנימציה */
        min-height: 220px; /* לוודא מקום */
        position: relative;
        overflow: hidden;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.08);
    }

    .animation-stage {
        display: none;
        text-align: center;
        animation: fadeInScale 0.6s ease-in-out; /* אנימציה משופרת */
        min-height: 180px; /* לוודא גובה קבוע לשלב */
        padding-bottom: 20px; /* ריפוד למניעת כיסוי ע"י כפתורים */
    }

    .animation-stage.active {
        display: block;
    }

     @keyframes fadeInScale {
        from { opacity: 0; transform: scale(0.98); }
        to { opacity: 1; transform: scale(1); }
    }

    .animation-stage p {
        font-size: 1.1em;
        color: #333;
        margin-bottom: 15px;
    }

    .animation-stage strong {
        color: #c0392b; /* אדום כהה לשלבים */
        font-size: 1.2em;
    }

    /* עיצוב סצנת האנימציה - ייצוג ויזואלי */
    .scene {
        margin-top: 20px;
        position: relative;
        width: 100%;
        height: 120px; /* גובה גדול יותר לסצנה */
        display: flex;
        align-items: center;
        justify-content: center; /* מרכוז אופקי */
        gap: 30px; /* רווח גדול יותר בין אלמנטים */
         overflow: hidden; /* למקרה של תנועה מחוץ לגבולות */
    }

    .bacterium, .phage, .genetic-material, .viral-components, .new-phages-forming, .new-phages {
        padding: 12px 18px; /* ריפוד גדול יותר */
        border-radius: 25px; /* פינות עגולות מאוד */
        font-size: 0.9em;
        white-space: nowrap;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        transition: all 0.6s ease-in-out; /* אנימציה של תנועה וצבע */
        display: flex;
        align-items: center;
        justify-content: center;
    }
     .bacterium i, .phage i { /* אייקונים */
         margin-left: 8px;
         font-size: 1.2em;
     }


    .bacterium {
        border: 3px solid #27ae60; /* ירוק חזק */
        background-color: #e8f8f5; /* ירוק בהיר מאוד */
         color: #27ae60;
         position: absolute; /* מיקום מדויק יותר לפי שלב */
         left: 15%;
         top: 50%;
         transform: translateY(-50%);
         min-width: 100px; /* גודל מינימלי */
    }

    .phage {
       background-color: #f1c40f; /* צהוב עז */
       border: 3px solid #f39c12; /* כתום חזק */
        color: #f39c12;
         position: absolute; /* מיקום מדויק יותר לפי שלב */
         right: 15%;
         top: 50%;
         transform: translateY(-50%);
          min-width: 120px;
    }

     /* מיקומים ואנימציות ספציפיים לשלבים */
    #stage-0 .phage.approaching {
         right: 5%; /* מתחיל מחוץ לפריים */
         opacity: 0; /* מתחיל שקוף */
         animation: slideInLeft 0.8s ease-out forwards; /* נכנס מימין */
     }
     @keyframes slideInLeft {
         to { right: 15%; opacity: 1; }
     }


    #stage-1 .phage.attached {
        left: calc(15% + 100px); /* נצמד לחיידק */
        border-color: #c0392b; /* צבע הדבקה */
        background-color: #f9e7eb;
        color: #c0392b;
        animation: attachPulse 0.8s infinite alternate; /* פעימה עדינה */
    }
     #stage-1 .bacterium.attached {
        border-color: #c0392b;
        background-color: #f9e7eb;
        color: #c0392b;
         animation: attachPulse 0.8s infinite alternate;
    }
    @keyframes attachPulse {
        to { transform: translateY(-50%) scale(1.02); opacity: 0.9; }
    }


     #stage-2 .phage.injected {
         left: calc(15% + 100px); /* עדיין מחובר */
         background-color: #bdc3c7; /* צבע אפור - מעטפת ריקה */
          border-color: #95a5a6;
         color: #95a5a6;
          min-width: 120px;
     }
     #stage-2 .bacterium.penetrated {
         border-color: #3498db; /* צבע כחול - נחדר */
          background-color: #ebf5fb;
          color: #3498db;
     }
      #stage-2 .genetic-material.inside {
         position: absolute;
         left: 25%; /* בתוך החיידק */
         top: 50%;
         transform: translate(-50%, -50%) scale(0.8); /* קטן יותר בפנים */
         background-color: #9b59b6; /* סגול */
         color: white;
         padding: 8px 12px;
         border-radius: 15px;
         font-size: 0.8em;
          box-shadow: 0 0 8px rgba(155, 89, 182, 0.6);
          animation: dnaPulse 1s infinite alternate;
     }
     @keyframes dnaPulse {
         to { transform: translate(-50%, -50%) scale(0.85); opacity: 0.9; }
     }


     #stage-3 .bacterium.replicating {
          border-color: #8e44ad; /* סגול כהה */
         background-color: #f4ecf7;
         color: #8e44ad;
          animation: replicateAnimation 1s infinite alternate ease-in-out;
     }
     @keyframes replicateAnimation {
         to { box-shadow: 0 0 15px rgba(142, 68, 173, 0.8); }
     }

     #stage-3 .viral-components {
         position: absolute;
         left: 50%;
         top: 50%;
         transform: translate(-50%, -50%);
         background-color: #fdedec; /* אדום בהיר מאוד */
         color: #c0392b;
         padding: 15px 20px;
         border-radius: 18px;
         font-size: 0.9em;
         border: 2px dashed #e74c3c;
         animation: componentsFloat 1.5s infinite ease-in-out alternate;
     }
     @keyframes componentsFloat {
         0% { transform: translate(-50%, -50%) translateY(0); }
         100% { transform: translate(-50%, -50%) translateY(-5px); }
     }


     #stage-4 .bacterium.assembling {
          border-color: #d35400; /* כתום עמוק */
         background-color: #fef5e7;
         color: #d35400;
          animation: assembleAnimation 1s infinite ease-in-out;
     }
      @keyframes assembleAnimation {
         0% { transform: translateY(-50%) rotate(0deg); }
         100% { transform: translateY(-50%) rotate(2deg); }
     }

     #stage-4 .new-phages-forming {
         position: absolute;
         left: 50%;
         top: 50%;
         transform: translate(-50%, -50%);
         background-color: #e8f8f5; /* ירוק בהיר */
         color: #1abc9c;
         padding: 15px 20px;
         border-radius: 18px;
         font-size: 0.9em;
         border: 2px dashed #16a085;
          animation: formingPulse 1.2s infinite alternate;
     }
     @keyframes formingPulse {
         to { background-color: #d4edea; box-shadow: 0 0 10px rgba(26, 188, 156, 0.7); }
     }


     #stage-5 .bacterium.lysed {
          border: 3px dashed #e74c3c; /* אדום מקווקו */
          color: #e74c3c;
          background-color: #fdedec;
          animation: pulseRed 0.5s infinite alternate;
     }
     @keyframes pulseRed {
         to { border-color: #c0392b; color: #c0392b; box-shadow: 0 0 15px rgba(192, 57, 43, 0.8); }
     }

     #stage-5 .new-phages.released {
         position: absolute;
         left: 50%;
         top: 50%;
         transform: translate(-50%, -50%);
         background-color: #d4edda; /* ירוק שחרור */
         color: #155724;
         padding: 15px 20px;
         border-radius: 18px;
         font-size: 0.9em;
         border: 2px dashed #28a745;
         animation: releaseSpread 1s ease-out forwards; /* מתפזר החוצה */
         opacity: 0;
     }
      @keyframes releaseSpread {
         0% { transform: translate(-50%, -50%) scale(0.8); opacity: 0.5; }
         100% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
     }


    /* עיצוב כפתורי שליטה */
    .animation-controls {
        margin-top: 25px;
         display: flex; /* סידור הכפתורים בשורה */
         justify-content: center; /* מרכוז */
         flex-wrap: wrap; /* גלישה לשורה הבאה אם אין מקום */
         gap: 10px; /* רווח בין כפתורים */
    }

    .control-button,
    .toggle-button {
        padding: 12px 20px; /* ריפוד גדול יותר */
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #3498db; /* כחול סטנדרטי */
        color: white;
        transition: background-color 0.3s ease, opacity 0.3s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .control-button:hover,
    .toggle-button:hover {
        background-color: #2980b9; /* כחול כהה יותר בהובר */
    }
     .control-button:disabled {
         opacity: 0.6;
         cursor: not-allowed;
     }
     .control-button:disabled:hover {
         background-color: #3498db; /* מונע שינוי צבע בהובר כשהכפתור לא פעיל */
     }

     .primary-button {
         background-color: #2ecc71; /* ירוק לכפתור הראשי (הפעל) */
     }
     .primary-button:hover {
         background-color: #27ae60; /* ירוק כהה יותר בהובר */
     }

    .toggle-button {
         display: block; /* כפתור בפני עצמו */
         margin: 25px auto;
         background-color: #9b59b6; /* סגול */
    }
     .toggle-button:hover {
         background-color: #8e44ad; /* סגול כהה */
     }
     .toggle-button i {
         margin-left: 8px;
     }


    /* עיצוב הסבר מפורט */
    .detailed-explanation {
        direction: rtl;
        margin-top: 25px;
        padding: 25px;
        border: none;
        border-radius: 12px;
        background-color: #ecf0f1; /* רקע בהיר */
        text-align: right;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
    }

    .detailed-explanation h3 {
        color: #555;
        margin-top: 20px;
        margin-bottom: 12px;
        border-bottom: 1px solid #bdc3c7; /* קו עדין יותר */
        padding-bottom: 6px;
        font-size: 1.3em;
        text-align: right;
    }

    .detailed-explanation ul,
    .detailed-explanation ol {
        margin-bottom: 20px;
        padding-right: 25px;
         list-style-position: inside; /* סידור רשימה טוב יותר RTL */
    }

    .detailed-explanation li {
        margin-bottom: 10px;
        line-height: 1.7;
        padding-right: 5px;
    }

     .detailed-explanation li strong {
         color: #34495e; /* כחול כהה */
     }

    /* אייקונים - דורש Font Awesome חיצוני או שילוב SVG/CSS */
    /* For this example, assuming Font Awesome is included in the environment */
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // Add Font Awesome kit script dynamically if needed and not already present
        // This is a common practice but might depend on the execution environment.
        // For strict adherence, assuming the environment provides FA or removing icons.
        // Keeping icons for visual intent, but be aware they need external resource.
        /*
        if (!document.querySelector('script[src*="font-awesome"]')) {
             const faScript = document.createElement('script');
             faScript.src = 'https://kit.fontawesome.com/YOUR_KIT_CODE.js'; // Replace YOUR_KIT_CODE
             faScript.crossOrigin = 'anonymous';
             document.head.appendChild(faScript);
        }
        */


        // --- Virus Model Interaction ---
        const virusParts = document.querySelectorAll('.virus-part');
        const tooltip = document.getElementById('tooltip');
        const tooltipName = tooltip.querySelector('.tooltip-name');
        const tooltipDescription = tooltip.querySelector('.tooltip-description');
        const virusModelContainer = document.querySelector('.virus-model-container');

        virusParts.forEach(part => {
            // Add click event for tooltip
            part.addEventListener('click', () => {
                // Hide previous tooltip if visible
                tooltip.classList.remove('visible');

                // Get data
                const name = part.getAttribute('data-name');
                const description = part.getAttribute('data-description');

                // Update tooltip content
                tooltipName.textContent = name;
                tooltipDescription.textContent = description;

                // Show the tooltip
                tooltip.classList.add('visible');

                // Optional: Add a temporary visual highlight to the clicked part
                part.classList.add('active');
                setTimeout(() => {
                    part.classList.remove('active');
                }, 800); // Highlight for 0.8 seconds
            });

             // Add hover effects for more dynamic feel
            part.addEventListener('mouseover', () => {
                 part.style.borderColor = '#3498db'; // Highlight on hover
                 part.style.transform = part.style.transform + ' scale(1.05)';
            });
             part.addEventListener('mouseout', () => {
                 if (!part.classList.contains('active')) { // Don't remove border if active
                     part.style.borderColor = 'transparent';
                     part.style.transform = part.style.transform.replace(' scale(1.05)', '');
                 }
             });
        });

        // Hide tooltip when clicking anywhere inside the model container, but not on a part
        virusModelContainer.addEventListener('click', (event) => {
            if (!event.target.closest('.virus-part')) { // Use closest to check if the click was inside any virus part
                tooltip.classList.remove('visible');
            }
        });


        // --- Animation Control ---
        const animationStages = document.querySelectorAll('.animation-stage');
        const prevButton = document.getElementById('prev-stage');
        const nextButton = document.getElementById('next-stage');
        const playButton = document.getElementById('play-animation');
        const pauseButton = document.getElementById('pause-animation');
        let currentStageIndex = 0;
        let animationInterval = null;
        const animationSpeed = 3500; // Milliseconds per stage (slightly slower for visual stages)

        function updateAnimationStage(index) {
            // Ensure index is within bounds
            if (index < 0 || index >= animationStages.length) {
                return;
            }

            // Hide current active stage with transition/animation class
            const activeStage = document.querySelector('.animation-stage.active');
             if (activeStage) {
                 activeStage.classList.remove('active');
                 // Optional: Add exit animation class here if needed
             }


            // Show the new active stage
            const nextActiveStage = animationStages[index];
            nextActiveStage.classList.add('active');
            // The CSS @keyframes fadeInScale handles the entry animation

            currentStageIndex = index;
            updateAnimationControls();
        }

        function updateAnimationControls() {
            prevButton.disabled = currentStageIndex === 0;
            nextButton.disabled = currentStageIndex === animationStages.length - 1;

            if (animationInterval) { // Playing
                playButton.style.display = 'none';
                pauseButton.style.display = 'inline-block';
                 prevButton.disabled = true; // Disable manual step during auto play
                 nextButton.disabled = true;
            } else { // Paused or Stopped
                 playButton.style.display = 'inline-block';
                 pauseButton.style.display = 'none';
                 prevButton.disabled = currentStageIndex === 0;
                 nextButton.disabled = currentStageIndex === animationStages.length - 1;
            }
        }

        function playAnimation() {
             if (animationInterval) return; // Already playing

             // If at the end, restart from the beginning smoothly
             if (currentStageIndex === animationStages.length - 1) {
                 updateAnimationStage(0); // Go to stage 0 immediately
                 // The interval will pick up from stage 0 after the first delay
             }

            animationInterval = setInterval(() => {
                if (currentStageIndex < animationStages.length - 1) {
                    updateAnimationStage(currentStageIndex + 1);
                } else {
                    pauseAnimation(); // Stop when animation finishes
                }
            }, animationSpeed);
             updateAnimationControls(); // Update button states immediately
        }

        function pauseAnimation() {
            clearInterval(animationInterval);
            animationInterval = null;
             updateAnimationControls(); // Update button states
        }

        prevButton.addEventListener('click', () => {
            pauseAnimation(); // Pause if playing
            updateAnimationStage(currentStageIndex - 1);
        });

        nextButton.addEventListener('click', () => {
             pauseAnimation(); // Pause if playing
            updateAnimationStage(currentStageIndex + 1);
        });

        playButton.addEventListener('click', playAnimation);
        pauseButton.addEventListener('click', pauseAnimation);


        // Initialize animation view
        updateAnimationStage(0);


        // --- Explanation Toggle ---
        const toggleButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        toggleButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';

            if (isHidden) {
                 explanationDiv.style.display = 'block';
                 explanationDiv.style.maxHeight = '0'; // Start collapsed
                 explanationDiv.style.overflow = 'hidden';
                 explanationDiv.style.transition = 'max-height 0.5s ease-in-out, opacity 0.5s ease-in-out';
                 explanationDiv.style.opacity = '0';

                 // Force reflow to make transition work
                 explanationDiv.offsetHeight;

                 // Expand
                 explanationDiv.style.maxHeight = explanationDiv.scrollHeight + 30 + 'px'; // Set to scrollHeight + padding
                 explanationDiv.style.opacity = '1';

                 // Optional: Add a class after transition ends to allow height: auto;
                 // explanationDiv.addEventListener('transitionend', function handler() {
                 //      explanationDiv.style.maxHeight = 'none';
                 //      explanationDiv.removeEventListener('transitionend', handler);
                 // });

            } else {
                 // Collapse
                  explanationDiv.style.maxHeight = explanationDiv.scrollHeight + 30 + 'px'; // Set current height before transition
                  explanationDiv.style.opacity = '1';

                  // Force reflow
                 explanationDiv.offsetHeight;

                 explanationDiv.style.maxHeight = '0';
                 explanationDiv.style.opacity = '0';

                 // Hide completely after transition
                 explanationDiv.addEventListener('transitionend', function handler() {
                      if (explanationDiv.style.maxHeight === '0px') {
                          explanationDiv.style.display = 'none';
                          explanationDiv.style.transition = ''; // Remove transition property
                          explanationDiv.style.overflow = ''; // Remove overflow hidden
                      }
                       explanationDiv.removeEventListener('transitionend', handler);
                 });
            }
        });
    });
</script>