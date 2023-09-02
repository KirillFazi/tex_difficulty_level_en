import numpy as np

from transformers import BertTokenizer
import torch

TOKENIZER = BertTokenizer.from_pretrained('sentence-transformers/all-mpnet-base-v2')


def split_text_by_n_words(text: str, n: int = 128) -> list:
    """
    Split text by n words
    :param text: Text to split
    :param n: Number of words in chunk
    :return: List of chunks
    """

    tokens = text.lower().split()
    chunked_text = []

    for i in range(0, len(tokens), n):
        chunk = " ".join(tokens[i:i + n])
        chunked_text.append(chunk)

    return chunked_text


def data_preprocess(subs: str, n: int = 128) -> tuple:
    """
    Preprocess data for prediction model. Split text by n words, tokenize it and split by 256 tokens
    :param n: Number of words in chunk
    :param subs: Subtitles string
    :return: Tuple of list of sequences and list of masks
    """
    text_list = split_text_by_n_words(text=subs, n=n)

    tokens_text = TOKENIZER.batch_encode_plus(
        text_list,
        max_length=256,
        padding='max_length',
        truncation=True
    )

    text_seq = torch.tensor(tokens_text['input_ids'])
    text_mask = torch.tensor(tokens_text['attention_mask'])

    list_seq = np.array_split(text_seq, 256)
    list_mask = np.array_split(text_mask, 256)

    return list_seq, list_mask


if __name__ == '__main__':
    test_subs = "ben on phone michelle, please don t hang up. just talk to me, okay? i can t believe you just left. michelle. come back. please say something. michelle, talk to me. look, we had an argument. couples fight. that is no reason to just leave everything behind. running away isn t gonna help it any. michelle, please. newscaster more details on that. elsewhere today, power has still not been restored to many cities on the southern seaboard in the wake of this afternoon s widespread blackout. while there had been some inclement weather in the region, the problem seems linked to what authorities are calling a catastrophic power surge that has crippled traffic in the area. no. no! damn. okay. okay, please. please. please don t hurt me. please. just let me go, okay? i won t tell anybody. i promise, okay? please just let me go. please. man you need fluids. you were in shock. what are you going to do to me? i m going to keep you alive. work on getting handy with these. my boyfriend was expecting me. he ll send the cops looking. i m sorry. but no one is looking for you. you ve got some fight in you. i can respect that. but don t even think about trying that again. you re lucky to be here at all. and my generosity only extends so far. eggs. toradol to help with your pain. please. please, just let me go. please. there is nowhere to go, michelle. i looked through your wallet. given as how i saved your life, i think that s acceptable. you re lucky to be here at all. what do you mean? i found you, and i saved your life by bringing you here. i don t understand. i. there s been an attack. what? an attack. a big one. i m not sure yet if it s chemical or nuclear, but down here, we re safe. and where are we exactly? underneath my farmhouse. forty miles outside of lake charles. i was driving north of here. you were in an accident. you were turned over on the side of the road. i was driving by and i saw. i saved your life, michelle. i couldn t just leave you there. okay. well, thank you so much for saving my life. i guess i should go to a hospital now. you can t leave. an attack means fallout. which contaminates the air above ground. that s how it works. how long do we have to wait until it s safe? depends on the proximity of the closest blast. one year, maybe two. and that s if we re talking about weapons that we know of. russians are developing some nasty stuff. and if the martians finally figured out a way to get here, their weapons will make the russkies look like sticks and stones. luckily, i ve prepared for this. right. well, i ll need to use your phone then to call my family and tell them that i m safe here and make sure they re okay. michelle, they re not okay. how do you know that? everyone outside of here is dead. but what about you? don t you have a family? who s that? excuse me. howard what did you do? you know what, michelle? i m gonna tell you what i told him. you need to eat, you need to sleep, and you need to start showing me a little bit of appreciation. my name is howard, by the way. oh, god! oh, shit. i m sorry. i m sorry about that. uh, i didn t mean to scare you. are you, um. here. you hungry? so, how are you doing? you okay? what is this? it s a bunker. your room s a little bit of a fixer upper, but at least you got a door. a scary door, but you still got a door. how long have you been down here? couple of days, i think. you know, it s actually kind of hard to tell with no windows or sunlight or anything. i mean, how do we get out of here? oh, he didn t tell you? about. getting out of here is the last thing you want to do. because the air up there, it s contaminated. howard i see you ve met emmett. what happened to him? he did that to himself. and his stumbling around isn t helping anything. what you heard earlier, was him knocking over a shelf with a whole week s worth of food, which he s sorry for, correct? totally. let s go. bathroom time. howard this is the common area. good for r r. as you can see, i ve planned for a long stay. the aquaponics system cleans the air and keeps it fresh. this is the living room. help yourself to any reading. if you like to watch films, i have some on dvd and vhs cassette. just make sure you put them back in their sleeve when they re done. the kitchen s fully functional. has an electric stove, refrigerator, freezer, silverware. and that table s a family heirloom, which means watch your glasses. always use coasters and placemats. keep your hands to yourself! understand? no touching. take a seat. this way. this is my private space. off limits, unless i give express permission. go ahead. i don t need to. you will, though. and i ve got to pace these things out, so please. i need privacy. you re welcome to close the curtain. i can t with you standing there. and i can t trust you not to burn this place down. this is for my own safety. i m not some pervert! just go. howard don t flush unless you ve gone! we can t afford wasted flushes. take a seat. are you hungry? those are megan s. she never went anywhere without two or three of those things. who s megan? megan s not with us anymore. don t worry. just the generator. maybe it s a car outside. that s not possible. i heard one earlier. above my room. if you had heard a car, the driver would be long dead by now. well, shouldn t we at least try to call the police or someone to find out what actually happened? there s no one left to call. see that? nothing s coming through. you think i sound crazy. i mean, it s amazing. you people. you wear helmets when you ride your bikes. you have seat belts in your cars. you have alarm systems to protect your homes. but what do you do when those alarms go off? crazy is building your ark after the flood has already come! i think maybe it s time you met frank and mildred. closest i could get to an airlock. see? what happened to them? they weren t as lucky as you. it s the air, michelle. that s what happens when you get exposed. i keep this door sealed at all times. no one comes in or out. emmett met frank and mildred, huh? it s funny, right? the whole world ends and the thing he s most upset about is a pair of dead pigs? you in need of some reading material? i took all the quizzes. sorry. but i did learn how to do a french braid, so, you know, if you want me to do that for you, just let me know. what do you know about him? he was in the navy, i know that. i guess he did, uh, some stuff with satellites. what kind of stuff? satellite stuff. well, what brought him out here? i m not sure. he bought this property a while back. but i never paid much attention till he hired me to help him get this place set up. the work was entertaining, though, that s for sure. you know, howard s like a black belt in conspiracy theory. plus, you know, how often do you get hired to help build a doomsday bunker? so, he didn t kidnap you? no! what about your arm? weren t you trying to escape? i was trying to get in. i watched howard build this place, piece by piece, for years. he was always talking about, you know, possible attacks from. al qaeda, russia, south korea. you mean north korea. is that the crazy one? so, yeah, that one. and, uh, you know, poured all his money into this place. took to it like his life depended on it. which, you know, that stays with you. so. he told you all this while you re building his bomb shelter. and now he says that the air is contaminated and everybody s dead. yeah, i know what you re getting at, but there s more to it. howard abducted me. he drove me off the road and he dragged me here. so, whatever he s telling you about the air, some big attack, the purpose of this shelter, is a lie. no. no way. the attack, i saw it myself. what do you mean? i was on my way home from work. and it looked like a flash. bright red. like an explosion, from way far off. it wasn t like fireworks. naw, this was more like something you d read about in the bible. so, what, you saw, what, a flash of light? lightning? a fire that flared up? i m not explaining it right. this wasn t like anything i d ever seen. and so, my first thought was to come here. and when i got here, howard was closing the door. and i could see it, right there on his face, he knew something was happening. something bad. and so, i fought my way in. i heard a car. right here. above us. you heard someone? right above us. that isn t possible. the air is. what, contaminated? how do you know that? because i told him. dinner s ready. i see you two are getting along. hmm. how s that sauce? it s fine. as cooks go, i m okay. not great, but okay. megan was a good cook. you ll learn to love cooking. mmm. emmett mmm. it s delicious. that s the best sauce i ve ever tasted. are you being funny? no, i mean, considering the alternative, which is, you know, getting burnt up in a chemical attack, or nuclear, i d say being alive and down here would make a fried turd taste pretty good, so. best damn sauce i ever had. that s not a bad point. and, please, watch your language at table. right? you know what i haven t been able to get out of my head, for some reason? ever since i got down here. tattoos. always wanted one. but i never got any. cause everybody always said, no, no, emmett, you ll never get a decent job if you do that. whatever. like that matters now, right? t ell you what, if i had known this was coming, i would ve gotten, like, of them. i swear, man. i would look like a circus freak, or something. i d just be covered head to toe. tattoos all over my. you know, everywhere. face? sure. right there. across my forehead. just my name. emmett. or, you know, thug life. yolo. i don t even know what that means, but, you know, i hear people saying it all the time, so, it must be cool. hey, what about you, howard? anything you wish you d done? in all honesty, no. no? no crazy nights in vegas? maybe, uh, take a pilgrimage to waco? everything i wanted to do, i did. i focused on being prepared. and i was. and here we are. emmett oh, my goodness. is that monopoly? there we go! yeah, that s how we kill the time. what would you say, howard, we re gonna be down here, what, like, a year? two? maybe? i bet you if we started a game right now, we might even get halfway finished by the time. stop talking! you don t need to make jokes about how long we re going to be down here when nobody knows how long that s going to be. your humor is not funny. i don t appreciate it while i m trying to eat, and neither does michelle. now, please shut up and let us eat in peace. hmm. emmett? would you pass me a napkin? thank you. i know what you re saying. i never could finish monopoly. that game really does take forever, right? for me, though, it was, um. chutes and ladders, uh. sorry!, and trouble. you know, the thing with the dice and the thing that you pressed, what was that called? the. both pop o matic bubble! yeah. did you ever play that, um. what was that, operation? loved operation! i m telling you, man, i couldn t play that game. it terrified me. why. that noise that thing would make when you hit that edge. i mean. good lord! it was pretty scary. could you hand me the salt? please? ah, shoot! i m sorry. i m gonna need the pepper also. what exactly do you think you re doing? i m asking for pepper. like hell you were! what was that? i don t know what you re talking about, howard. are you trying to insult me? here, in the shelter that i built that s keeping you alive? you don t think i see what you just did? is that how you thank me for saving your life? howard, calm down. shut up! shut up and stay in your seat! is it? now, let me tell you, i know what a traitor looks like. understand? i have shown you nothing, but generosity and hospitality. i want you to apologize. to tell me you re going to behave. i will. you will what? i ll behave. and i m so sorry. howard sit. ah. have to stay hydrated. hmm. that s easy to forget down here. what s wrong? nothing. where are my keys? michelle! michelle! stop! give me those keys! michelle come on. howard no! don t! stop! no! no, don t! don t! don t open that door! there s a car! there s a car! i see a car! howard no! here! here! here! howard michelle, listen to me, don t do this! oh, god! thank god! there s a woman. woman open the door! it s okay. i just want to come inside. she looks hurt. she wants me to let her in. do not let her in! look at her face, michelle! no! no, no, no! no! oh, my god, i m fine. i really am fine. no, please, i m okay. there s. it really only. it only touched me a little. a little! so, could you open the door? open it! she s begging me. you can t help her! no one can! let me in. i ll be okay. i ll be okay. it really hardly touched me at all. open the door! howard don t listen to her! god! open the door, you bitch! let me in! let me in! let me in! let me in! let me in! you! you! you! you! you! i know it s hard, realizing they re all gone. the ones you love. i have something to confess to you. i crashed into your car. your accident was my fault. when i found out about the incoming attack, i got frantic. i knew i needed to get back here as soon as possible, so i was driving like a maniac. i tried to pass you, and i m the reason you went off the road. i mean, i know i seem like a sensible guy, but at the time, i wasn t myself. it was an accident, but it was my fault. i was afraid to tell you, and, i m sorry. um. you should shower. even the smallest amount of air that came through the hinges could be toxic. these were megan s. if you want. i recognized that woman s car. her name was leslie, i think. you knew her? she was a neighbor. emmett wasn t the only one who knew about this place. if any others somehow survived, they could be coming here, too. as of friday, kindness and generosity are antiquated customs. i m going to need some stitches. what? you want me to. this is your doing, isn t it? i mean, i don t think i m really qualified. i ll walk you through it. here. have a drink. what is it? technically, it s vodka. ah! it s safe. i distilled it myself. i just said i distilled it, i didn t say anything about it actually tasting good. yeah, that s awful. you want it on the rocks? little trick i taught myself as a young man stationed on a ship with way too much free time. every now and again, if the c.o. was working us too hard, we d freeze and snap the knob off the bathroom door while he was still inside. it usually took him an hour or two to get out. i m good. suit yourself. cheers. ah. this is clean. all you need to do is stitch. you re doing fine. howard some stuff i grabbed from your car. i didn t have time to bring in the booze. sadly. what is all that? i wanted to design clothes. no wonder you were so good with the stitches. megan wanted to be an artist. she was your daughter? yes. she was smart. loved to read. the magazines were just for fun. she inhaled books. anything with paris. she liked their movies, their culture, you know. we used to have this little joke. every once in a while i d ask her, what do you want to be when you grow up? you know what she d say? french. anyway, her mother turned her against me. took her off to chicago. people are strange creatures. you can t always convince them that safety is in their own best interest. you don t know they re gone. anyway, at least i tried to help them. emmett hey. there was nothing you could ve done for that woman. even if you let her in, she still would ve died. you asked earlier about regrets? yeah, i ve got some of those. welcome to the club. i mean, i lived my life in a mile radius. and that was by design. i made sure that happened. i was so fast in high school, i even managed to outrun my bad grades. i was all state track three years in a row. caught a full ride to louisiana tech, up there in ruston. i remember i spent the last two weeks of that summer showing off the bus ticket they sent me to anybody who d take a look at it. and then came the night before i was supposed to leave. and i just got so worried about how bad i was gonna do up there with all those smart kids. so, i went out of my way to get just piss wasted so bad that i knew there was no chance i was waking up in the morning. so, i missed the bus. and i didn t buy a ticket for the next one. or the one after that. well, if you d gone, you might be dead now. yeah, lucky me, right? lucky us. a few years ago, i was at a hardware store. and there was this little girl with her dad. and he was in a hurry, and she wasn t keeping up. so, he kept yanking on her arm. but really hard, you know? too hard. i know that feeling. when my dad got that way, my brother colin was always there to take the worst of it for me. and i thought, seeing this little girl, i thought maybe i could do that for her. but i just kept watching. and they re about to leave, and i ve done nothing. and she slips. and it throws him off balance, and he hits her. and i wanted so badly to do something to help her, but. i did what i always do when things get hard. i just panicked and ran. look, we re here. we re alive. and that means something. it s gotta. you ve got to be kidding me. what? we re missing pieces here. look at this poor cat. he s been deformed. he s got one eye. he s about to go snorkeling and everything, too. what are you doing? ooh! cornering the market on post apocalyptic fashion, huh? mmm hmm. you need more axes and chain saws. for what? she has a shotgun. yeah. but what if up there it s like. what? lumberjacks? zombies. though even howard doesn t think that one s plausible. but you should hear his theory about mutant space worms. what is that? howard! stay calm. we re okay. what was that? quiet. that sounds like helicopters. howard could be military. but not ours. emmett how can you tell? fourteen years in the navy. what s happening up there? my guess? those flashes that kicked this all off? that was phase one. take out your opponent s population centers with big hits, all at once, fast. and then for round two, ground sweeps. a satellite log showed an increase in coded traffic recently. possibly extraterrestrial signals. i bet what we just heard were airborne patrols sent to hunt down the remaining signs of life. like us. okay. oh, boy. that s bad. and that s worse. what s up there? air filtration system. i can t. something blocking the hatch. if we can t get it back on, we re gonna run out of breathable air fast. you re the only one small enough to reach it. reach what? the filtration system. through there, the main duct. someone needs to get in there and restart it. give me a hand. let me go. she s not gonna know her way around the unit. you won t fit. plus your arm. she ll be fine. now, to restart the unit, you just swing the handle off, then on, off, then on. that should do it. and neither of us will be able to go in and help you if you get stuck. don t get stuck. howard michelle! everything okay up there? it looks like a dead end. howard that s the incline. climb up that and you re almost there. ah, this sucks. emmett what s wrong? howard. he lied, he lied about megan. what do you mean? i think he did something horrible to her. no, his family moved to chicago years ago. what s this? is that blood? here, come with me. wait, that. that s not megan. what do you mean? yeah. her name is brittany. i remember her. she went to high school with my little sister. she. she went missing. two years back. it was on the news and everything. most people just thought she skipped town. there was a message up there. it said help. it was scratched on the inside of the window. and this earring. this earring was with it. did she ever show back up after she went missing? he said to me. he said to my face, that this was his daughter. he said this was megan. he took her and he killed her. all right, let s just think. maybe we take away his gun. tie him up, get him to confess to whatever it is he s done. confess to who? the police? look, like i said, we can t be the only survivors, right? the woman, she was able to get around, right? at least a little. yeah, until she died. directly above us, making choking noises. of all the people to save us. howard now, that was a great example of teamwork. very well done. i feel like some music. problem solving always puts me in a musical mood. michelle, you should go shower, just in case. sure. i think i might have an idea. ten better ways to style my bangs ? no, not the article. this. i think i can only make one, but it s a start. no kidding. what are you doing up? i didn t wake you up yet. man well, i m fixing your breakfast. one egg over medium. hey, howard. what is this? you re watching sixteen candles? pretty in pink. it was one of megan s favorite movies. can i help you with something? no. no, i m just grabbing some water. say, um. you know, i was just thinking. not that i m trying to tell you how to run this place or anything. i m just a little curious. michelle. say, how close do you think she got to that air filtration unit? you think she touched it? yeah, i m pretty sure she touched it. well, i know she cleaned up after and everything, but i m just thinking, given that unit filters god knows what through from outside, if she tracked anything back in with her, it d be pretty concentrated. and, i mean, it could be all over the shower and the sink in your bathroom, right now. anyway, it s just a thought. emmett not bad so far, partner. michelle if howard finds this, he s gonna kill us. all right, so, we get the gun away from him. all right. we tie him up, make sure he isn t going anywhere. and then one of us just goes out and looks for help. um. first word. uh. tiny. small. pygmy. um. little. yep! mmm hmm. all right, uh, second word. ooh! michelle is a. a girl. a girl. a child. um. a girl. no, she s older, see, so she is a. little princess ? um. no, it was woman. um, little women. wow. little woman. next time, try being a little more specific. let s see here. i m always watching. always. um. god. i go wherever i want. uh. i mean. well, i don t know. i know what you re doing. i see what you re doing. um. i know what you re up to. look, howard, i don t know what you re getting at, but. i see you when you re sleeping. i know what you re doing, and i m always watching. always watching! i m always watching! santa claus! you re santa claus. yeah, michelle, that s great. except it was emmett s turn. sorry, i just got a little excited. yeah, well, i m keeping that point. totally. you earned it. emmett? hey. i need your help with something. sure. you. on deck. what is this? howard the barrel. what s in it? move it into the bathroom. howard this is perchloric acid. do either of you know what that is? it s usually produced as a precursor to ammonium perchlorate, a fuel used for launching naval satellites into orbit. it s highly corrosive. dissolves most biological material on contact. with humans, right down to the bone. hey, howard, uh, what are you showing this to us for? you think i m an idiot? emmett uh. howard, please, you re gonna have to tell us what it is that you re talking about. i m talking about getting rid of some waste. tell me what you two were doing with these. you tell me what you two were planning, right now! howard, listen, just take it easy. take it easy. howard, come on, please. no. i m giving you one chance. emmett hey. howard, just calm down. one chance to answer with some dignity, or i swear to god, you re going into this barrel while you re alive to feel it. it was me. all right? not her. it s just me. no, no, no, we. stay out of this, all right? she doesn t have a clue what you re talking about. i wanted your gun. and so, i was thinking about making a weapon to get it from you. i want her to respect me the way that she respects you. i m not saying that i was right, okay? and i m sorry. you re sorry? i m sorry. i accept your apology. listen to me. you heard him. you heard him. he was making a weapon. he was gonna hurt us. he was gonna hurt you. and it s okay. this was the way it was always supposed to be. you re safe. now it s just you and me. it s okay, you know. you should go to your room now. this next part isn t something you need to see. okay. go on. howard michelle? hey. i thought we d change things up tonight and have dessert before dinner. after all, we can do whatever we want now. would you like a cone or a bowl? megan always wanted hers in a bowl. she said the cones were too messy. i know that this isn t the life you d prefer, that it isn t easy for you living down here, but i want us to be a happy family. you and me. the mess is all taken care of. so, just hang loose and i ll go get dinner started. howard michelle? everything all right? yeah, i was just about to do some reading. hmm. it s time to set the table. supper s ready. yeah. okay. it keeps doing that. i don t know why. michelle, why is this loose? get up. why? get off the mattress now! oh, shit! michelle! stop! goddamn it, get back here! howard you gonna walk out on me? after i saved you and kept you safe, this is how you repay me. no. this is. howard michelle! stop! you don t know what s out there. you can t run from them! howard stay with me! let me go! oh, come on. keys, keys, keys. come on, damn it! come on. come on. help! i m out here! help! oh, god. oh, fuck. female broadcaster the military has taken back the southern seaboard. if you are hearing this and aren t in a safe zone, head north of baton rouge. but if you have any medical training or combat experience, we need help. there are people in houston. there are survivors at mercy hospital. please help. repeat. there are people in houston who need our help. come join us. we ve taken back the southern seaboard. and we re winning. but if you have any medical training or combat experience, there are survivors. "
    print(data_preprocess(test_subs))