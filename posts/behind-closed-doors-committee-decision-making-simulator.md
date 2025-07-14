---
title: "מאחורי הדלתיים הסגורות: סימולטור קבלת החלטות בוועדה"
english_slug: behind-closed-doors-committee-decision-making-simulator
category: "מדעי החברה / מדע המדינה ומדיניות ציבורית"
tags: [קבלת החלטות, מדיניות ציבורית, סימולציה, פסיכולוגיה חברתית, כלכלה התנהגותית, הטיית מסגור]
---
# מאחורי הדלתיים הסגורות: סימולטור קבלת החלטות בוועדה

כיצד מתקבלות החלטות הרות גורל בוועדות ציבוריות? האם הכל מבוסס על עובדות וניתוח קר, או שיש כוחות נסתרים ודינמיקות אנושיות שמשפיעים על הכף? היכנסו לסימולטור הזה וגלו בעצמכם את הדרמה שמאחורי דיוני הוועדות החשובות.

<div id="simulation-area">
    <div id="intro-screen">
        <h2>קבלו החלטה קריטית: עתיד הקרקע המרכזית</h2>
        <p>תרחיש: ועדה ציבורית דנה בהקצאת שטח קרקע יקר ערך במרכז העיר. עומדות על הפרק שתי הצעות מהותיות:</p>
        <ul>
            <li><strong>הצעה א':</strong> הקמת פארק ציבורי גדול, ריאה ירוקה שתשרת את כלל התושבים.</li>
            <li><strong>הצעה ב':</strong> אישור פרויקט בנייה מסחרי ועתיר משרדים, שיניב הכנסות משמעותיות לעירייה וייצר מקומות עבודה.</li>
        </ul>
        <p>תפקידך כיועץ הוא להציג את הנושא בפני חברי הוועדה. הדרך בה תציג את הדברים תשפיע משמעותית על נקודת מבטם ועל החלטתם.</p>

        <div id="user-input">
            <h3>בחרו את אופן הצגת הנושא (ה'מסגור'):</h3>
            <div class="framing-option">
                <input type="radio" id="framing-public" name="framing" value="public" checked>
                <label for="framing-public">
                    <h4>מסגור חברתי-סביבתי</h4>
                    <p>הדגשת התועלת הציבורית, איכות החיים, היבטים אקולוגיים ותרומה לקהילה. (נוטה לתמוך בפארק - הצעה א')</p>
                </label>
            </div>
            <div class="framing-option">
                <input type="radio" id="framing-economic" name="framing" value="economic">
                <label for="framing-economic">
                    <h4>מסגור כלכלי-עסקי</h4>
                    <p>הדגשת התשואה הכלכלית, הכנסות לעירייה, יצירת מקומות עבודה, ויעילות ניצול הקרקע. (נוטה לתמוך בפרויקט המסחרי - הצעה ב')</p>
                </label>
            </div>
            <button id="start-simulation">התחילו את הדיון!</button>
        </div>
    </div>

    <div id="committee-display" style="display: none;">
        <h3>דיון הוועדה יוצא לדרך...</h3>
        <div class="committee-members-grid">
            <!-- Members will be populated and animated here -->
        </div>
        <button id="show-outcome" style="display: none;">צפו בהחלטה</button>
    </div>

    <div id="outcome" style="display: none;">
        <h3>החלטת הוועדה סוכמה:</h3>
        <p id="decision-text"></p>
        <p id="explanation-text"></p>
        <button id="restart-simulation">התחילו סימולציה חדשה</button>
    </div>
</div>

<style>
#simulation-area {
    font-family: 'Heebo', sans-serif; /* Using Heebo for modern look */
    direction: rtl;
    text-align: right;
    border: 1px solid #e0e0e0;
    padding: 30px;
    margin-bottom: 30px;
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}

h2, h3 {
    color: #333;
    border-bottom: 2px solid #f0f0f0;
    padding-bottom: 10px;
    margin-bottom: 20px;
}

#user-input {
    margin-top: 20px;
    padding: 20px;
    background-color: #f8f8f8;
    border-radius: 8px;
}

.framing-option {
    margin-bottom: 15px;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.framing-option:hover {
    background-color: #eef;
    border-color: #cce;
}

.framing-option input[type="radio"] {
    margin-left: 10px;
    transform: scale(1.2);
}

.framing-option label {
    display: inline-block;
    cursor: pointer;
    font-weight: normal;
    color: #555;
}

.framing-option label h4 {
    margin: 0 0 5px 0;
    color: #0056b3;
}

.framing-option label p {
    margin: 0;
    font-size: 0.9em;
    color: #777;
}


button {
    padding: 12px 25px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    margin-top: 15px;
    transition: background-color 0.3s ease, transform 0.1s ease;
    display: block;
    width: fit-content;
    margin-left: auto;
    margin-right: auto;
}

button:hover {
    background-color: #0056b3;
}

button:active {
    transform: scale(0.98);
}

#show-outcome {
     background-color: #28a745; /* Green color for outcome button */
     margin-top: 30px;
}

#show-outcome:hover {
     background-color: #218838;
}

#restart-simulation {
    background-color: #6c757d; /* Gray for restart */
    margin-top: 30px;
}

#restart-simulation:hover {
    background-color: #5a6268;
}


#committee-display {
    margin-top: 30px;
    padding-top: 20px;
    animation: fadeIn 1s ease-out;
}

.committee-members-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); /* Responsive grid */
    gap: 20px;
}


.committee-member {
    display: flex;
    flex-direction: column;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #fdfdfd;
    overflow: hidden; /* Needed for border-radius on children */
    opacity: 0; /* Start hidden for animation */
    transform: translateY(20px); /* Start slightly below for animation */
    animation: slideInUp 0.6s ease-out forwards; /* Animation handled by JS delay */
}

.member-info {
    padding: 15px;
    background-color: #eef; /* Light background for info */
    border-bottom: 1px solid #dde;
}

.member-info h4 {
    margin-top: 0;
    margin-bottom: 5px;
    color: #333;
}

.member-info p {
    margin: 0;
    font-size: 0.9em;
    color: #555;
}

.member-reaction {
    padding: 15px;
    background-color: #fff; /* White background for reaction */
    flex-grow: 1;
    position: relative;
    border-right: 4px solid #007bff; /* Accent border */
    color: #333;
    font-style: italic;
    opacity: 0; /* Start hidden for animation */
    transform: translateX(20px); /* Start slightly right for animation */
    animation: fadeInText 0.8s ease-out forwards; /* Animation handled by JS delay */
}

/* Subtle arrow for reaction */
.member-reaction::before {
    content: "";
    position: absolute;
    right: -8px; /* Position the pointer */
    top: 20px;
    border-top: 8px solid transparent;
    border-bottom: 8px solid transparent;
    border-right: 8px solid #007bff; /* Color of the pointer */
}


#outcome {
    margin-top: 30px;
    padding: 25px;
    border-top: 3px solid #28a745; /* Green accent */
    background-color: #e9f7ef; /* Light green background */
    border-radius: 8px;
    animation: fadeIn 1s ease-out;
}

#outcome h3 {
    margin-top: 0;
    color: #218838; /* Darker green */
    border-bottom-color: #cce;
}

#decision-text {
    font-size: 1.2em;
    font-weight: bold;
    color: #0056b3; /* Blue */
    margin-bottom: 15px;
}

#explanation-text {
    font-size: 1em;
    color: #444;
    line-height: 1.6;
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes slideInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeInText {
    from { opacity: 0; transform: translateX(20px); }
    to { opacity: 1; transform: translateX(0); }
}


/* Explanation Section Styling */
#toggle-explanation {
    display: block;
    width: fit-content;
    margin: 30px auto;
    padding: 12px 25px;
    background-color: #6c757d;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease;
}

#toggle-explanation:hover {
    background-color: #5a6268;
}

#explanation {
    margin-top: 20px;
    padding: 30px;
    border: 1px solid #e0e0e0;
    background-color: #f9f9f9;
    border-radius: 12px;
    direction: rtl;
    text-align: right;
    box-shadow: 0 4px 8px rgba(0,0,0,0.08);
}

#explanation h2, #explanation h3 {
    color: #333;
    margin-bottom: 15px;
    border-bottom: 1px solid #eee;
    padding-bottom: 8px;
}

#explanation p {
    line-height: 1.7;
    margin-bottom: 18px;
    color: #444;
}

#explanation ul {
    margin-bottom: 18px;
    padding-right: 25px;
    color: #444;
}

#explanation li {
    margin-bottom: 10px;
    line-height: 1.6;
}
</style>

<button id="toggle-explanation">גלו מה קרה מאחורי הקלעים: הסבר תיאורטי</button>

<div id="explanation" style="display: none;">
    <h2>הסבר תיאורטי: ניווט במבוך קבלת החלטות בוועדות</h2>

    <p>כפי שחוויתם בסימולטור, קבלת החלטות במדיניות ציבורית אינה תהליך אחיד, שקוף ותמיד רציונלי. היא מושפעת עמוקות לא רק מניתוח אובייקטיבי של נתונים, אלא גם מדינמיקות אנושיות, אינטרסים מגוונים, לחצים חיצוניים, ובעיקר – <strong>הטיית המסגור (Framing Bias)</strong>.</p>

    <h3>הטיית מסגור והשפעתה</h3>
    <p>הטיית מסגור היא הטיה קוגניטיבית שבה אנשים מגיבים לבחירות שונות בהתאם לאופן שבו האפשרויות מוצגות להם – כלומר, ה"מסגרת" או ההקשר שבו המידע מוגש. גם אם הנתונים האובייקטיביים זהים לחלוטין, הצגה שמדגישה היבטים חיוביים מסוימים לעומת אחרים יכולה להוביל להחלטה שונה לחלוטין.</p>
    <p>בסימולטור, הצגת הנושא מנקודת מבט חברתית-סביבתית לעומת נקודת מבט כלכלית-עסקית הדגימה כיצד אותו פרויקט (פארק או מסחרי) יכול להיתפס אחרת לחלוטין בעיני חברי הוועדה, בהתאם להיבטים שהובלטו.</p>

    <h3>למה קבלת החלטות בוועדות מורכבת כל כך?</h3>
    <p>מעבר להטיות קוגניטיביות אישיות, קבלת החלטות קבוצתית בוועדות מוסיפה שכבות נוספות של מורכבות:</p>
    <ul>
        <li>**מגוון אינטרסים ומומחיות:** כל חבר ועדה מגיע עם רקע, ערכים, אינטרסים וקשרים משלו (כלכלנית, סוציולוג, פוליטיקאית, מומחה טכני...). המפגש בין נקודות המבט השונות הכרחי לדיון מעמיק, אך הוא גם מקור טבעי לחילוקי דעות ודחיפת אג'נדות.</li>
        <li>**לחצים פוליטיים וציבוריים:** ועדות ציבוריות פועלות בזירה פוליטית. שיקולים כמו שמירה על תמיכה פוליטית, תגובת הציבור, לחצי לובי וקבוצות אינטרס – כל אלו משפיעים על שיקולי החברים לצד (ולעיתים במקום) הניתוח האובייקטיבי. הפוליטיקאית בסימולטור מדגימה היבט זה.</li>
        <li>**דינמיקה קבוצתית:** בתוך קבוצה יכולות לפעול דינמיקות כמו "חשיבת יחד" (Groupthink), לחץ חברתי לקונפורמיזם, או השפעת יתר של חבר ועדה דומיננטי. גם האופן שבו מנוהל הדיון והאם כל הקולות נשמעים משפיע.</li>
        <li>**מגבלות רציונליות ("רציונליות חסומה"):** גם אם היו מנסים להיות רציונליים לחלוטין, מקבלי החלטות מוגבלים בזמן, בידע זמין, וביכולת עיבוד מידע. לכן, לרוב הם מסתפקים בפתרון "מספק" ולאו דווקא "אופטימלי" (מודל סטיספייסינג).</li>
    </ul>

    <h3>סיכום</h3>
    <p>קבלת החלטות בוועדות ציבוריות היא בבסיסה משחק מורכב של השפעה, שכנוע, ניווט בין אינטרסים שונים, והתמודדות עם מגבלות אנושיות ופוליטיות. הבנת ה"מסגור" של הדיון והדינמיקות המופעלות בתוך הוועדה היא קריטית כדי להבין מדוע החלטות מסוימות מתקבלות, לעיתים בניגוד לניתוח "רציונלי" לכאורה.</p>
</div>

<script>
document.getElementById('start-simulation').addEventListener('click', startSimulation);
document.getElementById('toggle-explanation').addEventListener('click', toggleExplanation);
document.getElementById('show-outcome').addEventListener('click', showOutcome);
document.getElementById('restart-simulation').addEventListener('click', restartSimulation);


const committeeMembersData = [
    { id: 'aviva', name: 'אביבה', role: 'הכלכלנית הפרגמטית', initialLeaning: -0.1, publicFramingEffect: 0.1, economicFramingEffect: -0.4, publicReaction: "הנתונים הסביבתיים מרשימים, אך מה המשמעות הכלכלית ארוכת הטווח? צריך לבחון את יחס עלות-תועלת והכנסות פוטנציאליות לעומק.", economicReaction: "הצגת הנתונים הכלכליים ברורה. חשוב להבטיח את יעילות ההשקעה ואת הסיכונים הפיננסיים הכרוכים בפרויקט."}, // -1 for Commercial, +1 for Park. Leaning is a continuous scale
    { id: 'david', name: 'דוד', role: 'הסוציולוג האכפתי', initialLeaning: 0.4, publicFramingEffect: 0.5, economicFramingEffect: -0.3, publicReaction: "ההצעה הזו תתרום רבות לקהילה, תשפר את איכות החיים ותחזק את הלכידות החברתית. זה נכס יקר ערך לתושבים!", economicReaction: "אני חושש שהדגש על ההיבטים הכלכליים בא על חשבון צרכי התושבים, המרחב הציבורי וההשלכות החברתיות השליליות האפשריות."},
    { id: 'sara', name: 'שרה', role: 'הפוליטיקאית הריאלית', initialLeaning: 0, publicFramingEffect: 0.6, economicFramingEffect: -0.5, publicReaction: "הציבור יאהב את זה! זה פרויקט עם תדמית חיובית ויזכה לתמיכה רחבה. זו השקעה חכמה בעתיד העיר ואזרחיה.", economicReaction: "הפרויקט הזה יביא הכנסות משמעותיות לעירייה, יתרום לצמיחה כלכלית וייצור מקומות עבודה. חשוב לדבר עם הגורמים הרלוונטיים ולקדם אותו במהירות."},
    { id: 'yossi', name: 'יוסי', role: 'המומחה הטכני', initialLeaning: 0, publicFramingEffect: 0.2, economicFramingEffect: -0.2, publicReaction: "מההיבט ההנדסי והסביבתי, הפרויקט נראה בר-ביצוע ועומד בתקנים הנדרשים. האתגרים הטכניים ניתנים לניהול.", economicReaction: "יש לבחון לעומק את התחזיות הכלכליות ואת עלויות התחזוקה והתפעול לאורך זמן. מההיבט הטכני, שני הפרויקטים אפשריים עם הבדלים בפרטים."},
];

let simulationOutcome = null; // To store the result between steps

function startSimulation() {
    const framing = document.querySelector('input[name="framing"]:checked').value;
    const introScreen = document.getElementById('intro-screen');
    const committeeDisplay = document.getElementById('committee-display');
    const membersGrid = committeeDisplay.querySelector('.committee-members-grid');
    const showOutcomeButton = document.getElementById('show-outcome');

    // Hide intro, show committee display
    introScreen.style.display = 'none';
    committeeDisplay.style.display = 'block';
    membersGrid.innerHTML = ''; // Clear previous members
    showOutcomeButton.style.display = 'none';

    let finalLeanings = {};
    let memberReactionsHTML = '';
    let overallExplanationParts = [`הדיון בוועדה התפתח על בסיס ההצגה שהתמקדה ב<strong>${framing === 'public' ? 'תועלת הציבורית והסביבתית (פארק)' : 'תועלת הכלכלית והתשואה (מסחרי)'}</strong>.`];
    let votes = { park: 0, commercial: 0 };
    let memberVoteExplanations = {};

    committeeMembersData.forEach(member => {
        let currentLeaning = member.initialLeaning;
        let reactionText = "";
        let voteExplanation = "";

        if (framing === 'public') {
            currentLeaning += member.publicFramingEffect;
            reactionText = member.publicReaction;
        } else { // framing === 'economic'
            currentLeaning += member.economicFramingEffect;
            reactionText = member.economicReaction;
        }

        // Add some randomness to the final leaning for less predictability
        currentLeaning += (Math.random() - 0.5) * 0.3; // +/- 0.15 randomness

        finalLeanings[member.id] = currentLeaning;

        // Determine vote based on final leaning
        let vote;
        if (currentLeaning > 0.2) { // Threshold for Park
            vote = 'park';
            votes.park++;
            voteExplanation = `נטה משמעותית לכיוון הפארק והצביע בעדו.`;
        } else if (currentLeaning < -0.2) { // Threshold for Commercial
            vote = 'commercial';
            votes.commercial++;
             voteExplanation = `נטה משמעותית לכיוון הפרויקט המסחרי והצביע בעדו.`;
        } else {
            vote = 'abstain';
             voteExplanation = `עמד על הגדר או התמקד בהיבטים טכניים/בחינה נוספת, ונמנע.`;
        }
         memberVoteExplanations[member.id] = `<strong>${member.name}, ${member.role}:</strong> ${voteExplanation}`;


        // Create HTML for member, initially hidden
        memberReactionsHTML += `
            <div class="committee-member" data-member="${member.id}">
                <div class="member-info">
                    <h4>${member.name}</h4>
                    <p>${member.role}</p>
                </div>
                <div class="member-reaction"></div>
            </div>
        `;
    });

    membersGrid.innerHTML = memberReactionsHTML;

    // Animate members appearing and speaking
    const memberElements = membersGrid.querySelectorAll('.committee-member');
    let delay = 0;
    memberElements.forEach((memberEl, index) => {
        const memberId = memberEl.getAttribute('data-member');
        const memberData = committeeMembersData.find(m => m.id === memberId);
        const reactionEl = memberEl.querySelector('.member-reaction');

        // Animate member container
        memberEl.style.animationDelay = `${delay}s`;
        memberEl.style.opacity = 1; // Override initial opacity for animation start

        // Animate reaction text appearing after member container
        setTimeout(() => {
            reactionEl.innerText = memberData.publicReaction; // Use the determined reaction text
            reactionEl.style.animationDelay = '0s'; // Apply text animation immediately after parent appears
            reactionEl.style.opacity = 1; // Override initial opacity for animation start
        }, delay * 1000 + 300); // Small delay after member slide-in

         delay += 1.2; // Delay for the next member

    });

    // Determine final decision after reactions are shown
    let decision = "";
    let outcomeExplanation = "";

    if (votes.park > votes.commercial) {
        decision = "<strong>הוחלט לאשר את הקמת הפארק הציבורי (הצעה א').</strong>";
        outcomeExplanation = `ההצגה שלך, שהדגישה את התועלת ה${framing === 'public' ? 'ציבורית והסביבתית' : 'כלכלית (שייתכן ופורשה כחיובית גם עבור הפארק ע"י חלק מהחברים)'}, הובילה לכך שרוב חברי הוועדה (${votes.park} קולות מול ${votes.commercial}) נטו לתמוך באופציית הפארק.`;
    } else if (votes.commercial > votes.park) {
         decision = "<strong>הוחלט לאשר את פרויקט הבנייה המסחרי (הצעה ב').</strong>";
         outcomeExplanation = `ההצגה שלך, שהדגישה את התועלת ה${framing === 'economic' ? 'כלכלית והתשואה' : 'ציבורית (שלא הספיקה לשכנע את הרוב)'}, הובילה לכך שרוב חברי הוועדה (${votes.commercial} קולות מול ${votes.park}) נטו לתמוך באופציית הפרויקט המסחרי.`;
    } else {
        decision = "<strong>הוועדה הגיעה למבוי סתום. לא התקבלה החלטה.</strong>";
        outcomeExplanation = `למרות הצגתך, הוועדה הייתה חלוקה באופן שווה (${votes.park} בעד פארק, ${votes.commercial} בעד מסחרי) ולא הצליחה להגיע להכרעה. הדבר מדגיש את השפעת האינטרסים השונים וחוסר ההסכמה גם לאחר הצגת הנתונים.`;
    }

    overallExplanationParts.push("להלן כיצד נטו חברי הוועדה והצבעתם:");
     committeeMembersData.forEach(member => {
        overallExplanationParts.push(memberVoteExplanations[member.id]);
     });
    overallExplanationParts.push(outcomeExplanation);

    simulationOutcome = {
        decision: decision,
        explanation: overallExplanationParts.join("<br>") // Use <br> for new lines in HTML
    };


    // Show outcome button after animations complete
    setTimeout(() => {
        showOutcomeButton.style.display = 'block';
    }, delay * 1000 + 500); // Show button shortly after the last reaction animation

}

function showOutcome() {
    const committeeDisplay = document.getElementById('committee-display');
    const outcomeDiv = document.getElementById('outcome');
    const decisionTextEl = document.getElementById('decision-text');
    const explanationTextEl = document.getElementById('explanation-text');

    committeeDisplay.style.display = 'none';
    outcomeDiv.style.display = 'block';

    if (simulationOutcome) {
        decisionTextEl.innerHTML = simulationOutcome.decision;
        explanationTextEl.innerHTML = simulationOutcome.explanation;
    }
}

function restartSimulation() {
     const introScreen = document.getElementById('intro-screen');
     const outcomeDiv = document.getElementById('outcome');

     outcomeDiv.style.display = 'none';
     introScreen.style.display = 'block';
      // Optional: Reset radio button to default
     document.getElementById('framing-public').checked = true;
     simulationOutcome = null;
}


function toggleExplanation() {
    const explanationDiv = document.getElementById('explanation');
    const button = document.getElementById('toggle-explanation');
    if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
        explanationDiv.style.display = 'block';
        button.innerText = 'הסתר הסבר תיאורטי';
         explanationDiv.scrollIntoView({ behavior: 'smooth' }); // Scroll to explanation
    } else {
        explanationDiv.style.display = 'none';
        button.innerText = 'גלו מה קרה מאחורי הקלעים: הסבר תיאורטי';
    }
}

// Initial setup on page load
window.onload = function() {
    document.getElementById('committee-display').style.display = 'none';
    document.getElementById('outcome').style.display = 'none';
    document.getElementById('explanation').style.display = 'none'; // Ensure explanation is hidden initially
}
</script>
```