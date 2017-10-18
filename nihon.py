# -*- coding: utf-8 -*-

import random
import time
import sys

from flask import Flask, render_template, session
import json

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
	"wa",							"wo",
	"n", 
	"ga",	"gi",	"gu",	"ge",	"go",
	"za",	"zi",	"zu",	"ze",	"zo",
	"da",	"di",	"du",	"de",	"do",
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
	u"あ", 	u"い", 	u"う", 	u"え", 	u"お", 
	u"か", 	u"き",	u"く",	u"け",	u"こ",
	u"さ", 	u"し",	u"す", 	u"せ",	u"そ",
	u"た",	u"ち",	u"つ",	u"て",	u"と",
	u"な",	u"に",	u"ぬ",	u"ね",	u"の",
	u"は",	u"ひ",	u"ふ",	u"へ",	u"ほ",
	u"ま",	u"み",	u"む",	u"め",	u"も",
	u"や",			u"ゆ",			u"よ",
	u"ら",	u"り",	u"る",	u"れ",	u"ろ",
	u"わ",							u"を",
	u"ん", 
	u"が",	u"ぎ",	u"ぐ",	u"げ",	u"ご",
	u"ざ",	u"じ",	u"ず",	u"ぜ",	u"ぞ",
	u"だ",	u"ぢ",	u"づ",	u"で",	u"ど",
	u"ば",	u"び",	u"ぶ",	u"べ",	u"ぼ",
	u"ぱ",	u"ぴ",	u"ぷ",	u"ぺ",	u"ぽ",
	u"きゃ",			u"きゅ",			u"きょ",
	u"ぎゃ",			u"ぎゅ",			u"ぎょ",
	u"しゃ",			u"しゅ",			u"しょ",
	u"じゃ",			u"じゅ",			u"じょ",
	u"ちゃ",			u"ちゅ",			u"ちょ",
	u"にゃ",			u"にゅ",			u"にょ",
	u"ひゃ",			u"ひゅ",			u"ひょ",
	u"びゃ",			u"びゅ",			u"びょ",
	u"ぴゃ",			u"ぴゅ",			u"ぴょ",
	u"みゃ",			u"みゅ",			u"みょ",
	u"りゃ",			u"りゅ",			u"りょ",
]

pian = [
	u"ア", 	u"イ", 	u"ウ", 	u"エ", 	u"オ", 
	u"カ", 	u"キ",	u"ク",	u"ケ",	u"コ",
	u"サ", 	u"シ",	u"ス", 	u"セ",	u"ソ",
	u"タ",	u"チ",	u"ツ",	u"テ",	u"ト",
	u"ナ",	u"ニ",	u"ヌ",	u"ネ",	u"ノ",
	u"ハ",	u"ヒ",	u"フ",	u"ヘ",	u"ホ",
	u"マ",	u"ミ",	u"ム",	u"メ",	u"モ",
	u"ヤ",			u"ユ",			u"ヨ",
	u"ラ",	u"リ",	u"ル",	u"レ",	u"ロ",
	u"ワ",							u"ヲ",
	u"ン", 
	u"ガ",	u"ギ",	u"グ",	u"ゲ",	u"ゴ",
	u"ザ",	u"ジ",	u"ズ",	u"ぜ",	u"ゾ",
	u"ダ",	u"ヂ",	u"ヅ",	u"デ",	u"ド",
	u"バ",	u"ビ",	u"ブ",	u"ベ",	u"ボ",
	u"パ",	u"ピ",	u"プ",	u"ペ",	u"ポ",
	u"キャ",			u"キュ",			u"キョ",
	u"ギャ",			u"ギュ",			u"ギョ",
	u"シャ",			u"シュ",			u"ショ",
	u"ジャ",			u"ジュ",			u"ジョ",
	u"チャ",			u"チュ",			u"チョ",
	u"ニャ",			u"ニュ",			u"ニョ",
	u"ヒャ",			u"ヒュ",			u"ヒョ",
	u"ビャ",			u"ビュ",			u"ビョ",
	u"ピャ",			u"ピュ",			u"ピョ",
	u"ミャ",			u"ミュ",			u"ミョ",
	u"リャ",			u"リュ",			u"リョ",
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
idx_queue = []
flag = {}
for i in range(total): 
	ran = random.randint(0, total - 1)
	while str(ran) in flag:
		ran = (ran + 1) % total
	flag[str(ran)] = True
	idx_queue.append(ran)

idx = 0

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
	global idx
	global total
	global idx_queue
	global question
	global result
	quest = question[idx_queue[idx]]
	idx = (idx + 1) % total
	return render_template('index.html', a = quest, b = result[quest][0], c = result[quest][1])

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=10001, debug=True)

