#-*- coding:utf-8 -*-

import os
import sys
import time
import bs4
import urllib.request

def crawring(url, extensions):
	"""
		Content:
			クローリング
		Param:
			url:		クローリングするURL
			extensions:	取得するリソースの拡張子(list)
	"""
	# 指定したURLのHTMLを取得
	html = get_html_string(url)
	if len(html) < 1:
		print("HTMLが取得できませんでした。")
		print("URLを確認してください。")
		sys.exit(1)

	# リソース取得
	get_resource(html, extensions)

def get_resource(html, extensions):
	"""
		Content:
			リソース取得
		Param
			html:		HTML
			extensions	拡張子のリスト
	"""

	resource_list = []

	soup = bs4.BeautifulSoup(html)
	for a_tag in soup.find_all("a"):
		href_str = a_tag.get("href")
		try:
			(path, ext) = os.path.splitext(href_str)
			if ext in extensions:
				resource_list.append(href_str)
		except:
			pass

	resource_list = sorted(set(resource_list), key=resource_list.index)
	for resource in resource_list:
		try:
			print("download ---> [%s]" % os.path.basename(resource))
			request = urllib.request.urlopen(resource)
			f = open(os.path.basename(resource), "wb")
			f.write(request.read())
		except Exception as e:
			print(e)
			print("download failed ... [%s]" % os.path.basename(resource))
		finally:
			time.sleep(3)

def get_html_string(url):
	"""
		Content:
			HTML取得
		Param:
			url	HTMLを取得するURL
	"""
	decoded_html = ""

	# HTMLを取得
	try:
		request = urllib.request.urlopen(url)
		html = request.read()
	except:
		return decoded_html

	# エンコードを取得
	enc = check_encoding(html)
	if enc == None:
		return decoded_html

	# HTMLをデコード
	decoded_html = html.decode(enc)

	return decoded_html

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


def check_args():
	"""
		Content:
			起動引数確認
	"""
	if len(sys.argv) == 3:
		return True
	else:
		return False

def print_usage():
	print("Usage: %s URL Extensions" % __file__)
	print("URLにはクロールしたいウェブサイトのアドレスを指定してください。")
	print("Extensionsにはクロールしたときに取得するファイルの拡張子を指定してください。")
	print("Extensionsはカンマ区切りで複数指定できます。")

def main():
	"""
		Content:
			main
	"""
	# 引数確認
	if check_args() is False:
		print_usage()
		sys.exit(1)
	
	url = sys.argv[1]
	extensions = sys.argv[2].split(",")

	# クロール開始
	crawring(url, extensions)

if __name__ == "__main__":
	main()
