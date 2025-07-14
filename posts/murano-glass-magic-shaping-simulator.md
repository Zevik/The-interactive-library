---
title: "קסם הזכוכית המוראנו: הסימולטור המעצב"
english_slug: murano-glass-magic-shaping-simulator
category: "מלאכות יד"
tags: [זכוכית, מוראנו, מלאכה מסורתית, חומרים, אמנות, סימולציה]
---
<h1>קסם הזכוכית המוראנו: הסימולטור המעצב</h1>

דמיינו לרגע: חול פשוט, אש יוקדת, ונשימה אחת מדויקת שהופכת הכל ליצירת אמנות זוהרת וצבעונית. ברוכים הבאים למוראנו, אי הקוסמים של הזכוכית, שם סודות עתיקים פוגשים יצירתיות מודרנית. במקום רק לקרוא, הצטרפו אלינו למסע וירטואלי ללב הסדנה – תפסו את הקאנה הווירטואלית ובואו ליצור בעצמכם!

<div id="app-container">
    <h2 class="app-title">עצבו את יצירת המופת מזכוכית שלכם</h2>
    <div class="controls">
        <div class="control-group">
            <label for="temp-slider">להט הכבשן (טמפרטורה):</label>
            <input type="range" id="temp-slider" min="800" max="1400" value="1100" step="10" class="slider">
            <span id="temp-value">1100°C</span>
        </div>
        <div class="control-group">
            <label for="blow-slider">עוצמת הנשימה (ניפוח):</label>
            <input type="range" id="blow-slider" min="0" max="100" value="0" class="slider">
            <span id="blow-value">0%</span>
        </div>
        <div class="control-group">
            <label for="rotate-slider">קצב הסיבוב (סימטריה):</label>
            <input type="range" id="rotate-slider" min="0" max="100" value="50" class="slider">
            <span id="rotate-value">50%</span>
        </div>
        <div class="control-group">
            <label>כלי העבודה הקסומים:</label>
            <div class="tool-buttons">
                <button class="tool-button" data-tool="none">✨ בלי כלי</button>
                <button class="tool-button" data-tool="push">👉 דחיפה</button>
                <button class="tool-button" data-tool="pull">🤏 משיכה</button>
                <button class="tool-button" data-tool="cut">✂️ חיתוך</button>
            </div>
        </div>
        <div class="control-group color-group">
            <label>הוסיפו נגיעות צבע:</label>
            <input type="color" id="color-picker" value="#ff0000">
            <button id="add-color-button">🎨 הוסף צבע</button>
        </div>
        <button id="reset-button">🔄 התחל מחדש</button>
    </div>

    <div id="canvas-container">
         <canvas id="glass-canvas" width="600" height="400"></canvas>
         <div id="tool-cursor" style="display: none;"></div>
    </div>


</div>

<button id="toggle-explanation" class="info-button">📚 גלו את הסודות: על יצירת זכוכית מוראנו</button>

<div id="explanation" style="display: none;">
    <h2>על קסם יצירת זכוכית מוראנו</h2>

    <h3>🔥 מסע אל לב האש: היסטוריה בלהבות</h3>
    <p>שורשי אמנות הזכוכית בוונציה נטועים עמוק בזמן. ב-1291, בצעד דרמטי שהונע מחשש לשריפות בעיר התעלות הצפופה ורצון לשמור על ידע יקר מפז, הועברו כל ענקי הזכוכית לאי הקטן מוראנו. שם, בבידוד יחסי, פרחה האמנות והטכניקות התפתחו לשיאים חדשים. משפחות אמני הזכוכית שמרו בקנאות על סודותיהן, והפכו את מוראנו למרכז עולמי לשכיות חמדה מזכוכית, סמל ליוקרה ואיכות שאין שנייה לה.</p>

    <h3>💎 החומר הקסום: מהחול לזכוכית נוזלית</h3>
    <p>הקסם מתחיל בחול, או ליתר דיוק, חול קוורץ טהור. אבל חול לבדו דורש חום בלתי נתפס. כדי להוריד את טמפרטורת ההיתוך ולהפוך אותו לחומר שניתן לעצב, מוסיפים לו "קסמים" נוספים – סודה לשתייה (נתרן פחמתי) שמסייעת בהמסה, ואבן גיר או דולומיט לייצוב התערובת. שילוב מדויק זה, המחומם בכבשנים מיוחדים לטמפרטורות עוצרות נשימה של מעל 1400 מעלות צלזיוס, הופך לגוש זוהר, נוזלי וצמיג – הזכוכית המותכת, מוכנה לקבל צורה ונפח.</p>

    <h3>🛠️ כלי האמן: כלים פשוטים, מיומנות על-אנושית</h3>
    <p>הכוכב הבלתי מעורער של הסדנה הוא ה"קאנה" (cana) – צינורית מתכת ארוכה וחלולה. זהו למעשה שלוחה של האמן, דרכה אוספים כמות קטנה של זכוכית מותכת, המכונה "גאפרה", ישירות מהכבשן הלוהט. כלים נוספים כמו מלקחיים מדויקים (pizze), מספריים חדות (tagianti), וכמובן, סדרה של כבשנים משניים לחימום מחדש ("פונטלו") וקירור מבוקר, כולם חלק מהתזמורת המופלאה של יצירת הזכוכית.</p>

    <h3>🌬️ נשימת החיים: אמנות הניפוח</h3>
    <p>עם גוש הזכוכית הלוהט בקצה הקאנה, מתחיל שלב הניפוח – שלב עדין הדורש ריכוז ונשימה מבוקרת. האמן נושף בעדינות דרך הצינורית, ואוויר חם נכלא בתוך הזכוכית ויוצר בועה פנימית. תוך כדי ניפוח, הצינורית מסובבת ללא הרף. הסיבוב הזה אינו סתמי; הוא ששומר על הזכוכית במרכז הכובד ומאפשר יצירת צורה סימטרית, אחידה ויפה כשהבועה גדלה ומעצבת את חלל הכלי.</p>

    <h3>✋ מגע הקסם: עיצוב ופיסול הזכוכית</h3>
    <p>לאחר שהכלי קיבל את צורתו הבסיסית דרך הניפוח, נכנסים לתמונה כלי העיצוב. בעזרת מלקחיים, מוטות מתכת רטובים (הלם הטמפרטורה יוצר קיפולים וצורות), וטכניקות משיכה ולחיצה, האמן מעצב את הפרטים: יוצר ידיות אלגנטיות, רגליים יציבות, שוליים מסולסלים או דפנות עם טקסטורה מיוחדת. כל מגע הוא מדויק ומחושב, מנצל את גמישותה הזמנית של הזכוכית לפני שהיא מתקשה.</p>

    <h3>🌈 פלטת הצבעים של האלכימאי: הוספת גוונים</h3>
    <p>אי אפשר לדבר על מוראנו בלי הצבעים העזים והעשירים. הסוד טמון בתוספת תחמוצות מינרלים שונות לתערובת הבסיס, או בגלגול גוש הזכוכית המותכת באבקות צבעוניות, שבבי זכוכית ("פירולי") או מוטות צבע מיוחדים (מורייני) לפני או במהלך העיצוב. כל מינרל מעניק גוון אחר: נחושת לירוק או כחול, קובלט לכחול מלכותי, זהב לאדום אודם עמוק, ועוד אינסוף אפשרויות ליצירת פסיפס של צבעים ודפוסים בתוך הזכוכית עצמה.</p>

    <h3>🧊 מנוחה אחרונה: שלב הקירור המכריע</h3>
    <p>השלב האחרון, ולעיתים המכריע ביותר, הוא הקירור. הכלי המוגמר מוכנס לכבשן קירור מיוחד הנקרא "לר" (ler), שם הוא מתקרר לאט ובהדרגה לאורך שעות או אפילו ימים. תהליך איטי זה, המכונה "חישול" (annealing), חיוני כדי להסיר מתחים פנימיים שהצטברו בזכוכית במהלך החימום והעיצוב המהירים. קירור מהיר מדי יותיר את הכלי שביר להפליא, נתון לסכנת התנפצות גם ממגע קל ביותר. רק לאחר הקירור המבוקר, יצירת המופת מוכנה לחשוף את יופייה לעולם.</p>
</div>

<script>
    const canvas = document.getElementById('glass-canvas');
    const ctx = canvas.getContext('2d');

    const tempSlider = document.getElementById('temp-slider');
    const tempValue = document.getElementById('temp-value');
    const blowSlider = document.getElementById('blow-slider');
    const blowValue = document.getElementById('blow-value');
    const rotateSlider = document.getElementById('rotate-slider');
    const rotateValue = document.getElementById('rotate-value');
    const toolButtons = document.querySelectorAll('.tool-button');
    const colorPicker = document.getElementById('color-picker');
    const addColorButton = document.getElementById('add-color-button');
    const resetButton = document.getElementById('reset-button');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const toolCursor = document.getElementById('tool-cursor');
    const canvasContainer = document.getElementById('canvas-container');


    let glassShape = []; // Array of points representing the glass outline
    let currentTool = 'none';
    let addedColors = []; // Array of colors added
    let animationFrameId = null; // To manage canvas redraw loop

    // Initialize glass shape (basic blob)
    function resetGlass() {
        glassShape = [];
        const initialRadius = 20;
        const centerX = canvas.width / 2;
        const startY = canvas.height - 50; // Position on the pipe end
        // Create a simple circle at the end of the pipe
        for (let i = 0; i <= 360; i += 10) {
            const angle = (i * Math.PI) / 180;
            const x = centerX + initialRadius * Math.cos(angle);
            const y = startY - initialRadius * Math.sin(angle * 0.5); // Slight oval for pipe end
            glassShape.push({ x, y });
        }
        addedColors = [];
        blowSlider.value = 0;
        blowValue.textContent = '0%';
        rotateSlider.value = 50; // Default rotation speed
        rotateValue.textContent = '50%';
        updateGlassShape(); // Initial draw
    }

    function getGlassColor(temp) {
        // More nuanced temperature to color mapping (simulated glow)
        const t = parseInt(temp);
        if (t < 850) return '#FF4500'; // Deep Orange-Red
        if (t < 950) return '#FFA500'; // Orange
        if (t < 1050) return '#FFD700'; // Gold
        if (t < 1150) return '#FFFF00'; // Yellow
        if (t < 1250) return '#FFFFE0'; // Light Yellow
        if (t < 1350) return '#FFFFFF'; // White-hot
        return '#FFFFFF'; // Pure White
    }

    function drawGlass() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw pipe (more integrated visually)
        const pipeWidth = 30;
        const pipeHeight = 100;
        const pipeX = canvas.width / 2 - pipeWidth / 2;
        const pipeY = canvas.height - pipeHeight;
        ctx.fillStyle = '#a0522d'; // Sienna Brown
        ctx.fillRect(pipeX, pipeY, pipeWidth, pipeHeight);

        // Draw connecting piece/ferrule
        ctx.fillStyle = '#778899'; // LightSlateGrey
        ctx.beginPath();
        ctx.arc(canvas.width / 2, pipeY, pipeWidth / 2 + 5, 0, Math.PI, true);
        ctx.fill();


        if (glassShape.length === 0) return;

        // Draw glass blob
        ctx.beginPath();
        // Use quadratic curves for smoother shape
        ctx.moveTo(glassShape[0].x, glassShape[0].y);
        for (let i = 1; i < glassShape.length - 2; i++) {
            const xc = (glassShape[i].x + glassShape[i + 1].x) / 2;
            const yc = (glassShape[i].y + glassShape[i + 1].y) / 2;
            ctx.quadraticCurveTo(glassShape[i].x, glassShape[i].y, xc, yc);
        }
        // Complete the shape with a curve back to the start
        const lastPoint = glassShape[glassShape.length - 1];
        const secondLastPoint = glassShape[glassShape.length - 2];
        ctx.quadraticCurveTo(lastPoint.x, lastPoint.y, secondLastPoint.x, secondLastPoint.y);

        ctx.closePath();

        // Apply base color based on temperature
        const baseColor = getGlassColor(parseInt(tempSlider.value));
        ctx.fillStyle = baseColor;
        ctx.fill();

        // Add gradient for simulated heat/glow
        const gradient = ctx.createRadialGradient(
            canvas.width / 2, glassShape[0].y - 30, 10, // Inner circle (center, radius)
            canvas.width / 2, glassShape[0].y, Math.max(50, blowSlider.value * 1.5) // Outer circle (center, radius)
        );
        gradient.addColorStop(0, 'rgba(255, 255, 200, 0.8)'); // Bright center glow
        gradient.addColorStop(0.5, 'rgba(255, 165, 0, 0.5)'); // Orange glow
        gradient.addColorStop(1, 'rgba(255, 0, 0, 0.1)'); // Reddish edge fade

        ctx.fillStyle = gradient;
        ctx.fill(); // Overlay gradient

        // Add colors effect (more visually distinct)
        if (addedColors.length > 0) {
             addedColors.forEach((color, index) => {
                // Draw color blobs or stripes (simplified visualization)
                ctx.fillStyle = color + '99'; // Add transparency

                // Simple stripes effect based on color index
                const stripeWidth = 15;
                const offset = (index * stripeWidth * 1.5) % (canvas.width / 2); // Offset stripes
                for(let i = 0; i < glassShape.length; i += 2) {
                     const p1 = glassShape[i];
                     const p2 = glassShape[(i + glassShape.length / 2) % glassShape.length]; // Point opposite

                     // Draw a simple line/stripe
                     ctx.beginPath();
                     ctx.moveTo(p1.x + Math.sin(i * 0.1) * offset, p1.y); // Add a wavy effect
                     ctx.lineTo(p2.x + Math.sin((i + glassShape.length / 2) * 0.1) * offset, p2.y);
                     ctx.lineWidth = stripeWidth;
                     ctx.strokeStyle = color + '99';
                     ctx.stroke();
                }
             });
        }


        // Add some simple highlight/reflection (simulated)
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.8)';
        ctx.lineWidth = 3;
        ctx.stroke();

         // Add bubble effect (simulated)
         if (parseInt(blowSlider.value) > 20) {
             const bubbleRadius = Math.max(5, parseInt(blowSlider.value) / 20);
             ctx.fillStyle = 'rgba(255, 255, 255, 0.4)';
             ctx.beginPath();
             ctx.arc(canvas.width / 2 + bubbleRadius, glassShape[0].y - bubbleRadius, bubbleRadius, 0, Math.PI * 2);
             ctx.fill();
              ctx.beginPath();
             ctx.arc(canvas.width / 2 - bubbleRadius * 1.5, glassShape[0].y - bubbleRadius * 0.5, bubbleRadius * 0.7, 0, Math.PI * 2);
             ctx.fill();
         }

         // Basic tool interaction visual feedback (does not alter shape in this version)
         // Could potentially draw a visual indicator on the canvas where the mouse is
         // if a tool is active, suggesting interaction points. (Too complex for this scope)

    }

     let lastBlowValue = 0;
     let animationStartTime = null;

    function updateGlassShape(timestamp) {
         if (!animationStartTime) animationStartTime = timestamp;
         const elapsed = timestamp - animationStartTime;
         const duration = 200; // Animation duration in ms

         const blowStrength = parseInt(blowSlider.value) / 100; // 0 to 1
         const currentBlowValue = parseInt(blowSlider.value);

         // Interpolate blow effect for smoother animation
         const interpolatedBlow = lastBlowValue + (currentBlowValue - lastBlowValue) * Math.min(1, elapsed / duration);


        const baseRadius = 20;
        const blowFactor = 1 + (interpolatedBlow / 100) * 2.5; // Max 3.5 times initial radius
        const centerX = canvas.width / 2;
        const startY = canvas.height - 50;

        // Re-calculate shape based on interpolated blow strength and simulated rotation
        glassShape = [];
        const numPoints = 36; // Fewer points for potentially faster drawing/manipulation
        const rotateEffect = (parseInt(rotateSlider.value) - 50) / 50 * 0.1; // -0.1 to 0.1 (simulated wobble)
         const wobbleSpeed = 0.05; // How fast the shape wobbles

         for (let i = 0; i <= numPoints; i++) {
            const angle = (i / numPoints) * Math.PI * 2; // Full circle
             // Add wobble based on rotation speed and time
             const wobble = Math.sin(angle * 3 + elapsed * wobbleSpeed) * rotateEffect * (interpolatedBlow / 100) * 20;


            // Simple elliptical expansion based on angle, influenced by blow
            // Offset center slightly for more natural bulge
            const offsetX = Math.sin(elapsed * wobbleSpeed * 0.5) * (interpolatedBlow / 100) * 5;
            const offsetY = Math.cos(elapsed * wobbleSpeed * 0.5) * (interpolatedBlow / 100) * 5;


            const currentRadius = baseRadius * blowFactor * (1 + 0.4 * Math.sin(angle * 1.5)) + wobble; // Make it more bulbous and add wobble
            const x = centerX + offsetX + currentRadius * Math.cos(angle);
            const y = startY + offsetY - currentRadius * Math.sin(angle * 0.8) - (interpolatedBlow / 100) * 80; // Move up and slightly distort vertically

             // Add variation based on simulated tool effect (very basic)
             // This would require mouse interaction and is just a placeholder concept
             if (currentTool !== 'none' && canvas.matches(':hover')) {
                // Placeholder: Apply a slight perturbation to points near mouse
                // For a real sim: Calculate distance from mouse, apply force/offset based on tool
             }

            glassShape.push({ x, y });
        }

         drawGlass();

         // Continue animation only if blowing or wobbling
         if (Math.abs(currentBlowValue - lastBlowValue) > 0.5 || Math.abs(rotateEffect) > 0.005) {
             lastBlowValue = interpolatedBlow;
             animationFrameId = requestAnimationFrame(updateGlassShape);
         } else {
             lastBlowValue = currentBlowValue;
             animationStartTime = null; // Reset for next animation
         }
    }

    // Start animation loop when relevant sliders are moved
    function startAnimation() {
         if (!animationFrameId) {
             animationStartTime = null; // Ensure start time is reset
             animationFrameId = requestAnimationFrame(updateGlassShape);
         }
    }

    function stopAnimation() {
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
            animationFrameId = null;
            animationStartTime = null; // Reset start time
        }
    }


    // --- Event Listeners ---

    tempSlider.addEventListener('input', () => {
        tempValue.textContent = tempSlider.value + '°C';
        drawGlass(); // Redraw to update color immediately
    });

    blowSlider.addEventListener('input', () => {
        blowValue.textContent = blowSlider.value + '%';
        startAnimation(); // Start/continue animation
    });

     blowSlider.addEventListener('change', () => {
        // When user stops dragging, ensure shape is finalized and stop animation
        stopAnimation();
        updateGlassShape(performance.now()); // Final update
     });


    rotateSlider.addEventListener('input', () => {
        rotateValue.textContent = rotateSlider.value + '%';
        startAnimation(); // Start animation for wobble effect
    });
     rotateSlider.addEventListener('change', () => {
         // When user stops dragging, continue animation for wobble if needed, otherwise stop
         const rotateEffect = (parseInt(rotateSlider.value) - 50) / 50 * 0.1;
         if (Math.abs(rotateEffect) < 0.005) {
             stopAnimation();
         } else {
              updateGlassShape(performance.now()); // Final update with rotation
         }
     });


    toolButtons.forEach(button => {
        button.addEventListener('click', () => {
            currentTool = button.dataset.tool;
            toolButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            console.log("Tool selected:", currentTool); // For demonstration
            // In a real simulation, this would enable canvas mouse event listeners
            // tailored to the selected tool to modify the shape dynamically on mousemove/drag.
            // This is not implemented in this basic version.
        });
    });

     addColorButton.addEventListener('click', () => {
        const color = colorPicker.value;
        if (addedColors.length < 5) { // Limit added colors
            addedColors.push(color);
             console.log("Color added:", color); // For demonstration
            drawGlass(); // Redraw with new color effect
        } else {
             // Provide visual feedback instead of alert
             addColorButton.classList.add('shake-effect'); // Add a class for animation
             setTimeout(() => {
                 addColorButton.classList.remove('shake-effect');
             }, 500); // Remove class after animation
        }
    });


    resetButton.addEventListener('click', () => {
        resetGlass();
        // Reset controls to default
        tempSlider.value = 1100;
        tempValue.textContent = '1100°C';
        blowSlider.value = 0;
        blowValue.textContent = '0%';
        rotateSlider.value = 50;
        rotateValue.textContent = '50%';
        toolButtons.forEach(btn => btn.classList.remove('active'));
        document.querySelector('.tool-button[data-tool="none"]').classList.add('active');
        currentTool = 'none';
        stopAnimation(); // Ensure animation is stopped on reset
    });

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? '🔼 הסתר הסודות' : '📚 גלו את הסודות: על יצירת זכוכית מוראנו';
        // Optional: scroll to the explanation section
        if (!isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth' });
        }
    });


    // --- Tool Cursor Logic ---
    canvasContainer.addEventListener('mousemove', (event) => {
        // Position the cursor relative to the viewport, adjusted for scrolling
        if (currentTool !== 'none') {
             toolCursor.style.display = 'block';
             toolCursor.style.left = event.clientX + 'px';
             toolCursor.style.top = event.clientY + 'px';
             toolCursor.textContent = {
                 'push': '👉', // Pushing emoji
                 'pull': '🤏', // Pinching/pulling emoji
                 'cut': '✂️'   // Scissors emoji
             }[currentTool] || '✨';
             // Hide native cursor over the canvas container
             canvasContainer.style.cursor = 'none';
        } else {
             toolCursor.style.display = 'none';
             canvasContainer.style.cursor = 'default'; // Show native cursor when no tool
        }
    });

     canvasContainer.addEventListener('mouseleave', () => {
        toolCursor.style.display = 'none';
         canvasContainer.style.cursor = 'default'; // Restore native cursor
     });


    // --- Initial setup ---
    resetGlass();
    document.querySelector('.tool-button[data-tool="none"]').classList.add('active');
    // Initial draw needs to be called at least once
    drawGlass();


</script>

<style>
    :root {
        --murano-blue: #17a2b8;
        --murano-red: #dc3545;
        --murano-green: #28a745;
        --murano-yellow: #ffc107;
        --murano-gray: #6c757d;
        --murano-dark: #333;
        --murano-light: #f9f9f9;
        --murano-border: #ccc;
    }

    #app-container {
        direction: rtl;
        font-family: 'Arial', sans-serif; /* Consider a more artistic font if available and web-safe */
        max-width: 900px; /* Slightly wider container */
        margin: 30px auto; /* More margin */
        padding: 30px; /* More padding */
        border: 1px solid var(--murano-border);
        border-radius: 12px; /* Rounded corners */
        background: linear-gradient(to bottom, var(--murano-light), #e9e9e9); /* Subtle gradient background */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* Soft shadow */
        position: relative; /* Needed for absolute positioned tool cursor */
    }

    h1, h2 {
        text-align: center;
        color: var(--murano-dark);
        margin-bottom: 20px; /* Space below titles */
    }

    .app-title {
        color: #a0522d; /* Sienna/Pottery color */
        font-size: 2em; /* Larger title */
        margin-bottom: 30px;
        position: relative;
    }
    .app-title::after {
        content: '';
        display: block;
        width: 60px;
        height: 3px;
        background: linear-gradient(to right, var(--murano-red), var(--murano-yellow));
        margin: 10px auto 0;
        border-radius: 2px;
    }


    p {
        text-align: justify;
        line-height: 1.8; /* More comfortable reading */
        color: #555;
    }

    .controls {
        display: flex;
        flex-wrap: wrap;
        justify-content: center; /* Center controls */
        gap: 20px; /* Increased gap */
        margin-bottom: 30px;
        padding: 20px;
        background-color: #fff; /* White background for controls */
        border-radius: 8px;
        box-shadow: inset 0 1px 5px rgba(0, 0, 0, 0.05); /* Subtle inner shadow */
    }

    .control-group {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        min-width: 180px; /* Wider control groups */
        flex-grow: 1; /* Allow groups to grow */
        max-width: 45%; /* Max width for two columns */
    }
    /* Specific layout for tool and color groups */
    .tool-buttons, .color-group {
         display: flex;
         flex-wrap: wrap;
         gap: 8px; /* Space between buttons */
         margin-top: 5px; /* Space below label */
    }
     .color-group input[type="color"] {
         padding: 0;
         border: 1px solid var(--murano-border);
         border-radius: 4px;
         height: 38px; /* Match button height */
         cursor: pointer;
     }


    .control-group label {
        font-weight: bold;
        margin-bottom: 8px; /* More space below label */
        color: var(--murano-dark);
        font-size: 1.1em;
    }

    .slider {
        width: 100%;
        cursor: pointer;
        -webkit-appearance: none; /* Override default appearance */
        appearance: none;
        height: 8px;
        background: var(--murano-border);
        outline: none;
        opacity: 0.7;
        transition: opacity 0.2s ease;
        border-radius: 4px;
    }

    .slider:hover {
        opacity: 1;
    }

    .slider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--murano-blue);
        border-radius: 50%;
        cursor: pointer;
        border: 2px solid white;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
    }

    .slider::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--murano-blue);
        border-radius: 50%;
        cursor: pointer;
        border: 2px solid white;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
    }


    .control-group span {
        font-size: 1em; /* Slightly larger value text */
        color: #333;
        text-align: center;
        width: 100%;
        margin-top: 5px; /* More space above value */
        font-weight: bold;
    }

    button {
        padding: 10px 15px; /* More padding */
        border: none;
        border-radius: 5px; /* Slightly more rounded */
        cursor: pointer;
        background-color: var(--murano-blue);
        color: white;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease; /* Add transform for press effect */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Button shadow */
    }

    button:hover {
        background-color: #0056b3;
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
    }
     button:active {
         transform: translateY(1px); /* Simulate button press */
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
     }

    .tool-button {
         background-color: var(--murano-gray);
         flex-grow: 1; /* Allow tool buttons to fill space */
         text-align: center;
    }
     .tool-button:hover {
         background-color: #545b62;
    }
    .tool-button.active {
        background-color: var(--murano-green);
        font-weight: bold;
        box-shadow: 0 2px 5px rgba(40, 167, 69, 0.4); /* Green shadow for active */
    }
     #add-color-button {
         background-color: var(--murano-yellow);
         color: var(--murano-dark);
         flex-grow: 1;
     }
      #add-color-button:hover {
         background-color: #e0a800;
     }
     /* Shake animation for add color button */
     .shake-effect {
         animation: shake 0.5s;
     }
     @keyframes shake {
         0%, 100% { transform: translateX(0); }
         10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
         20%, 40%, 60%, 80% { transform: translateX(5px); }
     }


      #reset-button {
         background-color: var(--murano-red);
         margin-top: 10px; /* Space above reset button */
         width: 100%; /* Full width button */
      }
      #reset-button:hover {
         background-color: #c82333;
     }

    #canvas-container {
        position: relative; /* Needed for the tool cursor positioning */
        width: 600px;
        height: 400px;
        margin: 20px auto;
        border: 2px solid #000; /* More prominent border */
        border-radius: 8px; /* Rounded corners */
        overflow: hidden; /* Hide anything outside the canvas */
        background: linear-gradient(to bottom, #87ceeb, #cceeff); /* Sky blue gradient */
        box-shadow: inset 0 0 10px rgba(0,0,0,0.2); /* Inner shadow for depth */
         cursor: default; /* Default cursor over canvas area */
    }


    #glass-canvas {
        display: block;
        width: 100%;
        height: 100%;
    }

    .info-button { /* Style for the toggle explanation button */
        display: block;
        width: fit-content;
        margin: 30px auto;
        background-color: var(--murano-blue);
        font-size: 1.1em;
        padding: 12px 20px;
    }
     .info-button:hover {
        background-color: #138496;
    }


    #explanation {
        direction: rtl;
        margin-top: 40px; /* More space above explanation */
        padding: 30px;
        border: 1px solid var(--murano-border);
        border-radius: 12px;
        background-color: #fff;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
    }

    #explanation h3 {
        color: #a0522d; /* Matching glass color */
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 1px dashed #eee; /* Subtle separator */
        padding-bottom: 5px;
    }

    #explanation p {
         text-align: right;
         margin-bottom: 15px; /* Space between paragraphs */
         color: #444;
    }

     #tool-cursor {
         position: fixed;
         pointer-events: none;
         font-size: 2.5em; /* Larger emoji */
         z-index: 1000;
         transform: translate(-50%, -50%); /* Center on pointer */
         text-shadow: 0 0 5px rgba(0, 0, 0, 0.3); /* Shadow for visibility */
     }


</style>