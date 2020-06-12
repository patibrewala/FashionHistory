def print_decade_info(chosen_year) :
    """Gets the fashion history of a particular decade

    Parameters
    ----------
    chosen_year: string or int
        The year whose decade history is to be found

    Returns
    -------
    info_return: string
        The fashion history of that decade

    """
    # Convert the string input to integer        
    get_info_year = int(chosen_year)

    info_2020 = """
It is currently 2020, a new decade where people are in lockdown. 
No fashion history available for current year.
"""
    
    info_2010s = """
The 2010s was defined by hipster fashion, athleisure, a revival of 
austerity-era period pieces and alternative fashions, swag-inspired outfits, 
unisex early 1990s style elements influenced by grunge and skater fashions. 
The later years of the decade witnessed the growing importance in the 
western world of social media influencers paid to promote fast fashion 
brands on Instagram. 

Flower crowns came back in the 2010s. High low dresses were also having 
their style moment. The cold shoulder detail just quietly swept over women’s 
fashion in the 2010s, highlighting a flattering part of the body and adding 
feminine flourishes to dresses and blouses. Pattern leggings and leggings in 
general took over 2010s fashion. Chokers, not just the black plastic ones, 
also came back strong.

The early to mid 2010s witnessed a revival of grunge fashion with more of an
"edgy" interest of denim ripped jeans, ripped jackets, flannels, animal 
prints which were frequently color or stone faded, black combat boots, and 
leather motorcycle jackets. 

Early 2010s:

The early 2010s saw many recycled fashions from the 50s, 70s, 80s as 
designers from stores replicated vintage clothing. Many late 2000s trends 
stayed popular. People also started wearing tribal inspired prints and neon    
colors. Fringe was once more having its moment.

Mid 2010s:

By the mid 2010s, neon colors were out of style. More subdued colors became 
popular such as burgundy, mustard yellow, olive green, mauve, and blush 
pink. Neutrals came back in full force. Wearing monochromatic clothing was a
huge trend of the time. Denim declined in popularity in the US, with yoga 
pants, leggings, and slim-fit jogger pants replacing them.

Late 2010s:

From 2017 to 2020, the brightly colored beige, red, green, brown and orange 
1970s revival fashions began to replace the grey and monochromatic of mid 
2010s. Gucci brought back loafers in style. Fashion trends were hugely 
influenced by influencers on Instagram, Pinterest and YouTube. 
Tiny sunglasses is a trend popularized by influencers. 
"""
    
    info_2000s = """ 
Many clothing trends in the 2000s were born out of globalization, the rise 
of fast fashion (affordable clothes based off runway designs), and 
celebrities’ growing influence as style icons.

Following the 1990s, fashion in the 2000s moved away from the minimalist 
approach, incorporating the fusion of trends from several different styles. 
By the early 2000s, designers began incorporating more color and pattern 
into their clothing. Women’s fashion took a more feminine turn as women 
began wearing denim miniskirts and jackets, halter tops, belly shirts, 
low-rise jeans, and capri pants. During the mid 2000s, the tunic dress 
gained popularity among young women and teenagers, often paired with a thin 
belt at the waist. By late 2000s, ballet flats had become a staple in 
women’s fashion, along with sweater dresses and long button-down shirts.

Interestingly, jean trends were all over the place in this decade. 
The ultra low ride jeans from early 2000s took a complete 180 into high 
waisted flared jeans from the late 2000s.

Early 2000s:

Casual clothing and leisurewear were the other big trends of the early 
2000s. Denim became a staple going beyond jeans to shirts, jackets, and 
hats. Casual clothing and leisurewear were the other big trends. The color 
palette was filled with shiny black tones and reflective metallics. 

Mid 2000s:

Mid 2000s fashion began to take cues from 1960s bohemian looks. Yoga pants, 
low-rise jeans, cowl-neck shirts, peasant tops, capri pants, cropped jackets,
and dresses over jeans were popular outfit choices for women. These were 
often paired with accessories like chunky belts, aviator sunglasses, ties 
worn around the neck or as belts, ballet flats, and platform boots.

Late 2000s: 

Crop tops were replaced with camisoles and miniskirts gave way to babydoll, 
bubble skirt, and sweater dresses reviving the 50s style. There was also a 
1980s and 1990s revival that reintroduced neon colors, animal prints, 
geometric shapes, light denim jeggings, and ripped acid washed jeans that 
were worn with gladiator sandals, ballet flats, and headbands. An oversized 
look started to gain popularity. Head accessories especially headbands came 
back in style. Emo style was also having its moment inspired by the scene 
movement.
"""
    
    info_1990s = """
The nineties, while not quite as loud as the eighties, took a minimalistic 
approach and tried to be a little smarter and a little classier. 
 
Some common items of clothing from the 1990s were black leggings with oversized 
sweater, low heel shoes, flannel shirts, denim everything, t-shirts, sweatpants, 
skirts, Birkenstocks, solid colors, silk shirts, turtlenecks (under cardigans or 
sweaters), plain white Keds and army surplus clothing to name a few.
    
Shear clothing was a huge trend of the time. Active wear and platform snekears 
were also huge back in the day. Moreover, the seventies look was really hot, 
with teens wearing tie dye shirts, bell-bottom jeans and long, straight hair. 
Chokers also came back in style in the 90s continuing in the 2000s.
    
Anything eighties was considered a bad thing. 
Most women didn’t want wild patterns and colors, they wanted simple and humble. 
Solid colors, preferably subdued was the way to go.
"""
    
    info_1980s = """
The 1980s were a decade of bold style, colors, and silhouettes— and heaping 
amounts of permed hair. Fashion for women evolved quite dramatically during the 
1980s. Apparel tended to be very bright and vivid in appearance. Punk fashion 
began as a reaction against both the hippie movement of the past decades and the 
materialist values of the current decade. Throughout the decade, elaborate 
licensed prints featuring cartoon and movie characters were much more popular 
than in decades before. It was a decade of shoulder pads, bubble hem dresses, 
acid wash dresses and big crazy hair styles.

In the early 1980s, women preferred soft fabrics and neutral colors. 
It witnessed a backlash against the brightly colored disco fashions of the late 
1970s in favor of a minimalist approach to fashion, with less emphasis on 
accessories. Around that time most every woman owned a turtleneck or six, and 
scarves made a huge comeback in the early 80s. Silk blouses were all the rage 
throughout the entire decade. Denim jeans were hot, arriving in styles with 
wild bleaching and dyeing. 

The mid- to late-eighties were a period of experimentation. From fabrics that 
changed color to clothes meant to be worn backwards, nothing was off limits. 
Bright neon colors were very popular and rocking brand names was more important 
than ever. Belts and bracelets were the most vital accessories in the wardrobe. 
Some fashion trends in the late 80s were inspired by the glam metal scene of the 
time.     
"""

    info_1970s = """
Fashion in the 1970s was about individuality. In the early 1970s, 
Vogue proclaimed "There are no rules in the fashion game now". Common items 
included miniskirts, bell-bottoms, vintage clothing from the 30s, 40s, and 50s, 
and the androgynous glam rock and disco styles that introduced platform shoes, 
bright colors, glitter, and satin. Above all, women could finally wear whatever 
they wanted. Sure, gender roles still played a part in wardrobe choices, but 
compared to previous generations, women’s fashion in the 1970s was nothing short 
of revolutionary. Hair was long and natural. Often times women could do their 
hair in minutes instead of hours.

Seventies fashion began with a continuation of the late 1960s hippie style. 
Extreme, bright colors were in high demand and long, flowing skirt and pants 
were everywhere. With every year, pants were flaring wider and wider. It was 
common for a pair of women’s wide-flare slacks to have 32″ around the bottom of 
the leg hem. Soon the flare exploded into bell bottoms and it couldn’t go 
anywhere but smaller from there. Another trend was emerging and soon took over 
the fashion world: suits including leisure suits, pant suits, jump suits and 
track suits. Women were wearing pants in every walk of life. Female executives 
were wearing business suits with pants, women at home were wearing jeans.

By 1974, the T-shirt was no longer considered underwear, and was by then made in 
elaborate designs such as slogans, sports teams, and other styles. In the 
mid-1970s, accessories were generally not worn, adopting a minimalistic approach 
to fashion akin to that of the 1950s. Activewear also became popular in this 
era. The disco spawned its own fashion craze in the mid to late 1970s. Young 
people gathered in nightclubs dressed in new disco clothing consisting of 
jumpsuits that was designed to show off the body and shine under dance-floor 
lights.    
"""
 
    info_1960s = """
Fashion of the 1960s featured a number of diverse trends. It was a decade that 
broke many fashion traditions, mirroring social movements during the time. 
Fashion became progressively more casual across all genders and ages. Broadly 
categorized, there were three main trends in 1960s womenswear: 1) the lady-like 
elegance inherited from the previous decade seen on the likes of First Lady 
Jacqueline Kennedy, 2) the fun, youthful designs popularized by Swinging London, 
and 3) the Eastern-influenced hippie styles of the late 1960s.

Style and trends in the early years of the decade reflected the elegance of the 
First Lady, Jacqueline Kennedy. In addition to tailored skirts, women wore 
stiletto heel shoes and suits with short boxy jackets, and oversized buttons. 
Simple, geometric dresses, known as shifts, were also in style. For evening 
wear, full-skirted evening gowns were worn; these often had a low décolletage 
and close-fitting waists. For casual wear, capris were the fashion for women and
 girls. The early 1960s gave birth to drainpipe jeans and capri pants, which 
 were worn by Audrey Hepburn. 

Mary Quant popularized the mini skirt, and Jackie Kennedy introduced the pillbox 
hat; both became extremely popular. False eyelashes were worn by women 
throughout the 1960s. Hairstyles were a variety of lengths and styles. 
Psychedelic prints, neon colors, and mismatched patterns were in style. 
Bikinis while invented in France in 1946, didn’t gain much popularity until 
mid 60s after the release of hit teen film Beach Party.

By 1966, the early-sixties look had become much sleeker and more modern. The 
lines were sharper and more form-fitting. Fur was less popular, but gloves were 
still a necessity. Most of this fashion sense was taken directly from the London 
mod scene.

But by the time the late sixties rolled around, all bets were off. Often times 
women were seen wearing the same clothes as men. That’s not to say that 
femininity was thrown completely out the window, but frankly, women’s clothing 
became more masculine while men’s clothing became more feminine. Starting in 
1967, youth culture began to change musically, and Mod culture shifted to a more 
laid-back hippie or Bohemian style. Fringe was also a huge deal at this point in 
time. The late sixties were the era of the flared-bottomed pants, foreshadowing 
the much more obvious bell-bottoms of the seventies. Polyester was a very common 
material and skirts were short. Women were no longer embarrassed to flaunt their 
stuff in public. Although wild colors were nothing new, in the late 1960s the 
patterns were even brighter. And then something crazy happened. The waistline 
disappeared again. Women were strolling around in tunics and culottes, with the 
wind flowing right through their comfortable, flowing and quite baggy gowns.    
"""

    info_1950s = """
In many ways, the 1950s took a big step back, especially for women. As men 
returned home from the war, women also returned to the home as wives, mothers, 
and homemakers. There was a migration to newly built suburbs where life was 
supposed to be picture-perfect and traditional. Society became very conservative
and there was a rise in affluence. Overall the fashion mood in the fifties 
leaned towards femininity and formality. The waistline was a major issue in the 
1950s. Some women really like the snug fit of the Dior dresses while others 
liked the dresses with no waistline, often referred to as “sack dresses.” 
No matter what time of day, throughout the decade, it was exceedingly important 
that a woman be impeccably turned out. This meant perfectly groomed hair, 
spotless makeup, and sets of matching accessories. 

The popular look that dominated womenswear in the 1950s actually emerged in the 
late 1940s. When Christian Dior’s “New Look” appeared in February 1947, it 
became an instant success and the nipped-in waist and full-skirted silhouette 
remained the leading style until the mid-1950s. As the decade progressed, the 
dominant silhouette became progressively straighter and slimmer, and as fashion 
began to look to the new “teenager” for inspiration, the elegance and formality 
of the early part of the decade began to lessen.

The full look of the 1950s was mature, glamorous, and very put-together. 
Dresses, skirts, and undergarments were constricting, but a wide range of new 
‘leisure clothes’ allowed people to dress casually at home. Women were expected 
to be impeccably dressed and groomed in public or when their spouse was home, 
always with coordinating hats, shoes, bags, belts, gloves, and jewelry. 
In privacy, women dressed much more simply and comfortably. 
Eventually, these casual fashions became public clothing as well.

The undergarments in the 50s were serious business. Corsets had gone out of 
fashion during the war and was replaced by gridle, a slightly more comfortable 
version of corset, and brassiere, also known as the ‘bullet bra’, in the 1950s. 
The ‘bullet bra’ emphasized the boobs to represent motherhood as it was a big 
focus for women in the 50s given the whole return to traditionalism thing.

Designers, led by Dior, started contracting out the manufacture of some 
clothing, and a wide range of accessories that were stamped with their labels. 
Everything from perfume to gloves, hats, bags, and ties were ‘branded’ by the 
designers. This practice is widespread today, as you can see by visiting any 
department store, but was a new idea in the ‘50s. Dior also set up boutiques 
all over the world – another novel idea that is the norm in fashion today.    
"""
 
    info_1940s = """
Fashion in the 1940s was a little sharper, a little more trim, and a LOT more 
modern. With the first half of the 1940s dominated by World War II, fashion 
stalled. Both men and women were often seen in their uniforms during the war 
and, if they were not, their clothing styles were dictated by rationing and 
Utility clothing. After the war, Christian Dior launched the New Look in Paris, 
returning women’s fashion to an overtly feminine silhouette.

Utility clothing and uniforms were the most ubiquitous forms of “fashion” during 
the war. Utility clothing could be bought with ration coupons. Both Utility 
dresses and uniforms adopted similar design elements: The look was simple but 
stylish, with good proportion and line. It incorporated padded shoulders, a 
nipped-in waist, and hems to just below the knee.

The war ended in 1945, but life did not immediately go back to normal and that 
included fashion. Clothes rationing stayed in. However, the smart simplicity of 
Utility clothing quickly lost its appeal with the launch in February 1947 of 
Dior’s defining post-war style, dubbed “The New Look” by fashion editor Carmel 
Snow. Gloves were a necessity. In almost any picture you find, women are wearing 
gloves.

In a nutshell, 1940s women’s fashion was about creating an hourglass silhouette 
with masculine details: padded shoulders, nipped-in high waist tops, and A-line 
skirts that came down to the knee. This was the everyday shape for clothing, 
from suits to dresses. Even pants had a similar high waisted, wide leg shape. 
1940s fashion accessories such as hats, gloves, handbags, and jewelry completed 
an outfit, while natural makeup with bright red lips painted a happy face during 
difficult times.    
"""
    
    info_1930s = """
As the 1920s turned into the 1930s, women’s fashion softly evolved from the 
boyish look of the previous decade into the feminine silhouette of the early 
thirties. The Great Depression began to affect the public, and a more 
conservative approach to fashion displaced that of the 1920s. For women, skirts 
became longer, and the waistline was returned up to its normal position. 
A return to conservatism after the Roaring Twenties also marked fashion during 
this period. By the early 1930s, the fashionable silhouette was evolving into 
a slender, elongated torso with widening shoulders and a neat head with softly 
waved short hair. Though the lines were simple, the overall effect was one of 
complete sinuous femininity with a natural waist and skirts flaring out slightly 
at the ankle.

In the 1930s, women wore dresses everywhere. It didn’t matter if they were at 
work or at home, it was vital to wear a dress. Ensembles that included an 
overcoat were very popular as well. Women did not show much skin. In the mid30s 
some women also decided they were no longer going to wear hats. 
Patterns were all the rage and nice, flowing, flowery dresses were the most 
popular item a woman could wear. Fur was still quite popular, although during 
the depression most women were still making their own clothing.

In the 1930s, fashion saw a profound influence from films. Hollywood 
disseminated fashion to the masses and stars like Greta Garbo, Marlene Dietrich,
 and Bette Davis, among others, became some of the first Hollywood style icons. 
 Many women all over the world attempted to emulate their style. Making this a 
 little easier was a rise in makeup and the beauty industry, allowing women to 
 copy their favorite stars at a small cost.    
"""
    
    info_1920s = """
For nearly one hundred years, 1920s fashion has been known as one of the most 
glamorous and innovative periods in modern fashion history. Fashion in the 
roaring twenties gained comfort while showing off an entirely new and outrageous
use of color and decoration. Twenties fashion is often remembered for its glitz 
and glamour, though underlying this was a move toward simplicity in dress. 
For women, this meant shorter skirts and simple shapes.

1920s clothing left behind the prim and proper mold of Victorian ideals and 
launched into more free-spirited and casual clothes. Women’s fashion in the 20s 
is distinguished by a long, straight silhouette. Slender was the “in” look — 
curves were not accentuated at all. Small hats were in high demand, as were 
thin, white gloves. Coats had fur and shoes generally had heels. Brooches and 
pearl necklaces were common accessories for the modern woman. Purses were not 
common, as most women carried their money in billfolds.

This simplicity created the popular tubular “la garçonne” look that dominated 
much of the decade. Also known as the flapper, the look typified 1920s dress 
with a dropped waist and creeping hemlines that could be created in economical 
fabrics. Evening dresses sometimes still nearly reached the ground, though many 
of the popular styles followed the hemline trends of daywear.

Both waistlines and hemlines followed similar, though inverse, projections 
throughout the decade, as waistlines dropped until 1923 before beginning to 
rise again in 1928; while hemlines rose until 1926, when they started to fall 
again.

Another trend for women that enjoyed massive popularity in the twenties was 
that of sportswear worn as daywear. Sportswear had long been an acceptable form 
of casual wear for men, but in the 1920s, it also became acceptable for women.    
"""
    
    info_1910s = """
Fashion in the 1910s, like the decade itself, may be divided into two periods: 
before the war and during the war. World War I had a profound effect on society 
and culture as a whole and fashion was no exception. While changes in women’s 
fashion that manifested in the 1920s are often attributed to changes due to 
World War I, many of the popular styles of the twenties actually evolved from 
styles popular before the war and as early as the beginning of the decade.

The 1910s opened with a softer silhouette than the decade before, which was 
dominated by the “S-shape.” While the contorted shape created by 
straight-fronted corsets had softened into a more natural silhouette, the 
style in the early years of the decade still had an emphasis on the bust that 
echoed styles of the previous decade. 

Early in the period, waistlines were high (just below the bust), echoing the 
Empire or Directoire styles of the early 19th century. Full, hip length 
"lampshade" tunics were worn over narrow, draped skirts. The Art Deco movement 
began to emerge at this time and its influence was evident in the designs of 
many couturiers of the time. Simple felt hats, turbans, and clouds of tulle 
replaced the styles of headgear popular in the 1900s. By mid 1910s, skirts were 
widest at the hips and very narrow at the ankle. These hobble skirts made long 
strides impossible. Waistlines were loose and softly defined. They gradually 
dropped to near the natural waist by mid-decade, where they were to remain 
through the war years. Tunics became longer and underskirts fuller and shorter. 
By 1916 women were wearing calf-length dresses.

In 1914, the world was thrown into the “war to end all wars.” Tunics worn over 
skirts were a popular wartime fashion, as were simple, utilitarian clothing. 
Women began to wear uniforms, including overalls and trousers, as they worked in 
munitions factories for the war effort. Changed dresses during World War I were 
dictated more by necessity than by fashion. As more and more women entered the 
workforce, they demanded clothes that were better suited to their new 
activities; these derived from the shirtwaists and tailored suits. Social events
were postponed in favor of more pressing engagements and the need to mourn the 
increasing numbers of dead, visits to the wounded, and the general gravity of 
the time meant that darker colors and simpler cuts became the norm. 
A new monochrome look emerged that was unfamiliar to young women in comfortable 
circumstances. Women dropped the cumbersome underskirts from their 
tunic-and-skirt ensembles, simplifying dress and shortening skirts in one step.

After the war ended, simple styles continued, and a “barrel”-like silhouette 
emerged. Skirts were still long, but an attempt was made to confine the body in 
a cylinder”. This would eventually develop into the popular flapper look of the 
next decade.
"""
    
    info_1900s = """
While technology progressed in the first decade of the twentieth century, 
fashion largely remained the same. Subtle changes in silhouette occurred in 
womenswear until the tubular shape of the 1910s was beginning to emerge by the 
end of the decade. Lace and other embellishments were key. Fashion for women in 
the first decade of the twentieth century largely followed the fashion of the 
previous century. The highly structured silhouette of the Gibson Girl was still 
popular at the beginning of the decade.

For a large part of the decade, the fashionable silhouette continued to be 
dominated by the S-shape created by a new “health” corset. These corsets pushed 
the bust forward and the hips back in an attempt to avoid pressure on the 
abdomen. The shape emphasized a narrow waist and large “mono-bosom”. Tops were 
blousy and loose, the extra fabric helping to emphasize this top-heavy shape. 
Sleeves were equally dramatic. The effect was enhanced with petticoats that had 
full backs and smooth fronts. Modesty was emphasized with day dresses covering 
the body from the neck to the floor and long sleeves covering the arms. Skirts 
were bell-shaped and lace was a popular decoration. Colors were light but 
embellished with decorations. Overall, the prevailing look was that of a mature, 
sophisticated, and graceful woman.

Evening dress largely followed the same silhouette, though these gowns were more 
revealing with very low décolletage and short sleeves. The sleeve length was 
offset by the wearing of long gloves. Where day dresses had blousy, 
high-collared bodices, evening gowns had more fitted bodices with low-cut necks. 
Sleeves could also be draped, and necklines were sometimes off-the-shoulder.

While the wealthy woman wore the extravagantly decorated styles of the 1900s, 
many women were beginning to work outside the home. These women needed something 
more practical to wear and this came in the form of the “tailor-made.” These 
suits were introduced in the late 1800s and both working, and wealthy wore them 
in the 1900s. Tailored suits became more popular for the women that were 
beginning to work in white collar jobs. Tailored suits with no frills allowed 
for women maintaining an office job to seem more masculine and blend into the 
male dominated environment. Shortly the number of women attending colleges 
increased, and the shirtwaist became popular among the average college girl. 
The outfit worn by the typical college girl was a skirt that was usually shorter 
than current fashion, and a shirtwaist, which is best described as the 
equivalent of jeans and a T-shirt today.

As the decade progressed, fashions began to soften. The rigid S-bend shape 
popular in the early part of the decade gradually straightened out into a more 
natural shape. The loose tops and oversized sleeves became narrower, as did 
skirts. Waists were higher and the tubular silhouette that would become popular 
in the next two decades began to emerge. As fashion moved into the 1910s, styles 
were moving quickly towards the slimmed down shapes that would dominate the next 
two decades, while embellishment and long skirts continued from earlier in the 
decade.    
"""
 
    info_1890s = """
The 1890s were a transitional decade from the stiff Victorian Era to a new 
century. New freedoms and technologies drove an era that became known as the 
“Gay Nineties.”

As the century drew to a close, the world began to move away from the stiff, 
moralistic, Victorian Era (Laver 211). Urban centers were growing, and new 
technologies, such as the introduction of electricity into clothing 
manufacturing, produced a boom in the ready-to-wear market. The “New Woman” of 
the era was an intellectual young female who worked, cycled, and played sports.

By 1892, the dramatic, protruding bustle had completely disappeared, and the 
silhouette most associated with the 1890s took hold. Skirts were bell-shaped, 
gored to fit smoothly over the hips, while bodices were marked by the large 
leg-o-mutton or gigot sleeves. Beginning in 1890 with a small puff at the 
shoulder seam, sleeves grew in size until reaching an apex in 1895. The width 
at the top and bottom of the silhouette was balanced by a nipped waist, to 
create an hourglass effect. Around 1897, the silhouette began to slowly shift 
with the introduction of the straight-front corset. Supposedly designed as a 
healthier alternative, these new corsets forced a woman’s chest forward and hips 
backward into a curvilinear “S” shape, that became the dominant silhouette by 
1900.

Early 1890s dresses consisted of a tight bodice with the skirt gathered at the 
waist and falling more naturally over the hips and undergarments than in 
previous years. Puffy leg-of-mutton sleeves (also known as gigot sleeves) made a 
comeback, growing bigger each year until reaching their largest size around 
1895. 
During the mid-1890s, skirts took on an A-line silhouette that was almost 
bell-like. The late 1890s returned to tighter sleeves often with small puffs or 
ruffles capping the shoulder but fitted to the wrist. Skirts took on a trumpet 
shape, fitting more closely over the hip and flaring just above the knee. 
Corsets in the 1890s helped define the hourglass figure. In the very late 1890s, 
the corset elongated, giving the women a slight S-bend silhouette that would be 
popular well into the Edwardian era.

Morning wear featured high necklines and long sleeves, while afternoon clothing 
opened at the neck and featured shortened sleeves, and finally, evening wear 
bared the chest and arms. Women generally arranged their hair in high, neat 
chignons with soft curls at the front. Hats were an all-important accessory 
and were available in a variety of styles. Usually, 1890s hats were wide and 
heavily trimmed with tall upwardly curling feathers, ribbons, and flowers.
"""

    info_1880s = """
1880s women’s fashion was defined by the rigidly structured bustle and an 
abundance of decoration. Dress reformers, influenced by artistic movements, 
protested these heavy, ultra-restrictive trends.

Fashion in the 1880s was increasingly slender and angular, marked by heavy 
decoration. Throughout the decade, the focus of clothing design was concentrated 
at the back, a continuation of trends that began in the 1870s. 

The 1880s featured two distinct silhouettes in women’s fashions. 

The first was marked by the “princess line” and had begun earlier, around 1877. 
It was a dress without a horizontal waist seam, instead molded snuggly to the 
body by vertical seams and tucks, creating a body-hugging silhouette. Similarly, 
this long, slim line could be created with a cuirass bodice, which emerged as 
early as 1875; it consisted of a long, tightly fitted bodice that extended over 
the hips.

The second silhouette of the 1880s began developing around 1883 and disappeared 
in the 1890s. By 1884, the bustle had returned, this time a hard, shelf-like 
protrusion that projected from the small of the back. This bustle was rigidly 
structured, as opposed to the soft, draped bustle of the 1870s. The 
undergarments contrived to support this look became increasingly complex. 
The bustle reached its largest size by 1886. After about 1888, the bustle began 
to slowly shrink in size until 1891, when it gave way to the bell-shaped skirts 
of the 1890s.

Throughout the 1880s, day bodices and dresses featured high, narrow shoulders 
descending into impossibly tight sleeves, a departure from the low, sloping 
shoulders of the past few decades. Collars were tall and fitted, sometimes 
boned for shaping. During the day, hemlines were usually just above the floor. 
Bodices could feature long basques or designs that appeared to be a jacket and 
vest, in imitation of menswear fashions.

Perhaps womenswear in the 1880s was most marked by the weightiness of 
decoration. Womenswear featured an extensive use of trims, including ribbons, 
ruffles, flounces, shirring, bows, and lace; this over-decoration was not only 
seen in the evening, but throughout the day. Women began to wear their hair more 
neatly in the 1880s. The long, cascading curls of the previous decade were now 
tucked up into tight chignons. As the female form became angular and protruded 
from the back, hats rose in height to balance the silhouette. Tall, narrow hats 
were worn directly on top of the head.

No discussion of 1880s fashion is complete without mention of the Aesthetic 
Movement and the calls for dress reform. Throughout the second half of the 
nineteenth century, several artistic groups were reacting against the new, 
industrial era, and looking to the past for true beauty. These movements, 
arguably, all coalesced in their influence on fashion in the 1880s. 
For women, Aesthetic dress consisted of a dress with a loosely-fit waist, 
puffed sleeves, and, most importantly, was often worn without a corset or heavy 
petticoats and bustles. Aesthetic dress was also notable for its earth-toned 
colors, such as mossy green and ochre yellow.    
"""
    
    info_1870s = """
During the 1870s, women’s clothing became increasingly complex, colorful, and 
restrictive. In the late 1860s, the volume of the skirt had begun to swing 
backwards, a departure from the circular skirts of the mid-century. This trend 
became fully realized in the 1870s, with the focus of clothing concentrated at 
the back, as skirts projected backwards and fell flat against the body in the 
front. The decade saw two distinct silhouettes in womenswear, both maintaining 
the focus on the back of the skirt.

The first silhouette of the decade began in 1870; the great, circular or oval 
crinolines of previous decades collapsed into the so-called first bustle style. 
The bustle was a softly draped protrusion at the back of the waist, created by a 
manipulation of fabric and drapery. This sloped bustle style was supported by 
horsehair-ruffled petticoats or crinolettes, an adaption of the earlier steel 
crinolines. A crinolette consisted of rows of fabric-covered steel half-hoops. 
Bustled dresses of this period were frothy confections, with layers of ruffles, 
pleats, and gathers. Many featured looped overskirts or long bodices that were 
draped up over the hips; these were often referred to as “polonaise” style 
dresses.

The silhouette of the first half of the 1870s was also defined by a higher than 
natural waistline and lower sloped shoulders. In the first years of the decade, 
the bell-shaped sleeves of the 1860s continued to be seen. Bodices were 
frequently quite as decorated as the skirts. Daytime bodices had high necklines, 
as was customary throughout most of the nineteenth century. During the early 
1870s though, it became common for day bodices to open at the front into a 
V-neck or square neckline. These open necklines were almost always trimmed with 
ruffles, ribbons, lace, or braid, usually echoing the trim of the skirt. 
Importantly, these revealing necklines caused a trend for prominent necklaces 
such as velvet chokers and jet pendants. 

The second silhouette of the 1870s began around 1876. The bustle collapsed into 
the “princess line” style. Named for Alexandra, Princess of Wales, who 
popularized the look, it consisted of a dress without a horizontal waist seam, 
fitted instead with long, vertical tucks and darts to create an extremely slim, 
body-conscious look. Similarly, the princess line was echoed in the cuirass 
bodice; it did not have a waistline seam and was lengthened to fit over the 
hips. Snug around the hips, princess line dresses and cuirass bodices lacked a 
bustle, with volume instead spilling from below the hips, and sometimes from 
below the knees. This fullness could extend into long trains, even on day 
dresses. The waistline dropped to the natural waist in princess line looks. 
Additionally, shoulder seams began to creep slowly upwards, and sleeves 
tightened, further accentuating the long, slim line. This newly figure-framing 
style required more severe corsetry. Corsets lengthened over the hips to secure 
the body into the fashionable slim princess silhouette. 

Throughout the decade, bonnets, defined by the strings tied around the chin, 
were seen alongside the ever more fashionable hat, differentiated by its lack of 
strings. Hairstyles were elaborate during the first half of the 1870s. Women’s 
hair, usually parted in the center and waved around the face, was piled up in an 
intricate knots and braids with cascades of curls falling down the back; false 
hair was generally worn. This “waterfall hairstyle” pushed headwear up and 
forward to perch over the forehead. These precariously tipped hats and bonnets 
were frequently heavily trimmed with falls of flowers and ribbons. Hairstyles 
simplified with the introduction of the princess line, and by the end of the 
decade, hair was worn in high, tight chignons without loose curls. With the new, 
neat hairstyles, hats took on more definite shapes, created out of dense felts 
and straws.    
"""
    
    info_1860s = """
The silhouette of the 1860s was defined by the cage crinoline or hoop skirt, 
a device that emerged in the late 1850s, consisting of a series of concentric 
steel hoops attached with vertical bands of tape or braid. Eliminating the need 
for multiple heavy petticoats to achieve the fashionable wide skirts, cage 
crinolines allowed skirts to reach their largest circumference around 1860. 
Hoops were relatively affordable, creating a fashion that was worn throughout 
society. Throughout the decade, the shape of the cage crinoline subtly changed, 
altering the entire silhouette with it. In 1860, it was huge, often measuring 
twelve to fifteen feet in circumference, and dome-shaped; that is almost equally 
circular all the way round, the shape that defined the 1850s. By about 1862, 
the cage began to swing toward the back, becoming pyramid-shaped, the silhouette 
for the majority of the decade. By 1868, it had flattened in the front and most 
of the volume was at the back. In fact, in 1868, the crinolette, a series of a 
half-hoops only supporting volume at the back, was beginning to be worn.

Womenswear consisted of a fitted bodice, a variety of sleeve styles, and a 
floor-skimming wide skirt. The cage crinoline was worn over a chemise, drawers, 
and a corset. Corsets shortened as there was no need to confine the hips. 
In general, corsets were not tight-laced during this period; the sheer size of 
the skirts made waists appear small by comparison. The location of the waistline 
moved upwards during the 1860s, creating a short-waisted effect that would carry 
into the bustle silhouette of the 1870s. Around 1865, it also became common for 
the topmost skirt layer to be drawn upwards to reveal the underskirt or 
petticoat beneath, particularly in walking dresses or those worn for sporting. 
Petticoats, now often exposed, could then be found trimmed with ruffles along 
the hem and made in bold colors and patterns. 

In the evening, the neckline of dresses dropped off-the-shoulder and could be 
straight or dipped in the center. Sleeves were very short, sometimes mere straps 
across the shoulders. Regarding outerwear, shawls continued to be favored, 
especially as the wide skirts were a perfect surface upon which to display a 
large Paisley or “India” shawl. However, jackets were increasingly worn, 
particularly toward the end of the decade. The paletot, a three-quarter length 
jacket, featured loose sleeves and draped gently from shoulder to hem. 

In the 1860s, a trend for skirts paired with shirtwaists, or blouses, as opposed 
to a matching bodice became prevalent for casual daytime wear, especially among 
young women. Women wore their hair parted in the center and smoothly combed back 
into a chignon, sometimes featuring small curls or braids above the ears. The 
hair net, or snood, was an all-important accessory, usually made of chenille 
yarns or silk, worn looped around the chignon at the back. Late in the decade, 
hairstyles became more complicated; curls were left loose in the back underneath 
ever larger arrangements of braids and chignons. False hair became commonplace, 
sold in puffs, curls, and braids. As hairstyles grew in size and complexity, 
the snood fell out of fashion. Throughout the decade, both the bonnet, defined 
by its strings tied around the chin, and the hat, which lacked such strings, 
were worn. Bonnets shrank to a small depth and were worn tipped back on the 
head. Hats, meanwhile, were worn at the center of the head, and were generally 
low-crowned, round, and could feature a wide or narrow brim.

Technology and invention were evident in the fashion of 1860s women. Firstly, 
the use of the sewing machine grew exponentially. Secondly, synthetic dyes were 
becoming all the rage. 

The 1860s witnessed the rise of one of the most important characters in 
nineteenth-century fashion, Charles Frederick Worth, who is celebrated as 
“the father of haute couture”.     
"""
    
    info_1850s = """
The fashionable silhouette of the 1850s was defined by a small waist, drooping 
shoulders, and a voluminous skirt that steadily grew in size through the decade. 
By 1853, the long, dropped waistline of the 1840s rose to its natural position, 
and as a result, the emphasis on tight lacing lessened as the corset shortened 
and flared. By far, the most important characteristic of 1850s womenswear was 
the dome-shaped skirt with its fullness evenly distributed. The large skirt was 
supported underneath by multiple petticoats, sometimes up to seven at once. 
At least one of these petticoats would typically be a crinoline, a type of 
petticoat that was stiffened with horsehair. In 1856, the cage crinoline, a 
device consisting of a series of concentric steel hoops, was introduced; it 
provided immediate relief from the multiple heavy and cumbersome petticoats. 
It allowed skirts to reach new proportions, especially between 1858 and 1862. 
Relatively inexpensive, the cage crinoline was worn at all levels of society. 

Daytime dresses featured high necklines, often completed with a wide white 
collar, long sleeves, and most frequently, a straight or curved waistline. 
The narrow-fitted sleeve of the 1840s began to loosen at the end of the decade, 
and in the 1850s, sleeves became wide and open, expanding from either the 
shoulder or the elbow. These sweeping “pagoda” sleeves were worn with removable 
white undersleeves called “engageantes” that puffed and closed at the wrist. 
Reaching the widest point from 1857 to 1860, the pagoda sleeve was often trimmed 
with bows and fringed epaulettes. 

During the 1850s, it became common to have a dress made in two pieces: a skirt 
and a separate matching bodice. Sometimes a skirt would have two matching 
bodices, one for day and one for evening. The volume of the 1850s skirt was 
often emphasized by tiered flounces, sometimes made in fabric that was woven a 
disposition, meaning it was woven specifically for these flounces. In the 
evening, the high-necked, long-sleeved day bodice was traded for one baring the 
chest and shoulders. Evening sleeves were short, and frequently, the waistline 
would end in a point.

Regarding outerwear, the shawl reigned supreme as it draped beautifully across 
the sweeping skirts. Cashmere shawls, either imported from India for those who 
could afford it, or the cheaper imitations made in France, England, and 
Scotland, were the dominant choice. The hairstyle in the 1850s was parted in 
the center, brushed down and arranged heavily on the sides, completely covering 
the ears. Bonnets remained the vastly dominant choice of millinery, but they 
changed subtly from the inhibiting style of the previous decade. Brims shortened 
away from a woman’s face, and it was worn further back on the head, exposing 
more hair. 

Any discussion of 1850s womenswear would be incomplete without mention of 
Bloomers. In Seneca Falls, New York, in 1851, feminist leaders Elizabeth Smith 
Miller, Elizabeth Cady Stanton, and Amelia Jenks Bloomer shocked the nation when 
they stepped out in their reform costume: a shortened skirt worn over “Turkish 
trousers”. The outfit, and more specifically the trousers, were nicknamed 
“Bloomers” after Amelia, despite the fact that she did not invent the costume. 
An explicit reaction against the increasingly restrictive and burdensome women’s 
fashions, the Bloomer costume became inseparably associated with the early 
feminist movement, and it was an 1850s sensation. Reported, and more often 
savagely ridiculed, throughout the press, bloomers never became mainstream 
dress. The idea of women wearing trousers offended deeply held beliefs about men 
and women and their “separate spheres,” and stoked wild fears about a possible 
sexual revolution. It made an indelible mark on the fashion landscape of the 
mid-nineteenth century, and adaptations survived in later athletic womenswear.    
"""  
 
    # dictionary to get history of a decade 
    # with deade as the key and its histroy as the value
    decade_dict = {
        "2020" : info_2020,
        "2010s" : info_2010s,
        "2000s" : info_2000s,
        "1990s" : info_1990s,
        "1980s" : info_1980s,
        "1970s" : info_1970s,
        "1970s" : info_1970s,
        "1960s" : info_1960s,
        "1950s" : info_1950s,
        "1940s" : info_1940s,
        "1930s" : info_1930s,
        "1920s" : info_1920s,
        "1910s" : info_1910s,
        "1900s" : info_1900s,
        "1890s" : info_1890s,
        "1880s" : info_1880s,
        "1870s" : info_1870s,
        "1860s" : info_1860s,
        "1850s" : info_1850s,
        }  

    #list containing all year in a decade 
    list2010s = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    list2000s = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]
    list1990s = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
    list1980s = [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989]
    list1970s = [1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979]
    list1960s = [1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969]
    list1950s = [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959]
    list1940s = [1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949]
    list1930s = [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939]
    list1920s = [1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929]
    list1910s = [1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919]
    list1900s = [1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909]
    list1890s = [1890, 1891, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899]
    list1880s = [1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889]
    list1870s = [1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879]
    list1860s = [1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869]
    list1850s = [1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859]
    
    info_return = "Fashion history could not be found. Please try again!"

    # invalid input if input is not 4 digits
    if get_info_year < 1000 or get_info_year > 9999:
        info_return = "Year not entered correctly. Please try again!"

    # history of current year/decade
    elif get_info_year == 2020:
        info_return = decade_dict["2020"]
    
    # history of 2010s decade    
    elif get_info_year > 2009 and get_info_year < 2020:
        for year in list2010s:
            if get_info_year == year:
                info_return = decade_dict["2010s"]
    
    # history of 2000s decade  
    elif get_info_year > 1999 and get_info_year < 2010:            
        for year in list2000s:
            if get_info_year == year:
                info_return = decade_dict["2000s"]

    # history of 1990s decade  
    elif get_info_year > 1989 and get_info_year < 2000:           
        for year in list1990s:
            if get_info_year == year:
                info_return = decade_dict["1990s"]
   
    # history of 1980s decade               
    elif get_info_year > 1979 and get_info_year < 1990:
        for year in list1980s:
            if get_info_year == year:
                info_return = decade_dict["1980s"]
   
    # history of 1970s decade                 
    elif get_info_year > 1969 and get_info_year < 1980:
        for year in list1970s:
            if get_info_year == year:
                info_return = decade_dict["1970s"]
                   
    # history of 1960s decade 
    elif get_info_year > 1959 and get_info_year < 1970:
        for year in list1960s:
            if get_info_year == year:
                info_return = decade_dict["1960s"]
                   
    # history of 1950s decade 
    elif get_info_year > 1949 and get_info_year < 1960:
        for year in list1950s:
            if get_info_year == year:
                info_return = decade_dict["1950s"]
               
    # history of 1940s decade 
    elif get_info_year > 1939 and get_info_year < 1950:
        for year in list1940s:
            if get_info_year == year:
                info_return = decade_dict["1940s"]
                   
    # history of 1930s decade 
    elif get_info_year > 1929 and get_info_year < 1940:
        for year in list1930s:
            if get_info_year == year:
                info_return = decade_dict["1930s"]
                     
    # history of 1920s decade 
    elif get_info_year > 1919 and get_info_year < 1930:
        for year in list1920s:
            if get_info_year == year:
                info_return = decade_dict["1920s"]
                     
    # history of 1910s decade 
    elif get_info_year > 1909 and get_info_year < 1920:
        for year in list1910s:
            if get_info_year == year:
                info_return = decade_dict["1910s"]
                       
    # history of 1900s decade 
    elif get_info_year > 1899 and get_info_year < 1910:
        for year in list1900s:
            if get_info_year == year:
                info_return = decade_dict["1900s"]
                   
    # history of 1890s decade 
    elif get_info_year > 1889 and get_info_year < 1900:
        for year in list1890s:
            if get_info_year == year:
                info_return = decade_dict["1890s"]
                   
    # history of 1880s decade 
    elif get_info_year > 1879 and get_info_year < 1890:
        for year in list1880s:
            if get_info_year == year:
                info_return = decade_dict["1880s"]
                   
    # history of 1870s decade 
    elif get_info_year > 1869 and get_info_year < 1880:
        for year in list1870s:
            if get_info_year == year:
                info_return = decade_dict["1870s"]
                   
    # history of 1860s decade 
    elif get_info_year > 1859 and get_info_year < 1870:
        for year in list1860s:
            if get_info_year == year:
                info_return = decade_dict["1860s"]
                   
    # history of 1850s decade 
    elif get_info_year > 1849 and get_info_year < 1860:
        for year in list1850s:
            if get_info_year == year:
                info_return = decade_dict["1850s"]       
        
    return info_return

def print_apparel_info(chosen_apparel):
    """Gets the fashion history of a particular clothing article

    Parameters
    ----------
    chosen_year: string
        The apparel whose history is to be found

    Returns
    -------
    info_return: string
        The fashion history of that apparel

    """

    # convert the input to lowercase and remove all the spaces
    get_info_apparel = chosen_apparel.lower().replace(' ', '')

    info_crop_top = """
A crop top is a top that exposes the waist, navel, or abdomen.

The early history of the crop top intersects with cultural views towards 
the midriff, starting with the performance of "Little Egypt" at the 1893 
Chicago World's Fair. However, the first crop top was not accepted by Western 
fashion until the 1940s since an exposed midriff was immodest. 
Although the crop top started gaining prominence in the fashion industry 
during the 1930s and 1940s — the latter in particular due to fabric rationing in 
World War II — it was largely confined to swimwear at the time. It was not 
until the sexual revolution of the late 1960s and early 1970s that it 
started to achieve widespread acceptance. 
In the 1980s, cutoff crop tops became more common as part of the aerobics 
craze and as a result of the popularity of the movie Flashdance. 
The biggest pop culture rise of crop tops was in the 1990s. From being seen 
on television shows like Saved by the Bell to teen movies like Clueless. 
Although the crop top trend dropped a bit in the early 2000s, it experienced 
a revival due to the popularity of 1990s retro fashion in the 2010s.
"""
         
    info_bikini = """
The bikini, a two-piece bathing suit of diminutive proportions, 
first appeared on the fashion scene in the summer of 1946. 
Its impact was compared to that of the atomic bomb tests conducted that 
same summer by the United States at Bikini Atoll in the Pacific Islands, 
which was arguably the source of its name. Both the French couturier Jacques 
Heim and the Swiss engineer Louis Reard are credited with launching the skimpy 
two-piece, which they dubbed the atome and bikini, respectively.

At first, the bikini was more of a sensation than a success. French women 
welcomed the design but the Catholic Church, some media, and a majority of the 
public initially thought the design was risqué or even scandalous. 
At the outset, bikinis were facing possible bans at beaches across European, 
Mediterranean, and Catholic nations, and even the Miss World Contest and 
pageants worldwide. 
Tides began to change in the 1960s and even Neiman Marcus was declaring the 
bikini the “next big thing.” The bikini gradually grew to gain wide acceptance 
in Western society. The bikini’s popularity continued to be driven by aesthetics 
in the late 1980s when thong swimsuits spread from Brazil to the US. However, 
in the 1990s, athletes and feminist activists alike began pushing against the 
bikini, arguing that the suits were simply a tool for objectification. 

Despite the initial controversy, the bikini has become a perennial in swimwear 
fashion, particularly among the young.
"""

    info_bodysuit = """
A bodysuit is a one-piece form-fitting or skin-tight garment that covers the 
torso and the crotch, and sometimes the legs, hands, and feet, and cannot be 
used as a swimsuit.[1] The style of a basic bodysuit is similar to a one-piece 
swimsuit and a leotard, though the materials may vary. 

Evolving from the leotard, the bodysuit made its way out of the athletic wear 
category and into day-to-day closets. It was presented in the United States 
after 1950 by fashion designer Claire McCardell. It was worn as a blouse or 
T-shirt. Though snug, bodysuits were typically cut with a high neck and long 
sleeves. Since they could be paired easily with a variety of other separates, 
they became quite popular. 

The 1950’s did not generate much interest in bodysuits, but from the 1960’s 
onward, women began to appreciate the simple, modern concept of “body clothes.” 
The bodysuit became the 1970’s version of athleisure- everyone wore a leotard, 
cat suit, or bodysuit as a part of their fashion wardrobe. It was a fashion item 
for both men and women in by the 1980s. After a slowdown, it was resurrected as 
shaping underwear or lingerie, and in the 2010s it reappeared as a blouse 
bodysuit and classic turtleneck bodysuit, as well as a part of evening wear.
"""

    info_jumpsuit = """
A jumpsuit, also know as "boiler suits", is a slim-fitting, one-piece garment 
that covers the arms and legs. It was originally created in 1919 as a functional 
garment for parachuters to, yes, jump from planes in. In the 1930s, fashion 
designer Elsa Schiaparelli began creating jumpsuits for elegant women.

The late 1960s and 1970s were prime years for the jumpsuit. There were 
sportswear styles for day, and leather one-pieces or embellished designs for 
evening. By 1980, the jumpsuit had become so popular that the American designer 
Geoffrey Beene declared it “the ballgown of the next century”. With everything 
going big in the '80s it was no surprise that the jumpsuit would also do the 
same. During these years the jumpsuit got supersized with shoulder pads, 
tapered trousers and bat-wing sleeves.

But the style may have reached saturation as it fell out of favor until the 
early 2000s. And thus, the style was relaunched. Easy to wear, versatile and a 
little bit feisty, the jumpsuit has become a modern wardrobe staple.
"""

    info_overalls = """
Overalls, also called bib-and-brace overalls, or dungarees are a type of garment 
usually used as protective clothing when working. The garments are commonly 
referred to as a "pair of overalls" by analogy with "pair of trousers".

Overalls were originally made of denim, but they can also be made of corduroy or 
chino cloth. Overalls were invented in the 1890s by Levi Strauss and Jacob W. 
Davis at Levi Strauss & Co., but they went through an evolution to reach their 
modern form. Initially only used for protective clothing in work settings, 
they have become a garment of high fashion as "potential cult items". 
Overalls were not reserved solely for the working man. Women could be seen 
in bib overalls too by the 1900s. 

Bib overalls (in different colors and textiles) have become a popular garment 
among American youth, from the 1960s onward. The overalls especially became a 
signature style of the 90s. In the 21st century, overalls have evolved into a 
high fashion garment and part of every women’s closet.
"""

    info_romper = """
A romper suit, or just romper, is a one-piece or two-piece combination of shorts 
and a shirt. It is also known as a playsuit, its generally short sleeves and 
pant-legs contrasting with the typical long ones of the jumpsuit.

Rompers appeared in the United States of America in the early 1900s.[1] 
They were popular as playwear for younger children because people thought they 
were ideal for movement. “After World War II, in terms of culture, you start to 
see a great move of people into the suburbs and housing developments,” she said. 
“At that time, there were outfits called playsuits that women wore.” The 
playsuits were casual one-piece outfits that women wore when entertaining close 
friends at their homes. Today, we refer to those same pieces as rompers.

While rompers had been popular among women in the 1950s, they re-emerged in the 
1970s as a fashion for adult women. In the 1970s rompers were usually a casual 
garment made of terrycloth, and often in a tube top style. They were common in 
the 1980s in a wider variety of materials such as silky fabrics for evening 
wear. Since 2006, rompers have enjoyed a minor renaissance as a fashionable 
garment for women. These days, the romper is back in a big way. It’s likely 
women will have one in their closet right now.
"""

    info_jeans = """
Jeans are a type of pants or trousers, typically made from denim or dungaree 
cloth. Often the term "jeans" refers to a particular style of trousers, called 
"blue jeans", which were invented by Jacob W. Davis in partnership with Levi 
Strauss & Co. in 1871 and patented by Jacob W. Davis and Levi Strauss on 
May 20, 1873. 

Jeans marked culture of the last 140 years probably more than we think. 
They were first working clothes, then symbols of disobedience only to become 
fashion items. Jeans are undeniably a fashion staple, but that wasn’t always the 
case. In fact, jeans are one fashion item that has definitely had its ups and 
downs and evolved significantly throughout time. 

In the 1920s and 1930s, jeans became popular Western wear in the United States, 
worn by miners, cowboys and other male workers who needed sturdy clothing that 
could withstand heavy wear and tear. Women only started wearing in the sixties. 
The 1980s is the decade when designer denim was truly born. Denim fashion 
changed again in the 1990s, as the grunge era in fashion began. In this decade, 
jeans became more about slouchy, casual style, than something you would wear to 
dress up in. 

Denim became a fashion staple once again, becoming an appropriate item of 
clothing to wear for going out on a Saturday night, or even to the office. 
Flare and boot cut denim were among the most popular cuts of the early 2000s 
and came in a variety of washes. 

But the biggest denim style story of the decade began in the mid-to-late 2000s, 
with the resurgence of the skinny jean, as a result of innovations in denim 
stretch technology. Today, the trend in denim fashion is toward variety, 
although skinnier styles for women remain the most popular by a margin, and are 
a fashion mainstay for most women, because of their versatility as a casual or 
dressier pant.
"""

    info_leggings = """
The first iteration of legging came about in 14th century Scotland. 
That’s right, the same men that are secure enough in their masculinity to don 
kilts are also credited with the invention of leggings. They were originally 
created for men and came in two pieces, one for each leg of course. This version 
covered the entire leg, with each piece securing at the waist in a way that 
resembled chaps. These leggings were worn for both casual and military dress. 
For the next few centuries, leggings were frequently worn all over Europe, 
albeit still only by men. 

Finally, by the 19th century after leggings had become globally widespread, 
women began to adopt these early two-piece leggings as well. Leggings remained 
in the realm of protective or underclothing for another century or so. “Fashion” 
leggings as we recognize them today originated in the 1960’s. These modern 
versions were tighter and moved away from a unisex garment into more feminine 
territory. They were worn both in high fashion and sportswear. 

When flared pants began trending in the 70’s, people wore leggings a little bit 
less, but were still around, nonetheless. The 80’s were a significant chapter in 
legging history. 80’s culture was characterized by its fitness craze, which 
spilled over into fashion. It became perfectly acceptable to incorporate workout 
wear into one’s daily wardrobe. Soon leggings, once mainly relegated to aerobics 
class, were everywhere. The only style rule of the 80’s: leggings go with 
anything. In the early 90’s, leggings were less ubiquitous, but women 
occasionally wore colorful versions with dresses and tops. They fell out of 
fashion as flare and boot cut pants gained popularity. But by 2005, they came 
back with a vengeance. Toward the end of the decade, full-length liquid leggings 
replaced pants for the most part.
"""

    info_palazzo_pants = """
Palazzo pants are flared and loose, long-legged pants that widen out from the 
waist to all the way down. 

Originally seen worn by fearless women like Coco Chanel in the roaring 20s, and 
later by avant garde actress Katharine Hepburn in the 30s, palazzo pants first 
became popular during the 1960s. Some upscale restaurants resisted modern 
fashion trends by refusing to admit women wearing trousers, which were 
considered inappropriate by some proprietors. This posed a problem for women 
who did not want to wear the skirt styles that were then in fashion. Some women 
opted to circumvent restaurant bans on women in pants by wearing the palazzo 
trouser. By the late 1960’s the counter culture movement adopted the looser more 
comfortable flared pant going so far as to buy naval uniforms from surplus 
stores to embellish with stitching and patches.

When the 80s came, the wide leg flared pants or palazzo pants went out fashion 
once again. Today, the palazzo pants have made a complete comeback and they are 
once again a hot item in department stores and fashion boutiques.
"""

    info_capris = """
Capri pants are pants that are longer than shorts but are not as long as 
trousers. They typically come down to between the knee and the calf or ankle.

Capri pants were introduced by fashion designer Sonja de Lennart in 1948, and 
were popularized by her and English couturier Bunny Roger. Their popularity 
exploded in the late ‘50s and early ‘60s when they were worn by stars Mary Tyler 
Moore (who often wore them on “The Dick Van Dyke Show”), Audrey Hepburn and 
Grace Kelly. After a drop in popularity during the 1970s through the 1990s, 
capris returned to favor in the mid 2000s.
"""

    info_cargo_pants = """
Cargo pants were first worn in 1938 by British military personnel. 
These cargo pants were part of their Battle Dress Uniforms (BDUs). 
The original cargo pants style featured one pocket on the side thigh and one on 
the front hip. Cargo pants were first worn in the United States on military 
uniforms in the 1940s. 

Cargo pants surged onto the fashion scene in the mid-to-late 1990s. 
Following a “trickle up” theory of how fashions spread, cargo pants first were 
worn as fashion by urban hip-hop performers in the 1990s. This trend flowed up 
to the mass market; cargo pants were ubiquitous at almost any men's or women's 
clothing retailer at this time. Although the cargo pockets on most items were 
functional, they often were unused and just worn as decorative details.
"""

    info_sweatpants = """
Sweatpants(or joggers) are a casual variety of soft trousers intended for 
comfort or athletic purposes, although they are now worn in many different 
situations. 

The first pair of sweatpants was introduced in the 1920s by Émile Camuset, 
the founder of Le Coq Sportif. These were simple knitted gray jersey pants that 
allowed athletes to stretch and run comfortably. The simple gray sweatpants — 
named for their ability to absorb sweat— were a utilitarian but highly effective 
answer to the tight-fitting trousers that had dominated men’s fashion since the 
French Revolution.

It remained this way until the 1980s. The growth in gym use and the new waves of 
health and fitness in the 1980s certainly saw the move of sweatpants from the 
sports-specific context to a more general leisurewear one. Nowadays, women are 
seen casually sporting these pants.  
"""

    info_shorts = """
Shorts are a garment worn over the pelvic area, circling the waist and splitting 
to cover the upper part of the legs, sometimes extending down to the knees but 
not covering the entire length of the leg. They are called "shorts" because they 
are a shortened version of trousers, which cover the entire leg, but not the 
foot. Shorts are typically worn in warm weather or in an environment where 
comfort and air flow are more important than the protection of the legs. 

In much of Europe and the Americas during the 19th and early 20th centuries, 
shorts were worn as outerwear only by young boys until they reached a certain 
height or maturity. The 1950s decade was the first that embraced women wearing 
shorts for more than just beach wear or for pinup girls. Women’s 1950s shorts 
came in several lengths and styles to fit a variety of leisure activities women 
enjoyed. Today shorts have become a staple for all women and multiple pairs came 
be found in their closets. They are of many different lengths and made of many 
different fabrics. 
"""

    info_miniskirt = """
A miniskirt is a skirt with its hemline well above the knees, generally at 
mid-thigh level, normally no longer than 10 cm (4 in) below the buttocks. 
Short skirts have existed for a long time, though they were generally not called 
"mini" or recognized as a fashion trend until the 1960s. 

One of the earliest known cultures where women regularly wore clothing 
resembling miniskirts was a subgroup of the Miao people of China, the Duan Qun 
Miao. Extremely short skirts became a staple of 20th-century science fiction, 
particularly in 1940s pulp artwork such as that by Earle K. Bergey who depicted 
futuristic women in a "stereotyped combination" of metallic miniskirt, bra and 
boots.

British designer Mary Quant is credited for inventing the modern miniskirt in 
1964. Her revolutionary garment became an instant hit among young women. This is 
because it paved the way for them to express their sexual freedom as well as 
their taste in fashion. From 1969 onwards, the fashion industry largely returned 
to longer skirts such as the midi and the maxi. In spring of 1982 short skirts 
began to re-emerge. Many women began to incorporate the miniskirt into their 
business attire, a trend which grew during the remainder of the century. 
Miniskirts have now become a common sight.
"""

    info_pencil_skirt = """
A pencil skirt is a slim-fitting skirt with a straight, narrow cut. 
Generally, the hem falls to, or is just below, the knee and is tailored for a 
close fit. It is named for its shape: long and slim like a pencil.

The first pencil skirt was designed by Christian Dior as part of his “H-Line” 
collection of 1954. Since the Mid 50’s, the pencil skirt has become a staple of 
working wardrobes, with the hemline raising and lowering depending on the 
prevailing trends of the day. Following the 1960s the pencil skirt began to be 
seen as a more dated look, as the mini skirt was coming into style, but the 
pencil skirt always remained on the shelves. In the 1980s, women wore them as 
part of their power suits teamed up with pussy bow blouses and large shoulder 
pads. The pencil skirt is seen today as one of the "working women's staples". 
It's seen as super glamorous with celebrities such as Kim Kardashian and 
Christina Hendricks even wearing them on the red carpet. Believing it to be the 
most flattering shape for women of all sizes, stylists across the globe dress 
their ladies in this figure-hugging skirt.
"""

    info_maxi_skirt = """
A maxi skirt is an ankle length skirt. In the 1960′s high end fashion designer, 
Oscar de la Renta set out to design something that would be gracing the ankles 
of fashionable people all over the world. Designers such as YSL and Dior led by 
example, making the maxi dress some what of an epidemic in fashion during the 
70′s. By the 80′s the Maxi Dress reign was over, being taken over by shoulder 
pads and playsuits. Come the 90′s, grunge and mini skirts left no room for the 
casual elegance of the maxi.

In recent years the maxi dress has made it’s come back. From 2010 onwards modern 
maxi dresses have become more popular, with the hem line dropping to the ground 
they were creeping into stores everywhere.
"""

    info_maxi_dress = """
Maxi dresses (c.1970) - maxi is a term used since the late 1960s[64] for 
ankle-length, typically informal dresses. Until the late 60's, mini and 
"midi" skirts were all the craze. Longer skirts and dresses had fallen out of 
style in the 60's as women sought to step away from the safer, more traditional 
styles of the 50's, but the maxi dress brought the long dress back in a totally 
unique way. The maxi dress became the quintessential clothing for the moment, 
as boho trends started to merge into the mainstream and blended perfectly with 
the maxi's style.

Maxi dresses fell out of style in the late 1970's, perhaps due to their roots 
in the Bohemian trend and their connection to nonconforming subcultures of the 
era. After disappearing in the 1980's and most of the 90's, the maxi dress 
finally reappeared in the late 90's, mostly in the form of the maxi skirt. 
It was still having trouble shedding its debilitating boho connection, but 
fashion designers started to take an interest in the dress once again, moving 
it beyond boho and giving it the freedom to blend with other styles, making it a 
staple in every woman's wardrobe.
"""

    info_wrap_dress = """
A wrap dress is a dress with a front closure formed by wrapping one side across 
the other, and knotting the attached ties that wrap around the back at the waist 
or fastening buttons. This forms a V-shaped neckline and hugs the wearer's 
curves. A faux wrap dress resembles this design, except that it comes already 
fastened together with no opening in front, but instead is slipped on over the 
head.

While the wrap dress is of course synonymous with Diane Von Furstenberg and the 
1970’s, this particular silhouette was around for several decades prior, and 
continues to be a staple in women’s closets even today. The wrap dress’ true 
origin began about four decades prior to its spike in popularity- back to the 
1930’s. During this time, designer Charles James was taking the fashion world by 
storm with his garments. The designer created the very first iteration of the 
wrap dress- a clinging sheath that “spiraled” around the body, clasping at the 
hip or zipping across the torso. 

Fast-forward 30 years to the early 1970’s. Diane Von Furstenberg was in her 20’s 
and had just arrived to the United States. The simple wrap dresses were 
originally just an experiment- a little something she would try to sell in 
America. While Von Furstenberg did not necessarily invent the silhouette, she 
certainly perfected it. Her version was a collared, long sleeved shirt-dress 
that wrapped around the torso in a way that it easily accentuated curves while 
hiding any undesirable bulge. 

Other designers have noted just how flattering the wrap dress is, and have 
created their own versions- you can find the silhouette on every runway from 
J.Crew to Alexander McQueen. The wrap has become a definitive fashion staple, 
and will likely continue to grace the runways for a long time to come.
"""

    info_bandage_dress = """
Bandage dress or the bodycon dress are figure hugging sexy dress which usually 
is below or up to the knee. It is known to fit like second skin.

Herve Leger was credited with the invention of bandage dresses, or the “bender” 
as it was called then in his 1989 runway show. He acknowledged his inspiration 
to be the bathing suits of the yester years and his work with the seam bindings. 
In the 21st century, bandage dresses have assumed an aura of versatility and can 
be anything and everything you want. From fierce and confident outfits in bold 
colors to the nude shades, which highlight your svelte figure, you can be sweet 
or sexy in a single trip to the dressing room. More than one such dress can 
usually be found in a women’s closet.
"""

    info_shirt_dress = """
A shirtdress is a style of women's dress that borrows details from a man's 
shirt. These can include a collar, a button front, or cuffed sleeves. 
Often, these dresses are made up in crisp fabrics including cotton or silk, 
much like a men's dress shirt would be. As they are typically cut without a 
seam at the waist, these dresses often have a looser fit, usually relying on a 
belt to define the waist. Button fronts and a forgiving fit make this a 
flattering look for most body types.

The 1950s version of the shirtdress was launched as part of Christian Dior's 
post–World War II "New Look" couture designs, with a full skirt held up by 
wearing a crinoline.[1] They often featured a notched collar, and elbow-length 
sleeves with cuffs. It was initially called the shirtwaist, and it began with a 
skirt that was made fuller and flashier with a crinoline, and was later 
discarded as women began prioritizing their comfort.

A variation of the original shirtdress is the "T-shirt dress". T-shirt dresses 
began being produced in the 1960s and are simply an elongated version of a 
T-shirt. Now, many women around the world still use that dress, probably without 
thinking about its origins and, surely, without caring about any kind of 
feminine perfection other than looking awesome.
"""

    info_sundress = """
A sundress is an informal or casual dress intended to be worn in warm weather, 
typically in a lightweight fabric, most commonly cotton, and usually 
loose-fitting. It is commonly a bodice style, sleeveless dress, typically with 
a wide neckline and thin shoulder straps, and may be backless. A sundress is 
typically worn without a layering top and is not typically worn over a blouse, 
sweater or t-shirt, nor with leggings.

While the word "sundress" was first used in the early 1940s, they really came 
into vogue in the 1950s, and were especially popularized by Lilly Pulitzer in 
the 1960s. 

The sundress provides a feminine look that is more comfortable than a skirt and 
blouse or another sort of dress. Most women today can be wearing summer dresses 
all around the world.
"""

    info_lbd = """
A little black dress (LBD) is a black evening or cocktail dress, cut simply and 
often quite short.

In 1926 Gabrielle "Coco" Chanel published a picture of a short, simple black 
dress in American Vogue. It was calf-length, straight and decorated only by a 
few diagonal lines. Vogue called it "Chanel's Ford". The little black dress was 
simple and accessible for women of all social classes. Vogue also said that the 
LBD would become "a sort of uniform for all women of taste". This, as well as 
other designs by the house of Chanel helped disassociate black from mourning, 
and reinvent it as the uniform of the high-class, wealthy, and chic. 

The little black dress continued to be popular through the Great Depression, 
predominantly through its economy and elegance. The rise of Dior's "New Look" in 
the post-war era and the sexual conservatism of the 1950s returned the little 
black dress to its roots as a uniform and a symbol of the dangerous woman. The 
popularity of casual fabrics, especially knits, for dress and business wear 
during the 1980s brought the little black dress back into vogue. The grunge 
culture of the 1990s saw the combination of the little black dress with both 
sandals and combat boots, though the dress itself remained simple in cut and 
fabric. The resurgence of body conscious clothing, muted colour schemes, and the 
reemergence of predominant black, along with the retrospective trends of the 
1980s in the late 2000s paved way to the return of interest to the dress.

The "little black dress" is considered essential to a complete wardrobe by many 
women and fashion observers, who believe it a "rule of fashion" that every woman 
should own a simple, elegant black dress that can be dressed up or down 
depending on the occasion.
"""

    info_tshirt = """
A T-shirt is a style of fabric shirt named after the T shape of its body and 
sleeves. Traditionally it has short sleeves and a round neckline, known as a 
crew neck, which lacks a collar. T-shirts are generally made of a stretchy, 
light and inexpensive fabric and are easy to clean.

The origins of the t-shirt date back to the late 19th century, First, the 
one-piece union suit underwear was cut into separate top and bottom garments, 
with the top long enough to tuck under the waistband of the bottoms to keep cool 
in warmer months during the year. The first manufactured t-shirt was invented 
between the Mexican-American War in 1898, and 1913 when the U.S. Navy began 
issuing them as standard undershirts. These were a crew-necked, short-sleeved, 
white cotton undershirt to be worn under a uniform.

Though the t-shirt was created in the early 20th century, it was rare to see it 
worn as anything other than an undershirt. It wasn’t uncommon to see veterans 
wearing a t-shirt tucked into their trousers post-World War II, but outside of 
that, t-shirts were almost exclusively used underneath “proper” clothes. By the 
Great Depression, the T-shirt was often the default garment to be worn when 
doing farm or ranch chores, as well as other times when modesty called for a 
torso covering but conditions called for lightweight fabrics.

Though graphic t-shirts and t-shirt printing began in the 1950s and 1960s, it 
wasn’t until the ’70s that t-shirts became the powerful messaging platform that 
we know them as today. All of this to say, the t-shirt has become not only an 
American staple, but an essential garment worn around the world, and their 
unique ability to convey a message hasn’t gone anywhere.
"""

    info_hoodie = """
A hoodie (also spelt hoody, and alternatively known as a hooded sweatshirt) is a 
sweatshirt with a hood. Hoodies often include a muff sewn onto the lower front, 
and (usually) a drawstring to adjust the hood opening.

The hooded sweatshirt is a utilitarian garment that originated in the 1930s in 
the US for workers in cold New York warehouses.[6] The modern clothing style was 
first produced by Champion in the 1930s and marketed to laborers working in 
freezing temperatures in upstate New York.[7] The term hoodie entered popular 
usage in the 1990s.

The hoodie took off in the 1970s, with several factors contributing to its 
success. Hip hop culture developed in New York City around this time and high 
fashion also contributed during this era. In the 1980s, hip-hop artists were 
moving more into mainstream music — and hoodies came with them. By the 1990s, 
the hoodie had become a staple in wardrobes around the world, spanning college 
campuses and counter-cultural movements.

Today, hoodies bridge hip-hop and high fashion. They are an effortless way to 
look cool and casual while staying comfortable. They are an every day 
wash-and-wear staple for both men and women alike. 
"""

    # dictionary to get history of a clothing item 
    # with apparel as the key and its histroy as the value
    apparel_dict = {
        "t-shirt" : info_tshirt,
        "croptop" : info_crop_top,
        "bikini" : info_bikini,
        "bodysuit" : info_bodysuit,
        "jumpsuit" : info_jumpsuit,
        "overalls" : info_overalls,
        "romper" : info_romper,
        "jeans" : info_jeans,
        "leggings" : info_leggings,
        "palazzopants" : info_palazzo_pants,
        "capris" : info_capris,
        "cargopants" : info_cargo_pants,
        "sweatpants" : info_sweatpants,
        "shorts" : info_shorts,
        "miniskirt" : info_miniskirt,
        "pencilskirt" : info_pencil_skirt,
        "maxiskirt" : info_maxi_skirt,
        "maxidress" : info_maxi_dress,
        "wrapdress" : info_wrap_dress,
        "bandagedress" : info_bandage_dress,
        "shirtdress" : info_shirt_dress,
        "sundress" : info_sundress,
        "lbd" : info_lbd,
        "hoodie" : info_hoodie
        }

    info_return = """
No article of clothing with that name was found! 
Please check your spelling and try again.
"""

    # if elif branch to get the fashion hisotry of a particular apparel
    if get_info_apparel == "t-shirt" :
        info_return = apparel_dict["t-shirt"] 

    elif get_info_apparel == "croptop" :
        info_return = apparel_dict["croptop"]

    elif get_info_apparel == "bikini" :
        info_return = apparel_dict["bikini"]

    elif get_info_apparel == "bodysuit" :
        info_return = apparel_dict["bodysuit"]

    elif get_info_apparel == "jumpsuit" :
        info_return = apparel_dict["jumpsuit"]

    elif get_info_apparel == "overalls" :
        info_return = apparel_dict["overalls"]

    elif get_info_apparel == "romper" :
        info_return = apparel_dict["romper"]

    elif get_info_apparel == "jeans" :
        info_return = apparel_dict["jeans"]

    elif get_info_apparel == "leggings" :
        info_return = apparel_dict["leggings"]

    elif get_info_apparel == "palazzopants" :
        info_return = apparel_dict["palazzopants"]

    elif get_info_apparel == "capris" :
        info_return = apparel_dict["capris"]

    elif get_info_apparel == "cargopants" :
        info_return = apparel_dict["cargopants"]

    elif get_info_apparel == "sweatpants" or get_info_apparel == "joggers" :
        info_return = apparel_dict["sweatpants"]

    elif get_info_apparel == "shorts" :
        info_return = apparel_dict["shorts"]

    elif get_info_apparel == "miniskirt" :
        info_return = apparel_dict["miniskirt"]

    elif get_info_apparel == "pencilskirt" :
        info_return = apparel_dict["pencilskirt"]

    elif get_info_apparel == "maxiskirt" :
        info_return = apparel_dict["maxiskirt"]

    elif get_info_apparel == "maxidress" :
        info_return = apparel_dict["maxidress"]

    elif get_info_apparel == "wrapdress" :
        info_return = apparel_dict["wrapdress"]

    elif get_info_apparel == "bandagedress" or get_info_apparel == "bodycondress" :
        info_return = apparel_dict["bandagedress"]

    elif get_info_apparel == "shirtdress" or get_info_apparel == "t-shirtdress" :
        info_return = apparel_dict["shirtdress"]

    elif get_info_apparel == "sundress" :
        info_return = apparel_dict["sundress"]

    elif get_info_apparel == "lbd" or get_info_apparel == "littleblackdress" :
        info_return = apparel_dict["lbd"]

    elif get_info_apparel == "hoodie" :
        info_return = apparel_dict["hoodie"]

    return info_return

