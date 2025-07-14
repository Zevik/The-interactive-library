---
title: "סימולטור שוק האמנות הדיגיטלי: האם תהפכו למיליונרי NFT או תפסידו הכל?"
english_slug: nft-digital-art-market-simulator-can-you-profit
category: "כלכלה התנהגותית"
tags:
  - NFT
  - שוק האמנות
  - בלוקצ'יין
  - ספקולציה
  - כלכלה
---
# סימולטור שוק האמנות הדיגיטלי: האם תהפכו למיליונרי NFT או תפסידו הכל?

ציור דיגיטלי שאפשר להוריד חינם נמכר במיליוני דולרים. הזוי? מציאות! בועה ספקולטיבית ענקית, מהפכה אמנותית, או אולי שילוב פרוע ובלתי צפוי? היכנסו לסימולטור ובדקו אם יש לכם את מה שצריך לשרוד בשוק ה-NFT הפרוע!

<div id="simulator-container">
    <div id="stats">
        <div class="stat-item">
            <label>יתרה:</label>
            <span id="balance" class="stat-value"></span>
        </div>
         <div class="stat-item">
            <label>שווי תיק נוכחי:</label>
            <span id="total-value" class="stat-value"></span>
        </div>
        <div class="stat-item">
            <label>רווח/הפסד כולל:</label>
            <span id="potential-profit-loss" class="stat-value"></span>
        </div>
        <div class="stat-item">
            <label>יום בסימולציה:</label>
            <span id="day-counter" class="stat-value"></span>
        </div>
    </div>
    <button id="advance-time-button">קדימה ליום הבא! 🚀</button>
    <div id="messages" class="message-box">
        <!-- הודעות על קנייה/מכירה או שגיאות יופיעו כאן -->
    </div>
    <div id="gallery">
        <h2>גלריה - קנו פריטים חדשים!</h2>
        <div id="gallery-items">
            <!-- NFT items will be rendered here by JS -->
        </div>
    </div>
    <div id="inventory">
        <h2>האוסף שלי - האם הגיע זמן למכור?</h2>
        <ul id="inventory-list">
             <li>האוסף שלך ריק כרגע. מצא הזדמנות בגלריה!</li>
        </ul>
    </div>
    <!-- פוטנציאל עתידי: הצגת גרפים היסטוריים -->
</div>

<button id="toggle-explanation-button">למה זה קורה? הצגת/הסתרת ההסבר המלא</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: עולם שוק ה-NFT הפרוע</h2>

    <h3>מה זה NFT ואיך הוא מייצג 'בעלות' על נכס דיגיטלי?</h3>
    <p>NFT (Non-Fungible Token) הוא כמו "תעודת מקוריות" דיגיטלית, ייחודית ולא ניתנת להחלפה באחרת. בניגוד למטבעות כמו שקל או ביטקוין (שכל יחידה זהה לאחרת), כל NFT הוא יחיד במינו ומקושר לנכס דיגיטלי ספציפי – כמו יצירת אמנות, קטע וידאו נדיר, או פריט משחק אקסקלוסיבי. הבעלות מתועדת על גבי בלוקצ'יין – ספר חשבונות ציבורי, שקוף ובלתי ניתן לשינוי. גם אם מיליון אנשים יכולים להוריד את אותה תמונה למחשב, רק בעל ה-NFT מחזיק ב"מקור" הדיגיטלי המתועד בבלוקצ'יין. זהו הבסיס למושג "נדירות דיגיטלית".</p>

    <h3>כיצד נקבע 'ערך' בשוק ה-NFT? (נדירות, בעלות, קהילה, ובעיקר... הייפ!)</h3>
    <p>אם חשבתם שמחיר נקבע לפי יופי או שימושיות, תחשבו שוב! ערך NFT הוא תופעה סוריאליסטית לעיתים קרובות. הגורמים העיקריים כוללים: <strong>נדירות דיגיטלית:</strong> כמה עותקים יש מהפריט הזה? <strong>הוכחת בעלות:</strong> ה-NFT מוכיח שאתה הבעלים ה"רשמי". <strong>קהילה:</strong> האם יש קהילה סוערת ותומכת מאחורי הפרויקט או האמן? קהילה חזקה יכולה להזניק את הביקוש. וחשוב מכל: <strong>הייפ (Hype)!</strong> ככל שיותר אנשים מדברים, מצייצים ומתלהבים מפרויקט מסוים, כך עולה הסיכוי שהמחיר שלו יטוס למעלה, לעיתים ללא שום קשר ל"ערך אמנותי" או פונקציונלי אמיתי. זהו מנוע הספקולציה המרכזי.</p>

    <h3>ספקולציה והשפעתה הדרמטית על תנודתיות המחירים</h3>
    <p>רוב הקונים בשוק ה-NFT אינם אספני אמנות קלאסיים. הם ספקולנטים שמקווים למכור את הפריט שרכשו ביוקר רב יותר בעתיד. הציפייה לרווחים מהירים יוצרת ביקוש עצום שמנפח מחירים בצורה מסחררת. אבל ברגע שההייפ דועך, ה"עדר" נבהל, וכולם ממהרים למכור לפני שהמחיר יתרסק. התוצאה היא תנודתיות אדירה, עליות מסחררות וירידות כואבות, כמו שראינו בסימולטור. היכולת "לתזמן" את השוק הזה כמעט בלתי אפשרית.</p>

    <h3>דמיון ושוני בין שוק ה-NFT לשווקים אחרים (אמנות מסורתית, קריפטו, מניות)</h3>
    <p>שוק ה-NFT הוא בן כלאיים מוזר. <strong>דומה לשוק האמנות המסורתי:</strong> גם שם, שם האמן והנדירות משפיעים, וספקולציה מצד סוחרים היא חלק מהמשחק. <strong>דומה לשוקי קריפטו:</strong> שניהם מבוססים על בלוקצ'יין, שניהם מושפעים עמוקות מסנטימנט השוק, רגולציה ובעיקר - הייפ ותנודתיות קיצונית. <strong>שונה משוקי מניות:</strong> מניות מייצגות חלק מחברה אמיתית עם פעילות עסקית. רבים מה-NFTs, נכון לעכשיו, אינם מייצרים הכנסות או רווחים, והערך שלהם נגזר כמעט כולו מביקוש ספקולטיבי ואמונה של קהילה בערכם העתידי. זה הופך אותם לנכסים תנודתיים ומסוכנים במיוחד.</p>

    <h3>סיכונים וסיכויים: האם שוק ה-NFT הוא בועה שתתפוצץ?</h3>
    <p>זו שאלת מיליון הדולר (או מיליון ה-NFT). יש הרואים בו בועה קלאסית שסופה להתפוצץ ולהשאיר ספקולנטים רבים עם הפסדים. אחרים רואים בו חלוץ של כלכלה דיגיטלית חדשה, בה בעלות על נכסים ואינטראקציה קהילתית מקבלים ממד חדש (Web3, Metaverse). הסיכון הברור הוא אובדן כסף מהיר וגדול. הסיכויים קיימים בפוטנציאל צמיחה אדיר לפרויקטים שיצליחו לבנות קהילה אמיתית, להציע ערך מעבר לספקולציה (כמו גישה לקהילות אקסקלוסיביות או פונקציונליות בתוך משחקים/פלטפורמות), או להיות פשוט... הבא בתור בהייפ. הסימולטור נועד להראות כמה הסיכון גבוה והניבוי קשה.</p>

    <h3>הפסיכולוגיה בפעולה: התנהגות עדר ו-FOMO</h3>
    <p>כמו בכל שוק תנודתי, הפסיכולוגיה האנושית משחקת תפקיד ענק. פחד (Fear), חמדנות (Greed), אופטימיות יתרה, ובעיקר - FOMO (Fear Of Missing Out - הפחד לפספס הזדמנות) מניעים החלטות. אנשים קונים כי "כולם קונים" והמחיר עולה, ונבהלים ומוכרים כי "כולם מוכרים" והמחיר יורד. הסימולטור מנסה לתפוס חלק מההתנהגות הזו – שוק שמושפע מרגשות וטרנדים לא פחות (ולפעמים יותר) מיסודות כלכליים הגיוניים.</p>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6;
        margin: 0;
        padding: 20px;
        direction: rtl;
        text-align: right;
    }

    h1, h2, h3 {
        color: #1a2e35;
        text-align: center; /* Center titles for better look */
        margin-bottom: 20px;
    }

    h1 {
        font-size: 2em;
        font-weight: 700;
        margin-bottom: 30px;
    }

    h2 {
        font-size: 1.5em;
        font-weight: 700;
        border-bottom: 2px solid #e0e0e0;
        padding-bottom: 10px;
        margin-top: 25px;
        text-align: right; /* Align section titles right */
    }

     h3 {
        font-size: 1.2em;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 10px;
        color: #2c3e50;
     }


    #simulator-container {
        max-width: 900px;
        margin: 20px auto;
        padding: 30px;
        border: 1px solid #dcdcdc;
        border-radius: 12px;
        background-color: #ffffff;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }

    #stats {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 15px;
        margin-bottom: 30px;
        padding: 20px;
        background-color: #eef2f7;
        border-radius: 8px;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    .stat-item {
        text-align: center;
    }

    .stat-item label {
        display: block;
        font-size: 0.9em;
        color: #555;
        margin-bottom: 5px;
    }

    .stat-value {
        font-size: 1.4em;
        font-weight: 700;
        color: #007bff; /* Default color */
        transition: color 0.3s ease; /* Smooth color change */
    }

    #potential-profit-loss.profit {
        color: #28a745; /* Green */
    }

    #potential-profit-loss.loss {
        color: #dc3545; /* Red */
    }


    #advance-time-button {
        display: block;
        width: 100%;
        padding: 15px;
        font-size: 1.2em;
        font-weight: 700;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        margin-bottom: 25px;
        transition: background-color 0.2s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 123, 255, 0.3);
    }

    #advance-time-button:hover {
        background-color: #0056b3;
        box-shadow: 0 3px 7px rgba(0, 123, 255, 0.4);
    }

    #advance-time-button:active {
        background-color: #004085;
        transform: scale(0.98);
    }

    .message-box {
        margin-bottom: 20px;
        padding: 15px;
        border: 1px solid;
        border-radius: 6px;
        font-weight: 700;
        display: none; /* Hidden by default */
        opacity: 0; /* Start hidden for fade-in */
        transition: opacity 0.3s ease-in-out;
        text-align: right;
    }

    .message-box.show {
         opacity: 1;
    }

    .message-box.info {
        background-color: #fff3cd; /* Light yellow */
        border-color: #ffecb5;
        color: #856404; /* Dark yellow text */
    }

    .message-box.error {
        background-color: #f8d7da; /* Light red */
        border-color: #f5c6cb;
        color: #721c24; /* Dark red text */
    }

    .message-box.success {
        background-color: #d4edda; /* Light green */
        border-color: #c3e6cb;
        color: #155724; /* Dark green text */
    }


    #gallery, #inventory {
        margin-top: 25px;
        padding: 20px;
        border: 1px solid #dcdcdc;
        border-radius: 8px;
        background-color: #ffffff;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }


    #gallery-items {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
        gap: 25px;
        margin-top: 20px;
    }

    .nft-item {
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        background-color: #f9f9f9;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
        height: 100%; /* Ensure items take full height in grid */
    }

     .nft-item:hover {
         transform: translateY(-5px);
         box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
     }

    .nft-item img {
        width: 100%; /* Make image responsive within its container */
        height: 120px; /* Fixed height */
        object-fit: cover;
        margin-bottom: 15px;
        background-color: #eceff1; /* Placeholder background */
        border-radius: 6px;
        border: 1px solid #cfd8dc;
    }

    .nft-item h3 {
        font-size: 1.1em;
        margin: 0 0 8px 0;
        color: #37474f;
        flex-grow: 1; /* Allow title to take up space */
    }

    .nft-item p.price {
        font-size: 1.1em;
        margin: 0 0 15px 0;
        font-weight: 700;
        color: #007bff; /* Default price color */
        transition: color 0.3s ease; /* Smooth price color change */
    }

     .nft-item p.price.price-up {
         color: #28a745; /* Green for price increase */
     }

     .nft-item p.price.price-down {
         color: #dc3545; /* Red for price decrease */
     }


    .nft-item .actions {
         display: flex;
         justify-content: space-around;
         gap: 5px;
    }

    .nft-item .actions button {
        flex-grow: 1; /* Distribute space evenly */
        padding: 10px 15px;
        cursor: pointer;
        border: none;
        border-radius: 5px;
        font-size: 0.9em;
        font-weight: 700;
        transition: background-color 0.2s ease, opacity 0.2s ease;
    }

    .nft-item .actions .buy {
        background-color: #28a745; /* Green */
        color: white;
    }

    .nft-item .actions .buy:disabled {
        background-color: #a5d6a7;
        cursor: not-allowed;
        opacity: 0.7;
    }
     .nft-item .actions .buy:hover:not(:disabled) {
         background-color: #218838;
     }


    .nft-item .actions .sell {
        background-color: #dc3545; /* Red */
        color: white;
    }
     .nft-item .actions .sell:disabled {
        background-color: #ef9a9a;
        cursor: not-allowed;
        opacity: 0.7;
    }
     .nft-item .actions .sell:hover:not(:disabled) {
         background-color: #c82333;
     }


    #inventory ul {
        list-style: none;
        padding: 0;
        margin-top: 20px;
    }

    #inventory li {
        background-color: #eef2f7; /* Light blue-grey */
        border: 1px solid #dcdcdc;
        margin-bottom: 8px;
        padding: 12px 15px;
        border-radius: 6px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap; /* Allow wrapping */
        font-size: 1em;
        color: #333;
    }

    #inventory li:last-child {
        margin-bottom: 0;
    }

     #inventory li span {
         font-weight: normal;
         font-size: 0.9em;
          margin-right: 15px; /* Space between name/qty and value */
          color: #555;
     }

    #inventory li .inventory-profit {
        font-weight: 700;
        color: #28a745; /* Green for profit */
    }
     #inventory li .inventory-loss {
        font-weight: 700;
        color: #dc3545; /* Red for loss */
    }


    #explanation {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid #dcdcdc;
        border-radius: 12px;
        background-color: #ffffff;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        direction: rtl; /* Hebrew support */
        text-align: right; /* Hebrew support */
    }

    #explanation p {
        line-height: 1.8;
        color: #555;
        margin-bottom: 15px;
    }
     #explanation p:last-child {
         margin-bottom: 0;
     }

    #explanation strong {
        color: #1a2e35;
    }


    #toggle-explanation-button {
        display: block;
        width: 100%;
        padding: 12px;
        font-size: 1.1em;
        font-weight: 700;
        background-color: #6c757d;
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        margin-top: 20px;
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
        transition: background-color 0.2s ease;
    }
     #toggle-explanation-button:hover {
         background-color: #5a6268;
     }

    @media (max-width: 768px) {
        #simulator-container, #explanation {
            padding: 20px;
        }

        #stats {
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 10px;
        }

        #gallery-items {
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 15px;
        }

        .nft-item img {
            height: 100px;
        }
        .nft-item .actions button {
             padding: 8px 10px;
             font-size: 0.85em;
        }

        #inventory li {
             flex-direction: column;
             align-items: flex-start;
        }
         #inventory li span {
             margin-right: 0;
             margin-top: 5px;
         }

        #advance-time-button, #toggle-explanation-button {
            font-size: 1em;
            padding: 10px;
        }
    }

     @media (max-width: 480px) {
         h1 {
             font-size: 1.6em;
         }
         h2 {
             font-size: 1.3em;
         }
         .stat-value {
             font-size: 1.2em;
         }
         #gallery-items {
             grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
             gap: 10px;
         }
         .nft-item img {
             height: 80px;
         }
         .nft-item h3 {
             font-size: 1em;
         }
          .nft-item p.price {
             font-size: 1em;
         }
         .nft-item .actions button {
             padding: 6px 8px;
             font-size: 0.8em;
         }
         #inventory li {
             font-size: 0.9em;
         }
     }

</style>

<script>
    const initialBalance = 1000;
    let userBalance = initialBalance;
    let userInventory = []; // [{ itemId: 1, purchasePrice: 100 }, ...]
    let day = 0;

    const nfts = [
        { id: 1, name: 'שקיעה דיגיטלית', initialPrice: 50, currentPrice: 50, volatility: 0.08, history: [50], image: 'https://via.placeholder.com/150x100/667eea/ffffff?text=NFT+1' }, // Added specific image URLs
        { id: 2, name: 'קוף עצבני #123', initialPrice: 200, currentPrice: 200, volatility: 0.15, history: [200], image: 'https://via.placeholder.com/150x100/f7fafc/1a202c?text=NFT+2' },
        { id: 3, name: 'ציפור פיקסלים נדירה', initialPrice: 120, currentPrice: 120, volatility: 0.1, history: [120], image: 'https://via.placeholder.com/150x100/4299e1/ffffff?text=NFT+3' },
        { id: 4, name: 'דמות מרחבי המטאברס', initialPrice: 80, currentPrice: 80, volatility: 0.06, history: [80], image: 'https://via.placeholder.com/150x100/f6ad55/ffffff?text=NFT+4' },
        { id: 5, name: 'אמנות גנרטיבית #42', initialPrice: 180, currentPrice: 180, volatility: 0.12, history: [180], image: 'https://via.placeholder.com/150x100/ed64a6/ffffff?text=NFT+5' },
        { id: 6, name: 'נוף מופשט דור 3', initialPrice: 70, currentPrice: 70, volatility: 0.09, history: [70], image: 'https://via.placeholder.com/150x100/48bb78/ffffff?text=NFT+6' },
         { id: 7, name: 'פורטרט רובוטי', initialPrice: 150, currentPrice: 150, volatility: 0.13, history: [150], image: 'https://via.placeholder.com/150x100/805ad5/ffffff?text=NFT+7' },
    ];

    // Get DOM elements
    const balanceSpan = document.getElementById('balance');
    const totalValueSpan = document.getElementById('total-value'); // New element for total value
    const potentialProfitLossSpan = document.getElementById('potential-profit-loss');
    const dayCounterSpan = document.getElementById('day-counter');
    const galleryItemsContainer = document.getElementById('gallery-items'); // Direct reference
    const inventoryList = document.getElementById('inventory-list'); // Direct reference
    const messagesDiv = document.getElementById('messages');
    const advanceTimeButton = document.getElementById('advance-time-button');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation-button');

    function updateDisplay() {
        balanceSpan.textContent = userBalance.toFixed(2) + '$';

        let potentialInventoryValue = 0;
        userInventory.forEach(item => {
            const nft = nfts.find(n => n.id === item.itemId);
            if (nft) {
                potentialInventoryValue += nft.currentPrice;
            }
        });

        const totalValue = userBalance + potentialInventoryValue;
         totalValueSpan.textContent = totalValue.toFixed(2) + '$'; // Update total value

        const potentialProfitLoss = totalValue - initialBalance;
        potentialProfitLossSpan.textContent = potentialProfitLoss.toFixed(2) + '$';
        // Use classes for color transition
        potentialProfitLossSpan.classList.remove('profit', 'loss');
        if (potentialProfitLoss >= 0) {
             potentialProfitLossSpan.classList.add('profit');
        } else {
             potentialProfitLossSpan.classList.add('loss');
        }

        dayCounterSpan.textContent = day;


        // Update gallery items
         nfts.forEach(nft => {
             const itemElement = galleryItemsContainer.querySelector(`.nft-item[data-id="${nft.id}"]`);
             if (itemElement) {
                 const priceElement = itemElement.querySelector('.price');
                 // Add temporary class for price change animation/color
                 const oldPrice = parseFloat(priceElement.textContent.replace('מחיר: ', '').replace('$', ''));
                 priceElement.classList.remove('price-up', 'price-down');
                 if (nft.currentPrice > oldPrice) {
                     priceElement.classList.add('price-up');
                 } else if (nft.currentPrice < oldPrice) {
                     priceElement.classList.add('price-down');
                 }
                  // Remove the class after animation duration (or a bit longer)
                 setTimeout(() => {
                    priceElement.classList.remove('price-up', 'price-down');
                 }, 600); // Match CSS transition duration + buffer

                 priceElement.textContent = 'מחיר: ' + nft.currentPrice.toFixed(2) + '$';

                 const buyButton = itemElement.querySelector('.buy');
                 buyButton.disabled = userBalance < nft.currentPrice;

                 const sellButton = itemElement.querySelector('.sell');
                 // Disable sell button if user doesn't own any of this NFT type
                 sellButton.disabled = !userInventory.some(item => item.itemId === nft.id);
             }
         });


        // Update inventory display
        inventoryList.innerHTML = ''; // Clear current list

        // Count occurrences and calculate average purchase price for each item ID
        const inventorySummary = userInventory.reduce((acc, item) => {
            if (!acc[item.itemId]) {
                acc[item.itemId] = { count: 0, totalPurchaseCost: 0, nft: nfts.find(n => n.id === item.itemId) };
            }
            acc[item.itemId].count++;
            acc[item.itemId].totalPurchaseCost += item.purchasePrice;
            return acc;
        }, {});


        for (const itemId in inventorySummary) {
            const summary = inventorySummary[itemId];
            const nft = summary.nft;
            if (nft) {
                const listItem = document.createElement('li');
                const averagePurchasePrice = summary.totalPurchaseCost / summary.count;
                const currentValueTotal = nft.currentPrice * summary.count;
                const profitLossPerItemType = currentValueTotal - summary.totalPurchaseCost;

                let profitLossClass = '';
                if (profitLossPerItemType > 0) {
                    profitLossClass = 'inventory-profit';
                } else if (profitLossPerItemType < 0) {
                    profitLossClass = 'inventory-loss';
                }


                listItem.innerHTML = `
                    <span>${nft.name} (${summary.count})</span>
                    <span>
                        שווי נוכחי: ${currentValueTotal.toFixed(2)}$ |
                        ע.רכישה ממוצעת: ${averagePurchasePrice.toFixed(2)}$
                    </span>
                     <span class="${profitLossClass}">
                         רווח/הפסד: ${profitLossPerItemType.toFixed(2)}$
                     </span>
                `;
                inventoryList.appendChild(listItem);
            }
        }
        if (userInventory.length === 0) {
            inventoryList.innerHTML = '<li>האוסף שלך ריק כרגע. מצא הזדמנות בגלריה!</li>';
        }
    }

    function showMessage(msg, type = 'info') { // type can be 'info', 'error', 'success'
        messagesDiv.textContent = msg;
        messagesDiv.className = 'message-box show ' + type; // Reset classes and add type/show

        // Hide after 4 seconds with fade-out
        setTimeout(() => {
            messagesDiv.classList.remove('show');
             // Completely hide after fade-out
            setTimeout(() => {
                 messagesDiv.style.display = 'none';
            }, 300); // Matches CSS transition duration
        }, 4000);

         messagesDiv.style.display = 'block'; // Show before adding 'show' class for transition
    }

    function buyNFT(id) {
        const nft = nfts.find(n => n.id === id);
        if (!nft) return;

        if (userBalance >= nft.currentPrice) {
            userBalance -= nft.currentPrice;
            userInventory.push({ itemId: id, purchasePrice: nft.currentPrice });
            updateDisplay();
            showMessage(`🎉 קנית את "${nft.name}" ב-${nft.currentPrice.toFixed(2)}$`, 'success');
        } else {
            showMessage('💰 אין לך מספיק כסף לרכישה!', 'error');
        }
    }

    function sellNFT(id) {
        const nft = nfts.find(n => n.id === id);
        if (!nft) return;

        // Find one instance of this item in inventory
        const itemIndex = userInventory.findIndex(item => item.itemId === id);

        if (itemIndex !== -1) {
            const itemToSell = userInventory[itemIndex];
            userInventory.splice(itemIndex, 1); // Remove one item
            userBalance += nft.currentPrice; // Sell at current market price
            const profitLoss = nft.currentPrice - itemToSell.purchasePrice;

             const messageType = profitLoss >= 0 ? 'success' : 'error';
             const emoji = profitLoss >= 0 ? '💸' : '💔';
             showMessage(`${emoji} מכרת את "${nft.name}" ב-${nft.currentPrice.toFixed(2)}$ (רווח/הפסד: ${profitLoss.toFixed(2)}$)`, messageType);

            updateDisplay();
        } else {
            // This case should be rare if sell button is disabled correctly
            showMessage('🧐 אין לך פריט זה למכירה!', 'error');
        }
    }


    function simulateMarketStep() {
        day++;
         advanceTimeButton.disabled = true; // Disable button during simulation step
         advanceTimeButton.textContent = 'מעדכן מחירים...';

        // Store old prices to check for changes
        const oldPrices = nfts.map(nft => ({ id: nft.id, price: nft.currentPrice }));

        nfts.forEach(nft => {
            // Use a more sophisticated random walk model (Geometric Brownian Motion style)
            // New Price = Current Price * exp( (drift - 0.5 * volatility^2) * time + volatility * sqrt(time) * Z )
            // Simplifying for daily step (time=1) and focusing on volatility
            const drift = 0.01; // Small upward bias over time? Or 0 for true random walk around 0
            const shock = Math.random() * 2 - 1; // Random value between -1 and 1 (standard normal would be better but Math.random is simpler)
            const priceChangeFactor = Math.exp( (drift - 0.5 * nft.volatility * nft.volatility) + nft.volatility * shock);
            let newPrice = nft.currentPrice * priceChangeFactor;


            // Add some minor correlation between NFTs? (Optional complexity)
            // E.g., slightly nudge prices based on a global sentiment factor

            // Prevent price from going below a minimum (e.g., 5$)
            newPrice = Math.max(newPrice, 5);

            nft.currentPrice = newPrice;
            nft.history.push(newPrice);
        });

        // After updating prices, update display and re-enable button
        updateDisplay();

        // Trigger price change visual feedback after updateDisplay
         oldPrices.forEach(oldNft => {
             const newNft = nfts.find(n => n.id === oldNft.id);
             if (newNft) {
                 const itemElement = galleryItemsContainer.querySelector(`.nft-item[data-id="${newNft.id}"]`);
                  if(itemElement) {
                     const priceElement = itemElement.querySelector('.price');
                     priceElement.classList.remove('price-up', 'price-down'); // Clear previous state
                     if (newNft.currentPrice > oldNft.price) {
                         priceElement.classList.add('price-up');
                     } else if (newNft.currentPrice < oldNft.price) {
                         priceElement.classList.add('price-down');
                     }
                     // Remove class after animation
                     setTimeout(() => {
                         priceElement.classList.remove('price-up', 'price-down');
                     }, 600); // Match CSS transition duration
                  }
             }
         });


         advanceTimeButton.disabled = false;
         advanceTimeButton.textContent = 'קדימה ליום הבא! 🚀';
    }

    function renderGallery() {
        galleryItemsContainer.innerHTML = ''; // Ensure it's empty before rendering

        nfts.forEach(nft => {
            const itemElement = document.createElement('div');
            itemElement.classList.add('nft-item');
            itemElement.dataset.id = nft.id;
            itemElement.innerHTML = `
                <img src="${nft.image}" alt="${nft.name}">
                <h3>${nft.name}</h3>
                <p class="price">מחיר: ${nft.currentPrice.toFixed(2)}$</p>
                <div class="actions">
                    <button class="buy" data-id="${nft.id}">קנה</button>
                    <button class="sell" data-id="${nft.id}" disabled>מכור</button>
                </div>
            `;
            galleryItemsContainer.appendChild(itemElement);

            // Add event listeners to buttons immediately
            itemElement.querySelector('.buy').addEventListener('click', () => buyNFT(nft.id));
            itemElement.querySelector('.sell').addEventListener('click', () => sellNFT(nft.id));
        });
    }

    function toggleExplanation() {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתרת ההסבר המלא';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.textContent = 'למה זה קורה? הצגת ההסבר המלא'; // More engaging text
        }
    }


    // Initial setup
    document.addEventListener('DOMContentLoaded', () => {
        renderGallery();
        updateDisplay(); // Initial display
        advanceTimeButton.addEventListener('click', simulateMarketStep);
        toggleExplanationButton.addEventListener('click', toggleExplanation);
    });

</script>