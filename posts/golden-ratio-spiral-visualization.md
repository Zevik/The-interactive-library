---
title: "הדגמה חווייתית: מסע אל ספירלת הזהב ויחס פי"
english_slug: golden-ratio-spiral-visualization
category: "מדעים מדויקים / מתמטיקה"
tags: [יחס הזהב, פי, ספירלת הזהב, הדמיה, ויזואליזציה, מתמטיקה, אמנות, טבע, יופי, הרמוניה]
---
# הדגמה ויזואלית של "יחס הזהב" (פי): מסע אל ספירלת היופי הקוסמית

האם שמתם לב פעם לתבניות קסומות החוזרות על עצמן בטבע, ביצירות אמנות עוצרות נשימה או אפילו במבנה גלקסיות מרוחקות? אולי יש סוד מתמטי מאחורי תחושת ההרמוניה הזו? קיימת תאוריה מרתקת לפיה יחס מתמטי מיוחד, המכונה "יחס הזהב" או "פי" (Phi), הוא שפה סודית של היופי, והספירלה האלגנטית הנגזרת ממנו נגלית לעינינו בצורות רבות סביבנו.

התנסו עכשיו בעצמכם! לחצו על הכפתורים וגלו כיצד "ספירלת הזהב" מתאימה באופן מפתיע לצורות אייקוניות, החל מפלאי הטבע ועד יצירות מופת אנושיות. האם זו אמת מדעית קוסמית או קסם אופטי שובה לב? שפטו בעצמכם!

<div class="interactive-app" aria-label="הדגמה אינטראקטיבית של ספירלת הזהב">
    <div class="image-gallery">
        <div class="image-card" aria-roledescription="כרטיס הדגמה">
            <h3>קסם בתוך קונכייה: נאוטילוס</h3>
            <div class="image-wrapper" id="image-nautilus" aria-label="תמונה של קונכיית נאוטילוס">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/NautilusCutaway7.jpg/800px-NautilusCutaway7.jpg" alt="חתך רוחב של קונכיית נאוטילוס, המציג את תאיה הפנימיים המסודרים בספירלה" class="sample-image" loading="lazy">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Golden_spiral_%28Log_spiral%29.svg/1200px-Golden_spiral_%28Log_spiral%29.svg.png" alt="ספירלת הזהב המתוארת על ידי קשתות המבוססות על יחס הזהב" class="golden-spiral" data-image="nautilus" aria-hidden="true">
            </div>
            <button class="toggle-spiral-btn" data-target="nautilus" aria-controls="image-nautilus">
                <span class="show-text">גלו את הספירלה הקסומה</span>
                <span class="hide-text" style="display: none;">הסתירו את הספירלה</span>
            </button>
        </div>
        <div class="image-card" aria-roledescription="כרטיס הדגמה">
            <h3>יקום ספירלי: גלקסיה M51</h3>
            <div class="image-wrapper" id="image-galaxy" aria-label="תמונה של גלקסיה ספירלית M51">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Messier51_sRGB.jpg/800px-Messier51_sRGB.jpg" alt="תמונה מרהיבה של גלקסיה ספירלית M51, המציגה את זרועותיה המסודרות בדפוס ספירלי" class="sample-image" loading="lazy">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Golden_spiral_%28Log_spiral%29.svg/1200px-Golden_spiral_%28Log_spiral%29.svg.png" alt="ספירלת הזהב המתוארת על ידי קשתות המבוססות על יחס הזהב" class="golden-spiral" data-image="galaxy" aria-hidden="true">
            </div>
             <button class="toggle-spiral-btn" data-target="galaxy" aria-controls="image-galaxy">
                <span class="show-text">גלו את הספירלה הקוסמית</span>
                <span class="hide-text" style="display: none;">הסתירו את הספירלה</span>
            </button>
        </div>
         <div class="image-card" aria-roledescription="כרטיס הדגמה">
            <h3>יופי אנושי? מונה ליזה</h3>
            <div class="image-wrapper" id="image-face" aria-label="תמונה של הציור מונה ליזה מאת לאונרדו דה וינצ'י">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Mona_Lisa_color_corrected.jpg/800px-Mona_Lisa_color_corrected.jpg" alt="הפורטרט המפורסם של המונה ליזה" class="sample-image" loading="lazy">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Golden_spiral_%28Log_spiral%29.svg/1200px-Golden_spiral_%28Log_spiral%29.svg.png" alt="ספירלת הזהב המתוארת על ידי קשתות המבוססות על יחס הזהב" class="golden-spiral" data-image="face" aria-hidden="true">
            </div>
             <button class="toggle-spiral-btn" data-target="face" aria-controls="image-face">
                <span class="show-text">גלו את סודות הקומפוזיציה</span>
                <span class="hide-text" style="display: none;">הסתירו את הספירלה</span>
            </button>
        </div>
    </div>
</div>

<button id="show-explanation-btn" class="explanation-button" aria-expanded="false" aria-controls="explanation">
    <span class="show-text">פתח את תיבת הסודות: מה זה בעצם פי?</span>
    <span class="hide-text" style="display: none;">סגור את ההסבר</span>
</button>

<div id="explanation" class="explanation-section" style="display: none;" aria-hidden="true">
    <h2>פענוח הקוד: יחס הזהב (φ) וספירלת הזהב</h2>
    <p>
        **יחס הזהב (Phi, φ ≈ 1.618)** הוא לא סתם מספר, הוא יחס הרמוני מיוחד שמכונה גם "חיתוך הזהב" או "יחס אלוהי". דמיינו קטע שחילקתם לשני חלקים. היחס הוא 'פי' אם היחס בין הקטע השלם לחלק הגדול שווה בדיוק ליחס בין החלק הגדול לחלק הקטן. זהו יחס שמייצר סוג של איזון ויזואלי ומתמטי.
        <br/>
        בצורה מתמטית:
        $$ \frac{\text{שלם}}{\text{חלק גדול}} = \frac{\text{חלק גדול}}{\text{חלק קטן}} = \phi \approx 1.618 $$
        נוסחת הקסם שלו היא:
        $$ \phi = \frac{1 + \sqrt{5}}{2} $$
    </p>
    <p>
        **ספירלת הזהב** היא ספירלה לוגריתמית ייחודית שקצב הגדילה שלה קשור ישירות ליחס פי. היא גדלה החוצה בפקטור של φ בכל רבע סיבוב. דרך ויזואלית פופולרית לבניית קירוב שלה היא באמצעות סדרת ריבועים הנבנים בתוך "מלבני זהב" (מלבנים שהיחס בין צלעותיהם הוא φ), כשבכל ריבוע מציירים קשת מעגלית. הספירלה המתקבלת נחשבת לאחת הצורות האסתטיות בטבע.
    </p>
    <p>
        **היכן נפגוש את פי?** יש הטוענים שיחס הזהב וספירלת הזהב חבויים במקומות רבים:
        <ul>
            <li>**בטבע:** סידור העלים על גבעולים (פילוטקסיס), מבנה זרעי חמנייה, אצטרובלים, צורת קונכיות (כמו הנאוטילוס שראינו), מבנה כפות ידיים ואפילו זרועות גלקסיות ספירליות ענקיות.</li>
            <li>**באמנות ואדריכלות:** יש מחקרים וטענות רבות (חלקן שנויות במחלוקת!) על שימוש ביחס הזהב בפירמידות במצרים, בפרתנון ביוון, ביצירות רנסנס של לאונרדו דה וינצ'י ואמנים אחרים, וביצירות אמנות מודרנית רבות. האם האמנים השתמשו בו במודע כדי ליצור יופי, או שאנו פשוט רואים תבניות מוכרות במקומות בהם אנו מחפשים אותן? הוויכוח ממשיך לרגש!</li>
        </ul>
        בין אם מדובר בחוק טבע יסודי של היופי או באשליה ויזואלית מרתקת, ספירלת הזהב ממשיכה להדהים ולעורר השראה.
    </p>
</div>

<style>
    :root {
        --primary-color: #4A90E2; /* A clean, modern blue */
        --secondary-color: #50E3C2; /* A fresh, vibrant green */
        --accent-color: #F5A623; /* A warm accent gold */
        --text-color: #333333;
        --bg-color: #F8F9FA; /* Light gray background */
        --card-bg: #FFFFFF; /* White card background */
        --border-color: #E0E0E0; /* Light gray border */
        --hover-primary: #357ABD; /* Darker blue on hover */
        --hover-secondary: #3EBC9F; /* Darker green on hover */
        --shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        --card-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
        --transition-speed: 0.5s;
    }

    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
        line-height: 1.7;
        color: var(--text-color);
        background-color: var(--bg-color);
        padding: 20px;
        direction: rtl;
        text-align: right;
        margin: 0;
        overflow-x: hidden; /* Prevent horizontal scroll from potential animations */
    }

    h1, h2, h3 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 20px;
        font-weight: 700;
    }

    h1 { font-size: 2.5em; margin-top: 20px; }
    h2 { font-size: 2em; }
    h3 { font-size: 1.3em; color: var(--secondary-color); margin-bottom: 15px;}

    p { margin-bottom: 15px; }

    ul { margin-bottom: 15px; padding-right: 20px; }
    li { margin-bottom: 8px; }

    .interactive-app {
        margin: 40px auto;
        padding: 30px;
        background-color: var(--card-bg);
        border-radius: 12px;
        box-shadow: var(--shadow);
        max-width: 1000px; /* Limit width on large screens */
        width: 100%;
        box-sizing: border-box;
    }

    .image-gallery {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); /* Responsive grid */
        gap: 30px;
        justify-content: center;
    }

    .image-card {
        border: 1px solid var(--border-color);
        border-radius: 10px;
        padding: 20px;
        background-color: var(--bg-color);
        text-align: center;
        box-shadow: var(--card-shadow);
        display: flex;
        flex-direction: column;
        align-items: center;
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
    }

    .image-card:hover {
         transform: translateY(-5px);
         box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
    }

    .image-wrapper {
        position: relative;
        width: 100%;
        padding-bottom: 75%; /* 4:3 Aspect Ratio for consistency */
        height: 0;
        overflow: hidden;
        border-radius: 8px;
        margin-bottom: 20px;
        background-color: #e9ecef; /* Subtle placeholder */
        display: flex; /* Use flex to potentially center image if aspect ratio differs */
        justify-content: center;
        align-items: center;
    }

    .sample-image {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover; /* Cover the wrapper area */
        display: block;
    }

    .golden-spiral {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%; /* Base size, will be adjusted by JS */
        height: 100%; /* Base size, will be adjusted by JS */
        object-fit: contain;
        opacity: 0; /* Initially hidden */
        transform: scale(0.8); /* Start slightly smaller for animation */
        transition: opacity var(--transition-speed) ease-in-out, transform var(--transition-speed) ease-in-out;
        pointer-events: none; /* Allow clicking through */
         /* Default positioning - adjusted by JS */
    }

    .golden-spiral.visible {
        opacity: 1;
        transform: scale(1); /* Animate to normal scale */
        /* Specific positioning applied by JS */
    }

    .toggle-spiral-btn, .explanation-button {
        display: inline-block;
        padding: 12px 25px;
        font-size: 1em;
        font-weight: 600;
        color: #fff;
        background-color: var(--primary-color);
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease-in-out;
        margin-top: auto;
        text-align: center;
    }

    .toggle-spiral-btn:hover, .explanation-button:hover {
        background-color: var(--hover-primary);
        transform: translateY(-2px);
    }
    .toggle-spiral-btn:active, .explanation-button:active {
         transform: translateY(0);
    }

    .explanation-button {
        display: block;
        margin: 40px auto;
        width: fit-content;
        background-color: var(--secondary-color);
    }

    .explanation-button:hover {
         background-color: var(--hover-secondary);
    }


    .explanation-section {
        margin-top: 30px;
        padding: 30px;
        background-color: var(--card-bg);
        border-radius: 12px;
        box-shadow: var(--shadow);
        animation: slideInAndFade 0.8s ease-out forwards; /* Combined animation */
        max-width: 1000px; /* Limit width */
        margin-left: auto;
        margin-right: auto;
        box-sizing: border-box;
    }

    @keyframes slideInAndFade {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Hide/Show text within buttons */
    .toggle-spiral-btn .hide-text,
    .explanation-button .hide-text {
        display: none;
    }
    .toggle-spiral-btn.visible .show-text,
    .explanation-button.visible .show-text {
        display: none;
    }
    .toggle-spiral-btn.visible .hide-text,
    .explanation-button.visible .hide-text {
        display: inline;
    }

    /* Basic responsiveness */
    @media (max-width: 768px) {
        h1 { font-size: 2em; }
        h2 { font-size: 1.6em; }
        h3 { font-size: 1.1em; }
        .interactive-app, .explanation-section {
            padding: 20px;
            margin: 20px auto;
        }
         .image-gallery {
             gap: 20px;
         }
        .image-card {
            padding: 15px;
        }
        .toggle-spiral-btn, .explanation-button {
            padding: 10px 15px;
            font-size: 0.9em;
        }
         .image-wrapper {
             padding-bottom: 65%; /* Slightly less height on mobile */
         }
    }
     @media (max-width: 480px) {
         h1 { font-size: 1.8em; }
         h2 { font-size: 1.4em; }
         .image-card {
            max-width: 100%; /* Allow cards to take full width */
        }
     }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const toggleButtons = document.querySelectorAll('.toggle-spiral-btn');
        const explanationButton = document.getElementById('show-explanation-btn');
        const explanationSection = document.getElementById('explanation');

        // Function to update button text based on spiral visibility
        const updateButtonText = (button, isVisible) => {
            button.classList.toggle('visible', isVisible);
            button.setAttribute('aria-expanded', isVisible);
        };

        toggleButtons.forEach(button => {
            button.addEventListener('click', () => {
                const targetImageId = button.dataset.target;
                const spiralElement = document.querySelector(`.golden-spiral[data-image="${targetImageId}"]`);
                if (spiralElement) {
                    const isVisible = spiralElement.classList.toggle('visible');
                    updateButtonText(button, isVisible);
                     spiralElement.setAttribute('aria-hidden', !isVisible); // Accessibility
                }
            });
        });

        explanationButton.addEventListener('click', () => {
            const isHidden = explanationSection.style.display === 'none';
            if (isHidden) {
                explanationSection.style.display = 'block';
                explanationSection.setAttribute('aria-hidden', 'false');
                explanationButton.setAttribute('aria-expanded', 'true');
                updateButtonText(explanationButton, true);
            } else {
                explanationSection.style.display = 'none';
                explanationSection.setAttribute('aria-hidden', 'true');
                 explanationButton.setAttribute('aria-expanded', 'false');
                 updateButtonText(explanationButton, false);
            }
        });

        // Adjust spiral positioning and scaling dynamically on image load
        document.querySelectorAll('.image-wrapper').forEach(wrapper => {
             const img = wrapper.querySelector('.sample-image');
             const spiral = wrapper.querySelector('.golden-spiral');
             if (img && spiral) {
                 img.onload = () => {
                     const imageId = wrapper.id.replace('image-', '');

                     // Reset any previous styles
                     spiral.style.cssText = ''; // Clear inline styles

                     // Apply base styles from CSS class
                     spiral.classList.remove('visible'); // Ensure not visible initially

                     // --- Specific adjustments per image for better alignment ---
                     // These values are based on visual estimation and may need fine-tuning
                     if (imageId === 'nautilus') {
                          // Align spiral origin to the shell's center, scale and rotate
                         spiral.style.transformOrigin = '50% 50%'; // Origin of the spiral graphic itself
                         spiral.style.transform = 'rotate(-90deg) scale(1.2)'; // Rotate to match shell curve, scale up
                         spiral.style.top = '-10%'; // Shift up slightly
                         spiral.style.left = '-10%'; // Shift left slightly
                         spiral.style.width = '120%'; // Increase size
                         spiral.style.height = '120%'; // Increase size
                     } else if (imageId === 'galaxy') {
                          // Align spiral origin to the galactic core (center)
                         spiral.style.transformOrigin = '50% 50%';
                         spiral.style.transform = 'scale(1.0) rotate(0deg)'; // Scale to fit, no rotation needed for this example
                         spiral.style.top = '0%';
                         spiral.style.left = '0%';
                         spiral.style.width = '100%';
                         spiral.style.height = '100%';
                     } else if (imageId === 'face') {
                          // Align spiral origin near the eye/nose area, scale for head
                          // This is a very subjective alignment for demonstration
                         spiral.style.transformOrigin = '50% 50%';
                         spiral.style.transform = 'scale(0.7) rotate(10deg)'; // Scale down, slight rotation
                         spiral.style.top = '15%'; // Position vertically
                         spiral.style.left = '25%'; // Position horizontally
                         spiral.style.width = '100%'; // Base width
                         spiral.style.height = '100%'; // Base height
                     }
                      // Ensure base styles are set after specific adjustments
                     spiral.style.position = 'absolute';
                     spiral.style.objectFit = 'contain';
                     spiral.style.pointerEvents = 'none';
                     spiral.style.transition = 'opacity var(--transition-speed) ease-in-out, transform var(--transition-speed) ease-in-out'; // Re-apply transition

                     // Initial state for animation (before 'visible' class)
                     spiral.style.opacity = 0; // Ensure hidden initially
                     // The scale(0.8) from CSS class handles the starting transform
                 };
                // Trigger onload manually if image is already cached
                if (img.complete) {
                    img.onload();
                }
             }
        });

        // Initial setup for explanation button text
        updateButtonText(explanationButton, explanationSection.style.display !== 'none');

    });
</script>