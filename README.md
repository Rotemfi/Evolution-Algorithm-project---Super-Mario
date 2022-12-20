
<h1 align="center">Super Mario! 👨🏻‍🔧 </h1>
<h3 align="center">🍄 Using evolution algorithm project 🍄 </h3>

<h4 align="center"> <b>נכתב על ידי</b>:<br/> מירב סיני <br/> ולד טובבין <br/> רותם פירסטטר</h4>




![GamePreview](https://github.com/Rotemfi/Evolution-Algorithm-project---Super-Mario/blob/main/images/animation.gif)

<html lang="he">
<head>
    <meta charset="utf-8" />
</head>
<body dir="rtl">
  <h2>מבוא</h2>
  <h3> הקדמה - סופר מריו </h3>
      <p>אסופר מריו הוא דמות מצוירת ממשחק וידאו פופולרי של חברת "נינטנדו" היפנית. מריו הוא שרברב איטלקי הנמצא בממלכת פטריות מלאה הרפתקאות. אין לו כלי נשק בניגוד למשחקי וידאו רבים אחרים: הוא משתמש בקפיצה והתחמקות על מנת להתמודד עם אויבי הנקרים בדרכו.
    </p>
    <p>
      יוצרו של מריו הוא שיגרו מיאמוטו. הצבעים של מריו: אדום וכחול, נבחרו מפאת המגבלות הגרפיות של משחקי המחשב באותה תקופה - בעלי ניגודיות חזקה לצבעי הרקע במשחק. בשל הקשיים הגרפים נבחר מריו ללבוש כובע גדול שיבטל את הצורך בהנפשות של פרטים קטנים דוגמת השיער שלו כאשר דמותו במשחק מתקדמת\קופצת וכו', ושפם על מנת לחסוך את ההתעסקות בהבעות הפנים. ניתן להבין את כל זאת כאשר מגלים שהגודל של הדמות המקורית הייתה 8*8 פיקסלים בלבד. בהדרגה עם השנים וההתפתחות הטכנולוגית, מראהו של מריו הופך למורכב יותר ויותר.
    </p>
  
<h3>הקדמה - אלגוריתם אבולוציוני </h3>
    <p>
    ״מוטציה היא אקראית. הברירה הטבעית היא ההפך הגמור מאקראיות.״ ~ ריצ׳רד דוקינס,     ״השען העיוור״ (1986)
    </p>
  <p>
  אלגוריתמים אבולוציוניים מתבססים על הרעיון של התפתחות אבולוציה. כל דור שנוצר טוב יותר מהקודם שלו, והאלגוריתמים הללו באים לחקות את ההתנהגות הזו. מובן שיש אלמנט של אקראיות, אך עצם היותו אבולוציוני מבטא את היכולת של אלגוריתם לקבל בעיה ולמצוא פתרון אופטימלי ע"י שיפור האבולוציה מדור לדור - דבר שלא יכול להיות אקראי בלבד.  כלומר, האלגוריתם משנה את דרך הפעולה של עצמו מדור לדור. אנו מעצבים אותו להיות מבורר על רעיון "הברירה הטבעית". האלגוריתם מקבל כקלט מופעים כלשהם, שהם קלט לבעיה המקורית. הפלט נבדק ע"י פונקצית התאמה (fitness) ואז מתבצעות מוטציות שונות בפתרון - מתודת הבחירה המבוססת על הערכת ההתאמה נבחרת, והאבולוציה מתחילה.
  </p>
      <p>
      בפרויקט שלנו אנו שואפים לפתח אלגוריתם אבולוציוני היודע להעריך את ההצלחה של כל משחק על פני כל שלב, ויודע למצוא באמצעות אבולוציה את הדרך הטובה ביותר של שחקן להתמודד עם מסלול שניתן לו - לסיים את המסלול ללא להפסל ולמקסם את מספר הנקודות ששחקן צובר.
    </p>
    
    
 <h2>תיאור הבעיה \ מטרת הפרויקט </h2>
      <p>
      מימוש אלגוריתם אבולוציוני של סופר מריו שמקבל את ההחלטות הכי טובות כאשר המטרה היא לצבור כמה שיותר נקודות במשחק.
    </p>
    
 <h3> חוקי המשחק </h3>
      <p>
    המטרה היא להשיג כמה שיותר נקודות במסלול ולהגיע לדגל בסופו - לא להפסל ע"י אויבים בדרך.
    <br/> 
    ישנם 2 סוגי אויבים: <br/>
    1. <b>גומבה</b>
        - אויבי קרקע שאסור להתקל בהם. מריו נמצא גם הוא בגובה הקרקע ולכן צריך לקפוץ מעליהם. <br/>
    2. <b>לקיטו</b>- מפלצות אוויר שנמצאות בגובה הראש של מריו, על כן יש להתחמק מהן ע"י התכופפות.
      </p>
      <p>
מפלצות יכולות להיות בגובה הראש של מריו ולכן הוא צריך להתכופף, או על הקרקע ואז הוא צריך לקפוץ. נקודות נוספות יתקבלו במידה והוא קופץ 2 צעדים לפני המפלצת כך שהוא נוחת בדיוק עליה ומוחץ אותה. 
          <br/><br/>
מריו יכול לקבל נקודות ע"י אסיפת פטריות שנמצאות במסלול.
          <br/><br/>
שימו לב שאף אחד מהפריטים לא זז. 
      </p>
 <h3> תיאור המשחק </h3>
    <p>
      פיתחנו משחק בו האלגוריתם יוצר באופן אקראי שלבים חדשים כך שלשחקנים יש מספר שלבים לשחק. אנו נשתמש באלגוריתם אבולוציוני שמגיב ומשתפר במהירות טובה - ראו גרפים מצורפים למטה.
    </p>
  
 <h3> פורמט השלבים וייצוג הפעולות </h3>
    <p>
אנו מבטאים כל שלב באמצעות מחרוזת רצופה של אותיות (string) ע"י הסימונים הבאים:
    </p>
    
  ![Table](https://github.com/Rotemfi/Evolution-Algorithm-project---Super-Mario/blob/main/Nw5wdMgmyG6JnpD.png)

     <p>
את המשחק קוראים, והוא גם רץ משמאל לימין. כך שהאות הראשונה במחרוזת תיאור המסלול מתארת את הנקודה הראשונה שמשחק והאות האחרונה מתארת את סיום המסלול (בו נמצא הדגל). לדוגמא:
   ![example]( https://github.com/Rotemfi/Evolution-Algorithm-project---Super-Mario/blob/main/images/BpxpATSJDPje53H.png)
     </p>
     <p>
         במצב הנתון לעיל מריו מתקדם משמאל לימין והמחרוזת המייצגת היא:
     </p>
  
<h3 align="center">'_ _ G _ M L _ _ G _ _ _ _'</h3>
       <p>       ניתן לראות שכדי לקבל את הניקוד המקסימלי מריו צריך לזוז רק ימינה ויש לו 3 אפשרויות פעולה. 
          <br/>
           התקדמות ימינה (מצב דיפולטיבי) - ייצוג ע"י '0'
          <br/>
          קפיצה למעלה (והתקדמות ימינה) - ייצוג ע"י '1'
          <br/>
           התכופפות מטה (והתקדמות ימינה) - ייצוג ע"י '2'
      </p>
        <p> 
            בעזרת ייצוגים אלו אנו מבטאים את הבחירות של השחקן להתקדמות, גם כן באמצעות רצף של תווים - מחרוזת. לדוגמא, עבור המסלול הנתון למעלה, אשר מורכב מ-13 חלקים, רצף פעולה אידיאלי עבור השלב שלעיל (כלומר, יאסוף את כל הפטריות, ימחץ את כל מפלצות הקרקע ויחמוק מכל מפלצות האוויר) הוא כדלקמן:
        </p> 

  <h3 align="center">'  0 0 0 1 0 2 0 0 1 0 0 0 '</h3>
  
 <h2>תיאור פתרון - אלגוריתם אבולוציוני </h2>
  <p>
     אלגוריתם אבולוציוני מורכב מכמה מחזורים של יצירת דורות שאנו רוצים שילכו שיתפרו.
  </p>
 <h3>מציאת גודל אוכלוסיה אופטימלי</h3>
 <h4> מבנה הפרט </h4>
 <p>כל פרט מורכב מוקטור באורך n (המייצג את אורכו של השלב במשחק)</br>
כאשר
 k&#8714{0,1,2}
vector[i] = k  
כלומר במקום ה-
i
של הוקטור, נמצאת הפעולה ה-
i.
כאשר במידה ו - 
 vector[i]=0
  אז מריו ממשיך להתקדם ימינה, ואם,
  vector[i] = 1
  מריו קופץ
  ,
   ואם vector[i] = 2 מריו מתכופף.

 </p>
 
  <h4> אתחול האוכלוסייה </h4>
  <p>
   נאתחל m (גודל האוכלוסיה שנבחר) וקטורים באורך n (אורך השלב הנתון) כך ש vector[i] =k   (k&#8714{0,1,2}) , וכל k נבחר רנדומלית.
  </p>
  <h4> חישוב הפיטנס </h4>
  <p>
  הפיטנס של קומבינצית צעדים תלוי בבחירת ההתמודדות עם המכשולים השונים בדרך, האם אוסף הפעולות גרם לסיום השלב או לא, ואורך המסלול שהצליח להגיע אליו. כל אלו יחד נותנים לאלג' את ההערכה של כמה טוב הוקטור הנבחר.
  </p>
    <p>
            <b> בחירות נקודתיות שמעלות את הfitness: </b></br>
        עבור קפיצה על מפלצת קרקע (גומבה) - מחסל אותה:
        <b> 2+ </b></br>
        עבור אכילת פטרייה:
        <b> 3+ </b></br>
        קפיצה על דגל הסיום:
        <b> 2+ </b></br>
  </p>
  <p>
        <b> בחירות נקודתיות אשר מורידות את הfitness: </b></br>
    קפיצה שלא לצורך:
    <b> 1- </b></br>
   ניסיון לבצע קפיצה רצופה:
    <b> 1- </b></br>
  </p>
  <p>
          <b> שרידות לאורך המסלול: </b></br>
  לנקודות ה"נצברות" במסלול נוסיף את כמות הצעדים הרצופים שהאלגוריתם הצליח להתקדם כדי לתת פיטנס טוב יותר לוקטורים שבהם בוצעו מספר רב של צעדים רצופים בלי להיפסל. אם הוא סיים את המסלול בריצה אחת רצופה נכפיל את כמות הצעדים ב-1.25 על מנת להעלות את הפיטנס בצורה ניכרת יותר מקרה זה.
  </p>
  
<h4> יצירת אוכלוסיה חדשה </h4>
    <p>
          - נבצע crossover על שני וקטורים באוכלוסיה בהסתברות 0.5.<br/>
          - על כל אחד מהוקטורים באוכלוסייה, אנחנו מבצעים מוטציה בהסתברות של k. <br/>
                    - בהמשך נציג ביצוע ניסויים על מנת למצוא את ה-k האופטימלי. פונקציית המוטציה בוחרת וקטור לבצע עליו את המוטציה בהסתברות k. פונקציית המוטציה בוחרת ביט בוקטור ומשנה אותו לפעולה אחרת שאותה מריו יבצע.<br/>
   - את האוכלוסיה החדשה נבחר על ידי ביצוע טורניר בגודל 4, בין הוקטורים באוכלוסיה הנוכחית.
 <br/>
    </p>
 <h2> התוכנה - מבט על </h2>
 <p>
 נעזרנו בסימולטור אשר מריץ שלב אחד של המשחק סופר מריו בעזרת הספרייה pygame. אנו משתמשים בספרייה eckity כדי לחשב את הריצה הכי טובה האפשרית של הבעיה ומשתמשים בסימולטור כדי להציג אותה.
 </p>
 <h4>תיאור הקבצים</h4>
 <p>
 התיקייה  <b>images</b> - מכילה תמונות המשמשות לסימולטור. </br>
 התיקייה <b>maps</b> - מכילה קבצי טקסט שכל קובץ טקסט מכיל סטרינג המייצג מפה של שלב 
במשחק.
 </br>
 הקובץ <b>output.txt</b> - מכיל את הנתונים מהריצה האחרונה של האלגוריתם.</br>
 הקובץ <b>constants.py </b> - מכיל משתנים קבועים אשר משמשים כהגדרות לסימולטור כגון גודל מסך, הגדרות של צבעים ותמונות. </br>
 הקובץ <b>map.py</b> - מכיל משתנים אשר משמשים כהגדרות המפה שנציג. </br>
 הקובץ <b>screen_manager.py</b> - מכיל את הקוד אשר מאתחל את המשחק ומריץ עליו את הפתרון שנחשב בעזרת האלגוריתם האבולוציוני. בקובץ ישנה מחלקה Display אשר אחראית להצגת המשחק על המסך. </br>
 הפונקציה <b>init</b> - מאתחלת את כל ההגדרות שהמשחק צריך - גדלים, צבעים ותמונות.
</br>
 הפונקציה <b>draw_cells</b> - אחראית על הדפסת המסלול והמפלצות על המסך. </br>
 הפונקציה <b>draw_in_potision</b> - אחראית להצגת דמות במיקום מסוים ספציפי כלומר להציג את מריו כאשר הוא זז על המסך. </br>
 הפונקציה <b>run_solution</b> - מקבלת פתרון ומריצה אותו בעזרת הפונקציות האחרות. </br>
הפונקציה <b>begin_display</b> -אחראית להניעה את הלולאה של הרצת הסימולטור והצגתו למסך. </br>
 הקובץ <b>mario_plot.py</b> - מכיל מחלקה Information אשר אנחנו משתמשים בה כדי להדפיס ניתוח נתונים בצורת גרף. </br>
הפונקציה <b>read_file</b> - קוראת את קובץ output.txt (אשר משמש לשמירת נתוני הריצה, הדפסות של האלגוריתם האבולוציוני) ומחלצת משם נתונים כגון התוצאה הכי טובה/גרועה/ממוצעת בכל generation . </br>
הפונקציה <b>plot_graph</b> - מדפיסה גרף על המסך בעזרת הנתונים שחולצו בפונקציה read_file. </br>
הקובץ <b>mario_evaluator.py</b> - מכיל את המחלקה SuperMarioEvaluator אשר מכילה את הפונקציה הבאה: </br>
הפונקציה <b>_evaluate_individual.py</b> - שתפקידה לחשב את הפיטנס של אינדיבידואל מסויים. </br>
הפונקציה <b>read_map.py</b> - קוראת מתוך קובץ טקסט את הסטרינג שמייצג מפה . </br>
הפונקציה <b>route_creator.py</b> -  יוצרת באופן רנדומלי מפה עבור המשחק.</br>
הקובץ <b>mario_main.py.py</b> -  מכיל את לב ריצת האלגוריתם פונקצית main. תחילה אנו מאתחלים את האלגוריתם האבולוציוני אשר מייצג פרטים בצורת וקטורים בדומה למה שהודגם בדוגמאות בכיתה. ההדפסות של האלגוריתם מועברות  לקובץ output.txt למטרות ניתוח והדפסת גרפים. לאחר חישוב הפתרון הסופי מודפס גרף והסימולטור רץ על הפתרון.
</br>
 

 </p>


 
 <h2>ניסויים, מהלך האבולוציה ותוצאות</h2>
   <p>
     תחילה רצינו לבדוק מה גודל האוכלוסייה שיהיה הטוב ביותר עבור האלגוריתם.
הרצנו את האלגוריתם האבולוציוני עם גדלי אוכלוסייה שונים: 100, 300, 500.
עבור כל גודל אוכלוסיה, הרצנו את האלגוריתם 20 פעמים ובדקנו את הממוצע של best fitness, worst fitness, average fitness עבור כל דור. מכיוון שהאלגוריתם מבצע בחירות אקראיות, הרצה של האלגוריתם פעם אחת אינה משקפת בצורה מספקת את טיבו, ועל כן בחרנו לבצע 20 ריצות שונות ולבדוק את הממוצע של כל הריצות יחד. 
את כל הניסויים ביצענו על שלב מספר 9.<br/>
<br/>
     <b>הגענו לתוצאות הבאות:</b>
  </p>
  <p>
     <u> עבור גודל אוכלוסיה של 100 וקטורים קיבלנו:</u>
  </p>
  <p>
  
   ![100vectors]( https://github.com/Rotemfi/Evolution-Algorithm-project---Super-Mario/blob/main/images/100%20vectorcs.PNG)
  </p>
  <p align="center">
    Best Fitness calculated: 80.5
    <br/>
    <b> best fitnessאין התכנסות ל</b>
  </p>
  <p>
     <u> עבור גודל אוכלוסיה של 300 וקטורים קיבלנו:</u>
  </p>
    <p>
  
   ![100vectors]( https://github.com/Rotemfi/Evolution-Algorithm-project---Super-Mario/blob/main/images/300%20vectors.PNG)
  <p align="center">
    Best Fitness calculated: 85.5
    <br/>
    <b> החלה מדור 36 best fitnessההתכנסות אל ה </b>
  </p>
  <p>
     <u> עבור גודל אוכלוסיה של 500 וקטורים קיבלנו:</u>
  </p>
     <p>
  
   ![100vectors]( https://github.com/Rotemfi/Evolution-Algorithm-project---Super-Mario/blob/main/images/500%20vectors.PNG)
  <p align="center">
    Best Fitness calculated: 85.5
    <br/>
    <b> החלה מדור 32 best fitnessההתכנסות אל ה </b>
  </p>
  
   <h3> מציאת ההסתברות האופטימלית לביצוע מוטציה על פרט באוכלוסיה</h3>
   <p>
     תחילה רצינו לבדוק מה גודל האוכלוסייה שיהיה הטוב ביותר עבור האלגוריתם.דבר נוסף שרצינו לבדוק הוא מה גודל ההסתברות האופטימלי לביצוע של מוטציה על פרט באוכלוסיה.
בדקנו את ההסתברויות הבאות: 0.01, 0.05, 0.09. גם פה ביצענו 20 ריצות ולקחנו את הממוצע של כל הריצות. בדקנו עבור אוכלוסיה בגודל 300.
  </p>
   <p>
     <u> :עבור הסתברות לביצוע מוטציה של 0.01 </u>
  </p>
  <p>
  
   ![0.01 probability]( https://github.com/Rotemfi/Evolution-Algorithm-project---Super-Mario/blob/main/images/0.01%20prop.PNG)
  <p align="center">
    Best Fitness calculated: 85.5
    <br/>
    <b> החלה מדור 81 best fitnessההתכנסות אל ה </b>
  </p>
  <p>
     <u> :עבור הסתברות לביצוע מוטציה של 0.05 </u>
  </p>
  <p>
  
   ![0.05 probability]( https://github.com/Rotemfi/Evolution-Algorithm-project---Super-Mario/blob/main/images/0.05%20prob.PNG)
  <p align="center">
    Best Fitness calculated: 85.5
    <br/>
    <b> החלה מדור 36 best fitnessההתכנסות אל ה </b>
  </p>
  <p>
     <u> :עבור הסתברות לביצוע מוטציה של 0.09 </u>
  </p>
  <p>
  
   ![0.09 probability]( https://github.com/Rotemfi/Evolution-Algorithm-project---Super-Mario/blob/main/images/0.09%20prob.PNG)
  <p align="center">
    Best Fitness calculated: 85.5
    <br/>
    <b> החלה מדור 51 best fitnessההתכנסות אל ה </b>
  </p>
  
  <h2>מסקנות</h2>
  <h3>גודל אוכלוסייה אופטימלי</h3>
  <p>
    מהבדיקות שביצענו על מנת למצוא את גודל האוכלוסיה האופטימלי ניתן לראות שעבור אוכלוסיה בגודל 100, אין התכנסות לפתרון האופטימלי כעבור 100 דורות.
עבור אוכלוסיות בגדלים 300 ו 500 -  ישנה התכנסות לפתרון האופטימלי כאשר עבור אוכלוסייה בגודל 300 ההתכנסות מתחילה מדור 36, ועבור אוכלוסייה בגודל 500 הוא מתכנס החל מדור 32.
  </p>
    <p>
    נשים לב שההתכנסויות בריצות השונות מתבצעות החל מדורות 32 ו-36 - שמאד קרובים אחד לשני, אך ריצה עם 500 וקטורים דורשת הרבה יותר זמן ריצה מאשר ריצה עם 300 וקטורים, ולכן נעדיף לספוג את ה"עונש" בהתכנסות של 4 דורות אבל לצמצם משמעותית את זמן הריצה של האלגוריתם.
  </p>
    <p>
    על כן הגענו למסקנה שגודל האוכלוסייה שנרצה לבחור הוא 300 - החיסרון הוא שהוא רץ 4 דורות יותר מהמקרה של גודל אוכולוסייה 500 - אך זהו מספר זניח, לעומת זמן הריצה שמשתפר משמעותית מגודל אוכלוסייה 500 ל-300.
  </p>
  <h3>אופן חישוב הfitness.</h3>
   <p>תחילה, חישבנו את הfitness בצורה דומה למה שהצגנו בעבודה בדרך קלאסית של הגדלת הfitness עבור צבירת נקודות מסלול, והורדה עבור פסילה או פספוס.  בנוסף לכך,  על כל התקלות במפלצת ("פסילה") החזרנו fitness של מינוס אינסוף כי לא רצינו שזו דרך הפעולה שתבחר. כתוצאה מכך הבחנו כי וקטורים רבים שיכולים להוות פתרון טוב בהמשך לא נבחרו - כלומר נדרשות עוד מספר פעולות crossover על מנת שיגיעו לכך. נתח גדול מוקטורים אלו מכילים את המסלול של הריצה האופטימלית, בשילוב חלק קטן שגורם לפסילה. חשבנו שאולי הפרזנו והחלפנו את ערך ה"קנס" ב-1000-. לדאבוננו הגענו לאותו מצב. </p
    <p>
    הפתרון שהגענו אליו הוא להוריד את גודל הקנסות באופן כללי, וחיפשנו פרמטרים אחרים שיהוו עבורנו אינדיקציה לפתרון. מצאנו כי להגדיל את הfitness (לתת "בונוס" לוקטור) עבור אורך המסלול - כמה הוא הצליח "לשרוד" במשחק. בנוסף לכך, עבור וקטור שצלח את ה מסלול כולו ללא פסילות נתנו בונוס מוגדל.
    </p>




    
</body>
</html>
