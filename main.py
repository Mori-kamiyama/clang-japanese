import re

def main(input_file, output_file):
    # キーワードとC言語の対応表
    keywords = {

        #型
        r'\bゔぉいど\b': 'void',
        r'\bいんと\b': 'int',
        r'\bちゃー\b': 'char',
        r'\bふろーと\b': 'float',
        r'\bだぶる\b': 'double',

        r'\bしょーと\b': 'short',
        r'\bろんぐ\b': 'long',
        r'\bさいんど\b': 'signed',
        r'\bあんさいんど\b': 'unsigned',

        r'\bたいぷでふ\b': 'typedef',

        r'\bこんすと\b': 'const',
        r'\bすたてぃっく\b': 'static',
        r'\bえくすたーん\b': 'extern',

        r'\bれじすた\b': 'register',  # レジスタ変数の宣言
        r'\bぼる\b': 'volatile',  # 変数が外部で変更される可能性があることを示す

        #制御構文
        r'\bめいん\b': 'main',
        r'\bりたーん\b': 'return',

        r'\bいふ\b': 'if',
        r'\bえるす\b': 'else',
        r'\bえるすいふ\b': 'else if',

        r'\bふぉー\b': 'for',
        r'\bわいる\b': 'while',
        r'\bどぅー\b': 'do',
        r'\bぶれーく\b': 'break',
        r'\bこんてぃにゅー\b': 'continue',
        r'\bすいっち\b': 'switch',
        r'\bけーす\b': 'case',
        r'\bでふぉると\b': 'default',

        r'\bごーとぅー\b': 'goto',  # ラベルへジャンプする制御文

        #関数
        r'\bぷりんとえふ\b': 'printf',
        r'\bすきゃんえふ\b': 'scanf',
        r'\bげっつ\b': 'gets',
        r'\bぷっつ\b': 'puts',
        r'\bすてぃあかっと\b': 'strcat',
        r'\bすてぃあれん\b': 'strlen',

        r'\bぱーせんとでぃー\b': '%d',

        #構造体・列挙型・共用体
        r'\bすとらくと\b': 'struct',
        r'\bえぬむ\b': 'enum',
        r'\bゆにおん\b': 'union',

        #プリプロセッサ
        r'\bいんくるーど\b': '#include',
        r'\bでぃふぁいん\b': '#define',
        r'\bいふでふ\b': '#ifdef',
        r'\bいふんでふ\b': '#ifndef',
        r'\bえんでぃふ\b': '#endif',
        r'\bしんたっくす\b': 'syntax',
        r'\bすてゅでぃおどっとえいち\b': '<stdio.h>',

        #メモリ
        r'\bまろっく\b': 'malloc',
        r'\bふりー\b': 'free',
        r'\bりあろっく\b': 'realloc',
        r'\bきゃるっく\b': 'calloc',
        r'\bぽいんた\b': 'pointer',
        r'\bあどれす\b': 'address',

        #演算子
        r'は': r'=',
        r'（': r'(',
        r'）': r')',
        r'「': r'{',
        r'」': r'}',
        r'；': r';',
        r'”': r'"',

        r'\bぷらす\b': '+',
        r'\bぷらすぷらす\b': '++',
        r'\bまいなす\b': '-',
        r'\bまいなすまいなす\b': '--',
        r'\bすたー\b': '*',
        r'\bすらっしゅ\b': '/',
        r'\bぱーせんと\b': '%',
        r'\bいこーる\b': '==',
        r'\bよりおおきい\b': '>',
        r'\bみまん\b': '<',
        r'\bいか\b': '>=',
        r'\bいじょう\b': '<=',
        r'\bあんど\b': '&&',
        r'\bおあ\b': '||',
        r'\bびっとのっと\b': '~',
        r'\bびっとしふと\b': '>>',
    }

    # ファイルの読み込み
    with open(input_file, 'r', encoding='utf-8') as file:
        code = file.read()

    # キーワードを正規表現で置換
    for jp_keyword, c_keyword in keywords.items():
        code = re.sub(jp_keyword, c_keyword, code)

    # 全角スペースを半角スペースに変換
    code = code.replace('　', ' ')  # 全角スペースから半角スペースへ

    # 変換後のコードを出力
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(code)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("使い方: python transpiler.py 入力ファイル 出力ファイル")
    else:
        main(sys.argv[1], sys.argv[2])