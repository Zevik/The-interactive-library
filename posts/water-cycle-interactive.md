---
title: "מסע המים הקסום: גלו את מחזור המים בטבע!"
english_slug: water-cycle-interactive
category: "מדע"
tags:
  - מים
  - טבע
  - גאוגרפיה
  - סביבה
  - אינטראקטיבי
  - סימולציה
---
# מחזור המים בטבע: הרפתקה אינטראקטיבית

המים – החומר שבלעדיו אין חיים! הם לא נחים לרגע, אלא נמצאים בתנועה מתמדת על פני כדור הארץ ומעליו, במסע קסום ונצחי המחבר בין אוקיינוסים אדירים, עננים מרחפים, נהרות זורמים ואדמה יבשה. הצטרפו אלינו למסע מרתק בעקבות טיפות המים, וגלו את הסודות של מחזור המים בטבע דרך חוויה אינטראקטיבית ומרהיבה!

<div id="water-cycle-diagram">
    <div id="sky"></div>
    <div id="sun"></div>
    <div id="clouds-container">
        <div class="cloud cloud-1"></div>
        <div class="cloud cloud-2"></div>
        <div class="cloud cloud-3"></div>
    </div>
     <div id="mountains"></div>
    <div id="land"></div>
    <div id="water">
        <div class="water-surface"></div>
    </div>


    <!-- Interactive Points -->
    <!-- Added numbers for clearer sequencing hint -->
    <div id="point-evaporation" class="interactive-point" data-stage="evaporation">1</div>
    <div id="point-condensation" class="interactive-point" data-stage="condensation">2</div>
    <div id="point-precipitation" class="interactive-point" data-stage="precipitation">3</div>
    <div id="point-collection" class="interactive-point" data-stage="collection">4</div>

    <div id="stage-label">
        <div class="label-text"></div>
        <div class="label-description"></div>
        <div class="label-arrow"></div>
    </div>

    <!-- Animation Layers -->
    <div id="evaporation-anim-layer" class="anim-layer"></div>
    <div id="precipitation-anim-layer" class="anim-layer"></div>
    <div id="runoff-anim-layer" class="anim-layer"></div>
</div>

<button id="show-explanation-button">מעוניינים לדעת יותר? קראו את ההסבר המלא</button>

<div id="explanation">
    <h2>הסבר מעמיק: צלילה לשלבי מחזור המים</h2>
    <p>מחזור המים, הידרוספרה, הוא מערכת סגורה ומדהימה המניעה את המים על פני כדור הארץ. המסע האינסופי הזה מתרחש במספר שלבים מרכזיים, כל אחד חיוני לקיום המערכת כולה:</p>
    <ul>
        <li><strong>1. אידוי (Evaporation):</strong> הכל מתחיל בחום! אנרגיית השמש מחממת את פני השטח של אוקיינוסים, ימים, אגמים, נהרות ואפילו קרקע לחה. המים הנוזליים הופכים לאדי מים (מצב גזי) קלים, ועולים לאטמוספרה כחלק בלתי נראה מהאוויר שאנו נושמים. תהליך דומה מתרחש בצמחים (דיות - Transpiration).</li>
        <li><strong>2. התעבות (Condensation):</strong> ככל שאדי המים עולים גבוה יותר באטמוספרה, הם פוגשים אוויר קר יותר. הקור גורם להם להתעבות – לחזור למצב נוזלי (טיפות מים זעירות) או מוצק (גבישי קרח זעירים) סביב חלקיקים קטנטנים באוויר (כמו אבק או מלח). מיליארדי הטיפות/גבישים הללו מתאספים ויוצרים את העננים שאנו רואים בשמיים.</li>
        <li><strong>3. משקעים (Precipitation):</strong> כשהעננים מתמלאים באדי מים מתעבים והטיפות או גבישי הקרח גדלים וכבדים מספיק, הם כבר לא יכולים להישאר תלויים באוויר. כוח המשיכה מושך אותם מטה והם נופלים על פני כדור הארץ. צורת המשקעים משתנה בהתאם לטמפרטורה באטמוספרה – גשם, שלג, ברד או גשם קפוא.</li>
        <li><strong>4. איסוף וזרימה (Collection & Runoff):</strong> המים שמגיעים לקרקע מתחילים את חלקם הבא במסע. חלקם הגדול נופל ישירות לגופי מים קיימים (אוקיינוסים, אגמים, נהרות). חלק אחר נופל על היבשה – הוא יכול לחלחל (infiltration) לתוך האדמה ולהפוך למי תהום, או לזרום על פני השטח (runoff) ולחזור בהדרגה לנחלים, נהרות, אגמים, ובסופו של דבר לאוקיינוס, מוכן להתחיל את המחזור מחדש. צמחים גם קולטים חלק מהמים.</li>
    </ul>
    <p>מחזור המים הוא מנוע האקלים העולמי, הוא מעצב את הנוף, ומספק את המים המתוקים החיוניים לקיום כל צורות החיים על פני כדור הארץ. הקליקו על הנקודות בתרשים כדי לראות את השלבים בפעולה!</p>
</div>

<style>
    /* Global Styles & Container */
    #water-cycle-diagram {
        position: relative;
        width: 100%;
        max-width: 750px; /* Slightly wider */
        height: 450px; /* Slightly taller */
        margin: 40px auto;
        overflow: hidden;
        border-radius: 15px; /* More rounded corners */
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3); /* Stronger shadow */
        background: linear-gradient(to bottom, #7BDFF2 0%, #B2EBF2 70%, #E0FFFF 100%); /* Lighter, more vibrant sky */
        direction: ltr; /* Ensure points are positioned correctly regardless of page RTL */
        font-family: 'Arial', sans-serif; /* More refined font */
    }

    /* Background Elements - Layers */
    #sky {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 65%; /* Sky takes more space */
        background: linear-gradient(to bottom, #7BDFF2 0%, #B2EBF2 70%, #E0FFFF 100%);
        z-index: 0;
    }

    #sun {
        position: absolute;
        top: 30px;
        right: 30px;
        width: 60px; /* Bigger sun */
        height: 60px;
        background-color: #FFEB3B; /* Brighter yellow */
        border-radius: 50%;
        box-shadow: 0 0 30px 10px rgba(255, 235, 59, 0.7); /* Stronger glow */
        z-index: 1;
        animation: pulseGlow 3s infinite alternate ease-in-out; /* Subtle pulse animation */
    }

    @keyframes pulseGlow {
        0% { box-shadow: 0 0 30px 10px rgba(255, 235, 59, 0.7); }
        100% { box-shadow: 0 0 40px 15px rgba(255, 235, 59, 0.9); }
    }

    #mountains {
        position: absolute;
        bottom: 35%; /* Adjust based on new sky/land height */
        left: 0;
        width: 100%;
        height: 35%; /* Taller mountains */
        background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 350" preserveAspectRatio="none"><path fill="%23795548" d="M0 350 L100 150 L180 300 L250 50 L330 250 L400 0 L480 200 L550 0 L630 180 L700 50 L780 280 L850 80 L920 300 L1000 100 V350 Z" /></svg>') repeat-x bottom;
        background-size: auto 100%;
        z-index: 2;
    }
     #mountains::before { /* Darker base */
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 50%; /* Covers bottom half of mountains */
        background-color: #8D6E63; /* Slightly darker brown */
        z-index: -1; /* Behind the SVG mountains */
     }


    #land {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 40%; /* Land meets water */
        background-color: #8BC34A; /* Brighter green */
        z-index: 3;
    }
     /* Removed linear gradient transition, water/land edge is sharper */


    #water {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 35%; /* Base water level */
        background-color: #03A9F4; /* Vibrant blue */
        z-index: 4;
        overflow: hidden; /* Contain ripples */
    }
    .water-surface {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 10px; /* Thin layer for ripples */
        background: rgba(255, 255, 255, 0.3);
        filter: blur(2px);
        animation: waterRipple 5s linear infinite;
        z-index: 5; /* Above main water color */
    }
    @keyframes waterRipple {
        0% { transform: translateX(0) scaleY(1); }
        50% { transform: translateX(20px) scaleY(1.1); }
        100% { transform: translateX(0) scaleY(1); }
    }


    #clouds-container { /* Renamed for clarity */
        position: absolute;
        top: 10%;
        left: 0;
        width: 100%;
        height: 25%; /* Slightly taller cloud area */
        z-index: 5;
        pointer-events: none; /* Don't block clicks on points */
    }

    .cloud {
        position: absolute;
        background: #ffffff;
        border-radius: 50%;
        filter: drop-shadow(0 5px 8px rgba(0, 0, 0, 0.15));
        animation: moveClouds 25s linear infinite alternate; /* Slower, smoother movement */
        opacity: 0.9;
    }
    .cloud::before, .cloud::after {
        content: '';
        position: absolute;
        background: #ffffff;
        border-radius: 50%;
    }

    .cloud-1 {
        width: 120px; height: 50px; left: 10%; top: 20px; animation-duration: 28s; opacity: 0.95;
    }
    .cloud-1::before { width: 70px; height: 70px; top: -20px; left: 20px; }
    .cloud-1::after { width: 50px; height: 50px; top: -10px; right: 20px; }

    .cloud-2 {
        width: 150px; height: 60px; left: 40%; top: 10px; animation-duration: 25s; animation-delay: 5s;
    }
     .cloud-2::before { width: 90px; height: 90px; top: -30px; left: 30px; }
    .cloud-2::after { width: 60px; height: 60px; top: -15px; right: 30px; }


    .cloud-3 {
        width: 110px; height: 45px; left: 70%; top: 30px; animation-duration: 30s; animation-delay: 10s; opacity: 0.85;
    }
     .cloud-3::before { width: 60px; height: 60px; top: -15px; left: 15px; }
    .cloud-3::after { width: 40px; height: 40px; top: -5px; right: 15px; }


    @keyframes moveClouds {
        0% { transform: translateX(0); }
        100% { transform: translateX(80px); } /* Move further */
    }

    /* Interactive Points - Enhanced Styling */
    .interactive-point {
        position: absolute;
        width: 35px; /* Bigger points */
        height: 35px;
        background-color: rgba(255, 255, 255, 0.9); /* More opaque */
        border-radius: 50%;
        cursor: pointer;
        z-index: 10;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 18px; /* Bigger number */
        font-weight: bold;
        color: #333;
        border: 3px solid rgba(0, 0, 0, 0.2); /* Thicker border */
        transition: transform 0.3s ease, background-color 0.3s ease, border-color 0.3s ease;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3); /* Stronger shadow */
    }

    .interactive-point:hover {
        transform: scale(1.3); /* More pronounced hover effect */
        background-color: #ffffff;
        border-color: #007bff; /* Highlight color */
    }

    /* Add a subtle pulse animation to points when a stage is active */
    .interactive-point.active {
        animation: pulsePoint 1.5s infinite ease-in-out;
    }

    @keyframes pulsePoint {
        0% { box-shadow: 0 0 10px rgba(0, 123, 255, 0.6), 0 4px 10px rgba(0,0,0,0.3); }
        50% { box-shadow: 0 0 20px rgba(0, 123, 255, 0.9), 0 4px 10px rgba(0,0,0,0.3); }
        100% { box-shadow: 0 0 10px rgba(0, 123, 255, 0.6), 0 4px 10px rgba(0,0,0,0.3); }
    }


    /* Positioning points (relative to diagram container) */
    #point-evaporation { bottom: 28%; left: 15%; } /* Over water, slightly higher */
    #point-condensation { top: 20%; left: 40%; } /* Near clouds, higher */
    #point-precipitation { top: 38%; left: 60%; } /* Under clouds, lower */
    #point-collection { bottom: 18%; right: 15%; } /* On land/near water, adjusted */


    /* Stage Label - Enhanced Styling */
    #stage-label {
        position: absolute;
        background-color: rgba(0, 0, 0, 0.85); /* Darker, more opaque */
        color: white;
        padding: 12px 18px; /* More padding */
        border-radius: 8px; /* More rounded */
        font-size: 15px; /* Slightly larger font */
        line-height: 1.5;
        text-align: center;
        white-space: normal; /* Allow wrapping */
        max-width: 200px; /* Limit width */
        pointer-events: none;
        opacity: 0;
        transition: opacity 0.4s ease; /* Slower fade */
        transform: translate(-50%, -10px); /* Position above point, slight offset */
        transform-origin: bottom center; /* For potential scaling/animation */
        z-index: 15;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }
     #stage-label.visible { opacity: 1; }

     /* Arrow pointer */
    .label-arrow {
        position: absolute;
        bottom: -10px; /* Position below the label box */
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 0;
        border-left: 10px solid transparent;
        border-right: 10px solid transparent;
        border-top: 10px solid rgba(0, 0, 0, 0.85); /* Match label background */
    }

     .label-text {
        font-weight: bold;
        margin-bottom: 5px;
         font-size: 16px;
     }
     .label-description {
        font-size: 13px;
     }


    /* Animation Layers */
    .anim-layer {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 8; /* Below points, above diagram elements */
        pointer-events: none; /* Don't block clicks */
    }

    /* Animation Styles - Enhanced Particles */
    /* Evaporation particles: Water droplets turning to vapor, rising */
    @keyframes evaporateAnim {
        0% { transform: translate(0, 0) scale(1); opacity: 1; background-color: rgba(255, 255, 255, 0.8); }
        50% { background-color: rgba(255, 255, 255, 0.6); }
        100% { transform: translate(var(--travelX), var(--travelY)) scale(0.5); opacity: 0; background-color: rgba(255, 255, 255, 0.3); }
    }
    .evaporation-particle {
        position: absolute;
        width: 6px; /* Bigger particle */
        height: 6px;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 50%;
        animation: evaporateAnim var(--duration) ease-out forwards;
    }

     /* Precipitation particles: Rain drops falling */
     @keyframes rainAnim {
        0% { transform: translate(0, 0) scaleY(1); opacity: 1; }
        100% { transform: translate(var(--travelX), var(--travelY)) scaleY(0.5); opacity: 0; }
    }
    .precipitation-drop {
        position: absolute;
        width: 3px; /* Wider drop */
        height: 12px; /* Longer drop */
        background-color: rgba(3, 169, 244, 0.8); /* Match water blue */
        border-radius: 3px;
        animation: rainAnim var(--duration) linear forwards; /* Linear movement for rain */
        transform-origin: top center;
    }

    /* Runoff particles: Water flowing over land */
    @keyframes runoffAnim {
        0% { transform: translate(0, 0) scaleX(1); opacity: 1; }
        100% { transform: translate(var(--travelX), var(--travelY)) scaleX(0.5); opacity: 0; }
    }
     .runoff-flow {
        position: absolute;
        width: 15px; /* Wider flow segment */
        height: 6px; /* Taller flow segment */
        background-color: rgba(3, 169, 244, 0.7); /* Match water blue, slightly transparent */
        border-radius: 4px;
        animation: runoffAnim var(--duration) ease-in forwards; /* Accelerate slightly */
     }


    /* Explanation Section */
    #show-explanation-button {
        display: block;
        margin: 30px auto; /* More space */
        padding: 12px 25px; /* More padding */
        font-size: 17px; /* Larger font */
        cursor: pointer;
        border: none;
        border-radius: 6px; /* More rounded */
        background-color: #007bff; /* Primary blue */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    #show-explanation-button:hover {
        background-color: #0056b3; /* Darker blue on hover */
    }
     #show-explanation-button:active {
        transform: scale(0.98); /* Press effect */
     }

    #explanation {
        margin-top: 25px; /* More space */
        padding: 25px; /* More padding */
        border: 1px solid #ccc; /* Lighter border */
        border-radius: 10px; /* More rounded */
        background-color: #e1f5fe; /* Light blue background */
        color: #333;
        font-size: 15px;
        line-height: 1.7; /* Improved readability */
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }

    #explanation h2 {
        margin-top: 0;
        color: #0288D1; /* Darker blue heading */
        border-bottom: 2px solid #B3E5FC; /* Underline */
        padding-bottom: 10px;
        margin-bottom: 15px;
    }
    #explanation ul {
        padding-right: 25px; /* Adjust for Hebrew list style */
        margin-bottom: 15px;
    }
    #explanation li {
        margin-bottom: 12px; /* More space between list items */
        line-height: 1.6;
    }
     #explanation strong {
        color: #01579B; /* Darkest blue for stage names */
     }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const points = document.querySelectorAll('.interactive-point');
        const stageLabel = document.getElementById('stage-label');
        const labelText = stageLabel.querySelector('.label-text');
        const labelDescription = stageLabel.querySelector('.label-description');
        const explanationButton = document.getElementById('show-explanation-button');
        const explanationDiv = document.getElementById('explanation');

        const evaporationAnimLayer = document.getElementById('evaporation-anim-layer');
        const precipitationAnimLayer = document.getElementById('precipitation-anim-layer');
        const runoffAnimLayer = document.getElementById('runoff-anim-layer');

        // Get diagram bounds for animation positioning
        const diagram = document.getElementById('water-cycle-diagram');
        let diagramRect = diagram.getBoundingClientRect();

        // Update diagram bounds on window resize
        window.addEventListener('resize', () => {
            diagramRect = diagram.getBoundingClientRect();
        });


        const stageNames = {
            evaporation: 'אידוי',
            condensation: 'התעבות',
            precipitation: 'משקעים',
            collection: 'איסוף וזרימה'
        };

        const stageDescriptions = {
            evaporation: 'השמש מחממת מים והם הופכים לאדי מים בלתי נראים שעולים לאטמוספרה.',
            condensation: 'אדי המים הקרים מתעבים לטיפות זעירות שיוצרות עננים.',
            precipitation: 'כשהעננים כבדים, מים נופלים בחזרה לאדמה כגשם, שלג או ברד.',
            collection: 'המים שנאספים זורמים על פני השטח או מחלחלים לקרקע, וחוזרים לגופי מים גדולים.'
        };

        function showLabel(element, name, description) {
            const rect = element.getBoundingClientRect();
            const diagramRect = diagram.getBoundingClientRect();

            // Position relative to the diagram container
            const pointCenterX = rect.left - diagramRect.left + rect.width / 2;
            const pointTop = rect.top - diagramRect.top;

            labelText.textContent = name;
            labelDescription.textContent = description;

            stageLabel.style.left = pointCenterX + 'px';
            stageLabel.style.top = pointTop + 'px';
            stageLabel.classList.add('visible'); // Use class for opacity transition

            // Calculate translation after content is set for accurate centering
             // Using setTimeout with 0 allows the DOM to update first
             setTimeout(() => {
                // Adjust top position based on label height to place it nicely above the point
                 const labelHeight = stageLabel.offsetHeight;
                 stageLabel.style.transform = `translate(-50%, -${labelHeight + 10}px)`; // 10px padding above point
                 // Adjust arrow position if needed (arrow is relative to label's bottom)
             }, 0);


            // Hide label after a few seconds or on next click
            // It will be hidden by clearLabel
        }

        function clearLabel() {
            stageLabel.classList.remove('visible');
            // Clear content after fade out
             setTimeout(() => {
                 labelText.textContent = '';
                 labelDescription.textContent = '';
             }, 400); // Match CSS transition duration
        }

        function clearAnimations() {
            evaporationAnimLayer.innerHTML = '';
            precipitationAnimLayer.innerHTML = '';
            runoffAnimLayer.innerHTML = '';
             // Remove active class from all points
             points.forEach(p => p.classList.remove('active'));
        }

        function triggerAnimation(stage, startElement) {
             clearAnimations(); // Clear previous animations

            // Add active class to the current point
            startElement.classList.add('active');

            const startRect = startElement.getBoundingClientRect();
            const startX = (startRect.left - diagramRect.left) + startRect.width / 2;
            const startY = (startRect.top - diagramRect.top) + startRect.height / 2;

            switch (stage) {
                case 'evaporation':
                    // Animate particles rising from the water point towards clouds
                    const cloudHeight = diagramRect.height * 0.2; // Approximate cloud height
                    const waterTop = diagramRect.height * (1 - 0.35); // Approximate water top edge

                    for (let i = 0; i < 30; i++) { // More particles
                        const particle = document.createElement('div');
                        particle.classList.add('evaporation-particle');

                        // Start particle near the water point, with random spread
                        const startX = (document.getElementById('point-evaporation').getBoundingClientRect().left - diagramRect.left) + (Math.random() - 0.5) * 30; // Spread around evaporation point
                        const startY = waterTop + (Math.random() * 20); // Start slightly above or at water top

                        // Target the general cloud area
                        const targetX = (diagramRect.width * (0.3 + Math.random() * 0.4)); // Random X across cloud area
                        const targetY = diagramRect.height * (0.1 + Math.random() * 0.15); // Random Y within cloud height area

                        particle.style.left = startX + 'px';
                        particle.style.top = startY + 'px';
                        particle.style.setProperty('--travelX', (targetX - startX) + 'px');
                        particle.style.setProperty('--travelY', (targetY - startY) + 'px');


                        particle.style.animationDuration = (3 + Math.random() * 1.5) + 's'; // Longer duration
                        particle.style.animationDelay = (Math.random() * 1.5) + 's';
                        evaporationAnimLayer.appendChild(particle);

                        // Remove particle after animation finishes
                        particle.addEventListener('animationend', () => {
                            particle.remove();
                        });
                    }
                    break;

                case 'condensation':
                    // No particle animation representing condensation itself in this setup.
                    // The clouds are the visual representation.
                    // Maybe add a subtle pulse or shake to the clouds?
                    // Let's just rely on the label and the static cloud visuals for now.
                     console.log('Condensation triggered - clouds are forming!'); // Placeholder
                    break;

                case 'precipitation':
                     // Animate drops falling from the general cloud area towards land/water
                    const cloudBottom = diagramRect.height * 0.35; // Approximate cloud bottom edge
                    const groundTop = diagramRect.height * 0.6; // Approximate land/water top edge

                    for (let i = 0; i < 50; i++) { // Many drops
                        const drop = document.createElement('div');
                        drop.classList.add('precipitation-drop');

                        // Start drop from random point across cloud width/bottom area
                        const startX = (diagramRect.width * (0.2 + Math.random() * 0.6)); // Spread across diagram width
                        const startY = diagramRect.height * (0.2 + Math.random() * 0.15); // Start within cloud vertical range

                         // Target random point on the lower part of the diagram
                        const targetX = startX + (Math.random() - 0.5) * 50; // Slight horizontal drift
                        const targetY = diagramRect.height * (0.8 + Math.random() * 0.15); // Target land/water area

                        drop.style.left = startX + 'px';
                        drop.style.top = startY + 'px';
                        drop.style.setProperty('--travelX', (targetX - startX) + 'px');
                        drop.style.setProperty('--travelY', (targetY - startY) + 'px');


                        drop.style.animationDuration = (1 + Math.random() * 1) + 's'; // Varied speed
                        drop.style.animationDelay = (Math.random() * 1) + 's'; // Staggered start
                        precipitationAnimLayer.appendChild(drop);

                         // Remove drop after animation finishes
                        drop.addEventListener('animationend', () => {
                            drop.remove();
                        });
                    }
                    break;

                 case 'collection':
                     // Animate flow from the collection point towards water
                    const collectionPoint = document.getElementById('point-collection');
                    const waterElement = document.getElementById('water');
                    const waterRect = waterElement.getBoundingClientRect();
                    const waterLeft = waterRect.left - diagramRect.left;
                    const waterTop = waterRect.top - diagramRect.top;

                    for (let i = 0; i < 25; i++) { // More flow particles
                        const flow = document.createElement('div');
                        flow.classList.add('runoff-flow');

                        // Start flow near the collection point, with some spread
                        const startX = startX + (Math.random() - 0.5) * 20;
                        const startY = startY + (Math.random() - 0.5) * 20;

                        // Target a point within the water body
                        const targetX = waterLeft + (Math.random() * waterRect.width * 0.8); // Target anywhere in the water width
                        const targetY = waterTop + (Math.random() * waterRect.height * 0.8); // Target anywhere in the water height

                        flow.style.left = startX + 'px';
                        flow.style.top = startY + 'px';
                         flow.style.setProperty('--travelX', (targetX - startX) + 'px');
                        flow.style.setProperty('--travelY', (targetY - startY) + 'px');


                         flow.style.animationDuration = (2 + Math.random() * 1) + 's';
                        flow.style.animationDelay = (Math.random() * 0.8) + 's';
                        runoffAnimLayer.appendChild(flow);

                        // Remove flow after animation finishes
                        flow.addEventListener('animationend', () => {
                            flow.remove();
                        });
                    }
                    break;
            }
        }

        points.forEach(point => {
            point.addEventListener('click', function() {
                const stage = this.dataset.stage;
                // Hide explanation if visible? Or let it stay? Let's let it stay.
                clearLabel(); // Clear previous label instantly
                showLabel(this, stageNames[stage], stageDescriptions[stage]);
                triggerAnimation(stage, this); // Pass the clicked element
            });
        });

        explanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            explanationButton.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'מעוניינים לדעת יותר? קראו את ההסבר המלא';
        });

        // Ensure explanation is hidden on load
        explanationDiv.style.display = 'none';
    });
</script>