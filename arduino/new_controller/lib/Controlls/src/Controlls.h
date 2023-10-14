/*
  Controlls.h - Library for controlling Controlls.
  Created by Maximilian Weber, April 29, 2023.
*/
#ifndef Controlls_h
#define Controlls_h

#include "Arduino.h"

static const byte SETTING_STATIC = 0;
// 1-29 are singular settings
static const byte SETTING_SINGULARFLASH = 2;
static const byte SETTING_SINGULARBURST = 3;
static const byte SETTING_SINGULARLINEAR = 10;
static const byte SETTING_SINGULARBEZIER = 20;

static const byte SETTING_SINGULAR_DIVIDER = 30;
// 30-99 are continuous settings
static const byte SETTING_SINWAVE = 30;
static const byte SETTING_LINEARWAVE = 40;
static const byte SETTING_LINEARSAW = 41;

static const byte SETTING_BEZIERWAVE = 50;
static const byte SETTING_BEZIERSAW = 51;

static const byte SETTING_SQUAREWAVE = 60;

static const byte SETTING_EFFECT_DIVIDER = 100;
// 100-149 are Effects
static const byte EFFECT_UPVIBRATO = 63;
static const byte EFFECT_DOWNVIBRATO = 64;
static const byte EFFECT_UPDOWNVIBRATO = 65;
static const byte EFFECT_STROBE = 70;
static const byte EFFECT_PERLIN = 80;
static const byte EFFECT_UP = 90;
static const byte EFFECT_DOWN = 91;
static const byte EFFECT_UPDOWN = 92;
static const byte EFFECT_NONE = 140;

static const byte LIGHT_SET_CHANNEL = 150;

static const byte CHANNEL_SET_SETTING = 160;
static const byte CHANNEL_SET_CHANNEL = 161;
static const byte CHANNEL_SET_STATIC = 162;

static const byte CHANNEL_ADD_EFFECT = 170;
static const byte CHANNEL_REMOVE_EFFECT = 171;
static const byte CHANNEL_REMOVE_EFFECTS = 172;

static const byte SETTINGS_RESET = 180;
static const byte EFFECTS_RESET = 181;
static const byte CHANNELS_RESET = 182;
static const byte NOW_INCREASE = 190;
static const byte NOW_DECREASE = 191;
static const byte SYNC_ON = 192;
static const byte SYNC_OFF = 193;


static const byte MOTOR_SPEED = 220;
static const byte MOTOR_DIRECTION = 221;


// other global variables
static const unsigned int PERLIN_SIZE = 900;
const PROGMEM float PERLIN_NOISE[PERLIN_SIZE] = {
  0.7813468849570299f, 0.7537971700738431f, 0.7262474551906564f, 0.6986977403074698f, 0.6832585875854792f, 0.6678194348634888f, 0.6523802821414985f, 0.640997824062393f, 0.6504702911372845f, 0.6599427582121761f, 0.6590973005827955f, 0.6582518429534152f, 0.6574063853240346f, 0.672968217413889f, 0.6885300495037434f, 0.6661871623244552f, 0.6338948125961624f, 0.6016024628678693f, 0.5693101131395766f, 0.5188219723700029f, 0.4683338316004294f, 0.4178456908308559f, 0.4225689092804824f, 0.42729212773010905f, 0.4320153461797356f, 0.3910930082004425f, 0.35017067022114934f, 0.3092483322418562f, 0.32501749410959263f, 0.37544563002260095f, 0.42587376593560927f, 0.43295722005949827f, 0.44004067418338716f, 0.44712412830727616f, 0.4864006969614642f, 0.5256772656156523f, 0.5401299391212421f, 0.4989932134855578f, 0.4578564878498734f, 0.41671976221418905f, 0.4287911366869154f, 0.4408625111596417f, 0.4529338856323681f, 0.4632760835314356f, 0.4736182814305032f, 0.48396047932957076f, 0.43587925274824885f, 0.387798026166927f, 0.339716799585605f, 0.34398069120080016f, 0.3481095108067114f, 0.3522383304126225f, 
  0.36658161649787274f, 0.3809249025831229f, 0.3952681886683731f, 0.3512930982932398f, 0.30731800791810654f, 0.28116424389329936f, 0.2860701063873715f, 0.29097596888144356f, 0.2958818313755157f, 0.3086594307552669f, 0.321437030135018f, 0.3342146295147692f, 0.4021259915185208f, 0.47003735352227255f, 0.5379487155260242f, 0.5378455820625588f, 0.5377424485990936f, 0.5376393151356282f, 0.5464426948226386f, 0.5101683170938469f, 0.47389393936505536f, 0.4924014387104145f, 0.5109089380557736f, 0.529416437401133f, 0.5025414928516422f, 0.47566654830215155f, 0.45828983239147686f, 0.45499319662432003f, 0.45169656085716314f, 0.4483999250900062f, 0.406868468897401f, 0.3653370127047959f, 0.3238055565121907f, 0.3691705831407972f, 0.4145356097694036f, 0.45990063639801004f, 0.43440168009014907f, 0.408902723782288f, 0.38340376747442684f, 0.4064644125363295f, 0.4260863316607652f, 0.44570825078520093f, 0.4284148200326995f, 0.411121389280198f, 0.3938279585276966f, 0.3956816036529325f, 0.3975352487781684f, 0.38629349201109103f, 0.38694524505683714f, 0.38759699810258336f, 0.3882487511483296f, 0.37333686116484577f, 0.35842497118136213f, 0.3435130811978783f, 0.36144964430949006f, 0.37938620742110163f, 0.39732277053271337f, 0.382950770023441f, 0.3685787695141686f, 0.3542067690048963f, 0.32549456262369336f, 0.3049592832133593f, 0.28442400380302524f, 0.33063965106816107f, 0.37685529833329695f, 0.4230709455984327f, 0.38621821600645556f, 0.34936548641447845f, 0.3106114608863354f, 0.3347780381993877f, 0.35894461551244006f, 0.3831111928254924f, 0.3680831829442539f, 0.3530551730630153f, 0.33802716318177684f, 0.35332584553374824f, 0.36862452788571953f, 0.3839232102376909f, 0.4507666580099105f, 0.5176101057821303f, 0.5844535535543498f, 0.6065923827843923f, 0.6280123743692395f, 0.6494323659540866f, 0.6357459301024447f, 0.6220594942508029f, 0.608373058399161f, 0.6565524934665499f, 0.7047319285339386f, 0.7235761269828916f, 0.6980772079252576f, 0.6725782888676234f, 0.6470793698099895f, 0.6391571234599217f, 0.6312348771098542f, 0.6233126307597865f, 0.5949587491923736f, 0.5666048676249605f, 0.5382509860575476f, 0.5173299962498973f, 0.4964090064422469f, 0.4754880166345965f, 0.4346289224724617f, 0.4303311940125668f, 0.42603346555267185f, 0.473038521439099f, 0.5200435773255263f, 0.5670486332119535f, 0.5943285639521901f, 0.6216084946924268f, 0.648633227957356f, 0.6210926369022522f, 0.5935520458471486f, 0.5660114547920448f, 0.6169359997199627f, 0.6678605446478805f, 0.7187850895757983f, 0.65879886912816f, 0.5988126486805219f, 0.5388264282328837f, 0.5407359072661359f, 0.542645386299388f, 0.5445548653326402f, 0.5461217991846282f, 0.5631068988514344f, 0.5800919985182407f, 0.5656315479846654f, 0.55117109745109f, 0.5367106469175148f, 0.5395309995850498f, 0.542351352252585f, 0.5504915909651511f, 0.5302024609625365f, 0.509913330959922f, 0.4896242009573073f, 0.5097845083040009f, 0.5299448156506945f, 0.5501051229973882f, 0.5329130206093287f, 0.515720918221269f, 0.49852881583320935f, 0.5020419061845741f, 0.5055549965359388f, 0.5090680868873037f, 0.5171769802253012f, 0.5416048676963701f, 0.5660327551674388f, 0.5760914385704233f, 0.5861501219734078f, 0.5962088053763922f, 0.5968814699488957f, 0.597554134521399f, 0.6089664690639063f, 0.6019106797874888f, 0.5948548905110712f, 0.5877991012346538f, 0.6337246451416152f, 0.6796501890485763f, 0.7255757329555379f, 0.7216581318662117f, 0.7177405307768858f, 0.7138229296875597f, 0.6929924382401458f, 0.6721619467927316f, 0.6513314553453178f, 0.6550422375312347f, 0.6737508618985737f, 0.6924594862659125f, 0.6792969159118472f, 0.666134345557782f, 0.6529717752037166f, 0.6685509739048001f, 0.6841301726058833f, 0.6686522821049726f, 0.6787794178788994f, 0.6889065536528263f, 0.6990336894267531f, 0.6780877769347878f, 0.6571418644428226f, 0.6361959519508573f, 0.6053525409999384f, 0.5745091300490196f, 0.5436657190981007f, 0.5377598789818457f, 0.5318540388655908f, 0.5259481987493358f, 0.48315832332314357f, 0.46426841076964864f, 0.4453784982161537f, 0.4516911907512774f, 0.45800388328640096f, 0.46431657582152464f, 0.4953610551445847f, 0.5264055344676447f, 0.5637095051088946f, 0.577658747238204f, 0.5916079893675132f, 0.6055572314968226f, 0.6250309536851462f, 0.6445046758734697f, 0.6639783980617933f, 0.6306468014132626f, 0.597315204764732f, 0.5639836081162011f, 0.5491876142366791f, 0.5343916203571568f, 0.5195956264776348f, 0.47785014403585174f, 0.4451502791575236f, 0.4124504142791954f, 0.45025732887801106f, 0.48806424347682675f, 0.5258711580756423f, 0.5162979951329697f, 0.5067248321902972f, 0.5179427960342045f, 0.5161696084185958f, 0.5143964208029871f, 0.5126232331873782f, 0.49566829894713993f, 0.47871336470690173f, 0.4617584304666635f, 0.5018613382449886f, 0.5419642460233137f, 0.5820671538016389f, 0.5667839476052257f, 0.5515007414088127f, 0.5362175352123996f, 0.5618125694763324f, 0.5570717171145323f, 0.5523308647527322f, 0.554013517549815f, 0.5556961703468979f, 0.5573788231439808f, 0.5411481575430174f, 0.5249174919420541f, 0.5163639012895772f, 0.532720685885357f, 0.5490774704811368f, 0.5654342550769167f, 
  0.529813353721941f, 0.49419245236696524f, 0.45857155101198965f, 0.4707982601022155f, 0.48302496919244126f, 0.49525167828266686f, 0.4897593052587682f, 0.48426693223486955f, 0.4787745592109708f, 0.5097176234073738f, 0.5439191927098386f, 0.5781207620123031f, 0.5478738308966287f, 0.5176268997809542f, 0.48737996866527983f, 0.5112645059881386f, 0.5351490433109974f, 0.5491387391992142f, 0.5261356455555659f, 0.5031325519119176f, 0.4801294582682694f, 0.4898426347332369f, 0.4995558111982045f, 0.509268987663172f, 0.5244164448633757f, 0.5395639020635792f, 0.5547113592637828f, 0.5320001247801905f, 0.5092888902965981f, 0.4865776558130057f, 0.5330931413495401f, 0.5707019692636738f, 0.6083107971778076f, 0.5775432373206709f, 0.5467756774635343f, 0.5160081176063978f, 0.5051902237613535f, 0.4943723299163093f, 0.5042701381152094f, 0.49972586805796537f, 0.4951815980007215f, 0.49063732794347753f, 0.5428192480986512f, 0.5950011682538249f, 0.6471830884089987f, 0.645599477409957f, 0.6440158664109155f, 0.6424322554118739f, 0.611136449033055f, 0.5798406426542362f, 0.5485448362754172f, 0.5378143493139987f, 0.5072954400446279f, 0.476776530775257f, 0.4785647742000517f, 0.48035301762484656f, 0.48214126104964133f, 0.4273070877262066f, 0.37247291440277214f, 0.3490017751640694f, 0.33614278530633424f, 0.3232837954485991f, 0.31042480559086394f, 0.3157219310161509f, 0.3210190564414379f, 0.32631618186672484f, 0.36084833468781774f, 0.39538048750891064f, 0.42991264033000354f, 0.41943673241279394f, 0.4089608244955843f, 0.3984849165783747f, 0.40186905168121084f, 0.41554473564549993f, 0.42922041960978913f, 0.3966898589144239f, 0.36415929821905857f, 0.3316287375236933f, 0.3630286071851482f, 0.39442847684660304f, 0.40599308725861866f, 0.3573285059434177f, 0.3086639246282166f, 0.2599993433130157f, 0.25440774303859587f, 0.24881614276417607f, 0.24322454248975628f, 0.28564090890810856f, 0.3280572753264609f, 0.3704736417448133f, 0.3559800234353575f, 0.34148640512590167f, 0.32699278681644584f, 0.38281101763330305f, 0.4044372671085105f, 0.4260635165837181f, 0.36190507404108097f, 0.29774663149844394f, 0.23358818895580688f, 0.2257547332990705f, 0.2179212776423341f, 0.23750550743186225f, 0.267286823399684f, 0.2970681393675058f, 0.3268494553353276f, 0.3172869455193011f, 0.30772443570327446f, 0.29816192588724805f, 0.3251493432130761f, 0.3521367605389042f, 0.3791241778647323f, 0.38732946075692365f, 0.39553474364911506f, 0.4037400265413065f, 0.37171097097003153f, 0.34505744099744456f, 0.31840391102485754f, 0.3406002711449472f, 0.36279663126503675f, 0.38499299138512627f, 0.4047007874629352f, 0.4244085835407441f, 0.43035340370541164f, 0.40777102393308323f, 0.3851886441607549f, 0.36260626438842647f, 0.3857689708179953f, 0.40893167724756396f, 0.4320943836771327f, 0.4201296604566344f, 0.408164937236136f, 0.3962002140156376f, 0.4099624939900595f, 0.42372477396448127f, 0.43748705393890325f, 0.45543904133865043f, 0.4589194596593488f, 0.4623998779800473f, 0.45593562302391805f, 0.4494713680677888f, 0.44300711311165947f, 0.4075539883315737f, 0.3721008635514881f, 0.32434747806122766f, 0.3168200718352043f, 0.309292665609181f, 0.30176525938315757f, 0.28351808172789095f, 0.26527090407262427f, 0.2470237264173576f, 0.2355741089586689f, 0.22412449149998012f, 0.21267487404129146f, 0.2059370927715092f, 0.19919931150172698f, 0.19246153023194482f, 0.16765833699385083f, 0.168750078721755f, 0.16984182044965918f, 0.19358397109741565f, 0.2173261217451721f, 0.24106827239292858f, 0.2705980257618668f, 0.300127779130805f, 0.3021563975066882f, 
  0.2665433358706176f, 0.23093027423454696f, 0.1953172125984763f, 0.17757292831733426f, 0.15982864403619226f, 0.14208435975505018f, 0.17614762696563982f, 0.21021089417622937f, 0.244274161386819f, 0.28567634840174494f, 0.32707853541667087f, 0.36848072243159674f, 0.4012999749364907f, 0.40303394772127993f, 0.4047679205060692f, 0.34376510920936965f, 0.2827622979126701f, 0.22175948661597053f, 0.234323896901218f, 0.2468883071864654f, 0.2772213161659025f, 0.25524401114561385f, 0.23326670612532524f, 0.21128940110503652f, 0.21842022627798086f, 0.22555105145092522f, 0.23268187662386952f, 0.2609167005234312f, 0.2891515244229929f, 0.3173863483225546f, 0.32648231642554487f, 0.3355782845285352f, 0.34467425263152546f, 0.35536487033813247f, 0.36455132849357397f, 0.3737377866490153f, 0.3828751380272434f, 0.3920124894054714f, 0.4011498407836994f, 0.4078891240858746f, 0.4146284073880497f, 0.40573512091377983f, 0.4143602746160636f, 0.4229854283183474f, 0.43161058202063124f, 0.43619221399134184f, 0.4407738459620526f, 0.4453554779327632f, 0.430623819027736f, 0.41589216012270885f, 0.40116050121768165f, 0.4399628449041374f, 0.4787651885905932f, 0.5175675322770491f, 0.4960712921427036f, 0.4759114977908593f, 0.455751703439015f, 0.4759206495824137f, 0.49608959572581235f, 0.5162585418692112f, 0.48534897560333035f, 0.4544394093374496f, 0.42003801227436544f, 0.40799290348228806f, 0.3959477946902107f, 0.3839026858981334f, 0.38494804208507705f, 0.3859933982720207f, 0.3870387544589644f, 0.4377269234880036f, 0.48841509251704296f, 0.5391032615460821f, 0.5269125898086614f, 0.5147219180712405f, 0.5025312463338197f, 0.5652043162298668f, 0.5959090479469996f, 0.6266137796641323f, 0.6193198395069153f, 0.6120258993496982f, 0.604731959192481f, 0.5435331068291885f, 0.48233425446589606f, 0.42872858775961453f, 0.44332651886557417f, 0.45792444997153375f, 0.4725223810774934f, 0.45846731781757133f, 0.44441225455764927f, 0.4303571912977273f, 0.43527061814856854f, 0.44018404499940983f, 0.44509747185025106f, 0.48507245077417066f, 0.52504742969809f, 0.5650224086220098f, 0.5530175608005183f, 0.5545376343594685f, 0.5560577079184185f, 0.5574865768192527f, 0.5589154457200871f, 0.5603443146209215f, 0.6278985015097014f, 0.6954526883984813f, 0.72231362317461f, 0.7004214047440556f, 0.678529186313501f, 0.6566369678829466f, 0.5907788591484548f, 0.5249207504139634f, 0.45906264167947175f, 0.5013017955494269f, 0.543540949419382f, 0.585780103289337f, 0.5882786677853743f, 0.5907772322814117f, 0.5932757967774489f, 0.6182053342235064f, 0.6296410765264706f, 0.6410768188294345f, 0.6073280760037244f, 0.5735793331780142f, 0.539830590352304f, 0.5449709824929857f, 0.5501113746336673f, 0.53717896270701f, 0.5211172093885863f, 0.5050554560701626f, 0.4889937027517389f, 0.42473573823421135f, 0.36047777371668377f, 0.2962198091991562f, 0.3145232236528571f, 0.33282663810655816f, 0.35113005256025925f, 0.3920760228453283f, 0.43302199313039713f, 0.4739679634154662f, 0.47672515355188005f, 0.4523705602831524f, 0.42801596701442474f, 0.4442664294703344f, 0.46051689192624423f, 0.47676735438215395f, 0.48440444944211525f, 0.49204154450207654f, 0.5021358956706117f, 0.460978460928825f, 0.41982102618703837f, 0.37866359144525186f, 0.37653347668784365f, 0.3744033619304355f, 0.37227324717302734f, 0.41750447410996266f, 0.46273570104689804f, 
  0.5079669279838334f, 0.47108161933766374f, 0.43419631069149406f, 0.3973110020453242f, 0.43569045715703186f, 0.4772256451688757f, 0.5187608331807195f, 0.5291025989447656f, 0.5394443647088119f, 0.549786130472858f, 0.5551913051349027f, 0.5605964797969475f, 0.5676028361466519f, 0.5450937717269085f, 0.5225847073071651f, 0.5000756428874218f, 0.5247361131237223f, 0.5493965833600226f, 0.5740570535963232f, 0.5619823254479086f, 0.5499075972994942f, 0.5378328691510796f, 0.5815082908562846f, 0.6251837125614895f, 0.6688591342666944f, 0.6760379640747702f, 0.6785428003155688f, 0.6810476365563672f, 0.6899211875534603f, 0.6987947385505533f, 0.7076682895476464f, 0.6951048108961957f, 0.682541332244745f, 0.6497830112709174f, 0.6352506551108316f, 0.6207182989507455f, 0.6061859427906595f, 0.5938743745130002f, 0.5815628062353406f, 0.5692512379576812f, 0.5899585381615516f, 0.610665838365422f, 0.6313731385692924f, 0.6371343412500116f, 0.6428955439307306f, 0.6486567466114497f, 0.6201015475388227f, 0.5855545206342213f, 0.5510074937296199f, 0.5589172321430509f, 0.566826970556482f, 0.5747367089699129f, 0.5597693795046847f, 0.5448020500394565f, 0.5193126716552962f, 0.5050711251064502f, 0.4908295785576043f, 0.4765880320087583f, 0.4439756361932001f, 0.4113632403776417f, 0.3787508445620833f, 0.4138202830122521f, 0.44888972146242073f, 0.4839591599125893f, 0.4820729641083865f, 0.48018676830418366f, 0.47830057249998076f, 0.46168081923639553f, 0.451665309484133f, 0.4416497997318706f, 0.48793814269347624f, 0.5342264856550819f, 0.5805148286166877f, 0.5534470556218049f, 0.5263792826269221f, 0.4978580270488219f, 0.5277379461975594f, 0.557617865346297f, 0.5874977844950344f, 0.6097743385030021f, 0.6320508925109697f, 0.6543274465189374f, 0.6221965715941602f, 0.5900656966693831f, 0.557934821744606f, 0.5812349320502895f, 0.6045350423559729f, 0.6278351526616563f, 0.6376143944091838f, 0.6341346404140962f, 0.6306548864190087f, 0.6249236382869898f, 0.619192390154971f, 0.6134611420229522f, 0.5871084566200633f, 0.5607557712171745f, 0.5470222217869111f, 0.5956282587746282f, 0.6442342957623455f, 0.6928403327500625f, 0.6829319824281705f, 0.6730236321062784f, 0.6631152817843863f, 0.6171357399237611f, 0.5711561980631361f, 0.525176656202511f, 0.5441990222304279f, 0.5632213882583448f, 0.5822437542862617f, 0.5939991378200159f, 0.6221950930238068f, 0.6503910482275977f, 0.626978893736921f, 0.6035667392462444f, 0.5801545847555675f, 0.5933081636604993f, 0.6064617425654311f, 0.5997186121365785f, 0.5939972704697069f, 0.5882759288028351f, 0.5825545871359634f, 0.5511781937128186f, 0.5198018002896739f, 0.48842540686652924f, 0.5034140909258705f, 0.5184027749852117f, 0.533391459044553f, 0.576862783391906f, 0.620334107739259f, 0.663805432086612f, 0.6732743835328913f, 0.6757306453656665f, 0.6781869071984418f, 0.6604950057681324f, 0.6428031043378226f, 0.625111202907513f, 0.6608772491606477f, 0.6966432954137823f, 0.7230654590951711f, 0.6888021414282668f, 0.6545388237613622f, 0.6202755060944576f, 0.6459711427453546f, 0.6716667793962516f, 0.6973624160471489f, 0.6455307382665315f, 0.5936990604859143f, 0.5418673827052969f, 0.5202956676292796f, 0.49872395255326224f, 0.477152237477245f, 0.5023055748343576f, 0.533072980990281f, 0.5638403871462045f, 0.5415029594622258f, 0.5191655317782472f, 0.4968281040942685f, 0.46309277362170664f, 0.4293574431491448f, 0.4242051664880857f, 0.4439823969154091f, 0.4637596273427325f, 0.48353685777005595f, 0.5101628670207609f, 0.5367888762714659f, 0.5634148855221708f, 0.5572739432011121f, 0.5511330008800536f, 0.544992058558995f, 0.5448674112180726f, 0.54474276387715f, 0.5446181165362275f, 0.5611857736925039f, 0.5688768107103888f, 0.5765678477282736f, 0.5688916844773017f, 0.5612155212263297f, 0.5535393579753577f, 0.5448381195855091f, 0.5361368811956605f, 0.5368092274127295f, 0.5108464616452966f, 0.48488369587786373f, 0.4589209301104309f, 0.4586627091369837f, 0.45840448816353635f, 0.45814626719008916f, 0.47118517385955283f, 0.4842240805290164f, 0.49726298719848006f, 0.5150526885587231f, 0.532842389918966f, 0.550632091279209f, 0.535522871955787f, 0.5115970973601651f, 0.48767132276454334f, 0.5257853323213296f, 0.5638993418781157f, 0.602013351434902f, 0.5918859064236872f, 0.5817584614124726f, 0.5632824831514868f, 0.5284283705935637f, 0.4935742580356405f, 0.45872014547771744f, 0.4567554572814299f, 0.4547907690851425f, 0.4528260808888549f, 0.4782201671411948f, 0.5036142533935346f, 0.5290083396458746f, 0.5374830301037986f, 0.5459577205617226f, 0.5544324110196468f, 0.5724399632379441f, 0.5571592486927741f, 0.5418785341476043f, 0.5422681820819649f, 0.5426578300163256f, 0.5430474779506862f, 0.5379140317590556f, 0.5327805855674249f, 0.5261370296925841f, 0.4712829908845305f, 0.41642895207647695f, 0.3615749132684235f, 0.3332588898692955f, 0.3049428664701676f, 0.27662684307103974f, 0.30452371730648603f, 0.33242059154193215f, 0.3603174657773784f, 0.3777494939568637f, 0.3951815221363489f, 0.4126135503158341f, 0.4771770885577972f, 0.514895413206565f, 0.5526137378553326f, 0.520573501988039f, 0.4885332661207455f, 0.45649303025345184f, 0.44801308665446515f, 0.4395331430554784f, 0.45622643129726403f, 0.5093038986476026f, 0.5623813659979411f, 0.6154588333482796f, 0.6289141058977762f, 0.6423693784472728f, 0.6558246509967697f, 0.6346795921565169f, 0.6135345333162642f, 0.5923894744760112f, 0.6056715947661105f, 0.6189537150562099f, 0.6322358353463092f, 0.6453986803815873f, 0.6569910624000339f, 0.6685834444184807f, 0.6421614577968118f, 0.6157394711751426f, 0.5893174845534737f, 0.5887548355975557f, 0.5881921866416379f, 0.5805564511336345f, 0.5910929294940497f, 0.6016294078544647f, 0.6121658862148799f, 0.5932256952447652f, 0.5742855042746504f, 0.5553453133045357f, 0.598325626057367f, 0.6413059388101984f, 0.6842862515630297f, 0.6730920478246359f, 0.6618978440862423f, 0.6507036403478483f, 0.6672774531445763f, 0.6830336024133828f, 0.6987897516821895f, 0.7324778568379818f, 0.7661659619937743f, 0.7998540671495664f, 0.810536626210356f, 0.8212191852711453f, 0.8008023956261381f, 0.7891289481134917f, 0.7774555006008453
};

// motor controlls
static const byte MAXIMAL_SPEED_DIFFERENCE = 5;
static const byte MAXIMUM_SPEED = 130;

// sync controlls
static const unsigned int SYNC_MILLIS = 5009;

#endif
