import random
import time
import sys

m = [
	"a", 	"i", 	"u", 	"e", 	"o", 
	"ka", 	"ki",	"ku",	"ke",	"ko",
	"sa", 	"shi",	"su", 	"se",	"so",
	"ta",	"chi",	"tsu",	"te",	"to",
	"na",	"ni",	"nu",	"ne",	"no",
	"ha",	"hi",	"fu",	"he",	"ho",
	"ma",	"mi",	"mu",	"me",	"mo",
	"ya",			"yu",			"yo",
	"ra",	"ri",	"ru",	"re",	"ro",
	"wa",							"o",
	"n", 
	"ga",	"gi",	"gu",	"ge",	"go",
	"za",	"ji",	"zu",	"ze",	"zo",
	"da",	"ji",	"zu",	"de",	"do",
	"ba",	"bi",	"bu",	"be",	"bo",
	"pa",	"pi",	"pu",	"pe",	"po",
	"kya",			"kyu",			"kyo",
	"gya",			"gyu",			"gyo",
	"sya",			"syu",			"syo",
	"ja",			"ju",			"jo",
	"cha",			"chu",			"cho",
	"nya",			"nyu",			"nyo",
	"hya",			"hyu",			"hyo",
	"bya",			"byu",			"byo",
	"pya",			"pyu",			"pyo",
	"mya",			"myu",			"myo",
	"rya",			"ryu",			"ryo",
]

ping = [
	"あ", 	"い", 	"う", 	"え", 	"お", 
	"か", 	"き",	"く",	"け",	"こ",
	"さ", 	"し",	"す", 	"せ",	"そ",
	"た",	"ち",	"つ",	"て",	"と",
	"な",	"に",	"ぬ",	"ね",	"の",
	"は",	"ひ",	"ふ",	"へ",	"ほ",
	"ま",	"み",	"む",	"め",	"も",
	"や",			"ゆ",			"よ",
	"ら",	"り",	"る",	"れ",	"ろ",
	"わ",							"を",
	"ん", 
	"が",	"ぎ",	"ぐ",	"げ",	"ご",
	"ざ",	"じ",	"ず",	"ぜ",	"ぞ",
	"だ",	"ぢ",	"づ",	"で",	"ど",
	"ば",	"び",	"ぶ",	"べ",	"ぼ",
	"ぱ",	"ぴ",	"ぷ",	"ぺ",	"ぽ",
	"きゃ",			"きゅ",			"きょ",
	"ぎゃ",			"ぎゅ",			"ぎょ",
	"しゃ",			"しゅ",			"しょ",
	"じゃ",			"じゅ",			"じょ",
	"ちゃ",			"ちゅ",			"ちょ",
	"にゃ",			"にゅ",			"にょ",
	"ひゃ",			"ひゅ",			"ひょ",
	"びゃ",			"びゅ",			"びょ",
	"ぴゃ",			"ぴゅ",			"ぴょ",
	"みゃ",			"みゅ",			"みょ",
	"りゃ",			"りゅ",			"りょ",
]

pian = [
	"ア", 	"イ", 	"ウ", 	"エ", 	"オ", 
	"カ", 	"キ",	"ク",	"ケ",	"コ",
	"サ", 	"シ",	"ス", 	"セ",	"ソ",
	"タ",	"チ",	"ツ",	"テ",	"ト",
	"ナ",	"ニ",	"ヌ",	"ネ",	"ノ",
	"ハ",	"ヒ",	"フ",	"ヘ",	"ホ",
	"マ",	"ミ",	"ム",	"メ",	"モ",
	"ヤ",			"ユ",			"ヨ",
	"ラ",	"リ",	"ル",	"レ",	"ロ",
	"ワ",							"ヲ",
	"ン", 
	"ガ",	"ギ",	"グ",	"ゲ",	"ゴ",
	"ザ",	"ジ",	"ズ",	"ズ",	"ゾ",
	"ダ",	"ヂ",	"ヅ",	"デ",	"ド",
	"バ",	"ビ",	"ブ",	"ベ",	"ボ",
	"パ",	"ピ",	"プ",	"ペ",	"ポ",
	"キャ",			"キュ",			"キョ",
	"ギャ",			"ギュ",			"ギョ",
	"シャ",			"シュ",			"ショ",
	"ジャ",			"ジュ",			"ジョ",
	"チャ",			"チュ",			"チョ",
	"ニャ",			"ニュ",			"ニョ",
	"ヒャ",			"ヒュ",			"ヒョ",
	"ビャ",			"ビュ",			"ビョ",
	"ピャ",			"ピュ",			"ピョ",
	"ミャ",			"ミュ",			"ミョ",
	"リャ",			"リュ",			"リョ",
]

question = []
result = {}

for i in range(len(m)):
	result[m[i]] = [ping[i], pian[i]]
	result[ping[i]] = [m[i], pian[i]]
	result[pian[i]] = [m[i], ping[i]]

	question.append(m[i])
	question.append(ping[i])
	question.append(pian[i])

print("五十音图大作战...\n")
print("游戏规则：")
print("随机给出一个平假名或片假名或罗马音，快速运行你的大脑，联想出它对应的平假名或片假名或罗马音，然后摁下Enter对答案吧。\n")
print("开始\n\n")

random.seed (time.time())

total = len(m) * 3
queue = []
flag = {}
for i in range(total): 
	ran = random.randint(0, total - 1)
	while str(ran) in flag:
		ran = (ran + 1) % total
	flag[str(ran)] = True
	queue.append(ran)

index = 0
while True:
	test = question[queue[index]]
	sys.stdout.write("%s:" % test)
	input()
	print("answer: %s %s\n" % (result[test][0], result[test][1]))
	index = (index + 1) % total
