---
title: "חוזים חכמים באת'ריום: הקסם שמאחורי הקוד האוטומטי"
english_slug: smart-contracts-ethereum-how-code-becomes-trusted-intermediary
category: "מדעי המחשב"
tags:
  - את'ריום
  - חוזים חכמים
  - בלוקצ'יין
  - קריפטו
  - Web3
  - קוד
  - ביזור
---
# חוזים חכמים באת'ריום: הקסם שמאחורי הקוד האוטומטי

מה אם יכולתם לחתום על הסכם דיגיטלי שמבטיח שהכסף ישולם רק ברגע שהמוצר הגיע, או שהגישה לשירות תינתן אוטומטית מיד עם התשלום? הסכם שלא דורש עורכי דין, בנקים, או גוף מרכזי אחר שיפקח עליו. הסכם שנאכף על ידי קוד המחשב עצמו, בצורה שקופה, אוטומטית ועמידה לשינויים. נשמע עתידני? זה כאן, וקוראים לזה "חוזה חכם". איך זה עובד באמת? בואו נצלול יחד לסימולציה אינטראקטיבית ונראה את זה קורה בזמן אמת!

<div id="smart-contract-app">
    <h2>🎮 סימולציה: פתיחת תוכן אקסקלוסיבי באמצעות חוזה חכם </h2>
    <p>דמיינו שהמאמר הזה נעול, ורק חוזה חכם יכול לפתוח אותו עבורכם. הנה החוקים הפשוטים של החוזה:</p>

    <div class="contract-zone">
        <div class="contract-icon">📜</div>
        <div class="contract-details">
            <h3>חוזה חכם: "שומר המאמר"</h3>
            <p>📍 <strong>כתובת בסימולציה:</strong> 0xAbCdEf123...</p>
            <p>💰 <strong>דרישת גישה:</strong> שליחת <strong>לפחות 0.1 סימולטבי-את'ר</strong> לכתובת החוזה.</p>
            <p>🔑 <strong>הפעולה האוטומטית:</strong> אם התנאי מתקיים, החוזה פותח גישה למאמר הבלעדי.</p>
        </div>
    </div>

    <div class="user-interaction-zone">
        <div class="wallet-icon">💳</div>
        <div class="user-input">
            <h4>הארנק הדיגיטלי שלכם (סימולציה):</h4>
            <label for="ether-amount">כמה סימולטבי-את'ר תרצו לשלוח לחוזה?</label><br>
            <input type="number" id="ether-amount" value="0.05" step="0.01" min="0.01"> סימולטבי-את'ר <br>
            <button id="send-ether-button">שלח את'ר לחוזה »</button>
        </div>
    </div>

    <div class="simulation-flow-zone">
        <h4>🛣️ מסע העסקה בבלוקצ'יין (סימולציה):</h4>
        <div id="step-sending" class="step">
            <div class="step-icon">📤</div>
            <div class="step-text">1. אתם שולחים את העסקה לרשת...</div>
        </div>
        <div id="step-mining" class="step">
             <div class="step-icon">⛏️</div>
             <div class="step-text">2. כורי רשת מאשרים ומוסיפים לבלוק...</div>
         </div>
        <div id="step-execution" class="step">
             <div class="step-icon">🤖</div>
             <div class="step-text">3. החוזה החכם רץ על ה-EVM...</div>
         </div>
    </div>

    <div id="simulation-result" class="result">
        <!-- תוצאת הסימולציה תופיע כאן -->
    </div>

    <div id="exclusive-article" class="hidden">
        <div class="access-granted">🎉 גישה הוענקה על ידי החוזה! 🎉</div>
        <div class="article-content">
            <h5>מאמר בלעדי: עתיד ה-Web3 ואיך חוזים חכמים משנים את המשחק</h5>
            <p>Web3 מייצג את הדור הבא של האינטרנט, המבוסס על טכנולוגיות מבוזרות כמו בלוקצ'יין. במקום להסתמך על שרתים מרכזיים, Web3 מאפשר למשתמשים שליטה גדולה יותר על הנתונים שלהם ועל האינטראקציות הדיגיטליות שלהם. חוזים חכמים ממלאים תפקיד קריטי באקוסיסטמה זו, ומאפשרים אוטומציה וביזור של שירותים ופלטפורמות...</p>
            <p>[...המשך המאמר הבלעדי ועמוק יותר על EVM, Gas, ואפשרויות מתקדמות...]</p>
             <p>ב-Web3, חוזים חכמים משמשים לבניית יישומים מבוזרים (dApps), ארגונים אוטונומיים (DAOs), שווקי אסימונים (NFTs), ועולמות וירטואליים (Metaverse). הם מספקים שכבת לוגיקה אמינה ואוטומטית מעל תשתית הבלוקצ'יין הבלתי ניתנת לשינוי...</p>
             <p>דוגמאות בולטות לשימוש בחוזים חכמים הן בפלטפורמות DeFi (Decentralized Finance) כמו UniSwap או Aave, שמאפשרות מסחר, הלוואות והשאלות ללא מוסדות פיננסיים מרכזיים. כל הפעולות האלו מנוהלות באמצעות קוד גלוי ושקוף בחוזים חכמים.</p>
        </div>
    </div>
</div>

<button id="toggle-explanation-button"> מה בדיוק קרה כאן? (הסבר מורחב) </button>

<div id="explanation" class="hidden">
    <h2>הסבר מורחב: חוזים חכמים באת'ריום - המהפכה האוטומטית</h2>

    <h3>מהו חוזה חכם (Smart Contract)? מעבר להגדרה היבשה</h3>
    <p>תחשבו על חוזה חכם לא כעל מסמך משפטי משעמם, אלא כעל "סוכן דיגיטלי" שגר על הבלוקצ'יין. מרגע שהוא פורס, הוא לא שוכח, לא משוחד, ולא מתעייף. הוא פשוט יושב שם ומחכה שהתנאים שתוכנתו לתוכו יתקיימו. ברגע שזה קורה, הוא מבצע אוטומטית את הפעולה המתוכננת – מעביר כסף, נותן גישה, מעדכן רישום, הכל לפי הקוד. זו הדרך להפוך הסכמות ל-"Trustless" – אתם לא צריכים לסמוך על הצד השני, רק על הקוד הציבורי בבלוקצ'יין.</p>

    <h3>ניק סאבו והמכונה האוטומטית של העתיד</h3>
    <p>הרעיון המבריק הזה עלה במוחו של הקריפטוגרף ניק סאבו כבר בשנות ה-90, הרבה לפני שהבלוקצ'יין היה מילה מוכרת. הוא דמיין מכונה אוטומטית משוכללת בקנה מידה גלובלי: אתם "מכניסים מטבעות" (שולחים עסקה), המכונה "בודקת" (החוזה בודק את התנאים), ואם עמדתם בדרישות, המכונה "פולטת את המוצר" (החוזה מבצע את הפעולה). את'ריום הוא למעשה מימוש מודרני ועוצמתי של החזון הזה, שמאפשר הרבה יותר מלהוציא פחית שתייה.</p>

    <h3>הבמה של את'ריום: EVM, Gas ואיך הכל רץ</h3>
    <p>את'ריום היא הבלוקצ'יין הפופולרי שהפך את החוזים החכמים למציאות נגישה. דמיינו את ה-**Ethereum Virtual Machine (EVM)** כ"מחשב עולמי" ענק, המשותף לכל המשתתפים ברשת. כשהחוזה החכם שלכם רץ, הוא רץ על ה-EVM הזה. כל צומת ברשת מאמת את הפעולה, מה שמבטיח שכולם מסכימים על התוצאה – שקיפות ואי-שינוי ברמה גבוהה ביותר.</p>
    <p>אבל "ריצה" של קוד דורשת משאבים. כאן נכנס ה-**Gas**. Gas הוא כמו "דלק" שמשלמים עליו באת'ר כדי שהעסקה והפעלת החוזה יתבצעו. זה מונע ניצול לרעה של הרשת (למשל, חוזים שתקועים בלולאה אינסופית) ומתגמל את הכורים (או המאמתים ב-Proof-of-Stake) על עבודתם. ככל שהפעולה מורכבת יותר, היא דורשת יותר Gas.</p>

    <h3>למה זה מדהים? היתרונות בקצרה</h3>
    <ul>
        <li><strong>אוטומציה ללא הפסקה:</strong> אין צורך להתעסק ידנית, החוזה עושה את העבודה לבד ברגע שהתנאים בשלים.</li>
        <li><strong>שקיפות מקסימלית:</strong> הקוד לרוב גלוי לכל, וכל אינטראקציה מתועדת בבלוקצ'יין הציבורי.</li>
        <li><strong>עמידות לצנזורה:</strong> אף גורם יחיד לא יכול לעצור או לשנות חוזה שפרוס על רשת מבוזרת.</li>
        <li><strong>"Trustless":</strong> אתם לא צריכים לסמוך על בן אדם, אלא רק על המכניקה המאומתת של הבלוקצ'יין והקוד הגלוי.</li>
    </ul>

    <h3>הצד השני של המטבע: חשוב להיות מודעים לסיכונים</h3>
    <ul>
        <li><strong>באגים קוד קטלניים:</strong> טעות אחת בקוד לפני הפריסה עלולה לעלות ביוקר (מאות מיליוני דולרים אבדו בעבר מבאגים בחוזים). בגלל שהקוד לרוב בלתי ניתן לשינוי, תיקון הוא אתגר גדול.</li>
        <li><strong>קשה לעדכן (Immutable):</strong> זה יתרון לאמינות, אבל חיסרון כשיש צורך בשיפורים או תיקונים. תכנון מראש קריטי.</li>
        <li><strong>אין מקום לפרשנות:</strong> הקוד הוא החוק. אין "רוח החוק", רק מה שכתוב שחור על גבי לבן (קוד על גבי בלוק).</li>
        <li><strong>עולם משפטי חדש:</strong> איך מתייחסים לחוזה אוטומטי בבית משפט? הרגולציה עדיין מדביקה את הקצב.</li>
    </ul>

    <h3>היכן פוגשים חוזים חכמים היום? (ועוד שימושים מגניבים)</h3>
    <p>חוזים חכמים הם עמוד השדרה של הרבה מההתפתחויות המרגשות בעולם ה-Web3:</p>
    <ul>
        <li><strong>DeFi (מימון מבוזר):</strong> בנקים ללא בנקים, בורסות ללא בורסה מרכזית, הכל באמצעות קוד.</li>
        <li><strong>NFTs (אסימונים ייחודיים):</strong> החוזים החכמים מגדירים את הבעלות והייחודיות של כל פריט דיגיטלי או פיזי המיוצג כאסימון.</li>
        <li><strong>DAOs (ארגונים אוטונומיים):</strong> חברות או פרויקטים שמנוהלים על ידי קוד והצבעות משתמשים, לא מועצת מנהלים מרכזית.</li>
        <li><strong>גיימינג:</strong> בעלות על פריטים במשחק וכללים משחקיים אוטומטיים.</li>
        <li><strong>ניהול זהויות, שרשראות אספקה, הצבעות ועוד...</strong> הפוטנציאל עצום ועדיין נחקר.</li>
    </ul>

    <h3>לסיכום: הסכמים חכמים לעולם מבוזר</h3>
    <p>חוזים חכמים הם הרבה יותר מסתם קוד. הם כלי עוצמתי לבניית אמון במערכות ללא צורך באמון בין צדדים. הם מאפשרים אוטומציה חסרת תקדים, שקיפות ועמידות. למרות הסיכונים והאתגרים, הם מרכיב קריטי בעתיד האינטרנט (Web3) ומשנים את הדרך בה אנו מבצעים עסקאות והסכמים בעולם הדיגיטלי. הסימולציה שראיתם היא הצצה קטנה לאופן שבו הקוד הופך למתווך האמין החדש.</p>

</div>

<script>
    const sendButton = document.getElementById('send-ether-button');
    const etherInput = document.getElementById('ether-amount');
    const stepSending = document.getElementById('step-sending');
    const stepMining = document.getElementById('step-mining');
    const stepExecution = document.getElementById('step-execution');
    const simulationResult = document.getElementById('simulation-result');
    const exclusiveArticle = document.getElementById('exclusive-article');
    const toggleExplanationButton = document.getElementById('toggle-explanation-button');
    const explanationDiv = document.getElementById('explanation');
    const simulationFlowZone = document.querySelector('.simulation-flow-zone');


    const requiredAmount = 0.1; // The contract's price

    // Toggle Explanation Visibility
    toggleExplanationButton.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
        const isHidden = explanationDiv.classList.contains('hidden');
        toggleExplanationButton.textContent = isHidden ? ' מה בדיוק קרה כאן? (הסבר מורחב) ' : ' ⬆️ הסתר הסבר מורחב ⬆️ ';
        toggleExplanationButton.classList.toggle('active-toggle', !isHidden);
    });


    sendButton.addEventListener('click', async () => {
        const amount = parseFloat(etherInput.value);

        // Reset simulation steps and result
        const allSteps = simulationFlowZone.querySelectorAll('.step');
        allSteps.forEach(step => step.classList.remove('active', 'done', 'error'));
        simulationResult.textContent = '';
        simulationResult.className = 'result'; // Reset classes
        exclusiveArticle.classList.add('hidden');
        sendButton.disabled = true; // Disable button during simulation
        sendButton.textContent = 'שולח...';
        simulationResult.classList.remove('success', 'failure'); // Ensure no old result classes

        // --- Simulation Steps with more visual feedback ---

        // Step 1: Sending Transaction
        stepSending.classList.add('active');
        stepSending.querySelector('.step-icon').textContent = '🔄'; // Indicate processing
        await delay(1200); // Simulate network delay

        stepSending.classList.remove('active');
        stepSending.classList.add('done');
        stepSending.querySelector('.step-icon').textContent = '✅'; // Indicate done
        stepMining.classList.add('active');
        stepMining.querySelector('.step-icon').textContent = '⛏️'; // Indicate processing mining

        // Step 2: Mining/Confirmation (Block Creation)
        await delay(2000); // Simulate block confirmation

        stepMining.classList.remove('active');
        stepMining.classList.add('done');
        stepMining.querySelector('.step-icon').textContent = '🧱'; // Indicate block added
        stepExecution.classList.add('active');
         stepExecution.querySelector('.step-icon').textContent = '🤖'; // Indicate processing execution


        // Step 3: Smart Contract Execution
        await delay(1500); // Simulate EVM execution

        stepExecution.classList.remove('active');
        stepExecution.classList.add('done');


        // --- Contract Logic & Results ---

        if (amount >= requiredAmount) {
            stepExecution.querySelector('.step-icon').textContent = '👍'; // Indicate successful execution
            simulationResult.textContent = '✅ העסקה אושרה ע"י החוזה. גישה הוענקה!';
            simulationResult.classList.add('success');
            exclusiveArticle.classList.remove('hidden');
        } else {
             stepExecution.querySelector('.step-icon').textContent = '👎'; // Indicate failed execution
             stepExecution.classList.add('error'); // Optional: highlight error step
            simulationResult.textContent = `❌ עסקה נדחתה ע"י החוזה. נשלח ${amount} פחות מהמינימום הדרוש (${requiredAmount}). הכסף 'הוחזר' או נכשל (תלוי בחוזה, בסימולציה זו - נדחה).`;
            simulationResult.classList.add('failure');
        }

        sendButton.disabled = false; // Re-enable button
        sendButton.textContent = 'שלח את'ר לחוזה »'; // Reset button text
    });

    function delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    // Initialize the explanation as hidden
    explanationDiv.classList.add('hidden');
    toggleExplanationButton.textContent = ' מה בדיוק קרה כאן? (הסבר מורחב) ';
     toggleExplanationButton.classList.remove('active-toggle');


</script>

<style>
    #smart-contract-app {
        direction: rtl;
        font-family: 'Arial', sans-serif; /* More modern font */
        max-width: 750px; /* Slightly wider */
        margin: 30px auto;
        padding: 30px;
        border: none; /* Remove default border */
        border-radius: 12px; /* More rounded corners */
        background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2); /* Soft gradient background */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Deeper shadow */
        color: #333;
    }

    h2 {
        color: #00796b; /* Teal */
        text-align: center;
        margin-bottom: 25px;
        font-size: 2em;
        font-weight: bold;
    }

     h3 {
         color: #004d40; /* Darker Teal */
         margin-top: 0;
         font-size: 1.3em;
     }

    h4 {
        color: #555;
        margin-top: 0;
        font-size: 1.1em;
        margin-bottom: 15px;
    }

    p {
        line-height: 1.7;
        margin-bottom: 15px;
    }


    .contract-zone, .user-interaction-zone, .simulation-flow-zone, .result {
        margin-bottom: 25px;
        padding: 20px;
        border: none;
        border-radius: 10px;
        background-color: #ffffff; /* White background */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08); /* Soft inner shadow */
        display: flex; /* Use flexbox for layout */
        align-items: center; /* Vertically align items */
    }

     .contract-zone .contract-icon,
     .user-interaction-zone .wallet-icon {
         font-size: 3em; /* Larger icons */
         margin-left: 20px; /* Space from text */
         color: #00796b; /* Icon color */
     }

     .contract-zone .contract-details,
     .user-interaction-zone .user-input {
         flex-grow: 1; /* Allow text content to take space */
     }


    .user-input input {
        margin-left: 15px; /* Increased space */
        padding: 10px; /* Larger padding */
        border: 1px solid #b2ebf2; /* Light teal border */
        border-radius: 5px;
        font-size: 1em;
        width: 100px; /* Fixed width for input */
        text-align: center; /* Center text */
    }

    .user-input button {
        padding: 12px 25px; /* More padding */
        background-color: #4caf50; /* Green */
        color: white;
        border: none;
        border-radius: 25px; /* Pill shape */
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transition */
        font-weight: bold;
    }

    .user-input button:hover {
        background-color: #388e3c; /* Darker green */
    }

     .user-input button:active {
         transform: scale(0.98); /* Press effect */
     }

     .user-input button:disabled {
         background-color: #cccccc;
         cursor: not-allowed;
     }

    .simulation-flow-zone {
         display: block; /* Revert to block for list-like flow */
    }

    .simulation-flow-zone h4 {
        display: flex;
        align-items: center;
    }

    .simulation-flow-zone h4 .step-icon {
        font-size: 1.5em;
        margin-left: 10px;
    }


    .simulation-flow-zone .step {
        margin-bottom: 12px; /* More space between steps */
        padding: 12px 15px;
        border: 1px solid #e0e0e0; /* Light grey border */
        border-radius: 8px;
        background-color: #f5f5f5; /* Lighter grey */
        opacity: 0.7; /* Slightly faded when inactive */
        transition: opacity 0.6s ease-in-out, background-color 0.6s ease-in-out, transform 0.3s ease; /* Smoother, longer transition */
        display: flex; /* Flexbox for icon and text */
        align-items: center;
    }

    .simulation-flow-zone .step-icon {
        font-size: 1.5em;
        margin-left: 15px;
        transition: transform 0.5s ease; /* Icon animation */
        color: #757575; /* Grey icon color */
    }

    .simulation-flow-zone .step-text {
        flex-grow: 1;
    }

    .simulation-flow-zone .step.active {
        opacity: 1;
        background-color: #fff9c4; /* Light yellow */
        font-weight: bold;
        border-color: #fbc02d; /* Darker yellow border */
        transform: translateY(-3px); /* Subtle lift effect */
    }

     .simulation-flow-zone .step.active .step-icon {
         animation: pulse 1.5s infinite; /* Pulsing animation for active step */
     }

     @keyframes pulse {
         0% { transform: scale(1); }
         50% { transform: scale(1.1); }
         100% { transform: scale(1); }
     }


     .simulation-flow-zone .step.done {
        background-color: #e8f5e9; /* Light green */
        border-color: #a5d6a7; /* Green border */
        opacity: 1;
        font-weight: normal; /* Reset font weight */
     }

     .simulation-flow-zone .step.done .step-icon {
         transform: rotate(360deg); /* Spin on done */
         color: #4caf50; /* Green icon color */
     }

      .simulation-flow-zone .step.error {
         background-color: #ffebee; /* Light red */
         border-color: #ef9a9a; /* Red border */
         opacity: 1;
      }

       .simulation-flow-zone .step.error .step-icon {
         color: #f44336; /* Red icon color */
       }


    .result {
        font-size: 1.2em; /* Larger font */
        font-weight: bold;
        text-align: center;
        min-height: 50px; /* More space */
        display: flex; /* Center content vertically */
        align-items: center;
        justify-content: center;
        border-radius: 10px;
        opacity: 0; /* Start invisible */
        transform: translateY(20px); /* Start lower */
        transition: opacity 0.8s ease-out, transform 0.8s ease-out; /* Animated appearance */
    }

    .result.success {
        color: #1b5e20; /* Dark green */
        background-color: #e8f5e9;
        border-color: #c8e6c9;
         opacity: 1;
         transform: translateY(0);
    }

    .result.failure {
        color: #b71c1c; /* Dark red */
        background-color: #ffebee;
        border-color: #ffcdd2;
        opacity: 1;
        transform: translateY(0);
    }

    #exclusive-article {
        margin-top: 30px;
        padding: 25px;
        border: 2px dashed #00796b; /* Teal dashed border */
        background-color: #e0f2f7; /* Light blue background */
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        opacity: 0; /* Start invisible */
        transform: scale(0.95); /* Start slightly smaller */
        transition: opacity 0.8s ease-out, transform 0.8s ease-out; /* Animated appearance */
    }

     #exclusive-article:not(.hidden) {
         opacity: 1;
         transform: scale(1);
     }

     .access-granted {
         font-size: 1.5em;
         font-weight: bold;
         text-align: center;
         color: #004d40;
         margin-bottom: 20px;
         animation: bounceIn 1s ease-out; /* Add a bounce animation */
     }

      @keyframes bounceIn {
          0% { transform: scale(0.3); opacity: 0; }
          50% { transform: scale(1.05); opacity: 1; }
          70% { transform: scale(0.9); }
          100% { transform: scale(1); }
      }


     .article-content h5 {
         color: #00796b;
         margin-bottom: 15px;
         font-size: 1.2em;
     }
      .article-content p {
          color: #555;
      }


    .hidden {
        display: none;
    }

    #toggle-explanation-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        background-color: #0277bd; /* Blue */
        color: white;
        border: none;
        border-radius: 25px; /* Pill shape */
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    #toggle-explanation-button:hover {
        background-color: #01579b; /* Darker blue */
    }
     #toggle-explanation-button:active {
         transform: scale(0.98);
     }
     #toggle-explanation-button.active-toggle {
         background-color: #d84315; /* Orange/Red when active */
     }
     #toggle-explanation-button.active-toggle:hover {
         background-color: #bf360c;
     }


     #explanation {
        margin-top: 30px;
        padding: 25px;
        border-top: 1px solid #ddd;
        background-color: #ffffff;
        border-radius: 10px;
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
     }

     #explanation h2, #explanation h3 {
         color: #004d40; /* Dark Teal */
         margin-bottom: 12px;
     }

     #explanation p {
         line-height: 1.7;
         margin-bottom: 15px;
         color: #555;
     }

     #explanation ul {
         margin-bottom: 15px;
         padding-right: 20px; /* Adjust padding for RTL list */
     }

      #explanation li {
          margin-bottom: 8px;
          color: #555;
      }

    /* Responsive adjustments */
    @media (max-width: 600px) {
        #smart-contract-app {
            padding: 20px;
            margin: 20px;
        }

        .contract-zone, .user-interaction-zone, .simulation-flow-zone, .result {
            flex-direction: column; /* Stack elements vertically on small screens */
            align-items: flex-start; /* Align items to start */
        }

        .contract-zone .contract-icon,
        .user-interaction-zone .wallet-icon {
            margin-left: 0;
            margin-bottom: 15px;
        }

        .user-input input {
            margin-left: 0;
            margin-bottom: 15px;
            width: 100%; /* Full width on small screens */
            box-sizing: border-box; /* Include padding and border in width */
        }

        .user-input button {
            width: 100%; /* Full width button */
        }

        .simulation-flow-zone .step {
            flex-direction: row; /* Keep step icon and text side by side */
            align-items: center;
        }
         .simulation-flow-zone .step-icon {
              margin-left: 10px; /* Adjust margin */
         }
    }


</style>
```