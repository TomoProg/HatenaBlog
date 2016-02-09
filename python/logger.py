#-*- coding:utf-8 -*-

import datetime
import inspect

class Logger():
	"""
		自作ロガー
	"""
	def __init__(self, filepath):
		"""
			Content:
				コンストラクタ
			Param:
				1. filepath:	ファイルパス
		"""
		self.__filepath = filepath

	def write(self, msg):
		"""
			Content:
				書き込みメソッド
			Param:
				1. msg:	出力メッセージ
		"""
		# スタックフレーム解析
		stack_frame = inspect.stack()[1]
		frame = stack_frame[0]
		info = inspect.getframeinfo(frame)

		# ログファイル内容作成
		linetxt = ""
		linetxt += datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S ")
		linetxt += (info.filename + " ")
		linetxt += (str(info.lineno) + " ")
		linetxt += msg
		linetxt += "\n"

		# ログファイルに書き込む
		with open(self.__filepath, "a") as f:
			f.write(linetxt)

if __name__ == "__main__":
	logger = Logger("abc.txt")
	logger.write("sample msg")
