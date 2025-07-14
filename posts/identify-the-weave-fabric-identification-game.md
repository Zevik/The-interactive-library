---
title: "זהה את האריג: מסע אינטראקטיבי לזיהוי בדים"
english_slug: identify-the-weave-fabric-identification-game
category: "אופנה וטקסטיל"
tags: אריגה, בד, טקסטיל, זיהוי בדים, סוגי אריגה
---

# מסע אל תוך סיבי האריג: משחק זיהוי בדים

כל בד מספר סיפור דרך מבנה האריגה שלו. האם תוכל לזהות את השזירה המסתתרת מתחת למראה הבד הסופי? בואו לצאת למסע זום אינטראקטיבי וללמוד לזהות את סוגי האריגה העיקריים שמשפיעים על הכל - מהמגע של חולצה ועד העמידות של ג'ינס. האתגר מתחיל עכשיו!

<div id="game-container" dir="rtl">
    <div id="progress-area">שאלה <span id="current-question">1</span> מתוך <span id="total-questions"></span></div>
    <h2>איזו אריגה זו?</h2>
    <div id="question-area">
        <div id="image-wrapper">
            <img id="fabric-image" src="" alt="תקריב של אריג בד">
        </div>
        <div id="options" class="options-layout">
            <!-- Option buttons will be inserted here by JS -->
        </div>
    </div>
    <div id="feedback-area" class="feedback-style">
        <!-- Feedback text will appear here -->
    </div>
    <button id="next-button" class="control-button" style="display: none;">לשאלה הבאה</button>
     <div id="end-message" style="display: none;" class="completion-message">
        <p>✨ כל הכבוד! ✨</p>
        <p>סיימת בהצלחה את כל האתגרים! כעת אתה מוכן לצלול עמוק יותר אל עולם האריגה עם ההסבר המורחב.</p>
     </div>
</div>

<style>
    /* --- כללי ומכלים --- */
    #game-container {
        font-family: 'Heebo', sans-serif; /* Modern Hebrew-friendly font */
        max-width: 700px; /* Slightly wider container */
        margin: 20px auto;
        padding: 30px;
        border: none; /* Remove default border */
        border-radius: 12px; /* More rounded corners */
        background-color: #ffffff; /* Clean background */
        text-align: center;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        position: relative; /* For absolute positioning if needed */
    }

    h2 {
        color: #333;
        margin-top: 15px; /* Spacing below progress */
        margin-bottom: 25px; /* Spacing above image */
        font-size: 1.8em; /* Larger heading */
    }

    /* --- אזור התקדמות --- */
    #progress-area {
        position: absolute;
        top: 15px;
        left: 15px;
        font-size: 0.9em;
        color: #555;
        font-weight: bold;
    }

    /* --- אזור התמונה --- */
    #image-wrapper {
        width: 100%; /* Image container takes full width */
        max-width: 500px; /* Max width for image */
        margin: 0 auto 25px; /* Center image and add bottom space */
        border: 2px solid #eee;
        border-radius: 8px;
        overflow: hidden; /* Ensure image stays within bounds */
        background-color: #f0f0f0; /* Placeholder background */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
        position: relative; /* Needed for potential future effects */
    }

    #fabric-image {
        display: block; /* Remove extra space below image */
        width: 100%;
        height: auto;
        transition: transform 0.5s ease-in-out, opacity 0.5s ease-in-out; /* Smooth transitions */
        opacity: 1; /* Initial state */
    }

     #fabric-image.loading {
        opacity: 0.2; /* Indicate loading */
     }

    /* --- אפשרויות בחירה --- */
    #options {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 12px; /* More space between buttons */
        margin-top: 20px;
    }

    #options button {
        flex-grow: 1; /* Allow buttons to grow */
        flex-basis: 150px; /* Minimum width before wrapping */
        padding: 12px 20px; /* More padding */
        font-size: 1.1em; /* Larger font */
        cursor: pointer;
        border: 1px solid #ccc;
        border-radius: 6px;
        background-color: #f8f8f8;
        color: #333;
        transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.1s ease; /* Smooth transitions */
        min-width: 120px; /* Ensure minimum width */
        max-width: 200px; /* Ensure max width */
    }

    #options button:hover:not(:disabled) {
        background-color: #e0e0e0;
        border-color: #a0a0a0;
        transform: translateY(-2px); /* Slight lift effect */
    }

    #options button:active:not(:disabled) {
         transform: translateY(0); /* Press down effect */
    }


    #options button:disabled {
        cursor: not-allowed; /* Clearer disabled state */
        opacity: 0.6;
    }

    #options button.correct {
        border-color: #4CAF50; /* Green border */
        background-color: #e8f5e9; /* Light green background */
        color: #1b5e20; /* Darker green text */
        font-weight: bold;
        animation: pulse-correct 0.5s ease-in-out; /* Subtle animation */
    }

     #options button.incorrect {
        border-color: #F44336; /* Red border */
        background-color: #ffebee; /* Light red background */
        color: #b71c1c; /* Darker red text */
        font-weight: bold;
        animation: shake 0.3s ease-in-out; /* Shake animation */
    }

    /* --- אזור פידבק --- */
    #feedback-area {
        margin-top: 25px; /* Space above feedback */
        padding: 15px;
        border-radius: 8px;
        min-height: 3em; /* More space for text */
        font-size: 1.15em; /* Slightly larger font */
        line-height: 1.6;
        text-align: right; /* RTL text alignment */
        opacity: 0; /* Initially hidden */
        transform: translateY(10px); /* Start slightly below */
        transition: opacity 0.4s ease-out, transform 0.4s ease-out; /* Fade and slide in */
    }

     #feedback-area.visible {
        opacity: 1;
        transform: translateY(0);
     }


    #feedback-area.correct {
        background-color: #e8f5e9;
        color: #1b5e20;
        border: 1px solid #4CAF50;
    }

     #feedback-area.incorrect {
        background-color: #ffebee;
        color: #b71c1c;
        border: 1px solid #F44336;
    }

    /* --- כפתור הבא --- */
     .control-button {
        display: block; /* Make button take full width or center */
        margin: 25px auto 0; /* Center button and add space */
        padding: 12px 30px; /* More padding */
        font-size: 1.2em; /* Larger font */
        cursor: pointer;
        background-color: #007bff; /* Primary button color */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transitions */
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.2); /* Subtle shadow */
     }

    .control-button:hover {
        background-color: #0056b3; /* Darker on hover */
        transform: translateY(-1px); /* Slight lift */
    }

    .control-button:active {
         transform: translateY(0); /* Press effect */
    }

    /* --- הודעת סיום --- */
     .completion-message {
        margin-top: 30px;
        padding: 20px;
        border: 2px dashed #4CAF50; /* Green dashed border */
        border-radius: 8px;
        background-color: #e8f5e9; /* Light green background */
        color: #1b5e20;
        font-size: 1.3em;
        font-weight: bold;
        text-align: center;
     }

     .completion-message p:first-child {
         font-size: 1.5em;
         margin-bottom: 10px;
     }

    /* --- הסבר מורחב --- */
    #toggle-explanation {
        display: block; /* Make button take full width or center */
        margin: 40px auto 20px; /* Center button and add space */
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #6c757d; /* Secondary button color */
        color: white;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease;
        box-shadow: 0 4px 8px rgba(108, 117, 125, 0.2);
    }

    #toggle-explanation:hover {
        background-color: #545b62;
    }

    #explanation {
        margin-top: 20px;
        padding: 30px;
        border: none; /* Remove default border */
        border-radius: 8px;
        background-color: #f8f9fa; /* Light grey background */
        text-align: right; /* For RTL text */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }

    #explanation h2 {
        color: #0056b3;
        margin-top: 0; /* Remove top margin */
        margin-bottom: 15px;
        border-bottom: 2px solid #007bff; /* Blue border */
        padding-bottom: 8px;
        font-size: 1.6em;
        text-align: right;
    }

    #explanation h3 {
        color: #007bff;
        margin-top: 25px;
        margin-bottom: 10px;
        font-size: 1.3em;
        text-align: right;
    }

    #explanation p {
        line-height: 1.8; /* Increased line spacing */
        margin-bottom: 15px;
        color: #444;
    }

    #explanation ul {
        margin-bottom: 15px;
        padding-right: 20px; /* Add space for bullets */
        list-style-type: disc; /* Bullet points */
        color: #444;
    }

    #explanation ul li {
        margin-bottom: 8px;
        line-height: 1.6;
    }

    #explanation strong {
        color: #333;
    }

     /* --- אנימציות --- */
    @keyframes pulse-correct {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }

    @keyframes shake {
        0% { transform: translateX(0); }
        20% { transform: translateX(-5px); }
        40% { transform: translateX(5px); }
        60% { transform: translateX(-5px); }
        80% { transform: translateX(5px); }
        100% { transform: translateX(0); }
    }


</style>

<button id="toggle-explanation" class="control-button">הצג הסבר מורחב</button>

<div id="explanation" style="display: none;" dir="rtl">
    <h2>הבנת האריגה: יסודות מבנה הבד</h2>
    <p>
        ברוכים הבאים לצלילה לעומק עולם הטקסטיל! אריגה היא אומנות עתיקה ומשפיעה, שקובעת כיצד סיבים הופכים לבד. זהו לא רק חיבור אקראי של חוטים, אלא שזירה מדויקת של שתי קבוצות חוטים המכתיבה את תכונות הבד הסופי - החל מהחוזק והעמידות, דרך המגע והווילון (האופן שבו הבד נשפך), ועד למראה והברק. הבנת האריגה היא המפתח לזיהוי בדים שונים והערכת איכותם.
    </p>
    <p>
        <strong>השחקנים הראשיים: חוטי שתי וחוטי ערב</strong><br>
        בד ארוג מורכב תמיד משתי קבוצות של חוטים, הפועלות יחד בהרמוניה (או בניגוד מסוים) כדי ליצור את המבנה הרצוי:
        <ul>
            <li><strong>חוטי שתי (Warp):</strong> אלו החוטים האורכיים, המתוחים לכל אורכו של הנול (מכונת האריגה). הם מהווים את "עמוד השדרה" של הבד.</li>
            <li><strong>חוטי ערב (Weft / Filling):</strong> אלו החוטים הרוחביים, המוזנים לרוחב הנול ונשזרים בין חוטי השתי. הם ממלאים את המבנה הרוחבי של הבד.</li>
        </ul>
        המפגש והשזירה ההדדית בין חוטי השתי לחוטי הערב יוצרים את מבנה האריגה, הנקרא גם דגם האריגה (Weave Pattern). שינוי קטן בדגם יכול לשנות לחלוטין את תכונות הבד. נתמקד בשלושה דגמי אריגה בסיסיים וחשובים: פליין, טוויל וסאטן.
    </p>

    <h3>אריגת פליין (Plain Weave) - הפשטות היציבה</h3>
    <p>
        זוהי אם כל האריגות - הבסיסית, הפשוטה, והנפוצה ביותר. לעיתים נקראת גם אריגה רגילה או טאבי.
        <ul>
            <li><strong>הסוד במבנה:</strong> כל חוט ערב עובר פעם אחת מעל חוט שתי אחד ופעם אחת מתחת לחוט השתי הבא, בסדר קבוע של "אחד מעל, אחד מתחת". דמיינו שתי וערב שמתחלפים בתפקידים שוב ושוב כמו בריצרד פשוט.</li>
            <li><strong>התכונות המובהקות:</strong> בדים ארוגים בפליין הם בדרך כלל יציבים, עמידים יחסית, וללא צד ימין ושמאל מובחנים (אלא אם כן יש הדפס או גימור). האריגה הצפופה יחסית מקנה להם חוזק, אך היא גם גורמת להם להיות נוקשים מעט יותר ובעלי נטייה גבוהה יותר להתקמט בהשוואה לאריגות מורכבות יותר.</li>
            <li><strong>פוגשים אותה ביום יום:</strong> בדים כמו כותנה בסיסית (למשל, בטנות, חלק מחולצות T), מוסלין, ברודקלוט, פופלין (מכירים את החולצות המכופתרות הקלאסיות? רבות מהן פופלין), טפטה וקנבס בסיסי.</li>
        </ul>
    </p>

    <h3>אריגת טוויל (Twill Weave) - האלכסון העמיד</h3>
    <p>
        אריגת טוויל היא כוכבת עמידות עם טוויסט - תרתי משמע! היא מוכרת בזכות הקווים האלכסוניים הברורים שנראים על פני הבד.
        <ul>
            <li><strong>הסוד במבנה:</strong> כאן, חוט ערב עובר מעל שני חוטי שתי או יותר ברצף (למשל, שניים, שלושה או אפילו ארבעה), ורק אז עובר מתחת לחוט שתי אחד (או יותר, תלוי במורכבות הטוויל). הסוד לאלכסון הוא היסט קבוע של נקודות השזירה בכל שורה עוקבת. בכל פעם שהאריגה "עולה" שורה, נקודת השזירה "זזה" חוט שתי אחד הצידה, וכך נוצר קו אלכסוני.</li>
            <li><strong>התכונות המובהקות:</strong> בדי טוויל חזקים, עמידים מאוד בפני שחיקה (חשבו על ג'ינס!). הם נוטים להתקמט פחות מבדי פליין ובעלי וילון טוב יותר. יש להם צד ימין (עם האלכסון הבולט) וצד שמאל (עם האלכסון הפחות בולט, או בכיוון ההפוך).</li>
            <li><strong>פוגשים אותה ביום יום:</strong> ג'ינס (הטוויל הקלאסי!), גברדין (בד לחליפות), צ'ינו (מכנסיים קז'ואל), ואפילו באריג אדרה (הרינגבון), שהוא למעשה וריאציה של טוויל עם שינוי כיוון האלכסון.</li>
        </ul>
    </p>

    <h3>אריגת סאטן (Satin Weave) - הברק היוקרתי</h3>
    <p>
        כשמדברים על חלקות וברק, מדברים על סאטן. חשוב לזכור ש"סאטן" הוא שם האריגה, לא הרכב הסיבים! אפשר למצוא סאטן משי, סאטן כותנה, סאטן פוליאסטר וכו'.
        <ul>
            <li><strong>הסוד במבנה:</strong> כאן המטרה היא להסתיר ככל האפשר את נקודות השזירה. חוט אחד (בדרך כלל חוט השתי בסאטן קלאסי, או חוט הערב ב"סאטין") עובר מעל ארבעה, חמישה או יותר חוטים מהמערכת הנגדית ברצף, ורק אז נשזר מתחת לאחד. המעברים הארוכים האלה נקראים "ציפות" (Floats). הציפות הן שמשקפות את האור ויוצרות את הברק המפורסם. נקודות השזירה מפוזרות ולא יוצרות קו רציף.</li>
            <li><strong>התכונות המובהקות:</strong> המאפיין הבולט ביותר הוא משטח חלק, מבריק ונעים מאוד למגע. בדי סאטן בעלי וילון מצוין ונשפכים יפה. החיסרון הוא שנקודות השזירה המועטות והציפות הארוכות הופכות אותם לפחות עמידים בפני שחיקה, והם נוטים להיתפס ולהישלף בקלות רבה יותר מבדי פליין וטוויל בצפיפות דומה.</li>
            <li><strong>פוגשים אותה ביום יום:</strong> מצעי יוקרה (סאטן כותנה), שמלות ערב, בטנות לבגדים יוקרתיים, וצעיפים משי. סאטין (Sateen) היא גרסת כותנה עמידה יותר של אריגת סאטן, בה הברק נוצר בעיקר על ידי חוטי הערב, ומשמשת רבות במצעים וריפודים.</li>
        </ul>
    </p>

    <h3>כיצד האריגה מעצבת את הבד? סיכום השפעות</h3>
    <p>
        ראינו שסוג האריגה אינו רק עניין טכני, אלא קובע את ה"אישיות" של הבד:
        <ul>
            <li><strong>עמידות:</strong> פליין וטוויל חזקים ועמידים יותר מסאטן (עקב ריבוי נקודות השזירה). טוויל עמיד במיוחד לשחיקה.</li>
            <li><strong>מראה:</strong> פליין וטוויל בעלי מראה מאט או טקסטורה גלויה (פליין - אחידה, טוויל - אלכסונית). סאטן - חלק ומבריק.</li>
            <li><strong>מגע:</strong> סאטן הוא החלק והרך ביותר.</li>
            <li><strong>קמטים:</strong> טוויל מתקמט הכי פחות, פליין הכי הרבה. סאטן מתקמט בקמטים רכים.</li>
            <li><strong>וילון:</strong> סאטן וטוויל נשפכים יפה יותר מפליין.</li>
        </ul>
    </p>

    <h3>סיכום והזמנה לתרגול</h3>
    <p>
        המסע לזיהוי אריג דורש סבלנות והתבוננות. ככל שתתאמן ותבחן יותר בדים מקרוב, כך העין שלך תתחדד. קח בד כלשהו, חפש את הכיוונים (שתי וערב), נסה לראות את נקודות השזירה ואת התבנית שחוזרת על עצמה. האם יש אלכסון? האם המשטח חלק ומבריק? האם רואים הרבה נקודות מפגש קטנות? בהצלחה בזיהוי האריגים שמקיפים אותך בכל מקום!
    </p>
</div>

<script>
    // Helper function to shuffle an array
    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]]; // Swap elements
        }
        return array;
    }

    const questions = shuffleArray([ // Shuffle the order of questions
      {
        image: 'images/plain-weave-01.jpg',
        correctAnswer: 'אריגת פליין',
        options: ['אריגת פליין', 'אריגת טוויל', 'אריגת סאטן'],
        feedback: {
          correct: '🎉 נכון מאוד! 🎉 זוהי אריגת פליין. המבנה של "אחד מעל, אחד מתחת" בכל חוט יוצר את המראה היציב והצפוף הזה.',
          incorrect: {
            'אריגת טוויל': '🤔 לא מדויק. זו לא אריגת טוויל. חפש כאן את הקווים האלכסוניים שאופייניים לטוויל. אין כאן כאלה. המבנה האחיד והצפוף שאתה רואה הוא סימן זיהוי של אריגת פליין.',
            'אריגת סאטן': '🧐 לא מדויק. זו לא אריגת סאטן. אריגת סאטן נראית חלקה ומבריקה יותר, עם נקודות שזירה מרוחקות ולא בולטות. המבנה המחוספס יותר עם נקודות שזירה קרובות שמאפיין את התמונה הוא של אריגת פליין.'
          }
        }
      },
      {
        image: 'images/twill-weave-01.jpg',
        correctAnswer: 'אריגת טוויל',
        options: ['אריגת פליין', 'אריגת טוויל', 'אריגת סאטן'],
        feedback: {
          correct: '🚀 מצוין! 🚀 זיהית נכון את התבנית האלכסונית המובהקת של אריגת טוויל. הקווים האלכסוניים נוצרים מהיסט קבוע של נקודות השזירה בכל שורה.',
          incorrect: {
            'אריגת פליין': '🤔 לא מדויק. זו לא אריגת פליין. אריגת פליין יוצרת מבנה אחיד וצפוף ללא כיווניות אלכסונית. הקווים האלכסוניים שאתה רואה כאן הם הסימן המובהק של אריגת טוויל.',
            'אריגת סאטן': '🧐 לא מדויק. זו לא אריגת סאטן. אריגת סאטן נראית חלקה ומבריקה מאוד, כמעט ללא טקסטורה נראית לעין. המבנה האלכסוני שבתמונה מאפיין את אריגת הטוויל.'
          }
        }
      },
        {
        image: 'images/satin-weave-01.jpg',
        correctAnswer: 'אריגת סאטן',
        options: ['אריגת פליין', 'אריגת טוויל', 'אריגת סאטן'],
        feedback: {
          correct: '💎 פנטסטי! 💎 זהו אכן מראה חלק ומבריק של אריגת סאטן. הברק נוצר בגלל נקודות השזירה המועטות והציפות הארוכות שמשקפות את האור.',
          incorrect: {
            'אריגת פליין': '🤔 לא מדויק. זו לא אריגת פליין. אריגת פליין יוצרת מבנה צפוף ויציב יותר, ללא המראה החלק והמבריק העז שאתה רואה כאן, שמאפיין את אריגת הסאטן.',
            'אריגת טוויל': '🧐 לא מדויק. זו לא אריגת טוויל. אריגת טוויל מתאפיינת בתבנית אלכסונית ברורה. המראה החלק והאחיד שבתמונה הוא הסימן המובהק של אריגת סאטן.'
          }
        }
      },
       {
        image: 'images/plain-weave-02.jpg',
        correctAnswer: 'אריגת פליין',
        options: ['אריגת טוויל', 'אריגת פליין', 'אריגת סאטן'], // Shuffle options within questions too
        feedback: {
          correct: '🎯 יופי של זיהוי! 🎯 עוד דוגמה מצוינת לאריגת פליין הקלאסית. שים לב למבנה האחיד והצפוף, ללא אלכסונים או ברק מיוחד.',
          incorrect: {
            'אריגת טוויל': '🤔 זו לא אריגת טוויל. בדוק היטב - האם אתה רואה קווים אלכסוניים אופייניים לטוויל? אין כאן כאלה. המבנה האחיד והצפוף הוא של פליין.',
            'אריגת סאטן': '🧐 זו לא אריגת סאטן. מראה הסאטן חלק ומבריק הרבה יותר, עם נקודות שזירה מרוחקות. כאן רואים את נקודות השזירה בצורה ברורה ובפיזור אחיד יותר, אופייני לפליין.'
          }
        }
      },
        {
        image: 'images/twill-weave-02.jpg',
        correctAnswer: 'אריגת טוויל',
        options: ['אריגת סאטן', 'אריגת פליין', 'אריגת טוויל'], // Shuffle options
         feedback: {
          correct: '💯 בדיוק! 💯 שוב הקווים האלכסוניים של אריגת טוויל בולטים כאן. אריגה זו ידועה בחוזקה ובעמידותה הגבוהה לשחיקה.',
          incorrect: {
            'אריגת סאטן': '🤔 זו לא אריגת סאטן. סאטן נראה שונה לגמרי - חלק ומבריק מאוד. כאן יש מבנה אלכסוני ברור.',
            'אריגת פליין': '🧐 זו לא אריגת פליין. אריגת פליין חסרה את הקווים האלכסוניים המובהקים שנראים כאן. המבנה האלכסוני הוא הסימן הייחודי של טוויל.'
          }
        }
      },
        {
        image: 'images/satin-weave-02.jpg',
        correctAnswer: 'אריגת סאטן',
        options: ['אריגת פליין', 'אריגת טוויל', 'אריגת סאטן'], // Shuffle options
        feedback: {
          correct: '🌟 מדהים! 🌟 המשטח החלק והמבריק בצורה עקבית מצביע על אריגת סאטן. שים לב כמה מעט נקודות שזירה נראות לעין.',
          incorrect: {
            'אריגת פליין': '🤔 זו לא אריגת פליין. אריגת פליין בדרך כלל מטית יותר ופחות חלקה משמעותית. המראה החלק והמבריק שייך לסאטן.',
            'אריגת טוויל': '🧐 זו לא אריגת טוויל. אריגת טוויל מתאפיינת במבנה אלכסוני בולט שאינו קיים כאן. המראה החלק הוא של סאטן.'
          }
        }
      }
    ]);

    let currentQuestionIndex = 0;
    const fabricImage = document.getElementById('fabric-image');
    const optionsDiv = document.getElementById('options');
    const feedbackArea = document.getElementById('feedback-area');
    const nextButton = document.getElementById('next-button');
    const endMessage = document.getElementById('end-message');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const currentQuestionSpan = document.getElementById('current-question');
    const totalQuestionsSpan = document.getElementById('total-questions');

    totalQuestionsSpan.textContent = questions.length;

    function loadQuestion(index) {
        if (index >= questions.length) {
            showEndMessage();
            return;
        }

        const question = questions[index];
        currentQuestionSpan.textContent = index + 1;

        // Add loading class for image transition
        fabricImage.classList.add('loading');

        // Use a small delay to allow the loading class transition to start
        setTimeout(() => {
             fabricImage.src = question.image;
             // Remove loading class when image is loaded
             fabricImage.onload = () => {
                fabricImage.classList.remove('loading');
             };
             // Handle potential image loading errors
             fabricImage.onerror = () => {
                console.error('Failed to load image:', question.image);
                fabricImage.classList.remove('loading'); // Still remove class
                // Optionally show a placeholder or error message
             };
        }, 100); // Short delay


        optionsDiv.innerHTML = ''; // Clear previous options
        feedbackArea.textContent = ''; // Clear feedback
        feedbackArea.className = 'feedback-style'; // Reset feedback classes
        feedbackArea.classList.remove('visible'); // Hide feedback area initially
        nextButton.style.display = 'none'; // Hide next button

        const shuffledOptions = shuffleArray([...question.options]); // Shuffle options for diversity

        shuffledOptions.forEach(optionText => {
            const button = document.createElement('button');
            button.textContent = optionText;
            button.addEventListener('click', () => handleAnswer(optionText, question));
            optionsDiv.appendChild(button);
        });
    }

    function handleAnswer(selectedOption, question) {
        // Disable all buttons after selection
        Array.from(optionsDiv.children).forEach(button => {
            button.disabled = true;
            if (button.textContent === question.correctAnswer) {
                button.classList.add('correct'); // Highlight correct answer
            }
            if (button.textContent === selectedOption && selectedOption !== question.correctAnswer) {
                 button.classList.add('incorrect'); // Highlight user's incorrect answer
            }
        });

        // Set feedback text and class
        if (selectedOption === question.correctAnswer) {
            feedbackArea.textContent = question.feedback.correct;
            feedbackArea.classList.add('correct');
        } else {
            const feedbackText = question.feedback.incorrect[selectedOption] || 'תשובה שגויה.'; // Fallback
            feedbackArea.textContent = feedbackText + `\n\n💡 האריגה הנכונה היא: ${question.correctAnswer}.`; // Add correct answer hint
             feedbackArea.classList.add('incorrect');
        }

        // Show feedback area with animation
        feedbackArea.classList.add('visible');


        nextButton.style.display = 'block'; // Show next button
        // Optional: Add a small delay or animation to the next button appearance
    }

    function showEndMessage() {
        document.getElementById('game-container').style.display = 'none';
        endMessage.style.display = 'block';
        // Ensure explanation button is visible and correctly labeled at the end
        toggleExplanationButton.style.display = 'block';
        toggleExplanationButton.textContent = explanationDiv.style.display === 'none' ? 'הצג הסבר מורחב' : 'הסתר הסבר מורחב';
    }


    nextButton.addEventListener('click', () => {
        currentQuestionIndex++;
        loadQuestion(currentQuestionIndex);
    });

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        // Smooth toggle using transitions (requires height/max-height manipulation or CSS classes)
        // For simplicity and strict structure, we'll stick to display toggle for now, but use text transition.
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מורחב' : 'הצג הסבר מורחב';
    });

    // Initialize the first question when the page loads
    document.addEventListener('DOMContentLoaded', () => {
        loadQuestion(currentQuestionIndex);
    });


</script>
---
```