---
title: "הדמיה של פעולת האנזים - מודל מנעול ומפתח"
english_slug: enzyme-lock-and-key-simulation
category: "ביולוגיה"
tags: [אנזימים, קינטיקה, מודלים ביולוגיים, הדמיה]
---
# מסע מולקולרי: הדמיית פעולת האנזים במודל "מנעול ומפתח"

צאו למסע מיניאטורי אל תוך עולם הביולוגיה המולקולרית וגלו את הסוד שמאפשר לאנזימים לבצע את קסמם! אנזימים הם זרזים ביולוגיים מופלאים שמניעים אלפי תהליכים כימיים חיוניים בגופנו בקצב מדהים. אבל איך הם יודעים בדיוק על אילו מולקולות ספציפיות לפעול? הדמיה אינטראקטיבית זו תעזור לכם לגלות את התשובה, באמצעות מודל "המנעול והמפתח".

<div id="simulation-container">
    <div id="environment">
        <!-- Environmental particles/background elements can be added here -->
    </div>
    <div id="enzyme">
        <div id="active-site">
            <div id="active-site-notch"></div>
        </div>
        <div class="molecule-label enzyme-label">אנזים</div>
    </div>
    <div id="substrate">
        <div id="substrate-key"></div>
        <div class="molecule-label substrate-label">סובסטרט</div>
    </div>
     <div id="product1" class="product"></div>
     <div id="product2" class="product"></div>
     <div class="molecule-label complex-label">קומפלקס אנזים-סובסטרט</div>
     <div class="molecule-label products-label">תוצרים</div>

</div>

<div class="controls">
    <button id="start-simulation">התחל הדמיה</button>
    <button id="reset-simulation">איפוס</button>
</div>

<button id="toggle-explanation" class="explanation-button">הצג הסבר</button>
<div id="explanation" style="display: none;">
    <h2>הסבר מעמיק: מודל מנעול ומפתח בפעולת האנזים</h2>
    <p>מודל "המנעול והמפתח", שהוצע על ידי אמיל פישר בסוף המאה ה-19, הוא אנלוגיה קלאסית שמסבירה את הספציפיות המדהימה של אנזימים. למרות שמודל "התאמה מושרית" עדכני יותר ומסביר טוב יותר את הדינמיקה של האנזים, מודל "המנעול והמפתח" הוא נקודת פתיחה נהדרת להבנת העיקרון הבסיסי:</p>
    <ul>
        <li><strong class="enzyme-color">האנזים</strong> מדמה את ה"מנעול". יש לו אזור מיוחד וקריטי הנקרא <strong>האתר הפעיל</strong>. צורתו התלת-ממדית של האתר הפעיל קבועה ומדויקת, בדומה לחריץ במנעול שמיועד למפתח ספציפי.</li>
        <li><strong class="substrate-color">הסובסטרט</strong> (מולקולת המטרה) מדמה את ה"מפתח". לסובסטרט יש צורה ופיזור מטענים חשמליים המותאמים באופן מדויק ומשלים לצורת האתר הפעיל של האנזים.</li>
        <li>רק סובסטרט בעל התאמה מבנית מושלמת לאתר הפעיל יכול להיקשר אליו. קישור זה יוצר מבנה זמני הנקרא <strong>קומפלקס אנזים-סובסטרט</strong>.</li>
        <li>בתוך הקומפלקס, האנזים מזרז את התגובה הכימית, הופך את הסובסטרט ל<strong>תוצר(ים)</strong>.</li>
        <li>לאחר השלמת התגובה, ה<strong>תוצר(ים)</strong>, שכבר אינם מתאימים לצורת האתר הפעיל (כמו מפתח שבור), משתחררים מהאנזים.</li>
        <li>האנזים נשאר ללא שינוי בסוף התגובה והוא מוכן לקשור מולקולת סובסטרט חדשה ולזרז את התגובה שוב ושוב.</li>
    </ul>
    <p>הדמיה זו ממחישה כיצד ההתאמה המבנית, כמו בין מנעול למפתח, היא המפתח לספציפיות של האנזים וליכולתו לזרז רק תגובות ספציפיות.</p>
</div>

<style>
/* הגדרות כלליות וצבעים */
:root {
    --enzyme-color: #4CAF50; /* Green */
    --substrate-color: #FF9800; /* Orange */
    --product-color-1: #03A9F4; /* Light Blue */
    --product-color-2: #9C27B0; /* Purple */
    --container-bg: #e8f5e9; /* Light Green background */
    --border-color: #a5d6a7; /* Slightly darker green */
    --text-color: #333;
    --button-primary: #1b5e20; /* Dark Green */
    --button-secondary: #c62828; /* Dark Red */
    --button-info: #fbc02d; /* Dark Yellow */
    --shadow-color: rgba(0, 0, 0, 0.2);
}

body {
    font-family: 'Arial', sans-serif;
    color: var(--text-color);
}

#simulation-container {
    position: relative;
    width: 95%; /* Responsive width */
    max-width: 600px; /* Max width for desktop */
    height: 300px; /* Increased height for better spacing */
    border: 2px solid var(--border-color);
    border-radius: 12px;
    margin: 20px auto; /* Center container */
    background: radial-gradient(circle at top left, var(--container-bg), #c8e6c9); /* Subtle gradient */
    overflow: hidden; /* Hide elements outside */
    box-shadow: 0 8px 16px var(--shadow-color);
}

#environment {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    /* Add subtle background patterns or particles here if desired */
}

#enzyme {
    position: absolute;
    left: 15%; /* Enzyme position */
    top: 50%;
    transform: translateY(-50%);
    width: 180px; /* Larger size */
    height: 120px;
    background: linear-gradient(to right, var(--enzyme-color), #66bb6a); /* Gradient fill */
    border-radius: 25px; /* Softer corners */
    display: flex;
    justify-content: flex-end; /* Position active site on the right */
    align-items: center;
    box-shadow: 4px 4px 12px var(--shadow-color);
    border: 2px solid #388e3c; /* Darker green border */
}

#active-site {
    width: 60px; /* Larger active site */
    height: 80px;
    background-color: rgba(255, 255, 255, 0.9); /* Slightly transparent white */
    border-radius: 0 25px 25px 0; /* Rounded only on the right */
    position: relative;
    overflow: hidden;
    box-shadow: inset 3px 0 8px rgba(0,0,0,0.1); /* Inner shadow for depth */
}

#active-site-notch {
    position: absolute;
    top: 50%;
    left: -15px; /* Position relative to active site edge */
    transform: translateY(-50%);
    width: 30px; /* Size of the notch */
    height: 50px; /* Height of the notch */
    background-color: var(--enzyme-color); /* Same as enzyme body */
    border-radius: 50%; /* Circular notch */
    box-shadow: inset 2px 0 5px rgba(0,0,0,0.1);
}


#substrate {
    position: absolute;
    right: 15%; /* Start position on the right */
    top: 50%;
    transform: translateY(-50%);
    width: 70px; /* Larger substrate */
    height: 70px;
    background: linear-gradient(to bottom right, var(--substrate-color), #fb8c00); /* Gradient */
    border-radius: 15px; /* Softer corners */
    box-shadow: 4px 4px 12px var(--shadow-color);
    border: 2px solid #f57c00; /* Darker orange border */
    transition: all 1.5s ease-in-out; /* Smooth animation */
    display: flex;
    justify-content: flex-start; /* Position key on the left */
    align-items: center;
    z-index: 1; /* Ensure substrate is above enzyme initially */
}

#substrate-key {
    width: 30px; /* Size of the key part */
    height: 50px; /* Height of the key part */
    background-color: var(--substrate-color); /* Same as substrate body */
     border-radius: 50%; /* Circular key */
     position: absolute;
     left: -15px; /* Position relative to substrate edge, matching notch offset */
     top: 50%;
     transform: translateY(-50%);
     box-shadow: inset -2px 0 5px rgba(0,0,0,0.1);
}


/* Product styling */
.product {
    position: absolute;
    width: 40px; /* Smaller product size */
    height: 40px;
    border-radius: 50%; /* Round products */
    box-shadow: 2px 2px 8px var(--shadow-color);
    opacity: 0; /* Initially hidden */
    transition: all 1s ease-in-out; /* Animation for movement */
    z-index: 0; /* Products behind labels/complex */
}

#product1 {
    background: linear-gradient(to bottom right, var(--product-color-1), #0288d1);
    border: 2px solid #0277bd;
}

#product2 {
    background: linear-gradient(to bottom right, var(--product-color-2), #8e24aa);
     border: 2px solid #7b1fa2;
}

/* Labels */
.molecule-label {
    position: absolute;
    bottom: -25px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 0.9em;
    color: var(--text-color);
    white-space: nowrap; /* Prevent line breaks */
    opacity: 0.8;
}

.complex-label, .products-label {
    opacity: 0; /* Initially hidden */
    transition: opacity 0.5s ease-in-out;
}


/* Simulation States (triggered by JS adding classes) */
#simulation-container.binding #substrate {
    z-index: 2; /* Bring substrate to front during binding */
}

#simulation-container.bound #substrate {
    opacity: 0; /* Hide substrate when complex forms */
}

#simulation-container.bound .complex-label {
    opacity: 1; /* Show complex label */
    bottom: 15px; /* Position maybe closer to the center */
}

#simulation-container.products-formed #product1,
#simulation-container.products-formed #product2 {
     opacity: 1; /* Show products */
     z-index: 2; /* Bring products to front during release */
}

#simulation-container.products-formed .complex-label {
    opacity: 0; /* Hide complex label */
}
#simulation-container.products-formed .products-label {
    opacity: 1; /* Show products label */
    bottom: 15px; /* Position maybe closer to the center */
}

/* Controls styling */
.controls {
    text-align: center;
    margin-top: 20px;
}

#start-simulation, #reset-simulation, .explanation-button {
    padding: 12px 20px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    margin: 0 5px;
    transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    font-weight: bold;
}

#start-simulation {
    background-color: var(--button-primary);
    color: white;
}
#start-simulation:hover:not(:disabled) {
    background-color: #2e7d32; /* Darker green */
    box-shadow: 0 5px 10px rgba(0,0,0,0.2);
}
#start-simulation:active:not(:disabled) {
    transform: scale(0.98);
}


#reset-simulation {
    background-color: var(--button-secondary);
    color: white;
}
#reset-simulation:hover:not(:disabled) {
     background-color: #d32f2f; /* Darker red */
     box-shadow: 0 5px 10px rgba(0,0,0,0.2);
}
#reset-simulation:active:not(:disabled) {
    transform: scale(0.98);
}


#start-simulation:disabled, #reset-simulation:disabled {
    opacity: 0.6;
    cursor: not-allowed;
    box-shadow: none;
}


.explanation-button {
    display: block; /* Takes full width if needed, or inline-block */
    width: fit-content; /* Adjust width based on content */
    margin: 20px auto 15px auto; /* Center button below simulation */
    background-color: var(--button-info);
    color: var(--text-color);
}
.explanation-button:hover {
    background-color: #fbc02d; /* Darker yellow */
     box-shadow: 0 5px 10px rgba(0,0,0,0.1);
}
.explanation-button:active {
    transform: scale(0.98);
}


#explanation {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 20px;
    background-color: #fff;
    line-height: 1.6;
    margin-top: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

#explanation h2 {
    margin-top: 0;
    color: var(--text-color);
    border-bottom: 1px solid #eee;
    padding-bottom: 10px;
    margin-bottom: 15px;
}

#explanation ul {
    margin-bottom: 15px;
    padding-left: 20px; /* Indent list items */
}

#explanation li {
    margin-bottom: 10px;
    padding-left: 5px;
}

#explanation strong {
    color: #555;
}

.enzyme-color { color: var(--enzyme-color); font-weight: bold;}
.substrate-color { color: var(--substrate-color); font-weight: bold;}

/* Responsive Adjustments */
@media (max-width: 600px) {
    #simulation-container {
        height: 250px;
    }
    #enzyme {
        width: 150px;
        height: 100px;
        left: 10%;
    }
    #active-site {
        width: 50px;
        height: 60px;
    }
    #active-site-notch {
         width: 25px;
         height: 40px;
         left: -12px;
    }
    #substrate {
        width: 60px;
        height: 60px;
        right: 10%;
    }
    #substrate-key {
         width: 25px;
         height: 40px;
         left: -12px;
    }
     .product {
        width: 35px;
        height: 35px;
     }
     .molecule-label {
        font-size: 0.8em;
     }
    .controls button {
        margin: 5px;
        padding: 10px 15px;
        font-size: 0.9em;
    }
}

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const simulationContainer = document.getElementById('simulation-container');
    const enzyme = document.getElementById('enzyme');
    const substrate = document.getElementById('substrate');
    const product1 = document.getElementById('product1');
    const product2 = document.getElementById('product2');
    const enzymeLabel = simulationContainer.querySelector('.enzyme-label');
    const substrateLabel = simulationContainer.querySelector('.substrate-label');
    const complexLabel = simulationContainer.querySelector('.complex-label');
    const productsLabel = simulationContainer.querySelector('.products-label');

    const startButton = document.getElementById('start-simulation');
    const resetButton = document.getElementById('reset-simulation');
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');

    // --- Configuration & Initial Positions ---
    // Get enzyme and substrate dimensions and positions dynamically for responsiveness
    const enzymeRect = enzyme.getBoundingClientRect();
    const substrateRect = substrate.getBoundingClientRect();
    const containerRect = simulationContainer.getBoundingClientRect();

    // Calculate the target position for the substrate's 'key' to align with the active site's 'notch'
    // This needs to be relative to the container or consistent with CSS positioning.
    // Enzyme left is 15% (or 10% on mobile). Enzyme width is 180px (or 150px).
    // Active site is on the right of the enzyme, width 60px (or 50px).
    // Active site left edge is enzyme.left + enzyme.width - activeSite.width
    // Notch left edge is at activeSite.left - 15px (or -12px) relative to active site div.
    // Substrate width is 70px (or 60px). Key left edge is at substrate.left - 15px (or -12px) relative to substrate div.
    // To align the key (substrate.left - 15) with the notch (activeSite.left),
    // substrate.left should be activeSite.left + 15px (approx).
    // Using CSS calculated values is tricky in JS. Let's use `getBoundingClientRect` for calculation *once* on load
    // and then apply CSS transitions based on these pixel values or relative values if possible.

    const enzymeLeftPx = enzymeRect.left - containerRect.left;
    const enzymeWidthPx = enzymeRect.width;
    const activeSiteWidthPx = enzyme.querySelector('#active-site').getBoundingClientRect().width;
    const notchOffsetPx = 15; // Matches CSS left value for #active-site-notch
    const keyOffsetPx = 15; // Matches CSS left value for #substrate-key
    const substrateWidthPx = substrateRect.width;

    // The left edge of the active site is at enzymeLeftPx + enzymeWidthPx - activeSiteWidthPx
    const activeSiteLeftPx = enzymeLeftPx + enzymeWidthPx - activeSiteWidthPx;

    // To align the substrate's key (which is keyOffsetPx LEFT of the substrate's left edge)
    // with the active site's notch (which is notchOffsetPx LEFT of the active site's left edge),
    // the substrate's left edge needs to be positioned such that:
    // substrate.left - keyOffsetPx = activeSiteLeftPx - notchOffsetPx
    // substrate.left = activeSiteLeftPx - notchOffsetPx + keyOffsetPx
    // Since notchOffsetPx and keyOffsetPx are the same (15), substrate.left should be approximately activeSiteLeftPx.
    // Let's target the substrate's left edge to be exactly where the active site's left edge is.
    const targetSubstrateLeftPx = activeSiteLeftPx;

    // Position products initially hidden at the active site location
    const productInitialLeftPx = activeSiteLeftPx + activeSiteWidthPx / 2 - product1.getBoundingClientRect().width / 2; // Center product within active site
    const productInitialTopPx = containerRect.height / 2 - product1.getBoundingClientRect().height / 2; // Vertically centered

    product1.style.left = `${productInitialLeftPx}px`;
    product1.style.top = `${productInitialTopPx}px`;
    product2.style.left = `${productInitialLeftPx}px`;
    product2.style.top = `${productInitialTopPx}px`;

    // Position labels
    const enzymeLabelInitialBottom = enzymeLabel.style.bottom;
    const substrateLabelInitialBottom = substrateLabel.style.bottom;
    const complexLabelTopPx = containerRect.height / 2 + enzymeRect.height / 2 - 10; // Below the complex area
    const productsLabelTopPx = containerRect.height / 2 + enzymeRect.height / 2 - 10; // Below the products area

     complexLabel.style.top = `${complexLabelTopPx}px`;
     complexLabel.style.left = '50%'; // Center horizontally
     complexLabel.style.transform = 'translateX(-50%)';
     complexLabel.style.bottom = 'auto'; // Clear initial bottom style

     productsLabel.style.top = `${productsLabelTopPx}px`;
     productsLabel.style.left = '50%'; // Center horizontally
     productsLabel.style.transform = 'translateX(-50%)';
     productsLabel.style.bottom = 'auto'; // Clear initial bottom style


    // --- Simulation Logic ---
    let isSimulating = false;

    function disableButtons() {
        startButton.disabled = true;
        resetButton.disabled = true;
        startButton.style.opacity = 0.6;
        resetButton.style.opacity = 0.6;
        startButton.style.cursor = 'not-allowed';
        resetButton.style.cursor = 'not-allowed';
    }

     function enableStartButton() {
        startButton.disabled = false;
        startButton.style.opacity = 1;
        startButton.style.cursor = 'pointer';
        resetButton.disabled = true;
        resetButton.style.opacity = 0.6;
        resetButton.style.cursor = 'not-allowed';
     }

     function enableResetButton() {
         startButton.disabled = true;
         startButton.style.opacity = 0.6;
         startButton.style.cursor = 'not-allowed';
         resetButton.disabled = false;
         resetButton.style.opacity = 1;
         resetButton.style.cursor = 'pointer';
     }


    function startSimulation() {
        if (isSimulating) return;
        isSimulating = true;
        disableButtons();

        // Step 1: Substrate moves towards the enzyme active site
        simulationContainer.classList.add('binding');
        substrate.style.right = 'auto'; // Clear right positioning
        substrate.style.left = `${targetSubstrateLeftPx}px`; // Move to calculated target left
        substrate.style.transition = 'left 1.5s ease-in-out, transform 1.5s ease-in-out'; // Apply transition

        // Step 2: Wait for binding (transition end) and form complex
        substrate.addEventListener('transitionend', handleBindingComplete, { once: true });
    }

    function handleBindingComplete() {
         simulationContainer.classList.remove('binding');
         simulationContainer.classList.add('bound'); // Indicate complex is formed

         // Vibrate or slightly change enzyme/substrate appearance? (CSS animations)
         // For now, just show the complex label and hide substrate label
         substrateLabel.style.opacity = 0;
         complexLabel.style.opacity = 1;


         // Step 3: Simulate reaction time
         setTimeout(simulateReaction, 1000); // Wait for 1 second
    }

    function simulateReaction() {
        simulationContainer.classList.remove('bound');
        simulationContainer.classList.add('products-formed'); // Indicate products are formed

        // Hide substrate (already done by .bound) and complex label
        complexLabel.style.opacity = 0;

        // Show products at the active site location
        product1.style.opacity = 1;
        product2.style.opacity = 1;
         productsLabel.style.opacity = 1;

        // Step 4: Products detach and move away
        setTimeout(releaseProducts, 500); // Small pause before release
    }

    function releaseProducts() {
         // Animate products moving away
         const releaseDistance = 150; // Pixels to move away
         const releaseAngle1 = 45; // Degrees for product 1
         const releaseAngle2 = -45; // Degrees for product 2

         const radians1 = releaseAngle1 * Math.PI / 180;
         const radians2 = releaseAngle2 * Math.PI / 180;

         const product1TargetLeft = productInitialLeftPx + releaseDistance * Math.cos(radians1);
         const product1TargetTop = productInitialTopPx + releaseDistance * Math.sin(radians1);

         const product2TargetLeft = productInitialLeftPx + releaseDistance * Math.cos(radians2);
         const product2TargetTop = productInitialTopPx + releaseDistance * Math.sin(radians2);


         product1.style.left = `${product1TargetLeft}px`;
         product1.style.top = `${product1TargetTop}px`;
         product1.style.transition = 'all 1.5s ease-out';

         product2.style.left = `${product2TargetLeft}px`;
         product2.style.top = `${product2TargetTop}px`;
         product2.style.transition = 'all 1.5s ease-out';

         // Wait for products to move away, then reset
         product1.addEventListener('transitionend', handleReleaseComplete, { once: true });
         product2.addEventListener('transitionend', handleReleaseComplete, { once: true }); // Listen to both for safety, but {once:true} ensures it only runs once overall

         // Need a counter or flag to ensure cleanup runs only after *both* products have finished transitioning
         let releaseCount = 0;
         function handleReleaseComplete() {
             releaseCount++;
             if (releaseCount === 2) { // Assuming 2 products
                 setTimeout(resetSimulation, 500); // Small delay before full reset
             }
         }
    }


    function resetSimulation() {
        isSimulating = false;
        simulationContainer.classList.remove('binding', 'bound', 'products-formed');

        // Reset substrate position and visibility
        substrate.style.left = 'auto'; // Clear calculated left
        substrate.style.right = getComputedStyle(document.documentElement).getPropertyValue('--initial-substrate-right') || '15%'; // Reset to initial right (or CSS var)
        substrate.style.top = '50%'; // Ensure vertical alignment is reset
        substrate.style.transform = 'translateY(-50%)'; // Ensure vertical alignment is reset
        substrate.style.opacity = 1; // Make substrate visible
        substrate.style.transition = 'none'; // Disable transition immediately for reset

        // Hide and reset products position
        product1.style.opacity = 0;
        product2.style.opacity = 0;
         product1.style.left = `${productInitialLeftPx}px`;
         product1.style.top = `${productInitialTopPx}px`;
         product2.style.left = `${productInitialLeftPx}px`;
         product2.style.top = `${productInitialTopPx}px`;
         product1.style.transition = 'none'; // Disable transition immediately for reset
         product2.style.transition = 'none'; // Disable transition immediately for reset


        // Reset labels
        substrateLabel.style.opacity = 1;
        complexLabel.style.opacity = 0;
        productsLabel.style.opacity = 0;


        // Reset transition property on substrate after a brief moment to allow immediate reset
        setTimeout(() => {
            substrate.style.transition = 'all 1.5s ease-in-out'; // Re-enable transition for next simulation
             product1.style.transition = 'all 1s ease-in-out'; // Re-enable transition for products
             product2.style.transition = 'all 1s ease-in-out'; // Re-enable transition for products
        }, 50); // Small delay


        enableStartButton(); // Allow starting again
    }

    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר' : 'הצג הסבר';
    }

    // Add event listeners
    startButton.addEventListener('click', startSimulation);
    resetButton.addEventListener('click', resetSimulation);
    toggleButton.addEventListener('click', toggleExplanation);

    // Initialize button states and simulation elements
    enableStartButton(); // Only start is active initially

    // Store initial substrate right position as a CSS variable for robust reset
    // This requires accessing the computed style, which is tricky with percentage/calc
    // A simpler approach for reset is to just set right: '15%' (or 10% on mobile) as per CSS
     // Let's add a CSS variable to the root or container for this
     document.documentElement.style.setProperty('--initial-substrate-right', getComputedStyle(substrate).right);

     // Initial state - hide products and complex labels
    product1.style.opacity = 0;
    product2.style.opacity = 0;
    complexLabel.style.opacity = 0;
    productsLabel.style.opacity = 0;


});
</script>