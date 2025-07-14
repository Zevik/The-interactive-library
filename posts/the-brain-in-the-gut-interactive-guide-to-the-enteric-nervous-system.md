---
title: "המוח שבמעיים: מסע אינטראקטיבי למערכת העצבים האנטרית"
english_slug: the-brain-in-the-gut-interactive-guide-to-the-enteric-nervous-system
category: "מדעי החיים / ביולוגיה"
tags: ["מערכת העצבים האנטרית", "המוח השני", "מעיים", "עיכול", "נוירונים", "סימולציה", "אנטומיה", "פיזיולוגיה"]
---
# המוח שבמעיים: מסע אינטראקטיבי למערכת העצבים האנטרית

האם אי פעם הרגשתם "פרפרים בבטן" לפני אירוע חשוב? או אולי חוויתם כאב בטן בתקופות סטרס? זה לא סתם צירוף מקרים. גלו את העולם המופלא של "המוח השני" שלכם - מערכת העצבים האנטרית (ENS), רשת עצבים אוטונומית ומורכבת שפועלת בדופן המעי שלכם ויכולה להשפיע על הרבה יותר מתהליך העיכול!

צאו למסע אינטראקטיבי בתוך דופן המעי והבינו כיצד נוירונים חישתיים, אינטר-נוירונים ונוירונים מוטוריים עובדים יחד כדי לווסת תהליכים חיוניים, ואף מתקשרים עם המוח "הגדול" שבגולגולת.

<div id="ens-app">
    <div class="gut-section">
        <div class="layer mucosa">
            <div class="layer-label">רירית (Mucosa)</div>
            <!-- Sensory input area -->
            <div class="stimulus-area stretch-stimulus">
                <button class="stimulus-button" data-stimulus="stretch" title="גירוי מתיחה מדופן המעי (למשל עקב נוכחות מזון)">מתיחה / מזון</button>
            </div>
            <div class="stimulus-area chemical-stimulus">
                 <button class="stimulus-button" data-stimulus="chemical" title="גירוי מחומרים כימיים בתוך המעי (למשל תוצרי עיכול, רעלנים)">גירוי כימי</button>
            </div>
        </div>
        <div class="layer submucosa">
            <div class="layer-label">תת-רירית (Submucosa)</div>
            <div class="plexus submucosal-plexus">
                <div class="plexus-label">פקעת תת-רירית (Submucosal Plexus)</div>
                <!-- Neurons (simplified representation) -->
                <div class="neuron sensory-neuron" data-neuron-id="S1" data-plexus="submucosal" title="נוירון חישתי - קולט גירויים מהרירית והתת-רירית">S1</div>
                <div class="neuron inter-neuron" data-neuron-id="I1" data-plexus="submucosal" title="אינטר-נוירון - מעבד מידע ומקשר בין נוירונים">I1</div>
                <div class="neuron motor-neuron" data-neuron-id="M1" data-plexus="submucosal" title="נוירון מוטורי - שולט על הפרשות מקומיות וזרימת דם">M1</div>
                <!-- Connections (visualized by JS) -->
            </div>
        </div>
        <div class="layer muscularis-propria">
            <div class="layer-label">שכבת שריר (Muscularis Propria)</div>
            <div class="plexus myenteric-plexus">
                <div class="plexus-label">פקעת שרירית (Myenteric Plexus)</div>
                 <!-- Neurons -->
                <div class="neuron sensory-neuron" data-neuron-id="S2" data-plexus="myenteric" title="נוירון חישתי - קולט גירויים משכבת השריר (מתיחה)">S2</div>
                <div class="neuron inter-neuron" data-neuron-id="I2" data-plexus="myenteric" title="אינטר-נוירון - מעבד מידע ומקשר בין נוירונים בפקעת">I2</div>
                <div class="neuron inter-neuron" data-neuron-id="I3" data-plexus="myenteric" title="אינטר-נוירון - מסייע בקואורדינציה של תנועתיות">I3</div>
                <div class="neuron motor-neuron" data-neuron-id="M2" data-plexus="myenteric" title="נוירון מוטורי - שולט על התכווצות השריר הטבעתי (פריסטלטיקה/סגמנטציה)">M2</div>
                <div class="neuron motor-neuron" data-neuron-id="M3" data-plexus="myenteric" title="נוירון מוטורי - שולט על התכווצות השריר האורכי (פריסטלטיקה/סגמנטציה)">M3</div>
                 <!-- Connections -->
            </div>
             <div class="muscle-layer circular" data-muscle-type="circular">שריר טבעתי (Circular Muscle)</div>
             <div class="muscle-layer longitudinal" data-muscle-type="longitudinal">שריר אורכי (Longitudinal Muscle)</div>
        </div>
    </div>

    <div class="controls">
        <button class="action-button" id="reset-simulation">איפוס סימולציה</button>
        <button class="action-button" id="toggle-explanation">הסבר מפורט</button>
    </div>

    <div id="simulation-info" class="info-box">לחצו על כפתורי הגירוי (מתיחה/כימי) או על נוירון כדי להתחיל את הסימולציה!</div>
</div>

<style>
/* כללי */
#ens-app {
    font-family: 'Arial', sans-serif;
    max-width: 850px;
    margin: 25px auto;
    border: 2px solid #a0522d; /* Sienna brown for gut wall */
    border-radius: 12px;
    padding: 20px;
    background: linear-gradient(to bottom, #fdf5e6, #faebd7); /* Off-white/beige subtle gradient */
    position: relative; /* Needed for absolute positioning of lines/neurons */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    overflow: hidden; /* Ensure elements stay within bounds */
    direction: rtl; /* Hebrew support */
    text-align: right; /* Align text right for Hebrew */
}

/* שכבות המעי */
.gut-section {
    display: flex;
    flex-direction: column;
    gap: 1px; /* Visual separation between layers */
    border: 1px solid #8b4513; /* Darker brown inner border */
    border-radius: 6px;
    overflow: hidden;
}

.layer {
    padding: 20px 15px 15px 15px; /* More padding top for label */
    min-height: 90px;
    box-sizing: border-box;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 12px; /* Space between elements within layers */
    justify-content: center; /* Center content vertically */
    align-items: center; /* Center content horizontally */
}

.layer-label {
    font-weight: bold;
    font-size: 1em;
    color: #4a2a1a; /* Darker brown for labels */
    position: absolute;
    top: 8px;
    right: 10px; /* Align label to the right */
    background-color: rgba(255, 255, 255, 0.8);
    padding: 3px 8px;
    border-radius: 4px;
    z-index: 2; /* Ensure label is on top */
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.mucosa {
    background: linear-gradient(to bottom, #fff8dc, #ffefd5); /* Cornsilk/PapayaWhip gradient */
    border-bottom: 1px solid #d2b48c; /* Tan border */
}

.submucosa {
    background: linear-gradient(to bottom, #ffe4b5, #ffdab9); /* Moccasin/PeachPuff gradient */
    border-bottom: 1px solid #d2b48c;
}

.muscularis-propria {
     background: linear-gradient(to bottom, #b0e0e6, #add8e6); /* PowderBlue/LightBlue gradient */
     display: flex;
     flex-direction: column;
     justify-content: flex-start; /* Muscle layers at the bottom */
     gap: 8px; /* Space between muscle layers and plexus */
     padding-bottom: 10px; /* Add padding below muscle layers */
}

/* פקעות עצבים */
.plexus {
    border: 1.5px dashed #8a2be2; /* BlueViolet dashed border */
    padding: 15px;
    margin: 8px auto;
    width: 95%;
    min-height: 60px;
    box-sizing: border-box;
    position: relative;
    background-color: rgba(255, 255, 255, 0.6);
    border-radius: 8px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: 20px; /* Space between neurons */
    box-shadow: inset 0 0 5px rgba(138, 43, 226, 0.3);
}

.plexus-label {
     font-weight: bold;
     font-size: 0.9em;
     color: #5d3a80; /* Darker purple */
     position: absolute;
     top: -12px;
     right: 15px; /* Align label to the right */
     background-color: #faebd7; /* Match app background */
     padding: 0 7px;
     border-radius: 4px;
     z-index: 3; /* Ensure label is on top */
}

/* נוירונים */
.neuron {
    width: 35px;
    height: 35px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 0.9em;
    font-weight: bold;
    color: white;
    border: 2px solid #333;
    cursor: pointer; /* Indicate interactivity */
    transition: all 0.2s ease-in-out; /* Smooth transitions */
    box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    z-index: 5; /* Ensure neurons are above lines */
}

.neuron:hover {
    transform: scale(1.1); /* Grow slightly on hover */
    box-shadow: 0 0 15px rgba(255, 255, 0, 0.8); /* Stronger glow hint */
}

.sensory-neuron { background-color: #ff6347; /* Tomato */ border-color: #cd5a4a;}
.inter-neuron { background-color: #6495ed; /* CornflowerBlue */ border-color: #5a82d0;}
.motor-neuron { background-color: #3cb371; /* MediumSeaGreen */ border-color: #349865;}

.neuron.active {
    animation: neuron-pulse 0.5s ease-in-out forwards; /* Animation for active state */
}

@keyframes neuron-pulse {
    0% { box-shadow: 0 0 0 rgba(255, 255, 0, 0.8); transform: scale(1); }
    50% { box-shadow: 0 0 20px rgba(255, 255, 0, 1), 0 0 20px rgba(255, 255, 0, 0.8) inset; transform: scale(1.15); }
    100% { box-shadow: 0 0 0 rgba(255, 255, 0, 0.8); transform: scale(1); }
}


/* כפתורי גירוי */
.stimulus-area {
    position: absolute;
    top: 15px;
    width: 120px; /* Wider button area */
    text-align: center;
    z-index: 5; /* Above other layer elements */
}

.stretch-stimulus { left: 15%; }
.chemical-stimulus { right: 15%; }

.stimulus-button {
    padding: 8px 15px;
    background-color: #007bff; /* Blue */
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.9em;
    font-weight: bold;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.stimulus-button:hover {
    background-color: #0056b3; /* Darker blue */
    transform: translateY(-2px); /* Slight lift on hover */
}

.stimulus-button:active {
    background-color: #003f7f; /* Even darker on click */
    transform: translateY(0);
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}


/* שכבות שריר */
.muscle-layer {
    text-align: center;
    padding: 8px;
    margin: 0 10px; /* Add horizontal margin */
    font-size: 0.9em;
    color: #555;
    position: relative;
    border: 1px dashed #999; /* Indicate separate layers visually */
    border-radius: 4px;
    background-color: rgba(255, 255, 255, 0.3);
    transition: background-color 0.4s ease, transform 0.4s ease; /* Smooth transition for contraction */
}

.muscle-layer.circular { margin-top: 5px;} /* Space below plexus */

.muscle-layer.contracting {
     background-color: rgba(255, 99, 71, 0.5); /* Tomato tint for contraction */
     border-color: #ff6347;
     color: #333; /* Darker text on contraction */
     /* Optional: subtle visual contraction effect */
     /* transform: scaleY(0.95); */
}

/* קווי חיבור (דינמיים) */
.connection-line {
    position: absolute;
    height: 3px; /* Thicker lines */
    background: linear-gradient(to right, rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.6)); /* Subtle gradient */
    transform-origin: 0 0;
    z-index: 1; /* Below neurons */
    pointer-events: none; /* Don't interfere with clicks */
    border-radius: 2px;
    opacity: 0.7;
    transition: background-color 0.1s ease-in-out, box-shadow 0.1s ease-in-out, opacity 0.3s ease;
}

/* אנימציית קו פעיל */
.connection-line.active {
    background: linear-gradient(to right, #ffff00, #ffd700); /* Yellow/Gold gradient for active state */
    box-shadow: 0 0 8px #ffff00; /* Glow effect */
    opacity: 1;
     /* Optional: Animate a dot/pulse along the line - More complex JS needed, sticking to glow for this example */
}


/* אזור בקרה */
.controls {
    text-align: center;
    margin-top: 25px;
    display: flex;
    justify-content: center;
    gap: 15px; /* Space between buttons */
}

.action-button {
    padding: 10px 20px;
    background-color: #28a745; /* Green */
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    font-weight: bold;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.action-button#toggle-explanation {
    background-color: #17a2b8; /* Cyan for explanation */
}

.action-button:hover {
    background-color: #218838; /* Darker green */
    transform: translateY(-2px);
}

.action-button#toggle-explanation:hover {
     background-color: #138496; /* Darker cyan */
}

.action-button:active {
    transform: translateY(0);
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}


/* תיבת מידע */
.info-box {
    margin-top: 20px;
    padding: 10px 15px;
    border: 1px solid #007bff;
    background-color: #e9f7ff; /* Light blue background */
    color: #004085; /* Dark blue text */
    border-radius: 5px;
    text-align: center;
    font-size: 0.95em;
    animation: fadeIn 0.5s ease-out;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}


/* אזור הסבר מפורט */
#explanation {
    margin-top: 25px;
    padding: 20px;
    border: 1px solid #ddd;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    display: none; /* Hidden by default */
    line-height: 1.7;
}

#explanation h2 {
    color: #333;
    border-bottom: 2px solid #eee;
    padding-bottom: 8px;
    margin-top: 20px;
    font-size: 1.5em;
    margin-bottom: 15px;
}
#explanation h2:first-child { margin-top: 0; }

#explanation p {
    margin-bottom: 12px;
    text-align: justify; /* Justify text for better readability */
}

#explanation ul {
    margin-bottom: 12px;
    padding-right: 20px; /* Indent list items */
}

#explanation li {
    margin-bottom: 8px;
    position: relative; /* For custom bullet points if needed */
}

/* Custom bullet points example */
/* #explanation li::before {
    content: '•';
    color: #007bff;
    font-weight: bold;
    display: inline-block;
    width: 1em;
    margin-right: 0.5em;
    margin-left: -1em;
} */

</style>

<div id="explanation">
    <h2>מהי מערכת העצבים האנטרית (ENS)?</h2>
    <p>דמיינו רשת בקרה עצבית עצמאית לחלוטין החבויה בתוך דופן המעי שלכם. זוהי מערכת העצבים האנטרית (Enteric Nervous System - ENS), ולעיתים קרובות היא מכונה "המוח השני" בשל גודלה (כ-100 מיליון נוירונים - יותר מחוט השדרה!) ויכולתה לפעול באופן אוטונומי. ה-ENS מווסתת מגוון עצום של תהליכים חיוניים במערכת העיכול, החל מתנועת המזון וכלה בהפרשות וזרימת דם מקומית.</p>

    <h2>איפה היא נמצאת?</h2>
    <p>ה-ENS אינה מפוזרת אקראית, אלא מאורגנת בעיקר בשתי פקעות (plexuses) מרכזיות המשובצות בדופן המעי:</p>
    <ul>
        <li><strong>הפקעת התת-רירית (Submucosal Plexus / Meissner's Plexus):</strong> יושבת קרוב יותר לחלל המעי, בשכבת התת-רירית. תפקידה העיקרי הוא שליטה על הסביבה הפנימית: ויסות הפרשת נוזלים, ריר, וביקרבונט; בקרה על זרימת הדם המקומית; ואינטראקציה עם תאי חיסון.</li>
        <li><strong>הפקעת השרירית (Myenteric Plexus / Auerbach's Plexus):</strong> ממוקמת אסטרטגית בין שתי שכבות השריר הגדולות (הטבעתית והאורכית). תפקידה המרכזי הוא ויסות התנועתיות של המעי - הפריסטלטיקה (תנועת גלים דוחפת את המזון קדימה) והסגמנטציה (התכווצויות מקומיות לערבוב יעיל של המזון עם אנזימי העיכול).</li>
    </ul>

    <h2>השחקנים הראשיים: סוגי נוירונים</h2>
    <p>ה-ENS בנויה מרשת מסועפת של נוירונים בעלי תפקידים ספציפיים:</p>
    <ul>
        <li><strong>נוירונים חישתיים (Sensory Neurons):</strong> הם החיישנים של המעי. הם קולטים מידע מהסביבה הפנימית: כמה הדופן נמתחת (כשמזון נכנס), אילו חומרים כימיים נמצאים בחלל המעי (שומנים, חלבונים, חומציות, רעלנים), שינויים בטמפרטורה ועוד. הם מעבירים מידע זה הלאה לפקעות.</li>
        <li><strong>אינטר-נוירונים (Interneurons):</strong> אלו הם מרכזי הבקרה והקישור של ה-ENS. הם מקבלים מידע ממספר נוירונים חישתיים או אינטר-נוירונים אחרים, מעבדים אותו (כמו מיני-מעבד), ומחליטים לאילו נוירונים מוטוריים לשלוח אותות, או כיצד לתאם תגובות לאורך קטע מעי ארוך יותר. הם מאפשרים תגובות מורכבות ומתואמות.</li>
        <li><strong>נוירונים מוטוריים (Motor Neurons):</strong> אלו הם המבצעים. הם מקבלים הוראות מהאינטר-נוירונים ומשפיעים ישירות על רקמות המטרה: גורמים לשרירי המעי להתכווץ או להירגע, לבלוטות להפריש, או לכלי דם לשנות את זרימתם.</li>
    </ul>

    <h2>תפקידים קריטיים</h2>
    <p>ה-ENS אחראית על סינכרון ובקרה של מגוון תהליכים חיוניים באופן אוטונומי:</p>
    <ul>
        <li><strong>תנועתיות מעיים (Motility):</strong> תיאום התכווצויות והרפיה של השרירים להנעת המזון (פריסטלטיקה) ולערבובו (סגמנטציה). בלעדי ה-ENS, העיכול היה בלתי אפשרי!</li>
        <li><strong>הפרשות (Secretions):</strong> שליטה על הפרשת מיצי עיכול, חומצה, בסיסים וריר כדי לסייע בפירוק המזון ולהגן על דופן המעי.</li>
        <li><strong>זרימת דם (Blood Flow):</strong> ויסות זרימת הדם המקומית כדי למקסם את ספיגת חומרי המזון לאחר הפירוק.</li>
        <li><strong>תפקוד חיסוני ומחסום מעי:</strong> אינטראקציה עם המערכת החיסונית העצומה שבדופן המעי ושמירה על תקינות המחסום הפיזי מפני פתוגנים וחומרים לא רצויים.</li>
    </ul>

    <h2>אוטונומיה מדהימה</h2>
    <p>מה שהופך את ה-ENS למיוחדת כל כך הוא יכולתה לקלוט גירוי מקומי, לעבד אותו, ולייצר תגובה מוטורית או הפרשתית מתאימה - והכל באופן עצמאי, מבלי שהמידע יעבור אל המוח הגדול שבגולגולת או יקבל ממנו הוראה ישירה. דמיינו שהייתם צריכים לחשוב באופן מודע על כל התכווצות קטנה של המעי לאחר כל ארוחה - ה-ENS חוסכת מהמוח את העומס ומאפשרת לו להתפנות למשימות מורכבות יותר.</p>

    <h2>אבל היא לא מנותקת לגמרי...</h2>
    <p>למרות עצמאותה, ה-ENS מקיימת דו-שיח מתמיד עם מערכת העצבים המרכזית (CNS - המוח וחוט השדרה) באמצעות עצב הואגוס (Vagus Nerve) ועצבי השדרה הסימפתטיים:</p>
    <ul>
        <li><strong>עצב הואגוס:</strong> ערוץ תקשורת דו-כיווני קריטי. הוא מעביר הוראות מהמוח ל-ENS (למשל, האצת פעילות במנוחה) וגם שולח כמות עצומה של מידע חישתי מהמעי למוח (מידע על מתיחה, כימיקלים, מצב דלקתי) - מידע שמשפיע על תחושות רעב, שובע, בחילה ואפילו על מצב הרוח והתגובה לסטרס. זהו הבסיס לקשר "מוח-מעי".</li>
        <li><strong>עצבים סימפתטיים:</strong> מגיעים מהשדרה ובדרך כלל מעכבים את פעילות המעי במצבי סטרס (למשל, בזמן בריחה מאיום). הם גם מעבירים אותות כאב מהמעי ל-CNS.</li>
    </ul>
    <p>התקשורת הזו מאפשרת ל-CNS להשפיע על פעילות המעי במצבים שונים (כמו סטרס או הרפיה) ולקבל מידע חיוני על מצב מערכת העיכול, בעוד שה-ENS מטפלת בלוגיסטיקה המקומית באופן שוטף.</p>

     <h2>"המוח השני" - למה השם הזה?</h2>
    <p>הכינוי "המוח המעי" אינו רק קוריוז. הוא נובע ממספר סיבות:</p>
    <ul>
        <li>**גודל ומורכבות:** מספר הנוירונים העצום ומגוון תאי העצב והמוליכים העצביים הדומים לאלו שבמוח.</li>
        <li>**אוטונומיה:** היכולת לעבד מידע ולקבל החלטות באופן עצמאי ללא תלות ישירה ב-CNS.</li>
        <li>**השפעה על מצב רוח:** הקשר ההדוק בין המעי למוח באמצעות הואגוס וייצור מוליכים עצביים (כמו חלק גדול מהסרוטונין בגוף) במעי, משפיע גם על אספקטים התנהגותיים ופסיכולוגיים.</li>
    </ul>
    <p>הבנת תפקוד ה-ENS היא קריטית לא רק לפיזיולוגיה של העיכול, אלא גם להבנת מצבים רפואיים רבים הקשורים למעי ואפילו לקשרים המורכבים בין הבטן לרגשות ולמצב הנפשי.</p>

     <h2>חשיבות רפואית</h2>
    <p>בעיות בתפקוד ה-ENS קשורות למגוון מחלות וסימפטומים נפוצים, כמו תסמונת המעי הרגיז (IBS), עצירות כרונית, שלשולים, מחלות מעי דלקתיות (IBD), ובעיות תנועתיות לאחר ניתוחים. חקר ה-ENS פותח אפיקים חדשים לפיתוח טיפולים ממוקדים למצבים אלו ולשיפור איכות החיים של מיליוני אנשים.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');
    const resetButton = document.getElementById('reset-simulation');
    const appContainer = document.getElementById('ens-app');
    const stimulusButtons = document.querySelectorAll('.stimulus-button');
    const neurons = document.querySelectorAll('.neuron');
    const muscleLayers = document.querySelectorAll('.muscle-layer');
    const infoBox = document.getElementById('simulation-info');

    // Define neuron connections and activation paths (simplified model)
    // Structure: { neuronId: [{ target: 'targetNeuronId', delay: ms, lineKey: 'start-end' }] }
    const connections = {
        'S1': [{ target: 'I1', delay: 100, lineKey: 'S1-I1' }, { target: 'M1', delay: 200, lineKey: 'S1-M1' }], // Sensory 1 to Inter 1 and Motor 1 (Submucosal)
        'S2': [{ target: 'I2', delay: 100, lineKey: 'S2-I2' }, { target: 'I3', delay: 100, lineKey: 'S2-I3' }, { target: 'M2', delay: 200, lineKey: 'S2-M2' }], // Sensory 2 to Inter 2, Inter 3, Motor 2 (Myenteric)
        'I1': [{ target: 'M1', delay: 100, lineKey: 'I1-M1' }], // Inter 1 to Motor 1
        'I2': [{ target: 'M2', delay: 100, lineKey: 'I2-M2' }], // Inter 2 to Motor 2
        'I3': [{ target: 'M3', delay: 100, lineKey: 'I3-M3' }], // Inter 3 to Motor 3
        // Add connections between plexuses if desired, e.g., Myenteric to Submucosal control
        // 'I2': [{ target: 'I1', delay: 300, lineKey: 'I2-I1' }], // Myenteric to Submucosal communication
        // 'M2': [{ target: 'M1', delay: 350, lineKey: 'M2-M1' }], // Coordinated motor response? (Simplification)
    };

     // Simplified stimulus to initial neuron mapping
     const stimulusMap = {
         'stretch': ['S2'], // Stretch often activates myenteric sensory neurons (S2)
         'chemical': ['S1'] // Chemical often activates submucosal sensory neurons (S1)
     };

    // Store connection line elements
    const connectionElements = {};

    // Function to draw a connection line between two neurons
    function drawConnection(startNeuronId, endNeuronId, lineKey) {
        const startNeuron = document.querySelector(`[data-neuron-id="${startNeuronId}"]`);
        const endNeuron = document.querySelector(`[data-neuron-id="${endNeuronId}"]`);

        if (!startNeuron || !endNeuron) {
             console.error(`Could not find neurons to draw line: ${startNeuronId} to ${endNeuronId}`);
             return null;
        }

        const startRect = startNeuron.getBoundingClientRect();
        const endRect = endNeuron.getBoundingClientRect();
        const appRect = appContainer.getBoundingClientRect();

        // Calculate positions relative to the app container
        const x1 = startRect.left + startRect.width / 2 - appRect.left;
        const y1 = startRect.top + startRect.height / 2 - appRect.top;
        const x2 = endRect.left + endRect.width / 2 - appRect.left;
        const y2 = endRect.top + endRect.height / 2 - appRect.top;

        const length = Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
        const angle = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;

        const line = document.createElement('div');
        line.classList.add('connection-line');
        line.setAttribute('data-line-key', lineKey); // Add data attribute for easy lookup
        line.style.width = `${length}px`;
        line.style.transform = `translate(${x1}px, ${y1}px) rotate(${angle}deg)`;

        // Set transform origin based on direction for potential future animation complexity
        // This is tricky with arbitrary angles, default 0 0 is usually fine for simple lines

        appContainer.appendChild(line);
        return line;
    }

    // Draw all connections on load
    function initializeConnections() {
         // Clear existing lines first if re-initializing
         appContainer.querySelectorAll('.connection-line').forEach(line => line.remove());
         // Clear stored elements
         for (const key in connectionElements) { delete connectionElements[key]; }


         for (const startNeuronId in connections) {
            connections[startNeuronId].forEach(connection => {
                const endNeuronId = connection.target;
                const lineKey = `${startNeuronId}-${endNeuronId}`; // Generate a unique key
                // Check if lineKey is already used or use the specified one
                const finalLineKey = connection.lineKey || lineKey;

                connectionElements[finalLineKey] = drawConnection(startNeuronId, endNeuronId, finalLineKey);
            });
        }
    }


    // Function to simulate signal propagation (using setTimeouts for timing and visual steps)
    function simulateSignal(startNeuronId, currentTotalDelay = 0) {
         const neuronElement = document.querySelector(`[data-neuron-id="${startNeuronId}"]`);
          if (!neuronElement) {
              console.warn(`Neuron element not found: ${startNeuronId}`);
              return;
          }

          // --- Visual Activation Pulse for Neuron ---
          setTimeout(() => {
               neuronElement.classList.add('active');
               // The CSS animation handles the pulse, no need to manually remove 'active' for the pulse effect itself,
               // but we remove it to allow re-triggering the animation.
               setTimeout(() => neuronElement.classList.remove('active'), 500); // Match animation duration
          }, currentTotalDelay);


          // --- Propagate signals along connections ---
           if (connections[startNeuronId]) {
               connections[startNeuronId].forEach(connection => {
                   const nextNeuronId = connection.target;
                   const delay = connection.delay || 100;
                   const nextTotalDelay = currentTotalDelay + delay;
                   const lineKey = connection.lineKey || `${startNeuronId}-${nextNeuronId}`;
                   const lineElement = connectionElements[lineKey];

                   if(lineElement) {
                       // --- Animate Connection Line ---
                       // Activate the line *during* the signal travel time
                        setTimeout(() => {
                            lineElement.classList.add('active');
                             // Deactivate line after signal has passed
                            setTimeout(() => lineElement.classList.remove('active'), delay + 50); // Line active slightly longer than travel
                        }, currentTotalDelay + (delay * 0.2)); // Activate line slightly after leaving source neuron
                   } else {
                       console.warn(`Connection line element not found for key: ${lineKey}`);
                   }

                    // --- Recursive call for the next neuron ---
                   simulateSignal(nextNeuronId, nextTotalDelay);
               });
           }

           // --- Motor neuron effects ---
           if (neuronElement.classList.contains('motor-neuron')) {
                // Trigger muscle contraction visual *after* the motor neuron is fully activated
               setTimeout(() => {
                   if (startNeuronId === 'M1') { // Typically affects secretions/blood flow (submucosal plexus)
                       // For visualization, we could highlight the mucosa/submucosa layer or show a simple effect
                       // Let's add a simple visual cue - maybe a pulse on the surrounding plexus/layer
                       const plexus = neuronElement.closest('.plexus');
                       if(plexus) {
                           plexus.style.boxShadow = '0 0 15px rgba(0, 255, 255, 0.7)'; // Cyan glow
                           setTimeout(() => plexus.style.boxShadow = 'inset 0 0 5px rgba(138, 43, 226, 0.3)', 600); // Revert
                       }

                   } else if (startNeuronId === 'M2' || startNeuronId === 'M3') { // Affects muscle layers (myenteric plexus)
                        const muscleType = (startNeuronId === 'M2') ? 'circular' : 'longitudinal'; // M2 often circular, M3 often longitudinal (simplification)
                        const muscleLayer = document.querySelector(`.muscle-layer.${muscleType}`);
                         if(muscleLayer) {
                            muscleLayer.classList.add('contracting');
                            setTimeout(() => muscleLayer.classList.remove('contracting'), 800); // Contraction lasts 800ms
                         }
                   }
               }, currentTotalDelay + 100); // Delay slightly after neuron activation
           }
    }

    // Function to reset the simulation visuals
    function resetSimulation() {
        neurons.forEach(n => {
            n.classList.remove('active');
             // Remove inline styles if any were added by JS for effects (like box-shadow on plexus)
             const plexus = n.closest('.plexus');
             if (plexus) plexus.style.boxShadow = '';
        });
        muscleLayers.forEach(m => m.classList.remove('contracting'));
        document.querySelectorAll('.connection-line').forEach(line => line.classList.remove('active'));
        infoBox.textContent = 'לחצו על כפתורי הגירוי (מתיחה/כימי) או על נוירון כדי להתחיל את הסימולציה!';
        infoBox.style.borderColor = '#007bff';
        infoBox.style.backgroundColor = '#e9f7ff';
        infoBox.style.color = '#004085';
    }


    // Add event listeners to stimulus buttons
    stimulusButtons.forEach(button => {
        button.addEventListener('click', () => {
            const stimulusType = button.dataset.stimulus;
            resetSimulation(); // Clear previous state
            infoBox.textContent = `גירוי: ${stimulusType === 'stretch' ? 'מתיחה / מזון' : 'כימי'}. הסימולציה החלה...`;
            infoBox.style.borderColor = '#28a745'; // Greenish border for active sim
            infoBox.style.backgroundColor = '#d4edda'; // Greenish background
            infoBox.style.color = '#155724'; // Green text

            if (stimulusMap[stimulusType]) {
                // Trigger simulation for each initial neuron mapped to this stimulus
                 stimulusMap[stimulusType].forEach(startNeuronId => {
                     simulateSignal(startNeuronId);
                 });
            }
        });
    });

    // Add event listeners to neurons to make them clickable
     neurons.forEach(neuron => {
         neuron.addEventListener('click', () => {
             const neuronId = neuron.dataset.neuronId;
             console.log(`Activating neuron: ${neuronId}`);
             resetSimulation(); // Clear previous state
             infoBox.textContent = `הפעלת נוירון: ${neuronId}. הסימולציה החלה...`;
             infoBox.style.borderColor = '#ffc107'; // Yellowish border for neuron trigger
             infoBox.style.backgroundColor = '#fff3cd'; // Yellowish background
             infoBox.style.color = '#856404'; // Yellowish text

             simulateSignal(neuronId); // Simulate starting propagation from this neuron
         });
     });

     // Add event listener for reset button
     resetButton.addEventListener('click', resetSimulation);


    // Toggle explanation visibility
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר' : 'הצג הסבר מפורט';
        // Re-draw lines in case showing explanation affected layout (less likely with fixed max-width but good practice)
         // setTimeout(initializeConnections, 0); // Use setTimeout to ensure DOM update happens first
    });

    // Initial state: Explanation is hidden
    explanationDiv.style.display = 'none';
    toggleButton.textContent = 'הצג הסבר מפורט'; // Set initial button text


    // Initialize connections after the DOM is ready and rendered
    // Use a small delay to ensure layout is stable before measuring elements
    setTimeout(initializeConnections, 50);

    // Optional: Re-draw lines if window is resized (can affect element positions)
    // This is more complex to do robustly and might cause performance issues on resize.
    // Skipping for this simplified example, assuming fixed or mostly static layout.
    // window.addEventListener('resize', () => {
    //     clearTimeout(window._resizeTimeout);
    //     window._resizeTimeout = setTimeout(initializeConnections, 200);
    // });

});
</script>