#-*- coding:utf-8 -*-

def check_encoding(byte_string):
	"""
		Content:
			文字コード確認
		Param:
			byte_string: バイト文字列
	"""
	encoding_list = ["utf-8", "utf_8", "euc_jp", 
					"euc_jis_2004", "euc_jisx0213", "shift_jis",
					"shift_jis_2004","shift_jisx0213", "iso2022jp",
					 "iso2022_jp_1", "iso2022_jp_2", "iso2022_jp_3",
					"iso2022_jp_ext","latin_1", "ascii"]

	for enc in encoding_list:
		try:
			byte_string.decode(enc)
			break
		except:
			enc = None

	return enc

if __name__ == "__main__":
	enc_str = "あ".encode("shift_jis")
	print(enc_str)

	enc = check_encoding(enc_str)
	print(enc)
