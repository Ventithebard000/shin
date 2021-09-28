






init:
    python:
        def max_points(*values):
            return [ i for i, v in enumerate(values) if v == max(values) ]



define s = Character(" ")
define p = Character("[povname]")
define a = Character(" ", what_color="ffffff")
define m = Character(" ", what_color="f60609")



label start:





    $ points = 50
    $ name_list = ["sou", "hiyori", "sou hiyori", "hiyori sou", "SOU", "HIORI", "HIYORI SOU", "SOU HIYORI"]





    play music tansaku3 fadein 2
    scene bg black
    pause(2.0)



    a "> While the rest of the group is exploring the floor, you decide to risk it and stay behind."

    a "> You've noticed this room in the corner of the corridor a while ago, and yet others prefered to ignore it for some reason."

    a "> Maybe it's not a bad idea to go inside and search through it while others are gone."

    a "> You slow down your steps and then turn back completely."

    a "> Fortunately, the door isn't locked."

    scene bg monitor room
    with dissolve

    a "> . . . ."

    a "> At first, you don't see anything of interest. Or dangerous, at least."

    a "> The room has a bunch of screens and keyboards, and lots of other technical equipment."

    a "> Seems like it's a Floormaster's room."

    a "> Maybe you could just hack the system... But that's a bold claim. "

    a "> It's probably going to take more than just a password."

    a "> You decide to search the room thoroughly before the others found you. You don't have that much time."

    scene bg monitor room 1
    with hpunch

    play sound computer

    a "> . . . ?"

    a "> Hm?"

    stop music fadeout 2

    a "> The screen is.. on?"

    a "Look at it?"

    menu:
        "> Yes":


            a "> You approach the screen carefully."

            "'Ah, no, you're not... Who are you? You shouldn't be here...'"

            a "> It's seems that the voice is coming from the working screen."

            scene mon red
            with dissolve

            a "> When you lean towards the screen, you don't expect to see a face."

            play sound computer
            scene mon shin
            with hpunch
            pause (1.0)



            "'P-please, leave this room... You'll be in trouble! If you leave right now I won't tell anybody, I promise.'"
        "> No":

            a "> You decide to mind your business. It could be a trap."

            a "> When you're done exploring the room without touching anything, you get ready to leave."

            a "> But then... you hear a voice."

            scene mon red
            with dissolve
            pause (0.5)

            play sound computer
            scene mon shin
            with hpunch
            pause (1.0)



            "'Um... Hiyori-kun, is that you?'"

    menu:
        "> Is this a trap?":
            a "> You pull a chair closer to the working monitor to take a seat."

            a "> You've already seen the AIs before, and it probably wouldn't hurt you in any way. At least, too hard."

            "'I... I don't understand what you're talking about...'"

            "'This room could be dangerous, b-but that's not because of me...'"

            "'I mean, I would gladly help if anything happened... I can do that!'"

            "'Ah! I mean! It's not like something is going to happen..!'"

            jump who
        "> Who are you?":

            jump who


    label who:

    scene bg neutral
    with dissolve

    show neutral1
    with dissolve

    stop music fadeout 1
    play music denpa

    "'I'm.. I'm just a normal person... AI, i mean... Are you a friend of Hiyori's?'"

    "'He told me that someone might come but... I didn't think it would be just one person.'"

    hide neutral1
    show sad2

    "'Maybe.. something happened...'"

    "'If you're not the only one, you should go back to the others... Being alone here is very dangerous...'"

    menu:
        "> That's very nice of you":
            $ points += 1
            show bg love with dissolve

            hide sad2
            show shock1
            "'Nice? W-why... You don't have to...'"

            "'I just... I just want to help... I am against violence.'"

            "'I really can't tell you much, but I won't hurt you...'"
        "> Was someone here before me?":




            $ points += 0

            show bg neutral with dissolve

            hide sad2
            show neutral1

            "'No, not at all...'"

            "'Nobody was there... before you...'"

            "'Honestly, I've been alone for so long that I...'"

            "'I shouldn't talk to you, but... I'm so sorry, it's just... so quiet here...'"
        "> If it's a trap, it's a stupid one":



            $ points -= 1

            show bg bad with dissolve

            show nerv1

            "'What? I-I mean, you and me are on equal terms here, I'm...'"

            "'I'm just... I'm just trying to help... I am against violence.'"

            hide nerv1
            show sad2

            "'I really can't tell you much, but I won't hurt you...'"


    show bg neutral with dissolve

    show neutral2

    "'Oh! I forgot to introduce myself!..'"

    hide neutral2
    show happ1

    "'My name is Shin...'"

    hide happ1
    show happ3

    "'I'm sorry if it's asking too much but... Can you tell your name too?'"

    hide happ3
    show neutral1

    "'You can keep it a secret if you want... I don't mind.'"

    label name:

    menu:
        "> My name is...":
            $ points += 1
            $ nameset = True

            python:
                povname = renpy.input("What is your name?", length=32)
                povname = povname.strip()


            if povname in ["sou", "hiyori", "sou hiyori", "hiyori sou", "SOU", "HIORI", "HIYORI SOU", "SOU HIYORI", "Sou", "Hiyori", "Sou Hiyori", "Hiyori Sou", "Hiyori-kun", "Hiyori-san"]:


                play sound accent401
                stop music
                show bg bad

                show scared1

                "'. . . .'"

                hide scared1
                show scared2

                "'W-....'"

                "'Ah...'"

                "'I just... I didn't-'"

                hide scared2
                show scared1

                "'I'm sorry, for a second I just...'"

                hide scared1
                show nerv1

                play music denpa fadein 1

                "'Are you sure this is your name?'"

                menu:
                    "> Yes":

                        hide nerv1
                        show scared2

                        "'...I see.'"

                        "'It's just a bit surprising is all...'"

                        hide scared2
                        show nerv1

                        "'But if it's your name, then of course...'"

                        "'Sorry I've made such a fuss...'"

                        hide nerv1
                        show happ4

                        "'It's great to get to know you, [povname]!'"

                        show bg neutral with dissolve
                        hide happ4
                        show neutral2

                        "'You know, it kind of reminded me the first time I've heard this name...'"

                        "'I had another uh... another friend at school back then.'"

                        hide neutral2
                        show nerv1

                        "'Unfortunately, our friendship didn't last, and...'"

                        hide nerv1
                        show neutral1

                        "'Ah! I'm sorry, you're probably not interested in that.'"

                        "'Can I help you in any way?'"

                        jump talk
                    "> No, I'm just joking around":


                        hide nerv1
                        show shock1

                        "'Ah!'"

                        hide shock1
                        show nerv1

                        "'T-that wasn't a nice one!...'"

                        "'But you've totally got me, haha...'"

                        "'Sorry I've made such a fuss...'"

                        show bg neutral with dissolve
                        hide nerv1
                        show happ3

                        "'Do you mind telling me your actual name then?'"

                        "'Sorry If I'm insisting too much...'"

                        hide happ3
                        show nerv1

                        "'It's totally understandable if you don't want to share information about yourself.'"



                        jump name

            elif povname in ["владыка", "Владыка"]:

                hide neutral1
                show shock1

                "'. . . .'"

                "'Точно?'"

                hide shock1
                show neutral2

                "'..Как скажешь...'"

                hide neutral2
                show nerv1

                "'Но только не при всех, л-ладно?'"

                "'. . . .'"

                hide nerv1
                show scared1

                "'Господи, за что мне это...'"

                "'. . . .'"

                hide scared1
                show nerv1

                "'Рад познакомиться, эээ... [povname].'"

                "'Сделаем вид, что этого не было.'"



                jump talk

            elif povname in ["мочезавры", "мочезавр", "Мочезавры", "Мочезавр", "Уринозавр", "уринозавр", "Уринозавры", "уринозавры"]:

                hide neutral1
                show shock1

                "'. . . .'"

                "'. . . .'"

                hide shock1
                show nerv1

                "'Здорово.'"

                "'Хочешь проверить мою способность логически мылить?'"

                "'Или можно сразу начинать звонить в органы пепеги?'"

                "'Рад познакомиться, эээ... [povname].'"

                "'Сделаем вид, что этого не было.'"



                jump talk
            else:



                show bg love with dissolve

                hide neutral1
                show happ2

                "'Thank you!!'"

                "'[povname]!... Nice to meet you!'"

                jump fren

            label fren:


                show bg neutral with dissolve

                hide happ2
                show neutral2

                "'You know, I once had a friend with the same name...'"

                "'Unfortunately, our friendship didn't last, and...'"

                hide neutral2
                show nerv1

                "'Ah! I'm sorry, you're probably not interested in that.'"

                hide nerv1
                show neutral1

                "'Can I help you in any way?'"

                jump talk
        "> I'd rather not. It could be dangerous.":

            $ points -= 1


            show bg bad with dissolve

            hide neutral1
            show sad1

            "'Oh... Okay...'"

            "'You know... I once had a friend who also was very cautious...'"

            hide sad1
            show nerv1

            "'Ah! I'm sorry, you're probably not interested in that.'"

            hide nerv1
            show neutral1

            "'Can I help you in any way?'"


            jump talk


    label talk:

    scene
    show bg neutral

    show neutral1

    menu:
        "> And what happened to your friend?":
            $ points += 1


            show bg love with dissolve

            hide neutral1
            show neutral2

            "'Y-you're interested in that?..'"

            "'I don't know if I can talk about this...'"

            hide neutral2
            show happ4

            "'B-but I think I can trust you!.. Let me see...'"

            show bg neutral with dissolve
            hide happ4
            show neutral1



            "'I had a few friends in school to be honest... Things... never worked out.'"


            "'Sometimes we would eat lunch on the roof... Complaining about our teachers.'"

            hide neutral1
            show sad2

            "'They were a nice person. But they probably wouldn't call me their friend...'"

            hide sad2
            show sad3

            "'And when I met Hiyori, they... just disappeared.'"


            "'First they stopped talking to me, and then they transferred to another school.'"

            hide sad3
            show sad4

            "'They never answered my messages too...'"

            "'And I was thinking I'd be able to consider them a friend.'"

            "'But the feeling wasn't mutual, it seems... As expected...'"

            hide sad4
            show sad5

            "'Maybe I was too boring or... too annoying. Maybe both.'"

            menu:
                "> It's not true. I enjoy talking to you.":
                    $ points += 1

                    scene
                    show bg neutral
                    show sad5
                    show bg love with dissolve

                    hide sad5
                    show shock1

                    "'R-really?'"

                    "'I'm glad to know it!..'"

                    hide shock1
                    show nerv1

                    "'Even if I don't consider it to be true... It's still nice to hear.'"

                    hide nerv1
                    show happ4

                    "'I like talking to you too!'"

                    "'I know, it doesn't sound sincere because I don't have anything else to do but...'"

                    hide happ4
                    show happ1

                    "'I'm not lying. Thank you for listening to me.'"

                    show bg neutral with dissolve



                    jump about
                "> Did 'Hiyori-kun' tell you that?":

                    $ points -= 1

                    scene
                    show bg neutral
                    show sad5
                    show bg bad with dissolve


                    show shock1

                    "'Wh-what are you talking about?..'"

                    hide shock1
                    show sad1

                    "'Hiyori-kun might be a little bit too overprotective, and sometimes he does weird things, but...'"

                    hide sad1
                    show sad2

                    "'I don't think he's tied to that in any way...'"

                    "'Maybe they just... didn't like that I got a new friend.'"

                    hide sad2
                    show sad5

                    "'Yes... It's all my fault...'"

                    show bg neutral with dissolve



                    jump about
        "> Do you know if there are any other hidden rooms?":

            $ points += 0


            show bg neutral with dissolve


            show neutral2

            "'I... I'm not sure...'"

            "'There are some hidden rooms, but you wouldn't be able to access them...'"

            hide neutral2
            show neutral1

            "'You were able to go inside this room only because Hiyori-kun allows it.'"

            "Other rooms are for..."

            hide neutral1
            show sad5

            "'I'm sorry.'"

            "'I can't talk about that.'"

            "'I won't betray him.'"

            show bg neutral with dissolve


            jump about
        "> Do you just want me to ask you about your friend? You're a bad manipulator.":

            $ points -= 1

            scene
            show bg neutral
            show neutral1
            show bg bad with dissolve
            hide neutral1

            show shock1

            "'N-no!..'"

            hide shock1
            show sad5

            "'I... I'm sorry, I didn't mean for it to sound like that... You're right.'"

            "'I didn't mean to vent.'"

            "'You probably have a lot on your mind already...'"

            hide sad5
            show sad4

            "'I'm so sorry. I know I can be annoying at times...'"

            "'Or talk about things that I shouldn't bring up...'"

            "'You're probably not enjoying our conversation from the very start...'"

            hide sad4
            show sad5

            "'I'm very sorry.'"

            menu:
                "> That's not true. I didn't mean to sound rude.":
                    $ points += 0


                    show bg neutral with dissolve
                    hide sad5

                    show sad1

                    "'...Okay.'"

                    hide sad1
                    show sad2

                    "'Just let me know if... If I'm being too annoying, okay?'"

                    "'I don't want to be a burden...'"

                    "'Or to stall you.'"

                    hide sad2
                    show sad3

                    "'I just want what's best for everyone...'"

                    show bg neutral with dissolve


                    jump about
                "> You haven't said anything useful and you don't know when to stop talking.":


                    scene
                    show bg bad
                    show sad5
                    hide sad5
                    stop music



                    show shock1

                    "'. . . !'"

                    "'... I'm s-sorry.'"

                    show bg sad with dissolve
                    hide shock1
                    show sad5


                    "'I'm really sorry that...'"

                    show bg afraid with dissolve

                    hide sad5
                    show cry1

                    play sound kirekake

                    "'I'm sorry. I won't bother you anymore.'"

                    hide cry1
                    show bye1 with hpunch


                    "'I wish you only the best.'"

                    hide bye1

                    scene bg black
                    with hpunch
                    pause (1.0)

                    scene mon red with dissolve

                    a "> The friendly face had been suddenly consumed by the bright light."

                    a "> Before you were able to aknowledge it, the whole monitor is burning red again."

                    a "> Well. That was expected."

                    a "> You get up with a tired sigh."

                    scene bg black with dissolve
                    pause (1.0)

                    a "> And this is when... You understand."

                    scene 1111 with dissolve
                    play music heart_beat01 fadein 1

                    a "> Something's not right."

                    a "> . . ."

                    a "> You feel an unberable tension going through your body and making you completely still."

                    a "> There's someone else... in the room."

                    a "> You can't hear the steps nor the breathing, but you feel it."

                    a "> You feel a heavy gaze on the back of your head."

                    a "> . . . !"

                    play sound earth3

                    scene bg black with hpunch
                    pause (2.0)

                    "END 1"

                    return

    label about:


    scene
    show bg neutral

    show hz1

    menu:
        "> You're speaking a lot about others... Tell me some more about yourself, maybe?":
            $ points += 1

            scene
            show bg neutral
            show hz1
            show bg love with dissolve
            hide hz1

            show neutral1

            "'About others...'"

            "'To be honest, I don't have any other topics to bring up...'"

            "'Even though I never had much acquaintances...'"

            hide neutral1
            show sad2

            "'About myself... Oh, what can I say about myself?'"

            show bg neutral with dissolve

            show neutral2


            "'I'm a pretty boring person... Nothing special at all.'"

            "'I'm just a simple job-hopper.'"

            "'I've worked in the grocery stores for the most of it... Absolutely nothing special.'"

            hide neutral2
            show happ3

            "'What would you like to know? I don't have much useful information for you, to be honest...'"


            menu:
                "> Everything about you is interesting and useful. What do you usually do in here, for example?":
                    $ points += 1

                    scene
                    show bg neutral
                    show happ3
                    show bg love with dissolve
                    hide happ3

                    show shock1

                    "'. . !'"

                    "'O-oh, I...'"

                    hide shock1
                    show nerv1

                    "'I'm not even sure where to start!..'"

                    "'C-cause there's nothing to start with...'"

                    hide nerv1
                    show neutral2

                    "'Usually, I just... Wait for Hiyori-kun to come back...'"

                    "'He's against me talking to others, though...'"

                    hide neutral2
                    show happ1

                    "'But Maple-san is really nice. She always asks if I would like some tea, and... haha...'"

                    hide happ1
                    show nerv1

                    "'I can't drink it, of course. Even though I'd really love to.'"

                    hide nerv1
                    show neutral1

                    "'Other than that... There's nothing else to do...'"

                    "'. . .'"

                    hide neutral1
                    show happ2

                    "'I'm really happy you asked me, though...'"

                    show bg neutral with dissolve
                    hide neutral1
                    show happ2

                    "'Hiyori also asks me a lot about my interests and so on... However, I don't really understand why.'"

                    hide happ2
                    show neutral2

                    "'He knows everything already.'"

                    "'But I can't really say 'no' when he asks me to tell it all over again...'"

                    hide neutral2
                    show sad1

                    "'. . .'"

                    hide sad1
                    show nerv1

                    "'I'm s-sorry!... I'm talking about him again...Behind his back...'"

                    "'That's not very nice of me.'"



                    jump notsorry
                "> I've changed my mind. Let's talk about something else. Tell me more about Hiyori?":


                    label hiyori:

                    $ points -= 1

                    scene
                    show bg neutral
                    show happ3
                    show bg bad with dissolve
                    hide happ3


                    show sad1

                    "'. . .'"

                    hide sad1
                    show sad2

                    "...I see..."

                    "'Hiyori-kun, he's... Very peculiar.'"

                    hide sad2
                    show nerv1

                    "'He's my best friend, and yet... I mean, everyone's got their oddities, right?'"

                    hide nerv1
                    show neutral1

                    "'But, despite that, he's... Very, very smart.'"

                    "'He's got a lot of friends. He's not like me...'"

                    hide neutral1
                    show sad2

                    "'I can only wish of becoming more like him... Just, without the scary parts of it.'"

                    "'No wonder you want to know more about him...'"

                    hide sad2
                    show sad1

                    "'. . .'"

                    hide sad1
                    show nerv1

                    "'J-just... Be more careful, okay?..'"

                    "'Sometimes I... Don't really feel safe around him...'"

                    "'Even though he'd never done anything bad or weird to me...'"

                    show bg neutral with dissolve
                    hide nerv1
                    show neutral1

                    "'As I've mentioned before, he's just very peculiar...'"

                    "'Maybe, it's his... gaze?'"

                    hide neutral1
                    show sad1

                    "'...Oh...'"

                    hide sad1
                    show nerv1

                    "'It's terrible to speak ill of your friends behind their back. I'm extremely sorry.'"



                    jump notsorry
        "> Can you tell me about that 'Hiyori-kun'? I would like to know more, he seems more interesting than you.":



            jump hiyori
    label notsorry:

    scene
    show bg neutral
    show neutral2

    menu:
        "> You're still a bit tense. Can I do something to make you feel better?":
            $ points += 1

            scene
            show bg neutral
            show neutral2
            show bg love with dissolve
            hide neutral2

            show shock1

            "'... T-tense?'"

            hide shock1
            show nerv1

            "'N-not at all, I just... Stutter a lot.'"

            "'I think it has always been that way...'"

            hide nerv1
            show happ1

            "'Trust me, I enjoy your company!'"


            "'I feel at ease while talking to you... I truly do!'"

            hide happ1
            show happ3

            "'. . .'"

            show bg neutral with dissolve
            hide happ3
            show hz1


            "'I know you'll have to leave, sooner or later...'"

            hide hz1
            show sad1

            "'Everyone does...'"

            ". . ."

            hide sad1
            show happ4

            "'But if we ever happen to meet again... I'd be very glad!..'"

            show bg neutral with dissolve

            jump touch
        "> You don't have to apologize so much. I'm not judging you. We're friends after all.":

            $ points += 0

            scene
            show bg neutral
            show neutral2
            show bg bad with dissolve
            stop music
            hide neutral2

            show scared1

            "'. . .'"

            hide scared1
            show scared2

            "'F... Friends?..'"

            "'... Y-yeah, we're probably...'"

            "'I'm... I'm s-...'"

            hide scared2
            show nerv1

            "'Almost said it again... Haha...'"

            "'But... do you really see me as a friend?'"

            show bg neutral with dissolve

            show nerv1
            play music denpa fadein 1

            "'I... Nobody called me that for so long...'"

            hide nerv1
            show sad1

            "'I mean I barely know you!..'"


            "'But still...'"

            hide sad1
            show happ3

            "'I'm glad I've had an apportunity to talk with someone...'"

            hide happ3
            show sad2

            "'Someone else...'"


            jump touch
        "> I don't really understand how the AIs work. You shouldn't be able to be so nervous.":

            $ points -= 1

            scene
            show bg neutral
            show neutral2
            show bg bad with dissolve
            hide neutral2

            show sad1

            "'That's... not true...'"

            "'I can feel things...'"

            hide sad1
            show sad2

            "'I... I can feel fear just like you... And I am as confused as you are...'"

            "'Even if I'm just a code...'"

            hide sad2
            show sad5

            "'I still fear not existing.'"

            "'I'm afraid I'll become useless... Annoying... Worthless...'"

            "'Because then I'll be deleted for sure.'"

            hide sad5
            show sad4

            "'Like an old game you got tired of it.'"

            "'. . .'"

            hide sad4
            show sad5

            "'You could break this screen so easily...'"

            "'. . .'"
            show bg sad with dissolve


            show scared1

            "'. . .'"

            hide scared1
            show scared2

            "'Y-you wouldn't do that, would you?..'"

            menu:
                "> Of course not. I'd take you and your monitor with me if I could.":
                    $ points += 1

                    scene
                    show bg sad
                    show scared2
                    show bg love with dissolve
                    hide scared2


                    show shock1

                    "! . ."

                    hide shock1
                    show nerv1

                    "'Haha... I... I don't think it's that easy...'"

                    "'The monitor is probably heavy too... Haha...'"

                    hide nerv1
                    show sad1

                    "'Besides... I don't think I... can leave at all.'"

                    "'I don't want any trouble...'"
                    show bg neutral with dissolve


                    jump touch
                "> Even if I wanted to, it's too dangerous. Somebody wants you to stay there.":

                    $ points -= 1

                    scene
                    show bg sad
                    show scared2
                    show bg bad with dissolve
                    hide scared2


                    show sad2

                    "'Ah...'"

                    "'That's right...'"

                    hide sad2
                    show sad5

                    "'. . .'"

                    "'I... I promise I don't want to harm you, really...'"

                    "'But... I can see why you can't trust me. I'm sorry.'"
                    show bg neutral with dissolve


                    jump touch
                "> Even if I destroy you, you probably have a back-up file or something. It's pointless.":

                    $ points -= 1

                    scene
                    show bg sad
                    show bg bad with dissolve


                    show scared1

                    "'! . .'"

                    "'It's... It's not like that...'"


                    show sad4

                    "'Right now... I don't have any copies of myself...'"

                    "'If you break this screen, I won't... recover...'"

                    "'. . .'"

                    show bg sad with dissolve


                    show scared1

                    "'Wh-why are you looking at me like that?..'"
                    show bg neutral with dissolve


                    jump touch


    label touch:

    scene
    show bg neutral

    show sad1

    "'You know... I haven't spoke with someone for so long for a while...'"

    hide sad1
    show neutral2

    "'I mean, Hiyori-kun is a great listener, but...'"

    hide neutral2
    show sad2

    "'It's like... He does not participate in talking...'"

    "'But lately he upgraded my monitor to have a touch-screen, and now...'"

    hide sad2
    show nerv1

    "'All he does is poke me in the face...'"

    "'It's... a bit annoying!..'"

    a "> He looks at you as if he's expecting something..."

    a "> ...He's not very good at manipulating."

    a "> You're not sure if AI can feel anything, but you decide to try anyway."

    menu:
        "> Pet his head":

            scene
            show bg neutral
            show bg love with dissolve
            show pat3 with dissolve

            "'! . .'"

            "'. . .'"

            "'. . .'"

            "'He... He's never done that before...'"

            "'It's weird... But it feels nice...'"

            hide pat3
            show happ2 with dissolve

            "'...Thank you...'"

            "'Usually he just pinches my cheeks...'"

            show bg neutral with dissolve


            jump hobby
        "> Boop his nose":


            scene
            show bg neutral
            show bg love with dissolve
            show pat2 with dissolve
            play sound cat_like1a

            "'! . .'"

            "'. . .'"

            "'O-okay...'"

            "'I can't really feel how warm your hands are but...'"

            hide pat2
            show hz1 with dissolve

            "'It feels a little weird...'"

            show bg neutral with dissolve

            jump hobby
        "> Pinch his cheek":


            scene
            show bg neutral
            show bg bad with dissolve


            show pat1 with dissolve
            play sound squeaky_toy

            "'Ow!..'"

            "'. . .'"

            "'...Please, stop..."

            "'. . .'"


            show sad1 with dissolve
            hide pat1

            "'Hiyori-kun also does this to me...'"

            "'It doesn't hurt that much but...'"

            "'It's still unpleasant.'"

            show bg neutral with dissolve

            jump hobby



    label hobby:

    scene
    show bg neutral
    show nerv1

    "'Oh!...'"

    "'I think I am... making everything about myself...'"

    "'It's a bit embarassing, haha...'"

    hide nerv1
    show neutral2

    "'I'm sorry for not asking earlier but...'"

    "'I'll understand if you don't want to share...'"

    "'Can you tell me a bit more about yourself?'"

    hide neutral2
    show neutral1

    "'For example, I... Um...'"

    hide neutral1
    show happ3

    "'I like video games!..'"

    hide happ3
    show happ1

    "'Especially multiplayer games...'"

    "'If it was possible to install some games here...'"

    hide happ1
    show happ4

    "'I'd happily play some with you!..'"

    hide happ4
    show nerv1

    "'If you don't mind, of course!'"

    "'It would be very nice...'"

    hide nerv1
    show neutral1

    "'Do you have any hobbies? What do you like to do in your free time?'"

    python:
        povhobby = renpy.input("What do you like to do in your free time? (do not use CAPS)", length=32)
        povhobby = povhobby.strip()

    if povhobby in ["art", "ART", "Art", "drawing", "Drawing", "DRAWING", "making art", "Making art", "making Art", "Making Art"]:
        scene
        show bg neutral
        show neutral1
        show bg love with dissolve
        hide neutral1

        show happ1

        "'Drawing!...'"

        hide happ1
        show happ4

        "'That's so nice!.. It's wonderful that you have a thing that you enjoy doing...'"

        hide happ4
        show neutral1

        "'To be honest, I've never talked to any artists...'"

        "'So I don't really know much about it and what to say...'"

        "'But one thing for sure...'"

        hide neutral1
        show happ2

        "'Don't forget to take a break from time to time, okay?..'"

        "'Don't overwork yourself and your hand, and leave some time for yourself to relax.'"



        label goodboy:

            scene
            show bg love

            show neutral2

            "'Sometimes the inspiration comes in sudden bursts...'"

            "'But you and your wellbeing should always be your number one priority!...'"

            hide neutral2
            show happ3


            "'It's easier to do your favorite things when you're well rested.'"

            "'And even if you don't like what you can do right now...'"

            hide happ3
            show happ5
            play sound cat_like1a

            "'There are people who love what you do!'"

            "'And who love YOU, too!'"

            hide happ5
            show neutral2

            "'You can say a lot about a person by looking at their work!..'"

            hide neutral2
            show happ3

            "'I might not be very knowlegable, but I wish you only the best in your endevours!..'"

            "'Just remember that your hobby is something you do for yourself, and not for somebody else.'"

            hide happ3
            show happ1

            "'Then it will bring you much more enjoyment.'"

            hide happ1
            show nerv1

            "'I-I'm sorry, I got a bit carried away!.. I'd be happy if you've ever shown your work to me, haha...'"

            hide nerv1
            show happ4

            "'Thank you for sharing with me!'"

            show bg neutral with dissolve


            jump final

    elif povhobby in ["photo", "Photo", "PHOTO", "photography", "Photography", "PHOTOGRAPHY", "taking photos", "Taking photos", "Taking Photos", "photos", "PHOTOS", "Photos"]:

        scene
        show bg neutral
        show neutral1
        show bg bad with dissolve
        hide neutral1



        show scared1

        stop music
        play sound accent401

        "'. . . !'"

        hide scared1
        show scared2

        "'You... like t-taking photos?..'"

        hide scared2
        show nerv1

        "'Haha... It's... a nice hobby!..'"

        "'Yeah...'"

        hide nerv1
        show scared1

        "'. . .'"

        hide scared1
        show nerv1

        "'It's... very creative...'"

        "'. . .'"


        show bg neutral with dissolve
        show sad2
        play music denpa fadein 1

        "'Hiyori-kun... also enjoys photography.'"

        "'I don't really understand it...'"

        hide sad2
        show nerv1

        "'I-I mean!.. The landscape photos he takes are very pretty but...'"

        "'. . .'"

        hide nerv1
        show sad1

        "'I'm sorry for my reaction.'"

        hide sad1
        show neutral1

        "'I don't know what kind of photos you like to take... Portraits, landscapes, but...'"




        jump goodboy

    elif povhobby in ["sport", "Sport", "SPORT", "Sports", "SPORTS", "sports", "playing sports", "Playing sports", "football", "Football", "Basketball", "basketball", "baseball", "Baseball", "soccer", "Soccer", "gymnastics", "Gymnastics", "swimming", "Swimming"]:

        scene
        show bg neutral
        show neutral1
        show bg love with dissolve
        hide neutral1

        show happ1

        "'You like sports? That's so cool!'"

        "'I envy you, haha...'"

        hide happ1
        show happ4

        "'I've been on a weaker side since I remember...'"

        hide happ4
        show nerv1
        play sound powerdown07

        "'I can't imagine being able to train regularly, to be honest...'"

        hide nerv1
        show happ2

        "'But if you really enjoy it, it's very nice!'"

        "'I would gladly watch you practice...'"

        hide happ2
        show happ1

        "'. . .'"

        "'M-maybe you could train me... Haha...'"

        "'It would be fun!..'"

        hide happ1
        show happ3

        "'Right now I'm not bad at swiming!..'"

        "'So, if we ever met again, we could come up with something!'"

        "'I'd be more than happy to train with you!'"

        hide happ3
        show nerv1

        "'I-I realize that it sounds absurd, haha...'"

        hide nerv
        show happ4

        "'Thank you so much for sharing with me!'"

        show bg neutral with dissolve



        jump final

    elif povhobby in ["writing", "Writing", "WRITING", "to write", "write", "Write", "Fic writing", "fic writing", "ficwriting", "Ficwriting", "writing fics", "Writing fics", "poetry", "Poetry", "writing poetry", "Writing poetry"]:

        scene
        show bg neutral
        show neutral1
        show bg love with dissolve
        hide neutral1


        show neutral2

        "'O-oh, you're a writer?'"

        hide neutral2
        show happ1

        "'That's so cool!..'"

        "'You know, you could say I am a writer too, in a sense!'"

        hide happ1
        show happ4

        "'I really like coding...'"

        "'I'm not very good at it yet, but... I'm improving every day!'"

        hide happ4
        show neutral2

        "'Besides, I have an access to any educational info on this computer...'"

        "'You're probably writing something more... poetic?'"

        hide neutral2
        show happ3

        "'It would be nice to read one of your works sometime!..'"



        jump goodboy

    elif povhobby in ["gaming", "Gaming", "games", "Games", "playing games", "Playing games", "video games", "Video games"]:

        scene
        show bg neutral
        show neutral1
        show bg love with dissolve
        hide neutral1


        show shock1

        "'. . !'"

        "'I-I love it too!'"

        hide shock1
        show happ1

        "'Ah, I must've told you about it before already...'"

        "'But I also love gaming!'"

        hide happ1
        show happ3

        "'Sometimes I like to play something hardcore...'"

        "'But to be honest, most of all I enjoy sandbox games.'"

        "'You can just sit and relax after a hard day...'"

        "'Just run around and look at pretty landscapes... Farm games are also very relaxing...'"

        hide happ3
        show happ2

        "'Can you tell me about your favorite games when we meet again?'"

        hide happ2
        show happ1

        "'If we get the opportunity, of course...'"

        "'It would be very nice!'"

        hide happ1
        show happ3

        "'Just don't forget to take breaks while playing... Your eyes can get tired pretty quickly, even if your brain is relaxing.'"

        "'Thank you so much for sharing with me!'"



        jump final

    elif povhobby in ["music", "Music", "playing music", "Playing music", "playing instruments", "Playing instruments", "playing piano", "Playing piano", "playing guitar", "Playing guitar", "piano", "Piano", "Guitar", "guitar"]:

        scene
        show bg neutral
        show neutral1
        show bg love with dissolve
        hide neutral1


        show neutral2

        "'O-oh, you play music?'"

        hide neutral2
        show happ4

        "'That's so cool!..'"

        "'I never understood how to write music...'"

        hide happ4
        show neutral1

        "'I think, Hiyori-kun mentioned that he can play a couple of instruments... He can play piano for sure...'"

        hide neutral1
        show nerv1

        "'Ah!... I'm sorry, didn't mean to talk about him again.'"

        hide nerv1
        show happ1

        "'Anyways... I tried playing piano once, and never touched it again.'"

        "'But I enjoy listening to music!..'"

        "'Being able to create something is so amazing...'"



        jump goodboy

    elif povhobby in ["nothing", "Nothing", "NOTHING"]:

        scene
        show bg neutral
        stop music
        show neutral1
        show bg bad with dissolve
        hide neutral1

        show sad1



        "'. . .'"

        hide sad1
        show sad2

        "'O-okay...'"

        "'I don't mind if you don't want to share...'"

        hide sad2
        show happ3

        "'Just know that whatever it is, I support you and your hobby, and I'm glad you have a thing you enjoy doing!'"

        "'A hobby helps you forget about the world when everything is... too much.'"

        hide happ3
        show nerv1

        "'Sorry, that sounded grim.'"

        hide nerv1
        show sad2

        "'. . .'"

        hide sad2
        show neutral1
        play music denpa fadein 1

        "'But you know... It would be nice if we got an apportunity to talk about it sometime.'"

        "'But I can understand your distrust.'"
        show bg neutral with dissolve

        jump final

    elif povhobby in ["срать", "СРАТЬ", "Срать", "какать", "Какать", "КАКАТЬ", "srat", "SRAT", "Srat", "srat'", "SRAT'", "Srat'"]:

        scene
        show bg neutral
        show neutral1
        show bg black with dissolve
        hide neutral1

        show nerv1

        "'. . .'"

        "'Я же просил, давай без этого...'"

        "'А как же обещание... Сделать вид, что ничего не было...'"

        hide nerv1
        show hz1

        "'Кхм.'"

        hide hz1
        show happ3

        "'Очень классное хобби.'"

        "'Довольно... нестандартное. Для человека.'"

        hide happ3
        show nerv1

        "'Как ты видишь, я... На данный момент просто ПО, поэтому возможность выполнять данную функцию... у меня отсутствует.'"

        "'Но я, эм... Поддерживаю тебя... В твоих начинаниях.'"

        hide nerv1
        show hz1

        "'. . .'"

        hide hz1
        show nerv1

        "'Не обосрись, да не обосран будешь.'"
        show bg neutral with dissolve

        jump final
    else:


        scene
        show bg neutral
        show neutral1
        show bg love with dissolve
        hide neutral1


        show happ2

        "'That's so cool!'"

        "'I'm glad you have something you enjoy doing.'"

        hide happ2
        show happ1

        "'I love seeing how happy people get when they are talking about something they like...'"

        "'Even if I'm not very knowledgeble in this, I hope doing it helps you through the bad times...'"

        "'A hobby helps you forget about the world when everything is... too much.'"

        hide happ1
        show nerv1

        "'Sorry, that sounded grim.'"

        hide nerv1
        show happ2

        "'I'm just glad you have something you enjoy doing.'"

        hide happ2
        show neutral1

        "'But... It would be nice if we got an apportunity to talk more about it sometime.'"

        "'I know, right now is not the best time for that...'"

        hide neutral1
        show happ3

        "'Maybe in future... Haha...'"


        show bg neutral with dissolve

        jump final

    label final:

    scene
    show bg neutral
    show neutral1

    menu:
        "> That's really nice of you. (Pet the monitor)":
            $ points += 1

            scene
            show bg neutral
            show neutral1
            show bg love with dissolve
            hide neutral1
            show pat3 with dissolve
            play sound accent281

            "'! . . .'"

            "'. . .'"

            "'Th-thank you...'"

            hide pat3
            show happ1 with dissolve

            "'I'm glad to hear it!..'"

            "'I-I'm not that nice, but...'"

            hide happ1
            show happ3

            "'I'm just happy to help you...'"

            "'You're a good person. I can see that!'"



            jump finish
        "> Even if you don't know that much about it... Thank you.":

            $ points -= 0

            scene
            show bg neutral
            show neutral1
            show bg neutral with dissolve
            hide neutral1

            show nerv1

            "'Haha, yes... I really don't know much...'"

            "'As I said... I'm an ordinary and boring person, but...'"

            hide nerv1
            show happ3

            "'I'm happy to hear that I could keep you company!..'"

            "'Thank you, too!'"



            jump finish
        "> I don't need your fake support.":

            $ points -= 1

            scene
            show bg neutral
            show neutral1
            show bg bad with dissolve
            hide neutral1

            show shock1

            "'Ah!...'"

            hide shock1
            show sad5

            "'I-I understand your distrust, but...'"

            "'My support... isn't fake...'"

            hide sad5
            show sad4

            "'. . .'"

            "'Sorry if I upset you with my words...'"

            "'I'm not very good at that...'"

            "'I never wanted to make you upset...'"

            jump finish

    label finish:



    if points >= 58:

        show bg love with dissolve
        scene
        show bg love
        show sad1
        play music hakanai fadein 1

        "'I know we don't have much time left but...'"

        hide sad1
        show happ3

        "'I'm glad I got to spend some time with you!'"

        "'It would be nice to meet you again in the future... When things are... normal again.'"

        hide happ3
        show happ1

        "'We could talk more about you, your interests, your hobbies... I would be glad if we...'"

        "'If we...'"

        "'. . .'"

        hide happ1
        show shy1

        "'If we..could become real friends!..'"

        "'I'd love to be able to... call myself your friend...'"

        "'I'm sorry if this is too sudden!..'"

        hide shy1
        show happ1

        "'I'm just a bit nervous but... in a good way!..'"

        "'To be honest, I haven't felt at ease like this for a long time...'"

        hide happ1
        show happ3

        "'Thank you!..'"

        "'You came here even though it's dangerous to walk alone, but... I'm glad I met you.'"

        hide happ3
        show happ1

        "'Even for a little while.'"

        "'If I could ever help you with anything... Don't hesitate to ask!'"

        hide happ1
        show bye2 with dissolve

        "'I wish you only the best... Even if it's not right to say goodbye like that...'"

        "'Maybe next time we could play games together...'"

        "'A fighting game or... a farm?'"

        "'I would be so happy to spend time with you again.'"

        "'And also, we-...'"

        stop music fadeout 2

        "'. . .'"

        "'. . .'"

        hide bye2
        show bg afraid
        show bye3 with hpunch

        "'. . .'"

        "I-I'm sorry, I..."

        "'I'm sorry!'"

        "'You should-!'"

        hide bye3
        play sound computer

        scene bg black
        with hpunch
        pause (1.0)

        scene mon red with dissolve

        a "> The friendly face has been suddenly consumed by the bright light."

        a "> Before you were able to aknowledge it, the whole screen is burning red again."

        a "> What happened?"

        a "> You desperately touch the screen a couple of times, but there's no response."

        scene bg black with dissolve
        pause (1.0)

        a "> And this is when... You understand."

        scene 1111 with dissolve
        play music heart_beat01 fadein 1

        a "> Something's not right."

        a "> . . ."

        a "> You feel an unberable tension going through your body and making you completely still."

        scene end1 with dissolve

        a "> There's someone else... in the room."

        a "> You can't hear the steps nor the breathing, but you feel it."

        a "> You feel a heavy gaze on the back of your head."

        a "> . . ."

        scene bg black with dissolve
        pause (1.0)

        stop music

        m "'Hey there...'"

        m "'Haha... What are you doooing here?'"

        m "'Actually, that's mine...'"

        scene end2
        play sound horror_pianochord3

        m "'Weren't you taught not to stick your nose where it doesn't belong?'"

        m "'You're being awfully nice, aren't you?'"

        m "'It's a good thing I know juuuust how to fix this! Haha...'"

        play sound earth3
        scene bg black with hpunch
        pause (2.0)

        "END 2"

        return

    elif points <= 45:


        show bg sad with dissolve
        scene
        show bg sad
        show sad2
        play music hazama1 fadein 1

        "'I know we don't have much time left but...'"

        hide sad2
        show sad1

        "'I just don't understand... What did I do wrong?..'"

        "'I mean, I wasn't mean to you...'"

        "'Or do you just see me as an enemy because I'm... in this room? And because I know Hiyori-kun?'"

        "'I can understand that but...'"

        hide sad1
        show sad5

        "'. . .'"

        hide sad5
        show cry1

        play sound kirekake

        "'I-I'm sorry, it's just... not fair!..'"

        "'I never wanted to harm you, and...'"


        show bg afraid with dissolve
        hide cry1
        show cry2

        "'I've never tried to do anything to you while we were talking!...'"

        "'Even if I'm not a human, my conscious is... It's still the same as yours, as of any human...'"

        "'. . .'"

        hide cry2
        show bye1 with hpunch

        "'I'm sorry. I won't bother you anymore since you dislike me so much.'"

        hide bye1 with hpunch

        scene bg black
        with hpunch
        pause (1.0)

        scene mon red with dissolve

        a "> The friendly face had been suddenly consumed by the bright light."

        a "> Before you were able to aknowledge it, the whole monitor is burning red again."

        a "> Well. That was expected."

        stop music fadeout 2

        a "> You get up with a tired sigh."

        scene bg black with dissolve
        pause (1.0)

        a "> And this is when... You understand."

        scene 1111 with dissolve
        play music heart_beat01 fadein 1

        a "> Something's not right."

        a "> . . ."

        a "> You feel an unberable tension going through your body and making you completely still."

        a "> There's someone else... in the room."

        a "> You can't hear the steps nor the breathing, but you feel it."

        a "> You feel a heavy gaze on the back of your head."

        a "> . . ."

        scene bg black with dissolve
        pause (1.0)
        stop music

        m "'Hey there...'"

        m "'Haha... What are you doooing here?'"

        m "'Actually, that's mine...'"

        scene 11112
        play sound horror_pianochord3

        m "'Weren't you taught not to stick your nose where it doesn't belong?'"

        m "'So rude of you...'"

        m "'It's a good thing I know juuuust how to fix this! Haha...'"

        play sound earth3
        scene bg black with hpunch
        pause (2.0)

        "END 3"

        return
    else:




        show bg neutral with dissolve
        scene
        show bg neutral
        show sad1
        play music tunagu2 fadein 1


        "'I know we don't have much time left but...'"

        hide sad1
        show neutral2

        "'It was nice to spend time with you.'"

        "'Even if you still don't trust me completely, I can understand why...'"

        hide neutral2
        show happ3

        "'I'd be glad to get to know you more...'"

        "'Haha...'"

        hide happ3
        show neutral1

        "'But if you ever need my help...'"

        "'Don't be afraid to ask.'"

        hide neutral1
        show happ4

        "'Thank you for spending time with me...'"

        hide happ4
        show neutral2

        "'You probably should go back to your friends before it's to late...'"

        "'And don't worry, I won't tell anyone you were here!'"

        hide neutral2
        show happ2

        "'I wish you only the best!..'"

        hide happ2
        play sound computer

        scene bg black with dissolve
        pause (1.0)


        scene mon red with dissolve

        a "> Before you could answer, the screen went red again."

        a "> Well... It was an Experience."

        a "> You didn't learn anything that would help you, but for some reason you feel... at ease."

        a "> Maybe you just needed a distraction."

        scene bg monitor room 1 with dissolve
        play music tansaku3 fadein 1

        a "> You get up from your chair with a sigh and walk to the door."

        a "> You hear steps from behind it."

        a "> Feeling determined, you open the door."

        scene bg black with dissolve
        pause (2.0)

        "END 4"
        stop music fadeout 2

        return






    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
