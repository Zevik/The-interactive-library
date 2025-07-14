---
title: "בלצ'לי פארק: יום בחיי מפצח צפנים"
english_slug: bletchley-park-day-in-the-life-of-a-codebreaker
category: "ארכאולוגיה"
tags:
  - מלחמת העולם השנייה
  - בלצ'לי פארק
  - קריפטוגרפיה
  - צפנים
  - היסטוריה צבאית
---
# בלצ'לי פארק: יום בחיי מפצח צפנים

דמיין שזה בוקר אביבי שקט באחוזת כפר ציורית באנגליה. אבל בתוך הצריפים המכוסים בעצים, מוחם החריף ביותר של בעלות הברית נמצא במרוץ נגד הזמן. ערימות של טקסט חסר משמעות לחלוטין נוחתות על שולחנך מדי יום. אלו מברקים מוצפנים של האויב. גילוי קטן באחת מהערימות האלו יכול להציל אלפי חיי אדם או לשנות את גורל המלחמה כולה. ברוכים הבאים ליום בחיי מפצח צפנים בבלצ'לי פארק. משימתך: למצוא את ה'עריסות' - רמזי מפתח בטקסט המוצפן שיעזרו לפצח את הצופן היומי.

<div id="bletchley-app">
    <div class="app-header">
        <h2>משימת פענוח צפנים</h2>
        <div id="timer" class="timer">0:00</div>
    </div>

    <div class="card message-area">
        <p class="card-label">מברק מוצפן מנותח:</p>
        <div id="encrypted-message" class="encrypted-text">טוען מברק...</div>
    </div>

    <div class="card tool-area">
        <p class="card-label">כלי עזר וסטטוס:</p>
        <div class="indicator-lights-container">
            <span id="status-light" class="light working"></span>
            <span id="status-text" class="status-text">ממתין לבדיקה...</span>
        </div>
        <div class="crib-input-area">
            <input type="text" id="crib-input" placeholder="הזן עריסה (רמז טקסט)...">
            <button id="check-crib-button">בדוק עריסה</button>
        </div>
        <div id="feedback-area" class="feedback"></div>
    </div>

     <div class="card progress-area">
        <p class="card-label">התקדמות יומית:</p>
        <div class="progress-bar-container">
            <div id="progress-bar" class="progress-bar"></div>
        </div>
        <div id="message-counter" class="progress-text">מברק 0 מתוך 0</div>
    </div>
</div>

<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=Heebo:wght@400;600&display=swap');

#bletchley-app {
    font-family: 'Heebo', sans-serif;
    direction: rtl;
    text-align: right;
    max-width: 700px;
    margin: 20px auto;
    padding: 25px;
    border: 1px solid #4a4a4a;
    border-radius: 10px;
    background-color: #343a40; /* Dark background */
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
    color: #e9ecef; /* Light text */
    position: relative; /* Needed for pseudo-elements or absolute positioning if added */
}

.app-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 1px solid #4a4a4a;
}

#bletchley-app h2 {
    text-align: right;
    color: #17a2b8; /* Info color */
    margin: 0;
    font-size: 1.8em;
}

.timer {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 1.5em;
    font-weight: bold;
    color: #ffc107; /* Warning color */
    text-align: left; /* Keep timer left */
    min-width: 60px; /* Prevent layout shift */
}


.card {
    margin-bottom: 20px;
    padding: 15px;
    border: 1px solid #4a4a4a;
    border-radius: 8px;
    background-color: #454d55; /* Slightly lighter dark */
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.2);
}

.card-label {
    font-weight: bold;
    margin-bottom: 10px;
    display: block;
    color: #adb5bd; /* Muted grey */
    font-size: 0.9em;
}

.encrypted-text {
    font-family: 'IBM Plex Mono', monospace;
    white-space: pre-wrap;
    word-break: break-all;
    padding: 15px;
    border: 1px dashed #6c757d; /* Muted dashed border */
    background-color: #3a4047; /* Darker background */
    min-height: 80px;
    color: #ced4da; /* Lighter grey text */
    font-size: 1.1em;
    line-height: 1.6;
    overflow-x: auto; /* Allow horizontal scroll if needed */
    animation: fadeIn 1s ease-out; /* Fade in animation */
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}


.indicator-lights-container {
    display: flex;
    align-items: center;
    margin-bottom: 15px;
    justify-content: center; /* Center lights and text */
}

.light {
    display: inline-block;
    width: 14px; /* Slightly larger */
    height: 14px; /* Slightly larger */
    border-radius: 50%;
    margin: 0 10px;
    background-color: #6c757d; /* Default off color */
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
    transition: background-color 0.5s ease, box-shadow 0.5s ease;
}

.light.working {
    background-color: #ffc107; /* Warning color - Orange */
    box-shadow: 0 0 8px #ffc107;
    animation: pulse 1.5s infinite ease-in-out; /* Pulsing animation */
}

.light.success {
     background-color: #28a745; /* Success color - Green */
     box-shadow: 0 0 8px #28a745;
}

.light.error {
     background-color: #dc3545; /* Danger color - Red */
     box-shadow: 0 0 8px #dc3545;
     animation: shake 0.5s ease-in-out; /* Shake animation */
}

@keyframes pulse {
    0% { box-shadow: 0 0 8px rgba(255, 193, 7, 0.7); }
    50% { box-shadow: 0 0 15px rgba(255, 193, 7, 1); }
    100% { box-shadow: 0 0 8px rgba(255, 193, 7, 0.7); }
}

@keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-5px); }
    75% { transform: translateX(5px); }
}

.status-text {
    color: #ced4da;
    font-size: 1em;
}

.crib-input-area {
    display: flex;
    gap: 10px; /* Space between input and button */
    margin-bottom: 15px;
}

#crib-input {
    flex-grow: 1; /* Allow input to take available space */
    padding: 10px;
    border: 1px solid #6c757d;
    border-radius: 5px;
    background-color: #3a4047; /* Darker background */
    color: #e9ecef;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 1em;
    box-sizing: border-box; /* Include padding and border in element's total width and height */
}

#crib-input::placeholder {
    color: #adb5bd; /* Muted placeholder text */
}

#crib-input:focus {
    outline: none;
    border-color: #17a2b8; /* Highlight color on focus */
    box-shadow: 0 0 5px rgba(23, 162, 184, 0.5);
}


#check-crib-button {
    padding: 10px 20px;
    background-color: #17a2b8; /* Info color */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease, opacity 0.3s ease;
    min-width: 100px; /* Give button a minimum width */
}

#check-crib-button:hover:not(:disabled) {
    background-color: #138496;
}

#check-crib-button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}


.feedback {
    margin-top: 10px;
    padding: 15px;
    border-radius: 5px;
    min-height: 20px;
    font-size: 0.9em;
    border: 1px solid transparent; /* Add border for consistency */
}

.feedback.success {
    background-color: #d4edda; /* Light green background */
    color: #155724; /* Dark green text */
    border-color: #c3e6cb;
}

.feedback.warning {
    background-color: #fff3cd; /* Light yellow background */
    color: #856404; /* Dark yellow text */
    border-color: #ffeeba;
}

.feedback.error {
    background-color: #f8d7da; /* Light red background */
    color: #721c24; /* Dark red text */
    border-color: #f5c6cb;
}

.progress-bar-container {
    width: 100%;
    height: 15px;
    background-color: #6c757d;
    border-radius: 8px;
    overflow: hidden; /* Ensure progress bar stays within bounds */
    margin-bottom: 10px;
}

#progress-bar {
    height: 100%;
    width: 0%; /* Initial width */
    background-color: #28a745; /* Success color */
    border-radius: 8px;
    transition: width 0.5s ease-in-out; /* Smooth width transition */
}

.progress-text {
    text-align: center;
    font-weight: bold;
    color: #ced4da;
    font-size: 1em;
}

#toggle-explanation {
    display: block;
    width: fit-content;
    margin: 20px auto;
    padding: 10px 20px;
    background-color: #6c757d; /* Muted button color */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease;
}

#toggle-explanation:hover {
    background-color: #5a6268;
}

#explanation {
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
    color: #333; /* Dark text for explanation section */
}

#explanation h2, #explanation h3 {
    color: #333;
    margin-top: 15px;
}

#explanation p {
    line-height: 1.6;
    color: #555;
}

@media (max-width: 600px) {
    .app-header {
        flex-direction: column-reverse; /* Timer above title on small screens */
        align-items: flex-start;
    }
    .timer {
         text-align: right; /* Timer right aligned on small screens */
         width: 100%;
         margin-bottom: 10px;
    }
     #bletchley-app h2 {
        width: 100%;
        text-align: center; /* Title centered on small screens */
    }
    .crib-input-area {
        flex-direction: column;
        gap: 10px;
    }
    #crib-input, #check-crib-button {
        width: 100%;
        margin-left: 0;
    }
}
</style>

<button id="toggle-explanation">הצג/הסתר הסבר על בלצ'לי פארק</button>

<div id="explanation" style="display: none;">
    <h2>על בלצ'לי פארק ומפצחי הצפנים</h2>

    <h3>מה היה בלצ'לי פארק ומה היה תפקידו במלחמת העולם השנייה?</h3>
    <p>בלצ'לי פארק היה האחוזה הכפרית באנגליה ששימשה כמרכז העיקרי לפענוח צפנים עבור בריטניה במהלך מלחמת העולם השנייה. תפקידו היה קריטי: ליירט הודעות מוצפנות של מדינות הציר (בעיקר גרמניה הנאצית), לפענח אותן, ולהפוך את המידע הסודי הזה למודיעין שימושי עבור בעלות הברית. הצלחת בלצ'לי פארק קיצרה את המלחמה באופן משמעותי והצילה אינספור חיים.</p>

    <h3>מי היו מפצחי הצפנים והמפענחים (האנשים שמאחורי המכונות)?</h3>
    <p>צוות בלצ'לי פארק כלל אלפי אנשים ממגוון רחב של רקעים, לא רק מתמטיקאים וקריפטוגרפים (כמו אלן טיורינג המפורסם). היו שם בלשנים, שחקני שחמט, מומחי תשבצים, ואפילו פקידות וקלדניות שביצעו עבודה סיזיפית של ניתוח נתונים ותפעול מכונות. הם עבדו במשמרות, תחת לחץ עצום וסודיות מוחלטת, תוך שימוש בכישרון, יצירתיות וכושר המצאה.</p>

    <h3>מה הייתה מכונת האניגמה וכיצד פעלה באופן בסיסי?</h3>
    <p>האניגמה הייתה מכונת הצפנה אלקטרו-מכנית ששימשה את גרמניה הנאצית לתקשורת סודית. היא פעלה באמצעות מערכת של רוטורים מסתובבים ששינו את התמרת כל אות מוקלדת. כל לחיצה על מקש אותה לאות אחרת, אך ההתמרה השתנתה עם כל אות נוספת כשהרוטורים הסתובבו. זה יצר מספר עצום של שילובים אפשריים, מה שהפך את האניגמה לצופן שנחשב בזמנו לבלתי פריץ.</p>

    <h3>מה היו האתגרים בפענוח צפני האניגמה?</h3>
    <p>האתגר הגדול ביותר היה שינוי הגדרות המכונה מדי יום. מפעילי האניגמה היו משנים את סדר הרוטורים, את מיקומם ההתחלתי ואת חיבורי הכבלים בלוח הקדמי. כל שינוי כזה יצר מערכת הצפנה חדשה לגמרי. אתגרים נוספים כללו שגיאות אנוש בהפעלה ו"כפילויות" - מקרים שבהם שתי הודעות או יותר הוצפנו עם אותן הגדרות התחלה, דבר שיכול היה לעזור לפענוח אך לא היה קבוע.</p>

    <h3>כיצד נעשה הפענוח בפועל?</h3>
    <p>הפענוח לא היה רק פריצת המכונה, אלא בעיקר פריצת ההגדרות היומיות. אחת הטכניקות המרכזיות הייתה שימוש ב'עריסות' (Cribs) - ניחוש של קטעי טקסט סבירים שיופיעו בהודעות מסוימות (למשל, "היטלר", "מזג אוויר דו"ח", "אין שינוי מצב"). אם ניתן היה למצוא התאמה בין קטע מהמברק המוצפן לבין העריסה המשוערת בטקסט הפענוח, זה סיפק רמז יקר ערך לגבי ההגדרות ששימשו להצפנה. לשם כך פיתחו בבלצ'לי פארק מכונות כמו ה'בומב' (Bombe), שנועדו לבדוק במהירות מאות ואלפי שילובים אפשריים של הגדרות בהתבסס על ה'עריסות' הללו, ולצמצם את מספר האפשרויות לבדיקה ידנית.</p>

    <h3>מה הייתה ההשפעה של פענוח האניגמה על מהלך המלחמה?</h3>
    <p>המידע שהושג מפענוח האניגמה (שכונה "אולטרה" - Ultra) היה מודיעין חיוני. הוא איפשר לבעלות הברית לדעת מראש על תנועות כוחות, תוכניות צבאיות, התקפות מתוכננות של צוללות בקרב על האוקיינוס האטלנטי, ועוד. המידע הזה איפשר לבעלות הברית לקבל החלטות אסטרטגיות קריטיות, להסיט ספינות ממסלולים מסוכנים, ולתכנן מבצעים התקפיים. ההערכה היא ש"אולטרה" קיצרה את המלחמה בשנתיים או יותר.</p>

    <h3>כיצד נשמר הסוד של בלצ'לי פארק לאחר המלחמה?</h3>
    <p>סוד ההצלחה של בלצ'לי פארק נשמר במשך עשרות שנים לאחר המלחמה. המפענחים חויבו לשמור על שתיקה מוחלטת. הסיבות לכך היו מגוונות: למנוע מברית המועצות (שגם היא הייתה בעלת ברית אך הפכה ליריבה קרה) לדעת על היכולות של בריטניה בפענוח צפנים, לאפשר לבריטניה להמשיך להשתמש בשיטות דומות כנגד צפנים אחרים, ולהגן על אנשי קשר או שיטות איסוף מידע שהיו קשורים בעקיפין לפענוח. הסודיות הוסרה רק בשנות ה-70, מה שאיפשר לעולם לגלות את הסיפור המדהים של בלצ'לי פארק והאנשים שעבדו שם.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const encryptedMessageDiv = document.getElementById('encrypted-message');
    const timerDiv = document.getElementById('timer');
    const statusLight = document.getElementById('status-light');
    const statusText = document.getElementById('status-text');
    const cribInput = document.getElementById('crib-input');
    const checkCribButton = document.getElementById('check-crib-button');
    const feedbackArea = document.getElementById('feedback-area');
    const messageCounterDiv = document.getElementById('message-counter');
    const progressBar = document.getElementById('progress-bar');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    let currentMessageIndex = 0;
    let timerInterval = null;
    let secondsElapsed = 0;
    let isCheckingCrib = false; // Flag to prevent multiple clicks

    // Sample messages and their corresponding plaintexts and potential cribs
    // SIMPLIFICATION: In reality, mapping cribs to encrypted text is complex.
    // Here, we just check if the input matches a *known* crib for the *plaintext*,
    // and simulate the 'search' effort.
    const messages = [
        {
            encrypted: "UIF BTTBVMU JT QMBSSFE GPS UPNPSSPX BU EBXO", // Simple Caesar cipher (shift +1) of the plaintext
            plaintext: "THE ASSAULT IS PLANNED FOR TOMORROW AT DAWN",
            cribs: ["ASSAULT", "PLANNED", "TOMORROW", "DAWN"]
        },
        {
            encrypted: "XB OYJ FQOJ PZYM XAJW PQO", // Simple substitution: W=T, E=H, A=E, R=A, G=R, O=I, I=N, N=G, etc.
            plaintext: "WE ARE GOING WEST AGAIN TODAY",
            cribs: ["WE ARE", "GOING", "WEST", "AGAIN", "TODAY"]
        },
         {
            encrypted: "CNA URN LBEG GRT GUR PYBPX", // ROT13
            plaintext: "ALL YOU NEED IS THE CLOCK",
            cribs: ["ALL YOU NEED", "CLOCK"] // Note: Longer cribs are more powerful
        },
         {
            encrypted: "JVC RTTCEK KP URCRRW DCAF", // Simple substitution
            plaintext: "THE ATTACK IS HIGHLY LIKELY",
            cribs: ["ATTACK", "HIGHLY", "LIKELY"]
        },
        {
            encrypted: "KVZ BQG QVM LBW ZQM KQN JVSZ", // Simple substitution
            plaintext: "ALL SHIPS MUST RETURN TO PORT",
            cribs: ["SHIPS", "RETURN", "PORT"]
        }
    ];

    function startTimer() {
        secondsElapsed = 0;
        timerDiv.textContent = '0:00';
        clearInterval(timerInterval);
        timerInterval = setInterval(() => {
            secondsElapsed++;
            const minutes = Math.floor(secondsElapsed / 60);
            const seconds = secondsElapsed % 60;
            timerDiv.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
        }, 1000);
    }

    function stopTimer() {
        clearInterval(timerInterval);
    }

    function updateProgressBar() {
        const progress = (currentMessageIndex / messages.length) * 100;
        progressBar.style.width = `${progress}%`;
    }

    function loadMessage(index) {
        // Clear previous animations/states
        encryptedMessageDiv.style.animation = '';
        feedbackArea.className = 'feedback';
        feedbackArea.textContent = '';
        cribInput.value = '';
        cribInput.disabled = false;
        checkCribButton.disabled = false;
        isCheckingCrib = false;

        if (index >= messages.length) {
            stopTimer();
            encryptedMessageDiv.textContent = "כל המברקים ליום זה פוענחו! הצלחת במשימה היומית!";
            encryptedMessageDiv.style.animation = 'fadeIn 1s ease-out';
            cribInput.style.display = 'none';
            checkCribButton.style.display = 'none';
            feedbackArea.className = 'feedback success';
            feedbackArea.textContent = 'עבודה מצוינת! תרומתך לפיצוח הצופן היומי הייתה קריטית.';
            statusLight.className = 'light success';
            statusText.textContent = 'משימה הושלמה';
            messageCounterDiv.textContent = `עובדו ${messages.length} מתוך ${messages.length}`;
            updateProgressBar(); // Ensure progress bar is full
            return;
        }

        currentMessageIndex = index;
        encryptedMessageDiv.textContent = messages[index].encrypted;
        // Trigger reflow to restart animation
        void encryptedMessageDiv.offsetWidth;
        encryptedMessageDiv.style.animation = 'fadeIn 1s ease-out';

        messageCounterDiv.textContent = `מברק ${index + 1} מתוך ${messages.length}`;
        updateProgressBar();

        statusLight.className = 'light working';
        statusText.textContent = 'ממתין לעריסה...';


        startTimer();
    }

    function checkCrib() {
        if (isCheckingCrib) return; // Prevent double click
        isCheckingCrib = true;
        cribInput.disabled = true;
        checkCribButton.disabled = true;

        const inputCrib = cribInput.value.trim().toUpperCase();
        feedbackArea.textContent = ''; // Clear previous feedback
        feedbackArea.className = 'feedback';

        if (!inputCrib) {
            feedbackArea.className = 'feedback warning';
            feedbackArea.textContent = 'הזן עריסה (רמז) כדי לבדוק.';
            statusLight.className = 'light working'; // Still waiting
            statusText.textContent = 'הזן עריסה...';
            cribInput.disabled = false;
            checkCribButton.disabled = false;
            isCheckingCrib = false;
            return;
        }

        statusLight.className = 'light working';
        statusText.textContent = 'מריץ בדיקת עריסה...';


        // Simulate the time it takes to run a crib check
        const simulationDelay = 1500; // 1.5 seconds

        setTimeout(() => {
            const currentMessage = messages[currentMessageIndex];
            const plaintext = currentMessage.plaintext.toUpperCase();

            // Check if the input crib is in the list of *known* cribs for this message's plaintext
            const isCorrectCrib = currentMessage.cribs.includes(inputCrib);

            if (isCorrectCrib) {
                // Simulate finding the crib within the encrypted text pattern
                // (This part is highly simplified - in reality, this is the hard part)
                const indexInPlaintext = plaintext.indexOf(inputCrib);
                if (indexInPlaintext !== -1) { // Double check it's actually in the plaintext (should always be if in the cribs list)
                    feedbackArea.className = 'feedback success';
                    feedbackArea.textContent = `נמצאה התאמה פוטנציאלית עבור '${inputCrib}'! רמז חשוב לפענוח. המברק פוענח!`;
                    statusLight.className = 'light success';
                    statusText.textContent = 'התאמה נמצאה!';
                    stopTimer();
                    // Automatically load the next message after a short delay
                    setTimeout(() => {
                        loadMessage(currentMessageIndex + 1);
                    }, 2000); // Wait 2 seconds before loading next message

                } else {
                     // Fallback for logic error - shouldn't happen in this simplified model
                     feedbackArea.className = 'feedback error';
                     feedbackArea.textContent = `שגיאה פנימית: העריסה '${inputCrib}' רשומה אך לא נמצאה בטקסט הגלוי.`;
                     statusLight.className = 'light error';
                     statusText.textContent = 'שגיאת מערכת';
                     cribInput.disabled = false;
                     checkCribButton.disabled = false;
                     isCheckingCrib = false;
                }

            } else {
                // Not a correct crib for THIS message.
                // Provide more nuanced feedback.
                let feedbackText = `'${inputCrib}' לא נמצא כעריסה במברק זה. נסה רמז אחר.`;

                // Optional: Add a check if it's *any* word to give different feedback
                // (Requires a dictionary or similar, simplifying by assuming any non-crib is 'incorrect')
                 feedbackArea.className = 'feedback error';
                 statusLight.className = 'light error';
                 statusText.textContent = 'אין התאמה.';


                feedbackArea.textContent = feedbackText;
                cribInput.disabled = false;
                checkCribButton.disabled = false;
                isCheckingCrib = false;
            }
        }, simulationDelay);
    }

    checkCribButton.addEventListener('click', checkCrib);
    cribInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter' && !isCheckingCrib) {
            checkCrib();
        }
    });

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר על בלצ'לי פארק' : 'הצג/הסתר הסבר על בלצ'לי פארק';
         // Scroll to the explanation section if showing it
         if (!isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth' });
         }
    });


    // Initial load
    loadMessage(currentMessageIndex);
});
</script>