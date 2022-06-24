# これはサンプルの Python スクリプトです。

# Shift+F10 を押して実行するか、ご自身のコードに置き換えてください。
# Shift を2回押す を押すと、クラス/ファイル/ツールウィンドウ/アクション/設定を検索します。
import sys

def count_and_display_words(s):
    # スクリプトをデバッグするには以下のコード行でブレークポイントを使用してください。
    words = split_words(s)
    freqs = {}
    for w in words:
        if w in freqs:
            freqs[w] += 1
        else:
             freqs[w] = 1

    sorted_freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)

    i = 0
    for (k, v) in sorted_freqs:
        if i == 20:
            break
        print(" {}: {}".format(k, v))
        i += 1

def split_words(s):
    s = s.lower()
    s = s.replace(',', '')
    s = s.replace('.', '')
    s = s.replace('-', '')
    s = s.replace('_', '')
    s = s.replace(';', '')
    s = s.replace(':', '')
    s = s.replace('"', '')
    s = s.replace("'", '')
    s = s.replace('?', '')
    s = s.replace('!', '')
    s = s.replace('(', '')
    s = s.replace(')', '')
    s = s.replace('/', '')
    words = s.split()

    return words

# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    argc = len(sys.argv)
    if argc == 1:
        f = sys.stdin
    elif argc == 2:
        try:
            f = open(sys.argv[1], "r")
        except FileNotFoundError:
            sys.exit("wc: No such file or directory: " + sys.argv[1])
    else:
        sys.exit("usage: wc [file]")

    s = f.read()
    count_and_display_words(s)

# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください
