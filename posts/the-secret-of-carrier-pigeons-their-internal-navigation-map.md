---
title: "קסם הניווט היונתי: גלו את המפה והמצפן הפנימיים"
english_slug: the-secret-of-carrier-pigeons-their-internal-navigation-map
category: "ביולוגיה"
tags: [יוני דואר, ניווט בעלי חיים, ביולוגיה, התנהגות בעלי חיים, חישה, אקולוגיה התנהגותית]
---
# קסם הניווט היונתי: גלו את המפה והמצפן הפנימיים

דמיינו שאתם משוחררים במקום לא מוכר, עשרות או מאות קילומטרים מהבית שלכם, בלי GPS, מפות, או אפילו שלטי דרכים. איך הייתם מוצאים את הדרך חזרה? זו בדיוק החידה המדהימה שפתרו יוני הדואר! במשך שנים, מדענים מנסים לפענח את הסוד: אילו כוחות טבעיים מנחים אותם? הצטרפו אלינו לסימולציה אינטראקטיבית וגלו בעצמכם את המנגנונים המדהימים המאפשרים ליונים לנווט ברחבי העולם.

<div id="simulation-container">
    <div id="map">
        <!-- Map area - can use a background image or stylized div -->
        <div id="home" title="השובך (בית היונה)"></div>
        <canvas id="pigeon-path"></canvas>
        <div id="pigeon"></div>
        <!-- Optional: Add visual cues like sun icon, compass icon overlay if applicable -->
    </div>
    <div id="controls">
        <h3>המסע מתחיל: שחררו יונה</h3>
        <button id="set-start-point-btn">בחרו נקודת שחרור על המפה</button>
        <p id="start-point-text">נקודת שחרור: טרם נבחרה</p>

        <h4>כוחות הטבע: תנאי הסביבה</h4>
        <div class="cues-group">
             <div class="cue-item">
                <input type="checkbox" id="magnetic-field-ok" checked>
                <label for="magnetic-field-ok">שדה מגנטי תקין (מצפן מגנטי פעיל)</label>
             </div>
             <div class="cue-item">
                <input type="checkbox" id="sun-visible" checked>
                <label for="sun-visible">שמש גלויה (מצפן שמש פעיל)</label>
            </div>
             <div class="cue-item">
                <input type="checkbox" id="olfactory-cues-ok" checked>
                <label for="olfactory-cues-ok">ריחות מוכרים זמינים (מפת ריחות פעילה)</label>
             </div>
             <!-- ניתן להוסיף בעתיד: רמזי ראייה, אינפרא-סאונד וכו' -->
        </div>


        <div class="action-buttons">
            <button id="release-pigeon-btn" disabled>שחררו את היונה!</button>
            <button id="reset-simulation-btn">התחילו מחדש</button>
        </div>

        <p id="simulation-status"></p>
    </div>
</div>

<button id="toggle-explanation">מה עומד מאחורי הקסם? לחצו להסבר המדעי המפורט</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מדעי: מפת הניווט והמצפנים הפנימיים של יוני הדואר</h2>

    <h3>המסע המסתורי הביתה: חידת ההומינג</h3>
    יוני דואר, לצד מגוון מרהיב של בעלי חיים נוספים (ציפורים נודדות, צבי ים, דגים, ואפילו חרקים), הם אלופי הניווט. הם מסוגלים למצוא את דרכם חזרה לנקודת המוצא, או להגיע ליעד ספציפי, ממרחקים אדירים ובשטחים שמעולם לא הכירו. היכולת המופלאה הזו נקראת "הומינג" (Homing), והיא אחת התעלומות הגדולות והמרתקות ביותר בחקר התנהגות בעלי חיים. איך הם עושים זאת ללא שום עזרה טכנולוגית חיצונית?

    <h3>המפה והמצפן הפנימיים: המודל המוביל</h3>
    ההסבר המדעי המקובל ליכולת ניווט למרחקים ארוכים מתבסס על מודל "מפה ומצפן". הרעיון פשוט: כדי לנווט, בעל החיים זקוק לשני כלים בסיסיים:
    1.  **מפה פנימית (Map):** הבנה, ברמה קוגניטיבית או חישתית, של מיקומו הנוכחי ביחס ליעד (הבית, במקרה של היונה) ולסביבה הרחבה. זוהי מעין מפה מנטלית או חישתית של האזור.
    2.  **מצפן פנימי (Compass):** כלי המאפשר לקבוע כיוון תנועה (למשל, צפון, דרום-מערב) כדי לנוע בכיוון הנכון על סמך הנתונים מהמפה.
    יוני הדואר, ככל הנראה, לא מסתמכות על כלי אחד בלבד, אלא משלבות מידע ממגוון רחב של חושים ומנגנונים פיזיולוגיים כדי לבנות הן את ה"מפה" והן את ה"מצפן" שלהן.

    <h3>חישת כדור הארץ: המצפן המגנטי</h3>
    כן, יונים מסוגלות לחוש את השדה המגנטי העדין של כדור הארץ! הן משתמשות בחישה מגנטית (Magnetoreception) כמצפן אמין, המאפשר להן לדעת את הכיוון גם כשהשמש אינה נראית (יום מעונן, לילה). המנגנון הביולוגי המדויק עדיין נושא מחקר אינטנסיבי, אך סבורים שהוא כרוך בשילוב של חלבונים רגישים לאור ברשתית העין (אפקט הקוונטי של רדיקלים זוגיים) וייתכן שגם חלקיקי ברזל מגנטיים זעירים באזורים מסוימים בגוף, אולי במקור האף או במוח. עדות חזקה לכך מגיעה מניסויים: הצמדת מגנט קטן לראש היונה משבשת קשות את יכולת הניווט שלה, במיוחד כשהמצפן הסולארי אינו זמין.

    <h3>כוכב הצפון שלהם: ניווט לפי השמש</h3>
    בימים בהירים ושמשיים, יונים יכולות להשתמש במיקום השמש בשמיים כמצפן מדויק להפליא. הן "יודעות" את מסלול השמש היומי - זריחה במזרח, שקיעה במערב - ומיקומה בשמיים בכל שעה נתונה. כדי להשתמש בשמש כמצפן יעיל, הן חייבות לשקלל את השעה ביום, שכן כיוון השמש משתנה כל הזמן. לשם כך, הן נעזרות ב"שעון ביולוגי" פנימי מדויק. השעון הזה מאפשר להן לתקן את כיוון התעופה בהתאם לתנועה הנראית של השמש. ניסויים בהם "הזיזו" ליונים את השעון הביולוגי (למשל, על ידי חשיפה לסידורי אור וחושך מלאכותיים) הראו שגיאות ניווט עקביות הקשורות לכיוון השמש.

    <h3>החוש הסודי: מפת הריחות האווירית</h3>
    עבור רבות מהיונים, במיוחד כשהן לא רחוקות מדי מהבית (בטווח של עשרות עד מאות קילומטרים), חוש הריח ממלא תפקיד קריטי בבניית ה"מפה" הפנימית. ההשערה היא שהיונים לומדות לזהות ולהקשר ריחות שונים (ממפעלים, צמחייה, אדמה) המגיעים ברוח מכיוונים שונים, וליצור מעין "מפת ריחות" של הסביבה. כאשר יונה משוחררת בשטח לא מוכר, היא יכולה לרחרח את האוויר, לזהות ריחות מוכרים, ועל פי עוצמתם והכיוון ממנו הגיעו, להעריך את מיקומה ביחס לבית ולבחור את הכיוון הכללי. פגיעה בחוש הריח של היונה (על ידי חסימת נחיריהן או ניתוק עצבי הריח) פוגעת משמעותית ביכולת ההומינג שלהן, במיוחד בשחרורים הראשונים.

    <h3>עזרה מהסביבה: רמזים נוספים (ראייה, אינפרא-סאונד ועוד)</h3>
    *   **כוחה של הראייה:** ככל שהיונה מתקרבת יותר ויותר לשובך, היא מסתמכת בעיקר על רמזים ויזואליים מוכרים מהנוף - צורת הרים, נהרות, מבנים בולטים, כבישים - כדי למצוא את הדרך המדויקת ביותר לנקודת הנחיתה.
    *   **חישת תת-שמע (אינפרא-סאונד):** ישנן עדויות לכך שיונים מסוגלות לקלוט גלי קול בתדרים נמוכים מאוד (שאינם נשמעים לאוזן אנושית) הנוצרים על ידי תופעות טבע (גלי ים, רוח בהרים, זרמי אוויר). ייתכן שהן משתמשות בצלילים אלו ליצירת 'מפת קול' סביבתית המסייעת בניווט.
    *   **חישת כוח הכבידה:** השערות אחרות מדברות על רגישות לשינויים בכוח הכבידה או בגובה, המשמשים כחלק מהמפה.

    <h3>שילוב כוחות: איך היונה מחברת את הרמזים?</h3>
    סוד ההצלחה של היונה אינו טמון במנגנון בודד, אלא ביכולת המדהימה לשלב ולשקלל מידע מכל החושים והרמזים הללו באופן דינמי וגמיש. היונה בוחרת להסתמך על הרמזים הזמינים והאמינים ביותר בהתאם למרחק שלה מהבית ולתנאי הסביבה באותו רגע. ביום בהיר היא תשתמש בשמש כמצפן עיקרי; ביום מעונן תעבור להסתמך על המצפן המגנטי. בשני המקרים, אם היא נמצאת בטווח הנכון, היא תשתמש גם במפת הריחות כדי לדייק את כיוונה. כשהיא מתקרבת לשובך, הראייה הופכת להיות החוש החשוב ביותר. אם רמז מרכזי משובש או אינו זמין, היונה יכולה לנסות לפצות באמצעות רמזים אחרים, אך הניווט עלול להיות פחות מדויק או יעיל.

    <h3>סיפורים מהמעבדה: מה למדנו מהניסויים?</h3>
    שנים של מחקר באמצעות ניסויים מתוחכמים תמכו במודל המשולב:
    *   שחרור יונים עם מגנטים (המפריעים למצפן המגנטי) משבש ניווט בעיקר ביום מעונן.
    *   "הזזת" השעון הביולוגי גורמת לשגיאות כיוון קבועות בימים שמשיים.
    *   פגיעה בחוש הריח פוגעת ביכולת ההומינג, במיוחד אצל יונים צעירות או בשחרורים ראשונים.
    *   שחרור יונים באזורים עם אנומליות בשדה המגנטי או בסביבה ללא ריחות מוכרים משפיע על התנהגות הניווט שלהן.

    <h3>הפלא שבפנים: מורכבות הניווט היונתי</h3>
    מערכת הניווט של יוני הדואר היא פלא ביולוגי ואבולוציוני. זוהי דוגמה מרתקת לאופן שבו בעלי חיים מפתחים מערכות חישה ועיבוד מידע מורכבות ביותר. היונה היא לא רק "חץ מעופף" אלא נווטת מתוחכמת, המשלבת מידע ממקורות שונים כדי ליצור תמונה פנימית של העולם, המאפשרת לה למצוא את דרכה הביתה כנגד כל הסיכויים. חקר יכולת הניווט של היונים ממשיך לחשוף סודות חדשים ומעמיק את ההבנה שלנו על עולם החושים המופלא של בעלי החיים.
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const map = document.getElementById('map');
        const home = document.getElementById('home');
        const pigeon = document.getElementById('pigeon');
        const canvas = document.getElementById('pigeon-path');
        const ctx = canvas.getContext('2d');
        const setStartPointBtn = document.getElementById('set-start-point-btn');
        const startPointText = document.getElementById('start-point-text');
        const magneticFieldOk = document.getElementById('magnetic-field-ok');
        const sunVisible = document.getElementById('sun-visible');
        const olfactoryCuesOk = document.getElementById('olfactory-cues-ok');
        const releasePigeonBtn = document.getElementById('release-pigeon-btn');
        const resetSimulationBtn = document.getElementById('reset-simulation-btn');
        const simulationStatus = document.getElementById('simulation-status');
        const toggleExplanationBtn = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        let startPoint = null;
        let homePoint = { x: 0, y: 0 }; // Will be calculated based on home div position

        let isSettingStartPoint = false;
        let simulationInterval = null;
        let currentPigeonPos = null;
        const stepSize = 3; // pixels per step (slightly smaller for smoother path)
        const arrivalThreshold = 15; // pixels from home to consider arrived
        const olfactoryThreshold = 180; // Max distance where olfactory cues are significantly useful

        // --- Initial Setup & Positioning ---

        const updateHomePoint = () => {
             const mapRect = map.getBoundingClientRect();
             const homeRect = home.getBoundingClientRect();
             // Calculate home point relative to map's top-left corner
             homePoint = {
                 x: homeRect.left - mapRect.left + homeRect.width / 2,
                 y: homeRect.top - mapRect.top + homeRect.height / 2
             };
        };

        const resizeCanvas = () => {
            const mapRect = map.getBoundingClientRect();
            canvas.width = mapRect.width;
            canvas.height = mapRect.height;
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.strokeStyle = '#4a90e2'; // Path color
            ctx.lineWidth = 2;
            ctx.lineJoin = 'round';
            ctx.lineCap = 'round';

            updateHomePoint(); // Recalculate home position relative to resized map
             // Redraw path if simulation was active (simplified: clear path on resize)
        };

        // Use ResizeObserver for more reliable canvas resizing on div size changes
        const resizeObserver = new ResizeObserver(resizeCanvas);
        resizeObserver.observe(map);

        // Set initial position of home div (can be centered or fixed)
        home.style.left = 'calc(50% - 15px)'; // Center horizontally
        home.style.top = 'calc(50% - 15px)'; // Center vertically
        home.style.width = '30px'; // Make home target slightly larger
        home.style.height = '30px';

        updateHomePoint(); // Calculate initial home point

        // --- Button & Map Event Handlers ---

        toggleExplanationBtn.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            // Simple slide animation using max-height transition
             explanationDiv.style.maxHeight = isHidden ? explanationDiv.scrollHeight + 'px' : '0';
             explanationDiv.style.overflow = 'hidden';
             explanationDiv.style.transition = 'max-height 0.5s ease-in-out';

            // Wait for transition to end before removing max-height for responsiveness
            explanationDiv.addEventListener('transitionend', function handler() {
                if (explanationDiv.style.display !== 'none') {
                    explanationDiv.style.maxHeight = 'none';
                }
                explanationDiv.removeEventListener('transitionend', handler);
            });

            toggleExplanationBtn.textContent = isHidden ? 'הסתר את ההסבר המפורט' : 'מה עומד מאחורי הקסם? לחצו להסבר המדעי המפורט';
        });


        setStartPointBtn.addEventListener('click', () => {
            if (simulationInterval) {
                 simulationStatus.textContent = 'אנא אפס את הסימולציה לפני בחירת נקודה חדשה.';
                 return;
            }
            isSettingStartPoint = true;
            simulationStatus.textContent = 'לחצו על המפה כדי לבחור היכן היונה תשוחרר...';
            map.style.cursor = 'crosshair';
            setStartPointBtn.disabled = true; // Disable while setting
        });

        map.addEventListener('click', (event) => {
            if (isSettingStartPoint) {
                const rect = map.getBoundingClientRect();
                // Calculate point relative to map div
                startPoint = {
                    x: event.clientX - rect.left,
                    y: event.clientY - rect.top
                };

                // Ensure startPoint is within map bounds
                 startPoint.x = Math.max(0, Math.min(map.offsetWidth, startPoint.x));
                 startPoint.y = Math.max(0, Math.min(map.offsetHeight, startPoint.y));


                startPointText.textContent = `נקודת שחרור: כ (${Math.round(startPoint.x)}, ${Math.round(startPoint.y)}) פיקסלים`;
                isSettingStartPoint = false;
                map.style.cursor = 'default';
                releasePigeonBtn.disabled = false; // Enable release button
                setStartPointBtn.disabled = false; // Re-enable set point button

                // Position the pigeon at the start point
                pigeon.style.left = `${startPoint.x - pigeon.offsetWidth / 2}px`;
                pigeon.style.top = `${startPoint.y - pigeon.offsetHeight / 2}px`;
                pigeon.style.display = 'block';

                // Reset and start drawing the path from the new start point
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.beginPath();
                ctx.moveTo(startPoint.x, startPoint.y);
                currentPigeonPos = { ...startPoint }; // Start tracking pigeon position
                 simulationStatus.textContent = 'בחרו תנאי סביבה ולחצו "שחררו את היונה!"';
            }
        });

        releasePigeonBtn.addEventListener('click', () => {
            if (!startPoint || !currentPigeonPos) {
                simulationStatus.textContent = 'אנא בחרו נקודת שחרור על המפה קודם.';
                return;
            }
            if (simulationInterval) {
                 simulationStatus.textContent = 'היונה כבר בדרכה או הגיעה. אנא אפסו.';
                 return;
            }

            simulationStatus.textContent = 'היונה יצאה לדרך... עקבו אחרי מסלולה!';
            releasePigeonBtn.disabled = true; // Disable release once started
            setStartPointBtn.disabled = true; // Disable setting new point during flight

            // Start simulation loop using requestAnimationFrame for smoother animation
            function gameLoop() {
                 simulatePigeonStep();
                 if (simulationInterval !== null) { // Check if simulation is still running
                    requestAnimationFrame(gameLoop);
                 }
            }
            simulationInterval = 'running'; // Use a non-null value to indicate running
            requestAnimationFrame(gameLoop);
        });

        resetSimulationBtn.addEventListener('click', () => {
            // Stop the animation loop correctly
            if (simulationInterval !== null) {
                simulationInterval = null; // Signal loop to stop
            }

            startPoint = null;
            currentPigeonPos = null;
            startPointText.textContent = 'נקודת שחרור: טרם נבחרה';
            releasePigeonBtn.disabled = true;
            setStartPointBtn.disabled = false;
            simulationStatus.textContent = '';
            pigeon.style.display = 'none'; // Hide pigeon
            ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear path
        });

        // --- Simulation Logic (Refined) ---

        function simulatePigeonStep() {
            if (!currentPigeonPos) return; // Should not happen if simulationInterval is set correctly

            const dx = homePoint.x - currentPigeonPos.x;
            const dy = homePoint.y - currentPigeonPos.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            // Check for arrival
            if (distance < arrivalThreshold) {
                simulationInterval = null; // Stop the loop
                simulationStatus.textContent = `מדהים! היונה הגיעה הביתה בהצלחה!`; // More engaging message
                releasePigeonBtn.disabled = true;
                setStartPointBtn.disabled = false;
                // Add final touch like a bounce or color change on pigeon
                pigeon.style.backgroundColor = 'gold'; // Indicate arrival
                return;
            }

            // Determine available cues
            const hasMagnetic = magneticFieldOk.checked;
            const hasSun = sunVisible.checked;
            const hasOlfactory = olfactoryCuesOk.checked;

            let idealAngle = Math.atan2(dy, dx); // The true angle directly towards home
            let effectiveAngle = idealAngle;
            let noiseMagnitude = 0.05; // Base level of random movement/error

            let statusMessage = 'היונה טסה...';

            // Determine base navigation strategy based on compass availability
            if (hasSun) {
                // Use Sun Compass (Primary)
                effectiveAngle = idealAngle; // Assume perfect sun compass for simplicity
                statusMessage = 'היונה טסה (מצפן שמש)...';
                 noiseMagnitude = 0.03; // Very accurate with Sun
            } else if (hasMagnetic) {
                // Use Magnetic Compass (Fallback)
                effectiveAngle = idealAngle; // Assume perfect magnetic compass
                 statusMessage = 'היונה טסה (מצפן מגנטי)...';
                 noiseMagnitude = 0.06; // Slightly less accurate than Sun
            } else {
                // No Compass - impaired navigation
                 effectiveAngle = Math.random() * Math.PI * 2; // Random search pattern
                 statusMessage = 'היונה מבולבלת (אין מצפן)...';
                 noiseMagnitude = 0.5; // High randomness
            }

             // Olfactory cue refinement (more useful closer to home)
            if (hasOlfactory && distance < olfactoryThreshold) {
                 if (!hasSun && !hasMagnetic) {
                     // If no compass, olfactory provides the primary direction closer in
                     effectiveAngle = idealAngle; // Use smell to point towards home
                     statusMessage = 'היונה טסה (מנסה למצוא לפי ריחות)...';
                     noiseMagnitude = 0.15; // Smell is helpful, but not as precise as compass
                 } else {
                     // If a compass is available, olfactory helps refine the direction
                     // Simply reduce noise if olfactory is available and relevant
                     noiseMagnitude *= 0.8; // Olfactory improves accuracy
                      if (!statusMessage.includes('ריחות')) statusMessage = statusMessage.replace(')...', ' + ריחות)...'); // Add olfactory mention
                 }
            } else if (hasOlfactory && distance >= olfactoryThreshold) {
                 // Olfactory cue not useful at long distances, might add confusion if relied upon
                 if (!hasSun && !hasMagnetic) {
                     // If no compass and far, smell doesn't help - high randomness
                     effectiveAngle = Math.random() * Math.PI * 2;
                     statusMessage = 'היונה אבודה (אין מצפן או רמזי ריח)...';
                     noiseMagnitude = 1.0; // Maximum randomness
                 }
            } else if (!hasOlfactory && distance < olfactoryThreshold) {
                 // Close to home, but olfactory (and implied visual) cues are missing/off
                 // Navigation becomes harder to pinpoint home even with compass
                 noiseMagnitude += 0.1; // Added difficulty in final approach
                 if (statusMessage.includes('...')) statusMessage = statusMessage.replace(')...', ' (קשה למצוא את השובך)...');
            }


            // Apply final noise based on calculated magnitude
            const noise = (Math.random() - 0.5) * Math.PI * 2 * noiseMagnitude; // Random angle within noise cone
            const finalAngle = effectiveAngle + noise;


            // Calculate next position based on final angle and step size
            const moveX = stepSize * Math.cos(finalAngle);
            const moveY = stepSize * Math.sin(finalAngle);

            const nextX = currentPigeonPos.x + moveX;
            const nextY = currentPigeonPos.y + moveY;

             // Optional: Bounce off boundaries (simplifies simulation area)
             let bounced = false;
             if (nextX < 0 || nextX > map.offsetWidth) {
                 // Bounce X
                 currentPigeonPos.x = Math.max(0, Math.min(map.offsetWidth, currentPigeonPos.x)); // Clamp to edge
                 // Reverse X direction (simple bounce)
                 const currentAngle = Math.atan2(nextY - currentPigeonPos.y, nextX - currentPigeonPos.x);
                 effectiveAngle = Math.PI - currentAngle; // Reflect angle across Y axis
                 noiseMagnitude = 0.1; // Reset noise after bounce
                 bounced = true;
             }
             if (nextY < 0 || nextY > map.offsetHeight) {
                  // Bounce Y
                  currentPigeonPos.y = Math.max(0, Math.min(map.offsetHeight, currentPigeonPos.y)); // Clamp to edge
                  // Reverse Y direction
                  const currentAngle = Math.atan2(nextY - currentPigeonPos.y, nextX - currentPigeonPos.x);
                  effectiveAngle = -currentAngle; // Reflect angle across X axis
                  noiseMagnitude = 0.1; // Reset noise after bounce
                  bounced = true;
             }

            const finalMoveX = stepSize * Math.cos(effectiveAngle + (bounced ? 0 : noise)); // Reapply noise if not bounced
            const finalMoveY = stepSize * Math.sin(effectiveAngle + (bounced ? 0 : noise));

            const finalNextX = currentPigeonPos.x + finalMoveX;
            const finalNextY = currentPigeonPos.y + finalMoveY;


            // Draw path segment
            ctx.lineTo(finalNextX, finalNextY);
            ctx.stroke();

            // Update pigeon position visually with slight smoothing via CSS transition
            pigeon.style.left = `${finalNextX - pigeon.offsetWidth / 2}px`;
            pigeon.style.top = `${finalNextY - pigeon.offsetHeight / 2}px`;

            // Update current position
            currentPigeonPos.x = finalNextX;
            currentPigeonPos.y = finalNextY;

            // Update status text
            simulationStatus.textContent = statusMessage;
        }

        // --- Initial State Setup ---
        resizeCanvas(); // Set initial size and home position
        // Add initial styles for explanation to allow transition later
         explanationDiv.style.maxHeight = '0';
         explanationDiv.style.overflow = 'hidden';
         explanationDiv.style.transition = 'max-height 0.5s ease-in-out';
         explanationDiv.style.display = 'block'; // Set to block but with 0 max-height

    });
</script>

<style>
    /* הוספנו סגנונות לעיצוב מודרני ואפליקטיבי */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        margin: 0;
        padding: 20px;
        background-color: #eef2f7; /* Light blue background */
    }

    h1, h2, h3, h4 {
        color: #1a3b5d; /* Dark blue heading color */
    }

    #simulation-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px; /* Increased gap */
        margin: 30px auto; /* Center container */
        padding: 30px; /* Increased padding */
        border: none; /* Remove border */
        border-radius: 12px; /* More rounded corners */
        background-color: #ffffff; /* White background */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Soft shadow */
        max-width: 700px; /* Max width for container */
        width: 100%; /* Responsive width */
        box-sizing: border-box; /* Include padding in width */
    }

    #map {
        position: relative;
        width: 100%; /* Make map responsive within container */
        max-width: 500px; /* Max width for map */
        aspect-ratio: 5 / 4; /* Maintain aspect ratio */
        border: 2px solid #1a3b5d; /* Darker border */
        border-radius: 8px;
        background-color: #a8dadc; /* Pleasant map background color */
        overflow: hidden;
        cursor: default; /* Default cursor */
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1); /* Subtle inner shadow */
    }

    /* Placeholder image removed - using background color */
     #map img {
         display: none; /* Hide the placeholder image */
     }


    #pigeon-path {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%; /* Canvas fills map div */
        height: 100%; /* Canvas fills map div */
        pointer-events: none;
        z-index: 5;
        /* Path styling moved to JS for dynamic setting */
    }

    #home {
        position: absolute;
        width: 30px; /* Larger home marker */
        height: 30px;
        background-color: #e63946; /* Red/Orange for home */
        border-radius: 50%; /* Circle */
        z-index: 10;
        border: 3px solid #ffffff; /* White border for visibility */
        box-shadow: 0 0 8px rgba(0,0,0,0.3); /* Shadow for depth */
        /* Positioned using calc in JS for centering */
    }

     #home::after {
        content: '🏠'; /* Home emoji */
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 16px;
        color: #ffffff;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
     }


    #pigeon {
        position: absolute;
        width: 20px; /* Slightly larger pigeon */
        height: 20px;
        background-color: #457b9d; /* Blue-gray for pigeon */
        border-radius: 50%; /* Circle */
        z-index: 10;
        display: none; /* Hidden initially */
        border: 2px solid #ffffff; /* White border */
        box-shadow: 0 0 5px rgba(0,0,0,0.2); /* Shadow */
         /* Smooth transition for movement */
        transition: left 0.05s linear, top 0.05s linear, background-color 0.3s ease;
    }

     #pigeon::after {
        content: '🐦'; /* Bird emoji */
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 12px;
        color: #ffffff;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
     }


    #controls {
        background-color: #f1faee; /* Light green background */
        padding: 20px;
        border-radius: 8px;
        width: 100%; /* Full width within container */
        max-width: 500px; /* Match map max width */
        box-sizing: border-box;
        text-align: center; /* Center align text in controls */
    }

    #controls h3, #controls h4 {
        margin-top: 0;
        margin-bottom: 15px;
        color: #1a3b5d;
    }

    .cues-group {
        display: flex;
        flex-direction: column;
        align-items: flex-start; /* Align checkboxes to the left */
        gap: 10px; /* Space between cue items */
        margin-bottom: 20px;
        padding: 10px;
        background-color: #ffffff; /* White background for cue group */
        border-radius: 5px;
        border: 1px solid #a8dadc; /* Light blue border */
    }

    .cue-item {
        display: flex;
        align-items: center;
    }

    .cue-item input[type="checkbox"] {
        margin-right: 8px;
        accent-color: #457b9d; /* Custom checkbox color */
    }

     .cue-item label {
        font-size: 0.95em;
     }


    #start-point-text {
         font-style: italic;
         margin-bottom: 20px;
         color: #555;
         min-height: 1.2em; /* Reserve space */
    }

    .action-buttons {
        display: flex;
        justify-content: center; /* Center buttons */
        gap: 10px; /* Space between buttons */
        margin-top: 20px;
    }

    #controls button {
        padding: 10px 20px;
        cursor: pointer;
        border: none;
        border-radius: 5px;
        font-size: 1em;
        transition: background-color 0.3s ease, opacity 0.3s ease;
    }

    #set-start-point-btn {
         background-color: #457b9d; /* Blue button */
         color: white;
    }

    #release-pigeon-btn {
        background-color: #e63946; /* Red button for action */
        color: white;
        font-weight: bold;
    }

    #reset-simulation-btn {
        background-color: #a8dadc; /* Light blue button */
        color: #1a3b5d;
    }

     #controls button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.7;
    }

     #controls button:hover:not(:disabled) {
        opacity: 0.9;
     }
      #set-start-point-btn:hover:not(:disabled) { background-color: #3b6a8a; }
      #release-pigeon-btn:hover:not(:disabled) { background-color: #d82b3b; }
      #reset-simulation-btn:hover:not(:disabled) { background-color: #9accd0; }


    #simulation-status {
        margin-top: 15px;
        font-weight: bold;
        color: #1a3b5d;
        min-height: 1.5em; /* Reserve more space */
        text-align: center;
    }


    #toggle-explanation {
        display: block;
        margin: 30px auto; /* Center button */
        padding: 12px 25px;
        font-size: 1em;
        cursor: pointer;
        border: 1px solid #a8dadc;
        border-radius: 5px;
        background-color: #ffffff;
        color: #1a3b5d;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        text-align: center;
         box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }

     #toggle-explanation:hover {
        background-color: #f1faee;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
     }

    #explanation {
        border: none;
        padding: 30px;
        margin: 20px auto;
        border-radius: 12px;
        background-color: #ffffff;
         box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        max-width: 700px; /* Match container width */
        width: 100%;
        box-sizing: border-box;
        /* Initial display handled by JS and CSS max-height transition */
    }

    #explanation h2 {
         text-align: center;
         margin-bottom: 25px;
         color: #1a3b5d;
    }
    #explanation h3 {
        color: #457b9d; /* Blue section titles */
        margin-top: 25px;
        margin-bottom: 12px;
        border-bottom: 1px solid #a8dadc; /* Separator line */
        padding-bottom: 5px;
    }

    #explanation p, #explanation ul {
        margin-bottom: 15px;
        line-height: 1.7;
        color: #555;
    }
    #explanation ul {
        padding-left: 20px;
    }
    #explanation li {
        margin-bottom: 8px;
    }

    /* Responsive adjustments */
    @media (max-width: 600px) {
        #simulation-container, #explanation {
            padding: 20px;
            margin: 20px auto;
        }
         #controls {
            padding: 15px;
         }
        .action-buttons {
            flex-direction: column; /* Stack buttons on small screens */
            gap: 8px;
        }
         .action-buttons button {
             width: 100%; /* Full width buttons */
         }
         #toggle-explanation {
             padding: 10px 20px;
         }
    }

</style>