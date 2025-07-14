---
title: "מסעו המדהים של שבב הסיליקון: כך מייצרים מוח דיגיטלי זעיר"
english_slug: the-amazing-journey-of-a-silicon-chip-making-a-tiny-digital-brain
category: "הנדסת חשמל"
tags: [שבבים, סיליקון, פוטוליתוגרפיה, מיקרואלקטרוניקה, ייצור]
---
<h1>מסעו המדהים של שבב הסיליקון: כך מייצרים מוח דיגיטלי זעיר</h1>
<p>איך מצליחים לדחוס מיליארדי רכיבים זעירים על פיסת סיליקון קטנה יותר מציפורן? זה נשמע כמו קסם, אבל מדובר בתהליך הנדסי מורכב ומדויק להפליא. בואו נצא למסע ונגלה את סוד הייצור, שלב אחר שלב.</p>

<div id="simulation-app">
    <h2>סימולטור תהליך הפוטוליתוגרפיה</h2>
    <p>לחצו על "השלב הבא" כדי לראות כיצד מעתיקים דפוסים זעירים על הסיליקון.</p>
    <div id="simulation-container">
        <div id="wafer" class="layer"></div>
        <div id="photoresist" class="layer"></div>
        <div id="mask" class="layer">
            <div id="mask-pattern"></div>
        </div>
        <div id="uv-light" class="layer"></div>
         <div id="developer-fluid" class="overlay"></div>
         <div id="etching-gas" class="overlay"></div>
    </div>
    <p id="step-text"></p>
    <button id="next-step-button">השלב הבא</button>
</div>

<style>
    /* כללים כלליים ועיצוב בסיסי */
    #simulation-app {
        max-width: 650px; /* קצת יותר רחב לנראות טובה יותר */
        margin: 30px auto;
        border: 1px solid #d0d0d0;
        padding: 25px;
        border-radius: 12px; /* פינות מעוגלות יותר */
        text-align: center;
        background-color: #ffffff; /* רקע לבן ונקי */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* צל עדין */
        font-family: 'Arial', sans-serif; /* פונט נקי */
        color: #333;
    }

    #simulation-app h2 {
        color: #0056b3; /* כותרת בצבע מותג */
        margin-top: 0;
        font-size: 1.8em;
    }
     #simulation-app p {
         font-size: 1.1em;
         line-height: 1.6;
     }

    #simulation-container {
        position: relative;
        width: 95%; /* רוחב כמעט מלא */
        height: 250px; /* גובה מוגדל */
        border: 2px solid #a0a0a0; /* גבול עדין יותר */
        overflow: hidden; /* לוודא שהשכבות נשארות בפנים */
        margin: 20px auto; /* ממורכז עם מרווחים */
        background-color: #eef2f7; /* רקע בהיר ותכלכל עדין */
        border-radius: 8px;
        display: flex;
        justify-content: center;
        align-items: flex-end; /* Stack from the bottom */
    }

    /* שכבות הסימולציה */
    .layer {
        position: absolute;
        bottom: 0; /* Stack from the bottom */
        left: 50%; /* Center horizontally */
        transform: translateX(-50%) scaleY(1); /* התחלה ממורכזת */
        width: 90%; /* רוחב רלטיבי */
        box-sizing: border-box;
        transition: all 0.8s ease-in-out, background 0.8s ease-in-out; /* אנימציות מעבר חלקות */
        transform-origin: bottom center; /* Animation origin */
    }

    #wafer {
        height: 40px;
        background-color: #b8b8d1; /* צבע סיליקון */
        border-radius: 5px 5px 0 0; /* פינות עליונות מעוגלות */
        box-shadow: inset 0 3px 5px rgba(0,0,0,0.2); /* צל פנימי עדין */
        z-index: 1; /* שכבה תחתונה */
    }

    #photoresist {
        height: 35px; /* עובי קצת שונה */
        background-color: #f7a540; /* צבע Photoresist */
        z-index: 2; /* מעל ה-Wafer */
        opacity: 0; /* מתחיל מוסתר */
        bottom: 40px; /* מיקום התחלתי מעל ה-wafer */
        transform: translateX(-50%) scaleY(0); /* Start scaled down */
    }

    #mask {
        bottom: calc(40px + 35px + 20px); /* מיקום גבוה יותר, מעל Photoresist עם מרווח */
        height: 80px; /* גובה המסיכה */
        width: 85%; /* המסיכה יכולה להיות קצת שונה ברוחב */
        background-color: rgba(50, 50, 50, 0.9); /* צבע מסיכה כהה ואטום */
        border-radius: 4px;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 3; /* מעל Photoresist */
        opacity: 0; /* מתחיל מוסתר */
        transform: translateX(-50%) translateY(-50px); /* מתחיל גבוה יותר */
    }

    #mask-pattern {
         width: 40%; /* גודל הדפוס */
         height: 60%; /* גודל הדפוס */
         background-color: rgba(255, 255, 255, 0.1); /* שטח שקוף במסיכה - נראה בהיר יותר */
         border: 2px solid #ccc; /* תוחם את אזור הדפוס */
         box-shadow: inset 0 0 10px rgba(255,255,255,0.5); /* אפקט זריחה בשטח השקוף */
    }

    #uv-light {
        bottom: calc(40px + 35px); /* מתחיל בגובה Photoresist */
        height: 150px; /* יורד כלפי מטה */
        width: 80%; /* רוחב האור */
        background: linear-gradient(to bottom, rgba(255, 255, 0, 0.8), rgba(255, 255, 0, 0.2)); /* gradient צהוב חזק יותר למעלה */
        opacity: 0; /* מתחיל מוסתר */
        transition: opacity 0.4s ease-out; /* אנימציית הופעה מהירה יותר */
        z-index: 4; /* מעל הכל בזמן החשיפה */
        pointer-events: none; /* לא מפריע ללחיצות */
    }

     /* אפקטים של נוזל או גז מעל הסימולציה */
     .overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 150, 255, 0.2); /* Default blueish fluid */
        z-index: 5;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.6s ease-in-out;
     }
     #etching-gas {
         background: rgba(255, 0, 0, 0.15); /* Reddish gas */
     }


    /* טקסט של שלב */
    #step-text {
        font-size: 1.2em;
        min-height: 2em; /* שמירת מקום למניעת קפיצות */
        color: #007bff; /* צבע כחול לטקסט השלב */
        margin-top: 15px;
        font-weight: bold;
    }

    /* כפתורים */
    #next-step-button {
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #28a745; /* צבע ירוק */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        margin-top: 10px;
    }

    #next-step-button:hover {
        background-color: #218838; /* ירוק כהה יותר בהובר */
    }
     #next-step-button:active {
         transform: scale(0.98); /* אפקט לחיצה */
     }

    #toggle-explanation-button {
        display: block;
        margin: 20px auto;
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        background-color: #007bff; /* כחול */
        color: white;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }

    #toggle-explanation-button:hover {
        background-color: #0056b3; /* כחול כהה יותר בהובר */
    }

    /* איזור הסבר מפורט */
    #explanation {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid #d0d0d0;
        border-radius: 12px;
        background-color: #f8f9fa; /* רקע אפור בהיר */
        text-align: right; /* יישור לימין */
        line-height: 1.7;
    }

    #explanation h2, #explanation h3 {
        color: #0056b3;
        margin-bottom: 10px;
    }

    #explanation p {
        margin-bottom: 15px;
    }

    #explanation ul {
        padding-right: 20px;
    }

    #explanation li {
        margin-bottom: 8px;
    }

    /* הסתרה */
    .hidden {
        display: none;
    }

    /* סוגי Photoresist - השפעת אור שונה */
    .photoresist-positive {
        /* Exposed areas become soluble */
    }
     .photoresist-negative {
         /* Exposed areas become insoluble */
     }

    /* מצבי השכבות באנימציה */
    .wafer-etched {
         /* background: linear-gradient(to right, #b8b8d1 0%, #b8b8d1 25%, #9a9abc 25%, #9a9abc 75%, #b8b8d1 75%, #b8b8d1 100%); */
        /* Use a more subtle visual for etching */
         box-shadow: inset 0 -5px 10px rgba(0,0,0,0.3); /* Simulate depth */
         transition: box-shadow 0.8s ease-in-out;
    }
     .wafer-etched::after {
         content: '';
         position: absolute;
         bottom: 0;
         left: 25%; /* Position at the exposed area */
         width: 50%;
         height: 100%;
         background-color: rgba(100, 100, 100, 0.2); /* Darker shade in etched area */
         transition: background-color 0.8s ease-in-out;
     }


    .photoresist-exposed {
        /* Simulate chemical change - e.g., slightly different color/texture */
        /* Using background gradients to target specific areas */
         background: linear-gradient(to right, #f7a540 0%, #f7a540 25%, #e08e2a 25%, #e08e2a 75%, #f7a540 75%, #f7a540 100%); /* Darker where exposed */
    }

    .photoresist-developed {
        /* Simulate removal of exposed areas */
         background: linear-gradient(to right, #f7a540 0%, #f7a540 25%, transparent 25%, transparent 75%, #f7a540 75%, #f7a540 100%); /* Transparent where removed */
        /* Need to ensure underlying wafer/etching is visible */
    }

</style>

<button id="toggle-explanation-button">הצג/הסתר הסבר מפורט</button>

<div id="explanation" class="hidden">
    <h2>הסבר מפורט: מאחורי הקלעים של ייצור השבבים</h2>
    <h3>מהו שבב סיליקון ולמה הוא משמש?</h3>
    <p>שבב סיליקון, המכונה גם מעגל משולב (Integrated Circuit - IC), הוא פיסת סיליקון קטנה המכילה מיליארדי רכיבים אלקטרוניים זעירים (בעיקר טרנזיסטורים), המחוברים יחד ליצירת מעגל מורכב המבצע פונקציה ספציפית - למשל, מעבד במחשב, זיכרון בטלפון, או שבב גרפי. שבבים הם אבן הבניין של כל המכשירים האלקטרוניים המודרניים.</p>

    <h3>מבנה בסיסי של שבב (טרנזיסטורים, שכבות)</h3>
    <p>שבב בנוי על גבי פרוסת סיליקון דקה. הרכיב הבסיסי ביותר הוא הטרנזיסטור, הפועל כמתג אלקטרוני זעיר. מיליארדי טרנזיסטורים אלו, יחד עם רכיבים פסיביים כמו נגדים וקבלים, מחוברים באמצעות רשת מורכבת של "חוטים" מתכתיים (בדרך כלל נחושת או אלומיניום). המעגל כולו נבנה בשכבות רבות (לעיתים עשרות ואף מאות שכבות) של חומרים מוליכים, מבודדים ומוליכים למחצה, המודפסות זו על גבי זו.</p>

    <h3>סקירה כללית של תהליך הייצור</h3>
    <p>ייצור שבבים הוא תהליך מורכב ביותר, המתרחש בסביבות נקיות במיוחד (חדרים נקיים) וכולל מאות שלבים. הוא מתחיל מפרוסת סיליקון גבישית טהורה. באמצעות תהליכים כמו ציפוי (Deposition), פוטוליתוגרפיה (Photolithography), צריבה (Etching), אילוח (Doping) וליטוש (Polishing), בונים את המעגל האלקטרוני שכבה אחר שכבה על גבי הפרוסה.</p>

    <h3>התמקדות בפוטוליתוגרפיה - העיקרון המרכזי</h3>
    <p>פוטוליתוגרפיה היא התהליך המרכזי המאפשר "להדפיס" את התבניות המורכבות של המעגל על גבי פרוסת הסיליקון. זהו תהליך הדומה לצילום או הדפסה סטנסיל, בו משתמשים באור (בדרך כלל UV או EUV) כדי להעביר דפוס משכבה מיוחדת (המסיכה) אל שכבת חומר רגיש לאור (Photoresist) המצפה את הסיליקון. לאחר הפיתוח, השכבה הרגישה לאור הופכת למסיכה חדשה, המגנה על אזורים מסוימים של הסיליקון או של חומרים אחרים במהלך תהליכי הצריבה או האילוח.</p>

    <h3>שלבי תהליך הפוטוליתוגרפיה</h3>
    <ul>
        <li>**הכנה:** ניקוי קפדני של פרוסת הסיליקון והכנת פניה לקליטת החומרים הבאים.</li>
        <li>**ציפוי Photoresist:** מריחת שכבה אחידה ודקה ביותר של חומר פולימרי הרגיש לאור על גבי הפרוסה.</li>
        <li>**מסכה (Mask/Reticle):** שבלונה עשויה קוורץ עם דפוס מדויק של שכבת המעגל המיוצרת. אזורים מסוימים במסיכה אטומים לאור ואחרים שקופים.</li>
        <li>**חשיפה (Exposure):** הקרנת אור (בדרך כלל UV באורך גל קצר או EUV קצר אף יותר עבור דפוסים קטנים) דרך המסיכה על גבי שכבת ה-Photoresist. האור משנה את התכונות הכימיות של ה-Photoresist באזורים שנחשפו (או לא נחשפו, תלוי בסוג החומר).</li>
        <li>**פיתוח (Development):** טבילת הפרוסה בחומר מפתח הממיס את ה-Photoresist באזורים שנחשפו לאור (במקרים של Photoresist חיובי) או באזורים שלא נחשפו (במקרים של Photoresist שלילי). כך נוצרת מסיכת Photoresist עם הדפוס הרצוי.</li>
        <li>**צריבה (Etching):** שימוש בחומרים כימיים או פלזמה להסרת (צריבת) חומרים מהשכבה שמתחת ל-Photoresist באזורים שאינם מוגנים על ידי מסיכת ה-Photoresist שנוצרה.</li>
        <li>**הסרת חומר (Stripping):** הסרת שאריות ה-Photoresist ששימשו כמסיכה. כעת, הדפוס המקורי מהמסיכה הועתק אל שכבת החומר שמתחתיה.</li>
    </ul>

    <h3>חשיבות הדיוק והנקיון</h3>
    <p>תהליך הייצור דורש דיוק קיצוני, ברמה ננומטרית. כל גרגר אבק זעיר או סטייה קלה במיקום יכולים לגרום לשבב להיות בלתי שמיש. לכן, הייצור מתבצע ב"חדרים נקיים" (Cleanrooms), בהם בקרת האוויר והטמפרטורה מחמירה ביותר, ועובדים לובשים חליפות מיוחדות.</p>

    <h3>יצירת שכבות מרובות ובניית המעגל המלא</h3>
    <p>הפוטוליתוגרפיה היא רק שלב אחד במחזור חוזר ונשנה. לאחר שדפוס אחד הועתק לשכבה, מבצעים תהליכים נוספים (אילוח, ציפוי חומר חדש) וחוזרים על כל תהליך הפוטוליתוגרפיה עם מסיכה חדשה עבור השכבה הבאה במעגל. תהליך זה חוזר עשרות פעמים, בונים בהדרגה את המעגל התלת-ממדי המורכב של השבב, עם כל החיבורים והרכיבים שלו.</p>

    <h3>קנה המידה הננומטרי והאתגרים ההנדסיים</h3>
    <p>גודל הרכיבים בשבבים מודרניים נמדד בננומטרים (מיליארדית המטר). ייצור מבנים כה זעירים דורש ציוד יקר ומתוחכם ביותר ומהווה אתגר הנדסי עצום. התקדמות בייצור שבבים (כמו חוק מור) מונעת על ידי היכולת להקטין את גודל הטרנזיסטורים ולהגדיל את צפיפותם, מה שדורש פיתוח מתמיד של טכניקות פוטוליתוגרפיה מתקדמות יותר ויותר, כמו שימוש באור EUV ובשיטות אופטיות מורכבות.</p>
</div>

<script>
    const nextButton = document.getElementById('next-step-button');
    const wafer = document.getElementById('wafer');
    const photoresist = document.getElementById('photoresist');
    const mask = document.getElementById('mask');
    const uvLight = document.getElementById('uv-light');
    const stepText = document.getElementById('step-text');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation-button');
    const developerFluid = document.getElementById('developer-fluid');
    const etchingGas = document.getElementById('etching-gas');

    let currentStep = 0;

    // Define initial state and transitions
    function resetSimulation() {
        // Reset layers to hidden/initial state
        photoresist.style.opacity = 0;
        photoresist.style.transform = 'translateX(-50%) scaleY(0)';
        photoresist.style.backgroundColor = '#f7a540'; // Ensure original color
        photoresist.style.background = ''; // Remove gradients
        photoresist.classList.remove('photoresist-exposed', 'photoresist-developed');

        mask.style.opacity = 0;
        mask.style.transform = 'translateX(-50%) translateY(-50px)';

        uvLight.style.opacity = 0;

        developerFluid.style.opacity = 0;
        etchingGas.style.opacity = 0;

        // Reset wafer state
        wafer.style.backgroundColor = '#b8b8d1';
        wafer.style.background = '';
        wafer.classList.remove('wafer-etched');
        // Remove pseudo-element if added for etching visualization (CSS handles this with the class)

        // Ensure wafer is visible
        wafer.style.opacity = 1;
        wafer.style.transform = 'translateX(-50%) scaleY(1)';
    }


    const steps = [
        {
            text: "שלב 0: התחלה - פרוסת סיליקון מלוטשת ונקייה.",
            action: () => {
                resetSimulation(); // Fully reset
            }
        },
        {
            text: "שלב 1: מצפים את הפרוסה בשכבה דקה של חומר רגיש לאור (Photoresist).",
            action: () => {
                // Wafer is visible by default/reset
                photoresist.style.opacity = 1;
                photoresist.style.transform = 'translateX(-50%) scaleY(1)'; // Grow into place
            }
        },
        {
            text: "שלב 2: מניחים 'מסיכה' (שבלונה) המגדירה את הדפוס לשכבה זו.",
            action: () => {
                // Photoresist stays
                mask.style.opacity = 1;
                mask.style.transform = 'translateX(-50%) translateY(0)'; // Slide down into place
            }
        },
        {
            text: "שלב 3: חשיפה לאור UV דרך המסיכה. האור משנה את החומר הרגיש באזורים החשופים.",
            action: () => {
                // Mask and Photoresist stay
                uvLight.style.opacity = 1; // Light fades in

                // Simulate photoresist change AFTER light appears
                setTimeout(() => {
                     // Apply 'exposed' state style using background gradient
                     photoresist.classList.add('photoresist-exposed');
                     photoresist.style.backgroundColor = 'transparent'; // Allow gradient background to show
                }, 400); // Short delay after light appears
            }
        },
        {
            text: "שלב 4: 'פיתוח' - מסירים את החומר הרגיש שנחשף לאור באמצעות נוזל מפתח.",
            action: () => {
                // Light off, Mask removed
                uvLight.style.opacity = 0;
                mask.style.opacity = 0;
                mask.style.transform = 'translateX(-50%) translateY(-50px)'; // Slide mask back up

                // Show developer fluid briefly
                developerFluid.style.opacity = 1;

                // Simulate photoresist removal after brief delay for fluid
                setTimeout(() => {
                    developerFluid.style.opacity = 0; // Fluid disappears

                    // Apply 'developed' state style
                    photoresist.classList.remove('photoresist-exposed');
                    photoresist.classList.add('photoresist-developed');
                    // The photoresist layer now has transparent parts
                }, 600); // Delay for fluid effect
            }
        },
        {
            text: "שלב 5: 'צריבה' - מסירים חומר מהשכבה התחתונה (הסיליקון) באזורים החשופים.",
            action: () => {
                // Developed photoresist stays as mask
                // Show etching gas briefly
                etchingGas.style.opacity = 1;

                // Simulate etching on the wafer layer
                setTimeout(() => {
                    etchingGas.style.opacity = 0; // Gas disappears
                    wafer.classList.add('wafer-etched'); // Apply etched state style
                }, 600); // Delay for etching effect
            }
        },
        {
            text: "שלב 6: מסירים את שאריות החומר הרגיש. כעת הדפוס הועתק בהצלחה לשכבת הסיליקון!",
            action: () => {
                // Remove remaining photoresist
                photoresist.style.opacity = 0;
                 photoresist.style.transform = 'translateX(-50%) scaleY(0)'; // Scale down/fade out
                photoresist.classList.remove('photoresist-developed');
                photoresist.style.background = ''; // Clear gradients
                photoresist.style.backgroundColor = '#f7a540'; // Reset color

                // Wafer remains with etched pattern (handled by wafer-etched class)
            }
        },
         {
            text: "זהו סוף מחזור אחד! תהליך זה חוזר על עצמו עשרות פעמים לבניית כל שכבות השבב המורכב.",
            action: () => {
                 // Stay in the final state of step 6
                 // Wafer remains etched, other layers gone
                 // Next click will go back to step 0 (reset)
            }
        },
    ];

    function updateSimulation() {
        // Ensure smooth transitions by setting initial states before triggering changes
         if (currentStep === 0) {
             resetSimulation();
         } else if (currentStep === 1) {
              resetSimulation(); // Make sure everything is reset before adding photoresist
         } else if (currentStep === 2) {
             // Ensure photoresist is in place before adding mask
              photoresist.style.opacity = 1;
              photoresist.style.transform = 'translateX(-50%) scaleY(1)';
         } else if (currentStep === 3) {
             // Ensure photoresist and mask are in place before light
              photoresist.style.opacity = 1;
              photoresist.style.transform = 'translateX(-50%) scaleY(1)';
              mask.style.opacity = 1;
              mask.style.transform = 'translateX(-50%) translateY(0)';
               // Reset photoresist state just in case
               photoresist.classList.remove('photoresist-exposed', 'photoresist-developed');
                photoresist.style.background = '';
                photoresist.style.backgroundColor = '#f7a540';

         } else if (currentStep === 4) {
             // Ensure light and exposed photoresist are visible before developing
             photoresist.style.opacity = 1;
              photoresist.style.transform = 'translateX(-50%) scaleY(1)';
              mask.style.opacity = 1;
              mask.style.transform = 'translateX(-50%) translateY(0)';
              uvLight.style.opacity = 1;
             photoresist.classList.add('photoresist-exposed');
              photoresist.style.backgroundColor = 'transparent'; // Allow gradient to show

         } else if (currentStep === 5) {
              // Ensure developed photoresist and etched wafer state is ready before etching animation
              photoresist.style.opacity = 1;
              photoresist.style.transform = 'translateX(-50%) scaleY(1)';
              photoresist.classList.remove('photoresist-exposed');
              photoresist.classList.add('photoresist-developed');
               mask.style.opacity = 0; // Mask is removed
              uvLight.style.opacity = 0; // Light is off
               developerFluid.style.opacity = 0; // Fluid is gone
               wafer.classList.remove('wafer-etched'); // Remove etched state before applying again

         } else if (currentStep === 6) {
             // Ensure etched wafer state and developed photoresist are ready before stripping
              photoresist.style.opacity = 1;
              photoresist.style.transform = 'translateX(-50%) scaleY(1)';
              photoresist.classList.remove('photoresist-exposed');
              photoresist.classList.add('photoresist-developed');
              wafer.classList.add('wafer-etched'); // Wafer should be etched before stripping photoresist

         } else if (currentStep === 7) {
             // Ensure final state of step 6 is set before the final text
             photoresist.style.opacity = 0; // Photoresist should be gone
             photoresist.style.transform = 'translateX(-50%) scaleY(0)';
             photoresist.classList.remove('photoresist-developed');
             photoresist.style.background = ''; // Clear gradients
             photoresist.style.backgroundColor = '#f7a540'; // Reset color

             wafer.classList.add('wafer-etched'); // Wafer remains etched

         }


        // Execute the action for the current step
        steps[currentStep].action();

        // Update the text for the current step
        stepText.textContent = steps[currentStep].text;
    }

    // Event listener for the button
    nextButton.addEventListener('click', () => {
        currentStep = (currentStep + 1) % steps.length;
        updateSimulation();
    });

    // Initialize simulation on page load
    updateSimulation();

    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
         // Scroll to the explanation if showing, or back to sim if hiding? Optional.
         if (!explanationDiv.classList.contains('hidden')) {
             explanationDiv.scrollIntoView({ behavior: 'smooth' });
         } else {
             document.getElementById('simulation-app').scrollIntoView({ behavior: 'smooth' });
         }
    });

    // Ensure the explanation is hidden by default on load
    explanationDiv.classList.add('hidden'); // Redundant with HTML class, but good practice

</script>
```