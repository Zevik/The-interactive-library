---
title: "הקסם שמאחורי הסטופ-מושן: ניצור סרטון משלנו!"
english_slug: the-magic-behind-stop-motion-simulation-creation-process
category: "אמנות ועיצוב / אמנות דיגיטלית"
tags: ["אנימציה", "סטופ מושן", "קולנוע", "יצירה דיגיטלית", "אמנות"]
---
# הקסם שמאחורי הסטופ-מושן: ניצור סרטון משלנו!

ראית פעם דמות שקמה לתחייה מעצמה על המסך, או חפצים שזזים כאילו יש להם רצון משלהם? זה לא קסם, זו אמנות הסטופ-מושן! זו טכניקה מדהימה שהופכת סדרה של תמונות סטטיות לסרטון חי ונושם.

**בואו נצלול פנימה ונדמה את תהליך היצירה הבסיסי בעצמנו – זה כיף יותר ממה שזה נשמע!**

<div class="stop-motion-simulation-container">
    <div class="simulation-area">
        <canvas id="stopMotionCanvas" width="400" height="300"></canvas>
        <div id="hintText" class="hint">גרור את הכדור כדי להתחיל!</div>
    </div>

    <div class="controls">
        <button id="takeFrameBtn"><i class="fas fa-camera"></i> צלם פריים</button>
        <button id="playAnimationBtn" disabled><i class="fas fa-play"></i> הפעל סרטון</button>
        <label for="fpsSelect">מהירות:</label>
        <select id="fpsSelect">
            <option value="6">איטית (6 FPS)</option>
            <option value="12" selected>רגילה (12 FPS)</option>
            <option value="15">קצת מהר יותר (15 FPS)</option>
            <option value="24">חלקה (24 FPS)</option>
        </select>
        <button id="resetBtn"><i class="fas fa-sync-alt"></i> התחל מחדש</button>
    </div>
    <h3>ספריית הפריימים שלך:</h3>
    <div id="frameGallery" class="frame-gallery">
        <!-- Captured frames will appear here -->
        <div class="gallery-placeholder">הפריימים שצלמת יופיעו כאן</div>
    </div>
</div>

<style>
    /* Import Google Font (example: Poppins) - need to verify if external fonts are allowed or rely on system fonts */
    /* @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap'); */
    /* Using system fonts with good fallbacks */

    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
        background-color: #f0f2f5; /* Soft background */
        color: #333;
        line-height: 1.6;
    }

    h1 {
        text-align: center;
        color: #2c3e50; /* Dark blue-gray */
        margin-bottom: 30px;
        font-size: 2.5em;
        font-weight: 600;
    }

    .stop-motion-simulation-container {
        max-width: 650px; /* Slightly wider */
        margin: 40px auto;
        padding: 30px;
        background: linear-gradient(135deg, #ffffff, #f0f8ff); /* Subtle gradient */
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15); /* Deeper shadow */
        text-align: center;
        direction: rtl; /* Ensure RTL layout */
    }

    .simulation-area {
        position: relative; /* Needed for absolute positioning of hint */
        margin-bottom: 20px;
    }

    #stopMotionCanvas {
        display: block;
        margin: 0 auto;
        background-color: #fff;
        border: 2px solid #ced4da; /* Subtle border */
        border-radius: 8px;
        cursor: grab;
        transition: border-color 0.3s ease; /* Smooth transition */
    }

     #stopMotionCanvas:active {
        cursor: grabbing;
        border-color: #007bff; /* Highlight on active drag */
    }

    #stopMotionCanvas.flash { /* Animation for frame capture */
        animation: flash 0.3s ease-out;
    }

    @keyframes flash {
        0% { opacity: 1; }
        50% { opacity: 0.8; background-color: rgba(255, 255, 255, 0.5); }
        100% { opacity: 1; background-color: #fff; }
    }

    .hint {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: rgba(0, 123, 255, 0.9); /* Blue hint background */
        color: white;
        padding: 10px 15px;
        border-radius: 6px;
        font-size: 1.1em;
        font-weight: 600;
        pointer-events: none; /* Allow clicks/drags through the hint */
        opacity: 0; /* Start hidden */
        transition: opacity 0.3s ease, transform 0.3s ease;
         z-index: 10; /* Make sure hint is on top */
         white-space: nowrap; /* Prevent wrapping */
    }

    .hint.visible {
        opacity: 1;
        transform: translate(-50%, -50%) translateY(-10px); /* Slight float effect */
    }


    .controls {
        margin: 25px 0;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px; /* Increased gap */
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .controls button, .controls select {
        padding: 10px 20px; /* More padding */
        font-size: 1em;
        cursor: pointer;
        border: none; /* No default border */
        border-radius: 5px;
        transition: background-color 0.2s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        display: flex; /* Align icon and text */
        align-items: center;
        gap: 5px;
    }

    .controls button:active {
        transform: scale(0.98); /* Subtle press effect */
    }

    #takeFrameBtn {
        background-color: #28a745; /* Green for capture */
        color: white;
    }

    #takeFrameBtn:hover:not(:disabled) {
        background-color: #218838;
    }

    #playAnimationBtn {
        background-color: #007bff; /* Blue for play */
        color: white;
    }

    #playAnimationBtn:hover:not(:disabled) {
        background-color: #0056b3;
    }

     #resetBtn {
        background-color: #dc3545; /* Red for reset */
        color: white;
     }

    #resetBtn:hover:not(:disabled) {
        background-color: #c82333;
    }


    .controls select {
        background-color: #e9ecef; /* Light gray */
        border: 1px solid #ced4da;
        color: #495057;
    }

    .controls button:disabled, .controls select:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        box-shadow: none;
    }

    h3 {
        color: #555;
        margin-top: 25px;
        margin-bottom: 15px;
        font-size: 1.3em;
        font-weight: 600;
        text-align: right;
    }

    .frame-gallery {
        margin-top: 15px;
        border-top: 1px dashed #ced4da; /* Dashed border */
        padding-top: 20px; /* More space */
        min-height: 80px; /* More vertical space */
        display: flex;
        flex-wrap: wrap;
        gap: 8px; /* Increased gap */
        justify-content: center;
        background-color: #e9ecef; /* Light background for gallery */
        border-radius: 8px;
        padding: 15px;
    }

    .gallery-placeholder {
        color: #888;
        font-style: italic;
        text-align: center;
        width: 100%; /* Take full width */
        margin-top: 10px;
    }

    .frame-gallery img {
        width: 60px; /* Slightly larger thumbnails */
        height: auto;
        border: 2px solid #ddd;
        border-radius: 4px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .frame-gallery img:hover {
         transform: translateY(-3px); /* Subtle lift on hover */
         border-color: #007bff;
    }

     .frame-gallery img.active-frame { /* Highlight currently playing frame */
        border-color: #ffc107; /* Yellow highlight */
        box-shadow: 0 0 10px rgba(255, 193, 7, 0.5);
     }


    #toggleExplanationBtn {
        display: block;
        margin: 40px auto 20px; /* More vertical space */
        padding: 12px 25px; /* More padding */
        font-size: 1.1em;
        cursor: pointer;
        background-color: #6c757d; /* Gray button */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.2s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    #toggleExplanationBtn:hover {
        background-color: #5a6268;
    }
     #toggleExplanationBtn:active {
        transform: scale(0.98);
    }


    #explanationContent {
        max-width: 700px;
        margin: 20px auto;
        padding: 30px; /* More padding */
        border: 1px solid #ced4da; /* Match canvas border */
        border-radius: 8px;
        background-color: #e9ecef; /* Light background */
        text-align: right; /* Align text right for Hebrew */
        direction: rtl; /* Set direction to right-to-left */
        box-shadow: 0 5px 15px rgba(0,0,0,0.08); /* Subtle shadow */
         line-height: 1.7; /* Increased line height */
    }
    #explanationContent h2, #explanationContent h3 {
        color: #2c3e50; /* Dark blue-gray */
        border-bottom: 2px solid #a0b4c8; /* Thicker, colored border */
        padding-bottom: 8px; /* More space */
        margin-top: 25px; /* More space above */
        margin-bottom: 15px;
         font-weight: 600;
    }
    #explanationContent p {
        margin-bottom: 18px; /* More space below paragraphs */
    }
    #explanationContent ul {
        list-style: disc inside;
        padding-right: 25px; /* Adjust padding for RTL list */
        margin-bottom: 18px;
    }
    #explanationContent li {
        margin-bottom: 10px; /* More space between list items */
    }

    /* Add Font Awesome (for icons) - assume it's loaded globally or add link if allowed */
    /* If not allowed, remove <i class="fas fa-..."> and gaps */
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');

</style>

<button id="toggleExplanationBtn">הצג/הסתר הסבר מפורט על סטופ-מושן</button>

<div id="explanationContent" style="display: none;">
    <h2>מהי אנימציית סטופ-מושן?</h2>
    <p>סטופ-מושן היא טכניקת אנימציה שבה אובייקט פיזי (בובה, חפץ, ציור וכו') מזיז באופן ידני ופיזי במרווחים קטנים מאוד בין צילום של פריים אחד למשנהו. כל תמונה היא רק "תמונה קפואה" של רגע אחד. כשהפריימים הללו מוקרנים ברצף ובמהירות (בדרך כלל 12 עד 24 תמונות בשנייה), המוח שלנו "משלים" את הפערים ונוצרת אשליית התנועה הרציפה והחלקה, כאילו האובייקט קם לתחייה!</p>

    <h3>העיקרון המרכזי: לצלם פריים אחר פריים לאחר שינוי מינימלי</h3>
    <p>הליבה של הסטופ-מושן פשוטה להפליא, אך דורשת המון סבלנות ודיוק:
    <ol>
        <li>**הכנה:** בוחרים או יוצרים את האובייקט (בובה, כדור, יצור מחימר) ובוחרים את "הסט" - הרקע עליו הוא ינוע.</li>
        <li>**מיקום ראשוני:** מניחים את האובייקט בנקודת ההתחלה שלו ומצלמים את התמונה הראשונה (הפריים הראשון). **קריטי שהמצלמה תהיה מקובעת לחלוטין!**</li>
        <li>**הזזה עדינה:** מזיזים את האובייקט קצת מאוד מאוד - שינוי קטן בשבריר מילימטר או בזווית קטנה. ככל שהשינוי בין פריים לפריים קטן ועקבי יותר, התנועה שתיווצר תהיה חלקה וטבעית יותר.</li>
        <li>**צילום הפריים הבא:** מצלמים את התמונה החדשה לאחר ההזזה העדינה.</li>
        <li>**חוזרים על התהליך... הרבה!** לכל שנייה אחת של אנימציה נדרשים בדרך כלל 12 עד 24 פריימים (תמונות). סרטון סטופ-מושן באורך כמה דקות יכול לדרוש צילום של אלפי תמונות בודדות! זו עבודה סיזיפית אך מתגמלת.</li>
    </ol>
    </p>

    <h3>חשיבות מספר הפריימים לשנייה (FPS) על חלקות התנועה</h3>
    <p>מספר הפריימים לשנייה (Frames Per Second - FPS) קובע כמה תמונות שונות יופיעו על המסך בכל שנייה של וידאו. זה משפיע ישירות על התחושה של התנועה:
    <ul>
        <li>**FPS נמוך (למשל 6-12):** יוצר תחושה "קופצנית" או מקוטעת יותר. זה יכול להיות אפקט אמנותי מכוון, כמו באנימציות קלאסיות מסוימות או כדי לחסוך זמן ומאמץ.</li>
        <li>**FPS גבוה (למשל 24):** יוצר תנועה חלקה ורציפה שנראית קרובה יותר לתנועה "אמיתית" או לסרט קולנוע רגיל. זה דורש כמובן הרבה יותר פריימים לצלם.</li>
    </ul>
    בסימולציה שלנו תוכלו לשחק עם הגדרת ה-FPS ולראות איך היא משפיעה על הסרטון שלכם!</p>

    <h3>סוגים שונים ומרתקים של סטופ-מושן</h3>
    <p>אמנות הסטופ-מושן כוללת מגוון רחב של טכניקות וחומרים:</p>
    <ul>
        <li>**בובות מפרקיות (Puppet Animation):** שימוש בבובות מיוחדות בעלות שלד פנימי גמיש המאפשר הזזה מדויקת של כל איבר. דוגמאות מפורסמות: "הסיוט לפני חג המולד", "קורליין".</li>
        <li>**אנימציית חפצים (Object Animation):** שימוש בכל חפץ שאינו בובה: צעצועים, כלי מטבח, רהיטים קטנים - כל דבר שאפשר להזיז.</li>
        <li>**אנימציית חימר (Claymation):** יצירת דמויות ואובייקטים מחומר גמיש כמו פלסטלינה או חימר, שצורתם משתנה בין פריים לפריים. דוגמאות אהובות: סרטי "וולאס וגרומיט", "עופות בסכנה".</li>
        <li>**אנימציית Cutout:** יצירת דמויות מנייר, קרטון או חומר שטוח אחר, שחלקיהן נעים על משטח שטוח. הפרקים הראשונים של "סאות' פארק" נוצרו בטכניקה זו.</li>
        <li>**אנימציית פיקסלציה (Pixilation):** טכניקת סטופ-מושן המשתמשת באנשים אמיתיים כ"בובות"! האנשים זזים מעט בין צילום פריים לפריים, ויוצרים אשליה של תנועה קופצנית וסוריאליסטית.</li>
    </ul>

    <h3>דוגמאות מפורסמות מההיסטוריה ומהקולנוע המודרני</h3>
    <p>סטופ-מושן היא טכניקה ותיקה שקיימת כמעט מראשית ימי הקולנוע. חלוצים כמו ריי האריהאוזן יצרו איתה מפלצות ויצורים מיתולוגיים ש"קמו לתחייה" על המסך בסרטים כמו "ג'ייסון ושדי הזהב". כיום, אולפני לייקה (Laika) ממשיכים את המסורת ויוצרים סרטי אנימציה קסומים ושובי לב בטכניקות סטופ-מושן מתקדמות, בשילוב טכנולוגיות חדשות (כמו הדפסת תלת-ממד לפנים של הדמויות), לדוגמה בסרטים "קובו ושני המיתרים" ו"מיסטר לינק".</p>

    <p>אז עכשיו כשאתם מבינים קצת יותר מה קורה מאחורי הקלעים, חזרו לחלון הסימולציה ושחקו עם הכדור! צלמו פריימים, הזיזו אותו קצת, וצרו סרטון סטופ-מושן משלכם. תתפלאו כמה כיף ליצור תנועה מכלום!</p>
</div>

<script>
    const canvas = document.getElementById('stopMotionCanvas');
    const ctx = canvas.getContext('2d');
    const takeFrameBtn = document.getElementById('takeFrameBtn');
    const playAnimationBtn = document.getElementById('playAnimationBtn');
    const fpsSelect = document.getElementById('fpsSelect');
    const frameGallery = document.getElementById('frameGallery');
    const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
    const explanationContent = document.getElementById('explanationContent');
    const resetBtn = document.getElementById('resetBtn'); // Added reset button
    const hintText = document.getElementById('hintText'); // Added hint element
    const galleryPlaceholder = frameGallery.querySelector('.gallery-placeholder'); // Get placeholder

    // Ball state
    let ball = { x: canvas.width / 2, y: canvas.height / 2, radius: 20, color: '#ff6347' }; // Tomato red color
    let isDragging = false;
    let dragOffsetX, dragOffsetY;

    // Animation state
    let frames = []; // Stores { imageDataUrl, ballPosition: {x, y} }
    let animationInterval = null;
    let currentFrameIndex = 0;

    // Hint state
    let currentHint = 'drag'; // 'drag', 'take_frame', 'move_and_take', 'play'

    // --- Drawing Functions ---

    // Draw the background (optional, if canvas clear isn't enough)
    function drawBackground() {
        ctx.fillStyle = '#ffffff'; // White background
        ctx.fillRect(0, 0, canvas.width, canvas.height);
    }

     // Draw onion skin (previous frame)
    function drawOnionSkin() {
        if (frames.length > 0) {
            const lastFrameDataUrl = frames[frames.length - 1].imageDataUrl;
             const lastBallPos = frames[frames.length - 1].ballPosition; // Get captured position
            const img = new Image();
            img.onload = () => {
                 // Instead of drawing the *image* of the previous frame,
                 // let's draw a faint ball at the previous position for better 'onion skin' feel
                 ctx.globalAlpha = 0.4; // Make it semi-transparent
                 ctx.beginPath();
                 ctx.arc(lastBallPos.x, lastBallPos.y, ball.radius, 0, Math.PI * 2);
                 ctx.fillStyle = '#ffcccb'; // Light red for onion skin
                 ctx.fill();
                 ctx.closePath();
                 ctx.globalAlpha = 1.0; // Reset alpha
            };
            // img.src = lastFrameDataUrl; // We don't need the full image for this type of onion skin
             // No need to set img.src if we just draw the ball
        }
    }


    // Draw the ball
    function drawBall() {
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear entire canvas
        drawBackground(); // Redraw background
        drawOnionSkin(); // Draw onion skin BEFORE the current ball
        ctx.beginPath();
        ctx.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2);
        ctx.fillStyle = ball.color;
        ctx.fill();
        ctx.closePath();
    }

    // Redraw current frame during animation playback
    function drawAnimationFrame(frameDataUrl) {
         ctx.clearRect(0, 0, canvas.width, canvas.height);
         drawBackground();
         const frameImg = new Image();
         frameImg.onload = () => {
             ctx.drawImage(frameImg, 0, 0, canvas.width, canvas.height);
         };
         frameImg.src = frameDataUrl;
    }


    // --- Event Handlers ---

    // Handle mouse events for dragging
    canvas.addEventListener('mousedown', (e) => {
        const rect = canvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;

        const dist = Math.sqrt((mouseX - ball.x) ** 2 + (mouseY - ball.y) ** 2);

        if (dist < ball.radius) {
            isDragging = true;
            canvas.style.cursor = 'grabbing';
            dragOffsetX = mouseX - ball.x;
            dragOffsetY = mouseY - ball.y;
             updateHint('take_frame'); // Update hint after successful drag
        }
    });

    canvas.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        const rect = canvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;

        // Update ball position
        ball.x = mouseX - dragOffsetX;
        ball.y = mouseY - dragOffsetY;

        // Keep ball within canvas bounds
        ball.x = Math.max(ball.radius, Math.min(canvas.width - ball.radius, ball.x));
        ball.y = Math.max(ball.radius, Math.min(canvas.height - ball.radius, ball.y));

        drawBall(); // Redraw with new position
    });

    canvas.addEventListener('mouseup', () => {
        if (isDragging) {
           isDragging = false;
           canvas.style.cursor = 'grab';
            // drawBall(); // Redraw one last time to ensure correct position after drag end
        }
    });

    canvas.addEventListener('mouseleave', () => {
        isDragging = false; // Stop dragging if mouse leaves canvas
        canvas.style.cursor = 'grab';
    });

    // Touch events for dragging on mobile - Refined
     canvas.addEventListener('touchstart', (e) => {
        if (e.touches.length === 1) { // Only handle single touch
            const rect = canvas.getBoundingClientRect();
            const touchX = e.touches[0].clientX - rect.left;
            const touchY = e.touches[0].clientY - rect.top;

            const dist = Math.sqrt((touchX - ball.x) ** 2 + (touchY - ball.y) ** 2);

            if (dist < ball.radius + 10) { // Give a little more touch tolerance
                isDragging = true;
                // canvas.style.cursor = 'grabbing'; // Doesn't show on mobile but good practice
                dragOffsetX = touchX - ball.x;
                dragOffsetY = touchY - ball.y;
                e.preventDefault(); // Prevent scrolling/zooming
                updateHint('take_frame'); // Update hint
            }
        }
    });

    canvas.addEventListener('touchmove', (e) => {
        if (!isDragging || e.touches.length !== 1) return;
        const rect = canvas.getBoundingClientRect();
        const touchX = e.touches[0].clientX - rect.left;
        const touchY = e.touches[0].clientY - rect.top;

        ball.x = touchX - dragOffsetX;
        ball.y = touchY - dragOffsetY;

        // Keep ball within canvas bounds
        ball.x = Math.max(ball.radius, Math.min(canvas.width - ball.radius, ball.x));
        ball.y = Math.max(ball.radius, Math.min(canvas.height - ball.radius, ball.y));

        drawBall();
        e.preventDefault(); // Prevent scrolling
    });

    canvas.addEventListener('touchend', () => {
        if (isDragging) {
            isDragging = false;
            // canvas.style.cursor = 'grab'; // Doesn't show on mobile
            // drawBall(); // Redraw one last time
        }
    });
    canvas.addEventListener('touchcancel', () => { // Handle interruption
         if (isDragging) {
            isDragging = false;
            // canvas.style.cursor = 'grab';
         }
    });


    // Take a frame button click
    takeFrameBtn.addEventListener('click', () => {
         if (animationInterval) return; // Prevent capturing while animating

        // Trigger canvas flash animation (CSS)
        canvas.classList.add('flash');
        canvas.addEventListener('animationend', () => {
            canvas.classList.remove('flash');
        }, { once: true }); // Remove listener after one run

        const frameDataUrl = canvas.toDataURL('image/png');
        // Store both image and ball position
        frames.push({
            imageDataUrl: frameDataUrl,
            ballPosition: { x: ball.x, y: ball.y }
        });

        // Add frame thumbnail to gallery with animation
        const frameImg = document.createElement('img');
        frameImg.src = frameDataUrl;
        frameImg.style.opacity = 0; // Start faded out
        frameGallery.appendChild(frameImg);
        galleryPlaceholder.style.display = 'none'; // Hide placeholder if frames exist

        // Fade in the thumbnail
        setTimeout(() => {
            frameImg.style.transition = 'opacity 0.5s ease';
            frameImg.style.opacity = 1;
        }, 10); // Small delay to allow element to be added

        // Enable play button if enough frames
        if (frames.length > 1) {
            playAnimationBtn.disabled = false;
            updateHint('play'); // Update hint
        } else {
             updateHint('move_and_take'); // Hint to take another frame
        }

        // Optional: slightly change ball color after taking a frame for visual feedback (less intrusive than random)
         ball.color = `hsl(${frames.length * 40 % 360}, 70%, 50%)`;
         drawBall(); // Redraw with new color and onion skin
    });

    // Play the animation button click
    playAnimationBtn.addEventListener('click', () => {
        if (frames.length < 2 || animationInterval) return;

        // Disable controls during playback
        playAnimationBtn.disabled = true;
        takeFrameBtn.disabled = true;
        fpsSelect.disabled = true;
        resetBtn.disabled = true;
        updateHint(''); // Hide hints during playback

        const fps = parseInt(fpsSelect.value, 10);
        const frameDelay = 1000 / fps; // milliseconds per frame
        currentFrameIndex = 0;

        // Remove active highlight from previous playback (if any)
        frameGallery.querySelectorAll('img.active-frame').forEach(img => img.classList.remove('active-frame'));


        animationInterval = setInterval(() => {
            if (currentFrameIndex < frames.length) {
                // Highlight the current frame thumbnail
                if (currentFrameIndex > 0) {
                    frameGallery.children[currentFrameIndex - 1].classList.remove('active-frame');
                }
                 if (frameGallery.children[currentFrameIndex]) { // Check if element exists
                    frameGallery.children[currentFrameIndex].classList.add('active-frame');
                 }


                // Draw the frame onto the canvas
                drawAnimationFrame(frames[currentFrameIndex].imageDataUrl);

                currentFrameIndex++;
            } else {
                // Animation finished
                clearInterval(animationInterval);
                animationInterval = null;

                // Re-enable controls
                playAnimationBtn.disabled = false;
                takeFrameBtn.disabled = false;
                 fpsSelect.disabled = false;
                 resetBtn.disabled = false;

                 // Remove final highlight
                 if (frameGallery.children[currentFrameIndex - 1]) {
                    frameGallery.children[currentFrameIndex - 1].classList.remove('active-frame');
                 }

                 // Redraw the final state (the current ball position for continued interaction)
                 drawBall();
                 updateHint('play'); // Show play hint again, or maybe 'move_and_take'
            }
        }, frameDelay);
    });

    // Reset button click
    resetBtn.addEventListener('click', () => {
         if (animationInterval) { // Stop animation if running
            clearInterval(animationInterval);
            animationInterval = null;
         }

        // Clear frames array and gallery
        frames = [];
        frameGallery.innerHTML = ''; // Clear all thumbnails
        frameGallery.appendChild(galleryPlaceholder); // Bring back placeholder
        galleryPlaceholder.style.display = 'block';

        // Reset ball position and color
        ball.x = canvas.width / 2;
        ball.y = canvas.height / 2;
        ball.color = '#ff6347';

        // Redraw canvas to initial state
        drawBall();

        // Disable play button
        playAnimationBtn.disabled = true;
         takeFrameBtn.disabled = false; // Enable take frame
         fpsSelect.disabled = false; // Enable fps select
         resetBtn.disabled = false; // Keep reset enabled

         updateHint('drag'); // Restart hint sequence
    });


    // Toggle explanation visibility
    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationContent.style.display === 'none';
        explanationContent.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מפורט' : 'הצג/הסתר הסבר מפורט על סטופ-מושן';
        // Scroll to explanation if shown? Optional
        if (isHidden) {
             explanationContent.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

    // --- Hint Logic ---
    function updateHint(state) {
        currentHint = state;
        hintText.classList.remove('visible'); // Hide current hint first

        // Use a timeout to allow the class removal to register before adding the new one
        setTimeout(() => {
             let text = '';
             let show = true;
            switch (currentHint) {
                case 'drag':
                    text = 'גרור את הכדור כדי להתחיל!';
                    break;
                case 'take_frame':
                    text = 'מעולה! עכשיו לחץ על "צלם פריים".';
                     // Optional: Point to button?
                    break;
                case 'move_and_take':
                    text = 'יפה! הזיז את הכדור שוב וצלם פריים נוסף.';
                    break;
                case 'play':
                     text = `יש לך ${frames.length} פריימים! הזיז וצלם עוד, או לחץ על "הפעל סרטון".`;
                    break;
                default: // Hide hint
                    show = false;
                    break;
            }

            hintText.textContent = text;
            if (show) {
                 hintText.classList.add('visible');
                 // Position hint relative to relevant element? (Advanced, skip for now)
                 // For example, position hint near takeFrameBtn or playAnimationBtn
            }

        }, 50); // Small delay
    }


    // --- Initial Setup ---
    function initSimulation() {
        drawBall(); // Initial draw
        updateHint('drag'); // Show initial hint
        // Ensure buttons are in correct initial state
        playAnimationBtn.disabled = true;
        takeFrameBtn.disabled = false;
        resetBtn.disabled = false;
         galleryPlaceholder.style.display = 'block'; // Make sure placeholder is visible initially
    }


    // Initialize the simulation when the script loads
    initSimulation();


</script>